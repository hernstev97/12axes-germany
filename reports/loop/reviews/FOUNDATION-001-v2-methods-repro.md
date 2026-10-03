# FOUNDATION-001-v2: unabhängige Nachprüfung Methoden und Reproduktion

Stand: 2026-10-03. Reviewerrolle: unabhängiger Korrekturprüfer, kein Autor der geprüften Fassung. Dieser Bericht betrifft das eingefrorene FOUNDATION-Paket und öffentliche beziehungsweise erfundene Inputs.

Die zwölf angenommenen Findings aus Runde 1 sind in ihrem jeweils korrigierten dokumentarischen oder synthetischen Umfang nachvollziehbar. Ich habe keine neue erhebliche Beanstandung in diesem Umfang gefunden. Die Korrekturen liefern weiterhin keine empirische, methodische Gesamt-, Modell- oder Phasenfreigabe. Insbesondere sind die Geschlechter-Messentscheidung, eine gemeinsame Klimanorm, der reale Mischdesignvertrag, die persönliche Messunsicherheit und die vollständige Inventarabnahme offen.

## Fassung, Trennung und tatsächlicher Zugriff

Maßgeblich ist `reports/loop/packages/FOUNDATION-001/v2/manifest.json`, SHA-256 `10157ee7bca65ca0b92707e673bc75c3698c4d1acc6664da421b7b218e7a1988`, Freeze `2026-10-03T03:29:53.771764+00:00`. Die 42 eingefrorenen Dateien und alle 101 gebundenen öffentlichen/synthetischen Inputs hatten zu Beginn die erwarteten Hashes. Ausgangsfassung v1: Manifest-SHA `213eec2fba90ae60594323f1e52c39ed77d49af4656f3eea481c6300ecc0c5bb`; auch deren 25 Dateien und 36 Inputs wurden byteweise abgeglichen. Die abschließende Wiederholung steht in `outputs/loop/foundation-v2-methods/identity-after.json`; Anfangsbeleg ist `identity-before.json`. Hashidentität belegt die Fassung, keine inhaltliche Güte.

In diesem Bericht bedeutet `F/<Pfad>` stets `reports/loop/packages/FOUNDATION-001/v2/files/<Pfad>`. `O/<Pfad>` bedeutet den eigenen Schreibort `outputs/loop/foundation-v2-methods/<Pfad>`. Der Codecommit im Manifest ist `866a6c6fa0a1215ea743ccc6c969ec320224a80e`; die eingefrorenen Bytes haben Vorrang.

Gelesen wurden die eingefrorenen AGENTS-Regeln, Mandate, LIFE-93-Auftrag und Issuefassung, Arbeitsloop, Prüfregeln, Analyseplan, Lizenzen und Belegregister; der Methodenentwurf P01–P13, die Konstrukt- und Literaturergänzungen, die einschlägigen Themen-/Erwartungspassagen, Quellenregister, Parser und synthetischen Verträge. Die fünf ausdrücklich erlaubten, abgeschlossenen Erstberichte `FOUNDATION-001-{sources,politics,methods,neutrality,repro}.md`, ihre eingebetteten Aufträge, Autorentscheidungen, Korrekturbericht, drei ursprüngliche Autorenberichte und drei gebundene ursprüngliche Autorenaufträge wurden gelesen. Das sind historische Inputs, keine aktuellen Nachprüferurteile.

Keine anderen v2-Nachprüfberichte, aktuellen PREP-/SOFTWARE-Berichte oder weitere Autorenverteidigungen wurden gelesen. Es gab keine Rücksprache über die Bewertung; dem Koordinator wurde lediglich der eigene Arbeitsstand gemeldet. Keine zusätzlichen Agents eingesetzt. Gemeinsames Dateisystem und gemeinsame Toolumgebung sind keine technisch erzwungene Isolation. Die Trennung wurde durch den erlaubten Lesebereich, eigene Schreiborte und wiederholte Hashkontrolle eingehalten.

Keine Rohdaten, `data/raw/`, `data/local/`, Antworten, Personenkennungen, B, tatsächliche Partei- oder Links-Rechts-Werte geöffnet. Die Raw-Hashangabe im Manifest wurde nur als Metadatum gesehen und nicht durch Öffnen der betreffenden Datei kontrolliert. Öffentliche Frage-IDs, Frageformulierungen, Antwortkategorien und Filter wurden verwendet. Keine Portal-Analysis, Cookies, Credentials oder privaten Browserzustände abgefragt. Keine gemeinsamen Forschungsdateien geändert; keine Installation, Commit, Push, Merge, Deployment oder Tags. Alle eigenen Dateien liegen unter O, außer diesem Bericht.

Laufzeitangabe des Koordinators: geerbtes Codex `gpt-6.1-sol`, Reasoning `ultra`. Interne Modellrevision und Anbieterregeln sind unbekannt; diese Angaben wurden nicht durch interne Introspektion verifiziert. Verwendet wurden `functions.exec`, `exec_command`, `write_stdin`, `apply_patch`, `view_image` und `web__run`; Python, NumPy, Poppler und BeautifulSoup für eigene öffentliche/synthetische Belege. Die Skills `unslop` und `pdf` wurden gelesen und angewandt. Kein Computer-Use-Browser nötig, kein fremder Reviewdienst. Keine Gedächtnisquelle verwendet.

Eigene Umgebung: Python 3.14.7, NumPy 2.5.3, Poppler 26.08.0; Rscript und Mplus nicht im PATH. Das ist eine lokale Verfügbarkeitsbeobachtung, keine vollständige Systeminventur.

