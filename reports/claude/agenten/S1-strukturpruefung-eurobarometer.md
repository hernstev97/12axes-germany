# S1 – Strukturprüfung veröffentlichter Eurobarometer-Tabellen

Stand: 4. Oktober 2026 (Arbeit am 3. Oktober 2026 zwischen 23:10 und 23:40 UTC). Auftrag: `reports/claude/auftraege/S1-strukturpruefung-eurobarometer.md`. Ich bin die getrennte technische Rolle nach Entwurf `docs/analyseplan-v2.3.entwurf.md`, Abschnitte 4, 6 und 10. Branch `research/life-93-claude-20261003`, keine Commits.

Dieser Bericht enthält keine Anteile, Prozentwerte, Mittelwerte, Rangfolgen oder Aussagen über Ergebnisse. Die einzigen Zahlen aus Tabellen sind gewichtete und ungewichtete Fallzahlen für Deutschland bei Fragen an alle Befragten. Bei gefilterten Fragen gebe ich auch die Basis nicht aus, weil sie den Anteil der Filtergruppe verraten würde. Interviewzahlen, Feldzeiten und Seitenzahlen stammen aus Methodendokumenten.

Die maschinenlesbare Fassung mit allen 142 Einträgen und genau den verlangten Feldern steht in `reports/claude/agenten/S1-strukturpruefung-eurobarometer.json`. Das Skript, das sie erzeugt, ist `reports/claude/kontrollrechnung/s1_struktur.py`.

## 1 Kurzfassung

1. **Geprüft:** Volume A und Volume C (Datei für Deutschland) von sieben Erhebungen: Standard-Eurobarometer 104 und 105, Spezial-Eurobarometer 559, 564, 565 und 572, Flash-Eurobarometer 561. Je Frage oder Item ein Eintrag: 23 aus STD105, 24 aus STD104, 45 aus SP559, 11 aus SP564, 2 aus SP565, 2 aus SP572, 33 aus FL561.
2. **Was die Tabellen leisten.** Alle Volume-A-Tabellen haben eine Spalte DE für Deutschland gesamt, bei den persönlich erhobenen Wellen zusätzlich DEW und DEE. Jede Antwortkategorie steht einzeln, „Don't know“ immer als eigene Zeile. Zusammengefasste Kategorien („Total 'Agree'“ usw.) stehen zusätzlich, nicht statt der Einzelkategorien. Eine Zeile für Verweigerung gibt es nirgends. Die gewichtete Basis für Deutschland steht in Volume A („Total“) und Volume C („Weighted Base“). Bei allen geprüften Fragen an alle Befragten stimmen beide überein. Feldzeit, Modus und Interviewzahl für Deutschland finden sich in der Technischen Spezifikation derselben Welle.
3. **Was fehlt.** In keiner Volume-A- oder Volume-C-Tabelle der persönlich erhobenen Wellen steht eine ungewichtete Basis je Frage. Die Tabellen nennen nur „weighted“, keine Gewichtungsvariable. Die Technischen Spezifikationen beschreiben das Verfahren (Geschlecht × Alter, Region, Urbanisierungsgrad), aber nicht, wie die getrennt gezogenen Teilstichproben West und Ost für die Spalte DE zusammengeführt werden. Zum Umgang mit fehlenden Werten sagt keine Tabelle und keine Spezifikation etwas.
4. **Folge für Entwurf v2.3, Abschnitt 6 (Klasse T).** Der Entwurf verlangt für Zahlen die ungewichtete Basis und die verwendete Gewichtung. Beides fehlt in den Tabellen der Wellen 104.1, 105.2, 103.1, 103.2 und 105.1. Nach dem jetzigen Wortlaut dürfte die Ansicht für keine dieser Fragen Zahlen zeigen. Ob der Plan die Interviewzahl aus der Spezifikation als ungewichtete Basis bei „Base: All respondents“ zulässt und die Verfahrensbeschreibung als genannte Gewichtung gilt, ist eine Planentscheidung, keine technische.
5. **Flash-Eurobarometer 561** hat als einzige Erhebung ungewichtete und gewichtete Basis in der Tabelle. Es ist aber eine Online-Befragung aus Access-Panels mit Quoten, also keine Zufallsstichprobe (Klasse Q im Entwurf; R10 Abschnitt 5.2 Bedingung 2 nicht erfüllt). Ein Volume C für Deutschland ist nicht veröffentlicht, nur für Belgien.
6. **Zuordnung zum deutschen Fragebogen.** Eindeutig über R6 (gleiche Fragenummer in derselben Welle) für alle STD104-Einträge, für STD105 QB2 (SE037) und QB12_2 (ST0939 Item 2) sowie für SP564 QC3 und QC5, SP565 QD10 und QD11_2, SP572 QB5_6 und QB12. Unklar für STD105 QB6_2, QD2, QD3 und QE1, weil R6 die Fragenummern in 105.2 nicht nennt, und für alle Fragen aus SP559 und FL561.
7. **Trendfragen, jüngste Welle 2025/26.** SE037, SE040 Item 2, ST0350, ST0359 und ST0939 Item 2: 105.2. SE050: 105.2 (QE1, nur über den englischen Text zugeordnet), eindeutig zugeordnet in 104.1 (QF1). SE035 Item 5: nur 104.1 (QB2_5). SE035 Item 4 (Mindestlohn) und SE038 (Asylsystem, Außengrenzen) kommen in den Tabellen von 104.1 und 105.2 nicht vor.
8. **Deutscher Wortlaut bei der Kommission.** Der deutsche Datenanhang zu STD105 (Kommissionsdokument, deliverableId 105478) enthält deutsche Frage- und Antworttexte. In der einzigen geprüften Stichprobe (QB2.2) stimmt der Text wörtlich mit dem Zitat in R6 aus dem GESIS-Fragebogen ZA9144 überein. Das betrifft die offene Nutzung (5) in R10, Abschnitt 4.4.

