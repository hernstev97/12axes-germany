# R8 – Erweiterungspaket 2025/26: Außen-, Verteidigungs- und Friedenspolitik, Medien und Digitalpolitik, Bildung und Forschung

Stand: 4. Oktober 2026 (Recherche am 3. Oktober 2026, etwa 22:30 bis 23:15 UTC). Auftrag: `reports/claude/auftraege/R8-erweiterung-aussen-digital-bildung.md` mit dem gemeinsamen Teil `reports/claude/auftraege/R-erweiterung-gemeinsam.md`. Verfasst von einem getrennten Claude-Subagenten. Ausgangsstand: Branch `research/life-93-claude-20261003`, Commit `d444227`. Geschrieben habe ich nur diesen Bericht und `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json`.

Dieser Bericht ist eine Quellen- und Instrumentenprüfung. Er ist keine Validierung, keine Dimensionsprüfung, keine Rechtsauskunft und keine Abnahme. Ein Bereich ist eine Suchgliederung, keine Messdimension. „PDF-S.“ meint die physisch gezählte PDF-Seite.

## Kurzfassung

1. **Keine geprüfte Quelle schließt eine der drei Lücken sofort und rechtlich geklärt.** Das bestätigt R1, R6 und R7 für die Feldzeit 2024 bis 2026.
2. **Außen- und Verteidigungspolitik.** Aktuelle Fragen mit Zufallsstichprobe und bekanntem deutschem Wortlaut gibt es außerhalb von GESIS nur im Eurobarometer, und sie betreffen die EU-Ebene: gemeinsame Sicherheits- und Verteidigungspolitik, EU-Maßnahmen zum Krieg gegen die Ukraine, Verteidigungsausgaben „in der EU“, Zölle. Fragen zu Entscheidungen Deutschlands (Wehrdienst, deutscher Verteidigungshaushalt, deutsche Waffenlieferungen, Rüstungsexporte) fand ich nur in gesperrten GESIS-Studien (GLES 2025, GLES-Panel, Politbarometer) und in der ZMSBw-Bevölkerungsbefragung 2025. Die ZMSBw-Befragung ist das stärkste deutsche Instrument (Zufallsstichprobe, CAPI, 2.049 Interviews, April/Mai 2025). Ihre Wortlaute stehen aber nur in den Ergebniskapiteln, und die Daten liegen bei GESIS.
3. **Medien und Digitalpolitik.** Die am besten passende gefundene Frage ist Eurobarometer SP572 QB12 (Februar 2026): eine ausdrücklich zweiseitige Abwägung zwischen sorgfältiger Regulierung von KI und möglichst wenigen Einschränkungen. Dazu kommen eine einseitige Zustimmungsaussage zur Plattformregulierung (SP572 QB5) und eine Dringlichkeitsfrage zur Alterskontrolle (SP566 QE6). Für Rundfunkbeitrag, IP-Adressen-Speicherung, Gesichtserkennung, Hassrede gegen Meinungsfreiheit und ein Mindestalter für soziale Medien fand ich keine Bevölkerungsfrage mit zugänglichem Wortlaut und Zufallsstichprobe. Der Reuters Digital News Report 2025 enthält eine zweiseitige Frage zur Löschpraxis der Plattformen, aber nur als Online-Quotenstichprobe und nur mit englischem Quellwortlaut.
4. **Bildung und Forschung.** Für Bund-Länder-Zuständigkeit, BAföG, Studiengebühren, Kita- und Sprachtestpflicht, Schulstruktur und Forschungsausgaben fand ich keine aktuelle Frage mit Zufallsstichprobe. Eurobarometer SP557 (2024) trägt nur zwei Randfragen (frei zugängliche Forschungsergebnisse, Grenzen der Wissenschaft). Thematisch am nächsten ist das ifo Bildungsbarometer 2024/2025 (2025 zu sozialen Medien und Smartphones). Es ist eine Online-Quotenstichprobe, seine Wortlaute stehen nur in Ergebnisartikeln, und Daten gibt es nur für 2014 bis 2021.
5. **ESS Runde 12 bringt für die drei Bereiche keine Präferenzfrage.** Der Quellfragebogen enthält aber die Wahlrückerinnerung A27 zur letzten nationalen Wahl. Bei der deutschen Feldzeit 2025/26 wäre das die Bundestagswahl vom 23. Februar 2025 (Folgerung; der deutsche Fragebogen ist noch nicht veröffentlicht). Das betrifft R9.
6. **Eurobarometer und deutsches Profil.** Von den 23 Eurobarometer-Kandidaten in der JSON-Datei betrifft keiner allein eine Entscheidung Deutschlands. 20 betreffen eine EU-Politik, an der Deutschland im Rat oder bei der Umsetzung mitwirkt (eine davon ist eher ein Prinzip ohne konkrete Entscheidung), drei betreffen nur die EU-Ebene. Begrenzt geeignet für einen Bevölkerungsvergleich ohne Wählergruppen sind vor allem SP572 QB12, SE037 (gemeinsame Sicherheits- und Verteidigungspolitik) und einzelne Items von ST0359. Mehrere Items enthalten eine Prämisse („als Reaktion auf die russische Invasion“), eine wertende Zielformel („bis dauerhaft gerechter Frieden herrscht“) oder zwei Gegenstände in einem Satz.
7. **Rechte.** Für die Eurobarometer-Tabellen der Kommission gilt die Weiterverwendung nach Beschluss 2011/833/EU; die Lizenzangabe „COM_REUSE“ habe ich für fünf Datensätze bestätigt. Eine KI-Regel fand ich dort nicht. Der Bericht des Digital News Report 2026 steht laut Oxford-Archiv unter CC BY 4.0, für den Fragebogen fand ich keinen Vermerk. Münchner Sicherheitskonferenz und Initiative D21 verlangen für die Verwendung ihrer Inhalte in anderen Publikationen eine ausdrückliche Zustimmung; die Körber-Stiftung verlangt eine Quellenangabe und „soweit erforderlich“ eine Zustimmung. Die deutschen Eurobarometer-Fragebögen, die GLES- und ZMSBw-Daten liegen bei GESIS und bleiben gesperrt.
8. **Mehrere Quellen veröffentlichen ihre Fragen nur zusammen mit Ergebnissen**, darunter die inhaltlich wichtigsten: ZMSBw, Berlin Pulse und Pew (alle mit Zufallsstichprobe) sowie das ifo Bildungsbarometer. Sie brauchen eine Strukturprüfung durch einen getrennten Agenten, falls Steven diesen Weg will.

## 1. Vorgehen, Ergebnisblindheit und GESIS-Sperre

Gelesen im Repository: `AGENTS.md`, `docs/project.md`, `docs/abdeckung-v2.2.md`, die beiden Auftragsdateien, die Aufträge R9 und R10 (nur zur Abgrenzung), R1 vollständig, R6 vollständig, R7 vollständig, aus R3 die Abschnitte 1, 2.2, 3, 4.4 und 4.5, aus R2 die Abschnitte 0 und 6, aus R5 die Kurzfassung. `docs/handbuch.md` habe ich nicht gelesen, weil der Auftrag keine Oberfläche und keine sichtbaren Texte betrifft. Nicht gelesen: `data/raw/`, `data/local/`, `outputs/`, `data/reference-*`, `reports/phasen/02-*`, `03-*`, `04-*`, `web/src/app/policy-draft/reviewed-*`.

Ich baue auf R1 (Wahlprogramme 2025, Wahl-O-Mat-Thesen, GLES-Wortlaute), R6 (deutsche Eurobarometer-Wortlaute, Feldzeiten, Rechte) und R7 (ESS12, Pew, ZMSBw, ifo, Berlin Pulse) auf und wiederhole deren Recherche nicht. Nachgeprüft habe ich, wo meine Empfehlung davon abhängt: den ESS12-Quellfragebogen (gleicher Hash wie R3/R7), die Veröffentlichungsmeldung der ESS, die Lieferarten aller Eurobarometer-Befragungen 2024–2026 bei der Kommission (kein Fragebogen als eigene Datei), die Lizenzangaben von fünf Eurobarometer-Datensätzen auf data.europa.eu und das Methodenkapitel der ZMSBw-Befragung (gleicher Hash wie R7). Die deutschen Eurobarometer-Wortlaute konnte ich nicht nachprüfen, weil sie nur bei GESIS liegen.

**Ergebnisblindheit.** Ich habe keine Antwortverteilungen, Prozentwerte oder Ergebnisse recherchiert, gelesen oder übernommen. Ergebnisberichte, Tabellenbände, Toplines, Volumes und Factsheets habe ich nicht geöffnet. Von der Eurobarometer-Schnittstelle habe ich nur Titel, Feldzeit, Methode und Lieferarten ausgegeben, nicht die Beschreibungs- und „keyFindings“-Felder. Ungewollte Berührungen mit Ergebnissen, die ich nicht verwendet habe und hier nicht wiedergebe:

- Die Seite „Munich Security Index 2026“ (22:36 UTC) ist eine Ergebnisseite. Meine Stichwortextraktion gab mehrere Sätze mit Ergebnissen zu Risikowahrnehmungen aus. Ich habe die Seite danach nicht weiter gelesen.
- Die Methodenseite des Digital News Report 2026 enthält einen Satz mit einem US-Ergebniswert zu Zahlungen für Online-Nachrichten.
- Die Seite von Ludger Wößmann zum ifo Bildungsbarometer enthält einen Satz mit einem Ergebnis zu Lehrkräften.
- Die Seite der Vodafone Stiftung zur Kurzstudie 2018 enthält einen Ergebnissatz.
- Mehrere Zusammenfassungen der Websuche zeigten ungefragt Ergebnisse oder Ergebnisüberschriften: zum ifo Bildungsbarometer 2025 (soziale Medien, Smartphones an Schulen), zur Bertelsmann-Studie „Verunsicherte Öffentlichkeit“, zur Mainzer Langzeitstudie Medienvertrauen, zum TechnikRadar 2025 und eine Pressemeldung der Körber-Stiftung zu den transatlantischen Beziehungen.
- Der Subagent für die Rechtslage meldet, dass die Pressemitteilung des Europäischen Parlaments vom 26.11.2025 Umfragewerte enthielt; er hat sie nicht übernommen.

**GESIS-Sperre.** Ich habe keine GESIS-Server abgerufen, auch keine Fragebögen. GLES, ISSP 2024, Politbarometer, Eurobarometer-Einzeldaten und -Fragebögen sowie ZMSBw-Daten nenne ich nur mit Angaben aus R1 bis R7 und kennzeichne sie als gesperrt. Die DataCite-Metadaten von GESIS-Studien habe ich nicht abgefragt. Beim Wissenschaftsbarometer habe ich den Hinweis auf eine GESIS-Studiennummer nur aus einer Suchergebnisliste; die verlinkte GESIS-Seite habe ich nicht geöffnet.

**Werkzeugvorbehalt.** Wörtliche Zitate stammen aus selbst geladenem Rohtext (`curl`, `pdftotext`). Angaben, die nur aus Zusammenfassungen der Websuche stammen, kennzeichne ich mit „(nur Suchergebnis)“. Die Rechtslage in den Abschnitten 3.1, 4.1 und 5.1 hat ein weiterer, eng begrenzter Claude-Subagent recherchiert (Anhang D); ich kennzeichne seine Angaben mit „(Rechtsrecherche)“.

## 2. Übersicht der geprüften Erhebungen 2024–2026

