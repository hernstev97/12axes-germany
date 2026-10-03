"""Validate a fixed development aggregate before the coordinator publishes it.

Only reviewed A runtime outputs are accepted by the CLI. This is an accidental
disclosure guard, not an adversarial proof or scientific/release acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import r_runtime as runtime
from pipeline.public_schema import validate_a

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PINS = frozenset((
    "pipeline/ordinal/develop.R", "pipeline/ordinal/develop-config.R",
    "pipeline/ordinal/adapter_v2.R", "pipeline/ordinal/support.R",
))


def require(condition, code):
    if not condition:
        raise ValueError(code)


def validate(value):
    return validate_a(value)


def export_a(label, root=ROOT):
    require(bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", label)), "LABEL")
    authorization = runtime.preflight_private(root)
    folder = root / runtime.PRIVATE_ROOT / "runtime-runs" / label
    require(folder.is_dir() and not folder.is_symlink() and folder.resolve() == folder,
            "PRIVATE_RUN_PATH")
    receipt_path = runtime.regular_path(root, str((folder / "receipt.json").relative_to(root)), private=True)
    receipt_bytes = receipt_path.read_bytes()
    receipt_sha = hashlib.sha256(receipt_bytes).hexdigest()
    receipt = json.loads(receipt_bytes)
    current_code = runtime.code_hashes(root, runtime.CODE_DEVELOPMENT)
    require(receipt.get("stage") == "development-a" and receipt.get("exitCode") == 0 and
            receipt.get("runtimeProbeExitCode") == 0 and receipt.get("label") == label and
            receipt.get("privateAuthorization") == authorization and
            receipt.get("codeHashes") == current_code, "ACTUAL_A_RUN")
    path = runtime.regular_path(root, str((folder / "development-aggregate.private.json").relative_to(root)), private=True)
    expected = receipt["filesBeforeFinalReceipt"][str(path.relative_to(folder))]["sha256"]
    require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected), "AGGREGATE_PIN")
    frozen = path.read_bytes()
    require(hashlib.sha256(frozen).hexdigest() == expected, "AGGREGATE_PIN")
    aggregate = validate(json.loads(frozen))
    require(set(aggregate["source_code_pins"]) == SOURCE_PINS and
            all(aggregate["source_code_pins"][k] == current_code[k] for k in SOURCE_PINS),
            "AGGREGATE_CODE_PINS")
    contract = json.loads((root / "reports/loop/aggregate-publication-contract.json").read_text())
    aggregate["attribution"] = {**contract["source"], "changes": contract["changes"],
        "scope": "A exploratory development, conditional complete-case results; no empirical approval, B confirmation, ESS endorsement or release acceptance"}
    require(runtime.preflight_private(root) == authorization, "PREFLIGHT_DRIFT")
    require(runtime.code_hashes(root, runtime.CODE_DEVELOPMENT) == current_code and
            runtime.digest(receipt_path) == receipt_sha and runtime.digest(path) == expected,
            "PRE_COPY_DRIFT")
    destination = root / "reports/phasen/01-a-entwicklung.json"
    require(destination.parent.is_dir() and destination.parent.resolve() == destination.parent,
            "PUBLIC_OUTPUT_PATH")
    require(not destination.exists() and not destination.is_symlink(), "DO_NOT_OVERWRITE")
    payload = json.dumps(aggregate, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    with os.fdopen(fd, "w") as stream:
        stream.write(payload)
    return hashlib.sha256(payload.encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("label")
    args = parser.parse_args()
    try:
        print("A aggregate saved; SHA256 " + export_a(args.label))
    except Exception:
        print("AGGREGATE_EXPORT_REJECTED", file=sys.stderr)
        raise SystemExit(2) from None


if __name__ == "__main__":
    main()
