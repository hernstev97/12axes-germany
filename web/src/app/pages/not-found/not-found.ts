import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ArtFigure } from '../../art/art-figure';
import { NOT_FOUND_ARTWORK } from '../../art/artworks';

@Component({
  selector: 'app-not-found',
  imports: [ArtFigure, RouterLink],
  templateUrl: './not-found.html',
  styleUrl: './not-found.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class NotFound {
  protected readonly artwork = NOT_FOUND_ARTWORK;
}
