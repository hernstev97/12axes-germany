# Analyseplan v2.2: neue Originalfragen, Stichprobenunsicherheit und erklärendes Antwortprofil

Fassung 1.1 vom 3. Oktober 2026, verfasst von Claude (Anthropic) nach der Übernahme von LIFE-93. Fassung 1.0 (Prüfpaket `PLAN-V22-001`, Commit `de80a46`) erhielt zwei getrennte Codex-Prüfungen (`reports/claude/pruefungen/P1-methoden-v22.*`, `P2-quellen-fairness-v22.*`). Fassung 1.1 setzt deren Korrekturen um. Die Korrekturen stehen in Abschnitt 9. Dieser Nachtrag ergänzt den [Empirieplan v2](empirie-plan-v2.entwurf.md) und den [Gruppenvertrag v2.1](../data/gruppenvertrag.v2.1.entwurf.json). Er ersetzt sie nicht. Historische Pläne, Tags (`analyseplan-v1`, `erwartungsmodell-v1`, `modell-v1`, `analyseplan-v2`, `analyseplan-v2.1`), Exporte und Prüfberichte bleiben unverändert.

Grundlage sind die getrennten Rechercheberichte [R1](../reports/claude/agenten/R1-themen-aussen-bildung-digital.md), [R2](../reports/claude/agenten/R2-themen-gesundheit-arbeit-wohnen.md), [R3](../reports/claude/agenten/R3-themen-reichweite.md) und [R4](../reports/claude/agenten/R4-profilform.md), die [unabhängige Kontrollrechnung](../reports/claude/kontrollrechnung/bericht.md) und die [Quellen- und Fairnessprüfung](../reports/claude/agenten/V2-quellen-konstrukte-fairness.md). Alle Berichte stammen von Claude-Subagents, also von derselben Modellfamilie wie dieser Plan.

## 1 Was vor diesem Plan bekannt war

- Die 42 veröffentlichten Einzelreferenzen und 63 Gruppenpaare der 43 v2-Fragen sind öffentlich. Die Kontrollrechnung V1 hat sie neu berechnet und Übereinstimmung festgestellt. Ich habe ihre Zahlen beim Schreiben dieses Plans nicht angesehen. Bekannt sind sie trotzdem, und nichts in diesem Plan ist eine unberührte Bestätigung dieser Werte.
- Für die 19 neuen Fragen in Abschnitt 3 hat niemand in diesem Projekt Antwortdaten gelesen oder Verteilungen berechnet. Gelesen wurden nur Spaltennamen der lokalen CSV-Dateien und öffentliche ESS-Metadaten (`outputs/claude/sources/fetches.jsonl`). Die Rechercheagenten R1–R3 berichten, dass Suchmaschinen ungefragt einzelne Ergebniszahlen aus anderen Befragungen anzeigten. Diese Zahlen betreffen keine der hier ausgewählten ESS-Variablen in Deutschland und wurden nicht verwendet.
- Die Antworten der ESS11-Neunerfassung (v1, Teil A und B) sind seit dem v1-Lauf bekannt. Dieser Plan nutzt für die Homosexualitätsfragen deshalb nicht ESS11, sondern ESS10 Self-completion (Abschnitt 3.2).

## 2 Ziel und Messform

Das Produkt bleibt ein Vektor getrennter Einzelangaben mit Originalkategorien. Dieser Plan fügt drei Dinge hinzu:

1. 19 weitere Originalfragen aus lokal vorhandenen ESS-Dateien, die Lücken innerhalb der Bereiche verkleinern (Abschnitt 3).
2. Stichprobenunsicherheit für veröffentlichte Kategorienanteile, wo die Daten ein vollständiges Stichprobendesign enthalten (Abschnitt 4).
3. Ein regelbasiertes, erklärendes Antwortprofil ohne Gesamtwert (Abschnitt 5).

