# R6: Eurobarometer als Quelle für Vergleichsfragen

Stand: 3. Oktober 2026. Getrennter, ergebnisblinder Claude-Subagent im Auftrag R6. Grundlage: `reports/claude/auftraege/R6-eurobarometer.vollstaendig.md`. Ausgangsstand des Repositorys laut Auftrag: Commit `e9898fb`, Branch `research/life-93-claude-20261003`.

Diese Prüfung ist eine Quellen- und Rechtsrecherche, keine Rechtsberatung und keine wissenschaftliche Abnahme. Ein Themenfeld ist keine empirisch nachgewiesene Dimension. Antwortverteilungen, Prozentwerte oder Ergebnisse habe ich weder recherchiert noch berichtet.

## 1. Kernbefunde

1. **Es gibt zwei getrennte Zugangswege mit verschiedenen Regeln.**
   - **Weg A, Europäische Kommission:** Die Kommission veröffentlicht zu jeder Befragung Berichte, Datenanhänge (PDF), Länder-Factsheets und, für Standard-Eurobarometer, einen deutschen Länderbericht. Auf data.europa.eu liegen gewichtete Ergebnistabellen („Volumes“ A, AA, AP, AAP, B, BP, C, D) als xlsx- und zip-Dateien. Die Datensätze 2022–2026 tragen dort die Lizenzangabe „European Commission reuse notice“ mit Verweis auf Beschluss 2011/833/EU; zwei Datensätze von 2022 tragen „CC_BY_4_0“. Eine Regel zu KI-Systemen oder automatisierter Verarbeitung habe ich in den Rechtstexten der Kommission nicht gefunden.
   - **Weg B, GESIS:** Einzeldaten (SPSS, Stata) gibt es nur über GESIS. Laut den GESIS-Nutzungsbedingungen (gültig ab 04.02.2026) gelten für die Zugangskategorie „Open“ (früher „0“) die allgemeinen Nutzungsbedingungen mit „Registrierung + Download“. Deren § 4 verbietet die Verarbeitung mit KI-Systemen ohne Ausnahme. Für Eurobarometer-Einzeldaten gilt damit dieselbe Sperre wie für GLES, ISSP und ALLBUS. Den Vermerk in `docs/abdeckung-v2.2.md` („KI-Klausel ungeklärt“) präzisiert das: Nach dem Wortlaut gilt die Klausel auch für Eurobarometer-Einzeldaten.
2. **Deutsche Fragebögen veröffentlicht die Kommission für 2022–2026 nicht als eigene Dateien.** Laut Eurobarometer-Schnittstelle hat keine der Standard-, Spezial- und Flash-Befragungen ab 2022 eine Datei vom Typ „National questionnaire“, „Bilingual questionnaire“ oder „Technical specifications“. Die deutschen Länderfragebögen (`ZAxxxx_q_de.pdf`) und die zweisprachigen Basisfragebögen mit technischen Angaben (`ZAxxxx_bq.pdf`) liegen bei GESIS und lassen sich ohne Anmeldung herunterladen. Die Basisfragebögen tragen den Vermerk „© European Communities. The Eurobarometer questionnaires are reproduced by permission of its publishers“.
3. **Für Deutschland liegt ein vergleichbares Grunddesign vor.** Befragt werden 15-Jährige und Ältere mit der Staatsangehörigkeit eines EU-Mitgliedstaats, die in Deutschland wohnen. Die Stichprobe ist mehrstufig und zufällig (Wahrscheinlichkeitsauswahl). Pro Welle gibt es etwa 1.500 bis 1.600 Interviews. In allen geprüften Wellen außer 102.2 fanden in Deutschland nur persönliche Interviews statt (CAPI). Gewichtet wird nachträglich (Post-Stratifikation). Ein Designgewicht gibt es nicht. Ost- und Westdeutschland werden getrennt gezogen.
4. **Die Themenabdeckung ist breit, betrifft aber meist die EU-Ebene.** Gut abgedeckt sind gemeinsame Verteidigungs- und Sicherheitspolitik, Maßnahmen zum Krieg gegen die Ukraine, Verteidigungsausgaben „in der EU“, Erweiterung (auch je Bewerberland), Euro, gemeinsame Migrations-, Energie-, Klima- und Gesundheitspolitik, Plattform- und KI-Regulierung. Nationale deutsche Streitfragen fehlen fast vollständig, etwa Wehrpflicht, Rentenniveau, Bürgerversicherung, Mietregulierung, BAföG und Rundfunkbeitrag. Ausnahmen sind zwei Spezialmodule von 2022 (Klimamaßnahmen „in Deutschland“; Ausgabenwünsche an die Bundesregierung für Gesundheit, Rente, Pflege, Bildung und Wohnen) sowie die Aussage „Deutschland sollte Flüchtlingen helfen“.
5. **Vergleiche mit Wählergruppen sind mit Eurobarometer nicht möglich.** Die geprüften deutschen Standard-Fragebögen enthalten keine Frage nach Bundestagswahl oder Wahlabsicht. Nur die Europawahl-Nachbefragung 2024 (EB 101.5) fragt nach der Europawahlentscheidung 2024 und 2019. Diese Welle enthält aber keine der hier gesuchten Politikfragen.
6. **Ob die veröffentlichten Tabellen für Einzelvergleiche genügen, ist nur teilweise geklärt.** Belegt sind Gewichtung, Feldzeit und Fallzahl je Land. Ob die Tabellen für Deutschland alle Antwortkategorien enthalten, also auch „Weiß nicht“ und „Verweigert“, und welche Basis angegeben ist, habe ich nicht geprüft. Dafür hätte ich Ergebnistabellen öffnen müssen. Für Einzelvergleiche mit der Bevölkerung reichen die Tabellen voraussichtlich (Vermutung). Für Wählergruppen reicht keine Quelle.

## 2. Zugang

### 2.1 Was die Kommission selbst veröffentlicht

Quelle: Eurobarometer-Schnittstelle `https://europa.eu/eurobarometer/api/survey/get/latest?nb=5000` und `…/survey/get/one?id=<ID>`, Abruf 03.10.2026, ca. 20:57–21:05 UTC. Ausgewertet habe ich nur Metadaten: Titel, Feldzeit, Dateityp, Sprache und Land. Beschreibungstexte und „keyFindings“ habe ich nicht ausgegeben (siehe Abschnitt 9).

- Die Schnittstelle führt **10 Standard-Eurobarometer** (STD96 bis STD105, veröffentlicht 04.04.2022 bis 08.05.2026) und **70 Spezial-Eurobarometer** mit Veröffentlichung ab 2022.
- Für Spezial- und Standardbefragungen 2022–2026 kommen nur diese Dateitypen vor: Bericht (REPORS), Zusammenfassung, Länder-Factsheet auf Englisch (FACTEN) und in Landessprache (FACTLL), Infografik, Datenanhang (DATANX, PDF), Erste Ergebnisse, Präsentation, nationale Präsentation und nationaler Bericht (NATREP).
- **Für Deutschland** gibt es bei den Standard-Eurobarometern einen deutschen Länderbericht (NATREP, Sprache de) nur zu den Herbst- und Winterwellen (STD96, 98, 100, 102, 104). Datenanhang und Berichte gibt es auf Deutsch, bei Spezialbefragungen meist das deutsche Länder-Factsheet. Beispiel STD104 (ID 3378): Datenanhang de/en/fr, nationaler Bericht „national report_de_de.pdf“, Factsheet DE auf Englisch.
- Die Schnittstelle kennt auch die Typen „National questionnaire“ (NATQUE), „Bilingual questionnaire“ (BILQUE), „Questionnaire“ (QUEANX), „Technical specifications“ (TECANX) sowie Rohdaten im SPSS- und CSV-Format (SAVRAW, CSVRAW) (`…/metadata/deliverable_type/get/all`). Bei keiner Befragung ab 2022 sind solche Dateien veröffentlicht.
- **Ergebnistabellen auf data.europa.eu** (`https://data.europa.eu/api/hub/search/datasets/<id>`): Beispiele sind STD104 (`s3378_104_1_std104_eng`): Volumes A, AA, AP, AAP, B, BP, C (zip nach Ländergruppen, Deutschland in „C_AT-HR“), D; STD105, SP564, SP565, SP572 entsprechend. Die Dateien liegen unter `webgate.ec.europa.eu/ebsm/api/public/odp/download?key=…`. Die Inhalte beschreibt das Portal so (Datensatzbeschreibung STD98 und SP572, wörtlich):
  - Volume A: „frequencies and means or other synthetic indicators … describing distribution patterns of (weighted) replies for each country or territory and for (weighted) EU results“.
  - Volume C: „(labelled) weighted frequencies and means … for each country or territory surveyed separately and cross-tabulated by some 20 socio-demographic, socio-political or other variables (including a regional breakdown)“.
  - Volume D: „compares to previous polls in (weighted) frequencies and means … shifts for each country or territory foreseen in Volume A“.
