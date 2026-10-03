# INVENTORY-002-AB v2: unabhängige Reproduzierbarkeitsnachprüfung

Erster vollständiger Bericht, abgeschlossen 2026-10-03T06:29:16.881699+00:00. Prüffassung v2, Reparaturrunde 1. Modell laut erhaltenem Koordinatorauftrag `gpt-6.1-sol`, Denkaufwand `ultra`, geerbt. Interne Revision und nicht zugängliche Anbieterregeln sind unbekannt; eine unabhängige Introspektion dieser Modellangaben ist nicht möglich.

Die eng begrenzte Korrekturprüfung ist `BESTANDEN`. AB-S01 sowie der gemeinsame niedrige Befund AB-S02/AB-R01 sind in Runde 1 für diese Fassung nachgeprüft. Ich fand kein neues belegtes Finding und vergebe daher keine neue Kennung AB2-Rxx. Die ursprünglichen IDs und ihre Rundenzählung bleiben bestehen. 61 Quellen-/Versionsrestpunkte bleiben offen. Dieser KI-Audit ist keine Phase-1-, wissenschaftliche Gesamtinventar-, Eignungs-, Polungs- oder Neutralitätsabnahme.

## Gebundene Fassung und Unabhängigkeit

Autoritatives Manifest `reports/loop/packages/INVENTORY-002-AB/v2/manifest.json`, SHA-256 `2fe41dba331a3775c9a4a254f8136ded551f54c864cb9aea21b6c375863a4bd4`, eingefroren laut Manifest am 2026-10-03T06:08:31.458833+00:00; Code-Commit laut Manifest `595ab8b77fff1a32404691b3d4d6dd8de9e3e6ab`. Maßgeblich sind die gefrorenen Dateibytes und SourceInput-Hashes. Die geprüfte JSON hat 2.485.639 Bytes und SHA-256 `31a4fa49c0149f3aec5820fcb30fb85388a09dcd5470393b9f259cf9013fceb8`.

Die originale v1-Rückbindung ist Manifest-SHA-256 `5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856`, JSON-SHA-256 `9554a568c1a08fe7d6676960dd7e41d2b50d1ad7c16c5d8d33bfed4edc44c138`. Eigene sichere Vorher-/Nachherkontrollen bestanden für v1 10 Dateien + 89 SourceInputs sowie v2 14 Dateien + 168 SourceInputs. Beide Manifestdateien wurden ebenfalls gebunden, insgesamt 283 Prüflistenzeilen. Das ist ein Integritätsnachweis im festgelegten Umfang und kein Semantikbeweis.

Vor jedem SourceInput-Bytezugriff verlangt mein Guard einen relativen erlaubten Pfad ohne Traversal, Sperrordner oder Symlink, einen aufgelösten Pfad innerhalb des Worktrees sowie eine der tatsächlich manifestierten öffentlichen Scopeformulierungen. Unbekannte oder gesperrte Inputs würden nicht geöffnet. `before-hashes.json` und `after-hashes.json` enthalten alle Einzelvergleiche. Ihre Zeilen sind vollständig identisch.

Ich war an Autorarbeit, Erstprüfungen und bisherigen Korrekturen nicht beteiligt. Gelesen wurden die gefrorenen Projektanweisungen, Projektstand, dauerhafte Auftrag, vollständiges LIFE-93, Prüfregeln, Analyseanforderungen, Lizenzakte, v1-/v2-Prüfaufträge, Originalautorenbericht, vollständiger Korrekturbericht, Vorabpläne und ursprüngliche Erstberichte als ausdrücklich freigegebene Korrekturhistorie. Die abgeschlossenen Originalerstberichte sind sources `76bd287adea616f6964e2f86c24ecc63d8f24616f8908dd4abb72fae848671a4` und repro `74b5a6c5cf941741f411285dad1094f7de74a5cb1fe6f2021f564b5e12d38f51`. Große kombinierte Ausgaben waren anfangs begrenzt; kleinere Folgeaufrufe vervollständigten die erforderliche Lektüre. Eine Dateinamensinventur ist dokumentiert; ich las keine aktuellen Nachprüferurteile, Jurorberichte, Loopfindings, Agentlisten oder nachgelieferte Verteidigung.