## 2 Vorgehen

1. **Quellen.** Nur Dateien, die die Kommission ohne Anmeldung veröffentlicht: Eurobarometer-Schnittstelle (`europa.eu/eurobarometer/api/...`), Datensätze auf data.europa.eu, Dateien unter `webgate.ec.europa.eu/ebsm/api/public/odp/download`. Kein GESIS-Server, keine Einzeldaten, keine Anmeldung, keine Nachrichten. Alle Dateien liegen unter `outputs/claude/s1/` (von Git ausgeschlossen).
2. **Metadaten.** Aus der Eurobarometer-Schnittstelle habe ich nur Kennung, Titel, Feldzeit, Methode und Dateiliste ausgegeben, nie `descriptionEN` oder `keyFindings`. Aus data.europa.eu nur Lizenzfeld, Datum, Titel und Adresse der Distributionen, nie die Beschreibung.
3. **Skript.** `reports/claude/kontrollrechnung/s1_struktur.py` läuft in `outputs/claude/venv-readstat` (Python 3.11.15). Dort habe ich `openpyxl` 3.1.5 nachinstalliert. Das Skript ersetzt jede Zahl in einer Zelle durch `#`, ebenso Zahlen mit Prozentzeichen, mit Vorzeichen oder mit Dezimalstelle in Textzellen und die Signifikanzbuchstaben der Flash-Tabellen. Ausgenommen sind Zeilen, deren Beschriftung eine Basis bezeichnet und deren Werte wie Fallzahlen aussehen. Für das Formular gibt der Befehl `s1` von diesen Zeilen nur die Spalte DE aus, und nur bei Fragen an alle Befragten.
4. **Zeilen ohne Werte erkennen.** Um Basiszeilen, französische und englische Beschriftungen zu trennen, prüft das Skript intern nur den Typ der Werte einer Zeile (ganze Zahl oder Anteil zwischen 0 und 1) und das Zahlenformat der Zellen. Werte gibt es dabei nicht aus. Aufbau der STD- und SP-Tabellen: Je Kategorie folgt auf eine französisch beschriftete Zeile mit gewichteten Anzahlen eine englisch beschriftete Zeile mit Anteilen. Die erste Zahlenzeile „Total“ ist die gewichtete Basis.
5. **Technische Spezifikationen.** Die Datenanhänge der STD- und SP-Wellen enthalten keine. Ich habe sie in den Berichten gesucht und nur die Methodenseiten gelesen: Text mit maskierten Prozentwerten, die Ländertabelle als Bild. STD105: Bericht „Public opinion in the EU“, PDF-S. 269–273. STD104: nur im Bericht „First results“, PDF-S. 60–63; fünf weitere STD104-Berichte und der deutsche Länderbericht enthalten keine. SP559, SP564, SP565 und SP572: Anhang des jeweiligen Berichts. FL561: Bericht PDF-S. 83 und Datenanhang PDF-S. 3.

## 3 Dateien und Lizenz

Alle Distributionen tragen auf data.europa.eu das Lizenzfeld `COM_REUSE` („European Commission reuse notice“, Beschluss 2011/833/EU). Bedingungen nach Art. 6 Abs. 2: Quelle nennen, ursprüngliche Bedeutung nicht verzerren, Haftungsausschluss. Die Dateien selbst enthalten keine Versionsnummer. Als Fassung gilt das Datum der Distribution auf data.europa.eu.