- Die Eurobarometer-Seite „About“ (`https://europa.eu/eurobarometer/about/eurobarometer`) schreibt: „Data presented in the tables of results (‘Volumes’) available through the Open Data Portal are also weighted.“ Die Seite wird erst im Browser zusammengesetzt. Den Text habe ich aus ihrem JavaScript-Bündel gelesen (`angular/src_app_features_about_about_module_ts.4514644fc63dcdf2.js`).

### 2.2 Einzeldaten über GESIS

- Laut GESIS-OAI-Eintrag ZA9130 gibt es die Dateien `ZA9130_v1-0-0.dta` und `.sav`, den Basisfragebogen `ZA9130_bq.pdf`, Länderfragebögen (`ZA9130_q_de.pdf` u. a.) und eine Readme. Zugangskategorie: „0 - Daten und Dokumente sind für jedermann freigegeben.“ Version 1.0.0 vom 29.07.2026, doi:10.4232/1.14793.
- GESIS-Seite „Data & Documentation“ (Wayback 27.07.2026): „For accessing data through the data catalogue you need to sign in with user name (your e-mail address) and password. New users have to register first.“ – „The general regulations on usage of GESIS Data Catalogue resources apply.“ (Link auf `gesis.org/en/institute/data-usage-terms`).
- GESIS-FAQ (Wayback 27.07.2026): „All Eurobarometer surveys are available through the GESIS Data Catalogue after a free-of-charge registration has been completed.“ – Einzeldaten erscheinen „[u]sually … about 6 to 12 months after fieldwork“. Beispiel: STD105 wurde am 08.05.2026 veröffentlicht, ZA9144 am 13.08.2026.
- Die Readme zu ZA9130 bezeichnet die Daten als „Archive pre-release“: „This dataset edition has not yet passed the complete archive processing and documentation“.
- Fragebögen und Readme lassen sich ohne Anmeldung herunterladen (`https://access.gesis.org/dbk/<Dokument-ID>`, HTTP 200 mit Dateinamen). Die Datensätze selbst habe ich nicht angefragt.

## 3. Nutzungsbedingungen (wörtlich)

### 3.1 Europäische Kommission

**Beschluss 2011/833/EU** über die Weiterverwendung von Kommissionsdokumenten, ABl. L 330 vom 14.12.2011, S. 39 (`https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32011D0833`, Abruf ca. 20:56 UTC; EUR-Lex vermerkt „In force“, „Date of end of validity: No end date“, keine Änderungsrechtsakte):
- Art. 2 Abs. 1: Der Beschluss gilt für öffentliche Dokumente, „die von der Kommission oder von öffentlichen und privaten Stellen in ihrem Namen erstellt werden“ und veröffentlicht wurden oder „aus wirtschaftlichen oder praktischen Gründen nicht veröffentlicht worden sind, beispielsweise Studien, Berichte und andere Daten“.
- Art. 2 Abs. 2 lit. b: Er gilt nicht für „Dokumente, deren Weiterverwendung die Kommission nicht gestatten kann, weil sie geistiges Eigentum Dritter sind“.
- Art. 3 Nr. 2: „Weiterverwendung“ ist „die Nutzung von Dokumenten … für kommerzielle oder nichtkommerzielle Zwecke“.
- Art. 4: „Alle Dokumente stehen zur Weiterverwendung zur Verfügung: a) für kommerzielle oder nichtkommerzielle Zwecke …; b) gebührenfrei …; c) ohne Einzelbeantragung“.
- Art. 6 Abs. 2: Bedingungen können sein: „a) die Verpflichtung des Nutzers, die Quelle des Dokuments anzugeben; b) die Verpflichtung, die ursprüngliche Bedeutung oder Botschaft des Dokuments nicht verzerrt darzustellen; c) den Haftungsausschluss der Kommission“.

**Rechtlicher Hinweis der Kommission** (`https://commission.europa.eu/legal-notice_de`, Abruf ca. 20:56 UTC): „Die Weiterverwendungspolitik der Kommission unterliegt dem Beschluss der Kommission vom 12. Dezember 2011 über die Weiterverwendung von Kommissionsdokumenten. Sofern nicht anders (z. B. in individuellen Copyright-Vermerken) angegeben, werden im Eigentum der Kommission befindliche Inhalte auf dieser Website zu den Bedingungen der Lizenz Creative Commons Attribution 4.0 International (CC BY 4.0) zur Verfügung gestellt. Dies bedeutet, dass die Weiterverwendung mit ordnungsgemäßer Nennung der Quelle und unter Hinweis auf Änderungen gestattet ist.“ Gleichlautend: `https://european-union.europa.eu/legal-notice_en`.
- Zu KI enthält der Hinweis nur den Abschnitt „Nutzung künstlicher Intelligenz beim Erstellen von Inhalten“. Er betrifft Inhalte, die die Kommission selbst mit KI-Werkzeugen erstellt. **Eine Regel zur Verarbeitung durch Nutzende mit KI-Systemen, zu automatisierter Verarbeitung oder zu Text- und Data-Mining habe ich nicht gefunden.** Das ist keine Erlaubnis im Sinne einer ausdrücklichen Regel.

**Eurobarometer-Website, Abschnitt „Legal Notice“** (Quelle wie 2.1): „The copyright for the editorial content of this website, which is owned by the EU, is licensed under the Creative Commons Attribution 4.0 International licence. This means that you can re-use the content provided you acknowledge the source and indicate any changes you have made.“ – „The publications of EU institutions, bodies, offices and agencies, may be downloaded and reproduced provided the source is acknowledged.“

**data.europa.eu, Lizenzangabe je Datei:** STD104 und andere Wellen 2023–2026: `{"id": "COM_REUSE", "label": "European Commission reuse notice", "resource": "http://data.europa.eu/eli/dec/2011/833/oj"}`. SP527 und SP529 (2022): `CC_BY_4_0`.

**Beschluss C(2019) 1655** zur Einführung von CC BY 4.0: Den Originaltext habe ich nicht gefunden. Die Kommission verweist im rechtlichen Hinweis nur auf den Beschluss von 2011.

### 3.2 Europäisches Parlament (betrifft EP-Module in gemeinsamen Wellen)

Einige GESIS-Wellen enthalten Fragen im Auftrag des Parlaments, etwa EB 97.3 Block QA, EB 103.4 Block QA und EB 101.5. Rechtlicher Hinweis (`https://www.europarl.europa.eu/legal-notice/en/`; direkt HTTP 202 ohne Inhalt, gelesen über Wayback-Kopie vom 02.10.2026): „the reuse (reproduction or use) of textual data and multimedia items which are the property of the European Union … is authorised, for personal use or for further non-commercial or commercial dissemination, provided that the entire item is reproduced and the source is acknowledged.“ – „Any partial reproduction of data or multimedia items from this website must also cite the URL link of the complete item or the web page from which it was sourced.“ Eine KI-Regel habe ich nicht gefunden.

### 3.3 GESIS

**Datennutzungsbedingungen, „Gültig ab: 04.02.2026“.** Direktabruf HTTP 403. Gelesen über Wayback: HTML-Fassung vom 30.03.2026 (`web.archive.org/web/20260330121100/https://www.gesis.org/institut/datennutzungsbedingungen`) und PDF-Fassung vom 30.03.2026 (`…/20260330154523/…/Nutzungsbedingungen.pdf`, SHA-256 `2a46f4ff…`). Neuere Kopien gibt es laut Wayback-Verzeichnis nicht.
- Präambel: „Die Originaldaten (im Folgenden „Datenbasis“) werden ausschließlich auf Grundlage dieser Nutzungsbedingungen bereitgestellt.“
- § 3: „Für jede Bereitstellung der Datenbasis durch GESIS ist die Registrierung und die Zustimmung zu diesen Nutzungsbedingungen durch den Nutzer / die Nutzerin erforderlich.“
- § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“ – „Eine Weitergabe der bereitgestellten Datenbasis an Dritte ist nicht gestattet.“
- **Tabelle der Zugangskategorien** in § 2: Sie steht als Bild auf PDF-Seite 3, im HTML fehlt sie. Ich habe sie aus dem Bild gelesen. Erste Zeile: „Open | Allgemeine Nutzungsbedingungen | Freier Zugang | Registrierung + Download | 0“. Kopfzeile der alten Kategorien: „(werden in 2026 abgelöst)“. Die Spalte der alten Kategorien enthält auch den Text „Freier Zugang (ohne Registrierung)“. Die Zuordnung zu Zeilen ist im Bild nicht eindeutig.
- Folgerung: Auch für Eurobarometer-Einzeldaten der Kategorie 0/Open verlangen die Bedingungen Registrierung und Zustimmung. Das KI-Verbot in § 4 hat keinen Vorbehalt „soweit nicht ausdrücklich anders gekennzeichnet“. Ob „Freier Zugang“ in der Tabelle die Zweckbindung in § 1 („nur für wissenschaftliche Nutzungen im Rahmen eines zeitlich befristeten Vorhabens“, mit Vorbehalt „soweit nicht ausdrücklich anders gekennzeichnet“) aufhebt, ist **offen**.
- **Fragebögen:** GESIS-Seite „Data & Documentation“ (Wayback 27.07.2026): „Eurobarometer questionnaires are reproduced with the licence granted by the European Commission, DG Communication, 200 rue da le Loi, B-1049 Brussels (© European Communities).“ Danach liegen die Rechte an den Fragetexten bei der EU. Offen ist, ob GESIS heruntergeladene Fragebogen-PDFs als Teil der „Datenbasis“ ansieht. Die Bedingungen definieren diese als „Originaldaten“.

