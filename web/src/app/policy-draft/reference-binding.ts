import type { PublicCatalogue } from './catalogue-types';
import type {
  HistoricalCategoryReference,
  HistoricalReferenceInput,
  HistoricalUnavailableReference,
} from './historical-reference';

export interface ReviewedStudyDecision {
  readonly studyId: string;
  readonly candidateSha256: string;
  readonly approvedQuestionIds: readonly string[];
}

export interface ReviewedDecisionReceipt {
  readonly schemaVersion: number;
  readonly role: string;
  readonly reviewManifestSha256: string;
  readonly decision: string;
  readonly studies: readonly ReviewedStudyDecision[];
}

export interface PublicExportDecision {
  readonly schemaVersion: number;
  readonly decision: string;
  readonly scope: string;
  readonly studyDecisions: readonly (ReviewedStudyDecision & {
    readonly schemaVersion: number;
    readonly decision: string;
    readonly edition: string;
    readonly sourceContractSha256: string;
    readonly reviewManifestSha256: string;
    readonly reviewers: readonly {
      readonly role: string;
      readonly reportPath: string;
      readonly sha256: string;
      readonly decision: string;
    }[];
  })[];
  readonly publicFiles: readonly {
    readonly path: string;
    readonly sha256: string;
    readonly studyId: string;
    readonly reviewedReferenceCount: number;
    readonly questionInventoryCount: number;
  }[];
  readonly withheldIds: readonly string[];
}

export interface PublicReferenceFile {
  readonly schemaVersion: number;
  readonly status: string;
  readonly studyId: string;
  readonly edition: string;
  readonly sourceContractSha256: string;
  readonly candidateSha256: string;
  readonly reviewManifestSha256: string;
  readonly questions: readonly {
    readonly id: string;
    readonly status: string;
    readonly reference: null | {
      readonly weight: string;
      readonly validCount: number;
      readonly totalCount: number;
      readonly missingCount: number;
      readonly notAskedCount: number;
      readonly categories: readonly { readonly code: string; readonly proportion: number }[];
      readonly uncertainty: null;
    };
  }[];
}

export interface ReviewedProjectionSnapshot {
  readonly catalogue: PublicCatalogue;
  readonly exportDecision: PublicExportDecision;
  readonly receipts: readonly ReviewedDecisionReceipt[];
  readonly publicFiles: readonly PublicReferenceFile[];
}

export class ReviewedProjectionError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ReviewedProjectionError';
  }
}

function requireBinding(condition: boolean, message: string): asserts condition {
  if (!condition) throw new ReviewedProjectionError(message);
}

function sameIds(actual: readonly string[], expected: readonly string[]): boolean {
  return (
    actual.length === expected.length &&
    new Set(actual).size === actual.length &&
    actual.every((id) => expected.includes(id))
  );
}

/**
 * Pure, deterministic projection of already authenticated public exports.
 * The build script verifies actual file/report bytes before calling this function.
 * Counts and proportions are copied by original item/code; nothing is estimated.
 */