| Erhebung | Datei (Originalname) | Distribution vom | Größe (Byte) | SHA-256 |
| --- | --- | --- | --- | --- |
| STD105 | Standard Eurobarometer 105 spring 2026_volume A.xlsx | 2026-05-08 | 1040049 | 59f30387f4320203cca395b0c82e64702f702a59a2567c89bfe8f59da4d6138f |
| STD105 | Standard Eurobarometer 105 spring 2026_volumes C_EU27.zip | 2026-05-08 | 90881915 | 5336dc15a61b1acc18cd71a531eb8b7672f1a8b00951ec9f51c546cc140ea218 |
| STD105 | darin: …_volume C_DE.xlsx | – | – | 36e89f4dc4cf0b99237e600ca3ae680f49390fe65a8d3874884c39e4c4e18891 |
| STD104 | Standard Eurobarometer 104_Autumn 2025_volume A.xlsx | 2026-02-11 | 990968 | 392cfc50a7d5ca5691a90ff08654bd6066446283e21f0555c4636dfa9a28e1fb |
| STD104 | Standard Eurobarometer 104_Autumn 2025_volumes C_AT-HR (1).zip | 2026-02-11 | 50471732 | e92968f73678bc14540bcbe4f998c50b8f05e0a67272c562fd4cca53f2c6e21d |
| SP559 | Investing in fairness_SP559_volume_A.xlsx | 2026-03-05 | 396158 | d3b8b4517ba661843cdf390aaa19fde198eec4144116ccb6b1784211f2b725dc |
| SP559 | Investing in fairness_SP559_volume_C.zip | 2026-03-05 | 21563605 | 56955dfc5144ebc23fe45f41365a4ca32ec12e2c7d45f7881777c998ca26d4b7 |
| SP564 | Attitudes towards EU enlargement_SP564_volume_A.xlsx | 2025-09-02 | 390849 | ac182dbbb2d7e8e641d19ccf4f249a26ad4f592b2b3c3ad5b4980dfbb2d2e579 |
| SP564 | Attitudes towards EU enlargement_SP564_volume_C.zip | 2025-09-02 | 24753961 | 2c126c5835d5b6d395d45cb871af53e15290687bb20c760f07fb714dac1030b0 |
| SP565 | Climate change_SP565_volume A.xlsx | 2026-03-05 | 363192 | 7cde5bf75e2c825369b5c3080b9b3f1c477735f156089203f2a31f34a6deb5b1 |
| SP565 | Climate_Change_SP565_volume_C.zip | 2026-03-05 | 36096096 | d52a472b3981c410d8ce19c4cf3f0ed754600f3024234cea49d40779f7e32857 |
| SP572 | Digital decade_SP572_volume_A.xlsx | 2026-06-17 | 403075 | 2b39770c4b9c9c870a50c9741fe13203ec0218ba3160055b3284a19d1f2a878d |
| SP572 | Digital decade_SP572_Volume_C.zip | 2026-06-17 | 41319222 | 18bdec7d5bb380e0bd1aaccef517cb2615b29c7a09da2b5c7cd2fcec0c6aab46 |
| FL561 | fl_561_volume_A.xlsx | 2025-06-18 | 501262 | a3af8956a55e3b28d436d4acf7a056264171d45de1efa03895e799ef63e99d0f |
| FL561 | fl_561_volume_C_BE.xlsx (nur Belgien, nicht ausgewertet) | 2025-06-18 | 345506 | a0bee84c9c60cd1435007ad3937a8e367243ba4eea3f7b4ca47c4104162ffeaa |

Die SHA-256-Werte der deutschen Volume-C-Dateien in den Zip-Archiven stehen je Eintrag in der JSON-Datei. Adressen der Downloads und Methodendokumente: Abschnitt 7.1.

## 4 Methodenangaben für Deutschland (Technische Spezifikation)

| Erhebung | Welle | Feldzeit DE | Interviews DE | Institut | Modus DE | Fundstelle |
| --- | --- | --- | --- | --- | --- | --- |
| STD105 | 105.2 | 12.03.–01.04.2026 | 1.515 | Mantle Germany (Verian) | persönlich (CAPI); CAVI nur in CY, DK, MT, FI, SE | Bericht 108404, PDF-S. 269–273 |
| STD104 | 104.1 | 09.10.–29.10.2025 | 1.516 | Mantle Germany (Verian) | persönlich (CAPI); CAVI nur in CY, DK, MT, NL, FI, SE | „First results“ 101601, PDF-S. 60–63 |
| SP559 | 103.1 | 10.01.–28.01.2025 | 1.504 | Mantle Germany (Verian) | persönlich (CAPI); CAVI nur in CZ, DK, MT, NL, FI, SE | Bericht 98737, PDF-S. 103–107 |
| SP564 | 103.2 | 19.02.–10.03.2025 | 1.510 | Mantle Germany (Verian) | persönlich (CAPI); CAVI nur in DK, MT, NL, FI, SE | Bericht 100304, PDF-S. 87–92 |
| SP565 | 103.2 | 19.02.–10.03.2025 | 1.510 | Mantle Germany (Verian) | persönlich (CAPI); CAVI nur in DK, MT, NL, FI, SE | Bericht 98729, PDF-S. 95–99 |
| SP572 | 105.1 | 05.02.–24.02.2026 | 1.513 | Mantle Germany (Verian) | persönlich (CAPI); CAVI nur in CY, DK, MT, NL, FI, SE | Bericht 106581, PDF-S. 73–77 |
| FL561 | Flash | 26.03.–02.04.2025 | 513 Städte, 520 Kleinstädte und Vororte, 401 ländlich | Ipsos European Public Affairs | online (CAWI), Online-Access-Panels mit Quoten nach Alter, Geschlecht, DEGURBA; teils Anwerbung über soziale Netzwerke | Bericht 98987, PDF-S. 83; Datenanhang 98958, PDF-S. 3 |

Population laut Spezifikation: Staatsangehörige von EU-Mitgliedstaaten ab 15 Jahren mit Wohnsitz im jeweiligen Land (FL561: „EU citizens, 15 years and over“). Stichprobe der persönlich erhobenen Wellen: geschichtete mehrstufige Zufallsauswahl nach NUTS-Region und DEGURBA, Startadresse per Zufallskoordinate, Random Route, Zufallsauswahl im Haushalt, bis zu vier Kontaktversuche. Gewichtung: Anpassung an die Grundgesamtheit nach Geschlecht × Alter, Region und Urbanisierungsgrad, für EU-Werte zusätzlich nach Bevölkerungsanteil 15+. FL561: „rim weighting“ nach Alter × Geschlecht.

Auffälligkeiten in den Methodendokumenten:

- SP559 schreibt die Feldzeiten in der Ländertabelle im Format Monat-Tag-Jahr („01-10-2025 – 01-28-2025“). Ich lese das als 10. bis 28. Januar 2025, passend zum Text „Between 9 January and 4 February 2025“.
- Die Kopfzeilen der Spezifikation im Bericht SP572 nennen „Special Eurobarometer 569“. Text und Welle (105.1, 5. Februar bis 1. März 2026) gehören zu SP572.
- STD105: Volume A nennt die EU-Feldzeit „12/3 - 5/4/2026“, Volume C für Deutschland „12/3 - 1/4/2026“. Die zweite stimmt mit der Spezifikation überein.

## 5 Einträge je Erhebung

Die Spalte „R10 5.3“ gibt die Bedingungen 1 bis 9 in dieser Reihenfolge an: e = erfüllt, n = nicht erfüllt, u = ungeprüft. Bedeutung der Punkte und Begründung: Abschnitt 6. „Basis gew. DE“ ist die gewichtete Basis für Deutschland aus der Tabelle. Eine ungewichtete Basis fehlt in allen STD- und SP-Tabellen. Kategorien stehen englisch und französisch in der Tabelle, hier nur englisch.

### 5.1 Standard-Eurobarometer 105 (Welle 105.2)

| Kennung (Tabelle) | Trend | Itemtext (englisch, gekürzt) | Kategorien einzeln | Zusammengefasst | Basis (Tabelle) | Basis gew. DE | Zuordnung | R10 5.3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QB2_1 … QB2_12 | SE037 | „What is your opinion …? … for it or against it.“ 12 Items: common foreign policy; common security and defence policy; EU's common trade policy; common European policy on migration; common European energy policy; enlargement; free movement; common EU health policy; common strategy to improve competitiveness; economic and monetary union, euro; common climate policy; digital single market | For; Against; Don't know | – | All respondents | 1515 | eindeutig | e e n n e e n e e |
| QB6_2 | SE040 Item 2 | „(OUR COUNTRY) should help refugees“ | Totally agree; Tend to agree; Tend to disagree; Totally disagree; Don't know | Total 'Agree'; Total 'Disagree' | All respondents | 1515 | unklar | e e n n u e n e e |
| QB12_2 | ST0939 Item 2 | „The EU should impose customs tariffs in response to defend its interests (…)“ | wie QB6_2 | wie QB6_2 | All respondents | 1515 | eindeutig | e e n n e e n e e |
| QD2_1 … QD2_5 | ST0350 | „The EU has taken a series of actions …“: sanctions (mit Zusatz zu immobilisierten russischen Vermögenswerten); financing military equipment; welcoming people fleeing the war; financial and humanitarian support; candidate status for Ukraine | wie QB6_2 | wie QB6_2 | All respondents | 1515 | unklar | e e n n u e n e e |
| QD3_3 … QD3_5 | ST0359 | support Ukraine until a lasting and just peace; cooperation in defence at EU level; more money for defence in the EU | wie QB6_2 | wie QB6_2 | All respondents | 1515 | unklar | e e n n u e n e e |
| QE1 | SE050 | „With which of the following two statements do you most agree?“ | The EU should have greater financial means given its political objectives; The EU's financial means match its political objectives; Don't know | – | All respondents | 1515 | unklar | e e n n u e n e e |

Die Items „Member States' purchase of military equipment should be better coordinated“ und „The EU needs to reinforce its capacity to produce military equipment“ (ST0359 in 104.1) stehen in den 105.2-Tabellen nicht. QD3 enthält in 105.2 außerdem zwei Bedrohungsaussagen und eine Aussage zum eigenen Energieverbrauch. Sie gehören nicht zu den von R6 genannten Items, deshalb habe ich keine Einträge für sie angelegt.

### 5.2 Standard-Eurobarometer 104 (Welle 104.1)

| Kennung (Tabelle) | Trend | Itemtext (englisch, gekürzt) | Kategorien einzeln | Zusammengefasst | Basis | Basis gew. DE | Zuordnung | R10 5.3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QB1_1 … QB1_11 | SE037 | wie 105.2 QB2, ohne „digital single market“; Item 2 heißt „A common defence and security policy among EU Member States“ | For; Against; Don't know | – | All respondents | 1516 | eindeutig | e e n n e e n e e |
| QB2_5 | SE035 Item 5 | „There should be a fair taxation of large technology companies in the EU“ | Totally agree; Tend to agree; Tend to disagree; Totally disagree; Don't know | Total 'Agree'; Total 'Disagree' | All respondents | 1516 | eindeutig | e e n n e e n e e |
| QB4_2 | SE040 Item 2 | „(OUR COUNTRY) should help refugees“ | wie QB2_5 | wie QB2_5 | All respondents | 1516 | eindeutig | e e n n e e n e e |
| QD2_1 … QD2_5 | ST0350 | wie 105.2 QD2; Item 5 lautet „Granting candidate status as a potential Member of the EU to Ukraine“ | wie QB2_5 | wie QB2_5 | All respondents | 1516 | eindeutig | e e n n e e n e e |
| QD3_3 … QD3_7 | ST0359 | support Ukraine until peace; co-operation in defence; more money for defence in the EU; better coordinated purchase of military equipment; capacity to produce military equipment | wie QB2_5 | wie QB2_5 | All respondents | 1516 | eindeutig | e e n n e e n e e |
| QF1 | SE050 | „With which of the following two statements do you most agree?“ | wie 105.2 QE1 | – | All respondents | 1516 | eindeutig | e e n n e e n e e |

### 5.3 Spezial-Eurobarometer 564, 565 und 572

