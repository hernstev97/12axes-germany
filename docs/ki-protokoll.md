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

## 2026-10-03: KI-Audit mit tatsächlichen Subagents

Steven beauftragte ausdrücklich fünf isolierte Erstprüfer sowie einen sechsten Juror. Die ersten fünf wurden tatsächlich über `collaboration.spawn_agent` mit `fork_turns: none` gestartet. Wegen vier verfügbarer aktiver Slots einschließlich Hauptagent liefen sie in zwei Wellen. Alle erhielten dieselbe gehashte Ausgangsfassung und das live gelesene Issue. Berichte wurden erst nach Abschluss aller fünf inhaltlich zusammengeführt.

Zugängliche Eltern-Laufzeit: GPT-6.1-Sol, `gpt-6.1-sol`, Reasoning `ultra`, ohne Modelloverride. Interne Versionen und nicht zugängliche Anbieterregeln unbekannt. Getrennte Gespräche und Lektüreaufträge, gemeinsame Modellfamilie und gemeinsame Dateirechte; kein Nachweis unabhängiger interner Vorgaben. Die genaue jeweilige Werkzeugnutzung steht in den Erstberichten. Wortlaut aller tatsächlichen Agent-Aufträge, Modelle, Zeiten und Hashes: [agent-protokoll.json](../reports/audit-recherche/agent-protokoll.json).

Der Hauptagent prüfte die Versionshinweise zusätzlich im T3-Browser und die Lizenztrennung am Original-HTML; gespeicherte aktuelle Quellenbelege haben Zeitpunkt und Hash. Kein ESS-Login, keine Antwortanalyse oder Entblindung. Reviewer 3 führte ausdrücklich synthetische Gegenrechnungen aus. Sie sind kein Test der Projektpipeline. Historische technische Belege wurden lokal registriert; alte Laufzeiten werden durch neue Prüfungen nicht rückwirkend bestätigt.

Anforderungen und offene Evidenz bleiben getrennt von tatsächlich ausgeführten Prüfungen. Der Auditabschluss einschließlich Juror und Wiederholungsprüfungen wird im [Auditbericht](../reports/audit-recherche/README.md) festgehalten. Kein PR, Push, Merge, Tag oder Deployment.

## 2026-10-03: Überarbeitung der Gestaltung

- Agent: Claude Code über T3 Code.
- Modellkennung laut Laufzeit: `claude-opus-5-5` (Kontext 1M). Interne Modellversion und nicht zugängliche Anbieter-Vorgaben sind unbekannt.
- Werkzeuge: Shell und Dateibearbeitung, Web-Recherche, Lesen von LIFE-93 über Linear, lokaler Headless-Browser (Playwright mit Chromium) für Referenz und Prüfung, ImageMagick. Workflows mit Teilagenten desselben Modells recherchierten Gemälde, Provenienz und Flaggenfarben, schrieben drei getrennt erzeugte Textfassungen, führten sie in einer Jury zusammen und prüften Texte, Gestaltung, Barrierefreiheit, Code und Dokumentation. Übereinstimmung zwischen Teilagenten desselben Modells ist kein Beleg.
- Umfang: Name, Gestaltung, Texte und Bilder der Website, Schriftpaket (Libre Baskerville statt Fraunces und Newsreader), Gestaltungs- und Texthandbuch, zugehörige Dokumentation. Keine Datenanalyse, keine methodischen Erstbewertungen.
- PR: keiner; lokale Arbeit.

Stevens Auftrag im Wortlaut:

> ich möchte, dass du die webseite überarbeitest. zur info: das hier (https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) ist der task an dem grade von gpt 6.1 sol gearbeitet wird. die webseite hat es grundlegend schon aufgebaut und der allgemeine stil soll auch so bleiben. also großer wert auf serifen-ästhetik legen und romantische deutsche kunst. ich möchte es aber auch etwas "offizieller" (?) aussehen lassen. also es sieht grade EXTREM vibe coded aus. es sind viele gpt-isms drin. die schriftart, die vielen kleinen fast schon esotherisch wirkenden all-caps sätze, die wordings. es soll neutraler sein und nicht so ... ja .. esotherisch. außerdem möchte ich dass nicht nur ein gemälde zu sehen ist sondern immer wieder andere. ich denke als schriftart würde ich gerne libre baskerville verwenden. die deutschlandflagge soll auch zu sehen sein (am besten oben beim namen des projekts) und das projekt soll auch einfach nur (erstmal) 12 axes Deutschland heißen. bitte gestalte das einmal richtig konsequent durch und bleibe aber beim gleichen spirit.
>
> achso und https://contralabs.com/ war ursprünglich die design/spirit-inspiration

Stevens anschließender Handbuchauftrag im Wortlaut:

> du hast hier scheinbar extrem viel arbeit in das redesign gesteckt. baue daraus ein handbuch anhand dessen neue agents in zukunft die seite gestalten und texte schreiben müssen. die ganze UI/UX soll anhand dieses handbuchs geführt werden können

## 2026-10-03: Abschluss von Gestaltung und Handbuch

- Agent: Codex über T3 Code, `gpt-6.1-sol`, Reasoning `max`.
- Umfang: Prüfung des Chatkontexts, des Redesigns und des Handbuchs; Ergänzung der Browserbefehle, der Schriftgrößenskala und der Ausnahmen für Bild-Platzhalterfarben; Aktualisierung der Prüfberichte. Keine Änderung der Gestaltung oder des Produktumfangs.
- Prüfungen: `pnpm check` und `git diff --check` bestanden. Eigene Desktop-Stichprobe in der T3-Vorschau und visuelle Prüfung der vorhandenen Screenshots; der Größenwechsel der Vorschau brach wiederholt ab. Einzelheiten und Grenzen stehen in `validation.md`. Keine wissenschaftliche Abnahme.

Stevens Abschlussauftrag im Wortlaut:

> dann mach das noch und schiebs dann direkt zu main

## 2026-10-03: Arbeitsloop, erste Integration und Entwürfe

main 87eb549 wurde im isolierten Worktree zusammengeführt; alte Recherche und Audit bleiben erhalten. LOOP-000-v1 wurde von zwei tatsächlichen unabhängigen Codex-Subagents geprüft. Drei Regel-/Statusfehler sowie ein doppelter Befund wurden angenommen und mit unveränderter Ausgangsfassung dokumentiert. Nachprüfung v2 läuft; kein positives Gesamturteil behauptet. Ein eigener Browserbefund L000-A01 korrigiert die pauschale Lizenzbegründung des Rohdatenausschlusses. Original-Disclaimer erneut abgerufen.

Drei separate Autoren arbeiten an Originalfragen, konkurrierender Theorie und Methoden. Der Theorieentwurf liegt vor; alle Item-/Modellentscheidungen bleiben offen. Codex-Laufzeit GPT-6.1-Sol/ultra, interne Revision/Vorgaben unbekannt; keine andere Modellfamilie fingiert. Tatsächliche Aufträge und Dateien stehen in reports/loop/agents.json und den Autoren-/Reviewberichten.

Vorhandener Claude-CLI ist angemeldet. Der technische Test ohne Tools scheiterte am gemeldeten Sitzungslimit (Reset 06:10 Uhr Berlin); keine wissenschaftliche Prüfung durchgeführt. Keine Limitumgehung, keine System-/Kontoeinstellungen verändert.

Die aktuelle lokale Browserroutine bestand für drei vorhandene Projektseiten, fünf Breiten, axe, Netzwerk/Speicher, Tastatur und Galerie. Eine Folgeprüfung des Handbuchguards scheiterte an Semikolons in zwei korrigierten Sätzen. Die Fehlfassung bleibt im Nachprüfpaket erhalten; nach Abschluss der unabhängigen Berichte wird gezielt korrigiert. Keine Ergebnisberechnung oder Testdatenübertragung existiert bzw. wurde freigegeben.

## 2026-10-03: Nachprüfungen, zweite Reparaturrunde und tatsächlicher Claude-Protokollfall

Fünf FOUNDATION-Erstberichte und je zwei v2/v3-Nachberichte sind abgeschlossen und unverändert erhalten. Zwölf ursprüngliche Findings wurden vollständig angenommen. N-F01 wurde in Runde2 anhand der Originalfragen korrigiert und unabhängig bestätigt. Ein zusätzlicher historischer Pfad-/Hash-Verweisfehler ist separat angenommen und in v4 nachvollziehbar gebunden. Ein neuer unbeteiligter Juror und eine formale Nachprüfung laufen; es gibt keine wissenschaftliche Phasenfreigabe. Der PREP-Mindestbelegfehler ist in Runde2 korrigiert:20eigeneAjv-Fälle und der volle Appcheck wurden ausgeführt; noch nicht beide Nachprüfungen sind abgeschlossen.

Zwei echte frische Subagents prüften SOFTWARE-001 unabhängig anhand von Originalquellen, eigenen R-Läufen und Schwellenorakeln. Die native Stratumgrenze und die engen numerischen Befunde sind bestätigt. Der ursprüngliche Conda-Außenwrite bleibt NICHT_BESTANDEN. Die neue IOCTL-Beschreibungsbeanstandung ist vollständig angenommen; eine getrennte Autorenkorrektur wurde ohne Numerikänderung ausgeführt. Unabhängige Nachprüfung folgt.