Kein Gesamtwert, keine Achse, kein Perzentil, keine Rangfolge gegenüber der Bevölkerung, kein gemeinsames Referenzprofil über Studien. Das gilt unverändert aus v2 und wird durch R4 Abschnitt 4.8 gestützt.

## 3 Neue Originalfragen

### 3.1 Auswahlregeln

Eine Frage wird aufgenommen, wenn sie alle Bedingungen erfüllt:

- Sie liegt in einer lokal vorhandenen, lizenzierten ESS-Datei mit deutschem Originalfragebogen.
- Sie erfragt eine politische Präferenz oder ein politisches Prinzip, keine Wahrnehmung, Bewertung der Regierung, eigenes Verhalten oder Zufriedenheit.
- Sie verkleinert eine dokumentierte Lücke innerhalb eines Bereichs (R3 Abschnitt 4 und 5.1, V2-F09). Weitere Fragen zum selben engen Gegenstand reichen nicht.
- Sie ist nicht Teil eines Zufallszweigs, der einen eigenen Nenner bräuchte.

Die Auswahl entsteht aus Inhalt und Dokumentation, nicht aus Antwortverteilungen. Keine Frage wird nach Sichtung ihrer Ergebnisse entfernt, umgepolt oder einem anderen Bereich zugeordnet.

### 3.2 Ausgewählte Fragen

| Bereich (primär)                     | Studie, Frage, Variable                                                               | Grund                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Klima und Energie                    | ESS8 D4–D10: `elgcoal`, `elgngas`, `elghydr`, `elgnuc`, `elgsun`, `elgwind`, `elgbio` | Energieträger fehlen bisher (R3 4.6, Prüfhinweis 1). Vollständiger Originalblock, keine Teilauswahl einzelner Energiequellen.                                                                                                                                                                                                                     |
| Migration                            | ESS8 C42 `gvrfgap`, C44 `rfgbfml`                                                     | Asylprüfung und Familiennachzug fehlen (R3 4.7). C43 `rfgfrpc` ist eine Wahrnehmung und bleibt draußen.                                                                                                                                                                                                                                           |
| Sozialstaat                          | ESS8 E36 `basinc`                                                                     | Grundeinkommen mit allen sechs Definitionsmerkmalen der Liste 54 (R3 5.1). Die vollständige Definition erscheint auf der Website.                                                                                                                                                                                                                 |
| Europäische Integration              | ESS8 E37 `eusclbf`                                                                    | Gemeinsame EU-Sozialpolitik fehlt (R3 4.5). Alle drei Definitionsmerkmale der Liste 55 erscheinen.                                                                                                                                                                                                                                                |
| Gleichstellungs- und Familienpolitik | ESS10 Self-completion A47 `freehms`, A49 `hmsacld`; ESS8 B33A `mnrgtjb`               | Rechte gleichgeschlechtlicher Paare fehlen ohne Begründung (V2-F09, R3 Prüfhinweis 7). A48 `hmsfmlsh` fragt nach eigener Scham und ist keine politische Präferenz. `mnrgtjb` erfasst ein normatives Prinzip zur Gleichberechtigung bei knappen Arbeitsplätzen und erfüllt die Regeln in 3.1. Es wurde nach P2-V22-F02 ohne Dateneinsicht ergänzt. |
| Demokratie und politische Autorität  | ESS10 Self-completion A51 `accalaw`, A53 `loylead`; ESS5 B32 `prtyban`                | Fragen zu politischer Autorität und zum Verbot demokratiefeindlicher Parteien fehlen (V2-F04, V2-F09). A52 `lrnobed` betrifft Erziehungswerte für Kinder und keine politische Ordnung.                                                                                                                                                            |
| Bürgerrechte und Sicherheit          | ESS10 Self-completion A1 `panpriph`, A2 `panmonpb`                                    | Einzige lokal verfügbare Abwägungen zwischen Gesundheitsschutz und Wirtschaft sowie zwischen staatlicher Überwachung und Privatsphäre. Beide gelten ausdrücklich für die Bekämpfung einer Pandemie. Sie zählen weder als Abdeckung von Gesundheitspolitik noch von Digitalpolitik (R1, R2 Abschnitt 3.3).                                         |

