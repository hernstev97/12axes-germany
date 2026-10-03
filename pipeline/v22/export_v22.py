#!/usr/bin/env python3
"""Public v2.2 export (Analyseplan v2.2, Abschnitte 4.1, 6 und 8).

Two stages, after the result review E1 (reports/claude/pruefungen/E1-ergebnis-v22.md):

candidate
    Reads the frozen private run (data/local/v22/run.json) and the private design run for
    ESS5 and ESS8 (data/local/v22/sddf-run.json). Every value of the design run must equal
    the frozen run, apart from the intervals. Recomputed v2 and v2.1 shares must equal the
    published files. Writes candidate files in which every prepared reference keeps the
    status prepared_pending_result_review (E1-V22-F01), with categories in the bound code
    order (E1-V22-F02), and an aggregate cell-count evidence file for the prepared
    references only (E1-V22-F03). Nothing is marked reviewed.

release
    Needs an explicit decision bound to both private runs and to the candidate hashes.
    Rebuilds the candidates, refuses if a hash differs, and writes data/reference-v2.2 with
    reviewed_historical_reference only for approved entries. All others carry no numbers.

Missing reasons with one to four cases keep their count but lose the weight sum.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from pipeline.v22.run_v22 import item_specs  # noqa: E402

PREPARED = 'prepared_pending_result_review'
REVIEWED = 'reviewed_historical_reference'
NOT_APPROVED = 'not_approved_after_result_review'
MIN_VALID = 100
MIN_CELL = 5
TOLERANCE = 1e-12
INTERVAL_KEYS = ('intervals', 'design', 'intervalStatus')
DESIGN_RUN_STUDIES = ('ESS5e03_6', 'ESS8e02_3')
CONTRACT = ROOT / 'data/analysevertrag.v2.entwurf.json'
GROUP_CONTRACT = ROOT / 'data/gruppenvertrag.v2.1.entwurf.json'
SUPPLEMENT = ROOT / 'data/politikprofil-v2.2.ergaenzung.json'
RUN = ROOT / 'data/local/v22/run.json'
DESIGN_RUN = ROOT / 'data/local/v22/sddf-run.json'
EVIDENCE = 'zellnachweis.json'


class ExportError(Exception):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(document: dict) -> bytes:
    return (json.dumps(document, ensure_ascii=False, indent=1) + '\n').encode()


def without_interval(ref: dict) -> dict:
    return {k: v for k, v in ref.items() if k not in INTERVAL_KEYS}


def merge_design_run(run: dict, design_run: dict) -> dict:
    """ESS5 and ESS8 from the design run, after checking every shared value."""
    if design_run.get('privateRunSha256') != run.get('runSha256'):
        raise ExportError('design run is not bound to this private run')
    studies = dict(run['studies'])
    for sid in DESIGN_RUN_STUDIES:
        frozen, design = run['studies'][sid], design_run['studies'][sid]
        if not design['designAvailable']:
            continue
        if design['deRows'] != frozen['deRows'] or \
                design.get('eligibilityAccounting') != frozen.get('eligibilityAccounting'):
            raise ExportError(f'{sid}: design run differs from frozen run')
        if set(design['items']) != set(frozen['items']):
            raise ExportError(f'{sid}: question sets differ')
        for qid, entry in frozen['items'].items():
            if without_interval(design['items'][qid]['reference']) != \
                    without_interval(entry['reference']) or design['items'][qid]['new'] != entry['new']:
                raise ExportError(f'{qid}: design run differs from frozen run')
        for gid, group in frozen['groups'].items():
            own = design['groups'][gid]
            if own['groupSize'] != group['groupSize']:
                raise ExportError(f'{gid}: group size differs')
            for qid, ref in group['pairs'].items():
                if without_interval(own['pairs'][qid]) != without_interval(ref):
                    raise ExportError(f'{gid} {qid}: design run differs from frozen run')
        studies[sid] = design
    return studies


def check_against_published(study: str, items: dict, groups: dict) -> None:
    published = json.loads((ROOT / f'data/reference-v2/{study}.json').read_text())
    for question in published['questions']:
        own = items[question['id']]['reference']
        if (question['reference'] is None) != (own['status'] != PREPARED):
            raise ExportError(f'{question["id"]}: status differs from v2')
        for category in (question['reference'] or {}).get('categories', []):
            if abs(own['shares'][category['code']] - category['proportion']) > TOLERANCE:
                raise ExportError(f'{question["id"]}: share differs from v2')
    group_path = ROOT / f'data/reference-groups-v21/{study}.json'
    if not group_path.exists():
        return
    for group in json.loads(group_path.read_text())['groups']:
        own_pairs = groups.get(group['id'], {}).get('pairs', {})
        for pair in group['questions']:
            if pair['id'] not in own_pairs:
                continue
            own = own_pairs[pair['id']]
            if (pair.get('reference') is None) != (own['status'] != PREPARED):
                raise ExportError(f'{group["id"]} {pair["id"]}: status differs from v2.1')
            for category in (pair.get('reference') or {}).get('categories', []):
                if abs(own['shares'][category['code']] - category['proportion']) > TOLERANCE:
                    raise ExportError(f'{group["id"]} {pair["id"]}: share differs from v2.1')


def public_reference(ref: dict, order: list[str]) -> dict:
    if list(ref['shares']) and set(ref['shares']) != set(order):
        raise ExportError('category set differs from the bound order')
    categories = []
    for code in order:
        interval = (ref.get('intervals') or {}).get(code)
        categories.append(dict(code=code, proportion=ref['shares'][code],
                               lower=None if not interval else interval['lower'],
                               upper=None if not interval else interval['upper']))
    if abs(math.fsum(c['proportion'] for c in categories) - 1) > 1e-9:
        raise ExportError('shares do not sum to one')
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


def cell_evidence(key: str, ref: dict, order: list[str]) -> dict:
    """Aggregate proof of the publication rule for one prepared reference."""
    counts = [ref['categoryCounts'][code] for code in order]
    positive = [n for n in counts if n > 0]
    entry = dict(id=key, validCount=ref['validCount'], categories=len(counts),
                 positiveCategories=len(positive), minPositiveCount=min(positive),
                 countSumEqualsValidCount=sum(counts) == ref['validCount'])
    if ref['validCount'] < MIN_VALID or entry['minPositiveCount'] < MIN_CELL or \
            not entry['countSumEqualsValidCount']:
        raise ExportError(f'{key}: prepared reference violates the publication rule')
    return entry


def candidates(run: dict, design_run: dict) -> tuple[dict[str, dict], list[dict]]:
    """Candidate documents per study and the cell evidence of their prepared references."""
    specs = item_specs(json.loads(CONTRACT.read_text()), json.loads(SUPPLEMENT.read_text()))
    group_order = {s['studyId']: [g['groupId'] for g in s['groupsInDeclaredApiOrder']]
                   for s in json.loads(GROUP_CONTRACT.read_text())['studies']}
    supplement = {i['id']: i for i in json.loads(SUPPLEMENT.read_text())['items']}
    studies = merge_design_run(run, design_run)
    documents, evidence = {}, []
    for sid in sorted(studies):
        data = studies[sid]
        check_against_published(sid, data['items'], data['groups'])
        order = {s['id']: s['categories'] for s in specs[sid]}
        for qid, codes in order.items():
            if qid in supplement and codes != supplement[qid]['apiValidCodeOrder']:
                raise ExportError(f'{qid}: category order differs from apiValidCodeOrder')
        if set(order) != set(data['items']):
            raise ExportError(f'{sid}: question set differs from the catalogue')

        def entry(key: str, qid: str, ref: dict) -> dict:
            if ref['status'] != PREPARED:
                return dict(status=ref['status'], reference=None)
            evidence.append(cell_evidence(key, ref, order[qid]))
            return dict(status=PREPARED, reference=public_reference(ref, order[qid]))

        questions = [dict(id=qid, addedInV22=data['items'][qid]['new'],
                          **entry(qid, qid, data['items'][qid]['reference'])) for qid in order]
        groups = []
        for gid in [g for g in group_order.get(sid, []) if g in data['groups']]:
            pairs = data['groups'][gid]['pairs']
            groups.append(dict(groupId=gid, pairs=[
                dict(questionId=qid, **entry(f'{gid}|{qid}', qid, pairs[qid]))
                for qid in order if qid in pairs]))
        if len(groups) != len(data['groups']):
            raise ExportError(f'{sid}: group outside the declared order')
        source = data.get('designSource')
        documents[sid] = dict(
            schemaVersion=2, plan='docs/analyseplan-v2.2.md', stage='candidate_for_result_review',
            privateRunSha256=run['runSha256'],
            designRunSha256=design_run['runSha256'] if source else None,
            study=sid, designAvailable=data['designAvailable'],
            designSource=None if not source else dict(path=source['path'], sha256=source['sha256']),
            questions=questions, groups=groups)
    return documents, evidence


def load_runs() -> tuple[dict, dict]:
    run_bytes, design_bytes = RUN.read_bytes(), DESIGN_RUN.read_bytes()
    run, design_run = json.loads(run_bytes), json.loads(design_bytes)
    run['runSha256'], design_run['runSha256'] = sha256(run_bytes), sha256(design_bytes)
    return run, design_run


def write_candidates(out_dir: Path) -> list[Path]:
    run, design_run = load_runs()
    documents, evidence = candidates(run, design_run)
    out_dir.mkdir(parents=True, exist_ok=True)
    written, hashes = [], {}
    for sid, document in documents.items():
        path = out_dir / f'{sid}.json'
        path.write_bytes(dump(document))
        hashes[path.name] = sha256(dump(document))
        written.append(path)
    proof = dict(schemaVersion=1, plan='docs/analyseplan-v2.2.md', section='6',
                 rule=f'validCount >= {MIN_VALID}; every positive category >= {MIN_CELL} '
                      'unweighted cases; category counts sum to validCount',
                 privateRunSha256=run['runSha256'], designRunSha256=design_run['runSha256'],
                 candidateFiles=hashes, preparedReferences=len(evidence), references=evidence)
    (out_dir / EVIDENCE).write_bytes(dump(proof))
    written.append(out_dir / EVIDENCE)
    return written


def release(decision: dict, out_dir: Path) -> list[Path]:
    run, design_run = load_runs()
    if decision.get('privateRunSha256') != run['runSha256'] or \
            decision.get('designRunSha256') != design_run['runSha256']:
        raise ExportError('decision does not bind these private runs')
    documents, _ = candidates(run, design_run)
    if decision.get('candidateFiles') != {f'{sid}.json': sha256(dump(d)) for sid, d in documents.items()}:
        raise ExportError('decision does not bind these candidate files')
    approved = set(decision['approvedQuestionIds'])
    approved_pairs = {(p['groupId'], p['questionId']) for p in decision['approvedPairs']}

    def finalise(entry: dict, ok: bool) -> None:
        if entry['status'] == PREPARED:
            entry['status'] = REVIEWED if ok else NOT_APPROVED
            if not ok:
                entry['reference'] = None
        elif ok:
            raise ExportError('approval of an entry without a prepared reference')

    written = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for sid, document in documents.items():
        for question in document['questions']:
            finalise(question, question['id'] in approved)
        for group in document['groups']:
            for pair in group['pairs']:
                finalise(pair, (group['groupId'], pair['questionId']) in approved_pairs)
        document.update(stage='released_after_result_review', decision=decision['id'],
                        candidateSha256=decision['candidateFiles'][f'{sid}.json'])
        path = out_dir / f'{sid}.json'
        path.write_bytes(dump(document))
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    stages = parser.add_subparsers(dest='stage', required=True)
    candidate = stages.add_parser('candidate')
    candidate.add_argument('--out', default='outputs/claude/v22-candidate-2')
    final = stages.add_parser('release')
    final.add_argument('--decision', default='reports/claude/export-v22-entscheidung.json')
    final.add_argument('--out', default='data/reference-v2.2')
    args = parser.parse_args()
    try:
        if args.stage == 'candidate':
            written = write_candidates(ROOT / args.out)
        else:
            written = release(json.loads((ROOT / args.decision).read_text()), ROOT / args.out)
    except ExportError as error:
        print(json.dumps({'status': 'failed', 'reason': str(error)}))
        return 1
    for path in written:
        print(json.dumps({'written': str(path.relative_to(ROOT)), 'sha256': sha256(path.read_bytes())}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
