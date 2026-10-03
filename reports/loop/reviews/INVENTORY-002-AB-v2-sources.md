# INVENTORY-002-AB v2: unabhängige Quellen- und Kontextnachprüfung

Die eng begrenzte Korrekturprüfung ist **BESTANDEN**. AB-S01 sowie der gemeinsame historische Befund AB-S02/AB-R01 sind in Reparaturrunde 1 nachgeprüft. Ich fand kein neues belegtes Problem, das eine AB2-S-Kennung benötigt. B19–B22 enthalten genau die vollständige Originaleinleitung ohne Antworttabellenkopf. Die neue 08-Einfügung und die gleichlange 09→08-Ersetzung werden tatsächlich ausgeführt und abgewiesen. Die frühere Duplikat-01-Operation bleibt als frühere Operation erhalten.

Das Urteil gilt für die Korrektur dieser Quellenannotation. Es ist keine Gesamtinventar-, Wissenschafts-, Eignungs-, Polungs-, Neutralitäts-, Phase-1- oder Veröffentlichungsfreigabe. Die 61 Quellen-/Versionsrestpunkte bleiben offen. Ein bytegleicher Buildernachbau gehört zur getrennten Reproduzierbarkeitsnachprüfung; ich habe keinen Builder ausgeführt und behaupte deren Ergebnis nicht.

Rolle: frischer, bislang unbeteiligter Quellen-/Kontextnachprüfer. Erste protokollierte Hashprüfung 2026-10-03T06:11:13.520398+00:00; Berichtsabschluss 2026-10-03T06:22:53.465621+00:00. Modell laut tatsächlichem Auftrag `gpt-6.1-sol`, Denkaufwand `ultra`, geerbt. Interne Modellrevision und nicht zugängliche Anbieterregeln bleiben unbekannt; die zugewiesene Modellangabe wurde nicht unabhängig introspektiert.

## Fassung, Eingaben und tatsächliche Lektüre

Autoritative Fassung: `reports/loop/packages/INVENTORY-002-AB/v2/manifest.json`, SHA-256 `2fe41dba331a3775c9a4a254f8136ded551f54c864cb9aea21b6c375863a4bd4`; Manifest-Codecommit `595ab8b77fff1a32404691b3d4d6dd8de9e3e6ab`. Gefrorene v2-Ergänzung SHA-256 `31a4fa49c0149f3aec5820fcb30fb85388a09dcd5470393b9f259cf9013fceb8`. Original-v1-Rückbindung: Manifest `5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856`, Originalergänzung `9554a568c1a08fe7d6676960dd7e41d2b50d1ad7c16c5d8d33bfed4edc44c138`.

Alle 14 gefrorenen Dateien und 168 SourceInputs wurden vor und nach der Prüfung anhand der Manifestpfade, des öffentlichen Scopes, der Dateilängen und SHA-256 kontrolliert. Auch die unveränderte ursprüngliche 10+89-Kette besteht vor und nach der Arbeit. Die vollständigen Listen sind `before-hashes.json` und `after-hashes.json`; sie sind gleich. Relative sichere Pfade, Worktreegrenze und Ausschluss von raw/local/Secrets-Pfaden werden vor dem Hashzugriff verlangt. Der finale Guard prüft zusätzlich jeden Pfadbestandteil auf Symlinks und die aufgelöste Grenze. Keine unbekannte oder gesperrte Quelle wurde gelesen. Hashintegrität ist ein Fassungsnachweis, kein Semantikbeweis.

Vollständig selbst gelesen wurden die gefrorenen AGENTS- und Projektregeln, der dauerhafte Auftrag, LIFE-93, Prüfregeln, Analyseanforderungen, Lizenzakte, ursprünglicher und neuer Prüfauftrag, die freigegebene Korrekturentscheidung sowie der ursprüngliche und der vollständige neue Autorenbericht. Beide originalen Erstberichte wurden ausschließlich als ausdrücklich freigegebene Korrekturhistorie vollständig gelesen: Quellenbericht `76bd287adea616f6964e2f86c24ecc63d8f24616f8908dd4abb72fae848671a4`, Reprobericht `74b5a6c5cf941741f411285dad1094f7de74a5cb1fe6f2021f564b5e12d38f51`. Hinzu kamen die ursprünglichen/neuen Vorabpläne, die originale Negativkontrollstelle, der vollständige neue Tester, die konkrete Buildergrenze und die zugehörigen tatsächlichen Original-/Korrekturprotokolle. Eine zunächst große kombinierte Toolausgabe war abgeschnitten. Begrenzte vollständige Folgelektüren der Pflichttexte sind mit Zeilenbereichen protokolliert.

