#!/usr/bin/env python3
"""Private v2.2 design run for ESS5 and ESS8 with the SDDF files (Analyseplan v2.2, 4.1).

Plan 4.1: once the SDDF files exist, ESS5 and ESS8 get 95 % intervals by the same
procedure, without a new plan, if every German case maps via `idno` to exactly one design
row; otherwise no interval for that study. As for ESS9 in the frozen run, every single
reference and every vote-group pair of these studies is computed with intervals: the v2
and v2.1 questions and the new v2.2 questions. The point estimates come from the frozen
functions in run_v22.py. export_v22.py requires them to equal the frozen private run and
the published v2 and v2.1 files before anything is exported.

The SDDF variable PROB is not used. Strata come from STRATIFY (ESS5) or stratum (ESS8),
PSUs from PSU. Writes only data/local/v22/sddf-run.json (0600). Prints no rows,
identifiers, single weights or counts. Same positive gate as run_v22.py; in addition the
frozen private run must exist with the hash recorded in reports/claude/v22-laufbeleg.json.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from pipeline.v22.run_v22 import (  # noqa: E402
    PRIVATE_DIR, PRIVATE_RUN, RunError, classify, code_of, gate, item_specs, positive,
    ratio_diagnostic, read_de, reference, sha256_file, vote_party_states)
from pipeline.v22.sav import SavError, read_sav  # noqa: E402

SDDF_RUN = PRIVATE_DIR / 'sddf-run.json'
RECEIPT = ROOT / 'reports/claude/v22-laufbeleg.json'
SDDF = {
    'ESS5e03_6': dict(path='data/raw/ess5-sddf-de/ESS5_DE_SDDF.sav', format='sav',
                      sha256='dbd02a1e0ff891be5587c715a6c75d8d6c58ada00e2b8f7d08304704a74c2b48',
                      stratum='stratify'),
    'ESS8e02_3': dict(path='data/raw/ess8-sddf-1.1/ESS8SDDFe01_1.csv', format='csv',
                      sha256='bbcb3f7f2acf2a0acdd1de90bd383f908e1a6d8a4fab553d37ac4128de7bf9e1',
                      stratum='stratum'),
}


def canonical_id(value) -> str:
    """Canonical integer text of an identifier from CSV text or an SPSS number."""
    if isinstance(value, float):
        if not (math.isfinite(value) and value >= 0 and value == int(value)):
            raise RunError('invalid design identifier')
        return str(int(value))
    kind, code = code_of(value if isinstance(value, str) else '')
    if kind != 'code':
        raise RunError('invalid design identifier')
    return code


def read_design(spec: dict, path: Path) -> dict[str, tuple[str, str]]:
    """German design rows: canonical idno -> (stratum, psu). Refuses duplicates, blanks
    and, for the country file, any other country."""
    if spec['format'] == 'sav':
        try:
            raw = read_sav(path, ['cntry', 'idno', 'psu', spec['stratum']])
        except SavError as error:
            raise RunError('design file unreadable') from error
        if any(r['cntry'] != 'DE' for r in raw):
            raise RunError('design file contains other countries')
    else:
        with open(path, newline='', encoding='utf-8') as handle:
            raw = [r for r in csv.DictReader(handle) if r['cntry'] == 'DE']
    design: dict[str, tuple[str, str]] = {}
    for row in raw:
        idno = canonical_id(row['idno'])
        stratum, psu = row[spec['stratum']], row['psu']
        if stratum in (None, '') or psu in (None, ''):
            raise RunError('incomplete design row')
        if idno in design:
            raise RunError('duplicate design identifier')
        design[idno] = (str(stratum), canonical_id(psu))
    return design


def linked_design(rows: list[dict], design: dict[str, tuple[str, str]]):
    """Plan 4.1: every German case maps to exactly one design row, and no design row is
    left over. Returns the design per case or None."""
    ids = [canonical_id(r['idno']) for r in rows]
    if len(set(ids)) != len(ids) or set(ids) != set(design):
        return None
    return [design[i] for i in ids]


def run_study(study: dict, gs: dict | None, specs: list[dict], design_path: Path,
              design_spec: dict, verify_hashes: bool = True) -> dict:
    sid = study['study_id']
    path = Path(study['input']['path'])
    path = path if path.is_absolute() else ROOT / path
    if verify_hashes and (sha256_file(path) != study['input']['sha256']
                          or sha256_file(design_path) != design_spec['sha256']):
        raise RunError('input hash mismatch')
    columns = ['cntry', 'essround', 'edition', 'idno', 'pspwght', 'dweight', 'anweight']
    columns += [s['variable'] for s in specs]
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
    design = linked_design(rows, read_design(design_spec, design_path))
    out = dict(deRows=len(rows), designAvailable=design is not None,
               designSource=dict(path=design_spec['path'], sha256=design_spec['sha256'],
                                 linkage='complete_one_to_one' if design else 'incomplete'),
               items={}, groups={})
    if design is None:
        return out
    weights = {w: [positive(r[w]) for r in rows] for w in ('pspwght', 'dweight', 'anweight')}
    everyone = [True] * len(rows)
    out['anweightRatioAllGermanCases'] = ratio_diagnostic(
        weights['anweight'], weights['pspwght'], everyone)
    states = {spec['id']: classify(rows, spec) for spec in specs}
    for spec in specs:
        out['items'][spec['id']] = dict(new=spec['new'], reference=reference(
            states[spec['id']], weights, design, spec['categories'], everyone, True))
    if gs:
        party_of, accounting = vote_party_states(rows, gs)
        out['eligibilityAccounting'] = accounting
        out['anweightRatioEligibleGroupCases'] = ratio_diagnostic(
            weights['anweight'], weights['pspwght'], [p is not None for p in party_of])
        valid_parties = set(gs['nationalParty2Field']['validCodes'])
        for group in gs['groupsInDeclaredApiOrder']:
            code = group['party2Code']
            if code not in valid_parties:
                raise RunError('group code outside contract')
            domain = [p == code for p in party_of]
            out['groups'][group['groupId']] = dict(groupSize=sum(domain), pairs={
                spec['id']: reference(states[spec['id']], weights, design, spec['categories'],
                                      domain, True)
                for spec in specs})
    return out


def run(contract_path: Path, group_contract_path: Path, supplement_path: Path,
        verify_hashes: bool = True) -> dict:
    contract = json.loads(contract_path.read_text())
    groups = {s['studyId']: s for s in json.loads(group_contract_path.read_text())['studies']}
    specs = item_specs(contract, json.loads(supplement_path.read_text()))
    output = dict(schemaVersion=1, plan='docs/analyseplan-v2.2.md', section='4.1', studies={})
    for study in contract['studies']:
        sid = study['study_id']
        if sid not in SDDF:
            continue
        output['studies'][sid] = run_study(study, groups.get(sid), specs[sid],
                                           ROOT / SDDF[sid]['path'], SDDF[sid], verify_hashes)
    return output


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        tag_commit = gate()
        receipt = json.loads(RECEIPT.read_text())
        if not PRIVATE_RUN.exists() or sha256_file(PRIVATE_RUN) != receipt['privateRunSha256']:
            raise RunError('frozen private run missing or changed')
        if PRIVATE_DIR.is_symlink() or PRIVATE_DIR.stat().st_mode & 0o077:
            raise RunError('private output directory is not a plain 0700 directory')
        if SDDF_RUN.exists():
            raise RunError('existing private design run')
        result = run(ROOT / 'data/analysevertrag.v2.entwurf.json',
                     ROOT / 'data/gruppenvertrag.v2.1.entwurf.json',
                     ROOT / 'data/politikprofil-v2.2.ergaenzung.json')
    except RunError as error:
        print(json.dumps({'status': 'refused_or_failed', 'reason': str(error)}))
        return 1
    result['planTagCommit'] = tag_commit
    result['privateRunSha256'] = receipt['privateRunSha256']
    text = json.dumps(result, ensure_ascii=False, indent=1, sort_keys=True)
    fd = os.open(SDDF_RUN, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as handle:
        handle.write(text)
    print(json.dumps({'status': 'written', 'path': str(SDDF_RUN.relative_to(ROOT)),
                      'sha256': hashlib.sha256(text.encode()).hexdigest(),
                      'designLinkage': {sid: s['designSource']['linkage']
                                        for sid, s in result['studies'].items()}}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