| Erhebung | Feldzeit Deutschland | Population | Stichprobe, Modus, Fallzahl | Zugang | Wahl- oder Parteifrage | Status für das Projekt |
|---|---|---|---|---|---|---|
| Standard-Eurobarometer 102–105 (EB 102.2, 103.3, 104.1, 105.2) | 10.–31.10.2024; 26.03.–15.04.2025; 09.–29.10.2025; 12.03.–01.04.2026 (R6) | EU-Staatsangehörige ab 15 in Deutschland | Zufall, mehrstufig, Ost/West getrennt; CAPI (102.2 auch CAVI); je etwa 1.500 (R6) | Kommissionstabellen; Einzeldaten und deutsche Fragebögen bei GESIS (gesperrt) | keine Bundestagswahlfrage; Links-Rechts D1 (R6) | Kandidaten zur EU-Ebene |
| Spezial-Eurobarometer 554, 557, 564, 566, 568, 572 | 2024 bis Februar 2026 (R6, Abschnitt 6) | wie oben | wie oben | wie oben | keine | Kandidaten (Digitales, Forschung) |
| Flash-Eurobarometer 574, 579, 564, EP-Befragungen | 2025–2026 | laut Schnittstelle online bzw. face-to-face | Flash online, Stichprobenart ungeprüft (FL574 laut R6 Quote) | Fragebogen nur bei GESIS oder im Ergebnisbericht | keine geprüft | nicht prüfbar |
| ESS Runde 12 | ESS-weit 09/2025–05/2026; deutsche Termine nicht gefunden | ab 15 in Privathaushalten (bisherige Runden) | Zufall; Modusexperiment persönlich / Web und Papier | Daten ab Januar 2027 | Wahlrückerinnerung A27, Parteinähe A36–A38 | keine Kandidaten |
| ZMSBw-Bevölkerungsbefragung 2025 | 11.04.–17.05.2025 | deutschsprachige Bevölkerung ab 16 in Privathaushalten | Zufall (Random Route), CAPI, 2.049 | Bericht; Daten bei GESIS (gesperrt) | im Methodenkapitel nicht genannt | nur mit Ergebnissen veröffentlicht |
| GLES Querschnitt 2025 Nachwahl | 24.02.–23.04.2025 (R1) | Deutsche ab 16 | Registerstichprobe, CAWI/Papier | GESIS (gesperrt) | Nachwahlstudie; Fragenummer in R1–R7 nicht belegt | gesperrte Kandidaten |
| GLES-Panel W29/W30 (2025), W34 (2026) | Januar/Februar 2025; März/April 2026 (R1, R3) | Wahlberechtigte (W29: mit Internetzugang) | Online-Quote | GESIS (gesperrt) | nicht einzeln belegt | gesperrt, Quote |
| Politbarometer 2024/2025 | Monatswellen (R1) | Wahlberechtigte | Zufall, CATI/CAWI | GESIS (gesperrt) | nicht geprüft | gesperrt, Wortlaut ungesehen |
| ISSP 2024 Digital Societies | in R1–R7 nicht belegt | nicht geprüft | nicht geprüft | GESIS (gesperrt) | nicht geprüft | gesperrt, nur englischer Wortlaut |
| Körber Berlin Pulse 2025/26 | 15.–26.09.2025 (R7) | Wahlberechtigte ab 18 (nur Suchergebnis) | Zufall, CATI, 1.503 (R7) | Bericht, Tabellenband | nicht geprüft | nur mit Ergebnissen veröffentlicht |
| Munich Security Index 2025/2026 | November 2024; November 2025 (nur Suchergebnis) | rund 1.000 je Land | Online-Quote (nur Suchergebnis) | Bericht | nicht geprüft | Kern misst Wahrnehmungen |
| Pew Global Attitudes 2025/2026 | 27.02.–11.04.2025; 09.02.–16.04.2026 (R7) | ab 18 | Zufall (RDD), Telefon, 1.006 / 1.004 (R7) | Konto nötig | nicht geprüft | nur mit Ergebnissen veröffentlicht |
| FES Security Radar 2025 | September 2024 (nur Suchergebnis) | 14 Länder | Ipsos; Modus für Deutschland ungeprüft | Bericht | nicht geprüft | nicht geprüft |
| Reuters Digital News Report 2025/2026 | Mitte Januar bis Ende Februar 2025 bzw. 2026 | Online-Bevölkerung | Online-Quote (YouGov) | Fragebogen öffentlich (englisch) | Links-Rechts Q1F | ein eingeschränkter Kandidat |
| ifo Bildungsbarometer 2024/2025 | 2025: Mai/Juni (nur Suchergebnis) | 2025: 18–69 Jahre und 14–17 Jahre | Online-Access-Panels, gewichtet | Daten nur 2014–2021 (EBDC, Vertrag) | nicht geprüft | nur mit Ergebnissen veröffentlicht |
| D21-Digital-Index 2024/25 | 08/2023–07/2024 (nur Suchergebnis) | ab 14 | Zufall, CAPI und CAWI | nur Bericht | nicht geprüft | nur mit Ergebnissen veröffentlicht |

Einzelheiten je Quelle stehen in den Abschnitten 3 bis 9 und in der JSON-Datei unter `kandidaten` (37 Fragen) und `quellenOhnePruefbareFragen` (12 Einträge).

## 3. Außen-, Verteidigungs- und Friedenspolitik

### 3.1 Rechtslage

Angaben aus der Rechtsrecherche (Anhang D), Abrufe am 03.10.2026 zwischen 22:45 und 23:03 UTC; selbst nachgeprüft habe ich § 2a WPflG (23:07 UTC) und die Beschlussempfehlung zum Bundespolizeigesetz (23:08 UTC, Abschnitt 4.1).

- **Wehrdienst.** Wehrdienst-Modernisierungsgesetz vom 22.12.2025, BGBl. 2025 I Nr. 370, in Kraft am 01.01.2026 (Bundestag 05.12.2025, Bundesrat 19.12.2025, BR-Drs. 731/25). Der neue § 2 WPflG lautet: „(2) Die §§ 3 bis 52 gelten im Spannungs- oder Verteidigungsfall. (3) Außerhalb des Spannungs- oder Verteidigungsfalls gelten die §§ 3, 8a bis 20b, 25, 32 bis 35, 44 und 45.“ Nach § 15a hat jede erfasste Person auf Aufforderung „eine Erklärung zur Bereitschaft und Fähigkeit zu einer Wehrdienstleistung abzugeben“ (für Frauen freiwillig, § 58i SG); nach § 16 werden ungediente Wehrpflichtige vor der Heranziehung gemustert; beides gilt für nach dem 31.12.2007 Geborene. § 2a: „Der Bundestag entscheidet durch Gesetz über die Einsetzung einer Bedarfswehrpflicht …“ (`https://www.gesetze-im-internet.de/wehrpflg/__2a.html`, selbst gelesen 23:07 UTC). Ein Gesetz zur Bedarfswehrpflicht fand die Rechtsrecherche für 2026 nicht. Quellen: `https://www.recht.bund.de/bgbl/1/2025/370/regelungstext.pdf`, `https://www.gesetze-im-internet.de/wehrpflg/BJNR006510956.html`.
- **Verteidigungsausgaben und Schuldenregel.** Art. 109 Abs. 3 und Art. 115 Abs. 2 GG in der Fassung des Gesetzes vom 22.03.2025 (BGBl. 2025 I Nr. 94): Von den Krediten ist der Betrag abzuziehen, um den „die Verteidigungsausgaben, die Ausgaben des Bundes für den Zivil- und Bevölkerungsschutz sowie für die Nachrichtendienste, für den Schutz der informationstechnischen Systeme und für die Hilfe für völkerrechtswidrig angegriffene Staaten 1 vom Hundert im Verhältnis zum nominalen Bruttoinlandsprodukt übersteigen“. Art. 87a Abs. 1a GG (seit 2022): Sondervermögen für die Bundeswehr „einmalig bis zu 100 Milliarden Euro“. NATO-Zielmarke von Den Haag (Juni 2025): 3,5 plus 1,5 Prozent des BIP bis 2035 (R1).
- **Rüstungsexporte.** § 6 Abs. 1 KrWaffKontrG: „Auf die Erteilung einer Genehmigung besteht kein Anspruch.“; Abs. 3: Versagung, wenn „die Gefahr besteht, daß die Kriegswaffen bei einer friedensstörenden Handlung, insbesondere bei einem Angriffskrieg, verwendet werden“. § 8 AWV: Genehmigungspflicht für die Ausfuhr von Gütern aus Teil I Abschnitt A der Ausfuhrliste. Politische Grundsätze der Bundesregierung (Neufassung, Kabinett 26.06.2019 laut Rüstungsexportbericht 2019), Ziff. III.2: „Der Export von nach KrWaffKontrG und AWG genehmigungspflichtigen Kriegswaffen wird nicht genehmigt, es sei denn, dass im Einzelfall besondere außen- oder sicherheitspolitische Interessen … für eine ausnahmsweise zu erteilende Genehmigung sprechen.“ Israel: Am 08.08.2025 erklärte der Bundeskanzler, die Bundesregierung genehmige „bis auf Weiteres keine Ausfuhren von Rüstungsgütern, die im Gazastreifen zum Einsatz kommen können“; laut Regierungspressekonferenz vom 17.11.2025 wurde diese Beschränkung „ab dem 24. November 2025 in Vollzug gesetzt“ aufgehoben.
- **EU-Zuständigkeiten** (deutsche Vertragstexte über den Cellar-Dienst des Amts für Veröffentlichungen, konsolidierte Fassung ABl. C 202 vom 07.06.2016; EUR-Lex war per Bot-Prüfung gesperrt):
  - Art. 4 Abs. 2 EUV: „Insbesondere die nationale Sicherheit fällt weiterhin in die alleinige Verantwortung der einzelnen Mitgliedstaaten.“
  - Art. 24 Abs. 1 EUV: Die GASP „wird vom Europäischen Rat und vom Rat einstimmig festgelegt und durchgeführt, soweit in den Verträgen nichts anderes vorgesehen ist. Der Erlass von Gesetzgebungsakten ist ausgeschlossen.“ Art. 31 Abs. 1 EUV: Beschlüsse „einstimmig“. Art. 42 Abs. 4 EUV: GSVP-Beschlüsse einstimmig; Abs. 7 Beistandsklausel.
  - Art. 41 Abs. 2 EUV: operative Ausgaben zulasten des Unionshaushalts „mit Ausnahme der Ausgaben aufgrund von Maßnahmen mit militärischen oder verteidigungspolitischen Bezügen“.
  - Art. 49 EUV: Beitritt durch einstimmigen Ratsbeschluss nach Zustimmung des Europäischen Parlaments, Ratifikation durch alle Mitgliedstaaten.
  - Art. 3 Abs. 1 lit. e AEUV: ausschließliche Zuständigkeit für die „gemeinsame Handelspolitik“; Art. 207 Abs. 4 AEUV grundsätzlich qualifizierte Mehrheit. Art. 215 Abs. 1 AEUV: restriktive Maßnahmen „mit qualifizierter Mehrheit“ auf Grundlage eines GASP-Beschlusses.
  - SAFE: Verordnung (EU) 2025/1106 des Rates vom 27.05.2025 (Art. 122 AEUV), Darlehen „höchstens 150 000 000 000 EUR“. Europäische Friedensfazilität: Beschluss (GASP) 2021/509 vom 22.03.2021. Vorübergehender Schutz für Geflüchtete aus der Ukraine: Richtlinie 2001/55/EG, Durchführungsbeschluss (EU) 2022/382, zuletzt verlängert durch Durchführungsbeschluss (EU) 2026/1912 „bis zum 4. März 2028“.
