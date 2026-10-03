# Analyseplan v2.3: Erweiterung 2025/26 (Entwurf)

ENTWURF 0.2 vom 4. Oktober 2026, verfasst von Claude (Anthropic) im Auftrag von Steven. Fassung 0.2 legt nach der Strukturprüfung S1 (`reports/claude/agenten/S1-strukturpruefung-eurobarometer.md`) die Regeln für Tabellen ohne Basis je Frage fest (Abschnitt 6). S1 hat nur Struktur, Basen und Methodenangaben gemeldet. Ergebniswerte kennt die Auswahlrolle weiterhin nicht. Dieser Entwurf ist nicht festgeschrieben. Er erlaubt keine Auswertung, keinen Datenabruf und keine Aufnahme neuer Fragen in den Test. Voraussetzungen für jede Auswertung nach diesem Plan:

1. zwei getrennte Prüfungen dieses Entwurfs (Methoden und Reproduzierbarkeit; Quellen, Konstrukte und Fairness),
2. Stevens Freigabe jeder einzelnen Quelle nach der [Entscheidungsvorlage](entscheidungsvorlage-erweiterung-v1.entwurf.md),
3. Festschreibung mit dem Tag `analyseplan-v2.3`.

Der [Analyseplan v2.2](analyseplan-v2.2.md), seine Exporte und Prüfberichte bleiben unverändert. Dieser Entwurf ergänzt sie. Grundlage sind die ergebnisblinden Rechercheberichte R1 bis R3 und R5 bis R10 unter `reports/claude/agenten/`. Alle stammen von Claude-Subagents, also derselben Modellfamilie wie dieser Entwurf.

## 1 Was vor diesem Entwurf bekannt war

- Die Referenzen v2, v2.1 und v2.2 sind veröffentlicht und bekannt. Nichts in diesem Entwurf ist eine unberührte Bestätigung dieser Werte.
- Für die Kandidaten in Abschnitt 11 hat niemand im Projekt Antwortverteilungen gelesen. Die Rechercheberichte R8 bis R10 nennen die Fälle, in denen Suchmaschinen oder Webseiten ungefragt Ergebniszahlen anzeigten. Diese Zahlen wurden nicht verwendet.
- Die Auswahl in diesem Entwurf beruht nur auf Fragebögen, Methoden- und Rechtsdokumenten.

## 2 Ziel

Dieser Entwurf bereitet drei Erweiterungen vor:

1. Fragen für die sechs Bereiche ohne oder fast ohne eigene Frage und für die größten Lücken innerhalb der übrigen Bereiche, aus Erhebungen der Jahre 2024 bis 2026 (Abschnitt 11).
2. Aktualisierte Wählergruppen nach der Rückerinnerung an die Bundestagswahl vom 23. Februar 2025 (Abschnitt 7).
3. Eine Entscheidung über die ungleiche Sichtbarkeit von Gruppenvergleichen durch die Regel 100/5 (Abschnitt 8).

Das Profil bleibt ein Vektor getrennter Originalfragen. Keine Achsen, kein Gesamtwert, keine Perzentile, keine Lagerbezeichnungen.

## 3 Quellenklassen und Populationen

Jede Vergleichsquelle gehört genau einer Klasse an. Die Klasse bestimmt, was die Ansicht zeigen darf.

| Klasse | Beschreibung                                                          | Beispiele                                     | Erlaubte Anzeige                                                                                                                              |
| ------ | --------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Z      | Zufallsstichprobe mit Einzeldaten und dokumentiertem Design           | ESS                                           | Anteile, 95-%-Bereich nach Plan v2.2 Abschnitt 4, Wählergruppen nach Abschnitt 7                                                              |
| T      | Zufallsstichprobe, aber nur veröffentlichte Tabellen ohne Einzeldaten | Eurobarometer-Tabellen der EU-Kommission      | Anteile je Kategorie für Deutschland mit Basis und Feldzeit. Kein Bereich, solange kein Design veröffentlicht ist. Keine Wählergruppen        |
| Q      | Keine Zufallsstichprobe (Quote, Online-Panel)                         | OECD Risks that Matter, ifo Bildungsbarometer | Keine Zahlen, bis Steven Vergleiche mit nicht zufallsbasierten Stichproben grundsätzlich zulässt. Dann nur mit Kennzeichnung und ohne Bereich |

Regeln für Populationen:

