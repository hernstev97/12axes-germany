"""WIP fixed-gate I/O for private, separate historical second-vote groups.

No gate, tag, public export or empirical permission is created here. The caller
supplies externally reviewed pins; Root separately checks remote provenance.
This is a protocol guard, not hostile-Root or arbitrary-Python isolation.
Only pure v2 contract/metadata helpers are reused; no earlier runner is called.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import errno
import hashlib
import json
from math import isfinite
import os
from pathlib import PurePosixPath
import re
import secrets
import stat

from pipeline import policy_access_v2 as v2_io
from pipeline import policy_adapter_v2 as adapter_api
from pipeline import policy_analysis_v2 as analysis_api
from pipeline import policy_export_v2 as export_api
from pipeline import policy_groups_v21 as groups_api
from pipeline import policy_reference_v2 as reference_api
from pipeline import policy_report_v2 as report_api


PACKAGE = "GROUP-V21-001/v1"
PLAN_TAG = "analyseplan-v2.1"
DECISION = "ALLOW_HISTORICAL_DESCRIPTIVE_GROUPS_V21"
GATE_PATH = "reports/loop/gates/pre-group-v21.json"
MANIFEST_PATH = f"reports/loop/packages/{PACKAGE}/manifest.json"
FREEZE_PATH = f"reports/loop/packages/{PACKAGE}/freeze.json"
GROUP_CONTRACT_PATH = "data/gruppenvertrag.v2.1.entwurf.json"
STUDY_CONTRACT_PATH = "data/analysevertrag.v2.entwurf.json"
CATALOG_PATH = "data/politikprofil-v2.fragen.entwurf.json"
PRIVATE_STATUS = "PRIVATE_GROUP_CANDIDATE_PENDING_RESULT_REVIEW"
REVIEW_ROLES = {"methods_reproducibility", "sources_constructs_fairness"}
_SHA = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_RULE_KEYS = {
    "responseSerialization", "eligibilityAccounting", "questionDenominators",
    "weightPolicy", "displayPolicy", "transitionRequirements", "privacyAndOutputs",
    "sourceRights", "boundaries", "priorExposure",
}
_GROUP_KEYS = _RULE_KEYS | {
    "schemaVersion", "status", "planVersion", "createdUtc", "analysisPurpose",
    "measurement", "country", "references", "selectedQuestionCount", "studies", "sources",
}
# These source-only projections come from the fixed 9cd6b94e... draft. Opaque
# input hashes stay externally bound, so synthetic repositories need no real
# input bytes. Reference hash values are independently manifest-bound below.
_RULES_SHA256 = "0f3edd5759e113cd9a989aa4f40d3f8e0c71d0ea92ffb9b0352ee5249ceecf4d"
_SOURCE_IDENTITIES_SHA256 = "5bcab6ddec123da41540a5ada4a48df32b78837afa89b772a67a5ec52050e612"
_GROUP_BINDINGS_SHA256 = {
    "ESS5e03_6": "9ddc2346d771fd021aa79904157b451a254bff9f5f09252183ee90b6159f00a3",
    "ESS8e02_3": "5dab0b4dd6285eed3965369eb7d5d29e2b6ea885a3a74d32023c82c2b7e2fe35",
    "ESS9e03_3": "b9dfa081652a12b1917f581b2e04f4da84a065412b6be94ab4f7b2e51d041fa1",
    "ESS10SCe03_2": "25b76ba2b20aace1ffbc6f6bca189c00882b05d4b3e9253a03dca1e4581705a1",
    "ESS11e04_2": "bfbfd4b4d6f17e2082bbdf79ea62b3fce42074c8292fe03566c362ed7d3ea618",
}
_REFERENCE_PATHS = {
    "catalogue": CATALOG_PATH, "analysisContract": STUDY_CONTRACT_PATH,
    "publicGroupSource005": "outputs/loop/breadth-group-sources-005/crosswalk.json",
    "publicGroupBinding006": "outputs/loop/breadth-group-binding-006/binding-inventory.json",
    "exposureErratum005": "reports/loop/authors/BREADTH-GROUP-SOURCES-005-erratum.md",
}
_RUNTIME_MODULES = {
    "pipeline/policy_access_v2.py": v2_io,
    "pipeline/policy_adapter_v2.py": adapter_api,
    "pipeline/policy_analysis_v2.py": analysis_api,
    "pipeline/policy_export_v2.py": export_api,
    "pipeline/policy_groups_v21.py": groups_api,
    "pipeline/policy_reference_v2.py": reference_api,
    "pipeline/policy_report_v2.py": report_api,
}
CORE_ARTIFACTS = set(_RUNTIME_MODULES) | {
    "pipeline/policy_group_access_v21.py", GROUP_CONTRACT_PATH,
    STUDY_CONTRACT_PATH, CATALOG_PATH,
}


class AccessErrorCode(str, Enum):
    INVALID_PINS = "invalid_pins"
    INVALID_GATE = "invalid_gate"
    STUDY_NOT_ALLOWED = "study_not_allowed"
    PIN_MISMATCH = "pin_mismatch"
    INVALID_PUBLIC_DOCUMENT = "invalid_public_document"
    INVALID_CONTRACT = "invalid_contract"
    INVALID_SOURCE_IDENTITY = "invalid_source_identity"
    INVALID_PATH = "invalid_path"
    FILE_ACCESS_FAILED = "file_access_failed"
    RAW_IDENTITY_MISMATCH = "raw_identity_mismatch"
    INVALID_CSV = "invalid_csv"
    INVALID_METADATA = "invalid_metadata"
    GROUP_PREPARATION_REJECTED = "group_preparation_rejected"
    INVALID_PRIVATE_AGGREGATE = "invalid_private_aggregate"
    PRIVATE_OUTPUT_FAILED = "private_output_failed"


class PolicyGroupAccessError(ValueError):
    """Static error only, without cell values, identifiers or header text."""

    def __init__(self, code):
        self.code = code
        super().__init__(f"policy_group_access_error: {code.value}")


@dataclass(frozen=True, slots=True)
class AccessPins:
    manifest_sha256: str
    group_contract_sha256: str
    study_contract_sha256: str
    freeze_sha256: str
    frozen_commit: str
    plan_tag: str = PLAN_TAG


@dataclass(frozen=True, slots=True)
class RunReceipt:
    study_id: str
    status: str
    started_utc: str
    finished_utc: str
    gate_sha256: str
    manifest_sha256: str
    group_contract_sha256: str
    study_contract_sha256: str
    freeze_sha256: str
    input_sha256: str
    output_sha256: str
    private_path: str
    exit_code: int = 0


def _fail(code):
    raise PolicyGroupAccessError(code) from None


def _require(condition, code=AccessErrorCode.INVALID_CONTRACT):
    if not condition:
        _fail(code)


def _digest(blob):
    return hashlib.sha256(blob).hexdigest()


def _sha(value):
    return type(value) is str and _SHA.fullmatch(value) is not None


def _utc():
    return datetime.now(timezone.utc).isoformat()


def _object(value, keys, *, exact=True, code=AccessErrorCode.INVALID_PUBLIC_DOCUMENT):
    _require(type(value) is dict and all(type(k) is str for k in value), code)
    _require(set(value) == set(keys) if exact else set(keys) <= set(value), code)
    return value


def _canonical(value, *, absolute=False):
    _require(type(value) is str and value and "\\" not in value and "\x00" not in value,
             AccessErrorCode.INVALID_PATH)
    path = PurePosixPath(value)
    _require(path.is_absolute() == absolute and str(path) == value
             and all(x not in {".", ".."} for x in path.parts), AccessErrorCode.INVALID_PATH)
    return path


def _directory_at(parent_fd, name):
    return os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                   dir_fd=parent_fd)


def _absolute_directory(path):
    """Open every absolute component without following a symlink."""
    parts = _canonical(path, absolute=True).parts
    descriptor = os.open("/", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
    try:
        for component in parts[1:]:
            child = _directory_at(descriptor, component)
            os.close(descriptor); descriptor = child
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _read_fd_file(root_fd, relative):
    """Descriptor-relative traversal prevents symlinks in all components."""
    parts = _canonical(relative).parts
    parent = os.dup(root_fd)
    descriptor = None
    try:
        for component in parts[:-1]:
            child = _directory_at(parent, component)
            os.close(parent); parent = child
        descriptor = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC | os.O_NONBLOCK,
                             dir_fd=parent)
        _require(stat.S_ISREG(os.fstat(descriptor).st_mode), AccessErrorCode.FILE_ACCESS_FAILED)
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = None
            return stream.read()
    except OSError as error:
        _fail(AccessErrorCode.INVALID_PATH if error.errno in {errno.ELOOP, errno.ENOTDIR}
              else AccessErrorCode.FILE_ACCESS_FAILED)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent)


def _absolute_bytes(path):
    absolute = _canonical(os.path.abspath(path), absolute=True)
    parent = _absolute_directory(str(absolute.parent))
    try:
        return _read_fd_file(parent, absolute.name)
    finally:
        os.close(parent)


def _runtime_hashes():
    paths = {key: module.__file__ for key, module in _RUNTIME_MODULES.items()}
    paths["pipeline/policy_group_access_v21.py"] = __file__
    return {key: _digest(_absolute_bytes(value)) for key, value in paths.items()}


# Imports only pure/public source libraries. Record their bytes when this
# wrapper loads and recheck before raw access, detecting mid-process file drift.
# This cannot authenticate arbitrary monkeypatches or a hostile Python owner.
_LOADED_RUNTIME_HASHES = _runtime_hashes()


def _json(blob):
    def pairs(entries):
        result = {}
        for key, value in entries:
            _require(key not in result)
            result[key] = value
        return result
    def constant(_):
        _fail(AccessErrorCode.INVALID_PUBLIC_DOCUMENT)
    try:
        return json.loads(blob.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant)
    except PolicyGroupAccessError:
        raise
    except (UnicodeError, ValueError, TypeError, RecursionError):
        _fail(AccessErrorCode.INVALID_PUBLIC_DOCUMENT)


def _checked_json(root_fd, path, expected_sha):
    blob = _read_fd_file(root_fd, path)
    _require(_digest(blob) == expected_sha, AccessErrorCode.PIN_MISMATCH)
    return _json(blob)


def _json_digest(value):
    return _digest(json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                              separators=(",", ":")).encode("utf-8"))


def _reference_hash_projection(value):
    if type(value) is dict:
        return {key: "MANIFEST_BOUND_SHA256" if key == "sha256" else _reference_hash_projection(child)
                for key, child in value.items()}
    if type(value) is list:
        return [_reference_hash_projection(child) for child in value]
    return value


def _public_artifact_path(value, bound_source_paths):
    path = _canonical(value)
    permitted = (value in CORE_ARTIFACTS or value in bound_source_paths
                 or path.parts[0] in {"docs", "pipeline"}
                 or str(path.parent) in {"reports/loop/authors", "reports/loop/reviews"}
                 or value.startswith(f"reports/loop/packages/{PACKAGE}/"))
    _require(permitted and path.suffix in {".py", ".json", ".md", ".pdf", ".html"}
             and not {"state", "handoff", "private", "known-results"}.intersection(path.parts)
             and value not in {GATE_PATH, MANIFEST_PATH, FREEZE_PATH}, AccessErrorCode.INVALID_PATH)
    return value


def _group_contract(group, studies, artifacts):
    _object(group, _GROUP_KEYS, code=AccessErrorCode.INVALID_CONTRACT)
    _require(type(group["schemaVersion"]) is int and group["schemaVersion"] == 1
             and group["status"] == "DRAFT_PENDING_GROUP_TRANSITION_REVIEW"
             and group["planVersion"] == "2.1" and group["country"] == "DE"
             and group["measurement"] == "separate_categorical_responses"
             and group["analysisPurpose"] == "historical_separate_categorical_distributions_by_self_reported_Bundestag_second_vote"
             and type(group["selectedQuestionCount"]) is int and group["selectedQuestionCount"] == 43)
    _require(_json_digest(_reference_hash_projection({key: group[key] for key in _RULE_KEYS}))
             == _RULES_SHA256, AccessErrorCode.INVALID_CONTRACT)
    references = _object(group["references"], _REFERENCE_PATHS, code=AccessErrorCode.INVALID_CONTRACT)
    required_sources = {}
    def bind(reference, expected_path=None):
        _object(reference, {"path", "sha256"}, code=AccessErrorCode.INVALID_CONTRACT)
        path, sha = reference["path"], reference["sha256"]
        _canonical(path)
        _require(_sha(sha) and (expected_path is None or path == expected_path))
        _require(path in artifacts and artifacts[path] == sha, AccessErrorCode.PIN_MISMATCH)
        _require(path not in required_sources or required_sources[path] == sha)
        required_sources[path] = sha
    for key, expected_path in _REFERENCE_PATHS.items():
        bind(references[key], expected_path)
    exposure = group["priorExposure"]
    bind(exposure["externalShareExposureSource"], "outputs/loop/breadth-group-binding-006/exposure-boundaries.json")
    bind(exposure["knownDataContext"]["reference"], "outputs/loop/group-contract-v21/known-data-context.json")
    sources = group["sources"]
    _require(type(sources) is list and len(sources) == 32)
    projected = [{key: value for key, value in source.items() if key != "originalBytesSha256"}
                 for source in sources]
    _require(_json_digest(projected) == _SOURCE_IDENTITIES_SHA256, AccessErrorCode.INVALID_SOURCE_IDENTITY)
    _require(len({source["id"] for source in sources}) == len(sources))
    for source in sources:
        bind({"path": source["cachedPublicDocumentationPath"], "sha256": source["originalBytesSha256"]})
    _require(type(group["studies"]) is list and len(group["studies"]) == 5)
    grouped = {}
    for item in group["studies"]:
        identity = item.get("studyId") if type(item) is dict else None
        _require(type(identity) is str and identity in studies and identity not in grouped,
                 AccessErrorCode.INVALID_SOURCE_IDENTITY)
        _require(_json_digest({key: value for key, value in item.items() if key != "opaqueInputReference"})
                 == _GROUP_BINDINGS_SHA256[identity], AccessErrorCode.INVALID_SOURCE_IDENTITY)
        inp = _object(item["opaqueInputReference"], {"path", "sha256", "bytes", "editionEvidence",
                                                        "obtainedFrom", "rawBytesOpenedByThisAuthor"})
        _require({key: inp[key] for key in ("path", "sha256", "bytes", "editionEvidence")}
                 == studies[identity]["input"], AccessErrorCode.INVALID_SOURCE_IDENTITY)
        _require(inp["obtainedFrom"] == references["analysisContract"] and inp["rawBytesOpenedByThisAuthor"] is False)
        # Contract validation only: this helper never sees CSV text.
        groups_api._validated_contracts(studies[identity], item)
        grouped[identity] = item
    _require(set(grouped) == set(v2_io.STUDIES), AccessErrorCode.INVALID_SOURCE_IDENTITY)
    return grouped, required_sources


def _before_raw(root_fd, requested, pins):
    _require(type(pins) is AccessPins
             and all(_sha(value) for value in (pins.manifest_sha256, pins.group_contract_sha256,
                                               pins.study_contract_sha256, pins.freeze_sha256))
             and type(pins.frozen_commit) is str and _COMMIT.fullmatch(pins.frozen_commit) is not None
             and pins.plan_tag == PLAN_TAG, AccessErrorCode.INVALID_PINS)
    gate_blob = _read_fd_file(root_fd, GATE_PATH)
    gate = _json(gate_blob)
    _object(gate, {"schemaVersion", "package", "decision", "reviewedManifestSha256",
                   "frozenCommit", "planTag", "allowedStudyIds", "reviewers"}, code=AccessErrorCode.INVALID_GATE)
    _require(type(gate["schemaVersion"]) is int and gate["schemaVersion"] == 1
             and gate["package"] == PACKAGE and gate["decision"] == DECISION
             and gate["reviewedManifestSha256"] == pins.manifest_sha256
             and gate["frozenCommit"] == pins.frozen_commit and gate["planTag"] == PLAN_TAG,
             AccessErrorCode.INVALID_GATE)
    allowed = gate["allowedStudyIds"]
    _require(type(allowed) is list and bool(allowed)
             and all(type(value) is str and value in v2_io.STUDIES for value in allowed)
             and len(set(allowed)) == len(allowed), AccessErrorCode.INVALID_GATE)
    _require(requested in allowed, AccessErrorCode.STUDY_NOT_ALLOWED)
    reviewers = gate["reviewers"]
    _require(type(reviewers) is list and len(reviewers) == 2, AccessErrorCode.INVALID_GATE)
    roles, reports = set(), set()
    for reviewer in reviewers:
        _object(reviewer, {"role", "reportPath", "sha256", "decision"}, code=AccessErrorCode.INVALID_GATE)
        role, report = reviewer["role"], reviewer["reportPath"]
        _require(type(role) is str and role in REVIEW_ROLES and role not in roles
                 and reviewer["decision"] == "ACCEPTED_BOUNDED" and _sha(reviewer["sha256"]),
                 AccessErrorCode.INVALID_GATE)
        path = _canonical(report)
        _require(str(path.parent) == "reports/loop/reviews" and path.suffix == ".md"
                 and report not in reports, AccessErrorCode.INVALID_GATE)
        blob = _read_fd_file(root_fd, report)
        _require(bool(blob.strip()), AccessErrorCode.INVALID_GATE)
        _require(_digest(blob) == reviewer["sha256"], AccessErrorCode.PIN_MISMATCH)
        roles.add(role); reports.add(report)
    _require(roles == REVIEW_ROLES, AccessErrorCode.INVALID_GATE)
    freeze = _checked_json(root_fd, FREEZE_PATH, pins.freeze_sha256)
    _object(freeze, {"schemaVersion", "package", "frozenCommit", "planTag", "reviewedManifestSha256",
                     "groupContractSha256", "studyContractSha256"})
    _require(type(freeze["schemaVersion"]) is int and freeze["schemaVersion"] == 1
             and freeze["package"] == PACKAGE and freeze["frozenCommit"] == pins.frozen_commit
             and freeze["planTag"] == PLAN_TAG and freeze["reviewedManifestSha256"] == pins.manifest_sha256
             and freeze["groupContractSha256"] == pins.group_contract_sha256
             and freeze["studyContractSha256"] == pins.study_contract_sha256, AccessErrorCode.PIN_MISMATCH)
    manifest = _checked_json(root_fd, MANIFEST_PATH, pins.manifest_sha256)
    _object(manifest, {"schemaVersion", "package", "artifacts"}, exact=False)
    _require(type(manifest["schemaVersion"]) is int and manifest["schemaVersion"] == 1
             and manifest["package"] == PACKAGE and type(manifest["artifacts"]) is list)
    artifacts = {}
    for artifact in manifest["artifacts"]:
        _object(artifact, {"path", "sha256"})
        path, sha = artifact["path"], artifact["sha256"]
        _canonical(path)
        _require(path not in artifacts and _sha(sha))
        artifacts[path] = sha
    _require(CORE_ARTIFACTS <= set(artifacts)
             and artifacts[GROUP_CONTRACT_PATH] == pins.group_contract_sha256
             and artifacts[STUDY_CONTRACT_PATH] == pins.study_contract_sha256, AccessErrorCode.PIN_MISMATCH)
    # Read only fixed public paths before resolving any extra source artifact.
    group = _checked_json(root_fd, GROUP_CONTRACT_PATH, pins.group_contract_sha256)
    study_contract = _checked_json(root_fd, STUDY_CONTRACT_PATH, pins.study_contract_sha256)
    catalog = _checked_json(root_fd, CATALOG_PATH, artifacts[CATALOG_PATH])
    _require(study_contract["catalog"] == {"path": CATALOG_PATH, "sha256": artifacts[CATALOG_PATH]},
             AccessErrorCode.PIN_MISMATCH)
    studies = v2_io._validate_contract(study_contract, catalog)
    grouped, sources = _group_contract(group, studies, artifacts)
    for path, expected_sha in artifacts.items():
        _public_artifact_path(path, sources)
        _require(_digest(_read_fd_file(root_fd, path)) == expected_sha, AccessErrorCode.PIN_MISMATCH)
    runtime = _runtime_hashes()
    _require(runtime == _LOADED_RUNTIME_HASHES, AccessErrorCode.PIN_MISMATCH)
    _require(all(artifacts[path] == sha for path, sha in runtime.items()), AccessErrorCode.PIN_MISMATCH)
    return studies[requested], grouped[requested], _digest(gate_blob), artifacts


def _read_raw_bytes(root_fd, relative):
    """Only reached after the complete gate, manifest, library and source guard."""
    return _read_fd_file(root_fd, relative)


def _number(value, *, nullable=False, count=False):
    if value is None and nullable:
        return None
    _require(type(value) is int and value >= 0 if count else
             type(value) in {int, float} and isfinite(value) and value >= 0,
             AccessErrorCode.INVALID_PRIVATE_AGGREGATE)
    return value


def _aggregate_candidate(prepared, study, group_study):
    """Explicit aggregate allowlist; never dataclass-asdict or record traversal."""
    error = AccessErrorCode.INVALID_PRIVATE_AGGREGATE
    _require(type(prepared) is groups_api.PrivateGroupStudyReferences and prepared.schema == "policy-group-reference-v21-wip"
             and prepared.study_id == study["study_id"] and prepared.edition == study["edition"], error)
    expected_groups = group_study["groupsInDeclaredApiOrder"]
    _require(type(prepared.groups) is tuple and len(prepared.groups) == len(expected_groups), error)
    out_groups = []
    roles = [("pspwght", "primary"), ("dweight", "sensitivity"),
             ("unweighted", "sensitivity"), ("anweight", "equivalence_diagnostic")]
    for current, definition in zip(prepared.groups, expected_groups, strict=True):
        _require(type(current) is groups_api.PreparedGroup
                 and current.group_id == definition["groupId"] and current.party2_code == definition["party2Code"]
                 and current.kind == definition["kind"] and current.label_en_exact_api == definition["labelEnExactApi"]
                 and current.label_de_original_form == definition["labelDeOriginalForm"]
                 and current.label_de_official_appendix == definition["labelDeOfficialAppendix"]
                 and current.form_option_status == definition["formOptionStatus"], error)
        _require(type(current.questions) is tuple and len(current.questions) == len(study["adapter"]["questions"]), error)
        questions = []
        for question, declared in zip(current.questions, study["adapter"]["questions"], strict=True):
            _require(type(question) is groups_api.PreparedGroupQuestion
                     and question.question_id == declared["question_id"]
                     and type(question.status) is groups_api.GroupPreparationStatus, error)
            _require(type(question.estimates) is tuple and len(question.estimates) == 4, error)
            estimates = []
            for weighted, (weight, role) in zip(question.estimates, roles, strict=True):
                _require(type(weighted) is analysis_api.PreparedWeightReference
                         and weighted.weight == weight and weighted.role == role, error)
                reference = weighted.reference
                _require(type(reference) is reference_api.CategoricalReference
                         and type(reference.accounting) is reference_api.Accounting
                         and reference.design is None
                         and reference.variance_status in {reference_api.VarianceStatus.NO_DESIGN_BASIS,
                                                            reference_api.VarianceStatus.NO_VALID_RESPONSES}, error)
                analysis_api._validate_reference(reference, study["study_id"], declared["question_id"])
                _require([category.category for category in reference.estimates] == declared["categoryCodes"], error)
                accounting = {}
                for prefix in ("total", "eligible", "valid", "missing", "not_asked"):
                    accounting[prefix + "_count"] = _number(getattr(reference.accounting, prefix + "_count"), count=True)
                    accounting[prefix + "_weight"] = _number(getattr(reference.accounting, prefix + "_weight"))
                categories = []
                for category in reference.estimates:
                    _require(type(category) is reference_api.CategoryEstimate
                             and category.variance is None and category.standard_error is None, error)
                    categories.append({"category": category.category, "count": _number(category.count, count=True),
                                       "weight": _number(category.weight), "proportion": _number(category.proportion, nullable=True),
                                       "variance": None, "standard_error": None})
                estimates.append({"weight": weight, "role": role, "reference": {
                    "study_id": reference.study_id, "question_id": reference.question_id,
                    "accounting": accounting, "estimates": categories,
                    "variance_status": reference.variance_status.value, "design": None}})
            _require(type(question.missing_reasons) is tuple
                     and [value.reason for value in question.missing_reasons]
                     == list(dict.fromkeys(declared["missingCodes"].values())), error)
            missing = []
            for value in question.missing_reasons:
                _require(type(value) is analysis_api.MissingReasonAggregate, error)
                missing.append({"reason": value.reason, "count": _number(value.count, count=True),
                                "primary_weight_sum": _number(value.primary_weight_sum)})
            _require(type(question.not_asked) is analysis_api.NotAskedAggregate
                     and type(question.sensitivity) is groups_api.GroupQuestionSensitivity, error)
            questions.append({"question_id": question.question_id, "status": question.status.value,
                              "estimates": estimates, "missing_reasons": missing,
                              "not_asked": {"count": _number(question.not_asked.count, count=True),
                                            "primary_weight_sum": _number(question.not_asked.primary_weight_sum)},
                              "sensitivity": {key: _number(getattr(question.sensitivity, key), nullable=True)
                                              for key in ("max_abs_primary_unweighted", "max_abs_primary_dweight", "max_abs_primary_anweight")}})
        out_groups.append({"group_id": current.group_id, "party2_code": current.party2_code,
                           "kind": current.kind, "label_en_exact_api": current.label_en_exact_api,
                           "label_de_original_form": current.label_de_original_form,
                           "label_de_official_appendix": current.label_de_official_appendix,
                           "form_option_status": current.form_option_status,
                           "eligible_case_count": _number(current.eligible_case_count, count=True), "questions": questions})
    eligibility = prepared.eligibility
    _require(type(eligibility) is groups_api.GroupEligibilityDiagnostics, error)
    diagnostic = {}
    for key in ("de_case_count", "eligible_group_case_count", "non_yes_vote_with_valid_party_count", "yes_vote_with_party_not_asked_count"):
        diagnostic[key] = _number(getattr(eligibility, key), count=True)
    for key, expected in (("vote_states", ("yes", "no", "not_eligible", "source_missing", "technical_export_blank")),
                          ("party_states", ("valid_named_party", "valid_other_unlabelled", "structurally_not_asked", "source_missing", "technical_export_blank"))):
        values = getattr(eligibility, key)
        _require(type(values) is tuple and tuple(value.state for value in values) == expected, error)
        _require(all(type(value) is groups_api.StateCount for value in values), error)
        diagnostic[key] = [{"state": value.state, "count": _number(value.count, count=True)} for value in values]
    for key in ("vote_source_missing_reasons", "party_source_missing_reasons"):
        values = getattr(eligibility, key)
        _require(type(values) is tuple and all(type(value) is groups_api.ReasonCount for value in values)
                 and tuple(value.reason for value in values) == ("Refusal", "Don't know", "No answer"), error)
        diagnostic[key] = [{"reason": value.reason, "count": _number(value.count, count=True)} for value in values]
    ratio = prepared.study_ratio_diagnostic
    _require(type(ratio) is groups_api.EligibleRatioDiagnostic and ratio.scope == "all_eligible_group_cases"
             and ratio.tolerance == 1e-12
             and ratio.status in {"constant_within_tolerance", "nonconstant_ratio", "not_evaluable_no_eligible_group_cases"}
             and type(ratio.constant_against_first_within_tolerance) in {bool, type(None)}, error)
    return {"schema": prepared.schema, "study_id": prepared.study_id, "edition": prepared.edition,
            "groups": out_groups, "eligibility": diagnostic, "study_ratio_diagnostic": {
                "scope": ratio.scope, "case_count": _number(ratio.case_count, count=True), "status": ratio.status,
                "ratio_min": _number(ratio.ratio_min, nullable=True), "ratio_max": _number(ratio.ratio_max, nullable=True),
                "constant_against_first_within_tolerance": ratio.constant_against_first_within_tolerance,
                "tolerance": ratio.tolerance}}


def _write_private(root_fd, study_id, serialized):
    """Atomic private replacement with an own backup for controlled rollback."""
    relative = f"data/local/policy-groups-v21/{study_id}/run.json"
    parent = None
    temporary = backup = None
    temporary_owned = backup_owned = preserve_backup = False
    replaced = committed = False
    try:
        parent = _directory_at(root_fd, "data")
        for component in ("local", "policy-groups-v21", study_id):
            try:
                os.mkdir(component, mode=0o700, dir_fd=parent)
            except FileExistsError:
                pass
            child = _directory_at(parent, component)
            os.close(parent); parent = child
            _require(stat.S_IMODE(os.fstat(parent).st_mode) == 0o700, AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        try:
            previous = os.stat("run.json", dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            previous = None
        if previous is not None:
            _require(stat.S_ISREG(previous.st_mode) and stat.S_IMODE(previous.st_mode) == 0o600,
                     AccessErrorCode.PRIVATE_OUTPUT_FAILED)
            backup = ".previous-run-" + secrets.token_hex(16) + ".tmp"
            os.link("run.json", backup, src_dir_fd=parent, dst_dir_fd=parent, follow_symlinks=False)
            backup_owned = True
        temporary = ".run-" + secrets.token_hex(16) + ".tmp"
        descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC,
                             0o600, dir_fd=parent)
        temporary_owned = True
        with os.fdopen(descriptor, "wb") as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(serialized); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, "run.json", src_dir_fd=parent, dst_dir_fd=parent)
        temporary = None; replaced = True
        os.fsync(parent)
        committed = True
        return relative, _digest(serialized)
    except (OSError, ValueError, TypeError, ArithmeticError, RecursionError, PolicyGroupAccessError):
        if replaced and not committed:
            try:
                if backup is not None:
                    os.replace(backup, "run.json", src_dir_fd=parent, dst_dir_fd=parent)
                    backup = None
                else:
                    os.unlink("run.json", dir_fd=parent)  # Only this run's just-created target.
                os.fsync(parent)
            except OSError:
                preserve_backup = True  # Keep an own old-output backup if rollback itself fails.
        _fail(AccessErrorCode.PRIVATE_OUTPUT_FAILED)
    finally:
        for name, owned in ((temporary, temporary_owned), (backup, backup_owned and not preserve_backup)):
            if name is not None and owned and parent is not None:
                try:
                    os.unlink(name, dir_fd=parent)  # Only files created by this invocation.
                except OSError:
                    pass
        if parent is not None:
            os.close(parent)


def run_group_reference(repo_root, study_id, pins: AccessPins) -> RunReceipt:
    """Prepare exactly one explicitly gate-allowed study into private WIP JSON.

    The full guard precedes every raw path traversal/stat/open/read. Bytes are
    hashed before decoding. All DE rows' round/edition are checked before the
    pure group API sees party fields. Other CSV strings are lexically traversed,
    not semantically interpreted; no comprehensive blindness claim is made.
    """
    started = _utc()
    _require(type(study_id) is str and study_id in v2_io.STUDIES, AccessErrorCode.INVALID_SOURCE_IDENTITY)
    root_fd = None
    try:
        root_fd = _absolute_directory(os.fspath(repo_root))
    except (OSError, TypeError, ValueError):
        _fail(AccessErrorCode.INVALID_PATH)
    try:
        try:
            study, group_study, gate_sha, artifacts = _before_raw(root_fd, study_id, pins)
        except PolicyGroupAccessError:
            raise
        except (ValueError, TypeError, KeyError, AttributeError, ArithmeticError, RecursionError):
            _fail(AccessErrorCode.INVALID_PUBLIC_DOCUMENT)
        blob = _read_raw_bytes(root_fd, study["input"]["path"])
        input_sha = _digest(blob)
        _require(input_sha == study["input"]["sha256"] and len(blob) == study["input"]["bytes"],
                 AccessErrorCode.RAW_IDENTITY_MISMATCH)
        try:
            text = blob.decode("utf-8-sig")
        except UnicodeError:
            _fail(AccessErrorCode.INVALID_CSV)
        try:
            normalized = v2_io._metadata_and_response_text(text, study)
        except v2_io.PolicyAccessError as error:
            _fail(AccessErrorCode.INVALID_METADATA if error.code is v2_io.AccessErrorCode.INVALID_METADATA
                  else AccessErrorCode.INVALID_CSV)
        except (ValueError, TypeError, ArithmeticError):
            _fail(AccessErrorCode.INVALID_CSV)
        try:
            prepared = groups_api.prepare_group_references(normalized, study, group_study)
        except (ValueError, TypeError, AttributeError, ArithmeticError):
            _fail(AccessErrorCode.GROUP_PREPARATION_REJECTED)
        try:
            candidate = _aggregate_candidate(prepared, study, group_study)
            payload = {"schema": "policy-group-private-run-v21-wip", "status": PRIVATE_STATUS,
                       "study_id": study_id, "prepared_utc": _utc(),
                       "pins": {"manifestSha256": pins.manifest_sha256, "groupContractSha256": pins.group_contract_sha256,
                                "studyContractSha256": pins.study_contract_sha256, "freezeSha256": pins.freeze_sha256,
                                "gateSha256": gate_sha, "frozenCommit": pins.frozen_commit, "planTag": PLAN_TAG,
                                "inputSha256": input_sha, "catalogSha256": artifacts[CATALOG_PATH],
                                "runtimeLibraries": {path: artifacts[path] for path in sorted(_LOADED_RUNTIME_HASHES)}},
                       "candidate": candidate}
            serialized = (json.dumps(payload, ensure_ascii=False, allow_nan=False, separators=(",", ":")) + "\n").encode("utf-8")
        except PolicyGroupAccessError:
            raise
        except (ValueError, TypeError, KeyError, AttributeError, ArithmeticError, RecursionError):
            _fail(AccessErrorCode.INVALID_PRIVATE_AGGREGATE)
        private_path, output_sha = _write_private(root_fd, study_id, serialized)
        return RunReceipt(study_id, PRIVATE_STATUS, started, _utc(), gate_sha, pins.manifest_sha256,
                          pins.group_contract_sha256, pins.study_contract_sha256, pins.freeze_sha256,
                          input_sha, output_sha, private_path)
    finally:
        os.close(root_fd)
