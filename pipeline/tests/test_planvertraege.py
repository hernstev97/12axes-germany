"""Gegenfälle für vorgeschlagene Regeln; ausschließlich erfundene Eingaben."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("planvertraege", Path(__file__).resolve().parents[1] / "synthetic/planvertraege.py")
contracts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contracts)


class PlanContractsTests(unittest.TestCase):
    def test_equal_weight_quantiles_and_scale_invariance(self):
        expected = contracts.weighted_tertiles({0: 1, 5: 1, 10: 1})
        self.assertEqual(expected["cuts"], [0, 5])
        self.assertEqual(expected["weightedShares"], ["1/3"] * 3)
        self.assertEqual(expected, contracts.weighted_tertiles({10: 2, 5: 2, 0: 2}))

    def test_ties_are_whole_categories_with_unequal_shares(self):
        value = contracts.weighted_tertiles({0: 40, 5: 30, 10: 30})
        self.assertEqual(value["groups"], [[0], [5], [10]])
        self.assertEqual(value["weightedShares"], ["2/5", "3/10", "3/10"])
        self.assertNotEqual(value["weightedShares"], ["1/3"] * 3)

    def test_unseparable_mass_empty_domain_or_invalid_values_block(self):
        for values in [{0: 10, 5: 80, 10: 10}, {5: 1}, {}, {0: 0, 5: 0}]:
            with self.subTest(values=values):
                self.assertEqual(contracts.weighted_tertiles(values)["status"], "BLOCKIERT")
        for values in [{77: 1}, {88: 1}, {True: 1}, {0: -1}, {0: "nan"}]:
            with self.subTest(values=values), self.assertRaises((ValueError, ZeroDivisionError)):
                contracts.weighted_tertiles(values)

    def test_special_climate_answer_is_not_ordinal_or_ordinary_missing(self):
        special = contracts.climate_routing(55)
        self.assertEqual(special["causeType"], "Sonderantwort")
        self.assertIsNone(special["causeOrdinal"])
        self.assertFalse(special["followupsAsked"])
        self.assertEqual(special["followupStatus"], "STRUKTURELL_NICHT_ANWENDBAR")

    def test_refusal_and_dontknow_do_not_route_out_followups(self):
        for code in [77, 88]:
            value = contracts.climate_routing(code)
            self.assertIsNone(value["causeOrdinal"])
            self.assertTrue(value["followupsAsked"])
        for code in range(1, 6):
            value = contracts.climate_routing(code)
            self.assertEqual(value["causeOrdinal"], code)
            self.assertTrue(value["followupsAsked"])
        for code in [0, 99, True, "55"]:
            with self.subTest(code=code), self.assertRaises(ValueError):
                contracts.climate_routing(code)


if __name__ == "__main__":
    unittest.main()
