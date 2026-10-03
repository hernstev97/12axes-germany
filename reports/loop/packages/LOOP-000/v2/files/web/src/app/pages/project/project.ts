import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ArtFigure } from '../../art/art-figure';
import { ALL_ARTWORKS, PROJECT_ARTWORK } from '../../art/artworks';

@Component({
  selector: 'app-project',
  imports: [ArtFigure, RouterLink],
  templateUrl: './project.html',
  styleUrl: './project.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Project {
  protected readonly artwork = PROJECT_ARTWORK;
  protected readonly credits = ALL_ARTWORKS;
  protected readonly status = [
    { label: 'Website', value: 'Startseite und Seite zum Projektstand vorhanden' },
    { label: 'Fragenkatalog', value: 'Noch nicht festgelegt' },
    { label: 'Dimensionen', value: 'Anzahl und Struktur offen' },
    { label: 'Analyse der ESS-Daten', value: 'Noch nicht vorhanden' },
    { label: 'Auswertung', value: 'Noch nicht vorhanden' },
    { label: 'Vergleichswerte', value: 'Noch nicht berechnet' },
    {
      label: 'Methodische Prüfungen',
      value:
        'Ein KI-Audit hat Teile des Rechercheentwurfs geprüft. Eine empirische Modellprüfung fehlt.',
    },
    { label: 'Verständlichkeit', value: 'Noch nicht mit Menschen geprüft' },
    { label: 'Methodischer Freigabeprozess', value: 'Noch nicht eingerichtet' },
    {
      label: 'Technische Prüfungen',
      value: 'Für den Code der Website eingerichtet. Eine methodische Prüfung ersetzen sie nicht.',
    },
    { label: 'Gespeicherte Antworten', value: 'Keine. Es gibt noch keine Fragen.' },
    {
      label: 'Externe Dienste',
      value:
        'Die Website bindet keine Dienste für Webanalyse, Tracking oder KI ein. Schriften und Bilder liefert sie selbst aus.',
    },
  ] as const;
}
