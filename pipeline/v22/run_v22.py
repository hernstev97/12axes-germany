#!/usr/bin/env python3
"""Private v2.2 run (Analyseplan v2.2, Abschnitte 3, 4 und 6).

Computes, from the local ESS CSV files:
- single references for the 18 new questions (all five studies as needed),
- historical vote-group references for new ESS5/ESS8 questions (v2.1 groups),
- design-based 95 % intervals for every single reference of studies with a
  complete design (ESS9, ESS10-SC, ESS11) and for ESS9 group pairs,
- recomputed shares of the 43 v2 questions as a consistency check.

Writes only data/local/v22/run.json (directory 0700, file 0600); the path is
fixed. Prints no rows, identifiers, single weights or counts. The command line
refuses to run unless the tag `analyseplan-v2.2` exists locally and on origin
with the same target and the frozen plan, contract and software files in the
working tree equal their tagged versions. `run()` itself is a library function
used by the synthetic tests; it is not an access gate.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from pipeline.v22.survey import DesignError, Unit, estimate  # noqa: E402

csv.field_size_limit(sys.maxsize)
CANON = re.compile(r'^(0|[1-9][0-9]*)(?:\.0+)?$')
MIN_VALID = 100
MIN_CELL = 5
NO_VALID = 'no_valid_answers'
WITHHELD = 'withheld_base_or_cell_count'
PREPARED = 'prepared_pending_result_review'
GROUP_STUDIES = ('ESS5e03_6', 'ESS8e02_3', 'ESS9e03_3')


class RunError(Exception):
    """Errors carry only fixed, content-free messages."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, 'rb') as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def code_of(raw: str):
    if raw == '':
        return 'blank', None
    match = CANON.fullmatch(raw)
    return ('code', match.group(1)) if match else ('literal', None)


def positive(raw: str) -> float:
    try:
        value = float(raw)
    except ValueError as error:
        raise RunError('invalid weight') from error
    if not (math.isfinite(value) and value > 0):
        raise RunError('invalid weight')
    return value


def read_de(path: Path, columns: list[str]) -> list[dict[str, str]]:
    with open(path, newline='', encoding='utf-8', errors='surrogateescape') as handle:
        reader = csv.reader(handle)
        header = next(reader)
        if header and header[0].startswith('﻿'):
            header[0] = header[0][1:]
        if len(set(header)) != len(header):
            raise RunError('duplicate header names')
        index = {c: header.index(c) for c in columns if c in header}
        rows = []
        for row in reader:
            if len(row) != len(header):
                raise RunError('row with wrong field count')
            if row[index['cntry']] == 'DE':
                rows.append({c: row[i] for c, i in index.items()})
    return rows


def item_specs(contract: dict, supplement: dict) -> dict[str, list[dict]]:
    """Per study: existing v2 questions (adapter) and new v2.2 questions."""
    specs: dict[str, list[dict]] = defaultdict(list)
    for study in contract['studies']:
        for q in study['adapter']['questions']:
            missing = {k: v for k, v in q['missingCodes'].items() if k != ''}
            specs[study['study_id']].append(dict(
                id=q['question_id'], variable=q['variable'], categories=q['categoryCodes'],
                missing=missing, notAsked=set(q['structurallyNotAskedCodes']), new=False))
    for item in supplement['items']:
        specs[item['studyId']].append(dict(
            id=item['id'], variable=item['variable'],
            categories=[c['code'] for c in item['categories']],
            missing={m['code']: m['reasonApi'] for m in item['missingCodes']},
            notAsked=set(item['notAskedCodes']), new=True))
    return specs


def classify(rows, spec):
    """Per row: ('valid', code) | ('missing', reason) | ('not_asked', None) | ('blank', None)."""
    out = []
    for row in rows:
        kind, code = code_of(row[spec['variable']])
        if kind == 'blank':
            out.append(('blank', None))
        elif kind == 'literal':
            raise RunError('unknown literal')
        elif code in spec['categories']:
            out.append(('valid', code))
        elif code in spec['missing']:
            out.append(('missing', spec['missing'][code]))
        elif code in spec['notAsked']:
            out.append(('not_asked', None))
        else:
            raise RunError('unknown code')
    return out