ESS10 Self-completion statt ESS11: Die Fragen `freehms`, `hmsacld` und `loylead` liegen in beiden Runden vor. ESS10 Self-completion wurde schriftlich oder online beantwortet und liegt damit näher an einer Website. Außerdem sind die ESS11-Antworten zu den Homosexualitätsfragen aus v1 bekannt. Dieselbe Abwägung begründet nachträglich, dass die drei Zulassungsfragen und `vteurmmb` aus ESS10 Self-completion stammen (R3 Prüfhinweis 6). Eine zweite, neuere Referenz aus ESS11 wird nicht ergänzt. ESS12 soll laut ESS ab Januar 2027 verfügbar sein (R3 2.2). Er ist ein zu prüfender Aktualisierungsweg für Kernfragen wie Zuwanderung, EU-Abstimmung und Einkommensunterschiede sowie für das Zuwanderungsmodul. Für die übrigen Themenlücken ist kein ESS12-Weg belegt.

Nicht aufgenommen, mit Grund:

- ESS8 E21–E32 (Arbeitslosenunterstützung bei abgelehnten Stellen): Zufallsvignetten mit Zweignennern. Ein späterer eigener Plan ist möglich.
- ESS8 `smdfslv`, `dfincac`, ESS5 `gvprppv`: Verteilung und Armut sind schon erfasst. Mehr Fragen zum selben Gegenstand schaffen keine Breite.
- ESS10 A3, A4, A5 (Pandemie: Regeln, Grenzen, Bewegungsfreiheit): weitere Pandemiefragen würden einen historischen Ausnahmezustand überbetonen.
- GLES, ISSP, ALLBUS, Politbarometer, Eurobarometer: siehe Abschnitt 7.

### 3.3 Bindung

Wortlaute, Einleitungen, Antwortlisten und Fundstellen stehen in [`data/politikprofil-v2.2.ergaenzung.json`](../data/politikprofil-v2.2.ergaenzung.json). Das Skript `pipeline/v22/catalogue_v22.py` erzeugt die Datei und prüft jeden deutschen Text automatisch gegen den Text des Original-PDF. Codes und Missing-Gründe stammen aus den öffentlichen ESS-Metadaten.

Besonderheiten:

- `elg*`: Code 55 „Ich habe noch nie etwas von dieser Energiequelle gehört“ ist laut ESS-Metadaten eine gültige Antwort. Im Interview wurde sie nicht vorgelesen. Die Website bietet sie nicht als Antwort an. In der historischen Referenz bleibt sie eine eigene Kategorie im Nenner, wie alle gültigen Originalcodes (Plan v2).
- `gvrfgap`, `rfgbfml`: Der deutsche Fragebogen druckt die Codes 0–5, die Liste 31 hat fünf beschriftete Stufen. Gebunden werden die fünf Beschriftungen der Liste 31 und die API-Codes 1–5.
- `panpriph`, `panmonpb`: Code 66 „Not applicable“ zählt als nicht gestellte Frage, wie in v2.
- ESS10: Der Fragebogen bittet, alle Fragen „nach dem heutigen Stand der Dinge, auch wenn dieser durch die Pandemie anders ist als sonst“ zu beantworten (PAPI S. 1). Dieser Hinweis erscheint bei allen ESS10-Fragen (V2-F02).
- Gebunden ist die gedruckte Papierfassung. Die Webfassung von ESS10 ist nur als Bildschirmfoto dokumentiert. Ihr Wortlaut wird in der Prüfung nach Abschnitt 8 stichprobenartig verglichen.

## 4 Stichprobenunsicherheit

