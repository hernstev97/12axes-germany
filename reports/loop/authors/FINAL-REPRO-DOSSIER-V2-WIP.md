# FINAL-REPRO-DOSSIER-V2 — Autoren-Erstbericht

3. Oktober 2026. Begrenzte Dokumentationsvorbereitung, **WIP**, kein neuer Forschungs-, Rechen- oder Reviewauftrag. Zwei praktische Dokumente sind fertig: lokale Reproduktionsanleitung und Checkliste für die spätere von Steven veranlasste Claude-Schlusskontrolle. Keine tatsächliche Claude-Beauftragung oder -Verbindung.

Geschrieben wurden ausschließlich `docs/reproduktion-life93-v2.md`, `docs/claude-schlusskontrolle-v2.md`, dieser neue Erstbericht und eigene ignorierte Nachweise unter `outputs/loop/final-repro-dossier/`. Keine vorhandenen Forschungs-, Code-, State-, Handbuch-, Gate-, Manifest- oder anderen Berichtdateien wurden bearbeitet.

## Stand und nachträglich mitgeteilter Gruppenentscheid

Die Dokumente tragen Fassung 0.1 und Stand `2026-10-03T15:56:20.289903+00:00`. Zunächst galt der Gruppenexportguard als gezielt nachzuprüfen. Root meldete während dieses Auftrags den abgeschlossenen Methodenfix GR21-M-001, sein tatsächliches Lesen des vollständigen Berichts, die 64 öffentlichen/3 privaten Pinprüfungen und die neue öffentliche Exportentscheidung. Die beiden Dokumente wurden **vor Abschluss** auf diesen neuen Stand gebracht.

Gelesener Gruppenentscheid: `reports/loop/policy-group-v21-export-decisions.json`, SHA256 `544f31f83cac1e258ed13559c04373430a5ac0d792c4380421a32bb623ef42bc`, UTC `2026-10-03T15:54:40.395473+00:00`. Er bindet drei öffentliche Dateien und 63 ausdrückliche Frage-Gruppen-Paare, verteilt 21/30/12. Die vollständigen 8/9/9 Gruppenbestände bleiben erhalten, die übrigen Referenzen null. Das ursprüngliche Quellenurteil wurde laut Entscheid wegen unveränderter Kandidaten/Quellen/Schwellen begrenzt weitergenutzt; es wird nicht als neue Erstbewertung der Methodenrunde ausgegeben.

Die Dokumente behaupten keine fertige Gruppenanzeige oder menschliche Abnahme. Root darf die beiden Arbeitsdokumente später datiert um tatsächliche Gruppenanzeige-/Reproduktions-/Abnahmestände ergänzen. Dieser Autoren-Erstbericht bleibt als Beleg der hier beschriebenen Fassung erhalten.

## Inhalt der Reproduktionsanleitung

Die Anleitung unterscheidet eingefrorene Planartefakte, tatsächliche Bibliotheksläufe, noch nicht ausgeführte positive Fresh-checkout-CLI-Reproduktion und getrennte öffentliche Exportentscheidungen. v2/analyseplan-v2 und v2.1/analyseplan-v2.1 sind vor ihren jeweiligen Zugriffen gebunden. Historische v1-A/B-Einsicht und die angehaltene Altfolge bleiben sichtbar; bekannte Antworten werden nicht in unberührte Bestätigung umbenannt.

Die benötigten Eingaben werden durch Originalmanifestpfade und ihre Hashfelder beschrieben, ohne große Hash-/Begründungstabellen zu kopieren. Alle 36 externen öffentlichen `outputs/`-Einträge des Gruppenmanifests sind ignorierte lokale Voraussetzungen. Die fünf privaten CSV-Pfade stehen ausschließlich als deklarierte Vertragsmetadaten in der Anleitung; ich habe diese Dateien und Verzeichnisse nicht geöffnet oder aufgezählt und dort keine Dateimetadaten abgefragt. Für Gruppen werden nur ESS5/8/9 verarbeitet. Die Anleitung erklärt, dass ein Clone weder diese privaten Dateien noch die öffentlichen ignorierten Caches automatisch enthält.