### 3.4 Zusammenfassung je Prüfpunkt

| Prüfpunkt | Kommission (Tabellen, Berichte) | GESIS (Einzeldaten) |
|---|---|---|
| Kommerziell / nichtkommerziell | beides erlaubt (Beschluss Art. 3 Nr. 2, Art. 4) | kommerziell verboten, „soweit nicht ausdrücklich anders gekennzeichnet“ (§ 4) |
| Zusammengefasste Ergebnisse öffentlich zeigen | erlaubt mit Quellenangabe, Kennzeichnung von Änderungen, ohne verzerrte Darstellung (Art. 6; CC BY 4.0) | „Zulässig sind zusammenfassende Darstellungen der Daten, wie sie in wissenschaftlichen Arbeiten und Vorträgen üblich sind.“ (§ 5, PDF S. 4); Website-Nutzung offen |
| Deutsche Fragewortlaute zeigen | Rechte bei der EU (© European Communities). Weiterverwendung nach Beschluss und CC BY plausibel. Bezugsquelle ist aber GESIS; ausdrückliche Bestätigung fehlt (Vermutung) | siehe links; Rolle von GESIS als Bezugsquelle offen |
| Dateien weitergeben | keine Einschränkung im Beschluss gefunden | verboten (§ 4) |
| KI / automatisierte Verarbeitung | **keine Regel gefunden** | **verboten** ohne Ausnahmegenehmigung (§ 4) |

## 4. Deutschland: Wellen, Feldzeit, Stichprobe, Modus, Fallzahl, Gewichte

**Population** (alle Wellen, z. B. GESIS-OAI ZA9130 „universe“; Technische Spezifikation EB 104.1): „Bevölkerung der jeweiligen Nationalitäten und EU-Bürger der 27 Mitgliedsstaaten der EU, wohnhaft in den jeweiligen Mitgliedsstaaten, im Alter von 15 Jahren und älter.“ Die Population ist also **nicht** die deutsche Wahlbevölkerung (deutsche Staatsangehörige ab 18) und weicht auch von der ESS-Population ab.

**Stichprobe** (Technische Spezifikation EB 104.1, `ZA9130_bq.pdf` S. 34): „The basic sample design applied in all countries and territories is a stratified multi-stage, random (probability) one.“ Die Schichtung erfolgt nach NUTS-Region und Urbanität (DEGURBA). Ausgangspunkt jedes Sample-Punkts ist eine zufällige Koordinate, danach folgt „random route“ und eine Zufallsauswahl im Haushalt mit bis zu vier Kontaktversuchen. Laut GESIS-Seite „Population, Countries & Regions“ (Wayback 27.07.2026) werden Ost- und Westdeutschland getrennt gezogen, Berlin zählt seit EB 71.3 zu Ostdeutschland.

**Gewichte:**
- Technische Spezifikation EB 104.1, S. 37: „Weights are used to match the responding sample to the universe on gender by age, region and degree of urbanisation.“
- Readme ZA9130: Post-Stratifikation nach „sex, age, region NUTS II … and size of locality“. Weiter: „A design weight which would adjust for unequal selection probabilities (depending on the household size) is not made available.“ Und: „Meaningful descriptive results for … countries with separate samples (Germany) require population size weighting.“
- GESIS-Gewichtungsübersicht (Wayback 27.07.2026): „The actual calculus is not disclosed.“ Seit EB 95.3 passt das Gewicht `w1de` die Ost- und Westteilstichprobe an ihre Anteile im vereinten Deutschland an.

**Wellen mit geprüften Fragen.** Quellen der Feldzeit und Fallzahl für Deutschland: Technische Spezifikation im jeweiligen `ZAxxxx_bq.pdf` (Text oder Tabellenbild), Feldzeit zusätzlich GESIS-OAI. Institut laut Tabelle.

| GESIS-Welle | Kommissionsbezeichnung (Auswahl) | ZA, Version, DOI | Feldzeit DE | N DE | Institut DE | Modus DE |
|---|---|---|---|---|---|---|
| EB 97.3 | SP526 Key challenges 2022, EP-Frühjahr 2022 | ZA7888 v1.0.0, 10.4232/1.14055 | 19.04.–05.05.2022 | 1.514 | Kantar Deutschland | CAPI 1.514 |
| EB 97.4 | SP527 Fairness green transition, SP528, SP529 Fairness/inequality | ZA7901 v2.0.0, 10.4232/1.14279 | 01.06.–22.06.2022 | 1.520 | Kantar Deutschland | CAPI 1.520 |
| EB 97.5 | STD97 | ZA7902 v1.0.0, 10.4232/1.14010 | 20.06.–14.07.2022 | 1.507 | Kantar Deutschland | CAPI 1.507 |
| EB 98.2 | STD98 | ZA7953 v1.0.0, 10.4232/1.14081 | 13.01.–02.02.2023 | 1.532 | Kantar Deutschland | CAPI 1.532 |
| EB 99.2 | SP534, SP535 Discrimination | ZA7955 v1.0.0, 10.4232/1.14292 | 13.04.–02.05.2023 | 1.525 | Mantle Germany (Kantar Public) | CAPI 1.525 |
| EB 99.3 | SP536–SP539 (u. a. SP538 Climate, SP539 Tobacco) | ZA7996 v1.0.0, 10.4232/1.14166 | 11.05.–31.05.2023 | 1.507 | Mantle Germany (Kantar Public) | CAPI 1.507 |
| EB 99.4 | STD99 | ZA7997 v1.0.0, 10.4232/1.14167 | 02.06.–20.06.2023 | 1.553 | Mantle Germany (Kantar Public) | CAPI 1.553 |
| EB 100.2 | STD100 | ZA8779 v1.0.0, 10.4232/1.14363 | 24.10.–13.11.2023 | 1.527 | Mantle Germany (Kantar Public) | CAPI 1.527 |
| EB 100.3 | SP543, SP544 Trade, SP545 Gender stereotypes | ZA8840 v1.0.0, 10.4232/1.14504 | 15.01.–04.02.2024 | 1.537 | Mantle Germany (Verian) | CAPI 1.537 |
| EB 101.1 | SP546 Social Europe, SP547, SP548 | ZA8841 v1.0.0, 10.4232/1.14461 | 08.02.–26.02.2024 | 1.521 | Mantle Germany (Verian) | CAPI 1.521 |
| EB 101.3 | STD101 | ZA8843 v1.0.0, 10.4232/1.14376 | 04.04.–29.04.2024 | 1.559 | Mantle Germany (Verian) | nicht geprüft |
| EB 101.4 | SP553, SP554 AI & work, SP555 Energy | ZA8844 v1.0.0, 10.4232/1.14471 | 29.04.–21.05.2024 | 1.603 | Mantle Germany (Verian) | nicht geprüft |
| EB 102.1 | SP557 Science & technology, SP558 | ZA8904 v1.0.0, 10.4232/1.14519 | 13.09.–04.10.2024 | 1.570 | Mantle Germany (Verian) | CAPI (CAVI laut Text „only in“ CZ, DK, MT, NL, FI, SE) |
| EB 102.2 | STD102 | ZA8905 v1.0.0, 10.4232/1.14726 | 10.10.–31.10.2024 | 1.542 | Mantle Germany (Verian) | CAPI und CAVI: Deutschland ist im Technischen Bericht unter den CAVI-Ländern genannt, Aufteilung nicht gefunden |
| EB 103.2 | SP562–SP566 (SP564 Enlargement, SP565 Climate, SP566 Digital Decade 2025) | ZA9127 v1.0.0, 10.4232/1.14752 | 19.02.–10.03.2025 | 1.510 | Mantle Germany (Verian) | CAPI 1.510 |
| EB 103.3 | STD103 | ZA9128 v1.0.0, 10.4232/1.14782 | 26.03.–15.04.2025 | 1.506 | Mantle Germany (Verian) | CAPI 1.506 |
| EB 103.4 | EP-Frühjahr 2025, SP567, SP568 Democracy | ZA9129 v1.0.0, 10.4232/1.14785 | 05.05.–26.05.2025 | 1.530 | Mantle Germany (Verian) | CAPI 1.530 |
| EB 104.1 | STD104 | ZA9130 v1.0.0, 10.4232/1.14793 | 09.10.–29.10.2025 | 1.516 | Mantle Germany (Verian) | CAPI 1.516 |
| EB 105.1 | SP571, SP572 Digital Decade 2026, SP573 | ZA9143 v1.0.0, 10.4232/1.14834 | 05.02.–24.02.2026 | 1.513 | Mantle Germany (Verian) | CAPI 1.513 |
| EB 105.2 | STD105 | ZA9144 v1.0.0, 10.4232/1.14813 | 12.03.–01.04.2026 | 1.515 | Mantle Germany (Verian) | CAPI 1.515 |

