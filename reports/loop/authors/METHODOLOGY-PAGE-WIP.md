# Methodikseite: lokale Vorbereitung

Stand: 2026-10-03. WIP für die Integration durch Root. Autor: Codex, gpt-6.1-sol, ultra.

Arbeitsverzeichnis: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Zugewiesener Branch: `research/life-93-night-20261003`. Git wurde gemäß dem begrenzten Auftrag nicht aufgerufen; die Branchzuordnung wurde nicht eigenständig verifiziert.

## Gelesene Grundlagen

- `AGENTS.md` und `docs/project.md` im zugewiesenen Worktree.
- `docs/handbuch.md` vollständig, alle 378 Zeilen.
- `.agents/skills/unslop/SKILL.md`, auf die neuen Texte angewandt.
- Sichtbare Mustervorlage `web/src/app/pages/project/project.ts`, `.html`, `.scss` sowie `web/src/styles.scss`.
- `docs/empirie-plan-v2.entwurf.md`, `docs/abdeckung-v2.md`, `docs/messformen-v2.entwurf.md` und `docs/lizenzen.md` vollständig. Die Methodenplanung wurde als Entwurf übernommen, nicht als Datenfreigabe oder Ergebnisbeleg.
- Kurzer Memory-Registry-Abgleich zur Zuständigkeit des Handbuchs. Maßgeblich blieb das vollständig gelesene aktuelle Handbuch im Worktree.

Andere Autoren-/Reviewerberichte, Rohdateien, Header, lokale Daten, Antwortresultate, Zustand und Handoff wurden nicht gelesen. Auch der angebotene Dateieingangsbericht wurde nicht benötigt. Der aktualisierte Dateistand stammt unmittelbar aus der Sachstandssteuerung im Auftrag: vier weitere ESS-Dateien lokal bereitgestellt, keine Header-/Antwortinterpretation, v2-Zugriff weiterhin nicht freigegeben. Die vor dieser Steuerung gelesene Planfassung wurde nicht als Beleg für weiterhin fehlende Dateien übernommen.

## Geschriebener Umfang

Nur diese vier Dateien wurden geschrieben:

- `web/src/app/pages/methodology/methodology.ts`
- `web/src/app/pages/methodology/methodology.html`
- `web/src/app/pages/methodology/methodology.scss`
- dieser Bericht.

Die Komponente exportiert `MethodologyPage`, ist explizit standalone, nutzt `ChangeDetectionStrategy.OnPush` und importiert ausschließlich `RouterLink`. Selector: `app-methodology-page`. Die Klasse enthält keine UI-Logik oder Daten. Es gibt genau eine H1 mit `.page-title`, das Datum 3. Oktober 2026, einen Lead mit zwei Sätzen und sechs Dokumentabschnitte mit Inhaltsverzeichnis. Brotkrumen führen zur Startseite; alle sechs Inhaltslinks verwenden `routerLink="/methodik"` mit `fragment`.

Das Dokument nutzt das vorhandene Zwölfspaltenraster, die Dokumentseitenklassen und globale Typografie. Die SCSS-Datei enthält lediglich `:host { display: block; }` und ist 28 Bytes groß. Keine neuen Farben, Schriften, Bilder, Schaltflächen oder Gestaltungsregeln. Route, Navigation, App, Projektseite, globale Styles, Handbuch und Forschungsdateien wurden nicht verändert.

Der Fachtext behandelt getrennte Originalangaben, acht Themen einschließlich Wirtschaft/Verteilung und Demokratie/Autorität, die 43 Angaben ausschließlich als Auswahlentwurf, fünf getrennte historische ESS-Referenzen, Originalkontexte und Missing, geplante studienweise Gewichtung und gültige Nenner, Sensitivitäten und bedingte optionale Designstandardfehler. Es werden keine UI-Intervalle, Gesamtscores, Wählergruppenvergleiche oder Parteienzuordnungen angekündigt. Bekannte historische A-/B-Antworten werden nicht als unberührte Bestätigung ausgegeben. GLES-/ISSP-Wege bleiben mit ihren konkreten Zugangs- und Rechtebedingungen offen. Keine Forschung wurde bewertet oder verändert.

## Lokale Vorbereitung und Dateibelege

`pnpm exec prettier --write web/src/app/pages/methodology/methodology.ts web/src/app/pages/methodology/methodology.html web/src/app/pages/methodology/methodology.scss` endete mit Exitcode 0. Der abschließende Lauf meldete alle drei Dateien als unverändert.

Die sichtbaren HTML-Textknoten enthalten nach einfacher Leerraumzählung 688 Wörter einschließlich Titel, Brotkrumen, Datum und Inhaltsverzeichnis. Eine lokale Dateilesung lieferte folgende SHA-256-Werte nach der Formatierung:

| Datei | Bytes | SHA-256 |
| --- | ---: | --- |
| `web/src/app/pages/methodology/methodology.ts` | 366 | `c1a2819ed6486f13a28447b39ba3a0d0d57b8232da4cf80de024734117d3b317` |
| `web/src/app/pages/methodology/methodology.html` | 11984 | `94c76c3988c493e768691d113d85abbba5f7a1ea737e1eeeefb7cce32901ecd1` |
| `web/src/app/pages/methodology/methodology.scss` | 28 | `ec2c89fde913caff741baa0b0f3cf68a9acb5e85467e4f21b6c824fdad201394` |

Die Primärlinks stammen aus den gelesenen Grundlagen und der bestehenden Projektvorlage. ESS10-SC- und ESS11-DOIs wurden nur in der dort belegten Form übernommen. Für ESS5, ESS8 und ESS9 wurden keine zusätzlichen DOIs geraten. Feldzeiten, Population und Modi folgen der Themenmatrix; Editionsbindungen folgen dem Empirieentwurf. Die externen Links wurden gemäß Auftrag nicht über das Netz abgerufen. Es wurden keine vollständigen Quellentexte übernommen.

## Offene Schritte bei Root

1. Den Inhalt dieser Fassung prüfen und danach einen normalen frischen Prüfagenten mit begrenztem Kontext einsetzen. Die fachlichen Forschungs-Erstprüfungen sind davon getrennte offene Schritte.
2. Die Komponente später unter `/methodik` integrieren, einschließlich des Dokumentseitentitels und der abgestimmten Verlinkung. Die Exportklasse ist `MethodologyPage`.
3. Nach Integration die koordinierten technischen Checks und Browserprüfungen einschließlich Desktop-/Smartphone-Breiten, Sprungzielen, Tastaturfokus und Barrierefreiheit ausführen.
4. Dateistand, Versions-/Instrumentbindung und Quellenzitation bei der Integration mit dem von Root aktualisierten öffentlichen Plan abgleichen. Vor Ergebnisaussagen sind tatsächliche zulässige Analysen und die vorgesehenen getrennten Prüfungen erforderlich.

`pnpm check`, Fullcheck und Browserprüfungen wurden in diesem Teilauftrag ausdrücklich nicht ausgeführt. Keine Tests, Server, Installation, Delegation, Authentifizierungsarbeiten, Claude-Zugriffe, Git-Aktionen, neuen wissenschaftlichen Tags, Gates oder Veröffentlichungen. Diese Vorbereitung erteilt keine Forschungs-, Gestaltungs- oder Releasefreigabe. Claude-Schlusskontrolle durch Steven, menschliche Verständnistests sowie Test-/Ergebnisgestaltung und persönliche Releasefreigabe bleiben offen.
