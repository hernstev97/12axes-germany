# R5 – World Values Survey und European Values Study als Quelle

Stand: 3. Oktober 2026, Recherche ca. 20:55–21:30 UTC (22:55–23:30 MESZ). Auftrag: `reports/claude/auftraege/R5-wvs.vollstaendig.md` mit gemeinsamem Teil `R-alternativen-gemeinsam.md`. Ausgangsstand laut Auftrag: Commit `e9898fb`.

Dieser Bericht prüft Quellen, Zugang, Nutzungsbedingungen und Instrumente. Er ist keine Validierung, keine Dimensionsprüfung und keine rechtliche Bewertung. Ein Bereich ist hier eine Suchgliederung aus `docs/abdeckung-v2.2.md`, keine empirisch nachgewiesene Dimension. „PDF-S.“ meint die physische, 1-basiert gezählte PDF-Seite.

## Kurzfassung

- **Wo die Dateien liegen.** WVS-Daten (Welle 7 mit Deutschland 2018, frühere deutsche WVS-Erhebungen 1997, 2006, 2013, WVS-Trenddatei) gibt das WVS-Archiv (JD Systems, Madrid) über worldvaluessurvey.org ab. EVS-2017-Daten (ZA7500, ZA7502, ZA7501) und die EVS-Trenddatei (ZA7503) gibt nur GESIS ab. Die gemeinsame EVS/WVS-Datei 2017–2022 (ZA7505) gibt es laut beiden Programmen in identischer Fassung an zwei Stellen: bei GESIS und auf worldvaluessurvey.org.
- **WVS-Bedingungen.** Jeder Download auf worldvaluessurvey.org verlangt ein Formular mit Name, Institution, E-Mail und Zweck sowie die Zustimmung zu vier „Conditions of Use“. Das gilt auch für den deutschen Fragebogen. Die Bedingungen erlauben nur „non-profit purposes“, verbieten die Weitergabe der Datendateien und verlangen Zitation sowie Meldung jeder Veröffentlichung an die WVSA. Eine Regel zu KI-Systemen oder automatisierter Verarbeitung habe ich auf keiner geöffneten WVS-Seite gefunden. Das ist keine Erlaubnis. Zur Anzeige deutscher Fragewortlaute und zu Ergebnissen auf einer Website habe ich ebenfalls keine Regel gefunden.
- **EVS ist ein GESIS-Weg.** Die EVS-Website verweist für Daten auf GESIS und die „Data Usage Terms of GESIS“. Damit gilt für EVS-Daten aus GESIS das KI-Verbot in §4 der GESIS-Nutzungsbedingungen (Wortlaut selbst geprüft, Abschnitt 3.3). Ob es auch für den EVS-Teil der gemeinsamen Datei gilt, wenn sie von worldvaluessurvey.org stammt, ist in keinem geöffneten Dokument geregelt.
- **Deutschland 2017/18.** Kantar Public hat WVS7 und EVS 2017 in Deutschland gleichzeitig im Auftrag von GESIS erhoben, beide persönlich (CAPI) und aus einer gemeinsamen Registerstichprobe, die zufällig auf beide Studien verteilt wurde. WVS7: 1.520 vollständige und 8 ungültige Interviews laut WVS-Methodenbericht (gemeinsame Länderliste: 1.528). EVS 2017: 1.494 CAPI-Interviews, dazu Web- und Postbefragung; die integrierte Datei ZA7500 enthält 2.170 deutsche Fälle.
- **Inhalt.** WVS7 und EVS 2017 enthalten für Deutschland wortgleiche Präferenzfragen zu staatlicher Überwachung (Video, E-Mail/Internet, Datensammlung), zu Prinzipien der Wirtschaftsordnung (Einkommensgleichheit gegen Leistungsanreize, Privatisierung gegen Verstaatlichung, Wettbewerb, Staat gegen Eigenverantwortung), zu Umweltschutz gegen Wachstum und zu Regierungsformen (starker Staatschef, Experten, Militär, Demokratie). Nur im WVS7 steht eine Frage zur Zuwanderungspolitik (Q130). Nur in EVS 2017 stehen Fragen zu Sanktionen für Arbeitslose (v104), zur EU-Erweiterung (v198) und zu Aufgaben einer gerechten Gesellschaft (v221–v224).
- **Sechs fehlende Bereiche.** Für Arbeit und Rente, Gesundheit und Pflege, Wohnen sowie Bildung und Forschung fand ich in WVS7 und EVS 2017 keine politische Präferenzfrage, nur Normen, Moralurteile oder sehr allgemeine Formeln. Für Außen- und Verteidigungspolitik gibt es nur eine Rangfrage nach Landeszielen (darunter „starke Landesverteidigung“) und historische Fragen aus WVS 2006 und 2013. Für Digitalpolitik trägt nur Q197 (Überwachung von E-Mails und Internet). WVS und EVS schließen diese Lücken also nicht.
- **Vergleich.** Veröffentlichte Ländertabellen gibt es (WVS „Results“, gemeinsamer „Variable Report – Tables“, gewichtet mit `gwght`). Ich habe sie nicht geöffnet. Für Wählergruppen braucht es Einzeldaten. WVS7 enthält nur die Wahlabsicht (Q223), EVS 2017 nur die Parteinähe (Q49). Keine der beiden Studien fragt nach der erinnerten Zweitstimme, wie sie das bisherige Profil nutzt.
- **Empfehlung.** Wenn Steven die Klärung mit der WVSA übernimmt, ist WVS7 Deutschland ein vertretbarer Ergänzungsweg für Überwachung, Wirtschaftsordnung, Umwelt gegen Wachstum, Zuwanderungspolitik und Regierungsformen (Abschnitt 9). Die EVS-only-Fragen bleiben gesperrt wie GLES und ISSP.

## 1. Vorgehen und Ergebnisblindheit

