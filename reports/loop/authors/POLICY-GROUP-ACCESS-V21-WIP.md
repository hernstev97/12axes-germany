# POLICY-GROUP-ACCESS-V21-WIP

Stand 2026-10-03T14:58:22.624019+00:00. Die neue Funktionsbibliothek `pipeline/policy_group_access_v21.py` bereitet **ausschließlich private WIP-Gruppenaggregate** vor. Autorarbeit und 43 bestandene synthetische Tests erteilen keine tatsächliche Partei-/Datenfreigabe. Ein echtes Gruppen-Gate, Freeze oder Remote-Tag wurde weder gelesen noch erstellt oder verifiziert. Root koordiniert die separate Annahme und spätere feste Prüffassung.

## API und neues Protokoll

`run_group_reference(repo_root, study_id, pins: AccessPins) -> RunReceipt` verwendet nur die neue reine `prepare_group_references(csv_text, study_contract, group_study_contract)`. Als reine Vorprüfungen werden `policy_access_v2._validate_contract`, `policy_groups_v21._validated_contracts` und nach erfolgreicher Quellenprüfung die feste v2-DE-Metadaten-/43-Fragennormalisierung benutzt. Kein alter I/O-Runner, keine Marginalvorbereitung, kein öffentlicher Export oder Statuspromotion wird aufgerufen. Tests sperren diese alten Funktionen ausdrücklich.

Externe `AccessPins`: `manifest_sha256`, `group_contract_sha256`, `study_contract_sha256`, `freeze_sha256`, `frozen_commit` (40 Hexzeichen), `plan_tag='analyseplan-v2.1'`. Pins werden nicht aus beliebigen lokalen Freigabestrings abgeleitet.

- Gate ausschließlich `reports/loop/gates/pre-group-v21.json`; Paket `GROUP-V21-001/v1`.
- Exakte Gate-Felder: `schemaVersion=1`, `package`, `decision='ALLOW_HISTORICAL_DESCRIPTIVE_GROUPS_V21'`, `reviewedManifestSha256`, `frozenCommit`, `planTag`, **allowedStudyIds**, `reviewers`. Zusätzliche oder fehlende Felder scheitern.
- `allowedStudyIds` ist eine ausdrücklich angegebene nichtleere, eindeutige Untermenge der fünf fixen Studien. Der angeforderte Studienname muss darin enthalten sein. Die Hülle leitet nicht automatisch alle fünf Freigaben ab. Root muss diese Untermenge aus den beiden tatsächlichen Urteilen binden; die Hülle interpretiert keine Reviewtexte.
- Genau zwei verschiedene, nichtleere tatsächliche Berichtdateien direkt unter `reports/loop/reviews/*.md`, jeweils echter SHA256, Rollen `methods_reproducibility` und `sources_constructs_fairness`, Entscheidung `ACCEPTED_BOUNDED`. Autoren-/Zustands-/Handoff-Pfade sind keine Reviewerpfade.
- Manifest ausschließlich `reports/loop/packages/GROUP-V21-001/v1/manifest.json`: `schemaVersion=1`, `package`, `artifacts=[{path,sha256}]`. Öffentliche zusätzliche Manifestmetadaten sind möglich; Artefakte haben exakt zwei Felder, eindeutige kanonische Pfade und tatsächliche passende Bytes.
- Freeze ausschließlich im selben Paket unter `freeze.json`: exakt `schemaVersion=1`, `package`, `frozenCommit`, `planTag`, `reviewedManifestSha256`, `groupContractSha256`, `studyContractSha256`.

Die maschinenlesbaren Gate-/Freeze-Schemata, Schnittstellen und vollständige Pflichtartefaktliste stehen in `outputs/loop/policy-group-access-v21/interface-schema.json`. Das Dokument ist keine angelegte Freigabe. Der vorliegende Vertrag bleibt unverändert SHA256 `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702`.

## Grenze vor Roh-I/O