Zuordnung von Kommissionsbefragung und GESIS-Welle: über gleiche Feldzeiten, GESIS-Titel (z. B. ZA9127, ZA9143) und die Fragebogeninhalte. Bei ZA7888, ZA7901 und ZA7996 habe ich die Zuordnung nur über Feldzeit und Inhalt hergestellt (Vermutung, inhaltlich stimmig).

Rücklaufquoten Deutschland (CAPI) laut Technischer Spezifikation: EB 97.5 22,8 %, EB 99.4 23,9 %, EB 104.1 33,8 % (Methodenangabe, kein Befragungsergebnis). Ausweisung der Stichprobenfehler laut Technischer Spezifikation EB 104.1, S. 38: bei N = 1.500 und einem beobachteten Anteil von 50 % ±2,5 Prozentpunkte (95 %).

Keine Standard- oder Spezialbefragung 2022–2026 im Prüfumfang nutzt in Deutschland eine Quotenstichprobe. Flash Eurobarometer 574 „The European Union in Defence and Space“ (Feldzeit 05.–12.01.2026, ZA9126) ist laut DataCite „Non-probability: Quota“ und „SelfAdministeredQuestionnaire.WebBased“. Diese Befragung liegt außerhalb des Auftrags und eignet sich wegen der Quotenauswahl nicht als Bevölkerungsreferenz.

## 5. Deutsche Fragebögen

**Fundort:** GESIS-Datenkatalog, je Studie `ZAxxxx_q_de.pdf` (deutscher Länderfragebogen) und `ZAxxxx_bq.pdf` (englisch-französischer Basisfragebogen mit Technischer Spezifikation). Direkte Dokumentlinks: `https://access.gesis.org/dbk/<ID>`. Die IDs habe ich über Kopfzeilen-Abfragen ermittelt (Abschnitt 10.2).

| Studie | `_q_de` (ID, SHA-256-Präfix) | `_bq` (ID) |
|---|---|---|
| ZA7888 | 73682, `884a8c88` | 73675 |
| ZA7901 | 77741, `64d46a97` | 74783 |
| ZA7902 | 73858, `058da3f1` | 73843 |
| ZA7953 | 74572, `7d75ca1a` | 74557 |
| ZA7955 | 80210, `e85381f8` | 80203 |
| ZA7996 | 80333, `23a68215` | 80325 |
| ZA7997 | 76890, `34a2d779` | 76875 |
| ZA8779 | 77815, `ef89be0c` | 77803 |
| ZA8840 | 80395, `60a089c6` | 80387 |
| ZA8841 | 78815, `3a8c5bb6` | 78791 |
| ZA8843 | 78857, `a8607748` | 78845 |
| ZA8844 | 79062, `c3395197` | 79055 |
| ZA8904 | 80715, `872fea44` | 80704 |
| ZA8905 | 80658, `8bf06db5` | 80646 |
| ZA9127 | 81618, `22426918` | 81611 |
| ZA9128 | 81485, `7c1c5d74` | 81473 |
| ZA9129 | 81873, `ff8b3694` | 81866 |
| ZA9130 | 81730, `81c26b19` (identisch mit R3) | 81719 |
| ZA9143 | 82391, `7769f72a` | 82384 |
| ZA9144 | 81922, `0ad783e3` | 81910 |

**Form:**
- Bis etwa ZA8842 sind die Fragebögen rein deutsche Feldfragebögen mit Fragenummern (QA1, QB3 …) und internen Kennungen in den Forschungsnotizen (z. B. „EB96.3 SE037“).
- Ab ZA8843 sind es zweispaltige Übersetzungsexporte (Englisch/Deutsch) mit interner Kennung („SE037/title QB1“).
- Die Fragenummern wechseln zwischen Wellen. Die internen Kennungen (SE037, ST0350 usw.) bleiben stabil und eignen sich als Fundstelle.

**Antwortformat und fehlende Werte:** Die Forschungsnotizen schreiben fast überall „HIDESPECIAL CODE 999“ vor, teils auch 997 („Verweigert“). Die Interviewer lesen „Weiß nicht“ also nicht vor. Diese Antwort wird nur spontan erfasst. Eine Website, die „Weiß nicht“ sichtbar anbietet, misst anders.

## 6. Themenabdeckung: Originalfragen zu politischen Präferenzen

Aufgenommen habe ich nur Präferenzen und Prinzipien. Nicht aufgenommen habe ich:
- Wahrnehmungen (z. B. Desinformation „häufig begegnet“, ST0751, ST0015),
- Vertrauen,
- Bewertungen von Regierung, EU oder Plattformen (z. B. ST0349 Zufriedenheit mit der Ukraine-Reaktion; ST1059 „tun große Online-Plattformen genug“; SP568 QC17),
- eigenes Verhalten,
- reine Prioritätenlisten ohne Richtung (ST0746/ST0747, ST0748/ST0749, Budgetwünsche SE053). Prioritätenlisten nenne ich nur dort, wo sonst nichts vorliegt, und kennzeichne sie.

Wortlaute sind wörtlich aus dem deutschen Länderfragebogen übernommen, Seitenangaben beziehen sich auf die PDF-Seite.

### 6.1 Außen-, Verteidigungs- und Friedenspolitik (bisher keine Frage im Profil)

- **SE037, Item „gemeinsame Verteidigungs- und Sicherheitspolitik“.** In allen Standardwellen. EB 104.1 QB1, ZA9130_q_de S. 10: „Wie ist Ihre Meinung zu den folgenden Aussagen? Bitte sagen Sie für jede Aussage, ob Sie dafür oder dagegen sind.“ – „Eine gemeinsame Verteidigungs- und Sicherheitspolitik der EU-Mitgliedstaaten.“ / „Eine gemeinsame Außenpolitik der Mitgliedstaaten der EU“. Antworten: Dafür / Dagegen; „Weiß nicht“ verborgen. EB 105.2 QB2 (ZA9144 S. 12): „Eine gemeinsame Sicherheits- und Verteidigungspolitik der Mitgliedstaaten“ (geänderter Wortlaut, Kennzeichen „(M)“).
- **ST0350, Maßnahmen zum Krieg gegen die Ukraine.** EB 97.5 bis 105.2. EB 104.1 QD2, S. 18: „Die EU hat als Reaktion auf die russische Invasion in der Ukraine eine Reihe von Maßnahmen ergriffen. Inwieweit stimmen Sie jeder dieser Maßnahmen zu oder nicht zu?“ Items:
  - „Verhängung von Wirtschaftssanktionen gegen die russische Regierung, russische Unternehmen und russische Bürger (einschließlich der Verwendung von eingefrorenen russischen Vermögenswerten, um die Unterstützung für die Ukraine zu finanzieren)“; der Zusatz zu den Vermögenswerten ist neu ab 104.1;
  - „Finanzierung des Kaufs und der Lieferung von militärischer Ausrüstung für/an die Ukraine“;
  - „Aufnahme von Kriegsflüchtlingen in der EU“;
  - „Bereitstellung finanzieller und humanitärer Unterstützung für die Ukraine“; bis 102.2 nur „finanzieller Unterstützung“;
  - „Gewährung des Bewerberstatus als potenzielles EU-Mitglied für die Ukraine“; ab 99.4.
  Skala: Stimme voll und ganz zu … Stimme überhaupt nicht zu. In EB 97.5 bis 100.2 kam hinzu: „EU-weites Sendeverbot für staatliche Medien wie Sputnik und Russia Today“ (z. B. EB 98.2 QE2, ZA7953_q_de S. 41).
