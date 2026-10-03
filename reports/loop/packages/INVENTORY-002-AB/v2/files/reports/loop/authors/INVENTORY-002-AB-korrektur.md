# INVENTORY-002-AB: Korrekturfassung v2, Runde 1

Stand 2026-10-03. Die neue Ergänzung ist `data/inventar-ab.v2.ergaenzung.entwurf.json`, SHA-256 `31a4fa49c0149f3aec5820fcb30fb85388a09dcd5470393b9f259cf9013fceb8`. Sie korrigiert AB-S01 und führt für AB-S02/AB-R01 zwei tatsächlich ausgeführte 08-Gegenproben. Die erste Ergänzung, ihre Programme, Outputs, Prüfpakete und beide Erstberichte bleiben unverändert. Dies ist Autorenarbeit nach den vom Koordinator angenommenen Findings. Die unabhängigen Rechecks sind `NICHT_GEPRÜFT`; keine wissenschaftliche, politische Neutralitäts-, Eignungs- oder Polungsabnahme wird behauptet.

Modell laut Koordinator `gpt-6.1-sol`, Denkaufwand `ultra`, geerbt. Interne Revision und nicht zugängliche Anbieterregeln sind unbekannt; diese Angaben konnten nicht unabhängig introspektiert werden. Dieselbe Autorenrolle wurde für diese eng begrenzte Korrektur fortgesetzt, kein frischer unabhängiger Reviewer.

## Tatsächlicher vollständiger Auftrag

```text
Bearbeite jetzt eng begrenzt AB-S01 und AB-S02/AB-R01 aus beiden vollständig abgeschlossenen Erstberichten (reports/loop/reviews/INVENTORY-002-AB-sources.md und INVENTORY-002-AB-repro.md) in NEUER FASSUNG. CWD bleibt /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Koordinator nimmt beide Findings an: AB-S01 MITTEL vier B19–22 Einleitungen enthalten Tabellenkopf (OriginalQ PDF/gedruckt9, y0=429.688381), AB-S02/AB-R01 NIEDRIG ursprünglicher angeblicher08Fall war angehängtesDuplikat01. Runde1. ZUERST eigener Vorabplan/Kriterien. Schreibe ausschließlich neue data/inventar-ab.v2.ergaenzung.entwurf.json, reports/loop/authors/INVENTORY-002-AB-korrektur.md sowie eigene outputs/loop/inventory002-ab-correction/ Dateien. AlteJSON/Builder/Programme/Outputs/Pakete/Erstberichte/CSV/Parser und sämtliche laufendenMETHODS-002 Inputs UNVERÄNDERT! Kopiere Builder undTests in ownOutputs, dokumentiere Hashdiff, ändere nur neueOutputs/JSONziel und introBBox saubereUnterkante (z.B.429.5 nachselbstOriginalsicht). Original9/10 selbstlesen; vierkontexte inklTokens/Hashes/Referenzen sauber ohneAntwortkopf, Kategorien bleiben separat. WahreHistorie nichtumschreiben: OriginaltestDuplikat01; neueTests genuine08EinfügungUND gleichlange09→08Ersetzung expliziteCodefolgen/rejectedtrue. NegativeTests ohneeigenePosthoctoleranzlockerung. Reproduziere neuenBuilder bytegleich und tatsächliche Feldchecks, prüfe genauDiffv1/v2 nurvierIntroReferenzen/Belege/Hashes plus transparenteVersionsmetadata;836 übrigeBelegbefunde/61Rest/52Kategorien nichtstillverändern. Originalv1Manifest10+89 vor/nach prüfen, Quellen originalPublics only. KeinESS/Raw/Local/AntwortenA/B/PartyLRVerteilungen/Credentials/PortalAnalysis/Conda/globalWrites/Installationen/CommitPush. Eigenen vollständigen Auftrag/Modell/Tools/tatsächlicheExits/Fehlversuche aufzeichnen. KeinGesamtformat oderpnpmcheck; unabhängigeRechecks folgen. Keine neueFinaleEignung/Polung/Neutralitäts-/wissenschaftlicheAbnahme. Vollständigliefern mitSHA und Artefaktindex; ursprünglicheFassungenbewahren.
```

