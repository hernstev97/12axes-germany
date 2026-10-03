"""WIP gate-before-I/O runner for private historical categorical candidates.

This is a protocol guard, not protection against a deliberately intervening
repository owner. It neither verifies remote Git/tag state nor grants scientific
or publication approval. Only the fixed v2 gate can authorize raw-file opening.
"""

import csv
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from enum import Enum
import hashlib
from io import StringIO
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile

from pipeline import policy_adapter_v2 as adapter_api
from pipeline import policy_analysis_v2 as analysis_api
from pipeline import policy_reference_v2 as reference_api


PACKAGE = "EMPIRICAL-V2-001/v1"
PLAN_TAG = "analyseplan-v2"
GATE_PATH = "reports/loop/gates/pre-empirical-v2.json"
MANIFEST_PATH = f"reports/loop/packages/{PACKAGE}/manifest.json"
FREEZE_PATH = f"reports/loop/packages/{PACKAGE}/freeze.json"
CONTRACT_PATH = "data/analysevertrag.v2.entwurf.json"
CATALOG_PATH = "data/politikprofil-v2.fragen.entwurf.json"
METADATA_RULE = "integer_round_optional_dot_zero_decimal_edition_v1"
RESPONSE_RULE = "canonical_nonnegative_integer_optional_zero_fraction_v1"
EMPTY_REASON = "export_blank_unclassified"
PRIVATE_STATUS = "PRIVATE_CANDIDATE_PENDING_RESULT_REVIEW"
REVIEW_ROLES = {"methods_reproducibility", "sources_constructs_fairness"}
CORE_ARTIFACTS = {
    CONTRACT_PATH, CATALOG_PATH, "pipeline/policy_access_v2.py",
    "pipeline/policy_adapter_v2.py", "pipeline/policy_analysis_v2.py",
    "pipeline/policy_reference_v2.py",
}
# All identities are predetermined public file identities, never CSV discoveries.
STUDIES = {
    "ESS5e03_6": ("3.6", "5", "data/raw/ess5-ed3.6/ESS5e03_6.csv", "0189b86b-8aa4-4be3-88ad-39c58b02f19f"),
    "ESS8e02_3": ("2.3", "8", "data/raw/ess8-ed2.3/ESS8e02_3.csv", "ffc43f48-e15a-4a1c-8813-47eda377c355"),
    "ESS9e03_3": ("3.3", "9", "data/raw/ess9-ed3.3/ESS9e03_3.csv", "b2b0bf39-176b-4eca-8d26-3c05ea83d2cb"),
    "ESS10SCe03_2": ("3.2", "10", "data/raw/ess10-sc-ed3.2/ESS10SCe03_2.csv", "178d1c16-db15-466e-b1a5-cea36109e089"),
    "ESS11e04_2": ("4.2", "11", "data/raw/ess11-ed4.2/ESS11e04_2.csv", "242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef"),
}
_SHA = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_ROUND = re.compile(r"(?:0|[1-9][0-9]*)(?:\.0)?\Z")
_DECIMAL = re.compile(r"(?:0|[1-9][0-9]*)(?:\.[0-9]+)?\Z")
_RESPONSE = re.compile(r"(0|[1-9][0-9]*)(?:\.0+)?\Z")


class AccessErrorCode(str, Enum):
    INVALID_PINS = "invalid_pins"
    INVALID_GATE = "invalid_gate"
    PIN_MISMATCH = "pin_mismatch"
    INVALID_PUBLIC_DOCUMENT = "invalid_public_document"
    INVALID_CONTRACT = "invalid_contract"
    INVALID_SOURCE_IDENTITY = "invalid_source_identity"
    INVALID_PATH = "invalid_path"
    FILE_ACCESS_FAILED = "file_access_failed"
    RAW_IDENTITY_MISMATCH = "raw_identity_mismatch"
    INVALID_CSV = "invalid_csv"
    INVALID_METADATA = "invalid_metadata"
    ADAPTER_REJECTED = "adapter_rejected"
    PREPARATION_REJECTED = "preparation_rejected"
    PRIVATE_OUTPUT_FAILED = "private_output_failed"


class PolicyAccessError(ValueError):
    """Static message only: no path, header, record ID or response text."""

    def __init__(self, code: AccessErrorCode):
        self.code = code
        super().__init__(f"policy_access_error: {code.value}")