- **ST0359, Aussagen zur Verteidigung.** EB 97.5 bis 105.2. EB 104.1 QD3, S. 19: „Bitte geben Sie an, inwieweit Sie den folgenden Aussagen zustimmen oder nicht zustimmen.“ Items:
  - „Die EU sollte die Ukraine unterstützen, bis dauerhaft gerechter Frieden herrscht“; ab 103.3;
  - „Die Zusammenarbeit auf EU-Ebene sollte bei Verteidigungsfragen verstärkt werden“;
  - „In der EU sollte mehr Geld für Verteidigung ausgegeben werden“;
  - „Die Beschaffung militärischer Ausrüstung durch die Mitgliedstaaten sollte besser koordiniert werden“;
  - „Die EU muss ihre Kapazitäten zur Produktion von militärischer Ausrüstung stärken“.
  In 105.2 entfallen laut Notiz die Items 3, 6–13.
- **SP526 (EB 97.3) QC2, ZA7888_q_de S. 119:** „Sind Sie der Meinung, dass die EU-Mitgliedstaaten gemeinsam handeln sollten, wenn es um Folgendes geht?“ – u. a. „Verteidigung des EU-Gebiets“, „Beteiligung an UN-Friedensmissionen“. Antworten: „Ja, voll und ganz“ … „Nein, überhaupt nicht“. Nur 2022.
- **Handel:** ST0939 Item 2, EB 105.2 QB12, S. 17: „Die EU sollte als Reaktion Zölle einführen, um ihre Interessen zu verteidigen (z. B. wenn andere Länder ihre Zölle auf Importe aus der EU erhöhen)“. Ebenfalls in EB 103.3, in 104.1 nicht gestellt.
- **Nicht abgedeckt:** Wehrpflicht und Wehrdienst, Verteidigungsausgaben Deutschlands, deutsche Waffenlieferungen als nationale Entscheidung, Rüstungsexporte, NATO, China-Politik als Präferenz. Die Verteidigungs-Items beziehen sich auf die EU („in der EU“, „auf EU-Ebene“).

### 6.2 Medien und Digitalpolitik (bisher keine eigene Frage)

- **SP572 Digital Decade 2026 (EB 105.1).**
  - QB5 Item 6, ZA9143_q_de S. 18: „Inwieweit stimmen Sie den folgenden Aussagen zu oder nicht zu? Die EU sollte in den nächsten 10 Jahren mit EU-Mitgliedstaaten zusammenarbeiten, um … die Regulierung von Online-Plattformen zu stärken (z. B. soziale Online-Netzwerke, Marktplätze, App-Stores usw.)“.
  - QB12, S. 21: „Wenn Sie an künstliche Intelligenz (KI) denken, welche der folgenden Aussagen kommt Ihrer Meinung am nächsten?“ – „Die Entwicklung von KI sollte sorgfältig reguliert werden, um die Sicherheit zu gewährleisten, auch wenn dies bedeutet, dass KI- Entwickler/Innen gewissen Einschränkungen unterliegen.“ / „Die Entwicklung von KI sollte mit so wenigen Einschränkungen wie möglich erlaubt sein, auch wenn dies gewisse Sicherheitsrisiken mit sich bringt.“ Diese Frage nennt die Abwägung ausdrücklich.
- **SE035 Item 5** (EB 97.5 bis 104.1, nicht in 105.2), EB 104.1 QB2, S. 11: „Es sollte in der EU eine gerechte Besteuerung großer Technologieunternehmen geben“.
- **SE037/SE034 „Ein digitaler Binnenmarkt innerhalb der EU“** (Dafür/Dagegen), EB 97.5 bis 103.3 und 105.2.
- **SP566 (EB 103.2) QE6, ZA9127_q_de S. 97:** „Wie dringend sind Ihrer Meinung nach die Maßnahmen von öffentlichen Behörden zum Schutz von Kindern im Internet …?“ – u. a. „Hinsichtlich der Einführung von Mechanismen zur Alterskontrolle, um Inhalte einzuschränken, die altersunangemessen sind“. Dringlichkeitsskala.
- **SP566 QE4 Item 7, S. 96:** „Bekämpfung und Minimierung des Problems von Fake News und Desinformationen im Internet“ als Wichtigkeit für Behörden. Die Frage hat keine Gegenposition.
- **SP554 (EB 101.4) QB11, ZA8844_q_de S. 16:** Wichtigkeit von Regeln für KI am Arbeitsplatz, u. a. „Verbot vollständig automatisierter Entscheidungsprozesse“, „Einschränkung der automatischen Überwachung von Beschäftigten“. Wichtigkeitsskala, ohne Gegenposition.
- **Desinformation:** Präferenzfragen gibt es nur indirekt: Sendeverbot für RT/Sputnik (6.1), SP568 QC9 (Wichtigkeit von Transparenzmaßnahmen im Online-Wahlkampf, ZA9129_q_de S. 56). Die Standardfragen ST0751 und ST0015 messen Wahrnehmungen.
- **Nicht abgedeckt:** öffentlich-rechtlicher Rundfunk und Rundfunkbeitrag (nur Wahrnehmung ST0014), Speicherung von IP-Adressen, Gesichtserkennung, Hassrede-Regeln als Abwägung mit Meinungsfreiheit.

### 6.3 Gesundheit und Pflege (bisher keine Frage)

- **SE037 Item „Eine gemeinsame EU-Gesundheitspolitik“** (Dafür/Dagegen), alle Standardwellen, z. B. EB 104.1 S. 10. Betrifft nur die EU-Ebene.
- **SP529 (EB 97.4) QC5b, ZA7901_q_de S. 65:** „Wenn Sie an die Steuern und Sozialversicherungsbeiträge denken, die Sie möglicherweise zahlen müssen, würden Sie sich wünschen, dass die deutsche Bundesregierung weniger, gleich viel oder mehr Geld für die folgenden Bereiche ausgibt?“ Items u. a. „Gesundheitswesen (z. B. öffentliche Krankenhäuser, Krankenkassenzuschüsse, psychische Gesundheitsversorgung)“, „Langzeitpflege (z. B. Pflegehilfe für ältere Menschen zu Hause oder in Pflegeheimen)“. Fünfstufige Skala (viel mehr … viel weniger). Besonderheit: Laut Notiz „ASK ALL“ zeigt der Bildschirm die aktuellen jährlichen Pro-Kopf-Ausgaben je Bereich. Eine Website müsste dieselbe Information zeigen, Stand 2022.
- **SP539 (EB 99.3) QD16, ZA7996_q_de S. 61:** „Wären Sie für folgende Maßnahmen oder nicht dafür?“ – u. a. neutrale Zigarettenverpackungen, „Rauchverbot in Außenbereichen …“, „Verbot von Geschmacksrichtungen für E-Zigaretten“. Prävention, nicht Gesundheitsfinanzierung.
- **Nicht abgedeckt:** Bürgerversicherung, Beiträge, Pflegeversicherung und Eigenanteile, Krankenhausreform.

### 6.4 Arbeit und Rente (bisher fast nicht abgedeckt)

- **SE035 Item 4** (EB 97.5 QB6, ZA7902_q_de S. 31; EB 98.2 QB4, ZA7953_q_de S. 30): „Jeder EU-Mitgliedstaat sollte einen Mindestlohn für Arbeitnehmer haben“. Nur 2022/23; betrifft den Grundsatz in der EU, nicht die Höhe.
- **SP529 QC5b** (6.3): „Renten (z. B. Altersrente, Erwerbsunfähigkeitsrente, Hinterbliebenenrente)“ und „Arbeitslosenunterstützung …“ als Ausgabenwunsch an die Bundesregierung (2022).
- **SP554 QB11** (6.2): Regeln für KI am Arbeitsplatz.
- **Nur Prioritätenlisten:** SP546 (EB 101.1) QB4, ZA8841_q_de S. 30: „Welche der folgenden Themen sollten in Deutschland vorrangig angegangen werden?“ (u. a. „Geringe Löhne“, „Unzureichende Alterseinkommen und Renten bzw. Pensionen“, max. 3 Nennungen).
- **Nicht abgedeckt:** Rentenniveau, Renteneintrittsalter, Rentenfinanzierung, Arbeitszeit, Tarifbindung, Streikrecht.

### 6.5 Wohnen (bisher keine Frage)

