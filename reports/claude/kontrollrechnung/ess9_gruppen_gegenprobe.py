#!/usr/bin/env python3
"""Unabhängige Gegenprobe der Standardfehler für die ESS9-Gruppenpaare.

Wie `sddf_gegenprobe.py`, aber für ESS9: Das Design (`stratum`, `psu`) steht in der
Hauptdatei. Vergleicht Anteile und Standardfehler aller vorbereiteten ESS9-Gruppenpaare
und Einzelreferenzen des eingefrorenen privaten Laufs `data/local/v22/run.json` mit Codex'
`categorical_reference`. Schreibt nur `ess9-gruppen-gegenprobe.json` neben diese Datei:
Zahl der Referenzen und Kategorien und die größten Abweichungen.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))
from kontrolle import classify, read_de  # noqa: E402
from pipeline.policy_reference_v2 import DesignUnit, categorical_reference  # noqa: E402
from sddf_gegenprobe import TOLERANCE, compare, observations, questions  # noqa: E402

SID = 'ESS9e03_3'


def main() -> int:
    run_bytes = (ROOT / 'data/local/v22/run.json').read_bytes()
    study = json.loads(run_bytes)['studies'][SID]
    gs = next(s for s in json.loads((ROOT / 'data/gruppenvertrag.v2.1.entwurf.json').read_text())
              ['studies'] if s['studyId'] == SID)
    vote, party = gs['columns']['vote'], gs['columns']['party2']
    qs = questions(SID)
    path = next(s for s in json.loads((ROOT / 'data/analysevertrag.v2.entwurf.json').read_text())
                ['studies'] if s['study_id'] == SID)['input']['path']
    rows, _, _ = read_de(ROOT / path, ['cntry', 'idno', 'pspwght', 'psu', 'stratum', vote, party]
                         + [q['variable'] for q in qs])
    units = [DesignUnit(r['stratum'], r['psu']) for r in rows]
    basis = sorted(set(units), key=lambda u: (u.stratum, u.psu))
    stats = dict(referenzen=0, kategorien=0, ohneBereichImLauf=0,
                 maxAbweichungAnteil=0.0, maxAbweichungStandardfehler=0.0)
    everyone = [True] * len(rows)
    for q in qs:
        reference = study['items'][q['id']]['reference']
        if reference['status'] == 'prepared_pending_result_review':
            compare(categorical_reference(study_id=SID, question_id=q['id'], categories=q['categories'],
                                          observations=observations(rows, q, units, everyone),
                                          design_basis=basis), reference, stats)
    valid_parties = set(gs['nationalParty2Field']['validCodes'])
    party_of = [classify(r[party])[1] if classify(r[vote])[1] == '1'
                and classify(r[party])[1] in valid_parties else None for r in rows]
    for group in gs['groupsInDeclaredApiOrder']:
        domain = [p == group['party2Code'] for p in party_of]
        for q in qs:
            pair = study['groups'][group['groupId']]['pairs'][q['id']]
            if pair['status'] == 'prepared_pending_result_review':
                compare(categorical_reference(study_id=SID, question_id=q['id'],
                                              categories=q['categories'],
                                              observations=observations(rows, q, units, domain),
                                              design_basis=basis), pair, stats)
    stats['strata'] = len({u.stratum for u in basis})
    stats['psus'] = len(basis)
    stats['eindeutigeIdno'] = len({r['idno'] for r in rows}) == len(rows)
    stats['status'] = 'BESTANDEN' if (
        stats['eindeutigeIdno'] and stats['referenzen'] > 0 and stats['ohneBereichImLauf'] == 0
        and stats['maxAbweichungAnteil'] <= TOLERANCE
        and stats['maxAbweichungStandardfehler'] <= TOLERANCE) else 'NICHT_BESTANDEN'
    report = dict(privateRunSha256=hashlib.sha256(run_bytes).hexdigest(), toleranz=TOLERANCE,
                  status=stats['status'], studien={SID: stats})
    (HERE / 'ess9-gruppen-gegenprobe.json').write_text(json.dumps(report, indent=1) + '\n')
    print(json.dumps(report, indent=1))
    return 0 if report['status'] == 'BESTANDEN' else 1


if __name__ == '__main__':
    raise SystemExit(main())
