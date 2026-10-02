# Projektstand und Entscheidungen

Stand: 2026-10-03.

## Produkt

Das Vorbild für das erklärende Testerlebnis ist [12 Axes](https://12axes.vercel.app/) mit seinem [öffentlichen Repository](https://github.com/RomanCypherpunk/12axes). Dieses Projekt konzentriert sich vollständig auf Deutschland. Die erste Version soll politische Einstellungen erklären und mit der Bevölkerung sowie realen Wählergruppen zum Zeitpunkt einer Befragung vergleichen. Ideologie-, Länder- und Personen-Matches gehören nicht zum Umfang.

[LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) beschreibt die vorgesehene wissenschaftliche Grundlage. Zahl und Struktur der Dimensionen sind offen. Die Zahl zwölf im Repository-Namen ist keine methodische Vorgabe.

## Entscheidung zur Repository-Grundlage

Steven hat am 2026-10-03 Angular gewählt. Die Grundlage nutzt Angular 22 mit eigenständigen Komponenten, Router, strengen TypeScript- und Template-Prüfungen, SCSS und Vitest. Sie braucht aktuell keinen Server für Nutzerdaten. Die Schriften und das Kunstwerk liegen lokal; die Seite benötigt beim Aufrufen keine externen Dienste.

„Politikprofil“ ist ein Arbeitsname für die Oberfläche. Die Gestaltung orientiert sich an [Contra Labs](https://contralabs.com/): große Serifentitel, ruhige kleinere Serifentexte und klassische deutsche Kunst, bevorzugt Romantik. Details und Nachweise stehen in `design.md` und `assets.md`.

Alle elf Skills aus dem persönlichen Skills-Repository sind über die Skills CLI eingebunden. `skills.yaml` ist ihr Manifest.

Steven richtet Claude vorerst nicht ein und möchte CodeRabbit nutzen. Die Repository-Konfiguration bereitet technische PR-Reviews durch CodeRabbit vor. Sie ersetzt noch nicht die in LIFE-93 geforderten unabhängigen methodischen Erstbewertungen. Deren Verfahren, überprüfbare Review-Urteile und verbindliche Freigaberegeln werden als nächster Arbeitsschritt besprochen und umgesetzt. Die ältere Claude-Setup-Vorgabe in LIFE-93 wird in dieser Grundlage nicht ausgeführt.

## Jetzt vorhanden

- Startseite und Seite zum Projektstand, einschließlich Bild- und Schriftnachweisen.
- Lokaler Entwicklungsserver, Produktionsbuild und technische Prüfungen.
- Technische GitHub-CI und CodeRabbit-Konfiguration für spätere PRs.
- Ordner für die spätere Analyse sowie ein Git-Ausschluss für Rohdaten.

Es gibt noch keinen Fragenkatalog, keine Analyse, keine Bewertung und keine Vergleichswerte. Die Startseite kennzeichnet den Test als in Vorbereitung. Ein wissenschaftlicher Freigabeprozess ist noch nicht eingerichtet.

## Nächster Arbeitsschritt

Die Prüfregeln sollen konkret festlegen, welche Belege und Prüfberichte ein Agent liefern muss, wann ein Finding blockiert und welche Unsicherheiten oder fehlenden Abnahmen sichtbar bleiben müssen. Vor Datenanalyse oder Veröffentlichung muss auch geklärt sein, wie die unabhängigen KI-Erstbewertungen ohne das bisher vorgesehene Claude-Setup zustande kommen.
