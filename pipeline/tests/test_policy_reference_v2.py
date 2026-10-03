"""Synthetic hand-calculation oracles; no empirical data or source validation."""

from fractions import Fraction
from math import sqrt
import unittest

from pipeline.policy_reference_v2 import (
    DesignUnit,
    Observation,
    VarianceStatus,
    categorical_reference,
)


class PolicyReferenceTests(unittest.TestCase):
    def reference(self, rows, *, basis=None, study="synthetic-study", categories=("A", "B")):
        return categorical_reference(
            study_id=study,
            question_id="synthetic-question",
            categories=categories,
            observations=rows,
            design_basis=basis,
        )

    def test_unequal_weights_and_missing_use_valid_denominator(self):
        result = self.reference([
            Observation("A", 1, True, False),
            Observation("B", 3, True, False),
            Observation(None, 5, True, True),
            Observation(None, 7, False, False),
        ])
        # Hand oracle: valid=1+3=4, eligible=4+5=9, total=9+7=16.
        a, b = result.estimates
        self.assertEqual(a.proportion, float(Fraction(1, 4)))
        self.assertEqual(b.proportion, float(Fraction(3, 4)))
        self.assertEqual((a.count, b.count, a.weight, b.weight), (1, 1, 1, 3))
        account = result.accounting
        self.assertEqual((account.total_count, account.total_weight), (4, 16))
        self.assertEqual((account.eligible_count, account.eligible_weight), (3, 9))
        self.assertEqual((account.valid_count, account.valid_weight), (2, 4))
        self.assertEqual((account.missing_count, account.missing_weight), (1, 5))
        self.assertEqual((account.not_asked_count, account.not_asked_weight), (1, 7))
        self.assertEqual(result.variance_status, VarianceStatus.NO_DESIGN_BASIS)
        self.assertIsNone(a.standard_error)
        self.assertIsNone(a.variance)

    def test_zero_domain_psus_survive_full_design_basis(self):
        basis = tuple(DesignUnit("S", psu) for psu in (1, 2, 3, 4))
        result = self.reference([
            Observation("A", 1, True, False, basis[0]),
            Observation("B", 3, True, False, basis[1]),
            Observation(None, 5, True, True, basis[2]),
            Observation(None, 7, False, False, basis[3]),
        ], basis=basis)
        # p_A=1/4, W=4, u=(3/16,-3/16,0,0), mean=0.
        # V=(4/3)*(9/256+9/256)=3/32, not the two-PSU value 9/64.
        expected = float(Fraction(3, 32))
        self.assertEqual(result.variance_status, VarianceStatus.COMPUTED_WRT_TAYLOR)
        self.assertEqual(result.design.basis, basis)
        self.assertEqual(result.design.stratum_psu_counts, (("S", 4),))
        for estimate in result.estimates:
            self.assertAlmostEqual(estimate.variance, expected)
            self.assertAlmostEqual(estimate.standard_error, sqrt(expected))

    def test_psus_without_any_observation_survive(self):
        basis = tuple(DesignUnit("S", psu) for psu in (1, 2, 3, 4, 5))
        result = self.reference([
            Observation("A", 1, True, False, basis[0]),
            Observation("B", 3, True, False, basis[1]),
        ], basis=basis)
        # u=(3/16,-3/16,0,0,0); V=(5/4)*(18/256)=45/512.
        self.assertEqual(len(result.design.basis), 5)
        self.assertAlmostEqual(result.estimates[0].variance, float(Fraction(45, 512)))

    def test_two_strata_with_different_psu_counts(self):
        basis = (
            DesignUnit("X", 1), DesignUnit("X", 2),
            DesignUnit("Y", 1), DesignUnit("Y", 2), DesignUnit("Y", 3),
        )
        result = self.reference([
            Observation("A", 1, True, False, basis[0]),
            Observation("B", 1, True, False, basis[1]),
            Observation("A", 2, True, False, basis[2]),
            Observation("B", 2, True, False, basis[3]),
        ], basis=basis)
        # W=6, p=1/2. X: u=(1/12,-1/12), V_X=1/36.
        # Y: u=(1/6,-1/6,0), V_Y=1/12. Total V=1/9, SE=1/3.
        self.assertEqual(result.estimates[0].proportion, float(Fraction(1, 2)))
        self.assertAlmostEqual(result.estimates[0].variance, float(Fraction(1, 9)))
        self.assertAlmostEqual(result.estimates[0].standard_error, float(Fraction(1, 3)))
        self.assertEqual(result.design.stratum_psu_counts, (("X", 2), ("Y", 3)))

    def test_stratum_centering_with_nonzero_stratum_means(self):
        basis = (
            DesignUnit("X", 1), DesignUnit("X", 2),
            DesignUnit("Y", 1), DesignUnit("Y", 2),
        )
        result = self.reference([
            Observation("A", 1, True, False, basis[0]),
            Observation("A", 1, True, False, basis[1]),
            Observation("B", 1, True, False, basis[2]),
            Observation("B", 3, True, False, basis[3]),
        ], basis=basis)
        # W=6, p_A=1/3. X: u=(1/9,1/9), mean=1/9, V_X=0.
        # Y: u=(-1/18,-1/6), mean=-1/9; deviations=(1/18,-1/18).
        # V_Y=2*(2/324)=1/81, SE=1/9. Uncentered squares differ.
        self.assertEqual(result.estimates[0].proportion, float(Fraction(1, 3)))
        self.assertAlmostEqual(result.estimates[0].variance, float(Fraction(1, 81)))
        self.assertAlmostEqual(result.estimates[0].standard_error, float(Fraction(1, 9)))

    def test_separate_studies_and_questions_keep_separate_references(self):
        first = self.reference([
            Observation("A", 1, True, False), Observation("B", 3, True, False),
        ], study="synthetic-one")
        second = categorical_reference(
            study_id="synthetic-two", question_id="different-question",
            categories=("A", "B"),
            observations=[Observation("A", 3, True, False), Observation("B", 1, True, False)],
        )
        self.assertEqual((first.study_id, second.study_id), ("synthetic-one", "synthetic-two"))
        self.assertEqual((first.question_id, second.question_id), ("synthetic-question", "different-question"))
        self.assertEqual(first.estimates[0].proportion, float(Fraction(1, 4)))
        self.assertEqual(second.estimates[0].proportion, float(Fraction(3, 4)))
        self.assertEqual((first.accounting.valid_weight, second.accounting.valid_weight), (4, 4))

    def test_singleton_stratum_has_no_variance_even_with_zero_domain_contribution(self):
        basis = (DesignUnit("X", 1), DesignUnit("X", 2), DesignUnit("Y", 1))
        result = self.reference([
            Observation("A", 1, True, False, basis[0]),
            Observation("B", 3, True, False, basis[1]),
        ], basis=basis)
        self.assertEqual(result.variance_status, VarianceStatus.SINGLETON_STRATUM)
        self.assertEqual(result.design.singleton_strata, ("Y",))
        self.assertIsNone(result.estimates[0].variance)
        self.assertIsNone(result.estimates[0].standard_error)
        self.assertEqual(result.estimates[0].proportion, float(Fraction(1, 4)))

    def test_missing_design_identifier_prevents_variance(self):
        basis = (DesignUnit("S", 1), DesignUnit("S", 2))
        result = self.reference([
            Observation("A", 1, True, False, basis[0]),
            Observation("B", 3, True, False, basis[1]),
            Observation(None, 5, True, True),
        ], basis=basis)
        self.assertEqual(result.variance_status, VarianceStatus.INCOMPLETE_DESIGN_IDENTIFIERS)
        self.assertEqual(result.design.observations_without_design, 1)
        self.assertIsNone(result.estimates[0].standard_error)

    def test_observation_identifiers_do_not_reconstruct_design_basis(self):
        result = self.reference([
            Observation("A", 1, True, False, DesignUnit("S", 1)),
            Observation("B", 3, True, False, DesignUnit("S", 2)),
        ])
        self.assertEqual(result.variance_status, VarianceStatus.NO_DESIGN_BASIS)
        self.assertIsNone(result.design)
        self.assertIsNone(result.estimates[0].variance)

    def test_no_valid_responses_is_not_zero_share(self):
        result = self.reference([
            Observation(None, 5, True, True), Observation(None, 7, False, False),
        ])
        self.assertEqual(result.accounting.valid_weight, 0)
        self.assertEqual(result.variance_status, VarianceStatus.NO_VALID_RESPONSES)
        for estimate in result.estimates:
            self.assertEqual((estimate.count, estimate.weight), (0, 0))
            self.assertIsNone(estimate.proportion)
            self.assertIsNone(estimate.variance)
            self.assertIsNone(estimate.standard_error)

    def test_unused_original_category_has_zero_share_when_denominator_exists(self):
        result = self.reference([Observation("A", 2, True, False)], categories=("B", "A", "C"))
        self.assertEqual(tuple(x.category for x in result.estimates), ("B", "A", "C"))
        self.assertEqual(tuple(x.proportion for x in result.estimates), (0, 1, 0))

    def test_empty_observation_set_is_explicit(self):
        result = self.reference([])
        self.assertEqual((result.accounting.total_count, result.accounting.total_weight), (0, 0))
        self.assertEqual(result.variance_status, VarianceStatus.NO_VALID_RESPONSES)

    def test_invalid_weights_raise(self):
        for weight in (0, -1, float("nan"), float("inf"), -float("inf"), True, "1"):
            with self.subTest(weight=repr(weight)), self.assertRaises(ValueError):
                self.reference([Observation("A", weight, True, False)])

    def test_finite_weights_with_overflowing_total_raise(self):
        with self.assertRaises(ValueError):
            self.reference([Observation("A", 1e308, True, False), Observation("B", 1e308, True, False)])

    def test_unknown_response_is_never_silently_missing_or_unasked(self):
        for eligible, missing in ((True, False), (True, True), (False, False)):
            with self.subTest(eligible=eligible, missing=missing), self.assertRaisesRegex(ValueError, "unexpected response"):
                self.reference([Observation("unexpected", 1, eligible, missing)])

    def test_contradictory_or_implicit_missingness_raises(self):
        for row in (
            Observation(None, 1, True, False),
            Observation("A", 1, True, True),
            Observation("A", 1, False, False),
            Observation(None, 1, False, True),
            Observation("A", 1, 1, False),
            Observation("A", 1, True, 0),
        ):
            with self.subTest(row=row), self.assertRaises(ValueError):
                self.reference([row])

    def test_invalid_original_categories_raise(self):
        for categories in ((), ("A", "A"), (1, 1.0), (None,), (True,), (float("nan"),)):
            with self.subTest(categories=categories), self.assertRaises(ValueError):
                self.reference([], categories=categories)

    def test_invalid_design_basis_or_unknown_pair_raises(self):
        unit = DesignUnit("S", 1)
        for basis in ((), (unit, unit), (DesignUnit(None, 1),)):
            with self.subTest(basis=basis), self.assertRaises(ValueError):
                self.reference([], basis=basis)
        with self.assertRaisesRegex(ValueError, "outside"):
            self.reference([Observation("A", 1, True, False, DesignUnit("S", 3))],
                           basis=(unit, DesignUnit("S", 2)))

    def test_absent_study_or_question_identity_raises(self):
        for study, question in (("", "q"), ("s", " "), (None, "q")):
            with self.subTest(study=study, question=question), self.assertRaises(ValueError):
                categorical_reference(study_id=study, question_id=question,
                                      categories=("A",), observations=[])