@dataclass(frozen=True, slots=True)
class AccessPins:
    manifest_sha256: str
    contract_sha256: str
    freeze_sha256: str
    frozen_commit: str
    plan_tag: str = PLAN_TAG


@dataclass(frozen=True, slots=True)
class RunReceipt:
    """Only public identities, status, times, hashes and the fixed private path."""

    study_id: str
    status: str
    started_utc: str
    finished_utc: str
    gate_sha256: str
    manifest_sha256: str
    contract_sha256: str
    freeze_sha256: str
    input_sha256: str
    private_path: str
    exit_code: int = 0


def _fail(code):
    raise PolicyAccessError(code) from None


def _require(condition, code):
    if not condition:
        _fail(code)


def _sha(value):
    return type(value) is str and _SHA.fullmatch(value) is not None


def _digest(value):
    return hashlib.sha256(value).hexdigest()


def _utc():
    return datetime.now(timezone.utc).isoformat()


def _mapping(value, required, *, exact=False, code=AccessErrorCode.INVALID_PUBLIC_DOCUMENT):
    _require(type(value) is dict and all(type(k) is str for k in value), code)
    _require(set(required) <= set(value) and (not exact or set(value) == set(required)), code)
    return value


def _canonical_path(value):
    _require(type(value) is str and value and "\\" not in value and "\x00" not in value, AccessErrorCode.INVALID_PATH)
    p = PurePosixPath(value)
    _require(not p.is_absolute() and str(p) == value and all(x not in {".", ".."} for x in p.parts), AccessErrorCode.INVALID_PATH)
    return p


def _public_path(value):
    p = _canonical_path(value)
    # Public package inputs only. Raw/local/output/auth/state routes cannot be
    # smuggled into manifest artifacts or reviewer report identities.
    allowed = (value in {CONTRACT_PATH, CATALOG_PATH}
               or p.parts[0] in {"docs", "pipeline"}
               or value.startswith("reports/loop/authors/")
               or value.startswith("reports/loop/reviews/")
               or value.startswith(f"reports/loop/packages/{PACKAGE}/"))
    _require(allowed and p.suffix in {".json", ".md", ".py"}, AccessErrorCode.INVALID_PATH)
    return value


def _repo_path(root, relative):
    p = _canonical_path(relative)
    target = root.joinpath(*p.parts)
    # Prevent existing path components from redirecting I/O outside this tree.
    current = root
    try:
        for component in p.parts:
            current /= component
            if current.is_symlink():
                _fail(AccessErrorCode.INVALID_PATH)
    except OSError:
        _fail(AccessErrorCode.FILE_ACCESS_FAILED)
    return target


def _read_repo_bytes(root, relative):
    path = _repo_path(root, relative)
    descriptor = None
    try:
        descriptor = os.open(path, os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW)
        _require(stat.S_ISREG(os.fstat(descriptor).st_mode), AccessErrorCode.FILE_ACCESS_FAILED)
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = None
            return stream.read()
    except OSError:
        _fail(AccessErrorCode.FILE_ACCESS_FAILED)
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _json_bytes(blob):
    def pairs(entries):
        result = {}
        for key, value in entries:
            _require(key not in result, AccessErrorCode.INVALID_PUBLIC_DOCUMENT)
            result[key] = value
        return result
    def invalid_constant(_):
        _fail(AccessErrorCode.INVALID_PUBLIC_DOCUMENT)
    try:
        return json.loads(blob.decode("utf-8"), object_pairs_hook=pairs, parse_constant=invalid_constant)
    except (UnicodeError, ValueError, TypeError, RecursionError):
        _fail(AccessErrorCode.INVALID_PUBLIC_DOCUMENT)


def _checked_document(root, path, expected_sha):
    blob = _read_repo_bytes(root, path)
    _require(_digest(blob) == expected_sha, AccessErrorCode.PIN_MISMATCH)
    return _json_bytes(blob)


