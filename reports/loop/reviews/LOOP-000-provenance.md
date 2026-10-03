# LOOP-000: Nachprüfbarkeit und Statusgrenzen

Die eingefrorenen Dateien, die Übernahme der main-Webdateien und das erhaltene alte Auditarchiv sind anhand ihrer Hashes und Git-Objekte nachvollziehbar. Die wissenschaftlichen Voraussetzungen bleiben im gespeicherten Zustand offen. Ich beanstande einen Widerspruch zwischen den aktiven Regeln für Prüfstatus. Dieser Bericht erteilt weder eine wissenschaftliche Freigabe noch eine vollständige LOOP-000-Abnahme.

## Prüfgegenstand und Trennung

- Reviewer: `/root/loop000_review_provenance`, unabhängiger Codex-Subagent, kein Autor.
- Arbeitsort: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Keine Zugriffe auf den ursprünglichen Arbeitsbaum oder andere Projekte, abgesehen von der vorgegebenen `unslop`-Skill.
- Prüfpaket: `reports/loop/packages/LOOP-000/v1/manifest.json`, eingefroren am `2026-10-03T01:13:38.863167+00:00`.
- Selbst berechneter Manifest-SHA-256: `ac9f8f5231f881c883e771cc50072e43a20b6db8519db06ca76453ddc45a2496`.
- Code-Commit: `002fb8e28b57559179692668d3abd89b1d852082`. Eingehendes main: `87eb549c7b601630c9efdce1825b1f6ae9e3cdc0`.
- Erste Zeitabfrage: `2026-10-03 01:14:51 UTC`. Abschluss der inhaltlichen Prüfungen: `2026-10-03 01:20:31 UTC`. Die anschließende Bearbeitung beschränkt sich auf diesen Bericht und seine Formatprüfung.
- Keine weiteren Agents gestartet. Keine aktuellen oder alten Reviewerurteile und keine zusätzliche Autorenverteidigung gelesen. Alte Berichtsdateien wurden ausschließlich für Hashvergleiche als Bytes verarbeitet. Gelesen wurden die vorgegebenen Loop-Findings und dokumentierte alte Prüfprotokolle.
- Modellangabe: Codex-Subagent ohne von mir gesetzten Modelloverride. Das Paket dokumentiert die gemeinsame Laufzeitfamilie `gpt-6.1-sol`; ich habe diese Kennung nicht über eine separate Modell-API verifiziert. Eine eigene interne Modellrevision und nicht zugängliche Anbieterregeln sind unbekannt. Es fand kein Review durch eine andere Modellfamilie statt.
- Genutzte Werkzeuge: `functions.exec`, Shell über `exec_command`, Python für JSON-, Hash- und Metadatenvergleiche, Git für historische Blobs und Remote-Referenz, UTC-Uhr und `apply_patch` für diesen Bericht. Versionsabfragen ergaben Node `v24.21.0`, pnpm `11.23.0`, Python `3.14.7`, Git `2.55.0`, Benutzer-ID `1000`. Browser-, Webrecherche- und Delegationswerkzeuge wurden nicht eingesetzt.

Die aktiven Forschungsdateien wurden nicht als spätere Ersatzfassung bewertet. Wo aktuelle Dateirechte oder die Remote-Referenz geprüft wurden, ist das unten ausdrücklich als zusätzliche Beobachtung ausgewiesen.

## Finding L000-P01: Zwei unvereinbare Prüfstatus-Vorgaben

**Betroffene Aussage.** `docs/pruefregeln.md`, Zeile 9, schreibt für jeden Prüfbericht vor: „Vier Zustände sind erlaubt: `offen`, `durchgeführt`, `freigegeben`, `entfällt`.“ Der neue Auftrag verlangt dagegen `BESTANDEN`, `NICHT_BESTANDEN`, `NICHT_GEPRÜFT`, `BLOCKIERT` und `IN_DIESER_PHASE_NICHT_ERFORDERLICH`. Der Arbeitsloop übernimmt diese fünf Zustände, und der neue Zustand nutzt sie bereits.

