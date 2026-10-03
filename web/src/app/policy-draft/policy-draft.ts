import {
  afterNextRender,
  ChangeDetectionStrategy,
  Component,
  computed,
  ElementRef,
  inject,
  Injector,
  input,
  signal,
  viewChild,
} from '@angular/core';
import { PolicyProfileSession, type PolicyAnswer } from '../research/policy-profile';
import { type HistoricalReferenceInput, referenceState } from './historical-reference';
import type { HistoricalGroupInput } from './group-reference-types';
import { groupComparison, groupFieldworkLabel, groupReferenceState } from './group-reference';
import {
  categoryLabel,
  POLICY_DRAFT_ITEMS,
  POLICY_DRAFT_QUESTIONS,
  POLICY_RUBRICS,
  type PolicyDraftItem,
} from './policy-catalogue';
import { PolicySourceDetails } from './policy-source-details';
import { AREA_SCOPES, UNCOVERED_AREAS } from './profile/area-scope';
import { buildAnswerProfile, type ProfileAnswer } from './profile/profile-engine';
import { CROSS_REFERENCE_NOTE, MIDDLE_NOTE } from './profile/profile-structure';
import {
  indexReferencesV22,
  intervalFor,
  pairKey,
  type EntryV22,
  type ReferencesV22,
} from './reference-v22';
import { ITEM_RULES } from './profile/profile-rules';

type DraftView = 'questions' | 'overview' | 'results';

/** One historical single reference as displayed, from v2 or v2.2, with optional intervals. */
interface ReferenceView {
  readonly weight: 'pspwght';
  readonly validUnweightedN: number;
  readonly totalUnweightedN: number;
  readonly missingUnweightedN: number;
  readonly notAskedUnweightedN: number;
  readonly categoryShares: readonly {
    readonly code: string;
    readonly share: number;
    readonly lower: number | null;
    readonly upper: number | null;
  }[];
  readonly hasIntervals: boolean;
}

/** Studies whose data files contain a complete sampling design (Analyseplan v2.2, 4.1). */
const DESIGN_STUDIES = new Set(['ESS9e03_3', 'ESS10SCe03_2', 'ESS11e04_2']);
type SkipReason = 'unspecified' | 'dont-know' | 'decline';

/**
 * Unrouted preparation. Requires the existing App shell and global styles.
 * Session answers remain in this instance's RAM. No output emits answers, no
 * persistence/network service is injected, and navigation never changes URLs.
 * Mounting this component is not a test, design, data, or release approval.
 */