## AB-S01, Runde 1: Originaleinleitung und Antwortkopf getrennt

Betroffene Aussage war die Originaleinleitung von B19–B22 mit gemeinsamer Beleg-ID `QCTX-behav-intro2`. In v1 enthielt sie zusätzlich `Ja Nein (Antwort (Weiß`, die vier Anfänge des separaten Antwortspaltenkopfs. Das ursprüngliche mittlere Finding betrifft eine semantisch falsche Einleitungsannotation für vier Identitäten. Es belegt keinen Rechen-, Daten- oder Eignungsfehler.

Ich extrahierte den öffentlichen deutschen Fragebogen frisch mit Poppler, renderte PDF-/gedruckte Seiten 9 und 10 neu und las beide Bilder tatsächlich mit `view_image`. Quelle ist der gepinnte [ESS11-Fragebogen Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), SHA-256 `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`. Es fand kein neuer Netzabruf statt; geprüft wurde diese lokale Originalfassung.

Auf Seite 9 endet die zweite Verhaltenseinleitung mit „Haben Sie... BITTE VORLESEN...“. Der folgende Kopf gehört visuell zu den Antwortspalten. Meine Auswahl verlangt vollständige Wortboxeinschließung in `(x0=0,x1=595,y0=379,y1=429.5)`. Die letzte Einleitungsbox endet bei y=429.409532; die erste Kopfbox beginnt bei y=429.688381. Genau 37 Originaltokens bleiben, ohne Kopfwort. Ihr selbst rekonstruierter Text ergibt SHA-256 `de17ced533eddefe84f4ee7c1ee28f52def0afcece5729f932eafbf88986785d`.

Der gemeinsame v2-Beleg stimmt vollständig mit diesem eigenen Auszug überein: Originalquelle, PDF-/gedruckte Seite 9, Region, vollständige Tokenboxen, exakter Text und Extrakthash. Alle vier Kontextfelder führen genau einmal den unveränderten Belegnamen und enthalten genau die gelesene Einleitung. Der Antwortkopf bleibt in den separaten Kategoriebelegen. Meine unabhängigen Gegenproben hängen den ursprünglichen Kopf an B19, B20, B21 und B22 und weisen jeden Fall ab.

Nachprüfung `BESTANDEN` im benannten Korrekturumfang. Originalfundstelle und konkrete Wirkung des alten Problems bleiben dokumentiert; v1 und die Erstberichte wurden nicht umgeschrieben.

## AB-S02/AB-R01, Runde 1: tatsächliche 08-Gegenfälle und erhaltene Historie

Die alte Behauptung einer ausgeführten „invented B24 code08“-Gegenprobe war falsch bezeichnet. Das ursprüngliche `read_tests.py:115`, SHA-256 `a7f6f09559aca3414d5d940964da98535f64c6b2f02ca14e8a04d07d41c3eb16`, hängt eine tiefe Kopie der ersten Kategorie 01 an. Mein eigener Nachvollzug erzeugt `01,02,03,04,05,06,07,09,01`; er enthält keine 08. Originalskript und Originaloutput mit dem alten Namen bleiben unverändert. Die neue Korrektur benennt diesen historischen Lauf ausdrücklich als Duplikat 01 und behauptet keine rückwirkende 08-Ausführung.

Originalfundstelle ist derselbe Fragebogen, PDF-/gedruckte Seite 10, B24. Die sichtbare Liste druckt 01–07 und 09 ohne 08; der separate B25-Filter druckt weiterhin 08. Diese Originalinkonsistenz bleibt erhalten. Die Codebook-4.1-Information zu 8/dieBasis gegenüber 9/Die PARTEI und 55/Other wurde im strengen Erhaltungsdiff gebunden; ich beanspruche hier keine neue vollständige Codebook-Originallesung. Der ursprüngliche niedrige Befund betrifft die tatsächlich protokollierte Testoperation und deren Nachprüfbarkeit, keine nachgewiesene falsche Ausgangskategorie.