Private Ausgaben sind getrennt `data/local/policy-v2` und `data/local/policy-groups-v21`, Verzeichnisse `0700`, Dateien `0600`. Die aktuellen Wrapper verweigern vorhandene `run.json`-Dateien; die Anleitung nutzt dafür einen separaten Checkout und erhält historische Outputs. Keine Lösch-/Umbenennungs-/Überschreibumgehung. Die tatsächliche CLI prüft lokale und Remoteplantags mit Git und benötigt beim Datenlauf Netzwerkzugang zum bestehenden `origin`; `--help` endet davor. Ich habe Git und Netzwerk nicht ausgeführt.

Die Reproduktionsbefehle sind eine **künftige Nutzeranleitung**, keine hier gestarteten Datenläufe. Auch `scripts/build-policy-v2-report.py --check` ist nur als späterer read-only Bytevergleich beschrieben und wurde in diesem Auftrag nicht ausgeführt. Seine zusätzlichen 30 Katalog-Quellencaches werden gesondert genannt. Ein erfolgreicher Darstellungbuild wäre keine Rohreproduktion.

Die öffentliche Einzelentscheidung mit 43 Inventarfragen, acht Rubriken, 42 historischen Referenzen und cttresa=null bleibt getrennt vom neuen Gruppenentscheid. Private Kandidaten werden nicht selbständig zu öffentlichen Referenzen. Kandidatenstatus, synthetische Tests oder sichere Receipts ersetzen keine tatsächlichen Ergebnis-/Manifest-/Reportpins und Rootentscheidung.

## Inhalt der Claude-Checkliste

Die Checkliste nennt prüfbare Fragen zu Belegen, Reproduktionsumfang, Nennern/Missing, Originalcodes, Gewichtssensitivitäten und unterschiedlichen Ratio-Scopes. Sie trennt Einzelangaben von latenten oder formativen Gesamtformen und historische Wählergruppen von aktuellen Parteienpositionen. Themen-/Binnenlücken, gleiche Belegstandards und faire Benennungen bleiben kontrollierbar.

B1–B12 Demokratie im Allgemeinen, B13–B24-Auslassung, B12/keydec im Originalblock sowie B25/ausgelassene B26–B29 und unbelegter operativer CAWI-Nachlauf sind konkrete Kontrollpunkte. Zeit-/Modus-/Kontextübertragung, ESS8-München, bekannte v1-A/B und v2-Einzelreferenzen werden nicht als unabhängige Bestätigung ausgegeben. Die Codex-Erstrollen gehören derselben Modellfamilie an; Übereinstimmung ist kein Neutralitätsnachweis.

Offen bleiben fünf tatsächliche menschliche Verständnistests mit geeigneter UI-/Referenz-/Zeigeskriptbindung und Einwilligung, eigene Gruppenverständnisergänzung, Designzustimmung, sichtbarer Tastaturfokus, echter 200%-Zoom, Claude-Schlusskontrolle, konkrete Rechte-/kommerzielle Nutzungsprüfung und persönlicher Release. Keine Kontaktaufnahme oder simulierte menschliche Ergebnisse. Dokumentations- und Datenlizenzen werden getrennt behandelt.

## Tatsächlich gelesener Kontext

- Aktuelles `AGENTS.md`, Breitennachtrag und `docs/project.md`; einschlägige bestehende `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/entscheidungen.md`, frühere Methoden-/Belegregisterkenntnis und aktuelle `docs/lizenzen.md`. `unslop/SKILL.md` wurde vor Schreiben erneut gelesen und angewandt.
- Aktueller kurzer Handoff und ausgewählte Status-/Plan-/Gruppen-/Humanfelder von `reports/loop/state.json`, ausdrücklich als erlaubter Autorenkontext. Alte historische Einzelstatusfelder wurden nicht über die konkreten späteren Exportentscheidungen gestellt.
- `scripts/run-policy-v2.py`, `scripts/run-policy-groups-v21.py`, einschlägige bestehende Accessguard-Codeabschnitte, `pipeline/README.md` und `data/reference-v2/README.md`. Das Pipeline-README enthält frühen historischen Vorbereitungsstand; die neuen Dokumente binden die aktuellen separaten v2-Wege.
- Öffentliche v2-/v2.1-Manifeste, Freezes, Gates und Run-/Accessreceipts; der v2-Plantagbeleg, aktueller öffentlicher Analysevertrag und dessen deklarierte fünf Inputpfade; Manifestmetadaten der gezielten Präsentations- und Gruppenergebnisrunde. Andere Reviewerberichte wurden in diesem Auftrag nicht geöffnet oder überprüft.
- Öffentlicher Einzelentscheid und öffentliche Einzeldateibytes als Pins; der neu ausdrücklich erlaubte Gruppenentscheid und die drei öffentlichen Gruppendateien zur Schema-/Status-/Inventarmetadatenkenntnis und Bytebindung. Keine Bewertung oder Neuberechnung ihrer tatsächlichen Anteile.

