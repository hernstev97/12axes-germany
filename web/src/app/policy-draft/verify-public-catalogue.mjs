/** Read-only parity check. Opens public metadata and this folder, never response data. */
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { stripTypeScriptTypes } from 'node:module';

const repository = new URL('../../../../', import.meta.url);
const originalBytes = readFileSync(
  new URL('data/politikprofil-v2.fragen.entwurf.json', repository),
);
const expectedHash = '5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4';
assert.equal(createHash('sha256').update(originalBytes).digest('hex'), expectedHash);
const original = JSON.parse(originalBytes.toString('utf8'));
const projectedCode = stripTypeScriptTypes(
  readFileSync(new URL('./public-catalogue.ts', import.meta.url), 'utf8'),
).replace(/^import .*?;\n/m, 'const freezePublicMetadata = value => value;\n');
const { PUBLIC_CATALOGUE: projected } = await import(
  `data:text/javascript;base64,${Buffer.from(projectedCode).toString('base64')}`
);
assert.equal(projected.catalogueSha256, expectedHash);
assert.equal(projected.items.length, 43);
assert.equal(
  projected.items.reduce((count, item) => count + item.categories.length, 0),
  315,
);
const keys = [
  'studyId',
  'variable',
  'primaryTheme',
  'originalQuestionId',
  'wordingDe',
  'introductionsDe',
  'responseStemDe',
  'situationDe',
  'instructionDe',
  'groupId',
  'originalOrderInGroup',
  'responseType',
  'categories',
  'apiValidCodeOrder',
  'missingCodes',
  'notAskedCodes',
];
for (const source of original.items) {
  const item = projected.items.find((candidate) => candidate.id === source.id);
  assert.ok(item, 'Public source item missing from projection');
  for (const key of keys) assert.deepEqual(item[key], source[key], `${item.id}.${key}`);
  const binding = source.sourceRefs.find((ref) => ref.sourceFieldId === source.sourceFieldId);
  for (const key of [
    'sourceFieldId',
    'sourceFieldMetadataVersion',
    'dataFileMetadataId',
    'dataFileMetadataVersion',
  ]) {
    assert.equal(item.codeBinding[key], binding[key], `${item.id}.codeBinding.${key}`);
  }
  assert.equal(item.codeBinding.sourceId, binding.sourceId);
}
console.log(
  'PASS: pinned public source; 43 original questions and 315 explicit printed/API bindings match. No response data opened.',
);
