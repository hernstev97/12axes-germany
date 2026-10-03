/** Build-only adapter. Reads an exact public allowlist; never response/private files. */
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';
import { stripTypeScriptTypes } from 'node:module';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { format } from 'prettier';

const repository = new URL('../../../../', import.meta.url);
const exportPath = 'reports/loop/policy-v2-export-decisions.json';
const methodsReceipt = 'reports/loop/reviews/RESULTS-V2-001-methods-decision.json';
const sourcesReceipt = 'reports/loop/reviews/RESULTS-V2-001-sources-decision.json';
const methodsReport = 'reports/loop/reviews/RESULTS-V2-001-methods-first.md';
const sourcesReport = 'reports/loop/reviews/RESULTS-V2-001-sources-first.md';
const cataloguePath = 'web/src/app/policy-draft/public-catalogue.ts';
const output = new URL('./reviewed-historical-references.ts', import.meta.url);

export const PUBLIC_SOURCE_PINS = Object.freeze({
  'data/reference-v2/ESS5e03_6.json':
    'e489fe013d1cbd3d72b9ae816e422757ce8d34ae575d09f64df13a1750dc4bc6',
  'data/reference-v2/ESS8e02_3.json':
    'fb720cc18049f037ed86670bd76a51c3c1770342a61f5627b7afbfb127898ad7',
  'data/reference-v2/ESS9e03_3.json':
    '34e71b448c0c315cf9f19bda30628874c95464faf661813a65f25a3f9ad82be2',
  'data/reference-v2/ESS10SCe03_2.json':
    'e75dfbadcf68c14dce9d13c8a8a2dd1abc6e8a6e96618f960c8cd61c54bc3184',
  'data/reference-v2/ESS11e04_2.json':
    '453d8ce3273c9e29bb08a49be6e69da46591e3d1ed89f306051b085c511ec721',
  'data/reference-v2/README.md': 'a2917e6b57c59e96298345e526e9311de82b1422cfbb9a8bb1cfabc0684ba57c',
  [exportPath]: 'a87f780a7219253f7f3773d051b7001f438b19b2fb2d0ee820fc22c1157a16df',
  [methodsReceipt]: '765db3005c736174a3d1f9819ab212917ce50d6143059b8cfce2dac3f6f67806',
  [sourcesReceipt]: 'e5c3a730dc6cf71e5b788d4251c109b86a7d510684bf945b17ceaa6e48306065',
  [methodsReport]: '1bb14ba2dba3d57612d66c5a50c29ce049606e8fddb062ff6b616f56b60462ee',
  [sourcesReport]: '7a2814359b94ab3a73dd22a090b2a10c6b51db6cc243d8586e8ae15bfdc580e8',
  [cataloguePath]: '7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6',
});

const studyPaths = Object.keys(PUBLIC_SOURCE_PINS).filter((path) =>
  /^data\/reference-v2\/.+\.json$/.test(path),
);
const reportByRole = Object.freeze({
  methods_reproducibility: methodsReport,
  sources_constructs_fairness: sourcesReport,
});

function sha256(bytes) {
  return createHash('sha256').update(bytes).digest('hex');
}

async function importLocalTypescript(code) {
  const javascript = stripTypeScriptTypes(code);
  return import(`data:text/javascript;base64,${Buffer.from(javascript).toString('base64')}`);
}