export function projectReviewedReferences(
  snapshot: ReviewedProjectionSnapshot,
): HistoricalReferenceInput {
  const { catalogue, exportDecision, receipts, publicFiles } = snapshot;
  requireBinding(
    catalogue.catalogueSha256 ===
      '5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4',
    'Unbound semantic catalogue',
  );
  requireBinding(
    exportDecision.schemaVersion === 1 &&
      exportDecision.decision === 'ALLOW_REVIEWED_HISTORICAL_REFERENCE_V2',
    'No bounded public export decision',
  );
  requireBinding(
    exportDecision.scope ===
      'public research-branch aggregate export only; no current norm/instrument/design/human/legal/release acceptance',
    'Export scope changed',
  );
  const studyIds = catalogue.studies.map((study) => study.id);
  requireBinding(
    sameIds(
      exportDecision.studyDecisions.map((study) => study.studyId),
      studyIds,
    ),
    'Study decision inventory differs',
  );
  requireBinding(
    sameIds(
      exportDecision.publicFiles.map((file) => file.studyId),
      studyIds,
    ),
    'Public file decision inventory differs',
  );
  requireBinding(
    sameIds(
      publicFiles.map((file) => file.studyId),
      studyIds,
    ),
    'Public reference file inventory differs',
  );
  requireBinding(
    receipts.length === 2 &&
      sameIds(
        receipts.map((receipt) => receipt.role),
        ['methods_reproducibility', 'sources_constructs_fairness'],
      ),
    'Two prescribed receipts required',
  );
  const manifest = exportDecision.studyDecisions[0]!.reviewManifestSha256;
  for (const receipt of receipts) {
    requireBinding(
      receipt.schemaVersion === 1 &&
        receipt.decision === 'ACCEPTED_BOUNDED' &&
        receipt.reviewManifestSha256 === manifest,
      'Receipt or manifest changed',
    );
    requireBinding(
      sameIds(
        receipt.studies.map((study) => study.studyId),
        studyIds,
      ),
      'Receipt study inventory differs',
    );
  }
  requireBinding(
    sameIds(exportDecision.withheldIds, ['ESS10SCe03_2:cttresa']),
    'Withheld inventory changed',
  );
  const references: HistoricalCategoryReference[] = [];
  const unavailableReferences: HistoricalUnavailableReference[] = [];
  const seen = new Set<string>();
  for (const file of publicFiles) {
    const study = catalogue.studies.find((study) => study.id === file.studyId)!;
    const decision = exportDecision.studyDecisions.find(
      (decision) => decision.studyId === file.studyId,
    )!;
    const publicDecision = exportDecision.publicFiles.find(
      (decision) => decision.studyId === file.studyId,
    )!;
    requireBinding(
      file.schemaVersion === 2 && file.status === 'reviewed_historical_descriptive_reference',
      'Unreviewed public reference file',
    );
    requireBinding(
      file.edition === study.edition && decision.edition === study.edition,
      'Study edition changed',
    );
    requireBinding(
      decision.schemaVersion === 1 &&
        decision.decision === exportDecision.decision &&
        decision.reviewManifestSha256 === manifest,
      'Study decision changed',
    );
    requireBinding(
      file.candidateSha256 === decision.candidateSha256 &&
        file.sourceContractSha256 === decision.sourceContractSha256 &&
        file.reviewManifestSha256 === manifest,
      'Public file provenance differs from decision',
    );
    requireBinding(
      decision.reviewers.length === 2 &&
        sameIds(
          decision.reviewers.map((reviewer) => reviewer.role),
          receipts.map((receipt) => receipt.role),
        ) &&
        decision.reviewers.every((reviewer) => reviewer.decision === 'ACCEPTED_BOUNDED'),
      'Study reviewer evidence differs',
    );
    for (const receipt of receipts) {
      const accepted = receipt.studies.find((accepted) => accepted.studyId === study.id)!;
      requireBinding(
        accepted.candidateSha256 === decision.candidateSha256 &&
          sameIds(accepted.approvedQuestionIds, decision.approvedQuestionIds),
        'Independent receipts do not accept identical items and candidate',
      );
    }
    const expectedItems = catalogue.items.filter((item) => item.studyId === file.studyId);
    requireBinding(
      sameIds(
        file.questions.map((question) => question.id),
        expectedItems.map((item) => item.id),
      ),
      'Public question inventory differs from semantic catalogue',
    );
    requireBinding(
      file.questions.length === publicDecision.questionInventoryCount &&
        decision.approvedQuestionIds.length === publicDecision.reviewedReferenceCount,
      'Declared inventory counts differ',
    );
    requireBinding(
      sameIds(
        file.questions
          .filter((question) => question.status === 'reviewed_historical_reference')
          .map((question) => question.id),
        decision.approvedQuestionIds,
      ),
      'Public reference status differs from accepted inventory',
    );
    for (const question of file.questions) {
      const item = expectedItems.find((item) => item.id === question.id)!;
      requireBinding(!seen.has(item.id), 'Duplicate original question');
      seen.add(item.id);
      if (!decision.approvedQuestionIds.includes(item.id)) {
        requireBinding(
          exportDecision.withheldIds.includes(item.id) &&
            question.reference === null &&
            question.status === 'withheld_base_or_cell_count',
          'Unaccepted question contains reference numbers',
        );
        unavailableReferences.push(
          Object.freeze({
            questionId: item.id,
            reference: null,
            reason: 'withheld_base_or_cell_count',
          }),
        );
        continue;
      }
      const reference = question.reference;
      requireBinding(
        reference !== null && question.status === 'reviewed_historical_reference',
        'Accepted reference is absent',
      );
      requireBinding(
        reference.weight === 'pspwght' && reference.uncertainty === null,
        'Unexpected weight or uncertainty field',
      );
      for (const count of [
        reference.validCount,
        reference.totalCount,
        reference.missingCount,
        reference.notAskedCount,
      ]) {
        requireBinding(Number.isSafeInteger(count) && count >= 0, 'Invalid public count');
      }
      requireBinding(
        reference.validCount > 0 &&
          reference.totalCount ===
            reference.validCount + reference.missingCount + reference.notAskedCount,
        'Public count breakdown does not reconcile',
      );
      requireBinding(
        sameIds(
          reference.categories.map((category) => category.code),
          item.categories.map((category) => category.code),
        ),
        'Original export category codes differ',
      );
      const byCode = new Map(
        reference.categories.map((category) => [category.code, category.proportion]),
      );
      let sum = 0;
      for (const category of reference.categories) {
        requireBinding(
          typeof category.proportion === 'number' &&
            Number.isFinite(category.proportion) &&
            category.proportion >= 0 &&
            category.proportion <= 1,
          'Invalid published category share',
        );
        sum += category.proportion;
      }
      requireBinding(Math.abs(sum - 1) <= 1e-6, 'Published category shares are incomplete');
      const binding = item.codeBinding;
      references.push(
        Object.freeze({
          questionId: item.id,
          studyId: item.studyId,
          variable: item.variable,
          originalQuestionId: item.originalQuestionId,
          edition: study.edition,
          dataDoiUrl: study.dataDoiUrl,
          instrumentSourceIds: Object.freeze([
            ...new Set(item.sourceRefs.map((source) => source.sourceId)),
          ]),
          codeSourceId: binding.sourceId,
          sourceFieldId: binding.sourceFieldId,
          sourceFieldMetadataVersion: binding.sourceFieldMetadataVersion,
          dataFileMetadataId: binding.dataFileMetadataId,
          dataFileMetadataVersion: binding.dataFileMetadataVersion,
          basis: 'historical-study-item',
          weight: 'pspwght',
          denominator: 'valid_item_responses',
          validUnweightedN: reference.validCount,
          totalUnweightedN: reference.totalCount,
          missingUnweightedN: reference.missingCount,
          notAskedUnweightedN: reference.notAskedCount,
          categoryShares: Object.freeze(
            item.categories.map((category) =>
              Object.freeze({ code: category.code, share: byCode.get(category.code)! }),
            ),
          ),
        }),
      );
    }
  }
  requireBinding(
    seen.size === 43 && references.length === 42 && unavailableReferences.length === 1,
    'Expected 43 questions, 42 references and one explicit null',
  );
  return Object.freeze({
    catalogueSha256: catalogue.catalogueSha256,
    references: Object.freeze(references),
    unavailableReferences: Object.freeze(unavailableReferences),
  });
}
