# R1 – Themenrecherche: Außen-/Verteidigungs-/Friedenspolitik, Bildung/Forschung, Medien/Digitalpolitik

Stand: 3. Oktober 2026, Recherche ca. 21:00–21:50 Uhr MESZ. Auftrag: `reports/claude/auftraege/R1-themen-aussen-bildung-digital.vollstaendig.md`. Ausgangsstand laut Auftrag: Commit `e9898fb`.

Dieser Bericht ist eine Quellen- und Instrumentenprüfung. Er ist keine Validierung, keine Dimensionsprüfung und keine Abnahme. Ein Themenfeld ist hier eine Suchgliederung, keine empirisch nachgewiesene Dimension. Seitenangaben „PDF-S.“ meinen physische, 1-basiert gezählte PDF-Seiten; gedruckte Seitenzahlen weichen teils ab.

## Kurzfassung

- Die lokal vorhandenen ESS-Ausgaben (ESS5, ESS8, ESS9, ESS10-SC, ESS11) enthalten in allen drei Bereichen praktisch keine Politikpräferenzen. Vorhanden sind Vertrauen in die Vereinten Nationen, Bewertung des Bildungssystems, wahrgenommene Bildungschancen, zwei Wahrnehmungsfragen zur Online-Kommunikation und eine pandemiebezogene Abwägung „Überwachen/Nachverfolgen vs. Privatsphäre“ (ESS10-SC A2). Nur diese letzte Frage ist eine Präferenzabwägung; ihr Gegenstand ist an die Pandemie gebunden.
- Außenpolitik ist teilweise über aktuelle Originalfragen erschließbar: GLES Querschnitt 2025 Nachwahl (ZA10100) enthält „Waffenlieferungen an die Ukraine beenden“ (q27e), „Israel weiterhin mit Waffen unterstützen“ (q27o) und ein verpflichtendes Gesellschaftsjahr bei Bundeswehr oder im sozialen Bereich (q170). ISSP 2023 (ZA10010) enthält Handel, internationale Institutionen und nationale Interessen (F7). Verteidigungsausgaben, Wehrpflicht und Russland-Sanktionen fand ich aktuell nur im GLES-Panel, das eine nichtprobabilistische Quotenstichprobe ist.
- Bildung ist für aktuelle Streitfragen (Bund/Länder, BAföG, Studiengebühren, Kita-/Sprachtestpflicht, Schulstruktur) in keinem geöffneten aktuellen Bevölkerungsinstrument abgedeckt. Historisch vorhanden: ISSP 2016 (Bildungsausgaben, Studienförderung, Anbieter von Schulbildung) und ISSP 2019 (Gerechtigkeit gekaufter besserer Bildung).
- Medien und Digitalpolitik sind kaum abgedeckt. Für Rundfunkbeitrag, Plattformregulierung, Hassrede/Desinformation, KI-Regulierung, IP-Adressen-Speicherung und Gesichtserkennung fand ich kein Bevölkerungsinstrument. Staatliche Überwachung im Internet gibt es in ISSP 2016 (historisch) und ISSP 2024 Digital Societies (Daten ZA10020 v1.0.0 seit 14.09.2026, Deutschland enthalten; deutscher Wortlaut von mir nicht gefunden).
- Rechte: ESS-Dokumentation steht unter CC BY-SA 4.0, ESS-Daten unter CC BY-NC-SA 4.0. Für GESIS-archivierte Studien (GLES, ISSP, Politbarometer, ALLBUS) ist nur die Zugangskategorie A belegt. Ob deutsche Fragewortlaute auf der öffentlichen Website gezeigt und zusammengefasste Ergebnisse dort veröffentlicht werden dürfen, ist für diese Studien in keinem geöffneten Dokument geregelt. Die GESIS-Nutzungsbedingungen konnte ich nicht öffnen (HTTP 403).
- Die Angabe in `docs/abdeckung-v2.md`, Verteidigungsausgaben und Wehrpflicht stünden im Vorabfragebogen GLES-Panel W34 auf PDF-S. 54, konnte ich nicht prüfen (Dokument gesperrt, keine Archivkopie). Gleichlautende Items fand ich im Vorabfragebogen W29 (PDF-S. 40).

## 1. Vorgehen und Ergebnisblindheit

Gelesen: `AGENTS.md`, `docs/project.md`, `docs/abdeckung-v2.md`, `docs/empirie-plan-v2.entwurf.md`, die lokalen deutschen ESS-Fragebögen unter `outputs/loop/breadth-data-001/sources/` sowie die dort liegende GLES-2025-Fragebogendokumentation. Nicht gelesen: `data/raw/`, `data/local/`, `data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`. `docs/handbuch.md` habe ich nicht gelesen, weil der Auftrag keine Arbeit an Oberfläche oder sichtbaren Texten umfasst.

Ich habe keine Antwortverteilungen, Prozentwerte, Mittelwerte oder Parteiergebnisse recherchiert oder übernommen. Ungewollte Berührungen mit Ergebnissen, die ich nicht verwendet habe:

- Zwei Suchmaschinen-Zusammenfassungen zeigten ungefragt EU-weite Eurobarometer-Prozentwerte (Verteidigungspolitik, Ukraine) und einen Ergebnissatz zur INVEDUC-Studie.
- Der ALLBUS-2023-Variable-Report (GESIS-Dok. 78534) enthält Häufigkeitstabellen. Ich habe daraus nur Zeilen mit Variablennamen und -etiketten extrahiert. Die Einleitung erwähnt eine Abbildung mit Mittelwerten zu `ma02` (Ausländerthema, nicht mein Bereich); Werte habe ich nicht gelesen.
- Mello 2024 nennt deutsche Verteidigungsausgaben als BIP-Anteil. Das sind Haushaltsangaben, keine Befragungsergebnisse.
- Die GLES-Fragebogendokumentationen (ZA10100, ZA10119, W29-Vorabfassung) enthalten nach Stichprobe keine Häufigkeiten.

Werkzeugvorbehalt: Einige Webseiten habe ich nur über ein Abrufwerkzeug gelesen, das Inhalte durch ein Hilfsmodell zusammenfasst. Wörtliche Zitate in diesem Bericht stammen, wo nicht anders vermerkt, aus Rohtext (PDF-Extraktion oder direkt geladenes HTML). Abschnitte, die nur über das Abrufwerkzeug belegt sind, kennzeichne ich mit „(Abrufwerkzeug, nicht wörtlich geprüft)“.

## 2. Geprüfte Studien und Instrumente (Übersicht)