export async function readAuthenticatedSnapshot(
  readBytes = (path) => readFileSync(new URL(path, repository)),
) {
  const bytes = new Map();
  for (const [path, pin] of Object.entries(PUBLIC_SOURCE_PINS)) {
    // Exact allowlist is fixed above. No path supplied by a decision file is opened.
    const value = readBytes(path);
    assert.equal(sha256(value), pin, `Public input bytes changed: ${path}`);
    bytes.set(path, value);
  }
  const exportDecision = JSON.parse(bytes.get(exportPath).toString('utf8'));
  const receipts = [methodsReceipt, sourcesReceipt].map((path) =>
    JSON.parse(bytes.get(path).toString('utf8')),
  );
  const publicFiles = studyPaths.map((path) => JSON.parse(bytes.get(path).toString('utf8')));
  assert.equal(
    exportDecision.publicFiles.length,
    studyPaths.length,
    'Export decision public inventory changed',
  );
  for (const publicDecision of exportDecision.publicFiles) {
    assert.ok(studyPaths.includes(publicDecision.path), 'Unallowed public reference path');
    assert.equal(
      publicDecision.sha256,
      PUBLIC_SOURCE_PINS[publicDecision.path],
      'Public file decision hash differs',
    );
    assert.equal(
      JSON.parse(bytes.get(publicDecision.path).toString('utf8')).studyId,
      publicDecision.studyId,
      'Public study file identity differs',
    );
  }
  for (const decision of exportDecision.studyDecisions) {
    for (const reviewer of decision.reviewers) {
      const expectedPath = reportByRole[reviewer.role];
      assert.ok(expectedPath, 'Unexpected reviewer role');
      assert.equal(reviewer.reportPath, expectedPath, 'Unallowed report path');
      assert.equal(
        reviewer.sha256,
        PUBLIC_SOURCE_PINS[expectedPath],
        'Original report hash differs from decision',
      );
    }
  }
  // The generated catalogue is the unchanged, independently source-matched public
  // adapter. Its import is replaced only for the read-only build-time projection.
  const catalogueCode = bytes
    .get(cataloguePath)
    .toString('utf8')
    .replace(/^import .*?;\n/m, 'const freezePublicMetadata = value => value;\n');
  const { PUBLIC_CATALOGUE: catalogue } = await importLocalTypescript(catalogueCode);
  return { catalogue, exportDecision, receipts, publicFiles };
}

export async function generateReviewedReferenceModule(snapshot) {
  const { projectReviewedReferences } = await importLocalTypescript(
    readFileSync(new URL('./reference-binding.ts', import.meta.url), 'utf8'),
  );
  const input = projectReviewedReferences(snapshot);
  const provenance = {
    catalogueSha256: input.catalogueSha256,
    exportScope: snapshot.exportDecision.scope,
    inputSha256: PUBLIC_SOURCE_PINS,
    excludedQuestionIds: snapshot.exportDecision.withheldIds,
    reviewedReferenceCount: input.references.length,
  };
  const source =
    `// Generated by generate-reviewed-references.mjs. Do not edit by hand.\n` +
    `// ESS ERIC / Sikt historical aggregate derivatives: CC BY-NC-SA 4.0.\n` +
    `// Public research-branch references only; no instrument/design/human/release approval.\n` +
    `import { freezePublicMetadata } from './catalogue-types';\n` +
    `import type { HistoricalReferenceInput } from './historical-reference';\n\n` +
    `export const REVIEWED_HISTORICAL_REFERENCES: HistoricalReferenceInput = freezePublicMetadata(${JSON.stringify(input, null, 2)});\n\n` +
    `export const REVIEWED_REFERENCE_PROVENANCE = freezePublicMetadata(${JSON.stringify(provenance, null, 2)} as const);\n`;
  return format(source, {
    parser: 'typescript',
    singleQuote: true,
    printWidth: 100,
    trailingComma: 'all',
  });
}

export async function checkReviewedReferenceModule(readBytes) {
  const snapshot = await readAuthenticatedSnapshot(readBytes);
  const expected = await generateReviewedReferenceModule(snapshot);
  assert.equal(
    readFileSync(output, 'utf8'),
    expected,
    'Generated reference module differs; regenerate with --write',
  );
  return snapshot;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const mode = process.argv[2] ?? '--check';
  assert.ok(
    process.argv.length <= 3 && ['--check', '--write'].includes(mode),
    'Use --check or --write',
  );
  if (mode === '--write') {
    const snapshot = await readAuthenticatedSnapshot();
    writeFileSync(output, await generateReviewedReferenceModule(snapshot));
  } else {
    await checkReviewedReferenceModule();
  }
  console.log(
    `PASS ${mode}: authenticated public hashes and matching review decisions; 42 references copied by original code, cttresa remains null.`,
  );
}
