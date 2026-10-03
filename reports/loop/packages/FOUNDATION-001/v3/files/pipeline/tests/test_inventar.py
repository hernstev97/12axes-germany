"""Targeted repair counterexamples. No respondent data or semantic acceptance."""

from contextlib import redirect_stdout
import hashlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from pipeline import inventar as inv


class PinnedInputs(unittest.TestCase):
    def setUp(self):
        output = inv.ROOT / "outputs/loop/inventory-repair"
        output.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=output)
        self.addCleanup(self.temp.cleanup)
        self.cache = Path(self.temp.name)
        self.content = b"Synthetic public documentation licence fixture"
        self.source = {"file": "synthetic-licence.html", "url": "https://example.invalid/public.html", "sha256": hashlib.sha256(self.content).hexdigest()}
        self.sources = patch.object(inv, "SOURCES", {"ESS-CONDITIONS-OF-USE": self.source})
        self.sources.start()
        self.addCleanup(self.sources.stop)
        self.location = patch.object(inv, "CACHE", self.cache)
        self.location.start()
        self.addCleanup(self.location.stop)

    def response(self, content):
        response = io.BytesIO(content)
        response.geturl = lambda: self.source["url"]
        return response

    def test_missing_disclaimer_is_not_optional(self):
        with self.assertRaisesRegex(RuntimeError, "Missing or changed"):
            inv.verify_sources()

    def test_changed_disclaimer_blocks_extract_before_poppler(self):
        (self.cache / self.source["file"]).write_bytes(b"Changed synthetic input")
        with patch.object(inv.subprocess, "run") as process, self.assertRaises(RuntimeError):
            inv.run_extract()
        process.assert_not_called()

    def test_matching_download_and_existing_cache_verify(self):
        with patch.object(inv.urllib.request, "urlopen", return_value=self.response(self.content)) as request, redirect_stdout(io.StringIO()):
            inv.fetch()
        request.assert_called_once_with(self.source["url"], timeout=60)
        self.assertEqual((self.cache / self.source["file"]).read_bytes(), self.content)
        inv.verify_sources()
        with patch.object(inv.urllib.request, "urlopen") as request:
            inv.fetch()
        request.assert_not_called()

    def test_changed_network_bytes_never_create_pinned_file(self):
        with patch.object(inv.urllib.request, "urlopen", return_value=self.response(b"New public bytes")), redirect_stdout(io.StringIO()), self.assertRaisesRegex(SystemExit, "refusing silent update"):
            inv.fetch()
        self.assertFalse((self.cache / self.source["file"]).exists())

    def test_changed_cache_never_overwrites_or_fetches(self):
        path = self.cache / self.source["file"]
        path.write_bytes(b"Existing changed bytes")
        with patch.object(inv.urllib.request, "urlopen") as request, self.assertRaisesRegex(SystemExit, "refusing overwrite"):
            inv.fetch()
        request.assert_not_called()
        self.assertEqual(path.read_bytes(), b"Existing changed bytes")


class CardLocators(unittest.TestCase):
    def duplicated_card(self, heading="LISTE9292", labels="I7,I7, I8,I8, I9 I9", page=97):
        cards = [""] * 100
        cards[page - 1] = labels + "\n" + heading + "\n0 10"
        return cards

    def test_visual_duplicate_heading_locates_page_97(self):
        evidence = inv.showcard_evidence("92", self.duplicated_card())
        self.assertEqual(evidence["pdf_seiten"], [97])
        self.assertEqual(evidence["kategorienabnahme"], "NICHT_GEPRUEFT")
        self.assertEqual(inv.locator_status([evidence]), "ENTWURF_LOCATOR_KARTENINHALT_OFFEN")

    def test_duplicate_rule_requires_the_known_page_and_all_labels(self):
        for cards in [self.duplicated_card(page=96), self.duplicated_card(labels="I7 I8"), self.duplicated_card(heading="LISTE9293")]:
            with self.subTest(cards=cards[96]):
                self.assertEqual(inv.showcard_evidence("92", cards)["pdf_seiten"], [])

    def test_standard_heading_and_numeric_boundary(self):
        self.assertEqual(inv.showcard_evidence("92", ["LISTE 92\n0 10"])["pdf_seiten"], [1])
        self.assertEqual(inv.showcard_evidence("9", ["LISTE 92\n0 10"])["pdf_seiten"], [])

    def test_absent_locator_opens_row_even_if_status_is_incorrectly_closed(self):
        evidence = inv.showcard_evidence("92", [""] * 100)
        self.assertEqual(evidence["status"], "OFFEN_LISTENLOCATOR")
        row = {key: "ENTWURF" for key in inv.PENDING_CRITERIA}
        row["listenheft_beleg"] = inv.json_text([evidence])
        self.assertTrue(any("OFFEN_LISTENLOCATOR" in reason for reason in inv.pending_reasons(row)))


