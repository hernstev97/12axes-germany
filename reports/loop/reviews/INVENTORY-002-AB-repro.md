# INVENTORY-002-AB: unabhängiger Metadaten- und Reproduzierbarkeitsreview

Erste vollständige Fassung vom 2026-10-03T05:31:39.689154+00:00. Prüfpaket v1, Manifest-SHA-256 `5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856`. Modell laut tatsächlich erhaltenem Koordinatorauftrag `gpt-6.1-sol`, Denkaufwand `ultra`, geerbt. Interne Modellrevision und nicht zugängliche Anbieterregeln sind unbekannt.

Die Ergänzung ist im geprüften Quellenumfang nachvollziehbar und lässt sich aus den öffentlichen Pins bytegleich nachbauen. Alle 52 Identitäten, Original-Codebook-Locations, deutschen Kategorien und dokumentierten offenen Grenzen wurden verfolgt. Ich fand ein niedriges Problem im Bericht über eine Gegenprobe, AB-R01. Es betrifft die Bezeichnung des tatsächlich ausgeführten Tests. Die 61 Restfragen bleiben offen. Dies ist ein KI-Audit des Quellenentwurfs, keine Phase-1-Abnahme, endgültige Item-/Polungsentscheidung, akademische Begutachtung oder Neutralitätsgarantie.

## Prüfumfang und Quellen

Gelesen wurden die zehn gefrorenen Paketdateien, darunter AGENTS, Projektstand, dauerhafter Auftrag, vollständiges LIFE-93, Prüfregeln, Analyseanforderungen, Lizenzakte, Prüfauftrag, Ergänzung und vollständiger Autorenbericht. Dazu kamen der Vorabplan, Autorenprogramme und die konkreten Manifest-SourceInputs. Die Regeln wurden auf diesen engen Quellenauftrag angewendet. Ungefrorene aktuelle Plan-, Peer-, Juror-, Findings- und Agentregisterfassungen waren keine Prüfeingaben. Eine frühe Dateinamensuche listete andere Paketnamen; ihre Inhalte wurden nicht geöffnet.

Originallektüre: frische `pdftotext -layout`-Auszüge des deutschen Fragebogens PDF-/gedruckte S. 3–16; auf S. 17 der Übergang zu C1. Alle 52 zugehörigen Codebook-Einträge wurden aus der frischen vollständigen Layout-Extraktion gelesen, nicht nur aus dem Autorenregister. Alle LISTE 1–19 wurden im frischen Kartenextrakt gelesen. Sichtprüfung an 38 neu gerenderten Seiten: Fragebogen 3–16; Codebook 5, 6, 12, 21, 22, 38, 39, 40, 45, 46, 59, 63, 64, 65; Listenheft 3, 6, 10, 14, 15, 16, 17, 18, 19, 20. Die übrigen relevanten Originalseiten wurden im Text gelesen; ich behaupte keine vollständige Sichtprüfung sämtlicher drei PDFs.

Die Codebook-Fußzeile ist jeweils PDF-Seite minus eins, „… of 551“. Das Listenheft ist unpaginiert; LISTE und PDF-Seite sind die Locator. Verschobene doppelte Textlagen der Karten existieren in der Extraktion, während die betrachteten Bilder eine sichtbare Karte zeigen. Fehlende Wortlabels der numerischen Zwischenstufen bleiben null. Fragebogen-Codes und Codebook-Codes sind getrennte Metadatenfelder.