- Jeder Vergleich nennt seine Population. ESS: Menschen ab 15 Jahren in Privathaushalten unabhängig von der Staatsangehörigkeit. Eurobarometer: Staatsangehörige von EU-Staaten ab 15 Jahren mit Wohnsitz in Deutschland. Andere Quellen nach ihrer Dokumentation.
- Populationen verschiedener Quellen werden nie zusammengelegt, gemittelt oder gegeneinander verrechnet. Dasselbe gilt für verschiedene Runden derselben Quelle.
- Fehlende Wählergruppen schließen eine Quelle nicht aus. Ein Bevölkerungsvergleich ohne Gruppen ist ein begrenzter, eigener Vergleichstyp.

## 4 Auswahlregeln

Eine Frage kommt als Kandidat in Betracht, wenn sie alle Bedingungen erfüllt:

1. Sie erfragt eine politische Präferenz oder ein politisches Prinzip. Wahrnehmungen, Vertrauen, Bewertungen der Regierung, Wissen und eigenes Verhalten scheiden aus.
2. Sie verkleinert eine dokumentierte Lücke aus der [Themenabdeckung v2.2](abdeckung-v2.2.md) (Spalte „Nicht erfasst“ oder einer der sechs Bereiche). Höchstens drei Fragen je engem Gegenstand.
3. Ihr deutscher Originalwortlaut, die vollständige Antwortliste einschließlich ausdrücklicher „weiß nicht“-Kategorien und der Fragekontext sind aus der Quelle oder ihrer offiziellen Dokumentation belegt.
4. Eine Begründung oder Prämisse im Fragetext, eingeblendete Beträge oder Informationen werden mit der Frage gezeigt und gekennzeichnet. Fragen mit wertender Prämisse scheiden aus.
5. Ihr Geltungsbereich ist gekennzeichnet: Entscheidung Deutschlands, der EU oder beider. Fragen zur EU-Ebene sind zulässig, wenn die Entscheidung Deutschland unmittelbar betrifft. Die Ansicht nennt dann „Entscheidung auf EU-Ebene“.
6. Die Feldzeit liegt in den Jahren 2024 bis 2026. Ältere Fragen nur mit ausdrücklicher Begründung und Zeitvermerk.
7. Der Zugang ist nach dem Quellenbericht R10 durch eine vorhandene Lizenz erlaubt (Klasse C) oder von Steven ausdrücklich freigegeben. Ausdrücklich verbotene Nutzungen (Klasse A) scheiden aus. Ungeklärte Bedingungen (Klasse B) werden vor jeder Datenverarbeitung geklärt.
8. Sie ist kein Zweig einer Zufallsvignette mit eigenem Nenner.

Die Auswahl ist ergebnisblind. Die Auswahlrolle liest nur Fragebögen, Methoden- und Rechtsdokumente. Enthält eine Quelle die Fragen nur zusammen mit Ergebnissen, prüft eine getrennte technische Rolle die Struktur nach Abschnitt 10 und gibt keine Verteilungen an die Auswahlrolle weiter. Keine Frage wird nach Sichtung ihrer Ergebnisse aufgenommen, entfernt, umgepolt oder einem anderen Bereich zugeordnet.

## 5 Historische und aktuelle Vergleiche

- Jeder Vergleich nennt Quelle, Ausgabe oder Welle, Feldzeit, Population, Stichprobenart und Modus.
- Historische Vergleiche (ESS 2010 bis 2023) und aktuelle Vergleiche (2024 bis 2026) stehen getrennt und gekennzeichnet nebeneinander, wenn eine Frage in beiden vorkommt. Sie werden nicht gemittelt und nicht als Entwicklung gedeutet. Keine Aussagen über Veränderungen, keine Signifikanztests.
- Zeitbezogene Formulierungen („heute“, „schon jetzt“, „derzeit“) erhalten wie in v2.2 einen Hinweis auf den Bezugspunkt der damaligen Befragten.
- Kontextangaben trennen drei Ebenen: geltende Rechtslage mit Fundstelle und Stand, politische Vorschläge mit Urheber und Datum, gemessene Einstellungen. Vorschläge erscheinen nie als geltendes Recht.

## 6 Publikations- und Anzeigeregeln

