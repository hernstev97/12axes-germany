# R2: Themenrecherche Gesundheit und Pflege, Arbeit und Rente, Wohnen

Stand: 3. Oktober 2026, ca. 19:00–19:45 UTC. Getrennter Claude-Subagent mit begrenztem Auftrag (`reports/claude/auftraege/R2-themen-gesundheit-arbeit-wohnen.vollstaendig.md`). Ausgangsstand des Repositorys: `e9898fb`. Geschrieben wurde ausschließlich diese Datei.

Diese Recherche ist ergebnisblind angelegt. Ich habe keine Antwortverteilungen, Prozentwerte, Mittelwerte oder Parteiergebnisse aus Befragungen recherchiert oder verwendet. Ungefragt eingeblendete Ergebnisausschnitte sind in Abschnitt 10.2 vermerkt. Gesperrte Pfade (`data/raw/`, `data/local/`, `data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`) habe ich nicht geöffnet.

Ein Themenfeld ist hier keine nachgewiesene Messdimension. Literaturplausibilität ersetzt keine Validierung.

---

## 0. Kurzfazit

1. **Mit dem aktuellen 43-Fragen-Bestand sind alle drei Bereiche nicht angemessen erfasst.** Gesundheit/Pflege ist mit 0 Fragen vertreten und Wohnen ebenfalls mit 0. Rente kommt nur über eine allgemeine Verantwortungsfrage vor (ESS8 `gvslvol`). Arbeit erscheint nur über Arbeitslosenabsicherung und Aktivierung (`gvslvue`, `eduunmp`) sowie zwei Gleichstellungsfragen (`eqparlv`, `fineqpy`). Zu Mindestlohn, Arbeitszeit, Tarifbindung/Streikrecht, Rentenniveau, Renteneintrittsalter und Rentenfinanzierung enthält er keine Frage.
2. **Die lokal vorhandenen ESS-Ausgaben tragen diese Bereiche praktisch nicht.** Sofort auswertbar und thematisch nah sind nur die fünf Pandemie-Abwägungsfragen aus ESS10-SC (`panpriph`, `panmonpb`, `panfolru`, `panclobo`, `panresmo`; DE 2021/22). Sie gehören primär zu Bürgerrechten/Eingriffsbefugnissen und sind historisch. ESS8 hat 2016 die Verantwortungsfrage für Gesundheitsversorgung (`gvhlthc`) **nicht** wiederholt; sie existiert nur in ESS4 (2008/09, nicht lokal). ESS9 `iagrtr` ist eine Altersnorm und keine Präferenz zur Rentenpolitik.
3. **Tragfähige Originalfragen liegen fast nur bei GESIS.** Für Gesundheit sind das ISSP 2021 (ZA8000, deutsche Feldphase 2021, postalisch) mit F3, F4b, F5, F6a/b sowie ISSP 2016 J006/J007/J008. Für Wohnen sind es GLES 2025 Nachwahl `q27i` und ISSP 2016 J007b-I, für die Impfpflicht als historischen Konflikt GLES 2021 `q27j`. Für Altenhilfe/Pflege kommen ISSP 2022 F42/F43 hinzu, für Arbeitszeit ISSP 2016 J005F (Rahmung von 2016).
4. **Für zentrale aktuelle Streitfragen habe ich in den geprüften Instrumenten keine Bevölkerungs-Originalfrage gefunden.** Das betrifft Bürgerversicherung/duales System, Pflegevollversicherung/Eigenanteile, Krankenhausreform, Rentenniveau-Haltelinie, Regelaltersgrenze, Mindestlohnhöhe, Tariftreue/Streikrecht, Grundsteuer-Umlage, sozialen Wohnungsbau und Vergesellschaftung. Politbarometer 2024/2025 enthält laut Archiv-Metadaten Rentenfragen. Den Wortlaut habe ich nicht eingesehen.
5. **Zugang und Rechte sind der Engpass.** Die GESIS-Nutzungsbedingungen (gültig ab 04.02.2026) verbieten grundsätzlich die Verarbeitung bereitgestellter Daten mit KI-Systemen und erlauben Ausnahmen nur auf Anfrage. Sie binden die Nutzung an „zeitlich befristete“ wissenschaftliche Vorhaben. Das bestätigt einen bereits in `reports/loop/authors/BREADTH-ACCESS-002.md` dokumentierten Befund. Eine Freigabe zur Anzeige deutscher GESIS-Fragewortlaute auf einer Website habe ich nicht gefunden. ESS-Dokumentation steht dagegen unter CC BY-SA 4.0, ESS-Daten unter CC BY-NC-SA 4.0.
6. **Empfehlung:** Gesundheit/Pflege und Wohnen sollten als ausgewiesene Binnenfacetten mit eigener Primärzuordnung ergänzt werden. Rente gehört mit konkreteren Fragen in den Sozialstaat, Arbeitsmarktordnung in die Wirtschaftsrubrik. Eine eigene Messdimension folgt daraus nicht. Voraussetzung ist eine Klärung mit GESIS (KI-Ausnahme, Websitenutzung, Fragetextrechte). Ohne diese Klärung bleiben die Bereiche offen ausgewiesene Lücken.

---

## 1. Vorgehen

- Gelesen habe ich `docs/project.md`, `docs/abdeckung-v2.md` und `docs/empirie-plan-v2.entwurf.md` (Abschnitt „Konkrete Auswahl“) sowie die Auftragsdateien. `docs/handbuch.md` war nicht nötig, weil ich keine UI und keine sichtbaren Texte bearbeite.
- Lokale deutsche Fragebögen habe ich seitenweise mit `pdftotext -layout` extrahiert und mit Seitenangabe durchsucht: ESS5, ESS8 (mit Antwortlisten), ESS9, ESS10, ESS11, ISSP 2016/2019/2022/2023 (DE) sowie GLES 2025 Nachwahl, GLES 2021 Nach- und Vorwahl und GLES-Panel Welle 30.
- Neu geöffnet habe ich: ISSP 2021 DE (Fragebogen und Hintergrunddokumentation, GESIS-DBK), die ISSP-2021-Variablenübersicht, ALLBUS 2021 (CAWI, Selbstausfüller Split A) und ALLBUS 2023 (CAPI, MAIL A, MAIL B). Aus dem ALLBUS-2023-Variable-Report habe ich nur die Methodenseiten gelesen (Abschnitt 10.2). Hinzu kamen der ESS4-Source-Fragebogen, DataCite-Metadaten (Versionen, DOIs, Themenlisten), die Wahl-O-Mat-2025-Definitionsdatei, sieben Wahlprogramme 2025, der Koalitionsvertrag 2025, amtliche und fachliche Quellen (Abschnitt 10.1) sowie die GESIS-Nutzungsbedingungen und das GESIS-Impressum (über Wayback-Schnappschüsse, weil gesis.org direkt mit HTTP 403 antwortete).
- **Seitenangaben** sind physische, 1-basierte PDF-Seiten, sofern nicht anders vermerkt. Wahlprogramm-Seiten sind ebenfalls PDF-Seiten; die gedruckten Seitenzahlen weichen teils ab.
- Wahl-O-Mat-Thesen dienen nur als Beleg dafür, dass eine Streitfrage 2025 zur Wahl stand. Wahlprogramme belegen nur „Partei X fordert Y“. Ich werte keine Position.

---

## 2. Studienreferenzen (nur geprüfte Angaben)

| Kürzel | Studie, Archivnr., Version, DOI | Deutschland: Feldzeit, Population, Modus | Beleg / Grenze |
|---|---|---|---|
| E8 | ESS8, Edition 2.3 (lokal) | 23.08.2016–26.03.2017; ab 15 J. in Privathaushalten, unabhängig von der Staatsangehörigkeit; CAPI | Feldzeiten aus lokaler ESS-Portal-Metadatei `ess-public-de-metadata-post.json`; Population: ESS-Universum laut `ess10-study-access-metadata.json`. SDDF für ESS8 fehlt lokal. |
| E9 | ESS9, Edition 3.3 (lokal) | 29.08.2018–04.03.2019; wie E8; CAPI | wie oben |
| E10 | ESS10 Self-completion, Edition 3.2, DOI 10.21338/ess10sce03_2 (lokal) | 05.10.2021–04.01.2022; wie E8 (unter 18 J. mit Elternerlaubnis, Fragebogen PDF S. 2); Papier/Web | Portal-Zitation nennt teils noch 3.1 (lokale Metadatei) |
| E11 | ESS11, Edition 4.2 (lokal) | 09.05.–21.12.2023; CAPI | ausgewählte A/B-Antworten projektintern bereits bekannt |
| E4 | ESS4 (nicht lokal) | 27.08.2008–31.01.2009 (Portal-Metadaten) | nur englischer Source-Fragebogen geprüft; deutscher Wortlaut nicht eingesehen |
| G25 | GLES Querschnitt 2025 Nachwahl, ZA10100, v4.0.0, DOI 10.4232/5.ZA10100.4.0.0 | CAWI 24.02.–14.04.2025, Papier 24.02.–23.04.2025; deutsche Staatsangehörige ab 16 mit Hauptwohnsitz; selbstausgefüllt | Doku v1.3 (12.08.2026), PDF S. 6, 11; Datenzugang S. 7 |
| G21n | GLES Querschnitt 2021 Nachwahl, ZA7701, v2.1.0, DOI 10.4232/1.14169 | 27.09.–21.11.2021; deutsche Staatsangehörige ab 16; CAWI/PAPI | Doku v1.2, PDF S. 5, 9, 10. Neuere Versionen nicht ausgeschlossen (DataCite zeigt 2.1.0 als neueste gefundene). |
| G21v | GLES Querschnitt 2021 Vorwahl, ZA7700, v3.1.0, DOI 10.4232/1.14168 | 26.08.–25.09.2021; wie G21n | Doku v2.2, PDF S. 5 |
| RCS25 | GLES Rolling Cross-Section 2025, ZA10101 (DataCite: v3.0.0) | nicht geprüft | Fragebogen **nicht selbst geöffnet** (gesis.org 403, kein Archivschnappschuss); bekannt nur aus lokalem Codex-Auszug `outputs/loop/theory/GLES-RCS-2025.web-extract.json` |
| I16 | ISSP 2016 Role of Government V, ZA6900, v2.0.0, DOI 10.4232/1.13052 | als CASI-Selbstausfüllteil zusammen mit ALLBUS 2016 (Fragebogen PDF S. 3, 20, 22; Hintergrunddoku „CASI“) | Feldzeit 05.04.–18.09.2016 und Population 18+ laut Codex-Hilfsbericht `outputs/loop/breadth-data-001/issp/report-v1.md`, **von mir nicht im Original verifiziert** |
| I19 | ISSP 2019 Social Inequality V, ZA7600, v3.0.0, DOI 10.4232/1.14009 | 30.07.–30.09.2020, postalisch (nationaler Technikbericht M4) | Population laut Codex-Bericht 18+; nicht selbst geprüft |
| I21 | ISSP 2021 Health and Health Care II, ZA8000, v2.0.0, DOI 10.4232/5.ZA8000.2.0.0 | 2021 (Fragebogen „. . 2021“); „mail survey“ (Hintergrunddoku S. 3, 58) | **Exakte Feldzeit und Population nicht im Original verifiziert.** Eine Suchmaschinen-Zusammenfassung nannte Juni–August 2021 (ungeprüft). |
| I22 | ISSP 2022 Family V, ZA10000, v2.0.0, DOI 10.4232/5.ZA10000.2.0.0 | 17.05.–01.08.2023, postalisch, gemeinsamer Bogen mit ISSP 2023 (Technikbericht M4) | getrennte Archivdateien |
| A21 | ALLBUS 2021, ZA5280, v2.1.0, DOI 10.4232/1.14626 | 2021-06 bis 2021-08 (DataCite „Collected“); Personen in Privathaushalten, vor 01.01.2003 geboren (Deutsche und Ausländer); MAIL/CAWI | Fragebogendokumentation CAWI (2. Aufl.) und Split A geprüft |
| A23 | ALLBUS 2023, ZA8830, v1.2.0, DOI 10.4232/1.14544 | April–September 2023; Privathaushalte, vor 01.01.2005 geboren; CAPI sowie MAIL/CAWI (Designexperiment) | Variable Report S. 6, 53, 55 (nur Methodenseiten gelesen) |
| PB | Politbarometer 2021 ZA7856 v1.1.0 (10.4232/1.14464); 2022 ZA7970 v1.0.0 (10.4232/1.14103); 2023 ZA8785 v1.0.1 (10.4232/1.14405); 2024 ZA8974 v1.0.0 (10.4232/1.14517); 2025 ZA9151 v1.0.0 (10.4232/1.14794) | Wahlberechtigte; CATI, 2025 zusätzlich CAWI-Mobilfunkteilstichprobe (DataCite-Methodentext 2025) | **nur DataCite-Metadaten**; Wortlaute nicht eingesehen |

