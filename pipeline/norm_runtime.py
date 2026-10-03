#!/usr/bin/env python3
"""Fixed FULL norms after public gates; standalone invented probes are separate.

No arbitrary input/entry path, gate bypass, installer or public result copy.
Coordinator receipts are mutable. Hashes reduce drift; they do not make this a
read sandbox, an atomic transaction or unforgeable authorization.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
if __package__ in (None, ""):
    sys.path.insert(0, str(ROOT))
from pipeline import r_runtime as rt
from pipeline import confirm_runtime as cr
from pipeline import stage_access as access

WRAPPER = "pipeline/norm_runtime.py"
NORMS = "pipeline/ordinal/norms.R"
ENTRY = "pipeline/ordinal/reproduce-norms.R"
TEST = "pipeline/ordinal/test-norms.R"
CODE = tuple(dict.fromkeys((*cr.CODE_PRIVATE, WRAPPER, NORMS, ENTRY, TEST)))
GATE = "reports/loop/gates/pre-norms.json"
FULL_RESULT = "reports/phasen/03-full-anwendung.json"
FULL_PUBLIC_RUN = "reports/loop/full-runtime-public.json"
FULL_RUN_LABEL = "real-full-001"
FULL_RUN = access.PRIVATE + "/runtime-runs/" + FULL_RUN_LABEL
FULL_RUN_RECEIPT = FULL_RUN + "/receipt.json"
FULL_AGGREGATE = FULL_RUN + "/confirmation-aggregate.private.json"
REQUIRED_ARTIFACTS = (access.MODEL, access.B_RESULT, access.POST_B, FULL_RESULT, FULL_PUBLIC_RUN)
FROZEN_PINS = {
    **cr.FROZEN_PINS,
    "pipeline/empirical_access.py": "a21de31bd937e708681095a36673267b02578217effb185a01ae4c42a9019901",
    "pipeline/stage_access.py": "50774e5190c8c6e82b27f77223b6a572b261ff71088e02841a703557ec06c02f",
    "pipeline/confirm_runtime.py": "9399e29e4eda5a4faf2f46dc9f3f2fd6a3c74f2ceefa572c2caeab5b94844ba5",
    NORMS: "ea360f0f76e889a8d872488cc2c20b1f62936ddea18ca0160ca9c14bce4b1e32",
    TEST: "f91ea9c3c67188943215ad34b4b4f28921a2ad206949a47c968562669a254b52",
}


def sha(payload):
    return hashlib.sha256(payload).hexdigest()


def json_bytes(payload):
    value = json.loads(payload)
    rt.require(isinstance(value, dict), "NORM_JSON_OBJECT")
    return value


def public_binding(entry):
    rt.require(isinstance(entry, dict) and set(entry) == {"path", "sha256"}, "NORM_PUBLIC_BINDING")
    relative = access.relative_path(entry["path"], public=True)
    rt.require(access.valid_sha(entry["sha256"]), "NORM_PUBLIC_HASH")
    return relative


def validate_public(gate, observed, hashes, full_public, public_run, public):
    """Pure state validation. No files, private input or tag calls."""
    rt.require(set(gate) == {"schema", "decision", "review", "artifacts", "runtime"} and
               gate["schema"] == "life93-pre-norms-1" and gate["decision"] == "ACCEPTED_BOUNDED",
               "NORM_GATE_SCHEMA")
    review = gate["review"]
    rt.require(isinstance(review, dict) and set(review) == {"reviewer", "scope", "path", "sha256"} and
               isinstance(review["reviewer"], str) and bool(review["reviewer"].strip()) and
               review["scope"] == "norms-methods-repro", "NORM_REVIEW_SCOPE")
    review_binding = {key: review[key] for key in ("path", "sha256")}
    review_path = public_binding(review_binding)
    rt.require(observed.get(review_path) == review["sha256"], "NORM_REVIEW_PIN")
    artifacts = gate["artifacts"]
    rt.require(isinstance(artifacts, list), "NORM_ARTIFACTS")
    required = {}
    for entry in artifacts:
        path = public_binding(entry)
        rt.require(path not in required and path != review_path and observed.get(path) == entry["sha256"],
                   "NORM_ARTIFACT_PIN")
        required[path] = entry["sha256"]
    rt.require(set(REQUIRED_ARTIFACTS).issubset(required), "NORM_REQUIRED_ARTIFACTS")
    spec = gate["runtime"]
    rt.require(isinstance(spec, dict) and set(spec) == {"schema", "sourceSha256", "fullRunLabel", "reviewedCodeHashes"} and
               spec["schema"] == "r-norm-runtime-v1" and spec["sourceSha256"] == access.SHA and
               spec["fullRunLabel"] == FULL_RUN_LABEL, "NORM_GATE_RUNTIME")
    reviewed = spec["reviewedCodeHashes"]
    rt.require(isinstance(reviewed, dict) and set(CODE).issubset(reviewed) and
               all(reviewed.get(path) == value for path, value in hashes.items()) and
               all(reviewed.get(path) == value for path, value in public["codeSha256"].items()),
               "NORM_REVIEWED_CODE_PIN")
    rt.require(all(hashes.get(path) == value for path, value in FROZEN_PINS.items()), "NORM_FROZEN_CODE_PIN")
    rt.require(required[access.MODEL] == public["modelSha256"] and
               required[access.POST_B] == public["gateSha256"], "NORM_STAGE_REFERENCE")
    confirmation = full_public.get("confirmation", {})
    scores = confirmation.get("retained_scores")
    rt.require(full_public.get("schema") == "life93-fixed-model-confirmation-aggregate-1" and
               full_public.get("arm") == "FULL" and full_public.get("freeze") == public["freeze"] and
               full_public.get("model_name") == public["freeze"]["model"] and
               full_public.get("model", {}).get("status") == "EXECUTED" and
               full_public.get("model", {}).get("eligible") is True and
               confirmation.get("status") == "CRITERIA_PASSED_PENDING_RESULT_REVIEW" and
               confirmation.get("global_model_passed") is True and confirmation.get("minimum_scores") == 2 and
               access.canonical_scores(scores, public["freeze"]["model"]) and
               set(scores).issubset(public["B_retained_scores"]), "NORM_FULL_PUBLIC_CONTRACT")
    rt.require(set(public_run) == {"schema", "stage", "label", "exitCode", "runtimeProbeExitCode", "codeHashes", "runtimePins", "references", "limits"} and
               public_run["schema"] == "r-full-runtime-public-v1" and public_run["stage"] == "FULL" and
               public_run["label"] == FULL_RUN_LABEL and public_run["exitCode"] == 0 and
               public_run["runtimeProbeExitCode"] == 0 and
               public_run["codeHashes"] == {p: hashes[p] for p in cr.CODE_PRIVATE}, "NORM_FULL_PUBLIC_RUN")
    refs = public_run["references"]
    expected = {"model": access.MODEL, "bResult": access.B_RESULT, "fullResult": FULL_RESULT, "postB": access.POST_B}
    rt.require(isinstance(refs, dict) and set(refs) == set(expected) and
               all(refs[key] == {"path": path, "sha256": required[path]} for key, path in expected.items()),
               "NORM_FULL_PUBLIC_REFERENCES")
    return {"artifactSha256": required, "reviewedCodeHashes": reviewed}


def public_preflight(root=ROOT):
    """All new public review/code checks precede checked_preflight's private calls."""
    payload = rt.regular_path(root, GATE).read_bytes()
    gate = json_bytes(payload)
    rt.require(isinstance(gate.get("artifacts"), list) and isinstance(gate.get("review"), dict), "NORM_GATE_SCHEMA")
    entries = [*gate["artifacts"], {k: gate["review"].get(k) for k in ("path", "sha256")}]
    observed, frozen = {}, {}
    for entry in entries:
        relative = public_binding(entry)
        rt.require(relative not in observed, "NORM_DUPLICATE_BINDING")
        data = rt.regular_path(root, relative).read_bytes()
        rt.require(sha(data) == entry["sha256"], "NORM_PUBLIC_PIN")
        observed[relative], frozen[relative] = sha(data), data
    reviewed = gate.get("runtime", {}).get("reviewedCodeHashes")
    rt.require(isinstance(reviewed, dict), "NORM_REVIEWED_CODE_SET")
    for relative, expected in reviewed.items():
        access.relative_path(relative, public=True)
        rt.require(relative.startswith(("pipeline/", "data/")) and access.valid_sha(expected), "NORM_CODE_PATH")
        rt.require(rt.digest(rt.regular_path(root, relative)) == expected, "NORM_REVIEWED_CODE_PIN")
    hashes = rt.code_hashes(root, CODE)
    # Only public paths/tags here; never the confirmation private preflight yet.
    public = access.public_preflight(root, "FULL")
    rt.require(FULL_RESULT in frozen and FULL_PUBLIC_RUN in frozen, "NORM_REQUIRED_ARTIFACTS")
    full_public, public_run = json_bytes(frozen[FULL_RESULT]), json_bytes(frozen[FULL_PUBLIC_RUN])
    bindings = validate_public(gate, observed, hashes, full_public, public_run, public)
    return {"normGateSha256": sha(payload), "bindings": bindings, "public": public,
            "fullPublic": full_public, "fullPublicRun": public_run, "codeHashes": hashes}