Der Vorabplan `outputs/loop/inventory002-ab-correction/plan-before-work.json` wurde vor der Arbeit um `2026-10-03T05:48:56.360543+00:00` geschrieben. Seine Kriterien waren vollständige Erstberichtslektüre, eigene Originallesung der Seiten 9/10, vier sauber getrennte Einleitungen, unveränderte Kategorien und Restpunkte, echte 08-Einfügung und gleichlange 09→08-Ersetzung ohne gelockerte Gleichheitsprüfungen, byteidentische Reproduktion, ein strenger Ganzdokument-Diff sowie Vorher-/Nachherintegrität der ursprünglichen 10+89-Kette. Die vorab formulierten Kriterien blieben bestehen.

## Gelesene Erstberichte und eigene Quellenlektüre

Die vollständig abgeschlossenen Erstberichte wurden auf ausdrücklichen neuen Koordinatorauftrag vollständig gelesen: `reports/loop/reviews/INVENTORY-002-AB-sources.md` (186 Zeilen, SHA-256 `76bd287adea616f6964e2f86c24ecc63d8f24616f8908dd4abb72fae848671a4`) und `reports/loop/reviews/INVENTORY-002-AB-repro.md` (159 Zeilen, SHA-256 `74b5a6c5cf941741f411285dad1094f7de74a5cb1fe6f2021f564b5e12d38f51`). Eine große kombinierte Toolausgabe war abgeschnitten; danach wurden beide Berichte vollständig in begrenzten Zeilenabschnitten gelesen. Andere aktuelle Peer-/Jurorberichte, Loopfindings oder Agentregister wurden nicht geöffnet. Die erste Autorenfassung hatte diese beiden Berichte noch nicht gelesen; v2 dokumentiert den nun autorisierten Zugriff ausdrücklich.

Die ursprünglichen Repository-Regeln und Projekt-/LIFE-93-Dokumente waren bereits in dieser Autorensitzung gelesen. Der unveränderte v1-Pin wurde jetzt zusätzlich gegen sein Manifest geprüft. Es wurden keine Antworten, Datenkandidaten, Parteiverteilungen oder Links-rechts-Werte gelesen.

| Quelle | Gepinnter SHA-256 | Lokale öffentliche Quelle |
| --- | --- | --- |
| ESS11-DE-QUESTIONNAIRE | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` | ESS11_questionnaires_DE.pdf |
| ESS11-DE-SHOWCARDS | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` | ESS11_showcards_DE.pdf |
| ESS11-CODEBOOK | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` | ESS11_appendix_a7_e04_1.pdf |
| ESS-CONDITIONS-OF-USE | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` | ess-disclaimer.html |

