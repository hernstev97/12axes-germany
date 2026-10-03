# R3: Wie weit reichen die acht Bereiche, wie aktuell sind die 43 Fragen und welche neueren Instrumente gibt es?

Stand: 3. Oktober 2026. Auftrag: `reports/claude/auftraege/R3-themen-reichweite.vollstaendig.md`. Ausgangsstand: Commit `e9898fb`. Verfasst von einem getrennten Claude-Subagenten. Das Modell ist im Nachweisteil (Abschnitt 8) genannt.

Dieser Bericht ist Quellenrecherche. Er trifft keine Auswahlentscheidung und belegt weder Validität noch Neutralität. Ein Themenbereich ist hier immer eine Suchgliederung und keine empirisch nachgewiesene Dimension.

**Ergebnisblindheit:** Ich habe keine Antwortverteilungen, Prozentwerte, Mittelwerte oder Parteiergebnisse aus Befragungen gelesen oder übernommen. Bei der Dokumentensuche habe ich zwei Dateien mit Häufigkeitstabellen heruntergeladen: den Variable Report zu ALLBUS 2023 (GESIS-Dokument 78534) und den Variable Report zur ISSP-Kumulation Work Orientations (GESIS-Dokument 77968). Beide habe ich ungeöffnet gelöscht. Aus der Wahl-O-Mat-Definitionsdatei habe ich nur die Thesentexte ausgelesen, keine Parteiantworten. Die verbotenen Pfade (`data/raw/`, `data/local/`, `data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`/`03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`) habe ich nicht gelesen.

---

## 1. Kernbefunde

1. **Alle acht Bereiche sind nur teilweise abgedeckt.** Mehrere Bereiche messen bisher eine einzige Facette.
   - Wirtschaft: nur Gerechtigkeitsprinzipien und eine allgemeine Umverteilungsfrage. Steuern, Schuldenbremse, Marktregulierung, Industriepolitik und Mindestlohn fehlen.
   - Klima/Energie: drei Instrumente aus 2016/17. Energieträger, Gebäude, Verkehr und Klimaziele fehlen.
   - Migration: Zuzugsmengen nach Gruppen und Sozialleistungsanspruch. Asyl, Grenze, Integration und Staatsangehörigkeit fehlen.
   - Bürgerrechte: ein ESS5-Modul von 2010/11 ohne Überwachung, Datenschutz und Protestrecht.
   - Gleichstellung: konkrete Gleichstellungsmaßnahmen aus 2023. Rechte gleichgeschlechtlicher Paare und reproduktive Selbstbestimmung fehlen.
2. **Lokal vorhandene, bisher ungenutzte ESS8-Fragen schließen mehrere Lücken sofort.** Alle sind mit `ESS8e02_3` auswertbar und stammen aus der Feldzeit 2016/17. In `docs/abdeckung-v2.md` werden sie nicht genannt:
   - **Strommix-Präferenzen D4–D10** (`elgcoal`, `elgngas`, `elghydr`, `elgnuc`, `elgsun`, `elgwind`, `elgbio`; DE-Fragebogen S. 27–28) für Energieträger, Kernkraft und Kohle.
   - **Asylfragen C42 und C44** (`gvrfgap`, `rfgbfml`; S. 25) für Asylprüfung und Familiennachzug.
   - **EU-weites Sozialleistungsprogramm E37** (`eusclbf`; S. 44).
   - **Grundeinkommen E36** (`basinc`; S. 43).
   - **Vignetten zu Leistungskürzungen E21–E32** (S. 39–41).
   - Für gleichgeschlechtliche Paare die Adoptionsfrage `hmsacld`, lokal in ESS10-SC (A49, S. 6) und ESS11 (B36, S. 13).
3. **Aktualität der 43 Fragen.**
   - Für 4 der 43 Fragen gibt es eine neuere lokal vorhandene Runde mit wortgleichem deutschen Fragestamm: `imsmetn`, `imdfetn`, `impcntr` und `vteurmmb` liegen in ESS11 (2023) außer in ESS10-SC (2021/22) vor. Beim Modus unterscheiden sie sich: ESS11 ist CAPI mit Antwortliste, ESS10-SC ein Selbstausfüller. Bei `vteurmmb` sind die Nichtantwortkategorien in ESS11 nicht vorgelesen.
   - 6 Fragen stammen bereits aus ESS11: `gincdif`, `euftf` und die vier Gleichstellungsfragen.
   - Die übrigen 33 Fragen stammen aus Rotationsmodulen von ESS5, ESS8, ESS9 und ESS10. Sie wurden in keiner neueren lokalen Runde wiederholt.
   - **ESS12 ist noch nicht veröffentlicht.** Die ESS kündigt am 30. September 2026 die Erstveröffentlichung für Januar 2027 an. Laut englischem Quellfragebogen enthält ESS12 die Kernfragen `gincdif`, `hmsacld`, `euftf`, `imsmetn`/`imdfetn`/`impcntr` und `vteurmmb` sowie ein Migrationsmodul mit Asylfragen.
4. **Zeitbezüge, die eine heutige Website betreffen:**
   - ESS5 `hrshsnta` lautet „viel härter bestraft werden, als sie heute bestraft werden“. Die Einleitung D32–D37 bezieht sich auf „Deutschland heute“, also auf 2010/11.
   - ESS11 `euftf` fragt, ob die Einigung „schon jetzt zu weit gegangen“ ist.
   - Der ganze ESS10-SC-Fragebogen bittet, „nach dem heutigen Stand der Dinge, auch wenn dieser durch die Pandemie anders ist als sonst“ zu antworten (S. 1, 2, 7).
   - Mehrere Instrumentfragen setzen einen damaligen Ist-Zustand voraus, etwa „Erhöhung der Abgaben“. Seit 2021 gilt ein nationaler CO₂-Festpreis (§ 10 BEHG).
5. **Die GLES-2025-Frage zur Schuldenbremse („sollte gelockert werden“, q27j) hat ihre Bedeutung während der Feldzeit verändert.** Die Grundgesetzänderung vom 22. März 2025 (BGBl. 2025 I Nr. 94) trat am Tag nach der Verkündung in Kraft. Die Nachwahlbefragung lief vom 24. Februar bis zum 14. bzw. 23. April 2025.
6. **Die aktuellsten Instrumente mit denselben Gegenständen sind GLES 2025 und Eurobarometer 104.1.**
   - GLES 2025: Querschnitt Nachwahl `ZA10100` v4.0.0, Rolling Cross-Section `ZA10101` v3.0.0, Panelwellen 30 und 34.
   - Eurobarometer 104.1 (`ZA9130`, Oktober 2025) mit Fragen zu gemeinsamen EU-Politikfeldern.
   - ALLBUS 2021 (`ZA5280`) enthält Fragen zum Schwangerschaftsabbruch und zum Zuzug von Flüchtlingen nach Gruppen.
   - ISSP 2016 enthält konkrete Überwachungsfragen.
7. **Rechte: Die GESIS-Nutzungsbedingungen (gültig ab 4. Februar 2026) verbieten die Verarbeitung von GESIS-Daten mit KI-Systemen.** Ausnahmen sind nur auf Anfrage möglich. Das betrifft GLES, ALLBUS, ISSP, Eurobarometer und Politbarometer, sobald Agenten sie auswerten sollen.
   - **ALLBUS 2023 hat Zugangskategorie C** und ist nur mit schriftlicher Genehmigung des Datengebers zugänglich. Eurobarometer 104.1 hat Kategorie 0, die übrigen geprüften GESIS-Studien Kategorie A.
   - Das Anzeigen deutscher GESIS-Fragetexte auf einer Website ist nicht geklärt.
   - Die ESS-Dokumentation steht unter CC BY-SA 4.0, die ESS-Daten unter CC BY-NC-SA 4.0.

---

## 2. Aktualität der 43 Fragen

### 2.1 Fundstellen, neuere lokale Runden und Zeitbezüge

Seitenangaben beziehen sich auf die physischen Seiten der lokalen deutschen ESS-Fragebogen-PDFs unter `outputs/loop/breadth-data-001/sources/`. Bei den hier genutzten Seiten stimmen sie mit der aufgedruckten Seitenzahl überein. Feldzeiten in Deutschland laut ESS-API-Abfrage vom 3. Oktober 2026 (Abschnitt 8):

| Runde | Feldzeit | Modus |
| --- | --- | --- |
| ESS5 | 15.09.2010–03.02.2011 | CAPI |
| ESS8 | 23.08.2016–26.03.2017 | CAPI |
| ESS9 | 29.08.2018–04.03.2019 | CAPI |
| ESS10-SC | 05.10.2021–04.01.2022 | Papier/Web |
| ESS11 | 09.05.–21.12.2023 | CAPI |

Spaltenschlüssel: „neuer lokal“ heißt, dieselbe Frage liegt mit wortgleichem deutschem Fragestamm in einer jüngeren lokal vorhandenen Runde vor (höchstens bis ESS11). „ESS12-Quelle“ heißt, sie steht im englischen ESS12-Quellfragebogen. Die deutsche ESS12-Fassung ist nicht öffentlich.

