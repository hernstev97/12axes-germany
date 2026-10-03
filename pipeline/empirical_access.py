"""Private, positively selected ESS development input. No automatic public export.

The gate is a coordinator receipt, not a tamper-proof sandbox. Never prints input
values, keys, rows, or arbitrary library exceptions. Synthetic imports may call
the pure functions; the CLI accepts only the fixed version and real public gate.
"""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import os
from pathlib import Path
import random
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ITEM_IDS = ("B34", "B35", "B36", "B40", "B41", "B42", "B43", "B44", "B45")
SHA = "4b0bfa73fa86bcf9f868b0a6145f96504a40d7e3f2deeb3e822555993ab32dc8"
METADATA = ("cntry", "essround", "edition", "proddate", "psu", "stratum", "anweight")
LEXICAL_MISSING = ("", "NA", "NaN", ".")


class AccessError(Exception):
    """Fixed diagnostic codes only."""


def require(condition: bool, code: str) -> None:
    if not condition:
        raise AccessError(code)


def integer(value: str) -> int:
    try:
        number = Decimal(value)
        require(number.is_finite() and number == number.to_integral_value(), "INTEGER_CODE")
        return int(number)
    except (InvalidOperation, ValueError):
        raise AccessError("INTEGER_CODE") from None


def positive_weight(value: str) -> float:
    import math
    try:
        number = float(value)
        require(math.isfinite(number) and number > 0, "WEIGHT")
        return number
    except ValueError:
        raise AccessError("WEIGHT") from None


def table(frozen: bytes, expected_sha: str):
    require(hashlib.sha256(frozen).hexdigest() == expected_sha, "INPUT_PIN")
    stream = io.StringIO(frozen.decode("utf-8-sig"), newline="")
    rows = csv.reader(stream)
    header = next(rows)
    require(len(header) == len(set(header)) and set(METADATA).issubset(header), "HEADER")
    return header, rows


def metadata(header: list[str], row: list[str]) -> dict:
    require(len(row) == len(header), "ROW_WIDTH")
    result = {key: row[header.index(key)] for key in METADATA}
    require((result["essround"], result["edition"], result["proddate"]) ==
            ("11", "4.2", "02.07.2026"), "VERSION")
    if result["cntry"] == "DE":
        for key in ("psu", "stratum"):
            result[key] = integer(result[key])
            require(result[key] > 0, "DESIGN_CODE")
        result["anweight"] = positive_weight(result["anweight"])
    return result


def assignment(frozen: bytes, expected_sha: str = SHA) -> dict:
    """Metadata only. Answer fields are never selected or parsed here."""
    header, rows = table(frozen, expected_sha)
    strata: dict[int, set[int]] = {}
    psu_strata: dict[int, int] = {}
    n = 0
    for row in rows:
        m = metadata(header, row)
        if m["cntry"] != "DE":
            continue
        n += 1
        h, p = m["stratum"], m["psu"]
        require(p not in psu_strata or psu_strata[p] == h, "PSU_NESTING")
        psu_strata[p] = h
        strata.setdefault(h, set()).add(p)
    require(n > 0 and all(len(v) >= 2 for v in strata.values()), "DESIGN_SUPPORT")
    generator = random.Random(2026100301)
    units = []
    for h in sorted(strata):
        psus = sorted(strata[h])
        total = len(psus)
        if total < 4:
            units.extend({"stratum": h, "psu": p, "arm": "C", "probability": None}
                         for p in psus)
            continue
        generator.shuffle(psus)
        n_a = total // 2
        for i, p in enumerate(psus):
            arm = "A" if i < n_a else "B"
            selected = n_a if arm == "A" else total - n_a
            units.append({"stratum": h, "psu": p, "arm": arm,
                          "probability": selected / total})
    return {"inputSha256": expected_sha, "seed": 2026100301, "countryRows": n,
            "units": units, "scope": "private metadata assignment, no responses or IDs"}


def validate_item_contract(contract: dict) -> list[dict]:
    items = contract["items"]
    require(tuple(i["id"] for i in items) == ITEM_IDS, "ITEM_IDENTITIES")
    require(len({i["variable"] for i in items}) == 9, "ITEM_FIELDS")
    for item in items:
        allowed = item["allowed_values"]
        require(isinstance(allowed, list) and len(allowed) >= 2 and
                all(isinstance(v, int) for v in allowed) and
                allowed == sorted(set(allowed)), "ITEM_CATEGORIES")
        require(set(map(str, allowed)) == set(item["scoring"]["map"]), "SCORING_KEYS")
        require(not set(allowed).intersection(item["integrated_file_missing_codes"]), "MISSING_OVERLAP")
        scores = [item["scoring"]["map"][str(v)] for v in allowed]
        expected = [j / (len(allowed) - 1) for j in range(len(allowed))]
        require(scores == expected or scores == list(reversed(expected)), "SCORING_MAP")
    return items


