"""Synthetic public-shape guard cases and separate current public reproduction.

Numeric unit fixtures are invented and are never private candidates. Original
pair/source identities come from public contracts. The public reproduction test
does read the explicitly authorized public exports, not raw or private inputs.
"""

import ast
from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
from decimal import Decimal
from html import unescape
import importlib.util
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

from pipeline import policy_group_report_v21 as report
from pipeline.policy_group_export_v21 import _source


ROOT = Path(__file__).parents[2]
QA = ROOT / "outputs/loop/group-report"


def public_json(path):
    # Every caller passes a fixed public path, never a metadata path lookup.
    return json.loads((ROOT / path).read_bytes())


def synthetic_fixture():
    analysis = public_json("data/analysevertrag.v2.entwurf.json")
    groups = public_json("data/gruppenvertrag.v2.1.entwurf.json")
    catalogue = public_json("data/politikprofil-v2.fragen.entwurf.json")
    root = public_json("reports/loop/policy-group-v21-export-decisions.json")
    roles = {role: public_json(info[2]) for role, info in report.REVIEWERS.items()}
    sources = {s["study_id"]: s for s in analysis["studies"]}
    grouped = {s["studyId"]: s for s in groups["studies"]}
    exports = []
    for index, (sid, decision) in enumerate(zip(report.STUDY_IDS, root["studyDecisions"], strict=True), 1):
        # These formal identifiers deliberately identify invented public-shape
        # values. They do not assert that Root accepted the toy numbers.
        decision["candidateSha256"] = str(index) * 64
        approved = {(p["groupId"], p["questionId"]) for p in decision["approvedGroupQuestionIds"]}
        source, grouping = sources[sid], grouped[sid]
        inventory = []
        for original in grouping["groupsInDeclaredApiOrder"]:
            group = {key: original[source_key] for key, source_key in {
                "id": "groupId", "party2Code": "party2Code", "kind": "kind", "labelEnExactApi": "labelEnExactApi",
                "labelDeOriginalForm": "labelDeOriginalForm", "labelDeOfficialAppendix": "labelDeOfficialAppendix",
                "appendixNameSourceId": "appendixNameSourceId", "appendixNamePdfPage1Based": "appendixNamePdfPage1Based",
                "formOptionStatus": "formOptionStatus"}.items()}
            group["heterogeneousUnlabelledOther"] = original["kind"] == "other_unlabelled"
            questions = []
            for definition in source["adapter"]["questions"]:
                pair = (original["groupId"], definition["question_id"])
                reference = None
                if pair in approved:
                    categories = [{"code": code, "proportion": 0.9 if i == 0 else 0.1 if i == 1 else 0}
                                  for i, code in enumerate(definition["categoryCodes"])]
                    reference = {"weight": "pspwght", "validCount": 100, "totalCount": 105,
                                 "missingCount": 5, "notAskedCount": 0, "categories": categories, "uncertainty": None}
                questions.append({"id": definition["question_id"], "status": "reviewed_historical_reference" if reference else "result_review_withheld",
                                  "reference": reference})
            group["questions"] = questions
            inventory.append(group)
        scope = {"basis": "historical_same_study_policy_responses_grouped_by_recalled_Bundestag_second_vote",
                 "timeReference": groups["boundaries"]["answersTimeReference"],
                 "populationReference": groups["boundaries"]["historicalSelfReportInEachSurvey15Plus"],
                 "partyRecallAndModeLimit": groups["boundaries"]["partyRecallAndModeLimit"],
                 "independentNorm": False, "currentPartyPositions": False, "partyScores": False,
                 "personsOrStudiesPooled": False, "precisionOrAnonymityValidated": False}
        exports.append({"schemaVersion": 1, "status": "reviewed_historical_descriptive_group_reference",
                        "studyId": sid, "edition": source["edition"], **{key: decision[key] for key in
                        ("groupContractSha256", "studyContractSha256", "candidateSha256", "reviewManifestSha256")},
                        "source": _source(source, grouping, groups), "scope": scope, "groups": inventory})
    return exports, analysis, groups, catalogue, root, roles