**Problem und Fundstellen.** Die universelle Formulierung der weiterhin aktiven Prüfregeln wurde beim Einführen des neuen Schemas nicht eingegrenzt oder ersetzt. Es gibt keine dokumentierte Zuordnung und keine Trennung zwischen Bearbeitungsstand und Prüfergebnis. Fundstellen in der tatsächlich geprüften Fassung:

- `reports/loop/packages/LOOP-000/v1/files/docs/pruefregeln.md:9`
- `reports/loop/packages/LOOP-000/v1/files/docs/auftrag-life-93-2026-10-03.md:133`
- `reports/loop/packages/LOOP-000/v1/files/docs/arbeitsloop.md:22`
- `reports/loop/packages/LOOP-000/v1/files/reports/loop/state.json:75`

Die ersten drei Dateien sind Bestandteil des Manifests und ebenfalls im Code-Commit `002fb8e28b57559179692668d3abd89b1d852082` enthalten.

**Wirkung.** Eine neue Sitzung kann den Ergebnisstatus nach der einen Vorgabe korrekt schreiben und nach der anderen unzulässig. `durchgeführt` unterscheidet außerdem keinen erfolgreichen von einem fehlgeschlagenen Lauf. Das behindert die verlangte dauerhafte Wiederaufnahme und eine spätere eindeutige maschinelle Prüfung. Das Paket verlangt ausdrücklich kohärente aktive Anweisungen. Ich habe dadurch keinen falsch bestandenen empirischen Check nachgewiesen.

**Schweregrad: mittel.** Der Widerspruch betrifft einen verbindlichen Teil des Fortsetzungs- und Abnahmeverfahrens. Die im eingefrorenen Zustand sichtbaren wissenschaftlichen Prüfungen sind weiterhin offen, weshalb ich keinen erheblichen wissenschaftlichen Fehler daraus ableite.

**Abhilfe.** Die aktive Fassung der Prüfregeln auf das neue Ergebnisvokabular abstimmen. Falls die bisherigen Wörter weiterhin einen Bearbeitungsstand bezeichnen sollen, dafür ein getrenntes Feld mit eindeutiger Bedeutung definieren. Historische Berichte und eingefrorene Auditfassungen bleiben unverändert. `NICHT_GEPRÜFT` und `BLOCKIERT` dürfen dabei nicht in eine Freigabe übersetzt werden.

**Konkrete Nachprüfung.** Die korrigierte aktive Regelstelle und alle neuen Statusfelder in einem neuen Manifest erfassen. Eine unabhängige Nachprüfung vergleicht die erlaubten Werte in Auftrag, Arbeitsloop, Prüfregeln und Zustand; sie kontrolliert insbesondere die Darstellung einer fehlgeschlagenen, nicht durchgeführten und blockierten Prüfung. Diese Kontrolle ist eine formale Statusprüfung, keine empirische Abnahme.

## Tatsächlich ausgeführte Prüfungen