- **SP529 QC5b** (6.3): „Wohnungswesen (z. B. Sozialwohnungen, Wohngeld, Wohnungsbau)“ als Ausgabenwunsch (2022).
- Sonst nur Prioritätenlisten: ST0748 „Verbesserung des Zugangs zu Wohnraum in der EU“; SE053 „Wohnungsbau / Wohnungsbeschaffung“ als Budgetwunsch; SP546 QB4 „Fehlende Sozialwohnungen sowie Obdachlosigkeit“.
- **Nicht abgedeckt:** Mietregulierung, sozialer Wohnungsbau als Abwägung, Vergesellschaftung, Grundsteuer.

### 6.6 Bildung und Forschung (bisher keine Frage)

- **SP529 QC5b** (6.3): „Bildung (z. B. Schulen, Hochschulen, Angebote der Erwachsenenbildung)“ als Ausgabenwunsch (2022).
- **SP557 (EB 102.1) QA7, ZA8904_q_de S. 5:** „Die Ergebnisse öffentlich finanzierter Forschung, wie z. B. wissenschaftliche Artikel und Daten, sollten kostenlos online zur Verfügung gestellt werden“; „Es sollte keine Grenze geben, was Wissenschaft untersuchen darf“. Fünfstufig mit Mitte.
- **SP535 (EB 99.2) QB17, ZA7955_q_de S. 104:** „Der Schulunterricht und die Unterrichtsmaterialien sollten Informationen über ... enthalten.“ – u. a. „Sexuelle Orientierungen …“, „Die Existenz mehrerer Geschlechtsidentitäten …“, „Religionen und des Glaubens“.
- SP569 Berufsbildung (EB 104.2) enthält nur Bewertungen und Wahrnehmungen, keine Präferenzen.
- **Nicht abgedeckt:** Bund-Länder-Zuständigkeit, BAföG, Studiengebühren, Kita- und Sprachtestpflicht, Schulstruktur.

### 6.7 Lücken innerhalb vorhandener Bereiche

- **Europäische Integration** (Lücke: gemeinsame Politikfelder, Euro, Erweiterung, Finanzen):
  - SE037 vollständig, EB 104.1 S. 10 (11 Items, u. a. „Eine gemeinsame europäische Einwanderungspolitik“, „Eine gemeinsame europäische Energiepolitik“, „Eine Erweiterung der EU, um in den nächsten Jahren andere Länder aufzunehmen“, „Eine europäische Wirtschafts- und Währungsunion mit einer gemeinsamen Währung, dem Euro“, „Eine gemeinsame Klimapolitik“).
  - SP564 (EB 103.2) QC3, ZA9127_q_de S. 48: „Wenn Sie an eine zusätzliche Erweiterung der EU denken, würden Sie sagen, dass Sie alles in allem …?“.
  - SP564 QC5, S. 49: „Wären Sie dafür oder dagegen, dass sie der EU beitreten, sobald sie alle Bedingungen für die Mitgliedschaft erfüllt haben?“ (je Land, u. a. Ukraine, Türkei, Serbien, Georgien).
  - SE050 (EB 104.1 QF1, S. 23): „Die EU sollte angesichts ihrer politischen Ziele über größere finanzielle Mittel verfügen.“ / „Die finanziellen Mittel der EU entsprechen ihren politischen Zielen“. Asymmetrisch, eine Option „weniger“ fehlt.
  - Zum Wortlaut: „Eine zusätzliche Erweiterung …“ (bis 102.2) wurde ab 103.3 zu „Eine Erweiterung …“. Das Euro-Item stand bis 103.3 in SE034, ab 102.2 in SE037.
- **Migration** (Lücke: Grenzen, Asylsystem):
  - SE038, EB 97.5, 99.4, 100.2 und 101.3, danach nicht mehr gefunden. EB 99.4 QB9, ZA7997_q_de S. 34: „Ein Gemeinsames Europäisches Asylsystem“ / „Eine Verstärkung der EU-Außengrenzen mit mehr europäischen Grenzschutz- und Küstenwachebeamten“ (Dafür/Dagegen).
  - SE040 Item 2, alle Standardwellen ab 99.4, EB 104.1 QB4, S. 12: „Deutschland sollte Flüchtlingen helfen“.
  - Grenzkontrollen an Binnengrenzen und Zurückweisung habe ich nur als Prioritätennennung gefunden (SP549 QA15 „Abschaffung aller Kontrollen an den Schengen-Binnengrenzen“).
- **Klima und Energie** (Lücke: Gebäude und Heizung, Verkehr, Klimaziele):
  - SP565 (EB 103.2) QD10, ZA9127_q_de S. 75: „Inwieweit sind Sie für oder gegen das Ziel der EU, bis 2050 klimaneutral zu werden?“.
  - SP565 QD11 Item 2, S. 75: „Es sollte mehr öffentliche finanzielle Unterstützung für die Umstellung auf saubere Energien geben, selbst wenn das bedeutet, dass Subventionen für fossile Brennstoffe gesenkt oder eingestellt werden“.
  - SP538 (EB 99.3) QC11, ZA7996_q_de S. 37: Drei Antwortoptionen zum Tempo des Wandels: „… beschleunigen“ / „… im gleichen Tempo fortsetzen“ / „Wir sollten während der Energiekrise wieder mehr fossile Brennstoffe nutzen und den Wandel hin zu einer umweltfreundlichen Wirtschaft verlangsamen“.
  - SP527 (EB 97.4) QA16, ZA7901_q_de S. 21: „Inwieweit sind Sie für oder gegen die folgenden politischen Maßnahmen in Deutschland …?“ – u. a. „Besteuerung von Produkten und Dienstleistungen, die am stärksten zum Klimawandel beitragen, und Umverteilung der Einnahmen an die ärmsten und gefährdetsten Haushalte“, „Vergabe eines Energiekontingents an jeden Bürger …“, „Fördermittel für Personen, um ihnen zu helfen, ihr Zuhause energieeffizienter zu machen …“.
  - SP527 QA3 Item 3, S. 11: „Deutschland muss keine Maßnahmen ergreifen, um den Klimawandel und Umweltveränderungen zu bekämpfen, wenn andere Länder nicht ebenfalls Maßnahmen ergreifen.“
  - SP555 (EB 101.4) QC2, ZA8844_q_de S. 26: „Sollte die Europäische Union bei Energiefragen eine stärkere koordinierende Rolle haben?“ (fünf Optionen).
- **Gleichstellung** (Lücke: trans Personen, Quote):
  - SP535 (EB 99.2) QB15, ZA7955_q_de S. 102: „Gleichgeschlechtliche Ehen sollten in ganz Europa erlaubt sein“; „Transgender Personen sollten dieselben Rechte wie jeder andere auch haben (Recht auf Eheschließung, Adoptionsrecht, Elternrechte)“.
  - SP535 QB18, S. 104: „Sind Sie der Meinung, dass transgender Personen berechtigt sein sollten, ihre Personenstands- bzw. Identitätsdokumente entsprechend ihrer Geschlechtsidentität zu ändern?“ (Ja/Nein).
  - SP545 (EB 100.3) QD6 Item 5, ZA8840_q_de S. 88: „Es sind vorübergehende Maßnahmen (z. B. Quoten) notwendig, um die bestehende Unterrepräsentation von Frauen in der Politik zu überwinden“.
  - SE034 Item 4 (EB 97.5 QB5, S. 30): EU-Maßnahmen für Gleichstellung am Arbeitsplatz, „z. B. Maßnahmen zur Lohntransparenz oder Quoten …“.
  - Schwangerschaftsabbruch: nicht gefunden.
- **Wirtschaft und Verteilung** (Lücke: Steuern):
  - SP529 QC16, ZA7901_q_de S. 110: „Eine wichtige Aufgabe der Regierung ist die Besteuerung der Reichen, um die Armen zu unterstützen“. Skala 1–10, 1 = „stimme voll und ganz zu“.
  - Big-Tech-Besteuerung (6.2) und Zölle (6.1).

**Hinweise zu den Formulierungen:**
- Viele Items sind einseitige Zustimmungsaussagen zu EU-Maßnahmen oder Wichtigkeitsfragen ohne Gegenposition. Das kann Zustimmungstendenz begünstigen und die Unterscheidungskraft mindern.
- Eine Abwägung nennen ausdrücklich: SP572 QB12, SP538 QC11, SP565 QD11 Item 2, SP527 QA3 Item 3, EB 97.3 QA15 (Teil des EP-Moduls).
- Die Fragebögen entstehen im Auftrag der Generaldirektion Kommunikation der Kommission bzw. des Parlaments. Einige Aussagen beschreiben EU-Maßnahmen in deren Begriffen, etwa „als Reaktion auf die russische Invasion“ oder „bis dauerhaft gerechter Frieden herrscht“. Das ist eine Feststellung zur Herkunft, kein Urteil über Absichten.

