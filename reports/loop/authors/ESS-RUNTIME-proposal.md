# Reproduzierbare R-Läufe vor dem A-Zugriff

Autorenfassung vom 3. Oktober 2026. Technische synthetische Prüfung, keine Methodenübergangsprüfung oder empirische Freigabe. Neue Forschungsdateien sind ausschließlich `pipeline/r_runtime.py`, `pipeline/ordinal/reproduce-support.R` und dieser Bericht. Eigene Testbelege liegen unter `outputs/loop/resume-runtime-author/`; die ausdrücklich zusätzlich autorisierten finalen Läufe unter `outputs/loop/r-runtime/runtime-author-*`. Keine echte A-Datei, Assignment-Datei, ESS-Antwort, Personenkennung oder Rohdatenzeile gesucht, gelesen oder ausgeführt. Keine Recherche, Installation, Gitmutation oder `pnpm`-Ausführung. Der Koordinator führt die Repository-Prüfung aus.

## Aufruf und feste Schnittstellen

Vom bestätigten Worktree aus:

```sh
python pipeline/r_runtime.py synthetic --stage support --label reviewer-methods-support-001
python pipeline/r_runtime.py synthetic --stage development --label reviewer-methods-development-001
```

Jeder freie ASCII-Label legt genau ein neues `0700`-Verzeichnis unter `outputs/loop/r-runtime/` an. Ein vorhandenes Label stoppt. Es gibt keine frei wählbaren R-Einstiegspunkte, Shellbefehle, Installer, Ausgabe-Wurzeln oder Gate-Skipflags. Der synthetische Entwicklungseinstieg erzeugt seinen erfundenen Frame selbst und ruft dieselbe feste `ed_main`-/`ed_run_file`-Schnittstelle auf. Die vollständige Rezeptur liegt vor Ausführung als `development-entry.R` im Laufverzeichnis.

Für einen später tatsächlich freigegebenen Lauf existiert `python pipeline/r_runtime.py development-a --label <neues-label>`. Dieser Produktionsaufruf wurde hier nicht ausgeführt. Er akzeptiert ausschließlich `data/local/empirical-v1/A.csv`; seine neuen Ergebnisse liegen ausschließlich in `data/local/empirical-v1/runtime-runs/<label>/`. Kein R-Einstieg darf über die CLI ausgetauscht werden.

## Gate vor privaten Eingaben

Der Produktionsweg prüft zunächst den öffentlichen Gate-Pfad und dessen Artefaktpfade auf private Ziele und Symlinks. Danach ruft er das vorhandene `empirical_access.gate(root)` auf, einschließlich der beiden Reviewrollen, Artefakthashes, tatsächlichen lokalen und Remote-Tags und Python-Version. Anschließend prüft er **alle** `runtime.reviewedCodeHashes`. Er verlangt mindestens Wrapper, Accesscode, `develop.R`, `develop-config.R`, `adapter_v2.R` und `support.R`. Erst danach liest er einen privaten Beleg oder die A-Datei.

Das öffentliche Gate braucht `runtime.schema="r-runtime-v1"`, den unveränderten `sourceSha256`, die feste `privateReceiptPath="data/local/empirical-v1/runtime-input-receipt.json"` und `reviewedCodeHashes`. Der private Accessbeleg braucht `schema="r-runtime-input-v1"`, `sourceSha256`, `gateSha256`, `empiricalAccessSha256` sowie `assignment` und `developmentInput`, jeweils mit festem relativen Pfad und SHA256. Assignment-/A-Hashes und der Hash dieses ganzen Belegs bleiben privat. Der Accessprozess erzeugt diesen Beleg; ein Runtime-CLI-Flag erzeugt keine Abnahme.

Der Wrapper prüft alle Pfadkomponenten auf Symlinks, `0700`-Eltern und `0600`-Eingabedateien. Er hasht die gebundene Assignment-Datei und prüft deren ursprünglichen Quellhash und Seed vor dem A-Hash. Er liest keinen Rohdatensatz. Unmittelbar vor R und nach dem Lauf wiederholt er Gate, Remote-/Code- und Eingabebelege. Koordinatorbelege sind auf dem gemeinsamen Dateisystem veränderbar. Diese Checks beweisen keine kryptographische Vertrauenskette und schließen konkurrierende Änderungen zwischen Prüf- und Lesezeitpunkt nicht aus.

## Runtime und Reproduktion

Der vorhandene lokale Rscript ist mit SHA256 `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec` gebunden. Der komplette bestehende R-Prefix bindet Dateien und interne Symlinkziele mit Baumhash `3bc6b04077406586ef84c901beff6d93d04db3ea74160ad1ae45f4e6eba3b2e4`; lavaan und semTools außerhalb des Prefix besitzen eigene Paketbaum-Pins. Die Hashalgorithmen stehen im Wrapper. Vor und nach jedem Lauf werden diese Bindungen geprüft. Der tatsächliche R-Probe prüft R 4.5.3, lavaan 0.7.2, pbivnorm 0.6.0 und semTools 0.5.9 sowie Versionen und Fundorte der vollständigen benannten R-Paketabhängigkeiten. Diese lokale Runtime wird vorausgesetzt; es gibt weder Installation noch Abhängigkeit von früheren ignorierten Autorlaunchern.

