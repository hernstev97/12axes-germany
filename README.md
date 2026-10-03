# 12 Axes Deutschland

Forschungsprototyp für einen Test zu politischen Einstellungen in Deutschland. „12 Axes Deutschland“ ist ein vorläufiger Name. Die Zahl zwölf legt keine Dimensionen fest.

## Stand

Stand: 3. Oktober 2026. Auftrag ist [LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent).

| Teil                        | Stand                                                                                                                                                                                                                                                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fragen                      | Umgesetzt: 62 unveränderte Originalfragen aus fünf Befragungen des European Social Survey (ESS5, ESS8, ESS9, ESS10 Self-completion, ESS11; 2010 bis 2023), geordnet nach acht Bereichen. 43 Fragen stammen aus Plan v2, 19 aus [Plan v2.2](docs/analyseplan-v2.2.md).                                                         |
| Historische Vergleichswerte | Umgesetzt für die 43 v2-Fragen: gewichtete Anteile der Antwortkategorien in Deutschland je Befragung und für Wählergruppen nach erinnerter Zweitstimme (ESS5, ESS8, ESS9). Unabhängig nachgerechnet ([Kontrollrechnung](reports/claude/kontrollrechnung/bericht.md)). Für die 19 neuen Fragen in Vorbereitung nach Plan v2.2. |
| Stichprobenunsicherheit     | Geplant nach Plan v2.2 für Befragungen mit vollständigem Stichprobendesign (ESS9, ESS10, ESS11). Für ESS5 und ESS8 fehlen die Designdateien.                                                                                                                                                                                  |
| Erklärendes Profil          | Umgesetzt im lokalen Forschungsentwurf nach den [Profilregeln](docs/profilregeln-v1.md): Einzelaussagen, Muster innerhalb von Originalblöcken, Querbezüge. Kein Gesamtwert, keine Achsen.                                                                                                                                     |
| Themenabdeckung             | [Matrix für 14 Bereiche](docs/abdeckung-v2.2.md). Acht Bereiche teilweise abgedeckt, sechs ohne oder fast ohne eigene Frage. Der Weg über GESIS-Daten ist gesperrt, bis die KI-Klausel der GESIS-Nutzungsbedingungen geklärt ist.                                                                                             |
| Website                     | Öffentliche Seiten: Startseite, Projektstand, Methodik. Der Fragen- und Ergebnisentwurf läuft nur lokal mit `pnpm dev:research`. Es gibt keinen öffentlichen Teststart.                                                                                                                                                       |
| Prüfungen                   | KI-Reviews durch Codex- und Claude-Agenten, dokumentiert unter `reports/loop/` und `reports/claude/`. Keine Begutachtung durch Fachleute, kein Verständnistest mit Menschen, keine Freigabe durch Steven.                                                                                                                     |

Das Projekt ist weder validiert noch wissenschaftlich geprüft und kann keine Neutralität garantieren.

## Lokal starten

Node 24 und pnpm 11 sind erforderlich. Die verwendete Node-Version steht in `.node-version`.

```sh
pnpm install --frozen-lockfile
pnpm dev            # öffentliche Seiten, http://127.0.0.1:4311
pnpm dev:research   # zusätzlich der lokale Forschungsentwurf unter /forschungsentwurf, Port 4314
```

```sh
pnpm check
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'
```

`pnpm check` prüft Formatierung, die mechanischen Regeln des Handbuchs, das Review-Schema und die Typen, führt die UI-Tests aus und erstellt den Produktionsbuild. Die GitHub Action `CI` führt dieselben technischen Prüfungen aus. Wissenschaftliche Freigaben sind darin nicht enthalten.

Die Auswertungen brauchen die lokal bereitgestellten ESS-Dateien unter `data/raw/`. Sie sind nicht im Repository. Die Reproduktion beschreibt [docs/reproduktion-life93-v2.md](docs/reproduktion-life93-v2.md), den Rechenweg v2.2 [docs/analyseplan-v2.2.md](docs/analyseplan-v2.2.md).

## Aufbau

| Pfad              | Inhalt                                                                                |
| ----------------- | ------------------------------------------------------------------------------------- |
| `web/`            | Angular 22, Standalone Components, zoneless, SCSS, Vitest                             |
| `docs/`           | Aufträge, Pläne, Themenabdeckung, Profilregeln, Handbuch, Belege, KI-Protokoll        |
| `data/`           | Fragenkataloge, Analyseverträge, veröffentlichte zusammengefasste Vergleichswerte     |
| `data/raw/`       | lokale ESS-Rohdaten, von Git ausgeschlossen                                           |
| `pipeline/`       | Auswertungen in Python und R; `pipeline/v22/` für Plan v2.2                           |
| `reports/`        | Berichte, Prüfurteile und Agentenaufträge; `reports/claude/` für die Claude-Übernahme |
| `scripts/`        | Prüfungen, Berichtsbau und Bildverarbeitung                                           |
| `.agents/skills/` | Skills aus dem persönlichen Skills-Repository                                         |

Schrift und Gemälde werden lokal ausgeliefert. Die Website bindet keine Analyse-, Tracking- oder KI-Dienste ein und speichert oder überträgt keine Antworten.

## Skills und Review

`skills.yaml` hält die Auswahl der Skills fest. Zum erneuten Synchronisieren auf einem Rechner mit Zugang zum zentralen Repository:

```sh
SKILLS_REPO=/pfad/zum/skills-repository skills sync
```

`.coderabbit.yaml` bereitet deutschsprachige technische und inhaltliche PR-Reviews vor. Eine lokale Konfigurationsdatei belegt noch keinen erfolgreichen Review-Lauf.

Aktuelle Entscheidungen stehen in [docs/project.md](docs/project.md). Gestaltung, Texte und Bilder regelt das [Handbuch](docs/handbuch.md).
