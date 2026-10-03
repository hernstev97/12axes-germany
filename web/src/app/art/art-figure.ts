import { ChangeDetectionStrategy, Component, computed, input } from '@angular/core';
import { Artwork, artworkSrc, artworkSrcset } from './artwork';

@Component({
  selector: 'app-art-figure',
  template: `
    <figure>
      <img
        [src]="src()"
        [srcset]="srcset()"
        [sizes]="sizes()"
        [width]="artwork().width"
        [height]="artwork().height"
        [alt]="artwork().alt"
        [style.background-color]="artwork().tone"
        [attr.loading]="priority() ? null : 'lazy'"
        [attr.fetchpriority]="priority() ? 'high' : null"
        decoding="async"
      />
      <figcaption>
        <span class="artist">{{ artwork().artist }}</span>
        <span
          ><cite>{{ artwork().title }}</cite
          >, {{ artwork().date }}</span
        >
        <span>{{ artwork().collection }}</span>
      </figcaption>
    </figure>
  `,
  styles: `
    :host {
      display: block;
      min-width: 0;
    }
    figure {
      margin: 0;
    }
    img {
      width: 100%;
      height: auto;
    }
    figcaption {
      display: flex;
      flex-direction: column;
      margin-top: 0.8rem;
      color: var(--caption-color, var(--muted));
      font-size: var(--size-small);
      line-height: 1.55;
    }
    .artist {
      color: var(--caption-strong, var(--ink));
    }
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ArtFigure {
  readonly artwork = input.required<Artwork>();
  readonly sizes = input('(max-width: 860px) 92vw, 40vw');
  readonly priority = input(false);

  protected readonly src = computed(() => artworkSrc(this.artwork()));
  protected readonly srcset = computed(() => artworkSrcset(this.artwork()));
}