| # | Variable | Herkunft: Runde, Frage, DE-Seite | Neuer lokal? | Zeitbezug, Kontext, Hinweise |
|---|---|---|---|---|
| 1 | `sofrdst` | ESS9 G26, S. 97 | nein (nur ESS9) | Kein Zeitwort. Davor stehen G18–G20 mit konkreten Euro-Schwellen von 2018 (S. 93–95), was den Kontext prägt. |
| 2 | `sofrwrk` | ESS9 G27, S. 97 | nein | wie 1 |
| 3 | `sofrpr` | ESS9 G28, S. 97 | nein | wie 1 |
| 4 | `sofrprv` | ESS9 G29, S. 97 | nein | wie 1 |
| 5 | `gincdif` | ESS11 B33, S. 13 | ist bereits ESS11 | Wortgleich auch in ESS9 B33 (S. 13), ESS10-SC A46 (S. 6) und ESS8 B33 (S. 12). Kein Zeitwort. ESS12-Quelle A46. |
| 6 | `gvslvol` | ESS8 E6, S. 36 | nein | Kein Zeitwort. Der Fragebogen druckt die Skala 0–9, Liste 48 (Listenheft S. 49) zeigt 0–10. |
| 7 | `gvslvue` | ESS8 E7, S. 36 | nein | wie 6 |
| 8 | `gvcldcr` | ESS8 E8, S. 36 | nein | wie 6 |
| 9 | `bnlwinc` | ESS8 E33, S. 42 | nein | Kein Zeitwort. |
| 10 | `eduunmp` | ESS8 E34, S. 42 | nein | „Stellen Sie sich jetzt vor …“ ist ein hypothetisches Szenario, kein Zeitbezug. |
| 11–21 | `fairelc` (B1), `dfprtal` (B2), `medcrgv` (B3), `rghmgpr` (B4), `votedir` (B5), `cttresa` (B6), `gptpelc` (B7), `gvctzpv` (B8), `grdfinc` (B9), `viepol` (B10), `wpestop` (B11) | ESS10-SC, S. 10–11 | nein (Modul nur ESS6/ESS10) | Ausdrücklich „für die Demokratie **im Allgemeinen**“ (S. 10), also ohne Zeitbezug. Gesamtfragebogen mit Pandemie-Hinweis (S. 1, 2, 7). |
| 22 | `scchpldm` | ESS10-SC B25, S. 12 | nein | Kein Zeitwort. |
| 23 | `bplcdc` | ESS5 D18, S. 24 | nein | Pflichtfrage „gegenüber der Polizei in Deutschland“. Kein Zeitwort. |
| 24 | `dpcstrb` | ESS5 D20, S. 24–25 | nein | wie 23 |
| 25 | `hrshsnta` | ESS5 D33, S. 27 | nein | **„… viel härter bestraft werden, als sie heute bestraft werden“.** Die Einleitung spricht von „Aussagen über Deutschland heute“. Das Strafniveau von 2010/11 ist Teil der Frage. |
| 26 | `dbctvrd` | ESS5 D34, S. 27 | nein | Einleitung „Deutschland heute“. Die Aussage selbst ist zeitlos. |
| 27 | `lwstrob` | ESS5 D35, S. 27 | nein | wie 26 |
| 28 | `rgbrklw` | ESS5 D36, S. 27 | nein | wie 26 |
| 29 | `vteurmmb` | ESS10-SC A90, S. 10 | **ja: ESS11 C43, S. 31** | Fragestamm wortgleich („Stellen Sie sich vor, morgen würde eine Volksabstimmung …“). In ESS10-SC sind sechs Antwortoptionen sichtbar gedruckt. In ESS11 werden nur zwei vorgelesen, die übrigen sind spontane Codes (33/44/55/65). ESS9 C41 (S. 29) kodiert „Nicht stimmberechtigt“ als 66, ESS8 E41 (S. 45) hat weniger Kategorien. ESS12-Quelle A89a. |
| 30 | `keydec` | ESS10-SC B12, S. 11 | nein | Wichtigkeit für die Demokratie im Allgemeinen, kein Zeitwort. |
| 31 | `euftf` | ESS11 B37, S. 14 | ist bereits ESS11 | **„… dass sie schon jetzt zu weit gegangen ist“**, bezogen auf den Integrationsstand 2023. ESS12-Quelle A50 mit Fußnote: „Unification“ meint weitere Integration, nicht Erweiterung. |
| 32 | `inctxff` | ESS8 D30, S. 33 | nein | „Erhöhung der Abgaben auf fossile Brennstoffe“ setzt den Ist-Zustand von 2016/17 voraus. Seit 2021 gilt ein nationaler CO₂-Festpreis (§ 10 BEHG). |
| 33 | `sbsrnen` | ESS8 D31, S. 33 | nein | Kein Zeitwort. |
| 34 | `banhhap` | ESS8 D32, S. 33 | nein | Implizit am damaligen Ist-Zustand ausgerichtet. Ob die heutige EU-Ökodesign-Regulierung dem bereits entspricht, habe ich nicht geprüft. |
| 35 | `imsmetn` | ESS10-SC A54, S. 7 | **ja: ESS11 B40, S. 15** | Stamm wortgleich. Die Einleitung unterscheidet sich: ESS10-SC sagt „Bei den folgenden Fragen geht es um …“, ESS11 „Ich möchte Ihnen nun ein paar Fragen … stellen“. ESS11 fügt Listenhinweise hinzu. ESS12-Quelle A53. |
| 36 | `imdfetn` | ESS10-SC A55, S. 7 | **ja: ESS11 B41, S. 15** | wie 35 |
| 37 | `impcntr` | ESS10-SC A56, S. 7 | **ja: ESS11 B42, S. 15** | wie 35 |
| 38 | `imsclbn` | ESS8 E15, S. 37 | nein | Kein Zeitwort. Liste 50 (Listenheft S. 51). |
| 39 | `eqparep` | ESS11 E19, S. 51 | ist bereits ESS11 | Bezieht sich auf den „Bundestag“. Kein Zeitwort. |
| 40 | `eqparlv` | ESS11 E20, S. 52 | ist bereits ESS11 | Vollzeitpaar mit gleichem Verdienst als Szenario. Kein Zeitwort. |
| 41 | `freinsw` | ESS11 E21, S. 52 | ist bereits ESS11 | Kein Zeitwort. |
| 42 | `fineqpy` | ESS11 E22, S. 52 | ist bereits ESS11 | Kein Zeitwort. |
| 43 | `wrkprbf` | ESS8 E35, S. 42 | nein | „zusätzliche Sozialleistungen“ ist relativ zum Stand 2016/17. |

Die Zuordnung der ESS10-B-Fragen zu ihren Variablennamen habe ich über die englischen Variablenlabels der ESS-API geprüft. Grundlage ist die Codex-Projektion `outputs/loop/breadth-catalog-004/allowed-api-projection.json`; die Labels habe ich mit dem Inhalt der deutschen Fragen abgeglichen. Einen eigenen Variablenabruf habe ich dafür nicht gemacht.

Die Web-Fassung von ESS10-SC liegt im lokalen PDF nur als Bildschirmfotos ohne Textschicht vor (ab S. 37). Ich habe nur die Papierfassung wörtlich geprüft.

### 2.2 ESS12

- [ESS-Meldung vom 30.09.2026](https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027): „Data from Round 12 (2025/26) … is expected to be published for the first time in January 2027.“ Die Feldarbeit lief als Modusexperiment: per Zufall entweder Interview oder Selbstausfüller.
- Englischer [ESS12-Quellfragebogen](https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf) (SHA-256 `d5f768fa…`):
  - Kern: A46 `gincdif`, A47–A49 Homosexualitätsfragen, A50 Einigung, A53–A55 Zuwanderungszulassung, A89a EU-Referendum.
  - Rotationsmodul D „Immigration“: D14–D17 zu Asyl (u. a. D16 Großzügigkeit, als „AMENDED ITEM“ aus ESS7 markiert; D15 Arbeitserlaubnis; D17 Festhalten in Zentren).
  - Ein Familiennachzugs-Item habe ich in Modul D nicht gefunden.
- Die deutsche ESS12-Fassung ist unter dem üblichen Pfad nicht abrufbar (`…/round12/fieldwork/germany/ESS12_questionnaires_DE.pdf`: HTTP 404).
- Die ESS-API listet für Deutschland nur ESS1–ESS11.
- Ob Deutschland an ESS12 teilnimmt, habe ich nicht gesondert belegt (Vermutung: ja, als ESS-ERIC-Mitglied).
- **Konsequenz:** ESS12 ist frühestens 2027 nutzbar. Die deutschen Wortlaute müssen dann erneut mit ESS10/11 verglichen werden, denn D16 ist ausdrücklich verändert.

### 2.3 Übertragbarkeit zeitabhängiger Formulierungen auf eine heutige Website

- **Fragen mit explizitem Gegenwartsbezug** fragen nach dem Zustand zur Feldzeit: „heute“, „schon jetzt“, „als bisher“, „weiterhin“, „derzeitig“, „zurzeit“. Wer 2026 auf einer Website antwortet, bezieht „heute“ auf 2026. Ein Vergleich mit den Originalantworten vergleicht dann zwei verschiedene Bezugspunkte. Das gilt insbesondere für:
  - ESS5 `hrshsnta`
  - ESS11 `euftf`
  - GLES q27g („heute schon viel zu weit“) und q27l („als bisher“)
  - ALLBUS `pi01` („heute schon mehr als genug Sozialleistungen“)
  - ISSP 2016 J017 und ISSP 2019 F8b („Steuern … heute“), ISSP 2023 F9 („heutzutage“) und F29 („heute“)
  - fast alle Politbarometer-Fragen („Zurzeit wird darüber diskutiert …“, „Die Bundesregierung plant …“)
- **Implizite Ist-Zustands-Fragen** wie „Erhöhung“, „zusätzliche“ oder „gelockert“ verschieben ihre Bedeutung, wenn sich die Rechtslage ändert. Belegte Beispiele:
  - Schuldenbremse: Grundgesetzänderung März 2025
  - Fossile Abgaben: CO₂-Festpreis seit 2021
  - Kernkraft: Leistungsbetrieb endete mit Ablauf des 15. April 2023 (§ 7 Abs. 1e AtG)
  - Familiennachzug zu subsidiär Schutzberechtigten: bis 23. Juli 2027 ausgesetzt (§ 104 Abs. 14 AufenthG)
  - Adoptionsrecht gleichgeschlechtlicher Ehepaare: seit der Eheöffnung, siehe 4.8
- **Regel für die Website**, ohne den Wortlaut zu ändern: Jeder Vergleich nennt Feldzeit, Population und den rechtlichen Ist-Zustand der Feldzeit. Für einen Vergleich vorrangig zeitlose Fragen wählen. Fragen mit „heute“ vermeidet man entweder oder zeigt sie nur als historische Referenz. Ein ergänzter Erläuterungstext verändert den Kontext und muss als Kontextänderung gekennzeichnet werden (Entwicklungsbedarf, nicht Originaläquivalenz).

---

## 3. Studien, Zugang und Rechte

### 3.1 Übersicht

Feldzeit, Population und Modus stammen aus den jeweiligen Dokumentationen. Zugangskategorien laut GESIS-OAI-Metadaten bzw. Studiendokumentation; Fundstellen in Abschnitt 8.

| Kürzel | Studie, Archiv, Version, DOI | Feldzeit DE | Population | Modus | Zugang |
|---|---|---|---|---|---|
| E5/E8/E9/E10SC/E11 | ESS-Integrated-Files, lokal: 3.6 / 2.3 / 3.3 / SC 3.2 / 4.2 | siehe 2.1 | ab 15 Jahren in Privathaushalten, unabhängig von der Staatsangehörigkeit (ESS10-Universe laut ESS-Metadaten) | siehe 2.1 | lokal vorhanden; Daten CC BY-NC-SA 4.0 |
| G25 | GLES Querschnitt 2025 Nachwahl, ZA10100, v4.0.0, doi:10.4232/5.ZA10100.4.0.0; Fragebogendokumentation 1.3 vom 12.08.2026 | CAWI 24.02.–14.04.2025; Papier 24.02.–23.04.2025 (Doku S. 6) | deutsche Staatsangehörige ab 16 mit Hauptwohnsitz (S. 11) | CAWI/Papier, Register-Mehrstufenstichprobe; etwa ein Fünftel der Sample Points über Post Direkt (S. 9, 11) | „Safeguarded – A“ (Doku S. 7), OAI: A |
| R25 | GLES Rolling Cross-Section 2025, ZA10101, v3.0.0 (13.02.2026), doi:10.4232/5.ZA10101.3.0.0 | Vorwahl 06.01.–22.02.2025; Ergänzung 20.01.–31.03.; Nachwahl 25.02.–31.03.2025 (S. 6) | Wahlberechtigte in Privathaushalten (S. 11) | CAWI; Ziehung aus dem PAYBACK-Panel (S. 11) | A (S. 7) |
| P30 | GLES Panel 2025, Welle 30, ZA10119, v1.0.0 | 12.–22.02.2025 (S. 3) | wahlberechtigte deutsche Bevölkerung | CAWI; **Quotenstichprobe, nicht probabilistisch** (S. 3–4) | A (S. 4) |
| P34 | GLES Panel 2026, Welle 34, ZA10123, v1.0.0 (18.05.2026) | 23.03.–07.04.2026 (S. 3) | wie P30 | CAWI; **Quotenstichprobe** | Safeguarded – A (S. 4) |
| I16 | ISSP 2016 Role of Government V, ZA6900, v2.0.0, doi:10.4232/1.13052 | 05.04.–18.09.2016 (OAI) | nicht separat geprüft | Selbstausfüller am Laptop (CASI) im Anschluss an das ALLBUS-Interview (DE-Fragebogen S. 3) | A |
| I19 | ISSP 2019 Social Inequality V, ZA7600, v3.0.0, doi:10.4232/1.14009 | 30.07.–30.09.2020 (techn. Bericht/OAI) | nicht separat geprüft | Papierfragebogen (DE-Fragebogen S. 3–4) | A |
| I20 | ISSP 2020 Environment IV, ZA7650, v2.0.0, doi:10.4232/1.14153 | 14.06.–18.08.2021 | ab 18, jede Nationalität, inkl. Anstaltshaushalte (techn. Bericht S. 8) | postalischer Papierfragebogen (techn. Bericht S. 5) | A |
| I22/I23 | ISSP 2022 Family V, ZA10000, v2.0.0; ISSP 2023 National Identity, ZA10010, v1.0.0 | gemeinsames Instrument, 17.05.–01.08.2023 | ab 18, jede Nationalität (I23 techn. Bericht S. 8) | Papier (I23 techn. Bericht S. 5) | A |
| A21 | ALLBUS 2021, ZA5280, v2.1.0, doi:10.4232/1.14626 | 06–08/2021 | Personen (Deutsche und Ausländer) in Privathaushalten, geboren vor 01.01.2003 (OAI) | MAIL/CAWI; Splits A/B/C | **A** |
| A23 | ALLBUS 2023, ZA8830, v1.2.0, doi:10.4232/1.14544 | 04–09/2023 | wie A21, geboren vor 01.01.2005 | CAPI sowie MAIL/CAWI | **C** (nur mit schriftlicher Genehmigung des Datengebers) |
| EB104 | Eurobarometer 104.1, ZA9130, v1.0.0, doi:10.4232/1.14793 | DE 09.–29.10.2025 (OAI) | Staatsangehörige des jeweiligen Landes und EU-Bürger ab 15 (DataCite) | CAPI/Web | **0** („für jedermann freigegeben“) |
| PB25 | Politbarometer 2025 kumuliert, ZA9151, v1.0.0, doi:10.4232/1.14794 | Wellen 2025 | „Wahlberechtigte Wohnbevölkerung“ (OAI) | CATI/CAWI, Dual-Frame | A |
| WOM25 | Wahl-O-Mat Bundestagswahl 2025 (bpb) | – | – | **keine Befragung**, nur Beleg für die Salienz einer Streitfrage | – |

