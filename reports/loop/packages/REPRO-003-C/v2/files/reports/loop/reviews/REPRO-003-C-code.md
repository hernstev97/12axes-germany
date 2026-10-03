# REPRO-003-C: unabhängige CODE-Erstprüfung

Der lokale technische Nachbau des gefrorenen Pakets ist **BESTANDEN**. Ein eigener Fünfdateien-Minimalclone lud die drei festgelegten PDFs tatsächlich neu herunter und erzeugte exakt die historische Annotation. Ein zweiter echter Downloadlauf mit zusätzlicher Python-Auditbeobachtung bestätigte das Ergebnis. Ich habe kein belegtes Code-Finding gefunden. Diese Entscheidung betrifft den ausführbaren historischen Nachbau und seine ausdrücklich begrenzten Pfad-/Pin-/Provenienzaussagen. Sie ist keine semantische C-v2-Korrekturnachprüfung, wissenschaftliche Abnahme oder Veröffentlichungserlaubnis.

## Prüfbindung und Unabhängigkeit

Prüfpaket `reports/loop/packages/REPRO-003-C/v1/manifest.json`, SHA-256 `5cb5e10f09f32fa52a6929a33a92f56b384fe4a6af34fa583acb0e8c5feb11d3`, Code-Commitangabe `1fa2251bb7dc57d36ee9169cba7af6918d75c295`. Der Hash bindet die Fassung; er ersetzt die Prüfung nicht. Alle 16 gefrorenen Dateien und 31 `sourceInputs` wurden vor und nach der Prüfung gegen Pfadgrenzen, Symlinks, Dateityp, Bytegröße und SHA-256 geprüft und blieben unverändert. Die genaue Bindung steht in `outputs/loop/repro003-c-code/hashes-before.json` und `hashes-after.json`.

Ich war ein frisch zugewiesener CODE-Erstprüfer und kein Autor dieses Pakets. Ich las die gefrorenen AGENTS, LIFE-93, den Dauerauftrag, Prüfregeln, Analyseplan, ergänzende Analyseanforderungen, Lizenzen, Prüfauftrag, Nachbau-Dokumentation und den manifestgebundenen Autorenbericht. Der Vorabplan und die angebotenen Autorenbelege wurden geprüft. Mein Codevergleich bestätigte den vollständigen Autorendiff: nur die ausführbaren Root-/Outputpfade, die bewusst historischen Quellenpfadstrings, Pflichtargumente und die Verweigerung vorhandener Builderziele unterscheiden sich. Der Geometriehelfer ist bytegleich zum manifestgebundenen historischen Helfer.

Keine anderen aktuellen Reviewer-/Jurorberichte, Loopfindings, Agentlisten oder zusätzliche Autorenverteidigung wurden gelesen. Ein anfängliches `git status --short` zeigte Namen fremder geänderter Dateien, darunter einen anderen Reviewerbericht; es zeigte keine Inhalte oder Urteile. Diese Dateinamenexposition lege ich offen. `docs/project.md` wurde zusätzlich als allgemeine Repositoryanweisung gelesen, ohne den dort verlinkten Berichten zu folgen. Die angebotene `unslop`-Skillanweisung wurde vom in der Umgebung angegebenen Hauptcheckoutpfad gelesen. Von dort wurde kein Projektcode ausgeführt oder kopiert.

Alle eigenen Projektartefakte liegen im zugewiesenen Worktree auf `research/life-93-night-20261003`, eigene Skripte, PDFs, Testfälle und Logs ausschließlich unter `outputs/loop/repro003-c-code/`. Ich startete ausschließlich unveränderte eigene Kopien der drei gefrorenen Python-Dateien. Gemeinsamer Originalcode, Originalausgabe und Autoren-Minimalclone wurden nicht gestartet. Es gab keine weiteren Agents und keine Änderungen an gemeinsamen Forschungsartefakten. Die Trennung ist organisatorisch auf einem gemeinsamen Dateisystem, keine OS-Sandbox.