def _validate_contract(contract, catalog):
    error = AccessErrorCode.INVALID_CONTRACT
    _mapping(contract, {"schemaVersion", "status", "measurement", "catalog", "studies", "publicationRules", "boundaries"}, code=error)
    _require(type(contract["schemaVersion"]) is int and contract["schemaVersion"] == 2
             and contract["status"] == "DRAFT_PENDING_TRANSITION_REVIEW"
             and contract["measurement"] == "separate_categorical_responses", error)
    _require(type(contract["publicationRules"]) is dict and type(contract["boundaries"]) in {dict, list}, error)
    _mapping(catalog, {"schemaVersion", "studies", "items"}, code=error)
    _require(type(catalog["schemaVersion"]) is int and catalog["schemaVersion"] == 1
             and type(catalog["studies"]) is list and type(catalog["items"]) is list, error)
    source_studies, source_items = {}, {}
    for study in catalog["studies"]:
        _mapping(study, {"id", "edition", "fileMetadataId", "country"}, code=error)
        identity = study["id"]
        _require(type(identity) is str and identity in STUDIES and identity not in source_studies, AccessErrorCode.INVALID_SOURCE_IDENTITY)
        edition, _, _, file_id = STUDIES[identity]
        _require(study["edition"] == edition and study["fileMetadataId"] == file_id and study["country"] == "DE", AccessErrorCode.INVALID_SOURCE_IDENTITY)
        source_studies[identity] = study
    for item in catalog["items"]:
        _mapping(item, {"id", "studyId", "variable", "categories", "missingCodes", "notAskedCodes"}, code=error)
        identity = item["id"]
        _require(type(identity) is str and identity not in source_items
                 and type(item["studyId"]) is str and item["studyId"] in source_studies
                 and type(item["variable"]) is str
                 and identity == item["studyId"] + ":" + item["variable"], AccessErrorCode.INVALID_SOURCE_IDENTITY)
        source_items[identity] = item
    _require(type(contract["studies"]) is list and bool(contract["studies"]), error)
    studies = {}
    for study in contract["studies"]:
        _mapping(study, {"study_id", "edition", "round", "country", "input", "adapter", "metadata", "responseSerialization", "provenance"}, code=error)
        identity = study["study_id"]
        _require(type(identity) is str and identity in STUDIES and identity not in studies, AccessErrorCode.INVALID_SOURCE_IDENTITY)
        edition, round_number, raw_path, _ = STUDIES[identity]
        _require(study["edition"] == edition and str(study["round"]) == round_number
                 and type(study["round"]) in {str, int} and study["country"] == "DE"
                 and identity in source_studies and type(study["provenance"]) is dict, AccessErrorCode.INVALID_SOURCE_IDENTITY)
        inp = _mapping(study["input"], {"path", "sha256", "bytes", "editionEvidence"}, exact=True, code=error)
        evidence = "historical_v1_identity_plus_gated_metadata_check" if identity == "ESS11e04_2" else "user_file_label_plus_gated_metadata_check"
        _require(inp["path"] == raw_path and _sha(inp["sha256"])
                 and type(inp["bytes"]) is int and inp["bytes"] > 0
                 and inp["editionEvidence"] == evidence, AccessErrorCode.INVALID_SOURCE_IDENTITY)
        metadata = _mapping(study["metadata"], {"round_column", "edition_column", "expected_round", "expected_edition", "normalizationRule"}, exact=True, code=error)
        _require(metadata == {"round_column": "essround", "edition_column": "edition", "expected_round": round_number,
                             "expected_edition": edition, "normalizationRule": METADATA_RULE}, error)
        serialization = _mapping(study["responseSerialization"], {"rule", "emptyCellReason"}, exact=True, code=error)
        _require(serialization == {"rule": RESPONSE_RULE, "emptyCellReason": EMPTY_REASON}, error)
        try:
            parsed_contract = adapter_api._contract(study["adapter"])
        except (ValueError, TypeError, AttributeError, OverflowError):
            _fail(error)
        _require(parsed_contract._study_id == identity and parsed_contract._edition == edition, AccessErrorCode.INVALID_SOURCE_IDENTITY)
        for question in study["adapter"]["questions"]:
            source = source_items.get(question["question_id"])
            _require(source is not None and source["studyId"] == identity
                     and source["variable"] == question["variable"], AccessErrorCode.INVALID_SOURCE_IDENTITY)
            try:
                valid = [c["code"] for c in source["categories"]]
                missing = {c["code"]: c["reasonApi"] for c in source["missingCodes"]}
                not_asked = [c["code"] for c in source["notAskedCodes"]]
            except (KeyError, TypeError):
                _fail(error)
            _require("" not in missing, error)
            missing[""] = EMPTY_REASON
            _require(question["categoryCodes"] == valid and question["missingCodes"] == missing
                     and question["structurallyNotAskedCodes"] == not_asked, AccessErrorCode.INVALID_SOURCE_IDENTITY)
        declared_design = study["adapter"].get("design_columns")
        if declared_design is not None:
            _require(declared_design == {"psu": "psu", "stratum": "stratum"}
                     and {"psu", "stratum"} <= set(source_studies[identity].get("designFieldsDeclaredInMainFile", [])), AccessErrorCode.INVALID_SOURCE_IDENTITY)
        studies[identity] = study
    _require(set(studies) == set(STUDIES) and set(source_studies) == set(STUDIES)
             and len(source_items) == 43, AccessErrorCode.INVALID_SOURCE_IDENTITY)
    fixed_questions = [q["question_id"] for s in studies.values() for q in s["adapter"]["questions"]]
    _require(len(fixed_questions) == 43 and set(fixed_questions) == set(source_items), AccessErrorCode.INVALID_SOURCE_IDENTITY)
    return studies