| Quellen-ID | Geprüfter Pin | Offizielle Quelle |
| --- | --- | --- |
| ESS11-DE-QUESTIONNAIRE | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` | [ESS11_questionnaires_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf) |
| ESS11-DE-SHOWCARDS | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` | [ESS11_showcards_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf) |
| ESS11-CODEBOOK | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` | [ESS11_appendix_a7_e04_1.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf) |
| ESS-CONDITIONS-OF-USE | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` | [ess-disclaimer.html](https://www.europeansocialsurvey.org/contact/disclaimer) |

## Finding AB-R01

Schwere: NIEDRIG. Betroffene Behauptung: Der Autorenbericht, Tabelle „Gegenproben“, und `read-tests.json/negativeControls` nennen eine abgewiesene Mutation „invented B24 code08“.

Das Programm `outputs/loop/inventory002-ab/read_tests.py`, Abschnitt „Negative controls“, verändert bei dieser Kontrolle keinen Code auf 08. Es hängt `copy.deepcopy(r['antwortkategorien_fragebogen']['wert'][0])` an. Die erste B24-Kategorie hat Code 01. Tatsächlich entsteht deshalb die Codefolge 01,02,03,04,05,06,07,09,01. Der Nachbau reproduziert die irreführende Kontrollbezeichnung. Die Behauptung eines damals ausgeführten echten 08-Falls ist damit nicht belegt.

Originalbeleg: deutscher ESS11-Fragebogen PDF-/gedruckte S. 10, B24-Antwortliste mit 01–07 und 09, kein 08; dieselbe Seite, B25-Filter, nennt 08. Codebook 4.1 PDF-S. 45–46, gedruckt 44–45 of 551, Eintrag `prtclgde`, enthält 8 dieBasis, 9 Die PARTEI und 55 Other. Diese Unterscheidung macht die genaue Mutationsbezeichnung prüfrelevant. Die Belegketten sind `Q-B24-code-01`, `QCTX-filter-b25`, `CB-prtclgde-p45` und `CB-prtclgde-p46`.

Wirkung: Der Prüfbericht überschätzt die Genauigkeit der benannten Gegenprobe. Es ist kein nachgewiesener Fehler der eingefrorenen B24-Kategorien, Filter oder offenen Punkte. Die Schwere bleibt niedrig, weil die Ausgangsannotation korrekt getrennte Originalbefunde enthält und meine eigenen Gegenproben sowohl eine echte 08-Einfügung als auch eine gleichlange Ersetzung 09→08 abweisen. Diese Reviewerläufe ersetzen nicht rückwirkend den anders ausgeführten Autorenlauf.

Korrektur: Die historische Kontrolle wahrheitsgemäß als angehängtes Duplikat 01 benennen. In einer neuen Korrekturfassung zusätzlich tatsächlich Code 08 setzen, möglichst auch durch Ersetzung bei gleicher Kategorienzahl, und das neue Protokoll getrennt erhalten. Die ursprüngliche Erstfassung und der ursprüngliche Fehllauf bleiben unverändert.

Nachprüfung: Mutierte Codefolgen explizit ausgeben, echten 08-Tokeneintrag kontrollieren und Ablehnung nachweisen. Die hier bereits ausgeführten eigenen Kontrollen stehen in `outputs/loop/inventory002-ab-repro/independent-checks.json/negative_controls`: Einfügung 01…07,08,09 und Ersetzung 01…07,08, jeweils `rejected: true`. AB-R01 bleibt für die Autorenbehauptung offen; keine stille Reparatur am Prüfpaket.

## Befunde zu den tragenden Grenzen

B14a/B14b: Fragebogen S. 8 bezeichnet Erststimme und Zweitstimme. Codebook PDF-S. 21–22, gedruckt 20–21, bezeichnet `prtvgde1/B14DE1/Germany 1` und `prtvgde2/B14DE2/Germany 2`. In diesen Originaleinträgen steht kein expliziter Erst-/Zweitstimmen-Crosswalk. Beide bestätigten Zuordnungsfelder sind leer; die Variablennamen bleiben Kandidaten. Das ist korrekt als offen dokumentiert.

Partei-Codes: Interviewcode 09 bezeichnet bei B14a/B14b und B24 die offene andere Partei. Codebook 4.1 kennt 8 dieBasis, 9 Die PARTEI und 55 Other. Die Ergänzung erhält alle drei Konflikte, ohne einen fertigen Import- oder Rekodierungsvertrag zu behaupten. B24/B25 bewahren den zusätzlichen gedruckten 08-Filter und die Abwesenheit von 08 in B24.

B13: Fragebogen S. 7 und Codebook PDF-S. 16, gedruckt 15, führen die Nichtwahlberechtigung als Code 3. Sie bleibt eine inhaltliche Sonderantwort, getrennt von 7/8. Die gedruckte Anweisung für ungültige/leere Wahlzettel und die Weiterleitung 2/3/7/8 nach B15 bleiben erhalten.

A1/A3: Fragebogen S. 3 zeigt offene Stunden-/Minutenfelder mit 7777/8888. Codebook PDF-S. 5–6 nennt Minutenvariablen und Dauererfassung. Kein numerischer Wertebereich, keine abgeschlossene Umrechnung und keine Daten-Missingcodes werden erfunden. Der Filter A2=4/5 für A3 ist belegt.

Sammel-Locations: B6–12a, B15–18, B19–22, B33–36 und B38–39 liefern offizielle Gruppen-Locations. Die einzelnen deutschen Zeilen passen zu den selbst gelesenen jeweiligen Originalfragen im Codebook. Ihre Statusfelder benennen den Autorenabgleich. Daraus entsteht keine offizielle deutsche Crosswalk-Tabelle. Bei den übrigen Zuordnungen nennt der Grenztext ebenfalls den Autorenabgleich des deutschen Wortlauts.

Editionsgrenze: Die verwendete Dokumentation ist 4.1. Die Angaben zu 4.2 stammen ausschließlich aus dem gefrorenen Projekt-/Autorenstand. Ich habe weder die Kandidaten-Antwortdatei, deren Hash noch einzelne Antworten geöffnet. Alle 52 Daten-Missing-/Versionsfragen sind weiterhin offen. Die lokale Lizenzlektüre betrifft den gepinnten Disclaimerabschnitt „Conditions of use“ und den getrennten Dokumentationssatz CC BY-SA 4.0. Keine neue Rechtsfreigabe oder 4.2-Datenprüfung.

## Verfolgung aller 52 Identitäten

Die folgende Tabelle nennt die selbst gelesenen Original-Codebook-Locations. W ist der genaue Wortlautbeleg `Q-ID-wortlaut`; Kategorien und Missingzellen sind unter `Q-ID-code-CODE` und den jeweiligen Caption-Belegen nachvollziehbar. Das eigene `independent-checks.json/row_matrix` verbindet diese Tabelle mit den konkreten Quellenbeleg-IDs, Karten und Prüfstatus. Codebook-Seiten sind PDF-Seiten; die gedruckte Seite steht in der zweiten Zahl. Bei über zwei Seiten laufenden Einträgen gilt jede angegebene Seite. „A“ bedeutet nachvollzogener Autorenabgleich, „S“ Autorenabgleich einer Sammel-Location, „O“ exakte Zuordnung offen. Das sind keine Eignungsurteile.

| ID | Variable/Kandidat | Codebook Location | Q PDF/gedruckt | CB PDF / gedruckt | Zuordnung |
| --- | --- | --- | --- | --- | --- |
| A1 | nwspol | A1 | 3/3 | 5, 6 / 4, 5 | A |
| A2 | netusoft | A2 | 3/3 | 6 / 5 | A |
| A3 | netustm | A3 | 3/3 | 6 / 5 | A |
| A4 | ppltrst | A4 | 4/4 | 6, 7 / 5, 6 | A |
| A5 | pplfair | A5 | 4/4 | 7 / 6 | A |
| A6 | pplhlp | A6 | 4/4 | 7, 8 / 6, 7 | A |
| B1 | polintr | B1 | 5/5 | 10 / 9 | A |
| B2 | psppsgva | B2 | 5/5 | 10, 11 / 9, 10 | A |
| B3 | actrolga | B3 | 5/5 | 11 / 10 | A |
| B4 | psppipla | B4 | 6/6 | 11 / 10 | A |
| B5 | cptppola | B5 | 6/6 | 11, 12 / 10, 11 | A |
| B6 | trstprl | B6-12a | 7/7 | 12 / 11 | S |
| B7 | trstlgl | B6-12a | 7/7 | 12, 13 / 11, 12 | S |
| B8 | trstplc | B6-12a | 7/7 | 13 / 12 | S |
| B9 | trstplt | B6-12a | 7/7 | 13, 14 / 12, 13 | S |
| B10 | trstprt | B6-12a | 7/7 | 14 / 13 | S |
| B11 | trstep | B6-12a | 7/7 | 14, 15 / 13, 14 | S |
| B12 | trstun | B6-12a | 7/7 | 15 / 14 | S |
| B13 | vote | B13 | 7/7 | 16 / 15 | A |
| B14a | prtvgde1 | B14DE1 | 8/8 | 21 / 20 | O |
| B14b | prtvgde2 | B14DE2 | 8/8 | 21, 22 / 20, 21 | O |
| B15 | contplt | B15-18 | 9/9 | 38 / 37 | S |
| B16 | donprty | B15-18 | 9/9 | 38 / 37 | S |
| B17 | badge | B15-18 | 9/9 | 38, 39 / 37, 38 | S |
| B18 | sgnptit | B15-18 | 9/9 | 39 / 38 | S |
| B19 | pbldmna | B19-22 | 9/9 | 39 / 38 | S |
| B20 | bctprd | B19-22 | 9/9 | 39 / 38 | S |
| B21 | pstplonl | B19-22 | 9/9 | 39, 40 / 38, 39 | S |
| B22 | volunfp | B19-22 | 9/9 | 40 / 39 | S |
| B23 | clsprty | B23 | 9/9 | 40 / 39 | A |
| B24 | prtclgde | B24DE | 10/10 | 45, 46 / 44, 45 | A |
| B25 | prtdgcl | B25 | 10/10 | 59 / 58 | A |
| B26 | lrscale | B26 | 10/10 | 59, 60 / 58, 59 | A |
| B27 | stflife | B27 | 11/11 | 60 / 59 | A |
| B28 | stfeco | B28 | 11/11 | 60, 61 / 59, 60 | A |
| B29 | stfgov | B29 | 11/11 | 61 / 60 | A |
| B30 | stfdem | B30 | 11/11 | 61, 62 / 60, 61 | A |
| B31 | stfedu | B31 | 12/12 | 62 / 61 | A |
| B32 | stfhlth | B32 | 12/12 | 62, 63 / 61, 62 | A |
| B33 | gincdif | B33-36 | 13/13 | 63 / 62 | S |
| B34 | freehms | B33-36 | 13/13 | 63 / 62 | S |
| B35 | hmsfmlsh | B33-36 | 13/13 | 63, 64 / 62, 63 | S |
| B36 | hmsacld | B33-36 | 13/13 | 64 / 63 | S |
| B37 | euftf | B37 | 14/14 | 64, 65 / 63, 64 | A |
| B38 | lrnobed | B38-39 | 14/14 | 65 / 64 | S |
| B39 | loylead | B38-39 | 14/14 | 65 / 64 | S |
| B40 | imsmetn | B40 | 15/15 | 65, 66 / 64, 65 | A |
| B41 | imdfetn | B41 | 15/15 | 66 / 65 | A |
| B42 | impcntr | B42 | 15/15 | 66 / 65 | A |
| B43 | imbgeco | B43 | 16/16 | 66, 67 / 65, 66 | A |
| B44 | imueclt | B44 | 16/16 | 67 / 66 | A |
| B45 | imwbcnt | B45 | 16/16 | 67, 68 / 66, 67 | A |

Wortlaut, Einleitungen, Tabellenkopf-/Zeilenzellen, Kategorien und Missingoptionen wurden für jede Identität gegen die frischen Originalauszüge gelesen. An den anspruchsvollen Tabellen und Filterrahmen erfolgte zusätzlich die genannte Sichtprüfung. Gerade bei geteilten Köpfen ist das Auftreten eines Tokens auf einer Seite allein kein semantischer Zuordnungsbeweis. Die manuell festgehaltenen erwarteten Variablen und Kategorien in `independent_checks.py` stammen aus dieser Originallektüre; der eigene Tokenabgleich ist separat gezählt.

## Tatsächlich ausgeführte Prüfungen

| Prüfung | Tatsächliches Ergebnis | Grenze |
| --- | --- | --- |
| Eingangsmanifest: 10 gefrorene Dateien + 89 SourceInputs | BESTANDEN, alle Pfade im Worktree, Public-Scope, Bytes/Hashes identisch; Start 2026-10-03T05:18:04.292355+00:00 | Hashes belegen Fassung, keine richtige Kategorien-/Zellzuordnung |
| Umgeleiteter Nachbau | BESTANDEN, Exit 0, bytegleich `9554a568c1a08fe7d6676960dd7e41d2b50d1ad7c16c5d8d33bfed4edc44c138` | Kopie derselben Autorenprogramme; kein neuer unabhängiger Inhaltsbeweis |
| Reproduzierte Autorenlesetests | BESTANDEN, 7532 Checkereignisse, keine verbliebenen Fehler | Originalkontrolle AB-R01 falsch benannt; der Zähler ist kein Qualitätsmaß |
| Eigene Original-/Metadatenchecks | BESTANDEN, 2301 Checkereignisse, 0 Fehler | Manuelle Originallesung und automatischer Tokenabgleich getrennt; keine endgültige Auswahl |
| Eigene Gegenproben | BESTANDEN: echte 08-Einfügung, gleichlange 09→08-Ersetzung, falsche B6-Sammelzuordnung und erfundene bestätigte Wahlzuordnung erkannt | Nur öffentliche Metadaten/In-memory-Mutationen |
| Originalparser im eigenen Cache | BESTANDEN, Exit 0, 296 Zeilen, 205 Restzeilen, Berichtsbytes identisch | `semanticInventoryAcceptance` und `showcardCategoryAcceptance` bleiben NICHT_GEPRUEFT; kein Abzug 205−52 |
| Autoren-`pnpm check` | Gepinnten Log gelesen: 9 Tests, Build und vorherige Format-/Handbuch-/Reviewschema-/Typechecks erfolgreich | Kein eigener erneuter Gesamtlauf; kein wissenschaftlicher Nachweis |
| Visuelle Prüfung der 38 genannten Originalseiten | DURCHGEFÜHRT, alle Renderer Exit 0, alle 38 Bilder betrachtet | Nicht sämtliche PDF-Seiten visuell geprüft |
| ESS-Antwortanalyse / endgültige Eignung / Polung / Neutralitätsbeweis | IN_DIESER_PHASE_NICHT_ERFORDERLICH; nicht durchgeführt | Öffentliche Quellenannotation braucht keine Personenantworten; Folgeabnahmen bleiben offen |

Die 61 Restpunkte sind vollständig erhalten: 52 Versions-/Datenmissinggrenzen, 2 Wahlcrosswalks, 3 Partei-Codeübertragungen, 2 Erfassungen des B24/B25-08-Konflikts und 2 Dauer-Kodierungsabgleiche. Alle Restpunkt-IDs sind eindeutig. Sie können nicht allein durch Formulierungen oder bessere Tokenchecks geschlossen werden. Der Bestandscheck führt weiterhin 205 technische Restzeilen.

## Zeitliche Provenienz und echte Frühfehler

`downloads.json` protokolliert die drei PDF-Bezüge am 2026-10-03 um 01:16:38–39 UTC, HTTP 200, URLs und passende Hashes. Der Disclaimerdownload steht dort bei 01:16:39 UTC; die Quellenprovenienz nennt zusätzlich den späteren gepinnten Zugriff 01:45:13 UTC bei denselben Bytes. Der Autoren-Vorabplan enthält 04:48:40.668900 UTC; der eingefrorene Paketzeitpunkt ist 05:16:19.847984 UTC. Mein sicherer Nachbau lief 05:19:34.499556 bis 05:19:39.847226 UTC.

Diese Zeiten sind gespeicherte lokale Protokollangaben und meine tatsächlichen Laufzeitangaben. Sie passen in der dokumentierten Reihenfolge, sind aber keine unabhängig signierten Zeitstempel. Das Manifest nennt Code-Commit `5fd7bb37e44addcc13bd6840a8ad6e4339f1c9e2` und erklärt ausdrücklich die gefrorenen Dateifassungen sowie SourceInput-Hashes für maßgeblich. Es ist keine Git-Tag- oder Blindanalysefreigabe.

`read-tests-first-failed.json` ist ein echter negativer Datensatz des Autorenchecks mit anderem Artefakthash `78f6693735859b9f57d93c8150c8fc86d8e8cb1d24d30252b21b4666f4a7504b`: 7126 Checkereignisse und sieben fehlgeschlagene Kategorienlesetests B1–B5 sowie B41/B42. Der endgültige Lauf enthält 7532 Ereignisse, 0 Fehler und den geprüften Artefakthash. Die nun vorhandenen ersten Kategorien und Beschriftungen wurden an den Originalseiten nachgelesen. Der frühere fehlerhafte Artefaktstand ist nicht als vollständige JSON im definierten Paket enthalten; seine konkrete Bytefassung kann ich deshalb nicht nachbauen. Die zusätzliche Behauptung früherer Caption-/Syntaxabbrüche ist im Autorenbericht festgehalten, ohne eigene vollständige Fehllauftranskripte. Das ist eine Nachprüfbarkeitsgrenze, keine als selbst reproduziert ausgegebene Vorgeschichte.

## Sichere Skriptkopie, Befehle und Integrität

Der originale Builder und `reproduce.sh` wurden nicht ausgeführt. Die Kopien behalten die öffentlichen Eingaben bei und ändern nur den eigenen OUT-/DEST-Pfad und die entsprechenden Shellziele. `adaptation.json` und die drei `.diff`-Dateien enthalten exakte Diffs samt Original-/Kopiehashes. Die kopierte Plan- und Inputhashdatei ist bytegleich zum Autoreninput. Kein aktives Artefakt, Quellenpin oder Paket wurde verändert.

Die tatsächlich benannten Shellkommandos und einmaligen Pythonarbeiten stehen unter `outputs/loop/inventory002-ab-repro/commands.md`; Unterprozess-argv/Exitwerte unter `render-commands.json`, `reproduction-result.json`, `baseline-check-result.json` und `finalization.json`. Direkte Shellaufrufe sowie die beiden Nachbau-/Parseraufrufe beendeten sich mit Exit 0. Der Reviewer führt `pnpm check` nicht aus, weil dessen Build außerhalb des ausschließlich freigegebenen Reviewerbereichs schreiben würde. Eine gezielte Formatprüfung/-korrektur des eigenen Berichts wird gesondert protokolliert.

Die endgültige Nachkontrolle der gesamten 10+89 Eingabekette steht in `after-hashes.json`. Sie kontrolliert dieselben Public-Scope-/Pfadbedingungen vor erneuten Bytes-/Hashzugriffen. Unbekannte oder gesperrte Pfade würden als BLOCKIERT geführt und nicht gelesen. `outputs-index.json` bindet die eigenen reproduzierbaren Prüfdateien. Der eigene Erstbericht wird nach Übergabe nicht verändert.

Der unveränderte vollständige Autorenbericht ist `reports/loop/packages/INVENTORY-002-AB/v1/files/reports/loop/authors/INVENTORY-002-AB.md`, SHA-256 `8d1a211532493ed401ee56ad435a7d877a64610b3e43c4a2c47b219ad05b65c2`. Die Ausgangsergänzung ist `9554a568c1a08fe7d6676960dd7e41d2b50d1ad7c16c5d8d33bfed4edc44c138`.

## Tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger Metadaten-/Reproduzierbarkeitsreview, kein Autor/Polungsbewerter. Shell-CWD /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Prüfpaket reports/loop/packages/INVENTORY-002-AB/v1/manifest.json SHA5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856,10Dateien/89SourceInputs. Lies AGENTS/project/Issue/Auftrag/INVENTORY-002-AB-pruefauftrag sowie Vorabplan und vollständigen Autorenbericht. Keine anderen aktuellen Reviewer-/Jurorberichte/Loopfindings/Agentlisten/Autorenverteidigung außerhalb Paket. Verfolge alle52IDs über Wortlaut/Kategorien/Missing/Filter und genaue Originalbelege bis Original-Codebook-Locations. EinzelzuordnungeninSammelLocationsalsAutorenabgleichnichtoffizielleCrosswalktabelle. BesonderstragendB14a/bGermany1/2offen;9InterviewAndersvs9CodebookPARTEI55Other08Basis;B24/B25Filter08erhalten;B13Sonderantwort;A1/A3StundenMinuten;4.1Dokumentationnichtbelegter4.2Datenabgleich. Quellen selbstlesen/tokens/fundstellenundsemantischeZell/Zuordnungkritischkeine836HasheskonvertierenzuAbnahme. Prüfmanifeste/zeitlicheProvenienz/tatsächlicheChecksFrühfehler/Rest61undBestand205prüfen. Eigene Reproduktion/Gegenproben: Autorenreproduce.sh/Buildernichtdirektausführenfestepfade!nurKopiegezieltaufoutputs/loop/inventory002-ab-repro/OutputsanpassenundDiffHashdokumentieren. KeineaktivenCSV/Parser/Outputs/sourceinputs/Paketeändern. Alle10+89Hash/Pfad/Sourcescopevor/nachprüfen;publicundsyntheticsnur,unbekannteSperrdatenBLOCKIERTnichtHashlesen. KEINE ESS/raw/local/A/Bantworten/ParteiLRwerte/Verteilungen/angemeldetesPortalAnalysis/Secrets/globalWrites/Conda/Installationen. PDFSkillwichtigeseitenvisuell. Berichtnur reports/loop/reviews/INVENTORY-002-AB-repro.md plusownoutputs. JedesFindingstabileID AB-Rxx genaueBehauptung/Problem/prüfbarerOriginalbelegmitSeite/Wirkung/begründeterSchwere/Korrektur+Nachprüfung;VermutungenkenntlichkeineFindingquote. KeinendgültigesItemurteil/Polung/Neutralitätsbeweis. Vollständiger tatsächlicherStartauftragwortgetreu,Modellgpt-6.1-sol ultra geerbt interneVorgaben/Revisionunknown,Toolsangeboten/genutzt/tatsächlicheKommandosExit/TrennungsgrenzenSharedFS dokumentieren. KeinePeerslesen/weitereAgents/CommitPush/pnpmGesamtformatierung. VollständigabschließenOriginalberichtbewahrenPfadSHAundBefundsenden.
```

Der Auftrag steht zusätzlich bytegleich unter `outputs/loop/inventory002-ab-repro/startauftrag.txt`. Ich war frischer Reviewer, kein Autor und kein Eignungs-/Polungs-Erstbewerter. Es gab keinen weiteren fachlichen Auftrag oder eine Autorenverteidigung außerhalb des Pakets.

## Werkzeuge und Trennungsgrenzen

Angeboten waren die direkten Namespaces functions, clock, collaboration und mcp__cua_repl sowie 633 im functions-Katalog gelistete Nested Tools. Die vollständigen Metadaten und tatsächlich genutzten Werkzeuge sind in `offered-used-tools.json` erfasst. Genutzt wurden ausschließlich `functions.exec` mit `tools.exec_command`, `tools.view_image` und `tools.apply_patch`, Python-Standardbibliothek, bestehender Poppler und die bestehende gezielte pnpm/Prettier-Ausführung im kopierten Builder. Die Skills `pdf` und `unslop` wurden vor Anwendung gelesen. Kein Web-/Browserzugriff, keine Anmeldung, keine weiteren Agents, keine andere Modellfamilie, keine Installation, kein Conda, kein Commit/Push. Eine Fortschrittsnachricht ging über `collaboration.send_message` ausschließlich an den Koordinator; keine Peerurteile wurden empfangen oder gelesen.

Die Rollen- und Kontexttrennung ist organisatorisch. Das gemeinsame Dateisystem bietet keine technische Informationssandbox. Ich habe die Zugriffsbeschränkung eingehalten: keine Peer-/Jurorberichte, aktuellen Loopfindings oder Agentlisten geöffnet; keine ESS-Rohdaten, deren Hashes, Personenkennungen, Teil-A/B-Antworten, Partei-/LR-Werte oder Verteilungen, Credentials/Cookies oder Portal-Analysis gelesen. Public-Codebook-Kategorien und Variablennamen sind Dokumentationsmetadaten. Die lesenden Shells nutzten stets den genannten Worktree; Schreibzugriffe betrafen nur diesen Bericht und meine Outputs.

Die Prüfung ist vollständig abgeschlossen. AB-R01 benötigt eine wahrheitsgemäße Protokollkorrektur und erneute benannte Kontrolle in einer getrennten Fassung. Die vorhandenen offenen Zuordnungs- und Datenfragen behalten ihre Bedeutung; dieses Review hebt keine davon auf.
