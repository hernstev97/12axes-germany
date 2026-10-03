# INVENTORY-002-AB: unabhängiger Quellen- und Inhaltsreview

Erstbericht vom 2026-10-03. Rolle: öffentlicher Quellen-/Inhaltsreviewer, kein Inventarautor und kein Eignungs-/Polungsbewerter. Start `2026-10-03T05:18:04.179141+00:00`, Abschluss des Berichts `2026-10-03T05:38:07.043486+00:00`. Modell laut zugewiesenem Auftrag `gpt-6.1-sol`, Denkaufwand `ultra`, geerbt. Die genaue interne Revision und nicht zugängliche Anbieterregeln sind unbekannt. Diese Modellangaben konnte ich nicht unabhängig introspektieren.

Die Quellen-/Inhaltsprüfung des eingefrorenen Pakets ist `NICHT_BESTANDEN`, weil die Einleitungsannotation von B19–B22 einen abgeschnittenen Antwortspaltenkopf enthält. Die eigentlichen Wortlaute und die gedruckten Code-/Caption-Zuordnungen aller 52 Identitäten stimmen in meiner begrenzten Originalgegenprüfung. Ein weiterer kleiner Befund betrifft die falsch bezeichnete Autoren-Gegenprobe zu Code 08. Die beiden Befunde stehen unten als AB-S01 und AB-S02. Daraus folgt keine endgültige Itemauswahl, Polung, politische Neutralitätsabnahme oder Phase-1-Freigabe.

## Prüffassung und Eingaben

Prüfpaket `reports/loop/packages/INVENTORY-002-AB/v1/manifest.json`, SHA-256 `5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856`, Code-Commit laut Manifest `5fd7bb37e44addcc13bd6840a8ad6e4339f1c9e2`. Die 10 eingefrorenen Dateien und 89 SourceInputs wurden vor und nach der Quellenprüfung vollständig gegen ihre Dateilängen und SHA-256 geprüft. Beide Kontrollen bestanden. Keine unbekannte Sperrdatenquelle wurde geöffnet. CSV, Provenienz, Parser, Autorenbuilder, Autorenoutputs, Ergänzung und eingefrorene Paketdateien bleiben bytegleich. Die Original-Ergänzung hat SHA-256 `9554a568c1a08fe7d6676960dd7e41d2b50d1ad7c16c5d8d33bfed4edc44c138`.

Ich las die geltenden Repository-Anweisungen, Projektstand, vollständigen dauerhaften Auftrag und LIFE-93, den eingefrorenen Prüfauftrag, Vorabplan und vollständigen Autorenbericht. Große kombinierte Toolausgaben waren zunächst abgeschnitten; begrenzte Folgeaufrufe vervollständigten die erforderliche Lektüre. Zusätzlich gelesen wurden Prüfregeln, Analyseanforderungen, Lizenzakte sowie die nach AGENTS erforderlichen Dokumente Analyseplan, Belegregister und Entscheidungen. Verlinkte Berichte anderer aktueller Reviewer oder Juroren wurden nicht geöffnet. Angaben aus diesen Regeln über ältere Arbeiten dienen nur zur Abgrenzung des Auftrags, nicht als eigener Quellenbeweis.