Die umgeleitete neue Testkopie wurde tatsächlich ausgeführt. Ihr vollständiges Ergebnis ist inhaltlich und strukturell identisch mit dem eingefrorenen neuen Autorenoutput. Eigene zusätzliche Tests importieren weder Autorenbuilder noch Autorentester. Beide Prüfreihen enthalten folgende konkrete Fälle:

| Kontrolle | Tatsächliche mutierte Codefolge | Kategorienzahl | Ablehnung |
| --- | --- | --- | --- |
| Historisches angehängtes Duplikat 01 | 01,02,03,04,05,06,07,09,01 | 8 → 9 | true |
| Echte Einfügung 08, Label dieBasis | 01,02,03,04,05,06,07,08,09 | 8 → 9 | true |
| Gleichlange Ersetzung ausschließlich 09 → 08 | 01,02,03,04,05,06,07,08 | 8 → 8 | true |

Bei der gleichlangen Ersetzung bleiben sämtliche Kategorienlabels unverändert. Die feste erwartete Originalfolge bleibt `01,02,03,04,05,06,07,09`. Ein AST-Vergleich bindet die ursprüngliche und korrigierte Kategorien-Gleichheitsfunktion unverändert; die vollständig gelesenen v1/v2-Programmdiffs zeigen unveränderte Originalerwartungen und nur ergänzte Kontext-/Gegenprüfungen. Keine Toleranz wurde gelockert. Die künstliche 08 existiert ausschließlich in In-memory-Kopien, nicht in der Ergänzung.

Nachprüfung `BESTANDEN` für den gemeinsamen niedrigen Befund. AB-R01 bleibt das Duplikat von AB-S02 und erhält keine zusätzliche Runde. Eigene Läufe ersetzen nicht die historische Autorenoperation.

## Vollständiger Diff und kontrollierter Nachbau

Mein selbst geschriebener `verify_diff.py` liest die zwei gefrorenen JSONs und vergleicht das gesamte Dokument. Er verlangt exakt die dokumentierte Korrekturmetadata als vollständiges Dictionary, einschließlich weiterhin offener Abnahmen. Er prüft den gemeinsamen Beleg gegen die eigene Originalbeobachtung, lässt je betroffener Zeile genau ein `text_original` ändern und verlangt danach Gleichheit des gesamten restlichen Dokuments. Der Getter für Belegreferenzen und alle übrigen Kontextfelder bleiben gleich.

Der konkrete Diff hat 13 Einträge: vier Kontexttexte; am gemeinsamen Beleg Text, Extrakthash, y1 und vier entfernte Tokens; die zusätzliche Korrekturmetadata als ein ausdrücklich vollständig geprüftes Dictionary; `peerOrJurorReportsRead` false → true wegen der autorisierten ursprünglichen Erstberichte. Die 835 anderen Belege sind exakt gleich. Für jede der 52 Identitäten werden zusätzlich Antwortformat, Fragebogenkategorien, Fragebogen-/Datenmissing, Codebookkategorien/-metadata/-Location und Kartenstrukturen vollständig verglichen und mit identischen Strukturhashes gebunden. Alle 61 globalen und je Frage zugeordneten Restpunkte bleiben identisch. Die komplette residuale Gleichheit schützt auch Wortlaute, Filter, Weiterleitungen, Kandidaten und Zuordnungsgrenzen.

Sechs eigene Gegenfälle prüfen, dass der strenge Diff unerlaubte Kategorie-, Restpunkt-, Beleg- und Metadataänderungen, eine falsche unabhängige Abnahme sowie eine wieder verunreinigte Einleitung abweist. Dies prüft die eigene Diffkontrolle; es schafft keine neue fachliche Abnahme der unveränderten Felder.