### 4.1 Wofür

Für jeden veröffentlichten Kategorienanteil einer Einzelreferenz und eines Gruppenpaares, dessen Studie ein vollständiges Stichprobendesign enthält. Laut Kontrollrechnung V1 (Abschnitt 7) gilt das für ESS9 (89 Strata, 178 PSUs), ESS10 Self-completion (89, 179) und ESS11 (25, 500), jeweils ohne Stratum mit nur einer PSU. ESS5 und ESS8 enthalten keine Designfelder. Für sie wird kein Bereich berechnet, bis Steven die SDDF-Dateien bereitstellt (ESS8 SDDF Ausgabe 1.1, ESS5 SDDF Deutschland). Dann gilt dasselbe Verfahren ohne neuen Plan, sofern jeder deutsche Fall über `idno` genau einer Designzeile zugeordnet wird. Sonst kein Bereich für diese Studie.

### 4.2 Verfahren

Implementiert in `pipeline/v22/survey.py`, synthetisch geprüft in `pipeline/v22/test_survey.py`:

- Schätzer wie v2: gewichteter Anteil mit `pspwght` unter gültigen Antworten.
- Varianz: Taylor-Linearisierung des Quotienten. Erste Stufe mit Zurücklegen, ohne Endlichkeitskorrektur. Die Gewichte gelten als fest, die Poststratifikation wird nicht modelliert. Alle PSUs des vollständigen deutschen Designs gehen ein, auch solche ohne gültige Antwort in der Domäne. Quelle: R-Paket survey 4.5, Abschnitte svyCprod und svydesign, wie Beleg B-V2-M04. Die Formel stimmt in synthetischen Daten bis 1e-12 mit Codex' vorhandener Funktion `pipeline/policy_reference_v2.categorical_reference` überein.
- Bereich: 95 %, Logit-Transformation des Anteils, Delta-Methode, Quantil der t-Verteilung mit Design-Freiheitsgraden (PSUs minus Strata), Rücktransformation. Das entspricht `svyciprop(method = "xlogit")` im survey-Handbuch 4.5, PDF-Seite 93–94.
- Kein Bereich bei Anteil 0 oder 1, bei unvollständigem Design, bei einem Stratum mit nur einer PSU oder bei weniger als 20 Design-Freiheitsgraden. Ein fehlender Bereich wird als fehlend angezeigt, nie als null.
- Grenze: Laut survey-Handbuch (svyciprop, PDF-Seite 94) halten alle Verfahren ihre nominale Abdeckung bei Anteilen nahe 0 oder 1 nicht ein. Die Schwellen 100 gültige Antworten, fünf Fälle je beobachteter Kategorie und 20 Freiheitsgrade sind Projektkriterien. Sie garantieren weder ausreichende effektive Fallzahlen noch eine Abdeckung von 95 %, besonders bei seltenen oder stark gewichteten Kategorien. Diese Grenze wird mit den Bereichen genannt.

### 4.3 Anzeige und Bedeutung

- Format: „95-%-Bereich: 31,2 % bis 36,0 %“, gleiche Rundung wie der Anteil.
- Erklärung, einmal je Ansicht: Der Bereich beschreibt die Unsicherheit, die aus der Zufallsstichprobe der damaligen Befragung entsteht, unter den genannten vereinfachenden Annahmen. Er enthält keine Unsicherheit durch den zeitlichen Abstand, den anderen Befragungsmodus, Nichtteilnahme, den neuen Fragekontext auf der Website oder Messfehler einzelner Antworten. Er ist keine Unsicherheit der eigenen Antwort.
- Keine Signifikanzaussagen, keine Aussagen über Unterschiede zwischen Gruppen oder Studien.

### 4.4 Persönliche Messunsicherheit

Für Einzelantworten gibt es keine methodisch begründete persönliche Messunsicherheit. Sie wird nicht berechnet und nicht angezeigt (LIFE-93 Abschnitt 2b, R4 4.8).