def _validate_before_raw(root, pins):
    _require(type(pins) is AccessPins and all(_sha(v) for v in (pins.manifest_sha256, pins.contract_sha256, pins.freeze_sha256))
             and type(pins.frozen_commit) is str and _COMMIT.fullmatch(pins.frozen_commit) is not None
             and pins.plan_tag == PLAN_TAG, AccessErrorCode.INVALID_PINS)
    gate_blob = _read_repo_bytes(root, GATE_PATH)
    gate = _json_bytes(gate_blob)
    _mapping(gate, {"schemaVersion", "package", "decision", "reviewedManifestSha256", "frozenCommit", "planTag", "reviewers"}, exact=True, code=AccessErrorCode.INVALID_GATE)
    _require(type(gate["schemaVersion"]) is int and gate["schemaVersion"] == 1
             and gate["package"] == PACKAGE and gate["decision"] == "ALLOW_HISTORICAL_DESCRIPTIVE_V2"
             and gate["reviewedManifestSha256"] == pins.manifest_sha256
             and gate["frozenCommit"] == pins.frozen_commit and gate["planTag"] == PLAN_TAG, AccessErrorCode.INVALID_GATE)
    reviewers = gate["reviewers"]
    _require(type(reviewers) is list and len(reviewers) == 2, AccessErrorCode.INVALID_GATE)
    roles, reports = set(), set()
    for reviewer in reviewers:
        _mapping(reviewer, {"role", "reportPath", "sha256", "decision"}, exact=True, code=AccessErrorCode.INVALID_GATE)
        role, report = reviewer["role"], reviewer["reportPath"]
        _require(type(role) is str and role in REVIEW_ROLES and role not in roles
                 and reviewer["decision"] == "ACCEPTED_BOUNDED" and _sha(reviewer["sha256"]), AccessErrorCode.INVALID_GATE)
        _public_path(report)
        _require(PurePosixPath(report).parent == PurePosixPath("reports/loop/reviews") and report.endswith(".md")
                 and report not in reports, AccessErrorCode.INVALID_GATE)
        report_blob = _read_repo_bytes(root, report)
        _require(bool(report_blob), AccessErrorCode.INVALID_GATE)
        _require(_digest(report_blob) == reviewer["sha256"], AccessErrorCode.PIN_MISMATCH)
        roles.add(role); reports.add(report)
    _require(roles == REVIEW_ROLES, AccessErrorCode.INVALID_GATE)
    freeze = _checked_document(root, FREEZE_PATH, pins.freeze_sha256)
    _mapping(freeze, {"schemaVersion", "package", "frozenCommit", "planTag", "reviewedManifestSha256", "contractSha256"}, exact=True)
    _require(type(freeze["schemaVersion"]) is int and freeze["schemaVersion"] == 1
             and freeze["package"] == PACKAGE and freeze["frozenCommit"] == pins.frozen_commit
             and freeze["planTag"] == PLAN_TAG and freeze["reviewedManifestSha256"] == pins.manifest_sha256
             and freeze["contractSha256"] == pins.contract_sha256, AccessErrorCode.PIN_MISMATCH)
    manifest = _checked_document(root, MANIFEST_PATH, pins.manifest_sha256)
    _mapping(manifest, {"package", "artifacts"})
    _require(manifest["package"] == PACKAGE and type(manifest["artifacts"]) is list, AccessErrorCode.INVALID_PUBLIC_DOCUMENT)
    artifacts, blobs = {}, {}
    for artifact in manifest["artifacts"]:
        _mapping(artifact, {"path", "sha256"}, exact=True)
        path, sha = artifact["path"], artifact["sha256"]
        _public_path(path)
        _require(path not in artifacts and path not in {GATE_PATH, MANIFEST_PATH, FREEZE_PATH} and _sha(sha), AccessErrorCode.INVALID_PUBLIC_DOCUMENT)
        blob = _read_repo_bytes(root, path)
        _require(_digest(blob) == sha, AccessErrorCode.PIN_MISMATCH)
        artifacts[path] = sha; blobs[path] = blob
    _require(CORE_ARTIFACTS <= set(artifacts) and artifacts[CONTRACT_PATH] == pins.contract_sha256, AccessErrorCode.PIN_MISMATCH)
    # Bind the executing library source to the same reviewed artifact hashes.
    runtime = {"pipeline/policy_access_v2.py": Path(__file__),
               "pipeline/policy_adapter_v2.py": Path(adapter_api.__file__),
               "pipeline/policy_analysis_v2.py": Path(analysis_api.__file__),
               "pipeline/policy_reference_v2.py": Path(reference_api.__file__)}
    try:
        for path, executing_path in runtime.items():
            _require(_digest(executing_path.read_bytes()) == artifacts[path], AccessErrorCode.PIN_MISMATCH)
    except OSError:
        _fail(AccessErrorCode.FILE_ACCESS_FAILED)
    contract = _json_bytes(blobs[CONTRACT_PATH])
    catalog_link = _mapping(contract.get("catalog") if type(contract) is dict else None, {"path", "sha256"}, exact=True, code=AccessErrorCode.INVALID_CONTRACT)
    _require(catalog_link == {"path": CATALOG_PATH, "sha256": artifacts[CATALOG_PATH]}, AccessErrorCode.PIN_MISMATCH)
    studies = _validate_contract(contract, _json_bytes(blobs[CATALOG_PATH]))
    return studies, _digest(gate_blob)


