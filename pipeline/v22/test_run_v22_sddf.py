"""Synthetic checks for pipeline/v22/sav.py and run_v22_sddf.py. No survey data are read."""

import csv
import json
import struct
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from pipeline.v22.run_v22 import RunError, item_specs, run  # noqa: E402
from pipeline.v22.run_v22_sddf import linked_design, read_design, run_study  # noqa: E402
from pipeline.v22.sav import read_sav  # noqa: E402
from pipeline.v22.test_run_v22 import synthetic  # noqa: E402

SYSMIS = -sys.float_info.max


def write_sav(path: Path, variables: list[tuple[str, int]], rows: list[list], compressed: bool):
    """Minimal SPSS writer for tests: (name, width) with width 0 for numeric."""
    header = b'$FL2' + b'@(#) synthetic test file'.ljust(60)
    slots = sum(1 if w == 0 else (w + 7) // 8 for _, w in variables)
    header += struct.pack('<iiii', 2, slots, 1 if compressed else 0, 0)
    header += struct.pack('<i', len(rows)) + struct.pack('<d', 100.0)
    header += b'01 Jan 26' + b'00:00:00' + b' ' * 64 + b'\0' * 3
    assert len(header) == 176
    dictionary = b''
    for name, width in variables:
        dictionary += struct.pack('<iiiiii', 2, width, 0, 0, 0, 0) + name.upper().ljust(8).encode()
        for _ in range((width + 7) // 8 - 1 if width else 0):
            dictionary += struct.pack('<iiiiii', 2, -1, 0, 0, 0, 0) + b' ' * 8
    dictionary += struct.pack('<ii', 999, 0)
    cells = []
    for row in rows:
        for (_, width), value in zip(variables, row):
            if width == 0:
                cells.append(('num', value))
            else:
                text = value.encode().ljust(((width + 7) // 8) * 8)
                cells += [('str', text[i:i + 8]) for i in range(0, len(text), 8)]
    if not compressed:
        body = b''.join(struct.pack('<d', SYSMIS if v is None else v) if kind == 'num' else v
                        for kind, v in cells)
    else:
        body, codes, data = b'', [], b''
        for kind, value in cells:
            if kind == 'num' and value is None:
                codes.append(255)
            elif kind == 'num' and value == int(value) and -99 <= value <= 151:
                codes.append(int(value) + 100)
            elif kind == 'str' and value == b' ' * 8:
                codes.append(254)
            else:
                codes.append(253)
                data += struct.pack('<d', value) if kind == 'num' else value
            if len(codes) == 8:
                body += bytes(codes) + data
                codes, data = [], b''
        codes.append(252)
        body += bytes(codes + [0] * (8 - len(codes))) + data
    path.write_bytes(header + dictionary + body)


class SavReader(unittest.TestCase):
    def test_round_trip_compressed_and_uncompressed(self):
        variables = [('cntry', 2), ('idno', 0), ('psu', 0), ('stratify', 30), ('prob', 0)]
        rows = [['DE', 1001.0, 5.0, 'Stratum mit langem Namen A', 0.0123],
                ['DE', 250000.0, 151.0, '', None],
                ['DE', -3.0, 7.5, 'B', 1e-5]]
        for compressed in (True, False):
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'x.sav'
                write_sav(path, variables, rows, compressed)
                result = read_sav(path, ['cntry', 'idno', 'psu', 'stratify', 'prob'])
                self.assertEqual(result, [
                    dict(cntry='DE', idno=1001.0, psu=5.0, stratify='Stratum mit langem Namen A',
                         prob=0.0123),
                    dict(cntry='DE', idno=250000.0, psu=151.0, stratify='', prob=None),
                    dict(cntry='DE', idno=-3.0, psu=7.5, stratify='B', prob=1e-5)])


def write_csv(path: Path, rows: list[dict]) -> None:
    with open(path, 'w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def split_design(tmp: Path):
    """Moves psu and stratum of the synthetic study into a separate SDDF-like file."""
    with open(tmp / 'study.csv', newline='') as handle:
        rows = list(csv.DictReader(handle))
    design = [dict(name='SDDF', essround='9', edition='1.0', proddate='x', cntry=r['cntry'],
                   idno=r['idno'], psu=str(int(r['stratum']) * 10 + int(r['psu'].split('-')[1])),
                   domain='1', stratum=r['stratum'], prob='0.1')
              for r in rows if r['cntry'] == 'DE']
    design.append(dict(design[0], cntry='FR'))  # another country with the same idno is ignored
    write_csv(tmp / 'design.csv', design)
    write_csv(tmp / 'main.csv', [{k: v for k, v in r.items() if k not in ('psu', 'stratum')}
                                 for r in rows])
    return design


class SddfRun(unittest.TestCase):
    def run_both(self, tmp: Path):
        contract_path, groups_path, supplement_path = synthetic(tmp)
        frozen = run(contract_path, groups_path, supplement_path, verify_hashes=False)
        split_design(tmp)
        contract = json.loads(contract_path.read_text())
        study = contract['studies'][0]
        study['input']['path'] = str(tmp / 'main.csv')
        gs = json.loads(groups_path.read_text())['studies'][0]
        specs = item_specs(contract, json.loads(supplement_path.read_text()))['ESS9e03_3']
        spec = dict(path='design.csv', format='csv', sha256='unused', stratum='stratum')
        return frozen['studies']['ESS9e03_3'], run_study(study, gs, specs, tmp / 'design.csv',
                                                         spec, verify_hashes=False)

    def test_sddf_design_reproduces_design_in_main_file(self):
        with tempfile.TemporaryDirectory() as directory:
            frozen, sddf = self.run_both(Path(directory))
            self.assertTrue(sddf['designAvailable'])
            self.assertEqual(sddf['designSource']['linkage'], 'complete_one_to_one')
            self.assertEqual(sddf['items'], frozen['items'])
            self.assertEqual(sddf['groups'], frozen['groups'])
            self.assertEqual(sddf['eligibilityAccounting'], frozen['eligibilityAccounting'])
            self.assertIsNotNone(sddf['items']['ESS9e03_3:old']['reference']['intervals'])

    def test_incomplete_linkage_gives_no_design(self):
        rows = [dict(idno='1'), dict(idno='2')]
        self.assertIsNone(linked_design(rows, {'1': ('a', '1')}))
        self.assertIsNone(linked_design(rows, {'1': ('a', '1'), '2': ('a', '2'), '3': ('a', '3')}))
        self.assertIsNone(linked_design(rows + [dict(idno='2.0')], {'1': ('a', '1'), '2': ('a', '2')}))
        self.assertEqual(linked_design(rows, {'1': ('a', '1'), '2': ('b', '2')}),
                         [('a', '1'), ('b', '2')])

    def test_design_file_errors(self):
        spec = dict(format='csv', stratum='stratum')
        with tempfile.TemporaryDirectory() as directory:
            tmp = Path(directory)
            synthetic(tmp)
            design = split_design(tmp)
            self.assertEqual(len(read_design(spec, tmp / 'design.csv')), 400)
            for change in (dict(idno=design[1]['idno']), dict(psu=''), dict(idno='1x')):
                write_csv(tmp / 'bad.csv', [dict(design[0], **change)] + design[1:])
                with self.assertRaises(RunError, msg=str(change)):
                    read_design(spec, tmp / 'bad.csv')


if __name__ == '__main__':
    unittest.main()