- **Klasse Z:** unverändert nach Plan v2.2 Abschnitte 4 und 6 (mindestens 100 gültige Antworten, keine beobachtete Kategorie mit eins bis vier Fällen, 95-%-Bereiche).
- **Klasse T:** Die Strukturprüfung S1 zeigt, dass die Tabellen der Kommission je Frage eine Spalte für Deutschland, alle Kategorien einzeln und „Don't know“ als eigene Zeile enthalten, aber keine ungewichtete Basis je Frage, keine Gewichtungsvariable und keine Regel zu fehlenden Werten. Deshalb gelten diese Regeln:
  1. Nur Fragen, die laut Tabelle allen Befragten gestellt wurden („Base: All respondents“), aus Wellen mit persönlichem Interview in Deutschland. Gefilterte Fragen und Online-Befragungen (etwa Flash-Eurobarometer) scheiden aus.
  2. Als ungewichtete Basis gilt die Zahl der Interviews in Deutschland aus der Technischen Spezifikation derselben Welle. Die Ansicht nennt sie so: „Interviews in Deutschland laut Technischer Spezifikation“.
  3. Als Gewichtung gilt das in der Technischen Spezifikation beschriebene Verfahren. Die Ansicht nennt es und dass die Zusammenführung der Teilstichproben West und Ost nicht dokumentiert ist.
  4. Die Anteile beziehen sich wie in den Tabellen auf alle Befragten einschließlich „Weiß nicht“. Das unterscheidet sich vom ESS, wo der Nenner nur gültige Antworten enthält. Die Ansicht zeigt „Weiß nicht“ als eigene Zeile und nennt den anderen Nenner. Kein Umrechnen auf gültige Antworten.
  5. Die Tabellen speichern ganze Prozentpunkte. Die Ansicht zeigt sie ohne Nachkommastelle und nennt das.
  6. Der deutsche Wortlaut stammt aus dem deutschen Datenanhang der Kommission zur selben Welle. Die technische Rolle prüft ihn je Frage. Fehlt er dort, entfällt die Frage, bis die Rechte am Wortlaut geklärt sind.
  7. Je Frage gilt die jüngste Welle mit persönlichem Interview, in der die Tabelle eindeutig zur Fragenummer des deutschen Fragebogens passt.
  8. Die Werte überträgt die technische Rolle zweimal unabhängig. Beide Übertragungen müssen übereinstimmen. Kein 95-%-Bereich und keine selbst berechnete Unsicherheit ohne veröffentlichtes Design. Die Ansicht sagt das: Ein fehlender Bereich bedeutet keine Unsicherheit von null.
  9. Gliederungen aus Volume C, etwa nach Links-Rechts-Einstufung, gehören nicht zu diesem Plan.
- **Klasse Q:** keine Zahlen bis zu Stevens Grundsatzentscheidung.

## 7 Wählergruppen nach der Bundestagswahl 2025

- Quelle nur Klasse Z mit Rückerinnerung an die Zweitstimme. Wahlabsicht und Parteinähe sind andere Merkmale und bilden keine Wählergruppen im Sinne von v2.1.
- Gruppendefinition, Vorrang der Teilnahme an der Wahl, Prüfung der Codeinventare, Bilanz und Regel 100/5 wie im Gruppenvertrag v2.1. Ein neuer Gruppenvertrag v2.3 bindet die Parteiliste der neuen Erhebung vor jeder Dateneinsicht.
- Gruppen verschiedener Wahlen werden nicht verglichen oder als Entwicklung dargestellt.
- Kandidat ist ESS Runde 12, sobald Daten und deutscher Fragebogen veröffentlicht sind (Abschnitt 11). Bis dahin entsteht nichts.

## 8 Sichtbarkeit der Gruppenvergleiche

Von den Wählergruppenpaaren der Referenzen v2.2 tragen Zahlen: 6 von 43 bei Skalen von 0 bis 10, 22 von 45 bei vier Antwortstufen, 58 von 139 bei fünf und 10 von 63 bei sechs Kategorien. Grundlage sind nur die öffentlichen Status in `data/reference-v2.2/`. Kleine Gruppen und lange Skalen verlieren ihre Vergleiche häufiger, weil eine einzelne Kategorie mit eins bis vier Fällen die ganze Referenz sperrt. Welche Parteien zu welchem Thema erscheinen, hängt dadurch von Gruppengröße und Skalenlänge ab (V2-F14).

Optionen, keine davon ist beschlossen:

- **A Status quo.** Regel bleibt, die Ansicht nennt je Gruppe die Zahl der verfügbaren Vergleiche (seit dem 3. Oktober 2026 umgesetzt).
- **B Unterdrückung einzelner Zellen.** Die Referenz erscheint, Kategorien mit eins bis vier Fällen zeigen „unter 5 Fälle“. Weil Summe und übrige Anteile bekannt sind, ließe sich die Zelle zurückrechnen. B braucht deshalb eine zweite unterdrückte Zelle oder eine Begründung, warum das bei öffentlich verfügbaren ESS-Einzeldaten unerheblich ist.
- **C Andere Präzisionsregel.** Statt der Zellregel ein Kriterium für die Breite der 95-%-Bereiche. Jede Schwelle wäre eine neue Projektentscheidung und bräuchte eine Begründung vor Sichtung.

Empfehlung: A beibehalten, B und C in der Planprüfung bewerten lassen. Eine Änderung gilt erst nach Festschreibung und dann für alle Studien gleich.

## 9 Integration in das Antwortprofil

- Neue Fragen nutzen die vorhandenen Satzformen der [Profilregeln v1](profilregeln-v1.md) mit eigener Richtungstabelle je Frage.
- Neue Blockmuster nur für Originalblöcke mit gleicher Einleitung und Antwortliste. Neue Querbezüge nur, wenn dieser Plan sie vor der Festschreibung nennt.
- Fragen zur EU-Ebene tragen den Kontext „Entscheidung auf EU-Ebene“. Fragen mit eingeblendeten Informationen zeigen diese Informationen.
- Die Themenabdeckung wird nach der Aufnahme neu bewertet. Eine Lücke gilt erst als verkleinert, wenn eine Frage tatsächlich im Profil steht.

## 10 Rollen, Prüfungen und Freigaben

1. Auswahlrolle: ergebnisblind, liest nur Fragebögen, Methoden und Bedingungen.
2. Technische Rolle: prüft bei Klasse T die Struktur veröffentlichter Tabellen (Kategorien, Basis, Gewichtung, Fußnoten) und meldet nur ein festes Formular ohne Werte an die Auswahlrolle. Die Übertragung der Werte erfolgt erst nach Festschreibung.
3. Zwei getrennte Planprüfungen durch frische Prüfagenten: Methoden und Reproduzierbarkeit; Quellen, Konstrukte und Fairness. Danach Korrekturen und gezielte Nachprüfung.
4. Stevens Freigabe je Quelle. Die Entscheidungsvorlage nennt Empfehlung und Folgen.
5. Festschreibung mit Tag `analyseplan-v2.3`, danach Datenabruf, Ergebnisprüfung vor dem Export und ausdrückliche Exportentscheidung wie in v2.2.

## 11 Kandidaten

Grundlage: `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json` (37 Kandidaten) und `R9-erweiterung-sozial-wohnen-gruppen.json` (37 Kandidaten). Die Auswahl unten wendet die Regeln aus Abschnitt 4 an, ohne Kenntnis von Ergebnissen. Alle Kandidaten sind Forschungsentwürfe. Keiner ist in den Test aufgenommen.

### 11.1 Stufe 1: Eurobarometer-Tabellen der Kommission (Klasse T)

Voraussetzungen: Stevens Freigabe des Tabellenwegs, die Regeln aus Abschnitt 6 (Klasse T) und ein deutscher Wortlaut aus dem Datenanhang der Kommission oder eine Klärung der Rechte (Anfrage an das Eurobarometer-Team). Nach S1 sind alle Fragen der Wellen 104.1, 103.2 und 105.1 unten an alle Befragten gestellt und eindeutig zugeordnet. Für SE037 gilt die Welle 105.2 (12. März bis 1. April 2026, Frage QB2), für ST0350 und ST0359 die Welle 104.1, weil ihre Zuordnung in 105.2 unklar ist. SP557 (Welle 102.1) hat S1 nicht geprüft; die beiden SP557-Fragen bleiben bis zu einer Strukturprüfung zurückgestellt. Die deutschen Wortlaute stammen aus R6, das sie den GESIS-Fragebögen entnommen hat. Population: EU-Staatsangehörige ab 15 Jahren in Deutschland, persönliches Interview, „Weiß nicht“ nur spontan erfasst.

