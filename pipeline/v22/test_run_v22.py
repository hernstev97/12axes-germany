"""Synthetic end-to-end checks for pipeline/v22/run_v22.py. No survey data are read."""

import csv
import json
import random
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from pipeline.v22.run_v22 import NO_VALID, PREPARED, WITHHELD, RunError, run  # noqa: E402


def write_study(path: Path, rows: list[dict]) -> None:
    with open(path, 'w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def synthetic(tmp: Path, *, extra_code: str | None = None, vote_code: str | None = None):
    rng = random.Random(7)
    rows = []
    for i in range(400):
        stratum = i % 20
        rows.append(dict(cntry='DE', essround='9', edition='3.3', idno=str(i),
                         pspwght=f'{rng.uniform(0.5, 2):.6f}', dweight=f'{rng.uniform(0.5, 2):.6f}',
                         anweight=f'{rng.uniform(0.5, 2):.6f}',
                         psu=f'{stratum}-{i % 3}', stratum=str(stratum),
                         old=str(rng.choice([1, 2, 3, 4, 5, 8])), new=str(rng.choice([1, 2, 3, 4])),
                         rare=str(1 if i < 3 else 2), vote='1' if i % 2 else '2',
                         party='1' if i % 4 == 1 else ('2' if i % 4 == 3 else '66')))
    rows[8]['party'] = '1'  # vote = 2 with a valid party code: counted as inconsistency
    rows[10]['vote'] = '8'  # vote missing: Don't know
    rows[12]['party'] = '77'  # vote = 2 and party missing: Refusal
    rows.append(dict(rows[0], cntry='FR', idno='x'))
    if extra_code:
        rows[5]['new'] = extra_code
    if vote_code:
        rows[6]['vote'] = vote_code
    write_study(tmp / 'study.csv', rows)
    contract = dict(studies=[dict(
        study_id='ESS9e03_3', input=dict(path=str(tmp / 'study.csv'), sha256='unused'),
        metadata=dict(expected_round='9', expected_edition='3.3'),
        adapter=dict(questions=[
            dict(question_id='ESS9e03_3:old', variable='old', categoryCodes=['1', '2', '3', '4', '5'],
                 missingCodes={'8': "Don't know", '': 'export_blank_unclassified'},
                 structurallyNotAskedCodes=[]),
            dict(question_id='ESS9e03_3:rare', variable='rare', categoryCodes=['1', '2'],
                 missingCodes={}, structurallyNotAskedCodes=[]),
        ]))])
    groups = dict(studies=[dict(
        studyId='ESS9e03_3', columns=dict(vote='vote', party2='party'),
        voteField=dict(validCodes=['1', '2', '3'],
                       sourceMissingCodes=[dict(code=c, reasonApiExact=r) for c, r in
                                           (('7', 'Refusal'), ('8', "Don't know"), ('9', 'No answer'))]),
        nationalParty2Field=dict(validCodes=['1', '2'],
                                 sourceMissingCodes=[dict(code=c, reasonApiExact=r) for c, r in
                                                     (('77', 'Refusal'), ('88', "Don't know"),
                                                      ('99', 'No answer'))],
                                 structurallyNotAskedCodes=[dict(code='66')]),
        groupsInDeclaredApiOrder=[
            dict(groupId='ESS9e03_3:second_vote:1', party2Code='1', kind='named_party'),
            dict(groupId='ESS9e03_3:second_vote:2', party2Code='2', kind='other_unlabelled')])])
    supplement = dict(items=[dict(
        id='ESS9e03_3:new', studyId='ESS9e03_3', variable='new',
        categories=[dict(code=c) for c in ['1', '2', '3', '4']],
        missingCodes=[], notAskedCodes=[])])
    paths = []
    for name, value in (('contract', contract), ('groups', groups), ('supplement', supplement)):
        (tmp / f'{name}.json').write_text(json.dumps(value))
        paths.append(tmp / f'{name}.json')
    return paths


class RunV22(unittest.TestCase):
    def test_references_intervals_and_groups(self):
        with tempfile.TemporaryDirectory() as directory:
            tmp = Path(directory)
            result = run(*synthetic(tmp), verify_hashes=False)
            study = result['studies']['ESS9e03_3']
            self.assertEqual(study['deRows'], 400)
            self.assertTrue(study['designAvailable'])
            old = study['items']['ESS9e03_3:old']['reference']
            self.assertEqual(old['status'], PREPARED)
            self.assertAlmostEqual(sum(old['shares'].values()), 1.0)
            self.assertEqual(old['missingReasons'][0]['reason'], "Don't know")
            for category, interval in old['intervals'].items():
                self.assertLess(interval['lower'], old['shares'][category])
                self.assertGreater(interval['upper'], old['shares'][category])
            self.assertEqual(study['items']['ESS9e03_3:rare']['reference']['status'], WITHHELD)
            group = study['groups']['ESS9e03_3:second_vote:1']
            self.assertEqual(group['groupSize'], 100)
            self.assertIn('ESS9e03_3:old', group['pairs'])

    def test_unknown_codes_fail_the_study(self):
        for kwargs in (dict(extra_code='9'), dict(extra_code='1\n'), dict(vote_code='999'),
                       dict(vote_code='1 ')):
            with tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(RunError, msg=str(kwargs)):
                    run(*synthetic(Path(directory), **kwargs), verify_hashes=False)

    def test_vote_party_accounting_and_inconsistency(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run(*synthetic(Path(directory)), verify_hashes=False)
            accounting = result['studies']['ESS9e03_3']['eligibilityAccounting']
            self.assertEqual(sum(accounting['voteStates'].values()), 400)
            self.assertEqual(accounting['voteStates']['yes'], 200)
            self.assertEqual(accounting['nonYesVoteWithValidParty'], 1)
            self.assertEqual(result['studies']['ESS9e03_3']['groups']['ESS9e03_3:second_vote:1']
                             ['groupSize'], 100)
            self.assertEqual(accounting['voteMissingReasons'], {"Don't know": 1})
            self.assertEqual(accounting['partyMissingReasons'], {'Refusal': 1})
            self.assertEqual(accounting['partyStates']['valid_named_party'], 101)
            self.assertEqual(accounting['partyStates']['valid_other_unlabelled'], 100)
            study = result['studies']['ESS9e03_3']
            self.assertEqual(study['anweightRatioEligibleGroupCases']['cases'], 200)
            self.assertEqual(study['anweightRatioAllGermanCases']['status'],
                             'not_constant_within_tolerance')

    def test_private_directory_checks(self):
        import os
        from pipeline.v22.run_v22 import check_private_dir
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory) / 'local'
            target = parent / 'v22'
            check_private_dir(target, parent)  # nothing exists yet
            target.mkdir(parents=True, mode=0o700)
            os.chmod(target, 0o700)
            check_private_dir(target, parent)
            os.chmod(target, 0o755)
            with self.assertRaises(RunError):
                check_private_dir(target, parent)
            os.chmod(target, 0o700)
            (target / 'run.json').write_text('{}')
            with self.assertRaises(RunError):
                check_private_dir(target, parent)
            elsewhere = Path(directory) / 'elsewhere'
            elsewhere.mkdir(mode=0o700)
            link = Path(directory) / 'linked'
            link.symlink_to(elsewhere)
            with self.assertRaises(RunError):
                check_private_dir(link / 'v22', parent)

    def test_ratio_diagnostic_without_eligible_cases(self):
        from pipeline.v22.run_v22 import ratio_diagnostic
        self.assertEqual(ratio_diagnostic([1.0], [1.0], [False])['status'],
                         'not_evaluable_no_eligible_group_cases')
        self.assertEqual(ratio_diagnostic([2.0, 4.0], [1.0, 2.0], [True, True])['status'],
                         'constant_within_tolerance')

    def test_empty_domain_has_no_valid_answers(self):
        with tempfile.TemporaryDirectory() as directory:
            tmp = Path(directory)
            paths = synthetic(tmp)
            groups = json.loads(paths[1].read_text())
            groups['studies'][0]['nationalParty2Field']['validCodes'].append('3')
            groups['studies'][0]['groupsInDeclaredApiOrder'].append(
                dict(groupId='ESS9e03_3:second_vote:3', party2Code='3', kind='named_party'))
            paths[1].write_text(json.dumps(groups))
            result = run(*paths, verify_hashes=False)
            pair = result['studies']['ESS9e03_3']['groups']['ESS9e03_3:second_vote:3']['pairs']
            self.assertEqual(pair['ESS9e03_3:old']['status'], NO_VALID)


if __name__ == '__main__':
    unittest.main()
