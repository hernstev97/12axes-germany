"""Metadata-only ESS input check. Never selects response or person-ID fields."""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import io
import os
from decimal import Decimal, InvalidOperation
import json
import math
from pathlib import Path

EXPECTED_SHA256 = "4b0bfa73fa86bcf9f868b0a6145f96504a40d7e3f2deeb3e822555993ab32dc8"
FIELDS = ("cntry", "essround", "edition", "proddate", "psu", "stratum", "anweight", "pspwght", "dweight")
GLOBAL_METADATA = ("essround", "edition", "proddate")


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def audit(path: Path, *, expected_digest: str = EXPECTED_SHA256) -> dict:
    frozen_bytes = path.read_bytes()
    if hashlib.sha256(frozen_bytes).hexdigest() != expected_digest:
        raise ValueError("Input digest differs; no import performed")
    errors: Counter[str] = Counter()
    metadata = {key: set() for key in GLOBAL_METADATA}
    cluster_sets: dict[str, set[str]] = {}
    global_psu_strata: dict[str, set[str]] = {}
    row_count = de_count = valid_design_count = 0
    ratios: list[float] = []
    # Immutable memory view is exactly the hashed bytestand, including with a symlinked source.
    with io.StringIO(frozen_bytes.decode("utf-8-sig"), newline="") as stream:
        reader = csv.reader(stream)
        header = next(reader)
        if len(header) != len(set(header)) or not set(FIELDS).issubset(header):
            raise ValueError("Nonunique header or missing required metadata fields")
        offsets = {key: header.index(key) for key in FIELDS}
        for record in reader:
            row_count += 1
            if len(record) != len(header):
                errors["malformedRowWidth"] += 1
                continue
            # CSV tokenization necessarily handles the raw record. Only this
            # nine-field positive list is interpreted; no political field is selected.
            values = {key: record[index] for key, index in offsets.items()}
            for key in GLOBAL_METADATA:
                metadata[key].add(values[key])
            if values["cntry"] != "DE":
                continue
            de_count += 1
            valid = True
            for key in ("psu", "stratum"):
                if not values[key] or values[key] in ("NA", "NaN", "."):
                    errors["missingDesignField"] += 1
                    valid = False
                else:
                    try:
                        number = Decimal(values[key])
                        if not number.is_finite() or number != number.to_integral_value() or number < 1:
                            raise ValueError()
                        values[key] = str(int(number))
                    except (ValueError, InvalidOperation):
                        errors["invalidDesignCode"] += 1
                        valid = False
            weights = {}
            for key in ("anweight", "pspwght", "dweight"):
                try:
                    weight = float(values[key])
                    if not math.isfinite(weight) or weight <= 0:
                        raise ValueError()
                    weights[key] = weight
                except ValueError:
                    errors["invalidWeight"] += 1
                    valid = False
            if not valid:
                continue
            valid_design_count += 1
            stratum, psu = values["stratum"], values["psu"]
            cluster_sets.setdefault(stratum, set()).add(psu)
            global_psu_strata.setdefault(psu, set()).add(stratum)
            ratios.append(weights["anweight"] / weights["pspwght"])
    if metadata != {"essround": {"11"}, "edition": {"4.2"}, "proddate": {"02.07.2026"}}:
        errors["globalVersionMismatch"] += 1
    if de_count == 0:
        errors["noGermanyRows"] += 1
    sizes = Counter(len(units) for units in cluster_sets.values())
    ratio_constant = bool(ratios) and max(ratios) - min(ratios) <= 1e-10 * max(abs(x) for x in ratios)
    return {
        "kind": "DESIGN_METADATA_ONLY",
        "inputSha256": expected_digest,
        "selectedFields": list(FIELDS),
        "rowCountAllCountries": row_count,
        "rowCountGermany": de_count,
        "validDesignRowsGermany": valid_design_count,
        "strataCount": len(cluster_sets),
        "psuCountNested": sum(len(units) for units in cluster_sets.values()),
        "psusPerStratumHistogram": {str(n): count for n, count in sorted(sizes.items())},
        "psuCodesOccurringInMultipleStrata": sum(len(v) > 1 for v in global_psu_strata.values()),
        "anweightToPspwghtConstantWithinTolerance1eMinus10": ratio_constant,
        "errors": dict(errors),
        "metadataUsable": not errors,
        "fourPsusPerStratumSplitFeasible": bool(sizes) and min(sizes) >= 4 and not errors,
        "scope": "No respondent identifiers, response values, A/B split or political distributions emitted. Integrated coding is not validated solely by finite numbers.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[1]
    expected_source = project / "data/raw/ess11-ed4.2/ESS11e04_2.csv"
    if args.source.absolute() != expected_source or not expected_source.is_file():
        raise ValueError("Only the fixed local raw input is permitted")
    out = args.out.absolute()
    local = project / "data/local"
    private_folder = local / "design-metadata-v2"
    # Validate all path components before creating any directories.
    if out.parent != private_folder or out.parent.resolve() != out.parent or out.is_symlink() or out.exists():
        raise ValueError("Only a fresh result in the fixed private metadata folder is permitted")
    if not local.is_dir() or local.resolve() != local:
        raise ValueError("Existing unsymlinked data/local required")
    if private_folder.exists() and (not private_folder.is_dir() or private_folder.stat().st_mode & 0o077):
        raise ValueError("Existing metadata folder must be owner-only")
    result = audit(expected_source)
    private_folder.mkdir(mode=0o700, exist_ok=True)
    descriptor = os.open(out, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(descriptor, "w") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print("Metadata audit saved privately. No response analysis performed.")
    if not result["metadataUsable"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