| Erhebung | Kennung | Fragetext (englisch, gekürzt) | Kategorien einzeln | Zusammengefasst | Basis | Basis gew. DE | Zuordnung | R10 5.3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SP564 | QC3 | „Thinking about further enlargement of the EU, overall, would you say you are …“ | Very much in favour; Somewhat in favour; Not very much in favour; Not in favour at all; Don't know | Total 'In favour'; Total 'Not in favour' | All respondents | 1510 | eindeutig | e e n n e e n e e |
| SP564 | QC5_1 … QC5_10 | „… would you be in favour or opposed to them joining the EU once they have met all the membership conditions?“ Albania, Bosnia and Herzegovina, Georgia, Kosovo, Montenegro, North Macedonia, Republic of Moldova, Serbia, Türkiye, Ukraine | Strongly in favour; Fairly in favour; Fairly opposed; Strongly opposed; Don't know | Total 'In favour'; Total 'Opposed' | All respondents | 1510 | eindeutig | e e n n e e n e e |
| SP565 | QD10 | „… support or oppose the EU objective of becoming climate-neutral by 2050?“ (mit einleitender Erklärung der Klimaneutralität) | Totally support; Tend to support; Tend to oppose; Totally oppose; Don't know | Total 'Support'; Total 'Oppose' | All respondents | 1510 | eindeutig | e e n n e e n e e |
| SP565 | QD11_2 | „More public financial support should be given to the transition to clean energies even if it means subsidies to fossil fuels should be reduced or stopped“ | Totally agree … Totally disagree; Don't know | Total 'Agree'; Total 'Disagree' | All respondents | 1510 | eindeutig | e e n n e e n e e |
| SP572 | QB5_6 | „In the next ten years, the EU should cooperate with EU Member States to … strengthen the regulation of online platforms (…)“ | Totally agree … Totally disagree; Don't know | Total 'Agree'; Total 'Disagree' | All respondents | 1513 | eindeutig | e e n n e e n e e |
| SP572 | QB12 | „Thinking about artificial intelligence (AI), which of the following comes closest to your view?“ | zwei Aussagen (sorgfältig regulieren trotz Einschränkungen; so wenig Einschränkungen wie möglich trotz Risiken); Don't know | – | All respondents | 1513 | eindeutig | e e n n e e n e e |

Die SP564-Fragen QC3 und QC5 sind im englischen Fragebogen des Berichts Q3 und Q5 mit „ASK ALL“ und den Codes 1–4 und 999, ohne Verweigerungscode. Die Tabelle QC5T („% Total in favour“ über alle Länder) ist eine abgeleitete Übersicht. Für sie habe ich keinen Eintrag angelegt.

### 5.4 Spezial-Eurobarometer 559 „Investing in fairness“ (Welle 103.1)

Für SP559 gab es bisher keine Fragenliste (R9 6.7). Ich habe alle Blätter des Moduls QB aufgenommen. Keine Frage ist über einen deutschen Fragebogen zugeordnet (Zuordnung unklar, Bedingung 5 ungeprüft). Der Bericht enthält einen englischen Fragebogen (PDF-S. 108–118), nummeriert Q1 ff. statt QB1 ff.

| Kennungen | Inhalt laut Tabelle (englisch, gekürzt) | Kategorien | Basis (Tabelle) | Basis gew. DE |
| --- | --- | --- | --- | --- |
| QB1_1 … QB1_5 | „How worried … for the future of your household?“: skills devalued by digital change; lack of job opportunities; daily cost of living; paying rent or mortgage; fair salary | Very worried … Not at all worried; Don't know; 2 Summenzeilen | All respondents | 1504 |
| QB2_1 … QB2_8 | „… for the future of (OUR COUNTRY)?“: climate change; political polarisation; population ageing; affordability of housing; quality of public services; children in poverty; quality of education; too few escaping poverty | wie QB1 | All respondents | 1504 |
| QB4a_1 … QB4a_3 | Wichtigkeit von Unterstützung (Weiterbildung, Beratung) für die eigene Arbeitssituation | Very important … Not at all important; Don't know; 2 Summenzeilen | Respondents currently working | nicht ausgegeben (Filter) |
| QB4b_1, QB4b_3 | wie QB4a, künftige Arbeitssituation | wie QB4a | Respondents currently not employed, but able to work within the next 2 years | nicht ausgegeben (Filter) |
| QB4T_1, QB4T_2 | Zusammenfassung von QB4a und QB4b | wie QB4a | Respondents currently working or able to start working within the next two years | nicht ausgegeben (Filter) |
| QB5_1, QB5_2 | Bedeutung von und Bereitschaft zu Weiterbildung in digitalen Fähigkeiten | Totally agree … Totally disagree; Don't know; 2 Summenzeilen | Respondents currently working or able to work within the next two years | nicht ausgegeben (Filter) |
| QB6_1, QB6_2 | Arbeit und Weiterbildung für den grünen Wandel, persönliche Bedeutung | wie QB5 | wie QB5 | nicht ausgegeben (Filter) |
| QB7a | Wahrscheinlichkeit, ein „personal training budget“ zu nutzen | Very likely … Not likely at all; Don't know; 2 Summenzeilen | All respondents | 1504 |
| QB7b, QB7c, QB7bc | Gründe gegen die Nutzung (Mehrfachnennung bei c und bc) | 6 Gründe und Don't know | Respondents unlikely to use a ‘personal training budget’ (bei c: „for other reasons“) | nicht ausgegeben (Filter) |
| QB7d, QB7e, QB7de | Wofür das Budget genutzt würde | 7 Bereiche und Don't know | Respondents likely to use a ‘personal training budget’ (bei e: „for other reasons“) | nicht ausgegeben (Filter) |
| QB8_1 … QB8_3 | „… can people in (OUR COUNTRY) benefit from the following skills development programmes?“ | Very beneficial … Not beneficial at all; Don't know; 2 Summenzeilen | All respondents | 1504 |
| QB9_1 … QB9_5 | Zufriedenheit mit dem Zugang zu Kinderbetreuung, Langzeitpflege, bezahlbarem Wohnraum, Gesundheitsversorgung, sozialen Diensten | Very satisfied … Not at all satisfied; Don't know; 2 Summenzeilen | All respondents | 1504 |
| QB10_1 … QB10_5 | „Disadvantaged groups in (OUR COUNTRY) have sufficient access to …“ | Totally agree … Totally disagree; Don't know; 2 Summenzeilen | All respondents | 1504 |
| QB11_1 … QB11_3 | „… can young people of (OUR COUNTRY) benefit from the following programmes?“ | wie QB8 | All respondents | 1504 |

