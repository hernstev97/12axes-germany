"""Synthetic checks for pipeline/v22/survey.py. No survey data are read."""

import random
import sys
import unittest
from math import sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from pipeline.v22.survey import (  # noqa: E402
    DesignError, Unit, design_summary, estimate, logit_interval, t_quantile, weighted_shares,
)
from pipeline.policy_reference_v2 import (  # noqa: E402
    DesignUnit, Observation, VarianceStatus, categorical_reference,
)


class TQuantile(unittest.TestCase):
    def test_known_values(self):
        # Reference values of Student's t, 97.5 % quantile (tables; df 475 by Cornish-Fisher series).
        for df, expected in ((1, 12.706204736), (10, 2.228138852), (30, 2.042272456),
                             (90, 1.986674541), (475, 1.964970773), (10000, 1.960201263)):
            self.assertAlmostEqual(t_quantile(0.975, df), expected, places=6)


class Variance(unittest.TestCase):
    def test_simple_random_sample_case(self):
        # One stratum, one unit per PSU, equal weights: v = p(1-p)/(n-1).
        responses = [1] * 30 + [2] * 70
        units = [Unit(1.0, 'h', i, True, r) for i, r in enumerate(responses)]
        results, summary = estimate(units, [1, 2])
        self.assertEqual(summary.degrees_of_freedom, 99)
        self.assertAlmostEqual(results[0].share, 0.3)
        self.assertAlmostEqual(results[0].standard_error, sqrt(0.3 * 0.7 / 99))

    def test_matches_independent_codex_implementation(self):
        rng = random.Random(20261003)
        units, observations, basis = [], [], set()
        for stratum in range(12):
            for psu in range(rng.randint(2, 5)):
                basis.add((stratum, psu))
                for _ in range(rng.randint(1, 9)):
                    weight = rng.uniform(0.2, 3.0)
                    in_domain = rng.random() < 0.7
                    response = rng.choice([1, 2, 3, None]) if in_domain else None
                    units.append(Unit(weight, stratum, psu, in_domain, response))
                    observations.append(Observation(
                        response=response if in_domain else None, weight=weight,
                        eligible=in_domain, missing=in_domain and response is None,
                        design=DesignUnit(str(stratum), str(psu))))
        ours, _ = estimate(units, [1, 2, 3])
        theirs = categorical_reference(
            study_id='synthetic', question_id='q', categories=['1', '2', '3'],
            observations=[Observation(None if o.response is None else str(o.response), o.weight,
                                      o.eligible, o.missing, o.design) for o in observations],
            design_basis=[DesignUnit(str(h), str(j)) for h, j in sorted(basis)])
        self.assertIs(theirs.variance_status, VarianceStatus.COMPUTED_WRT_TAYLOR)
        for mine, other in zip(ours, theirs.estimates):
            self.assertAlmostEqual(mine.share, other.proportion, places=12)
            self.assertAlmostEqual(mine.standard_error, other.standard_error, places=12)

    def test_empty_psus_stay_in_the_design(self):
        base = [Unit(1.0, 'a', 1, True, 1), Unit(1.0, 'a', 2, True, 2),
                Unit(1.0, 'b', 3, True, 1), Unit(1.0, 'b', 4, True, 1)]
        extra = base + [Unit(1.0, 'a', 5, False, None)]
        self.assertNotAlmostEqual(estimate(base, [1, 2])[0][0].standard_error,
                                  estimate(extra, [1, 2])[0][0].standard_error)
        self.assertEqual(design_summary(extra).psus, 5)

    def test_singleton_stratum_gives_no_estimate(self):
        units = [Unit(1.0, 'a', 1, True, 1), Unit(1.0, 'a', 2, True, 2), Unit(1.0, 'b', 3, True, 1)]
        with self.assertRaises(DesignError):
            estimate(units, [1, 2])

    def test_invalid_input_is_rejected(self):
        with self.assertRaises(DesignError):
            estimate([Unit(0.0, 'a', 1, True, 1), Unit(1.0, 'a', 2, True, 1)], [1])
        with self.assertRaises(DesignError):
            weighted_shares([Unit(1.0, 'a', 1, True, 9)], [1, 2])


class Interval(unittest.TestCase):
    def test_logit_interval_properties(self):
        lower, upper = logit_interval(0.3, 0.02, 100)
        self.assertTrue(0 < lower < 0.3 < upper < 1)
        self.assertIsNone(logit_interval(0.0, 0.0, 100))
        self.assertIsNone(logit_interval(1.0, 0.0, 100))

    def test_no_interval_with_too_few_degrees_of_freedom(self):
        units = [Unit(1.0, 'h', i, True, 1 if i % 3 else 2) for i in range(10)]
        results, summary = estimate(units, [1, 2])
        self.assertEqual(summary.degrees_of_freedom, 9)
        self.assertIsNone(results[0].lower)


if __name__ == '__main__':
    unittest.main()
