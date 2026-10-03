import type { PolicyDraftItem } from './policy-catalogue';
import { POLICY_DRAFT_ITEMS } from './policy-catalogue';
import { PUBLIC_CATALOGUE } from './public-catalogue';

/**
 * A caller supplies separately reviewed, aggregate-only artifacts.
 * Shape/source validation is technical and does not grant publication approval.
 * No release flags are inferred from the input shape.
 */
export interface HistoricalCategoryReference {
  readonly questionId: string;
  readonly studyId: string;
  readonly variable: string;
  readonly originalQuestionId: string;
  readonly edition: string;
  readonly dataDoiUrl: string;
  readonly instrumentSourceIds: readonly string[];
  readonly codeSourceId: string;
  readonly sourceFieldId: string;
  readonly sourceFieldMetadataVersion: number;
  readonly dataFileMetadataId: string;
  readonly dataFileMetadataVersion: number;
  readonly basis: 'historical-study-item';
  readonly weight: 'pspwght';
  readonly denominator: 'valid_item_responses';
  readonly validUnweightedN: number;
  readonly totalUnweightedN: number;
  readonly missingUnweightedN: number;
  readonly notAskedUnweightedN: number;
  readonly categoryShares: readonly { readonly code: string; readonly share: number }[];
}

export interface HistoricalUnavailableReference {
  readonly questionId: string;
  readonly reference: null;
  readonly reason: 'withheld_base_or_cell_count';
}

export interface HistoricalReferenceInput {
  readonly catalogueSha256: string;
  readonly references: readonly HistoricalCategoryReference[];
  readonly unavailableReferences?: readonly HistoricalUnavailableReference[];
}

export type HistoricalReferenceState =
  | { readonly status: 'none' }
  | { readonly status: 'rejected' }
  | {
      readonly status: 'bound';
      readonly references: ReadonlyMap<string, HistoricalCategoryReference>;
      readonly unavailable: ReadonlyMap<string, HistoricalUnavailableReference>;
    };

export class HistoricalReferenceInputError extends Error {
  constructor() {
    super('Historical reference does not match the pinned public instrument metadata.');
    this.name = 'HistoricalReferenceInputError';
  }
}

function fail(): never {
  throw new HistoricalReferenceInputError();
}

function object(value: unknown, keys: readonly string[]): Record<string, unknown> {
  if (typeof value !== 'object' || value === null || Array.isArray(value)) return fail();
  const prototype: unknown = Object.getPrototypeOf(value);
  if (prototype !== Object.prototype && prototype !== null) return fail();
  const ownKeys = Reflect.ownKeys(value);
  if (ownKeys.length !== keys.length || ownKeys.some((key) => !keys.includes(String(key)))) {
    return fail();
  }
  for (const key of keys) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    if (!descriptor || !('value' in descriptor)) return fail();
  }
  return value as Record<string, unknown>;
}

function denseArray(value: unknown): readonly unknown[] {
  if (!Array.isArray(value)) return fail();
  const result: unknown[] = [];
  for (let index = 0; index < value.length; index++) {
    const descriptor = Object.getOwnPropertyDescriptor(value, String(index));
    if (!descriptor || !('value' in descriptor)) return fail();
    result.push(descriptor.value);
  }
  return result;
}