Vor jeder Rohpfad-Traversierung, jedem Raw-Stat/Open/Read prüft der Runner Gate, Rollen-/Berichtbytes, erlaubte Studie, externe Manifest-/Freeze-/Vertragspins, alle Manifestartefakte, aktuelle und beim Import erfasste Runtime-Librarybytes sowie Katalog-, Studien- und Gruppensource-Verknüpfungen. Das Manifest benötigt hier 48 feste öffentliche Pflichtartefakte: drei Verträge/Katalog, acht tatsächliche Runtime-Libraries und die übrigen im Gruppenvertrag gebundenen Inventar-/Erratum-/KnownDataContext-/Originalquellenbytes.32 Originalquellen werden nur gehasht; kein neuer Abruf oder Antwortquery.

Die vollständigen Regeln der v2.1-Hülle und die fünf Studienbindungen sind zusätzlich durch kanonische Projektionen des unveränderten Quellenentwurfs fixiert. Nur opake Inputreferenzen sowie unabhängig manifestgebundene Referenzhashes sind daraus ausgenommen, damit synthetische Repositories ohne Originaldaten geprüft werden können. Gewichte,100/5-Heuristik, alle Parteicodes/Other, Feld-UUIDs/Versionen, Wortlaute und Grenzen werden dadurch nicht frei einstellbar. Aktuelle v2-Fragencodes/-Missing-/NotAsked-Gruppen müssen zum tatsächlichen gepinnten Katalog passen.

Rohpfade sind ausschließlich die fünf bereits festgelegten Studien-/Dateipaare unter `data/raw/ess5-ed3.6`, `ess8-ed2.3`, `ess9-ed3.3`, `ess10-sc-ed3.2`, `ess11-ed4.2`. Die gesamte Datei wird vor Decodierung auf SHA256 und Bytezahl geprüft. Danach müssen **alle DE-Zeilen** die vorab definierte Round-/Edition-Regel bestehen, bevor die Gruppen-API einen Parteiwert semantisch verarbeitet. Numerische Round-Regel: Integer mit optionalem `.0`; Edition: erlaubte Dezimalsyntax und numerische Gleichheit. Ausgewählte43 Fragefelder behalten die kanonische Integer-/Nullbruchteil-Normalisierung, Vote/Partei dieselbe ausdrücklich im Gruppenvertrag gesetzte Regel der reinen Gruppen-API. Unbekannte Syntax wird nicht erraten.

Descriptor-relative Traversierung mit `O_DIRECTORY`/`O_NOFOLLOW`, einschließlich aller absoluten Root-/Librarypfadkomponenten, verhindert Symlinks in Eltern und Blattdateien. Gelesene Dateien müssen regulär sein. Fehler enthalten nur statische Codes; keine Zellen, IDs, Header oder dynamischen Datapfade. Nicht ausgewählte CSV-Strings können lexikalisch den Parser passieren; ein umfassender Blindheitsnachweis oder Betriebssystem-Isolation wird nicht behauptet.

## Private Ausgabe und Fehler

Ein expliziter Serializer akzeptiert ausschließlich die exakten Aggregat-Dataclasses und bekannten Felder der finalen Gruppen-API. Kein generisches `asdict`, `_records`, Antwortdataclass oder Design-/Personenkennungs-Traversieren. Alle Originalgruppen/Fragen bleiben inventarisiert, auch leere Gruppen. Die Varianzstatuswerte `no_design_basis` und bei fehlenden gültigen Antworten `no_valid_responses` sind erlaubt; jede Varianz/SE bleibt null. Promotion zu einem Reviewed-Status scheitert.

Ausgabe ausschließlich `data/local/policy-groups-v21/<fixed-study>/run.json`; lokale Verzeichnisse 0700, Datei 0600. Der Runner akzeptiert bereits vorhandene Verzeichnisse/Dateien nur mit diesen Modi, ohne fremde Dateien umzustellen. Eigene temporäre Datei, file-fsync, atomarer Rename und directory-fsync; vorhandene Ausgabe bekommt vorübergehend einen eigenen privaten Backup-Link. Kontrollierte Fehler vor/während Rename oder nachfolgendem fsync erhalten bzw. restaurieren ältere Bytes. Fremde Dateien mit kollidierendem temporärem Namen werden nicht gelöscht.

