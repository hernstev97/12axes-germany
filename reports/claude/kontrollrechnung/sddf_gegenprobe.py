#!/usr/bin/env python3
"""Unabhängige Gegenprobe der ESS5- und ESS8-Bereiche aus dem SDDF-Lauf.

Rechnet Anteile und Standardfehler für ESS5 und ESS8 mit Codex' vorhandener Funktion
`pipeline/policy_reference_v2.categorical_reference` neu und vergleicht sie mit dem privaten
Designlauf `data/local/v22/sddf-run.json`. Einlesen, Kodierung und Gruppenbildung folgen
der unabhängigen Kontrollrechnung V1 (`kontrolle.py`), nicht `pipeline/v22/run_v22.py`.
Die ESS8-SDDF wird hier direkt als CSV gelesen. Für die ESS5-SDDF gibt es nur den Leser
`pipeline/v22/sav.py`; seine Richtigkeit stützt der vollständige idno-Abgleich.

Schreibt nur `sddf-gegenprobe.json` neben diese Datei: Zahl der verglichenen Referenzen
und Kategorien sowie die größten Abweichungen. Keine Werte, Zeilen, Kennungen oder Gewichte.
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))
from kontrolle import CANON, classify, read_de  # noqa: E402
from pipeline.policy_reference_v2 import DesignUnit, Observation, categorical_reference  # noqa: E402
from pipeline.v22.sav import read_sav  # noqa: E402

# Same tolerance as the export check against published values (export_v22.TOLERANCE).
TOLERANCE = 1e-12
SDDF = {
    'ESS5e03_6': ('data/raw/ess5-sddf-de/ESS5_DE_SDDF.sav', 'stratify'),
    'ESS8e02_3': ('data/raw/ess8-sddf-1.1/ESS8SDDFe01_1.csv', 'stratum'),
}


def integer_text(value) -> str:
    if isinstance(value, float):
        return str(int(value))
    match = CANON.match(value)
    if match is None:
        raise SystemExit('nicht kanonische Kennung')
    return match.group(1)


def design_rows(sid: str) -> tuple[dict[str, DesignUnit], int]:
    """German design rows by idno and the number of duplicate idno."""
    path, stratum = SDDF[sid]
    if path.endswith('.sav'):
        rows = read_sav(ROOT / path, ['cntry', 'idno', 'psu', stratum])
    else:
        with open(ROOT / path, newline='', encoding='utf-8') as handle:
            rows = [r for r in csv.DictReader(handle) if r['cntry'] == 'DE']
    design: dict[str, DesignUnit] = {}
    duplicates = 0
    for r in rows:
        key = integer_text(r['idno'])
        duplicates += key in design
        design[key] = DesignUnit(str(r[stratum]), integer_text(r['psu']))
    return design, duplicates


def questions(sid: str) -> list[dict]:
    contract = json.loads((ROOT / 'data/analysevertrag.v2.entwurf.json').read_text())
    supplement = json.loads((ROOT / 'data/politikprofil-v2.2.ergaenzung.json').read_text())
    study = next(s for s in contract['studies'] if s['study_id'] == sid)
    out = [dict(id=q['question_id'], variable=q['variable'], categories=q['categoryCodes'],
                missing={c for c in q['missingCodes'] if c != ''},
                not_asked=set(q['structurallyNotAskedCodes']))
           for q in study['adapter']['questions']]
    out += [dict(id=i['id'], variable=i['variable'], categories=i['apiValidCodeOrder'],
                 missing={m['code'] for m in i['missingCodes']}, not_asked=set(i['notAskedCodes']))
            for i in supplement['items'] if i['studyId'] == sid]
    return out


def observations(rows, question, units, domain):
    result = []
    for row, unit, inside in zip(rows, units, domain):
        kind, code = classify(row[question['variable']])
        valid = kind == 'code' and code in question['categories']
        asked = not (kind == 'code' and code in question['not_asked'])
        result.append(Observation(response=code if valid and inside else None,
                                  weight=float(row['pspwght']), eligible=inside and asked,
                                  missing=inside and asked and not valid, design=unit))
    return result


def compare(own, private, stats):
    if private.get('intervals') is None:
        stats['ohneBereichImLauf'] += 1
        return
    stats['referenzen'] += 1
    for estimate in own.estimates:
        stats['kategorien'] += 1
        theirs = private['intervals'][estimate.category]
        stats['maxAbweichungAnteil'] = max(stats['maxAbweichungAnteil'], abs(
            estimate.proportion - private['shares'][estimate.category]))
        stats['maxAbweichungStandardfehler'] = max(stats['maxAbweichungStandardfehler'], abs(
            estimate.standard_error - theirs['standardError']))


def main() -> int:
    run_bytes = (ROOT / 'data/local/v22/sddf-run.json').read_bytes()
    private = json.loads(run_bytes)
    groups = {s['studyId']: s for s in json.loads(
        (ROOT / 'data/gruppenvertrag.v2.1.entwurf.json').read_text())['studies']}
    report = dict(designRunSha256=hashlib.sha256(run_bytes).hexdigest(), studien={})
    for sid in SDDF:
        study = private['studies'][sid]
        gs = groups[sid]
        vote, party = gs['columns']['vote'], gs['columns']['party2']
        qs = questions(sid)
        path = next(s for s in json.loads((ROOT / 'data/analysevertrag.v2.entwurf.json')
                                          .read_text())['studies'] if s['study_id'] == sid)['input']['path']
        rows, _, _ = read_de(ROOT / path, ['cntry', 'idno', 'pspwght', vote, party]
                             + [q['variable'] for q in qs])
        design, duplicates = design_rows(sid)
        ids = [integer_text(r['idno']) for r in rows]
        linkage = dict(duplicateDesignIdno=duplicates, mainUnique=len(set(ids)) == len(ids),
                       sameSet=set(ids) == set(design))
        if duplicates or not linkage['mainUnique'] or not linkage['sameSet']:
            report['studien'][sid] = dict(zuordnung=linkage, status='NICHT_BESTANDEN')
            continue
        units = [design[i] for i in ids]
        basis = sorted(set(units), key=lambda u: (u.stratum, u.psu))
        stats = dict(referenzen=0, kategorien=0, ohneBereichImLauf=0,
                     maxAbweichungAnteil=0.0, maxAbweichungStandardfehler=0.0)
        everyone = [True] * len(rows)
        for q in qs:
            reference = study['items'][q['id']]['reference']
            if reference['status'] != 'prepared_pending_result_review':
                continue
            own = categorical_reference(study_id=sid, question_id=q['id'], categories=q['categories'],
                                        observations=observations(rows, q, units, everyone),
                                        design_basis=basis)
            compare(own, reference, stats)
        valid_parties = set(gs['nationalParty2Field']['validCodes'])
        party_of = [classify(r[party])[1] if classify(r[vote])[1] == '1'
                    and classify(r[party])[1] in valid_parties else None for r in rows]
        for group in gs['groupsInDeclaredApiOrder']:
            domain = [p == group['party2Code'] for p in party_of]
            for q in qs:
                pair = study['groups'][group['groupId']]['pairs'][q['id']]
                if pair['status'] != 'prepared_pending_result_review':
                    continue
                own = categorical_reference(study_id=sid, question_id=q['id'],
                                            categories=q['categories'],
                                            observations=observations(rows, q, units, domain),
                                            design_basis=basis)
                compare(own, pair, stats)
        stats['strata'] = len({u.stratum for u in basis})
        stats['psus'] = len(basis)
        stats['zuordnung'] = linkage
        stats['status'] = 'BESTANDEN' if (
            stats['referenzen'] > 0 and stats['ohneBereichImLauf'] == 0
            and stats['maxAbweichungAnteil'] <= TOLERANCE
            and stats['maxAbweichungStandardfehler'] <= TOLERANCE) else 'NICHT_BESTANDEN'
        report['studien'][sid] = stats
    report['toleranz'] = TOLERANCE
    report['status'] = 'BESTANDEN' if all(
        s['status'] == 'BESTANDEN' for s in report['studien'].values()) else 'NICHT_BESTANDEN'
    (HERE / 'sddf-gegenprobe.json').write_text(json.dumps(report, indent=1) + '\n')
    print(json.dumps(report, indent=1))
    return 0 if report['status'] == 'BESTANDEN' else 1


if __name__ == '__main__':
    raise SystemExit(main())
