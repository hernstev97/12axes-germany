import { createHash } from 'node:crypto';
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import { format } from 'prettier';

const ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
const ROOT_DECISION = 'reports/loop/policy-group-v21-export-decisions.json';
const CATALOGUE = 'data/politikprofil-v2.fragen.entwurf.json';
const SOURCE_MANIFEST = 'reports/loop/packages/GROUP-RESULTS-V21-001/v1/manifest.json';
const METHODS_MANIFEST = 'reports/loop/packages/GROUP-RESULTS-V21-001/v2/manifest.json';
const METHODS_DECISION = 'reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1-decision.json';
const SOURCE_DECISION = 'reports/loop/reviews/GROUP-RESULTS-V21-001-sources-decision.json';
const METHODS_REPORT = 'reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1.md';
const SOURCE_REPORT = 'reports/loop/reviews/GROUP-RESULTS-V21-001-sources-first.md';
const STUDIES = ['ESS5e03_6', 'ESS8e02_3', 'ESS9e03_3'];
// Root supplied this remote-verified public checkpoint; never resolve caller-provided URLs.
const PUBLIC_CHECKPOINT =
  'https://github.com/hernstev97/12axes-germany/blob/d885a54e46aa9c1675f053b81ed503b0d79e3bdd/';

/** Closed public allowlist. Paths in decisions/manifests are compared, never opened. */
export const GROUP_SOURCE_PINS = Object.freeze({
  [CATALOGUE]: '5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4',
  'web/src/app/policy-draft/public-catalogue.ts':
    '7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6',
  'data/reference-groups-v21/README.md':
    '60ba830a02d4371214c29627f255add74d22d70f8f268d83cbeb6c346500342f',
  'data/reference-groups-v21/ESS5e03_6.json':
    '343d06f921f5a943e742f304255726302b71162fb55d8c73b73d11f2f184b19a',
  'data/reference-groups-v21/ESS8e02_3.json':
    'fda4e3dab0546ba25ebb2c265d0d930830615697b023fce2075e41c6a562ff3a',
  'data/reference-groups-v21/ESS9e03_3.json':
    'a1e7f8b116da9d055ffffb2dc5eb2af04e43524962433a9b032f09cbd8b5d093',
  [ROOT_DECISION]: '544f31f83cac1e258ed13559c04373430a5ac0d792c4380421a32bb623ef42bc',
  [METHODS_DECISION]: '3c99d784d23f070a77a843bb0848f26b16e4f795f951ce60d70346edf389e53a',
  [SOURCE_DECISION]: 'b13ae786173c280caf7d1c70f2eccc5015d87b3842fb256575f4f5fb2e95f960',
  [METHODS_REPORT]: '324a7faad5f7c2bb4d8acb2850073a6ac2bcce9607ef3e38c4bd9e668cf3f496',
  [SOURCE_REPORT]: '1d359b82b828ba085705d0fcb6803d5b84a46a15de9ed24e06512cccdcfed058',
  [SOURCE_MANIFEST]: 'dddbcda2fe8a18f46a45ee812100508d9c3ed10c5cca8c8d391be648e474b13a',
  [METHODS_MANIFEST]: '47aa3e3f3cf6043cc81bf25bf6b1228bc007f4a12c3e2866337d91161f114382',
});

function requireBound(condition, message) {
  if (!condition) throw new Error(`group_reference_binding: ${message}`);
}
function equal(a, b) {
  return JSON.stringify(a) === JSON.stringify(b);
}
function pairKeys(pairs) {
  const keys = pairs.map(({ groupId, questionId }) => `${groupId}|${questionId}`).sort();
  requireBound(new Set(keys).size === keys.length, 'duplicate approved pair');
  return keys;
}

export async function loadGroupSources() {
  return new Map(
    await Promise.all(
      Object.keys(GROUP_SOURCE_PINS).map(async (path) => [
        path,
        await readFile(resolve(ROOT, path)),
      ]),
    ),
  );
}

export function authenticateGroupSources(bytes) {
  requireBound(bytes.size === Object.keys(GROUP_SOURCE_PINS).length, 'closed public input set');
  for (const [path, hash] of Object.entries(GROUP_SOURCE_PINS)) {
    requireBound(bytes.has(path), `missing pinned input ${path}`);
    requireBound(
      createHash('sha256').update(bytes.get(path)).digest('hex') === hash,
      `SHA256 ${path}`,
    );
  }
}