| Prüfung                                                                          | Ergebnis und Reichweite                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 27 Paketdateien gegen Manifest-SHA-256 und Bytezahlen                            | BESTANDEN, keine Abweichung.                                                                                                                                                                                                                                                     |
| 64 als unverändert bezeichnete Code-Dateien gegen Blobs des Code-Commits         | BESTANDEN, keine Hashabweichung.                                                                                                                                                                                                                                                 |
| Merge-Eltern                                                                     | BESTANDEN. `55a001881cea242b19255fdd2588a4ff9fbd5dd9` hat `be8fa31ec902941707e0f39f10d0785457a75175` und das angegebene eingehende main als Eltern.                                                                                                                              |
| Sämtliche 61 in main getrackten Webdateien gegen Code-Commit                     | BESTANDEN, bytegleich.                                                                                                                                                                                                                                                           |
| `docs/handbuch.md`, `docs/assets.md`, `docs/validation.md` gegen main            | BESTANDEN, bytegleich.                                                                                                                                                                                                                                                           |
| Altes Auditarchiv gegen Forschungs-Merge-Elternteil                              | BESTANDEN. Alle 106 Dateien unter `reports/audit-recherche/` sind bytegleich erhalten.                                                                                                                                                                                           |
| Alte Ausgangs-, Korrektur- und Abschlussmanifeste gegen historische Commit-Blobs | BESTANDEN. 26, 28 und 105 referenzierte Dateien stimmen mit Hashes und gegebenenfalls Bytezahlen überein. Berichte wurden dabei nicht inhaltlich gelesen.                                                                                                                        |
| Drei alte technische Laufprotokolle                                              | BESTANDEN für die gespeicherten Log- und Eingabemanifest-Hashes. Alle drei dokumentieren Exitcode 0. Kein neuer `pnpm check` durchgeführt.                                                                                                                                       |
| Alter technischer Eingabestand gegen neuen Code-Commit                           | BESTANDEN als Unterschiedsnachweis. Je Lauf sind 28 der 63 alten Eingabepfade verändert und 6 nicht mehr vorhanden. Die alten grünen Läufe bestätigen diesen neuen Stand deshalb nicht.                                                                                          |
| Alte synthetische Gegenbeispiele erneut ausgeführt                               | BESTANDEN. Skript aus dem historischen Git-Blob, Exitcode 0, leere Fehlerausgabe, stdout bytegleich mit dem archivierten Log. Keine ESS-Daten verwendet.                                                                                                                         |
| Erste Push-Verifikation                                                          | BESTANDEN als zusätzliche Remote-Beobachtung. `git ls-remote --heads origin research/life-93-night-20261003` lieferte während dieses Prüfintervalls `002fb8e28b57559179692668d3abd89b1d852082`, identisch mit `push-001.json`. Kein Push ausgeführt.                             |
| Git-Ausschluss                                                                   | BESTANDEN für die getesteten Pfade. Paket-, Commit- und aktuelle `.gitignore` stimmen überein; `git check-ignore --no-index` schließt Testpfade in `data/raw/`, `data/local/` und `outputs/` aus. Im Code-Commit ist dort ausschließlich die leere `data/raw/.gitkeep` getrackt. |
| Präregistrierungs- und Modell-Tags                                               | BESTANDEN als lokale Metadatenbeobachtung: kein Tag passend zu `analyseplan-*`, `erwartungsmodell-*` oder `modell-*`. Keine Aussage über vollständige externe Historie oder tatsächliche Blindheit.                                                                              |
| Dateien und Dateirechte                                                          | Ausgeführt als Metadatenprüfung; Einzelheiten unten. Keine Rechte verändert.                                                                                                                                                                                                     |

Ein erster Vergleich der alten technischen Eingaben brach mit Exitcode 1 ab, weil `docs/design.md` im neuen Commit fehlt. Der anschließende vollständige Vergleich führte fehlende Pfade getrennt auf und schloss mit Exitcode 0 ab. Der Abbruch ist kein fehlgeschlagener Produktcheck und wird hier nicht als erfolgreicher Lauf versteckt.

Die alten Manifest-SHA-256-Werte sind:

- Ausgangsfassung: `dab36982ce6aac113acc2f807611e8630b546ee451684d683a096e0b4fd23cd8`
- Korrekturfassung: `c6fef40eff714e5e15bdf045c6e46f92b2e14bddda14a24148e56349c2439406`
- Auditabschluss: `c27390c7744d47883943033fcfb4ff9d22fd6ecf94ea4535c71e636c7b1ed9ca`

Das wiederholte synthetische Skript hat SHA-256 `4b104202c5095dd3c95c5cdf09c9a371be0cb9ae2b9bf54a9f2c193729291d6c`; seine neue stdout-Prüfsumme ist wie im alten Log `3968528d5e643de4f395c9a72db583ea7afa075251c71bcac5862672ada3a1fc`. Diese Gegenbeispiele prüfen mathematische Einzelfälle und keine Projektpipeline oder Normlösung.

