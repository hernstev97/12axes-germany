"""Synthetic fixed-oracle tests only; no actual file, item or response data."""

import copy
import csv
from dataclasses import asdict, FrozenInstanceError, replace
from fractions import Fraction
from io import StringIO
import json
from math import fsum, isfinite
import unittest

from pipeline.policy_adapter_v2 import parse_study_csv
from pipeline.policy_analysis_v2 import (
    AnalysisErrorCode,
    PolicyAnalysisError,
    PreparationStatus,
    expose_prepared_candidate,
    prepare_study_references,
)
from pipeline.policy_reference_v2 import VarianceStatus


def contract(*, study="synthetic-study-a", edition="synthetic-edition-a", second=False, design=False):
    supplied = {
        "study_id": study, "edition": edition, "country": "DE", "country_column": "cntry", "id_column": "idno",
        "weight_columns": {"primary": "pspwght", "sensitivities": ["dweight", "anweight"]},
        "questions": [{
            "question_id": "synthetic-question-1", "variable": "synthetic_q1",
            "categoryCodes": ["synthetic-A", "synthetic-B", "synthetic-zero"],
            "missingCodes": {
                "private-missing-cell-1": "synthetic-reason-1",
                "private-missing-cell-2": "synthetic-reason-2",
                "private-missing-cell-3": "synthetic-reason-1",
            },
            "structurallyNotAskedCodes": ["private-notasked-cell"],
        }],
    }
    if second:
        question = copy.deepcopy(supplied["questions"][0])
        question.update(question_id="synthetic-question-2", variable="synthetic_q2")
        supplied["questions"].append(question)
    if design:
        supplied["design_columns"] = {"stratum": "private_design_stratum", "psu": "private_design_psu"}
    return supplied


def row(index, code, primary, dweight, anweight, *, second=None, design=False):
    cells = ["DE", f"private-record-{index}", str(primary), str(dweight), str(anweight), code]
    if second is not None:
        cells.append(second)
    if design:
        cells.extend(["private-stratum-key", f"private-psu-key-{index}"])
    return cells


def valid_rows(n=100, a_count=30, *, scale=1.0, second=False, design=False):
    # Fixed weights: A has (primary,dweight,anweight)=(2,1,4), B=(1,2,2).
    return [row(index, "synthetic-A" if index < a_count else "synthetic-B",
                (2 if index < a_count else 1) * scale,
                (1 if index < a_count else 2) * scale,
                (4 if index < a_count else 2) * scale,
                second=("synthetic-A" if index < 60 else "private-missing-cell-1") if second else None,
                design=design)
            for index in range(n)]


def parsed(rows, supplied=None):
    selected = contract() if supplied is None else supplied
    header = ["cntry", "idno", "pspwght", "dweight", "anweight"]
    header += [question["variable"] for question in selected["questions"]]
    if selected.get("design_columns"):
        header += [selected["design_columns"]["stratum"], selected["design_columns"]["psu"]]
    stream = StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(header)
    writer.writerows(rows)
    return parse_study_csv(stream.getvalue(), selected)


def references(question):
    return {estimate.weight: estimate.reference for estimate in question.estimates}


