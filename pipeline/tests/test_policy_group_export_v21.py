"""Independent arithmetic fixtures; no real candidates, files, gates or reviews."""

import ast
from copy import deepcopy
import json
from math import nan
from pathlib import Path
import unittest

from pipeline import policy_group_export_v21 as export
from pipeline.policy_export_v2 import _canonical_hash


ROOT = Path(__file__).parents[2]


def source_contracts():
    # Public instrument contracts only. Never read raw/local or a real candidate.
    return (json.loads((ROOT / "data/analysevertrag.v2.entwurf.json").read_bytes()),
            json.loads((ROOT / "data/gruppenvertrag.v2.1.entwurf.json").read_bytes()))


def fixture(sid="ESS5e03_6", valid_count=100, positive_cell=5, missing_count=20,
            not_asked_count=0, active_group=0):
    study_contract, group_contract = source_contracts()
    study = next(s for s in study_contract["studies"] if s["study_id"] == sid)
    grouping = next(s for s in group_contract["studies"] if s["studyId"] == sid)
    total = valid_count + missing_count + not_asked_count
    groups = []
    for group_index, original in enumerate(grouping["groupsInDeclaredApiOrder"]):
        count = total if group_index == active_group else 0
        questions = []
        for question in study["adapter"]["questions"]:
            n = valid_count if group_index == active_group else 0
            missing = missing_count if group_index == active_group else 0
            not_asked = not_asked_count if group_index == active_group else 0
            counts = [0] * len(question["categoryCodes"])
            if n:
                counts[0] = n - positive_cell; counts[1] = positive_cell
            status = ("no_valid_answers" if not n else "withheld_base_or_cell_count"
                      if n < 100 or any(0 < cell < 5 for cell in counts) else "prepared_pending_group_result_review")
            estimates = []
            for weight, role, scale in (("pspwght", "primary", 1), ("dweight", "sensitivity", 3),
                                        ("unweighted", "sensitivity", 1), ("anweight", "equivalence_diagnostic", 2)):
                accounting = {"total_count": count, "eligible_count": n + missing, "valid_count": n,
                              "missing_count": missing, "not_asked_count": not_asked,
                              "total_weight": count * scale, "eligible_weight": (n + missing) * scale,
                              "valid_weight": n * scale, "missing_weight": missing * scale,
                              "not_asked_weight": not_asked * scale}
                categories = [{"category": code, "count": cell, "weight": cell * scale,
                               "proportion": cell / n if n else None, "variance": None, "standard_error": None}
                              for code, cell in zip(question["categoryCodes"], counts, strict=True)]
                estimates.append({"weight": weight, "role": role, "reference": {
                    "study_id": sid, "question_id": question["question_id"], "accounting": accounting,
                    "estimates": categories, "variance_status": "no_design_basis" if n else "no_valid_responses",
                    "design": None}})
            reasons = [{"reason": reason, "count": missing if reason == "export_blank_unclassified" else 0,
                        "primary_weight_sum": missing if reason == "export_blank_unclassified" else 0}
                       for reason in dict.fromkeys(question["missingCodes"].values())]
            questions.append({"question_id": question["question_id"], "status": status,
                              "estimates": estimates, "missing_reasons": reasons,
                              "not_asked": {"count": not_asked, "primary_weight_sum": not_asked},
                              "sensitivity": {"max_abs_primary_unweighted": 0.0 if n else None,
                                              "max_abs_primary_dweight": 0.0 if n else None,
                                              "max_abs_primary_anweight": 0.0 if n else None}})
        groups.append({"group_id": original["groupId"], "party2_code": original["party2Code"],
                       "kind": original["kind"], "label_en_exact_api": original["labelEnExactApi"],
                       "label_de_original_form": original["labelDeOriginalForm"],
                       "label_de_official_appendix": original["labelDeOfficialAppendix"],
                       "form_option_status": original["formOptionStatus"], "eligible_case_count": count,
                       "questions": questions})
    other = grouping["groupsInDeclaredApiOrder"][active_group]["kind"] == "other_unlabelled"
    candidate = {"schema": "policy-group-reference-v21-wip", "study_id": sid, "edition": study["edition"],
                 "groups": groups, "eligibility": {
                     "de_case_count": total, "eligible_group_case_count": total,
                     "non_yes_vote_with_valid_party_count": 0, "yes_vote_with_party_not_asked_count": 0,
                     "vote_states": [{"state": state, "count": total if state == "yes" else 0}
                                     for state in ("yes", "no", "not_eligible", "source_missing", "technical_export_blank")],
                     "party_states": [{"state": state, "count": total if state == ("valid_other_unlabelled" if other else "valid_named_party") else 0}
                                      for state in ("valid_named_party", "valid_other_unlabelled", "structurally_not_asked", "source_missing", "technical_export_blank")],
                     "vote_source_missing_reasons": [{"reason": reason, "count": 0} for reason in ("Refusal", "Don't know", "No answer")],
                     "party_source_missing_reasons": [{"reason": reason, "count": 0} for reason in ("Refusal", "Don't know", "No answer")]},
                 "study_ratio_diagnostic": {"scope": "all_eligible_group_cases", "case_count": total,
                                            "status": "constant_within_tolerance" if total else "not_evaluable_no_eligible_group_cases",
                                            "ratio_min": 2 if total else None, "ratio_max": 2 if total else None,
                                            "constant_against_first_within_tolerance": True if total else None,
                                            "tolerance": 1e-12}}
    pair = {"groupId": groups[active_group]["group_id"], "questionId": groups[active_group]["questions"][0]["question_id"]}
    decision = {"schemaVersion": 1, "decision": "ALLOW_REVIEWED_HISTORICAL_GROUP_REFERENCES_V21",
                "studyId": sid, "edition": study["edition"], "candidateSha256": _canonical_hash(candidate),
                "groupContractSha256": export.GROUP_CONTRACT_BYTES_SHA256,
                "studyContractSha256": export.STUDY_CONTRACT_BYTES_SHA256, "reviewManifestSha256": "4" * 64,
                "approvedGroupQuestionIds": [pair] if valid_count >= 100 and (positive_cell == 0 or positive_cell >= 5) else [],
                "reviewers": [{"role": role, "reportPath": f"reports/loop/reviews/synthetic-{role}.md",
                               "sha256": str(index) * 64, "decision": "ACCEPTED_BOUNDED"}
                              for index, role in enumerate(("methods_reproducibility", "sources_constructs_fairness"), 1)]}
    return candidate, study_contract, group_contract, decision


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.args = fixture()

    def build(self, args=None):
        return export.build_reviewed_group_reference_export(*(args or self.args))

    def reject_candidate(self, mutation):
        args = list(deepcopy(self.args)); mutation(args[0])
        args[3]["candidateSha256"] = _canonical_hash(args[0])
        with self.assertRaises(export.PolicyGroupExportError) as caught:
            self.build(args)
        self.assertNotIn("SYNTHETIC_PRIVATE_SECRET", str(caught.exception))

    def test_all_five_studies_and_43_question_assignments(self):
        assignments = set()
        for sid in ("ESS5e03_6", "ESS8e02_3", "ESS9e03_3", "ESS10SCe03_2", "ESS11e04_2"):
            result = self.build(fixture(sid))
            groups = result["groups"]
            self.assertTrue(all([q["id"] for q in group["questions"]] == [q["id"] for q in groups[0]["questions"]] for group in groups))
            assignments.update(q["id"] for q in groups[0]["questions"])
            self.assertTrue(all(q["reference"] is None for q in groups[-1]["questions"]))
            self.assertIsNone(groups[-1]["labelDeOriginalForm"])
            self.assertIsNone(groups[-1]["labelDeOfficialAppendix"])
            self.assertTrue(groups[-1]["heterogeneousUnlabelledOther"])
        self.assertEqual(len(assignments), 43)

    def test_public_allowlist_counts_and_shares_only(self):
        result = self.build(); reference = result["groups"][0]["questions"][0]["reference"]
        self.assertEqual(set(reference), {"weight", "validCount", "totalCount", "missingCount", "notAskedCount", "categories", "uncertainty"})
        self.assertEqual((reference["validCount"], reference["totalCount"], reference["missingCount"]), (100, 120, 20))
        self.assertTrue(all(set(category) == {"code", "proportion"} for category in reference["categories"]))
        self.assertIsNone(reference["uncertainty"])
        for group in result["groups"]:
            self.assertNotIn("eligible_case_count", group)
        rendered = json.dumps(result)
        for key in ("eligibility", "study_ratio_diagnostic", "missing_reasons", "primary_weight_sum", "sensitivity", "category_counts", "_records"):
            self.assertNotIn('"' + key + '"', rendered)

    def test_null_references_reveal_no_private_numbers(self):
        result = self.build()
        for group in result["groups"]:
            for question in group["questions"]:
                if question["reference"] is None:
                    self.assertEqual(set(question), {"id", "status", "reference"})
        self.assertEqual(result["groups"][0]["questions"][1]["status"], "result_review_withheld")
        self.assertEqual(result["groups"][1]["questions"][0]["status"], "no_valid_answers")

    def test_99_base_and_positive_cell4_stay_null(self):
        for args in (fixture(valid_count=99), fixture(positive_cell=4)):
            result = self.build(args)
            self.assertEqual(result["groups"][0]["questions"][0]["status"], "withheld_base_or_cell_count")
            self.assertIsNone(result["groups"][0]["questions"][0]["reference"])

    def test_100_base_cell5_and_original_zero_cells(self):
        reference = self.build()["groups"][0]["questions"][0]["reference"]
        self.assertEqual(reference["categories"][0]["proportion"], 0.95)
        self.assertEqual(reference["categories"][1]["proportion"], 0.05)
        self.assertTrue(all(item["proportion"] == 0 for item in reference["categories"][2:]))

    def test_empty_and_missing_only_groups_none_not_zero_reference(self):
        for args in (fixture(valid_count=0, positive_cell=0, missing_count=0), fixture(valid_count=0, positive_cell=0)):
            result = self.build(args)
            self.assertTrue(all(q["reference"] is None for g in result["groups"] for q in g["questions"]))

    def test_other_gets_identical_approval_and_threshold_rule(self):
        result = self.build(fixture(active_group=7))
        other = result["groups"][-1]
        self.assertTrue(other["heterogeneousUnlabelledOther"])
        self.assertEqual(other["labelEnExactApi"], "Other")
        self.assertIsNone(other["labelDeOriginalForm"])
        self.assertEqual(other["questions"][0]["status"], "reviewed_historical_reference")

    def test_source_native_appendix_form_labels_remain_separate(self):
        result = self.build(fixture("ESS11e04_2"))
        group = next(g for g in result["groups"] if g["party2Code"] == "8")
        self.assertIsNone(group["labelDeOriginalForm"])
        self.assertIn("Basisdemokratische", group["labelDeOfficialAppendix"])
        self.assertEqual(group["appendixNamePdfPage1Based"], 36)
        self.assertEqual(result["source"]["aliasToVoteTypeBinding"]["status"], "WIP_ORDERED_FORM_AND_API_LABEL_ASSOCIATION")
        self.assertFalse(result["source"]["automaticPrintedCodeToFileCodeMappingAllowed"])

    def test_source_and_scope_metadata_historical_only(self):
        result = self.build(fixture("ESS9e03_3"))
        self.assertEqual(result["source"]["election"]["year"], 2017)
        self.assertTrue(result["source"]["fieldwork"])
        self.assertEqual(result["source"]["aliasToVoteTypeBinding"]["status"], "OFFICIAL_ALIAS_EXPLICIT_TEXT_BOUND")
        self.assertFalse(result["scope"]["currentPartyPositions"])
        self.assertFalse(result["scope"]["independentNorm"])
        self.assertFalse(result["scope"]["personsOrStudiesPooled"])

    def test_byte_and_canonical_source_pins_are_different(self):
        args = list(deepcopy(self.args)); args[3]["groupContractSha256"] = _canonical_hash(args[2])
        with self.assertRaises(export.PolicyGroupExportError):self.build(args)

    def test_complete_source_mutations_and_extra_fields_rejected(self):
        for index, mutation in ((1, lambda c: c.update(extraSource="SYNTHETIC_PRIVATE_SECRET")),
                                (2, lambda c: c["sourceRights"]["responseData"].update(license="CC0")),
                                (2, lambda c: c["studies"][4]["nationalParty2Field"].update(fieldId="different")),
                                (2, lambda c: c["displayPolicy"].update(minimumValidQuestionCount=99))):
            args = list(deepcopy(self.args)); mutation(args[index])
            with self.assertRaises(export.PolicyGroupExportError) as caught:self.build(args)
            self.assertIs(caught.exception.code, export.ExportErrorCode.INVALID_CONTRACT)

    def test_candidate_hash_and_decision_study_pins(self):
        for key, value in (("candidateSha256", "0" * 64), ("studyContractSha256", "0" * 64),
                           ("groupContractSha256", "0" * 64), ("studyId", "ESS8e02_3"), ("edition", "0.0")):
            args = list(deepcopy(self.args)); args[3][key] = value
            with self.assertRaises(export.PolicyGroupExportError):self.build(args)

    def test_decision_extra_permissive_fields_and_role_paths(self):
        edits = [lambda d: d.update(extra="ALLOW"), lambda d: d.update(decision="ALLOW"),
                 lambda d: d.update(schemaVersion=True), lambda d: d["reviewers"][0].update(reportPath="reports/loop/authors/not-review.md"),
                 lambda d: d["reviewers"][1].update(role=d["reviewers"][0]["role"]),
                 lambda d: d["reviewers"][1].update(reportPath=d["reviewers"][0]["reportPath"]),
                 lambda d: d["reviewers"][0].update(decision="APPROVED")]
        for edit in edits:
            args = list(deepcopy(self.args)); edit(args[3])
            with self.assertRaises(export.PolicyGroupExportError):self.build(args)

    def test_pairs_exact_unique_same_study_and_prepared_only(self):
        for pairs in ([self.args[3]["approvedGroupQuestionIds"][0]] * 2,
                      [{"groupId": "foreign", "questionId": self.args[3]["approvedGroupQuestionIds"][0]["questionId"]}],
                      [{"groupId": self.args[3]["approvedGroupQuestionIds"][0]["groupId"], "questionId": "ESS8e02_3:gvslvol"}],
                      [{"groupId": self.args[0]["groups"][1]["group_id"], "questionId": self.args[0]["groups"][1]["questions"][0]["question_id"]}]):
            args = list(deepcopy(self.args)); args[3]["approvedGroupQuestionIds"] = pairs
            with self.assertRaises(export.PolicyGroupExportError):self.build(args)
        args = list(fixture(valid_count=99)); args[3]["approvedGroupQuestionIds"] = self.args[3]["approvedGroupQuestionIds"]
        with self.assertRaises(export.PolicyGroupExportError):self.build(args)

    def test_empty_approval_never_promotes_prepared(self):
        args = list(deepcopy(self.args)); args[3]["approvedGroupQuestionIds"] = []
        result = self.build(args)
        self.assertTrue(all(q["reference"] is None for g in result["groups"] for q in g["questions"]))

    def test_candidate_unknown_fields_private_rows_and_status_promotion(self):
        for mutation in (lambda c: c.update(_records=["SYNTHETIC_PRIVATE_SECRET"]),
                         lambda c: c["groups"][0].update(overallDistance=0),
                         lambda c: c["groups"][0]["questions"][0].update(status="reviewed_historical_reference"),
                         lambda c: c["groups"][0]["questions"][0].update(privateBase=120)):
            self.reject_candidate(mutation)

    def test_group_question_category_identity_duplicates_and_order(self):
        for mutation in (lambda c: c["groups"].append(deepcopy(c["groups"][0])),
                         lambda c: c["groups"][0].update(party2_code="66"),
                         lambda c: c["groups"][0].update(label_de_original_form="SYNTHETIC_PRIVATE_SECRET"),
                         lambda c: c["groups"][0]["questions"].reverse(),
                         lambda c: c["groups"][0]["questions"][0]["estimates"][0]["reference"]["estimates"].reverse()):
            self.reject_candidate(mutation)

    def test_invalid_and_small_basis_promotion_cannot_be_smuggled(self):
        args = list(fixture(valid_count=99)); args[0]["groups"][0]["questions"][0]["status"] = "prepared_pending_group_result_review"
        args[3]["candidateSha256"] = _canonical_hash(args[0]); args[3]["approvedGroupQuestionIds"] = self.args[3]["approvedGroupQuestionIds"]
        with self.assertRaises(export.PolicyGroupExportError):self.build(args)
        self.reject_candidate(lambda c: c["groups"][0]["questions"][0]["estimates"][0]["reference"]["accounting"].update(valid_count=True))

    def test_numeric_fraction_category_weight_and_unweighted_consistency(self):
        for mutation in (lambda c: c["groups"][0]["questions"][0]["estimates"][0]["reference"]["estimates"][0].update(proportion=0.94),
                         lambda c: c["groups"][0]["questions"][0]["estimates"][0]["reference"]["estimates"][0].update(weight=96),
                         lambda c: c["groups"][0]["questions"][0]["estimates"][2]["reference"]["estimates"][0].update(count=94),
                         lambda c: c["groups"][0]["questions"][0]["estimates"][1]["reference"]["accounting"].update(total_weight=361)):
            self.reject_candidate(mutation)

    def test_missing_reason_structural_and_group_total_consistency(self):
        for mutation in (lambda c: c["groups"][0]["questions"][0]["missing_reasons"][-1].update(count=19),
                         lambda c: c["groups"][0]["questions"][0]["missing_reasons"][-1].update(reason="Refusal"),
                         lambda c: c["groups"][0]["questions"][0]["not_asked"].update(count=1),
                         lambda c: c["groups"][0].update(eligible_case_count=119)):
            self.reject_candidate(mutation)

    def test_variance_uncertainty_zero_for_missing_and_sensitivity_invalid(self):
        for mutation in (lambda c: c["groups"][0]["questions"][0]["estimates"][0]["reference"]["estimates"][0].update(standard_error=0),
                         lambda c: c["groups"][0]["questions"][0]["estimates"][0]["reference"].update(design={}),
                         lambda c: c["groups"][1]["questions"][0]["estimates"][0]["reference"]["estimates"][0].update(proportion=0),
                         lambda c: c["groups"][0]["questions"][0]["sensitivity"].update(max_abs_primary_dweight=0.01)):
            self.reject_candidate(mutation)

    def test_eligibility_diagnostics_and_named_other_axes(self):
        for mutation in (lambda c: c["eligibility"].update(eligible_group_case_count=119),
                         lambda c: c["eligibility"]["vote_states"][0].update(count=121),
                         lambda c: c["eligibility"]["party_states"][0].update(count=0),
                         lambda c: c["eligibility"].update(non_yes_vote_with_valid_party_count=1)):
            self.reject_candidate(mutation)

    def test_ratio_scope_bounds_and_status_not_public(self):
        for mutation in (lambda c: c["study_ratio_diagnostic"].update(scope="all_DE"),
                         lambda c: c["study_ratio_diagnostic"].update(ratio_min=3, ratio_max=3),
                         lambda c: c["study_ratio_diagnostic"].update(constant_against_first_within_tolerance=False),
                         lambda c: c["study_ratio_diagnostic"].update(case_count=119)):
            self.reject_candidate(mutation)

    def test_primary_weighted_fractions_selected_sensitivities_stay_private(self):
        args = list(deepcopy(self.args))
        for question in args[0]["groups"][0]["questions"]:
            for index, scale in ((0, 1), (3, 2)):
                reference = question["estimates"][index]["reference"]
                reference["accounting"].update(valid_weight=195 * scale, eligible_weight=215 * scale, total_weight=215 * scale)
                reference["estimates"][0].update(weight=190 * scale, proportion=190 / 195)
                reference["estimates"][1].update(weight=5 * scale, proportion=5 / 195)
            difference = abs(190 / 195 - 0.95)
            question["sensitivity"].update(max_abs_primary_unweighted=difference, max_abs_primary_dweight=difference)
        args[3]["candidateSha256"] = _canonical_hash(args[0])
        result = self.build(args)
        self.assertAlmostEqual(result["groups"][0]["questions"][0]["reference"]["categories"][0]["proportion"], 190 / 195)
        self.assertEqual(result["groups"][0]["questions"][0]["reference"]["validCount"], 100)
        self.assertNotIn('"sensitivity"', json.dumps(result))

    def test_nonconstant_ratio_is_validated_but_not_published(self):
        args = list(deepcopy(self.args))
        for question in args[0]["groups"][0]["questions"]:
            reference = question["estimates"][3]["reference"]
            reference["accounting"].update(valid_weight=290, eligible_weight=330, total_weight=330)
            reference["estimates"][0].update(weight=285, proportion=285 / 290)
            reference["estimates"][1].update(weight=5, proportion=5 / 290)
            question["sensitivity"]["max_abs_primary_anweight"] = max(abs(285 / 290 - 0.95), abs(5 / 290 - 0.05))
        args[0]["study_ratio_diagnostic"].update(status="nonconstant_ratio", ratio_min=1, ratio_max=3,
                                                  constant_against_first_within_tolerance=False)
        args[3]["candidateSha256"] = _canonical_hash(args[0])
        result = self.build(args)
        self.assertEqual(result["groups"][0]["questions"][0]["reference"]["categories"][0]["proportion"], 0.95)
        self.assertNotIn("ratio_min", json.dumps(result))

    def test_unassigned_missing_and_notasked_diagnostics_do_not_escape(self):
        args = list(deepcopy(self.args)); diagnostic = args[0]["eligibility"]
        diagnostic.update(de_case_count=129, yes_vote_with_party_not_asked_count=4)
        diagnostic["vote_states"][0]["count"] = 124
        diagnostic["vote_states"][3]["count"] = 5
        diagnostic["party_states"][2]["count"] = 4
        diagnostic["party_states"][3]["count"] = 5
        diagnostic["vote_source_missing_reasons"][0]["count"] = 5
        diagnostic["party_source_missing_reasons"][0]["count"] = 5
        args[3]["candidateSha256"] = _canonical_hash(args[0])
        result = self.build(args)
        self.assertEqual(result["groups"][0]["questions"][0]["reference"]["totalCount"], 120)
        self.assertNotIn("de_case_count", json.dumps(result))

    def test_zero_categories_with_positive_valid_denominator_are_retained(self):
        result = self.build(fixture(positive_cell=0))
        categories = result["groups"][0]["questions"][0]["reference"]["categories"]
        self.assertEqual(categories[0]["proportion"], 1)
        self.assertTrue(all(item["proportion"] == 0 for item in categories[1:]))

    def test_canonical_hash_definition_order_numeric_representation(self):
        candidate = self.args[0]
        self.assertEqual(export.canonical_candidate_sha256(candidate), _canonical_hash(candidate))
        reverse = dict(reversed(list(candidate.items())))
        self.assertEqual(export.canonical_candidate_sha256(candidate), export.canonical_candidate_sha256(reverse))
        changed = deepcopy(candidate)
        changed["groups"][0]["questions"][0]["estimates"][0]["reference"]["accounting"]["valid_weight"] = 100.0
        self.assertNotEqual(export.canonical_candidate_sha256(candidate), export.canonical_candidate_sha256(changed))

    def test_nan_custom_cyclic_and_wrapper_objects_rejected(self):
        for mutation in (lambda c: c.update(extra=nan), lambda c: c.update(extra=("not", "json"))):
            altered = deepcopy(self.args[0]); mutation(altered)
            with self.assertRaises(export.PolicyGroupExportError):export.validate_group_reference_candidate(altered, self.args[1], self.args[2])
        cyclic = deepcopy(self.args[0]); cyclic["cycle"] = cyclic
        with self.assertRaises(export.PolicyGroupExportError):export.validate_group_reference_candidate(cyclic, self.args[1], self.args[2])
        with self.assertRaises(export.PolicyGroupExportError):self.build(({"candidate": self.args[0]}, *self.args[1:]))

    def test_detached_output_and_no_input_mutation(self):
        before = deepcopy(self.args); result = self.build()
        self.assertEqual(self.args, before)
        result["source"]["fieldwork"][0]["start"] = "changed only detached copy"
        result["groups"][0]["questions"][0]["reference"]["categories"][0]["proportion"] = 0
        self.assertEqual(self.args, before)

    def test_pure_module_has_no_application_io_or_access_import(self):
        tree = ast.parse((ROOT / "pipeline/policy_group_export_v21.py").read_text())
        imports = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
        self.assertNotIn("pipeline.policy_group_access_v21", imports)
        self.assertNotIn("pipeline.policy_access_v2", imports)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else ""
                self.assertNotIn(name, {"open", "read_text", "read_bytes", "write_text", "write_bytes", "run_study_reference", "run_group_reference"})


if __name__ == "__main__":
    unittest.main()
