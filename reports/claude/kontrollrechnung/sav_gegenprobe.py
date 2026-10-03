#!/usr/bin/env python3
"""Zweite, unabhängige Dekodierung der ESS5-Designdatei (LIFE-93, Fortsetzung 4. Oktober 2026).

Der Designlauf und die SDDF-Gegenprobe lesen `ESS5_DE_SDDF.sav` beide mit dem eigenen Leser
`pipeline/v22/sav.py`. Dieses Skript liest die Datei zusätzlich mit pyreadstat (ReadStat,
C-Bibliothek von Evan Miller, unabhängig vom Projektcode) in einer isolierten Umgebung:

    uv venv outputs/claude/venv-readstat
    uv pip install --python outputs/claude/venv-readstat/bin/python pyreadstat pandas
    PYTHONDONTWRITEBYTECODE=1 outputs/claude/venv-readstat/bin/python \\
        reports/claude/kontrollrechnung/sav_gegenprobe.py

Es prüft:
1. Dateimetadaten laut ReadStat (Variablen, Typen, Fallzahl, Kodierung).
2. Feldweise Gleichheit von CNTRY, IDNO, PSU, SAMPPOIN, STRATIFY und PROB zwischen ReadStat
   und sav.py, Zeile für Zeile.
3. Die Eins-zu-eins-Zuordnung zu den deutschen Fällen der ESS5-Hauptdatei, gelesen mit dem
   CSV-Leser der Kontrollrechnung V1 (nicht mit pipeline/v22).
4. Anteile und Standardfehler aller vorbereiteten ESS5-Referenzen und -Gruppenpaare mit
   Codex' categorical_reference und dem Design aus ReadStat, verglichen mit dem privaten
   Designlauf. Dieser Teil nutzt sav.py nicht.

Gibt nur Zählungen, Gleichheitsbefunde und größte Abweichungen aus. Keine Kennungen, Werte,
Gewichte oder Zeilen. Schreibt nur `sav-gegenprobe.json` neben diese Datei. Liest die privaten
Läufe nur und überschreibt sie nicht.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import pyreadstat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))
from kontrolle import CANON, classify, read_de  # noqa: E402
from pipeline.policy_reference_v2 import DesignUnit, categorical_reference  # noqa: E402

SAV = ROOT / 'data/raw/ess5-sddf-de/ESS5_DE_SDDF.sav'
SID = 'ESS5e03_6'
FIELDS = ['CNTRY', 'IDNO', 'PSU', 'SAMPPOIN', 'STRATIFY', 'PROB']


def missing(value) -> bool:
    return value is None or (isinstance(value, float) and math.isnan(value))


def integer_text(value) -> str:
    if isinstance(value, float):
        if not (math.isfinite(value) and value == int(value)):
            raise SystemExit('nicht ganzzahlige Kennung')
        return str(int(value))
    match = CANON.match(value)
    if match is None:
        raise SystemExit('nicht kanonische Kennung')
    return match.group(1)


def readstat_rows():
    frame, meta = pyreadstat.read_sav(str(SAV), apply_value_formats=False,
                                      user_missing=False, dates_as_pandas_datetime=False)
    rows = frame.to_dict('records')
    info = dict(
        library=f'pyreadstat {pyreadstat.__version__}',
        rows=meta.number_rows, columns=meta.number_columns,
        columnNames=list(meta.column_names), fileEncoding=meta.file_encoding,
        readstatTypes={k: v for k, v in meta.readstat_variable_types.items()},
        variableLabelsPresent=sum(1 for v in meta.column_labels if v),
        valueLabelSets=len(meta.variable_value_labels),
        fileLabel=bool(meta.file_label), notes=len(meta.notes or []))
    return rows, info


def compare_decoders(stat_rows):
    from pipeline.v22.sav import read_sav  # only for the decoder comparison
    own = read_sav(SAV, [f.lower() for f in FIELDS])
    result = dict(rowsReadStat=len(stat_rows), rowsSavPy=len(own), fields={})
    if len(own) != len(stat_rows):
        return result
    for field in FIELDS:
        equal = differ = 0
        for a, b in zip(stat_rows, own):
            x, y = a[field], b[field.lower()]
            if missing(x) and missing(y):
                equal += 1
            elif isinstance(x, str) or isinstance(y, str):
                equal += (str(x).rstrip() == str(y).rstrip())
                differ += (str(x).rstrip() != str(y).rstrip())
            else:
                same = not missing(x) and not missing(y) and float(x) == float(y)
                equal += same
                differ += not same
        result['fields'][field] = dict(equal=equal, different=differ)
    return result


def questions():
    contract = json.loads((ROOT / 'data/analysevertrag.v2.entwurf.json').read_text())
    supplement = json.loads((ROOT / 'data/politikprofil-v2.2.ergaenzung.json').read_text())
    study = next(s for s in contract['studies'] if s['study_id'] == SID)
    out = [dict(id=q['question_id'], variable=q['variable'], categories=q['categoryCodes'],
                not_asked=set(q['structurallyNotAskedCodes']))
           for q in study['adapter']['questions']]
    out += [dict(id=i['id'], variable=i['variable'], categories=i['apiValidCodeOrder'],
                 not_asked=set(i['notAskedCodes']))
            for i in supplement['items'] if i['studyId'] == SID]
    return out, study['input']['path']


def observations(rows, question, units, domain):
    from pipeline.policy_reference_v2 import Observation
    result = []
    for row, unit, inside in zip(rows, units, domain):
        kind, code = classify(row[question['variable']])
        valid = kind == 'code' and code in question['categories']
        asked = not (kind == 'code' and code in question['not_asked'])
        result.append(Observation(response=code if valid and inside else None,
                                  weight=float(row['pspwght']), eligible=inside and asked,
                                  missing=inside and asked and not valid, design=unit))
    return result


def main() -> int:
    stat_rows, info = readstat_rows()
    report = dict(
        sav=dict(path=str(SAV.relative_to(ROOT)),
                 sha256=hashlib.sha256(SAV.read_bytes()).hexdigest()),
        readstat=info)
    report['decoderComparison'] = compare_decoders(stat_rows)

    design = {}
    duplicates = 0
    for r in stat_rows:
        key = integer_text(r['IDNO'])
        duplicates += key in design
        design[key] = DesignUnit(str(r['STRATIFY']).rstrip(), integer_text(r['PSU']))
    report['readstatDesign'] = dict(
        countries=sorted({str(r['CNTRY']).rstrip() for r in stat_rows}),
        uniqueIdno=len(design), duplicateIdno=duplicates,
        strata=len({u.stratum for u in design.values()}),
        psus=len(set(design.values())),
        psusInMoreThanOneStratum=sum(
            1 for p in {u.psu for u in design.values()}
            if len({u.stratum for u in design.values() if u.psu == p}) > 1))

    qs, path = questions()
    private = json.loads((ROOT / 'data/local/v22/sddf-run.json').read_text())['studies'][SID]
    gs = next(s for s in json.loads((ROOT / 'data/gruppenvertrag.v2.1.entwurf.json').read_text())
              ['studies'] if s['studyId'] == SID)
    vote, party = gs['columns']['vote'], gs['columns']['party2']
    rows, _, _ = read_de(ROOT / path, ['cntry', 'idno', 'pspwght', vote, party]
                         + [q['variable'] for q in qs])
    ids = [integer_text(r['idno']) for r in rows]
    report['linkage'] = dict(mainGermanRows=len(rows), mainUniqueIdno=len(set(ids)),
                             matched=len(set(ids) & set(design)),
                             onlyMain=len(set(ids) - set(design)),
                             onlyDesign=len(set(design) - set(ids)))
    if report['linkage']['onlyMain'] or report['linkage']['onlyDesign']:
        (HERE / 'sav-gegenprobe.json').write_text(json.dumps(report, indent=1) + '\n')
        print(json.dumps(report, indent=1))
        return 1
    units = [design[i] for i in ids]
    basis = sorted(set(units), key=lambda u: (u.stratum, u.psu))
    stats = dict(referenzen=0, kategorien=0, maxAbweichungAnteil=0.0,
                 maxAbweichungStandardfehler=0.0, designfreiheitsgrade=len(basis)
                 - len({u.stratum for u in basis}))

    def check(question, domain, reference):
        own = categorical_reference(study_id=SID, question_id=question['id'],
                                    categories=question['categories'],
                                    observations=observations(rows, question, units, domain),
                                    design_basis=basis)
        stats['referenzen'] += 1
        for estimate in own.estimates:
            stats['kategorien'] += 1
            stats['maxAbweichungAnteil'] = max(stats['maxAbweichungAnteil'], abs(
                estimate.proportion - reference['shares'][estimate.category]))
            theirs = reference['intervals'][estimate.category]['standardError']
            stats['maxAbweichungStandardfehler'] = max(
                stats['maxAbweichungStandardfehler'], abs(estimate.standard_error - theirs))

    everyone = [True] * len(rows)
    for q in qs:
        ref = private['items'][q['id']]['reference']
        if ref['status'] == 'prepared_pending_result_review':
            check(q, everyone, ref)
    valid_parties = set(gs['nationalParty2Field']['validCodes'])
    party_of = [classify(r[party])[1] if classify(r[vote])[1] == '1'
                and classify(r[party])[1] in valid_parties else None for r in rows]
    for group in gs['groupsInDeclaredApiOrder']:
        domain = [p == group['party2Code'] for p in party_of]
        for q in qs:
            pair = private['groups'][group['groupId']]['pairs'][q['id']]
            if pair['status'] == 'prepared_pending_result_review':
                check(q, domain, pair)
    report['standardErrorsWithReadStatDesign'] = stats
    report['designRunSha256'] = hashlib.sha256(
        (ROOT / 'data/local/v22/sddf-run.json').read_bytes()).hexdigest()
    (HERE / 'sav-gegenprobe.json').write_text(json.dumps(report, indent=1) + '\n')
    print(json.dumps(report, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
