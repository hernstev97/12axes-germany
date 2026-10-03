"""Synthetic negative-access cases; never reads an ESS response file."""

import csv
import hashlib
import io
import json
from pathlib import Path
import unittest

from pipeline.empirical_access import (
    AccessError, ITEM_IDS, METADATA, assignment, development_frame,
)


class DevelopmentAccess(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[2]
        self.contract = json.loads((root / "data/item-core-v1.json").read_text())
        self.fields = [*METADATA, *[i["variable"] for i in self.contract["items"]],
                       "idno", "lrscale", "prtvgde2"]
        self.rows = []
        for h, count in ((1, 2), (2, 4), (3, 5)):
            for p in range(count):
                self.rows.append(["DE", "11", "4.2", "02.07.2026", str(h * 100 + p),
                                  str(h), "1.5",
                                  *[str(i["allowed_values"][0]) for i in self.contract["items"]],
                                  "DO_NOT_SELECT_ID", "DO_NOT_SELECT_LR", "DO_NOT_SELECT_VOTE"])
        _, _, initial = self.pack()
        self.units = {(u["stratum"], u["psu"]): u for u in initial["units"]}
        for row in self.rows:
            if self.unit(row)["arm"] != "A":
                row[len(METADATA):len(METADATA) + 9] = ["INVALID_WITHHELD_TOKEN"] * 9

    def unit(self, row):
        return self.units[(int(row[5]), int(row[4]))]

    def pack(self):
        buffer = io.StringIO(newline="")
        writer = csv.writer(buffer)
        writer.writerow(self.fields)
        writer.writerows(self.rows)
        frozen = buffer.getvalue().encode()
        sha = hashlib.sha256(frozen).hexdigest()
        return frozen, sha, assignment(frozen, sha)

    def frame(self):
        frozen, sha, split = self.pack()
        return development_frame(frozen, split, self.contract, sha)

    def test_withheld_invalid_tokens_and_person_fields_are_not_selected(self):
        header, rows = self.frame()
        self.assertEqual(header, ["stratum", "psu", "weight", *ITEM_IDS])
        self.assertEqual(len(rows), 4)
        self.assertTrue(all(len(row) == len(header) for row in rows))

    def test_predeclared_reserve_and_conditional_probabilities(self):
        frozen, sha, split = self.pack()
        self.assertEqual(split, assignment(frozen, sha))
        self.assertEqual(sum(u["arm"] == "C" for u in split["units"]), 2)
        for h, g in ((2, 4), (3, 5)):
            for arm, m in (("A", g // 2), ("B", g - g // 2)):
                selected = [u for u in split["units"] if u["stratum"] == h and u["arm"] == arm]
                self.assertEqual(len(selected), m)
                self.assertTrue(all(u["probability"] == m / g for u in selected))

    def test_unexpected_development_category_stops(self):
        row = next(r for r in self.rows if self.unit(r)["arm"] == "A")
        row[len(METADATA)] = "1234"
        with self.assertRaisesRegex(AccessError, "UNEXPECTED_A_CATEGORY"):
            self.frame()

    def test_missing_is_not_a_midpoint(self):
        row = next(r for r in self.rows if self.unit(r)["arm"] == "A")
        row[len(METADATA)] = "  NA  "
        _, output = self.frame()
        self.assertTrue(any(r[3] == "NA" for r in output))

    def test_exact_key_and_weight_errors_stop(self):
        self.rows[0][4] = "1.0000000000000001"
        with self.assertRaisesRegex(AccessError, "INTEGER_CODE"):
            self.frame()
        self.rows[0][4] = "100"
        self.rows[0][6] = "-1"
        with self.assertRaisesRegex(AccessError, "WEIGHT"):
            self.frame()

    def test_foreign_assignment_cannot_be_used(self):
        frozen, sha, split = self.pack()
        split["units"][0]["arm"] = "A"
        with self.assertRaisesRegex(AccessError, "SPLIT_REPRODUCTION"):
            development_frame(frozen, split, self.contract, sha)


if __name__ == "__main__":
    unittest.main()
