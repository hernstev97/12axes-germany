# WEBSITE-BREADTH-002/v1: unabhängiger Erstbericht

Prüfer: Codex, gpt-6.1-sol, ultra. Datum: 3. Oktober 2026. Prüfung von 2026-10-03T12:22:06.547043+00:00 bis 2026-10-03T12:29:39.240503+00:00, UTC; lokal entspricht UTC + zwei Stunden.

Zwei inhaltliche Präzisierungen sind nötig: Die Website sollte die vorgesehenen KI-Prüfer ausdrücklich benennen und die noch fehlende Websiteauswertung von der bereits erfolgten historischen Analyse unterscheiden. Hinzu kommt eine kleine, nicht blockierende Begriffsabweichung. Keine belegte zusätzliche politische Zuschreibung im dritten Durchgang gefunden. Das ist ein Befund zu diesem Textpaket, keine Neutralitätsbescheinigung.

## Prüffassung und Grenzen

Arbeitsverzeichnis ausschließlich `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Vorgegebener Branch: `research/life-93-night-20261003`; wegen des ausdrücklich ausgeschlossenen Git-Einsatzes nicht mit Git abgefragt. Kein anderer Checkout wurde verändert. Das ausdrücklich angegebene unslop-Skill wurde am Pfad im Hauptcheckout nur gelesen.

Gegenstand sind vollständig `home.html` (139 Zeilen), `project.html` (289 Zeilen) und die sichtbaren Statusstrings in `project.ts` (Datei vollständig gelesen, 46 Zeilen). Die sechs übrigen Manifestpins dienen als Sachbelege und Regeln, nicht als zusätzliche Änderungsgegenstände. `AGENTS.md`, `docs/project.md`, das vollständige `docs/handbuch.md` (378 Zeilen) und das angegebene unslop-Skill wurden gelesen. Aus dem Kernvertrag wurden für Sachprüfungen Quellen, die neun Originalformulierungen, Antwortdefinitionen und Fundstellen projiziert. Eingebettete frühere Itemurteile und Scorevorschläge wurden nicht als Urteil übernommen.

Keine anderen neuen Autoren- oder Reviewerberichte gelesen; einzige gelesene Autorenquelle ist der ausdrücklich gepinnte `ESS-CORE-VERSION-binding.md`. Keine Konsultation oder Delegation an andere Agenten. Kein state/handoff, keine Dateien aus `data/raw/` oder `data/local/`, keine politischen Rohantworten oder Personenkennungen. Keine ESS-Analyse oder Ergebnisinterpretation. Das Feld `knownResults` des Zugriffsbelegs wurde aus der inhaltlichen Lektüre ausgeschlossen. Die öffentlichen UUIDs in den API-Belegen bezeichnen Studien-, Datei- und Variablenmetadaten, keine Personen.

Drei getrennte Durchgänge wurden durchgeführt:

1. Tatsachen, Versionen, Belegumfang und heutige Auftragsgeltung; abgeschlossen um 12:26:41 UTC.
2. Erneute Textlektüre gegen Handbuch und unslop; abgeschlossen um 12:27:28 UTC. Wortsuche war nur eine Hilfe. Satzanfängliches „Sie“ bezeichnet in den betreffenden Sätzen Studien beziehungsweise Erhebung und ist keine direkte Anrede.
3. Erneute Prüfung auf politische Zuschreibung, Themenauswahl und Benennung; abgeschlossen um 12:27:54 UTC.

Die exakten Zeitstempel stehen in `outputs/loop/website-breadth-review/20261003T122206Z/pass-record.json`. Keine technische Prüfung, kein pnpm, keine Installation, kein Claude-Zugriff, kein Websitebrowser, kein Deployment, Commit, Push oder Merge. Die Ansicht gezielt gerenderter Original-PDF-Seiten ist eine Quellenprüfung und keine Browserprüfung der Website. Design, Bildprovenienz, Netzverhalten der gesamten App und Release wurden nicht abgenommen.

## Findings

Schweregrade: P2 bezeichnet eine inhaltliche Mehrdeutigkeit mit möglicher Fehlvorstellung beim Lesen; P3 eine kleine redaktionelle Abweichung. Kein P0- oder P1-Befund.

### WB-001 · P2 · Art und Umfang der Prüfungen eindeutig benennen

**Betroffene Aussage:** `web/src/app/pages/project/project.html:219–220`: „Zwei getrennte fachliche Prüfer beurteilen die wesentlichen Forschungsübergänge.“ Ergänzend `project.ts:30–31` und `home.html:126–127`: Quellen- und Methodenprüfungen werden ohne KI-Zusatz als vorhanden bezeichnet.

**Beleg:** `AGENTS.md` sieht an den wesentlichen Forschungsübergängen zwei getrennte Codex-Prüfagenten vor. Der Breitennachtrag, Abschnitt „Arbeitsfolge und Prüfungen“, behält diese Rollen bei und weist ausdrücklich auf gemeinsame Fehlerquellen hin. Handbuch 7.2 und 7.3 unterscheiden KI-Prüfungen von Begutachtung durch Fachleute. `project.html:193–197` benennt zwar die beiden neuen Rechercheautoren als Codex-Agenten; das identifiziert die späteren Prüfer nicht ausdrücklich.

**Befund:** „Fachliche Prüfer“ kann als menschliche fachwissenschaftliche Begutachtung gelesen werden. Auch die isoliert lesbaren Statuszeilen verraten die Art der früheren Prüfungen nicht. Die Pflichtformel und der spätere Hinweis auf offene Prüfungen reduzieren das Risiko, beseitigen diese Mehrdeutigkeit aber nicht. Es wird hier keine ausdrücklich behauptete erfolgte Fachbegutachtung unterstellt.

**Minimale nötige Korrektur:** „Zwei getrennte Codex-Prüfagenten prüfen die wesentlichen Forschungsübergänge.“ In den beiden Statuszeilen „Frühere KI-Prüfungen zu Quellen und Methoden vorhanden. Breite Fassung noch nicht geprüft.“ Der Hinweis auf dieselbe Modellfamilie und gemeinsame mögliche Fehler sollte auch eindeutig für diese Prüfungen gelten. Keine zusätzliche Prüfung oder andere Modellfamilie aus diesem Finding ableiten.

### WB-002 · P2 · Fehlende Websiteauswertung auf ihren Geltungsbereich begrenzen

**Betroffene Aussage:** `web/src/app/pages/project/project.ts:27`: „Auswertung: Noch nicht vorhanden“.

**Beleg:** `project.html:182–190` beschreibt eine bereits erfolgte Auswertung des früheren Entwicklungsteils und Prüfungsteils. `home.html:118–119` nennt vorhandene Teilmodulanalysen. Der gepinnte Zugriffsbeleg dokumentiert, dass B geöffnet und gerechnet wurde; sein Lauf liegt am 3. Oktober 2026 zwischen 11:57:55 und 11:58:06 UTC. Er hält zugleich die aktuelle Fortsetzung an. Seine Datums- und Umfangsangaben sind ein gelesener Koordinatorbeleg; keine selbst wiederholte oder numerisch nachgeprüfte Analyse.

**Befund:** Ohne Bezugswort kann die Statuszeile wie die Behauptung wirken, es habe überhaupt noch keine Auswertung gegeben. Gemeint ist offenbar die noch fehlende Auswertung des breiten Websiteprofils. Diese Lesart ist plausibel, steht aber nicht in der Zeile. Die historische Analyse und die fehlende Produktfunktion brauchen getrennte Bezeichnungen.

**Minimale nötige Korrektur:** Bezeichnung „Auswertung des breiten Websiteprofils“, Wert „Noch nicht vorhanden“. Die vorhandene Zeile „Analyse und Erweiterung“ und der historische Zugriffsabsatz können erhalten bleiben. Keine historischen Resultate hinzufügen oder freigeben.

### WB-003 · P3 · Nicht blockierende Handbuchterminologie

**Betroffene Aussage:** `web/src/app/pages/project/project.html:224`: „keine erfundene gemeinsame Achse“.

**Beleg:** Handbuch 7.3 nennt Teile des Profils „Dimension“ und verwendet „Achse“ nur im Namen.

**Befund und minimale Korrektur:** „keine erfundene gemeinsame Dimension“. Der Satz behauptet schon jetzt keine vorhandene Dimension; dies ist eine redaktionelle Angleichung, kein wissenschaftlicher Befund und kein Grund, das Paket allein deshalb zu blockieren. „Antwortskalen“ für Originalantwortmöglichkeiten und wissenschaftlich begründete unterschiedliche Messformen müssen dadurch nicht zu latenten Dimensionen umbenannt werden.

## Sachbefunde im geprüften Umfang

**Aktueller Auftrag und Breite.** Maßgeblich ist der gepinnte Breitennachtrag, nicht der ältere enge Forschungsstand. Er hält die alte B-/FULL-/Norm-/Gruppenfolge an, verlangt einen eigenen v2-Plan vor abhängigen Analysen und benennt das Neunermodul als unzureichend für das Hauptprodukt. Die Texte bilden diese Grenze ab. Wirtschaft/Verteilung und Demokratie/politische Autorität stehen ausdrücklich in `home.html:77–80` und `project.html:41–51`, mit weiteren Sachbereichen. Keine fertige Breite, feste Fragenzahl, zwölf Dimensionen oder allgemeine Drei-Item-Regel wird versprochen. Einzelpräferenzen und andere begründete Messformen bleiben möglich. Die Informationsseite braucht keinen konkreten Analyseplan oder vollständigen Quellenkatalog, um diesen Auftrag korrekt darzustellen.

`docs/project.md` enthält ausdrücklich historische Abschnitte sowie noch ältere negative Analyseangaben. Für den aktuellen Ausführungsstand wurden sie nicht gegen den neueren Breitennachtrag und den Zugriffsbeleg ausgespielt. Die erneute Claude-Kontrolle wird nur als späterer, offener Schritt beschrieben; daraus entsteht kein Setup- oder Zugriffsauftrag. Live-Agentenzustand und Fortschritt anderer neuer Entwürfe wurden entsprechend der Lesesperren nicht geprüft.

**ESS-Fassungen und Fundstellen.** Der [Länderbericht Ausgabe 4.0](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_country_documentation_report_e04.pdf#page=79), PDF-/Druckseiten 79–80, bestätigt den genannten deutschen Erhebungszeitraum und persönliche Interviews. Seite 79 wurde zusätzlich als Bild gelesen; Seite 80 als Text. Die [offiziellen Studienmetadaten](https://ess.sikt.no/en/study/412db4fe-c77a-4e98-8ea4-6c19007f551b), unabhängig über die öffentliche API abgerufen, bestätigen die Referenzpopulation ab 15 Jahren in Privathaushalten unabhängig von Staatsangehörigkeit. Die Trennung von Wahlberechtigten und der ungeprüften Websiteübertragung ist korrekt begrenzt.

Der [deutsche Fragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), Titel und PDF-/Druckseiten 13, 15 und 16, sowie das [Listenheft](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf), Titel und PDF-Seiten 14, 17–20, wurden gezielt gelesen. Diese acht Item-/Karten-Seiten wurden zusätzlich als Bilder angesehen. Die Website beschreibt tatsächlich die neun vorhandenen Fragen. Familiäre Scham bleibt hypothetisch, wahrgenommene Zuwanderungsfolgen werden nicht als gemessene tatsächliche Folgen ausgegeben. Das Wirtschaftswahrnehmungsitem zum Zuwanderungsthema wird nicht als schon erreichte allgemeine Wirtschaftsabdeckung verkauft.

Das [Codebook](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf) trägt auf dem Titel Ausgabe 4.1. Die einschlägigen Textabschnitte PDF63–68/Druck62–67 wurden gelesen, kein vollständiger visueller Codebook-Review. Fragebogen, Listenheft, Codebook und ESS-Disclaimer haben beim frischen Download dieselben SHA-256 wie die jeweiligen Quellenangaben im Kernvertrag. Kein umfassendes Routing- oder Quellenzellenzertifikat wird daraus abgeleitet.

[DOI und Dateiportal](https://doi.org/10.21338/ess11e04_2) binden die integrierte Datei an Ausgabe 4.2. Die öffentliche [Portal-API](https://api.nsd.no/graphql) liefert `ESS11e04_2`, kuratierte Version 4.2 und Metadatenversion 179. Für alle neun Felder wurden ausschließlich öffentliche Definitionen abgefragt. Dateizugehörigkeit, gültige Codes, Missingcodes und Locations stimmen mit dem Vertrag überein; die substanziellen englischen Antwortlabels stimmen mit den gelesenen 4.1-Codebookstellen überein. Jede abgefragte Codeliste ist vollständig paginiert. Damit ist die Websiteaussage zur öffentlichen Definitionsbindung in diesem Umfang nachvollziehbar. Tatsächliches CSV-Verhalten, beobachtete Antworten, Modell, Scores und numerische Gültigkeit wurden nicht geprüft.

**Lizenz- und Quellenlinks.** Die [ESS-Bedingungen](https://www.europeansocialsurvey.org/contact/disclaimer), Abschnitt „Conditions of use“, bestätigen die separate Lizenzierung von Daten und Dokumentation. Die Website erklärt kein pauschales gesetzliches Rohdatenverbot und lässt die konkrete spätere Veröffentlichungsprüfung offen. Keine rechtsfachliche Freigabe. Der [Original-Lizenztext von Libre Baskerville](https://raw.githubusercontent.com/impallari/Libre-Baskerville/master/OFL.txt) bestätigt SIL OFL 1.1; nach fehlgeschlagenem UTF-8-Lesen mit CP1252 gelesen, Originalbytes unverändert. ISSP-Bezeichnung und Original-12-Axes-Link waren erreichbar. Die statische 12-Axes-Seite zeigt ihren Zwölf-Achsen-Titel; ihre interaktive Auswertung wurde nicht geprüft. Der direkte GLES-Abruf ergab 403; er belegt keine fehlende Studie oder dauerhafte Nichterreichbarkeit. Keine vollständige Quelleninventarisierung, keine Live-Prüfung sämtlicher GitHub-Verzweigungslinks und kein Audit der dynamisch eingefügten Bildnachweise.

**Politische Interpretation, dritter Durchgang.** Das Textpaket setzt die Themenrubriken nicht mit genehmigten Dimensionen gleich, schreibt Gruppen keine gegenwärtige Parteiposition zu und gibt keine Wahlempfehlung. Es benennt eigene Auswahl- und Interpretationsverantwortung und getrennte Studienreferenzen. Die Benennung des alten Moduls entspricht dem belegten Frageninhalt und behauptet weder moralische Richtigkeit einzelner Antworten noch eine vollständige Gleichstellungs- oder Migrationsmessung. Keine zusätzliche notwendige Korrektur belegt. Auswahlfairness der späteren Items, Vollständigkeit des künftigen Profils und politische Neutralität können diese Texte nicht nachweisen.

## Abrufe, Erhaltung und Übergabe

Originalabrufe vom 3. Oktober 2026 liegen ausschließlich im eigenen ignorierten Evidenzordner. Acht anfängliche GETs zwischen 12:23:05 und 12:23:06 UTC erhielten HTTP200. Drei Portal-/DOI-HTMLs waren nur dieselbe JavaScript-Hülle; die inhaltlichen Behauptungen wurden deshalb mit der öffentlichen Metadaten-API geprüft. Sechs GraphQL-POSTs zwischen 12:23:29 und 12:25:26 UTC erhielten HTTP200: vier reine Schemaabfragen, ein Datei-/Studienmetadatenabruf und ein auf die neun Definitionen begrenzter Variablenabruf. Keine Antwortdaten- oder Analyseabfrage. Beim letzten Lauf nur öffentliche Codewerte und Labels, keine Antwortzahlen.

Vier ergänzende GETs zwischen 12:25:48 und 12:25:49 UTC: ISSP, 12 Axes und Schriftlizenz HTTP200, GLES HTTP403. Die separate Web-Zugriffsschicht meldete für den ESS-Disclaimer HTTP502 und lieferte keine nutzbar dargestellten PDF-Screenshots. Die direkte GET-Schicht erhielt HTTP200 für den Disclaimer; die Original-PDF-Seiten wurden lokal gerendert und angesehen. Diese Unterschiede werden nicht als vollständig bestandene Webprüfung ausgegeben. Einzelne anfangs abgeschnittene Toolausgaben wurden für die relevanten Stellen nochmals gezielt gelesen. Ein Darstellungshelfer für Schema-Typen wurde korrigiert; die Originalantworten blieben erhalten. Requests, Originalresponses, UTC-Zeiten, HTTP, Bytezahlen und SHA-256 stehen in den eigenen Abrufprotokollen.

Manifest-SHA-256: `a5fbc04d9d43a8efca531f0f0a036576c53bbfe9f06281190344d677677c2092`. Alle neun direkten Pins stimmen vor und nach der Prüfung mit dem Manifest überein:

| Pin | SHA-256 laut Manifest | vor / nach |
| --- | --- | --- |
| `web/src/app/pages/home/home.html` | `55107959368b6fb3852b0bcfd700aa68c646983aea60d2c98ea63c03ae13860e` | identisch / identisch |
| `web/src/app/pages/project/project.html` | `1deaf4e4a032ec3fe7d49ca977369095fa4e9bf472629134498bc67edade814f` | identisch / identisch |
| `web/src/app/pages/project/project.ts` | `535fcda9e63b70d2f5bf482ef744270ca56dba9e767220d2b0c74d84af6ca830` | identisch / identisch |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` | identisch / identisch |
| `docs/auftrag-life-93-breite-2026-10-03.md` | `d0a059efb9de65aec1be25b3c2d5fac3bcb61cb57b0d7af8e7d8f64ecb1fd5ed` | identisch / identisch |
| `reports/loop/b-access-disclosure-20261003.json` | `eb0c1c2dfcffb704e8f3c060730822027b0ae8a9d7668c949b2233c20936d290` | identisch / identisch |
| `data/item-core-v1.json` | `01dee3b72d72c074e2bf913b4791e8016acce591de3fffa120ab40eae2fb1b3e` | identisch / identisch |
| `reports/loop/authors/ESS-CORE-VERSION-binding.md` | `a05b22e814d6556e75cbd7e6028adf2df2b9fbf5ab1b7c22540c92e125b8a553` | identisch / identisch |
| `docs/lizenzen.md` | `b5b0303ec23bc4bbc8dba1f59994c9ccd7cd90c76474157399cf78d616753dcb` | identisch / identisch |

Das Manifest ist ebenfalls unverändert. `pins-before.json`, `pins-after.json`, `http-access.json`, `http-access-supplement.json`, `graphql-access-01.json` bis `graphql-access-06.json`, `metadata-nine-checks.json`, `metadata-label-checks.json` und `pass-record.json` sind die wichtigsten Nachprüfbelege. Nicht gepinnte Instruktionsquellen haben separate, erst nach ihrer Lektüre erfasste Kontext-Hashes; sie werden nicht nachträglich als Eingangspins ausgegeben.

Dieser Erstbericht wird einmal geschrieben und danach unverändert erhalten. Sein SHA-256 und der Evidenzindex stehen separat in `outputs/loop/website-breadth-review/20261003T122206Z/index.json`. Nur dieser Bericht und der eigene Evidenzordner wurden geschrieben. Codex-Prüfer und Koordinator gehören derselben Modellfamilie an; trotz unabhängiger Lektüre bestehen gemeinsame mögliche Fehlerquellen. Es wird weder numerische oder methodische Freigabe noch Neutralitäts-, Design- oder Releasefreigabe erteilt.
