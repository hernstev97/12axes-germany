# Projektstand und Entscheidungen

Stand: 2026-10-03.

## Produkt

Das Vorbild für das erklärende Testerlebnis ist [12 Axes](https://12axes.vercel.app/) mit seinem [öffentlichen Repository](https://github.com/RomanCypherpunk/12axes). Dieses Projekt konzentriert sich vollständig auf Deutschland. Die erste Version soll politische Einstellungen erklären und mit der Bevölkerung sowie realen Wählergruppen zum Zeitpunkt einer Befragung vergleichen. Ideologie-, Länder- und Personen-Matches gehören nicht zum Umfang.

[LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) beschreibt die vorgesehene wissenschaftliche Grundlage. Zahl und Struktur der Dimensionen sind offen. Die Zahl zwölf im Repository-Namen ist keine methodische Vorgabe.

## Entscheidung zur Repository-Grundlage

Steven hat am 2026-10-03 Angular gewählt. Die Grundlage nutzt Angular 22 mit eigenständigen Komponenten, Router, strengen TypeScript- und Template-Prüfungen, SCSS und Vitest. Sie braucht aktuell keinen Server für Nutzerdaten. Die Schriften und das Kunstwerk liegen lokal; die Seite benötigt beim Aufrufen keine externen Dienste.

„Politikprofil“ ist ein Arbeitsname für die Oberfläche. Die Gestaltung orientiert sich an [Contra Labs](https://contralabs.com/): große Serifentitel, ruhige kleinere Serifentexte und klassische deutsche Kunst, bevorzugt Romantik. Details und Nachweise stehen in `design.md` und `assets.md`.

Alle elf Skills aus dem persönlichen Skills-Repository sind über die Skills CLI eingebunden. `skills.yaml` ist ihr Manifest.

Steven richtet Claude vorerst nicht ein und möchte ausschließlich CodeRabbit nutzen. Am 2026-10-03 hat er bestätigt: Die methodische Freigabe bleibt offen; auch ein zusätzlicher Review-Auftrag an eine andere Modellfamilie wird vorerst nicht vorbereitet. CodeRabbit kann technische und inhaltliche Findings liefern. Die in LIFE-93 geforderten getrennten methodischen Erstbewertungen werden dadurch nicht ersetzt. Die ältere Claude-Setup-Vorgabe wird in diesem Arbeitsschritt nicht ausgeführt.

Steven hat inzwischen einen ESS-Account und die CSV-Datei lokal bereitgestellt. Dateiname, interne globale Metadaten und Header passen zu ESS11 Ausgabe 4.2. Die Datei liegt im ausgeschlossenen Rohdatenordner; ihre Prüfsumme ist erfasst. Noch keine Antwortdaten analysiert. Downloadbedingungen und vollständiger Import werden gesondert dokumentiert. Der [Dateieingangsbericht](../reports/phasen/00-dateieingang-2026-10-03.md) nennt Umfang und Grenzen der technischen Prüfung.

## Jetzt vorhanden

- Startseite und Seite zum Projektstand, einschließlich Bild- und Schriftnachweisen.
- Lokaler Entwicklungsserver, Produktionsbuild und technische Prüfungen.
- Technische GitHub-CI und CodeRabbit-Konfiguration für spätere PRs.
- Ordner für die spätere Analyse sowie ein Git-Ausschluss für Rohdaten.
- Erster Entwurf der [Prüfregeln](pruefregeln.md), [Review-Vorgaben](reviews/README.md) und [Analysevorbereitung](analyseplan.md).
- Öffentliche [Datenrecherche](datenlage.md), [Lizenzakte](lizenzen.md), [Belegregister](belegregister.md) und Dokumentversionen mit Hashes in [quellen.json](quellen.json).

Es gibt noch keinen Fragenkatalog, keine Analyse, keine Bewertung und keine Vergleichswerte. Die Startseite kennzeichnet den Test als in Vorbereitung. Die Prüfregeln liegen als Arbeitsfassung vor; unabhängige methodische Bewertungen, automatische Forschungsgates und wissenschaftliche Abnahmen sind noch nicht eingerichtet.

## Nächster Arbeitsschritt

Als Nächstes können der vollständige deutsche Fragenbestand und die Literatur zu Themenabdeckung und Prüfverfahren recherchiert werden. Endgültige Auswahl und empirische Untersuchung warten auf die erforderlichen Gegenprüfungen und den vollständig begründeten, öffentlich eingefrorenen Analyseplan. Fehlende Review-Abnahmen bleiben sichtbar. Der erste Teilbericht steht unter [reports/phasen/00-recherche-2026-10-03.md](../reports/phasen/00-recherche-2026-10-03.md).