## Die zwölf ursprünglichen Findings

Die IDs und Schweregrade aus Runde 1 bleiben erhalten. F-P02 und FM-F01 sind derselbe Fehler mit zwei ursprünglichen IDs; sie werden nicht als zwei unabhängige Belege oder Abstimmungen gezählt. `BESTANDEN` in den folgenden Einträgen gilt nur für die ausdrücklich benannte Korrektur und Nachprüfung.

### F-S01 — niedrig: unzutreffend beschriebener Quellenlesebereich

**Ursprünglicher Claim/Fundstelle:** `data/methoden-quellen.json`, ESS11-COUNTRY/readScope, beschrieb S. 82–86 als Stichproben-/Rahmenlektüre. Das konnte eine nicht geleistete Designprüfung suggerieren.

**Korrektur und eigener Beleg:** F/data/methoden-quellen.json, Eintrag ESS11-COUNTRY, nennt jetzt historische Feldarbeitslektüre S. 79–81, Kontrollmetadaten S. 82–85 und Regionenwarnung S. 86. Ich habe diese Originalseiten des gehashten Country Reports `007be2a…9d850` selbst textuell gelesen. Sie tragen diese engere Beschreibung, einschließlich der Grenze für Aussagen über Bundesländer. Das Original ist der ESS11 Country Documentation Report edition 04; sein Abrufzeitpunkt bleibt als historischer Autorzeitpunkt markiert.

**Nachprüfung/Impact:** BESTANDEN für die korrigierte Reichweite. Die Behauptung einer vollständigen deutschen Samplingprüfung wird nicht mehr erhoben. Die historische Lektüre selbst bleibt eine Autorangabe; mein heutiges Lesen beweist sie nicht rückwirkend. Eine vollständige Sampling-Procedure-/Metadaten-Reconciliation wurde hier nicht geprüft und ist vor Designfreigabe weiterhin erforderlich. Keine fehlgeschlagene empirische Prüfung.

### F-P01 — mittel: B37-Anker überinterpretiert

**Ursprünglicher Claim/Fundstelle:** Erwartungsmodell B37 leitete vom niedrigen Integrationsanker eine Rücknahmepräferenz ab. Die Originalfrage fragt nach der Bewertung des Integrationsstands und weiterer Integration.

**Korrektur und eigener Beleg:** F/docs/erwartungsmodell.entwurf.md:38 und der Korrekturhinweis ab :65 beschreiben die tatsächlichen Anker und schließen eine konkrete Rücknahmepräferenz aus. Ich habe DE-Q PDF S. 14 textuell und visuell nachgelesen; C43 auf S. 31 wurde getrennt als hypothetische Referendumsfrage gelesen. Die zwei Fragen werden nicht gleichgesetzt.

**Nachprüfung/Impact:** BESTANDEN für die engere Aussage. Keine Itemaufnahme, Polung oder breite EU-Dimension wird dadurch bestätigt. Die alte stärkere Handlungsaussage dürfte eine spätere Interpretation nicht mehr tragen.

### F-P02 — mittel: feste LR-Abschnitte statt Terzilen

**Ursprünglicher Claim/Fundstelle:** Methodenentwurf P10 schlug feste Abschnitte 0–3/4–6/7–10 vor, während der eingefrorene LIFE-93-Auftrag Phase 4 Terzile verlangt.

**Korrektur und eigener Beleg:** F/docs/analyseplan-methoden.entwurf.md:133 spezifiziert gewichtete inverse-CDF-Grenzen bei 1/3 und 2/3, gültige historische deutsche LR-Referenz mit positivem `anweight`, fehlende/verweigerte Antworten außerhalb dieser Verteilung, ungeteilte Antwortkategorien, Ausfall bei gleichen Grenzen oder leerer Gruppe und gemeinsame Grenzen für sämtliche Dimensionen/Masks. Zeitpunkt: Phase 4 nach abgeschlossenem blindem Modell, einmal vor Gruppenmodellen protokollieren. F/pipeline/synthetic/planvertraege.py ist eine synthetische Hilfsfunktion, kein Zugriffsgate.

**Nachprüfung/Impact:** BESTANDEN für diesen Vertragsvorschlag und die erfundenen Gegenfälle. Die fünf vorhandenen Vertragsprüfungen und 1.024 zusätzliche Gewichtskombinationen wurden ausgeführt; Details unten. Der Zeitpunkt wurde am Dokument kontrolliert, nicht durch einen echten Datenworkflow getestet. Tatsächliche Grenzen, Ausfälle, Präzision, Invarianz und Unsicherheit sind NICHT_GEPRÜFT. Keine LR-Verteilung wurde geöffnet.

### FM-F01 — mittel: dieselbe Terzilabweichung

**Ursprünglicher Claim/Fundstelle:** Der Methoden-Erstbericht beanstandete dieselbe feste P10-Gruppierung wie F-P02.

**Korrektur, Beleg, Impact und Nachprüfung:** Identische Nachprüfung wie F-P02, ursprüngliche ID separat erhalten. BESTANDEN ausschließlich für Spezifikation und synthetische Hilfsrechnung; keine zweite unabhängige empirische Bestätigung. Der reale Phase-4-Vergleich bleibt von blindem Modell, Metadaten-, Präzisions- und Invarianzfreigaben abhängig.

### F-P03 — hoch für spätere Konstruktfreigabe: Originalpaare und Messannahme