| Studie | Archiv-Nr., Version, DOI | Deutschland: Feldzeit, Population, Modus, Auswahl | Zugang laut Quelle | Von mir eingesehen |
| --- | --- | --- | --- | --- |
| ESS5 | Ausgabe 3.6 (laut Auftrag lokal) | DE 2010/11 laut Auftrag; ESS-Population „All persons aged 15 and over resident within private households …“ (lokale Metadaten `ess5-study-access-metadata.json`); CAPI; mehrstufige Wahrscheinlichkeitsauswahl (`ess-public-de-mode-metadata.json`) | ESS-Lizenzen, s. Abschnitt 6 | deutscher Fragebogen (lokal) |
| ESS8 | 2.3 | DE 2016/17 laut Auftrag; wie oben | wie oben | Fragebogen + Antwortlisten (lokal) |
| ESS9 | 3.3 | DE 2018/19 laut Auftrag | wie oben | Fragebogen (lokal); Variablennamen über ESS9 Data Protocol e01_4 |
| ESS10 Self-completion | 3.2, DOI 10.21338/ess10sce03_2 (laut lokaler Metadatei) | DE 2021/22, Papier/Web laut Auftrag | wie oben | deutscher Papierfragebogen (lokal); Variablennamen nur über ESS10 Data Protocol e01_7 der CAPI-Datei |
| ESS11 | 4.2 | DE 2023 laut Auftrag | wie oben | Fragebogen (lokal) |
| ESS12 | nicht veröffentlicht | „Data from Round 12 (2025/26) … is expected to be published for the first time in January 2027.“ (ESS-Meldung, 30.09.2026) | – | Source Questionnaire (06.02.2025) |
| GLES Querschnitt 2025 Nachwahl | ZA10100, 4.0.0, DOI 10.4232/5.ZA10100.4.0.0; Fragebogendokumentation 1.3 vom 12.08.2026 | CAWI 24.02.–14.04.2025, Papier 24.02.–23.04.2025 (PDF-S. 6); „Personen mit deutscher Staatsangehörigkeit ab 16 Jahren gemeldet mit Hauptwohnsitz in der Bundesrepublik Deutschland“ (PDF-S. 11); mehrstufige Registerstichprobe mit Ost-Oversampling, etwa ein Fünftel der Sample Points über Adressen der Deutschen Post (PDF-S. 9, 11); 12 Gewichtungsvariablen (PDF-S. 19) | „Daten und Dokumente sind für die wissenschaftliche, studentische und nicht kommerzielle Nutzung freigegeben: Zugangskategorie Safeguarded – A.“ (PDF-S. 7) | vollständige Fragebogendokumentation |
| GLES Querschnitt 2025 Vorwahl | – | Eine Vorwahl-Querschnittsstudie 2025 habe ich nicht gefunden; die Nachwahl-Dokumentation erwähnt keine. Vermutung: wegen der vorgezogenen Wahl nicht durchgeführt (nicht belegt). | – | – |
| GLES Rolling Cross-Section 2025 | ZA10101, 3.0.0, DOI 10.4232/5.ZA10101.3.0.0 | 06.01.–31.03.2025; Wahrscheinlichkeitsauswahl (CESSDA-Katalog) | A (CESSDA) | nur Katalogmetadaten; Fragebogen nicht erreichbar (gesis.org 403, keine Archivkopie) |
| GLES Panel 2025 Welle 29 | ZA10118, 1.0.0 (CESSDA) | 16.–30.01.2025; wahlberechtigte deutsche Bevölkerung „mit Internetzugang“; CAWI; Quotenauswahl aus nichtprobabilistischen Online-Panels | „Daten und Dokumente sind für die akademische Forschung und Lehre freigegeben: Zugangskategorie A.“ (Vorabfassung PDF-S. 3) | nur Vorabfassung des Frageprogramms (über Internet-Archiv) |
| GLES Panel 2025 Welle 30 | ZA10119, 1.0.0, DOI 10.4232/5.ZA10119.1.0.0; Dokumentation 1.0 vom 08.12.2025 | 12.–22.02.2025; „Zur Wahl des Deutschen Bundestags 2025 wahlberechtigte deutsche Bevölkerung.“; „Nicht-Wahrscheinlichkeitsauswahl: Quotenstichprobe“; CAWI (PDF-S. 3–4) | „A - Daten und Dokumente sind für die akademische Forschung und Lehre freigegeben.“ (PDF-S. 4) | vollständige Fragebogendokumentation |
| GLES Panel W31–W34, GLES Tracking T59–T63 | u. a. ZA10120–ZA10123, ZA10002, ZA10105–ZA10108 | 2024–2026, alle Quotenauswahl aus Online-Panels (CESSDA) | A | nur Katalogmetadaten |
| ISSP 2016 Role of Government V | ZA6900, 2.0.0, DOI 10.4232/1.13052; Deutschland enthalten | deutscher Teil im ALLBUS 2016 als Selbstausfüller am Laptop (Fragebogen PDF-S. 3, Filter verweisen auf ALLBUS 2016); ALLBUS 2016 Feldzeit 06.04.–18.09.2016 (CESSDA, ZA5250 2.1.0). Population von mir nicht geprüft. | A (CESSDA) | deutscher Fragebogen (GESIS-Dok. 63842) |
| ISSP 2019 Social Inequality V | ZA7600, 3.0.0, DOI 10.4232/1.14009 | deutscher Papierfragebogen mit Datumsfeld „2020“ (PDF-S. 4); genaue Feldzeit und Population nicht geprüft | A | deutscher Fragebogen (Dok. 70592) |
| ISSP 2023 National Identity & Citizenship | ZA10010, 1.0.0, DOI 10.4232/5.ZA10010.1.0.0 | deutscher Papierfragebogen mit Datumsfeld „2023“ (PDF-S. 4); kombiniert mit ISSP 2022 Familie (Dok. 79164 mit identischem Fragentext) | A | deutscher Papierfragebogen (Dok. 80542) |
| ISSP 2024 Digital Societies | ZA10020, 1.0.0; Deutschland enthalten (issp.org, Meldung 14.09.2026) | nicht geprüft | „You will have to create a new user ID and password before downloading data files free of charge.“ (issp.org/data-download) | nur englischer Source Questionnaire (25.08.2023) |
| ALLBUS 2021 | ZA5280, 2.0.0, DOI 10.4232/1.14002 | – | A | CAWI-Fragebogendokumentation (Dok. 72851) |
| ALLBUS 2023 | ZA8830, 1.2.0, DOI 10.4232/1.14544 | Schwerpunkt „Religion und Weltanschauungen“ | A | nur Variablenetiketten des Variable Reports (Dok. 78534) |
| ALLBUS 2024 | – | nicht gefunden | – | – |
| Politbarometer 2024 / 2025 | ZA8974, 1.0.0, DOI 10.4232/1.14517 / ZA9151, 1.0.0, DOI 10.4232/1.14794 | 09.01.–19.12.2024 / 07.01.–11.12.2025; CATI und CAWI; Wahrscheinlichkeitsauswahl (CESSDA) | A | nur Katalogabstracts; Wortlaute nicht eingesehen |
| ZMSBw-Bevölkerungsbefragung | ZA-Nummern nicht ermittelt | jährlich seit 1996 | „Die Datensätze … ab 1996 sind über das Datenarchiv der Gesis … zugänglich.“ (zms.bundeswehr.de) | nur Übersichtsseite |
| INVEDUC | ZA6961, 1.0.0, DOI 10.4232/1.13140 | 15.04.–28.05.2014; CATI; Zufallsauswahl (CESSDA) | A | nur Katalogmetadaten |
| ifo Bildungsbarometer | EBDC-SUF, z. B. DOI 10.7805/ies-suf-2019-v1 | jährlich seit 2014; SUF-Wellen 2014–2021 | nur wissenschaftliche Zwecke, Nutzungsvereinbarung (Abrufwerkzeug, nicht wörtlich geprüft) | nur Datensatzbeschreibung |
| Eurobarometer | – | – | – | nicht ausgewertet; nur Datensatzeintrag „Standard Eurobarometer 104“ auf data.europa.eu (verlinkt nur Ergebnistabellen, nicht geöffnet) |

## 3. Außen-, Verteidigungs- und Friedenspolitik

### 3.1 Streitfragen 2021–2026

Die Wahl-O-Mat-Thesen zitiere ich aus der Definitionsdatei der bpb (`https://www.wahl-o-mat.de/bundestagswahl2025/app/definitionen/module_definition.js`). Sie belegen nur, dass die Frage im Wahlkampf 2025 zur Wahl stand. Parteipositionen stammen aus den Wahlprogrammen 2025 und belegen nur „Partei X fordert Y“.

Militärische Unterstützung der Ukraine. Wahl-O-Mat-These 1: „Deutschland soll die Ukraine weiterhin militärisch unterstützen.“ CDU/CSU: „Daher unterstützen wir die Ukraine mit allen erforderlichen diplomatischen, finanziellen und humanitären Mitteln sowie mit Waffenlieferungen.“ (PDF-S. 47). SPD: „Die SPD bekennt sich klar zur diplomatischen, militärischen, finanziellen und humanitären Unterstützung der Ukrainerinnen und Ukrainer …“ (PDF-S. 58). FDP: Die Verteidigung der Ukraine dürfe „nicht am Geld und an Waffenlieferungen scheitern“ (PDF-S. 47). Grüne: Unterstützung, damit die Ukraine sich verteidigen und eine starke Position für einen möglichen Friedensprozess haben kann (PDF-S. 142). Gegenpositionen: Die Linke fordert „Statt immer mehr Waffenlieferungen … eine gemeinsame Initiative“, um Russland und die Ukraine an den Verhandlungstisch zu bringen (PDF-S. 21). BSW: „Den Ukrainekrieg durch Verhandlungen beenden“; „Waffenlieferungen werden das Sterben nicht beenden“ (PDF-S. 6–7). AfD: „Die Zukunft der Ukraine sehen wir als neutralen Staat außerhalb von NATO und EU.“ (PDF-S. 93). Fachliche Einordnung: Mello (2024) beschreibt die Entscheidung über Leopard-2-Lieferungen und die parteipolitische Auseinandersetzung darum (PDF-S. 10, 12).

Verteidigungsausgaben und NATO-Ziele. Keine Wahl-O-Mat-These. CDU/CSU: „Wir stehen zum Zwei-Prozent-Ziel – mindestens.“ (PDF-S. 8). SPD: „nachhaltige Verteidigungsfinanzierung von mindestens zwei Prozent des BIP“ (PDF-S. 57). Grüne: „dauerhaft deutlich mehr als 2 Prozent des Bruttoinlandsprodukts“ (PDF-S. 152). Gegenpositionen: BSW: „Wir lehnen höhere Militärausgaben ab, die Erfüllung des Zwei-Prozent-Zieles der NATO oder gar höhere Ausgaben …“ (PDF-S. 6). Linke: „Wir widersetzen uns der militaristischen Zeitenwende, weil wir wissen: Aufrüstung wirkt sich immer zulasten des Sozialen aus.“ (PDF-S. 5). Rechtsrahmen seit 2025: Art. 109 Abs. 3 und Art. 115 Abs. 2 GG ziehen Verteidigungsausgaben (u. a.) ab, soweit sie „1 vom Hundert im Verhältnis zum nominalen Bruttoinlandsprodukt übersteigen“ (BGBl. 2025 I Nr. 94, Gesetz vom 22.03.2025, S. 1). NATO-Gipfel Den Haag, 25.06.2025, Ziff. 3: „Allies will allocate at least 3.5% of GDP annually … by 2035 … And Allies will account for up to 1.5% of GDP annually …“. Mello (2024) dokumentiert die Auseinandersetzung um Sondervermögen und Zwei-Prozent-Ziel (PDF-S. 7–8). Mader/Schoen (2023, PVS 64(3), 525–547, DOI 10.1007/s11615-023-00463-5) untersuchen Bevölkerungseinstellungen zur Außen- und Verteidigungspolitik nach Februar 2022; davon habe ich nur Katalogmetadaten gesehen.

Wehrpflicht, Wehrdienst, Gesellschaftsjahr. Wahl-O-Mat-These 36: „Für junge Erwachsene soll ein soziales Pflichtjahr eingeführt werden.“ Für eine Wehrpflicht: CDU/CSU „Aufwachsende Wehrpflicht einführen. Wir setzen perspektivisch auf ein verpflichtendes Gesellschaftsjahr …“ (PDF-S. 52); AfD „Daher wollen wir die Wehrpflicht wieder einsetzen.“ (PDF-S. 89). Für Freiwilligkeit: SPD „Der neue Wehrdienst soll auf Freiwilligkeit basieren …“ (PDF-S. 58); Grüne wollen statt des ausgesetzten Grundwehrdienstes „den freiwilligen Wehrdienst und die Reserve“ stärken (PDF-S. 154). Dagegen: FDP „Die Wiedereinsetzung der allgemeinen Wehrpflicht lehnen wir ab.“ (PDF-S. 48) und sieht ein Gesellschaftsjahr als „schweren Freiheitseingriff“ (PDF-S. 32); Linke „keine Wiedereinführung der Wehrpflicht“ (PDF-S. 23); BSW „Wir lehnen die Wiedereinführung einer Wehrpflicht ab.“ (PDF-S. 6). Gesetzgebung: Der Bundestag beschloss am 05.12.2025 das Wehrdienst-Modernisierungsgesetz (Drs. 21/1853, 21/2581). Laut Bundestag basiert der neue Wehrdienst „zunächst auf Freiwilligkeit“, enthält aber eine verpflichtende Bereitschaftserklärung für Männer, die Musterung und eine Verordnungsermächtigung zur verpflichtenden Heranziehung (bundestag.de, Textarchiv 2025 kw49).