def checked_preflight(root=ROOT):
    public = public_preflight(root)
    full = cr.checked_preflight(root, "FULL")
    rt.require(all(full.get(key) == public["public"].get(key) for key in public["public"]),
               "NORM_FULL_PREFLIGHT_DRIFT")
    public["fullAuthorization"] = full
    return public


def validate_full_provenance(record, aggregate, public, runtime_pins, payload_hashes, probe):
    """Private pure validation; returns hashes only to the private run receipt."""
    auth = public["fullAuthorization"]
    hashes = public["codeHashes"]
    rt.require(record.get("schema") == "r-confirm-runtime-run-v1" and record.get("stage") == "FULL" and
               record.get("label") == FULL_RUN_LABEL and record.get("exitCode") == 0 and
               record.get("runtimeProbeExitCode") == 0 and not record.get("failureCode") and
               record.get("codeHashes") == {p: hashes[p] for p in cr.CODE_PRIVATE} and
               record.get("privateAuthorization") == auth and
               record.get("runtimePins") == runtime_pins and record.get("runtimePinsAfter") == runtime_pins,
               "NORM_ACTUAL_FULL_RUN")
    rt.require(public["fullPublicRun"]["runtimePins"] == runtime_pins, "NORM_PUBLIC_RUNTIME_PIN")
    inventory = record.get("filesBeforeFinalReceipt", {})
    for name in ("confirmation-aggregate.private.json", "runtime.json", "confirmation-entry.R", "authorization.json"):
        binding = inventory.get(name, {})
        rt.require(isinstance(binding, dict) and access.valid_sha(binding.get("sha256")) and
                   payload_hashes.get(name) == binding["sha256"], "NORM_FULL_RUN_FILE_PIN")
    rt.require(record.get("entrySha256") == payload_hashes["confirmation-entry.R"] == sha(cr.private_entry().encode()) and
               record.get("authorizationFileSha256") == payload_hashes["authorization.json"], "NORM_FULL_ENTRY_PIN")
    for path, expected in record["codeHashes"].items():
        rt.require(inventory.get("source-snapshot/" + path, {}).get("sha256") == expected and
                   payload_hashes.get("source-snapshot/" + path) == expected, "NORM_FULL_SOURCE_SNAPSHOT")
    rt.require(probe.get("R") == "4.5.3" and probe.get("packages") == rt.PACKAGE_VERSIONS and
               probe.get("outside_write_denied") is True, "NORM_FULL_RUNTIME_PROBE")
    public_aggregate = {key: value for key, value in public["fullPublic"].items() if key != "attribution"}
    rt.require(aggregate == public_aggregate, "NORM_PRIVATE_PUBLIC_FULL_MATCH")
    expected_sources = {path: hashes[path] for path in (*access.SOURCE_CODE, cr.CONFIRM)}
    rt.require(aggregate.get("source_code_pins") == expected_sources and aggregate.get("freeze") == auth["freeze"] and
               aggregate.get("arm") == "FULL", "NORM_FULL_AGGREGATE_PROVENANCE")
    return {"fullRunReceiptSha256": payload_hashes["receipt.json"],
            "fullAggregateSha256": payload_hashes["confirmation-aggregate.private.json"],
            "fullRunFileHashes": payload_hashes,
            **auth["privatehashes"]}