`HOME` bleibt unverändert. R-/Conda-/Mamba-Vorgaben und fremde Loader-Vorgaben werden bereinigt. TZ ist UTC, Locale C.UTF-8, BLAS-/OMP-Threads sind eins. Temp, Cache, XDG und R-Sentinels liegen im eigenen Laufordner. Python-Importe erzeugen dort außerhalb keine Bytecode-Caches. Je Lauf entstehen getrennte `start.json` und `receipt.json`, Runtime-Probe, Logs, UTC-Zeiten und Hashinventar; die einzeln fest benannten öffentlichen Quelldateien werden vor Ausführung unter `source-snapshot/` gesichert. Keine ganzen Verzeichniskopien.

`setpriv`/Landlock behandelt dieselben zwölf Child-Schreibrechte wie der erhaltene Launcher und erlaubt sie ausschließlich im Laufordner, zusätzlich `write-file` auf `/dev/null`. Der tatsächlich ausgeführte Probe verweigert die Anlage einer Datei außerhalb des eigenen Laufordners. Er prüft nicht jede der zwölf Operationen einzeln. Vollständige Lese-, Netzwerk-, Geräte-, Supervisor- oder Agent-Isolation wird nicht behauptet. `umask 077` und Nachprüfung halten Laufdateien auf `0600`.

Der dünne Supporteinstieg lädt das unveränderte, SHA-gepinnte `test-support.R` und ersetzt genau dessen einen historischen Ausgabe-Pfadguard. Keine wissenschaftliche Expression, Konstante, Toleranz oder Testreihenfolge wird geändert. Das intern vorangestellte `test-fixed-v2-` wählt `adapter_v2` und festes `W=I`. Der wissenschaftliche Hauptweg bleibt ULS auf den Momenten mit beobachtetem Jacobian. Native DWLS-Rechnungen bleiben begrenzte diagnostische Oracles.

## Tatsächlich ausgeführte Checks

| Beleg | Tatsächlicher Befund |
| --- | --- |
| `outputs/loop/r-runtime/runtime-author-support-final-003/receipt.json` | Exit 0; 54/54 unveränderte Supportchecks, keine Warnung; UTC 10:54:18–10:54:30. Quelle, feste Metrik und Hashpins geprüft. |
| `outputs/loop/r-runtime/runtime-author-development-final-002/receipt.json` | Exit 0; vollständiger generischer `ed_main`-Dateipfad. Erfundenes M3 mit 7680 Fällen, 192 PSUs, vier Strata, vier Null-Domänen-PSUs und Seed 2026100325; erwarteter M3-Kandidat H/Z/F. UTC 10:55:56–10:56:06. |
| `outputs/loop/resume-runtime-author/test-runtime-004.log` | 13/13 erfundene Receipt-/Pfad-/Reihenfolgechecks. Gatefehler, Codeänderung, privates Gateziel, falscher Modus, Symlink, Receipt-/Assignmentbindung und A-Hash stoppen; Label/Umgebung geprüft. Das Gate einschließlich Remoteprüfung ist hier gemockt. |
| `outputs/loop/resume-runtime-author/runtime-evidence-001.json` und `runtime-evidence-002.json` | Je 12/12 eng benannte Prüfungen von Quelle, Modus, eigener Schreibsperre, erfolgreichem synthetischem Pfad und festen Statuscodes. Die numerischen Ergebnisse sind keine weiteren unabhängigen Oracles. |
| `outputs/loop/resume-runtime-author/no-overwrite-001.log` | Echter Wiederaufruf des vorhandenen Supportlabels stoppt mit Exit 2 und `R_RUNTIME_DO_NOT_OVERWRITE`. |

Frühere eigene Laufordner bleiben unverändert. Die beiden ersten Python-Harnessaufrufe waren nicht bestanden: direkter Skriptstart fand das Paket `pipeline` nicht; unittest-Discovery fand wegen des Bindestrichs im Dateinamen keine Tests. Der dokumentierte `runpy`-Aufruf führt die 13 Tests tatsächlich aus. Frühere erfolgreiche Wrapperläufe hatten bereits Hashreceipts, aber noch keine einzeln archivierten Quelldateien. Die finalen neutralen Läufe enthalten diese Archive.

Finaler Wrapper-SHA256: `40168392ac69960d2b532f721aaaca4abc82317f8304f7145056537d8a901fce`. Dünner Supporteinstieg: `f7a11f2c2ed665e508402606686ea4d9c7e97c2ac9f9a49af555da3738e56b35`. Der finale Entwicklungslauf bindet `develop.R` mit `a263f93fde5d71dd169a011faf7319f10d5d578c79f87b0894756be762a9bac8` und `develop-config.R` mit `0ad5794876b98b9a99cb3567e2d04112e241341d99597d7a011f9095c8a65a4a`.

`run_r.py`, `test-support.R`, `support.R` und `adapter_v2.R` bleiben erhalten. Keine reale Gate-/Remote-Abnahme, ESS-Analyse, B-/Vergleichszugriffe, Abdeckungsstudie oder wissenschaftliche Freigabe wurde durch diese Autorenarbeit ausgeführt. Die neuen Runtimequellen brauchen den frischen Methodenübergangsreview. Die öffentliche Quellen-/Konstruktprüfung bleibt getrennt.
