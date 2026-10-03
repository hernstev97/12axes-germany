"""Synthetic hand oracles only: no file access, real items or study responses."""

import copy
import csv
from dataclasses import asdict, FrozenInstanceError
from fractions import Fraction
from io import StringIO
import unittest

from pipeline.policy_adapter_v2 import (
    AdapterDesignStatus,
    AdapterErrorCode,
    PolicyAdapterError,
    QuestionCounts,
    parse_study_csv,
)
from pipeline.policy_reference_v2 import Observation, VarianceStatus, categorical_reference


def contract(*, design=False):
    supplied = {
        "study_id": "synthetic-study-a",
        "edition": "synthetic-edition-a",
        "country": "DE",
        "country_column": "cntry",
        "id_column": "idno",
        "weight_columns": {"primary": "pspwght", "sensitivities": ["dweight", "anweight"]},
        "questions": [
            {
                "question_id": "synthetic-question-a",
                "variable": "synthetic_q",
                "categoryCodes": ["synthetic-A", "synthetic-B"],
                "missingCodes": {"synthetic-M": "synthetic-missing-reason"},
                "structurallyNotAskedCodes": ["synthetic-N"],
            }
        ],
    }
    if design:
        supplied["design_columns"] = {"stratum": "synthetic_stratum", "psu": "synthetic_psu"}
    return supplied


def csv_text(rows, *, columns=None):
    header = columns or ["cntry", "idno", "pspwght", "dweight", "anweight", "synthetic_q"]
    stream = StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(header)
    writer.writerows(rows)
    return stream.getvalue()


def row(identity="synthetic-private-key", code="synthetic-A", *, country="DE", weight="1"):
    return [country, identity, weight, "2", "4", code]