def _metadata_and_response_text(text, study):
    """Lexically parse all CSV cells; interpret only selected DE fields.

    The reader/writer changes CSV quoting/layout, not other cell values. No
    claim of comprehensive blindness to the lexical CSV contents is made.
    """
    supplied = study["adapter"]
    expected = study["metadata"]
    try:
        reader = csv.reader(StringIO(text, newline=""), strict=True)
        header = next(reader)
        _require(bool(header) and all(header) and len(set(header)) == len(header), AccessErrorCode.INVALID_CSV)
        required = {"cntry", "essround", "edition", *(q["variable"] for q in supplied["questions"])}
        _require(required <= set(header), AccessErrorCode.INVALID_CSV)
        indices = {column: n for n, column in enumerate(header)}
        rows = []
        for cells in reader:
            _require(len(cells) == len(header), AccessErrorCode.INVALID_CSV)
            if cells[indices["cntry"]] == "DE":
                round_text, edition_text = cells[indices["essround"]], cells[indices["edition"]]
                _require(_ROUND.fullmatch(round_text) is not None and _DECIMAL.fullmatch(edition_text) is not None, AccessErrorCode.INVALID_METADATA)
                _require(Decimal(round_text) == Decimal(expected["expected_round"])
                         and Decimal(edition_text) == Decimal(expected["expected_edition"]), AccessErrorCode.INVALID_METADATA)
            rows.append(cells)
        # Validate every DE row's source metadata before interpreting any
        # selected response, including when a bad metadata row appears last.
        for cells in rows:
            if cells[indices["cntry"]] == "DE":
                for question in supplied["questions"]:
                    column = indices[question["variable"]]
                    cells[column] = _normalize_response(cells[column])
        output = StringIO(newline="")
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(header); writer.writerows(rows)
        return output.getvalue()
    except (csv.Error, StopIteration, UnicodeError, InvalidOperation, OverflowError):
        _fail(AccessErrorCode.INVALID_CSV)


def _normalize_response(value):
    match = _RESPONSE.fullmatch(value)
    return match.group(1) if match is not None else value