export function projectHistoricalGroups(bytes) {
  authenticateGroupSources(bytes);
  const parse = (path) => JSON.parse(bytes.get(path).toString('utf8'));
  const root = parse(ROOT_DECISION);
  const catalogue = parse(CATALOGUE);
  const sourceManifest = parse(SOURCE_MANIFEST);
  const methodsManifest = parse(METHODS_MANIFEST);
  requireBound(root.decision === 'ALLOW_REVIEWED_HISTORICAL_GROUP_REFERENCES_V21', 'root decision');
  requireBound(
    root.rootReadCompleteOriginalSourceFirstAndMethodsFirstAndTargetedRound1 === true &&
      root.actual64Public3PrivateBytesVerified === true,
    'actual root authentication',
  );
  const reuse = root.sourceFirstReuse;
  requireBound(
    reuse.sourceManifestPath === SOURCE_MANIFEST &&
      reuse.sourceManifestSha256 === GROUP_SOURCE_PINS[SOURCE_MANIFEST] &&
      reuse.targetedMethodsManifestPath === METHODS_MANIFEST &&
      reuse.targetedMethodsManifestSha256 === GROUP_SOURCE_PINS[METHODS_MANIFEST],
    'source-first reuse manifests',
  );
  const changed = methodsManifest.publicArtifacts
    .filter((pin) => !sourceManifest.publicArtifacts.some((before) => equal(pin, before)))
    .map((pin) => pin.path);
  requireBound(
    equal([...changed].sort(), [...reuse.changedPaths].sort()),
    'targeted changed paths',
  );
  requireBound(
    changed.length === 2 &&
      sourceManifest.publicArtifacts.length === 64 &&
      methodsManifest.publicArtifacts.length === 64 &&
      reuse.unchangedPublicPins === 62 &&
      reuse.unchangedPrivatePins === 3 &&
      sourceManifest.privateAggregates.length === 3 &&
      equal(sourceManifest.privateAggregates, methodsManifest.privateAggregates),
    'unchanged source and private descriptors (no private reads)',
  );
  for (const manifest of [sourceManifest, methodsManifest]) {
    requireBound(
      manifest.rawAccessAllowed === false && equal(manifest.allowedStudyIds, STUDIES),
      'manifest study boundary',
    );
    requireBound(
      manifest.publicArtifacts.some(
        (pin) => pin.path === CATALOGUE && pin.sha256 === GROUP_SOURCE_PINS[CATALOGUE],
      ),
      'manifest catalogue pin',
    );
  }
  const reviewers = [
    ['methods_reproducibility', METHODS_DECISION, METHODS_REPORT, METHODS_MANIFEST],
    ['sources_constructs_fairness', SOURCE_DECISION, SOURCE_REPORT, SOURCE_MANIFEST],
  ].map(([role, decisionPath, reportPath, manifestPath]) => {
    const decision = parse(decisionPath);
    requireBound(
      decision.role === role &&
        decision.decision === 'ACCEPTED_BOUNDED' &&
        decision.reviewManifestSha256 === GROUP_SOURCE_PINS[manifestPath],
      'role and original review version',
    );
    requireBound(
      root.reviewDecisionFiles.some(
        (pin) => pin.path === decisionPath && pin.sha256 === GROUP_SOURCE_PINS[decisionPath],
      ),
      'actual role decision pin',
    );
    return { role, reportPath, decision };
  });
  requireBound(
    equal(
      root.studyDecisions.map((d) => d.studyId),
      STUDIES,
    ),
    'root study inventory',
  );
  const studies = STUDIES.map((studyId, index) => {
    const path = `data/reference-groups-v21/${studyId}.json`;
    const data = parse(path);
    const decision = root.studyDecisions[index];
    const original = catalogue.studies.find((s) => s.id === studyId);
    const source = data.source;
    requireBound(
      data.schemaVersion === 1 &&
        data.status === 'reviewed_historical_descriptive_group_reference' &&
        data.studyId === studyId &&
        data.edition === original.edition &&
        decision.edition === data.edition &&
        decision.decision === root.decision &&
        data.reviewManifestSha256 === GROUP_SOURCE_PINS[METHODS_MANIFEST],
      'study, edition and public status',
    );
    for (const key of [
      'candidateSha256',
      'groupContractSha256',
      'studyContractSha256',
      'reviewManifestSha256',
    ]) {
      requireBound(data[key] === decision[key], `study ${key}`);
    }
    for (const reviewer of reviewers) {
      requireBound(
        decision.reviewers.some(
          (r) =>
            r.role === reviewer.role &&
            r.reportPath === reviewer.reportPath &&
            r.sha256 === GROUP_SOURCE_PINS[reviewer.reportPath] &&
            r.decision === 'ACCEPTED_BOUNDED',
        ),
        'actual fixed reviewer report',
      );
      requireBound(
        equal(
          pairKeys(decision.approvedGroupQuestionIds),
          pairKeys(reviewer.decision.approvedGroupQuestionIdsByStudy[studyId]),
        ),
        'independent explicit pair intersection',
      );
    }
    const publicPin = root.publicFiles.find((pin) => pin.studyId === studyId);
    requireBound(
      publicPin.path === path && publicPin.sha256 === GROUP_SOURCE_PINS[path],
      'public export pin',
    );
    requireBound(
      source.catalogue.path === CATALOGUE &&
        source.catalogue.sha256 === GROUP_SOURCE_PINS[CATALOGUE],
      'public source catalogue',
    );
    for (const key of [
      'fieldwork',
      'dataDoiUrl',
      'documentationDoiUrl',
      'populationDeclaredEn',
      'dataLicenseId',
      'documentationLicenseId',
    ]) {
      requireBound(equal(source[key], original[key]), `original source ${key}`);
    }
    requireBound(
      source.country === 'DE' &&
        source.automaticPrintedCodeToFileCodeMappingAllowed === false &&
        source.recodeBoundary === null &&
        data.scope.independentNorm === false &&
        data.scope.currentPartyPositions === false &&
        data.scope.partyScores === false &&
        data.scope.personsOrStudiesPooled === false &&
        data.scope.precisionOrAnonymityValidated === false,
      'historical descriptive boundary',
    );
    const questionIds = catalogue.items
      .filter((q) => q.studyId === studyId)
      .map((q) => q.id)
      .sort();
    const approved = pairKeys(decision.approvedGroupQuestionIds);
    let approvedCount = 0;
    const printed = source.nationalParty2Field.originalQuestion;
    requireBound(data.groups.length === publicPin.declaredGroupCount, 'complete group inventory');
    requireBound(
      new Set(data.groups.map((g) => g.id)).size === data.groups.length,
      'unique groups',
    );
    const groups = data.groups.map((group) => {
      requireBound(
        group.id === `${studyId}:second_vote:${group.party2Code}`,
        'explicit group code',
      );
      const other = group.kind === 'other_unlabelled';
      requireBound(
        other === group.heterogeneousUnlabelledOther &&
          (other
            ? group.labelDeOriginalForm === null && group.labelEnExactApi === 'Other'
            : typeof group.labelDeOriginalForm === 'string'),
        'original group label and Other',
      );
      const boundOptions = other
        ? [printed.printedOther]
        : printed.printedValidCategories.filter(
            (option) => option.labelDe === group.labelDeOriginalForm,
          );
      requireBound(boundOptions.length === 1 && boundOptions[0], 'unique original label binding');
      requireBound(
        equal(group.questions.map((q) => q.id).sort(), questionIds),
        'full same-study questions',
      );
      const questions = group.questions.map((question) => {
        const isApproved = approved.includes(`${group.id}|${question.id}`);
        if (!isApproved) {
          requireBound(
            question.status === 'withheld_base_or_cell_count' &&
              question.reference === null &&
              equal(Object.keys(question).sort(), ['id', 'reference', 'status']),
            'withheld pair has no counts or proportions',
          );
          return { id: question.id, status: question.status, reference: null };
        }
        approvedCount++;
        const reference = question.reference;
        const item = catalogue.items.find((q) => q.id === question.id);
        requireBound(
          question.status === 'reviewed_historical_reference' && reference,
          'approved pair',
        );
        requireBound(
          reference.weight === 'pspwght' && reference.uncertainty === null,
          'weight and no precision',
        );
        const counts = ['validCount', 'totalCount', 'missingCount', 'notAskedCount'].map(
          (k) => reference[k],
        );
        requireBound(
          counts.every((n) => Number.isSafeInteger(n) && n >= 0) &&
            reference.validCount >= 100 &&
            reference.totalCount ===
              reference.validCount + reference.missingCount + reference.notAskedCount,
          'published question denominator',
        );
        requireBound(
          equal(
            reference.categories.map((c) => c.code),
            item.apiValidCodeOrder,
          ),
          'original category code order',
        );
        requireBound(
          reference.categories.every(
            (c) => Number.isFinite(c.proportion) && c.proportion >= 0 && c.proportion <= 1,
          ) && Math.abs(reference.categories.reduce((sum, c) => sum + c.proportion, 0) - 1) < 1e-12,
          'published proportions (never renormalized)',
        );
        return { id: question.id, status: question.status, reference };
      });
      return {
        id: group.id,
        party2Code: group.party2Code,
        printedCodeDe: boundOptions[0].code,
        label: group.labelDeOriginalForm ?? group.labelEnExactApi,
        labelEnExactApi: group.labelEnExactApi,
        heterogeneousUnlabelledOther: other,
        questions,
      };
    });
    requireBound(
      approvedCount === publicPin.approvedPairCount && approvedCount === approved.length,
      'all approved pairs present',
    );
    return {
      id: studyId,
      edition: data.edition,
      election: { monthDe: source.election.monthDe, year: source.election.year },
      fieldwork: source.fieldwork,
      dataDoiUrl: source.dataDoiUrl,
      documentationDoiUrl: source.documentationDoiUrl,
      voteVariable: source.voteField.variable,
      party2Variable: source.nationalParty2Field.variable,
      originalQuestionId: printed.questionId,
      originalQuestionPages: printed.pdfPages1Based,
      aliasBinding: source.aliasToVoteTypeBinding.status,
      aliasSourcePage: source.aliasToVoteTypeBinding.officialConcordancePdfPage1Based,
      dataLicenseId: source.dataLicenseId,
      documentationLicenseId: source.documentationLicenseId,
      attribution: source.attribution,
      documents: source.documents.map(({ id, publicUrl, originalBytesSha256 }) => ({
        id,
        publicUrl,
        originalBytesSha256,
      })),
      publicReferencePath: path,
      publicReferenceUrl: `${PUBLIC_CHECKPOINT}${path}`,
      publicReadmeUrl: `${PUBLIC_CHECKPOINT}data/reference-groups-v21/README.md`,
      publicReferenceSha256: GROUP_SOURCE_PINS[path],
      groups,
    };
  });
  return {
    schemaVersion: 1,
    status: 'reviewed_historical_descriptive_group_reference',
    catalogueSha256: GROUP_SOURCE_PINS[CATALOGUE],
    rootDecisionSha256: GROUP_SOURCE_PINS[ROOT_DECISION],
    sourceManifestSha256: GROUP_SOURCE_PINS[SOURCE_MANIFEST],
    methodsManifestSha256: GROUP_SOURCE_PINS[METHODS_MANIFEST],
    sourceOpinionReusedUnchanged: true,
    studies,
  };
}

export async function renderHistoricalGroups(bytes) {
  const data = projectHistoricalGroups(bytes);
  return format(
    `// Generated by group-reference-generator.mjs from fixed authenticated public bytes.\n// Source-first v1 is reused unchanged; methods round1 binds v2. No private inputs.\nimport { freezeHistoricalGroups, type HistoricalGroupInput } from './group-reference-types';\n\nconst payload = ${JSON.stringify(data, null, 2)} satisfies HistoricalGroupInput;\n\nexport const REVIEWED_HISTORICAL_GROUPS: HistoricalGroupInput = freezeHistoricalGroups(payload);\n`,
    { parser: 'typescript', singleQuote: true, printWidth: 100, trailingComma: 'all' },
  );
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const mode = process.argv[2];
  requireBound(mode === '--write' || mode === '--check', 'use --write or --check');
  const expected = await renderHistoricalGroups(await loadGroupSources());
  const output = new URL('./reviewed-historical-groups.ts', import.meta.url);
  if (mode === '--write') await writeFile(output, expected);
  else requireBound((await readFile(output, 'utf8')) === expected, 'generated adapter byte parity');
  console.log(
    'Authenticated public groups: 3 studies, 26 groups, 63 references; generated byte parity OK.',
  );
}