function reference(value: unknown, item: PolicyDraftItem): HistoricalCategoryReference {
  const binding = item.codeBinding;
  const identity = {
    questionId: item.id,
    studyId: item.studyId,
    variable: item.variable,
    originalQuestionId: item.originalQuestionId,
    edition: item.study.edition,
    dataDoiUrl: item.study.dataDoiUrl,
    codeSourceId: binding.sourceId,
    sourceFieldId: binding.sourceFieldId,
    sourceFieldMetadataVersion: binding.sourceFieldMetadataVersion,
    dataFileMetadataId: binding.dataFileMetadataId,
    dataFileMetadataVersion: binding.dataFileMetadataVersion,
    basis: 'historical-study-item' as const,
    weight: 'pspwght' as const,
    denominator: 'valid_item_responses' as const,
  };
  const input = object(value, [
    ...Object.keys(identity),
    'instrumentSourceIds',
    'validUnweightedN',
    'totalUnweightedN',
    'missingUnweightedN',
    'notAskedUnweightedN',
    'categoryShares',
  ]);
  for (const [key, expected] of Object.entries(identity)) {
    if (input[key] !== expected) return fail();
  }
  const instrumentSourceIds = denseArray(input['instrumentSourceIds']);
  const expectedSources = [...new Set(item.sourceRefs.map((source) => source.sourceId))];
  if (
    instrumentSourceIds.length !== expectedSources.length ||
    new Set(instrumentSourceIds).size !== expectedSources.length ||
    instrumentSourceIds.some((id) => typeof id !== 'string' || !expectedSources.includes(id))
  ) {
    return fail();
  }
  const n = input['validUnweightedN'];
  if (typeof n !== 'number' || !Number.isSafeInteger(n) || n < 1) return fail();
  const total = input['totalUnweightedN'];
  const missing = input['missingUnweightedN'];
  const notAsked = input['notAskedUnweightedN'];
  for (const count of [total, missing, notAsked]) {
    if (typeof count !== 'number' || !Number.isSafeInteger(count) || count < 0) return fail();
  }
  if (total !== n + (missing as number) + (notAsked as number)) return fail();
  const shares = denseArray(input['categoryShares']);
  if (shares.length !== item.categories.length) return fail();
  const byCode = new Map<string, number>();
  for (const row of shares) {
    const category = object(row, ['code', 'share']);
    const code = category['code'];
    const share = category['share'];
    if (
      typeof code !== 'string' ||
      !item.categories.some((option) => option.code === code && !option.isMissingApi) ||
      byCode.has(code) ||
      typeof share !== 'number' ||
      !Number.isFinite(share) ||
      share < 0 ||
      share > 1
    ) {
      return fail();
    }
    byCode.set(code, share);
  }
  // Only checks mathematical completeness; it says nothing about empirical validity.
  if (Math.abs([...byCode.values()].reduce((sum, share) => sum + share, 0) - 1) > 1e-6) {
    return fail();
  }
  return Object.freeze({
    ...identity,
    instrumentSourceIds: Object.freeze(expectedSources),
    validUnweightedN: n,
    totalUnweightedN: total as number,
    missingUnweightedN: missing as number,
    notAskedUnweightedN: notAsked as number,
    // Display order follows the bound instrument; matching always uses original codes.
    categoryShares: Object.freeze(
      item.categories.map((category) =>
        Object.freeze({ code: category.code, share: byCode.get(category.code)! }),
      ),
    ),
  });
}

export function bindHistoricalReferences(
  value: HistoricalReferenceInput | null,
): HistoricalReferenceState {
  if (value === null) return Object.freeze({ status: 'none' });
  const optional = Object.prototype.hasOwnProperty.call(value, 'unavailableReferences');
  const input = object(value, [
    'catalogueSha256',
    'references',
    ...(optional ? ['unavailableReferences'] : []),
  ]);
  if (input['catalogueSha256'] !== PUBLIC_CATALOGUE.catalogueSha256) return fail();
  const references = new Map<string, HistoricalCategoryReference>();
  for (const entry of denseArray(input['references'])) {
    // Inspect identity as a passive data field before the full shape validation.
    if (typeof entry !== 'object' || entry === null) return fail();
    const descriptor = Object.getOwnPropertyDescriptor(entry, 'questionId');
    if (!descriptor || !('value' in descriptor)) return fail();
    const questionId: unknown = descriptor.value;
    const item = POLICY_DRAFT_ITEMS.find((candidate) => candidate.id === questionId);
    if (!item || references.has(item.id)) return fail();
    references.set(item.id, reference(entry, item));
  }
  const unavailable = new Map<string, HistoricalUnavailableReference>();
  for (const entry of optional ? denseArray(input['unavailableReferences']) : []) {
    const missingReference = object(entry, ['questionId', 'reference', 'reason']);
    const id = missingReference['questionId'];
    if (
      typeof id !== 'string' ||
      !POLICY_DRAFT_ITEMS.some((item) => item.id === id) ||
      references.has(id) ||
      unavailable.has(id) ||
      missingReference['reference'] !== null ||
      missingReference['reason'] !== 'withheld_base_or_cell_count'
    )
      return fail();
    unavailable.set(
      id,
      Object.freeze({ questionId: id, reference: null, reason: 'withheld_base_or_cell_count' }),
    );
  }
  return Object.freeze({ status: 'bound', references, unavailable });
}

export function referenceState(value: HistoricalReferenceInput | null): HistoricalReferenceState {
  try {
    return bindHistoricalReferences(value);
  } catch (error) {
    if (error instanceof HistoricalReferenceInputError)
      return Object.freeze({ status: 'rejected' });
    throw error;
  }
}
