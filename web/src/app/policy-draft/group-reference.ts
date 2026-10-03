import type {
  HistoricalGroupInput,
  HistoricalGroupReference,
  HistoricalGroupStudy,
  HistoricalVoteGroup,
} from './group-reference-types';
import { REVIEWED_HISTORICAL_GROUPS } from './reviewed-historical-groups';

export type GroupReferenceState =
  | { readonly status: 'none' | 'rejected'; readonly studies: readonly [] }
  | { readonly status: 'bound'; readonly studies: readonly HistoricalGroupStudy[] };

/** Only the build-time authenticated immutable artifact may supply reference numbers. */
export function groupReferenceState(input: HistoricalGroupInput | null): GroupReferenceState {
  if (input === null) return { status: 'none', studies: [] };
  if (input !== REVIEWED_HISTORICAL_GROUPS) return { status: 'rejected', studies: [] };
  return { status: 'bound', studies: input.studies };
}

export type GroupComparison =
  | { readonly status: 'none' | 'other-study' | 'unavailable' }
  | {
      readonly status: 'available';
      readonly study: HistoricalGroupStudy;
      readonly group: HistoricalVoteGroup;
      readonly reference: HistoricalGroupReference;
    };

/** Selection is comparison context only. No answer or personal party inference enters this lookup. */
export function groupComparison(
  state: GroupReferenceState,
  studyId: string,
  groupId: string,
  questionId: string,
): GroupComparison {
  if (state.status !== 'bound') return { status: 'none' };
  const study = state.studies.find((candidate) => candidate.id === studyId);
  const group = study?.groups.find((candidate) => candidate.id === groupId);
  if (!study || !group) return { status: 'none' };
  if (!questionId.startsWith(`${study.id}:`)) return { status: 'other-study' };
  const question = group.questions.find((candidate) => candidate.id === questionId);
  if (!question?.reference) return { status: 'unavailable' };
  return { status: 'available', study, group, reference: question.reference };
}

export function groupFieldworkLabel(study: HistoricalGroupStudy): string {
  const date = new Intl.DateTimeFormat('de-DE', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    timeZone: 'UTC',
  });
  return study.fieldwork
    .map(
      (period) => `${date.format(new Date(period.start))} bis ${date.format(new Date(period.end))}`,
    )
    .join('; ');
}