def validate_frames(full_bytes, psp_bytes):
    """Only fixed CSV fields; positive original WR frame, paired row order."""
    rows = list(csv.reader(io.StringIO(full_bytes.decode("utf-8"), newline="")))
    psp = list(csv.reader(io.StringIO(psp_bytes.decode("utf-8"), newline="")))
    header = ["stratum", "psu", "weight", *access.ITEM_IDS]
    rt.require(rows and rows[0] == header and len(rows) > 1 and psp and psp[0] == ["pspwght"] and
               len(rows) == len(psp), "NORM_FRAME_HEADER_OR_LENGTH")
    columns = {name: [] for name in header}; weights = []; units = {}; strata = set()
    categories = (5, 5, 5, 4, 4, 4, 11, 11, 11)
    for row, alternative in zip(rows[1:], psp[1:], strict=True):
        rt.require(len(row) == len(header) and len(alternative) == 1, "NORM_FRAME_ROW_WIDTH")
        h, unit = access.access.integer(row[0]), access.access.integer(row[1])
        rt.require(abs(h) <= 2**53 and abs(unit) <= 2**53 and
                   (unit not in units or units[unit] == h), "NORM_FRAME_DESIGN")
        strata.add(h); units[unit] = h
        values = [h, unit, access.access.positive_weight(row[2])]
        for token, k in zip(row[3:], categories, strict=True):
            value = None if token in ("NA", "") else access.access.integer(token)
            rt.require(value is None or 0 <= value < k, "NORM_FRAME_CATEGORY")
            values.append(value)
        for name, value in zip(header, values, strict=True): columns[name].append(value)
        weights.append(access.access.positive_weight(alternative[0]))
    rt.require(len(strata) == 25 and len(units) == 500 and
               all(sum(v == h for v in units.values()) >= 2 for h in strata), "NORM_ORIGINAL_FULL_FRAME")
    rt.require(all(math.isfinite(x) for x in (*columns["weight"], *weights)), "NORM_FRAME_WEIGHT")
    return columns, weights


