# AE-01: begrenzte Exportkorrektur

Autorenfassung vom 2026-10-03 zur gesicherten [Erstprüfung](../reviews/AGGREGATE-EXPORT-001-first.md). Das Originalurteil bleibt unverändert. Diese Korrektur betrifft ausschließlich Strukturprüfung und Ausführungsbindung des neuen A-Aggregatexports. Die wissenschaftlichen Kriterien, vier eingefrorenen R-Quellen, A-/R-Laufzeit, bestehenden Gates und vorherigen B-/FULL-Dateien wurden nicht geändert. Der bestehende Reviewer prüft die Korrektur anschließend gezielt; dieses Autorenergebnis ist keine Abnahme.

## Änderung

Die globale Liste bekannter Wörter und die allgemeine 87er-Listenbegrenzung sind entfernt. `data/a-aggregate-public.schema.json` beschreibt nun die erforderlichen und erlaubten Felder je Pfad. Der kleine Abhängigkeitsfreie Validator `pipeline/public_schema.py` prüft genau diesen Schemaumfang: Typen, Konstanten, geschlossene Objekte, Pflichtfelder, Alternativen sowie feste Arraygrößen. Zahlen müssen endlich sein; Boolwerte sind keine Zahlen oder Counts. Es gibt keine allgemeine Annahme eines bekannten Wortes an einem anderen Ort.

Der Vertrag bindet die neun Items, 51 Schwellen und 87 Momentlabels; EFA-/CFA-Ladungen haben 9×k, Faktorkorrelationen k×k und Scorekovarianzen exakt die Itemzahl der betreffenden Skala zum Quadrat. Gleiches gilt für Kovarianzvektoren und nach Modell-/Itemidentität geschlossene Intervallcontainer. Counts und die neun Missingcounts sind skalare Ganzzahlen. Die feste R-Konfiguration bleibt inhaltlich unverändert und wird vollständig geprüft. `source_code_pins` muss genau die vier ursprünglichen Entwicklungsartefakte mit gültigen SHA256 enthalten; jede dieser vier Bindungen muss dem vollständigen aktuellen Codehashbeleg des tatsächlich autorisierten Runs entsprechen. Eine leere Pinmenge ist damit ausgeschlossen.

Die Quelle für Statuszweige sind die unveränderten Konstruktoren in `develop.R`: `ed_efa_suite`, `ed_model_evaluation`, `ed_select` und `ed_analyse`; Intervall-/Fit-/Countformen stammen aus `support.R` und `adapter_v2.R`. Explizit unterstützt werden ausgeführte und fehlgeschlagene EFA-Runs, ausgeführte beziehungsweise fehlgeschlagene Modelle, nicht verfügbare Diagnostik, ein offener RMS-Nahnullbefund sowie `NO_PROFILE_CANDIDATE`. Ein fehlgeschlagener EFA-Run erhält keine erfundenen Alignment-/Mappingfelder. R-/jsonlite-Eigenheiten bleiben abgebildet: skalare Einerelementvektoren, einzelne Failurestrings, leere M1-Korrelationsliste und als leeres Objekt serialisierte NULL-Felder. Keine Entscheidungsgrenze wurde ergänzt oder numerisch geändert.

Der Ablauf bleibt `A-Preflight → tatsächlich gebundener Runbeleg → Aggregat`. Das Aggregat wird einmal in einen Bytesnapshot gelesen; dessen Hash wird vor dem JSON-Lesen geprüft. Vor der Kopie werden Preflight, aktuelle Entwicklungscodehashes, Runbeleghash und tatsächlicher Aggregathash erneut geprüft. Das feste öffentliche Ziel `reports/phasen/01-a-entwicklung.json` wird ausschließlich neu angelegt; die ESS-Zitation, Datenlizenz und Änderungsnotiz aus dem unveränderten öffentlichen Veröffentlichungsvertrag bleiben erhalten. Keine neue Rohdatenquelle, Tagvoraussetzung oder wissenschaftliche Freigabe wurde eingeführt. Der direkte Pfadaufruf kann nun bereits die Hilfe anzeigen; empfohlen bleibt `python3 -B -m pipeline.aggregate_export LABEL`.

## Tatsächliche technische Prüfung

