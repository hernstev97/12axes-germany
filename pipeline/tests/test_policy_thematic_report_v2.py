"""Synthetic semantic/closed-public rendering tests; no actual exports or IO.

The existing technical-test fixture supplies synthetic public shapes, not
empirical answers. Fixed fractions below are independent hand oracles.
"""

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from pipeline.policy_report_v2 import PolicyReportError
from pipeline.policy_thematic_report_v2 import (
    THEMES, PolicyThematicReportError, render_thematic_report,
)
from pipeline.tests.test_policy_report_v2 import fixtures


def semantic_fixture():
    contracts, exports = fixtures()
    sources, studies, items = [], [], []
    assignment = {variable: key for key, _, variables, _, _ in THEMES for variable in variables}
    block = ["fairelc", "dfprtal", "medcrgv", "rghmgpr", "votedir", "cttresa", "gptpelc",
             "gvctzpv", "grdfinc", "viepol", "wpestop", "keydec"]
    for study in contracts:
        sid = study["study_id"]
        source_id = "SYNTHETIC-source-" + sid
        sources.append({"id": source_id, "kind": "SYNTHETIC national source", "licenseId": "SYNTHETIC-doc-license",
                        "publicUrl": "https://example.org/" + sid + ".pdf", "retrievedUtc": "SYNTHETIC-UTC",
                        "httpStatus": 200, "originalBytesSha256": "a" * 64})
        studies.append({"id": sid, "edition": study["edition"], "country": "DE",
                        **{key: deepcopy(study["provenance"][key]) for key in
                           ("dataDoi", "documentationDoi", "populationDeclaredEn", "fieldwork", "versionNotes")}})
        for definition in study["adapter"]["questions"]:
            var = definition["variable"]
            categories = []
            for index, code in enumerate(definition["categoryCodes"]):
                categories.append({"code": code, "labelDe": "SYNTHETIC original label " + code,
                                   "printedCodeDe": str(index + 1) if var == "vteurmmb" else ("00" if code == "0" else code),
                                   "isMissingApi": False, "labelSourceRef": source_id})
            mode = {"boundOriginalForm": "SYNTHETIC CAPI", "cawiWordingDe": None}
            if sid == "ESS10SCe03_2":
                mode = {"boundOriginalForm": "SYNTHETIC PAPI/CAWI", "cawiWordingDe": "SYNTHETIC full CAWI " + var,
                        "cawiIntroductionsDe": ["SYNTHETIC CAWI shared introduction"],
                        "cawiCategories": [{"code": c["code"], "labelDe": "SYNTHETIC CAWI label " + c["code"],
                                            "displayedCodeDe": None} for c in categories],
                        "cawiDifferenceFromPapi": "SYNTHETIC format difference", "cawiSourceRef": source_id}
            items.append({"id": definition["question_id"], "studyId": sid, "variable": var, "primaryTheme": assignment[var],
                          "originalQuestionId": "B" + str(block.index(var) + 1) if var in block else "SYNTHETIC-Q-" + var,
                          "wordingDe": "SYNTHETIC original wording " + var,
                          "introductionsDe": ["SYNTHETIC introduction " + var],
                          "responseStemDe": "SYNTHETIC response stem " + var,
                          "situationDe": "SYNTHETIC situation " + var,
                          "instructionDe": "SYNTHETIC instruction " + var,
                          "categories": categories, "apiValidCodeOrder": definition["categoryCodes"].copy(),
                          "missingCodes": [{"code": code, "reasonApi": reason, "isMissingApi": True,
                                            "printedCodeDe": None, "labelDe": None}
                                           for code, reason in definition["missingCodes"].items() if code != ""],
                          "notAskedCodes": [], "responseType": "SYNTHETIC nominal/ordered as bound",
                          "responseContentType": "SYNTHETIC content", "modeBinding": mode,
                          "routing": {"originalObservedRoutingDe": "SYNTHETIC routing only"},
                          "mappingNotes": ["SYNTHETIC mapping limit"],
                          "sourceRefs": [{"sourceId": source_id, "pdfPages": [12], "originalQuestionId": var},
                                         {"sourceId": source_id, "sourceFieldId": "SYNTHETIC-FIELD-" + var,
                                          "sourceFieldMetadataVersion": 3}]})
    catalog = {"schemaVersion": 1, "sources": sources, "studies": studies, "items": items,
               "groups": [{"originalQuestionRange": "B1–B12", "itemIds": ["ESS10SCe03_2:" + v for v in block],
                           "introductionDe": "SYNTHETIC full democracy introduction",
                           "responseStemDe": "SYNTHETIC full democracy stem"}]}
    analysis = {"studies": contracts, "catalog": {"path": "data/politikprofil-v2.fragen.entwurf.json", "sha256": "b" * 64},
                "publicationRules": {"minimumValidCount": 100, "minimumPositiveCellCount": 5,
                                     "arithmeticTolerance": 1e-12, "primaryWeight": "pspwght",
                                     "sensitivityWeights": ["dweight", "unweighted"], "equivalenceDiagnostic": "anweight",
                                     "descriptiveDesignVariance": False, "websiteConfidenceIntervals": False,
                                     "personalUncertainty": False, "allOriginalCategoriesRetained": True,
                                     "itemSelectionAfterResults": False}}
    return exports, analysis, catalog


