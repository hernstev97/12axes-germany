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
      value:
        '62 Originalfragen aus fünf historischen ESS-Studien in acht Bereichen. Sechs weitere Bereiche ohne oder fast ohne eigene Frage.',
    },
    { label: 'Dimensionen', value: 'Keine gemeinsamen Messdimensionen in der aktuellen Fassung' },
    {
      label: 'Analyse und Erweiterung',
      value:
        'Plan v2 und Analyseplan v2.2 versioniert gesichert. Auswertung ausgeführt, jede Befragung getrennt.',
    },
    {
      label: 'Ergebnisansicht',
      value:
        'Beschreibung je Frage, Muster in Fragenblöcken und Querbezüge. Nur lokal im Forschungsentwurf. Gestaltung nicht freigegeben.',
    },
    {
      label: 'Vergleichswerte',
      value:
        '59 historische Einzelreferenzen und 96 historische Wählergruppenreferenzen aus ESS5, ESS8 und ESS9, jeweils mit 95-%-Bereich. Keine aktuelle Bevölkerungsnorm.',
    },
    {
      label: 'KI-Prüfungen',
      value:
        'Codex hat Plan v2.2 und die Ergebnisse vor dem Export in KI-Reviews begrenzt geprüft. Claude hat den früheren Codex-Stand nachgeprüft. Gemeinsame Fehler bleiben möglich.',
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