ESS12 ist laut ESS-Meldung vom 30.09.2026 noch nicht veröffentlicht: „expected to be published for the first time in January 2027“. Die Module sind laut ESS-Meldung vom 04.01.2023 Immigration und Wellbeing, also keine meiner Bereiche.

---

## 3. Bereich A: Gesundheit und Pflege

### 3.1 Streitfragen 2021–2026 (Belege, keine Wertung)

| Nr. | Streitfrage | Beleg „stand zur Wahl“ / Kontext | vertretene Positionen (Wahlprogramme 2025, PDF-Seite) |
|---|---|---|---|
| G1 | Ein gemeinsames Versicherungssystem („Bürgerversicherung“) oder Fortbestand von GKV und PKV | Wahl-O-Mat 2025, These 16: „Alle Bürgerinnen und Bürger sollen in gesetzlichen Krankenkassen versichert sein müssen.“ Institutioneller Hintergrund: European Observatory, *Germany: Health System Summary 2024*, S. 3 (Versicherung über SHI oder substitutive PHI) | Für ein gemeinsames bzw. solidarisch ausgeglichenes System: SPD S. 28–29, Grüne S. 93, BSW S. 3, Linke S. 18 („solidarische Gesundheits- und Pflegeversicherung“, Wegfall der Beitragsbemessungsgrenze). Für das duale System: CDU/CSU S. 69 („zur Dualität von gesetzlicher und privater Krankenversicherung“), FDP S. 33 („lehnen wir eine Einheitskasse (sog. Bürgersversicherung) ab“). AfD: In den geprüften Gesundheitspassagen (S. 22–23) keine ausdrückliche Aussage zur Bürgerversicherung. |
| G2 | Finanzierung der GKV, Leistungsumfang, Zuzahlungen, Patientensteuerung | Koalitionsvertrag 2025, Z. 3379–3384 („verbindliches Primärarztsystem“); Health System Summary 2024, S. 15 (Deckelung von Zuzahlungen) | Steuerfinanzierung versicherungsfremder Leistungen bzw. Bürgergeld-Beiträge: Grüne S. 93, AfD S. 22. Weitere Einkommensarten verbeitragen: Grüne S. 94, Linke S. 18. Ausgabenbremse und Überprüfung von Leistungsausweitungen: FDP S. 33. Effizienz und Kassenwettbewerb: CDU/CSU S. 70. Zahnersatz und Sehhilfen zurück in den Leistungskatalog: BSW S. 27. Primärarztsystem: FDP S. 33, ähnlich CDU/CSU S. 70 („stärkere Steuerungsfunktion“). |
| G3 | Pflegeversicherung als Teilleistung oder Vollversicherung; Begrenzung der Eigenanteile | WD des Bundestages, WD 9-3000-035/19, S. 4 (SPV als „Teilleistungssystem“, Debatte über Vollversicherung); Koalitionsvertrag Z. 3466–3471 („große Pflegereform“); Health System Summary 2024, S. 12 (Pflegeunterstützungs- und -entlastungsgesetz vom 26.05.2023) | Deckel bzw. Vollversicherung: SPD S. 31 (Begrenzung der Eigenanteile, Einbeziehung der privaten Pflegeversicherung in den Risikostrukturausgleich), BSW S. 27 („Pflegevollversicherung, die überwiegend aus Steuermitteln finanziert wird“), Linke S. 18, Grüne S. 94 („Pflegebürgerversicherung“). Finanzierungsmix bzw. Teilleistung mit Kapitaldeckung: CDU/CSU S. 71 (u. a. „eigenverantwortliche Vorsorge“, Pflegezusatzversicherungen), FDP S. 35 („Teilleistung … beibehalten“, kapitalgedeckte Komponente). |
| G4 | Pflegekräfte: Bezahlung, Arbeitsbedingungen, Anwerbung aus dem Ausland | in den Programmen eher als Ausbau- denn als Richtungskonflikt sichtbar | Tarifgebundene Gehälter refinanzieren: SPD S. 32. Mehr Ausbildung und bessere Bezahlung, Anwerbung aus ärmeren Ländern als „zynische Politik“: BSW S. 27. Entlastung des Pflegepersonals: FDP S. 35. Eine ausdrücklich gegenläufige Position habe ich nicht gefunden; als Streitfrage ist G4 schwächer belegt. |
| G5 | Krankenhausreform (KHVVG 2024): Leistungsgruppen, Vorhaltevergütung, Länderplanung, Standortschließungen | Bundestag, Textarchiv 2024 kw42: Beschluss am 17.10.2024 (Drs. 20/11854, Beschlussempfehlung 20/13407); Kritik von CDU/CSU, AfD, Gruppe Die Linke, BSW und Ländern. Koalitionsvertrag Z. 3441–3454 (fortführen und anpassen) | Fortführen: Grüne S. 89. Korrigieren: CDU/CSU S. 69–70 („Fehlsteuerungen … korrigieren“, Planungshoheit der Länder). Ablehnen: BSW S. 27, AfD S. 28 („nicht geeignet“). Fallpauschalen abschaffen: Linke S. 17–18. Spezialisierung: FDP S. 33. |
| G6 | Impfpflicht (historischer Konflikt 2021/22) | GLES 2021 `q27j` (Studiendokumentation). Bundestag, Plenarprotokoll 20/28 vom 07.04.2022, TOP 6 (Drs. 20/516, 20/680, 20/899, 20/954, 20/978, 20/1353): Der Gruppenentwurf in Ausschussfassung wurde „in zweiter Beratung abgelehnt“. BVerfG, 1 BvR 2649/21, Beschluss vom 27.04.2022: Verfassungsbeschwerde gegen die einrichtungsbezogene Nachweispflicht (§ 20a IfSG) erfolglos. Deutscher Ethikrat, Ad-hoc-Empfehlung vom 22.12.2021: „Argumente gegen“ S. 11–13, „Argumente für“ S. 13–16; mehrheitliche Empfehlung der Ausweitung „mit vier Gegenstimmen“, S. 17 | Im Protokoll werden eine Impfpflicht ab 18, eine ab 60 mit Beratungspflicht, ein Vorsorge-Antrag der Union und die Ablehnung jeder Impfpflicht als Positionen benannt. Wahlprogramme 2025 sind dafür nicht einschlägig. |

### 3.2 Verfügbare Originalfragen

**Lokal vorhandene ESS-Ausgaben (zuerst geprüft):**

| Studie | Nr. / Variable | PDF-S. | Wortlaut (Auszug, wörtlich) | Skala / Filter | Eignung |
|---|---|---|---|---|---|
| E10-SC | A1 `panpriph` | 2 | „Ist es bei der Bekämpfung einer Pandemie wichtiger, die Gesundheit der Bevölkerung oder die Wirtschaft vorrangig zu berücksichtigen?“ | 0 „Viel wichtiger, die Gesundheit der Bevölkerung vorrangig zu berücksichtigen“ bis 10 „Viel wichtiger, die Wirtschaft …“; kein Filter | sofort auswertbar; pandemiebezogene Abwägung, historisch |
| E10-SC | A2 `panmonpb`, A4 `panclobo`, A5 `panresmo` | 2 | Überwachung/Nachverfolgung vs. Privatsphäre; Grenzen schließen; Bewegungsfreiheit einschränken | jeweils 0–10; kein Filter | primär Bürgerrechte/Eingriffsbefugnisse, sekundär Gesundheit |
| E10-SC | A3 `panfolru` | 2 | „…für Sie persönlich wichtiger, die staatlichen Vorschriften einzuhalten oder Ihre eigenen Entscheidungen zu treffen?“ | 0–10 | persönliche Befolgungsnorm, **keine Politikpräferenz** |
| E8, E9, E10, E11 | `stfhlth` | E8 S. 12, E9 S. 13, E10 S. 6, E11 S. 12 | „…den derzeitigen Zustand des Gesundheitssystems in Deutschland …“ | 0–10 | **Bewertung, keine Präferenz**: bewusst ausschließen |
| E11 | Gesundheitsmodul (Zugang, Wartezeit, Diskriminierung) | 37–38, 47–49 | Erfahrungen mit Arzttermin bzw. Behandlung | – | Erfahrungen, keine Einstellungen: ausschließen |
| E8 | Gesundheitsverantwortung | – | **nicht enthalten.** E6–E8 umfassen nur Alter, Arbeitslose und Kinderbetreuung (S. 36). | – | Lücke |
| E4 (nicht lokal) | D16 `gvhlthc` u. a. | Source S. 28 | „…ensure adequate health care for the sick?“ | 0–10 | nur 2008/09; deutscher Wortlaut nicht geprüft |