R10 5.3 für alle SP559-Einträge: e e n n u e n e e.

### 5.5 Flash-Eurobarometer 561 (online, Quotenstichprobe)

Alle Tabellen haben eine Spalte DE, die Basis „All“, ungewichtete und gewichtete Basis für Deutschland (beide 1434) und eine eigene Zeile „Don't know“. Zusammengefasste Kategorien gibt es nicht. Jede Zelle trägt Signifikanzbuchstaben aus paarweisen Ländervergleichen (Blatt „Note“). Sie sind Ergebnisse, das Skript maskiert sie. Ein Volume C für Deutschland fehlt. R10 5.3 für alle Einträge: e e e n u e n e n.

| Kennungen | Inhalt laut Tabelle (englisch, gekürzt) | Kategorien |
| --- | --- | --- |
| Q1 | Lebensqualität am Wohnort im Vergleich zu vor fünf Jahren | 5 Stufen von „Strongly improved“ bis „Strongly deteriorated“; Don't know |
| Q2_1 … Q2_8 | Wie groß ein Problem am Wohnort ist (Arbeitslosigkeit, Leerstand im Zentrum, Nachnutzung leerer Gebäude, bezahlbarer Wohnraum, Gentrifizierung, Integration, Armut, öffentliche Dienste) | An immediate and urgent problem; A problem to be dealt with in the future; Not much of a problem; Don't know |
| Q3 | Was am Wohnort am meisten verbessert werden müsste (bis zu drei Nennungen) | 11 Aspekte; Don't know |
| Q4_1 … Q4_4 | Wichtigkeit von Maßnahmen für die lokale Wirtschaft | Very important … Not important at all; Don't know |
| Q5_1 … Q5_5 | Nutzen von Maßnahmen für bezahlbares Wohnen am Wohnort (Neubau, Sanierung, Mietpreisbeobachtung und Mietzuschüsse „e.g. rent ceilings, rent vouchers“, Förderung von Erstkäufern, Begrenzung von Spekulation) | Benefit a lot; Benefit somewhat; Not benefit at all; Don't know |
| Q6, Q7, Q9 | Prioritäten für Investitionen (soziale Inklusion, Stadt-Land-Kooperation, Mobilität; jeweils bis zu drei Nennungen) | Listen von Bereichen; Don't know |
| Q8_1 … Q8_6 | Ob lokale Behörden genug für Klima und Umwelt tun | Taking enough action; Taking some action, but not enough; Not taking action at all; Don't know |
| Q10 | Eigene Beteiligung an lokalen Entscheidungen | Liste; Don't know |
| Q11_1 … Q11_3 | Aussagen zur Beteiligung an lokalen Entscheidungen | Totally agree … Totally disagree; Don't know |
| Q12 | Kenntnis von EU-Projekten in Städten | Yes; No, but I am aware of projects in other places; No, never heard of such investments; Don't know |

## 6 Bedingungen aus R10 Abschnitt 5.3

