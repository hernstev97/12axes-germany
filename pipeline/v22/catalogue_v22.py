#!/usr/bin/env python3
"""Build and verify the v2.2 catalogue supplement (Analyseplan v2.2, Abschnitt 3).

Every German text below is compared automatically with the text layer of the
cached original PDF (questionnaire or response list). Codes and missing reasons
come from cached public ESS metadata. No response data are read.

    python3 pipeline/v22/catalogue_v22.py          # write data/politikprofil-v2.2.ergaenzung.json
    python3 pipeline/v22/catalogue_v22.py --check  # verify the committed file byte for byte
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'data/politikprofil-v2.2.ergaenzung.json'
SRC = 'outputs/loop/breadth-data-001/sources'
PDFS = {
    'ess5-de-questionnaire': f'{SRC}/ess5-de-questionnaire.pdf',
    'ess8-de-questionnaire': f'{SRC}/ess8-de-questionnaire.pdf',
    'ess8-de-showcards': f'{SRC}/ess8-de-showcards.pdf',
    'ess10-de-questionnaire': f'{SRC}/ess10-de-questionnaire.pdf',
}
METADATA = {
    'ESS5e03_6': ['outputs/claude/sources/ess5-candidates.json'],
    'ESS8e02_3': ['outputs/claude/sources/ess8-candidates.json'],
    'ESS10SCe03_2': ['outputs/claude/sources/ess10sc-candidates.json',
                     'outputs/claude/sources/ess10sc-candidates-2.json'],
}
FILE_METADATA = {
    'ESS5e03_6': ('0189b86b-8aa4-4be3-88ad-39c58b02f19f', 89),
    'ESS8e02_3': ('ffc43f48-e15a-4a1c-8813-47eda377c355', 98),
    'ESS10SCe03_2': None,  # filled from the cached file metadata below
}

AGREE = ['Stimme stark zu', 'Stimme zu', 'Weder noch', 'Lehne ab', 'Lehne stark ab']
AGREE_LOWER = ['stimme stark zu', 'stimme zu', 'weder noch', 'lehne ab', 'lehne stark ab']
AGAINST_FIRST = ['Sehr dagegen', 'Dagegen', 'Dafür', 'Sehr dafür']
AMOUNT = ['Eine sehr große Menge', 'Eine große Menge', 'Eine mittelgroße Menge',
          'Eine kleine Menge', 'Überhaupt nichts']

ESS10_PANDEMIC_NOTE = (
    'Bitte beantworten Sie alle Fragen nach dem heutigen Stand der Dinge, auch wenn dieser '
    'durch die Pandemie anders ist als sonst.')

ELECTRICITY_INTRO = [
    'Im grauen Kasten oben auf dieser Liste sehen Sie verschiedene Energiequellen, aus denen '
    'Strom erzeugt werden kann. Bitte lesen Sie diese kurz durch.',
]
ELECTRICITY_STEM = ('Wie viel des Stroms, der in Deutschland verbraucht wird, sollte aus jeder '
                    'dieser Energiequellen erzeugt werden?')
ASYLUM_INTRO = [
    'Es gibt Menschen, die nach Deutschland kommen und Asyl beantragen, weil sie in ihrem '
    'eigenen Land Angst vor Verfolgung haben.',
    'Bitte sagen Sie mir anhand von Liste 31, wie sehr Sie jeder der folgenden Aussagen '
    'zustimmen oder wie sehr Sie diese ablehnen.',
]
ESS10_AGREE_INTRO = [
    'Wie sehr stimmen Sie jeder der folgenden Aussagen zu oder wie sehr lehnen Sie diese ab?',
    'Markieren Sie für jede Aussage ein Kästchen.',
]

# id, study, variable, area, question, group, order, type, content, wording, intro,
# stem, categories (labels in API code order), printed-code note, sources, notes
ITEMS = [
    *[
        dict(variable=v, study='ESS8e02_3', area='climate_energy', question=q,
             group='electricity_sources', order=i + 1, responseType='ordered_amount',
             content='measure', wording=w, intro=ELECTRICITY_INTRO, stem=ELECTRICITY_STEM,
             labels=AMOUNT, extraValid=[('55', 'Ich habe noch nie etwas von dieser Energiequelle gehört')],
             pages={'ess8-de-questionnaire': [27, 28], 'ess8-de-showcards': [36]},
             listLabel='Liste 35',
             notes=['Code 55 wurde im Interview nicht vorgelesen (Kategorie in Klammern). '
                    'Die Website bietet ihn nicht als Antwort an; in historischen Referenzen bleibt '
                    'er eine eigene gültige Kategorie.',
                    'Interviewerhinweis nur auf Nachfrage: Kohle umfasst Steinkohle und Braunkohle.'])
        for i, (v, q, w) in enumerate([
            ('elgcoal', 'D4', 'Wie viel des Stroms, der in Deutschland verbraucht wird, sollte aus Kohle erzeugt werden?'),
            ('elgngas', 'D5', 'Und wie viel aus Erdgas?'),
            ('elghydr', 'D6', 'Und wie viel aus Wasserkraft, also aus Flüssen, Stauseen oder dem Meer?'),
            ('elgnuc', 'D7', 'Wie viel des Stroms, der in Deutschland verbraucht wird, sollte aus Atomkraft bzw. Kernkraft erzeugt werden?'),
            ('elgsun', 'D8', 'Und wie viel aus Sonnenenergie?'),
            ('elgwind', 'D9', 'Und wie viel aus Windkraft?'),
            ('elgbio', 'D10', 'Und wie viel Strom sollte aus Biomasse wie Holz, Pflanzen oder Tiermist gewonnen werden?'),
        ])
    ],
    dict(variable='gvrfgap', study='ESS8e02_3', area='migration', question='C42',
         group='asylum', order=1, responseType='ordered_agreement', content='principle',
         wording='Bei der Prüfung von Asylanträgen sollte der Staat großzügig sein.',
         intro=ASYLUM_INTRO, stem=None, labels=AGREE,
         pages={'ess8-de-questionnaire': [25], 'ess8-de-showcards': [32]}, listLabel='Liste 31',
         notes=['Der Fragebogen druckt die Codes 0–5; Liste 31 hat fünf beschriftete Stufen. '
                'Gebunden sind die Beschriftungen der Liste 31 und die API-Codes 1–5.']),
    dict(variable='rfgbfml', study='ESS8e02_3', area='migration', question='C44',
         group='asylum', order=2, responseType='ordered_agreement', content='principle',
         wording='Asylbewerber, deren Anträge bewilligt wurden, sollten das Recht haben, ihre '
                 'engen Familienangehörigen nach Deutschland zu holen.',
         intro=ASYLUM_INTRO, stem=None, labels=AGREE,
         pages={'ess8-de-questionnaire': [25], 'ess8-de-showcards': [32]}, listLabel='Liste 31',
         notes=['Der Fragebogen druckt die Codes 0–5; Liste 31 hat fünf beschriftete Stufen. '
                'Gebunden sind die Beschriftungen der Liste 31 und die API-Codes 1–5.',
                'C43 (Wahrnehmung der Verfolgungsangst) liegt zwischen C42 und C44 und ist nicht '
                'ausgewählt.']),
    dict(variable='basinc', study='ESS8e02_3', area='welfare', question='E36',
         group='basic_income', order=1, responseType='ordered_support', content='measure',
         wording='Alles in allem, wären Sie gegen oder für ein solches Grundeinkommen in Deutschland?',
         intro=[
             'In einigen Ländern wird momentan über die Einführung eines Grundeinkommens '
             'diskutiert. Ich werde Sie gleich fragen, ob Sie gegen oder für ein solches '
             'Grundeinkommen sind. Zuerst aber ein paar Einzelheiten dazu.',
             'Im grauen Kasten oben auf Liste 54 sehen Sie die wichtigsten Eigenschaften. Ein '
             'solches Grundeinkommen umfasst alle folgenden Punkte:',
         ],
         definition=[
             'Der Staat zahlt jedem ein monatliches Einkommen, das alle grundlegenden '
             'Lebenshaltungskosten deckt.',
             'Dadurch werden viele bestehende Sozialleistungen ersetzt.',
             'Das Ziel ist es, jedem einen minimalen Lebensstandard zu garantieren.',
             'Alle erhalten den gleichen Betrag, egal ob man arbeitet oder nicht.',
             'Man kann zudem das Einkommen aus Erwerbstätigkeit oder anderen Quellen behalten.',
             'Das Grundeinkommen wird über Steuern finanziert.',
         ],
         stem=None, labels=AGAINST_FIRST,
         pages={'ess8-de-questionnaire': [43], 'ess8-de-showcards': [55]}, listLabel='Liste 54',
         notes=['Die Einleitung nennt eine Diskussion „momentan“, also zur Feldzeit 2016/17.']),
    dict(variable='eusclbf', study='ESS8e02_3', area='europe', question='E37',
         group='eu_social_benefit', order=1, responseType='ordered_support', content='measure',
         wording='Alles in allem, wären Sie gegen oder für ein solches EU-weites '
                 'Sozialleistungsprogramm?',
         intro=[
             'Es gibt den Vorschlag in der gesamten Europäischen Union ein Programm mit '
             'Sozialleistungen für alle armen Menschen einzuführen. Ich werde Sie gleich '
             'fragen, ob Sie gegen oder für ein solches Programm sind.',
             'Im grauen Kasten oben auf Liste 55 sehen Sie die wichtigsten Eigenschaften.',
             'Ein solches EU-weites Sozialleistungsprogramm umfasst alle der folgenden Punkte:',
         ],
         definition=[
             'Das Ziel ist es, einen minimalen Lebensstandard für alle armen Menschen in der EU '
             'zu garantieren.',
             'Die Höhe der Sozialleistungen wird an die Lebenshaltungskosten im jeweiligen Land '
             'angepasst.',
             'Das Programm erfordert, dass reichere EU-Länder mehr zur Finanzierung der '
             'Sozialleistungen beitragen als ärmere EU-Länder.',
         ],
         stem=None, labels=AGAINST_FIRST,
         pages={'ess8-de-questionnaire': [44], 'ess8-de-showcards': [56]}, listLabel='Liste 55',
         notes=[]),
    dict(variable='panpriph', study='ESS10SCe03_2', area='rights_security', question='A1',
         group='pandemic_tradeoffs', order=1, responseType='ordered_tradeoff', content='principle',
         wording='Ist es bei der Bekämpfung einer Pandemie wichtiger, die Gesundheit der '
                 'Bevölkerung oder die Wirtschaft vorrangig zu berücksichtigen?',
         intro=['In diesem ersten Teil werden wir Ihnen Fragen zu einer Auswahl verschiedener '
                'Themen stellen, zunächst zu Pandemien.'],
         instruction='Bitte markieren Sie einen Kreis von 0 bis 10. 0 bedeutet, dass es viel '
                     'wichtiger ist, die Gesundheit der Bevölkerung vorrangig zu berücksichtigen, '
                     'und 10 bedeutet, dass es viel wichtiger ist, die Wirtschaft vorrangig zu '
                     'berücksichtigen.',
         stem=None, scale=('Viel wichtiger, die Gesundheit der Bevölkerung vorrangig zu berücksichtigen',
                           'Viel wichtiger, die Wirtschaft vorrangig zu berücksichtigen'),
         pages={'ess10-de-questionnaire': [2]}, listLabel=None,
         notes=['Erhoben 2021/22 während der Coronavirus-Pandemie.']),
    dict(variable='panmonpb', study='ESS10SCe03_2', area='rights_security', question='A2',
         group='pandemic_tradeoffs', order=2, responseType='ordered_tradeoff', content='principle',
         wording='Ist es bei der Bekämpfung einer Pandemie wichtiger, dass Regierungen die '
                 'Bevölkerung überwachen und nachverfolgen oder die Privatsphäre des Einzelnen '
                 'bewahren?',
         intro=['In diesem ersten Teil werden wir Ihnen Fragen zu einer Auswahl verschiedener '
                'Themen stellen, zunächst zu Pandemien.'],
         stem=None, scale=('Viel wichtiger, die Bevölkerung zu überwachen und nachzuverfolgen',
                           'Viel wichtiger, die Privatsphäre des Einzelnen zu bewahren'),
         pages={'ess10-de-questionnaire': [2]}, listLabel=None,
         notes=['Erhoben 2021/22 während der Coronavirus-Pandemie. Die Frage betrifft die '
                'Pandemiebekämpfung und deckt Digitalpolitik nicht ab.']),
    dict(variable='freehms', study='ESS10SCe03_2', area='equality_family', question='A47',
         group='same_sex_couples', order=1, responseType='ordered_agreement', content='principle',
         wording='Schwule und Lesben sollten ihr Leben so führen dürfen, wie sie es wollen.',
         intro=ESS10_AGREE_INTRO, stem=None, labels=AGREE,
         pages={'ess10-de-questionnaire': [6]}, listLabel=None, notes=[]),
    dict(variable='hmsacld', study='ESS10SCe03_2', area='equality_family', question='A49',
         group='same_sex_couples', order=2, responseType='ordered_agreement', content='principle',
         wording='Schwule und lesbische Paare sollten die gleichen Rechte haben, Kinder zu '
                 'adoptieren, wie Paare, die aus Mann und Frau bestehen.',
         intro=ESS10_AGREE_INTRO, stem=None, labels=AGREE,
         pages={'ess10-de-questionnaire': [6]}, listLabel=None,
         notes=['A48 (eigene Scham bei einem schwulen oder lesbischen Familienmitglied) liegt '
                'zwischen A47 und A49 und ist nicht ausgewählt.']),
    dict(variable='accalaw', study='ESS10SCe03_2', area='democracy_authority', question='A51',
         group='strong_leader', order=1, responseType='ordered_acceptability', content='principle',
         wording='Wie akzeptabel wäre es für Sie, wenn Deutschland eine starke Führungsperson '
                 'hätte, die über dem Gesetz steht?',
         intro=[], stem=None, scale=('Überhaupt nicht akzeptabel', 'Voll und ganz akzeptabel'),
         pages={'ess10-de-questionnaire': [6]}, listLabel=None, notes=[]),
    dict(variable='loylead', study='ESS10SCe03_2', area='democracy_authority', question='A53',
         group='authority_values', order=2, responseType='ordered_agreement', content='principle',
         wording='Was Deutschland am meisten braucht, ist Loyalität gegenüber der politischen '
                 'Führung.',
         intro=ESS10_AGREE_INTRO, stem=None, labels=AGREE,
         pages={'ess10-de-questionnaire': [6]}, listLabel=None,
         notes=['A52 (Gehorsam und Respekt vor Autorität als Erziehungswerte) steht im selben '
                'Block und ist nicht ausgewählt.']),
    dict(variable='prtyban', study='ESS5e03_6', area='democracy_authority', question='B32',
         group='party_ban', order=1, responseType='ordered_agreement', content='principle',
         wording='Politische Parteien, die die Demokratie abschaffen wollen, sollten verboten werden',
         intro=['Bitte schauen Sie jetzt auf Liste 12 und sagen Sie mir, wie sehr Sie jeder der '
                'folgenden Aussagen zustimmen oder wie sehr Sie diese ablehnen.'],
         stem=None, labels=AGREE_LOWER,
         pages={'ess5-de-questionnaire': [11, 12]}, listLabel='Liste 12',
         notes=['Die Antwortbeschriftungen stehen im Fragebogenkopf in Kleinschreibung; die Liste 12 '
                'selbst liegt nicht als eigenes Dokument vor.']),
]

STUDY_PDF = {'ESS5e03_6': 'ess5-de-questionnaire', 'ESS8e02_3': 'ess8-de-questionnaire',
             'ESS10SCe03_2': 'ess10-de-questionnaire'}


def pdf_text(source_id: str, pages: list[int]) -> str:
    path = ROOT / PDFS[source_id]
    chunks = []
    for page in pages:
        out = subprocess.run(['pdftotext', '-raw', '-f', str(page), '-l', str(page), str(path), '-'],
                             capture_output=True, text=True, check=True).stdout
        chunks.append(out)
    return '\n'.join(chunks)


def normalise(text: str) -> list[str]:
    """Two variants: line-end hyphen removed (word split) or kept (compound with hyphen)."""
    t = text.replace(' ', ' ').replace('−', ' ').replace('', ' ')
    t = re.sub(r'[ \t]+', ' ', t)
    joined = re.sub(r'-\n', '', t)
    kept = re.sub(r'-\n', '-', t)
    return [re.sub(r'\s+', ' ', variant) for variant in (joined, kept)]


def verify(text: str, haystacks: list[str], where: str) -> None:
    needle = re.sub(r'\s+', ' ', text).strip()
    if not any(needle in hay for hay in haystacks):
        raise SystemExit(f'German text not found in {where}: {needle[:90]}')


def api_fields(study: str) -> dict[str, dict]:
    fields = {}
    for path in METADATA[study]:
        data = json.loads((ROOT / path).read_text())['data']['search']
        for value in data.values():
            fields[value['name']['en']] = value
    return fields


def file_metadata(study: str) -> tuple[str, int]:
    if FILE_METADATA[study]:
        return FILE_METADATA[study]
    data = json.loads((ROOT / f'{SRC.replace("breadth-data-001", "breadth-access-002")}/ess10sc-file-metadata.json').read_text())
    meta = data['data']['search']['dataFileMetadata']
    return meta['id'], meta['version']


def sha256(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def build() -> dict:
    items = []
    for spec in ITEMS:
        study = spec['study']
        api = api_fields(study)[spec['variable']]
        texts = {sid: normalise(pdf_text(sid, pages)) for sid, pages in spec['pages'].items()}
        questionnaire = texts[STUDY_PDF[study]]
        for text in [spec['wording'], *spec['intro'], *([spec['stem']] if spec.get('stem') else []),
                     *([spec['instruction']] if spec.get('instruction') else [])]:
            verify(text, questionnaire, f'{STUDY_PDF[study]} {spec["question"]}')
        if study == 'ESS10SCe03_2':
            verify(ESS10_PANDEMIC_NOTE, normalise(pdf_text('ess10-de-questionnaire', [1])),
                   'ess10 page 1')
        for line in spec.get('definition', []):
            verify(line, texts['ess8-de-showcards'], f'showcard {spec["listLabel"]}')
            verify(line, questionnaire, f'questionnaire {spec["question"]}')
        valid = [c for c in api['fullCodeList'] if not c['isMissing']]
        missing = [c for c in api['fullCodeList'] if c['isMissing']]
        if 'labels' in spec:
            label_source = texts.get('ess8-de-showcards', questionnaire)
            for label in spec['labels']:
                verify(label, label_source, f'labels {spec["variable"]}')
            labels = list(spec['labels']) + [label for _, label in spec.get('extraValid', [])]
            if len(labels) != len(valid):
                raise SystemExit(f'label count mismatch for {spec["variable"]}')
            categories = [
                dict(code=c['value'], labelDe=label, labelEn=c['label']['en'],
                     printedCodeDe=None if spec['variable'].startswith(('gvrf', 'rfgb')) else c['value'],
                     isMissingApi=False,
                     semanticRole='unprompted_nonposition' if c['value'] == '55' else 'substantive_response',
                     offeredOnWebsite=c['value'] != '55')
                for c, label in zip(valid, labels)
            ]
        else:
            low, high = spec['scale']
            for anchor in (low, high):
                verify(anchor, questionnaire, f'anchors {spec["variable"]}')
            if [c['value'] for c in valid] != [str(i) for i in range(11)]:
                raise SystemExit(f'unexpected scale codes for {spec["variable"]}')
            categories = [
                dict(code=c['value'], labelDe=low if c['value'] == '0' else high if c['value'] == '10' else c['value'],
                     labelEn=c['label']['en'], printedCodeDe=c['value'], isMissingApi=False,
                     semanticRole='substantive_response', offeredOnWebsite=True)
                for c in valid
            ]
        file_id, file_version = file_metadata(study)
        not_asked = [c['value'] for c in missing if c['label']['en'] in ('Not applicable', 'Not asked')]
        items.append(dict(
            id=f'{study}:{spec["variable"]}', studyId=study, variable=spec['variable'],
            primaryTheme=spec['area'], originalQuestionId=spec['question'],
            wordingDe=spec['wording'], introductionsDe=spec['intro'],
            definitionDe=spec.get('definition', []), responseStemDe=spec.get('stem'),
            situationDe=None, instructionDe=spec.get('instruction'),
            groupId=spec['group'], originalOrderInGroup=spec['order'],
            responseType=spec['responseType'], responseContentType=spec['content'],
            categories=categories,
            missingCodes=[dict(code=c['value'], reasonApi=c['label']['en'], isMissingApi=True,
                               printedCodeDe=None, labelDe=None)
                          for c in missing if c['value'] not in not_asked],
            notAskedCodes=not_asked,
            apiValidCodeOrder=[c['value'] for c in valid],
            apiDeclaredCodeOrder=[c['value'] for c in api['fullCodeList']],
            sourceFieldId=api['id'], sourceFieldMetadataVersion=api['version'],
            dataFileMetadataId=file_id, dataFileMetadataVersion=file_version,
            apiVariableLabelEn=api['label']['en'],
            sourceRefs=[dict(sourceId=sid, pdfPages=pages,
                             listLabelDe=spec['listLabel'] if sid.endswith('showcards') else None)
                        for sid, pages in spec['pages'].items()],
            contextNotes=([ESS10_PANDEMIC_NOTE] if study == 'ESS10SCe03_2' else []) + spec['notes'],
            boundOriginalForm='PAPI' if study == 'ESS10SCe03_2' else 'CAPI',
        ))
    return dict(
        schemaVersion=1,
        status='DRAFT_PENDING_PLAN_V22_REVIEW',
        plan='docs/analyseplan-v2.2.md',
        scope='18 additional original ESS questions; wording and labels verified automatically '
              'against the cached German PDF text layer; no response data read.',
        sources={sid: dict(path=path, sha256=sha256(path)) for sid, path in PDFS.items()},
        metadata={study: [dict(path=p, sha256=sha256(p)) for p in paths]
                  for study, paths in METADATA.items()},
        attribution='ESS ERIC / Sikt. Documentation CC BY-SA 4.0. Line breaks and line-end '
                    'hyphenation normalised; bullet characters removed.',
        items=items,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    text = json.dumps(build(), ensure_ascii=False, indent=2) + '\n'
    if args.check:
        if OUT.read_text() != text:
            print('catalogue_v22: committed file differs', file=sys.stderr)
            return 1
        print(f'catalogue_v22: verified {OUT.relative_to(ROOT)}')
        return 0
    OUT.write_text(text)
    print(f'catalogue_v22: wrote {OUT.relative_to(ROOT)} sha256={hashlib.sha256(text.encode()).hexdigest()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