- **Verhältnis zu USA und China, Ukraine-Unterstützung als nationale Entscheidung:** kein eigenes Gesetz; Entscheidungen der Bundesregierung (Ausfuhrgenehmigungen, Haushalt) und, bei Handel und Sanktionen, der EU.

Folge für die Erhebungen: GLES q170 (Feldzeit Februar bis April 2025) fragt nach einem Gesellschaftsjahr vor dem neuen Wehrdienstrecht; GLES q27o liegt vor der Exportbeschränkung vom August 2025. Die Eurobarometer-Items zu Sanktionen, GSVP und Zöllen betreffen Entscheidungen, die im Rat fallen.

### 3.2 Politische Vorschläge

Die Positionen der Parteien im Wahlkampf 2025 belegt R1 Abschnitt 3.1 mit Wahlprogrammen und Wahl-O-Mat-Thesen (These 1 Ukraine, These 15 Rüstungsexporte nach Israel, These 34 Zölle auf chinesische Elektroautos, These 36 soziales Pflichtjahr). Ich wiederhole das nicht. Ergänzend der Koalitionsvertrag von CDU, CSU und SPD vom April 2025 („Verantwortung für Deutschland“, `https://www.cdu.de/app/uploads/2025/04/KoaV-2025-Gesamt-final-0424.pdf`, abgerufen 22:43 UTC; Zitate mit Zeilennummer des Vertrags und PDF-Seite):

- Wehrdienst: „Wir schaffen einen neuen attraktiven Wehrdienst, der zunächst auf Freiwilligkeit basiert. … Wir orientieren uns dabei am schwedischen Wehrdienstmodell. Wir werden noch in diesem Jahr die Voraussetzungen für eine Wehrerfassung und Wehrüberwachung schaffen.“ (Z. 4149–4154, PDF-S. 132)
- Verteidigungsausgaben: „Mit der Ausnahme der Verteidigungsausgaben oberhalb von einem Prozent des BIP von der Schuldenregel haben wir die Grundlage geschaffen, in einer veränderten internationalen Sicherheitsordnung dauerhaft mehr Verantwortung übernehmen zu können.“ (Z. 1734–1736, PDF-S. 56)
- Rüstungsexporte: „Wir richten unsere Rüstungsexporte stärker an unseren Interessen in der Außen-, Wirtschafts- und Sicherheitspolitik aus.“ und „Wir streben eine Harmonisierung der europäischen Rüstungsexportregeln an.“ (Z. 4194–4200, PDF-S. 134)
- Ukraine: „Die Ukraine werden wir umfassend unterstützen, so dass sie sich gegen den russischen Aggressor effektiv verteidigen und sich in Verhandlungen behaupten kann.“ (Z. 3982–3983, PDF-S. 127); zu eingefrorenem russischem Staatsvermögen: „Wir suchen in Abstimmung mit unseren Partnern nach Möglichkeiten, das eingefrorene russische Staatsvermögen zur finanziellen und militärischen Unterstützung der Ukraine wirtschaftlich zu nutzen.“ (Z. 4022–4024, PDF-S. 129)
- NATO und USA: „Unser Bekenntnis zur NATO und zur EU bleibt unverrückbar.“ (Z. 3978, PDF-S. 127); „Die Beziehungen zu den USA bleiben von überragender Bedeutung.“ (Z. 4028, PDF-S. 129)
- China: „Mit China suchen wir Zusammenarbeit, wo dies im deutschen und europäischen Interesse liegt …“ und „Vor diesem Hintergrund werden wir einseitige Abhängigkeiten abbauen und eine Politik des De-Riskings verfolgen …“ (Z. 4077–4083, PDF-S. 130)

Gegenpositionen aus den Wahlprogrammen 2025 (BSW, Linke, AfD zu Waffenlieferungen, Verteidigungsausgaben, Wehrpflicht und Sanktionen; FDP, Linke, BSW gegen die Wehrpflicht) stehen in R1 Abschnitt 3.1.

### 3.3 Erhebungen und Fragenkandidaten

**Eurobarometer (Zufallsstichprobe, EU-Ebene).** Kandidaten mit deutschem Wortlaut nach R6 (Einzelheiten und Eignung in Abschnitt 6 und in der JSON-Datei):

- SE037, gemeinsame Sicherheits- und Verteidigungspolitik und gemeinsame Außenpolitik (Dafür/Dagegen), EB 104.1 QB1 und EB 105.2 QB2 mit geändertem Wortlaut.
- ST0350, fünf EU-Maßnahmen zum Krieg gegen die Ukraine (Sanktionen einschließlich eingefrorener Vermögenswerte, Finanzierung militärischer Ausrüstung, Aufnahme von Kriegsflüchtlingen, finanzielle und humanitäre Hilfe, Bewerberstatus), EB 104.1 QD2. Die Einleitung lautet: „Die EU hat als Reaktion auf die russische Invasion in der Ukraine eine Reihe von Maßnahmen ergriffen. Inwieweit stimmen Sie jeder dieser Maßnahmen zu oder nicht zu?“
- ST0359, fünf Aussagen zur Verteidigung (Unterstützung der Ukraine „bis dauerhaft gerechter Frieden herrscht“, mehr Zusammenarbeit auf EU-Ebene, mehr Geld für Verteidigung „in der EU“, Koordination der Beschaffung, Produktionskapazitäten), EB 104.1 QD3.
- ST0939 Item 2, Zölle als Reaktion auf Zölle anderer Länder, EB 105.2 QB12.
- SP564 QC5, Beitritt der Ukraine, sobald sie die Bedingungen erfüllt (Grenzfall, primär Europäische Integration).

**Gesperrte GESIS-Studien mit nationalen Fragen (nach R1).** GLES 2025 Nachwahl q27e („Deutschland sollte die Lieferung von Waffen an die Ukraine beenden.“), q27o (Waffen für Israel), q170 (Gesellschaftsjahr mit Bundeswehroption); GLES-Panel W29/W30 (Online-Quote) mit Zwei-Prozent-Ziel, Wehrpflicht, Russland, Sanktionen, Waffenlieferungen und Einfuhrbeschränkungen; Politbarometer 2024/2025 laut Katalogabstract mit Verteidigungsausgaben, Wehrpflicht, Ukraine-Hilfe und US-Zöllen (Wortlaut ungesehen). Alle sind gesperrt, bis Steven die KI-Klausel mit GESIS klärt.

**ZMSBw-Bevölkerungsbefragung 2025** (Forschungsbericht 139, gleiche Datei wie bei R7, SHA-256 `277a5b23…`; gelesen nur PDF-S. 3 und 94–96, 22:37 UTC):
- Design laut Tabelle 13.1 (PDF-S. 95): CAPI, 11.04.–17.05.2025, „Personen ab 16 Jahren, die in Privathaushalten in der Bundesrepublik Deutschland leben“, „Repräsentative, mehrfach geschichtete Zufallsstichprobe nach dem Random-Route-Verfahren“, 2.049 Nettointerviews, Ausschöpfung 50 Prozent. Im Fließtext ist die Grundgesamtheit enger gefasst: „die deutschsprachige und in Privathaushalten lebende Bevölkerung ab 16 Jahren“. Gewichtet nach Alter, Geschlecht, Bildung und Ortsgröße. Erhebung durch Ipsos GmbH.
- Themen laut Inhaltsverzeichnis (PDF-S. 3): Russlandbild und militärische Unterstützung für die Ukraine; Verteidigungsausgaben und Personalumfang; Landes- und Bündnisverteidigung; Wehrdienst und Verteidigungsbereitschaft; Einstellungen zu den USA und zur europäischen Verteidigungszusammenarbeit; Aufgaben und Einsätze der Bundeswehr; Außenpolitische Einstellungen.
- Ein Fragebogenanhang fehlt. Die Wortlaute stehen nur in den Ergebniskapiteln: nur mit Ergebnissen veröffentlicht, Strukturprüfung durch getrennten Agenten nötig.
- Daten: „der Forschung allgemein im Datenarchiv des GESIS zur Verfügung gestellt“ (PDF-S. 94), also gesperrt.
- Ein Bericht zur Befragung 2026 war nicht auffindbar. Die Live-Seite des ZMSBw brach die Verbindung ab (22:37 UTC); im Wayback-Verzeichnis fand ich unter den Dateien mit „bevoelkerungsbefragung“ im Namen nur den Bericht 2025.

**Weitere Quellen ohne prüfbare Einzelfragen.**
- Körber-Stiftung, The Berlin Pulse 2025/26: Zufallsstichprobe per Telefon, forsa, 1.503 Befragte, 15.–26.09.2025 (R7). Fragen und laut Suchergebnis ein forsa-Tabellenband nur mit Ergebnissen. Eine Ausgabe 2024/25 existiert (nur Suchergebnis), Methode ungeprüft.
- Munich Security Index 2025/2026: Laut MSC-Seite besteht der Index aus „a core index of questions on risk perceptions … and a set of additional questions relevant to security policy that may vary from year to year“ (`https://securityconference.org/en/publications/munich-security-index/`, 22:36 UTC). Der Kern misst Wahrnehmungen und fällt nach den Regeln aus R6 heraus. Stichprobe laut Suchergebnis: Online-Panels mit Quoten, rund 1.000 je Land, Feldzeit November 2024 bzw. November 2025.
- Pew Global Attitudes 2025/2026: Zufallsstichprobe per Telefon (R7). Fragetexte nur in Toplines mit Ergebnissen, Daten nur mit Konto.
- FES Security Radar 2025: September 2024, 14 Länder einschließlich Deutschland, Ipsos (nur Suchergebnis). Nicht geöffnet.
- Flash-Eurobarometer 574 „The European Union in Defence and Space“ (05.–11.01.2026, online; laut R6 Quotenstichprobe): EU-Ebene, Fragebogen nicht prüfbar.

### 3.4 Bewertung

Mit Quellen außerhalb von GESIS ist der Bereich nur auf EU-Ebene und nur begrenzt erschließbar. Die Kernfragen der deutschen Debatte 2025/26 (Wehrdienst nach dem neuen Gesetz, deutscher Verteidigungshaushalt, deutsche Waffenlieferungen, Rüstungsexporte, Verhältnis zu USA und China als deutsche Politik) bleiben ohne zugängliche Bevölkerungsfrage. Am nächsten kämen GLES 2025 q27e, q27o, q170 (gesperrt) und die ZMSBw-Befragung (Daten gesperrt, Wortlaute nur mit Ergebnissen). Die Eurobarometer-Fragen dürfen nicht als Fragen zur deutschen Politik gezeigt werden; „In der EU sollte mehr Geld für Verteidigung ausgegeben werden“ ist keine Frage zum deutschen Verteidigungshaushalt.

## 4. Medien und Digitalpolitik

### 4.1 Rechtslage

Angaben aus der Rechtsrecherche (Anhang D), Abrufe am 03.10.2026 zwischen 22:47 und 23:00 UTC.