Zur ALLBUS-Welle 2024: Eine DataCite-Suche nach dem Titel „ALLBUS 2024“ ergab keinen Treffer. Vermutung: Es gibt keine ALLBUS-Welle 2024, die nächste wäre 2025.

ISSP 2024 (Digital Societies, ZA10020 v1.0.0, 2026) ist laut DataCite veröffentlicht. Einen deutschen Fragebogen habe ich nicht gefunden. Das Thema betrifft R1.

### 3.2 Wörtliche Bedingungen

**ESS** ([Disclaimer](https://www.europeansocialsurvey.org/contact/disclaimer), abgerufen am 3.10.2026 um ca. 19:23 UTC):
> „European Social Survey data is licensed under CC BY-NC-SA 4.0“ – „European Social Survey documentation is licensed under CC BY-SA 4.0“ – „The data are available without restrictions, for not-for-profit purposes.“ – „ESS ERIC recommends that ESS datasets are not made available on external websites. Instead, please link to datasets on the ESS Data Portal.“ – „If a dataset is modified in any way, including translation changes, this should be indicated in the citation ‘Adapted from ESS Round X, version number X’.“

Folgerung:
- Zusammengefasste Ergebnisse auf einer nichtkommerziellen Website sind mit Namensnennung möglich. Abgeleitete Datenprodukte stehen unter NC-SA.
- Deutsche ESS-Wortlaute (Dokumentation) dürfen mit Namensnennung angezeigt werden. Abwandlungen sind unter CC BY-SA weiterzugeben.
- Offen: die Sikt-Download-Bedingungen, die ich nicht gelesen habe, und mögliche KI-Klauseln dort. Im Disclaimer habe ich keine gefunden.

**GESIS-Nutzungsbedingungen, „Gültig ab: 04.02.2026“.** Direkter Abruf HTTP 403. Gelesen über den [Wayback-Schnappschuss vom 30.03.2026](http://web.archive.org/web/20260330121100/https://www.gesis.org/institut/datennutzungsbedingungen), SHA-256 der HTML-Datei `10e14137…`:
> § 1: „Soweit nicht ausdrücklich anders gekennzeichnet, stellt GESIS die Datenbasis nur für wissenschaftliche Nutzungen im Rahmen eines zeitlich befristeten Vorhabens zur Verfügung.“
> § 4: „Soweit nicht ausdrücklich anders gekennzeichnet, ist eine kommerzielle Nutzung der von GESIS bereitgestellten Daten verboten.“ – „Eine Weitergabe der bereitgestellten Datenbasis an Dritte ist nicht gestattet.“ – **„Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“** – „Die Nutzung ist insbesondere auf die nach dem Urheber-, Marken- und Patentrecht zulässige Nutzung beschränkt.“
> § 5: „Die Darstellung oder Publikation von Einzelfällen … ist nicht erlaubt. … Zulässig sind zusammenfassende Darstellungen der Daten, wie sie in wissenschaftlichen Arbeiten und Vorträgen üblich sind.“
> § 6: Nach Erfüllung des Nutzungszwecks ist die Datenbasis „vollständig zu löschen. Jegliche Weiterverwendung der Datenbasis … ist unzulässig.“
> § 7: Pflicht zur Angabe von DOI und Version. § 8: „Der Nutzer / die Nutzerin hat GESIS die Veröffentlichung anzuzeigen.“

Die Tabelle der Zugangskategorien in § 2 war im Schnappschuss nicht enthalten.

**GESIS-Impressum, Copyright.** Direkter Abruf HTTP 403. Gelesen über den [Wayback-Schnappschuss vom 09.09.2026](http://web.archive.org/web/20260909155242/https://www.gesis.org/institut/impressum):
> „Das Copyright für veröffentlichte, von GESIS selbst erstellte Objekte bleibt allein bei GESIS. Eine Vervielfältigung oder Verwendung solcher Grafiken, Tondokumente, Videosequenzen und Texte in anderen elektronischen oder gedruckten Publikationen ist ohne ausdrückliche Zustimmung von GESIS nicht gestattet.“

**GLES-2025-Dokumentation**, S. 7, Abschnitt 1.9:
> „Daten und Dokumente sind für die wissenschaftliche, studentische und nicht kommerzielle Nutzung freigegeben: Zugangskategorie Safeguarded – A.“

**GESIS-OAI-Zugangsangaben** (`dbkapps.gesis.org/dbkoai`):
- ZA9130: „0 - Daten und Dokumente sind für jedermann freigegeben.“
- ZA8830: „C - Daten und Dokumente sind für die akademische Forschung und Lehre nur nach schriftlicher Genehmigung des Datengebers zugänglich. Das Datenarchiv holt dazu schriftlich die Genehmigung unter Angabe des Benutzers und des Auswertungszweckes ein.“
- ZA5280, ZA6900, ZA7600, ZA7650, ZA10000, ZA10010, ZA10100, ZA10101, ZA10119, ZA10123 und ZA9151: „A - Daten und Dokumente sind für die akademische Forschung und Lehre freigegeben.“

Die DataCite-Metadaten nennen CC0 nur für die **Katalog-Metadaten** („Alle im GESIS DBK veröffentlichten Metadaten sind frei verfügbar unter … CC0“). Das ist keine Lizenz für Fragebogentexte oder Daten.

### 3.3 Was für die Website folgt und was offen bleibt

- **Zusammengefasste Ergebnisse aus GESIS-Studien:** § 5 erlaubt „zusammenfassende Darstellungen … wie … in wissenschaftlichen Arbeiten und Vorträgen üblich“. Offen sind drei Punkte:
  - ob ein öffentliches, interaktives Testangebot als „wissenschaftliche Nutzung“ eines „zeitlich befristeten Vorhabens“ gilt;
  - wie sich die Löschpflicht nach § 6 mit dauerhaft angezeigten Referenzwerten verträgt;
  - ob ein indirekter wirtschaftlicher Nutzen ausgeschlossen ist.
  Das sollte vorab schriftlich bei GESIS geklärt werden. Kontakt laut § 1: Oliver Watteler.
- **KI-Verbot:** Jede Auswertung von GESIS-Daten durch Codex- oder Claude-Agenten wäre ohne Ausnahmegenehmigung ein Verstoß. Mögliche Wege:
  - Ausnahme beantragen (Bedingung: alleinige Kontrolle über das KI-System, ausschließlich wissenschaftlicher Zweck);
  - Auswertung durch Menschen mit Skripten ohne KI-Verarbeitung der Datenbasis. Ob agentengeschriebene, aber von Menschen ausgeführte Skripte zulässig sind, ist **offen**.
- **Deutsche Fragetexte von GLES, ALLBUS, ISSP-DE und Politbarometer:** Die Fragebogendokumentationen sind GESIS-Publikationen. Nach dem Impressum braucht ihre Vervielfältigung in anderen elektronischen Publikationen eine ausdrückliche Zustimmung. Ob das für einzelne Fragewortlaute gilt und wer bei ISSP oder Politbarometer (Forschungsgruppe Wahlen) die Rechte hält, ist **offen**.
- **Eurobarometer:** Kategorie 0 erleichtert den Datenzugang. Die Nutzungsbedingungen von GESIS gelten auch hier. Die Rechte an den Fragetexten (Europäische Kommission) habe ich nicht geprüft.
- **ALLBUS 2023:** Kategorie C, also Genehmigung des Datengebers nötig. Für Zuzugsfragen und Abtreibungsfragen ist ALLBUS 2021 (Kategorie A) die zugänglichere Alternative.

---

## 4. Bereiche

Für jeden Bereich: (a) Streitfragen 2021–2026, (b) Reichweite der vorhandenen Fragen, (c) Originalfragen für die größten Lücken, (d) Bewertung, (e) Empfehlung.

Als Salienzbeleg dienen die 38 offiziellen Thesen des Wahl-O-Mat 2025, ausgelesen aus der [bpb-Definitionsdatei](https://www.wahl-o-mat.de/bundestagswahl2025/app/definitionen/module_definition.js) (SHA-256 `b3e9bb84…`). Laut [bpb-Pressemitteilung vom 06.02.2025](https://www.bpb.de/die-bpb/presse/pressemitteilungen/559069/wahl-o-mat-zur-bundestagswahl-2025-geht-online/) gibt es 38 Thesen, die in einem Redaktionsprozess mit 36 Beteiligten entstanden sind. Die Thesen zeigen nur, dass eine Streitfrage im Wahlkampf zur Wahl stand. Sie sind keine Befragungsfragen und liefern keine Vergleichswerte. Parteipositionen habe ich weder gelesen noch berichtet. Wahlprogramme habe ich nicht geöffnet und schreibe deshalb keiner Partei eine Forderung zu.

Weitere Belege sind die Studiendokumentationen selbst (eine Frage wurde erhoben, weil der Gegenstand als Streitfrage galt) und Rechtsquellen, die den Stand der Rechtslage belegen. Politikwissenschaftliche Fachliteratur zu den deutschen Streitfragen 2021–2026 habe ich in dieser Runde **nicht** im Volltext geöffnet. Das ist eine Grenze (Abschnitt 8).

### 4.1 Wirtschaft und Verteilung

**a) Streitfragen**
- Schuldenbremse beibehalten oder lockern: WOM-These 22.
  - Erhoben in G25 q27j, R25 pre038a/pos047a, P34 `kp34_2880br` sowie in den Bewertungsfragen P34 DL/DM/DN.
  - PB25 V19 fragt, ob es richtig ist, die Schuldenbremse für Verteidigungsausgaben zu lockern (Fragebogenstand 21.03.2025, PDF-S. 126).
  - Rechtslage: [BGBl. 2025 I Nr. 94](https://www.recht.bund.de/bgbl/1/2025/94/regelungstext.pdf). Verteidigungsausgaben über 1 % des BIP werden von der Kreditgrenze abgezogen; den Ländern sind 0,35 % des BIP erlaubt (Art. 109); ein Sondervermögen von bis zu 500 Mrd. Euro wird zugelassen (Art. 143h). In Kraft am Tag nach der Verkündung vom 24.03.2025.
  - R25 nahm am Abend des 06.03.2025 eine Frage zum „Finanzpaket für Verteidigung und Infrastruktur“ auf (R25 S. 287).
- Spitzensteuersatz und Besteuerung hoher Einkommen: WOM 13; G25 q27l; PB25 V25 (S. 32), V41/V48.
- Unternehmenssteuern: PB25 V26 (S. 33).
- Mindestlohn von 15 Euro: WOM 38; P34 AJ. Arbeitszeit, 35-Stunden-Woche: WOM 25. Beides vertieft R2.
- Streikrecht in der kritischen Infrastruktur: WOM 31.
- Strompreisausgleich für energieintensive Unternehmen: WOM 8.
- Lieferkettenpflichten: WOM 20.
- EU-Zölle auf chinesische E-Autos: WOM 34.
- Staatliche Rolle in der Wirtschaft: G25 q27c; P34 G.
- Enteignung von Konzernen: P34 AP. Preisobergrenzen für Energie und Grundnahrungsmittel: P34 CN.
- Mietregulierung: WOM 6; G25 q27i. Gehört zu R2.

**b) Reichweite.** Vier Gerechtigkeitsprinzipien (ESS9, 2018/19) und `gincdif` (ESS11, 2023) erfassen Verteilungsnormen und die allgemeine Zustimmung zu staatlicher Einkommensangleichung. **Nicht erfasst:** Steuerhöhe und Progression, Staatsverschuldung und Schuldenbremse, Marktregulierung, Industrie- und Handelspolitik, Mindestlohn, Arbeitszeit. Der Bereich trägt deshalb den Namen „Verteilungsgerechtigkeit“, nicht „Wirtschaftspolitik“.

**c) Originalfragen für die Lücken**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut (gekürzt), Skala, Filter |
|---|---|---|---|---|
| Schuldenbremse | G25 | q27j | Doku S. 144, PAPI F61 | „Die Schuldenbremse sollte gelockert werden.“ 1 = stimme voll und ganz zu … 5 = stimme überhaupt nicht zu, −99. Kein Filter. **Bedeutung änderte sich während der Feldzeit.** |
| Schuldenbremse 2026 | P34 | kp34_2880br, dl, dm, dn | S. 28 | br: „Die Schuldenbremse sollte gelockert werden.“; dl: „Es ist sinnvoll, dass für Verteidigungsausgaben die Schuldenbremse aufgehoben wurde.“ u. a.; 1 … 5. Quotenstichprobe. |
| Steuern für Reiche | G25 | q27l | S. 159, F69 | „Reiche Bürger/innen sollten mehr Steuern bezahlen als bisher.“ („als bisher“ ist Zeitbezug) |
| Steuerprogression (zeitlos) | I19 | F8a | DE-Fragebogen S. 6 | „Sollten Leute mit hohem Einkommen einen GRÖßEREN ANTEIL ihres Einkommens an Steuern zahlen … den GLEICHEN … oder einen KLEINEREN ANTEIL?“ Fünf Kategorien und „Kann ich nicht sagen“. |
| Steuern und Sozialstaat | G25 | q40 | S. 108, F41 | 1 = „weniger Steuern und weniger sozialstaatliche Leistungen“ … 11 = „mehr sozialstaatliche Leistungen und mehr Steuern“. **Der erklärende Einleitungstext steht in der vorangehenden Parteieinstufung q39 (S. 106).** Eine selbsterklärende Fassung ohne Parteieinstufung bietet R25 pos044 (S. 280). |
| Marktordnung | G25 | q27c | S. 147, F63 | „Der Staat sollte sich aus der Wirtschaft heraushalten.“ |
| Wirtschaftspolitische Eingriffe | I16 | J005 A–F | S. 8 | Kürzungen der Staatsausgaben; Beschäftigungsprogramme; „Weniger gesetzliche Vorschriften für Handel und Industrie“; Unterstützung der Industrie bei neuen Produkten; Unterstützung niedergehender Industriezweige; Arbeitszeitverkürzung. Befürworte stark … lehne stark ab. Stand 2016. |
| Mindestlohn | P34 | kp34_2880aj | S. 50 | „Der Mindestlohn in Deutschland sollte deutlich angehoben werden.“ Quotenstichprobe. |
| Zusätzliche Verteilungsprinzipien (lokal) | E8 | E1 `dfincac`, E2 `smdfslv` | S. 34 | „Große Einkommensunterschiede sind gerechtfertigt, um unterschiedliche Begabungen und Leistungen angemessen zu belohnen.“ / „Damit eine Gesellschaft gerecht ist, sollten die Unterschiede im Lebensstandard der Menschen gering sein.“ 1–5. Verbreitert den Bereich nicht, nur weitere Verteilungsnormen. |

**d) Bewertung: teilweise abgedeckt.**
- Die fehlenden Facetten sind **Datenlücken**: Der ESS enthält in den lokalen Runden keine Fragen zu Steuern, Verschuldung oder Regulierung. Ich habe die lokalen DE-Fragebögen nach „Steuer“, „Mindestlohn“ und „Vermögen“ durchsucht.
- Erlaubte Interpretation: konkrete Einzelangaben.
- Keine gemeinsame „Wirtschaftsdimension“. Die vier ESS9-Prinzipien sind laut `abdeckung-v2.md` ausdrücklich nicht als Faktor angenommen; ich sehe keinen Grund, davon abzuweichen.
- Ein formativer Wert wäre nur mit begründeten Gewichten zulässig. Solche Gewichte liegen nicht vor.

**e) Empfehlung**
1. G25 q27c (Staat aus der Wirtschaft) und q27l (Steuern für Reiche). Beide sind aktuell, haben einen Deutschlandbezug und stammen aus einer Wahrscheinlichkeitsstichprobe. Rechte: Kategorie A, KI-Klausel, Wortlautrechte offen.
2. Schuldenbremse: G25 q27j nur mit ausdrücklicher Feldzeit- und Rechtsstand-Kennzeichnung. Alternativ P34 `br` aus 2026, aber aus einer Quotenstichprobe ohne Repräsentativitätsanspruch; dann nur als Panelreferenz kennzeichnen.
3. ISSP 2019 F8a (Progression) als zeitlose Steuerfrage. Feldzeit 2020, Papier.
4. G25 q40 nur zusammen mit dem Einleitungstext. Die selbsterklärende Fassung R25 pos044 hat eine andere Population (PAYBACK-Panel).
5. Mindestlohn, Arbeitszeit und Mietrecht an R2 übergeben. ISSP 2016 J005 nur als historische Ergänzung.

### 4.2 Sozialstaat

**a) Streitfragen**
- Grundsicherung (Bürgergeld): Höhe und Sanktionen. WOM 3 („Das Bürgergeld soll denjenigen gestrichen werden, die wiederholt Stellenangebote ablehnen.“); G25 q27k; PB25 V41/V43 („Die Bundesregierung plant, die Regelungen beim Bürgergeld zu verschärfen“); P34 DE.
- Rente: WOM 9 und 29; P34 CO; PB25 Rentenfragen. Gesundheit und Krankenversicherung: WOM 16. Beides vertieft R2.
- Abwägung zwischen Steuern und Sozialleistungen: G25 q40; ALLBUS `pi07`.