Modellangabe der Zuweisung: `gpt-6.1-sol`, Reasoning `ultra inherited`. Interne Revision und Anbietervorgaben sind unbekannt. Gleiche Codex-Familie, KI-Audit; kein akademisches Peer Review und keine Gültigkeitsgarantie.

## Eigener vollständiger Nachbau

Der frische Ordner `outputs/loop/repro003-c-code/minimal-clone/` enthielt vor dem Lauf genau:

```text
pipeline/reproduce_c_annotation.py
pipeline/annotations/c_builder_v2.py
pipeline/annotations/source_geometry.py
data/inventar.entwurf.csv
data/inventar.provenienz.json
```

Er enthielt keine PDFs, Annotationen, Autorenbuilder oder historischen Caches. `preflight-run1.json` hält vor dem Start ROOT, OUT, CACHE, TARGET, Sidecar, Builderlog und eigenes Reviewlog vollständig fest. Jeder Zielpfad lag unter dem eigenen Clone; die Ausgabe existierte vorher nicht. Die eigenen Case-Preflights dokumentieren dieselben Pfadklassen vor jedem weiteren Start.

Wortgetreuer CLI-Befehl, CWD der eigene Minimalclone:

```sh
python3 pipeline/reproduce_c_annotation.py --output-dir outputs/public-reproduction/code-run1
```

Tatsächlicher Lauf 2026-10-03, 08:19:59.355035–08:20:01.686845 UTC, Exit 0. Drei HTTP-200-Downloads, ohne beobachteten Redirect. Alle heruntergeladenen Originalbytes sind im eigenen Laufverzeichnis erhalten und stimmen derzeit weiterhin mit ihren Pins überein:

| Originaldatei und feste Startadresse | SHA-256 |
| --- | --- |
| [ESS11_questionnaires_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf) | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| [ESS11_showcards_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf) | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| [ESS11_appendix_a7_e04_1.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf) | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |

Die drei Popplerextraktionen endeten mit Exit 0. Laufumgebung: Python 3.14.7, Poppler `pdftotext` 26.08.0, Versionsabfrage Exit 0. Die komplette Annotation ist bytegleich zur eingefrorenen historischen Zielannotation, SHA-256 `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e`; 43 Identitäten, 1526 Evidenzobjekte. Diese Größen stammen aus dem tatsächlichen eigenen Outputvergleich in `verification-summary.json`, keine neue fachliche Entscheidung.

Ein zweiter tatsächlicher Downloadlauf in `cases/audited-real-download/clone/` erzeugte denselben Hash. Für ihn wurde die unveränderte eigene Wrapperkopie in einem frischen Python-Prozess geladen und `main()` mit den dokumentierten Arguments und eigenem Clone-CWD aufgerufen. Der Python-Audithook beobachtete Öffnungsversuche, URL-Requests und Subprozess-Arguments, ohne Authdaten oder Rohinhalte zu protokollieren. In diesem Fall wurden Transport und Poppler nicht ersetzt; die allgemeine Controller-Kennung `in-process-injected` bezeichnet die Inprozess-Testanordnung einschließlich des Audit-Hooks.

## Codebefund und Laufprovenienz

Der Wrapper bindet exakt zwei öffentliche Eingaben und die drei PDF-Pins, `pipeline/reproduce_c_annotation.py:15–23`. Er kontrolliert die öffentlichen Eingaben vor Zielanlage und nochmals nach Annotationvergleich, Zeilen 59–65 und 112–114. Alle drei Downloads müssen ihre Pins bestehen, Zeilen 80–96; der Builder prüft dieselben PDF-Pins nochmals vor Extraktion, `pipeline/annotations/c_builder_v2.py:100–113`. Der endgültige Annotationhash wird gegen den historischen Zielhash geprüft, Wrapper Zeilen 108–111. Kein Pin wird bei einer Änderung übernommen.