class ThematicReportTests(unittest.TestCase):
    def setUp(self):
        self.exports, self.analysis, self.catalog = semantic_fixture()

    def render(self):
        return render_thematic_report(self.exports, self.analysis, self.catalog)

    def section(self, text, qid):
        return text.split("### `" + qid + "`", 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]

    def rejected(self):
        with self.assertRaises((PolicyThematicReportError, PolicyReportError)) as raised:
            self.render()
        self.assertNotIn("SECRET-SYNTHETIC", str(raised.exception))

    def test_43_original_contexts_eight_rubrics_and_independent_fraction_table(self):
        text = self.render()
        for _, title, _, _, _ in THEMES:
            self.assertEqual(text.count("\n## " + title + "\n"), 1)
        for item in self.catalog["items"]:
            section = self.section(text, item["id"])
            for label in ("original wording", "introduction", "response stem", "situation", "instruction"):
                self.assertIn("SYNTHETIC " + label + " " + item["variable"], section)
            self.assertIn("#page=12", section)
            self.assertIn("physische PDF", section)
        # Counts 30/70, weights 2/1: category weights 60/70, total 130.
        # These fixed rationals do not rerun the renderer's computation.
        self.assertEqual(Fraction(60, 130), Fraction(6, 13))
        section = self.section(text, "ESS5e03_6:bplcdc")
        self.assertIn("| 0 | SYNTHETIC original label 0 | 00 | 46,153846 |", section)
        self.assertIn("| 1 | SYNTHETIC original label 1 | 1 | 53,846154 |", section)
        self.assertIn("| 10 | SYNTHETIC original label 10 | 10 | 0,000000 |", section)
        self.assertIn("Gültiger Antwortnenner: **100**", section)
        self.assertIn("fehlend: 3", section)
        self.assertIn("| export\\_blank\\_unclassified | 1 | 7 |", section)
        self.assertIn("| Refusal | 2 | 8 |", section)
        self.assertIn("ungewichtet 16,153846; dweight 28,506787", section)
        self.assertIn("Scope `all_de_cases`", section)
        self.assertNotIn("SYNTHETIC-NEVER-OPEN", text)

    def test_printed_and_export_nominal_codes_and_cawi_unprinted_codes_separate(self):
        section = self.section(self.render(), "ESS10SCe03_2:vteurmmb")
        self.assertIn("| 33 | SYNTHETIC original label 33 | 3 | 0,000000 |", section)
        self.assertIn("| 65 | SYNTHETIC original label 65 | 6 | 0,000000 |", section)
        self.assertIn("| 65 | SYNTHETIC CAWI label 65 | keiner gedruckt |", section)
        self.assertIn("SYNTHETIC full CAWI vteurmmb", section)

    def test_null_n0_withheld_unapproved_keep_meanings_without_numbers(self):
        statuses = ("no_valid_answers", "withheld_base_or_cell_count", "result_review_withheld")
        for export in self.exports:
            for i, q in enumerate(export["questions"]):
                q.update(status=statuses[i % 3], reference=None)
        text = self.render()
        self.assertNotIn("46,153846", text)
        for item in self.catalog["items"]:
            section = self.section(text, item["id"])
            self.assertIn("Weiterhin nicht freigegeben", section)
            self.assertIn("keine Referenz |", section)
            self.assertIn("Null bedeutet", section)
            self.assertNotIn("Gültiger Antwortnenner", section)
            self.assertNotIn("Missing-Abrechnung auf alle", section)
            self.assertNotIn("Gewichtsvergleiche", section)

    def test_separate_study_fraction_and_distinct_question_denominator(self):
        # Independent second source oracle: weights 50/60 => 5/11,6/11.
        for q in self.exports[1]["questions"]:
            q["reference"]["categories"][0]["proportion"] = float(Fraction(5, 11))
            q["reference"]["categories"][1]["proportion"] = float(Fraction(6, 11))
        ref = self.exports[0]["questions"][1]["reference"]
        ref["validCount"], ref["missingCount"] = 101, 2
        ref["missingReasons"][0].update(count=1, primaryWeightSum=4.0)
        ref["missingWeight"] = 11.0
        text = self.render()
        self.assertIn("46,153846", self.section(text, "ESS5e03_6:bplcdc"))
        self.assertIn("45,454545", self.section(text, "ESS8e02_3:gvslvol"))
        self.assertIn("Antwortnenner: **101**", self.section(text, "ESS5e03_6:dpcstrb"))

    def test_methods_b25_full_democracy_context_and_pending_acceptance(self):
        text = self.render()
        for fragment in ("WIP / Entwurf", "B13–B24", "B26–B29", "PDF162", "Antwort 1 → B26", "Antwort 2 → B28",
                         "München", "v1-A/B", "derselben Codex-Modellfamilie", "keine unabhängige Rohdaten-",
                         "100/5-Darstellungsheuristik", "keine aktuelle Bevölkerungsnorm", "B-V2-M03",
                         "CC BY-NC-SA 4.0", "menschliche Gestaltung"):
            self.assertIn(fragment, text)
        self.assertLess(text.index("ESS10SCe03_2:wpestop`, `ESS10SCe03_2:keydec`"), text.index("## Wirtschaft"))

    def test_metadata_html_markdown_and_link_delimiters_escaped(self):
        item = self.catalog["items"][0]
        item["wordingDe"] = "<script>SECRET-SYNTHETIC</script> [click](javascript:x) | *word*"
        item["categories"][0]["labelDe"] = "row | [fake](https://bad) <img>"
        self.catalog["sources"][0]["publicUrl"] = "https://example.org/x)evil[.pdf"
        text = self.render()
        self.assertNotIn("<script>", text)
        self.assertNotIn("[click](javascript:x)", text)
        self.assertIn("&lt;script&gt;", text)
        self.assertIn("row \\| \\[fake\\]", text)
        self.assertIn("https://example.org/x%29evil%5B.pdf", text)

    def test_semantic_code_order_labels_missing_and_identity_binding_rejected(self):
        original = deepcopy(self.catalog)
        mutations = [
            lambda c: c["items"][0]["categories"].reverse(),
            lambda c: c["items"][0]["categories"][0].update(labelDe=None),
            lambda c: c["items"][0].update(studyId="ESS11e04_2"),
            lambda c: c["items"][0].update(primaryTheme="europe"),
            lambda c: c["items"][0]["missingCodes"][0].update(reasonApi="SECRET-SYNTHETIC"),
            lambda c: c["items"][0]["sourceRefs"][0].update(sourceId="SECRET-SYNTHETIC"),
            lambda c: c["items"][0]["categories"][0].update(labelSourceRef="SECRET-SYNTHETIC"),
            lambda c: c["groups"][0]["itemIds"].reverse(),
            lambda c: c["studies"][0].update(edition="wrong"),
            lambda c: c["studies"][0].update(populationDeclaredEn="SECRET-SYNTHETIC"),
            lambda c: c["sources"][0].update(publicUrl="javascript:SECRET-SYNTHETIC"),
            lambda c: c["sources"][0].update(publicUrl="https://user:SECRET-SYNTHETIC@example.org/"),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutations.index(mutation)):
                self.catalog = deepcopy(original)
                mutation(self.catalog)
                self.rejected()

    def test_no_free_rules_or_catalogue_path_claims(self):
        original = deepcopy(self.analysis)
        mutations = [lambda a: a["publicationRules"].update(minimumValidCount=99),
                     lambda a: a["publicationRules"].update(minimumPositiveCellCount=4),
                     lambda a: a["publicationRules"].update(websiteConfidenceIntervals=True),
                     lambda a: a["catalog"].update(path="SECRET-SYNTHETIC`<script>"),
                     lambda a: a["catalog"].update(sha256="SECRET-SYNTHETIC")]
        for mutation in mutations:
            self.analysis = deepcopy(original)
            mutation(self.analysis)
            self.rejected()

    def test_closed_export_private_extra_keys_status_and_accounting_rejected(self):
        original = deepcopy(self.exports)
        mutations = [lambda e: e[0].update(raw="SECRET-SYNTHETIC"),
                     lambda e: e[0]["questions"][0].update(person="SECRET-SYNTHETIC"),
                     lambda e: e[0]["questions"][0].update(status="prepared_pending_result_review"),
                     lambda e: e[0]["questions"][0]["reference"].update(row="SECRET-SYNTHETIC"),
                     lambda e: e[0]["questions"][0]["reference"]["categories"][0].update(count=5),
                     lambda e: e[0]["questions"][0]["reference"].update(validCount=99),
                     lambda e: e[0]["questions"][0]["reference"]["categories"][0].update(proportion=float("nan"))]
        for mutation in mutations:
            self.exports = deepcopy(original)
            mutation(self.exports)
            self.rejected()

    def test_immutable_deterministic_order_permutation(self):
        before = deepcopy((self.exports, self.analysis, self.catalog))
        text = self.render()
        self.assertEqual((self.exports, self.analysis, self.catalog), before)
        self.exports.reverse()
        self.analysis["studies"].reverse()
        self.catalog["items"].reverse()
        self.catalog["sources"].reverse()
        self.assertEqual(self.render(), text)