Ich habe keine aktuellen Nachprüferurteile, Peerberichte anderer laufender Pakete, Agentlisten, Loopfindings, Jurorberichte oder nachgelieferte Verteidigung gelesen. Der anfängliche Dateinamensuchlauf listete auch historische Auditdateinamen; deren Inhalte wurden nicht als Eingaben dieses Reviews geöffnet. Eine kurze Memory-Suche fand keinen projektrelevanten Treffer; keine Erinnerung war Evidenz.

Die Quelle ist der lokal erneut gehashte öffentliche deutsche ESS11-Fragebogen, SHA-256 `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`. Original Q9 und Q10 wurden frisch als Text/BBox extrahiert, neu gerendert und beide vollständigen Bilder tatsächlich mit `tools.view_image` betrachtet. PDF-Seite und gedruckte Seite sind jeweils 9 beziehungsweise 10. Originalquelle: [ESS11-Fragebogen Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf). Lokaler Sourcepin: :codex-file-citation{path="/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/inventory/ESS11_questionnaires_DE.pdf" purpose="source"}.

Der Gegenstand ist der gepinnte öffentliche Dokumentstand. Ich führte keine neue Netzabfrage oder Portal-Anmeldung aus. Der vorhandene Downloadbeleg nennt den 2026-10-03 als Zugriffstag; diese historischen Downloadangaben sind lokale Protokolle, keine unabhängig signierten Zeitstempel. Die unveränderten übrigen Pins sind deutsches Listenheft `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca`, Codebook 4.1 `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` und Disclaimer `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d`. Die frischen automatischen BBox-Checks des kopierten Testers betreffen alle drei PDF-Pins. Eine eigene neue Vollinventar-/Gesamtcodebook- oder Listenheft-Sichtprüfung wurde hier nicht ausgeführt. Dokumentations- und Datenlizenz bleiben getrennt; keine rechtliche Veröffentlichungsfreigabe und kein Datenvergleich mit 4.2.

## AB-S01: reine Originaleinleitung, Runde 1 nachgeprüft

Ursprüngliche Aussage und Problem: Das als Originaleinleitung bezeichnete gemeinsame Kontextfeld B19–B22 enthielt nach „Haben Sie... BITTE VORLESEN...“ zusätzlich `Ja Nein (Antwort (Weiß`. Diese vier Fragmente gehören zum darunter liegenden vierteiligen Antworttabellenkopf. Der ursprüngliche Befund ist belegt, Schwere mittel. Seine Wirkung wäre ein verstümmelter Antwortkopf im später genutzten Einleitungstext; ein Rechen-, Antwortdaten- oder Eignungsfehler wurde nicht behauptet. Dieselbe Ursache und Reparaturrunde behalten AB-S01 als Kennung.

Eigene Originalfundstelle: ESS11-DE-QUESTIONNAIRE, PDF-/gedruckte S.9, zweite Verhaltensbatterie B19–B22. Die visuelle Lektüre zeigt einen vollständigen Absatz und die Vorleseanweisung oberhalb der separat ausgerichteten Ja-/Nein-/Missing-Spalten. Der letzte vollständige Einleitungstoken endet bei `y1=429.409532`. Der erste Kopf beginnt bei `y0=429.688381`. Dies sind getrennte semantische Bestandteile; ihre bloße Präsenz in derselben PDF wäre kein Einleitungsbeweis.

Meine eigene Auswahl vollständig eingeschlossener Wortboxen aus der frischen Originalextraktion in `x0=0, x1=595, y0=379, y1=429.5` enthält genau 37 Tokens. Sie rekonstruiert mit Originalzeilenumbrüchen:

```text
Denken Sie weiterhin an verschiedene Möglichkeiten, wie man versuchen kann, etwas in Deutschland zu
verbessern oder zu verhindern, dass sich etwas verschlechtert. Haben Sie im Verlauf der letzten 12 Monate
irgendetwas davon unternommen?
Haben Sie... BITTE VORLESEN...
```

