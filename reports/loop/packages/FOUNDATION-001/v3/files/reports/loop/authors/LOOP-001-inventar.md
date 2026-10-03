# LOOP-001: Autorenentwurf des deutschen ESS11-Frageninventars

Stand: 2026-10-03. Autorrolle: abgegrenzter Quellen-/Inventar-Autor im laufenden Codex-Auftrag, keine getrennte Erstbewertung, kein Reviewer und keine Claude-Bewertung. Verwendet wurden die dieser Sitzung zugewiesene Codex-Laufzeit, Python 3.14.7 und Poppler 26.08.0. Eine präzisere Modellkennung ist mir nicht als verifizierte Laufzeitmetadaten verfügbar. Es wurde kein weiterer Subagent gestartet.

Das Ergebnis ist ein belegter, teilweise strukturierter ENTWURF mit 296 Zeilen. Es ist noch kein vollständig geprüfter, modellfähiger Originalfragenbestand und keine Phase-1-Abnahme. Keine Zeile enthält eine endgültige Aufnahmeentscheidung oder Polung. Der Aufbau liest ausschließlich die unten genannten öffentlichen Dokumentations-PDFs. ESS-Rohdaten, Personenkennungen, Antwortzeilen, A/B-Teilmengen, Parteiverteilungen und Portal-Analysis wurden nicht geöffnet.

## Artefakte und Ausgangsbeleg

- `data/inventar.entwurf.csv`: Originalwortlaut, Originalantwortblock, Kategorien/Missingcodes mit Entwurfsstatus, Kontext, Variablenbeleg, Seiten, Quellenhash, Antwortgegenstand/-typ und vorläufiger Ausschlussstatus.
- `data/inventar.provenienz.json`: Quellen, Lizenzevidenz, Werkzeugstände, Aufbauhash, Abdeckung, exakte Restlisten und Wortlautprüfung.
- `pipeline/inventar.py`: reproduzierbarer Aufbau und Abgleich; keine automatische Auswahl oder Polung.
- Dieser Bericht: tatsächlicher Umfang, Befunde und Grenzen der Autorenarbeit.

Der vollständige tatsächliche Startauftrag ist wortgetreu in `reports/loop/authors/LOOP-001-inventar-auftrag.txt` gesichert. Vor den eigenen Änderungen wurden HEAD, vorhandener Git-Status und die Hashes der gelesenen Auftrags-/Regeldateien in `outputs/loop/inventory/baseline.json` gesichert. Abrufe sind in `outputs/loop/inventory/downloads.json` protokolliert. Die PDFs, Textauszüge, Renderings und weiteren Prüfprotokolle liegen ausschließlich unter dem ignorierten `outputs/loop/inventory/`. Kein vollständiger PDF-Download wurde in einen Git-Zielpfad kopiert.

## Offizielle Quellen und Lizenz

| Quellen-ID             | Fassung und Umfang                                                    | SHA-256                                                            |
| ---------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| ESS11-DE-QUESTIONNAIRE | Deutscher ESS11-Fragebogen, 100 PDF-Seiten                            | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| ESS11-DE-SHOWCARDS     | Deutsches ESS11-Listenheft, 100 PDF-Seiten                            | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| ESS11-CODEBOOK         | Integrierte Variablendokumentation 4.1, 552 PDF-/551 gedruckte Seiten | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |

Die genauen offiziellen URLs stehen im Provenienzartefakt und im Aufbauprogramm. Die vorhandenen Quellenkataloghashes wurden mit den tatsächlich heruntergeladenen Dateien abgeglichen. Zielkandidat ist ESS11-Datenedition 4.2; diese Autorenarbeit verwendete ausschließlich das dokumentierte Codebook 4.1. Der editionsübergreifende Variablen-/Kodierungsabgleich bleibt offen. Es wurde hierfür keine Antwortdatei gelesen.