def _write_private(root, study_id, payload):
    relative = f"data/local/policy-v2/{study_id}/run.json"
    temporary = None
    try:
        data_dir = _repo_path(root, "data")
        _require(data_dir.is_dir(), AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        parent = data_dir
        for part in ("local", "policy-v2", study_id):
            parent /= part
            _require(not parent.is_symlink(), AccessErrorCode.PRIVATE_OUTPUT_FAILED)
            if not parent.exists():
                parent.mkdir(mode=0o700)
            mode = parent.stat().st_mode
            _require(stat.S_ISDIR(mode) and stat.S_IMODE(mode) == 0o700, AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        target = parent / "run.json"
        _require(not target.is_symlink(), AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        if target.exists():
            mode = target.stat().st_mode
            _require(stat.S_ISREG(mode) and stat.S_IMODE(mode) == 0o600, AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        serialized = json.dumps(payload, ensure_ascii=False, allow_nan=False, separators=(",", ":")) + "\n"
        descriptor, temporary = tempfile.mkstemp(prefix=".run-", suffix=".tmp", dir=parent)
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(serialized); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, target)
        temporary = None
        directory_fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        return relative
    except (OSError, ValueError, TypeError, OverflowError, RecursionError):
        _fail(AccessErrorCode.PRIVATE_OUTPUT_FAILED)
    finally:
        if temporary is not None:
            try:
                os.unlink(temporary)  # Only the temporary file created above.
            except OSError:
                pass


def run_study_reference(repo_root, study_id, pins: AccessPins) -> RunReceipt:
    """Prepare one private candidate after full fixed-gate/pin validation.

    Caller pins must come from the public frozen package, not be inferred from
    arbitrary local gate text. Remote/tag verification remains the coordinator's
    separate responsibility. No CLI, public export or reviewed status is added.
    """
    started = _utc()
    _require(type(study_id) is str and study_id in STUDIES, AccessErrorCode.INVALID_SOURCE_IDENTITY)
    try:
        root = Path(repo_root).resolve(strict=True)
        _require(root.is_dir(), AccessErrorCode.INVALID_PATH)
    except (OSError, TypeError, ValueError):
        _fail(AccessErrorCode.INVALID_PATH)
    # No raw file stat/open/read occurs anywhere before this returns.
    try:
        studies, gate_sha = _validate_before_raw(root, pins)
    except PolicyAccessError:
        raise
    except (KeyError, TypeError, ValueError, AttributeError, ArithmeticError, RecursionError):
        _fail(AccessErrorCode.INVALID_PUBLIC_DOCUMENT)
    _require(study_id in studies, AccessErrorCode.INVALID_SOURCE_IDENTITY)
    study = studies[study_id]
    inp = study["input"]
    blob = _read_repo_bytes(root, inp["path"])
    input_sha = _digest(blob)
    _require(input_sha == inp["sha256"] and len(blob) == inp["bytes"], AccessErrorCode.RAW_IDENTITY_MISMATCH)
    try:
        text = blob.decode("utf-8-sig")
    except UnicodeError:
        _fail(AccessErrorCode.INVALID_CSV)
    prepared_text = _metadata_and_response_text(text, study)
    try:
        parsed = adapter_api.parse_study_csv(prepared_text, study["adapter"])
    except (ValueError, TypeError, AttributeError, ArithmeticError):
        _fail(AccessErrorCode.ADAPTER_REJECTED)
    try:
        prepared = analysis_api.prepare_study_references(parsed)
        candidate = analysis_api.expose_prepared_candidate(prepared)
    except (ValueError, TypeError, AttributeError, ArithmeticError):
        _fail(AccessErrorCode.PREPARATION_REJECTED)
    # Only the analysis API's aggregate allowlist is serialized; never records,
    # answer dataclasses, source identifiers or parser diagnostics.
    private_path = _write_private(root, study_id, {
        "schema": "policy-private-run-v2-wip", "status": PRIVATE_STATUS,
        "study_id": study_id, "prepared_utc": _utc(),
        "pins": {"manifestSha256": pins.manifest_sha256, "contractSha256": pins.contract_sha256,
                 "freezeSha256": pins.freeze_sha256, "gateSha256": gate_sha,
                 "frozenCommit": pins.frozen_commit, "planTag": PLAN_TAG, "inputSha256": input_sha},
        "candidate": candidate,
    })
    return RunReceipt(study_id, PRIVATE_STATUS, started, _utc(), gate_sha, pins.manifest_sha256,
                      pins.contract_sha256, pins.freeze_sha256, input_sha, private_path)