Der vollständige String, alle 37 Tokenboxen und die Quelle stimmen exakt mit `belegregister.QCTX-behav-intro2` überein. Der selbst berechnete UTF-8-Extrakthash ist `de17ced533eddefe84f4ee7c1ee28f52def0afcece5729f932eafbf88986785d`; die ursprüngliche verunreinigte Fassung hatte `026a2c6be4f6e6b2d7cead4c4a870165ebf4f2f508bd53d19c8c84c5b52d3aac` und 41 Tokens. Alle vier geerbten Textfelder enthalten genau eine passende Eintragung und Referenz auf denselben korrigierten Beleg. Einleitungsstatus und sonstige Kontexte sind erhalten, Antwortkategorien und Missinglabels stehen weiterhin getrennt.

Nachprüfung: `independent_tests.py` prüft die vollständigen Strings, Referenzen, vollständigen Boxen, Quellenhash, PDF-/Druckseite und Extrakthash. Eigene In-memory-Gegenfälle hängen bei jeder der vier Identitäten den Kopf an, entfernen den letzten Vorlesetoken oder ändern die Referenz. Alle zwölf werden abgewiesen. Der kontrolliert kopierte Autorentester weist die vier tatsächlichen Kopfanhänge ebenfalls ab. Eigener Witness: `original-boundary-observation.json`. Status dieser Korrektur: BESTANDEN. Das ist keine vierfach unabhängige Ursache und keine endgültige semantische Abnahme aller Fragen.

## AB-S02/AB-R01: echte 08-Proben, wahre Historie

Ursprüngliche Aussage und Problem: Der originale Autorenlauf bezeichnete die Operation als `invented B24 code08`, hing jedoch eine Kopie der ersten B24-Kategorie 01 an. Originalprogramm `outputs/loop/inventory002-ab/read_tests.py:115`, SHA-256 `a7f6f09559aca3414d5d940964da98535f64c6b2f02ca14e8a04d07d41c3eb16`, und der ursprüngliche Output bleiben erhalten. Meine eigene Nachbildung der Operation erzeugt `01,02,03,04,05,06,07,09,01` ohne 08. Der ursprüngliche Test erkannte ein Duplikat 01 und belegt keinen damaligen echten 08-Lauf.

Schwere des gemeinsamen historischen Befunds: niedrig. Der damalige Prüfbericht benannte den ausgeführten Fall falsch; die ursprüngliche B24-Annotation wurde dadurch nicht als fehlerhaft nachgewiesen. AB-R01 bleibt der dokumentierte Duplikatbefund von AB-S02. Es entsteht keine neue Kennung oder neue Reparaturrunde für dasselbe Problem.

Eigene Originalfundstelle: ESS11-DE-QUESTIONNAIRE, PDF-/gedruckte S.10. B24 druckt acht Kategorien `01,02,03,04,05,06,07,09`, keine 08. Meine eigene frische Extraktion der Code-Spalte `x380–398, y95–250` bestätigt genau diese Folge. Auf derselben vollständig betrachteten Seite nennt der gedruckte B25-Filter ausdrücklich `01,02,03,04,05,06,07,08,09`. Der Widerspruch bleibt in der v2-Annotation, den beiden Filterrestpunkten und `QCTX-filter-b25` erhalten. Das Codebook-4.1-Metadatenfeld ist davon weiterhin getrennt. Hier wurde kein Rohdaten-Importvertrag beschlossen.

Die neuen tatsächlichen Kontrollen sind:

| Lauf | Konkret mutierte Codefolge | Tatsächliche Ablehnung |
| --- | --- | --- |
| Historische Operation ehrlich erneut ausgeführt | 01,02,03,04,05,06,07,09,01 | true; enthält keine 08 |
| Neue echte Einfügung, expliziter Code08/Label dieBasis | 01,02,03,04,05,06,07,08,09 | true; Kategoriezahl 8→9 |
| Neue gleichlange Ersetzung ausschließlich 09→08 | 01,02,03,04,05,06,07,08 | true; Kategoriezahl 8→8, alle Labels erhalten |