| Punkt | STD104, STD105, SP559, SP564, SP565, SP572 | FL561 |
| --- | --- | --- |
| 1 Spalte Deutschland gesamt | erfüllt: Spalte DE, zusätzlich DEW und DEE | erfüllt: Spalte DE |
| 2 Alle Kategorien einzeln, „Weiß nicht“ eigen, Zusammenfassungen nur zusätzlich | erfüllt. Eine Verweigerungszeile gibt es nicht. Ob der deutsche Fragebogen einen Verweigerungscode hat, ist ohne GESIS-Fragebogen nicht prüfbar. In den englischen Fragebögen von SP564, SP565 und SP572 haben die geprüften Fragen keinen. | erfüllt, gleiche Einschränkung |
| 3 Basis ungewichtet und gewichtet, Filterhinweis | nicht erfüllt: nur gewichtete Basis. Der Filter steht in jeder Tabelle („Base: …“). | erfüllt |
| 4 Gewicht für Deutschland gesamt | nicht erfüllt: Tabelle nennt nur „weighted“. Spezifikation beschreibt das Verfahren, nennt aber weder Variable noch die Zusammenführung von West und Ost. | nicht erfüllt: „rim weighting“ nach Alter × Geschlecht genannt; wie die drei DEGURBA-Teilstichproben für DE gewichtet werden, steht nicht da |
| 5 Kennung passt eindeutig zum deutschen Fragebogen | erfüllt, wo R6 dieselbe Fragenummer in derselben Welle belegt (Abschnitt 5). Ungeprüft für STD105 QB6_2, QD2, QD3, QE1 und alle SP559-Fragen. Interne Kennungen (SE037 usw.) stehen nicht in den Tabellen. | ungeprüft |
| 6 Feldzeit und Modus DE aus der Spezifikation derselben Welle | erfüllt (Abschnitt 4) | erfüllt; Modus online |
| 7 Rundung und fehlende Werte | nicht erfüllt: Anteile sind in ganzen Prozentpunkten gespeichert (Zahlenformat „0%“), gewichtete Anzahlen ganzzahlig. Den Umgang mit fehlenden Werten beschreibt nichts. | nicht erfüllt: Anteile als ganze Zahlen mit Format „0\%“; fehlende Werte nicht beschrieben |
| 8 Fassung und Lizenz der Datei | erfüllt: Datum der Distribution und Lizenzfeld auf data.europa.eu; keine Versionsnummer in der Datei | erfüllt, ebenso |
| 9 Gliederungsmerkmale Volume C | erfüllt (Liste unten) | nicht erfüllt: kein Volume C für DE |

Gliederungsmerkmale in Volume C (Deutschland), nur Beschriftungen. Die vollständige Liste je Frage steht in der JSON-Datei.

- **Alle STD- und SP-Wellen:** Gender; Age-4; Age-7; Generation; Education (End of); Level of diploma; Socio-professional category; Difficulties paying bills; Consider belonging to; Subjective urbanisation; Use of the Internet; Left-right political scale (zwei Fassungen, drei und fünf Gruppen); Image of the EU; Satisfaction with democracy (Land, EU); My voice counts (EU, Land); Current und Previous working status.
- **STD104 und STD105 zusätzlich:** Things are going in … (Land, EU, eigenes Leben, USA); Marital status; Household situation; Political interest index; Talk about European political matters; Lebenszufriedenheit; Wissen und Verständnis der EU; Lage und Erwartungen der Wirtschaft; Enlargement; More decisions at EU level; Haltungen zu Handel und gemeinsamer Außen- und Verteidigungspolitik; Feels like an EU citizen; Gemeinsamkeiten; Zufriedenheit mit der Reaktion auf die Invasion der Ukraine; Bedrohung; EU's financial means; STD104 außerdem Mediennutzung. Gliederung nach Bundesländern (NUTS 1).
- **SP559 zusätzlich:** Workforce status; Likeliness of using a ‘personal training budget’; Workplace satisfaction; Bundesländer.
- **SP564 zusätzlich:** Telefon- und Internetausstattung; Level of information about EU enlargement; In favour of EU enlargement; Bundesländer (Bremen ohne eigene Spalte).
- **SP565 zusätzlich:** mehrere Gliederungen nach Antworten des Klimamoduls (u. a. Supports the EU objective of climate neutrality by 2050); keine Bundesländer.
- **SP572 zusätzlich:** Gliederungen nach Antworten des Digitalmoduls (u. a. Nutzung generativer KI, Priorität der EU-Digitalpolitik); Bundesländer.

Viele Gliederungen beruhen auf Antworten zu anderen inhaltlichen Fragen, darunter die Links-Rechts-Einstufung. Nach R10 5.3 Punkt 9 wäre jede Darstellung nach solchen Gruppen eine neue Vergleichsform mit eigenem Plan.

## 7 Nachweise

### 7.1 Geöffnete Quellen (3. Oktober 2026, UTC)

| Uhrzeit | Quelle | Gelesen |
| --- | --- | --- |
| 23:11:10 | `https://data.europa.eu/api/hub/search/search?q=…&filter=dataset` (sieben Suchen) | nur Kennung und Titel |
| 23:11:24 | `https://europa.eu/eurobarometer/api/survey/get/latest?nb=5000` | Kennung, Referenz, Titel, Typ, Datum |
| 23:11:41 | `https://europa.eu/eurobarometer/api/survey/get/one?id=` 3613, 3378, 3223, 3413, 3472, 3682, 3368 | Feldzeit, Methode, Dateiliste; keine Beschreibung, keine „keyFindings“ |
| 23:12:27 | `https://data.europa.eu/api/hub/search/datasets/` s3613_105_2_std105_eng, s3378_104_1_std104_eng, s3223_103_1_sp559_eng, s3413_103_2_sp564_eng, s3472_103_2_sp565_eng, s3682_105_1_sp572_eng, s3368_fl561_eng | Lizenzfeld, Datum, Titel und Adresse der Distributionen |
| 23:12:42–23:14:09 | 14 Volume-Dateien über `https://webgate.ec.europa.eu/ebsm/api/public/odp/download?key=…` (Schlüssel je Datei in der Tabelle unten) | nur über das Skript |
| 23:17:59–23:18:10 | Datenanhänge über `https://europa.eu/eurobarometer/api/deliverable/download/file?deliverableId=` 105497, 105478, 101962, 102000, 98734, 100331, 99200, 105242, 98958 | Suche nach Methodenseiten; FL561 S. 3; STD105 deutsch eine Seite (QB2.2) mit maskierten Zahlen |
| 23:19:16–23:19:51 | Berichte deliverableId 105699, 102474, 98737, 100304, 98729, 106581, 98987 | nur Methodenseiten und, bei den Spezialberichten, englische Fragebogenseiten |
| 23:20:13–23:20:25 | Berichte deliverableId 108404 (STD105) und 102796 (STD104) | STD105 PDF-S. 269–273; STD104 ohne Spezifikation |
| 23:21:23–23:21:43 | STD104-Berichte deliverableId 102762, 102657, 102690, 102658 | Stichwortsuche, keine Spezifikation |
| 23:22:06–23:22:13 | STD104 „First results“ 101601, deutscher Länderbericht 102221 | 101601 PDF-S. 60–63; 102221 Stichwortsuche ohne Treffer |
| 23:23–23:30 | Ländertabellen der Spezifikationen als Bild: STD105 S. 270, STD104 S. 61, SP559 S. 104, SP564 S. 89, SP565 S. 96, SP572 S. 74 | Zeilen DE |

