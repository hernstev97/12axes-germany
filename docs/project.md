# Projektstand und Entscheidungen

Stand: 2026-10-03.

## Produkt

Das Vorbild für das erklärende Testerlebnis ist [12 Axes](https://12axes.vercel.app/) mit seinem [öffentlichen Repository](https://github.com/RomanCypherpunk/12axes). Dieses Projekt konzentriert sich vollständig auf Deutschland. Die erste Version soll politische Einstellungen erklären und mit der Bevölkerung sowie Wählergruppen zum Zeitpunkt einer Befragung vergleichen. Ideologie-, Länder- und Personen-Matches gehören nicht zum Umfang.

[LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) beschreibt die vorgesehene wissenschaftliche Grundlage. Zahl und Struktur der Dimensionen sind offen. Die Zahl zwölf im Repository-Namen ist keine methodische Vorgabe.

## Entscheidung zur Repository-Grundlage

Steven hat am 2026-10-03 Angular gewählt. Die Grundlage nutzt Angular 22 mit eigenständigen Komponenten, Router, strengen TypeScript- und Template-Prüfungen, SCSS und Vitest. Sie braucht aktuell keinen Server für Nutzerdaten. Schrift und Gemälde liegen lokal; die Seite benötigt beim Aufrufen keine externen Dienste.

Die Gestaltung orientiert sich an [Contra Labs](https://contralabs.com/): große Serifentitel, ruhige Flächen und klassische deutsche Kunst, bevorzugt Romantik. Verbindliche Regeln stehen in `handbuch.md`, Nachweise in `assets.md`.

## Name und überarbeitete Gestaltung

Steven hat am 2026-10-03 entschieden, dass das Projekt vorerst „12 Axes Deutschland“ heißt. Der frühere Arbeitsname „Politikprofil“ entfällt in Oberfläche und Dokumentation. Intern heißen Paket, Angular-Projekt und Build-Ordner (`web/dist/politikprofil`) noch `politikprofil`. Der Name lehnt sich an [12 Axes](https://12axes.vercel.app/) an, legt aber keine zwölf Dimensionen fest. Die Projektseite erklärt das. Die Lizenz von 12 Axes behält dem Autor unter anderem das Zwölf-Achsen-Modell, Fragen, Texte und Gestaltung vor; nichts davon wird übernommen. Eine Abstimmung des Namens mit dem Autor von 12 Axes ist im Repository nicht dokumentiert; ob sie stattfinden soll, entscheidet Steven.

Am selben Tag hat Steven die erste Gestaltung überarbeiten lassen. Sie soll neutraler und offizieller wirken, ohne den Stil aufzugeben: Libre Baskerville als einzige Schrift, wechselnde Gemälde der deutschen Romantik statt eines einzelnen Bildes, die Bundesflagge beim Namen und sachliche Texte ohne direkte Anrede. Die Fußzeile stellt klar, dass die Seite kein Angebot einer Behörde oder Partei ist.

Alle elf Skills aus dem persönlichen Skills-Repository sind über die Skills CLI eingebunden. `skills.yaml` ist ihr Manifest.

Steven richtet Claude vorerst nicht ein und möchte CodeRabbit nutzen. Die Repository-Konfiguration bereitet technische PR-Reviews durch CodeRabbit vor. Sie ersetzt noch nicht die in LIFE-93 geforderten unabhängigen methodischen Erstbewertungen. Deren Verfahren, überprüfbare Review-Urteile und verbindliche Freigaberegeln werden als nächster Arbeitsschritt besprochen und umgesetzt. Die ältere Claude-Setup-Vorgabe in LIFE-93 wird in dieser Grundlage nicht ausgeführt.

## Jetzt vorhanden

- Startseite und Seite zum Projektstand, einschließlich Bild- und Schriftnachweisen. Die Startseite zeigt eine wechselnde Auswahl von Gemälden.
- Lokaler Entwicklungsserver, Produktionsbuild und technische Prüfungen.
- Technische GitHub-CI und CodeRabbit-Konfiguration für spätere PRs.
- Ordner für die spätere Analyse sowie ein Git-Ausschluss für Rohdaten.

Es gibt noch keinen Fragenkatalog, keine Analyse, keine Bewertung und keine Vergleichswerte. Die Startseite kennzeichnet den Test als in Vorbereitung. Ein wissenschaftlicher Freigabeprozess ist noch nicht eingerichtet.

## Nächster Arbeitsschritt

Die Prüfregeln sollen konkret festlegen, welche Belege und Prüfberichte ein Agent liefern muss, wann ein Finding blockiert und welche Unsicherheiten oder fehlenden Abnahmen sichtbar bleiben müssen. Vor Datenanalyse oder Veröffentlichung muss auch geklärt sein, wie die unabhängigen KI-Erstbewertungen ohne das bisher vorgesehene Claude-Setup zustande kommen.
