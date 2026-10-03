#!/usr/bin/env python3
"""Pinned B/FULL execution and a separate reproducible invented-input probe.

No public aggregate copy, arbitrary entry/input path, gate bypass or installer.
The twelve Landlock child write rights are reused from the frozen A runtime.
They do not isolate reads, network, devices, supervisors or other shared-FS agents.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
if __package__ in (None, ""):
    sys.path.insert(0, str(ROOT))
from pipeline import r_runtime as rt
from pipeline import stage_access as access

CONFIRM = "pipeline/ordinal/confirm.R"
ENTRY = "pipeline/ordinal/reproduce-confirm.R"
CODE_PRIVATE = tuple(dict.fromkeys((*rt.CODE_DEVELOPMENT, "pipeline/stage_access.py",
                                   "pipeline/confirm_runtime.py", CONFIRM)))
CODE_SYNTHETIC = (*CODE_PRIVATE, ENTRY)
FROZEN_PINS = {
    "pipeline/r_runtime.py": "40168392ac69960d2b532f721aaaca4abc82317f8304f7145056537d8a901fce",
    "pipeline/ordinal/develop.R": "d1b725b05ba43d9a3edbe4964e05ae0d5365ef951944fe1c83284967ff800e74",
    "pipeline/ordinal/develop-config.R": "44a74f0e59645d047f2bdc4508cc0058d0dd80ffb4a67a8963ee9e84f0f429b0",
    "pipeline/ordinal/adapter_v2.R": "8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b",
    "pipeline/ordinal/support.R": "b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22",
    CONFIRM: "e7c8d04d8010c456c5db6d9902353a37786737b201cf9a160d082f40a84bddad",
}


def checked_preflight(root, arm):
    """Required wrapper code pins are checked publicly before private helpers."""
    rt.require(arm in ("B", "FULL"), "ARM")
    public = access.public_preflight(root, arm)
    reviewed = public.get("codeSha256", {})
    rt.require(isinstance(reviewed, dict) and set(CODE_PRIVATE).issubset(reviewed),
               "CONFIRM_REVIEWED_CODE_SET")
    hashes = rt.code_hashes(root, CODE_PRIVATE)
    rt.require(all(reviewed[path] == hashes[path] for path in CODE_PRIVATE),
               "CONFIRM_REVIEWED_CODE_PIN")
    rt.require(all(hashes[path] == value for path, value in FROZEN_PINS.items()), "FROZEN_CODE_PIN")
    # The standard stage checker repeats its public checks before private reads.
    # Coordinator receipts remain mutable; this is not an atomic FS transaction.
    result = (access.preflight_confirmation(root) if arm == "B" else access.preflight_full(root))
    rt.require(all(result.get(key) == public.get(key) for key in
                   ("gateSha256", "modelSha256", "sourceSha256", "codeSha256", "authorization")),
               "CONFIRM_PREFLIGHT_DRIFT")
    return result


def private_entry():
    return """args <- commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==6L,identical(Sys.getenv('HOME'),args[[3]]))