def snapshot_private(root, public, runtime_pins):
    """Read original byte snapshots once, after all public+existing private guards."""
    folder = root / FULL_RUN
    rt.require(folder.is_dir() and folder.stat().st_mode & 0o777 == 0o700, "NORM_FULL_RUN_FOLDER")
    frozen = {}
    def read(relative):
        payload = rt.regular_path(root, relative, private=True).read_bytes()
        frozen[relative] = payload
        return payload
    record = json_bytes(read(FULL_RUN_RECEIPT))
    inventory = record.get("filesBeforeFinalReceipt", {})
    names = ["confirmation-aggregate.private.json", "runtime.json", "confirmation-entry.R", "authorization.json",
             *("source-snapshot/" + p for p in cr.CODE_PRIVATE)]
    run_payload = {name: read(FULL_RUN + "/" + name) for name in names}
    hashes = {name: sha(data) for name, data in run_payload.items()}
    hashes["receipt.json"] = sha(frozen[FULL_RUN_RECEIPT])
    for name, data in run_payload.items():
        rt.require(inventory.get(name, {}).get("bytes") == len(data), "NORM_FULL_RUN_FILE_SIZE")
    aggregate, probe = json_bytes(run_payload[names[0]]), json_bytes(run_payload["runtime.json"])
    rt.require(json_bytes(run_payload["authorization.json"]) == public["fullAuthorization"]["authorization"],
               "NORM_FULL_AUTH_FILE")
    provenance = validate_full_provenance(record, aggregate, public, runtime_pins, hashes, probe)
    full_bytes, psp_bytes = read(access.FULL_INPUT), read(access.SENSITIVITY)
    rt.require(sha(full_bytes) == provenance["fullSha256"] and sha(psp_bytes) == provenance["sensitivitySha256"],
               "NORM_FRAME_BYTES_PIN")
    columns, pspwght = validate_frames(full_bytes, psp_bytes)
    rt.require(aggregate.get("counts", {}).get("n_design") == len(pspwght) and
               aggregate.get("counts", {}).get("n_complete") == sum(all(columns[item][i] is not None for item in access.ITEM_IDS)
                   for i in range(len(pspwght))) and
               aggregate.get("counts", {}).get("psus") == 500 and aggregate.get("counts", {}).get("strata") == 25,
               "NORM_FULL_COUNTS")
    authorization = {"schema": "r-norm-runtime-auth-v1", "decision": "ACCEPTED_BOUNDED", "arm": "FULL",
        "wrapper_verified": True, "normGateSha256": public["normGateSha256"],
        "freeze_sha256": public["fullAuthorization"]["modelSha256"],
        "full_public_sha256": public["bindings"]["artifactSha256"][FULL_RESULT],
        "codeHashes": public["codeHashes"]}
    body = {"authorization": authorization, "frame": columns, "pspwght": pspwght, "full_aggregate": aggregate}
    transport = json.dumps(body, allow_nan=False, separators=(",", ":"))
    return transport, {**provenance, "transportSha256": sha(transport.encode()),
                       "sourceSha256": access.SHA, "normGateSha256": public["normGateSha256"]}