| Kandidat               | Bereich                                    | Welle, Feldzeit Deutschland             | Gegenstand                                                                             | Ebene                           | Hinweis in der Ansicht                                                 |
| ---------------------- | ------------------------------------------ | --------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------- |
| R8-EB-SE037-GSVP       | Außen-, Verteidigungs- und Friedenspolitik | EB 105.2, 12. März–1. April 2026        | gemeinsame Verteidigungs- und Sicherheitspolitik der EU-Mitgliedstaaten, dafür/dagegen | EU, Deutschland im Rat          | Entscheidung auf EU-Ebene                                              |
| R8-EB-SE037-GASP       | Außen-, Verteidigungs- und Friedenspolitik | EB 105.2, 12. März–1. April 2026        | gemeinsame Außenpolitik der Mitgliedstaaten der EU, dafür/dagegen                      | EU, Deutschland im Rat          | Entscheidung auf EU-Ebene                                              |
| R8-EB-ST0359-ZUS       | Außen-, Verteidigungs- und Friedenspolitik | EB 104.1, 9.–29. Oktober 2025           | Zusammenarbeit auf EU-Ebene bei Verteidigungsfragen verstärken, Zustimmung             | EU, Deutschland im Rat          | Entscheidung auf EU-Ebene                                              |
| R8-EB-ST0359-GELD      | Außen-, Verteidigungs- und Friedenspolitik | EB 104.1, 9.–29. Oktober 2025           | mehr Geld für Verteidigung „in der EU“, Zustimmung                                     | offen                           | Ebene offen: EU-Haushalt oder Summe der Mitgliedstaaten                |
| R8-EB-ST0350-2         | Außen-, Verteidigungs- und Friedenspolitik | EB 104.1, 9.–29. Oktober 2025           | EU-Finanzierung militärischer Ausrüstung für die Ukraine, Zustimmung                   | EU, Deutschland im Rat          | bereits beschlossene EU-Maßnahme                                       |
| R8-EB-SP564-QC5-UA     | Europäische Integration                    | EB 103.2, 19. Februar–10. März 2025     | Beitritt der Ukraine, sobald alle Bedingungen erfüllt sind, dafür/dagegen              | EU, Ratifikation in Deutschland | Bedingung im Fragetext                                                 |
| R8-EB-SP572-QB12-KI    | Medien und Digitalpolitik                  | EB 105.1, 5.–24. Februar 2026           | KI sorgfältig regulieren oder möglichst wenig einschränken, zwei Aussagen              | keine Ebene genannt             | –                                                                      |
| R8-EB-SP572-QB5-6      | Medien und Digitalpolitik                  | EB 105.1, 5.–24. Februar 2026           | Regulierung von Online-Plattformen stärken, Zustimmung                                 | EU mit Mitgliedstaaten          | Entscheidung auf EU-Ebene                                              |
| R8-EB-SP557-QA7-OA     | Bildung und Forschung                      | EB 102.1, 13. September–4. Oktober 2024 | Ergebnisse öffentlich finanzierter Forschung kostenlos online, Zustimmung              | keine Ebene genannt             | –                                                                      |
| R8-EB-SP557-QA7-GRENZE | Bildung und Forschung                      | EB 102.1, 13. September–4. Oktober 2024 | keine Grenze für wissenschaftliche Forschung, Zustimmung                               | keine Ebene genannt             | Prinzip, keine Maßnahme                                                |
| R9-21                  | Gesundheit und Pflege                      | EB 105.2, 12. März–1. April 2026        | gemeinsame EU-Gesundheitspolitik, dafür/dagegen                                        | EU                              | Entscheidung auf EU-Ebene, deckt nationale Gesundheitspolitik nicht ab |

Nicht vorgeschlagen, mit Grund nach Abschnitt 4: ST0350 Item 1 (zwei Gegenstände), ST0350 Item 4 (zwei Hilfearten), ST0350 Item 5 (Bewerberstatus von 2022, ersetzt durch SP564 QC5), ST0359 „bis dauerhaft gerechter Frieden herrscht“ (wertende Zielformel), ST0359 Beschaffung und Produktion (höchstens drei Fragen zum engen Gegenstand EU-Verteidigung: GSVP, Zusammenarbeit, Ausgaben), ST0939 Gegenzölle (Anlass im Fragetext), SE035 Item 5 („gerechte“ Besteuerung, wertend), SE037 digitaler Binnenmarkt (abstrakter Begriff), SP566 QE6 und QE4 sowie SP554 QB11 (Dringlichkeit oder Wichtigkeit ohne Gegenposition), SP568 QC9 (Wortlaut fehlt), SP546 QB4 von Februar 2024 (Prioritätenliste ohne Richtung).