Erlaubte Ausgangsdatei war ausschließlich das vollständig erfundene R-Aggregat unter `outputs/loop/r-runtime/root-development-correlation-round1-001/development-aggregate.private.json`, SHA256 `6bf81743ddc8c884950184666d578ac574037eeb1207c717152e51e26fe6c4a2`. Seine Bytes wurden vor der Schemakonstruktion geprüft. Das Schema enthält feste Konfigurations-/Formvorgaben, keine synthetischen geschätzten Ladungen, Scorekennwerte oder Personenwerte. Der reproduzierbare Schemakonstruktor liegt im eigenen Ausgabeordner.

`python3 -B -m outputs.loop.resume-aggregate-export-correction.tests` bestand mit 10/10 Tests in 0.741 Sekunden. Die 18 Injektionsfälle wurden jeweils sowohl am reinen Validator als auch im vollständigen nachgebildeten Exportfluss geprüft. Dazu gehören die ursprünglichen 20×9-Vektoren in H-Kovarianzen, `counts.values`, Antwortlisten im Missingcount, fehlende `scores`, leere/unvollständige/zusätzliche Pins, falsche Typen, nicht endliche Werte, falsch platzierte bekannte Wörter und fehlende Pflichtfelder. Die unveränderte echte synthetische R-Ausgabe sowie die genannten R-Fehlerzweige werden akzeptiert. Der vollständige Export prüft außerdem falschen Runstage, Fehlerexit, Runtime-Probe, Autorisierungs-/Codedrift, Hashprüfung vor semantischem Lesen, letzte Beleg-/Aggregatdrift, ESS-Metadaten und das Überschreibungsverbot.

Alle Flusstests verwenden disposable erfundene Projektwurzeln ausschließlich im eigenen Ausgabeordner. Der eigentliche A-Preflight und die aktuellen Codehashes sind dort ausdrücklich gemockt. Die Tests schreiben niemals das wirkliche öffentliche A-Ziel. Es gab keine echte ESS-Dateisuche, Existenzprüfung, Antwort-/Outputlektüre, empirische R-Ausführung oder Tagprüfung. `python3 -B pipeline/aggregate_export.py --help` und `python3 -B -m pipeline.aggregate_export --help` endeten beide erfolgreich. Kein Git-, pnpm-, Installations- oder Claude-Aufruf erfolgte.

## Pins und Grenze

| Korrekturdatei | SHA256 |
| --- | --- |
| `pipeline/aggregate_export.py` | `93321bd7395cd7dfddc2bde3dbfe7b1ae1d53c436d3162012eee768a0665deb9` |
| `pipeline/public_schema.py` | `41093aed8699db89846b6cb0b962335c450ea3a21e96f906e2d6dbfd8288b1bc` |
| `data/a-aggregate-public.schema.json` | `fe7d71fa47fa96b00e45cd60c8a97d4f623b351f91066d6120dd9d006cde3fd2` |
| eigener Schemakonstruktor | `2a2738d5fcec2459259fe481370ea7b3422d9a3f70e43ad2ff54f76a192765a0` |
| eigener Testtreiber | `ed0ad95e0a212ab31b6459a10d7a096d85ab28e22c0649f02e315e2a67dc2eee` |

Die Ursprungspinquelle wird in `outputs/loop/resume-aggregate-export-correction/pins-before.json` ausdrücklich benannt; die frühere Exportprüfsumme stammt aus dem unveränderten Erstbericht und ist keine nachträglich behauptete eigene Vorhermessung. `pins-after.json` enthält die tatsächliche aktuelle Messung. Alle vier R-Codepins, die synthetische Ausgangsdatei und der Veröffentlichungsvertrag stimmen mit dem dokumentierten Ausgangsstand überein. Testresultat und Testlog liegen daneben.

Die Sperre schützt gegen unbeabsichtigte falsche Struktur und Kopie. Veränderbare Koordinatorbelege und das gemeinsame Dateisystem sind weiterhin keine unverfälschbare Autorisierung oder technische Agent-Isolation. Die gleiche Codex-Modellfamilie kann gemeinsame Fehler enthalten. Schema- und Flusstests sind weder eine erneute Methodenvalidierung noch eine empirische oder persönliche Releasefreigabe.