def shares(states, weights, categories, domain):
    sums = {c: [] for c in categories}
    for state, weight, inside in zip(states, weights, domain):
        if inside and state[0] == 'valid':
            sums[state[1]].append(weight)
    total = math.fsum(math.fsum(v) for v in sums.values())
    return None if total <= 0 else [math.fsum(sums[c]) / total for c in categories]


def reference(states, weights, design, categories, domain, with_interval):
    counts = Counter(s[1] for s, inside in zip(states, domain) if inside and s[0] == 'valid')
    valid = sum(counts.values())
    missing = Counter(s[1] for s, inside in zip(states, domain) if inside and s[0] == 'missing')
    missing_weight = defaultdict(list)
    for s, w, inside in zip(states, weights['pspwght'], domain):
        if inside and s[0] == 'missing':
            missing_weight[s[1]].append(w)
    result = dict(
        validCount=valid,
        totalCount=sum(domain),
        categoryCounts={c: counts[c] for c in categories},
        missingReasons=[dict(reason=r, count=n, primaryWeightSum=math.fsum(missing_weight[r]))
                        for r, n in sorted(missing.items())],
        notAskedCount=sum(1 for s, inside in zip(states, domain) if inside and s[0] == 'not_asked'),
        exportBlankCount=sum(1 for s, inside in zip(states, domain) if inside and s[0] == 'blank'),
    )
    if valid == 0:
        result['status'] = NO_VALID
        return result
    small = any(1 <= counts[c] < MIN_CELL for c in categories)
    result['status'] = WITHHELD if valid < MIN_VALID or small else PREPARED
    primary = shares(states, weights['pspwght'], categories, domain)
    unweighted = shares(states, [1.0] * len(states), categories, domain)
    design_weight = shares(states, weights['dweight'], categories, domain)
    result['shares'] = dict(zip(categories, primary))
    result['sensitivityMaxAbs'] = dict(
        unweighted=max(abs(a - b) for a, b in zip(primary, unweighted)),
        dweight=max(abs(a - b) for a, b in zip(primary, design_weight)))
    if with_interval and design is not None and result['status'] == PREPARED:
        units = [Unit(w, h, j, inside, s[1] if inside and s[0] == 'valid' else None)
                 for s, w, (h, j), inside in zip(states, weights['pspwght'], design, domain)]
        try:
            estimates, summary = estimate(units, categories)
            result['intervals'] = {
                e.category: dict(standardError=e.standard_error, lower=e.lower, upper=e.upper)
                for e in estimates}
            result['design'] = dict(strata=summary.strata, psus=summary.psus,
                                    degreesOfFreedom=summary.degrees_of_freedom)
        except DesignError:
            result['intervals'] = None
            result['intervalStatus'] = 'design_not_usable'
    return result


def field_state(raw: str, field: dict) -> str:
    kind, code = code_of(raw)
    if kind == 'blank':
        return 'technical_export_blank'
    if kind == 'literal':
        raise RunError('unknown vote or party literal')
    if code in field['validCodes']:
        return 'valid'
    if code in {m['code'] for m in field['sourceMissingCodes']}:
        return 'source_missing'
    if code in {m['code'] for m in field.get('structurallyNotAskedCodes', [])}:
        return 'structurally_not_asked'
    raise RunError('unknown vote or party code')