## 7. Eignung als Vergleich

| Anforderung | Veröffentlichte Tabellen (Kommission) | Einzeldaten (GESIS) |
|---|---|---|
| Anteile je Kategorie für Deutschland | Volume A und C weisen gewichtete Häufigkeiten je Land aus (Portalbeschreibung). Ob alle Kategorien inkl. „Weiß nicht“ und „Verweigert“ enthalten sind: **nicht geprüft** | ja |
| Basis | **nicht geprüft**. N je Land steht in der Technischen Spezifikation | ja (ungewichtet und gewichtet) |
| Gewichtung | „weighted“ laut Portal und About-Seite. Welches Gewicht für Deutschland gesamt verwendet wurde: nicht dokumentiert gefunden | `w1de` / „WEIGHT SPECIAL GERMANY“ laut GESIS |
| Feldzeit, Modus | Technische Spezifikation (Berichtsanhang; bei GESIS im `_bq.pdf`) | ebenso |
| Unsicherheit | nur Faustregeln der Fehlertabelle; kein Designeffekt | rechnerisch möglich, aber ohne Designgewicht und Cluster-Angaben nur näherungsweise (Vermutung) |
| Wählergruppen nach Zweitstimme | **nicht möglich** | **nicht möglich**: keine Bundestagswahlfrage in den geprüften Standard- und Spezialwellen; nur Europawahl 2024/2019 in EB 101.5 |
| Links-Rechts-Gruppen (D1) | Volume C enthält „socio-political … variables“. Ob die Links-Rechts-Einstufung darunter ist: **nicht geprüft** | ja; D1 steht in allen Standardwellen (EB 104.1 S. 30) |

**Folgerung:** Für Einzelvergleiche mit der Bevölkerung Deutschlands (EU-Staatsangehörige ab 15, CAPI, Feldzeit X) könnten die Kommissionstabellen reichen, wenn eine ergebnisblinde Strukturprüfung bestätigt: Deutschland gesamt ist ausgewiesen, alle Kategorien inkl. „Weiß nicht“ sind enthalten, eine Basis ist angegeben. Das ist eine Vermutung. Für Wählergruppen gibt es keinen Weg. Gruppen nach Links-Rechts-Einstufung bräuchten Einzeldaten und damit die GESIS-Bedingungen, sofern Volume C sie nicht enthält.

**Weitere Grenzen eines Vergleichs mit Websitebesuchenden:**
- Selbstauswahl der Besuchenden.
- Andere Population.
- Interviewer-Modus mit Bildschirmvorlage gegenüber Selbstausfüllen.
- „Weiß nicht“ wird in der Befragung verborgen.
- Zeitbezug der Items (Maßnahmen „ergriffen“, Bewerberstatus 2022–2026).
- Wechselnde Itemwortlaute zwischen Wellen (6.1, 6.7).

## 8. Empfehlungen je Bereich

Prioritäten sind Empfehlungen für Stevens Entscheidung, keine Auswahl.

| Bereich | Priorität | Kandidaten | Voraussetzungen | Offene Fragen für Steven |
|---|---|---|---|---|
| Außen-, Verteidigungs-, Friedenspolitik | **1** | EB 105.2 (oder 104.1) ST0350 Items 3, 5, 6, 7 und 1; ST0359 Items 15, 4, 5; SE037 Items 1, 2 | ergebnisblinde Strukturprüfung der Volumes A/C von STD105; Quellenangabe nach Beschluss 2011/833/CC BY; Hinweis „EU-Ebene, nicht deutsche Politik“ | Reicht die EU-Ebene als Ersatz, oder bleibt die nationale Lücke (Wehrpflicht, Bundeswehr) sichtbar? (Empfehlung: sichtbar lassen) |
| Europäische Integration (Lücke) | **1** | SE037 alle Items (EB 105.2); SP564 QC3, QC5 (2025); SE050 | wie oben | Erweiterung je Land zeigen oder nur insgesamt? |
| Medien und Digitalpolitik | **2** | SP572 QB12, QB5 Item 6 (2026); SE035 Item 5 (bis 104.1) | wie oben; Volumes zu SP572 vorhanden (A, AA, AP, AAP, B, C, D) | Rundfunk bleibt Lücke |
| Klima und Energie (Lücke) | **2** | SP565 QD10, QD11 Item 2 (2025); SP538 QC11 (2023); SP527 QA16 (2022, Maßnahmen in Deutschland); SE037 Item 11 | wie oben; Alter der Daten kennzeichnen | Sind Messungen von 2022/23 zur Energiekrise noch sinnvoll? |
| Migration (Lücke) | **2** | SE038 (zuletzt EB 101.3, 2024); SE040 Item 2 (EB 105.2) | wie oben | Ist der Stand 2024 für das Asylsystem akzeptabel? |
| Gleichstellung (Lücke) | **2** | SP535 QB15 Items 3/5, QB18 (2023); SP545 QD6 Item 5 (2024) | wie oben | — |
| Gesundheit und Pflege | **3** | SE037 Item 8; SP529 QC5b (2022, mit Ausgabeninformation); SP539 QD16 | Pro-Kopf-Beträge 2022 müssten mitgezeigt werden; Gesundheitsfinanzierung bleibt Lücke | Ist ein Ausgabenwunsch von 2022 mit Informationsvorgabe vertretbar? |
| Arbeit und Rente | **3** | SP529 QC5b (Renten, Arbeitslose); SE035 Item 4 (Mindestlohn als EU-Grundsatz, 2022/23); SP554 QB11 | wie oben | Kernstreitfragen bleiben Lücke |
| Bildung und Forschung | **4** | SP529 QC5b (Bildung); SP557 QA7 Items 5, 7; SP535 QB17 | wie oben | Lücke bleibt weitgehend |
| Wohnen | **4** | nur SP529 QC5b (Wohnungswesen) | wie oben | Lücke bleibt |

**Nächste Schritte, die Steven entscheiden müsste:**
1. **Weg festlegen.** Kommissionstabellen statt GESIS-Einzeldaten. Für den Tabellenweg habe ich keine KI-Regel gefunden. Ob Agenten die Tabellen auslesen dürfen, sollte Steven trotzdem bewusst entscheiden. Der Einzeldatenweg braucht eine GESIS-Ausnahme nach § 4.
2. **Auswahl ergebnisblind einfrieren**, bevor jemand Werte sieht. Danach eine Strukturprüfung der Tabellen (Kategorien, Basis, Gewicht), getrennt von der Werteübernahme.
3. **Anfrage an das Eurobarometer-Team der Kommission** (Kontakt laut About-Seite):
   - Bestätigung, dass deutsche Länderfragebögen unter die Weiterverwendung nach 2011/833 bzw. CC BY 4.0 fallen;
   - Bezug der deutschen Fragebögen direkt bei der Kommission;
   - Aufbau der Volumes für Deutschland (Basis, „Weiß nicht“);
   - ob Volume C die Links-Rechts-Einstufung enthält.
4. **Anfrage an GESIS** (Kontakt laut § 1: Oliver Watteler), nur bei Bedarf: Gelten heruntergeladene Fragebogen-PDFs als „Datenbasis“? Gibt es eine KI-Ausnahme für Eurobarometer-Einzeldaten?

## 9. Ergebnisblindheit: Protokoll

- Ergebnistabellen (Volumes), Datenanhänge, Berichte, Factsheets, Präsentationen, GESIS-Variablenberichte und Datensätze habe ich **nicht** geöffnet.
- Die Eurobarometer-Schnittstelle lieferte zu STD104 im Feld „keyFindings“ ungefragt eine Überschrift. Sie formuliert ein EU-weites Ergebnis ohne Zahl zur Wahrnehmung der EU-Mitgliedschaft. Ich habe sie weder genutzt noch übernommen. Weitere Beschreibungs- und Ergebnisfelder habe ich gezielt nicht ausgegeben.
- Die Portalbeschreibung zu SP564 enthält Prozentzeichen. Ich habe nur die Sätze zu den Volumes gelesen, die übrige Beschreibung nicht.
- Der SP529-Fragebogen enthält Pro-Kopf-Ausgabenbeträge je Land. Das sind Vorgaben an die Befragten, keine Befragungsergebnisse. Ich habe sie nicht übernommen.
- Antwortraten und Fehlertabellen der Technischen Spezifikationen sind Methodenangaben. Ich habe nur die Werte für Deutschland bzw. die Tabellenregel zitiert.

## 10. Nachweise

