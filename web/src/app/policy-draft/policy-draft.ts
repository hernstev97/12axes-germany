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
import {
  categoryLabel,
  POLICY_DRAFT_ITEMS,
  POLICY_DRAFT_QUESTIONS,
  POLICY_RUBRICS,
  type PolicyDraftItem,
} from './policy-catalogue';
import { PolicySourceDetails } from './policy-source-details';

type DraftView = 'questions' | 'overview' | 'results';
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
  private readonly injector = inject(Injector);
  private readonly pageHeading = viewChild<ElementRef<HTMLElement>>('pageHeading');
  private readonly questionHeading = viewChild<ElementRef<HTMLElement>>('questionHeading');
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
  protected readonly counts = computed(() => {
    const responses = this.snapshot().responses;
    return {
      answered: responses.filter((response) => response.answer.status === 'answered').length,
      skipped: responses.filter((response) => response.answer.status === 'skipped').length,
      untouched: responses.filter((response) => response.answer.status === 'untouched').length,
    };
  });

  protected stateLabel(answer: PolicyAnswer): string {
    return { untouched: 'Unberührt', answered: 'Beantwortet', skipped: 'Übersprungen' }[
      answer.status
    ];
  }

  protected answerLabel(item: PolicyDraftItem, answer: PolicyAnswer): string | null {
    if (answer.status !== 'answered') return null;
    return categoryLabel(item, item.categories.find((category) => category.code === answer.code)!);
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

  protected referenceFor(id: string) {
    const state = this.references();
    return state.status === 'bound' ? (state.references.get(id) ?? null) : null;
  }

  protected unavailableReferenceFor(id: string) {
    const state = this.references();
    return state.status === 'bound' ? (state.unavailable.get(id) ?? null) : null;
  }

  protected referenceLabel(item: PolicyDraftItem, code: string): string {
    return categoryLabel(item, item.categories.find((category) => category.code === code)!);
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
  }

  private focus(target: 'page' | 'question'): void {
    afterNextRender(
      () => {
        const heading = target === 'page' ? this.pageHeading() : this.questionHeading();
        heading?.nativeElement.focus({ preventScroll: true });
      },
      { injector: this.injector },
    );
  }
}