Ich führte diese drei Fälle selbst mit unabhängig aus der Originalseite festgehaltener Erwartung aus. Zusätzlich wurde der vollständige neue Autorenprüfer in einer Kopie mit nur einer Own-Pfadzeilenänderung tatsächlich ausgeführt. Auch dort sind beide echten 08-Fälle samt Codefolgen, gleicher Ersatzlänge und erhaltenen Labels nachgewiesen. Seine Negativkontrollobjekte stimmen exakt mit dem eingefrorenen Korrekturlog überein. Der Gleichheitstest und die Erwartung `01…07,09` wurden nicht gelockert. Mein eigener Gegenfall entfernt zusätzlich 08 aus dem B25-Filter und wird ebenfalls abgewiesen.

Der Korrekturbericht und die v2-Metadata beschreiben den alten Fall wahrheitsgemäß als Duplikat01 und die echten08-Fälle als neue Kontrollen. Das ursprüngliche falsch benannte Outputobjekt wurde nicht umgeschrieben. Die neuen Reviewer-/Autorenläufe ersetzen die historische Operation nicht rückwirkend. Nachprüfung und konkrete Witnesses: `independent-results.json/negativeControls`, `read-tests.json/negativeControls`, `final-evidence.json`. Status der Korrektur in Runde1: BESTANDEN.

## Ganzdokumentvergleich und erhaltene Grenzen

Mein eigener Checker vergleicht das komplette v1- und v2-JSON rekursiv. Die vollständige Blattdifferenz ist in `independent-results.json/leafDiff` erhalten. Geändert sind genau die vier Textstrings für B19–B22 sowie bei `QCTX-behav-intro2` der Originalstring, dessen Hash, y1 und die Tokenliste. Hinzu kommen ausschließlich `korrektur` und die transparente Umstellung von `zugriffsgrenzen.peerOrJurorReportsRead` auf true für die zwei nun autorisierten abgeschlossenen Erstberichte.

Nach Rückführung ausschließlich dieser bekannten Änderungen ist das gesamte restliche Dokument exakt gleich. Die Versionsmetadata enthalten Originalhash, Version2/Runde1, Korrekturauftrag, die verifizierten Erstberichtshashes, die wahre Testhistorie und weiterhin NICHT_GEPRUEFT für wissenschaftliche/weitere unabhängige Abnahmen. Originalautorenauftrag, Quelle, Zugriffs- und Lizenzmetadata bleiben sonst gleich. Das ist ein strenger Ganzdokumentvergleich, keine offene Toleranzliste.

Alle 52 Kategorien-, Sonderantwort-, Missing-, Datenmissing-, Codebook- und Kartenstrukturen sind vollständig identisch. Die eigenen Strukturhashes sind je ID erhalten. Auch Originalwortlaute, Intervieweranweisungen, Filter, Weiterleitungen und bestätigte/offene Zuordnungen bleiben gleich. Von 836 Belegen ist nur der eine Einleitungsbeleg geändert; die 835 anderen sind exakt gleich. Alle 61 vollständigen Restpunktobjekte samt IDs, Texten, Status und Referenzen sind gleich. Keiner wurde geschlossen.

Der ursprüngliche Inventarstand von 296 Identitäten und 205 technischen Restzeilen wurde hier nicht erneut geparst oder als semantisch abgenommen erklärt. Es wurde kein 205−52-Abzug gemacht. Offene Wahlcrosswalks, Interview09 gegenüber Codebook09/55, 08-Filterwiderspruch und Zeitfeld-/Datenmissingverträge wurden nicht neu entschieden. Codebook4.1 ist kein ausgeführter Vergleich mit Antwortdatei4.2. Die neue Kontextkorrektur hebt keine getrennten Erstbewertungen, methodischen Nachweise oder menschlichen Voraussetzungen auf.

## Tatsächliche Prüfungen und kontrollierte Kopie