def vote_party_states(rows, gs) -> tuple[list[str | None], dict]:
    """Validates vote and second-vote fields for every German case (v2.1 contract).

    Returns the party code per case where vote = 1 and the party code is valid, else None,
    and a private accounting of vote states, party states and inconsistencies.
    """
    vote_field, party_field = gs['voteField'], gs['nationalParty2Field']
    vote, party = gs['columns']['vote'], gs['columns']['party2']
    vote_states, party_states = Counter(), Counter()
    inconsistent = 0
    party_of: list[str | None] = []
    for row in rows:
        v_state = field_state(row[vote], vote_field)
        v_code = code_of(row[vote])[1]
        if v_state == 'valid':
            v_state = {'1': 'yes', '2': 'no', '3': 'not_eligible'}[v_code]
        p_state = field_state(row[party], party_field)
        p_code = code_of(row[party])[1]
        vote_states[v_state] += 1
        party_states[p_state] += 1
        if p_state == 'valid' and v_state != 'yes':
            inconsistent += 1
        party_of.append(p_code if v_state == 'yes' and p_state == 'valid' else None)
    return party_of, dict(voteStates=dict(vote_states), partyStates=dict(party_states),
                          nonYesVoteWithValidParty=inconsistent)


def run(contract_path: Path, group_contract_path: Path, supplement_path: Path,
        verify_hashes: bool = True) -> dict:
    contract = json.loads(contract_path.read_text())
    groups = {s['studyId']: s for s in json.loads(group_contract_path.read_text())['studies']}
    supplement = json.loads(supplement_path.read_text())
    specs = item_specs(contract, supplement)
    output = dict(schemaVersion=1, plan='docs/analyseplan-v2.2.md',
                  inputs=dict(analysisContract=sha256_file(contract_path),
                              groupContract=sha256_file(group_contract_path),
                              supplement=sha256_file(supplement_path)),
                  studies={})
    for study in contract['studies']:
        sid = study['study_id']
        path = ROOT / study['input']['path'] if not Path(study['input']['path']).is_absolute() \
            else Path(study['input']['path'])
        if verify_hashes and sha256_file(path) != study['input']['sha256']:
            raise RunError('input hash mismatch')
        gs = groups.get(sid) if sid in GROUP_STUDIES else None
        columns = ['cntry', 'essround', 'edition', 'idno', 'pspwght', 'dweight', 'anweight', 'psu',
                   'stratum']
        columns += [s['variable'] for s in specs[sid]]
        if gs:
            columns += [gs['columns']['vote'], gs['columns']['party2']]
        rows = read_de(path, columns)
        meta = study['metadata']
        if any(code_of(r['essround'])[1] != meta['expected_round'] for r in rows):
            raise RunError('round mismatch')
        try:
            if any(Decimal(r['edition']) != Decimal(meta['expected_edition']) for r in rows):
                raise RunError('edition mismatch')
        except InvalidOperation as error:
            raise RunError('edition mismatch') from error
        if len({r['idno'] for r in rows}) != len(rows):
            raise RunError('duplicate respondent identifiers')
        weights = {w: [positive(r[w]) for r in rows] for w in ('pspwght', 'dweight', 'anweight')}
        ratios = [a / p for a, p in zip(weights['anweight'], weights['pspwght'])]
        ratio_diagnostic = dict(
            relativeSpread=(max(ratios) - min(ratios)) / min(ratios),
            constantWithin1e12=all(abs(r - ratios[0]) <= 1e-12 or abs(r - ratios[0]) <= 1e-12 * ratios[0]
                                   for r in ratios))
        has_design = all(r.get('psu', '') != '' and r.get('stratum', '') != '' for r in rows) \
            and 'psu' in rows[0]
        design = [(r['stratum'], r['psu']) for r in rows] if has_design else None
        everyone = [True] * len(rows)
        study_out = dict(deRows=len(rows), designAvailable=has_design, items={}, groups={},
                         anweightRatioDiagnostic=ratio_diagnostic)
        for spec in specs[sid]:
            states = classify(rows, spec)
            study_out['items'][spec['id']] = dict(
                new=spec['new'],
                reference=reference(states, weights, design, spec['categories'], everyone, True))
        if gs:
            valid_parties = set(gs['nationalParty2Field']['validCodes'])
            vote, party = gs['columns']['vote'], gs['columns']['party2']
            party_of, accounting = vote_party_states(rows, gs)
            study_out['eligibilityAccounting'] = accounting
            for group in gs['groupsInDeclaredApiOrder']:
                code = group['party2Code']
                if code not in valid_parties:
                    raise RunError('group code outside contract')
                domain = [p == code for p in party_of]
                pairs = {}
                for spec in specs[sid]:
                    if not spec['new'] and sid != 'ESS9e03_3':
                        continue
                    states = classify(rows, spec)
                    pairs[spec['id']] = reference(states, weights, design, spec['categories'],
                                                  domain, sid == 'ESS9e03_3')
                study_out['groups'][group['groupId']] = dict(groupSize=sum(domain), pairs=pairs)
        output['studies'][sid] = study_out
    return output


