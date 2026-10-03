# LIFE-93 v2: lokale Reproduktion

Fassung 0.1, Stand `2026-10-03T15:56:20.289903+00:00`. Dokumentations-WIP. Der Stand umfasst die öffentliche Gruppenentscheidung vom `2026-10-03T15:54:40.395473+00:00`; spätere Gruppenanzeige und Abnahmen ergänzt Root mit neuem Datum.

Der aktuelle [Breitenauftrag](auftrag-life-93-breite-2026-10-03.md) hat Vorrang vor der alten Analysefolge. v2 führt 43 Originalfragen in acht Inhaltsrubriken, ohne gemeinsamen Faktor oder Gesamtscore. 42 historische Einzelreferenzen sind veröffentlicht; `ESS10SCe03_2:cttresa` bleibt null. Die neue [Gruppenentscheidung](../reports/loop/policy-group-v21-export-decisions.json) veröffentlicht 63 einzelne historische Frage-Gruppen-Paare aus ESS5, ESS8 und ESS9. Die Gruppenanzeige ist damit noch nicht fertig oder freigegeben.

## Was tatsächlich reproduziert wurde

Die [v2-Receipts](../reports/loop/policy-v2-run-receipts.json) belegen fünf ausgeführte Bibliotheksläufe am 3. Oktober 2026, 14:25:06–14:25:18 UTC, jeweils Exitcode 0. Die [Gruppenreceipts](../reports/loop/group-v21-run-receipts.json) belegen drei private Bibliotheksläufe, 15:24:22–15:24:28 UTC, jeweils Exitcode 0. [Einzelzugriff](../reports/loop/policy-v2-access-disclosure.json) und [Gruppenzugriff](../reports/loop/group-v21-access-disclosure.json) benennen den jeweiligen Umfang und frühere Einsicht. Receipts beschreiben den Laufstand; spätere öffentliche Entscheidungen sind eigene Schritte.

Die beiden unten genannten Runner bestehen den aktuellen `--help`-Aufruf. Ein positiver End-to-end-Lauf dieser CLI aus einem frischen Checkout wurde bisher **nicht durchgeführt**. Vorhandene positive Bibliotheksläufe, synthetische Tests und Hilfeausgabe ersetzen diesen Nachweis nicht. Diese Dokumentationsarbeit führt keinen Datenlauf oder öffentlichen Berichtbuild aus.

## Eingaben und Bindungen

Ein frischer Checkout allein reicht nicht. Benötigt wird ein Forschungssnapshot mit den aktuellen Runnern, den unveränderten eingefrorenen Artefakten und den folgenden lokal bereitgestellten Eingaben. Nur den alten Plantag auszuchecken garantiert nicht, dass später ergänzte CLI-Skripte vorhanden sind.

| Weg                                  | Verbindliche Dateien                                                                                                                                                                                                                                                                             | Festgeschriebener Plan                                                |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Einzelreferenzen v2                  | [22-Pin-Manifest](../reports/loop/packages/EMPIRICAL-V2-001/v1/manifest.json), [Freeze](../reports/loop/packages/EMPIRICAL-V2-001/v1/freeze.json), [Zugriffsgate](../reports/loop/gates/pre-empirical-v2.json), [Analysevertrag](../data/analysevertrag.v2.entwurf.json)                         | `analyseplan-v2`, Commit `6702f187394aed903f04c03cf48b46708c2ff4e4`   |
| Historische Zweitstimmengruppen v2.1 | [51-Pin-Manifest](../reports/loop/packages/GROUP-V21-001/v1/manifest.json), [Freeze](../reports/loop/packages/GROUP-V21-001/v1/freeze.json), [Zugriffsgate](../reports/loop/gates/pre-group-v21.json), [Gruppenvertrag](../data/gruppenvertrag.v2.1.entwurf.json) und derselbe v2-Analysevertrag | `analyseplan-v2.1`, Commit `c8fe45333c8be0bf9e8cfa84fe160509802e9184` |

Die exakten SHA256 stehen je `artifacts[n].path` im jeweiligen Manifest, die Gate-Berichtpins unter `reviewers`, die CSV-Pins unter `studies[n].input.sha256` im Analysevertrag. Die Runner enthalten die erwarteten Manifest-, Vertrags- und Freezehashes als feste `PINS`. Abweichungen werden nicht durch neue Pins oder umbenannte Dateien übergangen.

Der Gruppenweg benötigt **alle 36 `outputs/`-Einträge des 51-Pin-Manifests** als ignorierte lokale Voraussetzungen. Dazu gehören öffentliche Original-PDFs, API-/Lizenzmetadaten sowie die öffentlichen Quellenableitungen aus `breadth-group-sources-005`, `breadth-group-binding-006` und `group-contract-v21`. Auch dokumentarische ESS10/ESS11-Einträge gehören zur vollständigen Quellenbindung; das erlaubt keinen Gruppen-Antwortzugriff auf diese ausgeschlossenen Studien. Die Originalbytes müssen an genau den manifestierten relativen Pfaden liegen. Sie werden nicht vom Runner heruntergeladen und sind nicht automatisch in einem Clone enthalten.

