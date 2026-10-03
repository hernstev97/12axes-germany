"""Bind only public instrument content and existing style/font assets for a local draft."""

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

WORKTREE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE = WORKTREE / 'data/politikprofil-v2.fragen.entwurf.json'
catalogue = json.loads(SOURCE.read_text())

item_fields = (
    'id', 'studyId', 'variable', 'primaryTheme', 'originalQuestionId', 'wordingDe',
    'introductionsDe', 'responseStemDe', 'situationDe', 'instructionDe', 'groupId',
    'originalOrderInGroup', 'responseType', 'sourceRefs',
)
items = []
for item in catalogue['items']:
    projected = {key: item.get(key) for key in item_fields}
    # Choices are public, valid original categories. Study missing codes are never UI choices.
    projected['categories'] = [
        {key: category.get(key) for key in ('labelDe', 'printedCodeDe', 'semanticRole')}
        for category in item['categories'] if category.get('isMissingApi') is False
    ]
    projected['boundOriginalForm'] = item['modeBinding']['boundOriginalForm']
    projected['sourceRefs'] = [
        {key: ref.get(key) for key in ('sourceId', 'pdfPages', 'originalForm', 'listLabelDe')}
        for ref in item['sourceRefs'] if ref.get('pdfPages')
    ]
    items.append(projected)

study_fields = (
    'id', 'edition', 'dataDoiUrl', 'documentationDoiUrl', 'citationRequirementDeclaredEn',
    'country', 'populationDeclaredEn', 'populationCoverageLimit', 'fieldwork', 'versionNotes',
    'dataLicenseId', 'documentationLicenseId',
    'samplingProceduresDeclaredEn',
)
public = {
    'catalogueSha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'attribution': {key: catalogue['attribution'][key] for key in ('creator', 'archive', 'licenses')},
    'studies': [{key: study.get(key) for key in study_fields} for study in catalogue['studies']],
    'sources': [
        {key: source.get(key) for key in ('id', 'kind', 'publicUrl', 'licenseId')}
        for source in catalogue['sources']
    ],
    'groups': [
        {key: group.get(key) for key in (
            'id', 'studyId', 'originalQuestionRange', 'introductionDe', 'responseStemDe', 'itemIds'
        )} for group in catalogue['groups']
    ],
    'items': items,
}
(OUT / 'catalogue.js').write_text(
    '// ESS ERIC / Sikt documentation excerpts: CC BY-SA 4.0. Local layout projection.\n'
    + 'export const designCatalogue = ' + json.dumps(public, ensure_ascii=False, indent=2) + ';\n'
)

styles = WORKTREE / 'web/src/styles.scss'
style_text = styles.read_text()
local_css = '\n'.join(line for line in style_text.splitlines() if not line.startswith('@import'))
(OUT / 'foundation.css').write_text(
    '/* Existing web/src/styles.scss; font package imports replaced by a local font face. */\n'
    + local_css + '\n'
)
assets = OUT / 'assets'
assets.mkdir(exist_ok=True)
font = WORKTREE / 'web/node_modules/@fontsource-variable/libre-baskerville/files/libre-baskerville-latin-wght-normal.woff2'
font_license = WORKTREE / 'web/public/fonts/licenses/libre-baskerville.txt'
shutil.copyfile(font, assets / font.name)
shutil.copyfile(font_license, assets / 'libre-baskerville-license.txt')
evidence = {
    'source': 'data/politikprofil-v2.fragen.entwurf.json',
    'sourceSha256': public['catalogueSha256'],
    'scope': 'Public original instrument content only. No answer data, gates or access state copied.',
    'itemCount': len(items),
    'primaryThemes': list(dict.fromkeys(item['primaryTheme'] for item in items)),
    'questionOrderRule': 'Catalogue order, moving B12 keydec directly after B11 within full B1–B12.',
    'originalStylesSha256': hashlib.sha256(styles.read_bytes()).hexdigest(),
    'fontSha256': hashlib.sha256(font.read_bytes()).hexdigest(),
    'fontLicenseSha256': hashlib.sha256(font_license.read_bytes()).hexdigest(),
    'networkRetrievals': False,
    'responseDataRead': False,
}
(OUT / 'source-binding.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
subprocess.run([
    'pnpm', 'exec', 'prettier', '--write',
    str(OUT / 'catalogue.js'), str(OUT / 'foundation.css'),
    str(OUT / 'index.html'), str(OUT / 'prototype.js'),
    str(OUT / 'prototype.css'), str(OUT / 'source-binding.json'),
], cwd=WORKTREE, check=True)
manifest_files = [p for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'manifest.json']
(OUT / 'manifest.json').write_text(json.dumps({
    'scope': 'Unpublished local design draft. Browser, human design approval and comprehension testing pending.',
    'files': [{'path': str(p.relative_to(OUT)), 'bytes': p.stat().st_size,
               'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in manifest_files],
}, ensure_ascii=False, indent=2) + '\n')
print('Prepared public catalogue projection and local style/font assets.')