Rüstungsexporte. Wahl-O-Mat-These 15: „Aus Deutschland sollen weiterhin Rüstungsgüter nach Israel exportiert werden dürfen.“ FDP: Rüstungsexporte seien „ein legitimes Mittel der Außen- und Sicherheitspolitik“; Israel solle NATO-Staaten gleichgestellt werden (PDF-S. 50). CDU/CSU: europäischer Binnenmarkt für Verteidigungsgüter „mit gemeinsamen Exportregeln“ (PDF-S. 53). SPD: „gemeinsame und koordinierte europäische Rüstungsexportpolitik“ (PDF-S. 59). Grüne: „kein Blankoscheck für Rüstungsexporte“, humanitäres Völkerrecht sei zu beachten (PDF-S. 147). Linke: „Rüstungsexporte vollständig verbieten“ (PDF-S. 23). BSW: „Verbot von Rüstungsexporten in Kriegsgebiete“ (PDF-S. 5).

Russland-Politik und Sanktionen. Keine Wahl-O-Mat-These. AfD: „sofortige Aufhebung der Wirtschaftssanktionen gegen Russland sowie die Instandsetzung der Nord Stream-Leitungen“ (PDF-S. 93). BSW kritisiert „Waffenlieferungen, Wirtschaftssanktionen“ als Konfliktunterstützung (PDF-S. 4). Linke: „Gezieltere Sanktionen, die sich nicht gegen die Bevölkerung, sondern gegen Putins Machtapparat …“ (PDF-S. 21). FDP: Finanzierung der Ukraine-Unterstützung „insbesondere auch durch die Nutzung der eingefrorenen russischen Vermögenswerte“ (PDF-S. 47).

Entwicklungszusammenarbeit. Keine Wahl-O-Mat-These. Grüne: mindestens „0,7 Prozent des Bruttonationaleinkommens in Entwicklungszusammenarbeit“ (PDF-S. 157). Linke will Kürzungen „umkehren“ (PDF-S. 25). FDP: „strukturelle Neuausrichtung der Entwicklungszusammenarbeit“ (PDF-S. 50). CDU/CSU: internationale Zusammenarbeit „gezielt an den strategischen Wirtschaftsinteressen Deutschlands“ ausrichten (PDF-S. 19) und Entwicklungszusammenarbeit auch auf das Ziel einer Wende in der Migrationspolitik ausrichten (PDF-S. 42). AfD: „Die deutsche Entwicklungspolitik ist gescheitert.“ (PDF-S. 96).

Handel, China, USA. Wahl-O-Mat-These 34: „Deutschland soll sich für die Abschaffung der erhöhten EU-Zölle auf chinesische Elektroautos einsetzen.“ CDU/CSU: „Grundsätzlich sind Zölle nicht der richtige Weg.“ (PDF-S. 20). SPD nennt Abkommen wie EU-Mercosur „wichtige Meilensteine“ (PDF-S. 65). Linke: „faire Kooperationsabkommen anstelle von Freihandelsabkommen“ (PDF-S. 25). BSW lehnt Handelsabkommen „wie das Mercosur-Abkommen“ ab (PDF-S. 19). AfD: „Das Mercosur-Abkommen schadet unserer Landwirtschaft derzeit …“ (PDF-S. 95). FDP: freihandelsähnliches Abkommen mit Taiwan (PDF-S. 50). Wahl-O-Mat-These 20 (Kontrolle von Zulieferern) berührt Handel, gehört primär zu Wirtschaft.

NATO und Bündnisse. CDU/CSU: „Ohne Wenn und Aber zur NATO stehen.“ (PDF-S. 52). FDP: „stehen uneingeschränkt zur NATO“ (PDF-S. 48). AfD: NATO-Mitgliedschaft bleibe zentral; „Eine Osterweiterung der EU und der NATO lehnen wir ab.“ (PDF-S. 88). Linke: „Entspannung statt Aufrüstung und Militarisierung“ (PDF-S. 21).

### 3.2 Verfügbare Originalfragen

Lokale ESS-Ausgaben: Keine Präferenzfrage zu Außen-, Verteidigungs- oder Friedenspolitik. Vorhanden ist nur Vertrauen in die Vereinten Nationen (`trstun`): ESS5 PDF-S. 7, ESS8 PDF-S. 8, ESS9 B12 PDF-S. 8, ESS10-SC A23 PDF-S. 4, ESS11 B12 PDF-S. 7; Skala 0 „Vertraue überhaupt nicht“ bis 10 „Vertraue voll und ganz“. Das ist Institutionenvertrauen, keine Politikpräferenz. ESS12 (noch nicht veröffentlicht) enthält laut Source Questionnaire als Rotationsmodule „Wellbeing“ und „Immigration“ (PDF-S. 2), also ebenfalls nichts Außenpolitisches außer Vertrauen in die Vereinten Nationen (A25, PDF-S. 16).

| Frage | Studie, Fundstelle | Deutscher Wortlaut | Antwortskala, Filter | Bemerkung |
| --- | --- | --- | --- | --- |
| q27e | GLES 2025 Nachwahl ZA10100, PDF-S. 147, Papier F63 | Einleitung „Was halten Sie von folgenden Aussagen?“; Item „(E) Deutschland sollte die Lieferung von Waffen an die Ukraine beenden.“ | (1) stimme voll und ganz zu, (2) stimme eher zu, (3) teils/teils, (4) stimme eher nicht zu, (5) stimme überhaupt nicht zu; (-99) keine Angabe; kein Eingangsfilter dokumentiert | Batterie mit A–D (Anpassung an deutsche Kultur, gendergerechte Sprache, Staat und Wirtschaft, Einkommensunterschiede); Wahrscheinlichkeitsstichprobe, aktuell |
| q27o | ZA10100, PDF-S. 166, F73 | „(O) Deutschland sollte Israel weiterhin mit Waffen unterstützen“ (ohne Schlusspunkt im Original) | wie q27e | Batterie mit Wahlalter 16 und Gesetzen mit AfD-Stimmen |
| q170 | ZA10100, PDF-S. 241, F115 | „Es gibt Diskussionen, statt der ausgesetzten Wehrpflicht in Zukunft ein verpflichtendes Gesellschaftsjahr einzuführen. Demnach sollen junge Menschen ein Jahr lang Dienst wahlweise bei der Bundeswehr oder im sozialen Bereich leisten müssen. Inwieweit stimmen Sie diesem Vorschlag zu?“ | (1) stimme voll und ganz zu bis (5) stimme überhaupt nicht zu; (-99) | misst ein Gesellschaftsjahr mit Wahl zwischen Bundeswehr und sozialem Bereich, keine reine Wehrpflicht; in `abdeckung-v2.md` bisher nicht aufgeführt |
| q56c, q38c | ZA10100, PDF-S. 190 / 248 | Bewertung der Arbeit der Bundesregierung „Umgang Krieg in UKR“; Angst vor Ausweitung des Krieges nach Deutschland | – | Leistungsbewertung bzw. Emotion, keine Präferenz |
| kp29_2880cf | GLES Panel W29, Vorabfassung PDF-S. 40 | „Deutschland sollte pro Jahr mindestens zwei Prozent seiner Wirtschaftsleistung für die Verteidigung ausgeben.“ | (1) stimme überhaupt nicht zu bis (5) stimme voll und ganz zu | Quotenstichprobe aus Online-Panels; Vorabfassung, endgültige Dokumentation ZA10118 nicht gesehen |
| kp29_2880cz | W29, PDF-S. 40 | „In Deutschland sollte eine Wehrpflicht gelten.“ | wie oben | wie oben |
| kp29_2880bk | W29, PDF-S. 36 | „Deutschland sollte gegenüber Russland weniger auf Kooperation und mehr auf Konfrontation setzen.“ | wie oben | wie oben |
| kp29_2880cl, kp30_2880cl | W29 PDF-S. 36; W30 PDF-S. 53 | „Deutschland sollte sich bei der Unterstützung der Ukraine besser zurückhalten, damit wir nicht auch angegriffen werden.“ | wie oben | enthält eine Begründung im Item; zwei Gegenstände in einem Satz |
| kp30_1200 | W30 ZA10119, PDF-S. 49 | „Und jetzt geht es um Deutschlands Haltung zu den Sanktionen gegen Russland. Manche meinen, Deutschland sollte die Sanktionen gegen Russland lockern. Andere meinen, Deutschland sollte die Sanktionen gegen Russland verschärfen. Wie ist Ihre Meinung zu diesem Thema?“ | 7 Punkte, Endpunkte „lockern“ (1) / „verschärfen“ (7) | Quotenstichprobe |
| kp30_1203 (auch kp29_1203) | W30 PDF-S. 51; W29 PDF-S. 34 | „Und welche Meinung haben Sie persönlich zum Thema ‚Waffenlieferungen an die Ukraine‘?“ | 7 Punkte, (1) Befürwortung, (7) Ablehnung | Quotenstichprobe |
| kp30_2880v, ag, ah, ai | W30, PDF-S. 54 | „(V) Alles in allem ist die Globalisierung eine gute Sache.“ „(AG) Das weltweite Zusammenwachsen der Märkte sollte weiter vorangetrieben werden.“ „(AH) Deutschland sollte die Einfuhr von Waren aus anderen Ländern einschränken.“ „(AI) Ausländische Unternehmen sollten in Deutschland uneingeschränkt investieren dürfen.“ | 5 Stufen wie oben | Quotenstichprobe |
| kp29_1484a–c | W29, PDF-S. 41 | Skalometer „Was halten Sie ganz allgemein von folgenden Ländern und Politikern?“ (USA, China, Russland) | -5 bis +5 | Bewertung von Ländern, keine Politikpräferenz |
| J006 E | ISSP 2016, Dok. 63842, PDF-S. 9 | „Bitte geben Sie nun für die folgenden Bereiche an, ob die Regierung dafür weniger oder mehr Geld ausgeben sollte. Bedenken Sie dabei, dass sehr viel höhere Ausgaben auch höhere Steuern erfordern können.“ Item „Verteidigung“ | (1) sehr viel mehr ausgeben, (2) etwas mehr ausgeben, (3) die Ausgaben auf dem jetzigen Stand halten, (4) weniger ausgeben, (5) sehr viel weniger ausgeben, (8) Kann ich nicht sagen | 2016, vor 2022; Variablenname nicht eingesehen |
| F7 a–c | ISSP 2023, Dok. 80542, PDF-S. 6 | „Inwieweit stimmen Sie den folgenden Aussagen zu oder nicht zu?“ „Deutschland sollte die Einfuhr ausländischer Produkte beschränken, um seine eigene Wirtschaft zu schützen.“ „Bei bestimmten Problemen wie der Umweltverschmutzung sollten internationale Institutionen das Recht haben, Lösungen durchzusetzen.“ „Deutschland sollte seine eigenen Interessen verfolgen, selbst wenn dies zu Konflikten mit anderen Ländern führt.“ | Stimme voll und ganz zu, Stimme zu, Weder noch, Stimme nicht zu, Stimme überhaupt nicht zu, Kann ich nicht sagen (Codes im Papierfragebogen nicht abgedruckt) | weitere F7-Items: Grunderwerb durch Ausländer, Vorzug deutscher Programme im Fernsehen, internationale Konzerne; Variablennamen nicht eingesehen |
| F11 (letztes Item) | ISSP 2023, PDF-S. 8 | „Dass jemand … bereit ist, notfalls Militärdienst zu leisten.“ (Wichtigkeit für einen guten Bürger) | 1 „überhaupt nicht wichtig“ bis 7 „sehr wichtig“ | Bürgernorm, keine Politikpräferenz zur Wehrpflicht |
| F11 (zweites Item) | ISSP 2019, Dok. 70592, PDF-S. 8 | „Menschen in reichen Ländern sollten eine zusätzliche Steuer entrichten, um den Menschen in armen Ländern zu helfen.“ | Stimme voll und ganz zu … Stimme überhaupt nicht zu, Kann ich nicht sagen | einziger gefundener Bezug zu globaler Umverteilung/Entwicklung; Feldjahr 2020 |