**Ursprünglicher Claim/Fundstelle:** Die eigene Gruppierung des Geschlechtermoduls verdeckte Originalpaare und einen reflektiv/formativ-Widerspruch. Original-Modulvorschlag PDF S. 11, 26, 29–33: E23/E24 HOSTILE, E25/E26 MODERN, E27/E28 BENEVOLENT; E15–E18 in Übersicht versus Detail widersprüchlich beschrieben.

**Korrektur und eigener Beleg:** F/docs/konstruktakten.entwurf.md:11–14 dokumentiert Paare und Widerspruch. F/docs/analyseplan-methoden.entwurf.md:49 erlaubt kein fachfremdes drittes Item, um den Vorschlag mindestens dreier Indikatoren formal zu erfüllen. Ich las Original-PDF S. 11, 26, 29–33, mit visueller Kontrolle 11/26/30/32, und DE-Q S. 51–54. Die Paare, unterschiedlichen Antwortgegenstände und widersprüchlichen Messannahmen sind am Original nachvollziehbar. Gleiche Antwortform erzeugt keine gemeinsame Konstruktaussage.

**Nachprüfung/Impact:** BESTANDEN für Dokumentation, Gegenalternativen und Einschränkung. Eine gemeinsame reflektive Skala ist dadurch nicht freigegeben. Der Widerspruch bleibt offen; theoretische Entscheidung und Identifikation sind NICHT_GEPRÜFT/BLOCKIERT für davon abhängige Modellarbeit. Ein ausdrücklich offen gehaltener Quellenwiderspruch ist hier keine vorgetäuschte Lösung und kein empirisch nicht bestandener Test.

### F-P04 — hoch für Klimavergleich/Norm: Anwendbarkeit vor Missing

**Ursprünglicher Claim/Fundstelle:** C30=55 könnte wie ein gewöhnlicher Fehlwert oder eine Stufe der Ursachenordnung behandelt werden. DE-Q S. 26 führt diese Sachantwort aus C31/C32 heraus; 77 und 88 führen dagegen weiter.

**Korrektur und eigener Beleg:** F/docs/analyseplan-methoden.entwurf.md:65/69 und F/docs/konstruktakten.entwurf.md:22–24 unterscheiden zuerst Score-/Anwendbarkeitsdomäne, danach vollständige Antwortmaske. Ich las DE-Q26 textuell und visuell und prüfte erfundene gültige, 55-, 77- und 88-Fälle. 55 erzeugt keinen Ursachenwert, keine erfundene Verantwortung/Besorgnis. Getrennte Folgefragen können bei 77/88 anwendbar sein, obwohl der Ursachenscore fehlt.

**Nachprüfung/Impact:** BESTANDEN für Routing und Einschränkung. Gemeinsamer C30–C32-Score und unbedingte Bevölkerungsnorm bleiben BLOCKIERT, solange Definition und Zielpopulation fehlen. Die Worst-Case-Schranken sind nur für inhaltlich definierte, aber unbeobachtete Scores in [0,1] zulässig; sie definieren keinen Score für 55. Kein empirischer Klimavergleich durchgeführt.

### FM-F02 — niedrig: Rundung 0,047 statt 0,046

**Ursprünglicher Claim/Fundstelle:** P03 rundete den synthetischen PSU-Split-Wert `0.04646136457085024` falsch auf drei Nachkommastellen.

**Korrektur und eigener Beleg:** F/docs/analyseplan-methoden.entwurf.md:41 verwendet 0,046. F/reports/loop/FOUNDATION-001-korrekturbericht.md:12 ist das getrennte Erratum; der historische Methoden-Autorenbericht bleibt unverändert. Mein identischer Replay hat dieselben JSON-Werte; eine separate Kovarianzimplementierung bestätigt den Wert im Rahmen numerischer Rundung.

**Nachprüfung/Impact:** BESTANDEN für die aktuelle Rundung und transparentes Erratum. Betrifft ausschließlich ein erfundenes Normal-Cluster-Szenario, keine ESS-Schätzung und keine Bestätigung tatsächlicher Split-Unabhängigkeit.

### N-F01 — mittel: unspezifische Antworttyp-Fallbacks

**Ursprünglicher Claim/Fundstelle:** `judgement`/CSV unterschieden unter anderem normative Rechtepräferenzen, eigene Erfahrungen und ein versorgungsbezogenes Ereignis nicht ausreichend.

**Korrektur und eigener Beleg:** F/pipeline/inventar.py:255ff. und :315, sowie 33 geänderte CSV-Annotationen. Ich verglich jede geänderte Zeile mit eigenständig extrahiertem Originalwortlaut; einschlägige DE-Q-Seiten 4–7, 13, 17–21, 26, 31–32, 37, 43–48 wurden gelesen. S. 13, 37, 48 zusätzlich visuell. 31 bisherige Fallbackfälle plus B36 und D14 ergeben 33 Präzisierungen. B34/B36 sind normative Rechtepräferenzen; B35 eine hypothetische persönliche Reaktion; E8M/W Identitätsbedeutung, E9M/W–E11M/W Erfahrungen; D14 nicht erhaltene benötigte medizinische Versorgung. Selbstberichtetes Interesse/Fähigkeit, Erwartungen an andere, Gefühle, Verantwortungszuschreibung und eigene Religiosität werden enger benannt.

