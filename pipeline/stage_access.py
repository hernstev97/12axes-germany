"""Bounded B and Full-DE inputs; public authorization precedes private reads.

The coordinator receipts are mutable on a shared filesystem. Hashes detect
drift; they do not provide unforgeable authorization or close concurrent races.
No political, group, identity or person fields are selected. The CLI is for the
coordinator only. Importing pure helpers does not open a private path.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
from pipeline import empirical_access as access

ROOT = Path(__file__).resolve().parents[1]
SHA = access.SHA
ITEM_IDS = access.ITEM_IDS
AccessError = access.AccessError
require = access.require
PRIVATE = "data/local/empirical-v1"
SOURCE = "data/raw/ess11-ed4.2/ESS11e04_2.csv"
MODEL = "data/modell-v1.json"
A_RESULT = "reports/phasen/01-a-entwicklung.json"
B_RESULT = "reports/phasen/02-b-bestaetigung.json"
PRE_A = "reports/loop/gates/pre-empirical.json"
PRE_B = "reports/loop/gates/pre-confirmatory.json"
POST_B = "reports/loop/gates/post-confirmatory.json"
ASSIGNMENT = PRIVATE + "/assignment.json"
A_RECEIPT = PRIVATE + "/runtime-input-receipt.json"
B_INPUT = PRIVATE + "/B.csv"
B_RECEIPT = PRIVATE + "/confirm-input-receipt.json"
FULL_INPUT = PRIVATE + "/FULL.csv"
SENSITIVITY = PRIVATE + "/FULL-pspwght.csv"
FULL_RECEIPT = PRIVATE + "/full-input-receipt.json"
SOURCE_CODE = (
    "pipeline/ordinal/develop.R", "pipeline/ordinal/develop-config.R",
    "pipeline/ordinal/adapter_v2.R", "pipeline/ordinal/support.R",
)
PLAN_ARTIFACTS = ("docs/empirie-plan-v1.entwurf.md", "data/analysevertrag.v1.entwurf.json",
                  "pipeline/ordinal/develop-config.R")
EXPECTATION_ARTIFACTS = ("data/item-core-v1.json",
                       "reports/loop/authors/ESS-CONSTRUCTS-resume-proposal.md")
REQUIRED_CODE = ("pipeline/stage_access.py", "pipeline/empirical_access.py",
                 "data/item-core-v1.json", *SOURCE_CODE)
GROUPS = {
    "M2": {"H": list(ITEM_IDS[:3]), "ZF": list(ITEM_IDS[3:])},
    "M3": {"H": list(ITEM_IDS[:3]), "Z": list(ITEM_IDS[3:6]), "F": list(ITEM_IDS[6:])},
}
LIMITS = "Mutable coordinator receipts and shared FS; no read isolation or unforgeable gate"


def sha_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def valid_sha(value) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def relative_path(value, *, public: bool) -> str:
    require(isinstance(value, str) and value != "" and
            not Path(value).is_absolute() and ".." not in Path(value).parts and
            Path(value).as_posix() == value, "PATH")
    if public:
        require(Path(value).parts[:2] not in (("data", "raw"), ("data", "local")),
                "GATE_PUBLIC_PATH")
    return value


def regular_path(root: Path, relative: str, *, public=False, private=False) -> Path:
    relative_path(relative, public=public)
    require(root.is_absolute() and root.resolve() == root, "ROOT_PATH")
    path = root / relative
    current = root
    for part in Path(relative).parts:
        current /= part
        require(not current.is_symlink(), "SYMLINK")
        require(current.exists(), "MISSING_PATH")
    require(path.is_file(), "REGULAR_FILE")
    if private:
        for folder in (root / "data/local", root / PRIVATE):
            require(folder.is_dir() and folder.stat().st_mode & 0o777 == 0o700,
                    "PRIVATE_PARENT_MODE")
        require(path.stat().st_mode & 0o777 == 0o600, "PRIVATE_FILE_MODE")
    return path


def json_file(path: Path) -> dict:
    value = json.loads(path.read_text())
    require(isinstance(value, dict), "JSON_OBJECT")
    return value


def _verified_gate(root: Path, relative: str) -> tuple[dict, str, dict[str, str]]:
    path = regular_path(root, relative, public=True)
    frozen = path.read_bytes()
    receipt = json.loads(frozen)
    require(isinstance(receipt, dict) and receipt.get("decision") == "ACCEPTED_BOUNDED",
            "GATE_DECISION")
    reviews = receipt.get("reviews")
    require(isinstance(reviews, list) and len(reviews) == 2 and
            all(isinstance(r, dict) and isinstance(r.get("reviewer"), str) and
                bool(r["reviewer"]) for r in reviews) and
            len({r["reviewer"] for r in reviews}) == 2 and
            {r.get("scope") for r in reviews} ==
            {"methods-repro", "sources-construct-fairness"}, "REVIEW_ROLES")
    artifacts = receipt.get("artifacts")
    require(isinstance(artifacts, list) and all(isinstance(a, dict) for a in artifacts),
            "GATE_ARTIFACTS")
    observed = {}
    for entry in [*artifacts, *reviews]:
        relative = relative_path(entry.get("path"), public=True)
        expected = entry.get("sha256")
        require(valid_sha(expected) and relative not in observed, "GATE_ENTRY")
        actual = digest(regular_path(root, relative, public=True))
        require(actual == expected, "GATE_PIN")
        observed[relative] = actual
    return receipt, sha_bytes(frozen), observed


def _tag(root: Path, name: str, expected: str) -> None:
    require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{40}", expected), "TAG_HASH")
    local = subprocess.run(["git", "rev-parse", f"refs/tags/{name}^{{commit}}"],
                           cwd=root, capture_output=True, text=True, check=True).stdout.strip()
    remote = subprocess.run(["git", "ls-remote", "origin", f"refs/tags/{name}",
                             f"refs/tags/{name}^{{}}"], cwd=root,
                            capture_output=True, text=True, check=True).stdout.splitlines()
    refs = {}
    for line in remote:
        parts = line.split()
        require(len(parts) == 2 and parts[1] in
                (f"refs/tags/{name}", f"refs/tags/{name}^{{}}") and
                parts[1] not in refs, "PUBLIC_TAG_PIN")
        refs[parts[1]] = parts[0]
    remote_commit = refs.get(f"refs/tags/{name}^{{}}", refs.get(f"refs/tags/{name}"))
    require(f"refs/tags/{name}" in refs and local == remote_commit == expected,
            "PUBLIC_TAG_PIN")


def _tag_tree(root: Path, name: str, relative: str, expected: str) -> None:
    """Hash fixed public tag-tree bytes without displaying their contents."""
    require(valid_sha(expected), "TAG_TREE_ARTIFACT")
    payload = subprocess.run(["git", "show", f"refs/tags/{name}:{relative}"], cwd=root,
                             capture_output=True, check=True).stdout
    require(isinstance(payload, bytes) and sha_bytes(payload) == expected, "TAG_TREE_PIN")


def canonical_scores(scores, model: str) -> bool:
    return (isinstance(scores, list) and len(scores) >= 2 and
            scores == [key for key in GROUPS[model] if key in scores])


def validate_freeze(freeze: dict, reviewed: dict, model_sha: str, artifacts: dict) -> dict:
    require(set(freeze) == {"schema", "model", "scores", "items", "groups", "config",
                            "source_code_pins", "a_result"}, "MODEL_KEYS")
    model = freeze.get("model")
    require(freeze.get("schema") == "life93-model-freeze-1" and model in GROUPS, "MODEL_SCHEMA")
    require(freeze.get("items") == list(ITEM_IDS) and freeze.get("groups") == GROUPS[model] and
            canonical_scores(freeze.get("scores"), model), "MODEL_SCORES")
    config = freeze.get("config")
    require(isinstance(config, dict) and config.get("items") == list(ITEM_IDS) and
            config.get("input_columns") == ["stratum", "psu", "weight", *ITEM_IDS] and
            isinstance(config.get("models"), dict) and config["models"].get(model) == GROUPS[model],
            "MODEL_CONFIG")
    pins = freeze.get("source_code_pins")
    require(isinstance(pins, dict) and set(pins) == set(SOURCE_CODE) and
            all(valid_sha(value) and reviewed.get(path) == value for path, value in pins.items()),
            "MODEL_SOURCE_CODE")
    a_result = freeze.get("a_result")
    require(isinstance(a_result, dict) and set(a_result) == {"path", "sha256"} and
            a_result.get("path") == A_RESULT and valid_sha(a_result.get("sha256")) and
            artifacts.get(A_RESULT) == a_result["sha256"] and artifacts.get(MODEL) == model_sha,
            "MODEL_RESULT_PIN")
    return freeze


def _reviewed_code(root: Path, receipt: dict, receipt_path: str) -> dict:
    runtime = receipt.get("runtime", {})
    require(isinstance(runtime, dict) and runtime.get("schema") == "r-stage-access-v1" and
            runtime.get("sourceSha256") == SHA and
            runtime.get("privateReceiptPath") == receipt_path, "GATE_RUNTIME")
    reviewed = runtime.get("reviewedCodeHashes")
    require(isinstance(reviewed, dict) and set(REQUIRED_CODE).issubset(reviewed), "REVIEWED_CODE_SET")
    for relative, expected in reviewed.items():
        relative_path(relative, public=True)
        require(relative.startswith(("pipeline/", "data/")) and valid_sha(expected),
                "REVIEWED_CODE_PATH")
        require(digest(regular_path(root, relative, public=True)) == expected, "REVIEWED_CODE_PIN")
    return reviewed


def public_preflight(root: Path = ROOT, arm: str = "B") -> dict:
    """Only public paths and actual local/remote tags, before any private read."""
    require(arm in ("B", "FULL"), "ARM")
    original, original_sha, original_artifacts = _verified_gate(root, PRE_A)
    gate, gate_sha, artifacts = _verified_gate(root, PRE_B)
    tags = gate.get("tags")
    require(isinstance(tags, dict) and isinstance(original.get("tags"), dict), "TAGS")
    for name in ("analyseplan-v1", "erwartungsmodell-v1"):
        require(tags.get(name) == original["tags"].get(name), "ORIGINAL_TAG_PIN")
        _tag(root, name, tags.get(name))
    _tag(root, "modell-v1", tags.get("modell-v1"))
    for name, paths in (("analyseplan-v1", PLAN_ARTIFACTS),
                        ("erwartungsmodell-v1", EXPECTATION_ARTIFACTS)):
        for relative in paths:
            _tag_tree(root, name, relative, original_artifacts.get(relative))
    require(sys.version_info[:3] == (3, 14, 7), "PYTHON_VERSION")
    reviewed = _reviewed_code(root, gate, B_RECEIPT)
    model_path = regular_path(root, MODEL, public=True)
    model_bytes = model_path.read_bytes()
    model_sha = sha_bytes(model_bytes)
    freeze = validate_freeze(json.loads(model_bytes), reviewed, model_sha, artifacts)
    _tag_tree(root, "modell-v1", MODEL, model_sha)
    _tag_tree(root, "modell-v1", A_RESULT, artifacts.get(A_RESULT))
    result = {"arm": arm, "gateSha256": gate_sha, "modelSha256": model_sha,
              "sourceSha256": SHA, "codeSha256": reviewed,
              "originalGateSha256": original_sha, "freeze": freeze,
              "authorization": {"decision": "ACCEPTED_BOUNDED", "arm": arm,
                                "wrapper_verified": True, "freeze_sha256": model_sha},
              "limits": LIMITS}
    if arm == "FULL":
        post, post_sha, post_artifacts = _verified_gate(root, POST_B)
        require(post.get("B_step_completed") is True, "B_STEP_INCOMPLETE")
        retained = post.get("B_retained_scores")
        require(canonical_scores(retained, freeze["model"]) and
                set(retained).issubset(freeze["scores"]), "B_REINTRODUCED_SCORE")
        b_result = post.get("b_result")
        require(isinstance(b_result, dict) and set(b_result) == {"path", "sha256"} and
                b_result.get("path") == B_RESULT and valid_sha(b_result.get("sha256")) and
                post_artifacts.get(B_RESULT) == b_result["sha256"] and
                post_artifacts.get(MODEL) == model_sha, "B_RESULT_PIN")
        aggregate = json_file(regular_path(root, B_RESULT, public=True))
        confirmation = aggregate.get("confirmation", {})
        require(aggregate.get("schema") == "life93-fixed-model-confirmation-aggregate-1" and
                aggregate.get("arm") == "B" and aggregate.get("freeze") == freeze and
                aggregate.get("model_name") == freeze["model"] and
                isinstance(confirmation, dict) and
                confirmation.get("status") == "CRITERIA_PASSED_PENDING_RESULT_REVIEW" and
                confirmation.get("global_model_passed") is True and
                confirmation.get("retained_scores") == retained and
                confirmation.get("minimum_scores") == 2, "B_RESULT_CONSISTENCY")
        post_tags = post.get("tags", {})
        require(all(post_tags.get(name) == tags.get(name) for name in
                    ("analyseplan-v1", "erwartungsmodell-v1", "modell-v1")), "POST_TAG_PIN")
        post_code = _reviewed_code(root, post, FULL_RECEIPT)
        require(all(post_code.get(key) == value for key, value in reviewed.items()), "POST_CODE_PIN")
        result.update(gateSha256=post_sha, confirmationGateSha256=gate_sha,
                      codeSha256=post_code, B_retained_scores=retained)
        result["authorization"].update(B_step_completed=True, B_retained_scores=retained)
    return result


def _responses(row, items, positions, diagnostic):
    values = []
    for item, at in zip(items, positions, strict=True):
        token = row[at].strip()
        if token in access.LEXICAL_MISSING:
            values.append("NA")
            continue
        value = access.integer(token)
        if value in item["integrated_file_missing_codes"]:
            values.append("NA")
            continue
        require(value in item["allowed_values"], diagnostic)
        order = item["allowed_values"].index(value)
        if item["scoring"]["map"][str(item["allowed_values"][0])] == 1:
            order = len(item["allowed_values"]) - 1 - order
        values.append(order)
    return values


def confirmation_frame(frozen: bytes, split: dict, contract: dict, expected_sha: str = SHA):
    """Reproduce metadata assignment; select B before interpreting nine answers."""
    require(split.get("inputSha256") == expected_sha and split.get("seed") == 2026100301,
            "SPLIT_PIN")
    require(split == access.assignment(frozen, expected_sha), "SPLIT_REPRODUCTION")
    items = access.validate_item_contract(contract)
    header, rows = access.table(frozen, expected_sha)
    require(all(i["variable"] in header for i in items), "ITEM_HEADER")
    positions = [header.index(i["variable"]) for i in items]
    units = {(u["stratum"], u["psu"]): u for u in split["units"]}
    output = []
    for row in rows:
        meta = access.metadata(header, row)
        if meta["cntry"] != "DE":
            continue
        unit = units[(meta["stratum"], meta["psu"])]
        if unit["arm"] != "B":
            continue
        values = _responses(row, items, positions, "UNEXPECTED_B_CATEGORY")
        output.append([meta["stratum"], meta["psu"],
                       meta["anweight"] / unit["probability"], *values])
    return ["stratum", "psu", "weight", *ITEM_IDS], output


def full_frame(frozen: bytes, contract: dict, expected_sha: str = SHA):
    """All DE rows and original weights; pspwght is a separate aligned column."""
    items = access.validate_item_contract(contract)
    header, rows = access.table(frozen, expected_sha)
    require(all(i["variable"] in header for i in items) and "pspwght" in header, "ITEM_HEADER")
    positions = [header.index(i["variable"]) for i in items]
    sensitivity_at = header.index("pspwght")
    strata = set()
    units = {}
    output, sensitivity = [], []
    for row in rows:
        meta = access.metadata(header, row)
        if meta["cntry"] != "DE":
            continue
        h, p = meta["stratum"], meta["psu"]
        require(p not in units or units[p] == h, "PSU_NESTING")
        units[p] = h
        strata.add(h)
        values = _responses(row, items, positions, "UNEXPECTED_FULL_CATEGORY")
        output.append([h, p, meta["anweight"], *values])
        sensitivity.append([access.positive_weight(row[sensitivity_at])])
    require(len(strata) == 25 and len(units) == 500, "FULL_DESIGN_FRAME")
    require(all(sum(value == h for value in units.values()) >= 2 for h in strata), "DESIGN_SUPPORT")
    return ["stratum", "psu", "weight", *ITEM_IDS], output, sensitivity


def private_boundary(root: Path, destinations: tuple[str, ...] = ()) -> Path:
    """Existing A folder and fresh outputs are checked before original input opens."""
    require(root.is_absolute() and root.resolve() == root, "ROOT_PATH")
    folder = root / PRIVATE
    current = root
    for part in Path(PRIVATE).parts:
        current /= part
        require(not current.is_symlink() and current.is_dir(), "PRIVATE_FOLDER")
        if current.is_relative_to(root / "data/local"):
            require(current.stat().st_mode & 0o777 == 0o700, "PRIVATE_PARENT_MODE")
    for relative in destinations:
        require(relative in (B_INPUT, B_RECEIPT, FULL_INPUT, SENSITIVITY, FULL_RECEIPT), "PRIVATE_PATH")
        path = root / relative
        require(path.parent == folder and not path.exists() and not path.is_symlink(), "DO_NOT_OVERWRITE")
    return folder


def _binding(root: Path, receipt: dict, key: str, relative: str) -> str:
    entry = receipt.get(key, {})
    require(isinstance(entry, dict) and set(entry) == {"path", "sha256"} and
            entry.get("path") == relative and valid_sha(entry.get("sha256")), "PRIVATE_INPUT_BINDING")
    observed = digest(regular_path(root, relative, private=True))
    require(observed == entry["sha256"], "PRIVATE_INPUT_PIN")
    return observed


def _assignment_provenance(root: Path, public: dict) -> dict:
    path = regular_path(root, A_RECEIPT, private=True)
    provenance = json_file(path)
    require(provenance.get("schema") == "r-runtime-input-v1" and
            provenance.get("sourceSha256") == SHA and
            provenance.get("gateSha256") == public["originalGateSha256"] and
            provenance.get("empiricalAccessSha256") == public["codeSha256"]["pipeline/empirical_access.py"],
            "ASSIGNMENT_PROVENANCE")
    assignment_sha = _binding(root, provenance, "assignment", ASSIGNMENT)
    split = json_file(regular_path(root, ASSIGNMENT, private=True))
    require(split.get("inputSha256") == SHA and split.get("seed") == 2026100301, "ASSIGNMENT_SOURCE_PIN")
    return {"assignmentSha256": assignment_sha, "assignmentProvenanceSha256": digest(path), "split": split}


def _confirmation_private(root: Path, public: dict) -> dict:
    private_boundary(root)
    provenance = _assignment_provenance(root, public)
    path = regular_path(root, B_RECEIPT, private=True)
    receipt = json_file(path)
    require(receipt.get("schema") == "r-confirm-input-v1" and
            receipt.get("gateSha256") == public["gateSha256"] and
            receipt.get("modelSha256") == public["modelSha256"] and
            receipt.get("sourceSha256") == SHA and receipt.get("codeSha256") == public["codeSha256"],
            "PRIVATE_RECEIPT_BINDING")
    require(_binding(root, receipt, "assignment", ASSIGNMENT) == provenance["assignmentSha256"] and
            _binding(root, receipt, "assignmentProvenance", A_RECEIPT) ==
            provenance["assignmentProvenanceSha256"], "ASSIGNMENT_PROVENANCE")
    return {"assignmentSha256": provenance["assignmentSha256"],
            "assignmentProvenanceSha256": provenance["assignmentProvenanceSha256"],
            "bSha256": _binding(root, receipt, "confirmationInput", B_INPUT),
            "confirmReceiptSha256": digest(path)}


def preflight_confirmation(root: Path = ROOT) -> dict:
    public = public_preflight(root, "B")
    public["privatehashes"] = _confirmation_private(root, public)
    return public


def preflight_full(root: Path = ROOT) -> dict:
    public = public_preflight(root, "FULL")
    b_public = dict(public, gateSha256=public["confirmationGateSha256"])
    # The B receipt binds the pre-B code set. Post-B may add reviewed helpers.
    b_public["codeSha256"] = _reviewed_code(root, json_file(regular_path(root, PRE_B, public=True)), B_RECEIPT)
    hashes = _confirmation_private(root, b_public)
    path = regular_path(root, FULL_RECEIPT, private=True)
    receipt = json_file(path)
    require(receipt.get("schema") == "r-full-input-v1" and
            receipt.get("gateSha256") == public["gateSha256"] and
            receipt.get("modelSha256") == public["modelSha256"] and
            receipt.get("sourceSha256") == SHA and receipt.get("codeSha256") == public["codeSha256"] and
            receipt.get("confirmReceiptSha256") == hashes["confirmReceiptSha256"], "PRIVATE_RECEIPT_BINDING")
    require(_binding(root, receipt, "assignment", ASSIGNMENT) == hashes["assignmentSha256"] and
            _binding(root, receipt, "assignmentProvenance", A_RECEIPT) ==
            hashes["assignmentProvenanceSha256"], "ASSIGNMENT_PROVENANCE")
    hashes.update(fullSha256=_binding(root, receipt, "fullInput", FULL_INPUT),
                  sensitivitySha256=_binding(root, receipt, "sensitivityInput", SENSITIVITY),
                  fullReceiptSha256=digest(path))
    public["privatehashes"] = hashes
    return public


def _csv_payload(header, rows):
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer)
    writer.writerow(header)
    writer.writerows(rows)
    return buffer.getvalue().encode()


def exclusive_write(root: Path, relative: str, payload: bytes) -> str:
    private_boundary(root, (relative,))
    path = root / relative
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "wb") as stream:
        os.fchmod(stream.fileno(), 0o600)
        stream.write(payload)
    return sha_bytes(payload)


def prepare_stage(root: Path = ROOT, arm: str = "B") -> None:
    """Coordinator action. Never called by a runtime preflight or pure test."""
    public = public_preflight(root, arm)
    destinations = (B_INPUT, B_RECEIPT) if arm == "B" else (FULL_INPUT, SENSITIVITY, FULL_RECEIPT)
    private_boundary(root, destinations)
    provenance = _assignment_provenance(root, public)
    b_hashes = None
    if arm == "FULL":
        b_public = dict(public, gateSha256=public["confirmationGateSha256"])
        b_public["codeSha256"] = _reviewed_code(root, json_file(regular_path(root, PRE_B, public=True)), B_RECEIPT)
        b_hashes = _confirmation_private(root, b_public)
    contract = json_file(regular_path(root, "data/item-core-v1.json", public=True))
    # This fixed path deliberately permits the existing original-data directory
    # link. The single byte snapshot, expected SHA and metadata version bind it.
    frozen = (root / SOURCE).read_bytes()
    if arm == "B":
        header, rows = confirmation_frame(frozen, provenance["split"], contract)
        input_sha = exclusive_write(root, B_INPUT, _csv_payload(header, rows))
    else:
        header, rows, sensitivity = full_frame(frozen, contract)
        input_sha = exclusive_write(root, FULL_INPUT, _csv_payload(header, rows))
        sensitivity_sha = exclusive_write(root, SENSITIVITY, _csv_payload(["pspwght"], sensitivity))
    receipt = {"schema": "r-confirm-input-v1" if arm == "B" else "r-full-input-v1",
               "gateSha256": public["gateSha256"], "modelSha256": public["modelSha256"],
               "sourceSha256": SHA, "codeSha256": public["codeSha256"],
               "assignment": {"path": ASSIGNMENT, "sha256": provenance["assignmentSha256"]},
               "assignmentProvenance": {"path": A_RECEIPT,
                                        "sha256": provenance["assignmentProvenanceSha256"]}}
    if arm == "B":
        receipt["confirmationInput"] = {"path": B_INPUT, "sha256": input_sha}
        receipt_path = B_RECEIPT
    else:
        receipt["fullInput"] = {"path": FULL_INPUT, "sha256": input_sha}
        receipt["sensitivityInput"] = {"path": SENSITIVITY, "sha256": sensitivity_sha}
        receipt["confirmReceiptSha256"] = b_hashes["confirmReceiptSha256"]
        receipt_path = FULL_RECEIPT
    exclusive_write(root, receipt_path, (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("arm", choices=("B", "FULL"))
    args = parser.parse_args()
    try:
        prepare_stage(ROOT, args.arm)
        print("Private stage saved. No rows, keys or answer values emitted.")
    except AccessError as error:
        print("STAGE_ACCESS_" + str(error), file=sys.stderr)
        raise SystemExit(2) from None
    except Exception:
        print("STAGE_ACCESS_INPUT_OR_GATE_ERROR", file=sys.stderr)
        raise SystemExit(2) from None


if __name__ == "__main__":
    main()
