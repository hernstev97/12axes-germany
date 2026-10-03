#!/usr/bin/env python3
"""Build reports/phasen/04-politikprofil-v22.md from the reviewed v2.2 exports.

All numbers come from data/reference-v2.2/*.json, the v2.2 catalogue supplement and
the run receipt. No number is written by hand. `--check` compares with the file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports/phasen/04-politikprofil-v22.md'
STUDIES = ['ESS5e03_6', 'ESS8e02_3', 'ESS9e03_3', 'ESS10SCe03_2', 'ESS11e04_2']
STUDY_NAMES = {
    'ESS5e03_6': 'ESS5 (2010/11, persönliches Interview)',
    'ESS8e02_3': 'ESS8 (2016/17, persönliches Interview)',
    'ESS9e03_3': 'ESS9 (2018/19, persönliches Interview)',
    'ESS10SCe03_2': 'ESS10 Self-completion (2021/22, Papier und Web)',
    'ESS11e04_2': 'ESS11 (2023, persönliches Interview)',
}
REVIEWED = 'reviewed_historical_reference'


def pct(value: float | None) -> str:
    if value is None:
        return '–'
    return f'{value * 100:.1f} %'.replace('.', ',')


def design_label(document: dict) -> str:
    if not document['designAvailable']:
        return 'nicht vollständig'
    source = document.get('designSource')
    return f'SDDF-Datei `{Path(source["path"]).name}`' if source else 'in den Daten'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(reference_dir: Path) -> str:
    catalogue = json.loads((ROOT / 'data/politikprofil-v2.2.ergaenzung.json').read_text())
    items = {item['id']: item for item in catalogue['items']}
    receipt = json.loads((ROOT / 'reports/claude/v22-laufbeleg.json').read_text())
    exports = {sid: json.loads((reference_dir / f'{sid}.json').read_text()) for sid in STUDIES}
    lines = [
        '# Politikprofil v2.2: neue Fragen und Stichprobenunsicherheit',
        '',
        'Erzeugt von `scripts/build-v22-report.py` aus den geprüften Exporten unter '
        '`data/reference-v2.2/`. Alle Zahlen stammen aus diesen Dateien. Plan: '
        '[Analyseplan v2.2](../../docs/analyseplan-v2.2.md), festgeschrieben mit dem Tag '
        f'`analyseplan-v2.2` (Commit `{receipt["planTagCommit"]}`).',
        '',
        'Die Werte beschreiben historische Befragte in Deutschland zur jeweiligen Feldzeit. '
        'Sie sind keine aktuelle Bevölkerungsnorm, keine Parteipositionen und keine '
        'Bewertung einer Antwort. Das Projekt ist weder validiert noch wissenschaftlich '
        'geprüft und kann keine Neutralität garantieren.',
        '',
        '## Eingaben und Prüfungen',
        '',
        f'- Privater Lauf: SHA-256 `{receipt["privateRunSha256"]}`, Exitcode {receipt["exitCode"]}.',
        f'- Abgleich mit v2: {receipt["consistencyWithPublishedV2"]}',
        f'- Unabhängige Gegenprobe der Anteile: {receipt["independentCrossCheck"]["shares"]}',
        f'- Unabhängige Gegenprobe der Standardfehler: {receipt["independentCrossCheck"]["standardErrors"]}',
        f'- Designlauf für ESS5 und ESS8 mit den SDDF-Dateien: SHA-256 `{receipt["designRun"]["designRunSha256"]}`, '
        f'Exitcode {receipt["designRun"]["exitCode"]}.',
        f'- Unabhängige Gegenprobe der ESS5/ESS8-Bereiche: {receipt["designRun"]["independentCrossCheck"]}',
        '- Ergebnisprüfungen vor dem Export (KI-Reviews, Codex): `reports/claude/pruefungen/E1-ergebnis-v22.md` '
        'und `reports/claude/pruefungen/E1-runde2-ergebnis-v22.md`.',
        '',
        'Exportdateien:',
        '',
    ]
    for sid in STUDIES:
        path = reference_dir / f'{sid}.json'
        lines.append(f'- `{path.relative_to(ROOT)}`: `{sha(path)}`')
    lines += [
        '',
        '## Stichprobenunsicherheit',
        '',
        'Für Befragungen mit vollständigem Stichprobendesign in den Daten oder in der Designdatei '
        '(SDDF) enthält jede '
        'veröffentlichte Kategorie einen 95-%-Bereich (Taylor-Linearisierung, Logit-Intervall, '
        'Design-Freiheitsgrade). Er beschreibt nur die Unsicherheit durch die damalige '
        'Zufallsstichprobe unter vereinfachenden Annahmen, nicht den Zeitabstand, den Modus, '
        'Nichtteilnahme oder den neuen Fragekontext. Nahe 0 und 100 % kann er die tatsächliche '
        'Unsicherheit unterschätzen.',
        '',
        '| Befragung | Stichprobendesign | Strata | PSUs | Freiheitsgrade | Einzelreferenzen mit Bereich |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    for sid in STUDIES:
        document = exports[sid]
        with_interval = [q for q in document['questions']
                         if q['reference'] and q['reference']['interval']]
        design = with_interval[0]['reference']['interval'] if with_interval else None
        lines.append(
            f'| {STUDY_NAMES[sid]} | {design_label(document)} | '
            f'{design["strata"] if design else "–"} | {design["psus"] if design else "–"} | '
            f'{design["degreesOfFreedom"] if design else "–"} | {len(with_interval)} |')
    lines += [
        '',
        '## Neue Fragen',
        '',
        'Anteile unter gültigen Antworten, gewichtet mit `pspwght`. Zurückgehaltene Referenzen '
        '(weniger als 100 gültige Antworten oder eine beobachtete Kategorie mit ein bis vier '
        'Fällen) erscheinen ohne Zahlen.',
        '',
    ]
    for sid in STUDIES:
        for question in exports[sid]['questions']:
            item = items.get(question['id'])
            if not item:
                continue
            lines += [f'### {item["originalQuestionId"]} `{item["variable"]}` ({STUDY_NAMES[sid]})', '',
                      f'„{item["wordingDe"]}“', '']
            reference = question['reference']
            if question['status'] != REVIEWED or reference is None:
                lines += [f'Keine Zahlen: Status `{question["status"]}`.', '']
                continue
            labels = {c['code']: c['labelDe'] for c in item['categories']}
            lines += ['| Antwortkategorie | Anteil | 95-%-Bereich |', '| --- | --- | --- |']
            for category in reference['categories']:
                interval = ('–' if category['lower'] is None
                            else f'{pct(category["lower"])} bis {pct(category["upper"])}')
                lines.append(f'| {labels[category["code"]]} | {pct(category["proportion"])} | {interval} |')
            lines += ['', f'Gültige Antworten: {reference["validCount"]}. Basis Deutschland: '
                      f'{reference["totalCount"]}. Fehlende Antworten: {reference["missingCount"]}. '
                      f'Nicht gestellt: {reference["notAskedCount"]}.', '']
    lines += ['## Gruppenpaare', '',
              'Wählergruppen nach erinnerter Zweitstimme der jeweils letzten Bundestagswahl vor der '
              'Befragung, wie in v2.1. Keine Parteipositionen und kein Abstand zu Parteien.', '',
              '| Befragung | Veröffentlichte Paare | Zurückgehaltene Paare | Paare mit Bereich |',
              '| --- | --- | --- | --- |']
    for sid in STUDIES:
        pairs = [p for g in exports[sid]['groups'] for p in g['pairs']]
        if not pairs:
            continue
        published = [p for p in pairs if p['status'] == REVIEWED]
        with_interval = [p for p in published if p['reference']['interval']]
        lines.append(f'| {STUDY_NAMES[sid]} | {len(published)} | {len(pairs) - len(published)} | '
                     f'{len(with_interval)} |')
    lines.append('')
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--references', default='data/reference-v2.2')
    args = parser.parse_args()
    text = build(ROOT / args.references)
    if args.check:
        if OUT.read_text() != text:
            print('v22 report differs', file=sys.stderr)
            return 1
        print(f'v22 report reproduced; sha256={hashlib.sha256(text.encode()).hexdigest()}')
        return 0
    OUT.write_text(text)
    print(f'wrote {OUT.relative_to(ROOT)} sha256={hashlib.sha256(text.encode()).hexdigest()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