## 5 Erklärendes Antwortprofil

Die Regeln stehen in [`docs/profilregeln-v1.md`](profilregeln-v1.md) und sind in `web/src/app/policy-draft/profile/` umgesetzt. Kurzfassung:

1. Einzelaussage je beantworteter Frage: Richtung aus der Beschriftung der Antwortkategorie, Originalwortlaut in Anführungszeichen, gewählte Kategorie, festes Kontextmerkmal.
2. Blockmuster nur innerhalb von Originalblöcken mit gleicher Einleitung und Antwortliste: gleiche oder unterschiedliche Antworten, höchster und niedrigster Wert, Aufzählung nach Antwortrichtung.
3. Sieben Querbezüge zwischen Blöcken und Studien, nur nebeneinandergestellt, mit Kontextsatz zu den Unterschieden der Fragen.
4. Historische Vergleiche nur je Frage: Anteil derselben Kategorie, vollständige Verteilung mit markierter eigener Kategorie, Studie, Feldzeit, Population, Modus, gegebenenfalls 95-%-Bereich.
5. Je Bereich eine Angabe „Erfasst“ und „Nicht erfasst“ aus der [Themenabdeckung v2.2](abdeckung-v2.2.md).

Diese Regeln hängen nicht von Antwortdaten ab. Sie werden deshalb nicht nach Sichtung von Verteilungen geändert, außer bei nachgewiesenen sachlichen Fehlern mit neuer Version.

## 6 Publikationsregeln

Unverändert aus v2 und v2.1: mindestens 100 gültige Antworten, keine beobachtete Kategorie mit eins bis vier ungewichteten Fällen, sonst keine Zahlen. Gruppenreferenzen für neue Fragen entstehen nur für ESS5 und ESS8 mit den Gruppendefinitionen aus v2.1. Wahl- und Parteiangaben werden für alle deutschen Fälle gegen die vollständigen Codeinventare des Gruppenvertrags geprüft. Unbekannte Codes oder Literale brechen die Studie ab. Wahlstatus, Parteistatus und Inkonsistenzen (Parteiangabe ohne Wahlteilnahme) werden getrennt und privat bilanziert. `anweight` wird wie in v2 validiert, das Verhältnis zu `pspwght` als private Diagnose festgehalten. ESS10-Gruppen bleiben ausgeschlossen (GROUP-V21-SOURCES-05/06). Ein Export setzt eine Ergebnisprüfung nach Abschnitt 8 und eine ausdrückliche Exportentscheidung voraus.

Neu: Die veröffentlichten Dateien nennen Missing-Gründe mit eins bis vier Fällen weiterhin mit Anzahl, aber ohne Gewichtssumme (Kontrollrechnung V1, offener Punkt 1). Bestehende v2-Dateien bleiben unverändert.

## 7 Externe Quellen und Stopp

Die GESIS-Nutzungsbedingungen, gültig ab 4. Februar 2026, verbieten in §4 „die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis“. Ausnahmen lässt GESIS nur auf Anfrage zu. §1 bindet die Nutzung an ein „zeitlich befristetes Vorhaben“ (R2 Abschnitt Rechte, Wayback-Kopie vom 30. März 2026). Das betrifft GLES, ISSP, ALLBUS, Politbarometer und Eurobarometer über GESIS. Nach den Stopp-Bedingungen von LIFE-93 hält dieser Weg an, bis Steven die Ausnahme, die Websitenutzung und die Rechte an deutschen Fragewortlauten mit GESIS geklärt hat. Die übrigen Arbeiten laufen weiter.

## 8 Prüfungen vor Freigabe