def build_fixture():
    """Mock published bytes; not genuine decisions, sources or hash evidence."""
    spec = importlib.util.spec_from_file_location("synthetic_thematic_build",
                                                  Path(__file__).parents[2] / "scripts/build-policy-v2-report.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    exports, analysis, catalog = semantic_fixture()
    for export in exports:
        export["reviewManifestSha256"] = module.MANIFEST_HASH
        for q in export["questions"]:
            if q["id"] == "ESS10SCe03_2:cttresa":
                q.update(status="withheld_base_or_cell_count", reference=None)
    def encoded(value):
        return json.dumps(value, ensure_ascii=False, allow_nan=False).encode()
    cache = {}
    for source in catalog["sources"]:
        source["cachedPath"] = "outputs/loop/breadth-data-001/sources/" + source["id"] + ".json"
        cache[source["cachedPath"]] = b"SYNTHETIC public source bytes"
        source["originalBytesSha256"] = sha256(cache[source["cachedPath"]]).hexdigest()
    catalog_bytes = encoded(catalog)
    analysis["catalog"]["sha256"] = sha256(catalog_bytes).hexdigest()
    cache["data/analysevertrag.v2.entwurf.json"] = encoded(analysis)
    cache["data/politikprofil-v2.fragen.entwurf.json"] = catalog_bytes
    artifacts = [{"path": p, "sha256": sha256(cache.get(p, b"SYNTHETIC public metadata")).hexdigest()}
                 for p in module.PUBLIC_MANIFEST_PATHS]
    for p in module.PUBLIC_MANIFEST_PATHS:
        cache.setdefault(p, b"SYNTHETIC public metadata")
    manifest = {"package": "RESULTS-V2-001/v1", "rawAccessAllowed": False, "publicArtifacts": artifacts,
                "privateAggregates": [{"path": "data/local/SYNTHETIC-NEVER-OPEN.json", "sha256": "f" * 64}]}
    decisions, public_files = [], []
    for export in exports:
        sid = export["studyId"]
        approved = [q["id"] for q in export["questions"] if q["reference"] is not None]
        decisions.append({"schemaVersion": 1, "decision": "ALLOW_REVIEWED_HISTORICAL_REFERENCE_V2", "studyId": sid,
                          "edition": export["edition"], "candidateSha256": export["candidateSha256"],
                          "sourceContractSha256": export["sourceContractSha256"],
                          "approvedQuestionIds": approved, "reviewManifestSha256": module.MANIFEST_HASH,
                          "reviewers": [{"role": role, "reportPath": info[0], "sha256": info[1], "decision": "ACCEPTED_BOUNDED"}
                                        for role, info in module.REVIEWERS.items()]})
        path = "data/reference-v2/" + sid + ".json"
        cache[path] = encoded(export)
        public_files.append({"studyId": sid, "path": path, "sha256": sha256(cache[path]).hexdigest(),
                             "reviewedReferenceCount": len(approved), "questionInventoryCount": len(export["questions"])})
    root_decision = {"schemaVersion": 1, "decision": "ALLOW_REVIEWED_HISTORICAL_REFERENCE_V2",
                     "rootReadBothCompleteFirstReports": True, "actualManifestAnd29Public5PrivateBytesVerified": True,
                     "withheldIds": ["ESS10SCe03_2:cttresa"], "studyDecisions": decisions, "publicFiles": public_files}
    for role, (report, _, path, _) in module.REVIEWERS.items():
        cache[report] = b"SYNTHETIC report, not a real review"
        cache[path] = encoded({"schemaVersion": 1, "role": role, "reviewManifestSha256": module.MANIFEST_HASH,
                               "decision": "ACCEPTED_BOUNDED", "studies": [{k: d[k] for k in
                                ("studyId", "candidateSha256", "approvedQuestionIds")} for d in decisions]})
    cache[module.MANIFEST], cache[module.DECISION] = encoded(manifest), encoded(root_decision)
    return module, cache, root_decision


class PublicBuildGuardTests(unittest.TestCase):
    def test_mock_public_build_never_traverses_private_manifest_and_binds_42(self):
        module, cache, _ = build_fixture()
        paths = []
        # This mock tests path/decision structure only, not authentic bytepins.
        def mock_pinned(path, expected):
            paths.append(path)
            return cache[path]
        with patch.object(module, "pinned", side_effect=mock_pinned):
            report = module.build_bytes().decode()
        self.assertIn("42 historische Einzelreferenzen", report)
        section = report.split("### `ESS10SCe03_2:cttresa`", 1)[1].split("\n### ", 1)[0]
        self.assertIn("Keine Zahlenreferenz", section)
        self.assertTrue(all(not p.startswith(("data/local/", "data/raw/")) for p in paths))

    def test_fake_roles_candidate_source_approval_or_private_path_fail_before_render(self):
        mutations = [lambda d: d["studyDecisions"][0]["reviewers"][0].update(role="fake"),
                     lambda d: d["studyDecisions"][0].update(candidateSha256="f" * 64),
                     lambda d: d["studyDecisions"][0].update(sourceContractSha256="f" * 64),
                     lambda d: d["studyDecisions"][0]["approvedQuestionIds"].pop(),
                     lambda d: d["publicFiles"][0].update(path="data/local/SYNTHETIC-NEVER-OPEN.json")]
        for mutation in mutations:
            module, cache, decision = build_fixture()
            mutation(decision)
            cache[module.DECISION] = json.dumps(decision).encode()
            paths = []
            def mock_pinned(path, expected):
                paths.append(path)
                return cache[path]
            with patch.object(module, "pinned", side_effect=mock_pinned):
                with self.assertRaises(module.PublicBuildError):
                    module.build_bytes()
            self.assertTrue(all(not p.startswith(("data/local/", "data/raw/")) for p in paths))

    def test_actual_hash_comparison_and_symlink_preflight_with_fake_filesystem(self):
        module, _, _ = build_fixture()
        class FakePath:
            def __init__(self, symlink=False):
                self.symlink, self.reads = symlink, 0
            def __truediv__(self, _):
                return self
            def joinpath(self, *_):
                return self
            def is_symlink(self):
                return self.symlink
            def read_bytes(self):
                self.reads += 1
                return b"SYNTHETIC public bytes"
        normal = FakePath()
        with patch.object(module, "ROOT", normal):
            with self.assertRaises(module.PublicBuildError):
                module.pinned("data/reference-v2/ESS5e03_6.json", "f" * 64)
            self.assertEqual(module.pinned("data/reference-v2/ESS5e03_6.json",
                             sha256(b"SYNTHETIC public bytes").hexdigest()), b"SYNTHETIC public bytes")
        symlink = FakePath(True)
        with patch.object(module, "ROOT", symlink):
            with self.assertRaises(module.PublicBuildError):
                module.pinned("data/reference-v2/ESS5e03_6.json", "f" * 64)
        self.assertEqual(symlink.reads, 0)

    def test_duplicate_json_keys_and_nonfinite_json_fail(self):
        module, _, _ = build_fixture()
        for data in (b'{"status":1,"status":2}', b'{"proportion":NaN}'):
            with self.assertRaises(module.PublicBuildError):
                module.decode(data)


if __name__ == "__main__":
    unittest.main()
