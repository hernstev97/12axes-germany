# Begrenzte B-/FULL-Laufzeit

Autorenfassung vom 2026-10-03. Neue Dateien sind ausschließlich `pipeline/confirm_runtime.py` und `pipeline/ordinal/reproduce-confirm.R`; Prüfbelege liegen im eigenen Ausgabeordner. Die bestehenden A-/R-, Zugangs-, Schema- und Exportdateien blieben unverändert. Keine echte ESS-Datei, Zuordnung, Antwort, private Phase oder laufende A-Ausgabe wurde gesucht, auf Existenz geprüft oder gelesen. Dies ist ein technisches Autorenpaket, keine Übergangsabnahme oder empirische Freigabe.

## Schnittstelle und Zugriffsfolge

Die festen Aufrufe lauten `python3 -B -m pipeline.confirm_runtime B --label LABEL`, entsprechend `FULL`, und für erfundene Daten `synthetic`. Es gibt keine freien Projekt-, Daten-, Freeze-, Entry- oder Ausgabepfade, keine Skipflags und keine echten Datenoptionen für den synthetischen Aufruf.

`checked_preflight(root, arm)` prüft zunächst ausschließlich den bestehenden öffentlichen Stage-Preflight. Dessen `runtime.reviewedCodeHashes` muss alle sechs ursprünglichen Entwicklungsdateien sowie `stage_access.py`, `confirm_runtime.py` und `confirm.R` enthalten. Alle neun tatsächlichen öffentlichen Codehashes müssen dazu passen. Die unveränderte A-Laufzeit, vier A-R-Quellen und die konkrete `confirm.R`-Fassung sind zusätzlich an ihre festen Quellpins gebunden. Fehlende oder abweichende Wrapperpins stoppen vor einem privaten Prüferaufruf. Erst danach ruft der Wrapper `stage_access.preflight_confirmation` beziehungsweise `preflight_full` auf und vergleicht dessen zurückgegebene öffentliche Bindungen nochmals. Diese Standardprüfer kontrollieren vor ihren privaten Belegen erneut Gate, Tags und öffentliche Codepins.

Privat werden ausschließlich das feste `B.csv` oder `FULL.csv` und `data/modell-v1.json` an `ec_main` übergeben. Das echte Autorisierungsobjekt enthält `decision,arm,wrapper_verified,freeze_sha256`; FULL verlangt zusätzlich den tatsächlichen B-Abschluss und den geprüften verbleibenden Scoreteil. Der Wrapper schreibt es ausschließlich mit Modus 600 in sein eigenes neues Laufverzeichnis. Er übernimmt weder Personen-, Parteien-, Links-rechts- noch Gruppenfelder. Normen und Gruppenberechnungen gehören noch nicht zu dieser Laufzeit; das FULL-Sensitivitätsgewicht wird nur durch den bestehenden Eingabeprüfer gebunden, hier nicht ausgeführt.

Private Läufe erhalten neue 700-Verzeichnisse unter `data/local/empirical-v1/runtime-runs/LABEL`; alle Dateien haben Modus 600. Synthetische Läufe liegen gesondert unter `outputs/loop/r-runtime/LABEL`. Der unveränderte A-Wrapper liefert Runtime-/Baumpins, Quellsnapshots, bereinigte Umgebung, Runtime-Probe, Landlock-Kommando, Ausführung und abschließendes Dateiinventar. HOME bleibt erhalten. Die zwölf benannten Kindprozess-Schreibrechte sind auf das eigene Laufverzeichnis und den erforderlichen Schreibzugriff auf `/dev/null` begrenzt.

Vor und nach R werden tatsächliche öffentliche Codehashes und Runtimepins geprüft; privat zusätzlich die vollständige Stage-Autorisierung und Eingabepins. Die tatsächlich konsumierte generierte Entrydatei und Autorisierungs-JSON werden vor und nach R eigens gehasht. Das private Runreceipt ist `r-confirm-runtime-run-v1`, enthält diese Pins, Befehle, Umgebung und das tatsächliche Inventar und bleibt privat. Der Wrapper gibt dort nur einen festen Fertigtoken aus; Bibliotheksausnahmen und Werte gelangen nicht in die Terminalausgabe. Es gibt weder RDS-Ausgabe noch automatische öffentliche Aggregatekopie.

## Tatsächliche technische Ausführung

Der neue öffentliche R-Entry erzeugt seine erfundenen neun Items selbst. Er benötigt keinen ausgeschlossenen Autorenfixturepfad: 192 PSUs, vier Strata, 40 Fälle pro PSU und vier PSUs ohne vollständige Antworten; gleiche vorab festgelegte Kategorien, RNG-Regel und dokumentierte synthetische Seeds. M2/M3, schwaches H, eingefrorenes Z/F trotz schwachem oder starkem H sowie FULL ohne Wiederherstellung des in B unterdrückten H wurden tatsächlich berechnet. Instrumentierte unveränderte Fithelper bestätigen genau drei EFA-Läufe mit der eingefrorenen Faktorzahl und genau ein gemeinsames eingefrorenes CFA-Modell. Die eigentliche File-API läuft gegen eine eigene erfundene öffentliche A-Referenz unter dem frischen synthetischen Ausgabeordner; niemals gegen das wirkliche öffentliche A-Ziel.

