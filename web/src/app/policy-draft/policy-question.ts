import {
  ChangeDetectionStrategy,
  Component,
  computed,
  DestroyRef,
  inject,
  input,
  model,
  output,
} from '@angular/core';
import type { PolicyAnswer } from '../research/policy-profile';
import { categoryLabel, type PolicyDraftItem } from './policy-catalogue';
import { type DraftCounts, PolicyProgress } from './policy-progress';
import { PolicySourceDetails } from './policy-source-details';

export type SkipReason = 'unspecified' | 'dont-know' | 'decline';

/** Pause after a deliberate choice, so the chosen option stays visible before the change. */
export const AUTO_ADVANCE_DELAY_MS = 350;

const SCALE_LABEL = /^(\d+)(: .+)?$/;

/**
 * One question of the local draft: progress, answer options, skipping and sources.
 * Holds no answers. Every change is emitted to PolicyDraft, which owns the session.
 */
@Component({
  selector: 'app-policy-question',
  standalone: true,
  imports: [PolicyProgress, PolicySourceDetails],
  templateUrl: './policy-question.html',
  styleUrl: './policy-question.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PolicyQuestion {
  readonly item = input.required<PolicyDraftItem>();
  readonly answer = input.required<PolicyAnswer>();
  /** One-based position in the catalogue. */
  readonly position = input.required<number>();
  readonly total = input.required<number>();
  readonly counts = input.required<DraftCounts>();
  readonly skipReason = input.required<SkipReason>();
  readonly autoAdvance = model(true);
  readonly answerChosen = output<string>();
  readonly skipReasonChanged = output<SkipReason>();
  readonly skipRequested = output<void>();
  readonly resetRequested = output<void>();
  readonly previousRequested = output<void>();
  readonly nextRequested = output<void>();

  protected readonly categoryLabel = categoryLabel;
  protected readonly isLast = computed(() => this.position() === this.total());
  protected readonly hasContext = computed(
    () =>
      this.item().introductionsDe.length > 0 ||
      !!this.item().definitionDe?.length ||
      !!this.item().situationDe,
  );
  /**
   * Numbered 0–10 lists can be shown as one row. Each label keeps its original
   * text; only the end descriptions move below the row on wide screens.
   */
  protected readonly scale = computed(() => {
    const item = this.item();
    if (item.offeredCategories.length < 7) return null;
    const options = item.offeredCategories.map((category) => {
      const match = SCALE_LABEL.exec(categoryLabel(item, category));
      return match ? { code: category.code, number: match[1]!, text: match[2] ?? '' } : null;
    });
    if (options.some((option) => option === null)) return null;
    const valid = options as { code: string; number: string; text: string }[];
    return {
      options: valid,
      start: valid[0]!.text.slice(2),
      end: valid.at(-1)!.text.slice(2),
    };
  });

  private arrowNavigation = false;
  private advanceTimer: ReturnType<typeof setTimeout> | undefined;

  constructor() {
    inject(DestroyRef).onDestroy(() => this.cancelAdvance());
  }

  protected stateLabel(answer: PolicyAnswer): string {
    return { untouched: 'Unberührt', answered: 'Beantwortet', skipped: 'Übersprungen' }[
      answer.status
    ];
  }

  /** Recreates the radio inputs for each question instead of reusing them. */
  protected optionKey(code: string): string {
    return `${this.item().id}:${code}`;
  }

  protected isSelected(code: string): boolean {
    const answer = this.answer();
    return answer.status === 'answered' && answer.code === code;
  }

  /**
   * Arrow keys move through a native radio group and select on the way; they never advance.
   * Space or Enter on a checked option confirms it. Chromium fires no click for Space on a
   * radio that is already checked, so the key itself confirms here.
   */
  protected handleKey(event: KeyboardEvent, pressed: boolean): void {
    if (event.key.startsWith('Arrow')) {
      this.arrowNavigation = pressed;
      return;
    }
    const target = event.target;
    if (
      !pressed &&
      (event.key === ' ' || event.key === 'Enter') &&
      target instanceof HTMLInputElement &&
      target.type === 'radio' &&
      target.checked
    ) {
      this.confirm(target.value);
    }
  }

  /** A click, tap or Space confirms an option; with auto-advance on, the next question follows. */
  protected confirm(code: string): void {
    this.cancelAdvance();
    if (this.arrowNavigation || !this.autoAdvance() || this.isLast()) return;
    const id = this.item().id;
    this.advanceTimer = setTimeout(() => {
      this.advanceTimer = undefined;
      const answer = this.answer();
      if (
        this.autoAdvance() &&
        this.item().id === id &&
        answer.status === 'answered' &&
        answer.code === code
      ) {
        this.nextRequested.emit();
      }
    }, AUTO_ADVANCE_DELAY_MS);
  }

  protected setAutoAdvance(on: boolean): void {
    this.cancelAdvance();
    this.autoAdvance.set(on);
  }

  protected setSkipReason(event: Event): void {
    const value = (event.target as HTMLSelectElement).value;
    if (value === 'unspecified' || value === 'dont-know' || value === 'decline') {
      this.skipReasonChanged.emit(value);
    }
  }

  protected request(action: 'skip' | 'reset' | 'previous' | 'next'): void {
    this.cancelAdvance();
    ({
      skip: this.skipRequested,
      reset: this.resetRequested,
      previous: this.previousRequested,
      next: this.nextRequested,
    })[action].emit();
  }

  private cancelAdvance(): void {
    clearTimeout(this.advanceTimer);
    this.advanceTimer = undefined;
  }
}