def development_frame(frozen: bytes, split: dict, contract: dict, expected_sha: str = SHA):
    """Only A responses are interpreted. B/C bytes are tokenized, never selected."""
    require(split["inputSha256"] == expected_sha and split["seed"] == 2026100301, "SPLIT_PIN")
    require(split == assignment(frozen, expected_sha), "SPLIT_REPRODUCTION")
    items = validate_item_contract(contract)
    header, rows = table(frozen, expected_sha)
    require(all(i["variable"] in header for i in items), "ITEM_HEADER")
    positions = [header.index(i["variable"]) for i in items]
    units = {(u["stratum"], u["psu"]): u for u in split["units"]}
    output = []
    for row in rows:
        m = metadata(header, row)
        if m["cntry"] != "DE":
            continue
        unit = units[(m["stratum"], m["psu"])]
        if unit["arm"] != "A":
            continue
        # This branch is the first and only selection of response fields.
        values = []
        for item, at in zip(items, positions, strict=True):
            token = row[at].strip()
            if token in LEXICAL_MISSING:
                values.append("NA")
                continue
            value = integer(token)
            if value in item["integrated_file_missing_codes"]:
                values.append("NA")
                continue
            require(value in item["allowed_values"], "UNEXPECTED_A_CATEGORY")
            order = item["allowed_values"].index(value)
            if item["scoring"]["map"][str(item["allowed_values"][0])] == 1:
                order = len(item["allowed_values"]) - 1 - order
            values.append(order)
        output.append([m["stratum"], m["psu"], m["anweight"] / unit["probability"], *values])
    return ["stratum", "psu", "weight", *ITEM_IDS], output


def gate(root: Path) -> dict:
    """Positive receipt and actual tag pins; does not parse prose to infer acceptance."""
    receipt = json.loads((root / "reports/loop/gates/pre-empirical.json").read_text())
    require(receipt["decision"] == "ACCEPTED_BOUNDED", "GATE_DECISION")
    reviews = receipt["reviews"]
    require(len(reviews) == 2 and len({r["reviewer"] for r in reviews}) == 2 and
            {r["scope"] for r in reviews} == {"methods-repro", "sources-construct-fairness"}, "REVIEW_ROLES")
    for entry in [*receipt["artifacts"], *reviews]:
        path = root / entry["path"]
        require(path.resolve().is_relative_to(root.resolve()) and path.is_file(), "GATE_PATH")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"], "GATE_PIN")
    for tag in ("analyseplan-v1", "erwartungsmodell-v1"):
        local = subprocess.run(["git", "rev-parse", f"refs/tags/{tag}^{{commit}}"], cwd=root,
                               capture_output=True, text=True, check=True).stdout.strip()
        remote = subprocess.run(["git", "ls-remote", "origin", f"refs/tags/{tag}"], cwd=root,
                                capture_output=True, text=True, check=True).stdout.split()
        require(len(remote) == 2 and remote[0] == local == receipt["tags"][tag], "PUBLIC_TAG_PIN")
    require(sys.version_info[:3] == (3, 14, 7), "PYTHON_VERSION")
    return receipt


def private_write(path: Path, payload: str) -> None:
    folder = ROOT / "data/local/empirical-v1"
    require(path.parent == folder and path.parent.resolve() == path.parent and
            not path.exists() and not path.is_symlink(), "PRIVATE_PATH")
    local = folder.parent
    require(local.is_dir() and local.resolve() == local and local.stat().st_mode & 0o077 == 0, "PRIVATE_PARENT")
    if folder.exists():
        require(folder.is_dir() and folder.stat().st_mode & 0o077 == 0, "PRIVATE_FOLDER")
    folder.mkdir(mode=0o700, exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "w") as stream:
        stream.write(payload)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("prepare", "A"))
    args = parser.parse_args()
    try:
        gate(ROOT)
        source = ROOT / "data/raw/ess11-ed4.2/ESS11e04_2.csv"
        frozen = source.read_bytes()
        folder = ROOT / "data/local/empirical-v1"
        if args.command == "prepare":
            split = assignment(frozen)
            private_write(folder / "assignment.json", json.dumps(split, indent=2) + "\n")
        else:
            split = json.loads((folder / "assignment.json").read_text())
            contract = json.loads((ROOT / "data/item-core-v1.json").read_text())
            header, rows = development_frame(frozen, split, contract)
            buffer = io.StringIO(newline="")
            writer = csv.writer(buffer)
            writer.writerow(header)
            writer.writerows(rows)
            private_write(folder / "A.csv", buffer.getvalue())
        print("Private stage saved. No rows, keys or answer values emitted.")
    except AccessError as error:
        print("EMPIRICAL_ACCESS_" + str(error), file=sys.stderr)
        raise SystemExit(2) from None
    except Exception:
        print("EMPIRICAL_ACCESS_INPUT_OR_GATE_ERROR", file=sys.stderr)
        raise SystemExit(2) from None


if __name__ == "__main__":
    main()
