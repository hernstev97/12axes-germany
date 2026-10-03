# KI-Protokoll

## 2026-10-03: Repository-Grundlage

- Agent: Codex über T3 Code.
- Modellkennung laut Laufzeit: `gpt-6.1-sol`, Reasoning `max`. Eine konkrete interne Modellversion und nicht zugängliche Anbieter-Vorgaben sind unbekannt.
- Lokale CLI: `codex-cli 0.153.4`.
- Werkzeuge: Shell und Dateibearbeitung, Web-Recherche in Primärquellen, Lesen von LIFE-93 über Linear, T3-Browser für Referenz und lokale Prüfung. Keine anderen Agents eingesetzt.
- Umfang: Angular-Grundlage und Gestaltung, alle vorhandenen persönlichen Skills per CLI, technische CI und CodeRabbit-Konfiguration. Keine Datenanalyse oder methodischen Erstbewertungen.
- PR: keiner; lokale Arbeit.

Stevens Auftrag im Wortlaut:

> ich glaube ich hätte da gerne eine angular webapp. und vom design her inspiriert von dieser webseite https://contralabs.com/
>
> ich stelle mir einfach vor: schöne große und mutige serifenschrift für überschriften und fragen, kleinere sanfte serifen für texte, bilder klassicher deutscher kunst (vielleicht gezielt vorallem aus der romantik?) für stellen an denen bilder passen (vermutlich eher auf der startseite als während eines tests)... so in diesem stil. das nur schonmal als richtung für die grundlage des repos. und dann zieh dir auch bitte die ganzen skills aus dem skills repo über die skills cli in das projekt. alle bitte.
>
> claude richte ich erstmal nicht ein. dafür habe ich coderabbit.
>
> sobald die grundlage des repos steht starten wir mit den prüfregeln

Die Umsetzung folgt diesem Auftrag. CodeRabbit bleibt zunächst technischer PR-Review; die methodische Unabhängigkeit und die Prüfregeln sind offene Arbeit.

Prüfergebnisse: `pnpm check` bestanden, CodeRabbit-Schema validiert, alle elf Skills bytegenau mit ihrer Quelle verglichen. Desktop- und Smartphone-Ansichten samt Navigation und Tastaturbedienung wurden im Browser geprüft. Der ergänzende lokale Browserlauf nutzte Playwright, nachdem die gemeinsame T3-Vorschau keinen erreichbaren Automation-Host mehr meldete. Ergebnisse und Grenzen stehen in `validation.md`. Kein gehosteter CI- oder CodeRabbit-Lauf und keine wissenschaftliche Abnahme durchgeführt.

## 2026-10-03: Beginn von Prüfregeln und Quellenrecherche

- Agent: Codex über T3 Code, `gpt-6.1-sol`. Die Laufzeit meldete zunächst Reasoning `medium`, später `max`; keine interne Modellversion bekannt. Keine weiteren Agents eingesetzt, keine unabhängige Erstbewertung durchgeführt.
- Auftrag: „okay dann fangen wir an.“ Ergänzend: vorerst nur CodeRabbit, methodische Freigabe offen. ESS-Account im laufenden Gespräch als inzwischen vorhanden gemeldet.
- Ausgangspunkt: lokaler Foundation-Commit `1a7b0c3`, Branch `research/life-93-methodology`. Kein PR, Push oder Deployment.
- Gelesener Auftrag: LIFE-93, `updatedAt 2026-10-02T22:07:24.510Z`. Die neuere Review-Entscheidung ist in `entscheidungen.md` dokumentiert; der Issue selbst wurde nicht geändert.
- Werkzeuge: Linear lesen, Websuche und Primärquellen, T3-Browser für öffentliche ESS-Metadaten, Shell/HTTP für öffentliche Dokumentation, Poppler für PDF-Text und visuelle Prüfung, lokale Dateibearbeitung. Bei Web-Fetch-Fehlern wurden öffentliche Dokumente direkt abgerufen. Keine ESS-Anmeldung und keine stellvertretende Akzeptanz von Bedingungen.
- Skills: `unslop` für die Texte, `pdf` für ausgewählte Originalseiten und Seitenzuordnung. Kein vollständiger Fragebogen-/Literaturreview behauptet.

### Zugriff und Exposition