- **Rundfunkbeitrag.** Derzeit „monatlich 18,36 Euro“ (rundfunkbeitrag.de). Der Betrag gilt aufgrund der Anordnung des BVerfG vom 20.07.2021 (1 BvR 2756/20 u. a., Pressemitteilung 69/2021): Art. 1 des Ersten Medienänderungsstaatsvertrags gilt „vorläufig mit Wirkung vom 20. Juli 2021 bis zum Inkrafttreten einer staatsvertraglichen Neuregelung“; der Text von § 8 Rundfunkfinanzierungsstaatsvertrag nennt weiter 17,50 Euro. Der Reformstaatsvertrag trat laut BVerfG-Pressemitteilung 29/2026 „am 1. Dezember 2025 … in Kraft“. Die KEF empfahl im Februar 2026 18,64 Euro ab 01.01.2027; einen Staatsvertrag der Länder dazu fand die Rechtsrecherche nicht. Verfahren „Rundfunkfinanzierung II“ (1 BvR 2524/24, 1 BvR 2525/24): mündliche Verhandlung am 23.06.2026; in den Pressemitteilungen bis Nr. 61/2026 keine Entscheidung und kein Verkündungstermin, also nach diesem Stand nicht entschieden.
- **Plattformregulierung, Hassrede, Desinformation.** Digital Services Act (Verordnung (EU) 2022/2065), gilt „ab dem 17. Februar 2024“. Digitale-Dienste-Gesetz, Art. 1 des Gesetzes vom 06.05.2024 (BGBl. 2024 I Nr. 149); § 12 Abs. 1 DDG: „Die Bundesnetzagentur … ist vorbehaltlich der Absätze 2 und 3 zuständige Behörde nach Artikel 49 Absatz 1 der Verordnung (EU) 2022/2065.“ Für Art. 28 Abs. 1 DSA ist die Bundeszentrale für Kinder- und Jugendmedienschutz zuständig. Im Netzwerkdurchsetzungsgesetz wurden „die §§ 2 bis 3f … aufgehoben“; es besteht als Rest fort. Strafrechtliche Grenzen der Meinungsäußerung habe ich nicht gesondert geprüft.
- **IP-Adressen-Speicherung.** Regierungsentwurf Drs. 21/6581 vom 19.06.2026, Gegenäußerung Drs. 21/7154; § 177 Abs. 1 TKG-E: „Die Daten nach Satz 1 sind jeweils für drei Monate zu speichern. Inhalte der Kommunikation … dürfen nicht aufgrund dieser Vorschrift gespeichert werden.“ Erste Lesung 24.06.2026, Rechtsausschuss federführend, öffentliche Anhörung am 07.10.2026. Nicht beschlossen.
- **Gesichtserkennung und biometrischer Abgleich.** Gesetz zur Modernisierung des Bundespolizeigesetzes (Drs. 21/3051; Beschlussempfehlung Drs. 21/6990 vom 08.07.2026) mit neuem § 31b BPolG „Biometrische Detektion in Echtzeit“ (von mir in Drs. 21/6990 bestätigt, 23:08 UTC). Die Schlussabstimmung vom Juli 2026 musste wiederholt werden, weil die erforderliche Mehrheit nicht festgestellt war; am 25.09.2026 nahm der Bundestag das Gesetz in namentlicher Abstimmung an (`https://www.bundestag.de/dokumente/textarchiv/2026/kw39-de-bundespolizeigesetz-1211314`, selbst gelesen 23:07 UTC). Bundesratsbeschluss und Verkündung sind nicht belegt. Weitere Entwürfe (erste Lesung 08.07.2026, in den Ausschüssen): StPO-Entwurf Drs. 21/6806 (§ 98d automatisierter Abgleich mit öffentlich zugänglichen Internetdaten) sowie Drs. 21/6132 und 21/6131 für BKA und Bundespolizei („Ein Abgleich mit öffentlich zugänglichen Echtzeitdaten ist unzulässig.“). EU-Rahmen: Art. 5 Abs. 1 lit. h KI-Verordnung verbietet biometrische Echtzeit-Fernidentifizierung in öffentlich zugänglichen Räumen zu Strafverfolgungszwecken außer in eng benannten Fällen; lit. e verbietet Datenbanken „durch das ungezielte Auslesen von Gesichtsbildern aus dem Internet“.
- **KI-Regulierung.** KI-Verordnung (EU) 2024/1689, „gilt ab dem 2. August 2026“ mit früheren Stufen (Kapitel I und II ab 02.02.2025, Allzweck-KI ab 02.08.2025). Geändert durch Verordnung (EU) 2026/1744 vom 08.07.2026 (Digital-Omnibus zur KI): Hochrisiko-Pflichten ab „2. Dezember 2027“ (Anhang III) bzw. „2. August 2028“ (Anhang I). Deutsche Durchführung: Gesetz zur Durchführung der KI-Verordnung, BGBl. 2026 I Nr. 223, Art. 1 KI-Marktüberwachungsgesetz, in Kraft 29.07.2026; § 2 Abs. 1: „Die Bundesnetzagentur ist die für die Einhaltung der Verordnung (EU) 2024/1689 zuständige Marktüberwachungsbehörde …“.
- **Altersgrenzen für soziale Medien.** Art. 8 Abs. 1 DSGVO: Einwilligung eines Kindes wirksam, „wenn das Kind das sechzehnte Lebensjahr vollendet hat“; im BDSG keine Abweichung gefunden. Art. 28 Abs. 1 DSA verlangt „geeignete und verhältnismäßige Maßnahmen“ zum Schutz Minderjähriger, ohne feste Altersgrenze; Leitlinien der Kommission 2025 (Text wegen Bot-Prüfung nicht geladen). JuSchG § 24a; Jugendmedienschutz-Staatsvertrag in der Fassung des Sechsten Medienänderungsstaatsvertrags seit 01.12.2025 (u. a. Jugendschutzvorrichtung in Betriebssystemen, § 12). Ein gesetzliches Mindestalter für soziale Medien gibt es nicht.

Folge für die Erhebungen: Bei IP-Speicherung und Gesichtserkennung ändert sich die Rechtslage gerade (Entwurf, Bundestagsbeschluss ohne Bundesrat). Fragen aus 2024/25 träfen einen anderen Stand.

### 4.2 Politische Vorschläge

Wahlprogramme 2025 und Wahl-O-Mat-These 7 (Gesichtserkennung an Bahnhöfen) belegt R1 Abschnitt 5.1. Ergänzend der Koalitionsvertrag 2025 (wie oben):

- IP-Adressen und Gesichtserkennung: „Wir führen eine verhältnismäßige und europa- und verfassungsrechtskonforme dreimonatige Speicherpflicht für IP-Adressen und Portnummern ein …“ und Sicherheitsbehörden sollen „den nachträglichen biometrischen Abgleich mit öffentlich zugänglichen Internetdaten, auch mittels Künstlicher Intelligenz, vornehmen können“ (Z. 2630–2637, PDF-S. 84).
- Rundfunk und Plattformabgabe: „Wir setzen uns im dualen Mediensystem sowohl für einen pluralen öffentlich-rechtlichen Rundfunk als auch für faire Regulierungs- und Refinanzierungsbedingungen für private Medien ein.“ und „Wir prüfen die Einführung einer Abgabe für Online-Plattformen, die Medieninhalte nutzen.“ (Z. 3910–3914, PDF-S. 124)
- Desinformation und Plattformen: „Die bewusste Verbreitung falscher Tatsachenbehauptungen ist durch die Meinungsfreiheit nicht gedeckt. Deshalb muss die staatsferne Medienaufsicht unter Wahrung der Meinungsfreiheit auf der Basis klarer gesetzlicher Vorgaben gegen Informationsmanipulation sowie Hass und Hetze vorgehen können.“ und „Der Digital Services Act (DSA) muss stringent umgesetzt und weiterentwickelt werden …“ (Z. 3929–3937, PDF-S. 125)
- Jugendschutz und Altersverifikation: „Dazu werden wir eine Expertenkommission einsetzen, um eine Strategie ‚Kinder- und Jugendschutz in der digitalen Welt‘ zu erarbeiten …“ und „Wir setzen uns für verpflichtende Altersverifikationen und sichere Voreinstellungen für Kinder und Jugendliche bei digitalen Endgeräten und Angeboten ein.“ (Z. 3182–3187, PDF-S. 102); „Altersverifikation auf digitalen Endgeräten sollte Standard in Europa sein.“ (Z. 3948, PDF-S. 125)
- KI-Regulierung: „Wir stellen sicher, dass die nationale Umsetzung des AI-Acts innovationsfreundlich und bürokratiearm erfolgt und die Marktaufsicht nicht zersplittert wird.“ (Z. 2270–2271, PDF-S. 72)

Ein ausdrückliches Mindestalter für soziale Medien steht nicht im Koalitionsvertrag (Stichwortsuche nach „Altersgrenze“, „Mindestalter“, „soziale Medien“, „Social Media“: nur die genannten Stellen zur Altersverifikation). Weitere Vorschläge 2025/26 zum Mindestalter (Rechtsrecherche):

- Expertenkommission „Kinder- und Jugendschutz in der digitalen Welt“ der Bundesregierung (eingesetzt September 2025, Handlungsempfehlungen 24.06.2026, Abschlussbericht 11.09.2026), Handlungsempfehlung 36 mit zwei Alternativen: „gesetzliche Mindestaltersgrenze von 13 Jahren für Social-Media-Accounts mit wirksamer Altersprüfung“ oder „keine einheitliche Altersgrenze, sondern dienst- und funktionsspezifische Beschränkungen“. Die zuständige Bundesministerin hält laut Ministerium eine gesetzliche Altersgrenze von 13 Jahren grundsätzlich für den richtigen Weg.
- Europäisches Parlament, Entschließung vom 26.11.2025 (P10_TA(2025)0299, nicht bindend), laut Pressemitteilung für ein „EU-weit geltendes Mindestalter von 16 Jahren“, mit Zugang ab 13 mit elterlicher Zustimmung.
- Bundesrat: Entschließungsantrag von Niedersachsen und Thüringen (BR-Drs. 169/26 vom 24.03.2026), die Nutzung sozialer Medien „erst ab 14 Jahren zuzulassen“; am 27.03.2026 an die Ausschüsse überwiesen, kein Beschluss vermerkt.

Damit liegen 2025/26 drei verschiedene Altersmarken (13, 14, 16) und eine Alternative ohne einheitliche Grenze als Vorschläge vor.

### 4.3 Erhebungen und Fragenkandidaten

**Eurobarometer** (deutsche Wortlaute nach R6):
- SP572 QB12 (EB 105.1, DE 05.–24.02.2026): „Wenn Sie an künstliche Intelligenz (KI) denken, welche der folgenden Aussagen kommt Ihrer Meinung am nächsten?“ mit den zwei Optionen „Die Entwicklung von KI sollte sorgfältig reguliert werden, um die Sicherheit zu gewährleisten, auch wenn dies bedeutet, dass KI- Entwickler/Innen gewissen Einschränkungen unterliegen.“ und „Die Entwicklung von KI sollte mit so wenigen Einschränkungen wie möglich erlaubt sein, auch wenn dies gewisse Sicherheitsrisiken mit sich bringt.“ Beide Optionen nennen den Preis ihrer Wahl. Das ist das ausgewogenste gefundene Format im Bereich.
- SP572 QB5 Item 6: EU und Mitgliedstaaten sollen „die Regulierung von Online-Plattformen … stärken“. Einseitige Zustimmungsaussage, Zehnjahresperspektive.
- SP566 QE6 (EB 103.2, Februar/März 2025): Dringlichkeit von „Mechanismen zur Alterskontrolle, um Inhalte einzuschränken, die altersunangemessen sind“. Kein Pro/Contra und kein Mindestalter für soziale Medien.
- Weitere Items mit Wichtigkeitsformat oder ohne Streitgegenstand (SP566 QE4 Item 7 Desinformation, SP554 QB11 KI am Arbeitsplatz, SP568 QC9 Online-Wahlkampf, SE035 Item 5 Besteuerung großer Technologieunternehmen, SE037 digitaler Binnenmarkt) sind in der JSON-Datei mit Begründung als eingeschränkt oder nicht geeignet markiert.