**Weitere Instrumente:**

| Studie | Nr. / Var. | PDF-S. | Wortlaut (Auszug, wörtlich) | Antwortskala / Filter | Eignung |
|---|---|---|---|---|---|
| I21 | F4 Zeile 2 / V5 (Q4b) | 4 | „Der Staat sollte nur eine medizinische Grundversorgung anbieten.“ | „Stimme voll und ganz zu“ … „Stimme überhaupt nicht zu“, „Kann ich nicht sagen“; alle | **hoch**: Umfang staatlicher Versorgung |
| I21 | F5 / V7 | 5 | „Inwieweit wären Sie bereit, höhere Steuern zu zahlen, um die Gesundheitsversorgung für alle Menschen in Deutschland zu verbessern?“ | „Auf jeden Fall bereit“ … „Auf keinen Fall bereit“, „Kann ich nicht sagen“ | **hoch**: Finanzierungsabwägung (persönliche Zahlungsbereitschaft) |
| I21 | F3 / V3 | 4 | „Ist es gerecht oder ungerecht, dass sich Menschen mit höherem Einkommen eine bessere Gesundheitsversorgung leisten können als Menschen mit geringerem Einkommen?“ | „Sehr gerecht“ … „Sehr ungerecht“, „Kann ich nicht sagen“ | **hoch**: Gleichheitsprinzip; berührt G1, misst aber **keine** Haltung zur Bürgerversicherung |
| I21 | F6 / V8, V9 | 5 | „Die Menschen sollten auch dann Zugang zu öffentlich finanzierter Gesundheitsversorgung haben, wenn … sie nicht die deutsche Staatsbürgerschaft haben / … sie sich gesundheitsschädigend verhalten.“ | 5 Zustimmungsstufen und „Kann ich nicht sagen“ | mittel: Anspruchsbedingungen (V8 sekundär Migration) |
| I21 | F27 / V55–V59; F28 / V61–V63 (international optional Q29) | 11–12 | „…in Zeiten schwerer Epidemien der Staat das Recht haben, Folgendes zu tun?“ (Geschäfte schließen, Zuhausebleiben anordnen, digitale Überwachung, Maskenpflicht, Versammlungsverbot; Isolation, Schulschließung, Grenzschließung) | „Auf jeden Fall“, „Eher ja“, „Eher nein“, „Auf keinen Fall“, „Kann ich nicht sagen“ | primär Bürgerrechte; historisch |
| I21 | F2, F4 Zeile 3, F19, F20, F15, F34 | 4, 8–9, 13 | Vertrauen, Funktionsbewertung, Zufriedenheit, Impf-Überzeugungen, Versicherungsart | – | Bewertungen, Überzeugungen oder Hintergrundmerkmal: **ausschließen** |
| I16 | J007a C | 9 | „Der Staat sollte … gesundheitliche Versorgung für Kranke sicherzustellen.“ | „auf jeden Fall verantwortlich sein“ … „auf keinen Fall verantwortlich sein“, „Kann ich nicht sagen“ | mittel: 2016, CASI |
| I16 | J006 B | 9 | „…ob die Regierung dafür weniger oder mehr Geld ausgeben sollte. Bedenken Sie dabei, dass sehr viel höhere Ausgaben auch höhere Steuern erfordern können.“ – „Gesundheitswesen“ | „sehr viel mehr ausgeben“ … „sehr viel weniger ausgeben“, „Kann ich nicht sagen“ | mittel |
| I16 | J008a / J008b | 11 | „Wer sollte Ihrer Meinung nach hauptsächlich für die Erbringung folgender Dienstleistungen zuständig sein?“ – „Gesundheitsversorgung von Kranken“ / „Betreuung und Pflege von älteren Menschen“ | nominal: Staat, private Unternehmen, Gemeinnützige, Kirchen, Familie, „Kann ich nicht sagen“ | mittel: einzige gefundene **Pflege**-Zuständigkeitsfrage (2016) |
| I22 | F42 / F43 | 17 | „Stellen Sie sich ältere Menschen vor, die Hilfe im Alltag brauchen, z. B. beim Einkaufen, Putzen, Wäschewaschen usw. Wer sollte Ihrer Meinung nach HAUPTSÄCHLICH diese Hilfe leisten?“ / „…die Kosten dieser Hilfe … HAUPTSÄCHLICH übernehmen?“ | nominal (F43: „Die älteren Menschen selbst oder deren Familie“, „Der Staat / Finanzierung aus öffentlichen Mitteln“, „Kann ich nicht sagen“) | mittel: Alltagshilfe, **nicht Pflege im Sinne des SGB XI**; Primärzuordnung mit der Familie-Rubrik abstimmen, nicht doppelt zählen |
| I19 | F9 Zeile 1 | 7 | „…dass Menschen mit höherem Einkommen sich eine bessere medizinische Versorgung leisten können als Menschen mit niedrigerem Einkommen?“ | 5 Gerechtigkeitsstufen und „Kann ich nicht sagen“ | Vorgänger von I21 F3 (2020) |
| G21n / G21v | `q27j` (Nw336/Vw256) | G21n 97–98 (F54); G21v 63 | „In Zeiten einer Pandemie wie Corona sollte es eine allgemeine Impfpflicht geben.“ | 1 „stimme voll und ganz zu“ … 5 „stimme überhaupt nicht zu“, -99; kein Filter | **historischer Konflikt** (Erhebung 2021); keine aktuelle Position |
| G25 | `q155` (Nw718, CSES Modul 6 Q26b) | 182 (F82) | „Wie gut ist unser politisches System in der Lage, eine angemessene Gesundheitsversorgung für alle Bürgerinnen und Bürger zu gewährleisten?“ | 4 Stufen | **Leistungsbewertung**: ausschließen |
| A21 / A23 | `iw04` | A23 CAPI 51 (F065F); A23 MAIL B 20 (F47); A21 CAWI 48 (F038, Split A, C) | „Der Staat muss dafür sorgen, dass man auch bei Krankheit, Not, Arbeitslosigkeit und im Alter ein gutes Auskommen hat.“ | 4 Zustimmungsstufen; je nach Modus Split-abhängig | bündelt vier Risiken; **keine bereichsspezifische Aussage**: nicht für Gesundheit oder Rente verwenden |
| PB 2021/2022 | (Variablennamen unbekannt) | – | laut DataCite-Themenliste u. a. „Befürwortung einer Impfpflicht für Beschäftige im Gesundheits- und Pflegebereich“, „Einstellung zu einer allgemeinen Impfpflicht“ | nicht eingesehen | nur Metadaten; CATI; Wahlberechtigte |

Eurobarometer: Ich habe keinen Fragebogen eingesehen. Die gefundene Spezialbefragung 509 „Social issues“ stammt aus Nov./Dez. 2020 und betrifft EU-Prioritäten, keine konkreten deutschen Reformen. Das ist nur über Metadaten und Suchergebnisse bekannt.

### 3.3 Bewertung und Rubrikprüfung

- **Aktueller 43-Fragen-Bestand: nicht abgedeckt.** Keine der fünf Sozialstaatsfragen (ESS8 `gvslvol`, `gvslvue`, `gvcldcr`, `bnlwinc`, `eduunmp`) betrifft Gesundheit oder Pflege. `docs/abdeckung-v2.md` benennt die Lücke bereits zutreffend („Gesundheit, Pflege und Leistungserbringung brauchen Ergänzung“).
- **Mit verfügbaren Instrumenten: teilweise erschließbar.** Allgemeine Prinzipien sind über ISSP 2021 und 2016 abbildbar: Umfang der Staatsleistung, Steuerbereitschaft, Gleichheit beim Zugang, Anspruchsbedingungen, Zuständigkeit für Versorgung und Altenpflege. Die konkreten deutschen Konflikte G1–G5 haben in den geprüften Instrumenten **keine** Bevölkerungs-Originalfrage.
- **Rubrikentscheidung:** Innerhalb „Sozialstaat“ ist der Bereich derzeit **nicht angemessen erfasst**. Ich empfehle eine **eigene Ergänzung als ausgewiesene Binnenfacette „Gesundheit und Pflege“** mit eigener Primärzuordnung und Mindestabdeckung. Begründung: eigene Institutionen (GKV/PKV, SPV, Länder-Krankenhausplanung), eigene Wahl-O-Mat-These (16) und eigene Literatur zur Legitimität von Gesundheitssystemen. Ob daraus eine sichtbare Hauptrubrik wird, ist eine Produktentscheidung für Steven. Empirisch spricht nichts geprüft dafür oder dagegen.
- Pandemie-Eingriffsbefugnisse (ESS10 A1–A5, ISSP 2021 F27/F28, GLES 2021 `q27j` und `q27k`) erhalten die **Primärzuordnung Bürgerrechte/Sicherheit** und eine Nebenbeziehung zur Gesundheit. So zählen sie nicht doppelt als Gesundheitsbreite.

### 3.4 Erlaubte Interpretation

- Jede Frage bleibt eine **konkrete Einzelangabe** mit Originalkategorien. Das gilt zum Beispiel für F4b („nur Grundversorgung“: Zustimmung bedeutet Präferenz für begrenzte Staatsleistung, Ablehnung keine bestimmte Reform) und F5 (persönliche Bereitschaft, keine Systempräferenz).
- Eine **gemeinsame Dimension** „Gesundheitssolidarität“ aus F3, F4b, F5 und F6 ist inhaltlich denkbar. Sie darf aber nicht vorausgesetzt werden: Antwortformate und Gegenstände unterscheiden sich, und ein Test bräuchte einen eigenen Prüfvertrag mit zurückgehaltenen Daten. Ein **formativer Wert** ist derzeit nicht begründbar, weil Gewichte und Inhaltsabdeckung fehlen.
- GLES 2021 `q27j` beschreibt nur die Haltung im Herbst 2021 zu einer „allgemeinen Impfpflicht in Zeiten einer Pandemie“. Daraus folgt keine heutige Position.