Keine ESS-Rohdaten heruntergeladen oder geöffnet; keine empirische Verteilung selbst berechnet. Öffentlich gelesen wurden deutsche Erhebungsmetadaten, Zielpopulation, Stichprobendesign, Wahlreferenz und dokumentierte Parteikodierungen. Automatische Dokumentorientierung zeigte auch politische Beschreibungen anderer Länder; daraus wurden keine Parteipositionen für das Modell abgeleitet.

Ein Suchtreffer zur Hauptdatei zeigte bereits eine öffentliche aggregierte Darstellung zur Variable `ipfrulea`. Dies war eine unbeabsichtigte Exposition gegenüber einem Beispiel aus dem Portal, kein Rohdatenzugriff. Die Darstellung wurde nicht zur Item-/Dimensionsauswahl verwendet. Die Analysis-Ansicht wurde nicht geöffnet. Es gibt noch keinen Split und keine technische Abschirmung von B. Spätere Blindheitsbehauptungen dürfen diesen Zugriff nicht unterschlagen.

Anfänglich gefunden: Gewichtungsleitfaden V1.1 und ältere Zitations-/Releaseangaben. Nach Live-Portalprüfung dokumentiert: V1.2, Hauptdatei 4.2, Codebook 4.1 und Länderbericht 4.0. Versionsunterschiede sind ausdrücklich erfasst. Quellkopien und gerenderte Seiten liegen temporär außerhalb von Git; der öffentliche Katalog enthält Links/Hashes statt vollständiger PDFs.

### Ergebnis und offene Prüfungen

Erstellt: Arbeitsfassungen der Regeln, des Analyseplans und Review-Formats; Daten-/Lizenzrecherche, Belegregister, Quellenkatalog und Teilbericht. CodeRabbit-Konfiguration auf diese Regeln ausgerichtet. Keine endgültigen Items, Dimensionen oder Modellparameter festgelegt; keine Analyse-/Modell-Tags erzeugt.

Technische Abschlussprüfungen werden im [Phasenbericht](../reports/phasen/00-recherche-2026-10-03.md) mit tatsächlichem Ergebnis festgehalten. Fundstellen-Gegenprüfung, CodeRabbit-Lauf, andere Modellfamilie, methodische Freigabe und Verständnistest bleiben offen. KI-Übereinstimmung und Autor-Selbstprüfung werden nicht als Peer Review bezeichnet.

## 2026-10-03: lokaler Dateieingang

Steven meldete: „die datei liegt jetzt drin“. Gefunden wurde `data/raw/ess11-ed4.2/ESS11e04_2.csv`. Ein lokales Python-Skript erfasste Größe und SHA-256 und prüfte den Git-Ausschluss. Es las den CSV-Header sowie ausschließlich `essround`, `edition` und `proddate` aus dem ersten Datensatz als globale Metadaten aus. Das Skript verarbeitete dafür den ersten Datensatz lokal; dessen Antworten oder Personenfelder wurden nicht ausgegeben. Es wurde kein vollständiger Analyseimport durchgeführt.

Der Agent erhielt nur Dateimetadaten, Spaltenzahl und Angaben über vorhandene Spalten. Keine Antwortverteilungen, Fall-/Gruppenauszählung, Deutschland-Selektion, A/B-Teilung, Scores oder Modellwahl. Dieser Metadatenzugriff fand vor Plan-Freigabe statt und wird ausdrücklich protokolliert. Der Datei-Hash allein belegt keine Übereinstimmung mit dem Originaldownload.

Ein lokaler Beleg liegt unter `data/local/ess11-file-arrival-2026-10-03.json`. Ein Bericht ohne Rohdaten steht unter [reports/phasen/00-dateieingang-2026-10-03.md](../reports/phasen/00-dateieingang-2026-10-03.md). Die ursprüngliche Entwurfsfassung wurde vor Statusänderungen gegen ihre Hashes geprüft und lokal in `outputs/research-snapshots/2026-10-03-initial-draft/` erhalten. Das Arbeitsmanifest führt ihre vorherigen Hashes weiter; dies ist keine Präregistrierung.

Agent: Codex/T3 Code, `gpt-6.1-sol`, Reasoning `max` laut Laufzeit. Keine weiteren Agents und keine unabhängige Gegenprüfung eingesetzt. Der Analysestart bleibt offen.