`python3 -B -m pipeline.confirm_runtime synthetic --label confirm-runtime-author-001` bestand mit Runtime-Probe 0, Stageexit 0 und 52/52 R-Prüfungen. Nach der kleinen Ergänzung des Entry-/Autorisierungsdateipins wurde der endgültige Wrapper einmal neu unter `confirm-runtime-author-002` ausgeführt: ebenfalls Probe 0, Exit 0 und 52/52 Prüfungen. Beide Originalreceipts bleiben unverändert. Die sechs synthetischen M2-/M3-/Scoreteil-/FULL-Aggregate stimmen zwischen den Läufen byteweise überein. Das ist Reproduktion unter denselben Parametern und derselben Umgebung, keine unabhängige wissenschaftliche Bestätigung.

Die 51 veröffentlichten Modellschwellen und ihre Labels wurden gegen die tatsächlichen Punkte eines gesondert erneut gefitteten gemeinsamen Modells geprüft. Die Differenz zu den beobachteten Schwellen wird nicht als exakt null vorausgesetzt: Die tatsächliche maximale Differenz war `2.5260874503274522e-08`; der ausgewiesene Wert stimmt mit der direkten Nachrechnung überein. Die File-API erzeugte ausschließlich die beiden erwarteten 600-JSON-Dateien, verweigerte Überschreibung und verlangte den B-Abschluss vor FULL-Eingaben.

`python3 -B -m outputs.loop.resume-confirm-runtime-author.tests` bestand zuletzt mit 8/8 gezielten Mocktests. Sie prüfen Gates und sämtliche Wrapperpinfehler vor privaten Helferaufrufen, den richtigen Standardprüfer pro Arm, Bindungsdrift, ungültige Stages/Pfade, neue 700-/600-Ausgaben ohne Aliasse oder Überschreibung sowie veränderte konsumierte Entry-/Autorisierungsbytes. Die Mocktests lesen keine echten privaten Stagedateien. Der erste Treiberaufruf scheiterte an einer Klammerung im neuen eigenen Testtreiber; nach Korrektur bestanden die Tests. `python3 -B -m pipeline.confirm_runtime --help` ist ebenfalls ausführbar. Keine Installation, Gitmutation, pnpm- oder Claude-Ausführung erfolgte.

## Pins und Grenzen

| Finale Datei oder Ausführung | SHA256 |
| --- | --- |
| `pipeline/confirm_runtime.py` | `9399e29e4eda5a4faf2f46dc9f3f2fd6a3c74f2ceefa572c2caeab5b94844ba5` |
| `pipeline/ordinal/reproduce-confirm.R` | `be801acf5e25a36e820277d5b048757fbd691456d2447e1fef65bc1566b0cb98` |
| unveränderte `pipeline/ordinal/confirm.R` | `e7c8d04d8010c456c5db6d9902353a37786737b201cf9a160d082f40a84bddad` |
| ursprünglicher synthetischer Run 001, Receipt | `3e9cfe96688c246a26152568ec8a662a8a66925689a1b0d91a28781249e4fe3e` |
| finaler synthetischer Run 002, Receipt | `0c98f68092e6e160a231ce91fdb5bd69064f79cecdff1ee148a7203d96fe5bdb` |
| identischer tatsächlicher R-Prüfbeleg beider Läufe | `b4a3cfda3201a9c414fc1d139f3750d07f2c6a7ee44b93152ae6846e7e5d38f3` |

`outputs/loop/resume-confirm-runtime-author/execution-evidence.json` hält tatsächliche Zeitpunkte, Pins, Runtime-Ergebnisse und Gleichheitsbeobachtungen fest. `pins-current.json`, Testlog und Testresultat liegen daneben. Die beiden Laufreceipts enthalten Quellsnapshots, echte Paket-/Umgebungspins und vollständige Inventare.

Gate- und Runreceipts sind auf dem gemeinsamen Dateisystem veränderbar. Die Prüfungen sind keine atomare Transaktion und keine unverfälschbare Autorisierung; gleichzeitige Änderungen bleiben möglich. Landlock begrenzt die zwölf benannten Schreibrechte des Kindes und isoliert weder Lesen, Netzwerk, Geräte, Supervisor noch andere Agents. Die getrennten Codex-Rollen gehören derselben Modellfamilie an und können gemeinsame Fehler haben. Es gab keine echte B-/FULL-Ausführung, methodische Übergangsabnahme, empirische Akzeptanz, politische Fairnessabnahme, menschliche Verständnistest- oder Releasefreigabe.