### 3.5 Verbleibende Lücken

Fehlende Daten in den geprüften Instrumenten: Bürgerversicherung bzw. Wahl zwischen GKV und PKV, Beitragsbemessung, Zuzahlungen und Praxisgebühr, Pflegevollversicherung und Eigenanteile, Pflegekräfte (Bezahlung, Anwerbung), Krankenhausreform, Primärarztsystem. Nicht geprüft habe ich GLES-Panelwellen außer W30, die GLES-RCS im Original, Politbarometer-Wortlaute, Eurobarometer-Wortlaute, den deutschen ESS4-Wortlaut, SOEP und den Gesundheitsmonitor.

---

## 4. Bereich B: Arbeit und Rente

### 4.1 Streitfragen 2021–2026

| Nr. | Streitfrage | Beleg „stand zur Wahl“ / Kontext | vertretene Positionen (PDF-Seite) |
|---|---|---|---|
| R1 | Rentenniveau (Haltelinie) | Bundestag, Textarchiv 2025 kw49: am 05.12.2025 Beschluss zum Entwurf eines Gesetzes zur Stabilisierung des Rentenniveaus (Drs. 21/1929), Haltelinie bis 2031; Rentenkommission für die Zeit danach. Koalitionsvertrag Z. 587–594 | Dauerhaft mindestens 48 %: SPD S. 25, Grüne S. 97. Anhebung auf 53 %: Linke S. 15. Höheres Leistungsniveau nach österreichischem Vorbild: BSW S. 3, 23. „ein durch wirtschaftliches Wachstum garantiertes stabiles Rentenniveau“ und Beitragsstabilität: CDU/CSU S. 35. Steigendes Niveau über Aktienrente: FDP S. 21. Fachlich: Sachverständigenrat, JG 2023/24, Kap. 5. Die Mehrheit nennt u. a. eine Dämpfung über den Nachhaltigkeitsfaktor als Option (S. 7); das Minderheitsvotum Truger lehnt wesentliche Elemente ab (S. 74). |
| R2 | Renteneintrittsalter, abschlagsfreier Zugang nach langer Beitragszeit | Wahl-O-Mat These 9: „Alle Beschäftigten sollen bereits nach 40 Beitragsjahren ohne Abschläge in Rente gehen können.“ Aktivrentengesetz (Drs. 21/2673), Bundestag 05.12.2025 | Bestehende Regelung samt 45-Jahre-Regel beibehalten: CDU/CSU S. 34. Keine Anhebung der Regelaltersgrenze, 45-Jahre-Regel bleibt: SPD S. 25. Regelaltersgrenze 65, nach 40 Jahren ab 60: Linke S. 15. Nach 45 Jahren mit 63, keine Erhöhung: BSW S. 23. Flexibel, abschlagsfrei nach 45 Arbeitsjahren: AfD S. 19. Flexibel nach schwedischem Vorbild: FDP S. 21. Fachlich: SVR-Mehrheit für eine Kopplung an die fernere Lebenserwartung (S. 2, 7). |
| R3 | Finanzierung und Kreis der Versicherten; Kapitaldeckung | wie oben; SVR Kap. 5 | Alle Erwerbstätigen bzw. Abgeordnete einbeziehen: Grüne S. 98, BSW S. 23. Politiker einbeziehen, weniger Verbeamtungen: AfD S. 19. Gesetzliche Aktienrente: FDP S. 21. Frühstart-Rente: CDU/CSU S. 35. „Junior-Spardepot“: AfD S. 20. „Keine Spekulation mit der Rente am Aktienmarkt“: BSW S. 23. |
| R4 | Mindestlohn: Höhe und wer festsetzt | Wahl-O-Mat These 38: „Der gesetzliche Mindestlohn soll spätestens 2026 auf 15 Euro erhöht werden.“ BMAS-Meldung vom 03.06.2022: 12 € per Gesetz zum 01.10.2022. Mindestlohnkommission, Beschluss vom 27.06.2025 (13,90 € ab 2026, 14,60 € ab 2027). Koalitionsvertrag Z. 544–552 („15 Euro im Jahr 2026 erreichbar“) | Bis 2026 auf 15 € bzw. höher: SPD S. 23, Grüne S. 67, Linke S. 26 (16 €), BSW S. 3, 21. Festsetzung durch die unabhängige Kommission, „keine Mindestlohnentscheidung im Deutschen Bundestag“: CDU/CSU S. 33; „lehnen politische Eingriffe … ab“: FDP S. 18. AfD: keine Aussage zur Höhe in den geprüften Passagen. |
| R5 | Arbeitszeit | Wahl-O-Mat These 25 (35-Stunden-Woche als gesetzliche Regelarbeitszeit). Koalitionsvertrag Z. 558–567 (wöchentliche statt tägliche Höchstarbeitszeit) | Wöchentliche Höchstarbeitszeit: CDU/CSU S. 14, FDP S. 18 (FDP lehnt zugleich eine gesetzliche Vier-Tage-Woche mit vollem Lohnausgleich ab). 32 Stunden bzw. Vier-Tage-Woche bei vollem Lohn- und Personalausgleich: Linke S. 16. |
| R6 | Tarifbindung, Tariftreue, Streikrecht | Wahl-O-Mat These 31 (Streikrecht in kritischer Infrastruktur einschränken). Koalitionsvertrag Z. 553–554 (Bundestariftreuegesetz) | Tariftreuegesetz: SPD S. 23, Grüne S. 67. Ziel höhere Tarifbindung: CDU/CSU S. 32. Pflichtschlichtung, Ankündigungsfristen und Notbetrieb in kritischen Bereichen: FDP S. 19. Absage an jede Einschränkung: SPD S. 23. Verteidigen, auch für Beamte: Linke S. 28. |
| R7 | Bürgergeld/Grundsicherung (nur Abgrenzung) | Wahl-O-Mat These 3; GLES 2025 `q27k`; Koalitionsvertrag Z. 500–501 | gehört primär zum Sozialstaat (anderer Auftrag); AfD S. 23 („Aktivierende Grundsicherung“) |
| R8 | Anwerbung ausländischer Fachkräfte | Wahl-O-Mat These 11; Koalitionsvertrag Z. 422 („Work-and-stay-Agentur“) | Ausländische Fachkräfte gewinnen: CDU/CSU S. 3, 15. „Vor jeglicher weiterer außereuropäischer Fachkräfteeinwanderung … zunächst die heimischen Potenziale ausschöpfen“: AfD S. 114. Arbeitsmigration: Grüne S. 127. Primär Migration, sekundär Arbeit. |

### 4.2 Verfügbare Originalfragen

**Lokal vorhandene ESS-Ausgaben:**

| Studie | Nr. / Variable | PDF-S. | Inhalt | Skala / Filter | Eignung |
|---|---|---|---|---|---|
| E8 | E6 `gvslvol` | 36 (Liste 48: Antwortlisten-PDF S. 49) | „…einen angemessenen Lebensstandard im Alter sicherzustellen?“ | 0–10, 77/88. Der Fragebogen druckt die Skala bis 9, die Liste bis 10 (bekannter Druckfehler) | **bereits im 43er-Bestand**; allgemeine Staatsverantwortung, kein Rentenniveau |
| E8 | E7 `gvslvue`, E34 `eduunmp`, E33 `bnlwinc` | 36, 42 | Arbeitslose, Aktivierung, Zielgruppenbegrenzung | 0–10 bzw. 4 Stufen | bereits im Bestand (Sozialstaat) |
| E8 | E21–E32 `ubpay`, `ubedu`, `ubunp` (+ `ub50*`, `ub20*`, `ubsp*`) | 38–41 | Kürzung der Arbeitslosenunterstützung bei Ablehnung schlechter bezahlter oder geringer qualifizierter Stellen bzw. unbezahlter Gemeinwohlarbeit | 4 Kategorien von „gesamte … verlieren“ bis „weiterhin … bekommen“; **E20-Zufallszuweisung, jede Person sieht eine Zielperson** | inhaltlich nah an Wahl-O-Mat These 3, aber 2016/17 und primär Sozialstaat; nur innerhalb des Zufallszweigs auswerten |
| E8 | E4 `slvpens`, E5 `slvuemp` | 35 | eingeschätzter Lebensstandard von Rentnern bzw. Arbeitslosen | 0–10 | Wahrnehmung: ausschließen |
| E9 | D21a/b `iagrtr` (Split-Ballot nach Frau/Mann) | 37 / 43 | „…ideale Alter für eine Frau, um sich dauerhaft aus dem Berufsleben zurückzuziehen?“ | offene Altersangabe; 000/111/222/777/888 | **Altersnorm, keine Rentenpolitik**: nicht als Renteneintrittsalter-Präferenz verwenden |
| E9 | G14b/G17b (Rentengerechtigkeit) | 87–88 | Gerechtigkeit eigener bzw. berufsgleicher Renten | gefiltert | Wahrnehmung: ausschließen |
| E11 | `eqparlv`, `fineqpy` | 51–52 laut Matrix | Elternzeit, Lohnungleichheitsbußgeld | 5 Stufen | im Bestand unter Gleichstellung; sekundär Arbeit, nicht doppelt zählen |
| E5 | Gewerkschaftseinfluss am Arbeitsplatz | 63 | Wahrnehmung | – | ausschließen |
| E4 (nicht lokal) | D15 `gvjbevn`, D20 `gvpdlwk`, D36 (Rentenhöhe nach Einkommen), D46 (Bezahlbarkeit der Renten) | Source 28, 32, 35 | – | – | historisch 2008/09; deutscher Wortlaut nicht geprüft |

**Weitere Instrumente:**

