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
    { label: 'Fragenkatalog', value: 'Neun Originalfragen vorgeschlagen. Noch nicht freigegeben.' },
    { label: 'Dimensionen', value: 'Anzahl und Struktur offen' },
    {
      label: 'Analyse der ESS-Daten',
      value: 'Stichprobenmetadaten geprüft. Noch keine politischen Antworten ausgewertet.',
    },
    { label: 'Auswertung', value: 'Noch nicht vorhanden' },
    { label: 'Vergleichswerte', value: 'Noch nicht berechnet' },
    {
      label: 'Methodische Prüfungen',
      value: 'Zwei getrennte KI-Erstbewertungen liegen vor. Eine empirische Modellprüfung fehlt.',
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
