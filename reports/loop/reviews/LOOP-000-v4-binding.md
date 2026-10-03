# LOOP-000 v4: unabhängige Nachprüfung der Scopebindung

Die zweite Reparaturrunde von L000-G04 und dem Bindungsanteil von L000-B03 ist für den festgelegten formalen Umfang BESTANDEN. Zustand und JSON-Abnahmebericht müssen jeweils exakt `LIFE-93/<phase>/complete-v1` tragen. Falsche nichtleere, fehlende, begrenzte und fremdphasige Kennungen scheitern in meinen eigenen Gegenfällen trotz ansonsten vollständiger Hash- und Archivbindung. Es gibt kein neues belegtes Finding in diesem Prüfumfang.

Die neun eingefrorenen Autorentests bestehen bei eigener Ausführung. Der eingefrorene tatsächliche Zustand bleibt RUNNING. `make all` liefert weiterhin Exit 2 und `scientificReproduction: BLOCKIERT`, selbst bei einer formal vollständigen synthetischen DONE-Fassung. Diese Nachprüfung erzeugt keine wissenschaftliche, menschliche, Website-, Phasen- oder Releaseabnahme.

## Prüffassung und Zugriff

Reviewer `/root/loop000_v4_binding`, eigenständiger Codex-Subagent, 2026-10-03. Der Zielworktree ist `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Projektbezogene Shellaufrufe nutzten diesen Worktree ausdrücklich; Unterprozesse liefen in den eigenen synthetischen Projektwurzeln darunter.

Das v4-Manifest `reports/loop/packages/LOOP-000/v4/manifest.json` hat den selbst berechneten SHA-256 `d5d68311890060cd48f30ff4588f3ed512e7f238ee50457be8dee692825d9cee`. Alle 19 gelisteten Dateien stimmen vor und nach der Prüfung in Hash und Bytezahl. Zusätzlich bestätigt das eingefrorene `verify()` diese 19 Dateien mit `allPassed: true`. Belege sind `outputs/loop/v4-binding/integrity-before.json`, `integrity-after.json` und `frozen-verify.json`.

Der Manifestcommit ist `866a6c6fa0a1215ea743ccc6c969ec320224a80e`. Maßgeblich waren ausschließlich die eingefrorenen Dateibytes, keine wechselnde Pipelinefassung. Ausgeführt wurden `pipeline/loop.py`, SHA-256 `a0ee7f1c98fa7b3ef11c797cd26289a12c1df2fb055bc7b45f4e7e0a2f9e729f`, und die neun Autorentests, SHA-256 `e3854830d3e5803864e945d195df98984921da7e8e780786c324fdd3fdf97564`.

`v4:` bezeichnet nachfolgend `reports/loop/packages/LOOP-000/v4/files/`. Der vollständige eingefrorene Ausführungsauftrag, AGENTS, LIFE-93-Issuewortlaut und v4-Prüfauftrag wurden gelesen, ebenso die ausdrücklich erlaubten beiden abgeschlossenen v3-Berichte und die eingefrorenen Autorentscheidungen. Aus dem Findingregister wurden die vorhandenen Einträge L000-G04 und L000-B03 gezielt ausgegeben. Beide führen `repairRounds: 2` und lassen die unabhängige v4-Nachprüfung noch offen. Ich verändere dieses Register nicht und eröffne keine zusätzliche Reparaturrunde.

Die beiden v3-Berichte unterscheiden sich im geprüften Umfang. Der Guardbericht führt den nichtleeren falschen Scope aus; der Browserbericht prüft unter anderem einen leeren Scope. Die Autorentscheidung folgt dem konkreten Gegenfall. Mein positives v4-Urteil beruht auf den nachfolgend selbst ausgeführten Fällen, nicht auf der Übereinstimmung mit einer früheren Bewertung.

Es gab einen Zugriff außerhalb des eingefrorenen Prüfpakets: Vor dessen vollständigem Lesen öffnete ich für die vorgegebenen Repository-Anweisungen `docs/project.md`, `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md`, `docs/entscheidungen.md` und `docs/lizenzen.md` aus dem Zielworktree. Diese sechs aktuellen Kontextdateien waren nicht hashgebundene Prüfeingaben; sie wurden nicht verändert und begründen keine Forschungsabnahme. Das weicht von der engeren Kontextgrenze „aktuelle Forschung nicht lesen“ im eingefrorenen v4-Prüfauftrag ab. Der Koordinator wurde darüber vor meinem Prüfurteil informiert. Die technische Ausführung und alle hier benannten Prüfbelege verwenden weiterhin ausschließlich die eingefrorene Infrastruktur und meine synthetischen Dateien.

Keine anderen v4-Berichte, FOUNDATION- oder PREP-Erstberichte, fremden Forschungsdateien, tatsächlichen Rohdaten, `data/local/`, B-Daten, Partei-/Links-rechts-Werte, Personenkennungen, Cookies oder Zugangsdaten wurden geöffnet. Der Rohdatenhash im Manifest ist ausschließlich gelesenes Metadatum; ich habe keine Rohdatei neu gehasht. Die ähnlich benannten Pfade der Autorentests enthalten ausschließlich deren selbst erzeugte Platzhalter innerhalb meines eigenen TMPDIR.

## L000-G04 / L000-B03, Reparaturrunde 2

Die genaue Sollbehauptung steht in `v4:reports/loop/LOOP-000-v4-pruefauftrag.md:3–5` und im Abschnitt „v3-Nachprüfung und Reparaturrunde 2“ der eingefrorenen Autorentscheidungen. Eine gültige Vollphasenkennung muss im Zustandsfeld und im JSON-Bericht stehen; bloße Übereinstimmung zweier frei benannter Teilprüfungen genügt nicht.

Der Code setzt das um. `v4:pipeline/loop.py:23–24` legt die zwölf Kennungen für `setup`, `release` und `phase-0` bis `phase-9` fest. `completion_binding()` prüft in Zeilen 135–137 den Zustand gegen diese feste Tabelle. Zeile 155 prüft den Bericht nochmals gegen denselben erwarteten Wert. Existenz, echte Manifest- und Berichtshashes, Archivbytes, Phase, BESTANDEN sowie bestandene Berichtschecks mit einer nichtleeren Evidenzangabe bleiben in Zeilen 138–159 erforderlich.

Meine Erwartungswerte wurden in `outputs/loop/v4-binding/run_binding_checks.py:17–19` separat aus dem vorgegebenen Vertragsformat aufgebaut. Die Fixture übernimmt nicht einfach `loop.COMPLETION_SCOPES` als Testoracle. Alle Funktionsaufrufe auf synthetische Fälle übergeben ausdrücklich deren tatsächliche Projektwurzel. Die echte Paketverifikation erhält den tatsächlichen Worktreeroot. Damit wird die Modulwurzel der eingefrorenen Kopie nicht als Projektwurzel missverstanden.

Die Positivfassung in `run_binding_checks.py:67–96` besitzt zwölf separate synthetische Pakete, zwölf existierende JSON-Protokolle und tatsächlich berechnete Hashes. Alle aktuellen Checks und Abhängigkeiten sind BESTANDEN, das Arbeitspaket ist DONE, aktive Agents und Blockerliste sind leer. Sie liefert `validate_state(...): []`. Der unverändert kopierte CLI-Code bestätigt über `make status` Exit 0, DONE und keine Zustandsfehler. Diese Akzeptanz gilt ausschließlich für die formale Fixture.

| Eigener Gegenfall | Ergebnis und konkreter Umfang |
| --- | --- |
| Gleicher falscher nichtleerer Scope in Zustand und Bericht | Für jede der zwölf Phasen abgewiesen. |
| Zwei übereinstimmende `format-only`-Scopes | Für jede Phase abgewiesen; eigener `make status` ebenfalls abgewiesen. |
| Scope fehlt im Zustand, Bericht oder in beiden | Jede Variante in jeder Phase abgewiesen. |
| Zustand korrekt, Bericht falsch; Zustand falsch, Bericht korrekt | Beide Richtungen in jeder Phase abgewiesen. |
| Kennung einer anderen vollständigen Phase | Beide gemeinsam falschen Felder sowie jeweils nur Zustand oder Bericht in jeder Phase abgewiesen. |
| Leeres Feld, Leerzeichen am Vertrag, falsche Vertragsversion | Für jede Phase abgewiesen. |
| Null, Boolean, Zahl, Array, Objekt, Whitespace und falsche Groß-/Kleinschreibung | Sieben zusätzliche Setup-Fälle abgewiesen. |

Das sind 175 eigene Scopefälle, beschrieben in `run_binding_checks.py:135–174`. Nach jeder Protokolländerung wird dessen echter Berichtshash neu in den Zustand geschrieben. Die separate Bindungskontrolle in Zeilen 100–127 bestätigt für alle zwölf Phasen jedes Falls existierende Manifest-/Berichtsdateien, korrekte Manifest-/Berichtshashes und passende Archive. Die Scopefälle scheitern deshalb nicht bloß an einem vergessenen Hashupdate. Der CLI-Gegenfall mit fremder Kennung für Phase 9 wurde ebenfalls ausgeführt und scheitert. `make` meldet bei beiden negativen CLI-Aufrufen Exit 2, weil das aufgerufene Statusprogramm Exit 1 liefert.

Die vollständigen Ergebnisse stehen in `case-results.json`. `summary.json` bestätigt `scopeCasesAllExistenceHashesArchivesValid: true`. Die Anzahl beschreibt den eigenen Lauf, keine Testvollständigkeit, Fehlerquote oder wissenschaftliche Güte.

## Existenz-, Hash-, Archiv- und Statusregressionen

Mit derselben sonst vollständigen Positivfassung kontrollierte ich zusätzlich jede einzeln fehlende Abschlussphase, fehlendes Manifest oder Protokoll, falsche echte Hashwerte, nichthexadezimale beziehungsweise verkürzte Hashes, Großbuchstaben im Manifesthash und einen nicht bestandenen Abschlussstatus. Diese Fälle scheitern.

Bei korrekt aktualisierten Berichtshashes scheitern auch eine falsche innere Phase, abweichende innere Manifestbindung, leere Checkliste, fehlender oder leerer Checkbeleg und jeder nicht bestandene beziehungsweise unbekannte Berichts- oder Checkstatus. Manipulierte Archivbytes und eine fehlende Archivdatei scheitern ebenso wie hashgleiche Symlinks für Archivdatei, Bericht oder Manifest. Die Belege liegen in `run_binding_checks.py:184–248` und den gleichnamigen Fällen in `case-results.json`.

Die 17 isolierten Statusgegenfälle in `run_binding_checks.py:250–264` behalten die vollständige formale Abschlussbindung. Sie setzen jeweils einen aktuellen Check oder eine Pflichtabhängigkeit auf NICHT_BESTANDEN, NICHT_GEPRÜFT, BLOCKIERT, IN_DIESER_PHASE_NICHT_ERFORDERLICH oder einen unbekannten Wert. Weitere Fälle setzen das Arbeitspaket auf einen der vier offenen Status oder einen unbekannten Wert, tragen einen aktiven Agent oder ein blockierendes Finding ein. Jeder Fall scheitert. Insbesondere bleibt die menschliche Phasenausnahme als unerfüllte DONE-Voraussetzung abgewiesen.

Insgesamt enthält der eigene Lauf 235 konkrete synthetische Beobachtungen. Neben den 175 Scopefällen sind dies 24 Bindungsfälle, zwölf fehlende Phasen, fünf Archivfälle, 17 Statusfälle, eine positive Vollvertragsfassung und eine Kontrolle der ausdrücklich dokumentierten Aussagegrenze. Alle lieferten das jeweils erwartete Ergebnis.

## Was die Vertragskennung nicht beweist

Die formale Bindung kontrolliert den erklärten Umfang. Sie bewertet nicht den wissenschaftlichen Inhalt oder die Echtheit eines durchgeführten Menschenbeitrags. Das steht ausdrücklich in `v4:pipeline/loop.py:4–6` und `21–22` und wird hier nicht erweitert.

Ich habe diese Grenze selbst geprüft. Der Fall `declared-full-contract-with-limited-detail` behält die exakte vollständige Kennung, trägt aber im freien Feld `scopeDetail` ausdrücklich ein, dass nur eine Formatprüfung ausgeführt worden sei und wissenschaftliche sowie menschliche Anforderungen ungeprüft seien. Nach korrektem Hashupdate akzeptiert der Guard die Fixture. Beleg `run_binding_checks.py:176–182` und der gleichnamige Eintrag in `case-results.json`. Dies ist die bekannte Grenze zwischen maschinenlesbarer Selbsterklärung und einer inhaltlichen Abnahme, kein neues Finding gegen die ausdrücklich formale Zusage.

Wer aus einer akzeptierten Kennung oder einem leeren `stateErrors`-Array wissenschaftliche Tragfähigkeit ableitet, überschreitet diesen geprüften Umfang. Das positive Urteil zu G04/B03 ersetzt weder die im echten Zustand offenen Anforderungen noch getrennte Erstbewertungen, Methodenreviews, empirische Untersuchung, Verständnistest oder persönliche Freigabe.

## Tatsächlich ausgeführte Läufe und Prüfstatus

Die eigene Ausführung begann am 2026-10-03T03:23:44.513563+00:00 und endete am 2026-10-03T03:23:50.287263+00:00. `run-results.json` dokumentiert Argumente, tatsächliche Arbeitsverzeichnisse, Zeiten und Exitcodes; stdout und stderr liegen jeweils separat im eigenen Outputordner. Code und Autorentests in `frozen-project/` sind unveränderte Kopien aus v4. TMPDIR lag unter `outputs/loop/v4-binding/tmp/`, `PYTHONDONTWRITEBYTECODE=1` verhinderte Bytecodeänderungen am Prüfpaket.

| Konkrete Kontrolle | Status | Reichweite |
| --- | --- | --- |
| Manifest und 19 Datei-Hashes/Bytezahlen vor und nach der Prüfung | BESTANDEN | Eingefrorene Fassung; keine Inhaltsabnahme. |
| Neun Autorentests, eigener unittest-Lauf | BESTANDEN | Exit 0, `Ran 9 tests`, `OK`; eigene `.stderr.log`. |
| Feste Scopebindung G04/B03 Runde 2 | BESTANDEN | 175 eigene Scopefälle mit ansonsten gültiger Bindung. |
| Eigene Existenz-/Hash-/Archiv-/Statusregressionen | BESTANDEN | Ausgeführte synthetische Fälle; keine allgemeine Sicherheitssandbox. |
| Eigene vollständige synthetische Positivfassung | BESTANDEN | Formal gültig; kein realer Projektabschluss. |
| Eingefrorener tatsächlicher Zustand, `make status` | BESTANDEN | Exit 0, RUNNING, `stateErrors: []`; offene Pflichten bleiben sichtbar. |
| Sperrverhalten von `make all` bei RUNNING und synthetischem DONE | BESTANDEN | Beide Aufrufe Exit 2 und `scientificReproduction: BLOCKIERT`. |
| Wissenschaftliche Reproduktion | BLOCKIERT | Der Aufruf erzeugt keine Analysepipeline, kein Modell und keine Ergebnisse. |
| Repositoryweiter `pnpm check` | NICHT_GEPRÜFT | Kein eigener erneuter Gesamtlauf im begrenzten Reviewerauftrag. |
| Forschungsgüte, Claude-Erstbewertungen/-Reviews, menschliche Abnahmen | NICHT_GEPRÜFT | Nicht ausgeführt; keine Ableitung aus Technik oder gelesenen Zustandsangaben. |
| Website-, Browser-, UI- und Releaseprüfung in diesem Reparaturpaket | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Der v4-Prüfauftrag betrifft ausschließlich Infrastruktur. Diese Abnahmen bleiben als Projektanforderungen offen. |

Die gelesenen v4-Autorenlogs dokumentieren ebenfalls neun bestandene Tests, RUNNING/Exit 0 und den blockierten Gesamtlauf. Mein Urteil über diese drei Verhaltensweisen stützt sich auf die eigenen Wiederholungen. Die früheren v3-Browserurteile und der dort offene echte Zoom wurden nicht erneut geprüft oder in eine v4-Freigabe umgedeutet.

## Trennungsgrenzen, Modell und Werkzeuge

Der Startkontext enthielt keinen bisherigen Koordinatordialog und keine anderen v4-Urteile. Die beiden abgeschlossenen v3-Berichte waren ausdrücklich erlaubte Eingaben. Es wurde keine weitere Delegation ausgeführt. Das gemeinsame Dateisystem besitzt keine technisch erzwungene Reviewer-Zugriffssandbox. Die hier protokollierte Zugriffsbeschränkung ist eine Auftragsgrenze; der genannte Zugriff auf sechs aktuelle Regel-/Kontextdateien bleibt sichtbar.

Der Code verspricht keine Abwehr gleichzeitig schreibender Benutzer oder fremder Hardlinks. Ich habe keinen TOCTOU-Race und keinen neuen Hardlinkangriff ausgeführt. Die bestandenen Symlinkfälle und neun Autorentests begründen keinen weitergehenden Schutz. Es wurden ausschließlich dieser eigene Bericht und Dateien unter `outputs/loop/v4-binding/` geschrieben. Kein gemeinsamer Code, Forschungsstand, Zustand, Findingsregister, eingefrorener Prüfinhalt oder anderer Erstbericht wurde verändert. Keine Installation, Systemänderung, Commits, Pushes, Merges oder Deployments.

Im tatsächlichen Startauftrag wurde das geerbte Modell `gpt-6.1-sol`, Reasoning `ultra`, mitgeteilt. Ich nahm keinen Modelloverride und keine unabhängige Provider-/Revisionsabfrage vor. Interne Revision und nicht zugängliche Anbieteranweisungen bleiben unbekannt. Dies ist ein Codex-KI-Audit derselben mitgeteilten Modellfamilie, keine Prüfung durch Claude oder eine weitere Modellfamilie und kein akademisches Peer Review.

Tatsächlich genutzt wurden `functions.exec`, `exec_command`, `write_stdin`, `collaboration.send_message`, Bash, `cat`, `rg`, `sed`, `nl`, Python 3.14.7 mit Standardbibliothek für Hashes, JSON, Import, synthetische Fixtures und Unterprozesse, unittest und Make. Zur abschließenden Formatierung und Formatkontrolle dient nur die bestehende lokale Prettier-CLI via pnpm auf diesem eigenen Bericht. Browser-, Web-, Bild- und externe App-Werkzeuge wurden nicht genutzt.

Der Skill `unslop` wurde unter `/home/stevenh/projects/12axes-germany/.agents/skills/unslop/SKILL.md` gelesen und auf die Berichtssprache angewandt. Eine kurze read-only Registry-Suche in `/home/stevenh/.codex/memories/MEMORY.md` nach `12axes`, `LOOP-000` und `LIFE-93` lieferte keine Treffer. Es wurden daraus keine Projektannahmen übernommen und keine Memories verändert. Diese Instruktionszugriffe sind kein Bestandteil des eingefrorenen Prüfpakets.

Nach gezielter eigener Formatkontrolle und abschließender Hashkontrolle wird dieser Erstbericht nicht verändert. Der Koordinator kann die geprüfte formale Korrektur anhand der unveränderten Berichte und Belege dokumentieren. Die ursprüngliche Kennung L000-G04, die Zuordnung zu L000-B03 und Reparaturrunde 2 bleiben erhalten.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Du bist zweiter unabhängiger v4-Nachprüfer mit frischem Kontext, keine anderen v4-Berichte lesen. Zielworktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Prüfpaket reports/loop/packages/LOOP-000/v4/manifest.json SHA d5d68311890060cd48f30ff4588f3ed512e7f238ee50457be8dee692825d9cee,19 Dateien. Lies eingefrorene Auftrag/AGENTS/Issue/Prüfauftrag, erlaubte beide v3-Berichte+Entscheidungen. Prüfe G04/B03 Runde2 Scopebindung unabhängig inklusive sonst vollgebundener positiverDONEFassung, falschem nichtleerem/fehlendem/format-only und fremdphasen Scope mit aktualisiertenkorrektenHashes. BeideState/ReportScopes müssenfestenvertraulichvorgegebenenPhasevertragLIFE-93/<phase>/complete-v1 erfüllen; prüfeauchExistenz/Hash/Archiv/Statusregressionen und eigeneGegenfälle. Codebelegt nichtwissenschaftlicheWahrheitdesBerichts. NeunAutorentests selbstwiederholen. EchteRUNNINGFassung undallExit2/BLOCKIERT nichtalsMethodenabnahmeumdeuten. Nur eigener Bericht reports/loop/reviews/LOOP-000-v4-binding.md und syntheticfiles outputs/loop/v4-binding/. KeinegemeinsamenÄnderungen/weitereAgents/Commit/Push/globalInstall/Browser. Rohdaten data/raw/data/local,B,Parteien/LR/IDs,Cookies/Credentials/fremdeForschungsdateien absolutnichtlesen. Modellgpt-6.1-sol/ultra lautgeerbterRuntime, interneunbekannt; tatsächlicheWerkzeuge/ganzenStartauftrag/Trennungsgrenzen imBericht. FindingsnurbelegtgenaueClaim/Fundstelle/Impact/Schwere/Korrektur/Nachprüfung, stabileG04IDrunde2, keineerzwungeneKritik. ScopegebundeneFünfPrüfstatus; hashkontrolle19vor/nach; formatnurOwnReport. NachAbschlussErstberichtnichtändern, Datei/SHA melden.
```