Der Rechenweg erzwingt die Reihenfolge technisch: `pipeline/v22/run_v22.py` läuft nur, wenn der Tag `analyseplan-v2.2` lokal und auf `origin` auf denselben Commit zeigt und Plan, Katalogergänzung, Verträge und Rechencode im Arbeitsverzeichnis byte-gleich mit dieser Fassung sind. Die private Ausgabe hat einen festen Pfad unter `data/local/v22/`. Ein vorhandener Lauf wird nicht überschrieben.

1. Vor der Festschreibung: zwei getrennte Prüfungen dieses Plans mit Katalogergänzung, Rechenmodul und Profilregeln. Methoden und Reproduzierbarkeit prüft ein frischer Codex-Agent. Quellen, Konstrukte, Interpretationen und politische Fairness prüft ein zweiter frischer Codex-Agent. Beide erhalten dieselbe Fassung und keine Urteile des anderen.
2. Nach Korrekturen: Festschreibung mit dem Tag `analyseplan-v2.2`.
3. Danach Rechnung, Kontrolle gegen V1 für die 42 bekannten Referenzen und eine gezielte Ergebnisprüfung der neuen Referenzen und Bereiche durch einen frischen Prüfagenten vor dem Export.

Diese Prüfungen sind KI-Reviews. Sie ersetzen keine Begutachtung durch Fachleute, keine empirische Validierung und keine Freigabe durch Steven.

## 9 Korrekturen nach der Prüfung von Fassung 1.0

| Finding    | Korrektur in Fassung 1.1                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P1-V22-F01 | Vollständige Prüfung von Wahl- und Parteicodes, Abbruch bei unbekannten Werten, getrennte private Bilanz einschließlich Inkonsistenzen (`run_v22.py`, Test). |
| P1-V22-F02 | `anweight` wird validiert, das Verhältnis zu `pspwght` privat diagnostiziert.                                                                                |
| P1-V22-F03 | Codes werden mit vollständigem Abgleich geprüft. Ein angehängter Zeilenumbruch bricht ab (Test).                                                             |
| P1-V22-F04 | Fester privater Ausgabepfad ohne Parameter. Abbruch bei Symlinks oder vorhandenem Lauf.                                                                      |
| P1-V22-F05 | Positive Sperre: Tag lokal und auf `origin` gleich, eingefrorene Dateien byte-gleich (Abschnitt 8).                                                          |
| P1-V22-F06 | Zusätzliche gültige Codes werden ausdrücklich gebunden und ihr Text gegen das PDF geprüft. Negativprobe mit falschem Text bricht ab.                         |
| P1-V22-F07 | Querbezug „Soziale Absicherung“ mit `basinc`, Zahl der Querbezüge auf sieben vereinheitlicht.                                                                |
| P1-V22-F08 | Tests für T14 und die neuen Blöcke ergänzt. T30 prüft der Komponententest zu `cttresa`. Der Allkategorientest nutzt nur angebotene Kategorien.               |
| P1-V22-F09 | Grenze der nominalen Abdeckung nahe 0 und 1 in Abschnitt 4.2 ergänzt.                                                                                        |
| P1-V22-F10 | Der Katalog-Builder prüft gepinnte Hashes aller gelesenen Quellen einschließlich der ESS10-Dateimetadaten. Das neue Prüfpaket nennt sie.                     |
| P2-V22-F01 | Querbezug umbenannt und ohne unterstellte Bedürftigkeitsprüfung formuliert.                                                                                  |
| P2-V22-F02 | `mnrgtjb` (ESS8 B33A) nach den Regeln in 3.1 aufgenommen, ohne Dateneinsicht.                                                                                |
| P2-V22-F03 | Themenabdeckung: Finanzierungsausgleich zwischen EU-Ländern im Sozialleistungsprogramm als teilweise erfasst.                                                |
| P2-V22-F04 | ESS12 nur noch als belegter Weg für Kern- und Zuwanderungsfragen genannt.                                                                                    |
| P2-V22-F05 | Plan, Profilregeln und Code nennen dieselben sieben Querbezüge.                                                                                              |
