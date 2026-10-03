#!/usr/bin/env python3
"""Public v2.2 export (Analyseplan v2.2, Abschnitt 6).

Reads the private run (data/local/v22/run.json) and an explicit export decision.
Writes data/reference-v2.2/<study>.json with only approved, prepared references:
category shares, 95 % intervals where computed, counts and missing reasons.
Missing reasons with one to four cases keep their count but lose the weight sum.
Recomputed shares of the 43 v2 questions must equal the published v2 files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREPARED = 'prepared_pending_result_review'
MIN_CELL = 5
TOLERANCE = 1e-12


class ExportError(Exception):
    pass


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def public_reference(ref: dict) -> dict:
    categories = []
    for code, share in ref['shares'].items():
        interval = (ref.get('intervals') or {}).get(code)
        categories.append(dict(code=code, proportion=share,
                               lower=None if not interval else interval['lower'],
                               upper=None if not interval else interval['upper']))
    return dict(
        validCount=ref['validCount'], totalCount=ref['totalCount'],
        missingCount=sum(m['count'] for m in ref['missingReasons']),
        missingReasons=[dict(reason=m['reason'], count=m['count'],
                             primaryWeightSum=m['primaryWeightSum'] if m['count'] >= MIN_CELL else None)
                        for m in ref['missingReasons']],
        notAskedCount=ref['notAskedCount'], exportBlankCount=ref['exportBlankCount'],
        categories=categories,
        interval=None if not ref.get('design') else dict(
            method='taylor_linearisation_xlogit', level=0.95,
            degreesOfFreedom=ref['design']['degreesOfFreedom'],
            strata=ref['design']['strata'], psus=ref['design']['psus']),
        sensitivityMaxAbs=ref['sensitivityMaxAbs'],
    )


def check_against_v2(study: str, items: dict, groups: dict) -> None:
    published = json.loads((ROOT / f'data/reference-v2/{study}.json').read_text())
    for question in published['questions']:
        own = items[question['id']]['reference']
        if question['reference'] is None:
            if own['status'] == PREPARED:
                raise ExportError(f'{question["id"]}: status differs from v2')
            continue
        for category in question['reference']['categories']:
            if abs(own['shares'][category['code']] - category['proportion']) > TOLERANCE:
                raise ExportError(f'{question["id"]}: share differs from v2')
    group_path = ROOT / f'data/reference-groups-v21/{study}.json'
    if not group_path.exists():
        return
    published_groups = json.loads(group_path.read_text())
    for group in published_groups['groups']:
        own_pairs = groups.get(group['id'], {}).get('pairs', {})
        for pair in group['questions']:
            if pair.get('reference') is None or pair['id'] not in own_pairs:
                continue
            own = own_pairs[pair['id']]
            for category in pair['reference']['categories']:
                if abs(own['shares'][category['code']] - category['proportion']) > TOLERANCE:
                    raise ExportError(f'{group["id"]} {pair["id"]}: share differs from v2.1')


def export(run: dict, decision: dict, run_sha: str, out_dir: Path) -> list[Path]:
    approved = set(decision['approvedQuestionIds'])
    approved_pairs = {(p['groupId'], p['questionId']) for p in decision['approvedPairs']}
    written = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for study, data in sorted(run['studies'].items()):
        check_against_v2(study, data['items'], data['groups'])
        questions = []
        for qid, entry in sorted(data['items'].items()):
            ref = entry['reference']
            include = qid in approved and ref['status'] == PREPARED
            questions.append(dict(id=qid, addedInV22=entry['new'], status=ref['status'] if not include
                                  else 'reviewed_historical_reference',
                                  reference=public_reference(ref) if include else None))
        groups = []
        for gid, group in sorted(data['groups'].items()):
            pairs = []
            for qid, ref in sorted(group['pairs'].items()):
                include = (gid, qid) in approved_pairs and ref['status'] == PREPARED
                pairs.append(dict(questionId=qid, status=ref['status'] if not include
                                  else 'reviewed_historical_reference',
                                  reference=public_reference(ref) if include else None))
            groups.append(dict(groupId=gid, pairs=pairs))
        document = dict(schemaVersion=1, plan='docs/analyseplan-v2.2.md',
                        privateRunSha256=run_sha, decision=decision['id'], study=study,
                        designAvailable=data['designAvailable'], questions=questions, groups=groups)
        for question in questions:
            ref = question['reference']
            if ref and abs(math.fsum(c['proportion'] for c in ref['categories']) - 1) > 1e-9:
                raise ExportError('shares do not sum to one')
        path = out_dir / f'{study}.json'
        path.write_text(json.dumps(document, ensure_ascii=False, indent=1) + '\n')
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', default='data/local/v22/run.json')
    parser.add_argument('--decision', default='reports/claude/export-v22-entscheidung.json')
    parser.add_argument('--out', default='data/reference-v2.2')
    args = parser.parse_args()
    run_path, decision_path = ROOT / args.run, ROOT / args.decision
    decision = json.loads(decision_path.read_text())
    if decision.get('privateRunSha256') != sha256(run_path):
        print(json.dumps({'status': 'refused', 'reason': 'decision does not bind this run'}))
        return 1
    try:
        written = export(json.loads(run_path.read_text()), decision, sha256(run_path), ROOT / args.out)
    except ExportError as error:
        print(json.dumps({'status': 'failed', 'reason': str(error)}))
        return 1
    for path in written:
        print(json.dumps({'written': str(path.relative_to(ROOT)), 'sha256': sha256(path)}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