**Reuters Institute Digital News Report** (Fragebögen selbst gelesen):
- Methode laut Methodenseiten 2025 und 2026 (22:38 UTC): „Research was conducted by YouGov using this online questionnaire from the middle of January to the end of February 2025“ (2026 entsprechend); Quoten nach Alter, Geschlecht, Region und Bildung; „We also applied political quotas based on vote choice in the most recent national election in around a third of our markets including the United States, Australia, and much of Western Europe“ (2026: „in 13 markets“); Gewichtung „to targets based on census/industry-accepted data“; „The use of a non-probability sampling approach means that it is not possible to compute a conventional ‘margin of error’“. Ob Deutschland unter den Märkten mit politischen Quoten ist und wie groß die deutsche Stichprobe ist, steht auf den Methodenseiten nicht.
- Fragebogen 2025 (englischer UK-Export, PDF-S. 27): Q1_social_2025 „Thinking about how social media and online video networks sometimes remove content that is deemed harmful or offensive (in addition to content that is illegal), which comes closest to your view?“ mit „removing too much“, „about the right amount“, „too little“, „Don’t know“. Basis „All“, kein Länderfilter angezeigt. Das ist ein zweiseitiges Format zur Löschpraxis, betrifft aber Plattformen, nicht staatliche Regeln.
- Fragebogen 2026 (PDF-S. 4–5): Q_PSM_Attitude fragt, ob Nachrichten öffentlich-rechtlicher Sender eine positive oder negative Wirkung haben. Das ist eine Bewertung, keine Frage zu Rundfunkbeitrag, Auftrag oder Finanzierung; ausgeschlossen.
- Der Fragebogen fragt Links-Rechts (Q1F), aber keine Wahl. Ein deutscher Wortlaut ist nicht veröffentlicht.

**ISSP 2024 Digital Societies** (gesperrt, nach R1): Q28a/b staatliche Videoüberwachung und Überwachung von Internetkommunikation, Q27 Verantwortung für Datenschutz; deutscher Wortlaut und deutsche Feldzeit unbekannt.

**Weitere Quellen:** D21-Digital-Index 2024/25 (Kantar, Feldzeit August 2023 bis Juli 2024, CAPI und CAWI, ab 14 Jahren, nur Suchergebnis; nur Bericht, die Seite für 2025/26 liefert HTTP 404). Mainzer Langzeitstudie Medienvertrauen (misst Vertrauen und Medienkritik, ausgeschlossen). Vodafone Stiftung Jugendstudie 2025 (nur 14- bis 20-Jährige). Bertelsmann „Verunsicherte Öffentlichkeit“ (Oktober 2023, außerhalb des Zeitraums). Flash-Eurobarometer 579 zu Bildschirmzeit und sozialen Medien bei jungen Menschen (30.03.–16.04.2026, online) und FL014EP „Social Media Survey 2025“ könnten Fragen zu Altersgrenzen enthalten; ihre Fragebögen liegen nur bei GESIS oder in Ergebnisberichten (nicht geprüft).

### 4.4 Bewertung

Weitgehend nicht abgedeckt. Außerhalb von GESIS trägt nur die KI-Regulierung eine aktuelle, ausgewogene Frage mit Zufallsstichprobe (SP572 QB12), und auch sie misst die EU-Population ab 15 im persönlichen Interview. Plattformregulierung ist nur mit einer einseitigen Zustimmungsaussage belegt. Rundfunkbeitrag und Auftrag des öffentlich-rechtlichen Rundfunks, IP-Adressen-Speicherung, Gesichtserkennung, Hassrede in Abwägung mit Meinungsfreiheit und ein Mindestalter für soziale Medien bleiben ohne Bevölkerungsfrage mit zugänglichem Wortlaut. Diese Lücken sollten sichtbar bleiben.

## 5. Bildung und Forschung

### 5.1 Rechtslage

Angaben aus der Rechtsrecherche (Anhang D), Abrufe am 03.10.2026 zwischen 22:53 und 23:03 UTC.

- **Bund-Länder-Zuständigkeit.** Art. 30 GG (staatliche Aufgaben „Sache der Länder, soweit dieses Grundgesetz keine andere Regelung trifft“), Art. 70 Abs. 1 GG, Art. 91b GG (Zusammenwirken bei Wissenschaft und Forschung), Art. 104c GG (Finanzhilfen „zur Steigerung der Leistungsfähigkeit der kommunalen Bildungsinfrastruktur“), Art. 7 Abs. 1 GG („Das gesamte Schulwesen steht unter der Aufsicht des Staates“). KMK-Ländervereinbarung vom 15.10.2020, Präambel: „Der Bildungsbereich ist dabei ganz überwiegend den Ländern zugeordnet“. DigitalPakt 2.0: Verwaltungsvereinbarung am 31.08.2026 unterzeichnet, in Kraft 01.09.2026, insgesamt 5 Mrd. Euro, je zur Hälfte von Bund und Ländern. Startchancen-Programm: Bund-Länder-Vereinbarung „für die Jahre 2024 bis 2034“.
- **Schulstruktur:** Ländersache (Art. 30, 70 GG; KMK-Vereinbarung); keine Detailrecherche.
- **BAföG.** Geltende Fassung zuletzt geändert durch Gesetz vom 16.04.2026 (BGBl. 2026 I Nr. 107); Wohnzuschlag nach § 13 Abs. 2 Nr. 2 „monatlich 380 Euro“. Entwurf eines 30. BAföG-Änderungsgesetzes (Kabinett 12.08.2026, BR-Drs. 457/26): Wohnzuschlag „zum Sommersemester 2027 (1. April 2027) von 380 Euro um rund 16 Prozent auf 440 Euro“, Bedarfssätze in zwei Schritten auf 563 Euro; Stellungnahme des Bundesrates am 25.09.2026; nicht beschlossen. Der Entwurf weicht im Zeitpunkt vom Koalitionsvertrag ab (dort Wintersemester 2026/27, Abschnitt 5.2). Ob der Entwurf die Elternabhängigkeit ändert, hat die Rechtsrecherche nicht geprüft.
- **Studiengebühren.** Baden-Württemberg, § 3 LHGebG (seit Gesetz vom 09.05.2017): „Die Studiengebühr für Internationale Studierende (Studiengebühr) beträgt pro Semester 1.500 Euro.“ Bayern, Art. 13 Abs. 3 BayHIG: „Die Hochschulen können Gebühren erheben für … das Studium ausländischer Studierender.“ (mit Ausnahmen). Thüringen: Gesetzentwurf der AfD-Fraktion (Drs. 8/3459 vom 13.05.2026). Einen Regierungsentwurf für Studiengebühren in einem weiteren Land fand die Rechtsrecherche nicht.
- **Kita- und Sprachtestpflicht.** Bund: Regierungsentwurf eines Startchancen- und Qualitätsentwicklungsgesetzes (Drs. 21/8239 vom 28.09.2026), § 22b Abs. 1 Nr. 2 SGB VIII-E: Träger stellen sicher, dass „bei jedem Kind spätestens im fünften Lebensjahr … der Sprachstand … sowie der Entwicklungsstand … festgestellt wird“ (für Kinder in Kitas); erste Lesung für den 09.10.2026 angesetzt; geplantes Inkrafttreten 01.01.2027. Länderbeispiele: Bayern, Art. 37 Abs. 3 BayEUG (bei unzureichenden Deutschkenntnissen Pflicht zum Besuch einer Kindertageseinrichtung mit Vorkurs im letzten Kindergartenjahr); Nordrhein-Westfalen, § 36 Abs. 2 SchulG (Sprachstandsfeststellung zwei Jahre vor der Einschulung, bei Bedarf „soll das Schulamt das Kind verpflichten, an einem vorschulischen Sprachförderkurs teilzunehmen“). Hamburg, Berlin und Hessen nicht belegt.
- **Smartphones an Schulen.** Hessen, § 69 Abs. 7 HSchG (seit 01.08.2025, nach Gesetzentwurf Landtags-Drs. 21/2048): „Zum Schutz der Kinder und Jugendlichen ist die Verwendung von mobilen digitalen Endgeräten für Schülerinnen und Schüler im Schulgebäude und auf dem Schulgelände grundsätzlich unzulässig.“ Fundstelle im Gesetz- und Verordnungsblatt nicht belegt.
- **Forschungsausgaben.** Keine gesetzliche Zielmarke. Hightech Agenda Deutschland (Kabinett 30.07.2025); im Agenda-Dokument fand die Rechtsrecherche keine 3,5-Prozent-Marke. Stellungnahme der Bundesregierung (Drs. 21/4100 vom 12.02.2026): „Das gesteckte 3,5-Prozent-Ziel bleibt herausfordernd.“ Pakt für Forschung und Innovation IV: „jährliche Steigerung der Zuwendungen … in den Jahren 2021 bis 2030 um drei Prozent“.

### 5.2 Politische Vorschläge

Wahlprogramme 2025 und Wahl-O-Mat-Thesen 14 (mehr Bundeskompetenzen in der Schulpolitik) und 21 (elternabhängiges BAföG) belegt R1 Abschnitt 4.1. Ergänzend der Koalitionsvertrag 2025:

- Bund-Länder: „Wir bekennen uns zum Bildungsföderalismus. In diesem Rahmen wollen wir die Zusammenarbeit von Bund, Ländern und Kommunen mit gemeinsam getragenen, übergreifenden Bildungszielen verbessern und effizienter gestalten.“ (Z. 2314–2316, PDF-S. 74; im PDF-Text „efÏzienter“)
- BAföG: „Wir wollen das BAföG in einer großen Novelle modernisieren. Die Wohnkostenpauschale erhöhen wir zum Wintersemester 2026/27 einmalig auf 440 Euro pro Monat und überprüfen diese regelmäßig. Die Freibeträge werden dynamisiert. Den Grundbedarf für Studierende passen wir in zwei Schritten (hälftig zum Wintersemester 2027/28 und 2028/29) dauerhaft an das Grundsicherungsniveau an.“ (Z. 2445–2448, PDF-S. 78)
- Sprachstand: „… werden wir die verpflichtende Teilnahme aller Vierjährigen an einer flächendeckenden, mit den Ländern vereinbarten Diagnostik des Sprach- und Entwicklungsstands einführen. Bei ermitteltem Förderbedarf erwarten wir von den Ländern geeignete, verpflichtende Fördermaßnahmen und -konzepte. Dafür führen wir ein Qualitätsentwicklungsgesetz (QEG) ein …“ (Z. 3111–3115, PDF-S. 100)
- Forschung: „Wirtschaft und Staat sollen bis 2030 jährlich mindestens 3,5 Prozent des BIP für Forschung und Entwicklung aufwenden.“ (Z. 2587–2588, PDF-S. 82); „Wir starten eine Hightech Agenda für Deutschland unter Einbindung der Länder.“ (Z. 2503, PDF-S. 79)
- Studiengebühren: im Koalitionsvertrag kein Treffer (Stichwortsuche „Studiengebühr“).