Autorprogramme mit festen Schreibzielen wurden nie direkt ausgeführt. Ich kopierte zuerst Builder, Tester und Shellrezept byteidentisch in Own und erfasste Original-/Kopiehashes. Am Builder änderte ich genau vier Pfadstellen: OUT, neues eigenes JSON-Ziel und zwei eigene Kopien der unveränderten Korrekturplan-/Vorherhashinputs. Am Tester änderte ich genau OUT und DEST. Das Shellrezept erhält ausschließlich umgeleitete Own-Pfade; es wurde nicht als Ganzes ausgeführt. Die relevanten Einzelkommandos wurden tatsächlich ausgeführt. Alle Unified-Diffs und Inputkopiehashes liegen in `adaptation.json` und den `.diff`-Dateien. Die Metadataverweise innerhalb der erzeugten JSON bleiben original, damit die gebundene v2-Bytefassung reproduzierbar ist.

| Programm | Eingangs-SHA-256 | Own-SHA-256 nach Pfadanpassung |
| --- | --- | --- |
| build_ab.py | 74e481f651b23fbcd5020609db2dac96a73fda69ec659ee4f7fcf231c30a824b | e1d6f4eb9d0d20b719026f63a7aa72fdfcc3cc95050d764f66ae8cf52889d2cc |
| read_tests.py | c99e61af8f0d304086e9a9d1c33497d3a7bc53e1e0f71a173a4052eb9e851bcb | 00a4f109ee2f6e3bfd6bcf297c84e4631d0a52079b59fb35de09bc05cc436886 |
| reproduce.sh | 1c1eee6c21ce0dd6a865a16eae0d5bb34a9b797bd65f87bfba23540e131a9bd8 | 58e792b266a8963e2b131ab1ad369f11240a3c5187539a5599dca3d397aa6c7d |

Zwei eigene Builderläufe ergaben jeweils exakt die 2.485.639 Bytes der eingefrorenen JSON, SHA-256 `31a4fa49c0149f3aec5820fcb30fb85388a09dcd5470393b9f259cf9013fceb8`. Der erste Nachbau bleibt zusätzlich separat erhalten. Die kopierten neuen Autorentests meldeten 7547 begrenzte Checkereignisse, null Fehler und alle neun Autorengegenfälle abgewiesen. Die eigene Prüfung meldet sieben unabhängige Gegenfälle, darunter beide echte 08-Fälle und vier Einleitungskontrollen. Solche Zähler sind kein Qualitäts-, Vollständigkeits- oder Neutralitätsmaß.

## Tatsächlicher Prüfstatus und Grenzen

| Prüfung | Ergebnis | Bedeutung |
| --- | --- | --- |
| Sichere v1 10+89 und v2 14+168 Vorher-/Nachherbindung | BESTANDEN | Gleiche geprüfte Public-Bytes; keine Semantikabnahme |
| Eigene visuelle Originallesung Q9/Q10 und 37-Token-Beleg | BESTANDEN im Korrekturumfang | Selbst gelesene Originalfundstellen |
| Selbständiger Ganzdokumentdiff 4 Kontexte / 1 Beleg / ausdrückliche Metadata | BESTANDEN | 835 Belege, 52 Strukturen und 61 Restpunkte identisch |
| Eigener kontrollierter zweimaliger Nachbau | BESTANDEN | Bytegleich zur manifestierten v2 |
| Neue Autorentests und eigene echte 08-/Einleitungsgegenfälle | BESTANDEN | Tatsächliche synthetische Mutationen und Ablehnung |
| Prettier auf eigenes Nachbauziel | ignored=true, inferredParser=null | Kein Formatvalidierungsnachweis trotz Exit 0 |
| pnpm check / Gesamtformatierung / Browser- oder UI-Test | NICHT_GEPRÜFT durch diesen Reviewer | Enger Schreibbereich, keine UI-Änderung; Repositorychecks beim Koordinator |
| Empirische ESS-Analyse | IN_DIESER_PHASE_NICHT_ERFORDERLICH; nicht ausgeführt | Prüfung öffentlicher Korrekturmetadata braucht keine Antworten |
| Gesamtinventar-/Phase-1-/Eignungs-/Polungs-/Neutralitätsabnahme | NICHT_GEPRÜFT | Unveränderte Inhalte erhalten dadurch keine neue wissenschaftliche Abnahme |