| Studie | Nr. | PDF-S. | Wortlaut (Auszug, wörtlich) | Skala | Eignung |
|---|---|---|---|---|---|
| I16 | J006 F / G | 9 | Mehr oder weniger Ausgaben für „Renten und Pensionen“ / „Arbeitslosenunterstützung“ (mit Steuerhinweis) | 5 Stufen und 8 | mittel |
| I16 | J007a A / D / F | 9 | „…einen Arbeitsplatz für jeden bereitzustellen, der arbeiten will.“ / „…den alten Menschen einen angemessenen Lebensstandard zu sichern.“ / Arbeitslose | 4 Verantwortungsstufen und 8 | mittel; D entspricht inhaltlich ESS8 `gvslvol` |
| I16 | J005 F / B | 8 | „Verkürzungen der wöchentlichen Arbeitszeit, um neue Arbeitsplätze zu schaffen“ / „Finanzierung von Beschäftigungsprogrammen“ | „Befürworte ich stark“ … „Lehne ich stark ab“, 8 | Rahmung von 2016 (Beschäftigung); **nicht** als Haltung zur 35-Stunden- oder Vier-Tage-Woche umdeuten |
| I19 | F4 Zeile 3 / F5 | 5 | Staat und Lebensstandard Arbeitslose / wer Einkommensunterschiede verringern soll (u. a. „Die Gewerkschaften“) | 5 Stufen / nominal | gering für Arbeit (F5 primär Wirtschaft) |
| G25 | `q27k` | 159 (F69) | „Das Bürgergeld sollte deutlich abgesenkt werden.“ | 1–5, -99 | **Sozialstaat**, nicht hier zählen |
| A21 / A23 | `pi01`/`pi02`, `pi07` | A23 CAPI 52; A23 MAIL B 20; A21 CAWI 51 | Sozialleistungen kürzen, beibehalten oder ausweiten; Steuersenkung oder mehr Geld für soziale Leistungen | nominal (CAPI/CAWI mit Vorfilter „Meinung gebildet“) | allgemeiner Sozialstaat, nicht spezifisch Rente |
| PB 2023 / 2024 / 2025 | – | – | laut DataCite u. a. „Beurteilung der Mindestlohnerhöhung“ (2023), „Einstellung … zu vorgezogenem Renteneintritt“ (2024), „präferierte Lösung der Finanzierung“ und „Fragen zum Rentenniveau“ (2025) | nicht eingesehen | **nur Metadaten**; potenziell aktuellster Rentenweg, Wortlaut, Filter und Monat ungeprüft |

Zu Mindestlohnhöhe, Tariftreue, Streikrecht, wöchentlicher Höchstarbeitszeit und Regelaltersgrenze habe ich in den geprüften ESS-, ISSP-, GLES- und ALLBUS-Instrumenten **keine** Originalfrage gefunden.

### 4.3 Bewertung und Rubrikprüfung

- **Aktueller Bestand: teilweise abgedeckt.** Rente ist nur über die allgemeine Staatsverantwortung im Alter vertreten (`gvslvol`). Arbeit nur über Arbeitslosenabsicherung bzw. Aktivierung und zwei Gleichstellungsmaßnahmen. `docs/abdeckung-v2.md` nennt „Rente/Arbeitslosigkeit/Betreuung erschlossen“. Für Rente ist das zu weit: Rentenniveau, Altersgrenze und Finanzierung sind nicht erfasst.
- **Rubrikentscheidung:**
  - **Rente** gehört in die Rubrik Sozialstaat. Dort ist sie nicht angemessen erfasst und braucht eine eigene Ergänzung als ausgewiesene Binnenfacette „Alterssicherung“ mit mindestens einer konkreten Maßnahmefrage. Ein Kandidat ist die ISSP-2016-Ausgabenfrage; aktueller wären Politbarometer-Fragen, falls Wortlaut und Rechte tragen.
  - **Arbeitsmarktordnung** (Mindestlohn, Arbeitszeit, Tarif/Streik) gehört zu Wirtschaft. Die Wirtschaftsauswahl (ESS9 Gerechtigkeitsprinzipien, `gincdif`) enthält dazu nichts. `docs/abdeckung-v2.md` nennt „Arbeits-/Industriepolitik“ selbst als unvollständig. Ich empfehle eine **eigene Binnenfacette „Arbeitsmarktordnung“**. Eine neue Hauptrubrik halte ich messtheoretisch nicht für nötig, solange beide Facetten sichtbar ausgewiesen und mit Lücken dokumentiert sind.
  - Fachkräfte haben die Primärzuordnung Migration, Bürgergeld die Primärzuordnung Sozialstaat. Beide werden hier nicht doppelt gezählt.

### 4.4 Erlaubte Interpretation

Es gibt nur konkrete Einzelangaben. Verantwortungs-, Ausgaben- und Maßnahmefragen dürfen nicht gleichgesetzt werden: „Staat verantwortlich“ heißt nicht „mehr Rentenniveau“. Eine gemeinsame Dimension „Sozialstaatsumfang“ über `gvslvol`, `gvslvue` und ISSP J006/J007 ist ein bekanntes Forschungsthema, hier aber ungeprüft. Unterschiedliche Studien, Jahre und Skalen erlauben keine gemeinsame Personenmatrix. Ein formativer Wert ist nicht begründet.

### 4.5 Verbleibende Lücken

Fehlende Daten: Mindestlohnhöhe und -festsetzung, Rentenniveau, Regelaltersgrenze bzw. abschlagsfreie Rente, Einbeziehung von Beamten und Selbstständigen, Aktienrente bzw. Generationenkapital, Tariftreue, Streikrecht, Arbeitszeitgesetz. Ein bewusster Ausschluss wird empfohlen für ESS9 `iagrtr`, die Wahrnehmungsfragen E4/E5 und ALLBUS `iw04` (Bündelung von vier Risiken).

---

## 5. Bereich C: Wohnen

### 5.1 Streitfragen 2021–2026

| Nr. | Streitfrage | Beleg / Kontext | vertretene Positionen (PDF-Seite) |
|---|---|---|---|
| W1 | Mietpreisbremse, Mietendeckel, Mietenstopp | Wahl-O-Mat These 6: „Bei Neuvermietungen sollen die Mietpreise weiterhin gesetzlich begrenzt werden.“ BVerfG 2 BvF 1/20 u. a., Beschluss vom 25.03.2021: Berliner MietenWoG „mit Art. 74 Abs. 1 Nr. 1 in Verbindung mit Art. 72 Abs. 1 GG unvereinbar und nichtig“. Bundestag 26.06.2025: Verlängerung bis 31.12.2029 (Drs. 21/322); abgelehnt wurden der Antrag der Linken 21/355 („Mietpreisbremse verschärfen – Mieten stoppen“) und der Grünen-Entwurf 21/222. GLES 2021 und 2025 führen eigene Fragen. | Unbefristet bzw. verschärft: SPD S. 20, Grüne S. 69 (inkl. „Mietenstopp“). Bundesweiter Mietendeckel: Linke S. 8, BSW S. 28. „wirksamer und angemessener Mieterschutz – dazu gehören auch die Regeln zur Miethöhe“: CDU/CSU S. 10, 73. Auslaufen lassen, kein Mietendeckel: FDP S. 44. Lehnt „die Mietpreisbremse oder den Mietendeckel ab“: AfD S. 39. |
| W2 | Vergesellschaftung großer Wohnungsunternehmen (Berlin) | Amtliche Mitteilung der Landesabstimmungsleiterin zum Volksentscheid am 26.09.2021: Beschlussentwurf S. 4–5, Argumente der Initiative und des Senats S. 7–10 (Senat u. a.: Volksbegehren „rechtlich unverbindlich“, „juristisches Neuland“). Expertenkommission, Abschlussbericht Juni 2023: Mehrheitsauffassung vs. Sondervotum dreier Mitglieder (S. 16–18) | Unterstützung: Linke S. 9. In den übrigen geprüften Bundesprogrammen keine ausdrückliche Position gesucht oder gefunden. Berlin-spezifisch; eine Abstimmung ist keine Befragung. |
| W3 | Sozialer bzw. gemeinnütziger Wohnungsbau oder Wohngeld | Koalitionsvertrag Z. 767, 777 | Ausbau sozialer/gemeinnütziger Bau: SPD S. 21, Grüne S. 72, Linke S. 9, BSW S. 27–28, CDU/CSU S. 10, 73 („solide gefördert“, Wohngeld anpassen). „Der bisherige soziale Wohnungsbau ist gescheitert“, stattdessen mehr Wohngeld: AfD S. 38. |
| W4 | Wohneigentumsförderung, Grunderwerbsteuer | Koalitionsvertrag Z. 735 („Starthilfe Wohneigentum“) | Freibeträge bzw. Befreiung beim Ersterwerb: CDU/CSU S. 34 (Länderoption), FDP S. 45, BSW S. 17; für Selbstnutzer aufheben: AfD S. 37. Eine ausdrückliche Gegenposition habe ich nicht gefunden. |
| W5 | Bauvorschriften, Baukosten, Gebäudeenergiegesetz | Koalitionsvertrag Z. 728–730 (Gebäudetyp E), Z. 754 („Heizungsgesetz abschaffen“). Wahl-O-Mat These 37 (fossile Heizungen) | Gebäudetyp E bzw. Baukostenmoratorium: CDU/CSU S. 73, FDP S. 44. Heizungsgesetz zurücknehmen bzw. abschaffen: CDU/CSU S. 22, AfD S. 37 (GEG abschaffen). GEG hat die Primärzuordnung Klima/Energie. |
| W6 | Grundsteuer: Umlage auf Mieter, Reform | Wahl-O-Mat These 30: „Die Grundsteuer soll weiterhin auf Mieterinnen und Mieter umgelegt werden dürfen.“ BVerfG 1 BvL 11/14 u. a., 10.04.2018 (Einheitsbewertung verfassungswidrig, Neuregelung, Fristen bis 2024) | Umlage begrenzen bzw. beenden: SPD S. 21, Grüne S. 69, Linke S. 8. Grundsteuer abschaffen: AfD S. 37, 59. Belastungsmoratorium: BSW S. 17. Eine ausdrückliche Befürwortung der Umlage habe ich nicht gesucht oder gefunden. |

### 5.2 Verfügbare Originalfragen

**Lokal vorhandene ESS-Ausgaben:** In ESS5, 8, 9, 10-SC und 11 habe ich keine wohnungspolitische Präferenzfrage gefunden, nur Angaben zu Wohngebiet und Wohnform. Damit ist **nichts sofort lokal auswertbar**.

**Weitere Instrumente:**