Gelesen: `AGENTS.md`, `docs/project.md`, `docs/abdeckung-v2.2.md`, beide Auftragsdateien sowie Kopf und Abschnitt 6 von R1 und R2 als Vorlage und für den Wortlaut der GESIS-Klausel. `docs/handbuch.md` habe ich nicht gelesen, weil der Auftrag keine Oberfläche betrifft. Nicht gelesen: `data/`, `data/raw/`, `data/local/`, `data/reference-*`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-*`.

Ich habe keine Antwortverteilungen, Prozentwerte oder Mittelwerte zu Einstellungsfragen recherchiert oder übernommen. Nicht geöffnet: WVS „Codebook & Results“ und „Results“ für Deutschland, „Variable Report – Tables“ der gemeinsamen Datei (GESIS-Dok. 69549), WVS-Onlineanalyse, „Findings & Insights“.

Berührungen mit ergebnisnahen Inhalten, die ich nicht verwendet habe:

- **EVS 2017 Variable Report (GESIS-Dok. 65190).** Laut PDF-S. 10 enthält Abschnitt 6 „frequency counts by country“. Ich habe das ganze PDF geladen, aber nur PDF-S. 1–46 als Text extrahiert (Methodik, Gewichte, Abweichungen). Abschnitt 6 habe ich nicht gelesen.
- **IHSN-DDI-Datei zu WVS7 Deutschland.** Sie enthält Variablenstatistiken. Ich habe per Skript nur Studienfelder ausgelesen (`stdyDscr`, Zugangs- und Nutzungsfelder). Die Statistiken habe ich nicht angezeigt.
- **WVS-2006-Dokumentation der Datenaufbereitung (IHSN 92164).** Sie nennt einen Anteil fehlender Angaben bei einer Frage, die nicht zu meinem Thema gehört. Nicht verwendet.
- **WVS-1997-Technikbericht Ost (IHSN 92559).** Er vergleicht Geschlecht, Alter und Ortsgröße der Stichprobe mit dem Zensus. Das sind keine Einstellungsergebnisse; ich verwende nur Feldzeit, Institut und Fallzahl.
- **Methodenangaben.** Ausschöpfungs- und Bearbeitungszahlen aus den Methodenberichten verwende ich als Methodik, nicht als Ergebnis.
- Die Suchmaschinen-Zusammenfassungen zeigten keine Einstellungsergebnisse.

Werkzeugvorbehalt: Wörtliche Zitate stammen aus Rohtext, also mit `curl` geladenem HTML oder `pdftotext`. WebSearch diente nur zum Finden von Seiten. Ein WebFetch-Versuch auf die GESIS-Suche scheiterte mit HTTP 403. Bei mehrspaltigen Fragebogentabellen habe ich Antwortkategorien aus dem Layout zusammengesetzt; das ist jeweils vermerkt.

Downloads: Ich habe keine Daten heruntergeladen. Ich habe kein WVS-Formular ausgefüllt und keine Bedingungen akzeptiert. Der Downloadversuch des deutschen WVS7-Fragebogens auf worldvaluessurvey.org lieferte ohne Formular nur ein Byte; danach zeigte die Lizenzseite das Pflichtformular (Abschnitt 3.1). Die deutschen WVS-Fragebögen und Methodenberichte habe ich deshalb aus dem IHSN-Katalog geladen, der sie ohne Anmeldung und ohne Zustimmung anbietet. Diese Kopien tragen dieselben Titel wie die WVS-Dateien. Ob die Kopien mit Zustimmung der WVSA dort liegen, habe ich nicht geprüft. GESIS-Dokumente (Fragebögen, Methoden- und Variablenberichte) ließen sich ohne Anmeldung laden.

## 2. Welche Datei liegt wo?

| Datei                                                            | Bereitsteller laut Quelle                                                                                    | Zugang                                                                                    | Beleg                                                                                                                  |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| WVS7, Länderdatei Deutschland 2018 (v5.1)                        | WVS-Archiv, worldvaluessurvey.org                                                                            | Formular und Zustimmung je Download                                                       | WVS-Dokumentationsseite Welle 7, Eintrag „Germany 2018“, Abschnitt „Data Files“; Lizenzseite (3.1)                     |
| WVS7, Gesamtdatei aller Länder                                   | WVS-Archiv                                                                                                   | wie oben                                                                                  | WVS-Seite „Documentation“: Zitierformat „World Values Survey Wave 7 … Version 4.0.0“; gemeinsamer Bericht nennt v6.0.0 |
| WVS Deutschland 1997, 2006, 2013                                 | WVS-Archiv                                                                                                   | wie oben                                                                                  | WVS-Dokumentationslisten der Wellen 3, 5, 6                                                                            |
| WVS Wellen 1 und 2 „Germany“                                     | auf der WVS-Seite als „Germany EVS“ geführt                                                                  | nicht geprüft                                                                             | WVS-Dokumentationslisten der Wellen 1 und 2                                                                            |
| EVS 2017 Integrated Dataset ZA7500 (v5.0.0)                      | GESIS                                                                                                        | GESIS-Konto und GESIS-Nutzungsbedingungen                                                 | EVS-Seite „Data access“; EVS Variable Report PDF-S. 8                                                                  |
| EVS 2017 Matrix Design Data ZA7502, Sensitive Data ZA7501        | GESIS                                                                                                        | wie oben; ZA7501 laut Suchergebnis mit eigenem Vertrag (nicht selbst geprüft)             | EVS Variable Report PDF-S. 8                                                                                           |
| EVS-Trenddatei 1981–2017 ZA7503                                  | GESIS                                                                                                        | wie oben                                                                                  | EVS-Seite „IVS 1981–2022 – Data and Documentation“                                                                     |
| Gemeinsame EVS/WVS-Datei 2017–2022 ZA7505 (v5.0.0)               | GESIS und WVS-Archiv, „identical version … through two data service points“                                  | bei GESIS: GESIS-Bedingungen; bei der WVS: Formular und WVS-Bedingungen                   | gemeinsamer Variable Report – Documentation, PDF-S. 5; WVS-Seite „WVS/EVS Joint 2017“; Lizenzformular für DOID 12153   |
| Integrated Values Surveys 1981–2022                              | keine eigene Datei; Nutzende verbinden die EVS-Trenddatei (GESIS) und die WVS-Trenddatei (WVS) per Syntax    | je nach Teil                                                                              | EVS-Seite „IVS 1981–2022“; „IVS Conditions of Use“ (GESIS-Dok. 71029)                                                  |
| Deutsche Fragebögen WVS 1997, 2006, 2013, 2018                   | WVS-Archiv (mit Formular); Kopien im IHSN-Katalog ohne Anmeldung                                             | IHSN: frei                                                                                | IHSN-Studien 9097, 8997, 9040, 11570                                                                                   |
| Deutsche Fragebögen EVS 2017 (CAPI, CAWI, Post, Matrix)          | GESIS, verlinkt von der EVS-Seite „Participating countries“                                                  | frei, ohne Anmeldung                                                                      | access.gesis.org/dbk/66247 (ZIP)                                                                                       |

Eine eigene GESIS-Studiennummer nur für WVS7 habe ich nicht gefunden. Die GESIS-Suche war für meine Werkzeuge gesperrt (HTTP 403), daher ist das nicht abschließend geprüft.

Eine Widersprüchlichkeit in den WVS-Texten: Die Nachricht zur gemeinsamen Datei vom 3. Januar 2023 und die WVS-Seite „WVS/EVS Joint 2017“ sagen „Access to the data … is free, with no registration or payments required.“ Dieselbe WVS-Seite führt die Dateien aber über das Formular mit Pflichtangaben und Zustimmung (Abschnitt 3.1). Die WVS-Seite „Documentation“ sagt: „When downloading files and result reports you will be asked to register at no charge and agree with the WVS non-redistribution data use license.“ Die WVS-FAQ sagt: „complete the registration information (when asked) with your name, organization and email“. Gemeint ist offenbar kein Konto, sondern ein Formular je Download.

## 3. Nutzungsbedingungen wörtlich

### 3.1 World Values Survey

**Formular und „Conditions of Use“** (https://www.worldvaluessurvey.org/AJDownloadLicense.jsp, aufgerufen für DOID 6609, den deutschen WVS7-Fragebogen, ca. 20:57 UTC, und für DOID 12153, die gemeinsame Datei als SPSS-Datei, ca. 21:10 UTC; beide Male identischer Text, Formular nicht abgeschickt):

> „In order to download the file you are asked to fill the following registration form and agree on the "Conditions of Use".“
>
> Pflichtfelder laut Seitenskript: Name, „Company/Institution“, E-Mail, „Intended use“ (Auswahl: „Instruction“, „Academic research project“, „Dissertation“, „Policy-related analysis“, „Others (please specify)“) und das Häkchen „I have read the 'Conditions of use' and agree with them“.
>
> „These data files are available without restrictions, provided:
> a) that they are used for non-profit purposes;
> b) correct citations are provided and sent to the World Values Survey Association for each publication of results based in part or entirely on these data files;
> c) the data files themselves are not redistributed;
> d) proper citation to the WVS data is included into the references list of the publication (citation format available for downloading in the Documentation section).“

Einordnung je Prüfpunkt:

| Prüfpunkt                                               | Befund                                                                                                                                                                                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kommerziell oder nichtkommerziell                       | Nur „non-profit purposes“. Eine Definition fehlt. Eine Regel für kommerzielle Nutzung habe ich nicht gefunden.                                                                                                           |
| Zusammengefasste Ergebnisse auf einer öffentlichen Website | Nicht ausdrücklich geregelt. Bedingung b verlangt Zitation und Meldung „for each publication of results“. Ob eine Website eine „publication“ ist, bleibt offen.                                                            |
| Deutsche Fragewortlaute anzeigen                        | Keine Regel gefunden. Die Bedingungen sprechen nur von „data files“. Die Seitenfußzeile lautet „Copyright @2020 World Values Survey Association“. Der deutsche WVS7-Fragebogen wurde für GESIS erstellt (Abschnitt 4); wer Rechte an der Übersetzung hält, ist offen. |
| Weitergabe von Dateien                                  | Verboten für „the data files themselves“ (Bedingung c).                                                                                                                                                                  |
| KI-Systeme oder automatisierte Verarbeitung             | **Keine Regel gefunden** auf Lizenzseite, „Documentation“, „Data & Documentation“, FAQ, „Institutional Members“, Nachricht ID 427 und Seite „WVS/EVS Joint 2017“. Das ist ausdrücklich keine Erlaubnis.                  |

Haftungsausschluss in der IHSN-Metadatei zu WVS7 Deutschland (Feld `useStmt`/`disclaimer`): „The user of the data acknowledges that the original collector of the data, the authorized distributor of the data, and the relevant funding agency bear no responsibility for use of the data or for interpretations or inferences based upon such uses.“

### 3.2 Integrated Values Surveys (EVS Foundation und WVSA)

„IVS Conditions of Use“ (https://access.gesis.org/dbk/71029, ca. 21:03 UTC), einziges Blatt:

> „The data are available without restrictions, provided that
> 1. They are used for non-profit purposes (scientific publications, research, teaching and similar)
> 2. Data files are not redistributed
> 3. Correct citations are provided wherever results based on the data are published. In addition, a bibliographic citation or electronic copy of each completed report, article, conference paper or thesis abstract based in part or entirely on these data files is provided to EVS and WVS.“

Hier wird „non-profit purposes“ mit Beispielen erläutert: „scientific publications, research, teaching and similar“. Eine Regel zu KI, Website oder Fragetexten enthält das Blatt nicht.

### 3.3 European Values Study und GESIS

EVS-Seite „Data access“ (https://europeanvaluesstudy.eu/surveys/data-access/, ca. 21:02 UTC):

> „Free of charge data and documentation download is provided by the GESIS – Leibniz Institute for the Social Sciences in Cologne.“
> „Data and documentation of EVS are customized according to the Data Usage Terms of GESIS.“
> „Registration: Users of data from GESIS Data Catalogue need to sign in with a username (e-mail address) and password.“

Die verlinkte Seite https://www.gesis.org/en/institute/data-usage-terms lieferte HTTP 403. Ich habe deshalb die GESIS-Nutzungsbedingungen „Gültig ab: 04.02.2026“ über den Wayback-Schnappschuss vom 30.03.2026 gelesen (http://web.archive.org/web/20260330154523/https://www.gesis.org/fileadmin/upload/Datenservices/Nutzungsbedingungen/Nutzungsbedingungen.pdf, ca. 21:11 UTC):

- Präambel: „Die Originaldaten (im Folgenden „Datenbasis“) werden ausschließlich auf Grundlage dieser Nutzungsbedingungen bereitgestellt.“
- Begriffsbestimmung (5): „„KI-System“ meint ein maschinengestütztes System, das für einen, in unterschiedlichem Maße autonomen Betrieb ausgelegt ist und das nach seiner Betriebsaufnahme anpassungsfähig sein kann und das aus den erhaltenen Eingaben für explizite oder implizite Ziele ableitet, wie Ausgaben wie etwa Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen erstellt werden, die physische oder virtuelle Umgebungen beeinflussen können.“
- §1: „Soweit nicht ausdrücklich anders gekennzeichnet, stellt GESIS die Datenbasis nur für wissenschaftliche Nutzungen im Rahmen eines zeitlich befristeten Vorhabens zur Verfügung.“
- §3: „Für jede Bereitstellung der Datenbasis durch GESIS ist die Registrierung und die Zustimmung zu diesen Nutzungsbedingungen durch den Nutzer / die Nutzerin erforderlich.“
- §4: „Soweit nicht ausdrücklich anders gekennzeichnet, ist eine kommerzielle Nutzung der von GESIS bereitgestellten Daten verboten.“
- §4: „Eine Weitergabe der bereitgestellten Datenbasis an Dritte ist nicht gestattet.“
- §4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“
- §5: „Die bereitgestellte Datenbasis darf nicht – auch nicht auszugsweise – mit weiteren Daten auf Individualebene zusammengeführt werden, sofern dies nicht ausdrücklich anders gekennzeichnet ist.“
- §5: „Zulässig sind zusammenfassende Darstellungen der Daten, wie sie in wissenschaftlichen Arbeiten und Vorträgen üblich sind.“
- §6: Nach Erfüllung des Nutzungszwecks ist die Datenbasis „vollständig zu löschen“.

Der Wortlaut stimmt mit dem Zitat in R2 Abschnitt 6 überein. Die Klauseln beziehen sich auf die „Datenbasis“, also die Originaldaten. Ob sie auch frei abrufbare Dokumentation wie Fragebögen und Variablenberichte erfassen, steht nicht ausdrücklich darin. Das Zitat aus dem GESIS-Impressum zu von GESIS erstellten Texten kenne ich nur aus R2. Der Wayback-Dienst war beim Prüfversuch offline.

Die EVS-Seite trägt die Fußzeile „Copyright © 2026 European Values Study“. Eine Regel zur Anzeige von Fragetexten habe ich dort nicht gefunden.

### 3.4 Gemeinsame EVS/WVS-Datei

Laut gemeinsamem Variable Report – Documentation (GESIS-Dok. 69548, PDF-S. 5) ist die Datei „accessible through two data service points“: GESIS und WVSA, mit getrennten DOIs (GESIS `10.4232/1.14320`, WVSA `10.14281/18241.26`). Bei Bezug über GESIS gelten die GESIS-Bedingungen. Bei Bezug über die WVS gilt das WVS-Formular (Abschnitt 3.1). Ob GESIS oder die EVS für den EVS-Teil der Datei auch bei Bezug über die WVS Bedingungen beanspruchen, ist in keinem geöffneten Dokument geregelt. Das sollte Steven nicht selbst auslegen, sondern schriftlich klären.

### 3.5 IHSN-Katalog

Die IHSN-Studienseiten geben für die Daten nur „Data available from external repository“ mit Link auf die WVS-Seite an. Die Dokumente lassen sich ohne Anmeldung laden. Die Fußzeile lautet „IHSN Survey Catalog, All Rights Reserved.“ Weitere Bedingungen habe ich auf den geöffneten Seiten nicht gefunden.

## 4. Deutschland: Erhebungen

Welle und Jahr laut Länderliste der Integrated Values Surveys (GESIS-Dok. 71043, Blatt „Countries in EVS and WVS“, Zeile 37 und 38): EVS 1981 (nur West), EVS 1990, WVS 1997, EVS 1999, WVS 2006, EVS 2008/2009, WVS 2013, EVS 2017/2018, WVS 2017–2018. Eine WVS-Welle 4 mit Deutschland gibt es laut WVS-Dokumentationsliste nicht.

| Erhebung                | Institut, Leitung                                                                                                    | Feldzeit                                                                                                                                                                       | Population und Stichprobe                                                                                                                                                                                                                                                           | Modus                                                                  | Fallzahl laut Dokumentation                                                                                                                                                 | Gewichte                                                                                                                                                                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **WVS7 2017/18**        | Kantar Public „On behalf of: GESIS“; PI Christian Welzel (Leuphana); Finanzierung GESIS (Teamblatt)                  | 23.10.2017–04.04.2018 (WVS-Methodenbericht, Frage 26, PDF-S. 7). Die gemeinsame Länderliste (GESIS-Dok. 69550) und der gemeinsame Bericht (Tabelle 3, PDF-S. 9) nennen 25.10.2017–31.03.2018. | Personen ab 18 in Privathaushalten, mit Erstwohnsitz gemeldet, geboren vor dem 1.10.1999; Interview nur auf Deutsch. Zweistufige Zufallsstichprobe: Gemeinden nach NUTS 3 und BIK geschichtet, proportional zur Bevölkerung ab 18; dann Personen aus dem Melderegister. 162 Sample Points, Ersatz von fünf Gemeinden (Sample-Design-Dokument PDF-S. 1–2; Methodenbericht Fragen 11–20) | CAPI, persönlich                                                       | 5.831 Bruttoadressen, 1.520 vollständige Interviews, 8 ungültige (Methodenbericht Frage 22, PDF-S. 5); gemeinsame Länderliste: 1.528                                        | Methodenbericht Frage 37 (PDF-S. 9): „Did you add a weight variable? → No.“ Nachgewichtung sollte das WVS-Archiv „in the same way as for the weighting of the European Values study“ vornehmen (PDF-S. 10). Gemeinsamer Bericht Tabelle 8 (PDF-S. 20): `gwght` aus der WVS7-Quelldatei, „computed using the marginal distribution of Age, Sex, Education and Region“. Ob diese Variable für Deutschland belegt ist, habe ich nicht geprüft. |
| **EVS 2017**            | GESIS (Programmleitung Christof Wolf); Feldinstitut Kantar Deutschland, Kantar Public                                | CAPI 23.10.2017–04.04.2018; Post 16.11.2017–20.03.2018; Web (CAWI) 20.09.2018–28.11.2018 (EVS Variable Report Tabelle 2, PDF-S. 14; EVS Method Report PDF-S. 216)              | Zielpopulation 68.850.007; Gemeinden proportional zur Größe, dann Zufallsauswahl aus Melderegistern; zwei Stufen (EVS Method Report PDF-S. 37). Gleiche Grundstichprobe wie WVS7 (Zitat unten)                                                                                     | CAPI als Hauptmodus; zusätzlich Web und Post, teils mit Matrixdesign  | Gesamt 5.456: CAPI 1.494, Web 1.021, Post 2.941 (Variable Report Tabelle 5, PDF-S. 18). ZA7500 enthält für Deutschland 2.170 Fälle: 1.494 CAPI und 676 Selbstausfüller mit vollem Fragebogen. 3.237 Matrix-Fälle nur in ZA7502 (Tabellen 7 und 8, PDF-S. 21) | `gweight` (Alter, Geschlecht, Bildung, Region; Quelle für Deutschland: Mikrozensus 2016, Regionen NUTS 1), `gweight_no_edu`, `dweight` (Designgewicht, „provided for … Germany“), `pweight` (Variable Report Tabelle 20, PDF-S. 34–35; EVS Weighting Data PDF-S. 11 und 19) |
| **WVS 2013 (Welle 6)**  | Ipsos; wissenschaftliche Leitung Christian Welzel                                                                    | 22.07.–13.11.2013 (Methodenbericht IHSN 92377, Abschnitt 3.3)                                                                                                                 | Personen ab 18 mit Erstwohnsitz; zweistufige Registerstichprobe, disproportional je 1.000 Interviews Ost und West angestrebt (Abschnitte 2.1–2.3)                                                                                                                                    | persönlich mit Laptop (Abschnitt 3.2); Methodenbericht 2: CAPI         | 2.046 (1.034 West, 1.012 Ost), 5.661 Bruttoadressen, Ausschöpfung 36 Prozent (Abschnitt 3.3)                                                                                | IPF-Gewichtung nach Alter × Geschlecht, Bundesland × Ortsgröße (BIK) und Schulabschluss, Sollwerte aus der Media-Analyse (Abschnitt 4)                                                                                           |
| **WVS 2006 (Welle 5)**  | infas, Bonn                                                                                                          | 02.05.–21.06.2006 (Methodenfragebogen IHSN 92163, Frage 29)                                                                                                                   | Getrennt für Ost und West, 400 Sample Points; Random Route und Kish-Grid, also Haushaltsstichprobe (Fragen 14, 15, 23)                                                                                                                                                               | persönlich; Daten nachträglich erfasst, also kein CAPI (Frage 32)      | 4.454 Bruttoadressen, 2.064 vollständige Interviews (Frage 25)                                                                                                              | zwei Gewichte: Alter, Geschlecht, Bundesland, Gemeindegröße; das zweite zusätzlich Ost-West-Verteilung (Frage 41)                                                                                                               |
| **WVS 1997 (Welle 3)**  | Forsa; PI Hans-Dieter Klingemann (WZB)                                                                               | Ost: 28.03.–30.05.1997 (Technikbericht IHSN 92559); West nicht geöffnet                                                                                                       | Ost: mehrstufig, Haushalte aus dem Telekom-Telefonverzeichnis, Auswahl der Person per Geburtstagsmethode am Telefon                                                                                                                                                                | aus dem Bericht nicht eindeutig; vermutlich telefonisch (Vermutung)   | Ost: 1.009                                                                                                                                                                  | nicht geprüft                                                                                                                                                                                                                  |

Gemeinsame Stichprobe von WVS7 und EVS 2017, WVS-Sample-Design-Dokument PDF-S. 2: „Following this sample design we drew one large sample of individuals. Then, this sample was randomly split into two separate EVS and WVS (World Values Survey) samples for each sample point, thereby ensuring the correct regional distribution. Therefore, both samples are representative for Germany on their own and also in combination. In Germany EVS and WVS were conducted simultaneously, each with an individual target sample size of n=1500 face-to-face interviews.“

Ausschöpfung EVS-CAPI Deutschland laut EVS Method Report Tabelle 7 (PDF-S. 55): RR1 28,1. Für WVS7 Deutschland nennt der Methodenbericht nur die Bearbeitungskategorien, keine Quote. Eine Quote habe ich nicht selbst berechnet.

Weitere Hinweise:

- Der deutsche WVS7-Fragebogen trägt auf PDF-S. 1 den Vermerk „CAPI Field Questionnaire (by Dec 15, 2017)“, also ein Datum nach Feldbeginn. Ob sich der Fragebogen während der Feldzeit geändert hat, ist offen.
- EVS 2017 Deutschland: In den Web- und Postfassungen mit Matrixdesign wurde bei Q25 (v72–v79, Rollenbilder) fälschlich eine Mittelkategorie ergänzt (EVS Variable Report Tabelle 21, PDF-S. 35). Laut Bericht ist der Fehler in den Fassungen mit vollem Fragebogen korrigiert.
- In der gemeinsamen Datei ist bei „Staat oder Eigenverantwortung“ die Polung zwischen WVS und EVS gegenläufig. Der gemeinsame Bericht kodiert WVS7 um: „1 Government <recoded to 10>“ (Variable E037, PDF-S. 200). Im deutschen WVS7-Fragebogen ist bei Q108 1 der Staat; im deutschen EVS-Fragebogen ist bei Q32A 1 der Einzelne.

## 5. Deutsche Fragebögen: Fundorte

| Instrument                         | Fundort                                                                                                                                                                                                    | Sprache und Umfang                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| WVS7 Deutschland                   | https://catalog.ihsn.org/catalog/11570/download/101964 (IHSN-Kopie von „WVS7 Questionnaire Germany 2017 German.pdf“; auf worldvaluessurvey.org DOID 6609 nur mit Formular)                                  | Deutsch, 41 Seiten, Kopf „WVS-7 GERMANY Field questionnaire“, Fragen Q1–Q289, Länderzusätze `_de` |
| WVS7 Methodik Deutschland          | IHSN 11570, Downloads 101965 (Methodology Report), 101966 (Team), 101967 (Sample Design)                                                                                                                   | Englisch                                                                                |
| WVS 2013 Deutschland               | IHSN 9040, Download 92374 (Fragebogen), 92375–92377 (Methodenberichte, Pretest)                                                                                                                            | Deutsch, Variablen V1–V2xx                                                              |
| WVS 2006 Deutschland               | IHSN 8997, Downloads 92161 (Version A), 92162 (Version B; Unterschied: Frage 33 entfällt), 92163, 92164                                                                                                    | Deutsch, „Weltwertestudie 2006“, Fragen 1–107                                           |
| WVS 1997 Deutschland               | IHSN 9097, Downloads 92557 (Ost), 92558 (West, nicht geladen), 92559                                                                                                                                       | Deutsch                                                                                 |
| EVS 2017 Deutschland               | https://access.gesis.org/dbk/66247 (ZIP mit `ZA7500_q_de_CAPI.PDF`, `…_CAWI_full`, `…_Mail_full`, `…_CAWI_matrix`, `…_Mail_matrix`, Matrix-Splitliste), verlinkt auf der EVS-Seite „Participating countries … Survey 2017“ | Deutsch, CAPI-Fassung 123 Seiten mit Listenheft „Leben und Einstellungen in Deutschland 2017“ |
| Englische Masterfragebögen         | EVS 2017: access.gesis.org/dbk/66239; WVS7 mit gelber Markierung des gemeinsamen Kerns: access.gesis.org/dbk/69555                                                                                         | Englisch                                                                                |
| Zuordnung gemeinsamer Variablen    | gemeinsamer Variable Report – Documentation, access.gesis.org/dbk/69548 (ohne Häufigkeiten)                                                                                                                | Englisch                                                                                |

Die deutschen Wortlaute von WVS7 und EVS 2017 sind bei den gemeinsamen Kernfragen weitgehend identisch, etwa bei Q196–Q198 und v205–v207 oder bei Q111 und v204. Das passt dazu, dass dasselbe GESIS-Team beide Erhebungen betreut hat. Das ist eine Beobachtung am Text, kein Beleg zur Urheberschaft.

## 6. Relevante Fragen im Wortlaut

Aufgenommen sind nur Präferenzen oder Prinzipien. Wahrnehmungen, Vertrauen, Bewertungen der Regierung und eigenes Verhalten sind ausgeschlossen; Grenzfälle sind gekennzeichnet. Quelle ohne Zusatz: deutscher WVS7-Fragebogen (IHSN 101964). EVS-Angaben: `ZA7500_q_de_CAPI.PDF`.

### 6.1 Staatliche Überwachung

WVS7 Q196–Q198, PDF-S. 20; EVS 2017 Q58, v205–v207, PDF-S. 31; gemeinsame Variablen H009–H011. Wortlaut in beiden Studien gleich:

> „Sollte Ihrer Meinung nach der deutsche Staat das Recht zu folgenden Maßnahmen haben oder nicht?“
> Q196 „In der Öffentlichkeit Menschen per Video zu überwachen“
> Q197 „Alle E-Mails und Informationen, die im Internet ausgetauscht werden, zu überwachen“
> Q198 „Informationen über jede Person, die in Deutschland lebt, ohne deren Wissen zu sammeln“
> Antworten (aus dem Tabellenlayout zusammengesetzt): „Sollte auf jeden Fall das Recht dazu haben“, „Sollte wahrscheinlich das Recht dazu haben“, „Sollte wahrscheinlich nicht das Recht dazu haben“, „Sollte auf keinen Fall das Recht dazu haben“.

Nicht aufgenommen: WVS 2013 V186 „Staatliches Überwachen meines Telefons und meiner Korrespondenz“. Die Frage misst, wie stark jemand diese Bedrohung empfindet, also eine Wahrnehmung (IHSN 92374, PDF-S. 15).

### 6.2 Wirtschaftsordnung und Verteilung

WVS7 Q106–Q110, PDF-S. 9 („Auf dieser Liste sehen Sie gegensätzliche Meinungen zu verschiedenen Themen. Wo würden Sie Ihre eigenen Ansichten auf dieser Skala einordnen?“, Skala 1–10):

> Q106: 1 „Einkommen sollten stärker aneinander angeglichen werden.“ – 10 „Es sollte größere Anreize für persönliche Leistung geben.“
> Q107: 1 „Mehr staatliche Unternehmen sollten privatisiert werden.“ – 10 „Mehr private Unternehmen sollten verstaatlicht werden.“
> Q108: 1 „Der Staat sollte mehr Verantwortung dafür übernehmen, dass jeder Einzelne abgesichert ist.“ – 10 „Jeder Einzelne sollte mehr Verantwortung für sich selbst übernehmen.“
> Q109: 1 „Wettbewerb ist gut.“ – 10 „Wettbewerb ist schädlich.“

Q110 (harte Arbeit gegen Glück) ist eine Überzeugung über Erfolg und keine Präferenz; nicht aufgenommen. In EVS 2017 Q32 A, C, D, E (v103, v105–v107, PDF-S. 16) stehen dieselben Pole; nur bei v103 ist die Richtung gedreht (Abschnitt 4). Gemeinsame Variablen: E035, E036, E037, E039. Der englische Master formuliert Q107 als „Private ownership of business and industry should be increased“ gegen „Government ownership …“. Die deutsche Fassung spricht von Privatisierung und Verstaatlichung und ist damit konkreter.

Nur in EVS 2017:

> Q32 B (v104), PDF-S. 16: 1 „Arbeitslose sollten jede Arbeit machen müssen, die sie bekommen, oder ihre Arbeitslosenunterstützung verlieren.“ – 10 „Arbeitslose sollten Arbeit, die sie nicht machen möchten, ablehnen können.“
>
> Q62 (v221–v224), PDF-S. 33: „Was sollte eine Gesellschaft ihren Mitgliedern bieten? Bitte sagen Sie mir zu jeder Aussage, für wie wichtig Sie diese halten.“ v221 „Große Einkommensunterschiede zwischen den Bürgerinnen und Bürgern beseitigen“; v222 „Dafür sorgen, dass die Grundbedürfnisse von allen Menschen befriedigt sind: Nahrung, Wohnung, Kleidung, schulische Grundausbildung, Gesundheit“; v223 „Die Verdienste und Leistungen jedes Einzelnen anerkennen“; v224 „Die Bevölkerung vor Terrorismus schützen“. Antworten: sehr wichtig, ziemlich wichtig, nicht wichtig, überhaupt nicht wichtig.

Grenzfälle in WVS7 Q241–Q249, PDF-S. 25: „Viele Dinge sind wünschenswert, aber nicht alle davon sind notwendige Bestandteile einer Demokratie. Bitte sagen Sie mir für jedes der folgenden Dinge, inwieweit es für Sie ein notwendiger Bestandteil einer Demokratie ist.“ Dazu gehören Q241 „Der Staat besteuert die Reichen und unterstützt die Armen.“, Q244 „Arbeitslose Menschen erhalten staatliche Unterstützung.“ und Q247 „Der Staat sorgt für Gleichheit der Einkommen.“ Diese Fragen messen Demokratieverständnis, keine Steuer- oder Sozialpräferenz.

### 6.3 Umwelt gegen Wachstum

WVS7 Q111, PDF-S. 9; EVS 2017 Q57 (v204), PDF-S. 31; gemeinsame Variable B008. Wortlaut gleich:

> „Hier sind zwei Aussagen, die man hört, wenn über Umweltschutz und Wirtschaftswachstum geredet wird. Welche dieser beiden Aussagen kommt Ihrer eigenen Meinung näher?“
> 1 „Dem Umweltschutz sollte Vorrang eingeräumt werden, auch wenn dadurch das Wirtschaftswachstum sinkt und Arbeitsplätze verloren gehen.“
> 2 „Dem Wirtschaftswachstum und der Schaffung von Arbeitsplätzen sollte Vorrang eingeräumt werden, selbst wenn darunter die Umwelt etwas leidet.“
> 3 „Andere Antwort“, nur wenn spontan genannt.

WVS 2013 V81 weicht ab: „Dem Umweltschutz sollte mehr Aufmerksamkeit geschenkt werden …“ (IHSN 92374, PDF-S. 7).

### 6.4 Zuwanderungspolitik

> WVS7 Q130, PDF-S. 12, nur in WVS: „Und was denken Sie, wenn Menschen aus anderen Ländern zu uns kommen, um hier zu arbeiten. Wie sollte sich unsere Regierung verhalten?“ 1 „Alle ins Land lassen, die kommen möchten.“ 2 „Menschen kommen lassen, wenn es für sie einen Arbeitsplatz gibt.“ 3 „Die Anzahl von Ausländern, die hierher kommen, strikt beschränken.“ 4 „Die Zuwanderung von Menschen aus dem Ausland verbieten.“
>
> WVS7 Q34, PDF-S. 4, und EVS 2017 Q26 (v80), PDF-S. 14; gemeinsame Variable C002_01: „Wenn die Arbeitsplätze knapp sind, sollten die Arbeitgeber Deutsche gegenüber Ausländern vorziehen.“ Fünf Stufen von „Stimme voll und ganz zu“ bis „Stimme überhaupt nicht zu“.
>
> EVS 2017 Q52 D (v188), PDF-S. 28, nur in EVS: 1 „Es ist besser, wenn Ausländer ihre eigenen Bräuche und Traditionen beibehalten“ – 10 „Es ist besser, wenn Ausländer ihre eigenen Bräuche und Traditionen nicht beibehalten“.

Zu v188: Die Frage betrifft eine Präferenz zur kulturellen Anpassung, aber keine staatliche Maßnahme. Der englische Master sagt „immigrants“, die deutsche Fassung „Ausländer“. Das ist eine andere Gruppe.

Nicht aufgenommen: WVS7 Q121–Q129 und EVS v184–v187. Sie fragen nach Wirkungen der Zuwanderung, also nach Wahrnehmungen. Ebenfalls ausgeschlossen sind EVS Q53 (v189–v193): „Einige Menschen sagen, die folgenden Dinge seien wichtig, um wirklich deutsch zu sein …“. Das ist ein Verständnis von Zugehörigkeit, keine Frage zum Staatsangehörigkeitsrecht. Ich stufe es als Grenzfall ein.

Historisch, WVS 2006 Frage 46 (IHSN 92161, PDF-S. 16): „Viele Menschen aus anderen Ländern kommen nach Deutschland, um hier zu arbeiten. Welche Entscheidung sollte die Regierung Ihrer Meinung nach am ehesten treffen?“ Die vier Vorgaben haben dieselbe Struktur wie Q130.

### 6.5 Demokratie und Regierungsformen

WVS7 Q235–Q239, PDF-S. 24; EVS 2017 Q43 (v145–v148), PDF-S. 22, ohne das Item zu religiösen Gesetzen; gemeinsame Variablen E114–E117:

> „Ich werde Ihnen nun verschiedene Typen von politischen Systemen beschreiben und fragen, was Sie von jedem einzelnen als Regierungsform für unser Land halten. Sagen Sie mir bitte jeweils, ob Sie eine solche Regierungsform für unser Land sehr gut, ziemlich gut, ziemlich schlecht oder sehr schlecht finden.“
> Q235 „Man sollte einen starken Staatschef haben, der sich nicht um ein Parlament und um Wahlen kümmern muss.“
> Q236 „Anstelle der Regierung sollten Experten entscheiden, was das Beste für das Land ist.“
> Q237 „Das Militär sollte das Land regieren.“
> Q238 „Man sollte ein demokratisches politisches System haben.“
> Q239 „Man sollte ein System haben, das durch religiöse Gesetze regiert wird und in dem es keine politischen Parteien oder Wahlen gibt.“ (nur WVS)

Weitere Prinzipienfragen, nur in WVS7:

> Q42, PDF-S. 4: „Hier sind drei Grundhaltungen, die in unserer Gesellschaft zu finden sind. Bitte wählen Sie diejenige, die Ihrer Meinung am nächsten kommt.“ 1 „Unser gesellschaftliches System muss insgesamt durch einen radikalen Umsturz verändert werden.“ 2 „Unser gesellschaftliches System muss durch Reformen Schritt für Schritt verbessert werden.“ 3 „Unser derzeitiges gesellschaftliches System muss entschlossen vor jeglichen aufrührerischen Kräften geschützt werden.“
> Q150, PDF-S. 14: „Für die meisten Menschen sind Freiheit und Sicherheit wichtig. Wenn Sie wählen müssten, welches von beiden wäre für Sie wichtiger?“ 1 Freiheit, 2 Sicherheit.
> Q149, PDF-S. 13: dieselbe Form mit „Freiheit und Gleichberechtigung“.
> Q45, PDF-S. 5: „Mehr Respekt vor Autoritäten“, als Entwicklung, die man „begrüße“, die einem „egal“ ist oder die man „ablehne“.

Hinweise: Bei Q42 enthalten die Vorgaben selbst wertende Begriffe wie „radikaler Umsturz“ und „aufrührerische Kräfte“. Bei Q149 steht im englischen Master „equality“. Die deutsche Fassung sagt „Gleichberechtigung“, was im Deutschen oft gleiche Rechte meint, besonders zwischen den Geschlechtern. Beides wäre bei einer Aufnahme zu dokumentieren.

Historisch, WVS 2006 Frage 50 (IHSN 92161, PDF-S. 18): ein Demokratiemerkmal „Die Menschen können Gesetze in Volksabstimmungen ändern“. Es misst Demokratieverständnis, keine Präferenz für Volksentscheide.

### 6.6 Gleichstellung

WVS7 Q29–Q31, Q33, Q35, Q36, PDF-S. 3–4; EVS 2017 Q25–Q27 (v72–v82), PDF-S. 13–14. Beispiele:

> Q29 „In politischen Führungspositionen sind Männer allgemein besser als Frauen.“ Q33 „Wenn die Arbeitsplätze knapp sind, haben Männer eher ein Recht auf Arbeit als Frauen.“ Q36 „Gleichgeschlechtliche Paare sind genauso gute Eltern wie andere Paare.“

Diese Fragen messen Rollenbilder und Einstellungen, keine Politikmittel wie Quoten, Elterngeld oder Abstammungsrecht. Q33 deckt sich laut `docs/abdeckung-v2.2.md` inhaltlich mit einer schon genutzten ESS8-Frage; den ESS-Wortlaut habe ich hier nicht selbst verglichen.

Q249 „Frauen haben die gleichen Rechte wie Männer.“ (PDF-S. 25) misst Demokratieverständnis.

Q184 „Abtreibung“ steht in der Batterie Q177–Q195 (PDF-S. 19): „ob Sie dies unter keinen Umständen in Ordnung finden, in jedem Fall in Ordnung finden oder irgendetwas dazwischen“. Das ist ein Moralurteil, keine Präferenz zur Rechtslage nach § 218 StGB. Dasselbe gilt für Q188 „Sterbehilfe (das Leben unheilbar Kranker beenden)“ und Q195 „Todesstrafe“.

## 7. Themenabdeckung

### 7.1 Die sechs fehlenden Bereiche

| Bereich                                    | Originalfragen mit Präferenz oder Prinzip                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Bewertung                                                                                                                                                                                         |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arbeit und Rente                           | **Rente: keine.** Arbeitsmarkt: EVS v104 (Arbeit annehmen oder Unterstützung verlieren), eher Sozialstaat; nur bei GESIS. WVS7 Q34 und EVS v80 (Vorrang für Deutsche bei knappen Arbeitsplätzen), eher Migration. WVS7 Q39–Q41 (Arbeitsethos) sind Werte, keine Politik.                                                                                                                                                                                                                       | Nicht geschlossen. Rentenniveau, Eintrittsalter, Mindestlohn, Arbeitszeit, Tarifbindung: keine Frage gefunden.                                                                                    |
| Gesundheit und Pflege                      | Keine Politikfrage. Nur WVS7 Q38 und EVS v84: „Erwachsene Kinder haben die Pflicht, für die Betreuung und Pflege ihrer Eltern im Alter zu sorgen.“ Das ist eine Familiennorm und streift nur mittelbar die Frage, wer pflegen soll. Q188 Sterbehilfe ist ein Moralurteil. EVS v222 nennt Gesundheit nur in einem Bündel von Grundbedürfnissen.                                                                                                                                                 | Nicht geschlossen.                                                                                                                                                                                |
| Wohnen                                     | Keine. Wohnung erscheint nur im Bündel EVS v222.                                                                                                                                                                                                                                                                                                                                                                                                                                            | Nicht geschlossen.                                                                                                                                                                                |
| Außen-, Verteidigungs- und Friedenspolitik | WVS7 Q152–Q153 und EVS Q33 (gemeinsam E001–E002): Rangfolge von vier Landeszielen, darunter „Für eine starke Landesverteidigung sorgen“ (PDF-S. 14); misst relative Priorität, keine Maßnahme. WVS7 Q90 (internationale Organisationen „wirksame oder demokratische Arbeitsweise“, PDF-S. 8): Prinzip der globalen Ordnung. Historisch: WVS 2013 V187 „Unter bestimmten Bedingungen ist Krieg notwendig zur Aufrechterhaltung des Rechts“ (IHSN 92374, PDF-S. 15); WVS 2006 Frage 60–61 (Höhe der Entwicklungshilfe), Frage 63 (Armut in der Welt oder eigene Probleme), Frage 64 (Friedenssicherung, Hilfe an arme Länder, Flüchtlinge besser national, durch die EU oder die UN geregelt; IHSN 92161, PDF-S. 21–22). Ausgeschlossen: Q151 „bereit, für Ihr Land zu kämpfen“ (eigenes Verhalten), Q65 und Q86 Vertrauen in Bundeswehr und NATO, Q146 Sorge vor Krieg. | Nicht geschlossen. Ukraine, Verteidigungsausgaben, Wehrpflicht, Rüstungsexporte, NATO, Handel: keine Frage. Die historischen Fragen von 2006 und 2013 liegen 13 bis 20 Jahre zurück.                     |
| Bildung und Forschung                      | WVS7 Q44 „Mehr für den technischen Fortschritt tun“ (begrüßen oder ablehnen, PDF-S. 5) ist allgemein und nennt kein Politikmittel. Q158–Q163 messen Einschätzungen der Wissenschaft. Q30 und EVS v77 messen ein Rollenbild.                                                                                                                                                                                                                                                                       | Nicht geschlossen.                                                                                                                                                                                |
| Medien und Digitalpolitik                  | WVS7 Q197 und EVS v206 „Alle E-Mails und Informationen, die im Internet ausgetauscht werden, zu überwachen“. Ausgeschlossen: Q117 Korruption bei Journalisten, Q66–Q67 Vertrauen in Presse und Fernsehen, Q226 und Q228 Wahrnehmungen der Wahlberichterstattung, Q201–Q208 Mediennutzung.                                                                                                                                                                                                         | Teilweise: staatliche Internetüberwachung. Rundfunkbeitrag, Plattformregulierung, Hassrede, KI-Regulierung: keine Frage.                                                                           |

### 7.2 Größere Lücken in vorhandenen Bereichen

| Bereich (Lücke laut `abdeckung-v2.2.md`)                                         | Originalfragen                                                                                                                         | Bewertung                                                                                                                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bürgerrechte und Sicherheit: Überwachung außerhalb der Pandemie, Gesichtserkennung | WVS7 Q196–Q198 (= EVS v205–v207); Q150 Freiheit oder Sicherheit; EVS v224 Schutz vor Terrorismus                                       | Inhaltlich der stärkste Beitrag. Die Fragen sind allgemein gefasst und nennen keine konkrete Technik wie Gesichtserkennung oder Speicherfristen.                               |
| Wirtschaft und Verteilung: Marktordnung, Regulierung, Steuern                     | WVS7 Q106, Q107, Q109 (= EVS v106, v107, v105); EVS v221, v223                                                                         | Prinzipien der Wirtschaftsordnung abgedeckt. Steuerprogression, Schuldenbremse, Mindestlohn: keine Frage.                                                                      |
| Sozialstaat: Bürgergeld, Sanktionen                                               | EVS v104 (nur GESIS); WVS7 Q108 (= EVS v103)                                                                                           | v104 passt inhaltlich zur Sanktionsfrage, ist aber nur über GESIS erhältlich. Q108 ist allgemein; das Profil hat bereits spezifischere ESS8-Fragen.                           |
| Demokratie: Reformen, Expertenregierung                                           | WVS7 Q236, Q237, Q239; Q42; Q45                                                                                                        | Neu gegenüber dem Profil sind die Expertenregierung und die Militärregierung. Q235 ähnelt laut Matrix der ESS10-Frage zur starken Führungsperson; den Wortlaut habe ich nicht verglichen. Wahlalter und Volksentscheide: keine aktuelle Frage. |
| Europäische Integration: Erweiterung                                              | EVS Q55 (v198), nur GESIS                                                                                                               | Inhaltlich passend, aber gesperrt wie GLES. Zum Zeitbezug siehe Abschnitt 8.                                                                                                   |
| Klima und Energie                                                                 | WVS7 Q111 (= EVS v204)                                                                                                                  | Allgemeine Abwägung, die im Profil laut Matrix fehlt. Gebäude, Verkehr, Tempolimit: keine Frage.                                                                               |
| Migration: Grenzkontrollen, Rückführung, Integration, Staatsangehörigkeit          | WVS7 Q130; Q34 (= EVS v80); EVS v188 (nur GESIS)                                                                                       | Q130 ist eine allgemeine Frage zur Begrenzung der Arbeitsmigration und unterscheidet sich von ESS10 (Herkunftsgruppen). Die genannten Einzellücken bleiben offen.               |
| Gleichstellung: Schwangerschaftsabbruch, Frauenquote, Sprache, trans Personen      | keine Politikfrage; Q184 ist ein Moralurteil                                                                                           | Nicht geschlossen.                                                                                                                                                             |

## 8. Eignung als Vergleich

- **Veröffentlichte Tabellen.** Laut gemeinsamem Bericht (PDF-S. 7) liefert der „Variable Report–Tables“ „frequency counts for almost all variables. Results are weighted by gwght and usually broken down by country/territory.“ Länder mit beiden Studien erscheinen „by country/study“, Deutschland also getrennt nach EVS und WVS. Ob die Tabellen ungewichtete Basen, „Weiß nicht“ und fehlende Werte getrennt ausweisen, weiß ich nicht, weil ich sie ergebnisblind nicht geöffnet habe. Solche Tabellen könnten Anteile je Kategorie für Deutschland liefern, aber nur für die gemeinsamen Kernfragen. Q130, Q42, Q90, Q149, Q150 und Q239 gehören nicht zum gemeinsamen Kern; für sie gäbe es nur die WVS-Länderergebnisse, die hinter dem WVS-Formular liegen. Ob das Zeigen solcher Tabellenwerte auf einer Website unter die Bedingungen fällt, ist offen (Abschnitt 3).
- **Wählergruppen brauchen Einzeldaten.** WVS7 Q223 lautet: „Wenn morgen Bundestagswahl wäre, welche Partei würde Sie dann wählen?“ (sic, PDF-S. 23). Das ist eine Wahlabsicht kurz nach der Bundestagswahl 2017. EVS Q49 lautet: „Welcher politischen Partei stehen Sie am nächsten?“ (PDF-S. 26). Das profilprägende ESS-Merkmal ist die erinnerte Zweitstimme. Gruppen aus WVS oder EVS wären also anders definiert und müssten anders benannt werden. Mit 1.528 WVS-Fällen werden kleine Parteigruppen klein. Eine Zahl habe ich nicht berechnet.
- **Gewichte.** Für WVS7 Deutschland sind die Angaben widersprüchlich: Der nationale Bericht sagt, das deutsche Team habe kein Gewicht geliefert. Die gemeinsame Dokumentation nennt `gwght` aus der Quelldatei. Das muss jemand vor einer Nutzung an der Datei selbst prüfen. EVS 2017 hat dokumentierte Kalibrierungs- und Designgewichte.
- **Kombination.** Laut Sample-Design-Dokument sind die WVS- und die EVS-Stichprobe „representative for Germany on their own and also in combination“. Für gemeinsame Kernfragen ließen sich beide Stichproben verbinden. Das bringt aber den EVS-Teil und damit die GESIS-Frage (Abschnitt 3.4) ins Spiel; außerdem enthält EVS Web- und Postfälle. Das ist eine Methodenentscheidung für einen eingefrorenen Plan, keine Empfehlung von mir.
- **Zeitbezug.** Die Feldzeit liegt 2017/18, also etwa acht Jahre vor 2026, ähnlich wie die bereits genutzten ESS8-Fragen von 2016/17. Bei EU-Erweiterung und staatlicher Überwachung kann sich der Bezugsrahmen seither verschoben haben. Belege dafür habe ich nicht geöffnet; das wäre wie in R3 Abschnitt 2.3 eigens zu prüfen.
- **Aktualisierung.** Die EVS-Seite zur Welle 2026 meldet: „The newest wave of EVS data is currently underway!“ Ob und wann Deutschland erhoben wird, habe ich nicht gefunden. Die Daten kämen wieder über GESIS. Auf der WVS-Seite zur Welle 8 (2024–2026) ist Deutschland nicht unter den genannten Ländern; den WVS-8-Fragebogen habe ich nicht geprüft.

## 9. Prüfung der Aussage aus dem externen KI-Review

Den Text des Reviews (GPT-6.1-Sol) habe ich nicht gesehen. Ich prüfe nur die im Auftrag wiedergegebene Aussage: Der WVS sei eine Alternative, und es brauche eine systematische Prüfung von Nutzungsrechten und Themenabdeckung.

Der Kern der Aussage stimmt. WVS7 Deutschland gibt nicht GESIS ab, sondern das WVS-Archiv, und auf den geöffneten WVS-Seiten steht keine KI-Klausel. Drei Einschränkungen gehören aber dazu:

1. Eine fehlende Regel ist keine Erlaubnis. Die WVS-Bedingungen verlangen „non-profit purposes“ und die Meldung jeder Veröffentlichung. Zu Website und Fragetexten sagen sie nichts Klares.
2. Die EVS ist ein GESIS-Weg und hat dieselbe Sperre wie GLES, ISSP und ALLBUS.
3. Inhaltlich schließt der WVS die sechs fehlenden Bereiche nicht. Er ergänzt einige Prinzipienfragen in Bereichen, die das Profil schon hat. Für Außen-, Gesundheits-, Wohn-, Renten-, Bildungs- und Digitalpolitik ersetzt er GLES und ISSP nach diesem Befund nicht.

## 10. Empfehlung je Bereich

Priorität heißt hier: lohnt die Klärung zuerst. Es ist keine Aufnahmeentscheidung. Jede Aufnahme bräuchte einen vorab eingefrorenen Plan und die Entscheidung von Steven.

| Bereich                                    | Kandidaten                                   | Priorität              | Voraussetzungen                                                                                                                                                       | Offene Fragen für Steven                                                                                                                         |
| ------------------------------------------ | -------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bürgerrechte und Sicherheit                | WVS7 Q196–Q198, Q150                         | hoch                   | Steven lädt die WVS7-Länderdatei selbst über das Formular und stimmt den Bedingungen zu; schriftliche Klärung mit der WVSA (Abschnitt 11, Punkte 1–3)                  | Reicht eine Klärung mit der WVSA, oder will Steven zusätzlich GESIS als Auftraggeberin der deutschen Erhebung fragen?                             |
| Wirtschaft und Verteilung                  | WVS7 Q106, Q107, Q109                        | mittel bis hoch        | wie oben; Abgleich mit ESS11 `gincdif`, damit keine Doppelung entsteht                                                                                                  | Sollen allgemeine Prinzipienskalen neben konkreten ESS-Maßnahmen stehen?                                                                          |
| Klima und Energie                          | WVS7 Q111                                    | mittel                 | wie oben                                                                                                                                                              | Passt eine allgemeine Abwägung zum Profil mit konkreten ESS8-Maßnahmen?                                                                           |
| Migration                                  | WVS7 Q130, Q34                               | mittel                 | wie oben; Hinweis, dass Q130 Arbeitsmigration und „Ausländer“ nennt                                                                                                    | Ist die Begrenzungsfrage von 2017/18 neben ESS10 als Vergleich sinnvoll?                                                                          |
| Demokratie                                 | WVS7 Q236, Q237; vorsichtig Q42              | mittel; Q42 niedrig    | wie oben; bei Q42 die wertenden Vorgaben dokumentieren                                                                                                                 | Q235 nur aufnehmen, wenn sie sich von der ESS10-Frage klar unterscheidet?                                                                        |
| Sozialstaat                                | EVS v104                                     | inhaltlich hoch, gesperrt | GESIS-Ausnahme nach §4 oder kein Weg; v104 ist nicht in der gemeinsamen Datei                                                                                          | Gehört v104 in die GESIS-Anfrage?                                                                                                                |
| Europäische Integration                    | EVS v198                                     | inhaltlich mittel, gesperrt | wie v104                                                                                                                                                         | wie v104                                                                                                                                         |
| Gleichstellung                             | keine Politikfrage                           | niedrig                | –                                                                                                                                                                     | –                                                                                                                                                |
| Außen-, Verteidigungs- und Friedenspolitik | WVS7 Q152 (Rangfrage), Q90; historisch WVS 2013 V187, WVS 2006 Fragen 60–64 | niedrig | Rangfrage als relative Priorität kennzeichnen; historische Fragen nur mit deutlichem Zeitvermerk                                                                         | Sind Fragen von 2006 und 2013 überhaupt vertretbar? Meine Einschätzung: eher nicht.                                                              |
| Medien und Digitalpolitik                  | WVS7 Q197 als Querbezug                      | niedrig bis mittel     | im Bereich Bürgerrechte führen und unter Digitalpolitik nur verweisen                                                                                                   | –                                                                                                                                                |
| Arbeit und Rente, Gesundheit und Pflege, Wohnen, Bildung und Forschung | keine                            | –                      | WVS und EVS sind hier kein Weg                                                                                                                                        | Sollen R6 und R7 oder eine GESIS-Ausnahme diese Bereiche tragen?                                                                                 |

## 11. Offene Punkte

1. **Klärung mit der WVSA (Steven, schriftlich).** Ist die Arbeit mit KI-Systemen (Codex, Claude) an WVS7-Daten zulässig, also Lesen, Skripte schreiben und Ausführen? Darf eine nichtkommerzielle öffentliche Website zusammengefasste Anteile und die deutschen Fragewortlaute zeigen? Gilt eine dauerhafte Website als „publication“ im Sinne der Meldepflicht? Kontakt laut WVS-Seiten: wvsa.secretariat@gmail.com.
2. **Nichtkommerzielle Nutzung.** Steven muss bestätigen, dass das Projekt „non-profit“ ist. Eine Definition fehlt bei der WVS; das IVS-Blatt erläutert den Begriff mit „scientific publications, research, teaching and similar“.
3. **Rechte an der deutschen Übersetzung.** Der deutsche WVS7-Fragebogen entstand für GESIS. Ob GESIS, Kantar oder die WVSA die Anzeige freigeben müssen, ist offen.
4. **Gemeinsame Datei.** Gilt die GESIS-Klausel für den EVS-Teil auch bei Bezug über worldvaluessurvey.org? Ohne schriftliche Antwort sollte das Projekt diesen Weg nicht nutzen.
5. **Fragebogenquelle.** Die geprüften deutschen WVS-Fragebögen stammen aus dem IHSN-Katalog. Für eine Veröffentlichung sollte Steven die offizielle Fassung über das WVS-Formular beziehen und mit der IHSN-Kopie abgleichen.
6. **Gewicht WVS7 Deutschland.** Vor einer Nutzung ist an der Datei zu prüfen, ob eine Gewichtsvariable (im gemeinsamen Bericht `gwght`) für Deutschland belegt ist. Das kann erst geschehen, wenn Steven die Daten geladen hat.
7. **Wählergruppen.** Wahlabsicht (WVS) und Parteinähe (EVS) sind andere Konstrukte als die erinnerte Zweitstimme. Steven sollte entscheiden, ob Gruppenvergleiche für diese Fragen entfallen oder anders benannt werden.
8. **Nicht geprüft:** WVS-8-Fragebogen, Stand der EVS 2026 in Deutschland, die Fragebögen WVS 1997 West und EVS 1990, 1999 und 2008, Zugangskategorie von ZA7500 und ZA7505 auf der GESIS-Seite (HTTP 403).

---

## Anhang A: Tatsächlich geöffnete Quellen (3.10.2026, Zeiten UTC)

WVS (worldvaluessurvey.org):

- https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp, 20:55
- https://www.worldvaluessurvey.org/AJDocumentation.jsp?CndWAVE=7&COUNTRY=, 20:55; dieselbe Seite mit CndWAVE=1 bis 6, ca. 21:04
- https://www.worldvaluessurvey.org/AJDocumentationSmpl.jsp (POST, Germany 2018, SAID 3310), 20:55; für Wellen 3, 5, 6 ca. 21:05
- https://www.worldvaluessurvey.org/AJDownload.jsp (POST, DOID 6609, Antwort 1 Byte, keine Datei), 20:56
- https://www.worldvaluessurvey.org/AJDownloadLicense.jsp (DOID 6609, 20:57; DOID 12153, ca. 21:10; Formular nicht abgeschickt)
- https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=Documentation, …=DataDoc, …=wvswave7, …=QuestDevelopment, 20:57; …=Faqs, …=instmemb, 21:03
- https://www.worldvaluessurvey.org/WVSNewsShow.jsp?ID=427, 20:59
- https://www.worldvaluessurvey.org/WVSEVSjoint2017.jsp, ca. 21:09

IHSN:

- https://catalog.ihsn.org/catalog/11570 (mit /related-materials, /get-microdata, /metadata/export/11570/ddi, nur Studienfelder ausgewertet), 20:56–20:58
- https://catalog.ihsn.org/catalog/11570/download/101964, 101965, 101966, 101967, 20:57
- IHSN-Katalogsuche „World Values Survey Germany“, ca. 21:05
- https://catalog.ihsn.org/catalog/9040/related-materials sowie Downloads 92374, 92375 (nur Feldzeit und Modus per Suche), 92376 (nicht gelesen), 92377, ca. 21:05–21:07
- https://catalog.ihsn.org/catalog/8997/related-materials sowie Downloads 92161, 92162, 92163, 92164, ca. 21:06–21:08
- https://catalog.ihsn.org/catalog/9097/related-materials sowie Downloads 92557, 92559, ca. 21:06–21:08

GESIS (access.gesis.org/dbk/…, ohne Anmeldung):

- 69548 gemeinsamer Variable Report – Documentation, vollständig, 20:59
- 65190 EVS 2017 Variable Report, nur PDF-S. 1–46 (PDF-S. 1 und 9–46 zur Seitenprüfung ca. 21:17), 21:00
- 65197 EVS 2017 Method Report, Länderbericht Deutschland, Stichproben- und Ausschöpfungstabellen, 21:00–21:01
- 66239 EVS-Masterfragebogen CAPI, 21:00
- 69555 WVS7-Masterfragebogen, 21:00
- 69491 EVS 2017 Weighting Data, ca. 21:12
- 65192, 65193, 65195, 66240, 69455: nur Titelseite, 21:00
- 69456 (leere Antwort) und 69486 (ZIP, nicht geöffnet), 21:00
- 66247 deutsche EVS-Fragebögen (ZIP; CAPI-Fassung gelesen), 21:02
- 71029 IVS Conditions of Use, 21:03
- 69550 gemeinsame Länderliste (Excel), 21:03
- 71043 IVS-Länderliste (Excel), 21:03
- 69553 Variable Correspondence (Excel), geladen, nicht ausgewertet, 21:03

GESIS (HTTP 403): https://www.gesis.org/en/european-values-study/data-and-documentation/joint-evs/wvs-2017-2022-dataset, https://www.gesis.org/en/european-values-study/data-and-documentation/5th-wave-2017, https://search.gesis.org/research_data/ZA7505, https://search.gesis.org/research_data/ZA7500 (auch per WebFetch), https://www.gesis.org/en/institute/data-usage-terms, ca. 20:59–21:11.

Internet Archive: http://web.archive.org/web/20260330154523/https://www.gesis.org/fileadmin/upload/Datenservices/Nutzungsbedingungen/Nutzungsbedingungen.pdf, ca. 21:11. Die Verfügbarkeitsabfrage für das GESIS-Impressum meldete „Temporarily Offline“, ca. 21:12.

EVS (europeanvaluesstudy.eu), ca. 21:02:

- Startseite
- /surveys/data-access/
- /surveys/surveys-evs/evs-2017/participating-countries-and-country-information-survey-2017/
- /surveys/evs-wvs-collaborations/joint-evs-wvs/data-and-documentation-joint-evs-wvs/
- /surveys/evs-wvs-collaborations/integrated-values-surveys/data-and-documentation/
- /surveys/surveys-evs/survey-2026/
- Geladen, nicht ausgewertet: /surveys/surveys-evs/evs-2017/ und /surveys/surveys-evs/evs-2017/documentation-survey-2017/
- HTTP 404: /methodology-data-documentation/survey-2017/full-release-evs2017/, /methodology-data-documentation/survey-2017/joint-evs-wvs/data-and-documentation-joint-evs-wvs/, /surveys/surveys-evs/survey-2026-outline/

Repository: `AGENTS.md`, `docs/project.md`, `docs/abdeckung-v2.2.md`, `reports/claude/auftraege/R5-wvs.vollstaendig.md`, `R5-wvs.md`, `R-alternativen-gemeinsam.md`, Kopf von R1 und Abschnitt 6 von R2.

## Anhang B: Ausgeführte Befehle in Kurzform

- `curl` für HTML und PDF in `/tmp/r5wvs`, darunter POST-Abrufe der WVS-Dokumentationsrahmen ohne Formulardaten
- `pdftotext -layout` und `pdfinfo`; beim EVS Variable Report nur Seiten 1–46
- Python-Skripte für HTML zu Text, Seitenzuordnung über Seitenvorschübe, Auslesen von XLSX ohne Zusatzbibliothek und Auswertung der DDI-Studienfelder
- `unzip` für das GESIS-ZIP der deutschen EVS-Fragebögen
- `grep`, `sed`, `awk` zur Suche in den Textauszügen
- WebSearch (8 Abfragen, nur zum Finden von Seiten); WebFetch (1 Abruf, HTTP 403)
- `git log`, `ls`, `grep` im Repository; `prettier --check` für diese Datei

## Anhang C: Grenzen der eigenen Prüfung

- Keine Rechtsprüfung. Die Abschnitte 3 und 11 stellen Wortlaute fest und nennen offene Fragen.
- Die Nutzungsbedingungen von GESIS stammen aus einem Wayback-Schnappschuss vom 30.03.2026, nicht vom Live-Server. Die GESIS-Studienseiten konnte ich nicht öffnen; die Zugangskategorien von ZA7500 und ZA7505 sind deshalb nicht selbst geprüft.
- Die deutschen WVS-Fragebögen stammen aus IHSN-Kopien. Ob sie mit den WVS-Originaldateien übereinstimmen, ist nicht geprüft.
- Ich habe nur die deutschen CAPI-Fragebögen von WVS7 und EVS 2017 vollständig nach Fragen durchgesehen. Die EVS-Fassungen für Web, Post und Matrix habe ich nicht verglichen. WVS 2006 und 2013 habe ich nur gezielt durchsucht. WVS 1997 West, EVS 1981, 1990, 1999 und 2008 habe ich nicht geprüft.
- ESS-Wortlaute habe ich nicht selbst mit WVS und EVS verglichen. Aussagen zu Überschneidungen stützen sich auf `docs/abdeckung-v2.2.md`.
- Die Einordnung „Präferenz oder Prinzip“ gegenüber „Wahrnehmung, Norm, Moralurteil“ ist meine Einschätzung. Ein zweiter Prüfer sollte sie gegenlesen.
- Ob Bezugsrahmen sich seit 2017/18 verschoben haben (EU-Erweiterung, Überwachung), habe ich nicht mit Quellen geprüft.
- Mehrspaltige Antwortkategorien habe ich aus dem PDF-Layout zusammengesetzt. Kleine Abweichungen in Zeichensetzung oder Umbruch sind möglich.

## Anhang D: Modell

Laut Systemangabe der Laufzeitumgebung: Claude Opus 5.5 (Modell-ID `claude-opus-5-5[1m]`). Einen weiteren technischen Beleg habe ich nicht. Ich bin ein getrennter Subagent ohne Zugriff auf Ergebnisse anderer Agenten, außer den genannten Repository-Dateien.