**b) Reichweite.** ESS8 (2016/17) erfasst die staatliche Verantwortung für Alter, Arbeitslose und Kinderbetreuung, die Zielgruppenorientierung (`bnlwinc`) und die Abwägung zwischen Ausbildung und Unterstützung (`eduunmp`). **Nicht erfasst:** Konditionalität und Sanktionen, Leistungshöhe, Finanzierung, Rente im Detail, Gesundheit und Pflege.

**c) Originalfragen**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut, Hinweis |
|---|---|---|---|---|
| Sanktionen und Konditionalität (lokal) | E8 | E21–E32 Vignetten (`ubpay`, `ubedu`, `ubunp`, Varianten für 50–60-Jährige, 20–25-Jährige, Alleinerziehende) | S. 38–41 | „Was sollte … mit der Arbeitslosenunterstützung geschehen, wenn diese Person … eine Stelle ablehnt, weil sie viel schlechter bezahlt ist …?“ Vier Kategorien von „gesamte … verlieren“ bis „weiterhin … bekommen“. **Zufallszuweisung auf vier Gruppen (E20)**, also je Zweig etwa ein Viertel der Stichprobe als Nenner. Interviewerhinweis: ALG I und II gemeint, Stand 2016/17. |
| Grundeinkommen (lokal) | E8 | E36 `basinc` | S. 43 | Sechs Merkmale auf Liste 54. Einleitung „In einigen Ländern wird **momentan** über die Einführung eines Grundeinkommens diskutiert“, ein Zeitbezug. Nur mit vollständiger Definition verwenden. |
| Bürgergeld-Höhe | G25 | q27k | S. 159, F69 | „Das Bürgergeld sollte deutlich abgesenkt werden.“ Einseitig gerichtete Aussage, nur wörtlich interpretieren. |
| Ausbau oder Kürzung | A21 | F039 (`pi07`), F040/F041 (`pi01`/`pi02`) | CAWI-Doku S. 50–51 | Steuersenkung oder mehr Geld für soziale Leistungen; „heute schon mehr als genug Sozialleistungen“ (Zeitbezug), gefiltert über `pi01`. In A23 als F067–F069 (CAPI-Doku S. 52), aber Kategorie C. |
| Ausgaben und Zuständigkeit | I16 | J006, J007 | S. 9–10 | Ausgaben „mehr/weniger“ mit Hinweis auf Steuern; Option „die Ausgaben auf dem jetzigen Stand halten“ ist ein Zeitbezug. Zuständigkeit u. a. für Gesundheitsversorgung und Wohnung. Stand 2016. |

**d) Bewertung: teilweise abgedeckt.** Zuständigkeiten sind gut erschlossen. Konditionalität und Leistungshöhe fehlen in den 43 Fragen. Das ist teils eine **bewusste Auslassung**: Der Plan klammert die Vignetten wegen der Zufallszweige aus, nicht wegen fehlender Daten. Teils ist es eine **Datenlücke**: Der ESS hat keine Frage zum Bürgergeld. Erlaubte Interpretation: Einzelangaben. Vignettenantworten nur im tatsächlich gestellten Zweig auswerten, keine gemeinsame Skala über Zweige.

**e) Empfehlung**
1. E8 Vignettengruppe 1 (E21–E23). Sofort lokal auswertbar. Historischer Kontext (Hartz IV), Zweig-Nenner.
2. G25 q27k nur mit dem Hinweis, dass es eine Richtungsaussage ist. A21 F039–F041 (Kategorie A) als zweite Quelle. Rente und Gesundheit übernimmt R2.