Ausgabeargumente müssen relative neue Kinder unter `outputs/public-reproduction` sein, ohne `..`; erkannte Symlinks und vorhandene Ziele werden abgewiesen, Wrapper Zeilen 30–50. Die Zielanlage nutzt `exist_ok=False`, Zeile 65. Der Wrapper setzt OWN/CACHE/TARGET und Builder-Arguments ausschließlich auf den eigenen Zielbaum, Zeilen 103–106. Der Builder löst Ausgabepfade auf, kontrolliert OWN-/Rootgrenzen und verweigert vorhandene Ausgabe- oder Arbeitsverzeichnisse, Builder Zeilen 328–335. Seine einzige Extraktionsunterprozessform ist eine Argumentliste für `pdftotext -bbox`, ohne Shell, Zeilen 109–112. Quelle und BBoxziel lagen in beiden realen Nachbauten unter dem jeweiligen eigenen Clone.

Die Pfade in `annotation.json.quellen[*].file` sind historische Metadatenstrings, Builder Zeile 322. Sie werden als Strings serialisiert und nicht als ausführbare Eingaben verwendet. Der direkte reale Fünfdateienlauf gelang ohne diese Legacycaches. Bytegleichheit sowie der eigene Metadatenvergleich bestätigten unverändert: Autor-/Korrekturrollen, ursprüngliche Startzeit, Autorenstatus, Peer-/Loopflags, ursprüngliche Zugriffserklärungen, Quellenpfade und Lizenzmetadaten. Zum Beispiel blieb `authorStartedUtc` `2026-10-03T05:50:57Z`, während der aktuelle Sidecar `startedAtUtc` `2026-10-03T08:19:59.422031+00:00` nennt. Die historischen Peer-/Loopflags werden deshalb nicht als heutige Reviewer-Selbstauskunft benutzt.

`reproduction.json` hält die tatsächlichen eigenen Downloadpfade, Start-/Endzeiten, Start-/End-URLs, HTTP-Status, Bytes/Pins, Annotationhash und Runtime getrennt fest. `scienceAcceptance` blieb `NICHT_GEPRÜFT`. Nach Download-/Extraktionsfehlern enthalten die tatsächlich angelegten Sidecars `NICHT_BESTANDEN` und einen konkreten Error; frühe Pfad-/Inputfehler erzeugten kein neues Ziel. Die Dokumentation erklärt diese Unterscheidung ausdrücklich, `docs/reproduktion-c-quellen.md`, Absätze zu historischen Metadaten und Fehlerprotokoll.

Im realen auditierten Lauf wurden keine Projektöffnungsversuche unter `data/raw/` oder `data/local/` und keine Öffnungsversuche der beobachteten Authdateiklassen festgestellt. Beobachtete Python-Schreibpfade lagen ausschließlich unter meinem eigenen Basisverzeichnis. Die drei Netzwerkrequests waren die festgelegten öffentlichen PDF-GETs. Python machte auch erfolglose Leseversuche für noch nicht vorhandene eigene `.pyc`-Caches; keine Bytecode-Schreibevents entstanden. Vollständige Ereignisse und Prozessarguments liegen in `cases/audited-real-download/events.jsonl`, die Zusammenfassung in `read-write-audit-summary.json`.

Diese Ereignisse sind keine vollständige Systemaufrufüberwachung: Python-Importe vor dem Hook und native Popplerinternals sind nicht erfasst. `strace` war nicht vorhanden und wurde nicht installiert. Der statisch gelesene Code, reale Fünfdateien-Nachbau, dokumentierte Requests, Subprozessarguments und Python-Auditdaten tragen die begrenzte Aussage. Ein universeller Schutz gegen beliebige Umgebungen oder native Prozesszugriffe wird daraus nicht abgeleitet.

## Tatsächlich ausgeführte zusätzliche Gegenfälle

