# AGGREGATE-EXPORT-001: gezielte Korrekturrunde 1

Datum 2026-10-03, derselbe Codex-Subagent `pre_empirical_methods`. **Urteil: ACCEPTED_BOUNDED für die korrigierte technische Exportgrenze. AE-01 ist geschlossen.** Das Urteil betrifft den Schutz gegen versehentliche falsche Aggregatstruktur, fehlende Codebindungen und Kopie. Kein neues Methoden-Gesamtaudit, kein Urteil über reale A-Ergebnisse, keine wissenschaftliche oder Releasefreigabe. Die konkrete reale Ausgabe muss weiterhin der Koordinator prüfen.

## Fassung und Zugriff

Expliziter Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch `research/life-93-night-20261003`, live HEAD `6466767c54070e747b5a233b0c0c41c07f0fc7ca`. Die Korrektur lag auf diesem Basiscommit als Arbeitsbaumfassung vor. Manifest `reports/loop/packages/AGGREGATE-EXPORT-001/v2/manifest.json`, SHA256 `f2be5e4f947f9698be9cf4458a9d6d34735292ca48b2a0e7f7a5cfd01c74e81c`. Alle sieben Manifestartefakte und die ausdrücklich erlaubte identische synthetische Ausgangsdatei stimmten vor/nach der Prüfung. Der Erstbericht blieb unverändert, SHA256 `8d88a723579d4a77dcc34f195e6af21cb890b0ab4ab83fbcbf0f26e9c277aea0`.

Korrigierte Exportdateien:

| Datei | SHA256 |
| --- | --- |
| `pipeline/aggregate_export.py` | `93321bd7395cd7dfddc2bde3dbfe7b1ae1d53c436d3162012eee768a0665deb9` |
| `pipeline/public_schema.py` | `41093aed8699db89846b6cb0b962335c450ea3a21e96f906e2d6dbfd8288b1bc` |
| `data/a-aggregate-public.schema.json` | `fe7d71fa47fa96b00e45cd60c8a97d4f623b351f91066d6120dd9d006cde3fd2` |

Die einzige Antwortausgabe als Eingabe war das bereits zuvor erlaubte erfundene Aggregat `outputs/loop/r-runtime/root-development-correlation-round1-001/development-aggregate.private.json`, SHA256 `6bf81743ddc8c884950184666d578ac574037eeb1207c717152e51e26fe6c4a2`. Ich las die Korrekturdateien, den zugehörigen Autorbericht und die relevanten öffentlichen R-Statuskonstruktoren. Keine fremden aktuellen Urteile, echten ESS-Roh-/Privatdateien, A/B-Antworten, realen Receipts oder realen Gates wurden gesucht oder geöffnet. Der eigentliche private Preflight wurde nicht aufgerufen. Eigene nachgebildete Projektwurzeln liegen vollständig unter `outputs/loop/aggregate-export-round1/`; ihre privaten Pfadnamen bezeichnen ausschließlich erfundene Testdateien. Keine gemeinsame Datei, Gitstand, Installation oder bestehende Ausgabe wurde verändert. HOME blieb unverändert.

## Eigene gezielte Gegenproben

Tatsächliche Befehle im genannten Worktree:

```text
PYTHONDONTWRITEBYTECODE=1 python3 outputs/loop/aggregate-export-round1/probes.py
PYTHONDONTWRITEBYTECODE=1 python3 pipeline/aggregate_export.py --help
PYTHONDONTWRITEBYTECODE=1 python3 -m pipeline.aggregate_export --help
```

Alle drei Befehle endeten mit Exit 0. Der frühere Fehler des direkten Pfadaufrufs ist damit ebenfalls behoben. Bei einer vorausgehenden eigenen Schema-Schlüsselinspektion verursachte `Counter.update(rule)` einen TypeError; der korrigierte Aufruf mit `rule.keys()` funktionierte. Das war ein Fehler des Inspektionshilfsbefehls, kein Export-/Schemafehler. Er ist in `execution-receipt.json` ausdrücklich erhalten.

Der eigene Treiberhash lautet `5fd69b421ceb4995d91068c067e4ef6ba5ddeaa81b16b456a2c92c613fd08dcf`. Originalergebnisse stehen in `probe-result.json` und `legitimate-result.json`, vollständige Eingabepins in `pins-before.json` und `pins-after.json`.