### 5.3 Erhebungen und Fragenkandidaten

- Eurobarometer SP557 QA7 (EB 102.1, DE 13.09.–04.10.2024; Wortlaut nach R6): „Die Ergebnisse öffentlich finanzierter Forschung, wie z. B. wissenschaftliche Artikel und Daten, sollten kostenlos online zur Verfügung gestellt werden“ und „Es sollte keine Grenze geben, was Wissenschaft untersuchen darf“. Fünfstufig mit Mitte. Randthemen ohne Bezug zu den Streitfragen Bund-Länder, BAföG oder Forschungsausgaben.
- ifo Bildungsbarometer 2024/2025: thematisch am nächsten. Für 2025 nur Suchergebnis: Mai/Juni 2025, Erhebung durch konkret mafo, 2.982 Erwachsene von 18 bis 69 Jahren und 1.033 Jugendliche von 14 bis 17 Jahren aus Online-Access-Panels, gewichtet. Thema laut Titel des Ergebnisartikels: soziale Medien und Smartphones. Die Wortlaute stehen nur im Ergebnisartikel; die ifo-Website antwortete mit einer Bot-Prüfung (22:40 UTC). Daten gibt es laut Seite von Ludger Wößmann nur für die „ersten acht Wellen (2014-2021)“ im LMU-ifo EBDC „zur wissenschaftlichen Nutzung“ (22:40 UTC). Fragen mit Informationsexperimenten wären nur in der Kontrollgruppe vergleichbar (R7).
- D21-Digital-Index und Wissenschaftsbarometer 2025 (CAWI, Payback-Panel, Quote, nur Suchergebnis; frühere Wellen laut Suchergebnisliste bei GESIS): nur mit Ergebnissen veröffentlicht bzw. gesperrt; Inhalte zu Bildungs- oder Forschungspolitik ungeprüft.
- Vodafone Stiftung: 2024–2026 nur Befragungen junger Menschen gefunden; keine Bevölkerungsreferenz.
- ESS12: nur die Bewertung des Bildungssystems (A44), keine Präferenz.

### 5.4 Bewertung

Für aktuelle bildungspolitische Präferenzen nicht abgedeckt. Ein Weg bestünde nur über das ifo Bildungsbarometer und setzt eine Klärung mit dem EBDC voraus, die R7 schon empfohlen hat; die Daten 2022–2025 sind nach meinem Stand nicht zugänglich. Forschungsausgaben, BAföG-Ausgestaltung und Studiengebühren bleiben ohne gefundene Bevölkerungsfrage.

## 6. Eurobarometer: Geltungsbereich und Eignung je Frage

Prüfmaßstab für einen Bevölkerungsvergleich ohne Wählergruppen: Zufallsstichprobe, Feldzeit 2024–2026, klarer Gegenstand, keine Prämisse oder Begründung im Fragetext, zweiseitiges oder neutrales Antwortformat, Ebene im Profil richtig benennbar. Für alle Eurobarometer-Fragen gilt zusätzlich: Population sind Deutsche und andere EU-Staatsangehörige ab 15 in Deutschland, nicht die Wahlbevölkerung; persönliches Interview (für EB 101.4 in Deutschland ungeprüft); „Weiß nicht“ wird nicht vorgelesen; Gewichte nur nach Post-Stratifikation; die Struktur der Kommissionstabellen für Deutschland (alle Kategorien, Basis, Gewicht) ist ungeprüft (R6 Abschnitt 7). „EU + DE“ heißt: Die EU entscheidet, Deutschland wirkt im Rat oder durch Umsetzung mit. Die Rechtsgrundlagen zu den Ebenen stehen in den Abschnitten 3.1 und 4.1.

| ID (JSON) | Frage (Kurzform) | Welle | Ebene | Eignung | Hauptgrund |
|---|---|---|---|---|---|
| R8-EB-SE037-GSVP | gemeinsame Sicherheits- und Verteidigungspolitik, dafür/dagegen | EB 104.1 / 105.2 | EU + DE | begrenzt geeignet | klarer Grundsatz, keine Prämisse; nur zwei Kategorien, Wortlautwechsel 105.2 |
| R8-EB-SE037-GASP | gemeinsame Außenpolitik | EB 104.1 | EU + DE | begrenzt geeignet | Integrationsprinzip, Überschneidung mit Europäischer Integration |
| R8-EB-ST0350-1 | Sanktionen einschließlich eingefrorener Vermögenswerte | EB 104.1 | EU + DE | eingeschränkt | zwei Gegenstände in einem Item, Prämisse |
| R8-EB-ST0350-2 | EU-Finanzierung militärischer Ausrüstung für die Ukraine | EB 104.1 | EU + DE | eingeschränkt | Prämisse, bewertet ergriffene Maßnahme; kein Ersatz für deutsche Lieferungen |
| R8-EB-ST0350-4 | finanzielle und humanitäre Hilfe | EB 104.1 | EU + DE | eingeschränkt | Prämisse, zwei Hilfearten |
| R8-EB-ST0350-5 | Bewerberstatus der Ukraine | EB 104.1 | EU + DE | eingeschränkt | Entscheidung von 2022, Grenzfall Integration |
| R8-EB-ST0359-UA | Ukraine unterstützen, „bis dauerhaft gerechter Frieden herrscht“ | EB 104.1 | EU + DE | eingeschränkt | wertende Zielformel |
| R8-EB-ST0359-ZUS | mehr Zusammenarbeit auf EU-Ebene bei Verteidigung | EB 104.1 | EU + DE | begrenzt geeignet | einseitige Zustimmungsaussage |
| R8-EB-ST0359-GELD | mehr Geld für Verteidigung „in der EU“ | EB 104.1 | EU + DE | eingeschränkt | mehrdeutig (EU-Haushalt oder Summe nationaler Haushalte); kein deutscher Haushalt |
| R8-EB-ST0359-BESCH | Beschaffung besser koordinieren | EB 104.1 | EU + DE | begrenzt geeignet | einseitig, wenig umstritten |
| R8-EB-ST0359-PROD | EU-Produktionskapazitäten stärken („muss“) | EB 104.1 | EU | begrenzt geeignet | einseitig |
| R8-EB-ST0939-ZOLL | EU-Gegenzölle | EB 105.2 | EU | eingeschränkt | Anlass im Fragetext; ausschließliche EU-Zuständigkeit |
| R8-EB-SP564-QC5-UA | Beitritt der Ukraine bei erfüllten Bedingungen | EB 103.2 | EU + DE | begrenzt geeignet | Bedingung im Text; primär Integration |
| R8-EB-SP572-QB5-6 | Regulierung von Online-Plattformen stärken | EB 105.1 | EU + DE | begrenzt geeignet | einseitig, keine Abwägung mit Meinungsfreiheit |
| R8-EB-SP572-QB12-KI | KI sorgfältig regulieren oder möglichst wenig einschränken | EB 105.1 | EU + DE | geeignet, mit den allgemeinen Eurobarometer-Grenzen | zweiseitige Abwägung, keine Ebene vorgegeben |
| R8-EB-SP566-QE6-ALTER | Dringlichkeit von Alterskontrollen | EB 103.2 | EU + DE | eingeschränkt | Dringlichkeit statt Pro/Contra; kein Mindestalter |
| R8-EB-SP566-QE4-7 | Bekämpfung von Fake News wichtig | EB 103.2 | EU + DE | nicht geeignet | Wichtigkeit ohne Gegenposition |
| R8-EB-SE035-5-TECHSTEUER | „gerechte“ Besteuerung großer Technologieunternehmen | EB 104.1 | EU + DE | eingeschränkt | wertendes Wort |
| R8-EB-SE037-DBM | digitaler Binnenmarkt | EB 105.2 | EU | kaum geeignet | abstrakter Begriff |
| R8-EB-SP554-QB11 | Regeln für KI am Arbeitsplatz wichtig | EB 101.4 | EU + DE | eingeschränkt | Wichtigkeitsformat |
| R8-EB-SP568-QC9 | Transparenz im Online-Wahlkampf | EB 103.4 | EU + DE | nicht prüfbar | Wortlaut fehlt |
| R8-EB-SP557-QA7-OA | Forschungsergebnisse kostenlos online | EB 102.1 | EU + DE | begrenzt geeignet | Randthema |
| R8-EB-SP557-QA7-GRENZE | keine Grenze für Wissenschaft | EB 102.1 | EU + DE (Prinzip) | eingeschränkt | Prinzip, keine Maßnahme |

Die Zählung in der Kurzfassung folgt dieser Tabelle: 20 Items EU + DE (darunter SP557-QA7-GRENZE, das eher ein Prinzip der Wissenschaftsfreiheit ohne konkrete Entscheidung ist), 3 Items nur EU (ST0359-PROD, ST0939-ZOLL, SE037-DBM). Diese Zuordnung ist eine Einschätzung; die JSON-Datei nennt für jede Frage die Ebenen und die Begründung.

**Folgerung.** Eurobarometer-Fragen können im Profil höchstens als Vergleich „Was denken EU-Staatsangehörige in Deutschland über eine EU-Politik?“ erscheinen. Sie ersetzen keine Frage zu einer Entscheidung von Bundestag oder Bundesregierung. Ein Vergleich ohne Wählergruppen ist methodisch vertretbar, wenn das Profil Population, Feldzeit, Modus, verborgenes „Weiß nicht“ und EU-Ebene sichtbar nennt und die Tabellenstruktur vorher ergebnisblind geprüft ist. Für Items mit Prämisse, Zielformel oder zwei Gegenständen empfehle ich, sie nicht aufzunehmen.

## 7. ESS Runde 12

- **Quellfragebogen** (06.02.2025, SHA-256 `d5f768fa…`, identisch mit R3 und R7; abgerufen 22:32 UTC): Übersicht PDF-S. 2: Kern A1–A89b („Media use; Internet use; social trust; politics, including: political interest, trust, electoral and other forms of participation, party allegiance, socio-political orientations, authoritarianism, immigration; … climate change, vote intention in EU referendum“), Rotationsmodule C „Wellbeing“ und D „Immigration“. Stichwortsuche nach Militär, Verteidigung, Ukraine, Bildung, Hochschule, Medien, Rundfunk, Internet, Überwachung, KI: nur A25 Vertrauen in die Vereinten Nationen (PDF-S. 16), A44 „What do you think overall about the state of education in [country] nowadays?“ (PDF-S. 22), Medien- und Internetnutzung (A9 u. a.) und Erwerbsstatus „in community or military service“. Keine Präferenzfrage für die drei Bereiche.
- **Wahlfrage:** A26 „Did you vote in the last [country nationality] national election in [month/year]?“ und A27 „Which party did you vote for in the last [country nationality] national election in [month/year]?“ (PDF-S. 16–17, länderspezifische Antwortliste, Fußnote: „Question text has been changed from Round 11 face-to-face for Round 12“); A36–A38 Parteinähe (PDF-S. 19–20).
- **Feldzeit und Modus:** ESS-weit September 2025 bis 15. Mai 2026 (R7); „sample units in each country have been randomly allocated to either complete a face-to-face interview or self-completion questionnaire (web and paper)“ (ESS-Meldung, abgerufen 22:33 UTC). Deutsche Feldtermine habe ich nicht gefunden. Erhebung in Deutschland durch Verian (R7).
- **Veröffentlichung:** „Data from Round 12 (2025/26) … is expected to be published for the first time in January 2027.“ Erstmals mit Post-Stratifikationsgewichten in der ersten Veröffentlichung (gleiche Meldung).
- **Deutscher Fragebogen:** unter dem üblichen Pfad weiterhin HTTP 404 (22:33 UTC; Gegenprobe ESS11 HTTP 200).
- **ESS13:** Feld September 2027 bis Mai 2028 (ESS-Meldungsliste auf derselben Seite); vorgeschlagene Frage N1 zu Militär- gegen Sozialausgaben nach R7, außerhalb des Zeitraums 2024–2026.