Weitere Instrumente, deren Wortlaut ich nicht gesehen habe: Politbarometer 2024 und 2025. Laut CESSDA-Abstract enthält ZA9151 (2025) u. a. „attitudes toward increased defense spending“, „questions on the reintroduction of compulsory military service in Germany“, „attitudes toward military aid for Ukraine and German arms deliveries“ und „assessments of US tariff policy and its economic effects“. ZA8974 (2024) enthält u. a. „support for a year of mandatory service (compulsory military service)“ und „support for Western military aid to Ukraine“. Die Abstracts betonen, dass viele Fragen nur in einzelnen Monatswellen gestellt wurden. Die ZMSBw-Befragung behandelt laut ZMSBw „Einstellungen zum außen- und sicherheitspolitischen Engagement Deutschlands, Haltungen der Bürgerinnen und Bürger zur Bundeswehr … und den Auslandseinsätzen“; ZA-Nummern und Wortlaute habe ich nicht ermittelt. Die ZMSBw-Forschungsberichte enthalten Ergebnisse; ich habe sie deshalb nicht geöffnet. Eurobarometer habe ich nicht ausgewertet.

### 3.3 Bewertung

Mit den lokalen ESS-Ausgaben: nicht abgedeckt. Nach Sichtung weiterer Instrumente: teilweise abgedeckt.

- Aktuell und mit Wahrscheinlichkeitsstichprobe belegt: Ukraine-Waffenlieferungen (q27e), Waffen für Israel (q27o), Gesellschaftsjahr mit Bundeswehroption (q170), alle GLES 2025 Nachwahl; Handel, internationale Institutionen und nationale Interessen (ISSP 2023 F7 a–c).
- Nur nichtprobabilistisch (GLES-Panel) oder ungesehen (Politbarometer): Verteidigungsausgaben aktuell, Wehrpflicht als solche, Russland-Sanktionen, Globalisierung/Investitionen.
- Nur historisch: Verteidigungsausgaben ISSP 2016; globale Umverteilung ISSP 2019.
- Fehlende Daten (nicht gefunden): Rüstungsexporte allgemein, NATO-Mitgliedschaft und Bündnisverpflichtungen, Auslandseinsätze, Entwicklungszusammenarbeit als konkrete Ausgaben- oder Zielfrage, Verhältnis zu USA und China als Präferenz.
- Bewusster inhaltlicher Ausschluss (meine Empfehlung): Vertrauen in die Vereinten Nationen, Länder-Skalometer, Regierungsbewertungen und Angstfragen nicht als außenpolitische Position werten. Sie messen Vertrauen, Bewertung oder Emotion.

Erlaubte Interpretation: nur konkrete Einzelangaben mit Wortlaut, Studie, Erhebungszeit und Population. Eine gemeinsame Dimension ist nicht begründbar: In GLES 2025 Nachwahl liegen nur drei außenpolitische Items mit verschiedenen Gegenständen vor, die übrigen Items stammen aus anderen Studien, Jahren und Populationen ohne gemeinsame Personen. Ein formativer Wert bräuchte eine eigene Inhalts- und Gewichtsbegründung; die liegt nicht vor. q27e und q27o haben Ablehnungs- bzw. Fortsetzungsformulierung; eine gemeinsame Polung „pro/contra Waffenlieferungen“ würde den Wortlaut verändern.

## 4. Bildung und Forschung

### 4.1 Streitfragen 2021–2026

Zuständigkeit Bund/Länder. Wahl-O-Mat-These 14: „Der Bund soll mehr Kompetenzen in der Schulpolitik erhalten.“ Grüne: „Das Kooperationsverbot wollen wir abschaffen.“ (PDF-S. 77). Linke: Das Kooperationsverbot „muss vollständig aufgehoben und stattdessen eine umfassende Gemeinschaftsaufgabe“ werden (PDF-S. 38). BSW: Das Kooperationsverbot „muss mit dem Ziel der Bildungsgerechtigkeit in den Ländern aufgehoben werden“ (PDF-S. 24). FDP: „grundlegende Reform des Bildungsföderalismus, die einheitliche Standards und eine stärkere Rolle des Bundes in der Bildung möglich macht“, dazu „einheitliche Abschlussprüfungen (Deutschland-Abitur)“ (PDF-S. 8). CDU/CSU: „bundesweit vergleichbares Abitur auf hohem Niveau“ (PDF-S. 9). Bei SPD und AfD fand ich per Stichwortsuche keine ausdrückliche Aussage zur Kompetenzverteilung in der Schulpolitik; die SPD will das Startchancen-Programm ausbauen und den Digitalpakt fortsetzen (PDF-S. 15). Rechtsrahmen: Art. 104c GG erlaubt Finanzhilfen des Bundes „zur Steigerung der Leistungsfähigkeit der kommunalen Bildungsinfrastruktur“ (gesetze-im-internet.de, Abrufwerkzeug). Die Bund-Länder-Vereinbarung zum Startchancen-Programm 2024–2034 stützt Säule I auf Art. 104c GG (KMK-PDF, PDF-S. 1). Politikwissenschaftlicher Hintergrund: Wollmann (2020) zu Föderalismusreform I und dem „Kooperationsverbot“ (Preprint PDF-S. 17–21; erschienen in Roters/Gräf/Wollmann, Springer VS, S. 263–284). Der Text liegt vor 2021.

Studienfinanzierung und Studiengebühren. Wahl-O-Mat-These 21: „Die Ausbildungsförderung BAföG soll weiterhin abhängig vom Einkommen der Eltern gezahlt werden.“ SPD: „Langfristig wollen wir das BAföG elternunabhängiger machen.“ (PDF-S. 16). Grüne: „Wir wollen das BAföG elternunabhängiger gestalten …“ (PDF-S. 79). FDP: „elternunabhängigen Baukasten-System“ (PDF-S. 10). CDU/CSU: BAföG und KfW-Studienkredit „besser aufeinander“ abstimmen, BAföG „muss auskömmlich sein“ (PDF-S. 69). Studiengebühren: AfD will für Studierende aus Nicht-EWR-Staaten „angemessene Studiengebühren“ (PDF-S. 164); Linke: „Wir sind gegen Studiengebühren, unabhängig vom Pass oder von der Studiendauer.“ (PDF-S. 40).

Schulstruktur. AfD: „Die AfD befürwortet ein nach Begabungen differenziertes Schulsystem …“ (PDF-S. 159), dazu „Schulpflicht zur Bildungspflicht umwandeln“ (Inhaltsverzeichnis PDF-S. 7). BSW: „Wir setzen uns für ein längeres gemeinsames Lernen ein.“ (PDF-S. 24). Linke: Ganztagsangebot „am besten an einer Gemeinschaftsschule“ (PDF-S. 39). FDP: Notenpflicht „spätestens ab der dritten Klasse“ (PDF-S. 8).

Frühkindliche Bildung. CDU/CSU: „verpflichtende Sprachtests im Vorschulalter. Kinder mit Sprachproblemen müssen eine Kita oder Vorschule besuchen.“ (PDF-S. 9). FDP: „bundesweit verpflichtende und altersgerechte Sprachtests für alle Kinder im Vorschulalter“ (PDF-S. 7). BSW: verpflichtender Deutschtest ab drei Jahren und „mittelfristig Beitragsfreiheit“ der Kita (PDF-S. 24). Linke: Ausbau der „gebührenfreien Kinderganztagsbetreuung“ (PDF-S. 16). SPD: Bund, Länder und Gemeinden sollen „gemeinsam weiter in gute Kita-Qualität investieren“ (PDF-S. 15).

Forschung. FuE-Ziel: CDU/CSU 3,5 Prozent des BIP bis 2030 (PDF-S. 5), Grüne „deutlich mehr als 3,5 Prozent“ (PDF-S. 22). Zivilklauseln: FDP fordert ihre Streichung (PDF-S. 11), CDU/CSU will „Einschränkungen für militärische Forschung aufheben“ (PDF-S. 68); Linke will Zivilklauseln „an allen Hochschulen und Forschungseinrichtungen“ verankern (PDF-S. 41), ebenso BSW (PDF-S. 25). AfD verlangt eine „Entpolitisierung der Forschungslandschaft“ (PDF-S. 165).

Bildungsausgaben. Keine Wahl-O-Mat-These; als Ausgabenpriorität im ISSP 2016 vorhanden (s. unten).

### 4.2 Verfügbare Originalfragen

Lokale ESS-Ausgaben:

| Frage | Fundstelle | Wortlaut | Skala | Bemerkung |
| --- | --- | --- | --- | --- |
| `stfedu` | ESS5 PDF-S. 11 (Liste 11); ESS8 B31 PDF-S. 11; ESS9 B31 PDF-S. 13; ESS10-SC A44 PDF-S. 5; ESS11 B31 PDF-S. 12 | ESS10-SC: „Wie schätzen Sie - alles in allem - den derzeitigen Zustand des Bildungssystems in Deutschland ein?“ | 0 „Äußerst schlecht“ bis 10 „Äußerst gut“ | Bewertung, keine Präferenz |
| `evfredu` (G6), `ifredu` (G4) | ESS9 PDF-S. 79; Namen laut ESS9 Data Protocol e01_4 | G6: „Allgemein haben alle Menschen in Deutschland eine faire Chance, den von ihnen angestrebten Bildungsabschluss zu erreichen.“ | 00 „Trifft überhaupt nicht zu“ bis 10 „Trifft voll und ganz zu“; G4 zusätzlich 55 „noch keinen Bildungsabschluss erreicht“ | Wahrnehmung, keine Präferenz |
| `eduunmp` (E34) | ESS8 PDF-S. 42 | „Wären Sie dagegen oder dafür, dass der Staat mehr für die Aus- und Weiterbildung von Arbeitslosen ausgibt, aber dafür weniger Arbeitslosenunterstützung zahlt?“ | Sehr dagegen (1) bis Sehr dafür (4) | bereits im 43er-Bestand, primär Sozialstaat |

Andere Instrumente:

| Frage | Studie, Fundstelle | Wortlaut | Skala | Bemerkung |
| --- | --- | --- | --- | --- |
| J006 D | ISSP 2016, PDF-S. 9 | Einleitung wie J006 E; Item „Bildungswesen“ | wie J006 E | 2016 |
| J007b H | ISSP 2016, PDF-S. 10 | „Bitte geben Sie nun an, inwieweit die folgenden Dinge in der Verantwortlichkeit des Staates liegen sollten. … Der Staat sollte … den Studenten aus einkommensschwachen Familien finanzielle Unterstützung zu gewähren.“ | (1) auf jeden Fall verantwortlich sein, (2) verantwortlich sein, (3) nicht verantwortlich sein, (4) auf keinen Fall verantwortlich sein, (8) Kann ich nicht sagen | Zuständigkeit, nicht BAföG-Ausgestaltung (z. B. Elternabhängigkeit) |
| J008c | ISSP 2016, PDF-S. 11 | „Wer sollte Ihrer Meinung nach hauptsächlich für die Erbringung folgender Dienstleistungen zuständig sein? … Schulbildung für Kinder“ | Der Staat (1), Private Unternehmen/gewinnorientierte Organisationen (2), Gemeinnützige Organisationen/… (3), Kirchen … (4), Familie, Verwandte oder Freunde (5), Kann ich nicht sagen (8) | nominal; Staat insgesamt, nicht Bund vs. Länder |
| F9 (zweites Item) | ISSP 2019, PDF-S. 7 | „Ist es gerecht oder ungerecht, dass Menschen mit höherem Einkommen … ihren Kindern eine bessere Ausbildung zukommen lassen können als Menschen mit niedrigerem Einkommen?“ | Sehr gerecht, Eher gerecht, Weder gerecht noch ungerecht, Eher ungerecht, Sehr ungerecht, Kann ich nicht sagen | normatives Gerechtigkeitsurteil, keine Maßnahme |
| im01 | ALLBUS 2023 (Etikett „BILDUNGSMOEGL.IN D.:JEDER N.S.BEGABUNG“) | Wortlaut nicht eingesehen | – | dem Etikett nach Wahrnehmung |

GLES 2025 Nachwahl, ALLBUS 2021 (CAWI-Dokumentation) und ESS12 enthalten nach meiner Suche keine Präferenzfrage zu Bildung oder Forschung; GLES und ALLBUS fragen nur den eigenen Bildungsabschluss, ALLBUS 2021 zusätzlich Vertrauen in „Hochschulen und Universitäten“ (pt11, PDF-S. 45). Nicht eingesehene Instrumente mit Bildungsbezug: ifo Bildungsbarometer (laut ifo „eine jährliche repräsentative Meinungsumfrage“ seit 2014 zu Bildungspolitik; SUF 2014–2021 über das LMU-ifo EBDC; Abrufwerkzeug), INVEDUC (2014; Ausgabenpräferenzen nach Bildungsbereich laut CESSDA-Beschreibung, Wortlaut nicht gesehen).

### 4.3 Bewertung

Für aktuelle bildungspolitische Präferenzen: nicht abgedeckt. Historisch: teilweise (ISSP 2016 Ausgaben und Zuständigkeiten, ISSP 2019 Gerechtigkeitsnorm).

- Fehlende Daten: Kompetenzverteilung Bund/Länder, Elternabhängigkeit des BAföG, Studiengebühren, Kita- oder Sprachtestpflicht, Schulstruktur, Zivilklauseln, Forschungsausgaben. In keinem geöffneten aktuellen Bevölkerungsinstrument gefunden. Das ifo Bildungsbarometer könnte einige dieser Gegenstände enthalten; das ist ungeprüft, und der Zugang ist auf wissenschaftliche Nutzung im EBDC beschränkt.
- Bewusster inhaltlicher Ausschluss (Empfehlung): `stfedu`, `evfredu`, `ifredu`, im01 nicht als Bildungsposition werten. Sie messen Bewertung oder Wahrnehmung.
- `eduunmp` und `gvcldcr` (Kinderbetreuung) bleiben primär Sozialstaat; als Nebenbezug Bildung dürfen sie keine Bildungsbreite vortäuschen.

Erlaubte Interpretation: nur Einzelangaben. Eine gemeinsame Dimension ist mangels mehrerer aktueller Items aus einer Studie nicht prüfbar. Ein formativer Bildungswert ist nicht begründet.

## 5. Medien und Digitalpolitik

### 5.1 Streitfragen 2021–2026

Öffentlich-rechtlicher Rundfunk und Rundfunkbeitrag. Keine Wahl-O-Mat-These; Rundfunkfinanzierung ist Ländersache. Das BVerfG stellte 2021 fest, Sachsen-Anhalt habe durch die fehlende Zustimmung zum Ersten Medienänderungsstaatsvertrag „die Rundfunkfreiheit der öffentlich-rechtlichen Rundfunkanstalten aus Artikel 5 Abs. 1 Satz 2 GG verletzt“ (Pressemitteilung 69/2021, Beschluss vom 20.07.2021, 1 BvR 2756/20 u. a.). Laut BVerfG-Pressemitteilung 29/2026 vom 13.05.2026 empfahl die KEF im Februar 2024 eine Erhöhung von 18,36 auf 18,94 Euro; die Regierungschefinnen und -chefs der Länder beschlossen im Dezember 2024, am bisherigen Betrag zwei Jahre festzuhalten; „am 1. Dezember 2025 [trat] der Reformstaatsvertrag in Kraft“; die KEF empfahl im Februar 2026 18,64 Euro ab 01.01.2027. Mündliche Verhandlung „Rundfunkfinanzierung II“ (1 BvR 2524/24, 1 BvR 2525/24) am 23.06.2026; eine Entscheidung habe ich nicht gefunden. Programme: AfD „GRUNDFUNK statt GEZ-Zwangsabgabe“ (PDF-S. 174), Aufgabe des Rundfunks solle „allein eine gebührenfreie Grundversorgung“ sein (PDF-S. 175). FDP will „den Rundfunkbeitrag deutlich senken“ (PDF-S. 27). BSW: „Eine Erhöhung des Rundfunkbeitrags lehnen wir ab.“, zugleich „nicht abschaffen, sondern … reformieren“ (PDF-S. 41). CDU/CSU: „Mehr Mut und Tempo bei Reform des öffentlich-rechtlichen Rundfunks“, Kernauftrag „Sparsamkeit, mehr Meinungsvielfalt und Neutralität“ (PDF-S. 57). SPD: Der Rundfunk „muss durch eine auftragsgerechte, rechtssichere Finanzierung gestärkt werden“ (PDF-S. 49). Grüne: „auskömmliche Finanzierung“, Bezug auf KEF-Vorschläge (PDF-S. 140). Linke: Programmvielfalt erhalten, Gehaltsstrukturen offenlegen (PDF-S. 55).

Plattformregulierung, Desinformation, Hassrede und Meinungsfreiheit. Keine Wahl-O-Mat-These. SPD: „Plattformbetreiber werden verpflichtet, illegale Inhalte zu entfernen …“ (PDF-S. 45) und „verpflichtende Tools zum Faktencheck auf großen Plattformen“ (PDF-S. 50). Grüne: Grenzen der Meinungsfreiheit, „wenn Desinformation sich unkontrolliert ausbreitet“ und Straftatbestände berührt sind (PDF-S. 114). CDU/CSU: bei der Umsetzung des Digital Services Act Schwerpunkt auf „mehr Transparenz, Kampf gegen Desinformation“ (PDF-S. 41). Linke: AI Act und Digital Services Act „müssen zügig in nationales Recht überführt … werden“ (PDF-S. 57). Gegenpositionen: FDP: DSA-Sorgfaltspflichten „dürfen nicht dazu führen, dass die Meinungsfreiheit beeinträchtigt wird“ (PDF-S. 27). AfD: „Kritische und vermeintlich störende Meinungen, solange sie nicht die Grenze zur Strafbarkeit überschreiten, gehören zum verfassungsrechtlich garantierten Recht …“ (PDF-S. 49). BSW kritisiert „unklare[…] oder schwammige[…] Begriffe wie ‚Desinformation‘ oder ‚Hass und Hetze‘“ (PDF-S. 39).

