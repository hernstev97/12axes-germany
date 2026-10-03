import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ArtFigure } from '../../art/art-figure';
import { ArtGallery } from '../../art/art-gallery';
import { BASIS_ARTWORK, HOME_GALLERY } from '../../art/artworks';

@Component({
  selector: 'app-home',
  imports: [ArtFigure, ArtGallery, RouterLink],
  templateUrl: './home.html',
  styleUrl: './home.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Home {
  protected readonly gallery = HOME_GALLERY;
  protected readonly basisArtwork = BASIS_ARTWORK;
}