Die unveränderten Restpunkte umfassen 52 Versions-/Datenmissinggrenzen, zwei Wahlcrosswalks, drei Partei-Codeübertragungen, zwei B24/B25-08-Konfliktaufzeichnungen und zwei Dauer-Kodierungsabgleiche. Die 4.1-Dokumentation wird nicht zu einer geprüften 4.2-Antwortkodierung erklärt. Lizenzmetadata und Quellenzugriffe bleiben identisch; keine neue Rechts- oder Veröffentlichungsfreigabe.

## Tatsächliche Kommandos und eigene Korrekturen

Die folgenden argv wurden durch `protocol.py run` tatsächlich im genannten Worktree ausgeführt. UTC-Start/Ende sowie vollständige stdout/stderr stehen in `commands.jsonl` und den einzelnen Logs.

| Lauf | Tatsächlicher Befehl | Exit |
| --- | --- | --- |
| q-render | `pdftoppm -f 9 -l 10 -r 130 -png outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab-v2-repro/q` | 0 |
| s-bbox | `pdftotext -bbox-layout outputs/loop/inventory/ESS11_showcards_DE.pdf outputs/loop/inventory002-ab-v2-repro/showcards.bbox.html` | 0 |
| q-bbox | `pdftotext -bbox-layout outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab-v2-repro/questionnaire.bbox.html` | 0 |
| c-bbox | `pdftotext -bbox-layout outputs/loop/inventory/ESS11_appendix_a7_e04_1.pdf outputs/loop/inventory002-ab-v2-repro/codebook.bbox.html` | 0 |
| original-observation | `python3 outputs/loop/inventory002-ab-v2-repro/read_original_boundary.py` | 0 |
| adapt | `python3 outputs/loop/inventory002-ab-v2-repro/adapt.py` | 0 |
| builder | `python3 outputs/loop/inventory002-ab-v2-repro/build_ab.py` | 0 |
| author-tests | `python3 outputs/loop/inventory002-ab-v2-repro/read_tests.py` | 0 |
| strict-diff | `python3 outputs/loop/inventory002-ab-v2-repro/verify_diff.py` | 0 |
| strict-diff-corrected-control | `python3 outputs/loop/inventory002-ab-v2-repro/verify_diff.py` | 0 |
| builder-second | `python3 outputs/loop/inventory002-ab-v2-repro/build_ab.py` | 0 |
| independent-checks | `python3 outputs/loop/inventory002-ab-v2-repro/independent_checks.py` | 0 |
| own-file-info | `pnpm exec prettier --file-info outputs/loop/inventory002-ab-v2-repro/inventar-ab.v2.reproduced.json` | 0 |
| version-python | `python3 --version` | 0 |
| version-node | `node --version` | 0 |
| version-pdftotext | `pdftotext -v` | 0 |
| version-pdftoppm | `pdftoppm -v` | 0 |
| version-pnpm | `pnpm --version` | 0 |

Direkte vorbereitende Lese-/Inline-Pythonaufrufe, ihre Exitwerte und Zwecke stehen in `startup-calls.md`; ihre vollständigen flüchtigen stdin-Bodies liegen im tatsächlichen Tooltranskript. `protocol.py init` und die direkte Nachherprüfung hatten Exit 0. Die resultwirksamen Prüf- und Erzeugerskripte sind vollständig gespeichert. Der im kopierten Builder enthaltene Prettier-Unterprozess beendet sich wegen `check=True` bei Fehler; beide Builderaußenaufrufe hatten Exit 0. Das frische eigene File-info-Ergebnis ist `ignored: true, inferredParser: null`, daher kein erfolgreicher Formatcheck.