| Gegenstand | Ergebnis | Grenze |
| --- | --- | --- |
| v2-Manifest, 14 Dateien +168 Inputs vor/nach | BESTANDEN, Exit0 | Fassung/Pfad/Public-Scope; keine Semantik |
| v1-Rückbindung, ursprüngliche 10+89 vor/nach | BESTANDEN, Exit0 | Originale einschließlich Programme/Outputs unverändert |
| Frischer Q9/10-Text, BBox und Rendering | BESTANDEN, drei Exit0; beide Bilder tatsächlich gelesen | Eigene visuelle Lektüre nur dieser zwei Originalseiten |
| Eigene 37-Token-/4-Kontext-/Referenz-/Hashprüfung | BESTANDEN, Exit0 | Kontextkorrektur AB-S01 |
| Eigener strenger kompletter v1/v2-Diff | BESTANDEN, Exit0 | 52 Strukturen,61 Restpunkte,835 andere Belege unverändert |
| 16 eigene tatsächliche Negativfälle | BESTANDEN, alle abgewiesen | 3 B24-Fälle,12 Kontextfälle,1 B25-Filterfall; In-memory |
| Ausschließlich umgeleiteter neuer Autorentester | BESTANDEN, Exit0;7547 Ereignisse,0 Fehler | Reproduktion des Testverhaltens; Zähler kein Qualitätsmaß |
| Neue/alte Kontrollhistorie und Erstberichtshashes | BESTANDEN, Exit0 | Wahre neue Tests, keine Rückdatierung |
| Builder-/reproduce.sh-Nachbau durch mich | NICHT_GEPRÜFT, nicht ausgeführt | Gegenstand der getrennten Reproprüfung |
| `pnpm check` und Gesamtformatierung durch mich | NICHT_GEPRÜFT, nicht ausgeführt | Enger Auftrag verbietet gemeinsame Build-/Formatwrites; Koordinator führt Repositorycheck nach Übernahme aus |
| Empirische ESS-Untersuchung | IN_DIESER_PHASE_NICHT_ERFORDERLICH, nicht ausgeführt | Öffentliche Quellenkorrektur benötigt keine Antworten |
| Wissenschaftliche Gesamtinventar-/Eignungs-/Polungs-/Neutralitätsabnahme | NICHT_GEPRÜFT | Dieser KI-Audit ersetzt diese Nachweise nicht |

Der neue Tester wurde erst bytegleich in `author_read_tests.py` kopiert, dann genau eine Zielzeile angepasst. Original-/Voradaptionshash ist `c99e61af8f0d304086e9a9d1c33497d3a7bc53e1e0f71a173a4052eb9e851bcb`; der angepasste Hash ist `fdd8d130132ef014b9acec5d9975e3b31c9308efbe49928f92f039681720ce0c`. `author_read_tests.py.diff` und `adaptation.json` halten die komplette Abweichung fest. Der ROOT und alle öffentlichen Inputpfade bleiben gleich. OUT und DEST zeigen ausschließlich in meinen Outputordner. Das eingefrorene v2-JSON und der öffentliche Baselinehashinput wurden bytegleich dort kopiert; die Einleitungsbeobachtung entstand dagegen unabhängig aus meiner Originallektüre und wurde nicht vom Autor übernommen.

Der kopierte Tester schreibt seine drei frisch erzeugten verify-BBox-Dateien und den eigenen Testoutput ausschließlich dorthin. Kein Original-Builder, Originaltester, Original-reproduce.sh oder Korrekturbuilder wurde direkt ausgeführt. CSV, Parser, aktive Annotationen, Sourcepins, Autorenoutputs, ursprüngliche Erstberichte und beide Pakete sind nach der abschließenden Hashkontrolle unverändert.

## Werkzeuge, Kommandos, Fehlversuche und Trennung

Genutzt wurden `functions.exec` mit `tools.exec_command`, `tools.apply_patch`, `tools.view_image`, Python-Standardbibliothek und vorhandenes Poppler. Nur Fortschrittsnachrichten an den Koordinator gingen über `collaboration.send_message`; keine Peerurteile wurden empfangen. Verfügbare direkte Namespaces: functions, clock, collaboration, mcp__cua_repl. Der tatsächliche angebotene Nested-Katalog mit633 Namen steht in `available-tools.json`. Angebote bedeuten keinen Zugriff. Die vor Anwendung gelesenen Skills sind PDF und Unslop. Versionen: Python3.14.7, pdftotext/pdftoppm26.08.0; alle drei Versionsaufrufe Exit0.

