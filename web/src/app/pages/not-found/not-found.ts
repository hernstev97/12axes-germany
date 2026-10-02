import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-not-found',
  imports: [RouterLink],
  template: `
    <section class="page-width">
      <p class="eyebrow">Seite nicht gefunden</p>
      <h1>Hier geht es<br /><em>zurück zum Anfang.</em></h1>
      <p>Unter dieser Adresse gibt es keine Seite.</p>
      <a class="button-link primary" routerLink="/"
        >Zur Startseite <span aria-hidden="true">↗</span></a
      >
    </section>
  `,
  styles: `
    section {
      padding-block: 4rem 5rem;
    }
    h1 {
      margin-top: 1.2rem;
      font-size: clamp(2.5rem, 6vw, 5rem);
    }
    p:not(.eyebrow) {
      margin-block: 1.5rem 2rem;
    }
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class NotFound {}
