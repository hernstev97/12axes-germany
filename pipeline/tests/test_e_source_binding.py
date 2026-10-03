"""Regressions for real E-v2 reviewer bypasses, using public annotation only."""

import copy
import json
import unittest
from pathlib import Path

from pipeline.annotations.e_source_binding_v3 import validate_bound_contexts


BASE = json.loads((Path(__file__).resolve().parents[2] /
                   "data/inventar-e.v2.ergaenzung.entwurf.json").read_text())


def question(obj, qid):
    return next(q for q in obj["fragen"] if q["frage_id"] == qid)


def context(obj, qid, ref):
    return next(c for c in question(obj, qid)["kontext"] if ref in c["text"]["belege"])


class SourceBindingRegressions(unittest.TestCase):
    def test_reviewed_base_and_administrative_status(self):
        self.assertEqual(validate_bound_contexts(BASE)["identities"], 32)
        obj = copy.deepcopy(BASE)
        obj["fragen"][0]["kontext"][0]["text"]["status"] = "review status changed"
        validate_bound_contexts(obj)

    def test_removed_filter_hidden_in_secondary_reference(self):
        obj = copy.deepcopy(BASE)
        question(obj, "E8W")["kontext"].remove(context(obj, "E8W", "QCTX-E8W-filter"))
        context(obj, "E8W", "QCTX-E-intro")["text"]["belege"].append("QCTX-E8W-filter")
        with self.assertRaises(ValueError):
            validate_bound_contexts(obj)

    def test_filter_evidence_coherently_retargeted(self):
        obj = copy.deepcopy(BASE)
        ref = "QCTX-E8W-filter"
        evidence = copy.deepcopy(obj["belegregister"]["QCTX-E8M-filter"])
        evidence["evidence_id"] = ref
        obj["belegregister"][ref] = evidence
        context(obj, "E8W", ref)["text"]["wert"] = evidence["originalextrakt"]
        with self.assertRaises(ValueError):
            validate_bound_contexts(obj)

    def test_type_origin_and_conflicting_filter(self):
        for change in ("type", "origin", "extra"):
            with self.subTest(change=change):
                obj = copy.deepcopy(BASE)
                if change == "type":
                    context(obj, "E8W", "QCTX-E8W-filter")["typ"] = "einleitung"
                elif change == "origin":
                    context(obj, "E10M", "QCTX-E9M-E11M-filter")["herkunft"] = "direkt"
                else:
                    question(obj, "E8W")["kontext"].append(
                        copy.deepcopy(context(obj, "E8M", "QCTX-E8M-filter")))
                with self.assertRaises(ValueError):
                    validate_bound_contexts(obj)

    def test_visible_value_kept_but_original_page_wrong(self):
        obj = copy.deepcopy(BASE)
        question(obj, "E19")["listenheft"]["sichtbare_kategorien_de"]["belege"] = ["SC-L67-page"]
        with self.assertRaises(ValueError):
            validate_bound_contexts(obj)


if __name__ == "__main__":
    unittest.main()