Die live abgerufene [ESS-Nutzungsbedingung](https://www.europeansocialsurvey.org/contact/disclaimer) unterscheidet Daten unter CC BY-NC-SA 4.0 von Dokumentation unter CC BY-SA 4.0. Gesicherter HTML-Beleg: `outputs/loop/inventory/ess-disclaimer.html`, SHA-256 `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d`. Das Inventar übernimmt Fragebogen-/Listenheftdokumentation unter der Dokumentationslizenz. Jede Zeile und die Provenienz enthalten Quellenangabe, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), Änderungsvermerk und den Hinweis, dass keine ESS-Billigung vorliegt. Die konkrete Veröffentlichungsprüfung des Inventars bleibt als Gate offen; dies ist keine juristische Abnahme. Das Aufbauprogramm wurde nicht pauschal unter die Dokumentationslizenz gestellt.

Verwendete ESS-Zitation: European Social Survey European Research Infrastructure (ESS ERIC) (2025). ESS round 11 - 2023. Social inequalities in health, Gender in contemporary Europe. Sikt - Norwegian Agency for Shared Services in Education and Research. https://doi.org/10.21338/ess11-2023.

Der Browserabruf von Disclaimer/Listenheft scheiterte mit Gateway-/Internal-Error; direkte öffentliche Abrufe mit Python gelangen. Diese Grenze wurde nicht als fehlende Quelle übergangen.

## Erfasster Umfang

Der Parser erfasst 254 tatsächliche gedruckte Frage-/Einleitungslabel-Vorkommen und ergänzt die 42 getrennten männlichen/weiblichen H-Porträts. Ergebnis: 296 Zeilen, 249 unterschiedliche Original-Labels. Die wiederholten Haushaltsfelder F2/F3/F4 erhalten eigene Inventar-IDs mit öffentlicher Fundstellen-Suffixierung. Diese Suffixe kennzeichnen Dokumentstellen und keine Befragten.

| Modul | Zeilen |
| ----- | -----: |
| A     |      6 |
| B     |     46 |
| C     |     43 |
| D     |     34 |
| E     |     32 |
| F     |     69 |
| H     |     44 |
| I     |      9 |
| K     |      4 |
| J     |      9 |

Die Erfassung enthält die Einstellungs-, Werte-, Wahrnehmungs- und gesellschaftlichen Präferenzfragen sämtlicher dieser Module, nicht nur vorab erwartete Themen. Persönliche Angaben, Verhalten, Gesundheit, Verwaltung sowie klar relevante ausgeschlossene Partei-/Regierungsfragen bleiben nachvollziehbar im selben Entwurfsinventar. Die vorläufigen Statuszahlen sind 137 `ENTWURF_OFFEN`, 44 `ENTWURF_AUSSCHLUSS_NACH_ISSUE`, 102 `ENTWURF_AUSSERHALB_AUFNAHME`, 12 `ENTWURF_KONTEXT_ODER_VERWALTUNG` und eine Außen-Prüfvariable B26. Dies sind Autorenannotationen zur Prüfung, keine akzeptierte Itemliste. C30 wird beispielsweise nicht allein wegen seines Klimabezuges als Wissensfrage ausgeschlossen; E2–E5 bleiben als Grenzfälle eigener Eigenschaften/Werte offen.

Nummerierungslücken werden aus dem deutschen Fragebogen übernommen. C44 aus der internationalen Modulübersicht ist im deutschen Dokument nicht als Originalfrage vorhanden; ein nummeriertes R-Item wurde ebenfalls nicht gefunden. Die Modulübersicht ersetzt daher keine nationale Vollständigkeitsprüfung. Die exakte erfasste Label-/Seitenliste steht in `coverage.capturedLabels`. Fünf zunächst gefundene Referenzen wurden nach Sichtung als Filterverweise verworfen: C11 auf PDF-Seite 21, F4 auf 58, F19 auf 65 und 66 sowie K1 auf 97. Die tatsächliche K1-Frage auf 97 bleibt erfasst.

## Wortlaut, Kategorien und Kontext

`wortlaut_de` wird aus den PDF-Wortkoordinaten gewonnen. Zeilenumbrüche, sichtbare Trennstriche, Schreibweisen und Satzzeichen werden erhalten; es erfolgt keine Umformulierung oder automatische Enttrennung. Jede Wortlautregion trägt die exakte PDF-Seite, Koordinaten und Wortfolge. Daneben bleibt der Originalblock mit Hash erhalten. Dieser enthält gegebenenfalls Kontext vor dem nächsten Label und ist kein bereinigter Fragebogen zur direkten Ausspielung.

226 Antwortblöcke sind als Entwurf strukturiert: 73 aus Tabellenköpfen/-zeilen, 153 aus vertikalen Code-/Labelzeilen. 70 stehen noch als Originalantwortblock mit offenem Status. Die Quelltokenprüfungen sichern die tatsächlich kopierten Token; sie beweisen noch nicht die vollständige semantische Kategoriezuordnung. Auch die 226 strukturierten Blöcke benötigen einen zeilenweisen Abgleich. Skalen ohne beschriftete Binnenpunkte erhalten keine erfundenen Beschriftungen. Bei reinen Buchstabenantworten muss die Bedeutung aus dem Listenheft noch vervollständigt werden.

73 Missingcodeblöcke stammen aus direkt zugeordneten Fragebogentabellen, 200 aus sichtbaren Codepaaren mit ausdrücklich noch nachzuprüfender Zuordnung; bei 23 Zeilen bleibt das Feld offen. Das Feld heißt `missingcodes_fragebogen`: Codes wie 66/99 aus dem integrierten Datencodebook werden nicht stillschweigend als gedruckte deutsche Antwortmöglichkeit ausgegeben. Der vollständige Abgleich Fragebogen-/Datencodes bleibt offen.

Für 51 Zeilen wurde geerbter Originalkontext gesondert mit Koordinaten übernommen, darunter Institutionenvertrauen, politische Handlungen, die Klimafilter-/Randomisierungsblöcke sowie I1–I9. Die 42 H-Porträts behalten Originaleinleitung und E1-Geschlechtsfilter. Bei 203 weiteren Zeilen bleibt der Seitenkontext mit offenem vollständigen Routingabgleich dokumentiert. Auch bereits übernommener Kontext ist noch keine akzeptierte Routingregel.

Die Listenheftreferenzen führen Quelle, Hash und Seitenfundstellen zur ausdrücklich gedruckten Listennummer. Ein vollständiger Bild-/Kategorienabgleich aller Listenheftseiten ist nicht durchgeführt.

## Konkrete Befunde und visuelle Stichproben

- Codebook-PDF-Seite 21 / gedruckt 20 weist `prtvgde1` und `prtvgde2` den deutschen B14DE1/B14DE2-Adaptionen zu. Die deutschen B14a/B14b-Originalantworten werden nicht mit den integrierten Parteicodes gleichgesetzt. Der Parteibezug dient ausschließlich dem Ausschlussbeleg.
- Codebook-PDF-Seite 546 / gedruckt 545 nennt für `testji9` die Location C36, während die deutsche Originalfrage I9 auf Fragebogen-PDF-Seite 96 steht. I9 bleibt `OFFEN_WIDERSPRUCH_CODEBOOK`; `testji9` wird nicht automatisch C36 zugeschlagen.
- Deutsche Schul-/Ausbildungsfelder F15/F44/F52/F55 bleiben offen; keine Gleichsetzung mit harmonisierten Bildungsvariablen. F33/F34/F34a und F47–F49 sind als gemeinsame Berufs-Kodierungsquellen dokumentiert, nicht als drei eigenständige messfertige Variablen ausgegeben.
- H1/H2 umfassen jeweils A–U; sämtliche 42 Originalporträts bleiben getrennt. Die Ha-u-Zuordnung ist ein dokumentierter Inhaltsabgleich, keine angenommene Polung.
- Quelleigenschaften wie `versucht,die` in H1.I, der fehlende Schlusspunkt in H2.M, die sichtbare Trennung `Manch mal` im D-Tabellenkopf und `Äußerst wahrscheinlich}` bei I7 wurden nicht sprachlich geglättet. Der D20–D27-Kopf auf Seite 39 wird auch für die Folgeseite 40 belegt.
- Die quelleneigene Darstellung von C31-DK auf PDF-Seite 26 verteilt 88 auf zwei Zeilen. Diese Darstellung wurde visuell überprüft und mit einer spezifischen Zuordnungsnotiz dokumentiert.

Visuell betrachtet wurden Fragebogen-Seiten 7, 8, 13, 14, 26, 39, 40, 43, 49, 51, 54, 67, 85–92, 95 und 96 sowie Codebook-Seiten 12, 21, 63, 165, 533 und 546. Die Codebook-Stichproben zeigen Originalmetadaten, keine Antwortverteilungen. `outputs/loop/inventory/visual-checks.json` benennt Renderdateien, Hashes und den tatsächlichen Sichtungsumfang. Eine erste skalierte Poppler-Ausgabe zeigte stellenweise abgeschnittene Bereiche. Feste DPI beziehungsweise Cairo/ungeskalierte Ausgaben machten die betroffenen Bereiche korrekt sichtbar; der Fehler wurde nicht als PDF-Quellfehler gewertet. Die Seiten wurden nicht als vollständige visuelle Abnahme aller 100 Fragebogen- oder Listenheftseiten ausgegeben.

## Reproduktion und tatsächliche Checks

Aus dem Repository-Wurzelverzeichnis:

```sh
python3 pipeline/inventar.py fetch
python3 pipeline/inventar.py build
python3 pipeline/inventar.py check
```

`fetch` ist der gesonderte öffentliche Downloadschritt und akzeptiert nur die drei festgelegten Quellen mit ihren Hashes. `build` und `check` benötigen die lokalen Dokumentationsdateien und führen keinen Rohdaten- oder Portalzugriff aus. Bei abweichenden Quellen-, Aufbau- oder CSV-Hashes scheitert der Abgleich. Benötigt werden Python-Standardbibliothek und Poppler `pdftotext`.

Tatsächlich durchgeführt:

- Wiederholter Aufbau und Quell-/Wortlautabgleich: 296 Zeilen, null technische Fehler; kein endgültiger Itementscheid.
- Zwei aufeinanderfolgende Aufbauten lieferten identische CSV- und Provenienzdateien. Beleg: `outputs/loop/inventory/verification.json`.
- Drei getrennte Negativkontrollen im Speicher: eine veränderte E20-Wortlautzeile, veränderte E19-Kategorien und veränderter I9-Kontext wurden jeweils zurückgewiesen. Die gespeicherten Inventarzeilen wurden dafür nicht manipuliert.
- Die Prüfungen vergleichen Quellenhashes, ausgegebene Wort-/Kategorie-/Kontexttoken, erfasste Zeilen und alle 42 Porträts sowie einzelne zuvor gelesene Regressionstellen. Sie validieren keine wissenschaftliche Eignung, vollständiges Routing oder umfassende semantische Kodierung.
- `pnpm check` wurde ausgeführt und stoppte bei `format:check` an der gemeinsam bearbeiteten `reports/loop/state.json`. Der gesondert gestartete Handbuchcheck meldete zwei Semikolon-Abweichungen in den fremdbearbeiteten `home.html`/`project.html`; Typecheck, Tests und Build liefen jeweils mit Exit 0 durch. Logs: `outputs/loop/inventory/pnpm-*.log`. Diese Beobachtung betrifft den gleichzeitigen Arbeitsstand, keine unveränderliche Gesamtfreigabe. Der Koordinator übernimmt die weiteren globalen Checks. Die App wurde durch diesen Autor nicht verändert, daher kein eigener UI-/Browserabnahmelauf.

## Exakte Restliste und Übergabegrenze

`coverage.pendingByCriterion` in `data/inventar.provenienz.json` enthält die konkreten IDs: 29 offene Variablenzuordnungen, 70 noch nicht zellenweise strukturierte Antwortblöcke, 23 offene Missingcodeblöcke und 203 Zeilen mit offenem vollständigem Kontext-/Routingabgleich. `checks.pending_rows` nennt 205 betroffene Inventarzeilen samt Gründen; die Mengen überlappen. Bereits als ENTWURF strukturierte Kategorien, Missingcodes und geerbte Kontexte brauchen zusätzlich ihre in den Statusfeldern genannte Prüfung. Diese Restliste ist kein bestandener Prüfbericht.

Die offenen Variablenzuordnungen betreffen F2/F3/F4 samt Wiederholungen, F14a, die acht deutschen Bildungsfragen, H1/H2 als Einleitungen, I9 und J1–J9. Zusätzlich bleiben die Edition-4.2-Verifikation, die genaue Listenheftbedeutung der Buchstabenkategorien, die nationale Vollständigkeitsabnahme und die konkrete Lizenz-/Veröffentlichungsprüfung offen. Es erfolgte kein eigener Commit oder Push. Ein eingefrorenes Autorenpaket kann jetzt getrennt begutachtet werden; Modellrechnung und endgültige Item-/Polungsentscheidung werden daraus nicht freigegeben.

## Abgabehashes

| Datei                           | SHA-256                                                            |
| ------------------------------- | ------------------------------------------------------------------ |
| `pipeline/inventar.py`          | `4f49a267327e72662614048de74a1fd27d0b6bb28da36823ccc0716ec5a4af3b` |
| `data/inventar.entwurf.csv`     | `685e4c7114129d0cbd6625018c38c1a1f9900b51581d711bf24a548f10aac1c2` |
| `data/inventar.provenienz.json` | `ed989bd8c25a8bc4167045303874b163a4d14a8a338361d5c32355f0421fd9b3` |