Die fünf privaten CSVs gehören ausschließlich an diese Pfade:

| Studie / Ausgabe | Vertraglicher Eingabepfad                  |
| ---------------- | ------------------------------------------ |
| ESS5 / 3.6       | `data/raw/ess5-ed3.6/ESS5e03_6.csv`        |
| ESS8 / 2.3       | `data/raw/ess8-ed2.3/ESS8e02_3.csv`        |
| ESS9 / 3.3       | `data/raw/ess9-ed3.3/ESS9e03_3.csv`        |
| ESS10-SC / 3.2   | `data/raw/ess10-sc-ed3.2/ESS10SCe03_2.csv` |
| ESS11 / 4.2      | `data/raw/ess11-ed4.2/ESS11e04_2.csv`      |

Für einen reinen Gruppenlauf werden davon nur ESS5/8/9 verarbeitet. Dateiname und Editionsetikett allein beweisen keine Herkunft. Hash, Bytezahl und die vorgeschriebene interne Deutschland-/Runden-/Editionsprüfung bleiben erforderlich; die unabhängige offizielle Download-/Rohreproduktion wird dadurch nicht behauptet.

Diese Metadatenliste lässt sich ohne Zugriff auf eine CSV oder einen Cache ausgeben:

```bash
python - <<'PY'
import json
from pathlib import Path

contract = json.loads(Path('data/analysevertrag.v2.entwurf.json').read_text())
for study in contract['studies']:
    print(study['input']['sha256'], study['input']['path'])

manifest = json.loads(Path('reports/loop/packages/GROUP-V21-001/v1/manifest.json').read_text())
for artifact in manifest['artifacts']:
    if artifact['path'].startswith('outputs/'):
        print(artifact['sha256'], artifact['path'])
PY
```

Die Anleitung ergänzt keine Downloadberechtigung. Daten- und Dokumentationsbedingungen, erlaubter lokaler Bezug und Attribution müssen erhalten bleiben. Siehe [Lizenzakte](lizenzen.md).

## Künftiger lokaler Datenlauf

Die folgenden Schritte sind eine Anleitung für eine gesondert vorbereitete Reproduktion, keine in diesem Dossier ausgeführte Analyse.

1. Einen separaten Checkout des passenden Forschungssnapshots nutzen. Den bestehenden Arbeitsstand und seine privaten Outputs erhalten. Die lokal und auf `origin` gebundenen Plantags müssen auf die oben genannten Commits zeigen. Beide Runner prüfen dies selbst mit Git; der tatsächliche Lauf benötigt deshalb Git und Netzwerkzugang zum konfigurierten `origin`. `--help` beendet sich davor.
2. Die erforderlichen privaten CSVs und öffentlichen Caches mit erlaubtem Zugang bereitstellen. Keine Rohdaten oder privaten Ergebnisse in Webapp, CI, Git, Agentenkontext oder öffentliche Logs kopieren. Die exakten manifestierten Bytes erhalten; andere API-Abrufe sind nicht automatisch Ersatz.
3. Python bereitstellen. Die aktuellen Hilfeaufrufe liefen mit Python 3.14.7; das ist keine Prüfung aller Pythonversionen. Die v2-Runner nutzen die Standardbibliothek, keine R-/pnpm-Installation für diesen Rechenweg.
4. Im Repository-Stamm zuerst die Hilfe lesen:

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/run-policy-v2.py --help
PYTHONDONTWRITEBYTECODE=1 python scripts/run-policy-groups-v21.py --help
```

5. Erst im dafür vorbereiteten separaten Checkout den gewünschten Weg ausführen:

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/run-policy-v2.py --study all
PYTHONDONTWRITEBYTECODE=1 python scripts/run-policy-groups-v21.py --study all
```

Alternativ akzeptiert `--study` eine der im jeweiligen Hilfeaufruf genannten Studienkennungen. Der Gruppenrunner erlaubt nur ESS5e03_6, ESS8e02_3 und ESS9e03_3. Die Wege werden getrennt gerechnet; `all` verbindet keine Personen und erzeugt keine Gesamtverteilung.

Die CLI verweigert vorhandene `run.json`-Dateien für ausgewählte Studien mit `existing_private_run_use_fresh_checkout`. Keine Umgehung durch Löschen, Umbenennen oder Überschreiben der historischen Outputs. Private Ergebnisse liegen unter `data/local/policy-v2/<study>/run.json` beziehungsweise `data/local/policy-groups-v21/<study>/run.json`; die Hüllen verlangen Verzeichnisse `0700` und Dateien `0600`. Sichere Receipts und tatsächliche Exitcodes getrennt sichern, ohne private Inhalte auszugeben.

Fehlende Caches, falsche Pins, Gate-/Quellen-/Studienabweichungen oder vorhandene Outputs sind echte Abweisungen. Ein nicht gelaufener Fresh-checkout-Versuch bleibt offen. Die Runner geben nur private Kandidaten und sichere Receipts aus; Erfolg ist keine automatische Veröffentlichungsentscheidung.