@Component({
  selector: 'app-policy-draft',
  standalone: true,
  imports: [PolicySourceDetails],
  templateUrl: './policy-draft.html',
  styleUrl: './policy-draft.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PolicyDraft {
  readonly historicalReferences = input<HistoricalReferenceInput | null>(null);
  readonly historicalGroups = input<HistoricalGroupInput | null>(null);
  readonly referencesV22 = input<ReferencesV22 | null>(null);
  protected readonly v22 = computed(() => indexReferencesV22(this.referencesV22()));
  private readonly injector = inject(Injector);
  private readonly pageHeading = viewChild<ElementRef<HTMLElement>>('pageHeading');
  private readonly questionHeading = viewChild<ElementRef<HTMLElement>>('questionHeading');
  private readonly answerFieldset = viewChild<ElementRef<HTMLFieldSetElement>>('answerFieldset');
  private readonly session = new PolicyProfileSession(POLICY_DRAFT_QUESTIONS);
  protected readonly snapshot = signal(this.session.snapshot());
  protected readonly view = signal<DraftView>('questions');
  protected readonly items = POLICY_DRAFT_ITEMS;
  protected readonly categoryLabel = categoryLabel;
  protected readonly skipReason = signal<SkipReason>('unspecified');
  private readonly skipReasons = signal<ReadonlyMap<string, SkipReason>>(new Map());
  protected readonly skipLabels: Readonly<Record<SkipReason, string>> = Object.freeze({
    unspecified: 'Keine Angabe',
    'dont-know': 'Weiß nicht',
    decline: 'Keine Antwort geben',
  });
  protected readonly references = computed(() => referenceState(this.historicalReferences()));
  protected readonly groups = computed(() => groupReferenceState(this.historicalGroups()));
  protected readonly selectedGroupStudyId = signal('');
  protected readonly selectedGroupId = signal('');
  protected readonly selectedGroupStudy = computed(() =>
    this.groups().studies.find((study) => study.id === this.selectedGroupStudyId()),
  );
  protected readonly selectedGroup = computed(() =>
    this.selectedGroupStudy()?.groups.find((group) => group.id === this.selectedGroupId()),
  );
  protected readonly groupFieldworkLabel = groupFieldworkLabel;
  protected readonly answers = computed(
    () =>
      new Map(this.snapshot().responses.map((response) => [response.question.id, response.answer])),
  );
  protected readonly currentIndex = computed(() =>
    this.items.findIndex((item) => item.id === this.snapshot().currentQuestionId),
  );
  protected readonly currentItem = computed(() => this.items[this.currentIndex()]!);
  protected readonly currentAnswer = computed(() => this.answers().get(this.currentItem().id)!);
  protected readonly resultRubrics = POLICY_RUBRICS.map((rubric) =>
    Object.freeze({
      ...rubric,
      items: this.items.filter((item) => item.primaryTheme === rubric.id),
    }),
  );
  protected readonly profile = computed(() =>
    buildAnswerProfile(
      this.items,
      POLICY_RUBRICS,
      new Map<string, ProfileAnswer>(
        this.snapshot().responses.map((response) => [response.question.id, response.answer]),
      ),
    ),
  );
  protected readonly counts = computed(() => {
    const responses = this.snapshot().responses;
    return {
      answered: responses.filter((response) => response.answer.status === 'answered').length,
      skipped: responses.filter((response) => response.answer.status === 'skipped').length,
      untouched: responses.filter((response) => response.answer.status === 'untouched').length,
    };
  });

  protected readonly middleNote = MIDDLE_NOTE;
  protected readonly crossReferenceNote = CROSS_REFERENCE_NOTE;
  protected readonly uncoveredAreas = UNCOVERED_AREAS;

  private readonly statementById = computed(
    () =>
      new Map(
        this.profile()
          .areas.flatMap((area) => area.statements)
          .map((statement) => [statement.itemId, statement]),
      ),
  );
  private readonly areaById = computed(
    () => new Map(this.profile().areas.map((area) => [area.areaId, area])),
  );

  protected statementFor(id: string) {
    return this.statementById().get(id) ?? null;
  }

  protected areaProfile(id: string) {
    return this.areaById().get(id)!;
  }

  protected scopeFor(id: string) {
    return AREA_SCOPES.find((scope) => scope.id === id) ?? null;
  }

  protected titlesFor(ids: readonly string[]): string {
    return ids.map((id) => ITEM_RULES[id]!.title).join(', ');
  }

  /** Share of the own category; null without an answer or for a zero share. */
  protected chosenShare(
    answer: PolicyAnswer,
    shares: readonly { readonly code: string; readonly share: number }[],
  ): number | null {
    if (answer.status !== 'answered') return null;
    return shares.find((entry) => entry.code === answer.code)?.share ?? null;
  }

  protected stateLabel(answer: PolicyAnswer): string {
    return { untouched: 'Unberührt', answered: 'Beantwortet', skipped: 'Übersprungen' }[
      answer.status
    ];
  }

  protected answerLabel(item: PolicyDraftItem, answer: PolicyAnswer): string | null {
    if (answer.status !== 'answered') return null;
    return categoryLabel(item, item.categories.find((category) => category.code === answer.code)!);
  }

  /** Recreates the radio inputs for each question instead of reusing them. */
  protected optionKey(code: string): string {
    return `${this.currentItem().id}:${code}`;
  }

  protected isSelected(answer: PolicyAnswer, code: string): boolean {
    return answer.status === 'answered' && answer.code === code;
  }

  protected skipLabel(id: string): string {
    return this.skipLabels[this.skipReasons().get(id) ?? 'unspecified'];
  }

  protected select(code: string): void {
    const id = this.currentItem().id;
    this.session.answer(id, code);
    this.clearSkipReason(id);
    this.update();
  }

  protected setSkipReason(event: Event): void {
    const value = (event.target as HTMLSelectElement).value;
    if (value === 'unspecified' || value === 'dont-know' || value === 'decline') {
      this.skipReason.set(value);
    }
  }

  protected skip(): void {
    const id = this.currentItem().id;
    this.session.skip(id);
    this.skipReasons.set(new Map(this.skipReasons()).set(id, this.skipReason()));
    this.next();
  }

  protected resetAnswer(): void {
    const id = this.currentItem().id;
    this.session.resetAnswer(id);
    this.clearSkipReason(id);
    this.update();
    this.focus('question');
  }

  protected previous(): void {
    this.session.previous();
    this.update();
    this.focus('question');
  }

  protected next(): void {
    if (this.currentIndex() === this.items.length - 1) {
      this.update();
      this.show('results');
    } else {
      this.session.next();
      this.update();
      this.focus('question');
    }
  }

  protected edit(id: string): void {
    this.session.goTo(id);
    this.update();
    this.view.set('questions');
    this.focus('question');
  }

  protected show(view: DraftView): void {
    this.view.set(view);
    this.focus('page');
  }

  protected referenceFor(id: string): ReferenceView | null {
    const state = this.references();
    const v2 = state.status === 'bound' ? state.references.get(id) : undefined;
    const entry: EntryV22 | undefined = this.v22().single.get(id);
    if (v2) {
      const categoryShares = v2.categoryShares.map((category) => ({
        ...category,
        lower: intervalFor(entry, category.code)?.lower ?? null,
        upper: intervalFor(entry, category.code)?.upper ?? null,
      }));
      return {
        weight: v2.weight,
        validUnweightedN: v2.validUnweightedN,
        totalUnweightedN: v2.totalUnweightedN,
        missingUnweightedN: v2.missingUnweightedN,
        notAskedUnweightedN: v2.notAskedUnweightedN,
        categoryShares,
        hasIntervals: categoryShares.some((category) => category.lower !== null),
      };
    }
    const reference = entry?.reference;
    if (!reference) return null;
    const categoryShares = reference.categories.map((category) => ({
      code: category.code,
      share: category.proportion,
      lower: category.lower,
      upper: category.upper,
    }));
    return {
      weight: 'pspwght',
      validUnweightedN: reference.validCount,
      totalUnweightedN: reference.totalCount,
      missingUnweightedN: reference.missingCount,
      notAskedUnweightedN: reference.notAskedCount,
      categoryShares,
      hasIntervals: categoryShares.some((category) => category.lower !== null),
    };
  }

  /** Why no numbers are shown: withheld by the 100/5 rule or no valid answers. */
  protected unavailableReferenceFor(id: string): 'withheld' | 'no-valid' | null {
    const state = this.references();
    if (state.status === 'bound' && state.unavailable.has(id)) return 'withheld';
    const status = this.v22().single.get(id)?.status;
    if (status === 'withheld_base_or_cell_count') return 'withheld';
    if (status === 'no_valid_answers') return 'no-valid';
    return null;
  }

  protected designStudy(studyId: string): boolean {
    return DESIGN_STUDIES.has(studyId);
  }

  protected referenceLabel(item: PolicyDraftItem, code: string): string {
    return categoryLabel(item, item.categories.find((category) => category.code === code)!);
  }

  protected setGroupStudy(event: Event): void {
    const id = (event.target as HTMLSelectElement).value;
    this.selectedGroupStudyId.set(this.groups().studies.some((study) => study.id === id) ? id : '');
    this.selectedGroupId.set('');
  }

  protected setGroup(event: Event): void {
    const id = (event.target as HTMLSelectElement).value;
    this.selectedGroupId.set(
      this.selectedGroupStudy()?.groups.some((group) => group.id === id) ? id : '',
    );
  }

  protected groupComparisonFor(id: string) {
    const base = groupComparison(
      this.groups(),
      this.selectedGroupStudyId(),
      this.selectedGroupId(),
      id,
    );
    if (base.status !== 'available' && base.status !== 'unavailable') return base;
    const entry = this.v22().pairs.get(pairKey(this.selectedGroupId(), id));
    if (base.status === 'available') {
      return { ...base, intervals: entry };
    }
    const reference = entry?.reference;
    if (!reference) return base;
    const study = this.selectedGroupStudy()!;
    const group = this.selectedGroup()!;
    return {
      status: 'available' as const,
      study,
      group,
      reference: {
        weight: 'pspwght' as const,
        validCount: reference.validCount,
        totalCount: reference.totalCount,
        missingCount: reference.missingCount,
        notAskedCount: reference.notAskedCount,
        categories: reference.categories.map((category) => ({
          code: category.code,
          proportion: category.proportion,
        })),
        uncertainty: null,
      },
      intervals: entry,
    };
  }

  protected groupInterval(entry: EntryV22 | undefined, code: string) {
    return intervalFor(entry, code);
  }

  protected groupDocumentLabel(id: string): string {
    if (id.endsWith('-de-questionnaire')) return 'Deutscher Originalfragebogen';
    if (id.endsWith('-political-parties-appendix')) return 'Offizielle Parteienappendix';
    if (id === 'party-and-vote-original-codelists')
      return 'Öffentliche API-Metadaten und Originalcodelisten';
    return 'ESS-Nutzungsbedingungen';
  }

  protected percentage(share: number): string {
    return new Intl.NumberFormat('de-DE', { style: 'percent', maximumFractionDigits: 1 }).format(
      share,
    );
  }

  private clearSkipReason(id: string): void {
    const reasons = new Map(this.skipReasons());
    reasons.delete(id);
    this.skipReasons.set(reasons);
    this.skipReason.set('unspecified');
  }

  private update(): void {
    this.snapshot.set(this.session.snapshot());
    this.skipReason.set(this.skipReasons().get(this.session.currentQuestion!.id) ?? 'unspecified');
    this.syncRadios();
  }

  /**
   * `[checked]` is only written when the bound value changes between renders.
   * Input faster than one render could leave a native radio checked while the
   * session says otherwise, so the rendered radios are aligned after each update.
   */
  private syncRadios(): void {
    afterNextRender(
      () => {
        const fieldset = this.answerFieldset()?.nativeElement;
        if (!fieldset) return;
        const answer = this.currentAnswer();
        for (const input of fieldset.querySelectorAll<HTMLInputElement>('input[type="radio"]')) {
          input.checked = answer.status === 'answered' && answer.code === input.value;
        }
      },
      { injector: this.injector },
    );
  }

  private focus(target: 'page' | 'question'): void {
    afterNextRender(
      () => {
        const heading = (target === 'page' ? this.pageHeading() : this.questionHeading())
          ?.nativeElement;
        if (!heading) return;
        heading.focus({ preventScroll: true });
        // Focus alone can leave the rendered target above the viewport after an edit.
        heading.scrollIntoView({ block: 'start', inline: 'nearest', behavior: 'instant' });
      },
      { injector: this.injector },
    );
  }
}
