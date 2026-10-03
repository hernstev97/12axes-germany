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
from pipeline import r_runtime as runtime

ROOT = Path(__file__).resolve().parents[1]
TOP = frozenset("schema scope config source_code_pins counts point_moments efa models selection limits".split())
FIELDS = frozenset("""
alignment_max_difference all_candidate_factor_pairs alpha bread_method categories
cfi.scaled chisq chisq.scaled config contributing_complete_psus converged correlation
correlation_family correlation_lower_exclusive correlation_upper_exclusive correlations
counts covariance_with_score criteria critical delta_rank design_df design_se df df.scaled
diagnostics dominance_family dominance_upper_max efa efa_factors eligible epsilon
error_variance estimate estimating_score_max estimator expected_mapping
expected_mapping_passed factors failures family fit free_parameters input_columns
item_covariance item_largest_positive item_missing_counts items jacobian_step jsonlite
label labels lavaan level limits loading_family loading_lower_exclusive loadings lower
main manifest max_difference mean method metric minimum_absolute_loading_gap
minimum_dimensions minimum_scores model model_components model_criteria model_dominance
models moment_count moments n_complete n_design n_excluded native_point_max_difference
near_zero_rms numerical_tie_tolerance oblimin observed_expected_bread_max_difference
observed_variance other_intervals passed pbivnorm permutation point_estimator point_metric
point_moments postcheck psus pvalue pvalue.scaled raw_components raw_dominance reliability
reliability_lower_exclusive repeat_alignment repeat_seed repeated reproduced rms
rms_interval rms_one_sided_upper_max rmsea.scaled rotation rotation_se rstarts rule runs
runtime sandwich schema scope scores seed selection selection_order sensitivity sign
solution source_code_pins source_pins srmr standardized_parameters standardized_points
status strata thresholds tli.scaled true_variance upper values variance weighted_missing_mass
zero_psus code reason mapping_failure R
""".split())
ITEMS = ("B34", "B35", "B36", "B40", "B41", "B42", "B43", "B44", "B45")
DOMAINS = frozenset((*ITEMS, "ALL", "H", "Z", "F", "ZF", "M1", "M2", "M3", "1", "2", "3"))
PIN_KEYS = frozenset(runtime.CODE_DEVELOPMENT)
PARAMETER = re.compile(r"(?:ALL|H|Z|F|ZF)(?:=~B(?:34|35|36|40|41|42|43|44|45)|~~(?:H|Z|F|ZF))")


def require(condition, code):
    if not condition:
        raise ValueError(code)


def validate(value):
    require(isinstance(value, dict) and set(value) == TOP, "TOP_FIELDS")
    require(value["schema"] == "life93-A-development-aggregate-1", "A_SCHEMA")
    require(value["point_moments"]["items"] == list(ITEMS), "MOMENT_ITEMS")
    require(len(value["point_moments"]["thresholds"]) == 51 and
            len(value["point_moments"]["labels"]) == 87, "MOMENT_LENGTH")
    corr = value["point_moments"]["correlation"]
    require(len(corr) == 9 and all(isinstance(row, list) and len(row) == 9 for row in corr), "MOMENT_MATRIX")
    require(set(value["models"]) == {"M1", "M2", "M3"}, "MODEL_SET")
    require(set(value["counts"]["item_missing_counts"]) == set(ITEMS), "MISSING_SET")

    def walk(node, depth=0):
        require(depth <= 15, "DEPTH")
        if isinstance(node, dict):
            for key, child in node.items():
                require(key in FIELDS or key in DOMAINS or key in PIN_KEYS or
                        PARAMETER.fullmatch(key), "UNLISTED_FIELD")
                if key in ("psus", "strata", "zero_psus", "contributing_complete_psus"):
                    require(isinstance(child, int) and not isinstance(child, bool), "DESIGN_COUNT_ONLY")
                walk(child, depth + 1)
        elif isinstance(node, list):
            require(len(node) <= 87, "ARRAY_LENGTH")
            for child in node:
                walk(child, depth + 1)
        elif isinstance(node, str):
            require(len(node) <= 600 and not re.search(
                r"(?:data/(?:raw|local)/|BEGIN .*PRIVATE KEY|gh[pousr]_[A-Za-z0-9]{20}|sk-[A-Za-z0-9]{20})", node), "STRING_BOUNDARY")
        elif isinstance(node, (int, float)) and not isinstance(node, bool):
            require(math.isfinite(node), "NONFINITE")
        else:
            require(node is None or isinstance(node, bool), "VALUE_TYPE")
    walk(value)
    return value


def export_a(label, root=ROOT):
    require(bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", label)), "LABEL")
    authorization = runtime.preflight_private(root)
    folder = root / runtime.PRIVATE_ROOT / "runtime-runs" / label
    require(folder.is_dir() and not folder.is_symlink() and folder.resolve() == folder,
            "PRIVATE_RUN_PATH")
    receipt_path = runtime.regular_path(root, str((folder / "receipt.json").relative_to(root)), private=True)
    receipt = json.loads(receipt_path.read_text())
    require(receipt.get("stage") == "development-a" and receipt.get("exitCode") == 0 and
            receipt.get("runtimeProbeExitCode") == 0 and receipt.get("label") == label and
            receipt.get("privateAuthorization") == authorization and
            receipt.get("codeHashes") == runtime.code_hashes(root, runtime.CODE_DEVELOPMENT), "ACTUAL_A_RUN")
    path = runtime.regular_path(root, str((folder / "development-aggregate.private.json").relative_to(root)), private=True)
    expected = receipt["filesBeforeFinalReceipt"][str(path.relative_to(folder))]["sha256"]
    require(runtime.digest(path) == expected, "AGGREGATE_PIN")
    aggregate = validate(json.loads(path.read_text()))
    require(all(aggregate["source_code_pins"].get(k) == receipt["codeHashes"][k]
                for k in aggregate["source_code_pins"]), "AGGREGATE_CODE_PINS")
    contract = json.loads((root / "reports/loop/aggregate-publication-contract.json").read_text())
    aggregate["attribution"] = {**contract["source"], "changes": contract["changes"],
        "scope": "A exploratory development, conditional complete-case results; no empirical approval, B confirmation, ESS endorsement or release acceptance"}
    require(runtime.preflight_private(root) == authorization, "PREFLIGHT_DRIFT")
    destination = root / "reports/phasen/01-a-entwicklung.json"
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