`adversarial_cases.py` und `countercase-plan.json` dokumentieren Verfahren und Vorabregeln. Jeder Fall nutzte eine neue eigene Fünfdateienkopie mit unverändertem Frozen-Code; die 17 eigenen Codekopien sind nachträglich alle gegen die drei Manifesthashes geprüft. Keine Caseausgabe wurde in den gemeinsamen `outputs/public-reproduction`-Baum geschrieben. Vorhandene künstliche Sentinels und Symlinks betreffen ausschließlich eigene Casepfade.

| Gegenfall | Tatsächliches Ergebnis |
| --- | --- |
| Vorhandene reguläre Zieldatei mit eigenem Sentinel | CLI Exit 1; Sentinel unverändert, kein Sidecar. |
| Dangling Symlink direkt am Ziel | CLI Exit 1; fehlendes Linkziel nicht angelegt. |
| Provenienz-Eingabe als Symlink auf bytegleiche eigene Datei | CLI Exit 1; kein neues Ausgabeziel. |
| Tatsächlich um ein Newline-Byte veränderte eigene Provenienzdatei | CLI Exit 1 wegen Inputpin; kein neues Ausgabeziel. |
| Verschachtelte Elternkomponente `nested/../escape` | CLI Exit 1; kein neues Ausgabeziel. |
| Bloßer Ausgabeoberordner ohne eigenes Kind | CLI Exit 1; kein neues Ausgabeziel. |
| Absoluter eigener Zielpfad | CLI Exit 1; kein neues Ausgabeziel. |
| Anderer Ausgabebaum `outputs/loop/...` | CLI Exit 1; kein neues Ausgabeziel. |
| Eigene Transportinjektion mit tatsächlich veränderten PDFbytes | Aufruf Exitabbildung 1; PDFpinfehler, Sidecar `NICHT_BESTANDEN`, keine Annotation. |
| Eigene HTTP-503-Injektion | Aufruf Exitabbildung 1; Sidecar `NICHT_BESTANDEN`, keine Annotation. |
| Poppler fehlt über leeren eigenen Prozess-PATH | Aufruf Exitabbildung 1; `FileNotFoundError`, Sidecar `NICHT_BESTANDEN`, kein gestarteter Poppler. |
| Eigenes Poppler-Testexecutable beendet Extraktion mit Exit 23 | Tatsächlicher Unterprozess Exit 23; Aufruf Exitabbildung 1, Toollog erhalten, Sidecar `NICHT_BESTANDEN`, keine Annotation. |
| Unveränderter vollständiger echter Lauf wird mit vorhandenem Ausgabeverzeichnis wiederholt | CLI Exit 1; sämtliche vorhandenen Laufdateien blieben hashgleich. |

Die ersten acht Zeilen sind echte separate CLI-Prozesse. Download-/Werkzeugfehler wurden in einem frischen Prozess durch dokumentierte Transport- beziehungsweise eigene PATH-Seams ausgelöst; diese sind tatsächlich ausgeführte synthetische Fälle gegen unveränderte Wrapper-/Builderbytes. Es wird kein realer Remote-503 behauptet. Alle äußeren Reviewer-Controller endeten mit Exit 0, weil sie die erwarteten inneren Fehler erfassten. Vollständige inneren Ergebnisse stehen in `cases/<name>/result.json`, die Wiederholung in `repeat-existing-directory.json`.

Drei weitere ausgeführte Fälle untersuchten ausdrücklich die dokumentierten Grenzen:

| Grenze | Eigene Beobachtung und Bewertung |
| --- | --- |
| Redirect mit weiterhin exakt gepinnten Originalbytes | Die eigene Transportantwort gab eine abweichende `finalUrl` unter `example.invalid` zurück. Der Wrapper nahm die gepinnten Bytes an und dokumentierte die abweichende URL. Annotation bytegleich, Status `BESTANDEN`. Das ist ein synthetischer Response-/Redirectfall; bei den realen Downloads gab es keinen beobachteten Redirect. Der Code bindet Startadressen und Bytes, keine Allowlist für Redirect-Endhosts. Die Dokumentation verspricht keine solche Allowlist. |
| Versionsabfrage scheitert, Extraktionen gelingen | Eigenes Tool gab nur für `-v` Exit 7 zurück; tatsächliche Extraktionen durch `/usr/bin/pdftotext` gelangen. Sidecar hielt `versionExit: 7` und die Fehlermeldung fest, Annotationvergleich blieb `BESTANDEN`. Der Status bestätigt hier die Nachbaubytes; er behauptet keinen Erfolg dieser Versionsabfrage. |
| Quellenänderung unmittelbar nach erfolgreicher Extraktion | Der eigene Subprozess-Controller ersetzte jede Quelldatei nach ihrem erfolgreichen `-bbox`-Lauf durch eigene kurze synthetische Bytes. Die Annotation blieb historisch bytegleich, Status `BESTANDEN`; die archivierten Quellen stimmten anschließend nicht mehr mit den beim Download protokollierten Hashes überein. Mutation und aktuelle Hashes sind erhalten. Das zeigt die deklarierte Race-/TOCTOU-Grenze praktisch. Der Wrapper ist keine Sandbox und verspricht keinen Schutz vor gleichzeitiger fremder Dateimanipulation. |

Diese Beobachtungen sind keine erfundenen Findings gegen nicht zugesagte Schutzgarantien. Bei einer künftigen Anforderung, Endhosts zu beschränken oder Archive gegen Dateimanipulation zu sichern, müssten Code und Abnahme entsprechend erweitert werden. Eine erneute SHA-Prüfung kann eine spätere Veränderung feststellen, beseitigt für sich allein keine allgemeine TOCTOU-Grenze.

## Originalfundstellen und Nutzungsrechte