## 8. Zugang und Bedingungen

| Quelle | Zugangsweg | Bedingungen (wörtlich, mit Fundstelle) | KI-Regel |
|---|---|---|---|
| Eurobarometer, Kommissionstabellen | öffentliche Tabellen (Volumes) auf data.europa.eu | Beschluss 2011/833/EU Art. 4 und 6 (nach R6 Abschnitt 3.1); Lizenzangabe „COM_REUSE“ für STD104, STD105, SP566, SP572, SP557 (data.europa.eu-Schnittstelle, 22:46 UTC); rechtlicher Hinweis der Kommission: CC BY 4.0 für Inhalte im Eigentum der Kommission, „sofern nicht anders … angegeben“ (nach R6) | keine Regel gefunden |
| Eurobarometer, Einzeldaten und deutsche Fragebögen | GESIS, Registrierung | GESIS § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten.“ (nach R3/R6) | Verbot, gesperrt |
| GLES 2025, GLES-Panel, Politbarometer, ISSP 2024, ZMSBw-Daten | GESIS | wie oben | Verbot, gesperrt |
| ZMSBw-Bericht 2025 | öffentliches PDF | „© ZMSBw 2025“ (nach R7) | nicht geprüft |
| Reuters Digital News Report | Fragebogen-PDF öffentlich; Datentabellen laut Suchergebnis auf Anfrage | Bericht 2026: „© Reuters Institute for the Study of Journalism. This work is licensed under CC BY 4.0.“ (Oxford University Research Archive, 22:39 UTC); Bericht 2025 dort ohne CC-Lizenz; für den Fragebogen kein Vermerk gefunden; der Link „Terms of use“ der Website führt auf die Datenschutzerklärung | keine Regel gefunden |
| Körber-Stiftung (Berlin Pulse) | Bericht, Tabellenband | „Jegliche Vervielfältigung, Weitergabe oder sonstige Nutzung ist nur mit Quellenangabe (Körber-Stiftung) und – soweit erforderlich – nach vorheriger Zustimmung der Rechteinhaber zulässig.“ (`https://koerber-stiftung.de/impressum/`, 22:37 UTC) | keine Regel gefunden |
| Münchner Sicherheitskonferenz (MSI) | Bericht | „Eine Vervielfältigung oder Verwendung des Inhalts in anderen elektronischen oder gedruckten Publikationen ist, abgesehen von der unten dargestellten erlaubten Nutzung ohne die ausdrückliche Zustimmung durch die Stiftung Münchner Sicherheitskonferenz (gemeinnützige) GmbH nicht gestattet.“ (`https://securityconference.org/impressum/`, 22:37 UTC) | keine Regel gefunden |
| Initiative D21 | Bericht | „Eine Vervielfältigung oder Verwendung solcher Grafiken, Tondokumente, Videosequenzen und Texte in anderen elektronischen oder gedruckten Publikationen ist ohne ausdrückliche Zustimmung der*des Autor*in nicht gestattet.“ (`https://initiatived21.de/impressum`, 22:47 UTC) | keine Regel gefunden |
| Pew Research Center | Konto und Zustimmung | nach R7 Abschnitt 3.3 | keine ausdrückliche Regel (R7) |
| ifo Bildungsbarometer | EBDC, projektbezogener Vertrag, nur 2014–2021 | „zur wissenschaftlichen Nutzung zugänglich“ (Seite Wößmann, 22:40 UTC); Vertrag nicht gesehen (R7) | offen |
| ESS12 | ESS Data Portal ab Januar 2027 | ESS-Dokumentation CC BY-SA 4.0, Daten CC BY-NC-SA 4.0 (nach R1/R3/R7) | keine Regel gefunden (R7) |

Wo ich keine KI-Regel gefunden habe, folgt daraus weder eine Erlaubnis noch eine zusätzliche Genehmigungspflicht. Die Einordnung in Klassen A bis C ist Aufgabe von R10.

## 9. Wahlfragen in den geprüften Erhebungen

| Erhebung | Wahl- oder Parteifrage | Form |
|---|---|---|
| ESS12 | ja | Rückerinnerung an die letzte nationale Wahl (A27), in Deutschland bei Feldzeit 2025/26 voraussichtlich die Bundestagswahl vom 23.02.2025 (Folgerung); Parteinähe A36–A38 |
| Eurobarometer Standard/Spezial | nein | nur Links-Rechts-Selbsteinstufung D1 (R6); Europawahl-Rückerinnerung nur in EB 101.5 (R6) |
| Reuters Digital News Report | nein im Fragebogen | Links-Rechts Q1F; politische Quoten nach letzter Wahl in einigen Märkten, Deutschland nicht ausgewiesen |
| GLES 2025 Nachwahl | Nachwahlstudie | Fragenummer der Rückerinnerung in R1–R7 nicht belegt; gesperrt |
| ZMSBw 2025, Berlin Pulse, MSI, Pew, FES, ifo, D21 | nicht geprüft | Fragebögen nicht öffentlich oder nur mit Ergebnissen |

Für Wählergruppen nach der Bundestagswahl 2025 gibt es in meinem Bereich außerhalb von GESIS nur ESS12, und ESS12 enthält keine Fragen zu den drei Bereichen.

## 10. Empfehlungen und Entscheidungen für Steven

Prioritäten sind Empfehlungen, keine Auswahl.

1. **Eurobarometer-Tabellenweg (Entscheidung aus `docs/abdeckung-v2.2.md`, Nr. 2).** Wenn Steven ihn freigibt, schlage ich vor, vor jeder Werteeinsicht diese Fragen ergebnisblind festzulegen: SP572 QB12 (KI), SE037 gemeinsame Sicherheits- und Verteidigungspolitik (eine Welle wählen), ST0359 „Zusammenarbeit auf EU-Ebene“ und „mehr Geld für Verteidigung in der EU“ (mit Hinweis auf die Mehrdeutigkeit), ST0350 Item 2 (mit Hinweis „EU-Maßnahme“), SP572 QB5 Item 6 und SP557 QA7 (frei zugängliche Forschung). Nicht aufnehmen würde ich ST0350 Item 1 (zwei Gegenstände), ST0359 „bis dauerhaft gerechter Frieden“ (Zielformel), SP566 QE4 Item 7, SP568 QC9 und den digitalen Binnenmarkt. Jede aufgenommene Frage bräuchte den sichtbaren Hinweis „EU-Ebene, EU-Staatsangehörige ab 15, persönliches Interview“.
2. **GESIS-Ausnahme (Entscheidung Nr. 1).** Sie würde in diesem Bereich die einzigen aktuellen nationalen Fragen mit Zufallsstichprobe öffnen: GLES 2025 q27e, q27o, q170 sowie die ZMSBw-Daten 2025. Die Politbarometer-Wortlaute müssten danach ergebnisblind geprüft werden.
3. **Anfrage beim ZMSBw (Nachricht nach außen, braucht Stevens Freigabe).** Fragen: Gibt es den Fragebogen 2025 ohne Ergebnisse, dürfen Wortlaute auf der Website gezeigt werden, und gelten für veröffentlichte Tabellen andere Bedingungen als für GESIS-Daten?
4. **Getrennte Strukturprüfung für Quellen, die Fragen nur mit Ergebnissen veröffentlichen** (ZMSBw-Bericht 2025, Berlin Pulse 2025/26, Pew-Toplines 2025/2026, ifo Bildungsbarometer 2025). Nur sinnvoll, wenn Steven solche Quellen überhaupt zulassen will (Pew und ZMSBw Zufall, ifo Online-Quote). Der prüfende Agent dürfte an keinem späteren Auswahlplan mitwirken.
5. **Online-Quotenstichproben (Entscheidung Nr. 4).** Betrifft hier Digital News Report, ifo, MSI und GLES-Panel. Ohne diese Entscheidung empfehle ich keinen dieser Kandidaten.
6. **Sichtbare Lücken.** Wehrdienst, deutscher Verteidigungshaushalt, deutsche Waffenlieferungen und Rüstungsexporte; Rundfunkbeitrag, IP-Adressen-Speicherung, Gesichtserkennung, Hassrede und Meinungsfreiheit, Mindestalter für soziale Medien; Bund-Länder-Zuständigkeit, BAföG, Studiengebühren, Kita- und Sprachtestpflicht, Schulstruktur, Forschungsausgaben. Sie sollten in der Matrix als Datenlücke oder gesperrt stehen bleiben. Eigene oder übersetzte Fragen schließen sie nach den Projektregeln nicht.
7. **Für R9:** ESS12 A27 ist der einzige gefundene Weg zu einer Wahlrückerinnerung an die Bundestagswahl 2025 außerhalb von GESIS. Der deutsche Wortlaut und die Antwortliste sind erst mit dem deutschen Fragebogen prüfbar.

## 11. Offene Punkte

- Deutsche Eurobarometer-Wortlaute konnte ich nicht nachprüfen (GESIS-Sperre); ich übernehme sie aus R6. Einleitungen und Antwortkategorien fehlen in R6 für mehrere Items (ST0359, ST0939, SP572 QB5, SP566 QE6, SE035).
- Welche ST0359-Items in EB 105.2 noch gestellt wurden, ist in R6 nicht eindeutig zugeordnet.
- Struktur der Kommissionstabellen für Deutschland (alle Kategorien, Basis, Gewicht) ist ungeprüft (R6, R10).
- Stichprobenart der Flash-Eurobarometer 579, 564 und FL014EP ist ungeprüft.
- Deutsche Feldzeit von ESS12; deutsche Fallzahlen von Digital News Report und MSI.
- Ob der Digital News Report die Frage Q1_social_2025 in Deutschland gestellt hat und wie der deutsche Wortlaut lautet.
- Methodenangaben zu MSI, Berlin Pulse (Population), FES Security Radar, ifo 2025, D21, Wissenschaftsbarometer, TechnikRadar und Mainzer Langzeitstudie stammen teilweise nur aus Suchergebnissen.
- Ob ein ZMSBw-Bericht zur Befragung 2026 existiert.
- Ob Pew, Berlin Pulse oder ZMSBw eine Wahl- oder Parteifrage enthalten.

## Anhang A: Tatsächlich geöffnete Quellen (3. Oktober 2026, UTC)

Lokal (22:30–22:32): `AGENTS.md` (über den Kontext), `docs/project.md`, `docs/abdeckung-v2.2.md`, die Auftragsdateien R8, R9, R10 und der gemeinsame Teil, `reports/claude/agenten/R1-…`, `R6-…`, `R7-…` vollständig, Abschnitte aus `R2-…`, `R3-…`, `R5-…`.

