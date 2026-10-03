# R7 – Weitere Quellen außerhalb von GESIS

Stand: 3. Oktober 2026, Recherche etwa 20:55–21:40 UTC. Auftrag: `reports/claude/auftraege/R7-weitere-quellen.vollstaendig.md` mit dem gemeinsamen Teil zur Alternativen-Recherche. Ausgangsstand laut Auftrag: Commit `e9898fb`.

Dieser Bericht prüft Quellen, Zugangswege und Nutzungsbedingungen. Er ist keine Validierung, keine Dimensionsprüfung und keine Rechtsauskunft. Ein Bereich ist hier eine Suchgliederung aus `docs/abdeckung-v2.2.md`, keine Messdimension. „PDF-S.“ meint die physisch gezählte PDF-Seite; gedruckte Seitenzahlen weichen teils ab.

## 1. Kurzfassung

1. **Keine geprüfte Quelle außerhalb von GESIS schließt eine der sechs Lücken sofort und rechtlich sauber.** Jeder Quelle fehlt mindestens eines: ein öffentlicher, frei nutzbarer deutscher Originalwortlaut, Einzeldaten ohne KI-Sperre oder Vertragsbindung, eine Zufallsstichprobe.
2. **OECD Risks that Matter (RTM) ist inhaltlich die breiteste Quelle.** Die Runden 2022 und 2024 enthalten Präferenzfragen zu Rente, Gesundheit, Langzeitpflege, Wohnen, Bildung, Steuern, Mindestlohn und Arbeitszeit. Dagegen stehen eine Online-Quotenstichprobe nur für 18- bis 64-Jährige, ein nur englisch veröffentlichter Fragebogen, Mikrodaten nur auf E-Mail-Anfrage und Nutzungsbedingungen, die ich nur als Auszug kenne. Mehrere Fragen folgen auf Informationsexperimente oder tragen eine Begründung im Fragetext.
3. **Das UK Data Service sperrt KI-Werkzeuge ausdrücklich.** Die Endnutzerlizenz (Fassung 16.00w, PDF von April 2026) verbietet in Ziffer 5.5 „Online Data Tools“ einschließlich KI-Werkzeugen ohne schriftliche Erlaubnis. Das betrifft die Eurofound-Daten und jede andere Quelle, die über das UK Data Service verteilt wird. Das GESIS-Problem ist also kein Einzelfall.
4. **ESS12 bringt für die sechs Bereiche nichts.** Deutschland nimmt teil (Erhebung durch Verian). Die Erstveröffentlichung ist laut ESS für Januar 2027 geplant. Die deutsche Fassung ist nicht abrufbar (HTTP 404). Die Rotationsmodule behandeln Wohlbefinden und Zuwanderung, die Klimafragen im Kern sind Wahrnehmungen. ESS13 (Feld 2027/28) bekommt ein Wohlfahrtsmodul mit einer vorgeschlagenen Abwägung zwischen Militär- und Sozialausgaben.
5. **Pew lässt sich ergebnisblind nicht prüfen.** Deutschland wird per Telefon (Zufallsstichprobe, 2025: 1.006 Interviews) befragt. Öffentliche Fragetexte gibt es nur in Topline-Dokumenten mit Ergebnissen, Datensätze nur mit Konto und Zustimmung zu Bedingungen. Einen öffentlichen deutschen Fragebogen habe ich nicht gefunden.
6. **Die EIB-Klimabefragung hat frei ladbare Einzeldaten, aber restriktive Bedingungen.** Die Nutzungsbedingungen der EIB-Website untersagen Veröffentlichung und Bearbeitung ohne schriftliche Erlaubnis. Es gibt nur englische Fragebögen, keine Parteifrage und eine Online-Quotenstichprobe. Inhaltlich geht es um Klima, also einen vorhandenen Bereich.
7. **Mehrere scheinbare Alternativen liegen doch bei GESIS.** Die Einzeldaten der ZMSBw-Bevölkerungsbefragung (Verteidigung) und der Umweltbewusstseinsstudie des UBA sind im GESIS-Archiv. Der ZMSBw-Bericht trägt „© ZMSBw 2025“, der UBA-Bericht nennt keine Lizenz.
8. **Das ifo Bildungsbarometer passt inhaltlich zur Bildungslücke.** Daten gibt es nur für 2014–2021, nur über einen projektbezogenen Nutzungsvertrag mit dem EBDC und nur für wissenschaftliche Zwecke. Die Stichproben stammen aus Online-Access-Panels. Deutsche Wortlaute stehen in den Codebüchern, die erst mit dem Vertrag zugänglich sind.
9. **Das Soziale Nachhaltigkeitsbarometer (Ariadne/RIFS) ist die einzige gefundene Quelle mit öffentlichen deutschen Fragebögen und Zufallsrekrutierung außerhalb von GESIS.** Es deckt Lücken innerhalb des Bereichs Klima ab, etwa Tempolimit und CO₂-Preis (2023), nicht die sechs Bereiche. Es gibt keinen Lizenzvermerk; der Datenzugang für 2021–2023 ist ungeklärt; die Reihe endete 2023.
10. **Ein lizenzrechtlich klarer Weg für deutsche Fragewortlaute besteht nur beim ESS** (Dokumentation unter CC BY-SA 4.0). Für alle anderen Quellen ist eine Erlaubnis nötig oder die Lage ungeklärt. Eine eigene Übersetzung englischer Fragen wäre kein Originalwortlaut und fiele unter die Projektregel, dass eigene oder umformulierte Fragen die Lücken nicht schließen.
11. **Für Außen-/Verteidigungs- sowie Medien-/Digitalpolitik habe ich außerhalb von GESIS keine nutzbare Quelle gefunden.** Diese Lücken sollten sichtbar bleiben.

## 2. Vorgehen, Abgrenzung und Ergebnisblindheit