def cli_module():
    spec = importlib.util.spec_from_file_location("fixed_public_group_cli_test", ROOT / "scripts/build-policy-group-report-v21.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PureReportTests(unittest.TestCase):
    def setUp(self):
        self.args = synthetic_fixture()

    def render(self, args=None):
        return report.render_historical_group_report(*(self.args if args is None else args))

    def reject(self, mutate):
        args = deepcopy(self.args)
        mutate(args)
        with self.assertRaises(report.PolicyGroupReportError) as caught:
            self.render(args)
        self.assertNotIn("SYNTHETIC_PRIVATE_SECRET", str(caught.exception))
        return caught.exception

    def first_reference(self, args):
        return next(q["reference"] for q in args[0][0]["groups"][0]["questions"] if q["reference"] is not None)

    def test_complete_inventory_and_63_original_approved_pairs(self):
        text = self.render()
        self.assertEqual(text.count("Gruppen-ID:"), 26)
        self.assertEqual(text.count("Gültiger Frage-Nenner, ungewichtet:"), 63)
        self.assertEqual(text.count("Frage `"), 8 * 6 + 9 * 10 + 9 * 4)
        for sid, group_count in zip(report.STUDY_IDS, (8, 9, 9), strict=True):
            self.assertIn("## " + sid + " – Ausgabe", text)
            self.assertEqual(sum(g["id"].startswith(sid + ":") for g in self.args[0][report.STUDY_IDS.index(sid)]["groups"]), group_count)

    def test_other_and_null_sections_have_no_private_bases(self):
        text = self.render()
        for section in text.split("#### Other – Dateicode ")[1:]:
            other = section.split("## ", 1)[0]
            self.assertIn("unbenannte, heterogene Originalkategorie", other)
            self.assertNotIn("Gültiger Frage-Nenner", other)
            self.assertNotIn("90,000000", other)
        self.assertIn("keine veröffentlichte Basis oder Anteile", text)

    def test_formatting_preserves_zero_categories_and_weighted_denominator_meaning(self):
        text = self.render()
        self.assertIn("Gültiger Frage-Nenner, ungewichtet: 100; Gesamtbasis dieser Frage: 105; Missing: 5; nicht gestellt: 0", text)
        self.assertIn("90,000000 %", text)
        self.assertIn("0,000000 %", text)
        self.assertIn("Kategorieanteile: `pspwght`", text)
        self.assertIn("Unsicherheit: `null`", text)

    def test_visible_rounding_is_never_renormalized(self):
        reference = self.first_reference(self.args)
        self.assertGreaterEqual(len(reference["categories"]), 3)
        for i, category in enumerate(reference["categories"]):
            category["proportion"] = 1 / 3 if i < 3 else 0
        text = self.render()
        self.assertIn("33,333333 %", text)
        self.assertNotIn("33,333334 %", text)

    def test_weighted_tiny_share_is_not_converted_to_invented_cell_count(self):
        reference = self.first_reference(self.args)
        reference["categories"][0]["proportion"] = 1 - 1e-8
        reference["categories"][1]["proportion"] = 1e-8
        text = self.render()
        self.assertIn("0,000001 %", text)
        self.assertIn("keine Zellcounts", text)

    def test_response_time_and_election_time_and_concordance_limits(self):
        text = self.render()
        for fieldwork, election in (("2010-09-15", "2009"), ("2016-08-23", "2013"), ("2018-08-29", "2017")):
            self.assertIn(fieldwork, text)
            self.assertIn("Erinnerte Bundestagswahl: " + election, text)
        self.assertIn("München", text)
        self.assertIn("WIP\\_ORDERED\\_FORM\\_AND\\_API\\_LABEL\\_ASSOCIATION", text)
        self.assertIn("OFFICIAL\\_ALIAS\\_EXPLICIT\\_TEXT\\_BOUND", text)
        self.assertIn("ESS10-SC und ESS11", text)

    def test_public_source_links_and_licenses_are_distinct(self):
        text = self.render()
        for url in ("https://creativecommons.org/licenses/by-nc-sa/4.0/", "https://creativecommons.org/licenses/by-sa/4.0/",
                    "https://doi.org/10.21338/ess5e03_6", "https://doi.org/10.21338/nsd-ess8-2016"):
            self.assertIn(url, text)
        self.assertIn("ESS ERIC", text)
        self.assertIn("Sikt", text)
        self.assertIn("Fragenkatalog", text)
        self.assertIn("vollständiger Themenbericht", text)

    def test_unknown_and_private_keys_rejected_at_every_level(self):
        for mutate in (lambda a: a[0][0].update(_records=["SYNTHETIC_PRIVATE_SECRET"]),
                       lambda a: a[0][0]["groups"][0].update(eligible_case_count=3),
                       lambda a: a[0][0]["groups"][0]["questions"][0].update(privateCount=3),
                       lambda a: self.first_reference(a).update(categoryCounts=[1, 2]),
                       lambda a: self.first_reference(a)["categories"][0].update(count=3)):
            self.reject(mutate)

    def test_null_with_numbers_status_promotion_and_hidden_base_rejected(self):
        for mutate in (lambda a: a[0][0]["groups"][-1]["questions"][0].update(reference={"validCount": 3}),
                       lambda a: a[0][0]["groups"][-1]["questions"][0].update(status="reviewed_historical_reference"),
                       lambda a: a[0][0]["groups"][-1]["questions"][0].update(status="zero_distribution"),
                       lambda a: self.first_reference(a).update(validCount=99, totalCount=104)):
            self.reject(mutate)

    def test_denominator_missing_notasked_and_uncertainty_guard(self):
        for mutate in (lambda a: self.first_reference(a).update(totalCount=104),
                       lambda a: self.first_reference(a).update(missingCount=-1),
                       lambda a: self.first_reference(a).update(validCount=True),
                       lambda a: self.first_reference(a).update(notAskedCount=1, totalCount=106),
                       lambda a: self.first_reference(a).update(weight="dweight"),
                       lambda a: self.first_reference(a).update(uncertainty=0)):
            self.reject(mutate)

    def test_shares_fraction_sum_nan_bool_and_category_identity_rejected(self):
        for value in (-1, 1.1, float("nan"), float("inf"), True, None, 0.8):
            self.reject(lambda a, v=value: self.first_reference(a)["categories"][0].update(proportion=v))
        self.reject(lambda a: self.first_reference(a)["categories"].reverse())
        self.reject(lambda a: self.first_reference(a)["categories"][0].update(code="foreign"))

    def test_group_question_source_order_and_labels_cannot_change(self):
        for mutate in (lambda a: a[0].reverse(), lambda a: a[0][0]["groups"].reverse(),
                       lambda a: a[0][0]["groups"][0]["questions"].reverse(),
                       lambda a: a[0][0]["groups"][0].update(party2Code="66"),
                       lambda a: a[0][0]["groups"][0].update(labelDeOriginalForm="SYNTHETIC_PRIVATE_SECRET"),
                       lambda a: a[0][0].update(edition="4.2"),
                       lambda a: a[0][0]["source"]["election"].update(year=2025),
                       lambda a: a[0][0]["scope"].update(independentNorm=0)):
            self.reject(mutate)

    def test_full_catalogue_and_contract_source_mutation_rejected(self):
        for mutate in (lambda a: a[3]["items"][0]["categories"][0].update(labelDe="foreign"),
                       lambda a: a[3].update(extra="foreign"),
                       lambda a: a[2]["displayPolicy"].update(minimumValidQuestionCount=99),
                       lambda a: a[1].update(extraSource="foreign")):
            self.reject(mutate)

    def test_both_actual_role_pair_intents_required_no_foreign_or_duplicate_pair(self):
        for mutate in (lambda a: a[5]["methods_reproducibility"]["approvedGroupQuestionIdsByStudy"][report.STUDY_IDS[0]].pop(),
                       lambda a: a[4]["studyDecisions"][0]["approvedGroupQuestionIds"].append(deepcopy(a[4]["studyDecisions"][0]["approvedGroupQuestionIds"][0])),
                       lambda a: a[4]["studyDecisions"][0]["approvedGroupQuestionIds"][0].update(questionId="ESS11e04_2:gincdif"),
                       lambda a: a[4]["studyDecisions"][0]["reviewers"][0].update(reportPath="data/raw/forbidden"),
                       lambda a: a[5]["sources_constructs_fairness"].update(decision="ALLOW"),
                       lambda a: a[4].update(extraPrivatePath="SYNTHETIC_PRIVATE_SECRET")):
            self.reject(mutate)

    def test_candidate_and_manifest_links_cannot_be_substituted(self):
        for mutate in (lambda a: a[0][0].update(candidateSha256="0" * 64),
                       lambda a: a[0][0].update(reviewManifestSha256=report.MANIFEST_FIRST_SHA256),
                       lambda a: a[4]["sourceFirstReuse"].update(unchangedPrivatePins=4),
                       lambda a: a[4]["publicFiles"][0].update(path="data/reference-groups-v21/foreign.json")):
            self.reject(mutate)

    def test_md_quotes_html_pipes_and_link_syntax(self):
        value = "it's <script>\"quoted\"</script> | [link](javascript:bad) `x` **bold**\n# heading"
        escaped = report._md(value)
        self.assertIn("it's", escaped)
        self.assertIn('"quoted"', escaped)
        self.assertIn("&lt;script&gt;", escaped)
        self.assertIn("\\|", escaped)
        self.assertIn("\\[link\\]\\(javascript:bad\\)", escaped)
        self.assertNotIn("&#x27;", escaped)
        self.assertNotIn("<script>", escaped)

    def test_inputs_unchanged_and_pure_module_no_application_io(self):
        before = deepcopy(self.args)
        self.render()
        self.assertEqual(before, self.args)
        tree = ast.parse((ROOT / "pipeline/policy_group_report_v21.py").read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else ""
                self.assertNotIn(name, {"open", "read_text", "read_bytes", "write_text", "write_bytes", "run_group_reference"})


class FixedPublicCliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cli = cli_module()
        # Complete current PUBLIC inputs only, including report bytes. No paths
        # from documents are traversed; the compiled pin map is the inventory.
        cls.public_bytes = {p: cls.cli.pinned(p) for p in cls.cli.INPUT_PINS}

    def test_current_public_byte_reproduction_separate_from_toy_fixtures(self):
        rendered = self.cli.build_bytes()
        self.assertEqual(rendered, (ROOT / self.cli.OUTPUT).read_bytes())

    def test_independent_current_public_values_and_nulls_presentation_oracle(self):
        # Independent extraction and Decimal display arithmetic, without the
        # renderer's percentage helper or any private/upstream re-estimation.
        # It checks public representation only, not empirical correctness.
        text = (ROOT / self.cli.OUTPUT).read_text()
        catalogue = json.loads(self.public_bytes["data/politikprofil-v2.fragen.entwurf.json"])
        labels = {q["id"]: {c["code"]: c["labelDe"] for c in q["categories"]} for q in catalogue["items"]}
        checked = 0
        for sid in report.STUDY_IDS:
            value = json.loads(self.public_bytes["data/reference-groups-v21/" + sid + ".json"])
            section = text.split("## " + sid + " – Ausgabe", 1)[1].split("\n## ", 1)[0]
            sections = section.split("### Gruppen in Originalreihenfolge", 1)[1].split("\n#### ")[1:]
            self.assertEqual(len(sections), len(value["groups"]))
            for group, group_text in zip(value["groups"], sections, strict=True):
                self.assertIn("Gruppen-ID: `" + group["id"] + "`", group_text)
                for question in group["questions"]:
                    block = group_text.split("Frage `" + question["id"] + "`:", 1)[1].split("\nFrage `", 1)[0]
                    reference = question["reference"]
                    if reference is None:
                        self.assertNotIn("Gültiger Frage-Nenner", block)
                        self.assertNotIn(" %", block)
                        self.assertNotIn("|", block)
                        self.assertIn(question["status"], block)
                        continue
                    counts = re.search(r"ungewichtet: ([0-9]+); Gesamtbasis dieser Frage: ([0-9]+); Missing: ([0-9]+); nicht gestellt: ([0-9]+)", block)
                    self.assertIsNotNone(counts)
                    self.assertEqual(tuple(map(int, counts.groups())), tuple(reference[k] for k in ("validCount", "totalCount", "missingCount", "notAskedCount")))
                    rows = [line for line in block.splitlines() if line.startswith("| ")][2:]
                    self.assertEqual(len(rows), len(reference["categories"]))
                    for row, category in zip(rows, reference["categories"], strict=True):
                        cells = re.split(r"(?<!\\)\|", row)[1:-1]
                        self.assertEqual(len(cells), 3)
                        self.assertEqual(cells[0].strip(), category["code"])
                        native_label = unescape(re.sub(r"\\([\\`*_{}\[\]()|#+.!-])", r"\1", cells[1].strip()))
                        self.assertEqual(native_label, labels[question["id"]][category["code"]])
                        percentage = format(Decimal(str(category["proportion"])) * 100, ".6f").replace(".", ",") + " %"
                        self.assertEqual(cells[2].strip(), percentage)
                    checked += 1
        self.assertEqual(checked, 63)

    def test_each_real_report_decision_and_root_byte_pin_is_authenticated(self):
        paths = [self.cli.ROOT_DECISION]
        paths += [p for info in report.REVIEWERS.values() for p in (info[0], info[2])]
        for path in paths:
            with self.subTest(path=path):
                original = self.public_bytes
                with patch.object(self.cli, "_read_fixed", side_effect=lambda p: original[p] + b"\n" if p == path else original[p]):
                    with self.assertRaises(self.cli.PublicGroupBuildError):
                        self.cli.build_bytes()

    def test_changed_public_export_bytes_rejected_before_output(self):
        target = "data/reference-groups-v21/ESS5e03_6.json"
        with patch.object(self.cli, "_read_fixed", side_effect=lambda p: self.public_bytes[p] + b" " if p == target else self.public_bytes[p]):
            with self.assertRaises(self.cli.PublicGroupBuildError):
                self.cli.build_bytes()

    def test_unlisted_dynamic_or_private_paths_fail_before_os_open(self):
        for path in ("data/raw/forbidden.csv", "data/local/forbidden.json", "../../escape", "/tmp/absolute", None):
            with self.subTest(path=path), patch.object(self.cli.os, "open") as opened:
                with self.assertRaises(self.cli.PublicGroupBuildError):
                    self.cli.pinned(path)
                opened.assert_not_called()

    def test_synthetic_public_path_symlink_and_wrong_bytes_rejected(self):
        QA.mkdir(mode=0o700, exist_ok=True)
        fixed = "data/reference-groups-v21/ESS5e03_6.json"
        with tempfile.TemporaryDirectory(dir=QA, prefix="synthetic-public-") as directory:
            temporary = Path(directory)
            (temporary / "data").mkdir()
            (temporary / "synthetic-target").mkdir()
            (temporary / "data/reference-groups-v21").symlink_to(temporary / "synthetic-target", target_is_directory=True)
            with patch.object(self.cli, "ROOT", temporary):
                with self.assertRaises(OSError):
                    self.cli.pinned(fixed)
            (temporary / "data/reference-groups-v21").unlink()
            (temporary / "data/reference-groups-v21").mkdir()
            (temporary / fixed).write_bytes(b"SYNTHETIC_PUBLIC_CHANGED_BYTES")
            with patch.object(self.cli, "ROOT", temporary):
                with self.assertRaises(self.cli.PublicGroupBuildError):
                    self.cli.pinned(fixed)

    def test_help_and_unknown_args_do_not_open_inputs_or_build(self):
        for args, expected in ((["--help"], 0), (["--raw"], 1), (["build", "foreign"], 1)):
            with patch.object(self.cli, "build_bytes") as build, redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(self.cli.main(args), expected)
                build.assert_not_called()

    def test_duplicate_json_keys_and_nonfinite_constants_rejected(self):
        for value in (b'{"a":1,"a":2}', b'{"a":NaN}', b'{"a":Infinity}'):
            with self.assertRaises(self.cli.PublicGroupBuildError):
                self.cli.decode(value)

    def test_cli_static_error_and_no_dynamic_json_path_reader(self):
        with patch.object(self.cli, "build_bytes", side_effect=ValueError("SYNTHETIC_PRIVATE_SECRET")), redirect_stderr(io.StringIO()) as error:
            self.assertEqual(self.cli.main(["build"]), 1)
            self.assertEqual(error.getvalue(), "policy_group_build_error\n")
        self.assertTrue(all(not p.startswith(("data/raw/", "data/local/")) for p in self.cli.INPUT_PINS))


if __name__ == "__main__":
    unittest.main()
