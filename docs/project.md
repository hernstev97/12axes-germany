# Projektstand und Entscheidungen

Stand: 2026-10-03, nach der Übernahme durch Claude.

## Aktueller Stand

Am 3. Oktober 2026 hat Claude (Anthropic) den Codex-Stand `e9898fb` nach dem Nachtrag „Claude: Abschlussprüfung, Ergänzungen und Übernahme“ in LIFE-93 übernommen. Die Arbeit läuft auf dem Branch `research/life-93-claude-20261003`. Den Ausgangsstand beschreibt [reports/claude/uebernahme.md](../reports/claude/uebernahme.md).

- **Fragen.** 61 Originalfragen aus fünf ESS-Befragungen (2010 bis 2023) in acht Bereichen: 43 aus [Plan v2](empirie-plan-v2.entwurf.md), 18 aus [Plan v2.2](analyseplan-v2.2.md).
- **Vergleichswerte.** Historische Anteile je Frage und je Wählergruppe nach erinnerter Zweitstimme für die 43 v2-Fragen. Eine [unabhängige Kontrollrechnung](../reports/claude/kontrollrechnung/bericht.md) hat alle veröffentlichten Werte bis auf Rundungsfehler bestätigt. Werte, Wählergruppen und Stichprobenunsicherheit für die neuen Fragen folgen Plan v2.2.
- **Profil.** Der lokale Forschungsentwurf zeigt ein erklärendes Antwortprofil nach den [Profilregeln v1](profilregeln-v1.md): Einzelaussagen, Muster innerhalb von Originalblöcken und Querbezüge, ohne Gesamtwert und ohne Achsen.
- **Themenabdeckung.** Die [Matrix v2.2](abdeckung-v2.2.md) beschreibt 14 Bereiche. Acht sind teilweise abgedeckt. Arbeit und Rente, Gesundheit und Pflege, Wohnen, Außen- und Verteidigungspolitik, Bildung sowie Medien und Digitalpolitik haben keine oder fast keine eigene Frage. Geeignete Fragen liegen bei GESIS. Die GESIS-Nutzungsbedingungen verbieten die Verarbeitung mit KI-Systemen ohne Ausnahme. Eine Stopp-Meldung in LIFE-93 nennt Steven die Optionen.
- **Offen bei Steven.** Klärung mit GESIS, Download der ESS5- und ESS8-Designdateien, Gestaltung von Test und Ergebnis, Rubriknamen, Verständnistest mit fünf Personen, Rechte und Veröffentlichung.

Die folgenden Abschnitte dokumentieren frühere Entscheidungen. Wo sie einen älteren Stand beschreiben, ist das vermerkt.

## Produkt