## Forschungsabnahmen und Reparaturrunden

Der im Paket gesicherte neue Auftrag umfasst alle LIFE-93-Phasen. `AGENTS.md:23` hebt die frühere reine Recherchegrenze ausdrücklich auf; fehlende wissenschaftliche Voraussetzungen bleiben verbindlich. Auftrag und Arbeitsloop verlangen zwei unabhängige Reviews für relevante Pakete, fünf Fachreviewer an den großen Forschungsabnahmen und einen anschließend unbeteiligten Juror. Sie erlauben getrennte Wellen bei begrenzten Slots. Der neue Zustand gibt weder das Setup noch Phase 0 oder spätere Phasen als vollständig abgeschlossen aus.

Das alte `agent-protokoll.json` im Code-Commit dokumentiert sechs tatsächliche Agent-Aufträge mit zurückgegebenen Tasknamen und `fork_turns: none`. Die fünf Erstberichte waren laut Protokoll um `00:27:44 UTC` abgeschlossen; als Beginn der Zusammenführung ist derselbe Zeitpunkt erfasst. Der Juror ist danach, um `00:42:54 UTC`, registriert. Das sind dokumentierte Beobachtungszeiten, keine unabhängige Rekonstruktion der tatsächlichen Spawn-Ereignisse aus Anbieterlogs. Die sechs Berichtshashes wurden durch den Vergleich des Abschlussmanifests geprüft.

Codex-Reviews ersetzen im Auftrag, Arbeitsloop und Zustand ausdrücklich weder Claude-Erstbewertungen noch Claude-Review oder Setup-Abnahme. `ACCESS-CLAUDE` ist blockiert; Setup und öffentliche Tags sind ungeprüft. Endgültige Itemauswahl, empirische Modellentwicklung, B-Zugriff und Entblindung bleiben dadurch gesperrt. Eine persönliche Statistik-Abnahme durch Steven wird nicht zusätzlich eingeführt. Menschliche Releasefreigabe und Verständnistest bleiben spätere echte Voraussetzungen. Diese Abgrenzungen sind nachvollziehbar; sie sind keine Bestätigung wissenschaftlicher Güte.

Die 15 vorhandenen Finding-IDs einschließlich `A-F01` bleiben im neuen Register erhalten. Die drei als korrigierter Wortlaut geführten Einträge haben `repairRounds: 1` und begrenzen `BESTANDEN` ausdrücklich auf die eingefrorene alte Forschungsfassung. Die zwölf anderen Einträge stehen auf `NICHT_GEPRÜFT` mit `repairRounds: 0`; ihre empirischen Untersuchungen haben noch nicht begonnen. Die fünf erheblichen abhängigen Anforderungen stehen in `blockingFindingIds`. Ich habe keine zurückgesetzte strittige Runde nachgewiesen. Bei späterer Arbeit muss dieselbe Kennung die tatsächlichen Bearbeitungsrunden behalten; bloß neue Agents oder ein neuer Modellname eröffnen keine unabhängige Bestätigung.

Der alte fehlgeschlagene Abschlusslauf ist erhalten: `07-abschlusspruefung-erster-lauf.json` meldet eine Abweichung bei `.prettierignore`. Danach dokumentieren der technische Abschlusslauf und `07-abschlusspruefung.json` eine Korrektur und Wiederholung. Die Belege unterscheiden Hashintegrität, formalen Textabgleich und spätere empirische Anforderungen. Der neue Zustand setzt `currentLocalTechnical` sowie `currentIndependentIntegration` korrekt auf `NICHT_GEPRÜFT`; die alte technische Freigabe wird dort nicht auf die integrierte Fassung übertragen.

## Wiederaufnahme, Dateirechte und Datenschutz

