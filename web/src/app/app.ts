import { DOCUMENT } from '@angular/common';
import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { Router, RouterLink, RouterLinkActive, RouterOutlet, Scroll } from '@angular/router';
import { filter } from 'rxjs';

@Component({
  imports: [RouterLink, RouterLinkActive, RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.scss',
  templateUrl: './app.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class App {
  private readonly document = inject(DOCUMENT);
  private hasActivatedPage = false;

  constructor() {
    // Sprunglinks innerhalb der App führen den Tastaturfokus mit, nicht nur die Scrollposition.
    inject(Router)
      .events.pipe(
        filter((event): event is Scroll => event instanceof Scroll && !!event.anchor),
        takeUntilDestroyed(),
      )
      .subscribe(({ anchor }) => this.focusElement(anchor));
  }

  /** Mit <base href="/"> würde ein reiner Fragment-Link auf Unterseiten zur Startseite führen. */
  protected skipToContent(event: Event): void {
    event.preventDefault();
    this.document.getElementById('main-content')?.focus();
  }

  protected focusPage(): void {
    if (this.hasActivatedPage) {
      this.document.getElementById('main-content')?.focus({ preventScroll: true });
    }
    this.hasActivatedPage = true;
  }

  private focusElement(id: string | null): void {
    const target = id ? this.document.getElementById(id) : null;
    if (!target) {
      return;
    }
    if (!target.hasAttribute('tabindex')) {
      target.setAttribute('tabindex', '-1');
    }
    target.focus({ preventScroll: true });
  }
}