**Nachprüfung/Impact:** BESTANDEN für diese 33 typisierten Entwurfsannotationen und den reproduzierten Neuaufbau. Keine Vollabnahme aller 296 Zeilen, Auswahl, Polung oder belegter gerichteter Bias. Alle 33 behalten `ENTWURF_OFFEN`; die Annotationen selbst beanspruchen keine unabhängige Gesamtsemantik. Eigene direkte Validatorgegenfälle mit falschem Antworttyp beziehungsweise vertauschten Kategorien passieren weiterhin: Technische Token-/Regionsprüfung ersetzt diese Lektüre nicht.

### REPRO-F01 — mittel: Lizenzinput nicht deterministisch gebunden

**Ursprünglicher Claim/Fundstelle:** Der Disclaimer war für die Provenienz wichtig, aber nicht zwingender gepinnter Input.

**Korrektur und eigener Beleg:** F/pipeline/inventar.py:33ff., :156, :699–701, :729 und :750–752. Alle vier Inputs einschließlich `ess-disclaimer.html` sind obligatorisch hashgeprüft. Eigener frischer Abruf, Build und Check mit explizitem Cache/CSV/Provenienz unter O ergeben byteidentische CSV und Provenienz. Fehlender oder veränderter Disclaimer und veränderte Netzwerk-/Cachebytes werden in den 15 Tests abgewehrt. Bedingungen der frischen Originalseite wurden gelesen.

**Nachprüfung/Impact:** BESTANDEN für deterministische lokale Reproduktion bei derselben Python-/Poppler-/Builderfassung. Documentation CC BY-SA 4.0 und Daten CC BY-NC-SA 4.0 bleiben getrennt; die Quellenzitation edition 4.1 macht das Datenfile nicht edition 4.1. Die spezifische Veröffentlichungsfreigabe des Inventars und Edition-4.2-Abgleich bleiben offen. Ein gehashter Disclaimer ist keine juristische Gesamtfreigabe.

### REPRO-F02 — mittel: echte Aufträge/Prüfprotokolle unvollständig gebunden

**Ursprünglicher Claim/Fundstelle:** v1 band die vollständigen ursprünglichen Inventar-/Theorieaufträge und mehrere behauptete historische Prüfbelege nicht ausreichend.

**Korrektur und eigener Beleg:** v2 bindet alle drei `LOOP-*-auftrag.txt` sowie verfügbare historische und neue Protokolle in 42 Dateien/101 Inputs. Ich las die Aufträge, ursprünglichen Autorenberichte, historische strukturierte Belege und die heutigen Korrekturläufe. F/reports/loop/FOUNDATION-001-korrekturbericht.md:15/:25 unterscheidet fehlende historische vollständige Befehls-/Zeitlogs von neu datierter Ausführung; Methoden-`verification.json` hält damalige Dokumenthashes und Recheninputs getrennt von später ergänzten Dokumentbytes.

**Nachprüfung/Impact:** BESTANDEN für heutige Belegbindung und zurückgenommene historische Reichweite. Die verfügbare Provenienz beweist keine vollständige damalige Ausführung oder technisch erzwungene damalige Trennung. Fehlende historische Nachweise bleiben NICHT_GEPRÜFT/Autorangabe. Mein heutiger Replay ersetzt sie nicht. Die im Korrekturbericht referierte allgemeine App-CI wurde nicht als Methodenbeleg verwendet oder erneut als Appprüfung ausgeführt.

### REPRO-F03 — niedrig: Liste 92 ohne Locator

**Ursprünglicher Claim/Fundstelle:** I7/I8/I9 verweisen auf Liste 92, deren doppelte Textlage nicht als Kartenlocator erkannt wurde.

**Korrektur und eigener Beleg:** F/pipeline/inventar.py:288–301 verlangt für die Sonderregel PDF97, `LISTE9292` und alle drei Labels. Ich prüfte die gepinnte Showcard97 textuell und visuell: sichtbarer Titel Liste 92, 0–10-Anker, I7/I8/I9. DE-Q95/96 wurden für die lokalen Verweise gelesen. Alle drei erzeugten Locatorbelege nennen PDF97. Eigene Gegenfälle mit entferntem I9-Label oder derselben Karte auf PDF96 finden keinen Locator; die Tests prüfen auch irrtümlich geschlossenen Status bei fehlendem Locator.

**Nachprüfung/Impact:** BESTANDEN für Locator und Statusregel. Kartenkategorien bleiben explizit `NICHT_GEPRUEFT`; keine semantische Vollabnahme der Karte. Die kontrollierte Sonderregel wird nicht auf beliebige doppelte OCR-/Textlagen verallgemeinert.

### REPRO-F04 — niedrig: Kontextauszug als exklusive Itemregion beschrieben

**Ursprünglicher Claim/Fundstelle:** `originalblock_de` enthält bei B6, C31, E20 nachfolgende Fragen, während die historische Autorenbeschreibung einen engeren Schnitt nahelegte.

**Korrektur und eigener Beleg:** F/pipeline/inventar.py:552–553/:651ff./:701 und die CSV markieren größere Seitenkontextauszüge ausdrücklich. Wortlaut-, Antwortzellen- und Filterregionen werden gesondert geführt. Eigener Vergleich mit v1: alle 296 `originalblock_de`-Bytes und ihre Hashes unverändert. B6 auf Q7 umfasst spätere B-Fragen, C31 auf Q26 auch C32, E20 auf Q52 auch E21/E22. A6 führt einen dokumentierten Seitensprung Q4/5. Separate Wortlautregionsbelege grenzen die Frage genauer ein.