### 4.3 Demokratie und politische Autorität

**a) Streitfragen**
- Volksentscheide auf Bundesebene: WOM 32. Erhoben in G25 q156c („Bürgerinnen/Bürgern bei Volksabstimmungen“) und q51b.
- Wahlalter 16 bei Bundestagswahlen: G25 q27n, R25 pre038f.
- Gottesbezug in der Präambel des Grundgesetzes: WOM 10.
- Bundesförderung von Projekten gegen Rechtsextremismus: WOM 19.
- Gesetzgebung mit Mehrheiten, die nur mit Stimmen der AfD zustande kommen: G25 q27p, R25 pre034g, P30/P34 DJ. Diese Fragen nennen eine Partei namentlich.
- Ob der 2021 gewählte Bundestag die Grundgesetzänderung beschließen durfte: P34 DN.

**b) Reichweite.** ESS10-SC B1–B11 und B25 erfassen breit, wie wichtig demokratische Prinzipien sind (Wahlen, Medien, Minderheiten, direkte Demokratie, Gerichte, Rechenschaft, sozialer Schutz, Volkswille) und wie Responsivität gegen Planbindung abgewogen wird. **Nicht erfasst:** konkrete Institutionenreformen (Wahlalter, Volksentscheid als konkrete Reform, Wahlrecht, Föderalismus), das Verhältnis von Mehrheitswille und Gerichtskontrolle in Konfliktfällen, Umgang mit Parteien.

**c) Originalfragen**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut, Hinweis |
|---|---|---|---|---|
| Wahlalter | G25 | q27n | S. 166, F73 | „Das Wahlalter bei Bundestagswahlen sollte von 18 auf 16 Jahre gesenkt werden.“ |
| Konkrete Autoritätskonflikte | G25 | q167a–g | S. 157, F68 | u. a. „Der Regierung sollte es möglich sein, Gerichtsurteile zu ignorieren …“, „Wenn der Bundestag die Arbeit der Regierung behindert, sollte er übergangen werden.“ |
| Gerichtskontrolle | G25 | q51h | S. 153, F66 | „Die Gerichte sollten in der Lage sein, die Regierung zu stoppen, wenn sie ihre Befugnisse überschreitet.“ |
| Volksentscheid statt Politik | G25 | q156c | S. 162, F71 | Rahmen: „Statt von gewählten Politikerinnen und Politikern würde das Land besser regiert werden, wenn wichtige politische Entscheidungen … überlassen würden: Bürgerinnen/Bürgern bei Volksabstimmungen“. Andere Konstruktlogik als WOM 32. |
| Ziviler Ungehorsam, Minderheitenrechte | I23 | F13 | S. 9 | Wichtigkeit 1–7; das Ungehorsams-Item ist ausführlich definiert. |
| Autoritätswerte (lokal) | E10SC A51–A53; E11 B38/B39 | – | E10 S. 6; E11 S. 14 | „starke Führungsperson …, die über dem Gesetz steht“; Gehorsam und Loyalität. Wertfragen, keine Reformpräferenzen; Variablennamen nicht geprüft. |

**d) Bewertung: teilweise abgedeckt, für Prinzipien substanziell.** Die konkreten Reformen sind eine **Datenlücke** in den lokalen ESS-Runden. Die Bewertungsfragen B13–B24 sind ein **bewusster Ausschluss**, um Präferenz und wahrgenommene Realität zu trennen; das halte ich für begründet. Fragen mit Parteinamen (q27p, DJ) würden eine Parteireferenz in ein parteineutrales Profil tragen. Ich empfehle sie nicht.

Erlaubte Interpretation: Einzelangaben. Ein Index „liberale“ oder „direkte“ Demokratie bräuchte einen eigenen Prüfplan. Literaturhinweise zu Dimensionen der ESS-Demokratiefragen habe ich nicht geöffnet.

**e) Empfehlung**
1. G25 q27n (Wahlalter).
2. G25 q167e/f (Gerichtsurteile ignorieren, Bundestag übergehen) zusammen mit q51h als konkrete Gewaltenteilungsfragen.
3. Für Volksentscheide genügt vorerst ESS10 `votedir`. Eine Bundesreform-Frage im Wortlaut der WOM-These habe ich in keiner geöffneten Befragung gefunden (**Lücke**).

### 4.4 Bürgerrechte und Sicherheit

**a) Streitfragen**
- Automatisierte Gesichtserkennung an Bahnhöfen: WOM 7.
- Strafmündigkeit unter 14: WOM 33.
- Streikrecht: WOM 31.
- Pandemiebedingte Grundrechtseinschränkungen 2021/22: dokumentiert als Erhebungsgegenstand in ESS10-SC A1–A5 (S. 2).
- Überwachung, Vorratsdatenspeicherung, Datenschutz: R1. Ich habe dazu keine eigene Rechtsquelle geöffnet.

**b) Reichweite.** ESS5 (2010/11) erfasst die Pflicht, Polizei- und Gerichtsentscheidungen zu folgen, Gesetzesgehorsam und Strafhärte. **Nicht erfasst:** staatliche Überwachung und Daten, Versammlungs- und Protestrecht, Strafverfahrensgarantien, Strafmündigkeit.

**c) Originalfragen**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut, Hinweis |
|---|---|---|---|---|
| Überwachung | I16 | J011 A/B, J013 A/B, J014 A–C | S. 13–15 | „Sollten staatliche Behörden in Deutschland … das Recht … haben … Menschen im öffentlichen Bereich mit Videokameras zu überwachen? / E-Mails … zu überwachen?“; Terrorverdacht: „ohne richterliche Anordnung beliebig lange in Haft zu nehmen“, „Telefongespräche abzuhören“, „einfach so auf der Straße anzuhalten und zu durchsuchen“. Auf jeden Fall / Eher ja / Eher nein / Auf keinen Fall / Kann ich nicht sagen. Stand 2016. |
| Protestrecht | I16 | J002 A/B, J003 | S. 6–7 | Öffentliche Versammlungen und Demonstrationen gegen die Regierung erlauben. |
| Gesetz oder Gewissen | I16 | J001 | S. 6 | Nahe an `rgbrklw`, aber anderes Format (zwei Optionen). |
| Gerichte zu hart oder zu milde | A21 | F035 (`ca24`) | S. 45 | Zu hart / zu milde / gerade richtig. Split B zeigt „Weiß nicht“ sichtbar an, Splits A und C nicht. |
| Pandemie: Überwachung gegen Privatsphäre (lokal) | E10SC | A2 | S. 2 | 0–10 von „Viel wichtiger, die Bevölkerung zu überwachen und nachzuverfolgen“ bis „… die Privatsphäre des Einzelnen zu bewahren“. Pandemiegebunden; Variablenname nicht geprüft. |
| Strafzumessung (lokal) | E5 | D38 `stcbg2t` | S. 27 | Szenario Wiederholungseinbruch. |

**d) Bewertung: teilweise abgedeckt, mit großer Zeitlücke.**
- Die neuesten konkreten Überwachungsfragen stammen aus 2016 (I16). Die Bürgerrechtsfragen der 43 stammen aus 2010/11. Das ist eine **Datenlücke**: G25 enthält keine Überwachungsfragen; q167a betrifft Zensur.
- Zu Gesichtserkennung und Strafmündigkeit habe ich in keinem geöffneten Instrument eine Bevölkerungsfrage gefunden.
- ALLBUS 2021 F051 (Wiedereinführung der Todesstrafe) ist keine aktuelle Streitfrage im WOM-2025-Sinn. Ich empfehle sie nicht und schließe sie bewusst aus.

**e) Empfehlung**
1. ISSP 2016 J011, J013 und J014 als einziger geprüfter konkreter Überwachungsweg. Stand 2016 deutlich kennzeichnen. Abgleich mit R1.
2. ESS5-Fragen mit „heute“-Bezug (`hrshsnta`) nicht als heutige Norm zeigen.
3. Neuere Instrumente zu Überwachung und Datenschutz sind über R1 zu suchen.

### 4.5 Europäische Integration

**a) Streitfragen**
- Euro durch eine nationale Währung ersetzen: WOM 27.
- EU-Handelspolitik und Zölle: WOM 34.
- Mitgliedschaft: ESS `vteurmmb`, I23 F29.
- Vertiefung: G25 q27f, ESS `euftf`.
- Gemeinsame Außen-, Verteidigungs-, Migrations-, Energie- und Klimapolitik, Erweiterung, Euro: EB104 QB1.
- Bewerberstatus der Ukraine: EB104 ST0350.

**b) Reichweite.** Mitgliedschaft, Integrationsrichtung und die Prinzipienfrage „national statt EU“ sind erfasst. **Nicht erfasst:** konkrete gemeinsame Politikfelder, Euro, Erweiterung, Finanzsolidarität.

**c) Originalfragen**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut, Hinweis |
|---|---|---|---|---|
| Gemeinsame Politikfelder, Euro, Erweiterung | EB104 | QB1 / SE037 Items 1–11 | DE-Fragebogen (GESIS-Dok. 81730) S. 10–11 | „Wie ist Ihre Meinung zu den folgenden Aussagen? Bitte sagen Sie für jede Aussage, ob Sie dafür oder dagegen sind.“ U. a. „Eine gemeinsame Verteidigungs- und Sicherheitspolitik der EU-Mitgliedstaaten“, „Eine gemeinsame europäische Einwanderungspolitik“, „Eine gemeinsame europäische Energiepolitik“, „Eine Erweiterung der EU, um in den nächsten Jahren andere Länder aufzunehmen“, „Eine europäische Wirtschafts- und Währungsunion mit einer gemeinsamen Währung, dem Euro“, „Eine gemeinsame Klimapolitik“. Dafür / Dagegen; „Weiß nicht“ laut Researcher Note „HIDESPECIAL CODE 999“. Zweistufig. |
| EU-Solidarität (lokal) | E8 | E37 `eusclbf` | S. 44 | EU-weites Sozialleistungsprogramm für arme Menschen mit drei Merkmalen, finanziert stärker von reicheren Ländern. Sehr dagegen … sehr dafür. |
| Macht der EU, Befolgen von EU-Entscheidungen | I23 | F27, F28 | S. 12 | Filter: F25 „Überhaupt nichts“ gehört → weiter bei F30. |
| Vertiefung 2025 | G25 | q27f | S. 144 | „Die europäische Einigung sollte weiter vorangetrieben werden.“ Gegenstand wie `euftf`, aber Zustimmungsformat statt bipolarer Skala; nicht austauschbar. |

**d) Bewertung: teilweise abgedeckt.** Politikfelder sind eine **Datenlücke** im ESS; EB104 schließt sie. Erlaubte Interpretation: Einzelangaben. Kein Gesamtwert „pro/anti EU“. Nichtwahl- und Nichtberechtigungskategorien bleiben eigene Kategorien.

**e) Empfehlung**
1. EB104 QB1 Items 2 (Verteidigung), 4 (Einwanderung), 5 (Energie), 6 (Erweiterung) und 9 (Euro). Aktuell (Oktober 2025), Kategorie 0. Population: Deutsche und EU-Bürger ab 15. Wortlautrechte offen.
2. E8 E37 sofort lokal auswertbar (historisch).
3. `vteurmmb`: bewusst zwischen ESS10-SC (sichtbare Nichtantwortkategorien, selbstausgefüllt wie eine Website) und ESS11 (neuer, CAPI) entscheiden.