Staatliche Überwachung, IP-Adressen, Gesichtserkennung. Wahl-O-Mat-These 7: „An Bahnhöfen soll die Bundespolizei Software zur automatisierten Gesichtserkennung einsetzen dürfen.“ CDU/CSU: „automatisierten Gesichtserkennung an Bahnhöfen, Flughäfen und anderen Kriminalitätsschwerpunkten“ (PDF-S. 39) und „Mindestdauer-Speicherung von IP-Adressen“ (PDF-S. 40). SPD nennt „IP-Adressen und Port-Nummern“ und „ergänzend“ die „Log-in-Falle“ (PDF-S. 45); ob eine Speicherpflicht gemeint ist, geht aus dem Satz nicht eindeutig hervor. Gegenpositionen: Grüne: „Instrumente der anlasslosen Massenüberwachung wie Vorratsdatenspeicherungen, Chatkontrolle oder die biometrische Erfassung im öffentlichen Raum lehnen wir ab.“ (PDF-S. 115). FDP: „Den Einsatz von automatisierter Gesichtserkennung im öffentlichen Raum lehnen wir ab.“ und Ablehnung der Vorratsdatenspeicherung zugunsten eines „Quick-Freeze-Modell[s]“ (PDF-S. 24). AfD: „Wir lehnen Staatstrojaner und die Vorratsdatenspeicherung ab.“ (PDF-S. 125). Linke: „gegen Vorratsdatenspeicherung“, biometrische Videoüberwachung und Chat-Kontrollen verbieten (PDF-S. 49). BSW lehnt Chatkontrolle und Vorratsdatenspeicherung ab (PDF-S. 43). Gesetzgebung: Regierungsentwurf zur IP-Adressspeicherung (Drs. 21/6581, 21/7154), erste Beratung am 24.06.2026; Zugangsanbieter sollen „für drei Monate die von ihnen an Endkunden vergebenen IP-Adressen … speichern“ (bundestag.de, Textarchiv 2026 kw26).

KI-Regulierung. CDU/CSU: Der AI Act müsse „bürokratiearm und innovationsoffen umgesetzt“ werden, „Eine Übererfüllung lehnen wir strikt ab.“ (PDF-S. 29). FDP: AI-Act-Umsetzung „deutlich innovationsfreundlicher gestalten“ (PDF-S. 11). SPD: „strikte Durchsetzung der Bot-Kennzeichnungspflicht aus der KI-Verordnung“ (PDF-S. 50). Linke: zügige Überführung und Weiterentwicklung (PDF-S. 57).

Digitalisierung der Verwaltung. CDU/CSU will ein Bundesdigitalministerium (PDF-S. 4), Grüne ebenfalls ein Digitalministerium (PDF-S. 34), AfD nennt „Vorantreiben der Digitalisierung der Verwaltung“ (PDF-S. 15), FDP hat ein eigenes Kapitel (Inhaltsverzeichnis PDF-S. 3). Meine Einschätzung (nicht belegt): In den Programmen ist das Ziel weitgehend geteilt; Unterschiede liegen in Organisation und Tempo. Als Positionsfrage für ein Profil ist das Thema deshalb schwächer als die vorigen.

Medienfreiheit. Als Demokratieprinzip in ESS6 und ESS10 abgefragt (s. unten). Eine eigene aktuelle Streitfrage im Wahlkampf 2025 habe ich nicht gesucht.

### 5.2 Verfügbare Originalfragen

Lokale ESS-Ausgaben:

| Frage | Fundstelle | Wortlaut | Skala | Bemerkung |
| --- | --- | --- | --- | --- |
| A2 (vermutlich `panmonpb`) | ESS10-SC DE, PDF-S. 2 | „Ist es bei der Bekämpfung einer Pandemie wichtiger, dass Regierungen die Bevölkerung überwachen und nachverfolgen oder die Privatsphäre des Einzelnen bewahren?“ | 0 „Viel wichtiger, die Bevölkerung zu überwachen und nachzuverfolgen“ bis 10 „Viel wichtiger, die Privatsphäre des Einzelnen zu bewahren“ | einzige lokale Präferenzabwägung im Bereich; pandemiegebunden. Variablenname aus ESS10 Data Protocol e01_7 (CAPI, K5a „panmonpb“); in der SC-Datei nicht geprüft. In der CAPI-Fassung gab es eine Zufallsvariante ohne Pandemiebezug (K5b `govmonpb`); der deutsche SC-Fragebogen zeigt nur die Pandemiefassung. |
| B3 `medcrgv` | ESS10-SC DE, PDF-S. 11 | „(Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…) …dass die Medien das Recht haben, Kritik an der Regierung zu üben?“ | 0 „Überhaupt nicht wichtig für die Demokratie im Allgemeinen“ bis 10 „Äußerst wichtig …“ | bereits im 43er-Bestand, primär Demokratie |
| D8, D9 (vermutlich `mcpriv`, `mcmsinf`) | ESS10-SC DE, PDF-S. 27 | „Wie sehr denken Sie, dass die Online- und Mobilkommunikation dazu führt, … dass die Privatsphäre gefährdet wird?“ / „… dass man falschen Informationen ausgesetzt ist?“ | 0 „Überhaupt nicht“ bis 10 „Voll und ganz“ | Wahrnehmung, keine Präferenz; Namen aus CAPI-Protokoll (G8, G9) |
| MEDCRGV, MEPRINF | ESS6 DE, PDF-S. 25 (keine lokalen Daten) | „… dass die Medien das Recht haben, Kritik an der Regierung zu üben“; „… dass die Medien verlässliche Informationen für die Bürger …“ | 0–10 | 2012; nur Fragebogen lokal |

Andere Instrumente:

| Frage | Studie, Fundstelle | Wortlaut | Skala | Bemerkung |
| --- | --- | --- | --- | --- |
| J011 A/B | ISSP 2016, PDF-S. 13 | „Sollten staatliche Behörden in Deutschland Ihrer Meinung nach das Recht zu Folgendem haben oder nicht haben?“ A „Menschen im öffentlichen Bereich mit Videokameras zu überwachen?“ B „E-Mails und anderen Informationsaustausch über das Internet zu überwachen?“ | Auf jeden Fall (1), Eher ja (2), Eher nein (3), Auf keinen Fall (4), Kann ich nicht sagen (8) | 2016; in `abdeckung-v2.md` primär Bürgerrechte, hier Nebenbezug; nicht doppelt zählen |
| J013 A/B, J014 A–C, J012 | ISSP 2016, PDF-S. 14–15 | u. a. „Über jeden, der in Deutschland lebt, Informationen zu sammeln, auch ohne deren Wissen.“; bei Terrorverdacht „Telefongespräche abzuhören?“ | wie J011; J012 0–10 | wie oben |
| Q28a/b | ISSP 2024 Source Questionnaire, PDF-S. 17 | englisch: „Do you think that the [COUNTRY’S] government should or should not have the right to do the following? a. Keep people under video surveillance in public areas? b. Monitor e-mails, social media content and any other personal information exchanged on the Internet?“ | Definitely should have right … Definitely should not have right, Can’t choose | deutscher Wortlaut nicht gefunden; Q28b weicht laut Fragebogen von ISSP 2016 Q11b ab („b is similar to Q11b“) |
| Q27 | ISSP 2024 Source, PDF-S. 17 | „Who should be mostly responsible for protecting personal information when using the Internet?“ | Online companies / People / Public authorities / Can’t choose | Zuständigkeitsfrage zum Datenschutz; deutscher Wortlaut offen |
| F7 (fünftes Item) | ISSP 2023, PDF-S. 6 | „Das deutsche Fernsehen sollte deutschen Filmen und Programmen den Vorzug geben.“ | wie F7 a–c | Programmpräferenz mit nationalem Bezug; kein Rundfunkfinanzierungsitem |
| F21 | ISSP 2023, PDF-S. 11 | „In Deutschland ist die Medienberichterstattung über Politik einseitig.“ | Stimme voll und ganz zu … Kann ich nicht sagen | Wahrnehmung |
| q79i, q79h | GLES 2025 Nachwahl, PDF-S. 239 | Vertrauen in „den öffentlich-rechtlichen Rundfunk“ bzw. „soziale Medien“ | – | Vertrauen, keine Präferenz |
| pt09, pt10 | ALLBUS 2021 CAWI, PDF-S. 45 | Vertrauen in „dem Fernsehen“, „dem Zeitungswesen“ | 1 „Überhaupt kein Vertrauen“ bis 7 „Sehr großes Vertrauen“ | Vertrauen |

Die ISSP-2024-Fragen Q35/Q36 zu KI (PDF-S. 21–22) messen persönliche Sorge und persönliches Wohlbefinden, keine Regulierungspräferenz. Politbarometer 2025 enthält laut CESSDA-Abstract Fragen zu „influence of fake news, social media, and Russian interference“ im Wahlkampf; Wortlaut nicht gesehen.

### 5.3 Bewertung

Weitgehend nicht abgedeckt.

- Teilweise: staatliche Überwachung allgemein (ISSP 2016 historisch, ISSP 2024 aktuell mit offenem deutschen Wortlaut); Medienfreiheit nur als Demokratieprinzip (ESS10 B3, bereits Demokratie).
- Fehlende Daten: Rundfunkbeitrag und Auftrag des öffentlich-rechtlichen Rundfunks, Plattformpflichten, Hassrede- und Desinformationsregeln, KI-Regulierung, IP-Adressen-Speicherung, Gesichtserkennung, Digitalisierung der Verwaltung. In keinem geöffneten Bevölkerungsinstrument gefunden.
- Bewusster inhaltlicher Ausschluss (Empfehlung): Vertrauen in Medien, wahrgenommene Einseitigkeit, wahrgenommene Risiken der Online-Kommunikation nicht als medien- oder digitalpolitische Position werten.
- ESS10 A2 ist eine echte Abwägung zwischen Überwachung und Privatsphäre, aber ausdrücklich für die Pandemiebekämpfung. Eine Übertragung auf Internetüberwachung oder Strafverfolgung wäre eine Umdeutung.

Erlaubte Interpretation: nur Einzelangaben. Keine gemeinsame Dimension, kein formativer Wert.

## 6. Zugang und Rechte

