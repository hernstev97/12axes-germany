/**
 * Build-only projection of data/politikprofil-v2.2.ergaenzung.json (Analyseplan v2.2).
 * Reads public instrument metadata only, never response data.
 *   node web/src/app/policy-draft/generate-public-catalogue-v22.mjs          # write
 *   node web/src/app/policy-draft/generate-public-catalogue-v22.mjs --check  # verify
 */
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';
import { format } from 'prettier';

const repository = new URL('../../../../', import.meta.url);
const sourcePath = 'data/politikprofil-v2.2.ergaenzung.json';
const output = new URL('./public-catalogue-v22.ts', import.meta.url);
const codeSources = {
  ESS5e03_6: 'ess5-original-codelists-direct',
  ESS8e02_3: 'ess8-original-codelists-direct',
  ESS10SCe03_2: 'ess10sc-original-codelists-direct',
};

const bytes = readFileSync(new URL(sourcePath, repository));
const sha256 = createHash('sha256').update(bytes).digest('hex');
const source = JSON.parse(bytes.toString('utf8'));
assert.equal(source.items.length, 19);

const items = source.items.map((item) => ({
  id: item.id,
  studyId: item.studyId,
  variable: item.variable,
  primaryTheme: item.primaryTheme,
  originalQuestionId: item.originalQuestionId,
  wordingDe: item.wordingDe,
  introductionsDe: item.introductionsDe,
  definitionDe: item.definitionDe,
  contextNotes: item.contextNotes,
  responseStemDe: item.responseStemDe,
  situationDe: item.situationDe,
  instructionDe: item.instructionDe,
  groupId: item.groupId,
  originalOrderInGroup: item.originalOrderInGroup,
  responseType: item.responseType,
  sourceRefs: item.sourceRefs.map((ref) => ({
    sourceId: ref.sourceId,
    pdfPages: ref.pdfPages,
    originalForm: null,
    listLabelDe: ref.listLabelDe,
  })),
  categories: item.categories.map((category) => ({
    code: category.code,
    printedCodeDe: category.printedCodeDe,
    labelDe: category.labelDe,
    labelEn: category.labelEn,
    isMissingApi: false,
    semanticRole: category.semanticRole,
    labelSourceRef: item.sourceRefs.at(-1).sourceId,
    offeredOnWebsite: category.offeredOnWebsite,
  })),
  boundOriginalForm:
    item.boundOriginalForm === 'PAPI'
      ? 'Gedruckter Papierfragebogen (Selbstausfüllung)'
      : 'Nationales Interviewskript (CAPI)',
  codeBinding: {
    sourceId: codeSources[item.studyId],
    sourceFieldId: item.sourceFieldId,
    sourceFieldMetadataVersion: item.sourceFieldMetadataVersion,
    dataFileMetadataId: item.dataFileMetadataId,
    dataFileMetadataVersion: item.dataFileMetadataVersion,
  },
  apiValidCodeOrder: item.apiValidCodeOrder,
  missingCodes: item.missingCodes,
  notAskedCodes: item.notAskedCodes,
}));

const text = await format(
  `// ESS ERIC / Sikt documentation excerpts: CC BY-SA 4.0.
// Generated from ${sourcePath} by generate-public-catalogue-v22.mjs. Do not edit by hand.
import type { PublicItem } from './catalogue-types';
import { freezePublicMetadata } from './catalogue-types';

export const PUBLIC_CATALOGUE_V22: { readonly sourceSha256: string; readonly items: readonly PublicItem[] } =
  freezePublicMetadata(${JSON.stringify({ sourceSha256: sha256, items })});
`,
  { parser: 'typescript', singleQuote: true, printWidth: 100 },
);

if (process.argv.includes('--check')) {
  assert.equal(readFileSync(output, 'utf8'), text, 'public-catalogue-v22.ts is not current');
  console.log(`PASS: public-catalogue-v22.ts matches ${sourcePath} (${sha256}).`);
} else {
  writeFileSync(output, text);
  console.log(`Wrote public-catalogue-v22.ts from ${sourcePath} (${sha256}).`);
}