Die offiziellen Pins liegen unter `outputs/loop/inventory/`. Der deutsche [ESS11-Fragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), das [Listenheft](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf), [Codebook 4.1](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf) und die [Conditions of use](https://www.europeansocialsurvey.org/contact/disclaimer) wurden nicht verändert. Dokumentationslizenz, Quellenzugriffe, Attribution und die Grenze 4.1 gegenüber nicht geprüften Antwortdaten 4.2 sind in v2 exakt aus v1 erhalten. Keine neue Netzabfrage oder rechtliche Veröffentlichungsfreigabe. Die frischen Volltext-/BBox-Extrakte liegen ausschließlich in den eigenen ignorierten Outputs.

Für diese Korrektur wurde die Fragebogenquelle frisch extrahiert. PDF-/gedruckte Seiten 9 und 10 wurden neu gerendert und beide Bilder tatsächlich mit `view_image` gelesen. Auf Seite 9 endet die Einleitung vor dem separaten Antworttabellenkopf. Das letzte Einleitungswort reicht bis y=429.409532; das erste Kopfwort beginnt bei y=429.688381. Die neue Unterkante 429,5 enthält jedes vollständige Einleitungswort und schließt alle vier angehängten Kopfanfänge aus. Die unabhängig vom Builder geschriebene Beobachtung `read_original_boundary.py` nutzt vollständige Wortboxeinschließung, verlangt den selbst gelesenen genauen Text und bewahrt konkrete Tokens in `original-boundary-observation.json`.

Auf Seite 10 wurden B24 samt Kategorien und der B25-Filter visuell gelesen. B24 druckt 01–07 und 09, keine 08. Der Originalfilter B25 druckt weiterhin 08. Der Konflikt und die getrennten Codebook-Kategorien bleiben unverändert.

## AB-S01: vier Einleitungen korrigiert

Betroffen sind ausschließlich B19, B20, B21 und B22 sowie deren gemeinsamer Beleg `QCTX-behav-intro2`, Quelle ESS11-DE-QUESTIONNAIRE, PDF-/gedruckte Seite 9. Die Region `(x0=0,x1=595,y0=379,y1=430)` wurde auf `y1=429.5` verkürzt. Die vier Kopfanfänge `Ja Nein (Antwort (Weiß` gehören in den separat belegten Antwortkopf. Sie stehen nicht mehr in der Einleitung.

Die genaue Einleitung in der neuen Fassung lautet:

```text
Denken Sie weiterhin an verschiedene Möglichkeiten, wie man versuchen kann, etwas in Deutschland zu
verbessern oder zu verhindern, dass sich etwas verschlechtert. Haben Sie im Verlauf der letzten 12 Monate
irgendetwas davon unternommen?
Haben Sie... BITTE VORLESEN...
```

Der Originalquellenhash bleibt `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`. Der Extrakthash ändert sich von `026a2c6be4f6e6b2d7cead4c4a870165ebf4f2f508bd53d19c8c84c5b52d3aac` zu `de17ced533eddefe84f4ee7c1ee28f52def0afcece5729f932eafbf88986785d`; die Auswahl enthält jetzt 37 statt 41 Tokens. Die vier Kontextfelder behalten dieselbe Beleg-ID, die innerhalb der eigenständigen v2-Datei auf den korrigierten Beleg zeigt. Wortlaut, Kategorien, Missinglabels, Filter und Weiterleitungen wurden dabei nicht verändert. Jeder der vier Kontexte wird gegen den genauen gelesenen Text und seine Referenz geprüft. Für jeden Kontext wurde zusätzlich eine In-memory-Gegenprobe mit angehängtem Kopf durchgeführt und abgewiesen.

## AB-S02/AB-R01: wahre Testhistorie und echte 08-Kontrollen

Die damalige Kontrolle war falsch benannt. Im unveränderten Originaltester, SHA-256 `a7f6f09559aca3414d5d940964da98535f64c6b2f02ca14e8a04d07d41c3eb16`, hing die Operation eine Kopie der ersten B24-Kategorie an. Die tatsächliche Codefolge war `01,02,03,04,05,06,07,09,01`. Der Originallauf bewies die Ablehnung eines zusätzlichen Duplikats 01 und führte keine echte 08-Mutation aus. Diese Aussage korrigiert die damalige Berichtsbehauptung; Originalprogramm und Originaloutput werden nicht umgeschrieben.

Die neue Kopie führt die historische Operation ehrlich benannt erneut aus. Sie führt außerdem eine echte 08-Einfügung mit ausdrücklich gesetztem Code `08` und Label `dieBasis` in einer In-memory-Kopie aus. Die zweite neue Kontrolle ersetzt bei gleicher Kategorienzahl ausschließlich den bisherigen Code `09` durch `08` und erhält alle Labels. Beide werden durch die unveränderte erwartete Originalfolge `01,02,03,04,05,06,07,09` abgewiesen. Kein künstlicher 08-Eintrag wird in der Ergänzung gespeichert.

| Tatsächlich ausgeführte Kontrolle | Mutierte Codefolge / Gegenstand | Abgewiesen |
| --- | --- | --- |
| swapped B2 captions | Kontext-/Labelmutation | `true` |
| reversed EU endpoints | Kontext-/Labelmutation | `true` |
| appended duplicate B24 code01; historical operation rerun | 01→02→03→04→05→06→07→09→01 | `true` |
| genuine B24 code08 insertion | 01→02→03→04→05→06→07→08→09 | `true` |
| same-length B24 code09-to08 replacement | 01→02→03→04→05→06→07→08 | `true` |
| answer-header fragment appended to B19 introduction | Kontext-/Labelmutation | `true` |
| answer-header fragment appended to B20 introduction | Kontext-/Labelmutation | `true` |
| answer-header fragment appended to B21 introduction | Kontext-/Labelmutation | `true` |
| answer-header fragment appended to B22 introduction | Kontext-/Labelmutation | `true` |

Die exakten Vorher-/Nachherfolgen, Kategorienanzahlen, expliziter 08-Code, Einfügelabel und erhaltene Ersetzungslabels stehen in `read-tests.json/negativeControls`. Der Original-Gleichheitstest für Codes und Labels blieb unverändert. Es wurden keine Toleranzen gelockert und keine erwarteten Originalkategorien um 08 ergänzt.

## Enger Diff und tatsächlich ausgeführte Checks

`verify_diff.py` ist ein eigener strenger Ganzdokumentvergleich. Er verlangt genau vier geänderte Fragezeilen und genau einen geänderten gemeinsamen Beleg. Danach normalisiert er ausschließlich diese bekannten Änderungen sowie die ausdrücklich dokumentierte Versions-/Zugriffsmetadata und verlangt Gleichheit des gesamten restlichen JSON.

| Gegenstand | Tatsächliches Ergebnis | Grenze |
| --- | --- | --- |
| Original-v1-Manifest und seine 10 Dateien + 89 SourceInputs vor Arbeit | BESTANDEN, Exit 0 | Public-Scope-/Pfad-, Byte- und Hashprüfung, keine semantische Abnahme |
| Eigene Originalbeobachtung Q9/Q10 und frische BBox-Auszüge | BESTANDEN, Exit 0 | Eigene Quellenlektüre; zwei Seiten visuell gelesen |
| Kopierter Builder | BESTANDEN, Exit 0; 52 Identitäten, 836 Belege, 61 Restpunkte | Nur neue v2-Datei und eigene Outputs |
| Strenger v1/v2-Vergleich | BESTANDEN, Exit 0; vier Einleitungstexte, ein gemeinsamer Beleg | 835 übrige Belege exakt gleich; Gesamtzahl weiterhin 836 |
| Alle Kategorien-, Missing-, Datenmissing-, Codebook- und Kartenstrukturen | Alle 52 Strukturen exakt gleich | Keine neue Kodierungs-/Versionsabnahme |
| Alle offenen Punkte | Alle 61 vollständig identisch | Kein Restpunkt geschlossen |
| Kopierte und ergänzte tatsächliche Quellen-/Feldchecks | BESTANDEN, Exit 0; 7547 begrenzte Checkereignisse, 0 Fehler | Eigenchecks, Zähler kein Güte- oder Vollständigkeitsmaß |
| Echte 08-Einfügung und gleichlange 09→08-Ersetzung | Beide `rejected: true`; tatsächlich ausgeführt | Nur In-memory-Mutationen gegen Originalmetadaten |
| Vier Einleitungs-Kopfgegenproben | Alle `rejected: true`; tatsächlich ausgeführt | Eigene Kontextkontrollen, kein unabhängiger Recheck |
| Zweiter Builderlauf | BESTANDEN, Exit 0; byteidentisch `31a4fa49c0149f3aec5820fcb30fb85388a09dcd5470393b9f259cf9013fceb8` | Reproduktion desselben Autorenartefakts |
| Original-v1-Manifest und 10+89-Kette nach Korrektur | BESTANDEN, Exit 0 | Gleiches Manifest `5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856`, alle ursprünglichen Bytes erhalten |
| `pnpm check`, Gesamtlauf-/Gesamtformatierung | NICHT_AUSGEFÜHRT gemäß engem Korrekturauftrag | Nur der kopierte Builder ruft Prettier für sein neues JSON-Ziel auf; dieses ist laut tatsächlicher File-info-Ausgabe ignored=true. Kein Formatvalidierungsnachweis |
| Unabhängige Rechecks / empirische ESS-Prüfung / Eignung, Polung, Neutralitäts- oder Phase-1-Abnahme | NICHT_GEPRÜFT / nicht durchgeführt | Der Koordinator lässt unabhängige Rechecks folgen |

Als Versionsmetadata kommt `korrektur` hinzu: Originalhash, Version/Runde, tatsächlicher neuer Auftrag, gelesene Erstberichtshashes, Historienkorrektur und offene Abnahmen. `zugriffsgrenzen.peerOrJurorReportsRead` ändert sich wahrheitsgemäß von false auf true, weil genau die beiden nun autorisierten abgeschlossenen Erstberichte gelesen wurden. Der ursprüngliche Autorstart, Quellenzugriffe, Lizenz und alle übrigen ursprünglichen Metadata bleiben gleich. `v1-v2-diff-check.json` nennt die exakt erlaubten Änderungen und je Identität den Hash ihrer unveränderten Kategorie-/Missing-/Kartenstruktur.

## Skriptkopien, Befehle und eigene Fehlversuche

Builder und Tester wurden zuerst byteidentisch in die eigenen Korrekturausgaben kopiert. `copy-before-adaptation.json` enthält die ursprünglichen und kopierten Hashes. Die endgültigen Änderungen sind als vollständige Unified-Diffs `build_ab.py.diff` und `read_tests.py.diff` festgehalten. Die zwei endgültigen Skripthashes stehen in `adaptation.json`:

- Builder `74e481f651b23fbcd5020609db2dac96a73fda69ec659ee4f7fcf231c30a824b`.
- Tester `c99e61af8f0d304086e9a9d1c33497d3a7bc53e1e0f71a173a4052eb9e851bcb`.

Builderänderungen: eigene Output-/JSONpfade, Lesen des byteidentisch kopierten ursprünglichen Autorplans, neue Unterkante und transparente v2-Metadata. Testeränderungen: eigene Ziele, genaue Einleitungschecks und ehrlich benannte beziehungsweise echte Mutationen. Die ursprünglichen Programme wurden nicht ausgeführt oder verändert.

Der erste eigene Adapter schrieb versehentlich ein wörtliches Backslash-n hinter sein JSON-Protokoll. Die erste Inspektion fing den `JSONDecodeError` ab und druckte ihn; der Außenaufruf hatte deshalb Exit 0, was keine bestandene JSON-Validierung war. Ein erster gezielter Escape-Fix scheiterte an einem AssertionError (Außenaufruf Exit 1). In derselben mehrteiligen Shell lief mangels `set -e` der unverbesserte Adapter noch einmal mit Exit 0; die anschließende JSON-Lektüre scheiterte wieder. Diese missverständliche Außen-/Unterprozessfolge bleibt in `early-failure-record.json` erhalten. Der fehlerhafte Originaloutput und die damalige eigene Adapterfassung liegen unter `adaptation-first-invalid.json.txt` und `adapt_scripts-first.py`. Die endgültige Korrektur beschränkt sich auf `chr(10)` für die Protokollnewline. Danach wurde `adaptation.json` erfolgreich geparst. Die kopierten Builder-/Testerbytes und ihre Abnahmebedingungen änderten sich durch diesen Protokollfix nicht. Die echten Quellen-/Feld- und Diffchecks hatten keine Fehlschläge.

Die protokollierten Subprozessbefehle mit tatsächlichen Exitwerten sind:

| Protokollname | Tatsächlicher Befehl | Exit |
| --- | --- | --- |
| v1-before | `python3 outputs/loop/inventory002-ab-correction/verify_v1.py before-hashes.json` | 0 |
| q-bbox | `pdftotext -bbox-layout outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab-correction/questionnaire.bbox.html` | 0 |
| q-render | `pdftoppm -f 9 -l 10 -r 130 -png outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab-correction/q` | 0 |
| original-observation | `python3 outputs/loop/inventory002-ab-correction/read_original_boundary.py` | 0 |
| adapt-scripts | `python3 outputs/loop/inventory002-ab-correction/adapt_scripts.py` | 0 |
| s-bbox | `pdftotext -bbox-layout outputs/loop/inventory/ESS11_showcards_DE.pdf outputs/loop/inventory002-ab-correction/showcards.bbox.html` | 0 |
| c-bbox | `pdftotext -bbox-layout outputs/loop/inventory/ESS11_appendix_a7_e04_1.pdf outputs/loop/inventory002-ab-correction/codebook.bbox.html` | 0 |
| builder-first | `python3 outputs/loop/inventory002-ab-correction/build_ab.py` | 0 |
| adapt-scripts-corrected | `python3 outputs/loop/inventory002-ab-correction/adapt_scripts.py` | 0 |
| strict-diff-first | `python3 outputs/loop/inventory002-ab-correction/verify_diff.py` | 0 |
| read-tests-first | `python3 outputs/loop/inventory002-ab-correction/read_tests.py` | 0 |
| adapt-scripts-final | `python3 outputs/loop/inventory002-ab-correction/adapt_scripts.py` | 0 |
| builder-second | `python3 outputs/loop/inventory002-ab-correction/build_ab.py` | 0 |
| byte-reproduction | `python3 outputs/loop/inventory002-ab-correction/check_reproduction.py` | 0 |
| v1-after | `python3 outputs/loop/inventory002-ab-correction/verify_v1.py after-hashes.json` | 0 |
| prettier-file-info | `pnpm exec prettier --file-info data/inventar-ab.v2.ergaenzung.entwurf.json` | 0 |

`command-events.jsonl` hält UTC-Start/Ende, argv, CWD und eigene Stdout-/Stderrdateien. Die Reportlektüre erfolgte mit `cat` und danach vollständig `sed -n '1,95p'`, `sed -n '96,186p'` für sources sowie `sed -n '1,80p'`, `sed -n '81,159p'` für repro; alle Leseaufrufe Exit 0. Flüchtige Inline-Pythonaufrufe schrieben den Vorabplan, machten unveränderte Skriptkopien, inspizierten Originalboxen, retteten und korrigierten das eigene Adapterprotokoll und erfassten Versionen. Der vollständige jeweilige stdin-Code liegt im Tooltranskript; die wirksamen reproduzierbaren Erzeuger und Checker sind vollständig als eigene Dateien vorhanden. Der Erzeuger dieses Berichts und der abschließende Artefaktindex werden ebenfalls im eigenen Verzeichnis erhalten. Eine anschließende tatsächliche `pnpm exec prettier --file-info data/inventar-ab.v2.ergaenzung.entwurf.json`-Abfrage hatte Exit 0 und meldete `ignored: true, inferredParser: null`. Der im kopierten Builder vorhandene gezielte Prettieraufruf hatte ebenfalls Exit 0, lieferte damit aber keine Formatvalidierung. Es fand weiterhin kein Gesamtlauf statt. Ein erster eigener Handoffentwurf enthielt für diese File-info fälschlich eine vorweg angenommene false/json-Angabe; er ist als `handoff-checks-first-wrong-file-info.json` erhalten und wird ausdrücklich verworfen. Die tatsächlich beobachtete ignored/null-Angabe wird in der finalen Handoffdatei aus dem frischen Kommandoprotokoll gelesen. Der vor dieser Klarstellung geschriebene, noch nicht übergebene eigene Berichtsentwurf bleibt unter `report-before-format-observation.md` erhalten. Quellen-/Kategorien-/Diffchecks und Artefakthash änderten sich dadurch nicht.

Angeboten waren functions, clock, collaboration und mcp__cua_repl sowie die Nested Tools in `tool-protocol.json`. Genutzt wurden `functions.exec` mit `tools.exec_command`, `tools.write_stdin` und `tools.view_image`, Python-Standardbibliothek, bestehender Poppler und der auf das neue JSON-Ziel begrenzte bestehende Prettieraufruf des kopierten Builders. Versionsabfragen von Python/Poppler/Node/pnpm hatten Exit 0; Werte stehen in `tool-versions.json`. Die in dieser Sitzung bereits gelesenen Skills `pdf` und `unslop` wurden weiter angewendet. Kein Browser-/Webzugriff, keine Installation oder Conda, keine weitere Modellfamilie oder weitere Agents, kein Commit/Push.

## Reproduktion, erhaltene Fassungen und Übergabe

Die neue autorseitige Reproduktion ist vollständig unter `outputs/loop/inventory002-ab-correction/reproduce.sh` angegeben. Sie regeneriert nur die neue JSON-Datei und eigene Korrekturausgaben. Das Shellskript selbst wurde nicht als Ganzes ausgeführt; seine Extraktions-, Builder-, Beobachtungs-, Test- und Diffschritte wurden mit den oben protokollierten Einzelbefehlen tatsächlich ausgeführt. Ein zweiter Builderlauf bestätigt die identische neue Bytefassung. Wegen seiner festen Ziele müssen unabhängige Reviewer vor eigenem Nachbau ihre Kopien auf ihre eigenen Output-/JSONziele umleiten.

Das originale v1-Manifest `5af3f5c77ffa84ecbba15dc2c3f541064c1530bda5297928e8a5d5c7ae1d9856` und alle 10+89 Einträge stimmen vor und nach der Korrektur. Beide Originalerstberichte haben ebenfalls dieselben Vorher-/Nachherhashes. Aktive CSV, Provenienz und Parser sind Teil dieser unveränderten Kette. Alle Writes blieben bei der neuen v2-Ergänzung, diesem neuen Autorenbericht und `outputs/loop/inventory002-ab-correction/`; sämtliche laufenden METHODS-002-Inputs blieben unberührt. Keine ESS-Rohdaten, `data/raw`, `data/local`, Personenkennungen, Antwortdaten aus A/B, Partei-/LR-Werte oder Verteilungen, Credentials, Cookies oder Portal-Analysis wurden geöffnet, gehasht oder ausgegeben. Public-Codebook-Kategorien sind Dokumentationsmetadaten.

Die gemeinsame Dateisystemoberfläche bietet keine technische Informationssandbox. Die Zugriffstrennung wurde durch den engen Auftrag, die zwei ausdrücklich freigegebenen Erstberichte, feste öffentliche Quellpins und den Vorher-/Nachhervergleich eingehalten. Keine unabhängige Eigenabnahme wird behauptet.

Das Übergabepaket umfasst die neue JSON-Datei, diesen Bericht und alle eigenen Korrekturausgaben: Vorabplan/Auftrag, beide Hashaudits, unveränderte Baselinekopien, Originalbeobachtung samt Bildern, angepasste Programme und genaue Diffs, Fehlversuchsbelege, Quellenlesetests, strengen Diff, Byte-Reproduktion, Commands/Tools und `artifacts-index.json`. Der Index verzeichnet Dateilängen und SHA-256 aller gelieferten Dateien; er enthält seinen eigenen Hash wegen der Rekursion nicht. Die erste Fassung wird nicht ersetzt. 61 Restpunkte bleiben offen, ebenso die unabhängigen Rechecks und alle wissenschaftlichen Folgeabnahmen.
