import assert from 'node:assert/strict';
import test from 'node:test';
import {
  GROUP_SOURCE_PINS,
  authenticateGroupSources,
  loadGroupSources,
  projectHistoricalGroups,
  renderHistoricalGroups,
} from './group-reference-generator.mjs';
import { readFile } from 'node:fs/promises';

const bytes = await loadGroupSources();
const projection = projectHistoricalGroups(bytes);

test('closed loader authenticates only the 13 fixed public sources, never descriptor paths', () => {
  assert.equal(bytes.size, 13);
  assert.ok(
    [...bytes.keys()].every(
      (path) => !path.startsWith('data/local/') && !path.startsWith('data/raw/'),
    ),
  );
  assert.deepEqual([...bytes.keys()], Object.keys(GROUP_SOURCE_PINS));
  authenticateGroupSources(bytes);
  const extra = new Map(bytes);
  extra.set('reports/arbitrary-review.md', Buffer.from('ACCEPTED_BOUNDED'));
  assert.throws(() => authenticateGroupSources(extra), /closed public input set/);
});

test('changed public proportions, invented role decisions or changed original report bytes fail authentication', () => {
  const publicPath = 'data/reference-groups-v21/ESS9e03_3.json';
  const publicData = JSON.parse(bytes.get(publicPath).toString('utf8'));
  publicData.groups[0].questions[0].reference.categories[0].proportion = 1;
  const decisionPath = 'reports/loop/reviews/GROUP-RESULTS-V21-001-sources-decision.json';
  const decision = JSON.parse(bytes.get(decisionPath).toString('utf8'));
  decision.role = 'invented_reviewer';
  const rootPath = 'reports/loop/policy-group-v21-export-decisions.json';
  const root = JSON.parse(bytes.get(rootPath).toString('utf8'));
  root.studyDecisions[0].reviewers[0].reportPath = 'reports/arbitrary-review.md';
  const reportPath = 'reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1.md';
  for (const [path, value] of [
    [publicPath, JSON.stringify(publicData)],
    [decisionPath, JSON.stringify(decision)],
    [rootPath, JSON.stringify(root)],
    [reportPath, bytes.get(reportPath).toString('utf8') + '\nInvented new acceptance'],
  ]) {
    const changed = new Map(bytes);
    changed.set(path, Buffer.from(value));
    assert.throws(() => projectHistoricalGroups(changed), /SHA256/);
  }
});

test('projection preserves every public category/code/proportion and null without publishing hidden bases', () => {
  let references = 0;
  let unavailable = 0;
  for (const study of projection.studies) {
    const source = JSON.parse(bytes.get(study.publicReferencePath).toString('utf8'));
    assert.deepEqual(
      study.groups.map((group) => group.id),
      source.groups.map((group) => group.id),
    );
    assert.deepEqual(study.fieldwork, source.source.fieldwork);
    for (const [groupIndex, group] of study.groups.entries()) {
      const original = source.groups[groupIndex];
      assert.equal(group.label, original.labelDeOriginalForm ?? original.labelEnExactApi);
      assert.equal(group.party2Code, original.party2Code);
      assert.deepEqual(group.questions, original.questions);
      for (const question of group.questions) {
        if (question.reference) references++;
        else {
          unavailable++;
          assert.deepEqual(Object.keys(question).sort(), ['id', 'reference', 'status']);
        }
      }
    }
  }
  assert.equal(references, 63);
  assert.equal(unavailable, 111);
  assert.deepEqual(
    projection.studies.map((study) => study.groups.length),
    [8, 9, 9],
  );
  const ess9 = projection.studies.find((study) => study.id === 'ESS9e03_3');
  assert.equal(ess9.groups[0].printedCodeDe, '01');
  assert.equal(ess9.groups[0].party2Code, '1');
  assert.equal(ess9.groups.at(-1).printedCodeDe, '09');
  assert.equal(ess9.groups.at(-1).label, 'Other');
  assert.equal(projection.sourceOpinionReusedUnchanged, true);
  assert.notEqual(projection.sourceManifestSha256, projection.methodsManifestSha256);
});

test('checked-in adapter is byte-identical to fresh authenticated build-time projection', async () => {
  assert.equal(
    await readFile(new URL('./reviewed-historical-groups.ts', import.meta.url), 'utf8'),
    await renderHistoricalGroups(bytes),
  );
});
