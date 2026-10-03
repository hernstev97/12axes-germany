/**
 * Reviewed v2.2 references (Analyseplan v2.2): shares with design-based 95 % intervals
 * where the study has a complete sampling design, references for the questions added in
 * v2.2, and vote-group pairs for new ESS5/ESS8 questions. Aggregates only.
 */
export interface CategoryV22 {
  readonly code: string;
  readonly proportion: number;
  readonly lower: number | null;
  readonly upper: number | null;
}

export interface ReferenceV22 {
  readonly validCount: number;
  readonly totalCount: number;
  readonly missingCount: number;
  readonly notAskedCount: number;
  readonly categories: readonly CategoryV22[];
  readonly interval: {
    readonly degreesOfFreedom: number;
    readonly strata: number;
    readonly psus: number;
  } | null;
}

export interface EntryV22 {
  readonly status: string;
  readonly reference: ReferenceV22 | null;
}

export interface ReferencesV22 {
  readonly sources: Readonly<Record<string, string>>;
  readonly studies: readonly {
    readonly study: string;
    readonly designAvailable: boolean;
    readonly questions: readonly (EntryV22 & { readonly id: string })[];
    readonly groups: readonly {
      readonly groupId: string;
      readonly pairs: readonly (EntryV22 & { readonly questionId: string })[];
    }[];
  }[];
}

export interface IndexedReferencesV22 {
  readonly single: ReadonlyMap<string, EntryV22>;
  readonly pairs: ReadonlyMap<string, EntryV22>;
}

const REVIEWED = 'reviewed_historical_reference';

export function pairKey(groupId: string, questionId: string): string {
  return `${groupId}|${questionId}`;
}

/** Indexes reviewed entries. Entries without the reviewed status never carry numbers. */
export function indexReferencesV22(input: ReferencesV22 | null): IndexedReferencesV22 {
  const single = new Map<string, EntryV22>();
  const pairs = new Map<string, EntryV22>();
  for (const study of input?.studies ?? []) {
    for (const question of study.questions) {
      single.set(question.id, {
        status: question.status,
        reference: question.status === REVIEWED ? question.reference : null,
      });
    }
    for (const group of study.groups) {
      for (const pair of group.pairs) {
        pairs.set(pairKey(group.groupId, pair.questionId), {
          status: pair.status,
          reference: pair.status === REVIEWED ? pair.reference : null,
        });
      }
    }
  }
  return { single, pairs };
}

/** The interval for one category, or null if none was computed. */
export function intervalFor(
  entry: EntryV22 | undefined,
  code: string,
): { readonly lower: number; readonly upper: number } | null {
  const category = entry?.reference?.categories.find((candidate) => candidate.code === code);
  if (!category || category.lower === null || category.upper === null) return null;
  return { lower: category.lower, upper: category.upper };
}