| Studie | Nr. / Var. | PDF-S. | Wortlaut (wörtlich) | Skala / Filter | Eignung |
|---|---|---|---|---|---|
| G25 | `q27i` (Nw336, Issuebatterie I) | 144–145 (F61) | „Der Staat sollte die Mietpreise stärker regulieren.“ | (5) „stimme überhaupt nicht zu“ … (1) „stimme voll und ganz zu“, (-99); kein Filter; Einleitung „Es gibt zu verschiedenen politischen Themen unterschiedliche Meinungen …“ | **hoch**: aktuell (Feb.–Apr. 2025), konkret. Der Status quo änderte sich danach (Verlängerung Juni 2025). Population nur deutsche Staatsangehörige. |
| G21n / G21v | `q27i` | 97–98 / 63 | „Die Regierung sollte einen landesweiten Mietendeckel einführen.“ | 1–5, -99 | historisch (Herbst 2021, nach BVerfG-Beschluss) |
| RCS25 | `pre038b` | (Auszug P50) | gleicher Wortlaut wie G25 `q27i` | 1–5 | **nicht selbst eingesehen**, nur aus Codex-Auszug |
| I16 | J007b I | 10 | „Der Staat sollte … denjenigen, die es sich finanziell nicht leisten können, eine angemessene Wohnung zur Verfügung zu stellen.“ | 4 Verantwortungsstufen und 8 | mittel: Wohnraumversorgung als Staatsaufgabe (2016) |
| I23 | F8 Zeile 5 | 7 | Bevorzugung in Deutschland Geborener u. a. bei „Wohnraum“ | 5 Stufen | primär Migration: hier nicht zählen |
| A23 | Migrationsfolgen „…zu Problemen auf dem Wohnungsmarkt“ | MAIL A 12; CAPI 25 | wahrgenommene Folge | – | primär Migration, Wahrnehmung: ausschließen |

Hinweis zu G25 und G21: Die Dokumentation 2025 listet die Ausprägungen in der Reihenfolge 5 bis 1, die von 2021 in der Reihenfolge 1 bis 5. Vor einer Nutzung ist zu prüfen, ob das nur die Auflistung betrifft oder auch Darstellung bzw. Codierung (Vermutung: nur Auflistung).

### 5.3 Bewertung und Rubrikprüfung

- **Aktueller Bestand: nicht abgedeckt** (0 Fragen). `docs/abdeckung-v2.md` führt Wohnen nur als Binnenfacette und listet `q27i` unter Wirtschaft. Die Auswahl übernimmt sie mangels GESIS-Zugang nicht.
- **Mit verfügbaren Instrumenten: teilweise erschließbar.** Abbildbar sind die Mietpreisregulierung (GLES 2025, aktuell), historisch der Mietendeckel (GLES 2021) und die allgemeine Staatsverantwortung für Wohnraum (ISSP 2016). Für W2–W6 habe ich keine Bevölkerungs-Originalfrage gefunden.
- **Rubrikentscheidung:** Wohnen ist weder in Wirtschaft noch in Sozialstaat angemessen erfasst. Mietregulierung ist Marktregulierung, Wohnraumversorgung ist Sozialstaat. Ich empfehle eine **eigene Ergänzung als ausgewiesene Binnenfacette „Wohnen“** mit Primärzuordnung je Frage: `q27i` primär Wirtschaft/Marktordnung, J007b I primär Sozialstaat, jeweils mit Nebenbezug Wohnen. Zusätzlich muss die Lücke bei W2–W6 sichtbar dokumentiert werden. Eine Hauptrubrik „Wohnen“ entscheidet Steven; mit derzeit höchstens zwei bis drei tragfähigen Fragen wäre sie dünn.

### 5.4 Erlaubte Interpretation

`q27i` ist eine konkrete Einzelangabe zur Richtung „stärkere Regulierung als 2025“. Ablehnung heißt nicht automatisch „Abschaffung der Mietpreisbremse“. GLES 2021 `q27i` (Mietendeckel) und 2025 `q27i` (Mietpreise regulieren) sind **verschiedene Gegenstände** und keine Zeitreihe. Für eine gemeinsame Dimension oder einen formativen Wert fehlt jede Grundlage.

### 5.5 Verbleibende Lücken

Fehlende Daten: sozialer bzw. gemeinnütziger Wohnungsbau, Vergesellschaftung (nur Berliner Abstimmung, keine Befragung), Eigentumsförderung, Bauvorschriften, Grundsteuer-Umlage. GEG gehört primär zu Klima/Energie.

---

## 6. Zugang und Rechte je Studie

| Studie | Zugang | Öffentliche zusammengefasste Ergebnisse (nichtkommerzielle Website) | Deutsche Fragewortlaute auf der Website | offen |
|---|---|---|---|---|
| **ESS** (E5–E11) | Registrierung im ESS-Portal; Steven hat ein Konto, die Dateien liegen lokal | Datenlizenz CC BY-NC-SA 4.0: nichtkommerzielle Nutzung mit Namensnennung möglich | Dokumentation CC BY-SA 4.0: mit Namensnennung, Änderungshinweis und Weitergabe unter gleichen Bedingungen | ob aggregierte Tabellen „Adapted Material“ sind und dann CC BY-NC-SA unterliegen; die ESS-Downloadbedingungen im Portal habe ich nicht selbst geprüft |
| **GLES** (G25, G21, RCS25) | „Zugangskategorie Safeguarded – A“; Registrierung und Zustimmung | nach GESIS-Bedingungen nur „zusammenfassende Darstellungen …, wie sie in wissenschaftlichen Arbeiten und Vorträgen üblich sind“; ob eine dauerhafte Website darunter fällt, ist offen | keine Freigabe gefunden; das GESIS-Impressum verlangt für GESIS-erstellte Texte „ausdrückliche Zustimmung“ | KI-Verarbeitungsverbot, Befristung, Fragetextrechte, CSES-Rechte bei `q155` |
| **ISSP** (I16–I23) | „Registration is required for data download.“ (GESIS-ISSP-2021-Seite, Wayback-Schnappschuss 25.06.2026) | wie GLES (GESIS-Bedingungen) | keine Freigabe gefunden. Die Hintergrunddoku 2021 trägt „© GESIS“; Rechte am englischen Source-Fragebogen (ISSP Research Group) nicht geprüft. | wie GLES; Downloadformate nicht verifiziert |
| **ALLBUS** (A21, A23) | Fragebogendokumente waren ohne Anmeldung abrufbar (selbst getestet); Daten über GESIS | wie GLES | keine Freigabe gefunden | wie GLES; Zugangskategorie nicht selbst geprüft |
| **Politbarometer** | über GESIS; Zugangskategorie nicht geprüft | wie GLES | ungeprüft; Primärforscher ist die Forschungsgruppe Wahlen | Wortlaut, Monat, Filter und Rechte vollständig offen |
| **Eurobarometer** | nicht geprüft | nicht geprüft | nicht geprüft | ganz offen |

**Wörtliche Bedingungen:**