ESS. Lokale Kopie und aktuelle Seite des ESS-Disclaimers (europeansocialsurvey.org/contact/disclaimer) lauten: „European Social Survey data is licensed under CC BY-NC-SA 4.0“; „European Social Survey documentation is licensed under CC BY-SA 4.0“; „The data are available without restrictions, for not-for-profit purposes.“; Änderungen seien als „‚Adapted from ESS Round X, version number X‘“ zu kennzeichnen. Folgerung (keine Rechtsauskunft): Deutsche Fragewortlaute sind als Dokumentation mit Namensnennung, Änderungskennzeichnung und Weitergabe unter CC BY-SA 4.0 zeigbar, sofern die nationalen Fragebögen als ESS-Dokumentation gelten; das habe ich nicht gesondert geprüft. Ob zusammengefasste Website-Ergebnisse als „Adapted Material“ der Daten unter die ShareAlike-Pflicht fallen, bleibt offen.

GESIS-archivierte Studien (GLES, ISSP, ALLBUS, Politbarometer, INVEDUC, ZMSBw). Belegt sind nur Zugangskategorien:

- GLES 2025 Nachwahl: „Daten und Dokumente sind für die wissenschaftliche, studentische und nicht kommerzielle Nutzung freigegeben: Zugangskategorie Safeguarded – A.“ (ZA10100-Dokumentation, PDF-S. 7, `https://access.gesis.org/dbk/79269`).
- GLES Panel W30: „A - Daten und Dokumente sind für die akademische Forschung und Lehre freigegeben.“ (ZA10119-Dokumentation, PDF-S. 4, `https://access.gesis.org/dbk/79985`).
- ISSP, ALLBUS, Politbarometer, INVEDUC: „A - Data and documents are released for academic research and teaching.“ (CESSDA-Katalogeinträge).
- ISSP-Website: „You will have to create a new user ID and password before downloading data files free of charge.“ (`https://issp.org/data-download/`).
- ZMSBw: „Die Datensätze der Bevölkerungsbefragungen zum sicherheitspolitischen Meinungsbild in Deutschland ab 1996 sind über das Datenarchiv der Gesis – Leibnizinstitut für Sozialwissenschaften zugänglich.“

Offen: (1) ob eine öffentliche, nichtkommerzielle Projektwebsite als „akademische Forschung und Lehre“ bzw. „wissenschaftliche … Nutzung“ gilt; (2) ob zusammengefasste Ergebnisse dort veröffentlicht werden dürfen; (3) ob deutsche Fragewortlaute dort angezeigt werden dürfen. Keine der geöffneten GESIS-, GLES- oder ISSP-Dokumentationen enthält einen Lizenz- oder Urheberrechtsvermerk (Textsuche nach „Lizenz“, „CC BY“, „Urheber“, „©“ ohne Treffer). Die GESIS-Nutzungsbedingungen (`https://www.gesis.org/fileadmin/user_upload/Usage_regulations.pdf`) lieferten HTTP 403; eine Archivkopie gab es nicht. Das in `outputs/loop/breadth-data-001/sources/gesis-usage-regulations.html` liegende Dokument ist nur eine Cloudflare-Prüfseite. Empfehlung: schriftliche Anfrage bei GESIS bzw. den Primärforschenden (GLES: gles@gesis.org), bevor Wortlaute oder Ergebnisse auf der Website erscheinen.

ifo Bildungsbarometer: Nutzung „nur für wissenschaftliche Zwecke“, projektbezogene Nutzungsvereinbarung, SUF über EBDC (Abrufwerkzeug, nicht wörtlich geprüft; eine direkte Abfrage scheiterte an einer Bot-Prüfung). Veröffentlichung auf einer Website und Wortlautanzeige offen.

Eurobarometer: Die Kommission erklärt für Inhalte ihrer Website „content owned by the EU on this website is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence“ (`https://commission.europa.eu/legal-notice_en`). Ob das für Eurobarometer-Fragebögen und GESIS-Datensätze gilt, habe ich nicht geprüft.

Wahl-O-Mat-Thesen und Wahlprogramme: hier nur als Beleg verwendet; keine Übernahme auf die Website vorgesehen.

## 7. Prüfung der bisherigen Angaben im Repository

`docs/abdeckung-v2.md`, Zeile „Zusätzliche Suchrubrik: Außen-, Verteidigungs- und Friedenspolitik“:

- „G25 q27e/F63/PDF147–148“: bestätigt. Die Frage steht auf PDF-S. 147; PDF-S. 148 enthält nur das Feld „Anmerkungen“.
- „Panel W34 Vorabfragebogen PDF54: Verteidigungsausgaben/Wehrpflicht“: nicht prüfbar. `https://www.gesis.org/fileadmin/admin/neu_Dateiablage_allgemein/ZA10123_fb_W34_v0-1.pdf` liefert 403, das Internet-Archiv hat keine Kopie, die lokale Datei `glespanel34-prerelease-questionnaire.html` ist eine Cloudflare-Prüfseite. Gleichlautende Items stehen in der W29-Vorabfassung auf PDF-S. 40. Die W34-Angabe sollte bis zur Prüfung als unbelegt gelten.
- „ISSP2016 Verteidigungsausgaben“: bestätigt (J006 E, PDF-S. 9).
- Es fehlen q170 (Gesellschaftsjahr mit Bundeswehroption, PDF-S. 241) und q27o (Waffen für Israel, PDF-S. 166) aus derselben Studie G25.

`docs/abdeckung-v2.md`, allgemeiner Teil: „Bildung und Wohnen werden als Binnenfacetten geführt.“ Für Bildung gibt es im 43er-Bestand nur `eduunmp` (Weiterbildung Arbeitsloser) und `gvcldcr` (Kinderbetreuung), beide primär Sozialstaat. Eine bildungspolitische Binnenfacette im engeren Sinn (Schule, Hochschule, Bund/Länder) ist damit nicht erschlossen.

`docs/empirie-plan-v2.entwurf.md`, Abschnitt „Konkrete Auswahl“: Keine der 43 Angaben hat Außen-, Bildungs- oder Medienpolitik als Primärbereich. Der Satz, Außenpolitik und digitale Überwachung blieben „begrenzte oder offene Inhaltswege“, ist zutreffend.

## 8. Priorisierte Empfehlung

Kriterien: Aktualität, Deutschlandbezug, Wahrscheinlichkeitsstichprobe, Zugang, Rechte. Alles unter dem Vorbehalt der offenen Rechtefragen aus Abschnitt 6.

1. GLES Querschnitt 2025 Nachwahl q27e und q170, danach q27o. Aktuell (2025), deutsche Originale, Registerstichprobe, dieselbe Studie wie die übrigen G25-Fragen der Matrix. q27o betrifft einen besonders sensiblen Gegenstand; der Gegenstand stand als Wahl-O-Mat-These 15 zur Wahl, die Aufnahme bleibt eine inhaltliche Entscheidung. Download: ZA10100, Version 4.0.0, DOI 10.4232/5.ZA10100.4.0.0 (GESIS-Login, Safeguarded–A; Dateiformat von mir nicht geprüft).
2. ISSP 2023 F7 a–c (Einfuhrbeschränkung, Durchsetzungsrecht internationaler Institutionen, nationale Interessen trotz Konflikten). Feldjahr 2023, deutsche Originale. Download: ZA10010, Version 1.0.0, DOI 10.4232/5.ZA10010.1.0.0; Variablenzuordnung über Variable Report prüfen (den ich nicht gesehen habe). Feldzeit, Population und Modus für Deutschland vorher binden.
3. ISSP 2024 Q28a/b und Q27 (Überwachungsrechte, Datenschutzverantwortung). Aktuellste Quelle für digitale Überwachung. Voraussetzung: deutschen Fragebogen beschaffen und Wortlaut prüfen. Download: ZA10020, Version 1.0.0.
4. Politbarometer 2025 (ZA9151 1.0.0) und 2024 (ZA8974 1.0.0): Zuerst nur die Dokumentation prüfen, ob Fragen zu Verteidigungsausgaben, Wehrpflicht, Ukraine und US-Zöllen mit stabilem Wortlaut, voller Monatsstichprobe und dokumentierter Filterung vorliegen. GESIS-Codebücher können Häufigkeiten enthalten; die Wortlautextraktion sollte deshalb ergebnisblind erfolgen.
5. ISSP 2016 J006 D/E, J007b H, J008c (Bildungs- und Verteidigungsausgaben, Studienförderung, Schulbildung) und ISSP 2019 F9 (zweites Item), F11 (zweites Item): nur als deutlich datierte historische Referenzen. Verteidigungsausgaben von 2016 liegen vor 2022 und vor der GG-Änderung 2025; ich empfehle sie nicht als Ersatz für eine aktuelle Frage. Downloads: ZA6900 Version 2.0.0 (DOI 10.4232/1.13052), ZA7600 Version 3.0.0 (DOI 10.4232/1.14009).
6. ZMSBw-Bevölkerungsbefragung: ZA-Nummern der Wellen 2022–2025 bei GESIS ermitteln und deutsche Fragebögen ergebnisblind prüfen. Die Reihe ist das spezifischste Instrument für Bundeswehr, Auslandseinsätze und Verteidigungsausgaben.
7. GLES-Panel W29/W30 (ZA10118, ZA10119): nur, wenn das Projekt nichtprobabilistische Quotenstichproben ausdrücklich zulässt und kennzeichnet. Als Bevölkerungsvergleichswert empfehle ich sie nicht.
8. Bildung: Für aktuelle Gegenstände gibt es nach meiner Prüfung keinen tragfähigen ersten Kandidaten. Nächster Schritt wäre die Dokumentation des ifo Bildungsbarometers (EBDC) ergebnisblind auf Bund/Länder-, BAföG- und Kita-Fragen zu prüfen. INVEDUC (2014) ist zu alt für eine aktuelle Referenz.
9. Medien und Digitales: Kein tragfähiger Kandidat für Rundfunkbeitrag, Plattformregulierung, KI oder IP-Speicherung gefunden. Diese Lücke sollte sichtbar bleiben und nicht durch eigene Fragen geschlossen werden, die als Originalfragen erscheinen.

Sofort mit den lokalen ESS-Ausgaben auswertbar wären nur: ESS10-SC A2 (Pandemie: Überwachen vs. Privatsphäre), D8/D9, `trstun`, `stfedu`; ESS9 `evfredu`/`ifredu`; ESS11 `trstun`, `stfedu` (Namen für ESS11 aus `data/inventar.csv`, nicht gegen das ESS11-Protokoll geprüft). Davon ist nur ESS10-SC A2 eine Präferenzabwägung, und sie ist pandemiegebunden. Ich empfehle, keine dieser Fragen als Breite in den drei Bereichen zu zählen. Falls ESS10-SC A2 aufgenommen wird, dann als historische Einzelangabe mit sichtbarem Pandemiekontext; vorher den Variablennamen in der SC-Datei bestätigen.

