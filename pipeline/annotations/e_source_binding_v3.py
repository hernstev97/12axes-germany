"""Regression guard for the source-reviewed E-v2 annotation.

This is a fixed-document contract, not a general semantic validator. The
historical v2 geometry/source checks remain necessary. It preserves complete
context objects and their original evidence positions, including origin/type,
and binds visible cards to the reviewed page. No CAPI or scientific approval.
"""

import hashlib
import json
from pathlib import Path


ANNOTATION_SHA256 = "0c031abd7be58e14c91360db4e2a438b0b211e1116dd2f1b84ebab612931f6de"
CONTRACT_SHA256 = "7d894a7461b330332dcdfc3c1114b733c10dde3292b104f19b44f4b3676e27f5"


def canonical_hash(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def content_projection(value):
    """Administrative review status is not an original context attribute."""
    if isinstance(value, dict):
        return {k: content_projection(v) for k, v in value.items() if k != "status"}
    if isinstance(value, list):
        return [content_projection(v) for v in value]
    return value


def make_contract(annotation):
    """Extract binding hashes; the CLI enforces the reviewed input byte pin."""
    items = {}
    evidence_ids = set()
    for question in annotation["fragen"]:
        contexts = question["kontext"]
        for context in contexts:
            evidence_ids.update(context["text"]["belege"])
        card = question["listenheft"]
        evidence_ids.update(card["sichtbare_kategorien_de"]["belege"])
        evidence_ids.add(card["vollstaendige_seite_beleg"])
        items[question["frage_id"]] = {
            "contextsSha256": canonical_hash(content_projection(contexts)),
            "cardNumber": card["nummer"],
            "cardPdfPage": card["pdf_seite"],
            "visibleEvidence": card["sichtbare_kategorien_de"]["belege"],
            "pageEvidence": card["vollstaendige_seite_beleg"],
        }
    return {
        "schemaVersion": 1,
        "baseAnnotationSha256": ANNOTATION_SHA256,
        "identities": [q["frage_id"] for q in annotation["fragen"]],
        "scope": "Fixed reviewed E-v2 contexts, origin/type/applicability and original evidence positions; visible card references. No general semantic/CAPI/empirical claim.",
        "items": items,
        "evidenceSha256": {
            key: canonical_hash(annotation["belegregister"][key])
            for key in sorted(evidence_ids)
        },
    }


def validate_bound_contexts(annotation):
    contract = json.loads(Path(__file__).with_name("e_source_bindings_v3.json").read_text())
    if canonical_hash(contract) != CONTRACT_SHA256:
        raise ValueError("E-v3: binding contract pin mismatch")
    questions = annotation["fragen"]
    if [q["frage_id"] for q in questions] != contract["identities"]:
        raise ValueError("E-v3: question identities or order changed")
    for key, expected in contract["evidenceSha256"].items():
        if canonical_hash(annotation["belegregister"].get(key)) != expected:
            raise ValueError("E-v3: reviewed original evidence changed: " + key)
    for question in questions:
        qid = question["frage_id"]
        expected = contract["items"][qid]
        if canonical_hash(content_projection(question["kontext"])) != expected["contextsSha256"]:
            raise ValueError(qid + ": reviewed context/text/type/origin/applicability binding changed")
        card = question["listenheft"]
        if (
            card["nummer"] != expected["cardNumber"]
            or card["pdf_seite"] != expected["cardPdfPage"]
            or card["sichtbare_kategorien_de"]["belege"] != expected["visibleEvidence"]
            or card["vollstaendige_seite_beleg"] != expected["pageEvidence"]
        ):
            raise ValueError(qid + ": visible card evidence is not the reviewed original page")
    return {"identities": len(questions), "status": "REVIEWED_DOCUMENT_REGRESSION_GUARD_ONLY"}


def validate_semantics(annotation, pages):
    """Combine the historical geometry checks with the new binding guard.

    As in v2, callers must verify the original PDF pins and extract pages from
    those bytes. This function cannot establish the provenance of pages alone.
    """
    from .e_semantic_contract_v2 import validate_semantics as validate_v2

    validate_bound_contexts(annotation)
    return validate_v2(annotation, pages)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", type=Path)
    parser.add_argument("--annotation", type=Path,
                        default=Path(__file__).resolve().parents[2] / "data/inventar-e.v2.ergaenzung.entwurf.json")
    args = parser.parse_args()
    data = args.annotation.read_bytes()
    if hashlib.sha256(data).hexdigest() != ANNOTATION_SHA256:
        raise ValueError("Generation requires the byte-pinned reviewed annotation")
    obj = json.loads(data)
    if args.generate:
        value = make_contract(obj)
        args.generate.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        print(canonical_hash(value))
    else:
        print(json.dumps(validate_bound_contexts(obj)))