- ESS-Disclaimer (https://www.europeansocialsurvey.org/contact/disclaimer, abgerufen 2026-10-03 ca. 19:29 UTC über WebFetch): „European Social Survey data is licensed under CC BY-NC-SA 4.0“; „European Social Survey documentation is licensed under CC BY-SA 4.0“; „The data are available without restrictions, for not-for-profit purposes.“ Gleichlautend im Feld `restrictions` der lokalen Datei `outputs/loop/breadth-data-001/sources/ess10-study-access-metadata.json`.
- GLES 2025, Studienbeschreibung, PDF S. 7, Abschnitt 1.9 (https://access.gesis.org/dbk/79269): „Daten und Dokumente sind für die wissenschaftliche, studentische und nicht kommerzielle Nutzung freigegeben: Zugangskategorie Safeguarded – A.“
- GESIS-Nutzungsbedingungen, „Gültig ab: 04.02.2026“ (https://www.gesis.org/fileadmin/upload/Datenservices/Nutzungsbedingungen/Nutzungsbedingungen.pdf; abgerufen über den Wayback-Schnappschuss vom 30.03.2026, weil der direkte Abruf mit 403 scheiterte):
  - §1: „Soweit nicht ausdrücklich anders gekennzeichnet, stellt GESIS die Datenbasis nur für wissenschaftliche Nutzungen im Rahmen eines zeitlich befristeten Vorhabens zur Verfügung.“
  - §3: „Für jede Bereitstellung der Datenbasis durch GESIS ist die Registrierung und die Zustimmung zu diesen Nutzungsbedingungen durch den Nutzer / die Nutzerin erforderlich.“
  - §4: „Soweit nicht ausdrücklich anders gekennzeichnet, ist eine kommerzielle Nutzung der von GESIS bereitgestellten Daten verboten.“
  - §4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“
  - §5: „Zulässig sind zusammenfassende Darstellungen der Daten, wie sie in wissenschaftlichen Arbeiten und Vorträgen üblich sind.“
  - §6: Bei Ende des Nutzungszwecks ist die Datenbasis „vollständig zu löschen“.
  - Die Tabelle der Zugangskategorien (§2) ist im PDF als Grafik eingebettet und wurde nicht als Text extrahiert.
- GESIS-Impressum (https://www.gesis.org/institut/impressum, Wayback-Schnappschuss 09.09.2026): „Das Copyright für veröffentlichte, von GESIS selbst erstellte Objekte bleibt allein bei GESIS. Eine Vervielfältigung oder Verwendung solcher Grafiken, Tondokumente, Videosequenzen und Texte in anderen elektronischen oder gedruckten Publikationen ist ohne ausdrückliche Zustimmung von GESIS nicht gestattet.“

Das ist eine Quellenfeststellung und keine rechtliche Bewertung. Offen sind insbesondere drei Punkte. Erstens: Ist das Projekt mit Codex- bzw. Claude-Agenten eine „Nutzung von KI-Systemen für die Verarbeitung der Datenbasis“? Das läge nahe, wenn Agenten Daten lesen oder verarbeiten; ob schon Skripte genügen, die Agenten schreiben und Steven ausführt, bleibt offen. Zweitens: Erfüllt eine dauerhafte öffentliche Website die Bedingung „zeitlich befristetes Vorhaben“ und die Löschpflicht? Drittens: Wer kann die Anzeige deutscher Fragetexte freigeben (GESIS, GLES-Team, ISSP Research Group, CSES)?

---

## 7. Priorisierte Empfehlung

### 7.1 Erste tragfähige Ergänzungen (Aktualität, Deutschlandbezug, Zugang, Rechte)

| Rang | Originalfrage(n) | Bereich (Primär) | Begründung | Voraussetzung |
|---|---|---|---|---|
| 1 | GLES 2025 Nachwahl `q27i` | Wohnen (Wirtschaft/Marktordnung) | aktuellste konkrete Wohnfrage, deutsch, Wahlkontext 2025 | Download ZA10100, GESIS-KI-Ausnahme oder Verarbeitung ohne KI, Website- und Fragetextrechte |
| 2 | ISSP 2021 DE F4b (V5), F5 (V7), F3 (V3) | Gesundheit | einzige gefundene deutsche Bevölkerungsfragen 2021 zu Umfang, Finanzierung und Gleichheit der Gesundheitsversorgung | Download ZA8000 (DE-Teil), Feldzeit und Population im Original verifizieren, Rechte wie oben |
| 3 | ISSP 2021 DE F6a/b (V8, V9) | Gesundheit (V8 Nebenbezug Migration) | Anspruchsbedingungen | wie Rang 2 |
| 4 | ISSP 2016 J007a C/D, J007b I, J006 B/F, J008a/b | Gesundheit, Alterssicherung, Wohnen, Pflege | breite Staatsaufgaben- und Ausgabenfragen mit Steuerhinweis; einzige Pflege-Zuständigkeitsfrage (J008b) | Download ZA6900 (DE), 2016 ist älter; CASI im ALLBUS-Kontext |
| 5 | ISSP 2022 F42/F43 | Pflege/Altenhilfe (Familie sekundär) | Erbringer und Finanzierung der Altenhilfe 2023 | Download ZA10000; Doppelzählung mit Familie vermeiden |
| 6 | GLES 2021 `q27j` (Impfpflicht), `q27i` (Mietendeckel) | historisch: Bürgerrechte/Gesundheit bzw. Wohnen | dokumentierter historischer Konflikt | Download ZA7701 oder ZA7700; als historisch kennzeichnen |
| 7 | Politbarometer 2024/2025 Rentenfragen | Alterssicherung | möglicherweise einzige aktuelle Rentenmaßnahmefragen | zuerst Wortlaut ergebnisblind prüfen. Die Codebücher enthalten vermutlich Häufigkeiten, das Prüfprotokoll muss das ausschließen. |

**Nicht empfohlen:** `stfhlth`, GLES `q155`, ISSP 2021 F2/F4c/F19/F20 (Bewertungen); ESS9 `iagrtr` (Altersnorm); ALLBUS `iw04` (vier Risiken gebündelt); ESS11-Gesundheitserfahrungen; ESS10 A3 `panfolru` (persönliche Norm); GLES-Kandidierendenstudie ZA10102 (keine Bevölkerungsreferenz).

### 7.2 Sofort mit lokalen ESS-Ausgaben auswertbar

Nur **ESS10-SC `panpriph`, `panmonpb`, `panclobo`, `panresmo`** (DE 2021/22, Papier/Web). Sie sind pandemiebezogen und historisch, mit Primärzuordnung Bürgerrechte bzw. Nebenbezug Gesundheit. Dazu kommen die bereits ausgewählten ESS8-Fragen (`gvslvol` usw.) und die ESS8-Zufallsvignetten `ub*`, die primär zum Sozialstaat gehören und nur je Zufallszweig auswertbar sind. Für Gesundheitspolitik im engeren Sinn, Pflege, Rentenmaßnahmen, Arbeitsmarktordnung und Wohnen liefern die lokalen ESS-Daten **keine** geeignete Frage.

### 7.3 Dateien, die Steven herunterladen müsste (erst nach Rechte- und KI-Klärung)

| Studie | Archivnr. | Version / DOI | Format |
|---|---|---|---|
| GLES Querschnitt 2025, Nachwahl | ZA10100 | 4.0.0 / 10.4232/5.ZA10100.4.0.0 | Stata (.dta, Version 16) laut Doku PDF S. 28; andere Formate nicht geprüft |
| ISSP 2021 Health and Health Care II | ZA8000 | 2.0.0 / 10.4232/5.ZA8000.2.0.0 | nicht verifiziert (Vermutung: SPSS/Stata) |
| ISSP 2016 Role of Government V | ZA6900 | 2.0.0 / 10.4232/1.13052 | nicht verifiziert |
| ISSP 2022 Family V | ZA10000 | 2.0.0 / 10.4232/5.ZA10000.2.0.0 | nicht verifiziert |
| optional GLES 2021 Nachwahl bzw. Vorwahl | ZA7701 / ZA7700 | 2.1.0 / 10.4232/1.14169 bzw. 3.1.0 / 10.4232/1.14168 | nicht verifiziert |
| optional Politbarometer 2025 bzw. 2024 | ZA9151 / ZA8974 | 1.0.0 / 10.4232/1.14794 bzw. 1.0.0 / 10.4232/1.14517 | nicht verifiziert; zuerst Wortlautprüfung |

---

## 8. Prüfung der Angaben in `docs/abdeckung-v2.md` und `docs/empirie-plan-v2.entwurf.md`

Bestätigt habe ich:
- ESS8 E6–E8 auf PDF S. 36 mit Antwortliste 48 (Antwortlisten-PDF S. 49, 0–10). Der Fragebogen druckt die Skala bis 9.
- ESS8 E33–E36 auf S. 42–43.
- G25 `q27i`/`q27j` auf F61 bzw. PDF S. 144–145 und `q27k` auf F69 bzw. PDF S. 159.
- ISSP 2016 J005 A–F (S. 8) und J007 (S. 9–10).
- ISSP 2022 F40–F43 (S. 17).
- Die Variablennamen `gvslvol`, `gvslvue`, `gvcldcr`, `bnlwinc`, `eduunmp` im ESS8-Fragebogen.

Zu präzisieren:
1. „ISSP2016 J006/J007: Ausgaben und Zuständigkeiten auch für Gesundheit/Wohnen/Bildung“: J006 enthält **kein** Wohnen; Wohnen steht nur in J007b I.
2. „Rente … erschlossen“ (Sozialstaat-Zeile) trifft nur auf die allgemeine Verantwortungsfrage zu. Rentenniveau, Altersgrenze und Finanzierung fehlen.
3. ISSP 2021 (Health and Health Care II) fehlt in der Matrix vollständig, obwohl ein öffentlicher deutscher Fragebogen existiert (access.gesis.org/dbk/77030). Für Gesundheit ist er der ergiebigste geprüfte Weg.
4. GLES 2021 `q27i` (Mietendeckel) und `q27j` (Impfpflicht) fehlen in der Matrix.
5. ESS10-SC A1–A5 (Pandemie-Abwägungen) fehlen in der Matrix; sie sind lokal sofort auswertbar.
6. Die Matrix stützt sich auf GESIS-Bedingungen ohne ausdrücklichen Hinweis auf das KI-Verarbeitungsverbot. Der Hinweis steht nur im Autorenbericht `reports/loop/authors/BREADTH-ACCESS-002.md`. Ich bestätige ihn unabhängig am PDF der Bedingungen.

---

## 9. Offene Punkte und Entscheidungen für Steven

1. Mit GESIS klären: KI-Ausnahme nach §4, Vereinbarkeit einer dauerhaften Website mit §1 und §6, Anzeige deutscher Fragewortlaute. Ohne Klärung bleiben Gesundheit, Wohnen und konkrete Rente als dokumentierte Lücken.
2. Produktentscheidung: Binnenfacetten (Empfehlung) oder sichtbare Hauptrubriken für Gesundheit/Pflege und Wohnen.
3. Sollen historische Konfliktfragen (Impfpflicht 2021, Mietendeckel 2021, Pandemiebefugnisse 2021/22) mit klarer Zeitkennzeichnung aufgenommen werden?
4. Politbarometer-Rentenfragen 2024/2025 nach einem ergebnisblinden Wortlautprotokoll prüfen. Dabei darf niemand die Häufigkeitsseiten der Codebücher öffnen.
5. Exakte deutsche Feldzeit und Population von ISSP 2021 (nationaler Technikbericht) sowie Feldzeit und Population von ISSP 2016 im Original verifizieren.
6. Weitere Instrumente bisher ungeprüft: GLES-Panelwellen 31–35, GLES-RCS-2025-Original, Eurobarometer, SOEP, Gesundheitsmonitor, ISSP 2015 Work Orientations IV (Gewerkschaften), deutscher ESS4-Wortlaut.

---

## 10. Nachweise

### 10.1 Tatsächlich geöffnete Quellen (Zugriff am 2026-10-03, Zeiten UTC)

**Lokale Dateien (gelesen ca. 19:00–19:35 UTC):**
- `reports/claude/auftraege/R2-themen-gesundheit-arbeit-wohnen.vollstaendig.md`, `00-gemeinsame-regeln.md`, `R-themen-gemeinsam.md`, `R2-themen-gesundheit-arbeit-wohnen.md`
- `docs/project.md`, `docs/abdeckung-v2.md`, `docs/empirie-plan-v2.entwurf.md`
- `outputs/loop/breadth-data-001/sources/`: `ess5-`, `ess8-`, `ess9-`, `ess10-`, `ess11-de-questionnaire.pdf`; `ess8-de-showcards.pdf`; `ess10-sc-source-questionnaire.pdf`; `gles2025-codebook.pdf` (ZA10100 Doku v1.3); `gles2021-codebook.pdf` (ZA7701 Doku v1.2); `glespanel30-questionnaire.txt`; `gles2025-instrument-only.txt`, `gles2025-variables-only.txt`; `ess-public-de-metadata-post.json`; `ess10-study-access-metadata.json`; `sourcecatalog.json`; `../exposure-boundaries.json`
- `outputs/loop/breadth-data-001/issp/`: `2016-DE-questionnaire.pdf`, `2019-DE-questionnaire.pdf`, `2020-DE-questionnaire.pdf`, `2022-DE-questionnaire.pdf`, `2023-DE-paper-questionnaire.pdf`, `2016-DE-background.txt` (gezielte Suche), `2016-monitoring.txt` (nur gezielte Zeilen zu Modus und Begleitstudie), `2019-DE-technical.txt`, `2020-DE-technical.txt`, `2022-DE-technical.txt`, `2023-DE-technical.txt` (M4-Zeilen), `report-v1.md` (Codex-Hilfsbericht)
- `outputs/loop/breadth-topics-001/gles2021pre.pdf` (ZA7700 Doku v2.2)
- `outputs/loop/breadth-access-002/gles-rights/facts-v1.md`, `gles-ai-conditions-web.json` (nur Metafelder), `sources/ess10sc-`, `ess8-`, `ess9-`, `ess5-file-metadata.json` (nur Variablennamen und -labels)
- `outputs/loop/theory/GLES-RCS-2025.web-extract.json` (Codex-Auszug)
- `reports/loop/authors/BREADTH-ACCESS-002.md` (nur die per Suche gefundenen Zeilen zum KI-Verbot)

**Online (Downloads nach `/tmp/r2`, ohne Anmeldung):**
- https://access.gesis.org/dbk/77030 (ISSP 2021 DE-Fragebogen; SHA-256 `8dd4f368…`) und https://access.gesis.org/dbk/76992 (ISSP 2021 DE-Hintergrunddoku), 19:11:54–19:11:55
- https://access.gesis.org/dbk/77370 (ISSP-2021-Übersicht Fragen/Variablen), 19:30:44
- https://access.gesis.org/dbk/77958 (ALLBUS 2023 CAPI), /77959 (CAWI, nur Titel), /77960 (MAIL A), /77961 (MAIL B), /75371 (ALLBUS 2021 CAWI), /75372 (Split A), 19:13:01–19:13:26
- https://access.gesis.org/dbk/78534 (ALLBUS 2023 Variable Report; **nur Methodenseiten S. 6, 53, 55 gelesen**, Stichwortsuche nur nach Design- und Formatbegriffen), 19:14:04
- https://web.archive.org/web/20260625020745/https://www.gesis.org/en/issp/data-and-documentation/health-and-health-care/2021 (ca. 19:11)
- https://web.archive.org/web/20260330154523id_/https://www.gesis.org/fileadmin/upload/Datenservices/Nutzungsbedingungen/Nutzungsbedingungen.pdf (SHA-256 `2a46f4ff…`), 19:29:35
- https://web.archive.org/web/20260909155242id_/https://www.gesis.org/institut/impressum, ca. 19:30
- https://www.europeansocialsurvey.org/contact/disclaimer (WebFetch, ca. 19:29); ESS-Meldungen „initial-round-12-data-release-scheduled-early-2027“ und „round-12-rotating-modules-selected“ (WebFetch, ca. 19:16)
- https://stessrelpubprodwe.blob.core.windows.net/data/round4/fieldwork/source/ESS4_source_main_questionnaire.pdf, 19:16:44
- https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS8_welfare_proposal.pdf (nur S. 2 und 9 gelesen), 19:27:26
- DataCite-API (api.datacite.org) für ZA8000, ZA10100, ZA10101, ZA10102, ZA10119–21, ZA10000, ZA10020, ALLBUS 2021/2023, GLES 2021, ISSP 2016/2019 sowie Politbarometer 2021–2025 (nur Titel, Versionen, Erhebungsdaten, Methoden- und Themenfelder), ca. 19:12–19:20
- https://www.wahl-o-mat.de/bundestagswahl2025/app/definitionen/module_definition.js (SHA-256 `b3e9bb84…`, Stand 06.02.2025), 19:17:14
- Wahlprogramme 2025, 19:18:41 (Linke 19:24:50): CDU/CSU https://www.cdu.de/app/uploads/2025/01/km_btw_2025_wahlprogramm_langfassung_ansicht.pdf; SPD https://www.spd.de/fileadmin/Dokumente/Beschluesse/Programm/2025_SPD_Regierungsprogramm.pdf; Grüne https://cms.gruene.de/uploads/assets/Regierungsprogramm_DIGITAL_DINA5.pdf; FDP https://www.fdp.de/sites/default/files/2024-12/fdp-wahlprogramm_2025.pdf; AfD https://www.afd.de/wp-content/uploads/2025/02/AfD_Bundestagswahlprogramm2025_web.pdf; Linke https://www.die-linke.de/fileadmin/user_upload/Wahlprogramm_Langfassung_Linke-BTW25_01.pdf; BSW https://bsw-vg.de/wp-content/themes/bsw/assets/downloads/BSW%20Wahlprogramm%202025.pdf
- Koalitionsvertrag 2025: https://www.koalitionsvertrag2025.de/sites/www.koalitionsvertrag2025.de/files/koav_2025.pdf, 19:24:01
- Bundestag Plenarprotokoll 20/28 (XML): https://www.bundestag.de/resource/blob/889400/831daf31987e4782b9c6d194a6776fa2/20028.xml, 19:21:23
- Bundestag Textarchiv (WebFetch, ca. 19:22–19:24): …/2025/kw49-de-rentenpaket-1128720; …/2025/kw26-de-mietpreisbremse-1084786; …/2024/kw42-de-krankenhausversorgung-1024614
- BVerfG-Pressemitteilungen (WebFetch, ca. 19:21–19:23): …/2022/bvg22-042.html; …/2021/bvg21-028.html; …/2018/bvg18-021.html
- https://www.bmas.de/DE/Service/Presse/Meldungen/2022/mindestlohn-steigt-auf-12-euro.html (WebFetch, ca. 19:22)
- https://www.mindestlohn-kommission.de/shareddocs/downloads/de/Bericht/beschluss2025.pdf, 19:22:27
- https://www.berlin.de/wahlen/historie/volksbegehren-und-volksentscheide/deutsche-wohnen-und-co-enteignen/amtliche-mitteilungen__ve.pdf, 19:22:02
- https://www.berlin.de/kommission-vergesellschaftung/_assets/abschlussbericht_vergesellschaftung-grosser-wohnungsunternehmen-230627.pdf, 19:26:50
- https://www.ethikrat.org/fileadmin/Publikationen/Ad-hoc-Empfehlungen/deutsch/ad-hoc-empfehlung-allgemeine-impfpflicht.pdf, 19:26:13
- https://www.sachverstaendigenrat-wirtschaft.de/fileadmin/dateiablage/gutachten/jg202324/JG202324_Kapitel_5.pdf, 19:26:30
- https://www.bundestag.de/resource/blob/650462/e8c573e5e5741752d1ea972a80ac025a/WD-9-035-19-pdf-data.pdf, 19:27:08
- European Observatory, *Germany: Health System Summary 2024*: https://iris.who.int/server/api/core/bitstreams/5204d87b-8e2e-4b9a-9da7-832c40e97ce1/content, 19:25:47
- bpb-Pressemitteilung 559822 (WebFetch, nur Satz zum Angebot von 38 Thesen), ca. 19:18

**Vergeblich bzw. nicht geöffnet:** gesis.org-Seiten direkt (HTTP 403 mit Cloudflare-Prüfung), GLES-RCS-2025-Fragebogen (403 bzw. 404), ISSP-2021-Monitoringbericht (kein Archivschnappschuss), deutscher ESS4-Fragebogen (URL nicht gefunden), Eurobarometer-Fragebögen (nicht gesucht).

### 10.2 Grenzen der Ergebnisblindheit (ungefragte Einblendungen)

- Suchmaschinen-Zusammenfassungen bzw. WebFetch-Ausgaben zeigten ungefragt: **EU-weite Prozentwerte aus dem Spezial-Eurobarometer 509** (Befragungsergebnisse), Ergebnis und Beteiligung des Berliner Volksentscheids 2021, Stimmenzahlen von Bundestagsabstimmungen (Impfpflicht 2022, KHVVG 2024, Rentenpaket 2025) sowie Fallzahlen (ISSP 2021 DE). Keine dieser Zahlen ist in die Bewertung eingeflossen oder in diesen Bericht übernommen.
- Der ALLBUS-2023-Variable-Report enthält Häufigkeitstabellen. Ich habe nur die Methodenseiten ausgegeben; Häufigkeitsseiten habe ich nicht angezeigt. Eine extrahierte Textfassung liegt unverändert unter `/tmp/r2/dbk78534.txt`.
- Die Health System Summary 2024 enthält Ausgaben- und EU-SILC-Kennzahlen. Eine Stichwortsuche zeigte eine Zeile mit einem Ausgabenanteil (keine Befragung) und eine Abbildungsunterschrift zu „unmet needs“. Die Abbildungswerte habe ich nicht angesehen.
- Das AfD-Programm nennt eigene Zahlen zum Rentenniveau; ich habe sie nicht übernommen.
- Projektdaten, Rohdaten und gesperrte Pfade habe ich nicht geöffnet.

### 10.3 Ausgeführte Befehle (Kurzform)

`git log`, `ls`, `cat`, `sed`, `head` und `grep` auf Repositorydateien; `pdftotext -layout` bzw. `pdftotext -f/-l`, `pdfinfo`, `pdftoppm` (eine Antwortlisten-Seite); kleine Python-Skripte zur seitenweisen Suche (`/tmp/r2/find.py`, `/tmp/r2/ctx.py`) und zum Auslesen von JSON und HTML; `curl` für öffentliche PDFs, DataCite-API-Abfragen und Wayback-Abrufe; `sha256sum`; `date -u`. Dazu WebSearch (Fundstellen-URLs) und WebFetch (bpb, ESS, BVerfG, Bundestag, BMAS). Keine Anmeldung, keine Cookies oder Token, keine Installation, kein Git-Schreibvorgang, kein `pnpm`.

### 10.4 Grenzen der eigenen Prüfung

- Rechtliche Aussagen sind Quellenfeststellungen, keine Rechtsberatung.
- GESIS-Bedingungen und -Impressum stammen aus Wayback-Schnappschüssen (30.03.2026 bzw. 09.09.2026). Eine neuere Fassung ist nicht ausgeschlossen.
- ISSP-2016- und ISSP-2021-Feldzeiten und -Populationen sind nicht vollständig im Original verifiziert. Die ISSP-Variablennamen habe ich nur für 2021 geprüft.
- Wahlprogramme habe ich per Stichwortsuche erschlossen. Weitere relevante Passagen und Gegenpositionen können fehlen; wo ich keine Gegenposition fand, ist das vermerkt.
- Politikwissenschaftliche Fachartikel im engeren Sinn habe ich nur über das ESS8-Modulkonzept herangezogen. Die übrigen fachlichen Belege sind amtliche bzw. sachverständige Dokumente (BVerfG, Bundestag, WD, Ethikrat, SVR, European Observatory, Berliner Expertenkommission) und Studiendokumentationen.
- Bürgergeld, Fachkräfte, GEG und Pandemiebefugnisse überschneiden sich mit anderen Aufträgen (Sozialstaat, Migration, Klima, Bürgerrechte). Hier sind sie nur zur Abgrenzung behandelt.
- Übereinstimmung mit früheren Codex-Berichten belegt keine Neutralität.

### 10.5 Eingesetztes Modell

Laut Laufzeitangabe: Claude Opus 5.5 (1M context), Modell-ID `claude-opus-5-5[1m]` (Anthropic). Ausgeführt als Claude-Code-Subagent.