Nach dem Providerreset war der Zugriff tatsächlich erfolgreich. Ein neuer Claude-Printprozess (CLI2.1.288, konkret angefordert und durch Laufzeitmetadaten belegt:claude-opus-5-5, zusätzlich Haiku4.5 beobachtet) bearbeitete CASE-P01 in frischem Kontext ohne Tools. Absichtlich fehlendes Manifest, Originalbelege und Menschenantworten führten zu BLOCKIERT. Auftrag, ursprünglicher Modelltext, exakter Prompthash, Metadaten und tatsächliche Ajv-Ausführung sind erhalten. Die Skill wurde explizit im Prompt übergeben. Der Fall ist kein Loadernachweis, erforderlicher Forschungsreview, Itemersturteil, Workflow oder Menschentest. Interne Modellrevisionen und Vorgaben bleiben unbekannt; die Codexagents laufen weiter als GPT-6.1-Sol/ultra.

Für die öffentliche Ergänzung der52A/B-Frageidentitäten arbeitet ein getrennter Autor mit eigenen Dateien. Vorhandene Forschungsfassungen bleiben während der Reviews unverändert. Dauerhafter Stand, Findings, vollständige Startaufträge und Pushbelege stehen unter reports/loop/. Keine Rohantworten oder A/B-/Partei-/LR-Werte wurden ausgewertet. Kein main-Push, Merge oder Deployment.

## 2026-10-03: Fortsetzung, Designmetadaten und Item-Ersturteile

Der Fortsetzungsnachtrag ersetzt die Claude-Zugangsvoraussetzung; seitdem keine weiteren Claude-Aufrufe. Zwei getrennte Codex-Agents bewerteten alle 296 Originalidentitäten ohne Autorenauswahl oder fremde Ersturteile. Berichte/Initial-CSVs bleiben unverändert, eine separate Text-Errata korrigiert eine unbelegte Zahl. Gleiche Modellfamilie und Shared-FS-Rechte lassen gemeinsame Fehler zu. Kappa 0.8954479226455914 beschreibt allein Dokumentenurteile; reproduzierbar mit `python pipeline/item_agreement.py`.

Nach gezielter technischer v2-Nachprüfung (89 synthetische Assertions) führte ausschließlich der Koordinator den begrenzten privaten Designmetadatenimport aus. Der erste CLI-Aufruf scheiterte vor Import am fehlenden eigenen `data/local`-Ordner. Nach dessen Anlage mit 0700 gelang der zweite Aufruf. Unveränderliche gehashte CSV-Bytes werden tokenisiert; ausschließlich neun freigegebene Metadatenfelder werden interpretiert. Keine Personenkennung, Einstellung, Wahl-, Links-rechts- oder Gruppenantwort wurde ausgewählt. Öffentlicher Bericht: [00-designmetadaten](../reports/phasen/00-designmetadaten-2026-10-03.json); private Ausgabe 0600. Reale 2420 DE-Fälle, 25 Strata, 500 PSUs; in zwei Strata nur je zwei PSUs. Das widerlegt die bisherige min4-Splitbedingung für das gesamte deutsche Design. Kein empirischer Messbefund.

Autoren bereiten getrennte Quellen-/Konstrukt-, Split-, Gruppen- und ordinale Softwareverträge vor. Der konkrete Plan ist weiterhin Entwurf. Der neue A-Import verweigert ohne zwei gehashte Übergangsurteile und verifizierte öffentliche Plan-/Erwartungstags jeden Zugriff; der tatsächliche Vorabaufruf endete mit festem Gatefehler, ohne Import. Synthetische Tests mit absichtlich unlesbaren B/C-/Wahl-/LR-/ID-Tokens prüfen die positive Auswahl. Keine Präregistrierung, A/B-Ziehung oder Antwortanalyse aus diesen Tests ableiten. Laufzeit Codex GPT-6.1-Sol/ultra; unbekannte interne Versionen und Vorgaben bleiben unbekannt.

## 2026-10-03: Planfreeze und tatsächliche A-Rechnung

Die beiden Vor-A-Ersturteile und gezielte PE-M01-Nachprüfung erlaubten den begrenzten Planfreeze. Plan-/Erwartungstags6466767 vor tatsächlichem A-Zugriff öffentlich verifiziert. Ausschließlich Root führte privaten Import und A-Rechnung aus. Festgelegte Auswahl M2/H-ZF, Belege und Grenzen im [A-Entscheid](../reports/phasen/01-a-entscheidung.md). Getrennter Exportreview fand AE-01; genaue Schema-/Pin-Korrektur in Runde1 unabhängig angenommen, anschließend tatsächlicher Export kontrolliert. Originalberichte unverändert. B/C und politische Vergleichsvariablen bleiben ungeöffnet. Neue B/FULL-/Normautoren verwendeten nur erfundene Antworten; Synthetik ist keine Empirie. Beide Codex-Rollen gehören derselben Modellfamilie an; keine Claude-Aufrufe seit dem Fortsetzungsnachtrag.
