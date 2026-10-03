"""Agreement of fixed independent document judgments, never ESS responses."""

from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

CATEGORIES = ("JA", "NEIN", "UNKLAR")
PINS = {
    "sources": "efeed8790f2c0ee34b21ab1b087d812e8971e4fcb967b80ee1d4bf8adf9eeb56",
    "methods": "c5a0be5ffffbe65bafca137f882514e4a2a89c43bbb52b83031da890d67c6921",
}


def agreement(left: list[str], right: list[str]) -> dict:
    if not left or len(left) != len(right) or any(x not in CATEGORIES for x in left + right):
        raise ValueError("Nonempty aligned judgments in fixed categories required")
    n = len(left)
    table = {a: {b: 0 for b in CATEGORIES} for a in CATEGORIES}
    for a, b in zip(left, right, strict=True):
        table[a][b] += 1
    same = sum(table[c][c] for c in CATEGORIES)
    a, b = Counter(left), Counter(right)
    expected_count_product = sum(a[c] * b[c] for c in CATEGORIES)
    denominator = n * n - expected_count_product
    return {
        "nIdentities": n,
        "table": table,
        "same": same,
        "observedAgreement": same / n,
        "expectedAgreement": expected_count_product / (n * n),
        "cohensKappa": (n * same - expected_count_product) / denominator if denominator else None,
        "undefinedReason": "Degenerate identical marginal category" if not denominator else None,
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    judgments = {}
    for reviewer, pin in PINS.items():
        path = root / f"reports/loop/reviews/ITEM-FIRST-001-{reviewer}.csv"
        if hashlib.sha256(path.read_bytes()).hexdigest() != pin:
            raise ValueError("Initial judgment changed")
        with path.open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        if len(rows) != 296 or len({r["inventar_id"] for r in rows}) != 296:
            raise ValueError("296 distinct initial identities required")
        judgments[reviewer] = rows
    left, right = judgments["sources"], judgments["methods"]
    if [r["inventar_id"] for r in left] != [r["inventar_id"] for r in right]:
        raise ValueError("Identity order differs")
    dissent = []
    for a, b in zip(left, right, strict=True):
        if a["eignung"] != b["eignung"]:
            dissent.append({
                "id": a["inventar_id"],
                "sources": {k: a[k] for k in ("eignung", "begruendung", "fundstelle")},
                "methods": {k: b[k] for k in ("eignung", "begruendung", "fundstelle")},
            })
    potential = [(a, b) for a, b in zip(left, right, strict=True)
                 if a["eignung"] != "NEIN" or b["eignung"] != "NEIN"]
    result = {
        "kind": "DOCUMENT_JUDGMENT_AGREEMENT; no respondent data or validity result",
        "initialCsvPins": PINS,
        "all296": agreement([r["eignung"] for r in left], [r["eignung"] for r in right]),
        "potentialAttitudeSubset": {
            "selection": "Supplementary, union of non-NEIN first judgments; conditional on judgments, not an independent accuracy sample",
            **agreement([a["eignung"] for a, _ in potential], [b["eignung"] for _, b in potential]),
        },
        "dissent": dissent,
        "sameNumericalDirectionCategory": sum(a["ordnungsrichtung"] == b["ordnungsrichtung"]
                                             for a, b in zip(left, right, strict=True)),
        "limits": [
            "Same Codex model family; shared errors possible; no correctness/neutrality/validity proof",
            "Administrative identities and parallel gender/PVQ versions affect margins and repeated content",
            "Equal numerical direction categories alone do not establish equal semantic poles",
        ],
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    target = root / "reports/loop/ITEM-FIRST-001-agreement.json"
    if target.exists():
        if json.loads(target.read_text()) != result:
            raise ValueError("No overwrite of differing agreement report")
    else:
        target.write_text(payload)
    print(json.dumps({"all296": result["all296"], "dissentIds": [r["id"] for r in dissent]}))


if __name__ == "__main__":
    main()