**Nachprüfung/Impact:** BESTANDEN für wahrheitsgemäße Benennung, separate Regionen und Erratum. Eigene Mutation des B6-Kontextblocks und eines belegten geerbten I9-Filters wird zurückgewiesen. Mutation eines ausdrücklich noch offenen E20-Filters passiert; das bestätigt die offengehaltene Prüfgrenze. Keine Behauptung exklusiver Einzelfrage für jeden großen Block, keine vollständige Routingabnahme.

## Eigene Methodenrechnung und Vertragsgegenfälle

Das eingefrorene NumPy-Skript wurde unverändert mit eigenem Arbeitsverzeichnis ausgeführt. Es akzeptiert keine Inputdatei; ein zusätzliches erfundenes Argument endete wie erwartet mit Exit 1. Sein Output steht ausschließlich in O/reports/loop/synthetic. Parsed JSON und sämtliche Zahlen sind exakt gleich der eingefrorenen Ausgabe. Bytehashes unterscheiden sich wegen der formatierten eingefrorenen JSON-Fassung: Replay `13ce08142ece64920ee6313d89764bf276a17d027c9b813c3d458fcafb4d05e9`, Freeze `fe5ae8294b90b3621ce91a13217e4ddd341bea557ff80011548ef73cfbd6a45b`. Es wird keine Byteidentität behauptet.

Zusätzlich habe ich eine getrennte Berechnung in O/independent_checks.py geschrieben. Sie definiert Ratio-Ziele separat, aggregiert jede linearisierte Zielvariable je PSU und addiert stratumweise äußere Produkte statt die Kovarianzfunktion des geprüften Skripts zu verwenden. Die sechs Szenarien verwenden denselben dokumentierten Zufallsstrom: acht künstliche Strata, je zehn Cluster mit 20 künstlichen Werten; latente Normal-Clusteranteile 0/0,25/0,5 und unabhängiger Gewichts-CV 0/1, jeweils 1.000 Wiederholungen. Die Zufallszahlen dienen ausschließlich der Vergleichbarkeit, keine personenbezogene Referenz.

Mittelwerte, empirische und linearisierte Varianz, gemeinsame 4×4-Kovarianz, Domänenkontrast, Midrank-CDF, Normalintervallabdeckung und beide Split-Korrelationen stimmen mit maximaler absoluter Abweichung `5.995204332975845e-15` überein. Der letztgültige eigene Lauf war `2026-10-03T03:46:02.286118+00:00` bis `03:46:08.545993+00:00`, Exit 0; vollständiger Befehl und Hashes in O/independent-execution.json.

| Szenario: latenter Clusteranteil / Gewichts-CV | Normalintervallabdeckung | Varianz linearisiert / empirisch | Zeilensplit-Korrelation | PSU-Split-Korrelation |
| ---------------------------------------------- | ------------------------ | -------------------------------- | ----------------------- | --------------------- |
| 0 / 0                                          | 0,948                    | 0,960                            | 0,034                   | 0,026                 |
| 0 / 1                                          | 0,952                    | 1,018                            | 0,007                   | −0,047                |
| 0,25 / 0                                       | 0,950                    | 1,096                            | 0,744                   | −0,036                |
| 0,25 / 1                                       | 0,955                    | 1,011                            | 0,565                   | −0,019                |
| 0,5 / 0                                        | 0,950                    | 0,988                            | 0,893                   | 0,046                 |
| 0,5 / 1                                        | 0,948                    | 1,050                            | 0,733                   | −0,040                |

Diese Zahlen belegen nur die künstliche Ratio-/Clusterrechnung. Es gibt hier kein ESS-Design, PPS-Auswahl, ordinale EFA/CFA, Modellidentifikation, Messinvarianz, Reliabilität, Fehlantwortmodell oder persönliche Unsicherheit. 1.000 Wiederholungen erlauben keine präzise Fehlbudgetfreigabe; bei Abdeckung 0,95 liegt die grobe Monte-Carlo-SE bei rund 0,0069. Die Normal-Clusterkalibrierung ersetzt P09s geplante ordinal/designgemäße Kalibrierung nicht.

Die fünf eingefrorenen Vertragsprüfungen bestanden. Die zusätzliche Terzilprüfung umfasst alle 1.024 Kombinationen von fünf erfundenen Kategoriegewichten aus {0,1,2,3}. Eine unabhängige ganzzahlige kumulierte Rechnung kontrolliert Schnitte und Ausfall. Leere Gesamtmasse, große Bindungen, gleiche Grenzen und leere Gruppe bleiben blockierbar; Kategorien werden nicht geteilt. Ungültige Kategorien 77/88, boolesche Schlüssel, −1/11 und negative/nichtendliche Gewichte wurden zurückgewiesen. Exakte Drittel mit rationalen Gewichten wurden geprüft.

Ein eigener Gewichtungsgegenfall ergibt gewichtet Grenzen [0,8] und Anteile 4/11, 6/11, 1/11; ungewichtet dagegen [2,8]. Ein Gegenfall zur gemeinsamen Referenz entfernt erfundene fehlende LR-Werte und Nullgewichte vor den Quantilen, lässt eine separate Dimensionsmaske aber außerhalb dieser Definition. Erneute Quantile nur auf der Dimensionsmaske würden hier einen blockierten leeren dritten Arm erzeugen. Diese Demonstration prüft die Vertragsbedeutung; eine echte Missing-/Zugriffsimplementierung wurde nicht zertifiziert.

Für das Klima wurde die hypothetische gemeinsame Ursachen-/Folgedomäne {1,…,5} von der Folgefragendomäne {1,…,5,77,88} getrennt, bevor eine Vollmaske entsteht. 55 gehört zu keiner Folgefragendomäne und erhält keinen Ursachenrang. Daraus wird kein gemeinsames Konstrukt ausgewählt.