class PolicyAnalysisTests(unittest.TestCase):
    def assert_safe_error(self, call, code, forbidden=()):
        with self.assertRaises(PolicyAnalysisError) as captured:
            call()
        error = captured.exception
        self.assertIs(error.code, code)
        self.assertEqual(str(error), f"policy_analysis_error: {code.value}")
        self.assertEqual(error.args, (f"policy_analysis_error: {code.value}",))
        for token in forbidden:
            self.assertNotIn(token, str(error))
            self.assertNotIn(token, repr(error))

    def test_100_cases_fixed_fraction_oracles_four_weights_zero_original_category(self):
        prepared = prepare_study_references(parsed(valid_rows()))
        question = prepared.questions[0]
        self.assertIs(question.status, PreparationStatus.PREPARED_PENDING_RESULT_REVIEW)
        self.assertEqual([(estimate.weight, estimate.role) for estimate in question.estimates], [
            ("pspwght", "primary"), ("dweight", "sensitivity"),
            ("unweighted", "sensitivity"), ("anweight", "equivalence_diagnostic"),
        ])
        # Hand sums: 60/(60+70)=6/13; 30/(30+140)=3/17; 30/100=3/10.
        for weight, first_share, total in [
            ("pspwght", Fraction(6, 13), 130), ("dweight", Fraction(3, 17), 170),
            ("unweighted", Fraction(3, 10), 100), ("anweight", Fraction(6, 13), 260),
        ]:
            reference = references(question)[weight]
            self.assertEqual([estimate.count for estimate in reference.estimates], [30, 70, 0])
            self.assertAlmostEqual(reference.estimates[0].proportion, float(first_share))
            self.assertAlmostEqual(reference.estimates[1].proportion, float(1 - first_share))
            self.assertEqual(reference.estimates[2].proportion, 0.0)
            self.assertEqual(reference.estimates[2].category, "synthetic-zero")
            self.assertEqual(reference.accounting.valid_weight, total)
            self.assertEqual(reference.accounting.valid_count, 100)
            self.assertAlmostEqual(fsum(estimate.proportion for estimate in reference.estimates), 1.0)
            self.assertTrue(all(isfinite(estimate.proportion) and 0 <= estimate.proportion <= 1 for estimate in reference.estimates))
            self.assertIs(reference.variance_status, VarianceStatus.NO_DESIGN_BASIS)
            self.assertIsNone(reference.design)
            self.assertTrue(all(estimate.variance is None and estimate.standard_error is None for estimate in reference.estimates))
        diagnostics = question.weight_diagnostics
        self.assertAlmostEqual(diagnostics.max_abs_primary_unweighted, float(Fraction(21, 130)))
        self.assertAlmostEqual(diagnostics.max_abs_primary_dweight, float(Fraction(63, 221)))
        self.assertEqual(diagnostics.max_abs_primary_anweight, 0.0)
        self.assertEqual((diagnostics.all_de_anweight_pspwght_ratio_min,
                          diagnostics.all_de_anweight_pspwght_ratio_max), (2.0, 2.0))
        candidate = expose_prepared_candidate(prepared)
        item = candidate["questions"][0]
        self.assertEqual(item["status"], "prepared_pending_result_review")
        self.assertEqual(item["category_counts"], [
            {"code": "synthetic-A", "count": 30}, {"code": "synthetic-B", "count": 70},
            {"code": "synthetic-zero", "count": 0},
        ])
        self.assertEqual(item["reference"]["variance_status"], "no_design_basis")
        self.assertNotIn("standard_error", json.dumps(candidate))
        json.dumps(candidate, allow_nan=False)

    def test_base_count_99_withholds_candidate_but_retains_private_estimates_and_item(self):
        prepared = prepare_study_references(parsed(valid_rows(n=99)))
        question = prepared.questions[0]
        self.assertIs(question.status, PreparationStatus.WITHHELD_BASE_OR_CELL_COUNT)
        self.assertAlmostEqual(references(question)["pspwght"].estimates[0].proportion, float(Fraction(20, 43)))
        candidate = expose_prepared_candidate(prepared)
        self.assertEqual(len(candidate["questions"]), 1)
        self.assertIsNone(candidate["questions"][0]["reference"])
        self.assertEqual(candidate["questions"][0]["primary_accounting"]["valid_count"], 99)
        self.assertNotIn("proportion", json.dumps(candidate))
        self.assertNotIn("max_abs", json.dumps(candidate))

    def test_positive_cell_four_withheld_five_prepared_and_zero_kept(self):
        for count, expected_status, expected_share in [
            (4, PreparationStatus.WITHHELD_BASE_OR_CELL_COUNT, Fraction(1, 13)),
            (5, PreparationStatus.PREPARED_PENDING_RESULT_REVIEW, Fraction(2, 21)),
            (0, PreparationStatus.PREPARED_PENDING_RESULT_REVIEW, Fraction(0, 1)),
        ]:
            prepared = prepare_study_references(parsed(valid_rows(a_count=count)))
            question = prepared.questions[0]
            self.assertIs(question.status, expected_status)
            self.assertAlmostEqual(references(question)["pspwght"].estimates[0].proportion, float(expected_share))
            item = expose_prepared_candidate(prepared)["questions"][0]
            self.assertEqual(item["category_counts"][0]["count"], count)
            self.assertEqual(item["category_counts"][2]["count"], 0)
            self.assertEqual(item["reference"] is not None,
                             expected_status is PreparationStatus.PREPARED_PENDING_RESULT_REVIEW)

    def test_no_valid_answers_has_no_proportions_and_missing_notasked_independent(self):
        data = [row(0, "private-missing-cell-1", 2, 1, 4),
                row(1, "private-missing-cell-3", 3, 1, 6),
                row(2, "private-missing-cell-2", 5, 1, 10),
                row(3, "private-notasked-cell", 7, 1, 14)]
        prepared = prepare_study_references(parsed(data))
        question = prepared.questions[0]
        self.assertIs(question.status, PreparationStatus.NO_VALID_ANSWERS)
        for reference in references(question).values():
            self.assertIs(reference.variance_status, VarianceStatus.NO_VALID_RESPONSES)
            self.assertTrue(all(estimate.proportion is None for estimate in reference.estimates))
            self.assertEqual(reference.accounting.valid_count, 0)
        primary = references(question)["pspwght"].accounting
        self.assertEqual((primary.total_count, primary.total_weight, primary.eligible_count,
                          primary.eligible_weight, primary.missing_count, primary.missing_weight,
                          primary.not_asked_count, primary.not_asked_weight), (4, 17, 3, 10, 3, 10, 1, 7))
        self.assertEqual([(reason.reason, reason.count, reason.primary_weight_sum) for reason in question.missing_reasons],
                         [("synthetic-reason-1", 2, 5), ("synthetic-reason-2", 1, 5)])
        self.assertIsNone(question.weight_diagnostics.max_abs_primary_unweighted)
        item = expose_prepared_candidate(prepared)["questions"][0]
        self.assertEqual(item["status"], "no_valid_answers")
        self.assertIsNone(item["reference"])
        self.assertNotIn("proportion", json.dumps(item))

    def test_reason_aggregation_uses_all_de_cases_and_separate_primary_denominators(self):
        data = valid_rows() + [row(100, "private-missing-cell-1", 3, 1, 6),
                               row(101, "private-missing-cell-3", 5, 1, 10),
                               row(102, "private-missing-cell-2", 7, 1, 14),
                               row(103, "private-notasked-cell", 11, 1, 22)]
        prepared = prepare_study_references(parsed(data))
        question = prepared.questions[0]
        primary = references(question)["pspwght"].accounting
        self.assertEqual((primary.total_count, primary.total_weight, primary.eligible_count,
                          primary.eligible_weight, primary.valid_count, primary.valid_weight,
                          primary.missing_count, primary.missing_weight,
                          primary.not_asked_count, primary.not_asked_weight), (104, 156, 103, 145, 100, 130, 3, 15, 1, 11))
        self.assertEqual([(reason.reason, reason.count, reason.primary_weight_sum) for reason in question.missing_reasons],
                         [("synthetic-reason-1", 2, 8), ("synthetic-reason-2", 1, 7)])
        item = expose_prepared_candidate(prepared)["questions"][0]
        self.assertIsNotNone(item["reference"])
        self.assertEqual(item["not_asked"], {"count": 1, "primary_weight_sum": 11.0})
        self.assertEqual(item["missing_reasons"], [
            {"reason": "synthetic-reason-1", "count": 2, "primary_weight_sum": 8.0},
            {"reason": "synthetic-reason-2", "count": 1, "primary_weight_sum": 7.0},
        ])
        self.assertAlmostEqual(item["reference"]["estimates"]["pspwght"]["categories"][0]["proportion"], float(Fraction(6, 13)))

    def test_two_questions_preserve_separate_denominators_and_contract_order(self):
        prepared = prepare_study_references(parsed(valid_rows(second=True), contract(second=True)))
        self.assertEqual([question.question_id for question in prepared.questions],
                         ["synthetic-question-1", "synthetic-question-2"])
        first, second = prepared.questions
        self.assertEqual(references(first)["pspwght"].accounting.valid_weight, 130)
        self.assertEqual(references(second)["pspwght"].accounting.valid_weight, 90)
        self.assertEqual(references(second)["pspwght"].accounting.missing_weight, 40)
        self.assertEqual(references(second)["pspwght"].accounting.valid_count, 60)
        self.assertEqual(references(second)["pspwght"].estimates[0].proportion, 1.0)
        self.assertIs(second.status, PreparationStatus.WITHHELD_BASE_OR_CELL_COUNT)
        candidate = expose_prepared_candidate(prepared)
        self.assertIsNotNone(candidate["questions"][0]["reference"])
        self.assertIsNone(candidate["questions"][1]["reference"])
        self.assertEqual(candidate["questions"][1]["category_counts"], [
            {"code": "synthetic-A", "count": 60}, {"code": "synthetic-B", "count": 0},
            {"code": "synthetic-zero", "count": 0},
        ])

    def test_studies_with_repeated_person_and_question_keys_are_separate(self):
        first = prepare_study_references(parsed(valid_rows()))
        second = prepare_study_references(parsed(valid_rows(a_count=70),
                                                 contract(study="synthetic-study-b", edition="synthetic-edition-b")))
        self.assertEqual(first.questions[0].question_id, second.questions[0].question_id)
        self.assertEqual((first.study_id, second.study_id), ("synthetic-study-a", "synthetic-study-b"))
        self.assertAlmostEqual(references(first.questions[0])["pspwght"].estimates[0].proportion, float(Fraction(6, 13)))
        self.assertAlmostEqual(references(second.questions[0])["pspwght"].estimates[0].proportion, float(Fraction(14, 17)))
        self.assertEqual(expose_prepared_candidate(second)["questions"][0]["source"], {
            "study_id": "synthetic-study-b", "edition": "synthetic-edition-b", "question_id": "synthetic-question-1",
        })
        self.assert_safe_error(lambda: prepare_study_references([first, second]), AnalysisErrorCode.INVALID_PARSED_INPUT)

    def test_design_never_reconstructed_or_exposed_even_with_complete_observed_pairs(self):
        prepared = prepare_study_references(parsed(valid_rows(design=True), contract(design=True)))
        for estimate in prepared.questions[0].estimates:
            self.assertIsNone(estimate.reference.design)
            self.assertIs(estimate.reference.variance_status, VarianceStatus.NO_DESIGN_BASIS)
            self.assertTrue(all(category.variance is None and category.standard_error is None for category in estimate.reference.estimates))
        serialized = json.dumps(expose_prepared_candidate(prepared))
        self.assertNotIn("private-stratum-key", serialized)
        self.assertNotIn("private-psu-key", serialized)
        self.assertNotIn("standard_error", serialized)
        incomplete_rows = valid_rows(design=True)
        incomplete_rows[0][7] = ""
        incomplete = prepare_study_references(parsed(incomplete_rows, contract(design=True)))
        self.assertEqual(expose_prepared_candidate(incomplete), expose_prepared_candidate(prepared))

    def test_anweight_diagnostic_and_all_de_ratio_extrema_are_descriptive_only(self):
        data = [row(index, "synthetic-A" if index < 30 else "synthetic-B",
                    2 if index < 30 else 1, 1 if index < 30 else 2,
                    3 if index < 30 else 4) for index in range(100)]
        data += [row(100, "private-missing-cell-1", 1, 1, 10),
                 row(101, "private-notasked-cell", 4, 1, 1)]
        prepared = prepare_study_references(parsed(data))
        question = prepared.questions[0]
        # 90/(90+280)=9/37; |6/13-9/37|=105/481.
        self.assertAlmostEqual(references(question)["anweight"].estimates[0].proportion, float(Fraction(9, 37)))
        self.assertAlmostEqual(question.weight_diagnostics.max_abs_primary_anweight, float(Fraction(105, 481)))
        self.assertEqual((question.weight_diagnostics.all_de_anweight_pspwght_ratio_min,
                          question.weight_diagnostics.all_de_anweight_pspwght_ratio_max), (0.25, 10.0))
        item = expose_prepared_candidate(prepared)["questions"][0]
        self.assertEqual(item["reference"]["anweight_equivalence_diagnostic"]["ratio_scope"], "all_de_cases")
        self.assertNotIn("equivalence_passed", json.dumps(item))
        self.assertIs(question.status, PreparationStatus.PREPARED_PENDING_RESULT_REVIEW)

    def test_no_raw_id_missing_cell_design_key_or_records_in_candidate_or_repr(self):
        data = valid_rows(design=True) + [row(100, "private-missing-cell-1", 3, 1, 6, design=True),
                                         row(101, "private-notasked-cell", 7, 1, 14, design=True)]
        prepared = prepare_study_references(parsed(data, contract(design=True)))
        outputs = [json.dumps(expose_prepared_candidate(prepared)), repr(prepared),
                   repr(prepared.questions[0]), repr(prepared.questions[0].estimates[0]), repr(asdict(prepared))]
        for output in outputs:
            for forbidden in ("private-record-", "private-missing-cell", "private-notasked-cell",
                              "private-stratum-key", "private-psu-key", "_records", "_raw_code", "idno"):
                self.assertNotIn(forbidden, output)
        self.assertFalse(hasattr(prepared, "_records"))
        self.assertFalse(hasattr(prepared, "_contract"))

    def test_common_weight_scaling_and_row_permutation_preserve_fractions_and_metadata(self):
        base = prepare_study_references(parsed(valid_rows()))
        base_candidate = expose_prepared_candidate(base)
        permuted = valid_rows()[::2] + valid_rows()[1::2]
        self.assertEqual(expose_prepared_candidate(prepare_study_references(parsed(permuted))), base_candidate)
        for scale in (0.25, 3.0, 1e-200, 1e200):
            prepared = prepare_study_references(parsed(valid_rows(scale=scale)))
            question = prepared.questions[0]
            self.assertEqual((prepared.study_id, prepared.edition, question.question_id, question.status),
                             (base.study_id, base.edition, base.questions[0].question_id, base.questions[0].status))
            for weight, expected_share in [("pspwght", Fraction(6, 13)), ("dweight", Fraction(3, 17)),
                                           ("unweighted", Fraction(3, 10)), ("anweight", Fraction(6, 13))]:
                self.assertAlmostEqual(references(question)[weight].estimates[0].proportion, float(expected_share))
                self.assertEqual([estimate.count for estimate in references(question)[weight].estimates], [30, 70, 0])
            self.assertAlmostEqual(question.weight_diagnostics.max_abs_primary_unweighted, float(Fraction(21, 130)))
            self.assertEqual(question.weight_diagnostics.all_de_anweight_pspwght_ratio_min, 2.0)
            self.assertAlmostEqual(references(question)["pspwght"].accounting.valid_weight / scale, 130.0)

    def test_contract_category_order_and_weight_metadata_order_are_respected(self):
        supplied = contract()
        supplied["questions"][0]["categoryCodes"] = ["synthetic-zero", "synthetic-B", "synthetic-A"]
        supplied["weight_columns"]["sensitivities"] = ["anweight", "dweight"]
        prepared = prepare_study_references(parsed(valid_rows(), supplied))
        primary = references(prepared.questions[0])["pspwght"]
        self.assertEqual([estimate.category for estimate in primary.estimates],
                         ["synthetic-zero", "synthetic-B", "synthetic-A"])
        self.assertEqual([estimate.count for estimate in primary.estimates], [0, 70, 30])
        self.assertAlmostEqual(primary.estimates[2].proportion, float(Fraction(6, 13)))
        self.assertAlmostEqual(references(prepared.questions[0])["dweight"].estimates[2].proportion, float(Fraction(3, 17)))

    def test_candidate_has_closed_allowlist_and_mutation_cannot_change_preparation(self):
        prepared = prepare_study_references(parsed(valid_rows()))
        candidate = expose_prepared_candidate(prepared)
        self.assertEqual(set(candidate), {"schema", "study_id", "edition", "questions"})
        item = candidate["questions"][0]
        self.assertEqual(set(item), {"source", "status", "category_counts", "primary_accounting",
                                     "missing_reasons", "not_asked", "reference"})
        self.assertEqual(set(item["source"]), {"study_id", "edition", "question_id"})
        self.assertEqual(set(item["primary_accounting"]), {
            "total_count", "total_weight", "eligible_count", "eligible_weight", "valid_count", "valid_weight",
            "missing_count", "missing_weight", "not_asked_count", "not_asked_weight",
        })
        self.assertEqual(set(item["reference"]), {"variance_status", "estimates", "sensitivity", "anweight_equivalence_diagnostic"})
        self.assertEqual(set(item["reference"]["estimates"]), {"pspwght", "dweight", "unweighted", "anweight"})
        self.assertEqual(set(item["reference"]["estimates"]["pspwght"]), {"role", "accounting", "categories"})
        self.assertEqual(set(item["reference"]["estimates"]["pspwght"]["categories"][0]), {"code", "count", "weight_sum", "proportion"})
        item["status"] = "published"
        item["source"]["study_id"] = "changed"
        item["reference"]["estimates"]["pspwght"]["categories"][0]["proportion"] = 0.99
        regenerated = expose_prepared_candidate(prepared)
        self.assertEqual(regenerated["questions"][0]["status"], "prepared_pending_result_review")
        self.assertAlmostEqual(regenerated["questions"][0]["reference"]["estimates"]["pspwght"]["categories"][0]["proportion"], float(Fraction(6, 13)))
        self.assert_safe_error(lambda: expose_prepared_candidate({**candidate, "unknown": "private-secret"}),
                               AnalysisErrorCode.INVALID_PREPARED_INPUT, ("private-secret",))
        with self.assertRaises(FrozenInstanceError):
            prepared.questions[0].status = PreparationStatus.NO_VALID_ANSWERS

    def test_fake_parsed_payload_flags_codes_weights_and_duplicate_ids_are_safe_errors(self):
        actual = parsed(valid_rows())
        self.assert_safe_error(lambda: prepare_study_references({"idno": "private-secret-id"}),
                               AnalysisErrorCode.INVALID_PARSED_INPUT, ("private-secret-id",))
        self.assert_safe_error(lambda: prepare_study_references(None), AnalysisErrorCode.INVALID_PARSED_INPUT)
        invalids = [replace(actual, _contract={"study_id": "private-secret-contract"}),
                    replace(actual, _records=list(actual._records)), replace(actual, _records=())]
        first = actual._records[0]
        invalid_answer = replace(first._answers[0], _raw_code="private-bogus-cell", _response="private-bogus-cell")
        invalids.append(replace(actual, _records=(replace(first, _answers=(invalid_answer,)), *actual._records[1:])))
        invalid_answer = replace(first._answers[0], _eligible=False)
        invalids.append(replace(actual, _records=(replace(first, _answers=(invalid_answer,)), *actual._records[1:])))
        invalid_weight = replace(first, _weights=(("pspwght", "private-bogus-weight"), ("dweight", 1.0), ("anweight", 4.0)))
        invalids.append(replace(actual, _records=(invalid_weight, *actual._records[1:])))
        duplicate = replace(actual._records[1], _idno=first._idno)
        invalids.append(replace(actual, _records=(first, duplicate, *actual._records[2:])))
        for invalid in invalids:
            self.assert_safe_error(lambda: prepare_study_references(invalid), AnalysisErrorCode.INVALID_PARSED_INPUT,
                                   ("private-record-0", "private-bogus-cell", "private-bogus-weight", "private-secret-contract"))

    def test_generic_arithmetic_failure_is_value_free(self):
        huge = [row(index, "synthetic-A", 1e308, 1, 1e308) for index in range(100)]
        actual = parsed(huge)
        self.assert_safe_error(lambda: prepare_study_references(actual), AnalysisErrorCode.ARITHMETIC_FAILURE,
                               ("private-record-0", "synthetic-A", "1e308"))

    def test_candidate_refuses_fake_release_status_count_override_and_nonfinite_aggregate(self):
        actual = prepare_study_references(parsed(valid_rows()))
        invalid_status = replace(actual.questions[0], status="published")
        self.assert_safe_error(lambda: expose_prepared_candidate(replace(actual, questions=(invalid_status,))),
                               AnalysisErrorCode.INVALID_PREPARED_INPUT)
        withheld = prepare_study_references(parsed(valid_rows(n=99)))
        fake_eligible = replace(withheld.questions[0], status=PreparationStatus.PREPARED_PENDING_RESULT_REVIEW)
        self.assert_safe_error(lambda: expose_prepared_candidate(replace(withheld, questions=(fake_eligible,))),
                               AnalysisErrorCode.INVALID_PREPARED_INPUT)
        first = actual.questions[0].estimates[0]
        category = replace(first.reference.estimates[0], proportion=float("nan"))
        reference = replace(first.reference, estimates=(category, *first.reference.estimates[1:]))
        fake_estimates = (replace(first, reference=reference), *actual.questions[0].estimates[1:])
        fake_question = replace(actual.questions[0], estimates=fake_estimates)
        self.assert_safe_error(lambda: expose_prepared_candidate(replace(actual, questions=(fake_question,))),
                               AnalysisErrorCode.INVALID_PREPARED_INPUT)


if __name__ == "__main__":
    unittest.main()