Die eingefrorene `state.json` unterscheidet sich von ihrer Version im Code-Commit; `push-001.json` ist erst im Paket vorhanden. Der Git-Commit allein rekonstruiert deshalb den nach dem ersten Push ergänzten Zustand nicht. Das Paket enthält beide Fassungsbestandteile mit Hash und erfüllt hier die vorgesehene Ergänzung zum Commit. Der verifizierte erste Push bestätigt den Commit, nicht die spätere Veröffentlichung dieses Prüfpakets. Ein späterer gesicherter Checkpoint muss das fertige Paket und den aktualisierten Zustand erfassen. Das ist im hier geprüften WIP noch kein behaupteter Paketabschluss.

Die im Auftrag benannte Sicherung des ursprünglichen uncommitteten Arbeitsbaums unter dessen `outputs/loop/bootstrap-20261003T010447Z/` habe ich aufgrund des vorgegebenen Worktree-Zugriffs nicht geöffnet. Die Erhaltung des Forschungs-Merge-Elternteils und des Auditarchivs ist unabhängig prüfbar; die Behauptung, der ursprüngliche aktuelle Arbeitsbaum sei unverändert, bleibt in dieser Prüfung `NICHT_GEPRÜFT`.

Aktuelle Metadaten zeigen `0755` für das Paketverzeichnis und die alte Ausgangsfassung sowie `0644` für Paketmanifest, eingefrorene `AGENTS.md` und einen alten Erstbericht. Diese Pfade sind für den gemeinsamen Benutzer schreibbar. Git bewahrt den früher dokumentierten Schutz ohne Schreibbits nicht als solchen. `02-schreibschutz.json` bezieht seine Schutzbehauptung auf `00:17:44 UTC` und nennt bereits die Grenze desselben Benutzers; der neue Pakettext nennt ausdrücklich eine gemeinsame Dateiumgebung ohne Sicherheitssandbox. Ich habe keinen aktuellen unbefugten Inhaltseingriff festgestellt. Die Hashkontrolle belegt Unverändertheit zum Prüfzeitpunkt, keinen erzwungenen Zugriffsschutz.

`data/raw/` ist ein Verzeichnis; der Unterpfad `data/raw/ess11-ed4.2` ist laut `lstat` ein Symlink. Ich habe den Link nicht inhaltlich verfolgt. Keine Rohdatei, Antwortzeile, Personenkennung, bestätigende Hälfte B oder gesperrter Partei-/Lagerwert wurde gelesen oder ausgegeben. Der im Paket gespeicherte Rohdatenhash wurde als Metadatum übernommen, nicht erneut aus der Rohdatei berechnet. Sein Abgleich mit einem ESS-Originaldownload bleibt ungeprüft, wie das Manifest selbst festhält.

Die Lizenzakte trennt Daten- und Dokumentationslizenzen und nennt den Rohdatenausschluss eine zusätzliche Projektregel. Diese Prüfung wiederholt weder die juristische Quellenprüfung noch eine Veröffentlichungsfreigabe. Der Git-Ausschluss und die Paketstruktur enthalten keinen gefundenen Rohdatenexport; ein vollständiger Geheimnis- oder Rohdaten-Leakscan der gesamten historischen Git-Historie wurde nicht durchgeführt.

## Offen und Ergebnis

`NICHT_GEPRÜFT` bleiben ein neuer technischer Lauf der integrierten Fassung, aktuelle Browserfunktion, gehostete CI, CodeRabbit-Lauf, vorgeschriebene Claude-Prüfungen, wissenschaftliche und empirische Abnahmen sowie menschliche Verständlichkeit und Releasefreigabe. Auch die tatsächliche Einhaltung aller Zugriffsbeschränkungen durch frühere Agents ist durch gemeinsame Dateirechte und Auftragsprotokolle allein nicht bewiesen.

Für diesen Review ist L000-P01 offen. Die nachgewiesenen Integritäts- und Git-Vergleiche tragen die Übernahme- und Erhaltungsaussagen innerhalb ihres benannten Umfangs. Sie ersetzen die offenen Checks des Pakets und die späteren Forschungsabnahmen nicht. Es wurde kein akademisches Peer Review und kein Validitäts- oder Neutralitätsnachweis erbracht.
