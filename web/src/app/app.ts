import { DOCUMENT } from '@angular/common';
import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

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

  protected focusPage(): void {
    if (this.hasActivatedPage) {
      this.document.getElementById('main-content')?.focus({ preventScroll: true });
    }
    this.hasActivatedPage = true;
  }
}
