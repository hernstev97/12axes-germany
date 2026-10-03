"""Synthetic checks for pipeline/v22/export_v22.py (E1-V22-F01 bis F03). No survey data."""

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from pipeline.v22.export_v22 import (  # noqa: E402
    ExportError, cell_evidence, merge_design_run, public_reference)

ORDER = [str(c) for c in range(11)]


def reference(counts: list[int]) -> dict:
    total = sum(counts)
    return dict(status='prepared_pending_result_review', validCount=total, totalCount=total + 2,
                categoryCounts=dict(zip(ORDER, counts)),
                shares={c: n / total for c, n in sorted(zip(ORDER, counts))},
                missingReasons=[dict(reason="Don't know", count=2, primaryWeightSum=1.5)],
                notAskedCount=0, exportBlankCount=0,
                sensitivityMaxAbs=dict(unweighted=0.0, dweight=0.0))


class Export(unittest.TestCase):
    def test_categories_follow_the_bound_order(self):
        ref = reference([10] * 11)
        self.assertEqual(list(ref['shares'])[:3], ['0', '1', '10'])
        public = public_reference(ref, ORDER)
        self.assertEqual([c['code'] for c in public['categories']], ORDER)
        self.assertIsNone(public['missingReasons'][0]['primaryWeightSum'])
        with self.assertRaises(ExportError):
            public_reference(ref, ORDER[:-1])

    def test_cell_evidence_enforces_the_publication_rule(self):
        entry = cell_evidence('q', reference([0] + [10] * 10), ORDER)
        self.assertEqual((entry['positiveCategories'], entry['minPositiveCount']), (10, 10))
        for counts in ([4] + [20] * 10, [9] * 11):
            with self.assertRaises(ExportError, msg=str(counts)):
                cell_evidence('q', reference(counts), ORDER)

    def test_design_run_must_equal_the_frozen_run(self):
        frozen = dict(runSha256='a', studies={sid: dict(
            deRows=200, designAvailable=False, items={'q': dict(new=True, reference=reference([20] * 11))},
            groups={'g': dict(groupSize=150, pairs={'q': reference([15] * 11)})})
            for sid in ('ESS5e03_6', 'ESS8e02_3')})
        design = copy.deepcopy(frozen)
        design['privateRunSha256'] = 'a'
        for study in design['studies'].values():
            study['designAvailable'] = True
            study['items']['q']['reference']['intervals'] = {c: {} for c in ORDER}
        self.assertTrue(merge_design_run(frozen, design)['ESS5e03_6']['designAvailable'])
        changed = copy.deepcopy(design)
        changed['studies']['ESS8e02_3']['groups']['g']['pairs']['q']['validCount'] += 1
        with self.assertRaises(ExportError):
            merge_design_run(frozen, changed)
        with self.assertRaises(ExportError):
            merge_design_run(frozen, dict(design, privateRunSha256='b'))


if __name__ == '__main__':
    unittest.main()