class ResponseTaskAnnotations(unittest.TestCase):
    def test_same_agreement_scale_does_not_equal_same_response_task(self):
        self.assertEqual(inv.table_answers("B34"), inv.table_answers("B35"))
        self.assertEqual(inv.table_answers("B34"), inv.table_answers("B36"))
        self.assertIn("Normative", inv.judgement("B34")[2])
        self.assertIn("Normative", inv.judgement("B36")[2])
        self.assertIn("Schamreaktion", inv.judgement("B35")[2])
        self.assertNotEqual(inv.judgement("B34")[2], inv.judgement("B35")[2])

    def test_experience_and_self_identity_do_not_share_a_fallback(self):
        self.assertIn("Selbstwahrnehmung", inv.judgement("E8M")[2])
        for number, domain in [(9, "medizinischen"), (10, "Berufsleben"), (11, "Polizeikontakt")]:
            male = inv.judgement(f"E{number}M")
            female = inv.judgement(f"E{number}W")
            self.assertEqual(male, female)
            self.assertIn("eigene Ungleichbehandlung", male[2])
            self.assertIn(domain, male[2])
            self.assertEqual(male[0], "ENTWURF_OFFEN")

    def test_d14_is_a_supply_experience_not_blanket_own_behavior(self):
        status, reason, kind = inv.judgement("D14")
        self.assertEqual(status, "ENTWURF_OFFEN")
        self.assertIn("Versorgungserfahrung", kind)
        self.assertNotEqual(kind, "Eigenes Verhalten")
        self.assertEqual(reason, "")

    def test_unread_unknown_item_remains_unknown(self):
        self.assertTrue(inv.judgement("X999")[2].startswith("UNBEKANNT"))
        self.assertEqual(inv.annotation_evidence("X999", {"pdf_seite": 1})[0], "OFFEN_ANTWORTTYP_UNBEKANNT")

    def test_d_block_separates_administration_body_and_supply_from_actions(self):
        status, reason, kind = inv.judgement("D9")
        self.assertEqual(status, "ENTWURF_KONTEXT_ODER_VERWALTUNG")
        self.assertIn("Interviewercodierung", kind)
        for qid in ["D11", "D12", "D15", "D16"]:
            with self.subTest(qid=qid):
                status, reason, kind = inv.judgement(qid)
                self.assertEqual(status, "ENTWURF_OFFEN")
                self.assertEqual(reason, "")
                self.assertNotEqual(kind, "Eigenes Verhalten")
        self.assertIn("Körpermerkmal", inv.judgement("D11")[2])
        self.assertIn("Körpermerkmal", inv.judgement("D12")[2])
        self.assertIn("Gründe", inv.judgement("D15")[2])
        self.assertIn("Versorgungsbedarf", inv.judgement("D16")[2])
        for qid in ["D2", "D17"]:
            self.assertEqual(inv.judgement(qid)[0], "ENTWURF_AUSSCHLUSS_NACH_ISSUE")
        self.assertIn("Obstkonsum", inv.judgement("D2")[2])
        self.assertIn("Betreuung", inv.judgement("D17")[2])
        for qid, page in [("D9",35),("D11",36),("D12",36),("D15",37),("D16",38)]:
            self.assertTrue(inv.annotation_evidence(qid, {"pdf_seite":page})[1])
            with self.assertRaises(RuntimeError):
                inv.annotation_evidence(qid, {"pdf_seite":page+1})

    def test_annotation_wrong_page_fails_instead_of_rebinding(self):
        with self.assertRaisesRegex(RuntimeError, "annotation page changed"):
            inv.annotation_evidence("B34", {"pdf_seite": 14})

    def test_pending_missing_and_unknown_type_are_reported(self):
        row = {key: "ENTWURF" for key in inv.PENDING_CRITERIA}
        row.update({"missingcodes_status": "OFFEN", "antworttyp_status": "OFFEN_ANTWORTTYP_UNBEKANNT", "listenheft_beleg": "[]"})
        self.assertEqual(inv.pending_reasons(row), ["OFFEN", "OFFEN_ANTWORTTYP_UNBEKANNT"])


if __name__ == "__main__":
    unittest.main()