ESS (22:32–22:33):
- https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf (SHA-256 `d5f768fa3988bdf5…`)
- HEAD-Abfragen: `…/sites/default/files/2026-01/ESS12_questionnaires_DE.pdf` (404), `https://stessrelpubprodwe.blob.core.windows.net/data/round12/fieldwork/germany/ESS12_questionnaires_DE.pdf` (404), `…/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf` (200), `https://www.europeansocialsurvey.org/about/country/germany` (200, nicht gelesen)
- https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027

Eurobarometer (22:33–22:34, 22:46):
- https://europa.eu/eurobarometer/api/survey/get/latest?nb=400 (nur Titel, Referenz, Veröffentlichungsdatum)
- https://europa.eu/eurobarometer/api/survey/get/one?id=… für 3613, 3378, 3372, 3215, 3216, 3413, 3362, 3682, 3174, 3175, 3383, 3227, 3222, 3367, 2993, 3652, 3686, 3592, 3352, 3752, 3632, 3572, 3492, 3366, 3220, 3181, 3373, 3392, 3176, 3681, 3225 (nur Feldzeit, Methode, Generaldirektion, Lieferarten; Beschreibungs- und keyFindings-Felder nicht ausgegeben)
- https://data.europa.eu/api/hub/search/datasets/ für s3613_105_2_std105_eng, s3682_105_1_sp572_eng, s3362_103_2_sp566_eng, s3227_102_1_sp557_eng, s3378_104_1_std104_eng (nur Lizenz und Dateinamen)

Münchner Sicherheitskonferenz (22:36–22:37):
- https://securityconference.org/en/publications/munich-security-index/
- https://securityconference.org/en/publications/munich-security-report/2026/munich-security-index-2026/ (Ergebnisseite, ungewollte Berührung, siehe Abschnitt 1)
- https://securityconference.org/en/imprint/, https://securityconference.org/impressum/, `…/en/legal-notice/` (404), `…/en/terms-of-use/` (404)

Körber-Stiftung (22:37): https://koerber-stiftung.de/impressum/, https://koerber-stiftung.de/en/imprint/, https://koerber-stiftung.de/datenschutz/

ZMSBw (22:37):
- https://zms.bundeswehr.de/de/mediathek/bevoelkerungsbefragungen-zur-bundeswehr--5324902 (Verbindung abgebrochen, zwei Versuche)
- http://archive.org/wayback/available?url=… (HTTP 429), Wayback-CDX-Abfrage für `zms.bundeswehr.de/resource/blob/*`
- http://web.archive.org/web/20260827154631id_/https://zms.bundeswehr.de/resource/blob/5990826/a096758210c3e9f9e699a8cbb7cc8aa2/zmsbw-forschungsbericht-139-bevoelkerungsbefragung-2025-data.pdf (SHA-256 `277a5b230949505f…`; nur PDF-S. 3 und 94–96)

Reuters Institute (22:38–22:39):
- https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/methodology und …/2026/methodology
- https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2025-06/DNR%202025%20UK%20questionnaire%20export%20%28ENG%29.pdf (SHA-256 `77fe382ebaf29151…`)
- https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2026-06/DNR%202026%20Questionnaire.pdf (SHA-256 `c6f621204dedb938…`)
- https://reutersinstitute.politics.ox.ac.uk/terms-and-conditions (404), https://reutersinstitute.politics.ox.ac.uk/privacy-policy
- https://ora.ox.ac.uk/objects/uuid:bdec3e82-9aee-4301-9556-9d908881c74a und https://ora.ox.ac.uk/objects/uuid:24de5b16-d5bb-40da-a55c-4e7c28ab6dff (nur Rechteangaben)
- https://leibniz-hbi.de/projekte/reuters-institute-digital-news-survey/ (22:52, HTTP 404)

Bildung (22:40–22:41):
- https://initiatived21.de/publikationen/d21-digital-index, …/2025-26 (404), …/2024-25 (nur Linkliste und Methodenzeilen); https://initiatived21.de/impressum (22:47)
- https://www.ifo.de/en/survey/ifo-education-survey und https://www.ifo.de/umfrage/ifo-bildungsbarometer (Bot-Prüfung, kein Inhalt)
- https://sites.google.com/view/woessmann/themen/bildungsbarometer/ifo-bildungsbarometer und https://sites.google.com/view/woessmann/forschung/%C3%B6ffentliche-meinung/daten
- https://www.vodafone-stiftung.de/kurzstudie-mehr-mut-zu-digitaler-bildung/ und https://www.vodafone-stiftung.de/jugendstudie-2025-social-media/ (nur Methodenzeilen)

Politische Vorschläge (22:43): https://www.cdu.de/app/uploads/2025/04/KoaV-2025-Gesamt-final-0424.pdf (SHA-256 `b3f35079486927ee…`, 146 PDF-Seiten; Stichwortsuche und die zitierten Stellen)

Selbst nachgeprüfte Rechtsquellen (23:07–23:08): https://www.gesetze-im-internet.de/wehrpflg/__2a.html, https://www.bundestag.de/dokumente/textarchiv/2026/kw39-de-bundespolizeigesetz-1211314, https://dserver.bundestag.de/btd/21/069/2106990.pdf (nur Stichwortsuche nach § 31b).

Versucht, ohne Inhalt: https://www.pewresearch.org/wp-json/prc-api/v2/interactive?slug=international-methodology-database (22:59, HTTP 403).

Rechtsrecherche des weiteren Subagenten (22:45–23:03, nach dessen Protokoll): recht.bund.de (BGBl. 2025 I Nr. 370, 2025 I Nr. 94, 2024 I Nr. 149, 2026 I Nr. 223); gesetze-im-internet.de (WPflG, GG Art. 7, 30, 70, 87a, 91b, 104c, 109, 115, KrWaffKontrG, AWG, AWV, DDG §§ 12–14, NetzDG, KI-MIG, BDSG, JuSchG § 24a, BAföG); bundesrat.de (BR-Drs. 731/25, 169/26, 457/26); bundestag.de und dserver.bundestag.de (Drs. 21/6581, 21/6132, 21/6990, 21/8239, 21/4100; Textarchiv 2025 kw49, 2026 kw26, kw28, kw39, kw41); bundesregierung.de (Erklärung vom 08.08.2025, Regierungspressekonferenz vom 17.11.2025, Kita-Kabinettsbeschluss, Publikationsportal); bundesverfassungsgericht.de (Pressemitteilungen 69/2021 und 29/2026 bis 61/2026, ab 62 HTTP 404); rundfunkbeitrag.de; gesetze-bayern.de (RFinStV, BayEUG Art. 37, BayHIG Art. 8 und 13); bass.schule.nrw (SchulG § 36); kultus.hessen.de und starweb.hessen.de (Drs. 21/2048); mwk.baden-wuerttemberg.de und GBl. 2017; parldok Thüringen (Drs. 8/3459); Bundeswirtschaftsministerium (Politische Grundsätze, Rüstungsexportbericht 2019); auswaertiges-amt.de; Cellar des Amts für Veröffentlichungen (EUV, AEUV, Verordnungen (EU) 2022/2065, 2025/1106, Beschlüsse 2021/509, 2022/382, 2026/1912, Richtlinie 2001/55/EG, DSGVO); eur-lex.europa.eu (Verordnungen 2024/1689 und 2026/1744; danach Bot-Prüfung); europarl.europa.eu (Pressemitteilung 20251120IPR31496; angenommener Text HTTP 202 ohne Inhalt); BMBFSFJ (Expertenkommission, DigitalPakt, Startchancen); bzkj.de; Medienanstalten (JMStV); KMK (Ländervereinbarung 2020); gwk-bonn.de (PFI); Forschungsministerium (Hightech Agenda, BAföG); cdu.de (Koalitionsvertrag); finanznachrichten.de nur zur Orientierung. Die EP-Pressemitteilung enthielt Umfragewerte; der Subagent hat sie nicht übernommen.

Websuchen (etwa 22:35–22:52, nur zum Auffinden; Ergebnisse nicht verwendet): Methodik Munich Security Index (zwei Suchen), Berlin Pulse, D21-Digital-Index, ifo Bildungsbarometer 2025 und 2026, Vodafone Stiftung, Wissenschaftsbarometer 2025, FES Security Radar 2025, Bertelsmann „Verunsicherte Öffentlichkeit“, Koalitionsvertrag 2025, Datenzugang Digital News Report, Mainzer Langzeitstudie Medienvertrauen, TechnikRadar 2025.

## Anhang B: Ausgeführte Befehle (Kurzform)

- `cat`, `sed`, `grep`, `wc`, `ls` auf Auftrags- und Berichtsdateien; `git status`, `git log` (nur lesend)
- `curl -sL` (mit Browser-Kennung) für Webseiten und PDFs nach `/tmp/r8/`, `curl -sI` für Kopfzeilen, Wayback-CDX-Abfrage
- `pdftotext` (seitenweise, mit und ohne `-layout`), `pdfinfo`, `file`, `gunzip`, `sha256sum`
- Python: HTML-zu-Text mit Stichwortfilter (Zeilen mit Prozentangaben ausgeblendet), Auswertung der Eurobarometer- und data.europa.eu-Schnittstellen (nur Metadatenfelder), Stichwortindex des Koalitionsvertrags, Erzeugung der JSON-Datei
- WebSearch zum Auffinden; ein weiterer Claude-Subagent für die Rechtslage
- Keine Anmeldung, keine Zustimmung zu Bedingungen, kein Download von Daten oder Ergebnistabellen, keine Git-Befehle mit Schreibwirkung, keine Nachrichten an Dritte. Arbeitsdateien liegen unter `/tmp/r8/`.

## Anhang C: Grenzen der eigenen Prüfung

- Ich habe Fragebögen nach Stichworten durchsucht. Items mit ungewöhnlicher Formulierung können mir entgangen sein, besonders im 66-seitigen Fragebogen des Digital News Report 2025.
- Die Eurobarometer-Wortlaute sind Übernahmen aus R6, nicht eigene Lesungen.
- Methodenangaben aus Suchergebnissen sind nicht geprüft und als solche markiert.
- Die Zuordnung der Ebenen (Abschnitt 6) ist eine rechtliche Einordnung ohne Rechtsauskunft; sie stützt sich auf die Rechtsrecherche.
- Parteipositionen zitiere ich nur aus dem Koalitionsvertrag; die übrigen stehen in R1 und sind keine vollständige Positionsanalyse.
- Übereinstimmung mit R1 bis R7 ist kein Neutralitäts- oder Richtigkeitsnachweis; alle Berichte stammen von Claude-Subagenten.

## Anhang D: Modell

Laut Laufzeitumgebung: Claude Opus 5.5, Modellkennung `claude-opus-5-5[1m]`. Für die Rechtslage (Abschnitte 3.1, 4.1, 5.1) habe ich einen weiteren Claude-Subagenten mit eng begrenztem Auftrag eingesetzt: nur Rechtsquellen, keine Umfrageergebnisse, keine GESIS-Abrufe, keine Schreibvorgänge im Repository. Modell dieses Subagenten laut seiner Laufzeitangabe: Claude Opus 5.5, `claude-opus-5-5[1m]`. Seine wörtlichen Auszüge stammen nach seiner Angabe aus selbst geladenem Rohtext; ich habe drei Angaben selbst nachgeprüft (§ 2a WPflG, Annahme des Bundespolizeigesetzes am 25.09.2026, § 31b BPolG-E in Drs. 21/6990) und keine Abweichung gefunden. Die übrigen Angaben sind nicht von mir nachgeprüft.
