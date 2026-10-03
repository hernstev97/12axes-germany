#!/usr/bin/env python3
"""Private v2.2 run (Analyseplan v2.2, Abschnitte 3, 4 und 6).

Computes, from the local ESS CSV files:
- single references for the 18 new questions (all five studies as needed),
- historical vote-group references for new ESS5/ESS8 questions (v2.1 groups),
- design-based 95 % intervals for every single reference of studies with a
  complete design (ESS9, ESS10-SC, ESS11) and for ESS9 group pairs,
- recomputed shares of the 43 v2 questions as a consistency check.

Writes only data/local/v22/run.json (directory 0700, file 0600). Prints no
rows, identifiers, single weights or counts. Refuses to run unless the tag
`analyseplan-v2.2` exists, unless --synthetic is given for tests.
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
    match = CANON.match(raw)
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
        columns = ['cntry', 'essround', 'edition', 'idno', 'pspwght', 'dweight', 'psu', 'stratum']
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
        weights = {w: [positive(r[w]) for r in rows] for w in ('pspwght', 'dweight')}
        has_design = all(r.get('psu', '') != '' and r.get('stratum', '') != '' for r in rows) \
            and 'psu' in rows[0]
        design = [(r['stratum'], r['psu']) for r in rows] if has_design else None
        everyone = [True] * len(rows)
        study_out = dict(deRows=len(rows), designAvailable=has_design, items={}, groups={})
        for spec in specs[sid]:
            states = classify(rows, spec)
            study_out['items'][spec['id']] = dict(
                new=spec['new'],
                reference=reference(states, weights, design, spec['categories'], everyone, True))
        if gs:
            valid_parties = set(gs['nationalParty2Field']['validCodes'])
            vote, party = gs['columns']['vote'], gs['columns']['party2']
            party_of = [code_of(r[party])[1] if code_of(r[vote])[1] == '1' else None for r in rows]
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


def plan_tag_present() -> bool:
    result = subprocess.run(['git', 'rev-parse', '--verify', '--quiet', 'analyseplan-v2.2^{}'],
                            cwd=ROOT, capture_output=True, text=True)
    return result.returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', default='data/local/v22/run.json')
    args = parser.parse_args()
    if not plan_tag_present():
        print(json.dumps({'status': 'refused', 'reason': 'analyseplan-v2.2 tag missing'}))
        return 1
    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    os.chmod(out.parent, 0o700)
    if out.exists():
        print(json.dumps({'status': 'refused', 'reason': 'existing private run'}))
        return 1
    try:
        result = run(ROOT / 'data/analysevertrag.v2.entwurf.json',
                     ROOT / 'data/gruppenvertrag.v2.1.entwurf.json',
                     ROOT / 'data/politikprofil-v2.2.ergaenzung.json')
    except RunError as error:
        print(json.dumps({'status': 'failed', 'reason': str(error)}))
        return 1
    text = json.dumps(result, ensure_ascii=False, indent=1, sort_keys=True)
    fd = os.open(out, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as handle:
        handle.write(text)
    print(json.dumps({'status': 'written', 'path': args.out,
                      'sha256': hashlib.sha256(text.encode()).hexdigest()}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