### 4.6 Klima und Energie

**a) Streitfragen**
- Kernenergie wieder nutzen: WOM 12. Rechtslage: Der Leistungsbetrieb von Isar 2, Emsland und Neckarwestheim 2 endete mit Ablauf des 15.04.2023 ([§ 7 Abs. 1e AtG](https://www.gesetze-im-internet.de/atg/__7.html)).
- Staatliche Förderung erneuerbarer Energien: WOM 2.
- Fossile Heizungen weiter erlauben: WOM 37. Die Fundstelle heißt bei gesetze-im-internet.de inzwischen „Gebäudemodernisierungsgesetz – GModG“, [§ 71](https://www.gesetze-im-internet.de/geg/__71.html) ist „(weggefallen)“. Datum und Umfang der Änderung habe ich nicht geprüft.
- Tempolimit: WOM 4; G25 q27m.
- Klimaneutralität als Ziel verwerfen: WOM 24.
- Schiene vor Straße: WOM 28.
- Ökologische Landwirtschaft: WOM 18.
- CO₂-Preis: [§ 10 BEHG](https://www.gesetze-im-internet.de/behg/__10.html), Festpreise ab 2021, Versteigerung ab 2026.
- Kohleausstieg: [§ 4 KVBG](https://www.gesetze-im-internet.de/kvbg/__4.html), Zieldatum spätestens 31.12.2038.
- Klimaschutz gegen Wachstum: G25 q48.

**b) Reichweite.** Drei Instrumente aus 2016/17: fossile Abgaben, Förderung erneuerbarer Energien, Verkaufsverbot ineffizienter Haushaltsgeräte. **Nicht erfasst:** Energieträger (Kernkraft, Kohle, Gas), Gebäude und Heizung, Verkehr, Klimaziele, Landwirtschaft.

**c) Originalfragen**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut, Hinweis |
|---|---|---|---|---|
| **Energieträger (lokal)** | E8 | D4–D10 `elgcoal`, `elgngas`, `elghydr`, `elgnuc`, `elgsun`, `elgwind`, `elgbio` | S. 27–28; Liste 35 = Listenheft S. 36 | „Wie viel des Stroms, der in Deutschland verbraucht wird, sollte aus Kohle erzeugt werden?“ / „… aus Atomkraft bzw. Kernkraft erzeugt werden?“ usw. 1 = eine sehr große Menge … 5 = überhaupt nichts; 55 = noch nie von dieser Energiequelle gehört (spontan); an alle. Stand 2016/17, vor dem Atomausstieg 2023 und vor dem KVBG. |
| Tempolimit | G25 | q27m | S. 159 | „Auf allen Autobahnen sollte ein Tempolimit gelten.“ |
| Fossile Abgaben 2025 | G25 | q27h | S. 144 | „Zur Bekämpfung des Klimawandels sollten die Abgaben auf fossile Brennstoffe wie Öl, Gas und Kohle erhöht werden.“ Gleicher Gegenstand wie `inctxff`, anderes Format; kein Ersatz für Vergleichswerte. |
| Klima gegen Wachstum | G25 | q48 | S. 116 | 1–11; die Einleitung steht in der Parteieinstufung q47 (S. 114). Eine selbsterklärende Fassung bietet R25 pos046 (S. 285). |
| Zahlungsbereitschaft, Instrumentwahl | I20 | F11, F14a/b | S. 9–10 | Akzeptanz höherer Preise/Steuern; Geldstrafen, Steuervergünstigung oder Information. Stand 2021. |
| Versorgungssorgen (lokal) | E8 | D11–D18 | S. 28–30 | Sorgen, keine Präferenzen; nicht als Politik interpretieren. |

**d) Bewertung: teilweise abgedeckt.** Energieträger lassen sich mit lokalen ESS8-Daten erschließen; bisher sind sie nicht genutzt. Gebäude und Heizung, Klimaziele, Schiene vor Straße und Landwirtschaft sind eine **Datenlücke**: in keinem geöffneten Instrument als Bevölkerungsfrage gefunden.

Erlaubte Interpretation: sieben Strommix-Einzelangaben als Profil getrennter Präferenzen, **kein** Summenindex. Kernkraftpräferenz von 2016/17 nicht als heutige Ausstiegsbewertung deuten.

**e) Empfehlung**
1. E8 D7 (`elgnuc`) und D4 (`elgcoal`), sofort lokal. Alle sieben nur gemeinsam mit der vollständigen Einleitung und Liste 35.
2. G25 q27m (Tempolimit).
3. G25 q48 nur mit Einleitung.
4. Gebäude, Heizung und Klimaziele bleiben als Entwicklungsbedarf offen; keine eigenen Fragen formulieren.

### 4.7 Migration

**a) Streitfragen**
- Zurückweisung Asylsuchender an den Grenzen: WOM 5; P30 DI; PB25 V22 (S. 178, Stand 21.05.2025).
- Dauerhafte Grenzkontrollen: P30 DG; PB25 V22A (S. 52).
- Abschiebungsgewahrsam: P30 DH.
- Arbeitserlaubnis für Asylsuchende: WOM 23; ESS12 D15 (künftig).
- Anwerbung von Fachkräften: WOM 11.
- Doppelte Staatsbürgerschaft: WOM 35. Rechtslage: [§ 10 StAG](https://www.gesetze-im-internet.de/stag/__10.html) mit Einbürgerung nach fünf Jahren rechtmäßigen Aufenthalts; §§ 12 und 25 StAG sind „(weggefallen)“. Dass Mehrstaatigkeit damit generell hingenommen wird, ist meine Vermutung aus diesen Fundstellen; ich habe es nicht weiter geprüft.
- Familiennachzug: [§ 104 Abs. 14 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__104.html). Familiennachzug zu subsidiär Schutzberechtigten wird „bis zum Ablauf des 23. Juli 2027 … nicht gewährt“.
- Kulturelle Anpassung: G25 q27a.

**b) Reichweite.** Allgemeine Zulassung nach Herkunftsgruppen (ESS10-SC) und Zeitpunkt gleicher Sozialrechte (ESS8). **Nicht erfasst:** Asylverfahren und Schutz, Grenze, Rückführung, Integrationsanforderungen, Staatsangehörigkeit, Familiennachzug.

**c) Originalfragen**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut, Hinweis |
|---|---|---|---|---|
| **Asylprüfung (lokal)** | E8 | C42 `gvrfgap` | S. 25; Liste 31 = Listenheft S. 32 | Einleitung: „Es gibt Menschen, die nach Deutschland kommen und Asyl beantragen, weil sie in ihrem eigenen Land Angst vor Verfolgung haben.“ Item: „Bei der Prüfung von Asylanträgen sollte der Staat großzügig sein.“ Liste 31 hat fünf Stufen (Stimme stark zu … Lehne stark ab); **der Fragebogen druckt fälschlich die Codes 0–5**. |
| **Familiennachzug (lokal)** | E8 | C44 `rfgbfml` | S. 25 | „Asylbewerber, deren Anträge bewilligt wurden, sollten das Recht haben, ihre engen Familienangehörigen nach Deutschland zu holen.“ Breiter als der heutige Streitpunkt (subsidiär Schutzberechtigte). |
| Weitere Asylaussagen | E8 | C45–C48 | S. 26 | Nur im deutschen Fragebogen (Label „QFIMWSK“), nicht in der ESS8-Quelle C1–C44. **Vermutung:** länderspezifisch, nicht im Integrated File. Ohne Prüfung der Datei nicht verwenden. |
| Zuzug nach Gruppen inkl. Flüchtlinge und Familiennachzug | A21 | F016A_1–7 (`mi05`–`mi11`) | CAWI-Doku S. 14–18 | „Wie ist es mit Flüchtlingen aus Ländern, in denen Krieg herrscht? Der Zuzug … soll UNEINGESCHRÄNKT möglich sein / soll BEGRENZT werden / soll völlig UNTERBUNDEN werden“; außerdem politisch Verfolgte, wirtschaftliche Not, EU- und Nicht-EU-Arbeitnehmer, Ehepartner und Kinder. Split B zeigt „Weiß nicht“. In A23 als F015 (Kategorie C). |
| Kriterien der Einbürgerung | A23 | MAIL A F24 | S. 12 | Neun Kriterien, darunter Sprache, Aufenthaltsdauer, Lebensunterhalt, Straffreiheit, Bekenntnis zur freiheitlichen demokratischen Grundordnung; 1–7. **Kategorie C.** |
| Grenze, Rückführung | P30 | `kp30_2880dg`/`dh`/`di` | S. 61 | „An den deutschen Außengrenzen sollten dauerhaft Grenzkontrollen stattfinden.“ / „Ausreisepflichtige Personen sollten bis zu ihrer Abschiebung oder Ausreise in Gewahrsam genommen werden.“ / „Flüchtlinge, die aus einem sicheren Drittstaat kommen, sollten an der deutschen Grenze zurückgewiesen werden.“ **Quotenstichprobe.** |
| Integration | G25 | q27a | S. 147 | „Einwanderinnen/Einwanderer sollten verpflichtet werden, sich der deutschen Kultur anzupassen.“ |
| Zuzug allgemein 2025 | G25 | q43 | S. 112 | 1 = „Zuzug von Ausländern erleichtern“ … 11 = „… einschränken“. `abdeckung-v2.md` schreibt „erschweren“; der Originalendpunkt lautet „einschränken“. |
| Anzahl, Kultur 2023 | I23 | F9, F10 | S. 7 | „heutzutage“. |
| Neuere Zulassungsfragen (lokal) | E11 | B40–B42 | S. 15 | wie 2.1 |

**d) Bewertung: teilweise abgedeckt.**
- Asyl und Familiennachzug lassen sich lokal aus E8 historisch (2016/17) erschließen. Grenze und Rückführung gibt es nur aus der Quotenstichprobe P30, das ist eine Lücke in den Wahrscheinlichkeitsstichproben.
- Staatsangehörigkeit gibt es nur in A23 (Kategorie C).
- Erlaubte Interpretation: Einzelangaben; keine Gesamtposition „Migration“.
- Wahrgenommene Folgen (B43–B45, q125c–e) sind andere Gegenstände.
- ALLBUS F20 („Ausländer … zurückschicken“, „politische Betätigung untersagen“) schließe ich bewusst aus. Sie sind Teil einer Vorurteilsbatterie, keine Politikstreitfrage im WOM-Sinn, und führen leicht zu Personenetiketten.

**e) Empfehlung**
1. E8 C42 und C44, sofort lokal.
2. A21 F016A_1, _2 und _7 (Flüchtlinge aus Kriegsländern, politisch Verfolgte, Familiennachzug), Kategorie A. Split und Darstellung von „Weiß nicht“ festlegen.
3. G25 q27a.
4. Grenze und Rückführung (P30) nur als Panelreferenz ohne Bevölkerungsanspruch.
5. Staatsangehörigkeit: A23 F24 nur nach Genehmigung, sonst bleibt sie offen.
6. ESS12-Modul D ab 2027 prüfen.

### 4.8 Gleichstellung, Familie und vielfältige Lebensformen

