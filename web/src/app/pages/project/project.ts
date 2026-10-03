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
    {
      label: 'Fragenkatalog',
      value: 'Breiter Katalog in Entwicklung. Neun frühere ESS-Fragen bleiben ein Teilmodul.',
    },
    { label: 'Dimensionen', value: 'Anzahl und Struktur offen' },
    {
      label: 'Analyse und Erweiterung',
      value: 'Früheres Teilmodul untersucht. Erweiterung erhält einen eigenen Plan.',
    },
    { label: 'Auswertung des breiten Websiteprofils', value: 'Noch nicht vorhanden' },
    { label: 'Vergleichswerte', value: 'Noch nicht berechnet' },
    {
      label: 'Methodische Prüfungen',
      value:
        'Frühere KI-Prüfungen zu Quellen und Methoden vorhanden. Breite Fassung noch nicht geprüft.',
    },
    { label: 'Verständlichkeit', value: 'Noch nicht mit Menschen geprüft' },
    { label: 'Methodischer Freigabeprozess', value: 'Dokumentiert. Erforderliche Abnahmen offen.' },
    {
      label: 'Technische Prüfungen',
      value: 'Für den Code der Website eingerichtet. Eine methodische Prüfung ersetzen sie nicht.',
    },
    { label: 'Gespeicherte Antworten', value: 'Keine. Die Website erhebt keine Antworten.' },
    {
      label: 'Externe Dienste',
      value:
        'Die Website bindet keine Dienste für Webanalyse, Tracking oder KI ein. Schriften und Bilder liefert sie selbst aus.',
    },
  ] as const;
}