Eine frühe Dateinamensuche enthielt irrtümlich den nicht vorhandenen Outputpfad `inventory002-ab-v2`; `rg` meldete den Fehler, während der letzte Pipelineprozess Exit 0 hatte. Das wurde nicht als Inputprüfung ausgegeben. Die tatsächliche Korrektur liegt unter `inventory002-ab-correction`.

Meine erste synthetische Diff-Gegenprobe trug die Bezeichnung B19, wählte aber über den festen Listenindex 26 B20. Die Ablehnung selbst war korrekt; ihre Bezeichnung war falsch. Ich bewahrte die erste Checkerfassung und den ersten Gegenkontrolloutput getrennt als `verify_diff.first-mislabeled.py` und `whole-diff-negative-controls.first-mislabeled.json`. Danach wählte ich B19 ausdrücklich über seine Identität und führte den strengen Diff erneut aus, Exit 0. Der vollständige Dokumentdiff blieb unverändert. Die separate unabhängige Einleitungsprüfung mutiert jede der vier Identitäten ausdrücklich. Dies ist eine dokumentierte eigene Werkzeugkorrektur, kein Finding über v2 und kein verschleierter neuer Autorenlauf. Andere tatsächliche eigene Prüfläufe scheiterten nicht.

## Tatsächlicher vollständiger Startauftrag

```text
Frischer unabhängiger Reproduzierbarkeitsnachprüfer INVENTORY-002-AB v2 Runde1, bisherunbeteiligt. ShellCWD /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. AutoritativeManifest reports/loop/packages/INVENTORY-002-AB/v2/manifest.json SHA2fe41dba331a3775c9a4a254f8136ded551f54c864cb9aea21b6c375863a4bd4,14Dateien/168SourceInputs. GefroreneAGENT/Auftrag/Issue/Prüfanforderungen, V2Prüfauftrag, vollständigerAutorKorrekturreport, v1Rückbindung und ursprünglicheErstberichte alsKorrekturhistorie selbstlesen. KEINE aktuellenNachprüferurteile/Agentlisten/Loopfindings/Jurorberichte/nachgelieferteVerteidigung. EigenerOriginalquellencheckQ9/10 anFundstellen plus eigenständiger strengerGanzdokumentdiff: genauvierB19–22Contexts+1gemeinsamerBeleg+ausdrücklicheVersionsmetadata geändert;835übrigeBelege/alle52Kategorien/Missing/Codebook/Karten und61Restpunkte identisch. Eigene kontrollierteByteReproduktion v2 in outputs/loop/inventory002-ab-v2-repro/: AutorenBuilder/reproduce/Testsniemalsdirektausführenfestepfade!nurKopien gezielt Own/JSONOutput umstellen,DiffHashbelegen. NeueTests+eigeneGegenfälle tatsächliche08EinfügungUNDgleichlange09→08Ersetzung mitgenauenCodefolgen ablehnen, historische01Duplikatbehauptungkorrigiertnichtumgeschrieben. Kontexte37TokensQCTX-behav-intro2/429.5BBox/HashsauberkeinenAntwortkopf. Original10+89 sowiev2 alle14+168Hash/SafePfadScope vor/nachunverändert. PublicOriginals/SyntheticMetadatanur;keinESSrawlocalA/Bantworten/ParteiLRwerte/Verteilungen/angemeldetesPortalAnalysis/Secrets/globalWrites/Conda/Install/Geräte/CommitPush/Gesamtformat/weitereAgents. AktiveCSV/Parser/Quellcache/Autorenprogramme/Outputs/Paketeunverändert. BerichtNUR reports/loop/reviews/INVENTORY-002-AB-v2-repro.md plusOwnOutputs. KI-AuditengbegrenzteNachprüfung,keinePhase1/wissenschaftlicheVollInventar-/Eignungs-/Polungs-/Neutralitätsabnahme; Hashzahlen/ignoredPrettierkeineSemantik. JedesFindingAB2-RxxgenaueBehauptung/Problem/Originalfundstelle/Wirkung/begründeteSchwere/KorrekturNachprüfung/Vermutungsklar;sameProblemalteIDs/RundenbeibehaltenkeineFindingquote. Vollständiger tatsächlicherStartauftragwortgetreu,Modelgpt-6.1-solultrageerbtinternunknown,Toolsangebot/Nutzung/CommandsExits/Fehlversuche/SharedFSGrenzen dokumentieren. Originalberichtimmutable; abschließenSHA+Befund.
```