Private Pfad-/Pinreferenzen aus erlaubten Metadaten wurden nie als Dateizugriff benutzt. Externe Cachepfade/Hashes wurden aus dem öffentlichen Manifest gezählt und beschrieben; ich habe diese 36 Cachedateien nicht erneut reproduziert oder alle ihre Originalinhalte überprüft. Root dokumentiert seine tatsächlichen vorgelagerten Byte-/Ergebnisprüfungen; ich erkläre sie nicht zu meinen eigenen Reviews.

## Eigene Checks und Prozesse

Alle gestarteten Kindprozesse sind beendet. `PYTHONDONTWRITEBYTECODE=1` war gesetzt. Logs und genaue Aufruf-/PID-/UTC-/Exitmetadaten liegen in den eigenen Outputs.

| Aufruf | PID | UTC-Start am 2026-10-03 | UTC-Ende | Exitcode |
| --- | --- | --- | --- | --- |
| `python --version` | 3725599 | 15:56:20.148567 | 15:56:20.149978 | 0 |
| `python scripts/run-policy-v2.py --help` | 3725600 | 15:56:20.150092 | 15:56:20.219038 | 0 |
| `python scripts/run-policy-groups-v21.py --help` | 3725601 | 15:56:20.219175 | 15:56:20.289903 | 0 |

Beobachtete Pythonversion: 3.14.7. Beide Hilfeausgaben zeigen die erwarteten Studienoptionen. Sie belegen Parser-/Import-/Hilfefunktion, keinen tatsächlichen Git-/Gate-/Input-/Privatlauf. Es wurde kein Rerun und kein neuer Fresh-checkout-Versuch gestartet.

Eine eigene reine Dokumentationsprüfung endete mit tatsächlichem Tool-Exitcode 0: PID 3746022, UTC `2026-10-03T15:59:26.947826+00:00`. Geprüft wurden balancierte Codefences, vorhandene lokale Beleglinks außerhalb von Raw/Local/Reviewpfaden, die neuen 63-Paar-/42-Einzel-/43-Fragen- und offenen Human-/200%-Angaben sowie die Übereinstimmung der fünf **Metadatenpfade** mit dem öffentlichen Vertrag und der 36 externen Einträge mit dem Manifest. Kein Rohdateizugriff. Nachweis: `documentation-check.json`.

36 vorab erfasste erlaubte Bestandsartefakte sind im Vergleich `before-pins.json`/`after-pins.json` bytegleich, zuletzt UTC `2026-10-03T15:59:40.271628+00:00`. Die separat als Snapshot erfassten Rootdateien `state.json` und `handoff.md` änderten sich während der Arbeit. Diese laufenden Kontextdateien werden ausdrücklich **nicht** als unverändert bezeichnet. Root lieferte den neuen Gruppenentscheid zusätzlich direkt; beide Dokumente beziehen sich auf dessen tatsächliche gepinnte Bytes.

## Pins dieser Fassung

- `docs/reproduktion-life93-v2.md`: SHA256 `d2fcd882085cccac2c5a3fcc0f192b421c54f8b8bf07f4a8e8b553e428151efe`.
- `docs/claude-schlusskontrolle-v2.md`: SHA256 `e7892c5eeacb3f8a5c0be43310496739afe390284b0d8cfce8204fde97dcb67f`.

Der Hash dieses Autoren-Erstberichts folgt separat an Root; kein selbstreferenzieller Hash. Geschützte ursprüngliche Gruppen-/technische Report-Erstberichte und ihre Bibliotheken wurden nicht geändert.

Nicht durchgeführt: positive Fresh-checkout-CLI, neue Zahlenrechnung, Raw-/Local-/Header-/Personenzugriff, neuer Quellenabruf, unabhängige Reviewprüfung, vollständiger Cache-Neuaufbau, Git-/Remoteprüfung, Netzwerk/Auth/Claude, Server/Browser, Installation, pnpm, Kontakt oder Release. Keine davon wird als bestanden ausgegeben. Der ausdrücklich begrenzte Dokumentationsauftrag umfasst diese beiden Hilfetests und eigene Text-/Linkprüfungen, keinen allgemeinen technischen oder wissenschaftlichen Abschlusscheck.