Schlüssel der Volume-Downloads: STD105 A `99134D6EF7DB334B8485DC4C0535E9C2`, C `F37005D0B7445A4268A21D4CE263E7B5`; STD104 A `A68C45C80315C6F37BBA366C32491DED`, C `DDA20686614BC23149BB026644CD55FE`; SP559 A `19C1574873817FA6CD36AB5F7B353252`, C `57426E4B5D06F09B50EF3E9E246C748C`; SP564 A `3BBC7C4BE8F1D434E8FCA249D58C82F1`, C `A4FD250EB72B101560A330A33D58564F`; SP565 A `043B2EC6D4E37AF8F80BD166BA4D1BA8`, C `7C7CAC2F6119759D1D47D65EE0F84CF4`; SP572 A `79B2D3656CA05298FADEA3936925DA81`, C `9CDD5627F7B9A806EBC89FADDF1978B8`; FL561 A `ECDAAF3786E52173F72D55C44F652F84`, C_BE `B51542D1FA905BDFCFCFF79B5A2D8A4E`. Größe und SHA-256 der Methodendokumente stehen in `outputs/claude/s1/meta/download_log.tsv`.

### 7.2 Ausgeführte Befehle (Kurzform)

- `curl` für Schnittstellen und Downloads; Ausgabe der Metadaten mit kleinen Python-Filtern (nur die in 7.1 genannten Felder).
- `uv pip install --python outputs/claude/venv-readstat/bin/python openpyxl`.
- `python s1_struktur.py sheets|content|dump|inv` für maskierte Strukturausgaben; `python s1_struktur.py s1 reports/claude/agenten/S1-strukturpruefung-eurobarometer.json` für das Formular.
- `pdfinfo`, `pdftotext -layout` seitenweise mit Stichwortsuche und Maskierung von Prozentwerten; `pdfimages -list`; `pdftoppm` für sechs Seiten mit Ländertabellen.
- `sha256sum`, `stat`.

### 7.3 Grenzen

1. Den deutschen GESIS-Fragebogen habe ich nicht geöffnet. Jede eindeutige Zuordnung stützt sich auf R6. Die internen Kennungen stehen in keiner Kommissionstabelle.
2. Geprüft habe ich nur Volume A und die deutschen Dateien aus Volume C. Volume AA, AP, AAP, B, BP und D habe ich nicht geöffnet.
3. Die Ländertabellen der Spezifikationen sind Bilder. Ich habe die Zeilen für Deutschland vom Bild abgelesen. Ein Ablesefehler ist möglich. Die Werte stimmen mit R6 Abschnitt 4 überein, soweit R6 dieselben Wellen nennt.
4. Beim Suchen der Methodenseiten habe ich die ersten Zeilen benachbarter Berichtsseiten ausgegeben. Dabei erschienen Bruchstücke von Ergebnissätzen auf EU-Ebene (STD104-Berichte, SP565 PDF-S. 94, SP572 PDF-S. 72). Eine frühe Strukturausgabe zeigte für FL561 Q5_3 die Signifikanzbuchstaben, bevor ich die Maskierung erweitert habe. Eine Typprüfung zeigte für eine FL561-Zeile, in wie vielen Länderspalten der Wert über 1 liegt, ohne Bezug auf Deutschland. Nichts davon habe ich verwendet oder hier wiedergegeben.
5. Die Prüfung des deutschen Datenanhangs beschränkt sich auf eine Seite (STD105, QB2.2). Ob alle deutschen Datenanhänge vollständige Feldwortlaute enthalten, ist offen.
6. Die Zuordnung der französischen und englischen Beschriftungen beruht auf dem Zeilenaufbau. Das Skript meldet Abweichungen von der Paarung, es gab keine.
7. Die gewichtete Basis bei gefilterten Fragen ist vorhanden, aber nicht ausgegeben. Ob die Auswahlrolle sie sehen darf, sollte der Plan festlegen.
8. Die Spezifikation von STD104 fand ich nur im Bericht „First results“, nicht im Hauptbericht.

### 7.4 Modell

Claude Opus 5.5 laut Laufzeit (`claude-opus-5-5[1m]`), getrennter Subagent in der technischen Rolle.

### 7.5 Bestätigung

Dieser Bericht und die JSON-Datei enthalten keine Anteile, Prozentwerte, Mittelwerte, Rangfolgen, Signifikanzangaben oder Aussagen über Ergebnisse. Zahlen aus Tabellen sind nur die gewichteten und ungewichteten Basen für Deutschland bei Fragen an alle Befragten.