class PolicyAdapterTests(unittest.TestCase):
    def assert_safe_error(self, text, supplied, expected, forbidden=()):
        with self.assertRaises(PolicyAdapterError) as captured:
            parse_study_csv(text, supplied)
        error = captured.exception
        self.assertIs(error.code, expected)
        self.assertEqual(str(error), f"policy_adapter_error: {expected.value}")
        self.assertEqual(error.args, (f"policy_adapter_error: {expected.value}",))
        for token in forbidden:
            self.assertNotIn(token, str(error))
            self.assertNotIn(token, repr(error))
        return error

    def test_fixed_weighted_oracles_and_missing_eligibility_are_separate(self):
        # Four DE rows: valid primary weights 1+3=4, missing=2, not asked=4.
        parsed = parse_study_csv(csv_text([
            ["DE", "synthetic-key-1", " 1 ", "2", "4", "synthetic-A"],
            ["DE", "synthetic-key-2", "3", "2", "1", "synthetic-B"],
            ["DE", "synthetic-key-3", "2", "3", "3", "synthetic-M"],
            ["DE", "synthetic-key-4", "4", "4", "4", "synthetic-N"],
        ]), contract())
        self.assertEqual(parsed.diagnostics.de_row_count, 4)
        self.assertEqual(parsed.diagnostics.question_counts, (QuestionCounts(2, 1, 1),))
        self.assertEqual([
            (answer._raw_code, answer._response, answer._eligible, answer._missing, answer._missing_reason)
            for record in parsed._records for answer in record._answers
        ], [
            ("synthetic-A", "synthetic-A", True, False, None),
            ("synthetic-B", "synthetic-B", True, False, None),
            ("synthetic-M", None, True, True, "synthetic-missing-reason"),
            ("synthetic-N", None, False, False, None),
        ])
        # Independent fixed fraction oracles: A shares 1/4, 1/2 and 4/5.
        for weight_column, expected_share in [
            ("pspwght", Fraction(1, 4)), ("dweight", Fraction(1, 2)), ("anweight", Fraction(4, 5)),
        ]:
            observations = [
                Observation(
                    response=record._answers[0]._response,
                    weight=dict(record._weights)[weight_column],
                    eligible=record._answers[0]._eligible,
                    missing=record._answers[0]._missing,
                ) for record in parsed._records
            ]
            reference = categorical_reference(
                study_id=parsed._contract._study_id,
                question_id=parsed._contract._questions[0]._question_id,
                categories=parsed._contract._questions[0]._category_codes,
                observations=observations,
            )
            self.assertAlmostEqual(reference.estimates[0].proportion, float(expected_share))
            self.assertIs(reference.variance_status, VarianceStatus.NO_DESIGN_BASIS)
            if weight_column == "pspwght":
                self.assertEqual(reference.accounting.valid_weight, 4)
                self.assertEqual(reference.accounting.missing_weight, 2)
                self.assertEqual(reference.accounting.not_asked_weight, 4)
                self.assertEqual(reference.accounting.total_weight, 10)

    def test_unknown_de_code_is_fatal_and_value_free(self):
        unknown = "synthetic-sensitive-unknown-code"
        identity = "synthetic-sensitive-identity"
        self.assert_safe_error(
            csv_text([row(identity, unknown)]), contract(), AdapterErrorCode.UNKNOWN_DE_CODE,
            forbidden=(unknown, identity, "synthetic_q"),
        )

    def test_non_de_unknowns_and_bad_weights_are_not_interpreted(self):
        parsed = parse_study_csv(csv_text([
            row(code="non-DE-uninterpreted-code", country="ZZ", weight="not-a-weight"),
            row(),
            row(code="another-uninterpreted-code", country=" DE ", weight="NaN"),
        ]), contract())
        self.assertEqual(parsed.diagnostics.de_row_count, 1)
        self.assertEqual(parsed.diagnostics.question_counts, (QuestionCounts(1, 0, 0),))
        self.assertEqual(len(parsed._records), 1)

    def test_duplicate_de_identity_is_fatal_and_value_free(self):
        identity = "synthetic-sensitive-identity"
        self.assert_safe_error(csv_text([row(identity), row(identity)]), contract(),
                               AdapterErrorCode.DUPLICATE_DE_ID, forbidden=(identity,))
        # The adapter never parses IDs numerically and never trims them.
        parsed = parse_study_csv(csv_text([row("01"), row("1"), row(" 1 ")]), contract())
        self.assertEqual([record._idno for record in parsed._records], ["01", "1", " 1 "])

    def test_csv_quotes_and_original_code_strings_survive_exactly(self):
        supplied = contract()
        codes = ['synthetic,comma', 'synthetic"quote', ' synthetic-space ', 'synthetic\nline']
        supplied["questions"][0]["categoryCodes"] = codes
        parsed = parse_study_csv(csv_text([row(f"synthetic-key-{index}", code) for index, code in enumerate(codes)]), supplied)
        self.assertEqual([record._answers[0]._response for record in parsed._records], codes)
        self.assert_safe_error(csv_text([row(code="synthetic-space")]), supplied,
                               AdapterErrorCode.UNKNOWN_DE_CODE)

    def test_empty_selected_answer_requires_explicit_empty_missing_code(self):
        text = csv_text([row(code="")])
        self.assert_safe_error(text, contract(), AdapterErrorCode.UNKNOWN_DE_CODE)
        supplied = contract()
        supplied["questions"][0]["missingCodes"][""] = "synthetic-empty-reason"
        parsed = parse_study_csv(text, supplied)
        answer = parsed._records[0]._answers[0]
        self.assertEqual((answer._raw_code, answer._response, answer._eligible, answer._missing,
                          answer._missing_reason), ("", None, True, True, "synthetic-empty-reason"))
        self.assertEqual(parsed.diagnostics.question_counts, (QuestionCounts(0, 1, 0),))

    def test_headers_are_exact_unique_and_complete_with_extra_fields_discarded(self):
        base = ["cntry", "idno", "pspwght", "dweight", "anweight", "synthetic_q"]
        for header, expected in [
            (base + ["idno"], AdapterErrorCode.DUPLICATE_HEADER),
            (base + ["synthetic-extra", "synthetic-extra"], AdapterErrorCode.DUPLICATE_HEADER),
            (base + [""], AdapterErrorCode.EMPTY_HEADER),
            (base + ["  "], AdapterErrorCode.EMPTY_HEADER),
            (base[:-1], AdapterErrorCode.MISSING_REQUIRED_COLUMN),
            (["cntry "] + base[1:], AdapterErrorCode.MISSING_REQUIRED_COLUMN),
        ]:
            self.assert_safe_error(csv_text([], columns=header), contract(), expected)
        parsed = parse_study_csv(csv_text([row() + ["synthetic-extra-private-value"]],
                                         columns=base + ["synthetic-extra"]), contract())
        self.assertEqual(len(parsed._records[0]._answers), 1)
        self.assertEqual(len(parsed._records[0]._weights), 3)
        self.assertNotIn("synthetic-extra-private-value", repr(parsed))
        self.assertNotIn("synthetic-extra", parsed._records[0].__slots__)

    def test_structural_row_errors_are_global_even_for_non_de(self):
        for cells in [row()[:-1], row() + ["extra"], row(country="ZZ")[:-1], []]:
            self.assert_safe_error(csv_text([cells]), contract(), AdapterErrorCode.INVALID_ROW_WIDTH)

    def test_all_selected_weights_must_be_positive_finite_and_errors_are_safe(self):
        for position in (2, 3, 4):
            for invalid in ("0", "-1", "nan", "NaN", "inf", "-inf", "1e9999", "1e-9999", "", " ", "synthetic-secret-weight"):
                cells = row()
                cells[position] = invalid
                self.assert_safe_error(csv_text([cells]), contract(), AdapterErrorCode.INVALID_WEIGHT,
                                       forbidden=("synthetic-private-key", "synthetic-secret-weight"))
        parsed = parse_study_csv(csv_text([row(weight=" 1e-2 ")]), contract())
        self.assertEqual(dict(parsed._records[0]._weights)["pspwght"], 0.01)

    def test_missing_or_invalid_design_retains_all_ratio_records_without_se(self):
        header = ["cntry", "idno", "pspwght", "dweight", "anweight", "synthetic_q", "synthetic_stratum", "synthetic_psu"]
        text = csv_text([
            row("synthetic-k1", "synthetic-A", weight="1") + ["synthetic-s1", "synthetic-p1"],
            row("synthetic-k2", "synthetic-B", weight="3") + ["synthetic-s1", ""],
            row("synthetic-k3", "synthetic-M", weight="2") + ["   ", "synthetic-p3"],
        ], columns=header)
        parsed = parse_study_csv(text, contract(design=True))
        self.assertEqual(len(parsed._records), 3)
        self.assertEqual(parsed.diagnostics.question_counts, (QuestionCounts(2, 1, 0),))
        self.assertIs(parsed.diagnostics.design.status, AdapterDesignStatus.INCOMPLETE_IDENTIFIERS)
        self.assertFalse(parsed.diagnostics.design.identifiers_complete)
        self.assertFalse(parsed.diagnostics.design.se_available)
        self.assertEqual((parsed.diagnostics.design.observed_strata_count,
                          parsed.diagnostics.design.observed_psu_count), (1, 1))
        self.assertIsNotNone(parsed._records[0]._design)
        self.assertIsNone(parsed._records[1]._design)
        self.assertIsNone(parsed._records[2]._design)
        self.assertEqual(sum(dict(record._weights)["pspwght"] for record in parsed._records[:2]), 4)
        # A declared design column missing from the header is a schema error.
        self.assert_safe_error(csv_text([row()]), contract(design=True),
                               AdapterErrorCode.MISSING_REQUIRED_COLUMN)

    def test_complete_observed_design_does_not_claim_a_full_basis(self):
        header = ["cntry", "idno", "pspwght", "dweight", "anweight", "synthetic_q", "synthetic_stratum", "synthetic_psu"]
        parsed = parse_study_csv(csv_text([
            row("synthetic-k1") + ["synthetic-s1", "synthetic-p1"],
            row("synthetic-k2", "synthetic-N") + ["synthetic-s1", "synthetic-p2"],
            row("synthetic-k3", "synthetic-M") + ["synthetic-s2", "synthetic-p1"],
        ], columns=header), contract(design=True))
        design = parsed.diagnostics.design
        self.assertIs(design.status, AdapterDesignStatus.IDENTIFIERS_COMPLETE_UNVERIFIED_BASIS)
        self.assertTrue(design.identifiers_complete)
        self.assertFalse(design.se_available)
        self.assertEqual((design.observed_strata_count, design.observed_psu_count), (2, 3))
        self.assertEqual(parsed._records[1]._design._psu, "synthetic-p2")
        # Zero-contribution missing/unasked records survive; no basis is inferred.
        self.assertEqual(parsed.diagnostics.question_counts, (QuestionCounts(1, 1, 1),))

    def test_no_declared_design_is_explicit_and_has_no_observed_basis(self):
        parsed = parse_study_csv(csv_text([row()]), contract())
        self.assertIs(parsed.diagnostics.design.status, AdapterDesignStatus.NO_DESIGN_DECLARED)
        self.assertFalse(parsed.diagnostics.design.identifiers_complete)
        self.assertFalse(parsed.diagnostics.design.se_available)
        self.assertEqual((parsed.diagnostics.design.observed_strata_count,
                          parsed.diagnostics.design.observed_psu_count), (0, 0))
        self.assertIsNone(parsed._records[0]._design)

    def test_selected_questions_remain_distinct_with_fixed_counts_per_question(self):
        supplied = contract()
        second = copy.deepcopy(supplied["questions"][0])
        second.update(question_id="synthetic-question-b", variable="synthetic_q2")
        supplied["questions"].append(second)
        header = ["cntry", "idno", "pspwght", "dweight", "anweight", "synthetic_q", "synthetic_q2"]
        parsed = parse_study_csv(csv_text([
            row("synthetic-k1", "synthetic-A") + ["synthetic-N"],
            row("synthetic-k2", "synthetic-M") + ["synthetic-B"],
        ], columns=header), supplied)
        self.assertEqual(parsed.diagnostics.question_counts, (QuestionCounts(1, 1, 0), QuestionCounts(1, 0, 1)))
        self.assertEqual([question._question_id for question in parsed._contract._questions],
                         ["synthetic-question-a", "synthetic-question-b"])
        self.assertEqual([answer._response for answer in parsed._records[0]._answers], ["synthetic-A", None])

    def test_studies_are_separate_even_with_identical_record_and_question_ids(self):
        first_contract = contract()
        second_contract = contract()
        second_contract.update(study_id="synthetic-study-b", edition="synthetic-edition-b")
        first = parse_study_csv(csv_text([row(code="synthetic-A")]), first_contract)
        second = parse_study_csv(csv_text([row(code="synthetic-B")]), second_contract)
        self.assertEqual(first._records[0]._idno, second._records[0]._idno)
        self.assertNotEqual(first._contract._study_id, second._contract._study_id)
        self.assertEqual(first._records[0]._answers[0]._response, "synthetic-A")
        self.assertEqual(second._records[0]._answers[0]._response, "synthetic-B")
        first_contract["questions"][0]["categoryCodes"].append("later-injected")
        self.assertEqual(first._contract._questions[0]._category_codes, ("synthetic-A", "synthetic-B"))
        with self.assertRaises(FrozenInstanceError):
            first._records[0]._idno = "later-change"

    def test_public_diagnostics_and_private_repr_never_expose_keys_or_codes(self):
        supplied = contract(design=True)
        header = ["cntry", "idno", "pspwght", "dweight", "anweight", "synthetic_q", "synthetic_stratum", "synthetic_psu"]
        parsed = parse_study_csv(csv_text([
            row("synthetic-secret-id") + ["synthetic-secret-stratum", "synthetic-secret-psu"],
        ], columns=header), supplied)
        public = repr(asdict(parsed.diagnostics))
        private_reprs = [repr(parsed), repr(parsed._contract), repr(parsed._records[0]),
                         repr(parsed._records[0]._answers[0]), repr(parsed._records[0]._design)]
        for output in [public, *private_reprs]:
            for token in ["synthetic-secret-id", "synthetic-secret-stratum", "synthetic-secret-psu",
                          "synthetic-A", "synthetic-study-a", "synthetic_q", "synthetic-question-a"]:
                self.assertNotIn(token, output)

    def test_empty_no_de_bad_quotes_and_bad_identity_are_safe_failures(self):
        self.assert_safe_error("", contract(), AdapterErrorCode.EMPTY_CSV)
        self.assert_safe_error(csv_text([]), contract(), AdapterErrorCode.NO_DE_ROWS)
        self.assert_safe_error(csv_text([row(country="ZZ")]), contract(), AdapterErrorCode.NO_DE_ROWS)
        malformed = 'cntry,idno,pspwght,dweight,anweight,synthetic_q\nDE,"synthetic-secret-id,1,2,4,synthetic-A\n'
        self.assert_safe_error(malformed, contract(), AdapterErrorCode.INVALID_CSV,
                               forbidden=("synthetic-secret-id",))
        for identity in ("", "  "):
            self.assert_safe_error(csv_text([row(identity)]), contract(), AdapterErrorCode.INVALID_DE_ID)
        self.assert_safe_error(None, contract(), AdapterErrorCode.INVALID_TEXT)

    def test_contract_groups_identities_columns_and_reasons_are_strict(self):
        variants = []
        for field, value in [("study_id", ""), ("edition", ""), ("country", "ZZ"),
                             ("country_column", "country"), ("id_column", "numeric_id")]:
            supplied = contract()
            supplied[field] = value
            variants.append(supplied)
        for field, value in [("categoryCodes", []), ("categoryCodes", ["synthetic-A", "synthetic-A"]),
                             ("categoryCodes", [1]), ("categoryCodes", [""]),
                             ("missingCodes", {"synthetic-A": "reason"}),
                             ("missingCodes", {"synthetic-M": ""}),
                             ("missingCodes", {1: "reason"}),
                             ("structurallyNotAskedCodes", ["synthetic-A"]),
                             ("structurallyNotAskedCodes", ["synthetic-M"]),
                             ("structurallyNotAskedCodes", ["synthetic-N", "synthetic-N"]),
                             ("structurallyNotAskedCodes", [""]), ("variable", "idno")]:
            supplied = contract()
            supplied["questions"][0][field] = value
            variants.append(supplied)
        for value in [{"primary": "dweight", "sensitivities": ["dweight", "anweight"]},
                      {"primary": "pspwght", "sensitivities": ["dweight"]},
                      {"primary": "pspwght", "sensitivities": ["dweight", "dweight", "anweight"]}]:
            supplied = contract()
            supplied["weight_columns"] = value
            variants.append(supplied)
        for value in [{"stratum": "idno", "psu": "synthetic_psu"},
                      {"stratum": "synthetic_psu", "psu": "synthetic_psu"},
                      {"stratum": "synthetic_stratum"}]:
            supplied = contract()
            supplied["design_columns"] = value
            variants.append(supplied)
        duplicate_id = contract()
        second = copy.deepcopy(duplicate_id["questions"][0])
        second["variable"] = "synthetic_q2"
        duplicate_id["questions"].append(second)
        variants.append(duplicate_id)
        duplicate_variable = contract()
        second = copy.deepcopy(duplicate_variable["questions"][0])
        second["question_id"] = "synthetic-question-b"
        duplicate_variable["questions"].append(second)
        variants.append(duplicate_variable)
        unexpected = contract()
        unexpected["not_a_contract_field"] = "synthetic-secret-contract-value"
        variants.append(unexpected)
        incomplete = contract()
        del incomplete["edition"]
        variants.extend([incomplete, {}, None])
        for supplied in variants:
            self.assert_safe_error(csv_text([row()]), supplied, AdapterErrorCode.INVALID_CONTRACT,
                                   forbidden=("synthetic-secret-contract-value", "synthetic-private-key"))


if __name__ == "__main__":
    unittest.main()