F/docs/analyseplan-methoden.entwurf.md:7/:83/:109–111/:139 unterscheidet weiterhin Referenz-CI, beobachteten deterministischen Score, populationsdurchschnittlichen RMS-Messfehler und persönliches Intervall. Keine Erweiterung zu einem numerischen persönlichen Intervall oder einer unsicherheitsabhängigen Rangfolge. Die betreffenden Freigaben bleiben blockiert.

## Frischer Inventaraufbau und technische Grenzen

Die öffentliche CLI wurde mit `--help` und danach `fetch`, `build`, `check` selbst ausgeführt. Alle drei Befehle bekamen explizit `--cache O/public-cache --csv O/rebuilt.csv --provenance O/rebuilt.provenance.json`; keine Standardpfade wurden überschrieben. Vollständige absolute Argumente, Arbeitsverzeichnisse, Start-/Endzeiten, Exitcodes und Loghashes stehen in O/execution.json. Der neue Cache war vor dem Abruf leer.

| Gepinnter öffentlicher Input | SHA-256                                                            |
| ---------------------------- | ------------------------------------------------------------------ |
| ESS11_questionnaires_DE.pdf  | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| ESS11_showcards_DE.pdf       | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| ESS11_appendix_a7_e04_1.pdf  | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |
| ess-disclaimer.html          | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` |

Abruf, Build und Check am 2026-10-03 03:38:43–03:38:46 UTC: jeweils Exit 0. Die URLs und tatsächlichen frischen Downloadhashes stehen in O/fresh-fetch.log. CSV `89d2c4611d44faee3e44d27e66e5e68550a5611112cf2cf63f96fa5d8a8b84f3` und Provenienz `89c75a95f2da2610396d25fd7428f51d213a71446a5abba50eed73a28fd4ecb7` sind byteidentisch mit F, siehe O/comparison.json.

Die 15 eingefrorenen Inventartests liefen gegen den eingefrorenen Parser, mit dessen Test-ROOT und Cache-/Outputkonstanten auf O umgebunden, damit feste Testtempverzeichnisse nicht im gemeinsamen oder eingefrorenen Paket landen. Kein Produktcode wurde für die Prüfung verändert; `-B`/`dont_write_bytecode` verhindern gemeinsame pycache-Dateien. Alle 15 bestanden, O/inventory-tests.log. Der vollständige Aufwand ist im eigenen Replay-Skript nachvollziehbar.

Die eigenen semantischen Gegenfälle wurden direkt an `validate` übergeben. Ein falsches B34-Antworttyp-Label und umgekehrte Tabellenkategorien passieren dabei; beschädigter Wortlaut, B6-Block und belegter I9-Filter werden zurückgewiesen. Dies umgeht bewusst den äußeren CSV-Bytehash, um die semantische Reichweite der inneren Prüfung zu isolieren. Es ist kein Beleg, dass ein verändertes CSV den vollständigen Provenienzcheck bestehen würde.

Der erste eigene Gegenfall erwartete irrtümlich, dass auch eine Mutation des bereits ausdrücklich offenen E20-Filters technisch scheitern müsse. Dieser eigene Test scheiterte, O/independent-checks-first.log. Ich korrigierte ausschließlich meine Testannahme, prüfte den belegten geerbten I9-Filter als Negativfall und behielt E20 als Gegenbeleg gegen eine Vollroutinggarantie. Kein Paketfehler wurde aus dem falschen Test abgeleitet; Fehlerlog bleibt erhalten.

Aktueller technischer Inventarstand: 296 Zeilen, 205 Restzeilen mit mindestens einem offenen technischen Kriterium; 29 Zuordnungen, 70 Kategorienblöcke, 23 Missingblöcke und 203 Kontextfälle offen, mit Überschneidungen. Die Null bei offenen Antworttyp-/Locatorzählungen bedeutet nicht 296 wissenschaftlich freigegebene Annotationen. Entwurfsstatus, Karteninhaltsabnahme, vollständige Filterlektüre und breitere Semantik bleiben eigene Prüfziele. Alle 296 großen Blockbytes wurden nur auf unveränderte Reproduktion verglichen, nicht vollständig inhaltlich abgenommen.

## Selbst gelesene Originalbelege und Reichweite

Die öffentlichen Original-PDFs wurden mit Poppler in O extrahiert, ausgewählte Seiten zusätzlich gerendert und mit `view_image` kontrolliert. Die Grenzen der folgenden Lektüre bleiben Bestandteil des Urteils.

| Original                                               | Tatsächlich gelesener Bereich                                                                            | Trägt / trägt nicht                                                                                                               |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| DE-Q 2023, gepinnter Hash oben                         | Alle 33 geänderten Typwortlaute; Q4–7/13–14/17–21/26/31–32/37/43–48/50–54/95–96; visuell Q13/14/26/37/48 | Antwortgegenstände, B37, Klimarouting, ausgewählte Kontext-/Geschlechterfragen; keine vollständige Fragebogen-/Routingabnahme     |
| DE-Showcards 2023                                      | PDF97 textuell und visuell                                                                               | Liste92-Locator; keine Karteninhalts-Gesamtfreigabe                                                                               |
| Geschlechtermodul-Originalvorschlag `091bea62…52a7`    | PDF11/26/29–33, visuell 11/26/30/32                                                                      | Paare und Messannahmewiderspruch; keine empirische Skalenvalidierung                                                              |
| ESS11 Country Report e04, `007be2a…9d850`              | PDF79–86                                                                                                 | Feldzeit/Kontrolle/Regionengrenze; kein vollständiges DE-Auswahldesign                                                            |
| ESS weighting guide v1.2, `6b9c04b…528e5`              | Relevante Abschnitte PDF6–11                                                                             | Unterschied Design-/Poststratifikations-/Analysegewichte; keine Prüfung des realen Gewichtsfiles                                  |
| semTools Manual, `486d541…a8a9e`                       | `compRelSEM`, PDF18–23                                                                                   | W, ord.scale, beobachtete versus latente Antwortskala und nicht unterstützte Mischkomposite; keine designgerechte Adapterfreigabe |
| survey Manual, `87b0ea7…8bac2c`                        | Bootstrap-/Replikatpassagen PDF14–15 und 103–105                                                         | Warnung SRS/PPS; keine ESS-Replikat- oder Runtimeprüfung                                                                          |
| Mplus Originalmanual Kapitel15/16                      | Betreffende öffentliche Variablenspezifikation, EFA/COMPLEX-Tabelle, RSTARTS- und DIFFTEST-Passagen      | Dokumentierter Kandidat, nicht ausgeführte Softwarekette                                                                          |
| lavaan offizielle History 0.7 und categorical tutorial | Aktuelle öffentliche Abschnitte zu weighted Gamma/NACOV und categorical WLSMV/FIML                       | Einzelne dokumentierte Funktionen; keine vollständige Stratum-/PSU-/Reliabilitätskette                                            |
| Frischer ESS-Disclaimer                                | Conditions-of-use-Abschnitt                                                                              | Getrennte Daten-/Dokumentationslizenzen; keine konkrete Veröffentlichungs- oder rechtliche Gesamtfreigabe                         |

Die offizielle [lavaan-0.7-History](https://lavaan.ugent.be/history/dot7.html) nennt 0.7-2 vom 16.07.2026 und die gewichtete Gamma/NACOV-Erweiterung; der [categorical tutorial](https://lavaan.ugent.be/tutorial/cat.html) dokumentiert WLSMV bei `ordered` und fehlende FIML-Unterstützung für kategoriale Daten. [Mplus Kapitel 16](https://www.statmodel.com/HTML_UG/chapter16V8.htm) dokumentiert die benannten EFA/COMPLEX-, Rotations- und Differenztestfunktionen; [Kapitel 15](https://www.statmodel.com/HTML_UG/chapter15V8.htm) die betreffenden Gewicht-/Cluster-/Stratumvariablen. Diese Seiten wurden zusätzlich live als offizielle Originale gelesen; Werkzeugauszug in O/software-web.txt. Das ergibt keinen Smoke-Test und keine reale Ausführung.

Green/Yang-Volltext, vollständige ordinal/designgemäße Identifikations- und Invarianzherleitungen, sämtliche Quellenvolltexte sowie vollständige reale Samplingreconciliation wurden nicht nachgelesen. Dafür wird kein PASS vergeben. Der semTools-Beleg bestätigt Funktionsoptionen; er beweist weder die benötigte gewichtete gemeinsame Reliabilitätsunsicherheit noch ein persönliches Fehlermodell.

Die neuen Literaturclaims L-THEO-017–019 wurden anhand der gebundenen Original-Publisher-Werkzeugauszüge O/find-001.json.txt und O/find-002.json.txt sowie der dokumentierten Einschränkungen plausibilisiert. Demel: deutsche instrumenteigene Faktoren, selektive Rekrutierung und explorative Entwicklung, keine ESS11-Validierung. Teney: 817 Items aus nicht zufällig rekrutiertem Onlinepanel 2022, Themen-/Formulierungsbezug, keine Kausalität, Faktorvalidierung oder repräsentative aktuelle Salienz. Alexander: Entwicklungs-/Übersetzungs-/Antwortformatprobleme des Geschlechtermoduls, keine deutsche Validierung oder nachgewiesene völlige Neutralität. Ich habe diese benannten Auszüge gelesen, nicht alle Artikel und Anhänge vollständig; deshalb kein Volltext-PASS oder systematisches Literaturvollständigkeitsurteil.

Feldzeit, Publikationsjahr und Websitezeitpunkt bleiben getrennt. Neue 2024/2026-Literatur darf die historische ESS11-Referenz nicht zu einer heutigen Bevölkerungsaussage machen. Die Ergänzungen beseitigen den alten reflektiv/formativ-Widerspruch nicht allein durch ihr Erscheinungsdatum.

## Verbleibende Freigabegrenzen und eigener Abschluss

Die Einschränkungen sind substantiell, aber angekündigte spätere empirische Tests sind in dieser Phase nicht als NICHT_BESTANDEN markiert. Ohne vollständiges Inventar, entschiedene Konstrukte/Missingdomänen, geklärtes Mischdesign einschließlich Split und Stichprobengewichten, identifizierte Software-/Reliabilitätskette, ordinal/designgemäße Simulation und persönliches Fehlermodell bleibt die abhängige empirische Arbeit blockiert. Fehlende Claude-Erstbewertungen/Reviews, persönliches Setup und fünf menschliche Verständnistests bleiben echte Voraussetzungen; dieser Codex-Bericht ersetzt sie nicht. Es wurde kein Claude-Setup oder Auftrag an eine weitere Modellfamilie vorbereitet.

Die Phase-0-Planfestschreibung wurde nicht durch eine zusätzliche persönliche Statistik-Abnahme Stevens blockiert; die dafür vorgesehenen fachlichen Voraussetzungen wurden zugleich nicht aufgehoben. CodeRabbit und App-CI sind keine methodische Validierung. Aus dieser Korrekturprüfung folgt keine Endauswahl, A/B-Bildung, Entblindung, Präregistrierungs-/Modelltag, Teststart, Merge- oder Deploymentfreigabe.

Alle ausführbaren Belege stehen unter O. Besonders maßgeblich: `identity-before.json`/`identity-after.json`, `execution.json`, `comparison.json`, `calibration-comparison.json`, `independent-execution.json`, `independent-results.json`, `context-checks.json`, Test-/Fehlerlogs und eigene Skripte. Die eigene Hashliste `evidence-hashes.json` bindet diese Dateien. Die gezielte Formatprüfung betrifft ausschließlich diesen Bericht; allgemeines `pnpm check` und Browser-Appprüfung waren kein Teil des auf Forschungs-/Reproduktionsprüfung begrenzten Auftrags.

Der erste eigene Abschlusslauf scheiterte am Vergleich unterschiedlich ausführlicher v1-Protokollzeilen (anfangs nur Pfad/ok, abschließend zusätzlich Soll-/Isthash). Alle Dateihashes hatten bereits übereingestimmt. Nur dieser eigene Schema-Vergleich wurde korrigiert; `finalize-first.log` hält Fehler und Ursache fest. Der erfolgreiche Abschlusslauf kontrolliert alle v1/v2-Sollhashes erneut und vergleicht den passenden Anfangsumfang.

## Vollständiger tatsächlich erteilter Auftrag

Der folgende Startauftrag wird wortgetreu wiedergegeben. Seine komprimierte Schreibweise wurde nicht nachträglich als anderer Auftrag geglättet.

```text
Du bist unabhängiger Korrekturprüfer FOUNDATION-001-v2, Schwerpunkt Methoden/Statistik/Reproduktion, keinAutor. Zielworktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Gefrorenes Manifest reports/loop/packages/FOUNDATION-001/v2/manifest.json SHA 10157ee7bca65ca0b92707e673bc75c3698c4d1acc6664da421b7b218e7a1988:42 Dateien/101öffentlicheInputs. Lies eingefrorene AGENTS/mandat/LIFE93/v2-Prüfauftrag, v1Ausgang(213eec2fba90ae60594323f1e52c39ed77d49af4656f3eea481c6300ecc0c5bb), alle fünf ERLAUBTEN abgeschlossenen FOUNDATION-Erstberichte und Autorentscheidungen/Korrekturbericht. Keine anderen v2Nachprüfberichte oder aktuellePREP/SOFTWARE/Autorenverteidigung lesen. Schreiborte nur eigener Bericht reports/loop/reviews/FOUNDATION-001-v2-methods-repro.md und eigenePublic/Syntheticdateien outputs/loop/foundation-v2-methods/. KeinegemeinsamenÄnderungen/Commit/Push/weitereAgents/globaleInstalls. Rohdaten data/raw/data/local,B,Antworten/IDs/Parteien/LRWerte,Cookie/Credentialabfragen verboten; nur öffentlicheOriginalfragen/Kodierungen. Prüfe ALL12Findings rollenpassend. Schwerpunkt unabhängigeNeuberechnungsynthetischeKalibrierung(6×1000, normalClusterkeineESS/SEM), fünfneueVertragsprüfungen+eigene Gegenfälle weightedTerzile/Binds/Missing/Referenz/Zeitpunkt, Klima55/77/88DomänevorMissing, richtige0.046Rundung, keineErweiterungpersönlicherFehlintervalle. ReproduziereInventar ausneuerPubliccachebasisuntereigenemSchreibort mitgepinnten4Inputs+License,CSV/Provenienzvergleich,15Inventartests+eigeneNegativfälleListe92/PDF97,Contextregionen,neueAntworttypen anOriginal prüfen. GrenzenTokenprüfungenvsSemantikbeachten. ÖffentlicheParserCLI/cache/outputoptionen selbstprüfen; niemalsStandardpfadeüberschreiben. KontrolliereechteAufträge/Protokollbindung/historischeAutorangaben vsheutigeAusführung. NeueLiteraturbehauptungen/Zeit/SemantikrollenpassendplausibilisierenaberkeinVolltextPASSohneLektüre. EigeneOriginalfundstellen/belegteSoftwaresupports nachlesen, geplanteempirischePrüfungenNICHTGEPR/indieserPhasenicht nötignichtNICHTBESTANDEN. NofakeEmpiricRelease:205Restzeilen,unvollständigesMixedDesign/personalError/Claude/HumansblockenabhängigeArbeitweiter. FindingsgenaueClaim/Fundstelle/Beleg/Impact/Schwere/Korrektur/Nachprüfung, ursprünglicheIDrunde1behaltenkeineMehrheitsentscheidung. Dokumentierevollen tatsächlichenAuftrag/ModellRuntimeAngaben(gpt6.1-solultrageerbtinterneunbekannt), verwendeteTools/Trennungsgrenzen,42Datei+101InputHashesvor/nach. PublicBrowserwennnötigT3firsteigenesTabkeineCookies. unslop/pdfskillswennrelevant. KeinglobalpnpmcheckerforderlichderAppcodeistnichtScope; eigenerReportformatcheckundimmutableEnde Pfad/SHA/wesentlicheBefunde.
```