**Konkrete Systemgrenze:** Scheitern sowohl der directory-fsync nach Rename als auch die Wiederherstellung, liefert der Runner einen statischen Fehler und keine Receipt. Er behält den eigenen0600-Backup-Link mit den älteren Bytes; der feste `run.json`-Pfad kann dann bereits den neuen privaten Kandidaten enthalten. Ein gleichzeitig dauerhaft fehlschlagendes Dateisystem erlaubt keine garantierte Wiederherstellung an diesem Pfad. Root müsste den privaten Backupzustand gesondert behandeln; nichts wird öffentlich promoted.

Eine erfolgreiche `RunReceipt` enthält ausschließlich Studie, privaten WIP-Status, Start-/End-UTC, Gate-/Manifest-/Vertrags-/Freeze-/Input-/Outputhashes, festen Privatpfad und Exitcode0. Keine Gruppenfälle, Zahlen, Kategorienanteile oder Personen. Persistierte reiche Aggregate bleiben auch unterhalb der Anzeigeheuristik privat und ungeprüft.

## Tatsächliche Prozesse und Tests

Lokale Python-/Textlese-/SHA256-Schritte, eigene Syntaxprüfung mittels `ast.parse`; keine Installation, Git, Auth, HTTP, Server, pnpm oder tatsächliche empirische Ausführung. `PYTHONDONTWRITEBYTECODE=1` verhindert zusätzliche Python-Cacheartefakte. Sämtliche temporären Test-Repositories lagen ausschließlich unter `outputs/loop/policy-group-access-v21/synthetic-repositories/` und wurden durch die Tests bereinigt. Roh-/lokale Dateinamen darin bezeichneten eigens generierte CSV-/Ausgabefakes, keine Kopien tatsächlicher Daten. Öffentliche Dokumentbytes in Fixtures waren gekennzeichnete künstliche Platzhalter mit eigenen Pins; keine Behauptung tatsächlicher Originaldokumentgleichheit.

Vier erhaltene Läufe desselben Testkommandos: `PYTHONDONTWRITEBYTECODE=1 python -m unittest pipeline.tests.test_policy_group_access_v21 -v`.

| Lauf | Ergebnis | Ursache/Fortschritt |
|---|---|---|
|01 |39 Tests;13 Failures,11 Errors; Exit1 | eigener falscher Name `rawBytesOpenedByAuthor` statt tatsächlichem `rawBytesOpenedByThisAuthor` stoppte positive Pfade früh |
|02 |39 Tests;5 Failures,11 Errors; Exit1 | Serializer ließ den tatsächlichen Varianzstatus leerer Gruppen noch nicht zu |
|03 |39/39; Exit0 | beide Integrationsfehler behoben |
|04 |43/43; Exit0 | zusätzlich Promotion-, Kollisions- und doppelte Dateisystemfehlergrenzen geprüft |

Die finalen 43 Tests prüfen reale finale Gruppen-API für alle fünf Studien, explizite Freigabeuntermenge, alte Gates/Runner gesperrt, permissive/fehlende/duplizierte Gates und Pins, tatsächliche Reviewbyte-/Rollenbindung, Source-/UUID-/Regel-/Softwaredrift vor Raw-Read, keine Manifestumleitung zu raw/local/state, Symlinks in Root/öffentlichen/Roh-/Privatpfaden, Bytehash vor Decoder/Parteifeld, sämtliche DE-Metadaten vor Gruppen-API, enge Normalisierung und statische Unknown-/Duplikat-/Headerfehler, keine Identifier-/unselected-cell-Ausgabe,0600/0700, Rollback und Erhaltung fremder temporärer Dateien. Das sind mechanische synthetische Nachweise, keine Daten-, Quellen-, Neutralitäts- oder Methodenabnahme.

Logs samt beiden gezielten synthetischen Debug-Traces und ihren Originalhashes bleiben im eigenen Output. `validation.json` bindet Kommandos, Exitcodes, Testzahlen, Laufzeiten und Loghashes. Kein Testlauf berührte die tatsächlichen `data/raw/` oder `data/local/` des Worktrees.

## Versionen, Pins und offene Abnahmen