### 10.1 Tatsächlich geöffnete Quellen (03.10.2026, Uhrzeiten UTC, ungefähr)

**Lokal (20:50–20:55):** `reports/claude/auftraege/R6-eurobarometer.vollstaendig.md`, `R6-eurobarometer.md`, `docs/project.md`, `docs/abdeckung-v2.2.md`, `reports/claude/agenten/R3-themen-reichweite.md` (Abschnitte 3, 4.5, 8), Fundstellen-Suche in R1 und R2.

**Recht (20:56–21:20):**
- EUR-Lex Beschluss 2011/833/EU, DE- und EN-HTML sowie Seite „ALL“ (`https://eur-lex.europa.eu/legal-content/{DE,EN}/TXT/HTML/?uri=CELEX:32011D0833`, `…/EN/ALL/?uri=CELEX:32011D0833`); SHA-256 DE `88362128…`
- `https://commission.europa.eu/legal-notice_de` und `_en` (DE `8da7a495…`)
- `https://european-union.europa.eu/legal-notice_en` und `_de`
- Europäisches Parlament, Legal notice: direkt HTTP 202 ohne Inhalt; WebFetch-Zusammenfassung (nicht als Zitatquelle genutzt); Wayback `http://web.archive.org/web/20261002160955/https://www.europarl.europa.eu/legal-notice/en/`
- GESIS-Datennutzungsbedingungen: Wayback HTML 30.03.2026 (`3ab9b346…`), PDF 30.03.2026 (`2a46f4ff…`), Bild der Kategorientabelle (PDF S. 3); Wayback-CDX-Liste 2026
- C(2019) 1655: EUR-Lex-Abruf HTTP 404; Dokumentenregister nur als JavaScript-Anwendung. Ein ID-Rateversuch lieferte ein **fremdes** PDF (C(2018) 4759, Normung); verworfen und gelöscht, nicht verwendet.

**Eurobarometer und Kommission (20:56–21:20):**
- `https://europa.eu/eurobarometer/screen/home`, JavaScript-Bündel `angular/main.c7a8487585ea19dc.js`, `…surveys_module_ts.b44dcb623b8be6fc.js`, `…surveysListing…2c73035db5d450c4.js`, `…about_module_ts.4514644fc63dcdf2.js`, `static/config.json`
- API: `/eurobarometer/api/survey/get/latest?nb=5`, `?nb=400`, `?nb=5000`; `/survey/get/one?id=` für alle Standard-, Spezial- und Flash-Befragungen ab 2022 (nur Metadaten ausgewertet); `/metadata/deliverable_type/get/all`
- data.europa.eu-API (`/api/hub/search/datasets/…`): s3378_104_1_std104_eng, s2872_98_2_std98_eng, s2262_93_1_93_1_eng, s3413_103_2_sp564_eng, s3682_105_1_sp572_eng, s1070_78_2_394, s408_61_0_std_61, s3472_103_2_sp565_eng, s2972_99_2_sp535_eng, s2652_97_4_sp529_eng, s2672_97_4_sp527_eng, s2954_99_3_sp538_eng, s3613_105_2_std105_eng, s2974_100_3_sp545_eng, s3222_101_4_sp554_eng (nur Lizenz, Dateinamen, Volume-Beschreibungen)

**GESIS (21:00–21:20):**
- Wayback-Kopien: `gesis.org/en/eurobarometer-data-service` (31.12.2025), `…/faq`, `…/data-and-documentation`, `…/standard-special-eb/population-countries-regions`, `…/weighting-overview`, `…/sampling-and-fieldwork` (27.07.2026), `…/standard-special-eb` (07.09.2026)
- OAI `https://dbkapps.gesis.org/dbkoai/?verb=GetRecord&identifier=oai:dbk.gesis.org:DBK/ZAxxxx&metadataPrefix=oai_ddi25-de` (und `oai_ddi25` für ZA9130, ZA9144) für die 29 Studien ZA7886, 7887, 7888, 7901, 7902, 7952–7955, 7996, 7997, 8778, 8779, 8840–8844, 8900, 8904–8906, 9127–9131, 9143, 9144
- DataCite-API (`api.datacite.org/dois?query=…Eurobarometer…GESIS…`, `…/dois/10.4232/1.14729`)
- Dokumente über `https://access.gesis.org/dbk/<ID>`: alle in Abschnitt 5 genannten `_q_de` und `_bq` sowie zusätzlich ZA7886_q_de (74147), ZA7887_q_de/bq (73638/73631), ZA7952_q_de/bq (77978/77971), ZA7954_q_de/bq (78643/78636), ZA8778_q_de/bq (78571/78229), ZA8842_q_de/bq (80441/80433), ZA8900_q_de/bq (81542/79844), ZA8906_q_de/bq (81420/81413), ZA9131_q_de/bq (82158/82151), ZA9130_readme (81773). In `_bq` habe ich nur Fragetexte und Technische Spezifikationen gelesen.

**Websuche:** drei WebSearch-Abfragen (GESIS-Eurobarometer-Dienst; Volume-Beschreibungen; C(2019) 1655). Die Ergebnisse dienten nur zum Auffinden; zitiert sind die selbst geöffneten Seiten.

### 10.2 Ausgeführte Befehle (Kurzform)

- `curl` für EUR-Lex, Kommissions-, EP- und EU-Seiten, Eurobarometer-API, data.europa.eu-API, DataCite, GESIS-OAI, Wayback und GESIS-Dokumente
- HEAD-Abfragen `curl -sI https://access.gesis.org/dbk/<ID>` für die IDs 66000–83400, nur Dateinamen aus `Content-Disposition`
- `pdftotext` (-layout, -raw), `pdfinfo`, `pdfimages`, `pdftoppm`; Python (PIL) zum Ausschneiden der Tabellenbilder der Technischen Spezifikationen und Bildansicht; eigene Python-Skripte zum Zerlegen der Fragebögen in Frageblöcke, zur Stichwortsuche und Seitensuche
- `sha256sum`
- Keine Git-Befehle mit Schreibwirkung, keine Anmeldung, kein Download von Datensätzen oder Ergebnistabellen. Geschrieben habe ich nur diese Berichtsdatei; Arbeitsdateien liegen unter `/tmp/r6`.

### 10.3 Grenzen der Prüfung

- **Rechtsfragen** sind Quellenfeststellungen, keine Rechtsberatung. GESIS-Seiten habe ich nur als Wayback-Kopien gelesen; spätere Änderungen sind möglich. Die Zuordnung der Kategorientabelle stammt aus einem Bild. C(2019) 1655 habe ich nicht im Original gesehen. Die Bedingungen der Download-Infrastruktur von data.europa.eu und `webgate.ec.europa.eu` habe ich nicht gesondert geprüft.
- **Tabellenstruktur** (Kategorien, Basis, verwendetes Gewicht, Links-Rechts-Aufgliederung in Volume C) ist wegen der Ergebnisblindheit ungeprüft. Ebenso offen ist, ob Berichts-PDFs einen Fragebogenanhang enthalten.
- **Vollständigkeit:** Ich habe 29 deutsche Fragebögen per Stichwortsuche durchsucht, inklusive ZA7954, ZA8778, ZA8842, ZA8906, ZA9131 (dort keine Präferenzfragen zu den Lücken gefunden), und die Treffer gelesen, nicht jede Frage. Spezialbefragungen mit Feldzeit 2021 (SP517, SP519) und Flash-Befragungen habe ich nicht ausgewertet. SP574 und SP577 (Feldzeit 2026) waren bei GESIS noch nicht verfügbar.
- **Modus Deutschland** in EB 101.3 und 101.4 nicht geprüft; für EB 102.2 ist die CAVI-Aufteilung unbekannt.
- **Fragebogenbezug über GESIS:** Ich habe öffentlich herunterladbare Fragebogen-PDFs von GESIS maschinell verarbeitet, wie zuvor R3. Ob GESIS solche Dokumente als „Datenbasis“ im Sinne von § 4 ansieht, ist offen (3.3).
- **Neutralität:** Kein Befund dieses Berichts ist ein Neutralitäts- oder Validitätsnachweis. Übereinstimmung mit R1 bis R3 oder dem externen KI-Review gilt nicht als Bestätigung. Die Aussage des externen Reviews, das Eurobarometer sei eine Alternative, trifft nach dieser Prüfung nur eingeschränkt zu: für Bevölkerungsvergleiche zu meist EU-bezogenen Fragen über Kommissionstabellen. Als Ersatz für Wählergruppen oder nationale Streitfragen taugt es nicht.

### 10.4 Modell

Laut Laufzeitumgebung: Claude Opus 5.5, Modell-ID `claude-opus-5-5[1m]`, als Subagent in Claude Code.