**a) Streitfragen**
- Frauenquote in Vorständen börsennotierter Unternehmen abschaffen: WOM 17.
- Schwangerschaftsabbruch nur nach Beratung straffrei: WOM 26.
- Parität im Parlament: ESS11 E19; G25 q152.
- Gendergerechte Sprache: G25 q27b.
- Ob Gleichstellungsmaßnahmen „heute schon viel zu weit“ gehen: G25 q27g.
- Elternzeit und Kinderbetreuung: E11 E20; I22.
- Rechte gleichgeschlechtlicher Paare. Rechtslage: [§ 1353 BGB](https://www.gesetze-im-internet.de/bgb/__1353.html): „Die Ehe wird von zwei Personen verschiedenen oder gleichen Geschlechts auf Lebenszeit geschlossen.“ [§ 1741 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__1741.html): „Ein Ehepaar kann ein Kind nur gemeinschaftlich annehmen.“ Eingeführt mit [BGBl. I 2017 S. 2787](https://dejure.org/BGBl/2017/BGBl._I_S._2787) vom 20.07.2017. Ehen seit 1.10. laut [Haufe-Überschrift](https://www.haufe.de/recht/familien-erbrecht/eherecht-der-dammbruch-die-ehe-fuer-alle_220_417480.html); das Inkrafttretensdatum habe ich nicht im Gesetzestext geprüft.
- Selbstbestimmungsgesetz und Abstammungsrecht habe ich nicht geprüft.

**b) Reichweite.** Vier konkrete Gleichstellungseingriffe (ESS11, 2023) und familienpolitische Leistungen (ESS8). **Nicht erfasst:** reproduktive Selbstbestimmung, Rechte gleichgeschlechtlicher Paare und vielfältiger Lebensformen, Frauenquote in der Wirtschaft, Sprache.

**c) Originalfragen**

| Lücke | Quelle | Frage | Fundstelle | Wortlaut, Hinweis |
|---|---|---|---|---|
| **Adoption durch gleichgeschlechtliche Paare (lokal)** | E10SC A49; E11 B36; auch E9 B36, E8 B36 | `hmsacld` | E10 S. 6; E11 S. 13 | „Schwule und lesbische Paare sollten die gleichen Rechte haben, Kinder zu adoptieren, wie Paare, die aus Mann und Frau bestehen.“ 1–5. **ESS8 (2016/17) liegt vor der Eheöffnung, ESS9 bis ESS11 danach.** Die Frage hat ihren Bezug zur Rechtslage verändert. Laut `abdeckung-v2.md` sind die ESS11-Antworten bereits bekannt. ESS10-SC ist die lokale Alternative; ob sie unberührt ist, habe ich nicht geprüft, weil ich den Zugriffsbericht nicht gelesen habe. |
| Allgemeine Akzeptanz (lokal) | E10SC A47; E11 B34 | `freehms` | wie oben | „Schwule und Lesben sollten ihr Leben so führen dürfen, wie sie es wollen.“ Allgemeine Norm, keine konkrete Maßnahme. `hmsfmlsh` (persönliche Scham) ist keine Politikfrage, daher bewusst ausgeschlossen. |
| **Schwangerschaftsabbruch** | A21 | F032_1–8 (`vm08`–`vm15`) | CAWI-Doku S. 37–42 | „Eine Frau möchte einen Schwangerschaftsabbruch vornehmen lassen. Sollte dies IHRER MEINUNG NACH in jeder Phase der Schwangerschaft, nur in den ersten drei Schwangerschaftsmonaten oder gar nicht gesetzlich möglich sein?“ Acht Bedingungen, z. B. „… wenn die Frau es so will, unabhängig davon, welchen Grund sie dafür hat?“ (F032_8). Split B mit „Weiß nicht“. Kategorie A, Feldzeit 2021. |
| Schwangerschaftsabbruch als Verbotsfrage | A21 | F050_C (`ca16`) | S. 66 | „Eine Frau lässt einen Schwangerschaftsabbruch vornehmen, weil sie keine Kinder haben möchte.“ → gesetzlich verboten / nicht verboten. Reihenfolge randomisiert. |
| Gleichgeschlechtliche Elternschaft | I22 | F34 Items 3/4 | S. 15 | „Ein Paar, bei dem beide Frauen sind, kann ein Kind genauso gut großziehen wie ein Mann und eine Frau.“ Einstellung, keine Rechtsfrage. Stand 2023. |
| Sprache, Maßnahmen | G25 | q27b, q27g | S. 147, 144 | q27b bewertet die Sinnhaftigkeit gendergerechter Sprache; q27g mit „heute schon“. Nur wörtlich interpretieren. |
| Elternzeit, Kinderbetreuung | I22 | F37/F38, F40/F41 | S. 16–17 | Monate bezahlter Elternzeit, Aufteilung, Anbieter und Kostenträger der Betreuung. |

**d) Bewertung: teilweise abgedeckt.**
- Vielfältige Lebensformen: Der ESS hat sie lokal. Ihr Fehlen in den 43 Fragen ist eine **inhaltliche Auswahlentscheidung**, die zu begründen oder zu korrigieren ist.
- Reproduktive Selbstbestimmung ist im ESS eine **Datenlücke**; ALLBUS 2021 schließt sie.
- Frauenquote in der Wirtschaft: in keinem geöffneten Instrument gefunden.
- Erlaubte Interpretation: Einzelangaben. Die acht Abtreibungsbedingungen sind ein Bedingungsprofil, kein Index.

**e) Empfehlung**
1. `hmsacld` (ESS10-SC oder ESS11), sofort lokal, mit Rechtsstandshinweis.
2. A21 F032_8 und eine Auswahl weiterer Bedingungen, oder F050_C. Kategorie A.
3. G25 q27b, mit genauer Beschreibung des Gegenstands.
4. ESS11 E23–E25 (Einschätzungen über Frauen) sind keine Politikfragen und bleiben bewusst draußen.

---

## 5. Priorisierte Gesamtempfehlung

### 5.1 Sofort mit den lokalen ESS-Ausgaben auswertbar

Alle Fragen stehen in den lokal vorhandenen Integrated Files. Einen Abgleich der Variablen gegen die Datei-Header habe ich wegen des Leseverbots für `data/raw/` nicht gemacht. Vor der Nutzung braucht es eine Code- und Header-Bindung.

| Prio | Bereich | Variablen | Datei | Hinweis |
|---|---|---|---|---|
| 1 | Klima/Energie | `elgcoal`, `elgngas`, `elghydr`, `elgnuc`, `elgsun`, `elgwind`, `elgbio` | ESS8e02_3 | Stand 2016/17; Code 55 eigene Kategorie; ESS8-SDDF fehlt lokal, betrifft nur Standardfehler |
| 1 | Migration | `gvrfgap`, `rfgbfml` | ESS8e02_3 | fünfstufig laut Liste 31 |
| 1 | Gleichstellung/Lebensformen | `hmsacld` (optional `freehms`) | ESS10SCe03_2 oder ESS11e04_2 | Eheöffnung 2017; Vorkenntnis der ESS11-Antworten beachten |
| 2 | EU | `eusclbf` | ESS8e02_3 | Definition auf Liste 55 vollständig zeigen |
| 2 | Sozialstaat | Vignette Gruppe 1 `ubpay`, `ubedu`, `ubunp` | ESS8e02_3 | Zweig-Nenner (E20 = 1) |
| 3 | Sozialstaat | `basinc` | ESS8e02_3 | sechs Definitionsmerkmale; „momentan“ |
| 3 | Migration/EU | ESS11-Fassungen von `imsmetn`/`imdfetn`/`impcntr`/`vteurmmb` | ESS11e04_2 | nur wenn Aktualität wichtiger ist als Modusnähe; Vorkenntnis A/B beachten |

### 5.2 Downloads, die Steven tätigen müsste

Alle setzen Anmeldung und Zustimmung zu den GESIS-Bedingungen voraus. Formate: G25 S. 28 nennt Stata-Datensätze in Version 16. R25 S. 28 nennt beiliegende Syntaxdateien, mit denen die fehlenden Werte in Stata und SPSS definiert werden. Die genauen Downloadformate in der GESIS-Suche habe ich nicht eingesehen, weil die Seite per Cloudflare blockiert war.

**Vor jedem Download klären:** GESIS-KI-Klausel (§ 4), Nutzungsart Website, Wortlautrechte.

| Prio | Datei | Archiv, Version, DOI | Zugang | Wofür |
|---|---|---|---|---|
| 1 | GLES Querschnitt 2025 Nachwahl | ZA10100 v4.0.0, 10.4232/5.ZA10100.4.0.0 | A / Safeguarded A | q27a, b, c, k, l, m, n; q27j mit Feldzeitvermerk; q167e/f; q51h |
| 1 | ALLBUS 2021 | ZA5280 v2.1.0, 10.4232/1.14626 | A | F032 (Schwangerschaftsabbruch), F016A (Zuzug, Flüchtlinge, Familiennachzug), F039–F041 |
| 2 | Eurobarometer 104.1 | ZA9130 v1.0.0, 10.4232/1.14793 | 0 | QB1 EU-Politikfelder |
| 2 | ISSP 2016 | ZA6900 v2.0.0, 10.4232/1.13052 (DE-Teil) | A | J011, J013, J014 Überwachung; J002 Protest |
| 2 | ISSP 2019 | ZA7600 v3.0.0, 10.4232/1.14009 | A | F8a Steuerprogression |
| 3 | GLES Panel W34 / W30 | ZA10123 v1.0.0 / ZA10119 v1.0.0 | A | Schuldenbremse 2026, Mindestlohn, Grenze; Quotenstichprobe, nur Panelreferenz |
| 3 | ALLBUS 2023 | ZA8830 v1.2.0, 10.4232/1.14544 | **C** | Einbürgerungskriterien F24; nur mit Genehmigung |
| später | ESS12 | voraussichtlich Januar 2027 | ESS-Bedingungen | Kernfragen 2025/26, Asylmodul |

### 5.3 Nicht empfohlen oder nur als Kontext

- **Parteinamen in Fragen:** G25 q27p, R25 pre034g, P30/P34 DJ, „AfD“.
- **Keine Politikpräferenzen:** Antisemitismus- und Vorurteilsfragen (G25 q27q, P34 CX/CY, ALLBUS F20) sowie ESS11 E23–E25.
- **Todesstrafe:** ALLBUS 2021 F051.
- **Stark zeit- oder regierungsgebundene Politbarometer-Fragen** („Die Bundesregierung plant …“). Gut als Beleg für die Salienz, schlecht als Websitefrage.
- **Wahl-O-Mat-Thesen als Fragen:** keine Bevölkerungsdaten, Rechte nicht geprüft.

---

## 6. Prüfhinweise zu `docs/abdeckung-v2.md` und `docs/empirie-plan-v2.entwurf.md`