Diese elf Fragen verkleinern Lücken nur auf EU-Ebene. Wehrdienst, deutscher Verteidigungshaushalt, deutsche Waffenlieferungen, Rüstungsexporte, Rundfunkbeitrag, IP-Adressen, Gesichtserkennung, Mindestalter für soziale Medien, Bildungsföderalismus, BAföG, Kita, Rente, Pflege, Mieten und Grundsteuer bleiben offen.

### 11.2 Stufe 2: ESS Runde 12 (Klasse Z), frühestens ab Januar 2027

Voraussetzungen: Veröffentlichung der Daten und des deutschen Fragebogens, ergebnisblinde Prüfung von Wortlaut, Parteiliste und Codes je Modus (persönliches Interview und Selbstausfüller), danach ein Gruppenvertrag v2.3.

- Aktuelle Referenzen für Profilfragen, die ESS12 wiederholt: laut R3 und R9 `gincdif`, `euftf`, `imsmetn`, `imdfetn`, `impcntr`, `hmsacld`, `vteurmmb`. Sie stehen getrennt neben den historischen Referenzen (Abschnitt 5).
- Wählergruppen nach der Rückerinnerung an die Bundestagswahl vom 23. Februar 2025 (Quellfragebogen A26 und A27). Der Bezug auf diese Wahl folgt aus dem Feldfenster und ist am deutschen Wortlaut noch zu prüfen.
- ESS12 enthält keine Präferenzfrage für die sechs Bereiche (R8 Abschnitt 7, R9 Abschnitt 6.1).

### 11.3 Stufe 3: Online-Quotenstichproben (Klasse Q), nur nach Stevens Grundsatzentscheidung

OECD Risks that Matter 2024 (Deutschland November bis Dezember 2024, 18 bis 64 Jahre, Online-Quote, Fragebogen nur englisch). Ohne Prämisse oder Begründung im Fragetext sind nur die Fragen Q19 g (Gesundheit), Q19 i (Renten), Q19 j (Langzeitpflege), Q19 f (Wohnen) und Q19 e (Mindestsicherung): Bereitschaft, 2 % des Einkommens zusätzlich für bessere Leistungen zu zahlen, als Mehrfachauswahl. Sie messen eine Zahlungsbereitschaft, keine Haltung zu einem deutschen Gesetz. Nicht vorgeschlagen: Q23 a (Prämisse), Q27 e (Kosten-Nutzen-Vorgabe), Q27 f (Zweckangabe), Q34 a und j (Begründung im Text, nach Informationsexperiment). Reuters Digital News Report 2025 und 2026 nur, wenn ein deutscher Wortlaut belegt ist.

### 11.4 Stufe 4: GESIS-Bestände, nur nach einer Ausnahme nach § 4

GLES Querschnitt 2025 Nachwahl q27e (Waffenlieferungen an die Ukraine), q27o (Waffen an Israel), q170 (Gesellschaftsdienst statt Wehrpflicht), q27i (Mietregulierung); GLES-Panel 2025/26 (Quotenstichprobe, Klasse Q) zu Verteidigungsausgaben, Wehrpflicht, Russland, Mindestlohn; Politbarometer 2024/25; ISSP 2024 „Digital Societies“; ZMSBw-Daten 2025. GLES q27k („Das Bürgergeld sollte deutlich abgesenkt werden.“) bezieht sich seit dem 1. Juli 2026 auf einen überholten Rechtsstand und wäre nur mit Zeitvermerk denkbar.

### 11.5 Nicht weiter verfolgt

SOEP (KI-Verarbeitung ausdrücklich untersagt), ifo Bildungsbarometer (Vertrag nur für wissenschaftliche Einrichtungen, Daten bis 2021), EIB (Veröffentlichung ohne Erlaubnis untersagt), ZQP (automatisiertes Lesen untersagt), Quellen, die Fragen nur mit Ergebnissen veröffentlichen (ZMSBw-Bericht, Berlin Pulse, Pew, DAK-Pflegereport, ver.di, SozialstaatsRadar), solange Steven sie nicht ausdrücklich zulässt.

## 12 Stopps

- Keine Quelle mit Klasse A. GESIS-Bestände bleiben gesperrt, bis Steven die Ausnahme nach § 4 geklärt hat.
- Fehlt für eine Quelle die Freigabe, bleibt ihr Bereich sichtbar als Lücke.
- Zeigt die technische Prüfung, dass eine Tabelle die Bedingungen aus Abschnitt 6 nicht erfüllt, entfällt die Frage ohne Ersatz aus derselben Quelle nach Ergebnissicht.
