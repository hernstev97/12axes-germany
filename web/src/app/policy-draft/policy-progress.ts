import { ChangeDetectionStrategy, Component, computed, input, output } from '@angular/core';

export interface DraftCounts {
  readonly answered: number;
  readonly skipped: number;
  readonly untouched: number;
}

/** Screen heading, processed questions and the switch for the automatic change. */
@Component({
  selector: 'app-policy-progress',
  standalone: true,
  templateUrl: './policy-progress.html',
  styleUrl: './policy-progress.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PolicyProgress {
  readonly heading = input.required<string>();
  readonly total = input.required<number>();
  readonly counts = input.required<DraftCounts>();
  readonly autoAdvance = input.required<boolean>();
  readonly autoAdvanceChange = output<boolean>();
  protected readonly processed = computed(() => this.counts().answered + this.counts().skipped);

  protected toggle(event: Event): void {
    this.autoAdvanceChange.emit((event.target as HTMLInputElement).checked);
  }
}
