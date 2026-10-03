# REPRO-003-C: unabhängiger Reproduktions-Erstbericht

Prüfdatum 2026-10-03. Reviewer `/root/repro003_c_repro`, kein Autor des Pakets. Geprüft wurde ausschließlich `reports/loop/packages/REPRO-003-C/v1/manifest.json`, SHA-256 `5cb5e10f09f32fa52a6929a33a92f56b384fe4a6af34fa583acb0e8c5feb11d3`, einschließlich der 16 eingefrorenen Dateien und 31 zusätzlich gebundenen sourceInputs. Arbeitsverzeichnis `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch `research/life-93-night-20261003`.

Der Nachbau ist im geprüften Umfang `BESTANDEN`: zwei eigene frische Fünfdatei-Kopien laden jeweils die drei fest gebundenen Original-PDFs neu herunter und erzeugen exakt die historischen C-v2-Bytes. Ein geringes, nicht blockierendes Finding RC-R01 betrifft die Protokollierung fehlgeschlagener HTTP-Versuche. Der vollständige Code-Erstbericht des anderen Reviewers ist nicht Teil meiner Prüfung und wurde nicht gelesen. Dieser Bericht allein erteilt daher keine gemeinsame Paketabnahme.

## Prüfgrundlage und Trennung

Vollständig gelesen wurden die gefrorenen Projektanweisungen, der Dauerauftrag, LIFE-93, Prüfregeln, Analyseplan, Analyseanforderungen, Lizenzakte, dieser konkrete Prüfauftrag, Nachbau-Dokument und Autorenbericht sowie alle drei Python-Dateien. Wegen einer gekürzten Toolanzeige wurde LIFE-93 anschließend vollständig in zwei Abschnitten erneut gelesen. `docs/project.md`, `docs/belegregister.md` und `docs/entscheidungen.md` wurden ergänzend als geltende Projektanweisungen gelesen; ihre verlinkten früheren Berichte wurden nicht geöffnet. Die öffentliche Inventardatei und Provenienz wurden als dokumentarische Eingaben, nicht als Antwortenmatrix behandelt. Eine spätere Strukturprüfung aller gebundenen Eingaben steht in `public-scope-inspection.json`.

Keine anderen Reviewer-/Jurorberichte, Loopfindings, Agentlisten oder zusätzliche Autorenverteidigung wurden gelesen. Kein weiterer Agent wurde gestartet. Die erste Dateinameninventur zeigte Namen anderer Pakete und Berichte, keine Berichtsinhalte. Die Anweisungsdokumente selbst erwähnen frühere Audits; diese Erwähnungen wurden nicht als unabhängige Evidenz übernommen.

Die organisatorische Trennung betrifft den frischen Prüferkontext und die getrennten Schreibpfade. Es bestand weiterhin ein gemeinsames Dateisystem mit breitem Werkzeugangebot. Ich behaupte keine OS-Sandbox, keine technisch erzwungene vollständige Isolation, kein akademisches Peer Review und keine Garantie wissenschaftlicher Gültigkeit.

Das Tool-/Auftragsprotokoll ist unter `outputs/loop/repro003-c-repro/` erhalten. `startauftrag.txt` enthält den tatsächlichen vollständigen Startauftrag im Wortlaut. Das Folgende ist keine ersatzweise verkürzte Auftragsfassung. `offered-tools.json` enthält die angebotenen Werkzeugmetadaten. Tatsächlich benutzt wurden `functions.exec`, darunter `exec_command`, `write_stdin`, `apply_patch`, `web__run`, sowie eine eigene Statusmeldung über `collaboration.send_message`. Auf Shellseite kamen Python-Standardbibliothek, vorhandenes Poppler, `pwd`, `git branch --show-current`, `rg`, `cat`, `sed` und `nl` zum Einsatz. Keine Connectoraktion, Installation oder Modellfamilienprüfung fand statt.

Die vom Startauftrag berichtete Modellkonfiguration ist `gpt-6.1-sol`, Reasoning ultra geerbt, dieselbe Codex-Familie. Ein separates Werkzeug zur Verifikation der internen Modellrevision stand nicht zur Verfügung; interne Revision und nicht zugängliche Anbietervorgaben bleiben unbekannt. Dies ist ein KI-Audit.

## Vorabprüfung der Pfade und Pins

Vor dem ersten Nachbau wurde der Manifesthash geprüft und jede der 47 gebundenen Dateien gegen Größe und SHA-256 gelesen. Die Pfade wurden absolut aufgelöst; absolute Manifestrelativpfade, Elternkomponenten, Ausbruch aus dem Worktree und symbolische Links in den gebundenen Pfaden wurden ausgeschlossen. Das dokumentarische Inventarschema, die Quellen-URLs und die deklarierten sourceInputs-Geltungsbereiche wurden überprüft. Kein Rohdatenpfad wurde geöffnet. `pins-before.json` hält jeden Pfad, jedes Ergebnis und die Schemabeobachtung fest. `pins-after.json` dokumentiert dieselbe Prüfung nach Abschluss und den Vergleich zur Vorabprüfung.

OWN ist ausschließlich `outputs/loop/repro003-c-repro/`. Die eigentlichen Ausführungskopien heißen `fresh-1/` und `fresh-2/`. Vor jedem Start wurde aus genau folgenden gefrorenen Dateien eine neue minimale Dateikopie erzeugt:

- `pipeline/reproduce_c_annotation.py`
- `pipeline/annotations/c_builder_v2.py`
- `pipeline/annotations/source_geometry.py`
- `data/inventar.entwurf.csv`
- `data/inventar.provenienz.json`

Diese Kopien sind keine Git-Klone. Sie enthielten anfangs keine PDF, Cache-, historische Annotation-, Autorenbuilder- oder Rohdatendateien. Insbesondere wurde die historische Zielannotation nur später zum Bytevergleich gelesen und niemals in eine Ausführungskopie gelegt. Der Wrapper wurde ausschließlich aus den eigenen Kopien gestartet. Das Livecode-Verzeichnis des ursprünglichen Worktrees war kein Ausführungsziel.

Die vollständigen Vorabauflösungen jedes ROOT-/OWN-/CACHE-/TARGET-/Log-/Arbeits-Pfads stehen in `preflight/fresh-1.json`, `preflight/fresh-2.json` und entsprechenden Gegenfall-Dateien. Aus `__file__` folgt jeweils der eigene Clone-ROOT. Der Builder hat zunächst cloneinterne Standardpfade unter `outputs/public-reproduction/c-v2`; vor seinem `main()` bindet der Wrapper OWN, CACHE und TARGET an den tatsächlich angelegten Zielpfad `outputs/public-reproduction/run`. Die eigene Nachbaukopie schreibt deshalb nur innerhalb ihres eigenen Clone-Verzeichnisses. Das ist eine Pfadkontrolle unter beobachteten Bedingungen, kein Nachweis gegen gleichzeitige bösartige Dateimanipulation.

## Zwei tatsächliche Nachbauten

Beide Kindprozesse liefen mit folgendem vollständigen argv in ihren jeweiligen eigenen Clone-CWDs:

```sh
/usr/bin/python3 pipeline/reproduce_c_annotation.py --output-dir outputs/public-reproduction/run
```

| Lauf | Tatsächliche UTC-Zeiten aus dem Sidecar | CLI-Exit | Sidecar | Ergebnis |
| --- | --- | --- | --- | --- |
| `fresh-1` | 08:26:59.939640 bis 08:27:02.152106 | 0 | `BESTANDEN` | Historische Zielbytes identisch |
| `fresh-2` | 08:27:02.231243 bis 08:27:04.383655 | 0 | `BESTANDEN` | Historische Zielbytes identisch |

Die drei echten Downloads je Lauf endeten mit HTTP 200 und unveränderten finalen URLs. Sie lagen jeweils im eigenen Ziel unter `sources/`, wurden gegen die exakten Pins geprüft und anschließend durch jeweils drei erfolgreiche `pdftotext -bbox`-Aufrufe verarbeitet. Keine historischen Cachepfade existierten in den Ausführungskopien.

| Öffentliche Originaldatei | Bytes | SHA-256 in beiden eigenen Läufen |
| --- | --- | --- |
| `ESS11_questionnaires_DE.pdf` | 1304009 | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| `ESS11_showcards_DE.pdf` | 2210799 | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| `ESS11_appendix_a7_e04_1.pdf` | 2162997 | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |

Die erzeugte Annotation umfasst 3418839 Bytes, 43 dokumentierte Identitäten und 1526 Belegobjekte. `fresh-1`, `fresh-2` und die eingefrorene historische Zieldatei sind vollständig bytegleich; SHA-256 `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e`. `byte-comparison.json` ist der ausgeführte Vergleich. Die Zahl der Belegobjekte ist eine Artefaktstruktur, kein Gütekennwert.

Beide tatsächlich aufgezeichneten Umgebungen nennen Python `3.14.7 (main, Aug 14 2026, 06:38:32) [GCC 16.2.1 20260810]`, Poppler `pdftotext version 26.08.0`, Versionsaufruf Exit 0. Die vollständigen Prozessaufrufe, UTC-Zeiten und stdout/stderr sind in `commands/fresh-1.json` und `commands/fresh-2.json` erhalten. Die Extraktionsaufrufe stehen in den jeweiligen `tool-exits.jsonl`; alle sechs haben Exit 0. Die anfänglichen fünf Dateien blieben in beiden positiven Kopien bytegleich zu den gefrorenen Eingaben.

## Tatsächlicher Lauf und historische Annotationmetadaten

`reproduction.json` beschreibt die neuen Zugriffe, Dateipfade, Pinwerte, Laufzeiten, Umgebung und technischen Status. In beiden eigenen positiven Läufen enthält es zusätzlich `scienceAcceptance: NICHT_GEPRÜFT` und `historicalAnnotationMetadataRetained: true`.

Die bytegleiche `annotation.json` beschreibt weiterhin die historische Autoren-/Korrekturfassung. Beispiele sind `authorStartedUtc: 2026-10-03T05:50:57Z`, die Autorenrolle `source annotation author`, historische Quellenpfade unter `outputs/loop/inventory002-ab/baseline-check-cache/` und `networkRefresh: NICHT_DURCHGEFUEHRT_DIESE_FASSUNG_NUTZT_GEPINNTE_BYTES`. Auch `peerOrJurorReportsRead: true` und `loopFindingsRead: true` stammen aus der erhaltenen historischen Korrekturmetadatenfassung. Sie beschreiben weder meinen Zugriff noch die neuen Prozesse. Ich habe diese Berichte und Findings nicht gelesen; die tatsächlichen eigenen Downloads sind im neuen Sidecar belegt.

Die alten Cache-, Lizenzlektüre- und Auftragsreferenzen sind historische Verweise, keine beim Nachbau benötigten Eingaben. Der Nachbau hat ihre Inhalte nicht geöffnet. `runtime-versus-historical.json` hält die tatsächlichen Sidecars, getrennte historische Metadatenfelder, Toolbefunde und die Feststellung fest, dass die historischen Cachepfade in beiden Kopien fehlen. Die Warnung im Nachbau-Dokument, Zeile 15, entspricht diesem beobachteten Unterschied. Die historischen Metadaten wurden deshalb nicht als aktuellen Selbstbericht beanstandet.

## Eigene echte Gegenfälle

Alle Veränderungen und Ziele lagen ausschließlich unter OWN. Neue Gegenfallkopien enthielten ebenfalls anfänglich nur die fünf freigegebenen Dateien. Die Mutationen sind mit Vorher-/Nachherhash oder tatsächlichem Symlink-/Werkzeugdelta erhalten. Es wurden keine gemeinsamen sourceInputs verändert und keine Rohdatenverzeichnisse gelesen.

| Eigener Gegenfall | Wirkliches Delta | Kind-Exit und beobachtetes Verhalten |
| --- | --- | --- |
| `counter-changed-pdf-pin` | Fragebogenpin im eigenen Wrapper durch 64 Nullen ersetzt | Exit 1; PDF-Pinfehler nach tatsächlichem Download, `NICHT_BESTANDEN`-Sidecar, keine Annotation |
| `counter-wrong-official-source` | Eigene Fragebogen-URL auf das offizielle Listenheft-PDF geändert; ursprünglicher Fragebogenpin bleibt | Exit 1; tatsächlich andere PDF-Bytes führen zum Pinfehler, keine Annotation |
| `counter-provenance-input` | Eine zusätzliche LF-Bytefolge an die eigene Provenienzdatei angehängt | Exit 1 vor Zielanlage; Eingabepinfehler auf stderr, kein neues Sidecar |
| `counter-poppler-exit17` | Eigenes ausführbares `pdftotext` im Kind-PATH gibt tatsächlich Exit 17 zurück | Exit 1 nach drei tatsächlichen Downloads; Extraktionslog erfasst Exit 17, `NICHT_BESTANDEN`-Sidecar, keine Annotation |
| `counter-dangling-output-symlink` | Tatsächlicher dangling Ziel-Symlink auf ein nicht vorhandenes Ziel innerhalb der eigenen Kopie | Exit 1 wegen symbolischem Pfad vor Zielanlage; verlinktes Ziel wird nicht angelegt |
| `counter-existing-fresh1-output` | Erneuter echter Aufruf mit dem vorhandenen eigenen erfolgreichen Ziel | Exit 1 vor Veränderung; komplette Vorher-/Nachherhashkarte aller Zieldateien ist identisch |
| `counter-official-http404` | Eigene Fragebogen-URL auf einen fehlenden öffentlichen Dokumentnamen desselben offiziellen Hosts geändert | Tatsächliches HTTP 404, Exit 1 und `NICHT_BESTANDEN`-Sidecar, keine Annotation; geringe Protokolllücke RC-R01 |

Die Herkunft einer im vorhandenen Ziel erhaltenen `BESTANDEN`-Datei wurde geprüft: Sie bleibt der Sidecar des vorherigen erfolgreichen Laufs und wird beim abgewiesenen Wiederholungsaufruf absichtlich nicht überschrieben. Sie ist kein Erfolgsbeleg des zweiten Aufrufs. Ebenso bedeutet Exit 0 des eigenen Testharness nur, dass die erwarteten Kindfehler wirklich beobachtet wurden. Die sieben vollständigen Fehlerausgaben und tatsächlichen Exits stehen in `commands/counter-*.json`; `countercase-summary.json` fasst sie zusammen. Pfad-/Eingabefehler ohne neues Sidecar entsprechen der dokumentierten Grenze in Zeile 17 des Nachbau-Dokuments.

## Originalquellen und Rechte

Vor dem Nachbau wurden die drei exakt gebundenen offiziellen PDF-Adressen direkt geprüft. Jeder Prefixabruf ergab HTTP 200 und eine PDF-Signatur. Diese Probe prüft Erreichbarkeit; die vollständigen Hashprüfungen stammen erst aus den zwei anschließenden neuen Downloads. Die tatsächlich benutzten URLs stehen vollständig in `source-probe.json`, in beiden eigenen Sidecars sowie in den gefrorenen Wrapperzeilen 20–22.

Die bibliografischen PDF-Seiten 1–2 wurden aus den eigenen neuen Downloads gelesen. Das Codebook nennt auf PDF-Seite 1 ausdrücklich ESS11, 2023 und Edition 4.1; die Kopfzeile auf PDF-Seite 2 nennt erneut Edition 4.1. Das Listenheft nennt Deutschland und 2023. Dies bestätigt die Dokumentfassung, keinen Ausgabenabgleich mit der Datendatei 4.2. Fundstellen und Extraktionsaufrufe sind in `primary-cover-readings.json`, `commands/primary-cover-*.json` und `primary-sources/*-cover-pages1-2.txt` erhalten. Inhaltliche Item-/Skalenabnahmen wurden daraus nicht abgeleitet.

Die [ESS-Bedingungen](https://www.europeansocialsurvey.org/contact/disclaimer), Abschnitt „Conditions of use“, wurden unabhängig direkt abgerufen, HTTP 200. Die eigene HTML-Datei hat SHA-256 `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d`. Dort werden CC BY-NC-SA 4.0 für Daten und CC BY-SA 4.0 für Dokumentation getrennt genannt. Die unmittelbar vorangehende Empfehlung bevorzugt Portalverlinkung gegenüber extern gespeicherten Datensätzen und verlangt Versions-/Änderungshinweise. Ein pauschales Weitergabeverbot wird daraus nicht abgeleitet.

Die [CC-BY-SA-Rechtsfassung](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en), §§ 2(a)(1), 3(a)(1), 3(b), und die [CC-BY-NC-SA-Rechtsfassung](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en), §§ 1(k), 2(a)(1), 3(a)(1), 3(b), wurden über das Webwerkzeug an den Originalfundstellen gelesen. Sie stützen die dokumentierte Unterscheidung von Dokumentationsrechten ohne NC-Klausel und Datenrechten mit NC-Klausel sowie Attribution und einschlägiger ShareAlike-Bedingung. Beide enthalten in § 2(a)(6) keine Befugnis, eine ESS-Billigung zu behaupten. Welche konkrete spätere Exportfassung lizenzrechtlich eine Bearbeitung enthält, wurde nicht abschließend beurteilt.

Ausgefallene Zugriffe bleiben sichtbar: Der Webabruf des ESS-Disclaimers meldete 502 und der Codebook-Webabruf einen internen Fehler; direkte Zugriffe und die anschließenden Downloads funktionierten. Direkte Pythonabrufe beider CC-Rechtsfassungen meldeten 403, während das Webwerkzeug die Primärtexte lieferte. Es gibt daher keine erfolgreiche eigene lokale Vollkopie der CC-Rechtstexte. Das sind ausgeführte Fehlabrufe, keine pauschale Quellen- oder Wissenschaftssperre. `source-readings.json` dokumentiert Zugang, Fundstelle, Grenze und Ergebnis.

## Finding RC-R01: fehlgeschlagener HTTP-Versuch ohne Quellenangabe im Sidecar

**Betroffene Aussage.** Das Nachbau-Dokument, Zeilen 15 und 17, nennt tatsächliche Zugriffszeiten und Laufstatus in `reproduction.json` und die Erfassung von Fehlern nach Zielanlage. Der Prüfauftrag, Zeile 7, verlangt nachvollziehbare tatsächliche Laufprovenienz.

**Problem.** Im Wrapper werden Dateiname, URL und Download-Startzeit lokal bestimmt, aber erst nach erfolgreichem `urlopen`, vollständigem Lesen und Dateischreiben an `sourceDownloads` angehängt. Bei einem HTTP-Fehler fehlen dort der fehlgeschlagene Dateiname, die URL, der Versuchsstart und HTTP-Status als eigenes strukturiertes Feld. Der allgemeine Fehlereintrag erhält nur Exceptiontyp und `str(error)`.

**Fundstelle.** Gefrorenes `pipeline/reproduce_c_annotation.py`, Zeilen 80–94 und 118–125. Tatsächlicher eigener Beleg `counter-http404-summary.json`, `commands/counter-official-http404.json`, `deltas/counter-official-http404.json` und `counter-official-http404/outputs/public-reproduction/run/reproduction.json`.

**Prüfbarer Beleg.** Der neue eigene Gegenfall änderte genau die Fragebogen-URL auf einen fehlenden öffentlichen Dokumentnamen auf demselben offiziellen Host. Der reale Netzwerkaufruf meldete HTTP 404. Der Prozess endete mit Exit 1. Sein Sidecar enthält `sourceDownloads: []`, `status: NICHT_BESTANDEN`, `errorType: HTTPError` und eine 404-Fehlermeldung, aber kein Feld für die tatsächlich versuchte URL oder ihren Start. Eine Annotation wurde nicht erzeugt.

**Wirkung und Schwere.** Gering, nicht blockierend für die beiden positiv belegten Nachbauten. Ein fehlgeschlagener Zugriff lässt sich aus diesem Sidecar allein nicht vollständig einer Quelle und Versuchszeit zuordnen. Ein erhaltener konkreter Code-/Deltastand und die feste Reihenfolge ermöglichen die Rekonstruktion; diese zusätzlichen Artefakte werden aber benötigt. Kein falscher Erfolg, keine Rohdatenexposition und keine Überschreibung wurde beobachtet.

**Gegenbelege.** Das allgemeine Fehlerprotokoll wird geschrieben, kennzeichnet den Lauf korrekt als fehlgeschlagen und enthält Anfang/Ende des Gesamtlaufs. Vollständige erfolgreiche Downloads sind in beiden positiven Sidecars korrekt dokumentiert; Hashabweichungen nach erfolgreichem Download erhalten URL und tatsächlichen Hash. Die Dokumentation verspricht keine OS-Sandbox. Diese Gegenbelege begrenzen das Finding auf unvollständige Fehlversuchsprovenienz.

**Konkrete Korrektur.** Vor dem Zugriff einen Versuchseintrag mit Dateiname, erwarteter URL/Pin und Startzeit anlegen; Erfolg oder Fehler anschließend mit Ende, HTTP-Status soweit vorhanden, finaler URL soweit vorhanden und tatsächlichem Dateipfad/Hash soweit erzeugt ergänzen. Fehlende Werte als fehlend lassen. Die historischen Annotationbytes bleiben dabei erhalten.

**Nachprüfung.** Zwei unveränderte positive Minimalnachbauten müssen erneut exakt `70ad2061…` ergeben. Zusätzlich einen tatsächlich ausgeführten fehlgeschlagenen Zugriff auf eine eigene begrenzte URL durchführen und prüfen, dass Exit 1, `NICHT_BESTANDEN`, keine Annotation sowie der konkrete fehlgeschlagene Versuch mit URL/Dateiname und Beginn/Ende erhalten sind. Die Korrektur wurde in dieser Erstprüfung nicht durchgeführt; Status `OFFEN`.

## Begrenztes Urteil und offene Abnahmen

| Prüfbereich | Ergebnis und Geltung |
| --- | --- |
| Gemeinsame Manifest-/Dateipins und beobachtete sichere Pfade | `BESTANDEN`, Vorher-/Nachhervergleich aller 16 + 31 Einträge |
| Eigener Minimalnachbau und offizielle Pinbindung | `BESTANDEN`, zwei reale komplette Läufe, keine Autorenbuilder-/Cacheabhängigkeit |
| Historische Zielbytes | `BESTANDEN`, zwei eigene Artefakte bytegleich zur gebundenen historischen Zieldatei |
| Trennung neuer Laufprovenienz von historischen Metadaten | `BESTANDEN` für die beiden neuen positiven Läufe; geringe Fehlversuchsprotokolllücke RC-R01 offen |
| Eigene ausgeführte begrenzte Gegenfälle | `BESTANDEN` hinsichtlich erwarteter Abbrüche und eigener unveränderter Zielbytes; kein allgemeiner Sicherheitsnachweis |
| Behauptete Trennung der Daten-/Dokumentationslizenzen | `BESTANDEN` als überprüfter Quellenbefund im genannten Umfang; keine rechtsfachliche oder konkrete Exportfreigabe |
| Vollständige semantische Prüfung der C-v2-Annotation und separate Korrekturnachprüfung | `NICHT_GEPRÜFT` durch diesen Reproduktionsbericht |
| Eignung, Polung, Auswahl, Konstrukt-/Messmodellentscheidungen und ESS-Analyse | `NICHT_GEPRÜFT` |
| Codebook-4.1-/Datenausgabe-4.2-Abgleich | `NICHT_GEPRÜFT` |
| Reliabilität, Validität, Invarianz, Neutralität und persönliche Unsicherheitsbereiche | `NICHT_GEPRÜFT` |
| Andere Modellfamilie, Website-/Browser-/Releaseabnahme und menschlicher Verständnistest | `NICHT_GEPRÜFT` |
| `pnpm check` und breites Repository-/Website-Testing | `NICHT_GEPRÜFT`; im abgegrenzten unveränderlichen Erstprüfauftrag ausdrücklich nicht auszuführen |

Das Nachbaupaket kann im belegten technischen Reproduktionsumfang beurteilt werden. Daraus folgen keine Fragenaktivierung, methodische Freigabe, Präregistrierungs-/Modell-Tags, Entblindung, Veröffentlichung oder Websiteabnahme. Keine Anforderung wird durch formale Textpräzisierung als empirisch bestanden bezeichnet.

## Erhaltene Belege und Freeze

Alle eigenen Quellen, Skripte, Minimaldateikopien, Fehlerdeltas, Logs und Kandidaten liegen ausschließlich unter `outputs/loop/repro003-c-repro/`. Die ausführbare Grundlage ist `review_runner.py`; die tatsächlichen Kindprozesse stehen vollständig in `commands/`. `session-actions.md` dokumentiert Befehle, Exits, Toolausfälle und die Grenze der nachträglich beschriebenen vorbereitenden Inline-Lesungen.

Der eigene Bericht wird nach vollständigem Schreiben nicht mehr geändert. `own-index.json` verzeichnet jedes eigene reguläre Artefakt mit Größe und SHA-256, den absichtlich erzeugten eigenen Symlink als Symlink sowie den vollständigen Bericht mit SHA-256. `freeze.json` nennt Bericht- und Indexhash. Index und Freeze enthalten keinen eigenen rekursiven Selbsthash. Der abschließende Freeze-Prozess prüft vor seiner Ausgabe sämtliche gemeinsamen Paket- und sourceInputs-Pins erneut. Diese Hashes binden die tatsächlich geprüfte Fassung, keine wissenschaftliche Freigabe.