## 9. Offene Punkte

- Rechte zur Anzeige deutscher Wortlaute und zur Veröffentlichung zusammengefasster Ergebnisse für GLES, ISSP, Politbarometer, ZMSBw und ifo.
- GESIS-Nutzungsbedingungen nicht gelesen (403).
- GLES-Panel-W34-Angabe in `abdeckung-v2.md` unbelegt; GLES-RCS-2025-Fragebogen und GLES-Panel-W32 („foreign policy“ laut Abstract) nicht eingesehen.
- Deutscher ISSP-2024-Fragebogen nicht gefunden; Feldzeiten, Populationen und Modi der deutschen ISSP-Erhebungen 2016, 2019, 2023, 2024 nicht selbst gebunden.
- Variablennamen der ISSP-Items nicht eingesehen; ESS10-SC-Variablennamen nur aus dem CAPI-Protokoll erschlossen.
- Eurobarometer und Politbarometer-Wortlaute nicht geprüft.
- ALLBUS 2024 nicht gefunden.
- Ob das ifo Bildungsbarometer aktuelle Wellen über 2021 hinaus bereitstellt, ist offen.
- Eine BVerfG-Entscheidung zu „Rundfunkfinanzierung II“ habe ich nicht gefunden.

## Anhang A: Tatsächlich geöffnete Quellen (3.10.2026, ca. 21:00–21:50 Uhr MESZ)

Lokal:
- `AGENTS.md`, `docs/project.md`, `docs/abdeckung-v2.md`, `docs/empirie-plan-v2.entwurf.md`
- `outputs/loop/breadth-data-001/sources/`: `ess5-`, `ess6-`, `ess8-`, `ess9-`, `ess10-`, `ess11-de-questionnaire.pdf` und `.txt`, `ess8-de-showcards.pdf`, `ess10-sc-source-questionnaire.txt`, `ess*-study-access-metadata.json`, `ess-public-de-mode-metadata.json`, `ess-disclaimer.html`, `gles2025-codebook.pdf` (= GESIS-Dok. 79269), `gles2025-instrument-only.txt`, `gles2025-design-only.txt`, `gles2025-variables-only.txt`, `glespanel34-prerelease-questionnaire.html`, `gles-rcs2025-prerelease-questionnaire.html`, `gesis-usage-regulations.html`, `gles2025-landing.html` (die letzten vier sind Cloudflare-Prüfseiten)
- `data/inventar.csv` (nur Kopfzeile und Zeilen zu `trstun`/`stfedu`), `data/core-integrated-4.2-binding.json` (nur Schlüssel), `reports/loop/authors/BREADTH-DATA-001-first.md` (nur URL-Liste)

GESIS-Dokumente (access.gesis.org/dbk/…): 79269 (GLES 2025 Nachwahl), 79985 (GLES Panel W30), 74259 (GLES 2021 Nachwahl), 63842 (ISSP 2016 DE), 70592 (ISSP 2019 DE), 72588 (ISSP 2020 DE, nur Titel), 79164 (ISSP 2022 DE), 80542 (ISSP 2023 DE), 72851 (ALLBUS 2021 CAWI), 73560 (ALLBUS 2021 Inhaltsübersicht, nur Titel), 78534 (ALLBUS 2023 Variable Report, nur Etiketten), 78536 (ALLBUS 2023 Supplement, nur Titelseite), 78330 (ISSP Health Kumulation, nur Titel)

Weitere:
- http://web.archive.org/web/20250715125247/https://www.gesis.org/fileadmin/upload/GLES/Dokumente/ZA6838_fb_W29.pdf
- https://dbkapps.gesis.org/dbkoai/ (GetRecord ZA10123, ZA10100)
- https://datacatalogue.cessda.eu/api/ (Einträge ZA10123, ZA10101, ZA10118–ZA10122, ZA10002, ZA10105–ZA10108, ZA10117, ZA6900, ZA7600, ZA10010, ZA10000, ZA7650, ZA5250, ZA8974, ZA9151, ZA6961)
- https://issp.org/wp-content/uploads/2023/12/ISSP2024_final-source-questionnaire.pdf
- https://issp.org/news/, https://issp.org/data-download/
- https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS9_data_protocol_e01_4.pdf
- https://stessrelpubprodwe.blob.core.windows.net/data/round10/survey/ESS10_data_protocol_e01_7.pdf
- https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf
- https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027
- https://www.europeansocialsurvey.org/contact/disclaimer
- https://www.wahl-o-mat.de/bundestagswahl2025/app/main_app.html und …/definitionen/module_definition.js
- Wahlprogramme 2025: https://www.cdu.de/app/uploads/2025/01/km_btw_2025_wahlprogramm_langfassung_ansicht.pdf; https://www.spd.de/fileadmin/Dokumente/Beschluesse/Programm/SPD_Programm_bf.pdf; https://cms.gruene.de/uploads/assets/20250205_Regierungsprogramm_DIGITAL_DINA5.pdf; https://www.fdp.de/sites/default/files/2024-12/fdp-wahlprogramm_2025.pdf; https://www.afd.de/wp-content/uploads/2025/02/AfD_Bundestagswahlprogramm2025_web.pdf; https://www.die-linke.de/fileadmin/user_upload/Wahlprogramm_Langfassung_Linke-BTW25_01.pdf; https://bsw-vg.de/wp-content/themes/bsw/assets/downloads/BSW%20Wahlprogramm%202025.pdf
- Mello, P. A. (2024): Zeitenwende. Politics and Governance 12, Article 7346, https://doi.org/10.17645/pag.7346 (PDF über cogitatiopress.com)
- Mader, M./Schoen, H. (2023), PVS 64(3), 525–547: nur Katalogeintrag https://madoc.bib.uni-mannheim.de/64811/ (Abrufwerkzeug); PDF-Download scheiterte
- Wollmann, H. (2020), Preprint: http://amor.cms.hu-berlin.de/~h0598bce/docs/Wollmann.Bildungssektor.print_Version.pdf
- Horton, L./Perry, A. (2020): Access Some Areas. IJDC 15(1), DOI 10.2218/ijdc.v15i1.708 (nur zur Einordnung der GESIS-Zugangskategorien; nicht als Regelquelle verwendet)
- https://www.recht.bund.de/bgbl/1/2025/94/regelungstext.pdf
- https://www.nato.int/cps/en/natohq/official_texts_236705.htm
- https://www.bundestag.de/dokumente/textarchiv/2025/kw49-de-wehrdienst-1128220
- https://www.bundestag.de/dokumente/textarchiv/2026/kw26-de-ip-adressen-1191866
- https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/DE/2021/bvg21-069.html
- https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/DE/2026/bvg26-029.html
- https://www.gesetze-im-internet.de/gg/art_104c.html (Abrufwerkzeug)
- https://www.kmk.org/fileadmin/Dateien/pdf/Bildung/AllgBildung/Startchancen/2024_08_01-BLV-Startchancenprogramm.pdf (PDF-S. 1–2)
- https://zms.bundeswehr.de/de/mediathek/bevoelkerungsbefragungen-zur-bundeswehr--5324902
- https://www.ifo.de/ebdc-datensaetze/ifo-bildungsbarometer-2019-suf (Abrufwerkzeug; direkter Abruf scheiterte)
- https://commission.europa.eu/legal-notice_en
- https://data.europa.eu/api/hub/search/search (Eintrag „Standard Eurobarometer 104“, nur Titel und Verteilungsnamen)
- https://www.lto.de/… (Kommentar zum Rundfunkbeitrag, nur zur Terminprüfung gelesen, nicht verwendet)

Versucht, aber nicht geöffnet: GESIS-Nutzungsbedingungen, GLES-W34- und GLES-RCS-Vorabfragebögen (403), search.gesis.org (403), journals.sagepub.com (403), econstor-PDF Mader/Schoen (Bot-Prüfung), Eurobarometer-Umfrageseite (JavaScript-Anwendung), EUR-Lex-Seiten zu DSA und AI Act (leer).

## Anhang B: Ausgeführte Befehle in Kurzform

- `cat`/`sed`/`grep` auf lokale Projektdateien und ESS-Textfassungen
- `curl` für PDFs und HTML nach `/tmp/r1/`, `pdfinfo`, `pdftotext` (seitenweise, mit und ohne `-layout`)
- kleine Python-Skripte: seitenweise PDF-Extraktion, Stichwortsuche mit Seitenangabe, HTML-zu-Text, Abfrage der CESSDA-API und der GESIS-OAI-Schnittstelle, Auslesen der Wahl-O-Mat-Definitionsdatei
- WebSearch und WebFetch für Auffindung und einzelne Seiten
- keine Schreibvorgänge außer dieser Berichtsdatei; keine Commits

## Anhang C: Grenzen der eigenen Prüfung

- Ich habe Instrumente nach Stichworten durchsucht. Items mit ungewöhnlicher Formulierung können mir entgangen sein, besonders in GLES 2025 (358 Seiten) und den Wahlprogrammen.
- Parteipositionen sind ausgewählte Programmstellen, keine vollständige Positionsanalyse. Fehlende Treffer bedeuten nicht, dass eine Partei zu einem Thema schweigt.
- Viele GESIS-Seiten waren gesperrt; Studienmetadaten stammen dann aus CESSDA- und OAI-Einträgen.
- Feldzeiten der ESS-Runden habe ich aus dem Auftrag übernommen und nicht neu gebunden.
- Juristische Folgerungen zu Lizenzen sind Lesarten, keine Rechtsauskunft.
- Literaturplausibilität und Wahlkampfrelevanz sind keine Validierung; Übereinstimmung mit anderen KI-Berichten wäre kein Neutralitätsnachweis.

## Anhang D: Modell

Laut Laufzeitumgebung (Systemangabe): Claude Opus 5.5, Modell-ID `claude-opus-5-5[1m]`. Laut Auftrag: frischer, getrennter Claude-Subagent.