Gelesen im Repository: `AGENTS.md`, `docs/project.md`, `docs/abdeckung-v2.2.md`, die Auftragsdateien, Abschnitte von R1–R3 zu ESS12, ZMSBw, ifo und GESIS sowie `docs/lizenzen.md`. Nicht gelesen: `data/raw/`, `data/local/`, `data/reference-*`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-*`. `docs/handbuch.md` habe ich nicht gelesen, weil der Auftrag keine Arbeit an Oberfläche oder sichtbaren Texten umfasst.

„Nicht über GESIS verteilt“ habe ich so geprüft: Wer stellt die Einzeldaten bereit, und wer veröffentlicht Tabellen? Bei ZMSBw, UBA und CSES liegt mindestens ein Teil bei GESIS oder stammt aus GESIS-Studien. Ich führe sie trotzdem auf, weil das für Stevens Entscheidung wichtig ist.

Ich habe keine Antwortverteilungen, Prozentwerte oder Ergebnisse recherchiert oder übernommen. Ergebnistabellen, Topline-Dokumente, Datenexplorer und die frei ladbaren EIB-Datensätze habe ich nicht geöffnet. Bei der EIB habe ich nur die HTTP-Kopfzeilen abgefragt. Ungewollte Berührungen mit Ergebnissen, nicht verwendet und hier nicht wiedergegeben:

- Die archivierte OECD-RTM-Programmseite listet Presseschlagzeilen mit Ergebnissen.
- Die Pew-Datensatzseite „Spring 2025 Survey Data“ zeigt Anrisstexte von Berichten mit Ergebnissen.
- Die archivierte Eurofound-Seite zu EQLS 2016 enthält einen Ergebnisabsatz zu Bewertungen öffentlicher Dienste.
- Die RWI-Seite zum Nachhaltigkeitsbarometer beginnt mit einem Ergebnissatz.
- Die UBA-Publikationsseite fasst Ergebnisse zusammen. Bei einer Stichwortsuche nach „GESIS“ im UBA-Bericht erschien auf PDF-S. 163 ein Absatz mit Ergebnissen anderer Studien.
- Eine Suchmaschinen-Zusammenfassung zur BZgA-Organspendebefragung nannte ungefragt Prozentwerte.
- Der ESS13-Modulantrag fasst auf PDF-S. 15 Literaturbefunde zusammen.

Werkzeugvorbehalt: Wörtliche Zitate stammen aus Rohtext (PDF-Extraktion mit `pdftotext`, direkt geladenes HTML oder Wayback-Rohkopien). Einige Seiten konnte ich nur über ein Abrufwerkzeug lesen, das Inhalte durch ein Hilfsmodell zusammenfasst. Solche Stellen sind mit „(Abrufwerkzeug, nicht wörtlich geprüft)“ markiert. Angaben, die nur aus Suchmaschinen-Zusammenfassungen stammen, sind mit „(nur Suchergebnis)“ markiert.

## 3. Quellen im Einzelnen

### 3.1 ESS Runde 12 und Ausblick auf Runde 13

**Zugang.** Die ESS ERIC stellt die Daten über das ESS Data Portal (Sikt) bereit, nicht über GESIS. Für Deutschland ist das nationale Team bei GESIS angesiedelt. Die deutsche Länderseite (europeansocialsurvey.org/about/country/germany) sagt wörtlich: „Der ESS wird in Deutschland von GESIS – Leibniz-Institut für Sozialwissenschaften verantwortet.“ und „Die Erhebung für die Runde 12 des ESS in Deutschland wird von Verian durchgeführt.“ Damit ist die deutsche Teilnahme an ESS12 belegt; R3 hatte sie nur vermutet. Laut `docs/project.md` nutzt Steven für Downloads ein ESS-Konto. Die im Data Portal angezeigten Bedingungen habe ich nicht gesehen.

**Bedingungen** (europeansocialsurvey.org/contact/disclaimer, abgerufen 20:57 UTC):

> „European Social Survey data is licensed under CC BY-NC-SA 4.0“
> „European Social Survey documentation is licensed under CC BY-SA 4.0“
> „The data are available without restrictions, for not-for-profit purposes.“
> „ESS ERIC recommends that ESS datasets are not made available on external websites. Instead, please link to datasets on the ESS Data Portal.“

Eine Regel zu KI-Systemen oder automatisierter Verarbeitung habe ich auf der Disclaimer-Seite nicht gefunden (Suche nach „artificial“, „AI“, „machine“, „automat“, „mining“). Das ist kein Beleg für eine Erlaubnis. Die Bedingungen im Data Portal hinter der Anmeldung kenne ich nicht.

**Deutschland, ESS12.**

- Feldzeit allgemein: „Round 12 fieldwork is expected to begin in September 2025 and must be completed by 15 May 2026.“ (ESS-Meldung vom 10.03.2025). Deutsche Feldtermine habe ich nicht gefunden.
- Modus: „sample units in each country have been randomly allocated to either complete a face-to-face interview or self-completion questionnaire (web and paper)“ (ESS-Meldung vom 30.09.2026).
- Gewichte: Poststratifikationsgewichte schon in der ersten Veröffentlichung (ebd.).
- Veröffentlichung: „expected to be published for the first time in January 2027“ (ebd.). Ursprünglich war November 2026 geplant (Meldung vom 12.01.2026). Laut Meldung vom 30.09.2026 nehmen 30 Länder teil, laut Meldung vom 12.01.2026 waren es 31.
- Population: Die deutsche Länderseite nennt für bisherige Runden alle „in Deutschland lebenden Personen, welche älter als 15 Jahre sind“, in Privathaushalten, „in einem strikten Zufallsverfahren ausgewählt“. Ihr Methodenabschnitt beschreibt noch CAPI, also den Stand vor ESS12. Eine deutsche Fallzahl für ESS12 ist nicht veröffentlicht.

**Fragebogen.** Englischer Quellfragebogen (SHA-256 `d5f768fa…`, identisch mit R3), Übersicht PDF-S. 1–2: Kern A1–A89b, Rotationsmodul C „Wellbeing“, Rotationsmodul D „Immigration“. Die deutsche Fassung unter `…/round12/fieldwork/germany/ESS12_questionnaires_DE.pdf` liefert HTTP 404. Gegenprobe: Der ESS11-Pfad liefert HTTP 200.

**Themenabdeckung.** Für die sechs Bereiche findet sich keine Präferenzfrage. Die Klimafragen im Kern sind Wahrnehmungen: A5 Ursache (PDF-S. 10), A7 „How worried are you about climate change?“ (PDF-S. 11). Militär kommt nur als Erwerbsstatus vor. Für Migration und `gincdif` verweise ich auf R3, Abschnitt 2.2.

**ESS13.** Laut ESS-Meldung vom 06.01.2025 enthält Runde 13 (Feld „late 2027 and early 2028“, nur Selbstausfüller) ein Wohlfahrtsmodul, das „new questions on welfare in the context of military spending, the deservingness of recipients, environmental subsidies“ aufnehmen soll. Der Modulantrag (PDF-S. 15) schlägt diese Frage vor:

> „N1 – Preferences for welfare expenditures over military defence expenditures. If the government had to choose between spending more on military defence at the cost of reducing social benefits and services, or spending more on benefits and services at the cost of reducing military defence, what should they do in your opinion?“ Skala 0 „increase spending on military defence a lot and decrease social benefits and services“ bis 10 „increase spending on social benefits and services a lot and decrease military defence“.

Das ist ein Antrag, kein endgültiger Fragebogen. Wann ESS13-Daten erscheinen, ist nicht angekündigt. Vermutung nach dem bisherigen Rhythmus: nicht vor 2029.

**CRONOS-3.** Das ESS-Online-Panel lief in elf Ländern ohne Deutschland (ESS-Meldung vom 21.07.2026: „Austria, Belgium, Czechia, Finland, France, Hungary, Iceland, Poland, Portugal, Slovenia, and the United Kingdom“).

### 3.2 OECD Risks that Matter (RTM)

**Zugang.** Die OECD stellt alles selbst bereit, nicht über GESIS. Die Live-Seiten auf oecd.org lieferten HTTP 403 (Cloudflare-Prüfung). Ich habe Wayback-Rohkopien genutzt. Auf der Datenseite „Risks that Matter data and methodology“ (Wayback 10.10.2025) stehen veröffentlichte „Collected Statlinks“ (Excel, Ergebnisse, nicht geöffnet), die englischen Kern- und Hintergrundfragebögen 2018–2024 und zum Zugang zu Einzeldaten:

> „To request access to the anonymised Public Use Microdata, please contact Valerie Frey (Valerie.FREY@oecd.org) and Pauline Fron (Pauline.FRON@oecd.org).“

Laut technischer Dokumentation hatten bis zum 2. Juni 2025 81 externe Forschende Zugang beantragt (OECD Working Paper Nr. 324, PDF-S. 8).

**Bedingungen.** Die Nutzungsbedingungen für die Mikrodaten habe ich nicht im Wortlaut gesehen. Das Working Paper fasst sie zusammen (PDF-S. 21–22): Nutzer müssen Reidentifikation verhindern und die Daten sichern; „users are prohibited from the presentation or publication of individual entries, even without direct reference to individual persons“; bei Reidentifikation sind die OECD zu informieren und Risiken zu mindern. Eine KI-Regel nennt diese Zusammenfassung nicht. Ob die vollständigen Bedingungen eine enthalten, ist offen.

Die allgemeinen OECD-Bedingungen (oecd.org/en/about/terms-conditions.html, Wayback 02.10.2026):

> „most OECD written content published as of 1 July 2024 is licensed under a Creative Commons Attribution BY 4.0 licence (CC BY 4.0). This licence permits users to reproduce, distribute and adapt (including translate) the content for any purpose without seeking authorisation from the OECD.“
> „Some OECD written content may be licensed under different terms. You should always check the copyright notice of the written content to confirm which licence applies.“
> Zu Daten: „Except where additional restrictions apply as stated above, you can extract from, download, copy, adapt, print, distribute, share and embed Data for any purpose, even for commercial use.“

Eine Regel zu KI oder automatisierter Verarbeitung enthält dieser Text nicht. Die Fundstellen für „Artificial intelligence“ auf der Seite sind nur Navigationslinks. Das Working Paper 324 steht ausdrücklich unter CC BY 4.0 (PDF-S. 2). Die Fragebogen-PDFs tragen keinen Lizenzvermerk. Der Kernfragebogen 2022 trägt auf jeder Seite den Vermerk „Restricted Use – À usage restreint“, obwohl die OECD ihn öffentlich verlinkt. Ob die CC-BY-Regel für die Fragebögen gilt, ist damit ungeklärt.

**Deutschland.** Deutschland ist seit 2018 in allen Runden dabei (Working Paper 324, Tabelle 3.1, PDF-S. 14: Länderliste 2018 mit Deutschland, danach „Same as …“).

- Feldzeit: 2024 „November to December“, 2022 „October to December“.
- Population: seit 2020 18–64 Jahre (2018: 18–70).
- Stichprobe: „The OECD RTM survey uses non-probability quota sampling“ (PDF-S. 18). Quoten für Geschlecht, Alter, Einkommen, Bildung und Erwerbsstatus.
- Rekrutierung: Online-Panels des Anbieters Bilendi, der in Deutschland eigene Panels hat (PDF-S. 17–18).
- Modus: online (CAWI).
- Gewichtung nach den Quotenmerkmalen (PDF-S. 18; Anhang B).
- Mindestfallzahl „1 000 respondents“ je Land und Welle (PDF-S. 14). Eine deutsche Fallzahl habe ich nicht gefunden.
- Sprache in Deutschland: Deutsch (Tabelle 3.2, PDF-S. 17). Die Übersetzung lieferte der Anbieter über die Firma Empower, „reviewed by mother-tongue OECD staff“ (PDF-S. 16).

Der Hintergrundfragebogen 2024 enthält die Wahlabsicht („If a national election were held tomorrow, for which party would you vote?“, Frage 35, PDF-S. 11) mit deutscher Parteiliste in Anhang A. Das ist eine Sonntagsfrage, keine erinnerte Zweitstimme.

**Deutscher Fragebogen.** Nicht veröffentlicht. Öffentlich sind nur die englischen Mastertexte. Für eine Anzeige deutscher Wortlaute müsste die OECD die deutsche Fassung herausgeben.

**Relevante Originalfragen (englisch, Kernfragebogen 2024).**

- Q18 (PDF-S. 6): „Do you think the government should be doing less, about the same, or more to ensure your economic and social security and well-being?“ Fünf Stufen von „much less“ bis „much more“ und „Can't choose“. Das ist eine allgemeine Sozialstaatspräferenz mit Bezug auf die eigene Person.
- Q19 (PDF-S. 7): „Would you be willing to pay an additional 2% of your income in taxes/social contributions to benefit from better provision of and access to:“, unter anderem b. Bildung, f. „Housing supports (e.g. social housing services, housing benefits, etc.)“, g. „Health services“, i. „Old-age pensions“, j. „Long-term care services for older people“, m. „I would not be willing to spend an extra 2% on any of these things“. Die Frage verbindet Präferenz und persönliche Zahlungsbereitschaft. Ob das als Politikpräferenz gelten soll, muss das Projekt entscheiden.
- Q20 (PDF-S. 7): „Should the government tax the rich more than they currently do in order to support the poor?“ (fünf Stufen und „Can't choose“). Gehört zu Wirtschaft und Verteilung.
- Q21 (PDF-S. 7): Fairness von Schenkungs- und Erbschaftsteuern. Das ist die Bewertung eines Prinzips, ein Grenzfall.
- Q22, Fassung für Deutschland (PDF-S. 8): „Suppose the current tax on inheritance were committed to be spent on a specific social programme. Would you prefer a higher, lower, or the same inheritance tax rate if the revenues were reserved (earmarked) for the following social outcome:“ e. Zugang zu und Bezahlbarkeit von Gesundheitsversorgung, f. dasselbe für Langzeitpflege, g. Unterstützung von Haushalten, die unter dem Klimawandel oder unter Klimaschutzmaßnahmen leiden, h. Unterstützung einkommensschwacher Haushalte.
- Q23 (PDF-S. 8): „Population ageing may lead to worker shortages … To what degree do you oppose or support the following measures …“, a. „Encouraging longer working lives“, c. „Increasing migration to bring more workers into the country“. Die Einleitung setzt eine Prämisse.
- Q27 (PDF-S. 10): Maßnahmen gegen Folgen der Digitalisierung, unter anderem a. „Investing more in university education and vocational training opportunities for young people“, c. „Investing more in digital infrastructure, such as the broadband network“, d. Steuer auf Roboter oder Technologieunternehmen, e. „Introducing a limit on (or lowering) working hours“, g. bedingungsloses Grundeinkommen, l. „Introducing trade tariffs to protect domestic industries“. Der Stamm verlangt ausdrücklich, Kosten und eigenen Nutzen abzuwägen.
- Q30 (PDF-S. 12): „To offset the economic consequences of climate change policies, governments should introduce or strengthen policies to:“, unter anderem e. Wohnkostenzuschüsse, g. „Increase the supply of social and affordable housing“, i. „Set limits on energy prices“, j. ÖPNV. Die Fragen sind an den Klimakontext gebunden.
- Q34 (PDF-S. 14), nach dem randomisierten Informationsexperiment Q31–Q33 (PDF-S. 12–13): unter anderem a. „Increase minimum wages as women are over-represented in low-wage jobs“ (Begründung im Fragetext), f. Führungsquoten, h. Kinderbetreuung, j. Rentenausgleich für Pflegezeiten. In Deutschland lief die Variante d. zur Entgelttransparenz. Nur die Kontrollgruppe ist ohne Informationsreiz.

Ausgeschlossen nach der Auftragsregel: Q1–Q17 (Sorgen, Wahrnehmungen, Bewertungen staatlicher Leistungen), Q24 (Vertrauen und Wahrnehmung zu KI in der Verwaltung), Q28 und Q32 (Bewertung der Regierung).

**Kernfragebogen 2022** (PDF-S. 6): Q18 „would you like to see the government spend less, spend the same, or spend more in each of the following areas?“ mit b. Bildung, f. Wohnen, g. Gesundheit, i. „Old-age pensions“, j. Langzeitpflege, k. öffentliche Sicherheit, l. ÖPNV. Fünf Stufen sowie „None“ und „Can't choose“. Q24 (PDF-S. 8) fragt nach Prioritäten der Regierung, darunter k. „Dealing with international security threats“. Die Fragen 46–47 liefen in Deutschland nach einem Informationsexperiment (PDF-S. 16–17).

**Bewertung.** RTM ist die einzige gefundene Quelle mit Präferenzfragen zu Rente, Gesundheit, Pflege und Wohnen zugleich. Für einen Vergleich mit dem bisherigen ESS-Profil gibt es drei schwere Einschränkungen: andere Population (18–64), nicht-probabilistische Online-Quote und kein öffentlicher deutscher Wortlaut.

### 3.3 Pew Research Center, Global Attitudes Survey

**Zugang.** Pew stellt die Daten direkt bereit. Die Datensatzseite „Spring 2025 Survey Data“ zeigt: „This content requires a Pew Research Center account.“ Für das Konto muss man den Terms of Use zustimmen. Ich habe nichts heruntergeladen.

**Bedingungen** (pewresearch.org/about/terms-and-conditions/, „Effective Date: 05/25/2018“, abgerufen etwa 21:00 UTC):

> Abschnitt 1: „you may access, print, copy, reproduce, cite, link, display, download, distribute, broadcast, transmit, publish, license, transfer, sell, modify, create derivatives of, or otherwise exploit the Content, provided that all copies display all copyright and other applicable notices … and provided further that you do not use the Content in any manner that implies … a Center endorsement …“ Bei Übersetzungen ist der Hinweis „Pew Research Center has published the original content in English but has not reviewed or approved this translation.“ Pflicht.
> „Under no circumstances may the Content be reproduced in principal part … or otherwise republished in its entirety or in principal part without the express written permission of the Center …“
> Abschnitt 3 verbietet: „engage in unauthorized spidering, ‚scraping,‘ or harvesting of content or personal information, or use any other unauthorized automated means to compile information“.
> Abschnitt 13 (Datensätze): Lizenz zu Nutzung und Veröffentlichung, sofern „any reproduction … of the Data is limited to excerpts“. Dazu kommen Pflichthinweis und Haftungsausschluss: „Pew Research Center bears no responsibility for the analyses or interpretations of the data presented here. …“

Eine ausdrückliche Regel zu KI-Systemen gibt es nicht. Abschnitt 3 betrifft das Sammeln von Inhalten der Website mit automatisierten Mitteln. Ob Pew darunter auch die Analyse mit KI-Werkzeugen fasst, lässt sich dem Text nicht entnehmen.

**Deutschland.** Aus der Pew-Methodendatenbank (JSON-Quelle der Seite „Country-Specific Methodology“, abgerufen etwa 21:05 UTC):

- 2025: „Telephone“, „Feb. 27-April 11, 2025“, Stichprobe „1,006“, Anbieter „Langer Research Associates“, Population „Adult population ages 18 and older“, Stichprobendesign „List-assisted random-digit-dial (RDD) probability sample of landline households (35% of sample) stratified by region (NUTS2), and RDD probability sample of mobile phone users (65% of sample)“, Gewichtung „Gender, age, education, region and probability of selection of respondent“, Sprache Deutsch.
- 2026: gleiches Design, „Feb. 9-April 16“, Stichprobe „1,004“.

**Fragebogen.** Öffentliche Fragetexte habe ich nur in Topline-Dokumenten gefunden, die Ergebnisse enthalten. Diese habe ich nicht geöffnet. Einen öffentlichen deutschen Fragebogen habe ich nicht gefunden. Ob die Datensatzpakete übersetzte Fragebögen enthalten, konnte ich ohne Konto nicht prüfen.

**Themenabdeckung.** Ergebnisblind nicht prüfbar. Die Berichtsliste auf der Datensatzseite nennt Themen wie KI, EU, internationale Zusammenarbeit und Klimawandel. Vermutung, ungeprüft: Viele internationale Pew-Fragen messen Sympathie, Vertrauen oder Bedrohungswahrnehmung und fielen damit nach der Auftragsregel heraus.

**Bewertung.** Die Stichprobe ist methodisch stark, eine Zufallsstichprobe per Telefon. Ohne Konto und ohne Toplines lässt sich aber weder die Frageliste noch eine deutsche Fassung prüfen. Parteivariablen im Datensatz habe ich nicht geprüft.

### 3.4 Europäische Investitionsbank (EIB), Climate Survey

**Zugang.** Die EIB stellt alles direkt bereit. Die Ressourcenseite (eib.org/en/surveys/climate-survey/all-resources) listet je Ausgabe „Methodology“, „Questionnaire“, „Dataset of full results“ und „Individual dataset of results“. Die Einzeldaten 2024–2025 (`eib-individual-data-2024-2025.xlsx`) liefern ohne Anmeldung HTTP 200 mit 15.301.854 Byte. Ich habe nur die Kopfzeilen abgefragt, nicht die Datei.

**Bedingungen** (eib.org/en/terms-of-use.htm, abgerufen etwa 21:10 UTC):

> „You may not modify, publish, transmit, display, participate in the transfer or sale, create derivative works, or in any way commercially exploit the content of this website without the express prior written permission of EIB and/or the copyright owner or except as otherwise expressly permitted under copyright law.“

Eine eigene Lizenz für die Datensätze habe ich nicht gefunden, ebenso keine Regel zu KI oder automatisierter Verarbeitung.

**Deutschland.**

- Ausgabe VII (Methodik-Datei der EIB): Fragebogen „Adaptation to climate change“, Feld „August 6th to August 23rd, 2024“, „online (computer, tablet or mobile)“, „Respondents were randomly selected from nationally representative panels“, „quota method“, Gewichtung nach „gender, age, occupation, and region“, Population 15 Jahre und älter, Deutschland 1.008 Befragte auf Deutsch.
- Ausgabe VI (PDF-S. 1): „August 7th to September 4th, 2023“, Deutschland 1.000.

**Fragebogen.** Es gibt nur englische Fassungen. Die DOCX von Ausgabe VII nummeriert automatisch; die Nummern unten habe ich aus der Reihenfolge und den Verweisen „11bis“ und „If Q16=1 or 2“ erschlossen. Ausgabe VI ist als „Public“ markiert.

**Relevante Fragen.**

- VII, Frage 2: „What do you think is the best way for your country to address climate change?“ (Vorrang Minderung, Vorrang Anpassung, gleichrangig).
- VII, Frage 18: „Who do you think should bear the cost of climate change adaptation?“
- VII, Frage 19: „Do you think that your country should pay more to help the most vulnerable developing countries to adapt to the impacts of climate change?“ Das berührt die Entwicklungsfinanzierung, also nur am Rand die Außenpolitik.
- VI Q14 (PDF-S. 5): zwei Gegensatzpaare, etwa „Your government should address climate change without affecting your personal budget“ gegenüber „… even if it affects your personal budget“.
- VI Q17 (PDF-S. 5): finanzieller Ausgleich an Entwicklungsländer, mit der Vorbemerkung „Your country has emitted a significant amount of CO2 … and is responsible for part of the climate change …“.
- VI Q21 (PDF-S. 6): drei Steuermodelle. Jede Antwortvorgabe enthält eine Zielbegründung, etwa „The goal is to make sure that everyone pays their fair share to address the climate crisis.“ Das ist eine einseitige Begründung im Fragetext und für ein neutrales Profil problematisch.

**Bewertung.** Die Fragen betreffen vor allem Klima, also einen vorhandenen Bereich. Die Quotenstichprobe ist online, es gibt keine Parteifrage und damit keine Wählergruppen. Bedingungen und Sprache sperren die Wortlautanzeige ohne Erlaubnis.

### 3.5 Eurofound und das UK Data Service

**Zugang.** Eurofound-Seiten lieferten HTTP 429, daher Wayback-Rohkopien. Seite „About Eurofound's surveys“ (Wayback 20.05.2026):

> „Eurofound's survey datasets are made available no later than two years after fieldwork completion. The Eurofound datasets are stored with the UK Data Service (UKDS) … The data are available free of charge to those who intend to use them for non-commercial purposes. Requests for use for commercial purposes will be forwarded to Eurofound for authorisation.“
> „All questionnaires are made available upon completion of the survey fieldwork.“
> „The methodology and questionnaires used in Eurofound's pan-European surveys are freely available for use by other researchers, subject to certain copyright conditions“.

**Bedingungen.** Eurofound-Rechtsseite (Wayback 25.07.2025):

> „The reuse of any information of this website is authorised for commercial and non-commercial purposes, under the following conditions: The re-user is obliged to acknowledge the source of the document. The original meaning or the message of the documents should not be distorted. …“

UK Data Service, End User Licence (`cd137-enduserlicence.pdf`, Fassung „CD137-EndUserLicence_16.00w“, PDF erstellt 17.04.2026), PDF-S. 5–6:

> Definition: „Online Data Tools: Any software, application, system or platform that operates via the internet or a cloud-based service and is used to process, analyse, manipulate or generate data and other types of content, including but not limited to tools that employ ‚artificial intelligence' (AI) technologies, including generative AI technologies …“
> Ziffer 5.5: „To abstain from using any Online Data Tools in connection with your use of the Data Collection(s), unless explicit written permission is granted by the Data Service Provider.“

Folgerung ohne Rechtsauskunft: Cloudbasierte KI-Agenten wie Codex oder Claude fallen nach dem Wortlaut unter diese Definition. Wer UKDS-Daten im Projekt so verarbeiten will, braucht eine schriftliche Erlaubnis. Das trifft alle Eurofound-Daten und jede andere über UKDS verteilte Studie.

**Deutschland, EQLS 2016** (Wayback-Kopie der Eurofound-Seite): Feld „September 2016 to February 2017 in the EU28“, Population ab 18 Jahren, „Multi-stage, stratified, random sample“, persönliche Interviews, Zielgröße „1,600 in Germany“, deutscher Fragebogen vorhanden. Die Seite betont „a considerable focus on public services“. Den Fragebogen selbst habe ich nicht geöffnet (HTTP 429). Vermutung: überwiegend Bewertungen und Lebensqualität, wenige Politikpräferenzen. Die Erhebung ist zudem zehn Jahre alt.

Die Eurofound-E-Befragung „Living and Working in the EU“ nutzt laut OECD Working Paper 324 (PDF-S. 12) „non-probability convenience and snowball sampling“. Ihren Fragebogen habe ich nicht geprüft.

**Bewertung.** Für die sechs Bereiche kaum ergiebig. Wichtig ist der Befund zur UKDS-Lizenz.

### 3.6 Erhebungen öffentlicher Stellen in Deutschland

Eine deutsche Bevölkerungsbefragung einer öffentlichen Stelle mit offener Lizenz und Präferenzfragen zu den sechs Bereichen habe ich nicht gefunden. Im Einzelnen:

**a) ZMSBw-Bevölkerungsbefragung (Bundeswehr), Forschungsbericht 139.**

- Daten: Laut Bericht stellt das ZMSBw die Befragungsdaten „der Forschung allgemein im Datenarchiv des GESIS zur Verfügung“ (PDF-S. 94). Die Einzeldaten unterliegen also den GESIS-Bedingungen.
- Rechte: Impressum (PDF-S. 2) „© ZMSBw 2025“, keine offene Lizenz.
- Design 2025 (Tabelle 13.1, PDF-S. 95): CAPI, Feld 11.04.–17.05.2025, Personen ab 16 Jahren in Privathaushalten, „Repräsentative, mehrfach geschichtete Zufallsstichprobe nach dem Random-Route-Verfahren“, 2.049 Nettointerviews, Ausschöpfung 50 Prozent, Ipsos GmbH. Gewichtet nach Alter, Geschlecht, Bildung und Ortsgröße (PDF-S. 95).
- Die Ergebniskapitel und damit die Fragewortlaute habe ich nicht geöffnet. Ob der Bericht vollständige Kategorien mit Basis zeigt, ist ungeprüft.
- Das ist methodisch das stärkste deutsche Instrument zu Verteidigung, das ich gesehen habe. Ein Weg außerhalb von GESIS führt nur über die veröffentlichten Tabellen; dafür bräuchte es eine Erlaubnis oder eine rechtliche Prüfung.

**b) Umweltbewusstseinsstudie 2024 (UBA).**

- Design: 2.552 Personen ab 18 Jahren, Herbst 2024, „PostDirekt-Verfahren“, „zufallsgesteuerte Auswahl“, gewichtet (UBA-Texte 01/2026, PDF-S. 18–19).
- Daten: Der Methodenbericht liegt „im GESIS-Archiv“ (PDF-S. 56). Die Einzeldaten haben laut Suchergebnis die Nummer ZA8973 (nur Suchergebnis; die GESIS-Seite lieferte HTTP 403).
- Rechte: Das Impressum (PDF-S. 4) nennt keine Lizenz.
- Inhalt: Klima und Umwelt, nicht die sechs Bereiche. Einen „Zeitreihenband … integrierter Datensatz“ hat das UBA verlinkt, ich habe ihn nicht geöffnet.

**c) ifo Bildungsbarometer (ifo Institut, LMU-ifo EBDC).** Quelle: ifo Working Paper 378 (2022), Wayback-Kopie.

- Population und Stichprobe: „representative opinion survey of the German voting-age population“, jährlich seit 2014, etwa 4.000 Befragte je Welle (2020: 10.000), „drawn from online access panels so that they match the German population with respect to age, gender, state, school degree, and employment status“ (PDF-S. 7–8). Bis 2017 kam eine Offline-Teilstichprobe hinzu, seit 2018 nur online. Anbieter: Kantar Public 2014–2019, Respondi 2020, Talk Online Panel 2021 (PDF-S. 8). Gewichte vorhanden.
- Inhalt: „around 25-35 substantive questionnaire items on preferences for various education policy topics, often with several randomized splits“ (PDF-S. 5). Schwerpunkte laut Tabelle 1 waren unter anderem Reformen, Lehrkräfte, Digitalisierung, Gleichstellung, Ungleichheit, Föderalismus 2020 und gesellschaftliche Herausforderungen 2021.
- Zugang (PDF-S. 9): „The research project must serve exclusively scientific purposes and must not pursue commercial goals.“ Codebücher enthalten „the original text of the survey questions and answer categories in German“. Laut EBDC-Seite ist ein projektbezogener Nutzungsvertrag nötig (Abrufwerkzeug, nicht wörtlich geprüft). Auf der EBDC-Seite habe ich als neueste Welle 2021 gesehen.
- Den Nutzungsvertrag selbst habe ich nicht gesehen; eine KI-Regel ist daher offen.
- Folge: Die Daten liegen nicht bei GESIS. Für eine öffentliche Website bleiben drei Fragen offen: ob ein öffentlicher Test als „scientific purpose“ gilt, ob deutsche Wortlaute gezeigt werden dürfen und ob neuere Wellen zugänglich werden.

**d) Soziales Nachhaltigkeitsbarometer der Energie- und Verkehrswende (RIFS Potsdam, Kopernikus-Projekt Ariadne, BMBF-gefördert).**

- Stichprobe: forsa.omninet, Rekrutierung „offline, das heißt per Telefon, über ein mehrstufiges Zufallsverfahren (ADM-Telefonstichproben-System)“ im Dual-Frame-Design, Befragung als CAWI oder per Set-Top-Box (Daten- und Methodenbericht 2021, PDF-S. 18–19).
- Population: „deutschsprachigen Personen ab 18 Jahren …, die das Internet nutzen“, in Privathaushalten (PDF-S. 19).
- Feld und Fallzahlen (Projektseite snb.ariadneprojekt.de): 2021 18.03.–12.04. mit 6.822 Befragten; 2022 23.03.–13.04. mit geteilter Stichprobe (Energie 3.305, Verkehr 3.310); 2023 17.02.–09.03. (Energie 3.267, Verkehr 3.276).
- Gewichtung: „Eine nachträgliche Gewichtung der Daten wurde nicht vorgenommen“ (2021, PDF-S. 21).
- Laufzeit: Laut Projektseite ist die Erhebung „mit Ende der derzeitigen Förderphase des Kopernikusprojekts Ariadne abgeschlossen“.
- Fragebögen: „Der Fragebogen ist frei zugänglich“ (PDF-S. 20). Die deutschen Fragebögen 2021, 2022 und 2023 sind als PDF verlinkt. Fragebogen 2023 (Stand Juli 2023):
  - AK12 (PDF-S. 12): energiepolitische Ziele, unter anderem „Ausstieg aus der Kernenergie“ und „Kohleausstieg bis 2030“, Skala „lehne ich stark ab“ bis „befürworte ich stark“ und „weiß nicht/keine Angabe“.
  - Block „First-Order-Belief“ (PDF-S. 38): „Bitte geben Sie an, inwieweit Sie die folgenden energie- und verkehrspolitischen Maßnahmen ablehnen oder befürworten.“ Items „Allgemeines Tempolimit von 120 km/h auf Autobahnen“, „Allgemeines Tempolimit von 30 km/h in Städten“, „Allgemeines Tempolimit von 80 km/h auf Landstraßen“, „CO2-Preis“ sowie Wind- und Solaranlagen im Wohnumfeld.
  - PKV3 Parteineigung und PKV3c Links-Rechts-Selbsteinstufung (PDF-S. 46).
- Rechte: Kein Lizenzvermerk im Fragebogen gefunden.
- Daten: Das FDZ Ruhr am RWI bietet nur die Wellen 2017–2019 an: „The data sets are available free of charge for scientific purposes as a Scientific Use File (SUF) Off-site.“ Einen Zugang zu den Wellen 2021–2023 habe ich nicht gefunden.
- Bewertung: Das ist kein Beitrag zu den sechs Bereichen, aber zur Lücke „Verkehr und Tempolimit“ im Bereich Klima. Der Gegenstand Kernenergie hat sich seit 2023 rechtlich verändert (R3 2.3).

**e) Nicht vertieft geprüft.** Die BZgA/BIÖG-Repräsentativbefragung zur Organspende könnte die Widerspruchslösung als Gesundheitsfrage enthalten. Ich habe weder Fragebogen noch Datenzugang gesehen; die Suchausgabe zeigte ungefragt Ergebnisse, die ich nicht verwende.

### 3.7 Weitere Kandidaten, knapp

- **The Berlin Pulse (Körber-Stiftung).** Ausgabe 2025/26, Impressum PDF-S. 26: „representative survey carried out by forsa … September 2025“, „© Körber-Stiftung 2025“. Methodenhinweis PDF-S. 18: „Computer-Assisted Telephone interviews were conducted with a representative random sample of 1,503 participants“, 15.–26.09.2025. Ein Datensatzangebot habe ich nicht gefunden. Ergebnisseiten nicht geöffnet. Thema Außenpolitik; die Rechte liegen bei einer privaten Stiftung.
- **eupinions (Bertelsmann Stiftung).**
  - Erhebung durch „Nira Data (formerly known as Dalia Research/Latana)“, quartalsweise in allen EU-Staaten, „representative with regard to age, gender, education and country/region“ (eupinions.eu/de/about).
  - Datenvertrag (Fassung PDF 29.09.2020), Ziffer 2.2: „The data must only be used for the data recipient's own research. In particular, using the data for any other scientific or commercial use is forbidden.“ Eine KI-Regel enthält der Vertrag nicht.
  - Website: „prior permission from the Bertelsmann Stiftung … is required for any use of information offered here“.
  - Den Stichprobentyp habe ich nicht im Wortlaut belegt. Vermutung: Online-Quote.
- **CSES Modul 6.** Die Seite zur „Second Advance Release“ vom 16.12.2025 listet im Archiv 18 Wahlstudien; Deutschland ist nicht darunter. Der deutsche Beitrag stammt laut R2 aus GLES 2025, also aus einer GESIS-Studie. Inhaltlich gibt es nur Demokratiefragen. Q05c lautet „Instead of elected politicians, the country would be run better if important political decisions were left up to: Citizens in referendums.“ und berührt die Lücke Volksentscheide. Ausgabenfragen enthält das Modul nicht.
- **FRA Fundamental Rights Survey (2019).** Laut Projektseite gab es eine Kombination aus persönlichen und Online-Befragungen durch Ipsos MORI (Abrufwerkzeug, nicht wörtlich geprüft). Nicht vertieft: Erhebung 2019, Schwerpunkt Erfahrungen und Rechtskenntnis.
- **ECFR-Umfragen.** Nur Suchergebnis: online durch Datapraxis und YouGov. Nicht geöffnet.
- **Nicht geprüft:** OECD Trust Survey (überwiegend Vertrauen, nach Auftragsregel ausgeschlossen), SOEP, IAB PASS, Munich Security Index, Krankenkassen-Umfragen.

## 4. Übersicht: Zugang und Rechte

| Quelle | Bereitsteller | Anmeldung oder Vertrag | Einzeldaten | KI-Regel im gesehenen Text | Deutscher Wortlaut öffentlich | Stichprobe Deutschland | Neueste deutsche Feldzeit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ESS12 | ESS ERIC (Sikt) | Konto im Data Portal | ab Jan. 2027 (geplant) | keine gefunden; Portalbedingungen nicht gesehen | ESS1–11 ja (CC BY-SA 4.0), ESS12 nein | Zufall, halb persönlich, halb Selbstausfüller | 09/2025–05/2026 (ESS-weit) |
| OECD RTM | OECD | E-Mail-Anfrage | ja (PUF) | in OECD-Bedingungen keine; PUF-Bedingungen nur als Auszug | nein (nur Englisch) | Online-Quote, 18–64 | Nov.–Dez. 2024 |
| Pew Global Attitudes | Pew | Konto, Zustimmung | ja | keine ausdrücklich; Verbot automatisierten Sammelns | nicht gefunden | Telefon, RDD-Zufall, 18+ | Feb.–Apr. 2026 |
| EIB Climate Survey | EIB | keine (Kopfzeilen geprüft) | ja (Excel, nicht geöffnet) | keine | nein (nur Englisch) | Online-Quote, 15+ | Aug. 2024 |
| Eurofound EQLS 2016 | UK Data Service | Registrierung, EUL | ja | **ja: Verbot ohne schriftliche Erlaubnis (EUL 5.5)** | ja (nicht geöffnet) | Zufall, persönlich, 18+ | 09/2016–02/2017 |
| ZMSBw | GESIS (Daten), ZMSBw (Bericht) | GESIS | bei GESIS | GESIS §4 (laut R2) | nur im Bericht (nicht geöffnet) | Zufall (Random Route), CAPI, 16+ | Apr.–Mai 2025 |
| UBA Umweltbewusstsein | GESIS (Daten), UBA (Bericht) | GESIS | bei GESIS | GESIS §4 (laut R2) | nicht geprüft | Zufall (PostDirekt), 18+ | Herbst 2024 |
| ifo Bildungsbarometer | LMU-ifo EBDC | Projektvertrag | ja, 2014–2021 | Vertrag nicht gesehen | nur in Codebüchern | Online-Access-Panel, gewichtet | 2021 (SUF) |
| Nachhaltigkeitsbarometer | RIFS/Ariadne; FDZ Ruhr (2017–2019) | SUF-Vertrag (2017–2019) | 2021–2023 ungeklärt | nicht gesehen | ja, ohne Lizenzvermerk | zufallsrekrutiertes Online-Panel, 18+ | Feb.–März 2023 |
| Berlin Pulse | Körber-Stiftung | – | nicht gefunden | – | nicht geprüft | Telefon, Zufall | Sept. 2025 |
| eupinions | Bertelsmann Stiftung | Datenvertrag, nur eigene Forschung | ja | keine im Vertrag 2020 | nicht geprüft | Online (Vermutung: Quote) | quartalsweise |

## 5. Deutsche Fragewortlaute: Wege und Grenzen

1. **ESS ist der einzige klare Weg.** Die Dokumentation steht unter CC BY-SA 4.0, also mit Namensnennung, Änderungshinweis und Weitergabe unter gleicher Lizenz. Das gilt für die deutschen Fragebögen ESS1–ESS11. Für ESS12 erst nach Veröffentlichung der deutschen Fassung. Ob nationale Fragebögen ausdrücklich als „documentation“ gelten, hat R1 als ungeprüft vermerkt.
2. **Bei der OECD wäre der Weg möglich, er ist aber nicht belegt.** OECD-Texte ab 1. Juli 2024 stehen überwiegend unter CC BY 4.0. Die deutsche RTM-Fassung ist aber nicht veröffentlicht. Der Fragebogen 2022 trägt „Restricted Use“, der von 2024 keinen Vermerk. Die OECD müsste die deutsche Fassung herausgeben und ihre Lizenz bestätigen.
3. **Eurofound erlaubt Weiterverwendung mit Quellenangabe.** Die Rechtsseite erlaubt die „reuse of any information of this website“ mit Quellenangabe und ohne Sinnentstellung. Das deckt vermutlich die veröffentlichten deutschen Fragebögen. Inhaltlich hilft EQLS 2016 kaum, und die Daten unterliegen der KI-Sperre des UKDS.
4. **Pew lizenziert „Content“ breit, aber eine deutsche Fassung ist nicht öffentlich.** Eine eigene Übersetzung wäre kein Originalwortlaut.
5. **EIB, ZMSBw, Körber und Bertelsmann brauchen eine ausdrückliche Erlaubnis.** EIB-Bedingungen und Bertelsmann-Website verlangen eine Erlaubnis, ZMSBw und Körber tragen einen Urheberrechtsvermerk ohne Lizenz.
6. **Nachhaltigkeitsbarometer und UBA tragen keinen Lizenzvermerk.** Die deutschen Wortlaute des Barometers sind öffentlich, beim UBA habe ich keinen Fragebogen geprüft. Erlaubnis oder Rechtsprüfung nötig.
7. **ifo:** deutsche Wortlaute nur in den Codebüchern unter Vertrag.
8. **Offene Rechtsfragen, die ich nicht beantworte.**
   - Sind einzelne Fragetexte überhaupt urheberrechtlich geschützt? Das hängt von der Schöpfungshöhe ab.
   - Trägt das Zitatrecht nach § 51 UrhG die Anzeige einzelner Fragen in einem Test, der die Fragen selbst stellt? Zweifelhaft, weil das Zitat dann kein Beleg ist, sondern der Inhalt.
   - Fallen Berichte von Bundesbehörden wie ZMSBw oder UBA unter § 5 Abs. 2 UrhG? Der „© ZMSBw“-Vermerk spricht dagegen, dass die Behörde selbst davon ausgeht.
   - Diese Fragen gehören zu einer juristischen Prüfung.

Dazu kommt eine methodische Grenze: Eine Frage ist nur dann ein Vergleich mit Originalantworten, wenn der gezeigte deutsche Wortlaut der ist, den die deutschen Befragten gesehen haben. Bei RTM, Pew und EIB liegt dieser Wortlaut nicht öffentlich vor.

## 6. Themenabdeckung je Bereich

Nur Präferenzen und Prinzipien. Ausgeschlossene Fragetypen sind in Abschnitt 3 genannt.

| Bereich | Gefundene Originalfragen außerhalb von GESIS | Grenzen |
| --- | --- | --- |
| Arbeit und Rente | RTM 2024 Q19i (Zahlungsbereitschaft Rente), Q23a (längeres Arbeiten), Q27e (Arbeitszeit begrenzen), Q34a (Mindestlohn, nach Informationsexperiment, mit Begründung im Text), Q34j (Rentenausgleich für Pflege, nach Experiment). RTM 2022 Q18i (Rentenausgaben). Ausblick ESS13 Wohlfahrtsmodul. | RTM: 18–64, Online-Quote, kein deutscher Wortlaut. Renteneintrittsalter, Rentenniveau, Tarifbindung: nichts gefunden. |
| Gesundheit und Pflege | RTM 2022 Q18g und Q18j (Ausgaben), RTM 2024 Q19g und Q19j (Zahlungsbereitschaft), Q22e und Q22f (Erbschaftsteuer zweckgebunden, deutsche Variante). | Bürgerversicherung, Eigenanteile, Krankenhausreform: nichts gefunden. Organspende ungeprüft. |
| Wohnen | RTM 2022 Q18f, RTM 2024 Q19f, Q30g (sozialer Wohnungsbau) und Q30e (Wohnkostenzuschüsse), beide im Klimakontext. | Mietregulierung, Vergesellschaftung, Grundsteuer: nichts gefunden. |
| Außen-, Verteidigungs- und Friedenspolitik | RTM 2022 Q24k (Priorität internationale Sicherheit). EIB VII Frage 19 und VI Q17 (Klimahilfen für Entwicklungsländer). Pew nicht prüfbar. ZMSBw und Berlin Pulse: Wortlaute nicht geöffnet. ESS13 N1 (Antrag). | Daten bei GESIS (ZMSBw) oder nicht verfügbar (Körber). Keine nutzbare Quelle für Ukraine, Wehrpflicht, Verteidigungsausgaben. |
| Bildung und Forschung | RTM 2022 Q18b, RTM 2024 Q19b, Q27a. ifo Bildungsbarometer (viele Präferenzfragen, Wortlaute nur im Codebuch). | ifo: Vertrag, nur Wissenschaft, bis 2021. Forschungsausgaben: nichts gefunden. |
| Medien und Digitalpolitik | RTM 2024 Q27c (Breitband) und Q27d (Steuer auf Roboter oder Technologieunternehmen), eher Wirtschafts- und Infrastrukturfragen. | Rundfunk, Plattformregulierung, Desinformation, KI-Regulierung: nichts gefunden. RTM Q24 ist eine Vertrauensfrage. |
| Wirtschaft und Verteilung (Lücke Steuern) | RTM 2024 Q20 (Reiche stärker besteuern), Q21 (Fairness Erbschaftsteuer, Grenzfall), Q22 (deutsche Variante), Q27l (Zölle). EIB VI Q21 (mit Zielbegründung im Text). | wie RTM |
| Klima und Energie (Lücke Verkehr, Gebäude) | Nachhaltigkeitsbarometer 2023: Tempolimits, CO₂-Preis, Kohleausstieg 2030 (deutsche Originale). EIB VI Q14, Q18, Q21. RTM 2024 Q30f (Förderung energetischer Sanierung). | Barometer ohne Lizenzvermerk, Daten 2021–2023 ungeklärt, ungewichtet. |
| Demokratie (Lücke Volksentscheide) | CSES M6 Q05c. | Deutschland nicht in der Veröffentlichung; deutsche Quelle ist GLES. |

## 7. Eignung als Vergleich

- **Veröffentlichte Tabellen.** Ich habe ergebnisblind keine Tabelle geöffnet und kann daher für keine Quelle bestätigen, dass sie für Deutschland alle Kategorien einschließlich „weiß nicht“ mit Basis, Gewichtung und Feldzeit ausweist. Kandidaten wären die OECD-„Collected Statlinks“, die ZMSBw-Berichte und der EIB-„Dataset of full results“. Das müsste eine Person ohne Ergebnisblindheitsauflage oder ein späterer, getrennt freigegebener Schritt prüfen.
- **Wählergruppen** brauchen Einzeldaten mit Parteivariable:
  - RTM hat eine Wahlabsicht (Sonntagsfrage).
  - Das Nachhaltigkeitsbarometer hat Parteineigung.
  - EIB hat keine Parteifrage.
  - Bei Pew, ZMSBw und ifo ist die Variable ungeprüft.
  - Keine der Quellen hat nach meinem Stand die erinnerte Zweitstimme, die das Projekt bisher nutzt.
- **Population und Modus weichen vom ESS ab** (15+, Zufall, persönlich): RTM 18–64 online mit Quote, EIB 15+ online mit Quote, Pew 18+ Telefon, ZMSBw 16+ CAPI, Barometer 18+ Internetnutzende. Jeder Vergleich müsste Population, Modus und Feldzeit nennen, wie es `docs/abdeckung-v2.2.md` schon verlangt. Quotenstichproben erlauben keine Stichprobenfehler im Sinne der bisherigen Intervalle.
- **Informationsexperimente** (RTM 2022 Q46–Q47, RTM 2024 Q31–Q34, ifo-Splits): Vergleichbar ist nur die Kontrollgruppe oder eine Frage vor dem Experiment.

## 8. Empfehlungen je Bereich

| Bereich | Priorität | Empfehlung | Voraussetzungen |
| --- | --- | --- | --- |
| Arbeit und Rente | mittel | OECD RTM 2024/2022 als einzige gefundene Option prüfen; ESS13 vormerken. | Deutsche RTM-Fassung und deren Lizenz von der OECD; PUF-Bedingungen im Wortlaut, ausdrücklich zu KI; Entscheidung, ob Online-Quote 18–64 als Vergleich zulässig ist. |
| Gesundheit und Pflege | mittel | wie Arbeit und Rente (RTM 2022 Q18, 2024 Q19 und Q22). | wie oben |
| Wohnen | mittel bis niedrig | RTM 2022 Q18f und 2024 Q19f; Q30 nur mit Hinweis auf den Klimakontext. | wie oben |
| Außen-, Verteidigungs- und Friedenspolitik | niedrig außerhalb von GESIS | Lücke sichtbar lassen. Wenn Steven ohnehin mit GESIS spricht, ZMSBw-Daten dort mitklären. Alternativ beim ZMSBw anfragen, ob veröffentlichte Ergebnisse und Wortlaute genutzt werden dürfen. Pew nur prüfen, wenn Steven ein Konto anlegen will. | Erlaubnis ZMSBw oder GESIS-Ausnahme; bei Pew Zustimmung zu Bedingungen durch Steven selbst. |
| Bildung und Forschung | mittel | ifo Bildungsbarometer ist inhaltlich die beste Quelle. Beim EBDC klären, ob ein öffentlicher, nichtkommerzieller Forschungsprototyp zulässig ist, ob Wortlaute gezeigt werden dürfen und ob KI-Verarbeitung erlaubt ist. | EBDC-Vertrag; Klärung des Zwecks; neuere Wellen. |
| Medien und Digitalpolitik | keine | Lücke sichtbar lassen. Keine eigenen Fragen. | – |
| Klima (Verkehr, Tempolimit) | mittel | Nachhaltigkeitsbarometer 2023 beim RIFS anfragen: Rechte an den Fragetexten, Zugang zu den Daten 2021–2023, Bedingungen. | Erlaubnis RIFS/Ariadne; Gewichtungsfrage; Zeitbezug 2023. |
| Übergreifend | hoch | Bei jeder neuen Quelle die KI-Klausel prüfen. UKDS-Quellen sind ohne schriftliche Erlaubnis gesperrt. | – |

## 9. Offene Fragen für Steven

1. Soll das Profil Vergleiche mit nicht-probabilistischen Online-Quotenstichproben (RTM, EIB, ifo) überhaupt zeigen? Die bisherigen Vergleichswerte beruhen auf Zufallsstichproben.
2. Soll ich oder eine andere Instanz bei der OECD die deutsche RTM-Fassung, deren Lizenz und die vollständigen PUF-Bedingungen einschließlich KI-Verarbeitung anfragen? Eine Anfrage wäre eine Nachricht nach außen und braucht Stevens Freigabe.
3. Soll beim EBDC (ifo) geklärt werden, ob ein öffentlicher Test als wissenschaftlicher Zweck gilt?
4. Soll beim ZMSBw und RIFS nach Rechten an Wortlauten und veröffentlichten Ergebnissen gefragt werden?
5. Wird ein Pew-Konto angelegt? Das wäre eine Zustimmung zu Bedingungen, die nur Steven geben kann.
6. Soll eine juristische Prüfung klären, ob einzelne Fragetexte geschützt sind und ob § 51 oder § 5 UrhG greifen?
7. Wie geht das Projekt mit Fragen um, die eine Begründung oder Prämisse im Text tragen (EIB VI Q21, RTM Q34a, Q23)? Nach den Neutralitätsregeln würde ich sie nicht aufnehmen oder nur mit sichtbarem Hinweis.

## 10. Grenzen dieser Prüfung

- Ergebnisblind heißt hier auch: Ob veröffentlichte Tabellen als Vergleich genügen, ist für keine Quelle geprüft.
- OECD-, Eurofound- und ifo-Seiten habe ich wegen Bot-Sperren über Wayback-Kopien gelesen. Die Live-Fassungen können abweichen.
- Nutzungsverträge, die erst nach Anmeldung oder auf Anfrage erscheinen (OECD-PUF, EBDC, ESS Data Portal, Pew-Konto, FDZ Ruhr), habe ich nicht gesehen.
- Pew-Fragetexte habe ich nicht gesehen. Die Einschätzung zu Pew-Fragetypen ist eine Vermutung.
- EQLS-2016-Fragebogen, UBA-Fragebogen, ZMSBw-Fragewortlaute und den deutschen ESS12-Fragebogen habe ich nicht gesehen.
- Deutsche Fallzahlen für RTM und ESS12 habe ich nicht gefunden.
- Ich habe nicht systematisch alle Bundes- und Landesbehörden durchsucht. Die Aussage „keine offene Lizenz gefunden“ bezieht sich auf die genannten Quellen.
- Rechtliche Aussagen sind Quellenfeststellungen, keine Rechtsauskunft.
- Übereinstimmung mit R1–R3 ist kein Neutralitäts- oder Richtigkeitsnachweis; alle stammen von Claude-Subagents.

## 11. Nachweise

### Geöffnete Quellen (Zugriff am 03.10.2026, UTC)

ESS (20:57–21:20):
- https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027
- https://www.europeansocialsurvey.org/news/article/round-12-questionnaire-and-provisional-release-dates
- https://www.europeansocialsurvey.org/news/article/preparing-round-12-data-collection
- https://www.europeansocialsurvey.org/news/article/rotating-modules-selected-round-13
- https://www.europeansocialsurvey.org/news/article/longitudinal-weights-panel-survey-now-available
- https://www.europeansocialsurvey.org/contact/disclaimer
- https://www.europeansocialsurvey.org/about/country/germany
- https://www.europeansocialsurvey.org/about/participating-countries
- https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf (SHA-256 `d5f768fa3988bdf5…`)
- https://www.europeansocialsurvey.org/sites/default/files/2025-01/R13-welfare-attitudes-social-security-insecure-times.pdf (`440f2120d37f5a1f…`)
- HEAD-Abfragen: `…/round12/fieldwork/germany/ESS12_questionnaires_DE.pdf` (404), `…/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf` (200)
- https://ess.sikt.no/en/ (nur dynamische Seite, kein Text)

OECD (20:59–21:05):
- https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf (`5672381901f57dcc…`)
- https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Background-Questionnaire.pdf (`df97adcf049be63e…`)
- https://webfs.oecd.org/Els-com/RtM/OECD-Risks-That-Matter-2022-Core-Questionnaire.pdf (`9ad7870bc403f6c4…`)
- OECD Working Paper 324: https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/07/survey-design-and-technical-documentation-supporting-the-oecd-risks-that-matter-survey_dfd831d9/5eebe551-en.pdf (`bd09930f1c601989…`)
- Wayback: http://web.archive.org/web/20251010065743id_/https://www.oecd.org/en/data/datasets/risks-that-matter-data-and-methodology.html
- Wayback: http://web.archive.org/web/20260923074842id_/https://www.oecd.org/en/about/programmes/oecd-risks-that-matter-rtm-survey.html
- Wayback: http://web.archive.org/web/20261002172601id_/https://www.oecd.org/en/about/terms-conditions.html
- Live-Seiten oecd.org: HTTP 403

Pew (21:00–21:08):
- https://www.pewresearch.org/about/terms-and-conditions/
- https://www.pewresearch.org/methods/feature/international-methodology/global-attitudes-survey/germany/all-year/
- https://www.pewresearch.org/wp-json/prc-api/v2/interactive?slug=international-methodology-database (Methodendaten, nur Deutschland-Zeilen gelesen)
- https://www.pewresearch.org/dataset/spring-2025-survey-data/ (Anrisstexte mit Ergebnissen, nicht verwendet)
- https://www.pewresearch.org/global/2025/06/11/methodology-us-image-2025/ und https://www.pewresearch.org/global/2026/02/17/appendix-a-survey-methodology-national-pride/ (Abrufwerkzeug, keine Deutschland-Angaben)

EIB (21:08–21:12):
- https://www.eib.org/en/surveys/climate-survey/all-resources
- https://www.eib.org/files/survey/methodology-eib-climate-survey-edition-vii.docx (`9882b7eced87264e…`)
- https://www.eib.org/files/survey/questionnaire-eib-climate-survey-edition-vii.docx (`10391f330319a88c…`)
- https://www.eib.org/attachments/survey/eib-climate-survey-vi-questionnaire.pdf (`7b898e24dd1f7052…`)
- https://www.eib.org/attachments/survey/eib-climate-survey-edition-vi-2023-2024-methodology.pdf (`9dfdeb041375b099…`)
- https://www.eib.org/en/terms-of-use.htm
- HEAD-Abfrage: https://www.eib.org/files/survey/eib-individual-data-2024-2025.xlsx (Inhalt nicht geladen)

Eurofound und UKDS (21:10–21:15):
- Wayback: http://web.archive.org/web/20260915095332id_/https://www.eurofound.europa.eu/en/surveys-and-data/surveys/european-quality-of-life-survey/eqls-2016
- Wayback: http://web.archive.org/web/20260520223024id_/https://www.eurofound.europa.eu/en/surveys-and-data/surveys/about-eurofound-s-surveys
- Wayback: http://web.archive.org/web/20250725103733id_/https://www.eurofound.europa.eu/en/legal-information
- https://ukdataservice.ac.uk/app/uploads/cd137-enduserlicence.pdf (`3b4f64adef7a1fc2…`)
- Live-Seiten eurofound.europa.eu: HTTP 429

Deutsche Quellen (21:12–21:22):
- https://zms.bundeswehr.de/resource/blob/5990826/a096758210c3e9f9e699a8cbb7cc8aa2/zmsbw-forschungsbericht-139-bevoelkerungsbefragung-2025-data.pdf (`277a5b230949505f…`; nur PDF-S. 2 und 94–96 gelesen)
- https://www.umweltbundesamt.de/publikationen/umweltbewusstseinsstudie-2024
- https://www.umweltbundesamt.de/system/files/medien/11850/publikationen/01_2026_texte.pdf (`71cc8b43be4cdc97…`; PDF-S. 4, 16, 18–19, 56 gelesen; PDF-S. 163 ungewollt angezeigt)
- Wayback: http://web.archive.org/web/20240629103217id_/https://www.ifo.de/DocDL/wp-2022-378-freundl-etal-ifo-education-survey.pdf (`f9bf2d415402d826…`)
- https://www.ifo.de/ebdc-datensaetze/ifo-bildungsbarometer-2021-suf (Abrufwerkzeug; direkter Abruf und Wayback scheiterten an einer Bot-Prüfung)
- https://sites.google.com/lergetporer.at/philipplergetporereconomics/data-ifo-education-survey (Abrufwerkzeug)
- https://snb.ariadneprojekt.de/
- https://snb.ariadneprojekt.de/sites/default/files/medien/dokumente/02_snb_fragebogen_2023_web.pdf (`1de3633131c2df6c…`)
- https://ariadneprojekt.de/media/2022/07/Ariadne-Hintergrund_Barometer_Juli2022.pdf (`6beea488ff1c21d3…`)
- https://ariadneprojekt.de/news-de/wie-das-soziale-nachhaltigkeitsbarometer-funktioniert/
- https://www.rifs-potsdam.de/en/output/publications/2022/soziales-nachhaltigkeitsbarometer-der-energie-und-verkehrswende-2021-daten
- https://www.rwi-essen.de/en/research-advice/further/research-data-center-ruhr-fdz/data-sets/microdata/social-sustainability-barometer
- https://search.gesis.org/research_data/ZA8973 (HTTP 403)

Weitere (21:15–21:22):
- https://koerber-stiftung.de/site/assets/files/50167/the_berlin_pulse_202526.pdf (`1592bb6397fc342b…`; nur PDF-S. 18 und 26)
- https://eupinions.eu/de/about
- https://eupinions.eu/fileadmin/files/Projekte/eupinions/Open_Data_Agreement.pdf (`3878aa9838db19ea…`)
- https://cses.org/data-download/cses-module-6-2021-2026/
- https://cses.org/wp-content/uploads/2026/04/CSES_Module6_Questionnaire.txt (`1892a59feaca56f2…`)
- https://cses.org/data-download/
- https://fra.europa.eu/en/project/2015/fundamental-rights-survey (Abrufwerkzeug)

Websuchen ohne geöffnete Zielseite (nur Suchergebnis): ESS12 Deutschland, RTM-Methodik, Pew-Methodik, EIB-Methodik, EQLS-Datenzugang, UKDS-KI-Richtlinie, FRA-Methodik, CSES-Modul 6, Umweltbewusstseinsstudie, Nachhaltigkeitsbarometer, ifo-Datenpapier, ZMSBw-Bericht, eupinions, Berlin Pulse, ECFR, BZgA-Organspende.

### Ausgeführte Befehle (Kurzform)

- `cat`, `sed`, `grep`, `head` auf Auftrags- und Projektdateien sowie R1–R3
- `curl -sL` für Webseiten und PDFs nach `/tmp/r7/`, `curl -sI` für Kopfzeilen, Wayback-CDX-Abfragen
- `pdftotext -layout`, `pdfinfo`, `file`, `gunzip` (ZMSBw-PDF war gzip-komprimiert ausgeliefert), `zcat` für Wayback-Rohkopien
- Python für HTML-zu-Text, DOCX-Text aus `word/document.xml`, Seitenzuordnung über Seitenvorschübe und Auslesen der Pew-JSON-Methodendaten
- `sha256sum` auf alle geladenen Dokumente
- `pnpm exec prettier --check` nur für diesen Bericht (bestanden). Das vollständige `pnpm check` habe ich nicht ausgeführt, weil es einen Build schreibt und der Auftrag nur diese eine Datei erlaubt.
- Keine Git-Befehle mit Schreibwirkung, keine Anmeldung, keine Zustimmung zu Bedingungen, kein Download von Daten. Einzige geschriebene Datei: dieser Bericht.

### Modell

Claude Opus 5.5, Modellkennung `claude-opus-5-5[1m]` laut Systemangabe der Laufzeitumgebung.