Erster technischer Pin am 2026-10-03T14:41:08.546810+00:00; Nachprüfung am2026-10-03T14:56:13.984364+00:00. Die Gruppen-API war beim ersten Lesen WIP SHA256 `0eebf13c207950af4b8dc00bcb775ca286306819b4599da97087ee06d99323d1`, danach durch ihren Autor fertiggestellt und von Root gemeldet. Tatsächlich verifizierter Finalhash: `9b680b07385cefc665a54e583cf4b44f03d1305b2829a724fb9afbd7103284b6`. Diese angekündigte Versionsdrift ist dokumentiert, keine vollständige Pin-Konstanz behauptet. Die übrigen vorab gebundenen öffentlichen Kontext-/Vertrags-/Librarybytes blieben gleich. `policy_report_v2.py` wurde als transitiver Import erkannt und zusätzlich gepinnt; es wird kein Bericht gerendert.

| tatsächliche Runtime-Library | verifizierter SHA256 |
|---|---|
| `pipeline/policy_access_v2.py` | `f2c26b2895f1730a344fde41fee63a960b9ff30f63a68a7beefb82a33e6366db` |
| `pipeline/policy_adapter_v2.py` | `3159243bc6f536359c896e414e8f418955b51e7504e38f3add62a811b0e5500e` |
| `pipeline/policy_analysis_v2.py` | `d7d23c99b84d352f161ea607f575155594ecd1ff365ad89e8f2624b4f9500309` |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/policy_export_v2.py` | `27b225b5975f0c321f08adbfa7ccab4e03dae8421f3987d0e104cf4945d0437a` |
| `pipeline/policy_groups_v21.py` | `9b680b07385cefc665a54e583cf4b44f03d1305b2829a724fb9afbd7103284b6` |
| `pipeline/policy_report_v2.py` | `53d68f23f2bf7c57c95e2bdd55ae0059da4dfe8598bcbd12e2681206a9e4d6ea` |
| `pipeline/policy_group_access_v21.py` | `a662e216c82085ab0a059056715ea880e3d9c63ba8ade9efaff2b5e7881a2f58` |

Offen sind Root-Paketfreeze/Remoteprovenienz, zwei getrennte Übergangsrollen samt ausdrücklich geeigneter Studienuntermenge, tatsächliche spätere gated Raw-/Editionreproduktion, fachliche Annahme und getrennte Ergebnis-/Publikationsentscheidung. Die bereits bekannten Quellenlücken des Gruppenvertrags werden weder gelöst noch umgedeutet. Gleiche Codex-Modellfamilie und gemeinsame mögliche Fehler bleiben bestehen; diese Autorenarbeit ist kein unabhängiges Ersturteil. Keine Veröffentlichung, Websiteänderung, Gruppenfreigabe oder aktuelles Parteiprofil aus dem Auftrag ableiten.

## Eigene Artefakthashes

| Artefakt | SHA256 |
|---|---|
| `pipeline/policy_group_access_v21.py` | `a662e216c82085ab0a059056715ea880e3d9c63ba8ade9efaff2b5e7881a2f58` |
| `pipeline/tests/test_policy_group_access_v21.py` | `27130d07b1f573ef0d0113459a19b66676bb93a84afb7aea1ffeb8896d915c8d` |
| `outputs/loop/policy-group-access-v21/api-pins-before.json` | `0cf476c7f99b182b822d76410ca303850ff7de39e9fc09d016401435a0ed1abd` |
| `outputs/loop/policy-group-access-v21/api-pins-after.json` | `f2184bdd83e3fee28c131390281e07be84fa0a38688ba9bd9328e25af7f99ce5` |
| `outputs/loop/policy-group-access-v21/interface-schema.json` | `a4604c79c2b5b06801a0b720f8fadc495cea374e551e24f79fd7386bdd876f50` |
| `outputs/loop/policy-group-access-v21/validation.json` | `0509d2c34fd1952ede2024cf2337a18d87fbc11c53684b736b20f4a9213a149c` |

Der anschließende eigene `artifact-hashes.json` enthält zusätzlich Bericht- und Log-/Debughashes; der Bericht enthält keinen Selbsthash. Der fertige Bericht wird anschließend unverändert erhalten.