Keine eigenen Quellen-/Assertions-/Nachprüfläufe schlugen fehl. Die initiale Memory-Suche `rg -n '12axes|INVENTORY-002' /home/stevenh/.codex/memories/MEMORY.md` hatte Exit1 für keinen Treffer; das ist kein gescheiterter Quellencheck. Zwei frühe große kombinierte Toolausgaben waren abgeschnitten. Die Pflichtlektüre wurde danach in begrenzten Abschnitten vollständig wiederholt. Der eigene Pfadguard wurde vor der finalen Kontrolle um explizite Symlink-/aufgelöste Sperrpfadprüfungen verstärkt; sämtliche erlaubten Pfade bestanden, und die Vorher-/Nachherlisten sind exakt gleich. Die Autoren-Frühfehler sind als Autorenvorgeschichte gelesen und in `final-evidence.json` gebunden, nicht als eigene reproduzierte Fehlversuche ausgegeben.

Die anfänglichen read-only Shells vor Einrichtung des lokalen Subprozesslogs nutzten `pwd`, `rg --files`, `head`, `cat`, `wc -l` und kurze Python-JSON-Lesehilfen. Außer dem leeren Memorysuchlauf hatten sie Exit0. Sie lasen nur die benannten Skilldateien, freigegebenen Paket-/Originalberichtspfadnamen und eingefrorenen Inputs. Kurze Pythonaufrufe schrieben den eigenen vollständigen Startauftrag/Vorabplan und inspizierten konkrete JSONfelder, den echten Newlinecount sowie Q10-Originalcodeboxen. Die vollständigen stdin-Bodies und apply_patch-Inhalte stehen im tatsächlichen Tooltranskript; die ergebniswirksamen Checker/Adapter/Erzeuger sind zusätzlich als vollständige eigene Dateien erhalten. Es gab keine verdeckte Installation oder externe Netzwerkoperation.