project <- normalizePath(args[[1]],mustWork=TRUE)
own <- normalizePath(args[[2]],mustWork=TRUE)
stopifnot(identical(own,Sys.getenv('ESS_RUNTIME_OUTPUT')))
source(file.path(project,'pipeline/ordinal/confirm.R'))
authorization <- ec_quiet(jsonlite::fromJSON(args[[6]],simplifyVector=TRUE))
code <- ec_main(project,args[[4]],args[[5]],own,authorization)
quit(status=code)
"""


def check_entry_files(entry, entry_sha, authorization_path=None, authorization_sha=None):
    rt.require(rt.digest(entry) == entry_sha, "ENTRY_DRIFT")
    if authorization_path is not None:
        rt.require(rt.digest(authorization_path) == authorization_sha, "AUTHORIZATION_FILE_DRIFT")


def run(arm, label, root=ROOT):
    rt.require(arm in ("synthetic", "B", "FULL"), "ARM")
    rt.require(isinstance(label, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", label), "LABEL")
    private = arm != "synthetic"
    os.umask(0o077)
    authorization = checked_preflight(root, arm) if private else None
    paths = CODE_PRIVATE if private else CODE_SYNTHETIC
    hashes = rt.code_hashes(root, paths)
    rt.require(all(hashes[path] == value for path, value in FROZEN_PINS.items()), "FROZEN_CODE_PIN")
    if private:
        rt.require(all(authorization["codeSha256"][path] == hashes[path] for path in CODE_PRIVATE),
                   "CONFIRM_REVIEWED_CODE_PIN")
    runtime_pins = rt.validate_runtime(root)
    own = rt.make_output(root, label, private)
    snapshots = rt.source_snapshots(root, own, hashes)
    env = rt.scoped_environment(root, own)
    probe = own / "runtime-probe.R"
    rt.exclusive_text(probe, rt.runtime_probe(root, own))
    probe_command = rt.child_command(root, own, probe, [str(root), str(own), env["HOME"]])
    auth_path = auth_sha = None
    if private:
        entry = own / "confirmation-entry.R"
        rt.exclusive_text(entry, private_entry())
        auth_path = own / "authorization.json"
        rt.save_json(auth_path, authorization["authorization"])
        auth_sha = rt.digest(auth_path)
        input_path = access.B_INPUT if arm == "B" else access.FULL_INPUT
        arguments = [str(root), str(own), env["HOME"], str(root / input_path),
                     str(root / access.MODEL), str(auth_path)]
    else:
        entry = root / ENTRY
        arguments = [str(root), str(own), env["HOME"]]
    command = rt.child_command(root, own, entry, arguments)
    entry_sha = rt.digest(entry)
    record = {"schema": "r-confirm-runtime-run-v1", "stage": arm, "label": label,
              "startedAtUtc": rt.utc(), "scope": "fixed private " + arm if private else
                  "invented synthetic responses only; no empirical acceptance",
              "command": command, "runtimeProbeCommand": probe_command, "cwd": str(own),
              "codeHashes": hashes, "sourceSnapshots": snapshots, "pythonVersion": sys.version.split()[0],
              "entrySha256": entry_sha, "authorizationFileSha256": auth_sha,
              "runtimePins": runtime_pins, "privateAuthorization": authorization,
              "childHandledWriteRights": rt.RIGHTS.split(","),
              "childAllowRules": [str(own), "/dev/null:write-file"], "limits": rt.LIMITS,
              "receiptTrustLimit": "Mutable coordinator receipts and shared FS; concurrent races not excluded",
              "homeUnchanged": env["HOME"] == os.environ["HOME"], "noCondaCall": True,
              "noAutomaticPublicCopy": True, "noRDS": True,
              "environment": {key: env[key] for key in ("HOME", "PATH", "TZ", "LC_ALL", "OPENBLAS_NUM_THREADS",
                  "OMP_NUM_THREADS", "R_LIBS_USER", "R_LIBS_SITE", "TMPDIR", "XDG_CACHE_HOME", "XDG_DATA_HOME",
                  "XDG_CONFIG_HOME", "R_USER_CACHE_DIR", "R_HISTFILE", "R_PROFILE_USER", "R_ENVIRON_USER")}}
    rt.save_json(own / "start.json", record)
    try:
        record["runtimeProbeExitCode"] = rt.execute(probe_command, env, own, "runtime-probe.log", 60)
        if record["runtimeProbeExitCode"] != 0:
            record["exitCode"] = record["runtimeProbeExitCode"]
        else:
            check_entry_files(entry, entry_sha, auth_path, auth_sha)
            rt.require(rt.code_hashes(root, paths) == hashes, "CODE_DRIFT_BEFORE_R")
            rt.require(rt.validate_runtime(root) == runtime_pins, "RUNTIME_DRIFT_BEFORE_R")
            if private:
                rt.require(checked_preflight(root, arm) == authorization, "PRIVATE_PREFLIGHT_DRIFT")
            record["exitCode"] = rt.execute(command, env, own, "stage.log", 600)
        record["runtimePinsAfter"] = rt.validate_runtime(root)
        check_entry_files(entry, entry_sha, auth_path, auth_sha)
        rt.require(record["runtimePinsAfter"] == runtime_pins, "RUNTIME_DRIFT")
        rt.require(rt.code_hashes(root, paths) == hashes, "CODE_DRIFT")
        if private:
            rt.require(checked_preflight(root, arm) == authorization, "PRIVATE_INPUT_DRIFT")
    except rt.RuntimeErrorCode as error:
        record["exitCode"] = 2
        record["failureCode"] = "CONFIRM_RUNTIME_" + str(error)
    except Exception:
        record["exitCode"] = 2
        record["failureCode"] = "CONFIRM_RUNTIME_STAGE_OR_RECEIPT_ERROR"
    record["endedAtUtc"] = rt.utc()
    try:
        record["filesBeforeFinalReceipt"] = rt.file_inventory(own)
    except Exception:
        record["exitCode"] = 2
        record["failureCode"] = "CONFIRM_RUNTIME_OUTPUT_METADATA_ERROR"
    rt.save_json(own / "receipt.json", record)
    print("CONFIRM_RUNTIME_PRIVATE_COMPLETED" if private else f"{label} exitCode {record['exitCode']}")
    return record["exitCode"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arm", choices=("synthetic", "B", "FULL"))
    parser.add_argument("--label", required=True)
    args = parser.parse_args()
    try:
        return run(args.arm, args.label)
    except Exception:
        print("CONFIRM_RUNTIME_INPUT_OR_GATE_ERROR", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
