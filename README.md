# 12 Axes Deutschland

Angular-Webapp für einen erklärenden Politiktest mit einem mehrdimensionalen Einstellungsprofil und Vergleichen zu Wählergruppen in Deutschland. „12 Axes Deutschland“ ist ein vorläufiger Name; die Zahl zwölf legt keine Dimensionen fest.

Aktuell steht die technische und gestalterische Grundlage. Es gibt eine Startseite und eine Seite zum Projektstand. Die öffentliche Recherche und ein erster Entwurf der wissenschaftlichen Prüfregeln liegen vor. Fragen, Auswertung und Vergleichsdaten sind noch nicht umgesetzt; die methodische Freigabe ist offen.

## Lokal starten

Node 24 und pnpm 11 sind erforderlich. Die verwendete Node-Version steht in `.node-version`.

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Die App läuft auf <http://127.0.0.1:4311>.

```sh
pnpm check
```

Dieser Befehl prüft Formatierung, die mechanischen Regeln des Handbuchs (`scripts/check-handbuch.mjs`) und die Typen, führt die UI-Tests aus und erstellt den Produktionsbuild. Die GitHub Action heißt `CI` und führt dieselben technischen Prüfungen aus. Wissenschaftliche Freigaben sind darin noch nicht enthalten.

Der Stand der lokalen und visuellen Prüfung ist in [docs/validation.md](docs/validation.md) festgehalten.

## Aufbau

| Pfad              | Inhalt                                                            |
| ----------------- | ----------------------------------------------------------------- |
| `web/`            | Angular 22, Standalone Components, zoneless, SCSS, Vitest         |
| `docs/`           | Projektentscheidungen, Handbuch, Asset-Nachweise und KI-Protokoll |
| `scripts/`        | Handbuch-Prüfung und Bildverarbeitung                             |
| `data/raw/`       | Lokale Rohdaten, von Git ausgeschlossen                           |
| `pipeline/`       | Platz für die spätere Analyse                                     |
| `model/`          | Platz für versionierte Modelle                                    |
| `reports/`        | Platz für spätere Analyse- und Prüfberichte                       |
| `.agents/skills/` | Alle Skills aus dem persönlichen Skills-Repository                |

Schrift und Gemälde werden lokal ausgeliefert. Die App bindet keine Analyse-, Tracking- oder KI-Dienste ein und speichert derzeit keine Antworten.

## Skills und Review

Alle elf verfügbaren Skills wurden mit der persönlichen Skills CLI installiert. `skills.yaml` hält die Auswahl fest. Zum erneuten Synchronisieren auf einem Rechner mit Zugang zum zentralen Repository:

```sh
SKILLS_REPO=/pfad/zum/skills-repository skills sync
```

`.coderabbit.yaml` bereitet deutschsprachige technische und inhaltliche PR-Reviews vor. CodeRabbit muss Zugriff auf dieses Repository haben; eine lokale Konfigurationsdatei belegt noch keinen erfolgreichen Review-Lauf. Es bleibt vorerst der einzige Review-Dienst. Die vorgeschriebenen unabhängigen methodischen Erstbewertungen und Freigaben sind offen.

Die Arbeitsfassung steht in [docs/pruefregeln.md](docs/pruefregeln.md), das Finding-Format in [docs/reviews/README.md](docs/reviews/README.md). [docs/analyseplan.md](docs/analyseplan.md) nennt den Ablauf und die noch fehlenden Entscheidungen vor Datenanalyse. Originalquellen, Nutzungsrechte und der recherchierte Datenkandidat sind über [docs/belegregister.md](docs/belegregister.md) nachvollziehbar. Ein erfolgreicher technischer Check gibt diesen Forschungsstand nicht methodisch frei.

Auftrag: [LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent). Aktuelle Entscheidungen stehen in [docs/project.md](docs/project.md). Gestaltung, Texte und Bilder regelt das [Handbuch](docs/handbuch.md).