Der Wortlaut steht außerdem in `startauftrag.txt`. Ich erhielt keine zusätzliche fachliche Verteidigung oder Peerurteile. Fortschrittsmeldungen an den Koordinator änderten den Auftrag nicht.

## Werkzeuge, Shared-FS und unveränderte Artefakte

Angeboten waren die direkten Namespaces functions, clock, collaboration und mcp__cua_repl sowie 633 Nested-Toolmetadaten, vollständig in `offered-tools.json`. Genutzt wurden `functions.exec` mit `tools.exec_command`, `tools.apply_patch` und `tools.view_image`, dazu `collaboration.send_message` ausschließlich für eigene Fortschrittsmeldungen an `/root`. Python-Standardbibliothek, bestehender Poppler und bestehendes pnpm/Prettier wurden genutzt. Gemessene Versionen: Python 3.14.7, Poppler 26.08.0, Node v24.21.0, pnpm 11.23.0; alle Versionsaufrufe Exit 0. Die Skills `pdf` und `unslop` wurden vor Anwendung gelesen. Kein Web-/Browserzugriff, keine Installation, kein Conda, keine weiteren Agents, keine andere Modellfamilie, kein Commit/Push, keine Gerätesteuerung oder globale Änderung.

Shared-FS bietet keine technische Informationssandbox. Die Unabhängigkeit beruht auf frischem begrenztem Auftrag, eingefrorener Prüffassung und eingehaltenen Lesebeschränkungen. Die gesamte 10+89- und 14+168-Kette stimmt vor/nach überein. CSV, Provenienz, Parser, öffentliche Quellpins/-caches, ursprüngliche Programme, Autorenoutputs, Ergänzungen, Erstberichte und Pakete sind darin gebunden und unverändert. Eigene Writes betreffen ausschließlich diesen einen neuen Bericht und `outputs/loop/inventory002-ab-v2-repro/`. Nicht manifestierte Fremdartefakte wurden nicht zu eigener Autorarbeit erklärt; ein systemweiter Änderungsnachweis wird nicht behauptet.

Keine ESS-Roh-/Zwischendaten aus data/raw oder data/local, Antwortdaten A/B, Personenkennungen, Partei-/LR-Antwortwerte oder Verteilungen, Rohdatenhashs, Credentials/Cookies, Portal-Anmeldung oder Portal-Analysis wurden geöffnet oder ausgegeben. Öffentliche Fragen, Variablen- und Kategorienmetadaten sind Dokumentationsinputs, keine Antwortdaten. Ungeprüfte Quell-/Versions- und wissenschaftliche Abnahmen bleiben offen.

Die Own-Artefakte enthalten Startauftrag/Vorabplan, Toolangebot und Laufprotokoll, sichere Vorher-/Nachherlisten, frische Originalauszüge/Bilder und eigene Originalbeobachtung, unveränderte und umgeleitete Programmkopien samt Diffs/Hashbindungen, beide eigenen JSON-Nachbauten, neue kopierte Quellenlesetests, unabhängige Gegenproben, strengen Ganzdokumentdiff, erhaltene eigene frühe Fehlbezeichnung sowie diesen Berichterzeuger. `artifacts-index.json` bindet die endgültigen Dateilängen und Hashes; der Index schließt seinen eigenen Selbsthash aus. `report-integrity.json` hält nach Erstellung den endgültigen Berichthash fest. Dieser erste vollständige Bericht wird nach Übergabe nicht geändert.