Die folgenden tatsächlich ausgeführten argv/Exits sind in `commands.jsonl` mit CWD, UTC-Start/Ende und vollständigen stdout/stderr-Dateien gespeichert. Alle Shells liefen in `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Die gerade diese Tabelle schreibende eigene Berichtserzeugung und die abschließende Indexerzeugung werden im lokalen Log zusätzlich nach ihrem Abschluss erfasst.

| Protokoll | Tatsächlicher Befehl | Exit |
| --- | --- | --- |
| hashes-before | `python3 outputs/loop/inventory002-ab-v2-sources/audit_hashes.py before-hashes` | 0 |
| issue1 | `sed -n 1,100p reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/issue-2026-10-03.md` | 0 |
| mandate1 | `sed -n 1,90p reports/loop/packages/INVENTORY-002-AB/v2/files/docs/auftrag-life-93-2026-10-03.md` | 0 |
| issue2 | `sed -n 101,200p reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/issue-2026-10-03.md` | 0 |
| mandate2 | `sed -n 91,165p reports/loop/packages/INVENTORY-002-AB/v2/files/docs/auftrag-life-93-2026-10-03.md` | 0 |
| rules1 | `sed -n 1,35p reports/loop/packages/INVENTORY-002-AB/v2/files/docs/pruefregeln.md` | 0 |
| issue3 | `sed -n 201,278p reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/issue-2026-10-03.md` | 0 |
| requirements | `sed -n 1,53p reports/loop/packages/INVENTORY-002-AB/v2/files/docs/analyseanforderungen.md` | 0 |
| rules2 | `sed -n 36,69p reports/loop/packages/INVENTORY-002-AB/v2/files/docs/pruefregeln.md` | 0 |
| originals1 | `sed -n 1,95p reports/loop/reviews/INVENTORY-002-AB-sources.md` | 0 |
| originalr1 | `sed -n 1,80p reports/loop/reviews/INVENTORY-002-AB-repro.md` | 0 |
| originalr2 | `sed -n 81,159p reports/loop/reviews/INVENTORY-002-AB-repro.md` | 0 |
| originals2 | `sed -n 96,186p reports/loop/reviews/INVENTORY-002-AB-sources.md` | 0 |
| originalauthor1 | `sed -n 1,85p reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/authors/INVENTORY-002-AB.md` | 0 |
| correction1 | `sed -n 1,70p reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/authors/INVENTORY-002-AB-korrektur.md` | 0 |
| originalauthor2 | `sed -n 86,172p reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/authors/INVENTORY-002-AB.md` | 0 |
| correction2 | `sed -n 71,135p reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/authors/INVENTORY-002-AB-korrektur.md` | 0 |
| bounded-mandates | `cat reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/INVENTORY-002-AB-pruefauftrag.md reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/INVENTORY-002-AB-entscheidung.md reports/loop/packages/INVENTORY-002-AB/v2/files/reports/loop/INVENTORY-002-AB-v2-pruefauftrag.md` | 0 |
| qlayout | `pdftotext -f 9 -l 10 -layout outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab-v2-sources/q9-10.layout.txt` | 0 |
| qbbox | `pdftotext -bbox-layout outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab-v2-sources/questionnaire.bbox.html` | 0 |
| qrender | `pdftoppm -f 9 -l 10 -r 150 -png outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab-v2-sources/q` | 0 |
| author-test-read | `cat outputs/loop/inventory002-ab-correction/read_tests.py` | 0 |
| original-test-boundary | `sed -n 100,125p outputs/loop/inventory002-ab/read_tests.py` | 0 |
| v2-build-boundary | `rg -n intro2|originalextrakt|sha256|OUT=|DEST=|plan-before|prettier outputs/loop/inventory002-ab-correction/build_ab.py` | 0 |
| independent-tests | `python3 outputs/loop/inventory002-ab-v2-sources/independent_tests.py` | 0 |
| adapt-test | `python3 outputs/loop/inventory002-ab-v2-sources/adapt_tests.py` | 0 |
| author-test-copy | `python3 outputs/loop/inventory002-ab-v2-sources/author_read_tests.py` | 0 |
| plans-read | `cat outputs/loop/inventory002-ab/plan-before-work.json outputs/loop/inventory002-ab-correction/plan-before-work.json` | 0 |
| python-version | `python3 --version` | 0 |
| pdftotext-version | `pdftotext -v` | 0 |
| pdftoppm-version | `pdftoppm -v` | 0 |
| final-evidence | `python3 outputs/loop/inventory002-ab-v2-sources/final_evidence.py` | 0 |
| hashes-after | `python3 outputs/loop/inventory002-ab-v2-sources/audit_hashes.py after-hashes` | 0 |

Nachprüfbefehl für die eigenen semantischen/diffbezogenen Kriterien ist `python3 outputs/loop/inventory002-ab-v2-sources/independent_tests.py`. Er liest die eingefrorenen v1/v2-Dateien und die eigene frisch erzeugte BBox und schreibt nur eigene Outputs. Die Hashkontrolle ist `python3 outputs/loop/inventory002-ab-v2-sources/audit_hashes.py after-hashes`. Die kopierten Autorentests können ausschließlich mit `python3 outputs/loop/inventory002-ab-v2-sources/author_read_tests.py` an den umgeleiteten Zielen laufen. Diese Befehle wurden tatsächlich wie oben protokolliert ausgeführt.

Shared-FS ist eine reale Grenze: keine technische Informationssandbox verhindert Zugriff auf andere Reports oder Daten. Die Trennung war organisatorisch durch frischen begrenzten Startauftrag, freigegebene Originalerstberichte als Historie, gefrorene Fassung, öffentliche Inputpfade und Verzicht auf aktuelle Peer-/Juror-/Agent-/Loopurteile. Ich war weder Inventarautor noch ursprünglicher Reviewer. Es wurden keine weiteren Agents, keine andere Modellfamilie, kein Browser-/Webzugriff, keine Anmeldung, kein Commit/Push, kein Conda, keine Installation oder globale Schreiboperation genutzt.

Keine ESS-Rohdaten, Rohdatenhashs, `data/raw`, `data/local`, Personenkennungen, Antworten aus A/B, Partei-/Links-rechts-Werte oder Verteilungen, Secrets, Cookies oder Portal-Analysen wurden gelesen oder ausgegeben. Variablennamen und veröffentlichte Code-/Labelmetadaten sind öffentliche Dokumentation. Alle eigenen Writes betreffen ausschließlich diesen neuen Bericht und `outputs/loop/inventory002-ab-v2-sources/`.

## Vollständiger tatsächlicher Startauftrag

```text
Frischer unabhängiger Quellen-/Kontextnachprüfer INVENTORY-002-AB v2 Runde1, bisherunbeteiligt. ShellCWD /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. AutoritativeManifest reports/loop/packages/INVENTORY-002-AB/v2/manifest.json SHA2fe41dba331a3775c9a4a254f8136ded551f54c864cb9aea21b6c375863a4bd4,14Dateien/168SourceInputs. GefroreneAGENT/Auftrag/Issue/Prüfanforderungen, V2Prüfauftrag, vollständigerAutorKorrekturreport, v1Rückbindung und ursprünglicheErstberichte alsKorrekturhistorie selbstlesen. KEINE aktuellenNachprüferurteile/Agentlisten/Loopfindings/Jurorberichte/nachgelieferteVerteidigung. EigeneOriginallektüreDEQPDF/gedruckt9/10 inklSichtprüfungPDFSkill, vorallemB19–22EinleitungvollständigexaktohneAntwortkopf,37Tokens/BelegQCTX-behav-intro2/429.5BBox/extrakthashnachvollziehen;BBoxTokenPresencealleinkeineSemantik. OriginalB24kein08/B25gedruckter08Konflikt bleibt. Neueechte08EinfügungUNDgleichlange09→08Ersetzungtatsächlichprüfen/selbstGegenfälle;HistorieDuplikat01nichts rückdatieren. StrengerGanzdokumentdiff52Kategorien/Sonder/Missing/Karten/61Restpunkte+835übrigeBelege unverändert, vierContexts/nur1gemeinsamerBelegänderungundVersionsmetadata. Original10+89Kettevor/nachunverändert. Alle14+168PublicPfadScopeHashvor/nachprüfen. EigeneLesetests/Gegenfälle unter outputs/loop/inventory002-ab-v2-sources/; Autorenbuild/reproduce/Testniemalsdirektausführenfestepfade, nurkontrollierteKopienOwnPfadeDiffHashes. AktiveCSV/Parser/Quellen/Programme/Outputs/Paketeunverändert. KeinESSrawlocalAntwortenA/B/ParteiLRwerte/Verteilungen/angemeldetesPortalAnalysis/Secrets/globalWrites/Conda/Install/CommitPush/pnpmGesamtformat/weiterAgents. BerichtNUR reports/loop/reviews/INVENTORY-002-AB-v2-sources.md plusOwnOutputs. KI-AuditengbegrenzteNachprüfungkeineGesamtInventar-/Wissenschafts-/Polungs-/Neutralitätsfreigabe. JedesFindingAB2-SxxgenaueBehauptung/Problem/Originalfundstelle/Wirkung/begründeteSchwere/KorrekturNachprüfung/Vermutungsklar,keineFindingquote; alteIDs/Rundensameproblembeibehalten. TatsächlichenvollständigenStartauftragwortgetreu,Modelgpt-6.1-solultrageerbtinternunknown,verfügbare/genutzteTools/CommandsExits/Fehlversuche/SharedFSorganisatorischeTrennungdokumentieren. VollständigabschließenunveränderlichenReportSHA+Befundsenden.
```

Der Wortlaut steht unverändert zusätzlich in `startauftrag.txt`. Weitere sachliche Startaufträge oder zusätzliche Autorenverteidigungen gab es nicht. Die organisatorischen Fortschrittsnachrichten enthalten keine Peerbewertungen.

## Unveränderliche Übergabe

Dieser vollständige Erstbericht ist `reports/loop/reviews/INVENTORY-002-AB-v2-sources.md`. Sein Erzeuger verweigert ein Überschreiben. Nach der Übergabe wird er nicht verändert. `report-integrity.json` und `outputs-index.json` binden den endgültigen Bericht und die eigenen Belege; der Index kann seinen eigenen Hash nicht rekursiv enthalten.

Die eigenen Artefakte enthalten Startauftrag und Vorabkriterien, Hashaudits, Toolkatalog, Kommandos/Exits, Originaltext/BBox und Q9/10-Renderings, eigene Lesetests und Ganzdokumentdiff, vollständige Token-/Grenzwitnesses, tatsächliche In-memory-Gegenfälle, bytegleiche Testinputs, umgeleiteten Autorentester mit exakt dokumentierter Pfadabweichung, historische Kontrollbindung und diese Berichtserzeugung. AB-S01 und AB-S02/AB-R01 sind für dieses Manifest in Runde1 korrigiert nachgeprüft; die ursprünglichen Befunde und Reports bleiben erhalten. Die getrennte Reproprüfung und alle darüber hinausgehenden wissenschaftlichen Abnahmen werden von diesem Bericht nicht vorweggenommen.