PRIVATE_DIR = ROOT / 'data/local/v22'
PRIVATE_RUN = PRIVATE_DIR / 'run.json'
PLAN_TAG = 'analyseplan-v2.2'
FROZEN_FILES = (
    'docs/analyseplan-v2.2.md',
    'data/politikprofil-v2.2.ergaenzung.json',
    'data/analysevertrag.v2.entwurf.json',
    'data/gruppenvertrag.v2.1.entwurf.json',
    'pipeline/v22/survey.py',
    'pipeline/v22/run_v22.py',
)


def git(*args: str) -> str:
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True).stdout.decode()


def gate() -> str:
    """Positive gate: the tag exists locally and on origin with the same target, and every
    frozen file in the working tree equals its version in the tag. Returns the tag commit."""
    try:
        local = git('rev-parse', f'{PLAN_TAG}^{{commit}}').strip()
        remote = git('ls-remote', 'origin', f'refs/tags/{PLAN_TAG}^{{}}', f'refs/tags/{PLAN_TAG}')
    except subprocess.CalledProcessError as error:
        raise RunError('plan tag missing') from error
    refs = dict(reversed(line.split('\t')) for line in remote.splitlines() if line)
    remote_target = refs.get(f'refs/tags/{PLAN_TAG}^{{}}', refs.get(f'refs/tags/{PLAN_TAG}'))
    if remote_target != local:
        raise RunError('plan tag not published on origin with the same target')
    for path in FROZEN_FILES:
        frozen = subprocess.run(['git', 'show', f'{local}:{path}'], cwd=ROOT,
                                capture_output=True, check=False).stdout
        if frozen != (ROOT / path).read_bytes():
            raise RunError('working tree differs from frozen plan files')
    return local


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        tag_commit = gate()
        private_root = (ROOT / 'data/local').resolve()
        if private_root != ROOT.resolve() / 'data/local' or PRIVATE_RUN.exists():
            raise RunError('private output path unavailable or existing private run')
        if PRIVATE_DIR.exists() and (PRIVATE_DIR.is_symlink() or PRIVATE_DIR.resolve() != private_root / 'v22'):
            raise RunError('private output path unavailable or existing private run')
        PRIVATE_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
        result = run(ROOT / 'data/analysevertrag.v2.entwurf.json',
                     ROOT / 'data/gruppenvertrag.v2.1.entwurf.json',
                     ROOT / 'data/politikprofil-v2.2.ergaenzung.json')
    except RunError as error:
        print(json.dumps({'status': 'refused_or_failed', 'reason': str(error)}))
        return 1
    result['planTagCommit'] = tag_commit
    text = json.dumps(result, ensure_ascii=False, indent=1, sort_keys=True)
    fd = os.open(PRIVATE_RUN, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as handle:
        handle.write(text)
    print(json.dumps({'status': 'written', 'path': str(PRIVATE_RUN.relative_to(ROOT)),
                      'sha256': hashlib.sha256(text.encode()).hexdigest(), 'planTagCommit': tag_commit}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