1. Klima/Energie: ESS8 D4–D10 (Energieträger) fehlen, obwohl lokal vorhanden. Die Aussage „Energieträgerwahl unvollständig“ ist mit lokalen Daten teilweise behebbar.
2. Migration: Asyl ist mit „E7 D15“ belegt. ESS7-Daten sind aber nicht lokal vorhanden, während ESS8 C42 (`gvrfgap`) und C44 (`rfgbfml`) lokal vorliegen und nicht genannt werden.
3. G25 q43: Der Endpunkt heißt „einschränken“, nicht „erschweren“. G25 q27k lautet „deutlich abgesenkt“; die Matrix spricht von „Bürgergeldkürzung“.
4. G25 q40, q43 und q48: Die erklärende Einleitung steht in der vorangehenden Parteieinstufung (q39 S. 106, q42 S. 110, q47 S. 114). Auf einer Website ohne Parteieinstufung ändert sich der Kontext. R25 enthält selbsterklärende Fassungen für Steuern (pos044, S. 280) und Klima (pos046, S. 285), aber nicht für Zuzug (pos045, S. 283).
5. G25 q27j: Wechsel der Rechtslage während der Feldzeit (BGBl. 2025 I Nr. 94) ist nicht vermerkt.
6. Die Wahl von ESS10-SC statt ESS11 für `imsmetn`/`imdfetn`/`impcntr` und `vteurmmb` ist im Plan nicht begründet. Für ESS10-SC sprechen die Modusnähe (Selbstausfüller) und die sichtbaren Antwortoptionen, für ESS11 die neuere Feldzeit.
7. Gleichstellung: Die Matrix nennt die Homosexualitätsfragen; der 43er-Bestand lässt sie ohne dokumentierte Begründung weg.
8. Rechte: Die GESIS-KI-Klausel (§ 4 der Bedingungen ab 4. Februar 2026) und die Kategorie C für ALLBUS 2023 kommen in den Plänen nicht vor.
9. Bestätigt: Liste 48 von ESS8 hat 0–10, der Fragebogen druckt 0–9. Zusätzlich gefunden: Liste 31 hat fünf Stufen, der Fragebogen druckt die Codes 0–5 (C42–C44).

---

## 7. Offene Punkte und Entscheidungen für Steven

1. **GESIS anfragen:**
   - KI-Ausnahme nach § 4 oder ein Auswertungsweg ohne KI-Verarbeitung der Datenbasis;
   - ob eine öffentliche Website mit dauerhaft angezeigten aggregierten Werten unter „wissenschaftliche Nutzung“ und § 5 fällt;
   - Zustimmung zur Anzeige deutscher Fragetexte (GLES, ALLBUS, ISSP-DE).
2. Für `vteurmmb` und die Zulassungsfragen entscheiden: ESS10-SC (Modusnähe) oder ESS11 (Aktualität).
3. Ob Fragen aus Quotenstichproben (GLES-Panel) als Referenz überhaupt erscheinen sollen.
4. Ob vor ESS12 (Januar 2027) eine erste Fassung erscheinen soll, die viele Fragen aus 2010/11 und 2016/17 enthält.
5. Lücken ohne geprüftes Originalinstrument bleiben Entwicklungsbedarf und dürfen nicht durch eigene Fragen ersetzt werden:
   - Gesichtserkennung, Strafmündigkeit
   - Heizung und Gebäudeenergie, Klimaneutralitätsziel, Schiene vor Straße
   - Frauenquote in der Wirtschaft
   - Volksentscheide als konkrete Bundesreform
   - Staatsangehörigkeit ohne Genehmigung für ALLBUS 2023
6. Ob Deutschland an ESS12 teilnimmt und wie die deutsche Fassung von D16 lautet, ist nach der Veröffentlichung zu prüfen.

---

## 8. Nachweise

### 8.1 Tatsächlich geöffnete Quellen

Alle Zugriffe am 3. Oktober 2026. Uhrzeiten in UTC, ungefähr.

**Lokale Dateien** (18:50–19:35):
- `docs/project.md`, `docs/abdeckung-v2.md`, `docs/empirie-plan-v2.entwurf.md`
- Auftragsdateien unter `reports/claude/auftraege/`
- Deutsche ESS-Fragebögen ESS5–ESS11 und ESS8-Listenheft: `outputs/loop/breadth-data-001/sources/ess{5,6,7,8,9,10,11}-de-questionnaire.pdf`, `ess8-de-showcards.pdf`. SHA-256 u. a.: ESS8 `977475c1…`, ESS10 `158004a8…`, ESS11 `be6fbca3…`.
- ESS-Quellfragebögen ESS8–ESS11 im selben Ordner.
- ESS10-Metadaten `ess10-study-access-metadata.json`
- Codex-API-Projektion `outputs/loop/breadth-catalog-004/allowed-api-projection.json`, nur Variablenlabels
- `outputs/loop/breadth-access-002/gles-rights/facts-v1.md` als Hinweisquelle; Inhalte selbst nachgeprüft
- ISSP-DE-Fragebögen und technische Berichte unter `outputs/loop/breadth-data-001/issp/`: 2016-DE-questionnaire (identisch mit dem Neuabruf, SHA-256 `3f38cfbf…`), 2019, 2020, 2022, 2023-DE-paper-questionnaire, 2019/2020/2023-DE-technical, PNG-Seiten 2020/2023
- GLES-Panel-W30-Dokumentation `glespanel30-questionnaire.pdf` (`6cfa009b…`)

**Online (bzw. heruntergeladen nach `/tmp/r3`), 19:05–19:35:**
- GESIS-Dokumente über `https://access.gesis.org/dbk/<ID>`:
  - 79269 (GLES 2025 Nachwahl, `d6e0a07b…`, identisch mit lokaler Kopie)
  - 79362 (GLES RCS 2025, `7758d457…`)
  - 81063 (GLES Panel W34, `9f67d159…`)
  - 77958, 77960, 77961 (ALLBUS 2023 CAPI `bce63e22…`, MAIL A `4d8eff9f…`, MAIL B)
  - 72851 (ALLBUS 2021 CAWI, `818f3f6c…`)
  - 81730 (Eurobarometer 104.1 DE, `81c26b19…`)
  - 81906 (Politbarometer 2025, `dedf7c47…`)
  - 63842 (ISSP 2016 DE)
  - 79062, 78924, 78961, 78998, 80783 (nur zur Identifikation geöffnet)
  - HEAD-Abfragen der IDs 78900–82600 (nur Dateinamen)
- GESIS-OAI: `https://dbkapps.gesis.org/dbkoai/?verb=GetRecord&identifier=oai:dbk.gesis.org:{DBK|COL}/ZA…&metadataPrefix=oai_ddi25(-de)` für ZA9130, ZA8830, ZA5280, ZA6900, ZA7600, ZA7650, ZA9151, ZA10000, ZA10010, ZA10100, ZA10101, ZA10119, ZA10123, ZA8000
- DataCite-API: `https://api.datacite.org/dois…` (ZA8830, ZA10100, ZA10101, ALLBUS 2021/2024/2025, ISSP 2021/2024, GLES Panel, Eurobarometer, Politbarometer)
- ESS:
  - [Meldung ESS12-Veröffentlichung](https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027)
  - [Meldung ESS12-Fragebogen](https://www.europeansocialsurvey.org/news/article/round-12-questionnaire-and-provisional-release-dates)
  - [Seite Source Questionnaire](https://www.europeansocialsurvey.org/methodology/ess-methodology/source-questionnaire)
  - [ESS12-Quellfragebogen](https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf)
  - [Disclaimer](https://www.europeansocialsurvey.org/contact/disclaimer) (`8e0ded72…`)
  - Länderseite Deutschland (ohne Ergebnis)
  - ESS-API `https://api.nsd.no/graphql`, POST mit dem von Codex gespeicherten Anfragekörper, für die DE-Feldzeiten
  - 404-Prüfungen der ESS12-DE-Pfade
- GESIS-Bedingungen und -Impressum über Wayback (siehe 3.2). Direkte Abrufe von `www.gesis.org` und `search.gesis.org`: HTTP 403.
- bpb: [Wahl-O-Mat-Definitionsdatei](https://www.wahl-o-mat.de/bundestagswahl2025/app/definitionen/module_definition.js), [Pressemitteilung 06.02.2025](https://www.bpb.de/die-bpb/presse/pressemitteilungen/559069/wahl-o-mat-zur-bundestagswahl-2025-geht-online/)
- Recht:
  - [BGBl. 2025 I Nr. 94](https://www.recht.bund.de/bgbl/1/2025/94/regelungstext.pdf) (`787a6aa6…`)
  - gesetze-im-internet.de: § 1353 und § 1741 BGB, § 7 AtG, § 4 KVBG, § 10 BEHG, § 71 GEG/GModG, §§ 10, 12, 25 StAG, § 104 AufenthG
  - [dejure BGBl. I 2017 S. 2787](https://dejure.org/BGBl/2017/BGBl._I_S._2787)
  - [Haufe zur Eheöffnung](https://www.haufe.de/recht/familien-erbrecht/eherecht-der-dammbruch-die-ehe-fuer-alle_220_417480.html)
- Erfolglos: congress.gov (403), Abruf von BGBl. 2024 I Nr. 439 (HTML statt PDF). Daraus habe ich nichts übernommen.

### 8.2 Ausgeführte Befehle (Kurzform)

- `pdftotext -layout` bzw. ohne `-layout` auf allen genannten PDFs
- Ein eigenes Python-Skript zur seitengenauen Suche (`/tmp/r3/find.py`)
- `pdftoppm` und Bildansicht für ESS10-SC S. 2, 10–13, ESS8 S. 25 und ISSP-Berichtsseiten
- `curl` für GESIS-Dokumente, -OAI und -HEAD-Scans, DataCite, ESS-API (POST), bpb, recht.bund.de, gesetze-im-internet.de, Wayback
- `sha256sum`
- WebSearch und WebFetch für ESS-Meldungen und die bpb-Pressemitteilung
- Gelöscht ohne Öffnen: ALLBUS-2023-Variable-Report (Dokument 78534) und ISSP-Kumulations-Variable-Report (77968)

Keine Git-Befehle mit Schreibwirkung, keine Anmeldung, keine Downloads mit Zustimmung zu Bedingungen.

### 8.3 Grenzen der Prüfung

- **Politikwissenschaftliche Fachliteratur** zu deutschen Streitfragen 2021–2026 habe ich nicht im Volltext geöffnet. Streitfragen sind über Wahl-O-Mat-Thesen, Studiendokumentationen und Rechtsquellen belegt. Parteipositionen und Wahlprogramme habe ich nicht geprüft.
- **Rechtliche Würdigung:** Die Rechtefragen sind Quellenfeststellungen, keine Rechtsberatung. GESIS-Rechtsseiten konnte ich nur als Wayback-Schnappschuss lesen (30.03.2026 bzw. 09.09.2026). Spätere Änderungen sind möglich. Sikt- und ESS-Downloadbedingungen sowie die Rechte an Eurobarometer- und Politbarometer-Wortlauten habe ich nicht geprüft.
- **Datei-Header** der lokalen ESS-Rohdaten habe ich nicht eingesehen. Ob die vorgeschlagenen ESS8-Variablen (insbesondere C45–C48) im Integrated File stehen, ist nicht bestätigt.
- **ESS10-SC:** Nur die Papierfassung habe ich wörtlich verglichen, nicht die Web-Bildschirme. Die Variablennamen für ESS10 A1–A5 und A51–A53 sowie ESS11 B38/B39 habe ich nicht geprüft.
- **Feldzeit und Population von ISSP 2016 und 2019:** nur teilweise geprüft (siehe 3.1). Die ALLBUS-2021-Split-Zuordnung (A, B, C) habe ich nicht weiter dokumentiert.
- Ob GESIS 2025/26 weitere Querschnitte, etwa ALLBUS 2025, veröffentlicht hat, habe ich nur über DataCite-Titelsuche geprüft.
- **Neutralität:** Keine Aussage dieses Berichts ist ein Neutralitäts- oder Validitätsnachweis. Übereinstimmung mit Codex-Berichten gilt nicht als Bestätigung.

### 8.4 Modell

Laut Laufzeitumgebung: Claude Opus 5.5, Modell-ID `claude-opus-5-5[1m]`, als Subagent in Claude Code.