| Quellen-ID | Öffentlicher Originalpin | SHA-256 |
| --- | --- | --- |
| ESS11-DE-QUESTIONNAIRE | [ESS11_questionnaires_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf) | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| ESS11-DE-SHOWCARDS | [ESS11_showcards_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf) | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| ESS11-CODEBOOK | [ESS11_appendix_a7_e04_1.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf) | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |
| ESS-CONDITIONS-OF-USE | [ess-disclaimer.html](https://www.europeansocialsurvey.org/contact/disclaimer) | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` |

Die Quellen wurden lokal neu gehasht und mit Poppler frisch extrahiert. Die vorliegenden öffentlichen Downloadbelege nennen HTTP 200 und Abrufe am 2026-10-03 um 01:16 UTC. Ich führte keine neue Netzabfrage und keine Portal-Anmeldung aus. Gegenstand ist diese gepinnte Fassung, nicht der aktuelle Ferninhalt der URLs. Die Fragebogen-/Listenheft-Pins werden als öffentliche Dokumentation behandelt; Rohdaten und ihre Lizenz sind davon getrennt. Es wurde keine rechtliche Veröffentlichungsfreigabe erteilt.

## Tatsächliche Originallektüre

Alle A1–A6 und B1–B45 einschließlich B14a/B14b wurden inhaltlich gelesen. Textlektüre des frischen Fragebogenauszugs umfasste PDF-/gedruckte Seiten 3–16; Seite 17 wurde nur für den Übergang B45→C1 gelesen. Die Seiten 3–16 wurden sämtlich neu gerendert und mit `view_image` visuell geprüft. Ich kontrollierte Code-/Caption-Zellen, geteilte Tabellenköpfe, offene Zeitfelder, Intervieweranweisungen, Einleitungen, Filter und die durch Kästen zugeordneten Weiterleitungen.

Alle deutschen Karten LISTE 1–19 auf PDF-Seiten 2–20 wurden selbst visuell gelesen. Die Listen enthalten keine Missingoptionen. Auf numerischen Skalen sind 0–10 sichtbar, während der Fragebogen die Interviewcodes 00–10 druckt. Die Ergänzung bezeichnet ihre Kartenabgleichsliste ausdrücklich als Fragebogenkategorien; sie erklärt deren führende Nullen nicht zu gedruckten Kartencodes. Sichtbare Wortlabels und Endpunkte passen. Die Karten enthalten eine sichtbare Liste pro Seite. Doppelte unsichtbare Textlagen sind im Rohtext erhalten und werden nicht zu zusätzlichen Kategorien erklärt.

Tragende Codebookmetadaten wurden an den frischen Originalseiten gelesen: PDF 5–8,21–22,38–40,45–46,59,63–65. PDF 5,6,7,21,22,45,46,59,63,64,65 wurden zusätzlich neu gerendert und visuell geprüft. Insbesondere Zeitvariablen, Wahlkandidaten, Partei-Code 09/55, Nähefilter und EU-Endpunkte waren Gegenstand der Gegenprüfung. Die vollständige Metadatenkette aller übrigen Codebookeinträge ist nicht das Urteil dieses Quellenreviews. Eine selbständige Reproduzierbarkeitsprüfung bleibt erforderlich.

Die Tabelle dokumentiert den gelesenen Inhalt. Die kurzen Inhaltsangaben sind Reviewer-Lesenotizen, keine neuen Items oder Konstrukte. Für jede Zeile liefen eigene Erwartungen zu vollständigem Wortlaut, Kategorien, Missing, Kartenidentität, Filter, Weiterleitung und geerbten Kontextreferenzen. Die Erwartungsstrings stammen aus meiner Originallektüre; der Autorenbuilder und die Autorentests wurden nicht importiert oder ausgeführt. Leerzeichen und Zeilenumbrüche werden im Wortlautvergleich normalisiert, gedruckte Trennstriche und Satzzeichen bleiben erhalten. Die Autorannotation bewahrt zudem die ursprünglichen Zeilenumbrüche.

| ID | Gelesener Antwortgegenstand | Fragebogen PDF / Druck | LISTE | Enumerierte Kategorien | Gedrucktes Missing | Kontextprüfung |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Zeit für politische Nachrichten | 3 / 3 | keine | 0 | 7777, 8888 | Abgleich ohne Befund |
| A2 | Häufigkeit der Internetnutzung | 3 / 3 | 1 | 5 | 7, 8 | Abgleich ohne Befund |
| A3 | Dauer der Internetnutzung | 3 / 3 | keine | 0 | 7777, 8888 | Abgleich ohne Befund |
| A4 | Menschen vertrauen oder vorsichtig sein | 4 / 4 | 2 | 11 | 77, 88 | Abgleich ohne Befund |
| A5 | Ausnutzung oder faires Verhalten | 4 / 4 | 3 | 11 | 77, 88 | Abgleich ohne Befund |
| A6 | Eigener Vorteil oder Hilfsbereitschaft | 4 / 4 | 4 | 11 | 77, 88 | Abgleich ohne Befund |
| B1 | Interesse an Politik | 5 / 5 | keine | 4 | 7, 8 | Abgleich ohne Befund |
| B2 | Mitsprache über Regierungshandeln | 5 / 5 | 5 | 5 | 7, 8 | Abgleich ohne Befund |
| B3 | Eigene Fähigkeit zur aktiven Rolle in einer politischen Gruppe | 5 / 5 | 6 | 5 | 7, 8 | Abgleich ohne Befund |
| B4 | Einflussmöglichkeit auf Politik | 6 / 6 | 7 | 5 | 7, 8 | Abgleich ohne Befund |
| B5 | Vertrauen in eigene politische Beteiligungsfähigkeit | 6 / 6 | 8 | 5 | 7, 8 | Abgleich ohne Befund |
| B6 | Vertrauen in den Bundestag | 7 / 7 | 9 | 11 | 77, 88 | Abgleich ohne Befund |
| B7 | Vertrauen in die Justiz | 7 / 7 | 9 | 11 | 77, 88 | Abgleich ohne Befund |
| B8 | Vertrauen in die Polizei | 7 / 7 | 9 | 11 | 77, 88 | Abgleich ohne Befund |
| B9 | Vertrauen in Politiker und Politikerinnen | 7 / 7 | 9 | 11 | 77, 88 | Abgleich ohne Befund |
| B10 | Vertrauen in Parteien | 7 / 7 | 9 | 11 | 77, 88 | Abgleich ohne Befund |
| B11 | Vertrauen in das Europäische Parlament | 7 / 7 | 9 | 11 | 77, 88 | Abgleich ohne Befund |
| B12 | Vertrauen in die Vereinten Nationen | 7 / 7 | 9 | 11 | 77, 88 | Abgleich ohne Befund |
| B13 | Teilnahme an Bundestagswahl September 2021 | 7 / 7 | keine | 3 | 7, 8 | Abgleich ohne Befund |
| B14a | Erststimme für einen Kandidaten | 8 / 8 | keine | 8 | 77, 88 | Abgleich ohne Befund |
| B14b | Zweitstimme für eine Partei | 8 / 8 | keine | 8 | 77, 88 | Abgleich ohne Befund |
| B15 | Kontakt mit Politiker oder Amtsperson | 9 / 9 | keine | 2 | 7, 8 | Abgleich ohne Befund |
| B16 | Spende an oder Mitwirkung in Partei oder Interessengruppe | 9 / 9 | keine | 2 | 7, 8 | Abgleich ohne Befund |
| B17 | Abzeichen oder Aufkleber einer politischen Kampagne | 9 / 9 | keine | 2 | 7, 8 | Abgleich ohne Befund |
| B18 | Unterschriftensammlung | 9 / 9 | keine | 2 | 7, 8 | Abgleich ohne Befund |
| B19 | Demonstration | 9 / 9 | keine | 2 | 7, 8 | AB-S01 |
| B20 | Produktboykott | 9 / 9 | keine | 2 | 7, 8 | AB-S01 |
| B21 | Politische Inhalte online posten oder teilen | 9 / 9 | keine | 2 | 7, 8 | AB-S01 |
| B22 | Ehrenamt für gemeinnützige oder wohltätige Organisation | 9 / 9 | keine | 2 | 7, 8 | AB-S01 |
| B23 | Einer Partei näher stehen als anderen | 9 / 9 | keine | 2 | 7, 8 | Abgleich ohne Befund |
| B24 | Namentliche Partei des Nähebezugs | 10 / 10 | keine | 8 | 77, 88 | Abgleich ohne Befund |
| B25 | Grad der Nähe zur genannten Partei | 10 / 10 | keine | 4 | 7, 8 | Abgleich ohne Befund |
| B26 | Links-rechts-Selbsteinstufung | 10 / 10 | 10 | 11 | 77, 88 | Abgleich ohne Befund |
| B27 | Zufriedenheit mit eigenem Leben | 11 / 11 | 11 | 11 | 77, 88 | Abgleich ohne Befund |
| B28 | Zufriedenheit mit Wirtschaftslage | 11 / 11 | 11 | 11 | 77, 88 | Abgleich ohne Befund |
| B29 | Zufriedenheit mit Arbeit der Bundesregierung | 11 / 11 | 11 | 11 | 77, 88 | Abgleich ohne Befund |
| B30 | Zufriedenheit mit Funktionsweise der Demokratie | 11 / 11 | 11 | 11 | 77, 88 | Abgleich ohne Befund |
| B31 | Zustand des Bildungssystems | 12 / 12 | 12 | 11 | 77, 88 | Abgleich ohne Befund |
| B32 | Zustand des Gesundheitssystems | 12 / 12 | 12 | 11 | 77, 88 | Abgleich ohne Befund |
| B33 | Einkommensunterschiede verringern | 13 / 13 | 13 | 5 | 7, 8 | Abgleich ohne Befund |
| B34 | Freiheit der Lebensführung für Schwule und Lesben | 13 / 13 | 13 | 5 | 7, 8 | Abgleich ohne Befund |
| B35 | Scham bei schwulem oder lesbischem Familienmitglied | 13 / 13 | 13 | 5 | 7, 8 | Abgleich ohne Befund |
| B36 | Gleiche Adoptionsrechte | 13 / 13 | 13 | 5 | 7, 8 | Abgleich ohne Befund |
| B37 | Europäische Einigung weiterführen oder zu weit gegangen | 14 / 14 | 14 | 11 | 77, 88 | Abgleich ohne Befund |
| B38 | Gehorsam und Respekt vor Autorität als Werte für Kinder | 14 / 14 | 15 | 5 | 7, 8 | Abgleich ohne Befund |
| B39 | Loyalität gegenüber politischer Führung | 14 / 14 | 15 | 5 | 7, 8 | Abgleich ohne Befund |
| B40 | Zuwanderung aus gleicher Volks-/ethnischer Gruppe | 15 / 15 | 16 | 4 | 7, 8 | Abgleich ohne Befund |
| B41 | Zuwanderung aus anderer Volks-/ethnischer Gruppe | 15 / 15 | 16 | 4 | 7, 8 | Abgleich ohne Befund |
| B42 | Zuwanderung aus ärmeren Ländern außerhalb Europas | 15 / 15 | 16 | 4 | 7, 8 | Abgleich ohne Befund |
| B43 | Folgen für deutsche Wirtschaft | 16 / 16 | 17 | 11 | 77, 88 | Abgleich ohne Befund |
| B44 | Folgen für kulturelles Leben | 16 / 16 | 18 | 11 | 77, 88 | Abgleich ohne Befund |
| B45 | Deutschland als schlechterer oder besserer Ort zum Leben | 16 / 16 | 19 | 11 | 77, 88 | Abgleich ohne Befund |

Bei A1/A3 bedeutet die Kategorieanzahl 0 ein offenes Stunden-/Minutenfeld. Sie bedeutet keine fehlende Frage. Bei B13 umfasst die Anzahl 3 die inhaltliche Sonderantwort „Nicht wahlberechtigt“. Es handelt sich ausschließlich um gedruckte Quellenmerkmale, nicht um Fallzahlen oder ESS-Antworten.

## Befunde

### AB-S01: Einleitung B19–B22 enthält abgeschnittenen Tabellenkopf

**Schwere: mittel. Status: OFFEN.** Betroffen sind `kontext.einleitung_und_geltung` der vier Identitäten B19–B22 und der geteilte Beleg `QCTX-behav-intro2`. Die Annotation bezeichnet den dortigen Text als Originaleinleitung und geltenden Kontext. Nach „Haben Sie... BITTE VORLESEN...“ folgen aber die Fragmente `Ja Nein (Antwort (Weiß`.

Der überprüfbare Originalbeleg ist ESS11-DE-QUESTIONNAIRE, SHA-256 `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`, PDF-/gedruckte Seite 9, untere Verhaltensbatterie B19–B22. Visuell endet die Einleitung bei „Haben Sie... BITTE VORLESEN...“. Die nächste Zeile bildet den separaten Antwortspaltenkopf; seine beiden Missinglabels setzen sich weiter unten fort. Es ist kein weiterer Einleitungssatz. In den frisch extrahierten Wortboxen beginnt dieser Kopf bei `y0=429.688381`. Die Autorenregion reicht bis `y1=430`. `build_ab.py:31–32` wählt Wörter anhand ihrer linken oberen Position; `build_ab.py:76` setzt die Einleitungsregion auf `(9,0,595,379,430)`. Dadurch geraten die vier Wörter des Kopfanfangs in die Einleitungsregion, obwohl ihre vollständigen Boxen bis `y1=442.009523` reichen. JSON-Fundstelle ist `belegregister.QCTX-behav-intro2` mit genau dieser Region und anschließend die vier geerbten Kontexttexte.

Das ist durch Quellenlektüre und eigene Tests belegt, keine Vermutung. Ein korrekter Quellhash beweist hier lediglich, dass die Wörter in derselben PDF stehen. Er beweist ihre Rolle als Einleitung nicht. Die erste und die erweiterte eigene Lesetestfassung melden dieselben vier Kontextfehler. Die jeweiligen Wortlaute und Code-/Caption-Prüfungen bestehen.

Die Wirkung ist begrenzt, aber konkret: Ein späterer Verbraucher des als Einleitung bezeichneten Felds würde einen verstümmelten Antwortkopf an den Fragetext hängen. Das verletzt die verlangte Trennung von Einleitung und Skala für vier Identitäten. Es ist kein belegter Rechen-, Daten- oder Eignungsfehler; deshalb mittel statt hoch. Vor einer Übernahme der Quellenannotation muss das Feld korrigiert werden.

Korrektur: Die Einleitungsregion unterhalb der vollständigen letzten Einleitungszeile und oberhalb des Antwortkopfs beenden. Beispielsweise isoliert `y1=429.5` im unveränderten Pin die vollständige Einleitung. Den Spaltenkopf weiter über seine vorhandenen eigenen Kategorienbelege führen. Alle betroffenen Kontextfelder, Belegregion, Tokenauswahl und Extrakthash neu erzeugen; den gefrorenen Erststand erhalten. Meine eigene gezielte Originalextraktion mit vollständig eingeschlossenen Wortboxen und Region `y379–429.5` liefert genau die erwartete Einleitung. Sie liegt unter `AB-S01-original-boundary-witness.json` und verändert keine Autorendatei.

Nachprüfung: Dieselbe Originalseite visuell lesen; vollständigen Einleitungstext gegen den frischen Auszug vergleichen; alle vier Identitäten auf den gemeinsamen Beleg prüfen. Eine Gegenprobe mit dem angehängten Tabellenkopffragment muss scheitern. Danach die betroffenen Beleg-/Hashprüfungen und eigenen Kontextlesetests auf einer neuen Paketfassung wiederholen. Die vorgeschlagene Grenze ist bereits lokal gegen den Pin geprüft; eine Korrektur des Autorenartefakts fand nicht statt.

### AB-S02: „Code 08“-Gegenprobe verdoppelt tatsächlich Code 01

**Schwere: niedrig. Status: OFFEN.** `outputs/loop/inventory002-ab/read-tests.json` berichtet eine erfolgreich zurückgewiesene Mutation `invented B24 code08`. Der tatsächliche Test in `read_tests.py:115` hängt aber eine tiefe Kopie der ersten vorhandenen B24-Kategorie an. Diese Kategorie besitzt Code 01 und Label CDU/CSU. Er setzt weder den Code auf 08 noch ein passendes neues Label.

Primärbeleg ist das unveränderte Autorenskript, SHA-256 `a7f6f09559aca3414d5d940964da98535f64c6b2f02ca14e8a04d07d41c3eb16`, Zeile115. Der öffentliche Originalfragebogen, PDF-/gedruckte Seite 10, führt in B24 die Codes01–07 und 09, ohne 08. Das Codebook 4.1, PDF 45–46 / gedruckt 44–45, führt getrennt Code 8=dieBasis. Die tatsächlich erzeugte Kategorienfolge lautet01,02,03,04,05,06,07,09,01. Meine gezielte In-memory-Nachbildung der konkreten Autorenoperation dokumentiert diese Folge in `AB-S02-probe-witness.json`. Ich führte weder das Autorenskript noch den Autorenbuilder aus.

Die Behauptung ist damit zu eng beziehungsweise falsch benannt. Belegt ist die Erkennung einer zusätzlichen doppelten01-Kategorie, nicht die protokollierte konkrete08-Mutation. Der Kategoriengleichheitstest würde nach seiner Struktur auch eine zusätzliche 08 ablehnen; daraus darf jedoch kein tatsächlich ausgeführter08-Lauf gemacht werden. Die Ergänzung selbst erfindet keine 08. Meine eigene Gegenprobe fügt ausdrücklich08/dieBasis in eine lokale Kopie ein und wird abgewiesen. Deshalb ist der Befund niedrig und kein eigener Itemkodierungsfehler.

Korrektur: Entweder den historischen Test ehrlich als duplizierten Code 01 bezeichnen und die ursprünglichen Ergebnisse erhalten, oder eine zusätzliche konkrete08-Gegenprobe ausführen und separat protokollieren. Bei einer Skriptänderung sollen Code und Label der neu eingefügten Kategorie ausdrücklich gesetzt werden.

Nachprüfung: Die mutierte In-memory-Kategorienfolge im neuen Prüflauf belegen, die tatsächliche 08 prüfen und die Ablehnung verifizieren. Historische Outputnamen allein genügen nicht. Der bereits vorhandene eigene08-Lauf dieses Reviews ersetzt keine rückwirkende Behauptung über den Autorenlauf.

## Gegenbelege und erhaltene Grenzen

Ich suchte gezielt nach Gegenbelegen zum Wahlcrosswalk im gesamten frisch extrahierten öffentlichen Codebook: `Germany 1`, `Germany 2`, `B14DE`, `first vote`, `second vote` und Varianten. Die deutschen Einträge auf PDF 21–22 unterscheiden Germany1/2, benennen diese beiden Einträge aber nicht als Erst-/Zweitstimme. Suchtreffer für explizite first/second vote betreffen Litauen. Das schließt einen zusätzlichen öffentlichen Anpassungsbeleg außerhalb dieser Pins nicht aus. In dieser Paketfassung bleiben B14a→prtvgde1 und B14b→prtvgde2 daher Kandidaten; das bestätigte Zuordnungsfeld ist leer. Das ist korrekt erhaltene Unsicherheit, kein durch Namensähnlichkeit gelöster Crosswalk.

Die drei Partei-Interviewlisten auf Fragebogen Seite 8 und 10 geben Code 09 für eine andere einzutragende Partei. Die getrennten Codebooklisten auf PDF 21–22 und 45–46 führen Code 8=dieBasis,9=Die PARTEI,55=Other. Diese widersprechenden Originalkodierungen stehen getrennt in der Ergänzung. Es gibt keinen stillen1:1-Import. Der gedruckte B25-Filter nennt auch B24=08, obwohl B24 keine 08-Kategorie druckt; diese Inkonsistenz bleibt sichtbar. Meine eigenen Filter- und Gegenproben prüfen beides gemeinsam.

B13 druckt 3=Nicht wahlberechtigt als inhaltliche Sonderantwort und 7/8 als Verweigerung/Weiß nicht. Die Anweisung, einen ungültig gemachten oder leer abgegebenen Wahlzettel als Nein einzutragen, bleibt erhalten. Alle B15–B22 beziehen sich über ihre Einleitungen auf die letzten 12 Monate. Die eigene Inhaltslektüre unterscheidet Parteispende/Mitwirkung, Kampagnenzeichen, Petition, Demonstration, Boykott, Onlineaktivität und Ehrenamt; diese Unterschiede wurden nicht allein aus den Variablennamen abgeleitet.

A1/A3 drucken Stunden-/Minutenfelder und 7777/8888. A1 enthält die Anweisung 00 00 für keine verbrachte Zeit. Das Codebook nennt Minuten im Variablenlabel. Die Ergänzung erfindet weder eine Stundenspanne noch einen abgeschlossenen Importvertrag. A3 bleibt auf A2=4/5 gefiltert. A1 und A3 sind keine enumerierten 0–10-Skalen.

Auch weitere Unterschiedlichkeiten bleiben als getrennte Originalmetadaten stehen: Beispielsweise nennt Codebook PDF 59 für `lrscale` CARD11, während der deutsche Fragebogen und das deutsche Listenheft LISTE 10 nennen. Solche Nummern werden nicht für einen mechanischen deutschsprachigen Kartenimport verwendet. Die deutsche Kartenidentität wurde gegen die tatsächliche deutsche Karte geprüft. Das ist keine neue Datenversionsabnahme.

Die 61 Autoren-Restpunkte bleiben offen. Darunter sind die 52 individuellen Versions-/Datenmissinggrenzen sowie zwei Wahlcrosswalks, drei Parteicodeübertragungen, zwei08-Filterkonflikte und zwei Zeitfeld-Kodierungsverträge. Ich habe keine Antwortdatei 4.2 und keine Rohdatenhashs geöffnet. Die hier gelesenen4.1-Variableneinträge dokumentieren keine abschließende Datenmissingliste; die Datenmissingfelder bleiben `null`. Es wurden keine „No answer“- oder „Not applicable“-Codes ergänzt. Das ist weder ein bestandener4.1/4.2-Datenvergleich noch ein Importtest.

## Eigene ausgeführte Prüfungen

| Gegenstand | Tatsächliches Ergebnis | Grenze |
| --- | --- | --- |
| Vorher-/Nachherhashes des Manifests,10 Dateien und 89 SourceInputs | BESTANDEN | Integrität und Pfad-/Scopekontrolle, kein Semantikbeweis |
| Frische `pdftotext -layout` und `-bbox-layout` für drei öffentliche PDF-Pins | BESTANDEN, sechs Exit 0 | Originalextraktion, keine Antwortdaten |
| Visuelle Originallektüre Q3–16, Karten2–20, elf tragende Codebookseiten | ausgeführt; Inhalte im benannten Umfang geprüft | Originallektüre, kein empirischer Nachweis |
| Vollständige Wortlaut-/Code-/Caption-/Missing-Erwartungen für 52 Identitäten | BESTANDEN innerhalb des beschriebenen Vergleichs | Keine Eignung, Polung oder Itemauswahl |
| Geerbte Einleitung B19–B22 | NICHT_BESTANDEN, vier Fehlereignisse mit gemeinsamer Ursache AB-S01 | Keine zusätzlichen vier unabhängigen Fehler behauptet |
| Finale eigene Lesetests | NICHT_BESTANDEN, 542 Prüfevents, 4 gemeldete Fehler; Exit 1 | Prüfzähler ist kein Güte- oder Vollständigkeitsmaß |
| Sechs eigene inhaltliche Gegenproben | BESTANDEN | Nur In-memory-Kopien; Originale unverändert |
| Gezielte Originalextraktion der reinen B19–B22-Einleitung | BESTANDEN; erwarteten Text reproduziert, Exit 0 | Vorschlag und Witness, keine erfolgte Autorenkorrektur |
| Gezielte Nachbildung der tatsächlich benannten Autoren-Code 08-Mutation | ausgeführt; doppelte 01 und fehlende 08 belegt, Exit 0 | Autorenprüfung nicht direkt ausgeführt |
| Original-CSV/Provenienz/Parser und Autorenartefakte | alle gefrorenen Hashes unverändert | Kein erneuter Parserlauf und keine Integration |
| `pnpm check` durch diesen Reviewer | NICHT_GEPRÜFT | Nur eigener Bericht/Outputs erlaubt; Gesamtlauf mit Build schreibt gemeinsame Artefakte. Koordinator muss Repositorycheck nach Übernahme ausführen |
| Empirische ESS-Untersuchung | IN_DIESER_PHASE_NICHT_ERFORDERLICH, nicht ausgeführt | Dieser Schritt ist öffentliche Quellenannotation |
| Endgültige Eignung, Polung, andere Modellfamilie und Phase1 | NICHT_GEPRÜFT | Dieser Quellenreview ersetzt keine vorgeschriebene Abnahme |

Die Gegenproben ersetzen gezielt Polizeiwortlaut durch Politikerwortlaut, fügen B24 ausdrücklich08/dieBasis hinzu, kehren den EU-Endpunkt um, entfernen die B13-Sonderantwort, entfernen die gedruckte 08 aus dem B25-Filter und lassen die gemeinsame Vertrauenseinleitung weg. Alle erzeugen einen neuen Fehlbefund gegenüber dem echten Baselinefehler. Der Test verschweigt den vorhandenen Kontextfehler nicht, um seine Negativkontrollen grün erscheinen zu lassen.

Der erste eigene Lesetest hatte 438 Ereignisse und denselben Kontextbefund. Sein Ergebnis liegt unverändert unter `independent-read-test-results-first.json`. Vor dem erweiterten Lauf ergänzte ich ausdrücklich die Vollständigkeit der geerbten Kontextreferenzen und Intervieweranweisungen. Eine zunächst selbst falsch als08 bezeichnete eigene Kopierprobe verdoppelte 01; ich korrigierte sie vor dem finalen Lauf zu einer wörtlichen 08/dieBasis-Mutation. Ein eigener Patchversuch scheiterte an einer nicht passenden Kontextzeile und war ein No-op. Auch eine zunächst zu enge eigene Scopeprüfung blockierte vier bereits bekannte öffentliche Inputs, weil deren Manifesttexte unterschiedliche zulässige Public-Scopeformulierungen haben. Nach Einsicht dieser Texte prüft der finale Guard jede gegen ihren bereits verifizierten individuellen Scope;10+89 bestehen. Diese Reviewer-Werkzeugkorrekturen sind kein Finding über die Autorenfassung und werden nicht als fehlerfrei ausgeführte Erstversuche ausgegeben.

## Werkzeuge, Kommandos und Trennung

Genutzt wurden `functions.exec` mit `tools.exec_command`, `tools.apply_patch` und `tools.view_image`, Python-Standardbibliothek, bestehendes Poppler, sowie Versionsabfragen von Node/pnpm. Die gelesenen Skills sind `unslop` und `pdf`. Keine Installation, kein Conda, keine andere Modellfamilie, kein Subagent-Aufruf, kein Commit und kein Push. Autoren-`reproduce.sh`, `build_ab.py` und `read_tests.py` wurden nicht ausgeführt. Ich habe keine umgestellte Builderkopie benötigt; die gezielte Reproduktion erfolgt durch unabhängige Originalbox-Auswahl und die eigene In-memory-Gegenprobe.

Das Toolangebot enthält zusätzlich Netzwerk-/Web-, Browser-, App-, Ressourcen-, Zeit-, Goal- und Kollaborationstools. Das tatsächlich angebotene Metadateninventar mit 633 Einträgen liegt in `available-tools.json`; die direkten Namespaceangebote und Nutzung stehen in `reviewer-protocol.json`. Angebot bedeutet keinen Zugriff. Die Versionen sind Python 3.14.7, Poppler 26.08.0, Node v24.21.0 und pnpm 11.23.0. Alle Versionsaufrufe hatten Exit 0.

Der auf den eigenen Bericht begrenzte `pnpm exec prettier --check` endete mit Exit0. `--file-info` zeigt jedoch `ignored: true`; das ist keine ausgeführte Inhalts- oder Formatvalidierung dieses Berichts. Es fand keine Prettier-Schreiboperation statt. Der Bericht wurde vor seiner finalen Hashfestschreibung nur in eigenen Prosaabständen korrigiert; der vollständige Startauftrag blieb unverändert. Die tatsächlichen Shellaufrufe und ihre Exitwerte stehen in `command-log.json`. Exakte Subprozess-Argumentlisten für Quellenextraktion, Rendering und Versionen stehen zusätzlich in `extraction-commands.json`, `render-commands.json`, `codebook-render-commands.json` und `tool-versions.json`. Bei flüchtigen JSON-/Text-Lesehilfen nennt das lokale Log Außenaufruf und konkrete Eingabe/Purpose; die vollständigen ursprünglichen stdin-Bodies stehen im tatsächlichen Tooltranskript. Die ergebniswirksamen finalen Lesetest- und Hashskripte sind separat vollständig gespeichert. Nachbaubare eigene Prüfbefehle sind:

```bash
python3 outputs/loop/inventory002-ab-sources/independent_read_tests.py
python3 outputs/loop/inventory002-ab-sources/verify_package.py
```

Der erste Befehl muss auf dieser unveränderten Fassung mit Exit 1 genau die vier AB-S01-Kontextmeldungen erzeugen. Der zweite muss mit Exit 0 die 10+89-Integrität bestätigen. Neue Reproduktionsoutputs aus diesen eigenen Befehlen bleiben im eigenen ignorierten Verzeichnis.

Alle Shells liefen im Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Shared-FS ist eine echte Grenze der Unabhängigkeit: Andere Agents haben denselben Dateizugriff; eine technische Informationssandbox existiert nicht. Die Trennung beruht auf begrenztem Startauftrag, Verzicht auf Peer-/Juror-/Loopfinding-/Agentlistenlektüre und auf der eingefrorenen Prüffassung. Der anfängliche Dateinamens-/Gitstatusaufruf zeigte Namen anderer Dateien, aber keine Reviewerurteile. Ich las keine nachgelieferte Autorenverteidigung außerhalb des Pakets. Die finale Hashprüfung bindet weiterhin dieselbe unveränderte Fassung.

Keine ESS-Personenzeilen, Antworten aus A/B, Partei- oder Links-rechts-Werte/Verteilungen, `data/raw`, `data/local`, Credentials, Cookies oder Portal-Analysen wurden gelesen oder ausgegeben. Alle eigenen Writes beschränken sich auf diesen Bericht und `outputs/loop/inventory002-ab-sources/`. Die Original-PDFs, übrigen Repositoryartefakte und gemeinsamen Outputs bleiben erhalten.

## Tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger Quellen-/Inhaltsreview, kein Autor/Polungsbewerter. Shell-CWD /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Prüfpaket reports/loop/packages/INVENTORY-002-AB/v1/manifest.json SHA5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856,10Dateien/89SourceInputs. Lies AGENTS/project/Issue/Auftrag/INVENTORY-002-AB-pruefauftrag sowie Vorabplan und vollständigen Autorenbericht. Keine anderen aktuellen Reviewer-/Jurorberichte/Loopfindings/Agentlisten/Autorenverteidigung außerhalb Paket. Eigene Originallektüre aller52 deutschenA/B-Frageidentitäten, exakte Kategorien/Codecaption-Zellen/Missing-Sonderantworten, Wortlaut/Einleitungen/gedruckteFilter/Weiterleitungen/Listen selbst prüfen und Gegenbelege suchen; CodebookMetadata nur soweittragend. AlleOriginalsources/publicwordingserlaubt; KEINE ESS/raw/local/A/Bantworten/ParteioderLRwerte/Verteilungen/angemeldetesPortalAnalysis/Secrets/globalWrites/Conda/Installationen. PDFSkill und wichtigeSeiten visuell. Besonders8↔9/55Parteicodes,B14a/bCrosswalkoffen,B24/B25Filter08,B13Sonderantwort,A1/A3Zeitfelder; keinefehlendeDatenmissinglisteerfinden4.1!=belegter4.2Datenvergleich. Alle52auchinhaltlichlesen,nicht836HashesalsSemantikübernehmen. Hashprüfung10+89vor/nachöffentlicheScope/Pfade checken, unbekannteSperrdatenBLOCKIERT. Eigene Lesetests/Gegenproben und gegebenenfallseigenegezielteReproduktion unteroutputs/loop/inventory002-ab-sources/:Autorenreproduce.sh/Buildernichtdirektausführenfestepfade!nurKopieanpassenaufownoutputs,Änderung/Hashdokumentieren. OriginalBuilder/Outputs/CSV/Parser/Artefakteunverändert. KeinefinaleEignung/Polung/ScienceNeutralitätsabnahme. Berichtnur reports/loop/reviews/INVENTORY-002-AB-sources.md plusownoutputs. JedesFindingstabileID AB-Sxx genaueBehauptung/Problem/prüfbarerOriginalbelegmitSeite/Wirkung/begründeterSchwere/Korrektur+Nachprüfung;Vermutungenkenntlich,keineFindingquote. VollständigentatsächlichenStartauftragwortgetreu,Modellgpt-6.1-sol ultra geerbt interneVorgaben/Revisionunknown,Toolsangeboten/genutzt/tatsächlicheKommandosExit/TrennungsgrenzenSharedFS dokumentieren. KeinePeerslesen/weitereAgents/CommitPush/pnpmGesamtformatierung. VollständigabschließenOriginalberichtbewahrenPfadSHAundBefundsenden.
```

Der Wortlaut liegt zusätzlich unter `startauftrag.txt`, SHA-256 `cd1bdb165ac5c9fb51a11e8a2c71bc46a6170fbbca85039b2ad7f2b123058cba`. Weitere sachliche Startaufträge gab es für diesen Reviewer nicht.

## Ausgabeartefakte und Übergabe

Der Originalerstbericht ist `reports/loop/reviews/INVENTORY-002-AB-sources.md`. Der Erzeuger `write_review.py` verweigert das Überschreiben eines bestehenden Berichts. Ein separater `report-integrity.json` wird nach der abschließenden eigenen Formatprüfung den Reporthash festhalten; diese Datei ist kein Selbsthash im Bericht.

Die eigenen Belege und Skripte stehen ausschließlich unter `outputs/loop/inventory002-ab-sources/`: Startauftrag, Reviewerprotokoll, Toolkatalog und Versionen; Vorher-/Nachherhashlisten; frische layout/bbox-Auszüge und gerenderte Originalseiten; Lesetestskript, festgelegte Erwartungen, Erst- und Finalresultat; AB-S01-/AB-S02-Witnesses; Kommandoprotokoll und Erzeuger dieses Berichts. Dieses Verzeichnis enthält ausschließlich öffentliche Quellen, Entwurfsmetadaten und eigene Quellenprüfungen, keine ESS-Antwortdaten.

AB-S01 verlangt eine neue korrigierte Quellenannotation und gezielte unabhängige Nachprüfung. AB-S02 verlangt eine ehrliche historische Testbeschreibung oder einen gesonderten wörtlichen 08-Lauf. Die 61 Quellen-/Versionsrestpunkte bleiben erhalten. Andere Reviewer- oder Jurorurteile, endgültige Itementscheidungen und eine wissenschaftliche Gesamtabnahme sind nicht Teil dieser Übergabe.