def execute_input(command, env, own, payload, timeout=600):
    """Memory-only stdin transport; no extra private row file or arbitrary entry."""
    fd = os.open(own / "stage.log", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "w") as log:
        try:
            return subprocess.run(command, env=env, cwd=own, input=payload, text=True,
                stdout=log, stderr=subprocess.STDOUT, close_fds=True, timeout=timeout).returncode
        except subprocess.TimeoutExpired:
            return 124


def validate_norm_output(value, full):
    """Receipt success needs an actual private aggregate; no public export rule."""
    keys = {"schema", "scope", "model_name", "retained_scores", "source_code_pins", "counts",
            "raw_mean_covariance", "scores", "limits"}
    rt.require(set(value) == keys and value["schema"] == "life93-full-norms-aggregate-1" and
               value["model_name"] == full["model_name"] and
               value["retained_scores"] == full["confirmation"]["retained_scores"] and
               value["source_code_pins"] == full["source_code_pins"] and
               set(value["scores"]) == set(value["retained_scores"]), "NORM_OUTPUT_CONTRACT")
    expected_counts = {"n_original": "n_design", "n_complete": "n_complete", "original_psus": "psus",
                       "original_strata": "strata", "original_design_df": "design_df", "zero_complete_psus": "zero_psus"}
    rt.require(all(value["counts"].get(k) == full["counts"].get(v) for k, v in expected_counts.items()),
               "NORM_OUTPUT_FRAME_COUNTS")
    # The separate publication schema/license package remains the export guard.
    return value


