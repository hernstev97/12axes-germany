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
    {
      label: 'Website',
      value: 'Informationsseiten vorhanden. Der Test ist nicht öffentlich verfügbar.',
    },
    {
      label: 'Fragenkatalog',
      value: '43 Originalangaben aus fünf historischen ESS-Studien in acht Themenrubriken',
    },
    { label: 'Dimensionen', value: 'Keine gemeinsamen Messdimensionen in der aktuellen Fassung' },
    {
      label: 'Analyse und Erweiterung',
      value: 'Plan v2 versioniert gesichert. Fünf getrennte Einzelstudienläufe ausgeführt.',
    },
    { label: 'Breiter Themenbericht', value: 'Als Forschungsfassung gesichert' },
    {
      label: 'Vergleichswerte',
      value: '42 historische Einzelreferenzen. Keine aktuelle Bevölkerungsnorm.',
    },
    {
      label: 'KI-Prüfungen',
      value:
        'Zwei getrennte Codex-Rollen haben die historischen Einzelreferenzen begrenzt geprüft. Gleiche Modellfamilie. Gemeinsame Fehler möglich.',
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