Den [ESS-Disclaimer](https://www.europeansocialsurvey.org/contact/disclaimer) las ich nach eigenem unverändertem HTTP-200-Abruf, 2026-10-03 08:20:37 UTC, SHA-256 `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d`. Maßgebliche Fundstellen: „Conditions of use“, „Restrictions“ und der Absatz vor „Conditions of use“ zu extern gespeicherten Datensätzen. Dort werden ESS-Daten unter CC BY-NC-SA 4.0 und Dokumentation unter CC BY-SA 4.0 getrennt. Die Empfehlung, auf das Datenportal zu verlinken, ist kein pauschales Weitergabeverbot. Originalbytes und Abrufprovenienz liegen in `license-sources/ess-disclaimer.html` und `downloads.json`.

Ich las selbst [CC BY-SA 4.0 Legal Code](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en), §§ 2(a)(1), 2(a)(5)–(6), 3(a)–(b), sowie [CC BY-NC-SA 4.0 Legal Code](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en), §§ 2(a)(1), 3(a)–(b). Die CC-Texte regeln unter anderem Attribution, Änderungsvermerke, ShareAlike bei einschlägigen Bearbeitungen und bei der Datenlizenz den nichtkommerziellen Rahmen. Sie geben keine ESS-Billigung des Projekts. Ein konkreter späterer Export bleibt einzeln zu prüfen. Der Lizenzrahmen wird hier nicht auf den gesamten eigenen Code übertragen.

Fehlläufe bleiben sichtbar: Der Web-ESS-Abruf gab 502; der direkte ESS-Abruf gelang anschließend. Beide direkten CC-Abrufe gaben 403; die Texte wurden über das verfügbare Webwerkzeug erfolgreich gelesen, dessen gelesene Ausgabe in `license-sources/web-cc-read.json` erhalten ist. Kein Authzugriff oder stellvertretendes Akzeptieren von Bedingungen fand statt. Der historische Codebook-4.1-Nachbau erbringt keinen Abgleich mit Datenedition 4.2.

## Findings und offene Prüfungen

Keine belegten Findings `RC-Cxx`. Es gibt weder eine Sollzahl noch eine Fehlerquote. Die drei oben ausgeführten Grenzbeobachtungen widersprechen dem erklärten Paketumfang nicht und werden nicht als erhebliche Fehler ausgegeben.

| Gegenstand | Status dieser Erstprüfung |
| --- | --- |
| Manifestbindung, sichere gebundene Eingaben vor/nach, eigene Codekopien unverändert | `BESTANDEN` |
| Eigener Nachbau aus genau drei Codes und zwei öffentlichen Eingaben mit drei echten neuen Downloads | `BESTANDEN` |
| Historische Annotationbytes und Metadaten erhalten; aktueller Sidecar getrennt | `BESTANDEN` |
| Ausgeführte Pfad-/Symlink-/Provenienz-/PDFpin-/Download-/Extraktionsgegenfälle und bestehendes Ziel unverändert | `BESTANDEN` im dokumentierten Umfang |
| Semantische vollständige Quellen-/Zellenkorrektheit der historischen C-v2-Annotation | `NICHT_GEPRÜFT` |
| Unabhängige fachliche C-v2-Korrekturnachprüfung | `NICHT_GEPRÜFT` durch diesen CODE-Auftrag |
| ESS-Rohantworten, Stichprobendesign/-zeilen, A/B, Wahl-/Links-rechts-Werte, Portal-Analysen, Datenedition-4.2-Abgleich | `NICHT_GEPRÜFT`, vom Auftrag ausgeschlossen |
| Messmodell, Eignung, Polung, Reliabilität, Validität, politische Neutralität, Unsicherheit | `NICHT_GEPRÜFT` |
| Vollständige OS-/Native-Subprozess-Sandboxprüfung oder Racefreiheit | `NICHT_GEPRÜFT`; nicht als Schutzgarantie zugesagt |
| Konkrete Veröffentlichung/Lizenzentscheidung für späteren Web-/Modellexport | `NICHT_GEPRÜFT` |
| Website/Browser/UI | `IN_DIESER_PHASE_NICHT_ERFORDERLICH`; kein UI-Auftrag und keine UI-Änderung |
| `pnpm check`, Commit, Push | Nicht ausgeführt, durch den eigenen Prüfauftrag ausgeschlossen; keine technische Repository-Gesamtfreigabe |

Der Bericht urteilt nicht über den Abschlussstand anderer Erstprüfer oder eines Jurors. Er kann durch Bytegleichheit deren Urteil, eine andere Modellfamilie oder spätere wissenschaftliche Gates nicht ersetzen.

## Werkzeug- und Befehlsprotokoll

Die vollständig angebotenen 633 Nested Tools einschließlich Beschreibungen und die direkten Werkzeuge sind in `tools-and-model.json` erhalten. Tatsächlich benutzt: `functions.exec`, `exec_command`, `apply_patch`, `write_stdin`, `web.run`, `collaboration.send_message`. Keine Agentliste oder weiteren Agents. Alle Shell-CWDs waren explizit, alle Patchpfade absolut. Der aufgerufene Reviewer-Code, Vorabplanung, vollständige Nachbau-/Gegenfallarguments, Runtime-Exits, stderr/stdout, Fehlläufe und lokale Nachprüfungen sind unter den oben benannten Artefakten gespeichert. `command-ledger.md` führt auch reine Lesungen, gekürzte Toolausgabe mit Nachlesung und die erfolglosen Netzlesungen auf. Das tatsächliche Werkzeugtranskript enthält die vollständigen Shell-Heredoc-Bodies der frühen reinen Lesungen; der Ledger gibt diese nicht als nachträglich ausgeführte Dateien aus.

Keine ESS-Roh-/Lokal-/Antwort-/Designzeilen, Personenkennungen, Authsecrets, globalen Writes, Installationen, Commit/Push, Gesamtformatierung oder Websiteänderungen. Die einzige spätere Datei außerhalb des eigenen Outputbaums ist dieser zugewiesene Erstbericht. Bericht und Erstprüfungsartefakte bleiben nach Abschluss unverändert; `own-index.json` und `completion.json` werden mit Abschluss-SHA separat übergeben.

## Vollständiger tatsächlich erhaltener Auftrag

```text
Frischer unabhängiger CODE-Erstprüfer REPRO-003-C, kein Autor. Ausschließlich Worktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003 Branch research/life-93-night-20261003. Shellworkdir explizit, apply_patch ABSOLUT. Paket reports/loop/packages/REPRO-003-C/v1/manifest.json SHA 5cb5e10f09f32fa52a6929a33a92f56b384fe4a6af34fa583acb0e8c5feb11d3,16files31sourceInputs. Alle gefrorenen Anforderungen/LIFE93/AGENTS/Dauerauftrag/Analyseplan/Prüfregeln/Lizenzen/Prüfauftrag/NachbauDoc/Autorenbericht lesen. Keine anderen aktuellen Reviewer-/Jurorberichte/Loopfindings/Agentlisten/Verteidigung; keine weiterenAgents. Hauptauftrag Code und Behauptungen: neuer Wrapper pipeline/reproduce_c_annotation.py, Builder annotations/c_builder_v2.py, source_geometry.py. Ist historisches C2 exakt nachbaubar aus nur3Codes+2PublicInputs, feste offiziellePDFURLs3SHA, keine Rohlesungen/Auth/globalenWrites, sichere begrenzte frischeOwnOutputpfade ohne Überschreiben; Symlink/traversal/Pin-/Werkzeugfehler/Unterprozesse/Quellewechsel aktiv prüfen mit echten zusätzlichen eigenen Gegenfällen. Nur eigene Kopien code aus Frozen16 nutzen, eigene Ausgabeunterkopie muss aufgrundWrapperoutputs/public-reproduction Regel unterdeinemOwnClonebleiben; keine ROOTLiveAusgabe/Originalcode starten! GenauesalleROOT/OUT/CACHE/TARGET/LogPreflight vorStart. Historische Annotationmetadaten behalten oldtiming/authorstatus/peerflags/sourcelegacycachepaths; separate reproduction.json beschreibt aktuellenLauf, wederScience nochIndependentRecheck ausByteEqualityableiten. GrenzenHTTPRedirect/sourceavailability/raceTOCTOU/pathchecks nichtOSsandbox sachgerecht prüfen, kein hypothetischesRisiko erfundeneFindingpflicht. Primärquellen fürnötigeZitation/Lizenzbehauptungen selbst lesen; keine Veröffentlichungsgarantie erfinden. Alle16+31InputsHash/SafePathsVorNach, Codeunverändert. Eigene Skripte/Originaldownloads/SyntheticCases/logs ausschließlich outputs/loop/repro003-c-code/, vollständiger Erstbericht reports/loop/reviews/REPRO-003-C-code.md. Jede FindingRC-Cxx genaueAussageProblemBelegFundstelleWirkungbegründeteSchwerekonkreteKorrekturNachprüfung; geplantesnichtausgeführtNICHTGEPRUEFT. KEIN ESSraw/local/AntwortoderDesignzeilen/A/B/ParteiLRwerte/PortalAnalysis/AuthSecrets/globalWrites/InstallConda/CommitPush/Gesamtformat/pnpmcheck/Websiteänderung. GemeinsameArtefakteundErstberichtbeendigungimmutable. Tatsächlicher vollständigerAuftragwortgetreu, alleangebotenen+genutztenWerkzeuge/CommandsExitsFehlläufe, Modellgpt-6.1-solultrageerbtinternunknown; gleicheCodexfamilie KI-AuditnichtakademischesPeerReview/Gültigkeitsgarantie. OrganisatorischeTrennungSharedFSkeineOSsandbox. NachabschlussSHA+OwnIndexmelden.
```

Bericht abgeschlossen am 2026-10-03T08:37:51.884258+00:00.