Das Vorbild für das erklärende Testerlebnis ist [12 Axes](https://12axes.vercel.app/) mit seinem [öffentlichen Repository](https://github.com/RomanCypherpunk/12axes). Dieses Projekt konzentriert sich vollständig auf Deutschland. Die erste Version soll ein thematisch breites Politikprofil tragen und politische Einstellungen erklären. Vergleiche mit Befragten und historischen Wählergruppen benötigen jeweils eine geeignete, getrennt nachvollziehbare Referenz. Ideologie-, Länder- und Personen-Matches gehören nicht zum Umfang.

[LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) beschreibt die vorgesehene wissenschaftliche Grundlage. Zahl und Struktur der Dimensionen sind offen. Die Zahl zwölf im Repository-Namen ist keine methodische Vorgabe.

## Entscheidung zur Repository-Grundlage

Steven hat am 2026-10-03 Angular gewählt. Die Grundlage nutzt Angular 22 mit eigenständigen Komponenten, Router, strengen TypeScript- und Template-Prüfungen, SCSS und Vitest. Sie braucht aktuell keinen Server für Nutzerdaten. Schrift und Gemälde liegen lokal; die Seite benötigt beim Aufrufen keine externen Dienste.

Die Gestaltung orientiert sich an [Contra Labs](https://contralabs.com/): große Serifentitel, ruhige Flächen und klassische deutsche Kunst, bevorzugt Romantik. Verbindliche Regeln stehen in `handbuch.md`, Nachweise in `assets.md`.

## Name und überarbeitete Gestaltung

Steven hat am 2026-10-03 entschieden, dass das Projekt vorerst „12 Axes Deutschland“ heißt. Der frühere Arbeitsname „Politikprofil“ entfällt in Oberfläche und Dokumentation. Intern heißen Paket, Angular-Projekt und Build-Ordner (`web/dist/politikprofil`) noch `politikprofil`. Der Name lehnt sich an [12 Axes](https://12axes.vercel.app/) an, legt aber keine zwölf Dimensionen fest. Die Projektseite erklärt das. Die Lizenz von 12 Axes behält dem Autor unter anderem das Zwölf-Achsen-Modell, Fragen, Texte und Gestaltung vor; nichts davon wird übernommen. Eine Abstimmung des Namens mit dem Autor von 12 Axes ist im Repository nicht dokumentiert; ob sie stattfinden soll, entscheidet Steven.

Am selben Tag hat Steven die erste Gestaltung überarbeiten lassen. Sie soll neutraler und offizieller wirken, ohne den Stil aufzugeben: Libre Baskerville als einzige Schrift, wechselnde Gemälde der deutschen Romantik statt eines einzelnen Bildes, die Bundesflagge beim Namen und sachliche Texte ohne direkte Anrede. Die Fußzeile stellt klar, dass die Seite kein Angebot einer Behörde oder Partei ist.

Alle elf Skills aus dem persönlichen Skills-Repository sind über die Skills CLI eingebunden. `skills.yaml` ist ihr Manifest.

Historisch, Stand vor dem Nachtrag vom 3. Oktober 2026: Steven richtet Claude vorerst nicht ein und möchte ausschließlich CodeRabbit nutzen. Am 2026-10-03 hat er bestätigt: Die methodische Freigabe bleibt offen; auch ein zusätzlicher Review-Auftrag an eine andere Modellfamilie wird vorerst nicht vorbereitet. CodeRabbit kann technische und inhaltliche Findings liefern. Die in LIFE-93 geforderten getrennten methodischen Erstbewertungen werden dadurch nicht ersetzt. Die ältere Claude-Setup-Vorgabe wird in diesem Arbeitsschritt nicht ausgeführt.

Steven hat inzwischen einen ESS-Account und die CSV-Datei lokal bereitgestellt. Dateiname, interne globale Metadaten und Header passen zu ESS11 Ausgabe 4.2. Die Datei liegt im ausgeschlossenen Rohdatenordner; ihre Prüfsumme ist erfasst. Beim damaligen Dateieingang wurden noch keine Antwortdaten analysiert. Downloadbedingungen und vollständiger Import werden gesondert dokumentiert. Der [Dateieingangsbericht](../reports/phasen/00-dateieingang-2026-10-03.md) nennt Umfang und Grenzen der technischen Prüfung.

## Produktauftrag vor der Übernahme durch Claude

Steven hat die erforderliche Breite im [Nachtrag vom3.Oktober2026](auftrag-life-93-breite-2026-10-03.md) ausdrücklich präzisiert. Wirtschaft/Verteilung und Demokratie/politischeAutorität müssen untersucht werden; daneben weitere unterschiedliche Sachbereiche substanziell erschließen. Die enge historische Teilmodulfassung erfüllt dieses Hauptproduktziel nicht. Fragenbestände/Instrumente aus GLES, weiteren ESS-Runden und gegebenenfallsISSP mit ihren eigenen Referenzen prüfen. Themen sind keine automatisch beschlossenen Dimensionen; begründete Einzelpräferenzen und formative Ansätze sind neben latenten Dimensionen möglich.

Aktuell gilt der [Erweiterungsplanv2](erweiterungsplan-v2.entwurf.md) als ergebnisblinder Quellen-/Auswahlentwurf ohne neue Datenfreigabe. Die alte Analysefolge ist angehalten. Historische Forschung, Verträge und Tags bleiben erhalten; frühere Dateneinsicht wird vom Koordinator getrennt dokumentiert. KeineFertigstellung allein aus dem engen Teilmodul. Claude kontrolliert später auf StevensVeranlassung; konkrete Design-/Verständnis-/Releasefreigaben bleiben offen.

## Historischer Repository-Aufbau

Die folgenden Abschnitte bewahren den frühen Aufbau-/Auftragsstand. Sie sind keine aktuellen Behauptungen zum Forschungsfortschritt; maßgeblich sind der Breitennachtrag und der versionierte neue Plan.

### Damals vorhanden

- Startseite und Seite zum Projektstand, einschließlich Bild- und Schriftnachweisen. Die Startseite zeigt eine wechselnde Auswahl von Gemälden.
- Lokaler Entwicklungsserver, Produktionsbuild und technische Prüfungen.
- Technische GitHub-CI und CodeRabbit-Konfiguration für spätere PRs.
- Ordner für die spätere Analyse sowie ein Git-Ausschluss für Rohdaten.
- Erster Entwurf der [Prüfregeln](pruefregeln.md), [Review-Vorgaben](reviews/README.md) und [Analysevorbereitung](analyseplan.md).
- Öffentliche [Datenrecherche](datenlage.md), [Lizenzakte](lizenzen.md), [Belegregister](belegregister.md) und Dokumentversionen mit Hashes in [quellen.json](quellen.json).

Damals gab es noch keinen Fragenkatalog, keine Analyse, keine Bewertung und keine Vergleichswerte. Den heutigen Stand beschreibt der Abschnitt „Aktueller Stand“. Die Startseite kennzeichnet den Test weiterhin als in Vorbereitung. Die Prüfregeln liegen als Arbeitsfassung vor; fünf Codex-Subagents haben eine partielle Quellen-, Inhalts-, Methoden- und Nachprüfbarkeitsprüfung im [KI-Audit](../reports/audit-recherche/README.md) durchgeführt. Getrennte Itembewertungen anderer Modellfamilien, automatische Forschungsgates und die empirischen Abnahmen fehlen weiterhin.

## Nächster Arbeitsschritt (historisch)

Damals hieß es: Als Nächstes können der vollständige deutsche Fragenbestand und die Literatur zu Themenabdeckung und Prüfverfahren recherchiert werden. Endgültige Auswahl und empirische Untersuchung warten auf die erforderlichen Gegenprüfungen und den vollständig begründeten, öffentlich eingefrorenen Analyseplan. Fehlende Review-Abnahmen bleiben sichtbar. Der erste Teilbericht steht unter [reports/phasen/00-recherche-2026-10-03.md](../reports/phasen/00-recherche-2026-10-03.md).

Die Korrekturen und offenen Anforderungen des Audits stehen in [analyseanforderungen.md](analyseanforderungen.md). Der vollständige Fragenkatalog und Deutschland-Themenrahmen bleiben die nächste Arbeit; das Audit liefert keine fertig geprüften Dimensionen.

## Dauerhafter Gesamtauftrag und Arbeitsloop

Der [Auftrag vom 2026-10-03](auftrag-life-93-2026-10-03.md) umfasst nun alle Phasen. Der [Arbeitsloop](arbeitsloop.md) und [gespeicherte Zustand](../reports/loop/state.json) führen Aufgaben, abhängige Stopps, tatsächliche Reviews und verifizierte Branch-Pushes. Die alte Umfangsbegrenzung auf ausschließlich Recherche und CodeRabbit gilt für den neuen Auftrag nicht mehr. Vorgeschriebene Claude-Prüfungen werden dadurch nicht als erfüllt erklärt.

Das neue main mit Claudes UI und Handbuch wurde im eigenen Worktree zusammengeführt. Die unveränderte Übernahme ist im [Integrationsbeleg](../reports/loop/000-main-integration.json) dokumentiert. Zwei unabhängige Reviews bestätigten Integrität und Erhaltung; ihre Status-/Textbefunde werden in einer eigenen Korrekturfassung bearbeitet.

Claude Code ist bereits installiert und angemeldet. Der erste beschränkte Zugriffstest scheiterte am Anbieter-Sitzungslimit; [Protokoll](../reports/loop/claude-access.json). Kein Review oder Itemurteil fand dabei statt. Github-Reviewworkflow, Branchschutz und Setup-Abnahme bleiben offen. Quellenbestand, Theorie und Methodenparameter werden in getrennten Entwürfen erarbeitet. Noch keine empirische ESS-Analyse.

## Forschungsvorbehalt nach der Breitenkorrektur (Stand vor der Übernahme)

Die älteren Abschnitte beschreiben den jeweiligen damaligen Stand. Mittlerweile wurden A und B des historischen Neunermoduls tatsächlich gerechnet; genaue Einsicht und Halt sind im [Zugriffsbericht](../reports/loop/b-access-disclosure-20261003.json) erhalten. Sie sind keine unangetastete Bestätigung für Erweiterungen und kein fertiges breites Hauptprodukt. Aktuell entsteht ein eigener breiter v2-Vertrag vor neuen Antworten; [Empirieentwurf](empirie-plan-v2.entwurf.md), [Themenmatrix](abdeckung-v2.md) und [Arbeitszustand](../reports/loop/state.json) sind maßgeblich. Kein Claude-Zugang ist Voraussetzung der Hauptarbeit; die von Steven veranlasste Schlusskontrolle bleibt ausstehend.

## Vorbereitete Kontrollfassung vom 3. Oktober 2026

2026-10-03T16:36:47.884766+00:00: Der zuvor als entstehend beschriebene breite Plan wurde separat festgeschrieben und ausgeführt. Die breite Forschungs-UI, öffentliche Themen-/Gruppenberichte und konkrete Vorführung sind vorbereitet. Aktuelle Grenzen, tatsächliche Reproduktion und die noch von Steven veranlasste Kontrolle stehen in [Reproduktion](reproduktion-life93-v2.md), [Claude-Checkliste](claude-schlusskontrolle-v2.md) und [gespeichertem Zustand](../reports/loop/state.json). Ein öffentlicher freigegebener Test oder menschliche Abnahme wird daraus nicht abgeleitet.
