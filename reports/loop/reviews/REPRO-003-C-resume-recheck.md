# REPRO-003-C/v2: gezielte Nachprüfung RC-R01 nach Fortsetzung

2026-10-03. Reviewer `/root/resume_c_recheck`, frischer begrenzter Prüfauftrag. RC-R01 ist im geprüften Umfang `BESTANDEN` nachgeprüft. Zwei eigene neue Minimalnachbauten laden die offiziellen Dokumente tatsächlich herunter und erzeugen bytegleich die historische Annotation. Zwei echte HTTP-404-Fälle protokollieren den fehlgeschlagenen Versuch vollständig. Es gibt keine neuen Findings.

Das Urteil gilt für Dokumentationsreproduktion und Fehlerprovenienz. Empirische oder methodische Validierung, Edition-4.2-Abgleich und Veröffentlichungsfreigabe sind `NICHT_GEPRÜFT`.

## Prüffassung und Auftrag

Arbeitsfassung war ausschließlich `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch `research/life-93-night-20261003`, HEAD zu Beginn `610543fa34d3a9772403c8e38f34f23645d692d8`. Gemeinsame Änderungen des Koordinators wurden erhalten. Der vollständige erhaltene Auftrag steht unter `outputs/loop/resume-c-review/task-received.txt`, der eigene Vorabplan unter `plan-before-tests.json`. Er wurde vor den Tests geschrieben, SHA-256 `3f0637f9208dae40f391c1f3818223ff3f482979d950acdc1c7a3dbebb52b6da`.

Geprüft wurde ausschließlich das eingefrorene Paket `reports/loop/packages/REPRO-003-C/v2/manifest.json`, SHA-256 `c3fd8f2bf210b62183c14739b91a3dd0b8ff809baad3d8186173f88bebfebab7`. Sein `codeCommit` ist `204ae72b446f9515832783f085d37eefd64aab54`. Die 22 Dateien wurden aus `v2/files/` geprüft, die 63 zusätzlichen `sourceInputs` an ihren gebundenen Pfaden. Sämtliche 85 Pins und der Manifesthash stimmten vor und nach den Läufen. Aktuell vom Koordinator bearbeitete Anweisungsdateien wurden nicht als gefrorene Fachartefakte behandelt.

| Eingabe | SHA-256 |
| --- | --- |
| Gefrorener Wrapper `pipeline/reproduce_c_annotation.py` | `8f8d9cbba76c1ee37f2e967321493265e33eb4445d1444f3a519180ea4dcc1d2` |
| Gefrorener Builder `pipeline/annotations/c_builder_v2.py` | `031aff14c42da05f6a57a78fef89ad8b5ba8220fc493cb65af1777a31d57c584` |
| Geometriehelper `pipeline/annotations/source_geometry.py` | `61fb05cd5d0e6b637346692267f2a4c44bb9cb07567fa5c8cc03a61e42a6170f` |
| Öffentlicher Dokumentinventar-CSV | `8c73adb8b361db2992f5fe9e321e0c5b978afdc41ba22c1cbb471f92e60057c1` |
| Inventarprovenienz | `533a12c517ac49f869aea1fbc09dc86e3c1dfe7ef9bc7b05018b5a49ba753aa6` |
| Historische Zielannotation | `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e` |
| Gefrorener Nachprüfauftrag | `59d070fb6854a3e1d465dde6fb603dc3366608145c9db87721b3b938bcae136c` |

Die vollständigen Pinlisten stehen im eigenen Output unter `inputhashes-before.json`, SHA-256 `fb27ca102c6c5ed1a914a33f253a2989e4d3831ebfdfd33dce42d5ef614fd0bd`, und `inputhashes-after.json`, SHA-256 `823405537bd0ec7ffdb2970a1a5c7326bbd971cd314e1dc79ed1f7ee16e30315`.

Gelesen wurden die aktuellen Arbeitsanweisungen und der Fortsetzungsnachtrag, der notwendige Projekt-/Regel-/Plan-/Lizenzkontext, der gefrorene Wrapper, die betroffenen Builderpfade sowie der ursprüngliche Befund RC-R01 und die gebundene Autorkorrektur einschließlich Diff und Vorabplan. Keine anderen aktuellen Reviewerurteile oder Loopfindings wurden gelesen. Die historische Vorgabe zweier Nachberichte in v2 ist durch den Fortsetzungsauftrag für normale Pakete abgelöst. Dieser Bericht erfüllt den Auftrag eines passenden Reviewers, ohne frühere Berichte umzuschreiben.

## Tatsächliche Ausführung

Alle neuen Dateien liegen unter `outputs/loop/resume-c-review/`; einzig dieser neue Bericht liegt außerhalb. Jede neue Kopie enthielt anfangs genau die fünf benötigten öffentlichen Dateien aus dem Freeze: Wrapper, Builder, Geometriehelper, Inventar und Provenienz. Keine historischen PDFs, Bbox-Dateien, Annotationen oder Autoren-Caches wurden in die Kopien übernommen.

Der eigene Harness `review_runner.py`, SHA-256 `8985e8fed7a2cd50d2cb292abb5cfe263b5534af580177df5fac8598c5a4117d`, wurde tatsächlich so gestartet:

```sh
python outputs/loop/resume-c-review/review_runner.py
```

Explizites Arbeitsverzeichnis war die oben genannte Arbeitsfassung. Die Toolausführung lief als Sitzung `60217` und endete mit Exit 0. Sie startete sechs wirkliche Kindprozesse, jeweils mit explizitem `cwd` der eigenen Kopie und `PYTHONDONTWRITEBYTECODE=1`:

```sh
python pipeline/reproduce_c_annotation.py --output-dir outputs/public-reproduction/run
```

`commands/<name>.json` enthält je Kindprozess tatsächliches Python-Executable, vollständige Argumentliste, Arbeitsverzeichnis, Beginn/Ende, Exit, stdout und stderr. `commands/<name>-copy.json` bindet die ursprünglichen fünf Kopiedateien; `<name>-delta.json` bindet jede Gegenfallmutation mit Vorher-/Nachherhash und exaktem Literal. Der Harness-Exit 0 bedeutet, dass die erwarteten begrenzten Beobachtungen vorlagen. Er macht die vier absichtlichen Kindfehler nicht zu erfolgreichen Nachbauten.

| Eigener Lauf | Kind-Exit | Tatsächliche Beobachtung |
| --- | --- | --- |
| `fresh1` | 0 | Drei neue offizielle HTTP-200-Downloads, alle Pins richtig; historische Annotation exakt nachgebaut |
| `fresh2` | 0 | Neue getrennte Fünfdatei-Kopie, erneut drei neue HTTP-200-Downloads; gleicher exakter Nachbau |
| `first404` | 1 | Nur die erste URL auf einen fehlenden PDF-Namen desselben offiziellen Hosts geändert; HTTP 404, vollständiger Fehlversuch, keine Annotation und keine PDF-Datei |
| `second404` | 1 | Nur die zweite URL geändert; erster Download bleibt als richtiger HTTP-200-/Pin-Erfolg erhalten, danach vollständiger HTTP-404-Versuch; keine Annotation |
| `wrongpin` | 1 | Nur der erste erwartete PDF-Pin durch 64 Nullen ersetzt; echter offizieller Download mit HTTP 200, tatsächliche Bytezahl/Hash erhalten, Pinfehler und keine Annotation |
| `unsupported-url` | 1 | Nur erste URL auf nicht unterstütztes Protokoll geändert; tatsächlicher lokaler `URLError`, kein Remoteabruf behauptet; unbekannte HTTP-/finale URL-/Byte-/Hashwerte bleiben `null`, keine Annotation |

Die sechs Positivdownloads fanden am 2026-10-03 zwischen `09:25:32.527559+00:00` und `09:25:35.790098+00:00` statt. Die drei tatsächlichen Originalquellen und geprüften Hashes sind:

- [Deutscher Fragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf): 1.304.009 Bytes, `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`.
- [Deutsches Listenheft](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf): 2.210.799 Bytes, `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca`.
- [Codebook 4.1](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf): 2.162.997 Bytes, `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35`.

Jeder Positivversuch trägt versuchte/finale URL, HTTP 200, Beginn/Ende, erwarteten/erhaltenen Hash, Bytezahl, `completeFileWritten: true` und `BESTANDEN_PIN`. Beide Annotationen haben 3.418.839 Bytes und den historischen SHA-256 `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e`. Zusätzlich wurde jede direkt byteweise gegen die gefrorene Zielannotation verglichen. Beide Vergleiche sind wahr; es wurde kein bloßer Autorenvergleich übernommen.

Die sechs wirklichen `pdftotext -bbox <eigene-PDF> <eigene-bbox>`-Unterprozesse endeten jeweils mit Exit 0. Die beiden `pdftotext -v`-Abfragen ebenfalls. Umgebung: Python `3.14.7`, GCC `16.2.1 20260810`, Poppler `26.08.0`. Exakte Toolargumente und Version stehen in `byte-and-tools-comparison.json`, SHA-256 `ad50caba48b37b409715233f4741430c88c2412025c6cd6c7ef6abc2daece867`, und den beiden `tool-exits.jsonl`/Sidecars. `actual-results.json`, SHA-256 `3b1ba7686b82da5ac7aba1e232f4476714ff29361306fc614de8038edfc2ab5a`, enthält alle sechs eigenen Ergebnisse.

## Finding RC-R01 und Nachprüfung

Das ursprüngliche Problem war die fehlende Zuordnung eines abgebrochenen HTTP-Downloads zu Quelle, URL und Versuchszeit im Sidecar. Der historische Befund steht im gebundenen `REPRO-003-C-repro.md`, Zeilen 96–112. Seine geringe Schwere blieb auf Fehlerprovenienz begrenzt; er widerlegte die positiven Nachbauten nicht.

Die Korrektur steht im gefrorenen Wrapper, Zeilen 80–114: Versuch vor `urlopen` anlegen, Fehlermerkmale nur aus beobachteten Angaben ergänzen und Ende im `finally` eintragen. Zeilen 136–143 erhalten zusätzlich den gescheiterten Gesamtstatus und schreiben den Sidecar. Der Builder ist unverändert.

Für `first404` wurde tatsächlich diese URL versucht: `https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/RC-R01-resume-c-review-20261003-missing-first.pdf`. Beginn war `2026-10-03T09:25:37.332532+00:00`, Ende `2026-10-03T09:25:37.415231+00:00`. Der Sidecar enthält Dateiname `ESS11_questionnaires_DE.pdf`, diese versuchte und finale URL, den ursprünglichen erwarteten Pin, Zielpfad, `httpStatus: 404`, `errorType: HTTPError`, `status: NICHT_BESTANDEN`, `completeFileWritten: false`, `bytes: null` und `sha256: null`. Gesamtstatus und Kind-Exit sind ebenfalls gescheitert; keine Annotation entstand.

Der zusätzliche zweite echte 404-Versuch nutzte `https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/RC-R01-resume-c-review-20261003-missing-second.pdf`, von `2026-10-03T09:25:37.715594+00:00` bis `2026-10-03T09:25:37.788125+00:00`. Er zeigt, dass ein vorheriger erfolgreicher Versuch erhalten bleibt und der folgende Fehlversuch getrennt vollständig zugeordnet wird. Der Pin-Gegenfall trennt abgeschlossenen Download von gescheiterter Pinprüfung. Der Protokoll-Gegenfall erfindet keine beobachtete HTTP-Antwort.

Auswirkung und Abhilfe sind damit im ursprünglich geforderten Umfang nachgeprüft: Zur Rekonstruktion der fehlgeschlagenen Quelle und Zeit ist kein zusätzliches Codedelta mehr notwendig, weil der Sidecar sie selbst enthält. Status RC-R01: `BESTANDEN` nachgeprüft. Neue Probleme mit überprüfbarer Auswirkung wurden in diesem begrenzten Bereich nicht festgestellt. Keine zusätzliche Reparaturrunde erforderlich.

## Grenzen und Erhaltung

Modellmetadaten wurden vom Koordinator als geerbtes Codex `gpt-6.1-sol` übergeben. Interne Revision und genauer Name der geerbten Reasoning-Einstellung sind mir nicht verfügbar. Gleiche Modellfamilie und mögliche gemeinsame Fehler bleiben Grenzen. Frischer Auftragskontext und getrennte Dateien sind organisatorische Trennung; das gemeinsame Dateisystem ist keine technische Sandbox.

`tool-and-model-metadata.json` hält angebotene Toolnamen und benutzte Werkzeuge fest. Benutzt wurden `functions.exec` mit `exec_command`, `write_stdin`, `apply_patch`, Python-Standardbibliothek, vorhandenes Poppler und `collaboration.send_message` für Status an den Koordinator. `unslop` wurde für den Bericht angewandt; der PDF-Skill wurde vor dem öffentlichen PDF-Nachbau gelesen. Kein PDF-Inhalts-/Layouturteil wird aus Hashvergleich oder Bbox-Erzeugung abgeleitet. Keine weiteren Agents, Installationen, Authentifizierungen, Commits, Pushes oder globalen Schreibzugriffe.

Unveränderte frühere Pfad-/Werkzeug-/Redirectbefunde wurden nicht nochmals vollständig auditiert. Nicht geprüft sind Abbrüche durch harte Prozessbeendigung, kaputte Protokollspeicher, allgemeine Racefreiheit oder eine Betriebssystem-Zugriffssperre. Der Protokoll-Gegenfall ist kein DNS-/TLS-/Timeouttest. Die historischen Rollen, Zeitangaben und Zugriffsdeklarationen innerhalb der Annotation bleiben historische Metadaten; heutige Beobachtungen stehen in den neuen Sidecars.

Keine ESS-Roh-/Zwischendaten, Personenzeilen, A/B- oder Wahl-/LR-Daten wurden geöffnet. Der Inventar-CSV ist eine öffentliche Dokumenteingabe. Keine Fragen-, Polungs-, Konstrukt- oder Modellentscheidung, keine Validitäts-, Invarianz-, Fairness- oder Güteaussage, keine Entblindung oder Präregistrierungs-/Modell-Tags wurden vorgenommen. Dokumentationsrechte wurden nur als bestehende Paketgrenze gelesen; keine neue Rechts- oder Exportfreigabe.

`pnpm check`, UI-/Browser-/Releaseprüfungen und wissenschaftliche Abnahmen sind durch diesen Reviewer `NICHT_GEPRÜFT`. Der Auftrag erlaubt ausschließlich eigenes Output und diesen Bericht; der übliche Repositorycheck mit gemeinsamen Buildausgaben bleibt beim Koordinator. Die eigenen Vorbereitungs-/Hash-/Vergleichsläufe endeten mit Exit 0. Die vier erwarteten Fehlerläufe sind vollständig erhalten; es gab keinen unerwarteten Testfehllauf.

Historische Pakete, Erstberichte und gemeinsame Forschungsdateien blieben unverändert. Ein eigener Artefaktindex und Freeze unter `outputs/loop/resume-c-review/` binden nach Abschluss den Bericht und die tatsächlichen lokalen Belege. Hashes bestätigen Identität der Prüffassung, keine wissenschaftliche Abnahme.
