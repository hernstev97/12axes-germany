import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import {
  checkReviewedReferenceModule,
  generateReviewedReferenceModule,
  PUBLIC_SOURCE_PINS,
  readAuthenticatedSnapshot,
} from './generate-reviewed-references.mjs';

const repository = new URL('../../../../', import.meta.url);
const readPublicBytes = (path) => readFileSync(new URL(path, repository));

test('build adapter reads the exact public allowlist and reproduces the checked-in module byte for byte', async () => {
  const seen = [];
  const snapshot = await checkReviewedReferenceModule((path) => {
    seen.push(path);
    return readPublicBytes(path);
  });
  assert.deepEqual(seen, Object.keys(PUBLIC_SOURCE_PINS));
  assert.ok(
    seen.every(
      (path) =>
        !path.startsWith('data/raw/') && !path.startsWith('data/local/') && !path.endsWith('.csv'),
    ),
  );
  const output = await generateReviewedReferenceModule(snapshot);
  assert.equal(output, await generateReviewedReferenceModule(snapshot));
});

for (const path of [
  'data/reference-v2/ESS10SCe03_2.json',
  'reports/loop/policy-v2-export-decisions.json',
  'reports/loop/reviews/RESULTS-V2-001-methods-decision.json',
  'reports/loop/reviews/RESULTS-V2-001-sources-first.md',
]) {
  test(`authentication rejects changed real bytes: ${path}`, async () => {
    await assert.rejects(
      readAuthenticatedSnapshot((candidate) =>
        candidate === path
          ? Buffer.concat([readPublicBytes(candidate), Buffer.from('\n')])
          : readPublicBytes(candidate),
      ),
      /Public input bytes changed/,
    );
  });
}

test('projection rejects disagreement between the two accepted question inventories', async () => {
  const snapshot = structuredClone(await readAuthenticatedSnapshot());
  snapshot.receipts[1].studies[0].approvedQuestionIds.pop();
  await assert.rejects(
    generateReviewedReferenceModule(snapshot),
    /Independent receipts do not accept identical items/,
  );
});

test('projection rejects another edition, candidate, or original category code', async () => {
  const authentic = await readAuthenticatedSnapshot();
  for (const mutate of [
    (snapshot) => {
      snapshot.publicFiles[0].edition = 'unaccepted-edition';
    },
    (snapshot) => {
      snapshot.publicFiles[0].candidateSha256 = 'unaccepted-candidate';
    },
    (snapshot) => {
      snapshot.publicFiles[0].questions[0].reference.categories[0].code = 'unbound-code';
    },
  ]) {
    const snapshot = structuredClone(authentic);
    mutate(snapshot);
    await assert.rejects(generateReviewedReferenceModule(snapshot));
  }
});

test('projection preserves explicit cttresa null and rejects any supplied numbers for the withheld question', async () => {
  const snapshot = structuredClone(await readAuthenticatedSnapshot());
  const study = snapshot.publicFiles.find((file) => file.studyId === 'ESS10SCe03_2');
  const withheld = study.questions.find((question) => question.id === 'ESS10SCe03_2:cttresa');
  assert.equal(withheld.reference, null);
  // Deliberately invalid in-memory negative fixture. No artifact is written.
  withheld.reference = structuredClone(study.questions[0].reference);
  await assert.rejects(
    generateReviewedReferenceModule(snapshot),
    /Unaccepted question contains reference numbers/,
  );
});

test('projection rejects a collapsed count breakdown and a new uncertainty value', async () => {
  const authentic = await readAuthenticatedSnapshot();
  for (const mutate of [
    (reference) => {
      reference.missingCount += 1;
    },
    (reference) => {
      reference.uncertainty = 0;
    },
  ]) {
    const snapshot = structuredClone(authentic);
    mutate(snapshot.publicFiles[0].questions[0].reference);
    await assert.rejects(generateReviewedReferenceModule(snapshot));
  }
});

test('projection matches categories by code even if a source list is reordered', async () => {
  const authentic = await readAuthenticatedSnapshot();
  const reordered = structuredClone(authentic);
  reordered.publicFiles[0].questions[0].reference.categories.reverse();
  assert.equal(
    await generateReviewedReferenceModule(reordered),
    await generateReviewedReferenceModule(authentic),
  );
});