Alle elf Validatorerwartungen wurden erfüllt. Insbesondere stoppen nun die ursprünglichen zwanzig Neuner-Antwortvektoren anstelle der H-Kovarianz 3×3, Vektoren unter `counts.values`, Antwortlisten anstelle eines Missingcount, der entfernte Pflichtcontainer `models.M3.scores` und die leere Pinmenge. Unbekannte Felder, falsch platzierte bekannte Felder, NaN und ungeeignete Listen werden verworfen. Die identische echte synthetische R-Ausgabe wird weiter akzeptiert.

Vierzehn vollständige nachgebildete Exportflüsse wurden ausgeführt. Der Normalfall wird ausschließlich in der eigenen Testwurzel mit ESS-Zitation, Lizenz, Änderungsnotiz und allen vier Codepins ausgegeben. Die übrigen dreizehn Fälle stoppen ohne Ausgabe: die sechs früher geprüften Run-/Hashabweichungen sowie Kovarianz-/Count-/Pflichtfeldinjektionen, leere und unvollständige Pins und ein formal gültiger, aber falscher Codehash. Die zuvor tatsächlich exportierte 20×9-Injektion und die leere Pinmenge werden jetzt auch in diesem vollständigen Fluss zurückgewiesen.

Der Preflight und aktuelle Codehashabruf sind in diesen Flusstests ausdrücklich gemockt. Damit werden keine wirklichen Tags, Quellantworten oder privaten Runbelege geprüft. Die überprüfte normale Reihenfolge bleibt `preflight → Aggregatbytes → preflight`. Runstage, Fehlerexit, Runtime-Probe sowie Autorisierungs-/Codedrift stoppen vor dem Aggregatlesen. Hashabweichung stoppt nach dem nötigen Bytesnapshot und vor dem semantischen JSON-Lesen. Reale A-Inhalte wurden aus diesen Proben niemals abgeleitet.

## Legitimer R-Statusumfang und Korrekturmechanismus

Zusätzlich akzeptiert das Schema alle 33 eigens aufgebauten legitimen Statusformen. Grundlage sind die öffentlichen Konstruktoren `develop.R:135–158`, `193–226`, `228–255`: sämtliche sieben nichtleeren Fehlerkombinationen der drei EFA-Runs für jede Faktorzahl, fehlgeschlagene M1/M2/M3-Modelle, nicht verfügbare Diagnostik, offener RMS-Nahnullbefund, `NO_PROFILE_CANDIDATE`, Nullwerte der zusätzlichen Diagnostik sowie einzelne oder mehrere Score-Failurestrings. Diese Formen wurden aus dem tatsächlichen Quellvertrag erzeugt; sie sind keine neuen empirischen R-Läufe. Der unveränderte erfolgreiche Baseline stammt aus der tatsächlichen früheren synthetischen R-Ausführung.

Die globale Wortliste ist entfernt. `public_schema.py:31–77` prüft die im Dokument verwendeten lokalen Referenzen, eindeutigen Alternativen, Pflichtfelder, geschlossenen Objekte, konkreten Typen, Konstanten, vollständigen Arraygrößen und endlichen Zahlen. Boolwerte zählen nicht als Counts oder Zahlen. Das Schema bindet Moment-/Modell-/Scorepfade an die vorgesehenen Item- und Faktorgrößen; ein bekanntes Wort erhält an anderer Stelle keine allgemeine Erlaubnis. Die geprüften Schema-Schlüssel stimmen mit dem tatsächlich implementierten Validatorumfang überein.

Die vier Entwicklungs-Codepins sind im Schema vollständig erforderlich. `aggregate_export.py:60–62` verlangt zusätzlich genau diese Vierermenge und vergleicht jeden Wert mit dem autorisierten aktuellen Run-Codebeleg. Die frühere leere Allquantifizierung kann dadurch nicht mehr bestehen. Zeilen 46–59 lesen einen gebundenen Bytesnapshot; Zeilen 66–69 prüfen vor Kopie erneut Preflight, aktuelle Codehashes, Runreceipthash und tatsächlichen Aggregathash. Der feste öffentliche Zielpfad wird ausschließlich neu angelegt. Keine numerische Forschungsgrenze wurde verändert.

**Kein offenes Finding aus AE-01 verbleibt.** Die Annahme gilt für diese gepinnte technische Implementierung und ihr Schema. Veränderbare Belege, gemeinsame Dateirechte und verbleibende Rennen sind keine unverfälschbare Autorität oder vollständige Agentisolation. Gleiche Codex-Modellfamilie und gemeinsame mögliche Fehler bleiben eine Grenze. Diese Prüfung ersetzt weder die konkrete Sichtprüfung des realen Exportartefakts durch den Koordinator noch spätere Methoden-, Ergebnis- oder Releaseabnahmen.