def run(arm, label, root=ROOT):
    rt.require(arm in ("synthetic", "FULL"), "NORM_ARM")
    rt.require(isinstance(label, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", label), "LABEL")
    os.umask(0o077); private = arm == "FULL"
    public = checked_preflight(root) if private else None
    hashes = rt.code_hashes(root, CODE)
    rt.require(all(hashes[path] == value for path, value in FROZEN_PINS.items()), "NORM_FROZEN_CODE_PIN")
    if private:
        rt.require(hashes == public["codeHashes"], "NORM_CODE_DRIFT_BEFORE_SNAPSHOT")
    runtime_pins = rt.validate_runtime(root)
    transport, provenance = snapshot_private(root, public, runtime_pins) if private else ("", None)
    own = rt.make_output(root, label, private)
    snapshots = rt.source_snapshots(root, own, hashes); env = rt.scoped_environment(root, own)
    entry = rt.regular_path(root, ENTRY); entry_sha = rt.digest(entry)
    probe = own / "runtime-probe.R"; rt.exclusive_text(probe, rt.runtime_probe(root, own))
    probe_command = rt.child_command(root, own, probe, [str(root), str(own), env["HOME"]])
    command = rt.child_command(root, own, entry, [str(root), str(own), env["HOME"], label, arm])
    record = {"schema": "r-norm-runtime-run-v1", "stage": arm, "label": label, "startedAtUtc": rt.utc(),
        "scope": "fixed private FULL norms" if private else "invented synthetic responses only; no empirical acceptance",
        "codeHashes": hashes, "sourceSnapshots": snapshots, "entrySha256": entry_sha,
        "runtimePins": runtime_pins, "privateAuthorization": public, "privateInputBindings": provenance,
        "command": command, "runtimeProbeCommand": probe_command, "pythonVersion": sys.version.split()[0],
        "homeUnchanged": env["HOME"] == os.environ["HOME"], "noCondaCall": True,
        "childHandledWriteRights": rt.RIGHTS.split(","), "childAllowRules": [str(own), "/dev/null:write-file"],
        "limits": rt.LIMITS, "receiptTrustLimit": "Mutable shared-FS coordinator receipts; no atomicity/unforgeability",
        "noAutomaticPublicCopy": True, "noCaseFile": True, "noRDS": True}
    rt.save_json(own / "start.json", record)
    try:
        record["runtimeProbeExitCode"] = rt.execute(probe_command, env, own, "runtime-probe.log", 60)
        if record["runtimeProbeExitCode"] != 0:
            record["exitCode"] = record["runtimeProbeExitCode"]
        else:
            rt.require(rt.digest(entry) == entry_sha and rt.code_hashes(root, CODE) == hashes, "NORM_CODE_DRIFT_BEFORE_R")
            rt.require(rt.validate_runtime(root) == runtime_pins, "NORM_RUNTIME_DRIFT_BEFORE_R")
            if private:
                rt.require(checked_preflight(root) == public, "NORM_PREFLIGHT_DRIFT_BEFORE_R")
            record["exitCode"] = execute_input(command, env, own, transport)
            if private and record["exitCode"] == 0:
                rt.require((own / "stage.log").read_text() == "ESS_NORMS_FULL_EXECUTED_PRIVATE_OUTPUT\n", "NORM_STAGE_SUCCESS_TOKEN")
                output = rt.regular_path(root, str((own / "norms-aggregate.private.json").relative_to(root)), private=True)
                output_bytes = output.read_bytes()
                validate_norm_output(json_bytes(output_bytes), public["fullPublic"])
                record["normAggregateSha256"] = sha(output_bytes)
        record["runtimePinsAfter"] = rt.validate_runtime(root)
        rt.require(record["runtimePinsAfter"] == runtime_pins, "NORM_RUNTIME_DRIFT")
        rt.require(rt.digest(entry) == entry_sha and rt.code_hashes(root, CODE) == hashes, "NORM_CODE_DRIFT")
        if private:
            rt.require(checked_preflight(root) == public, "NORM_INPUT_OR_GATE_DRIFT")
            # Rehash fixed historical run files; no new private row interpretation.
            rt.require(all(rt.digest(rt.regular_path(root, FULL_RUN + "/" + name, private=True)) == expected
                for name, expected in provenance["fullRunFileHashes"].items()), "NORM_FULL_RUN_DRIFT")
    except rt.RuntimeErrorCode as error:
        record["exitCode"] = 2; record["failureCode"] = "NORM_RUNTIME_" + str(error)
    except Exception:
        record["exitCode"] = 2; record["failureCode"] = "NORM_RUNTIME_STAGE_OR_RECEIPT_ERROR"
    record["endedAtUtc"] = rt.utc()
    try: record["filesBeforeFinalReceipt"] = rt.file_inventory(own)
    except Exception:
        record["exitCode"] = 2; record["failureCode"] = "NORM_RUNTIME_OUTPUT_METADATA_ERROR"
    rt.save_json(own / "receipt.json", record)
    print(("NORM_RUNTIME_PRIVATE_COMPLETED" if record['exitCode'] == 0 else "NORM_RUNTIME_PRIVATE_FAILED")
          if private else f"{label} exitCode {record['exitCode']}")
    return record["exitCode"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arm", choices=("synthetic", "FULL")); parser.add_argument("--label", required=True)
    args = parser.parse_args()
    try: return run(args.arm, args.label)
    except Exception:
        print("NORM_RUNTIME_INPUT_OR_GATE_ERROR", file=sys.stderr); return 2


if __name__ == "__main__":
    sys.exit(main())