## Öffentliche Referenzen und Bericht

Die [Einzelentscheidung](../reports/loop/policy-v2-export-decisions.json) bindet die fünf Dateien unter [data/reference-v2](../data/reference-v2/README.md). Die [Gruppenentscheidung](../reports/loop/policy-group-v21-export-decisions.json), SHA256 `544f31f83cac1e258ed13559c04373430a5ac0d792c4380421a32bb623ef42bc`, bindet die drei öffentlichen Dateien `data/reference-groups-v21/ESS5e03_6.json`, `ESS8e02_3.json` und `ESS9e03_3.json`. Sie enthält die genaue Frage-Gruppen-Paarfreigabe und Exporthashes. Veröffentlicht sind 21/30/12 Paare; alle 8/9/9 vorab definierten Gruppen bleiben im Bestand, einschließlich Other und leerer Gruppen. Alle übrigen Referenzen bleiben null.

Der gezielte Methodenfix GR21-M-001 ist laut Rootentscheidung abgeschlossen. Das ursprüngliche Quellenurteil wurde für die unveränderten Kandidaten und Quellen weitergenutzt, nicht als neue v2-Erstbewertung umbenannt. Der [gezielte Ergebnismanifeststand](../reports/loop/packages/GROUP-RESULTS-V21-001/v2/manifest.json) und die öffentliche Entscheidung bewahren diese Grenze. Dieses Dossier führt kein eigenes Review aus.

Ein neuer privater Reproduktionslauf darf bestehende öffentliche Dateien nicht ersetzen. Dafür braucht es tatsächliche Ergebnisprüfung, gebundene Bericht-/Manifestbytes, die explizite Schnittmenge zugelassener Einzelangaben beziehungsweise Frage-Gruppen-Paare und einen eigenen Root-Exportentscheid. Ein Statusstring im Kandidaten genügt nicht. Keine Veröffentlichung der privaten `run.json`.

Der [thematische Einzelbericht](../reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md) lässt sich aus den gebundenen öffentlichen Einzelreferenzen mit folgendem read-only Bytevergleich prüfen:

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/build-policy-v2-report.py --check
```

Dieser Build benötigt zusätzlich die 30 öffentlichen Quellen-Caches aus `catalogue.sources[].cachedPath` des [Fragenkatalogs](../data/politikprofil-v2.fragen.entwurf.json), ihre `originalBytesSha256`, die im Skript gebundenen öffentlichen Methoden-/Review-/Entscheidungsbytes und Exportdateien. Ohne `--check` schreibt der Builder das Berichtsartefakt; vorhandene Berichte deshalb für eine Reproduktion nicht unbesehen überschreiben. Ein erfolgreicher Bytevergleich reproduziert die Darstellung öffentlicher Aggregate, keine Rohrechnung. Der Gruppenexport ist davon ein eigener Schritt; diese Anleitung behauptet keinen fertigen Gruppenbericht oder Gruppen-Webtest.

## Aussagegrenzen und Aktualisierung

Bekannte v1-A/B-Antworten bleiben bekannt; die alte B-/FULL-/Norm-/Gruppenfolge bleibt angehalten. v2 wurde nach `analyseplan-v2`, die Parteisemantik nach dem gesonderten `analyseplan-v2.1` geöffnet. Auch v2-Einzelreferenzen waren vor dem Gruppenlauf bekannt. Keine dieser Einsichten ist eine unangetastete Bestätigung.

Historische Wählergruppen beruhen auf erinnerter Wahlteilnahme und Zweitstimme zur jeweiligen damaligen Wahl. Der Gruppenweg verlangt `vote=1` und eine gültige definierte Zweitstimmenkategorie. Ihr Nenner ist je Frage zusätzlich auf gültige Originalantworten konditioniert. Sie sind keine aktuellen Parteienpositionen, keine Gesamtübereinstimmung und kein Vorschlag einer nächsten Partei. Null bedeutet fehlende Freigabe, nicht null Prozent. Keine Studie wird mit einer anderen gepoolt. Unsicherheit, Kontext-/Modusübertragung, Nonresponse und ESS8s München-Grenze bleiben begrenzt; die 100/5-Regeln sind Darstellungsheuristiken.

Die Codex-Erstrollen gehörten derselben Modellfamilie an. Übereinstimmung ist kein Neutralitätsbeweis, und die Ergebnisrollen haben keine unabhängige Roh-/Downloadreproduktion geleistet. Menschenverständnistest mit fünf realen Personen, Designzustimmung, sichtbarer Tastaturfokus, echte 200%-Zoomprüfung, Claude-Schlusskontrolle, konkrete Rechte-/kommerzielle Nutzungsprüfung und persönlicher Release bleiben offen.

Root ergänzt hier später den Stand der Gruppenanzeige, gegebenenfalls einen eigenen reproduzierbaren Gruppenbericht und die tatsächlich abgeschlossenen menschlichen Prüfungen. Dafür Datum und Belegpfade ändern; die ursprünglichen Lauf-, Auswahl- und Nullgrenzen nicht rückwirkend umschreiben.
