import { DOCUMENT } from '@angular/common';
import {
  ChangeDetectionStrategy,
  Component,
  DestroyRef,
  computed,
  effect,
  inject,
  input,
  linkedSignal,
  signal,
} from '@angular/core';
import { RouterLink } from '@angular/router';
import { Artwork, artworkSrc, artworkSrcset } from './artwork';

function isKeyboardFocus(target: EventTarget | null): boolean {
  try {
    return target instanceof Element && target.matches(':focus-visible');
  } catch {
    // Ohne Unterstützung für :focus-visible gilt jeder Fokus als Tastaturfokus.
    return true;
  }
}

/** Seitenverhältnis des Passepartouts und Anteil der Bildfläche, siehe art-gallery.scss. */
const MAT_RATIO = 1;
const MAT_INNER = 0.86;

/**
 * Zeigt Gemälde nacheinander in einem Passepartout. Der Wechsel läuft nur, solange das aktuelle
 * Bild geladen ist. Er hält bei Hover und verborgenem Tab an und endet bei Tastaturfokus. Bei
 * reduzierter Bewegung startet er nicht von selbst.
 */
@Component({
  selector: 'app-art-gallery',
  imports: [RouterLink],
  templateUrl: './art-gallery.html',
  styleUrl: './art-gallery.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
  host: {
    '(mouseenter)': 'hovered.set(true)',
    '(mouseleave)': 'hovered.set(false)',
    '(focusin)': 'onFocusIn($event)',
  },
})
export class ArtGallery {
  readonly artworks = input.required<readonly Artwork[]>();
  readonly label = input.required<string>();
  readonly intervalMs = input(8000);
  /** Ohne Angabe beginnt die Galerie bei einem zufälligen Bild. */
  readonly startIndex = input<number>();

  private readonly start = computed(() => {
    const count = this.artworks().length;
    const start = this.startIndex() ?? Math.floor(Math.random() * count);
    return Math.max(Math.min(start, count - 1), 0);
  });

  protected readonly index = linkedSignal(() => this.start());
  protected readonly count = computed(() => this.artworks().length);
  /** Bilder, deren Datei geladen werden darf: das aktuelle und das jeweils nächste. */
  protected readonly requested = linkedSignal<ReadonlySet<number>>(() => new Set([this.start()]));
  private readonly loaded = linkedSignal<ReadonlySet<number>>(() => {
    this.artworks();
    return new Set();
  });

  protected readonly paused = signal(true);
  protected readonly hovered = signal(false);
  private readonly hidden = signal(false);
  protected readonly rotating = computed(
    () =>
      this.count() > 1 &&
      !this.paused() &&
      !this.hovered() &&
      !this.hidden() &&
      this.loaded().has(this.index()),
  );

  constructor() {
    const document = inject(DOCUMENT);
    const destroyRef = inject(DestroyRef);

    const motion = document.defaultView?.matchMedia?.('(prefers-reduced-motion: reduce)');
    this.paused.set(motion?.matches ?? true);
    const stopOnReducedMotion = (event: MediaQueryListEvent) => {
      if (event.matches) {
        this.paused.set(true);
      }
    };
    motion?.addEventListener?.('change', stopOnReducedMotion);

    const updateVisibility = () => this.hidden.set(document.visibilityState === 'hidden');
    updateVisibility();
    document.addEventListener('visibilitychange', updateVisibility);

    destroyRef.onDestroy(() => {
      motion?.removeEventListener?.('change', stopOnReducedMotion);
      document.removeEventListener('visibilitychange', updateVisibility);
    });

    effect((onCleanup) => {
      // Der Index wird gelesen, damit jeder Wechsel einen neuen Timer startet.
      const index = this.index();
      if (!this.rotating()) {
        return;
      }
      const timer = setTimeout(() => this.show(index + 1), this.intervalMs());
      onCleanup(() => clearTimeout(timer));
    });
  }

  protected show(target: number): void {
    const count = this.count();
    if (count === 0) {
      return;
    }
    const index = ((target % count) + count) % count;
    this.request(index);
    if (this.loaded().has(index)) {
      this.request((index + 1) % count);
    }
    this.index.set(index);
  }

  /** Nach dem Karussell-Muster der WAI-ARIA APG endet der Wechsel bei Tastaturfokus dauerhaft. */
  protected onFocusIn(event: FocusEvent): void {
    if (isKeyboardFocus(event.target)) {
      this.paused.set(true);
    }
  }

  protected togglePause(): void {
    this.paused.update((paused) => !paused);
  }

  protected markLoaded(index: number): void {
    this.loaded.update((loaded) => new Set(loaded).add(index));
    if (index === this.index()) {
      this.request((index + 1) % this.count());
    }
  }

  protected isWide(artwork: Artwork): boolean {
    return artwork.width / artwork.height >= MAT_RATIO;
  }

  /** Angezeigte Bildbreite relativ zur Galeriespalte der Startseite (home.scss). */
  protected sizes(artwork: Artwork): string {
    const share = MAT_INNER * Math.min(1, artwork.width / artwork.height / MAT_RATIO);
    const width = (column: string) => `calc(${column} * ${share.toFixed(2)})`;
    return `(max-width: 860px) ${width('min(92vw, 612px)')}, (max-width: 1360px) ${width('44vw')}, ${width('580px')}`;
  }

  protected src(artwork: Artwork): string {
    return artworkSrc(artwork);
  }

  protected srcset(artwork: Artwork): string {
    return artworkSrcset(artwork);
  }

  private request(index: number): void {
    if (!this.requested().has(index)) {
      this.requested.update((requested) => new Set(requested).add(index));
    }
  }
}
