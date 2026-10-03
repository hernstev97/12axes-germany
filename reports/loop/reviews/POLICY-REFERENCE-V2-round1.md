# Gezielte Korrekturprüfung PRV2-F01, Runde 1

PRV2-F01 ist in der gepinnten v2-Fassung behoben. Die beiden ursprünglich fehlschlagenden Unterfälle und die angeforderten Regressionen bestehen. Im unmittelbar untersuchten Korrekturpfad habe ich keinen neuen Fehler festgestellt. Dieses Urteil schließt den konkreten Softwarebefund; es ist kein Gesamtaudit und keine empirische, methodische oder öffentliche Freigabe.

## Prüffassung und Erhaltung

Geprüft wurde ausschließlich im Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch laut Auftrag `research/life-93-night-20261003`. Git wurde nicht aufgerufen. Grundlage war das tatsächlich gelesene [v2-Manifest](../packages/POLICY-REFERENCE-V2/v2/manifest.json). Sein selbst berechneter SHA-256 ist `1b4a87b76f884168054e3f3a6a762a747ba02176ced6342cf4772afd5c05ecc2`; eine erwartete Manifestprüfsumme wurde nicht aus der Nachricht abgeleitet.

| Datei | SHA-256 vor und nach dem Testlauf |
| --- | --- |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/tests/test_policy_reference_v2.py` | `01ddfaa79b3fedf1cc10d79b547a38622827fa218a29bd921f896e39568d5ad8` |

Manifest und beide Codepins stimmen vor und nach dem Lauf überein. Der ursprüngliche eigene Erstbericht behielt SHA-256 `d3aa9f4fe5721facef4a733679a6ed841f54f4c414f91b7c83038304dc7c3618`. Die vorhandene eigene Suite mit 29 Methoden behielt SHA-256 `c1bf85546ef65f3f55e67f88f952babd90307d978824dbf5ec67c5c622ea93ad`. Kein Inhalt dieser Dateien wurde geändert. Der im Manifest genannte historische v1-Commit wurde nicht über Git gelesen. Die abschließende Kontrolle nach Berichtserstellung steht in `outputs/loop/policy-reference-v2-review/round1/final-check.json`.

Der erste Manifestzugriff um `2026-10-03T12:46:12.812874+00:00` schlug tatsächlich mit `FileNotFoundError` und Exitcode 1 fehl. Nach der Bereitstellung wurde genau derselbe Pfad erfolgreich erneut geöffnet. Der fehlgeschlagene Zugriff ist in [start-evidence.json](../../../outputs/loop/policy-reference-v2-review/round1/start-evidence.json) erfasst; er war weder ein Testlauf noch ein fachlicher Befund.

## Gezielte Quelltextprüfung

In `pipeline/policy_reference_v2.py`, Zeile 258, lautet der Beitrag nun:

```python
(row.weight / valid_weight) * (indicator - proportion)
```

Damit erfolgt die Division durch den gültigen Nenner vor der Multiplikation. Die PSU-Summen in Zeilen 259–262 enthalten ausschließlich `fsum(contributions)`; es folgt keine zweite Division durch `valid_weight`. Stratumzentrierung, Varianzfaktor `G/(G-1)` und `sqrt(variance)` bleiben im geprüften Abschnitt erhalten. Der gültige Nenner für die Kategorieanteile bleibt in Zeile 247 unverändert. Der neue Quotient wird weiterhin nur bei `COMPUTED_WRT_TAYLOR` berechnet. Leere gültige Mengen und gesperrte Varianzpfade führen in den Regressionen weder zur Division durch null noch zu einem erfundenen SE.

Der ursprüngliche Fehler beruhte auf dem vorzeitigen Unterlauf von `weight * residual`. Die neue Reihenfolge verhindert ihn in beiden belegten Fällen. Es musste weder der zugelassene Bereich positiver endlicher Gewichte eingeschränkt noch eine PSU entfernt werden.

## Ausgeführte Regressionen

Alle Prozesse liefen mit `PYTHONDONTWRITEBYTECODE=1`. Die folgenden Exitcodes stammen jeweils vom tatsächlich gestarteten und abgewarteten unittest-Prozess, nicht aus einem zusammenfassenden Wahrheitswert:

| Suite | Testmethoden | Tatsächlicher Exitcode | Ergebnis |
| --- | --- | --- | --- |
| Gepinnte Autorensuite | 22 | 0 | Alle bestanden |
| Unveränderte eigene Erstprüfsuite | 29 | 0 | Alle bestanden, einschließlich der beiden früher fehlschlagenden Unterfälle |
| Neue gezielte eigene Orakel | 6 | 0 | Alle bestanden |

Keine Fehlschläge, Laufzeitfehler, übersprungenen Tests oder Timeouts wurden gemeldet. Die vorhandene 29er-Suite enthält weiterhin die 240 deterministischen Fraction-Designfälle. Ihre erneute Ausführung ist die angeforderte Regression; daraus wird kein neues Gesamtaudit abgeleitet. [run-evidence.json](../../../outputs/loop/policy-reference-v2-review/round1/run-evidence.json) hält Befehle, PIDs, Start-/Endzeiten, Laufzeiten und reale Exitcodes fest. Der übergeordnete Runner selbst endete ebenfalls mit Exitcode 0. Vollständige Ausgaben liegen in `author-tests.txt`, `existing-reviewer-tests.txt` und `targeted-tests.txt` im selben Ausgabeordner.

Die sechs [gezielten Orakel](../../../outputs/loop/policy-reference-v2-review/round1/targeted_tests.py) prüfen Anteile, Varianzen und SE mit relativer Toleranz `2e-14` und absoluter Toleranz `2e-15`:

- Zwei gleich gewichtete PSUs, je eine Kategorie: `p_A=p_B=1/2`, `V_A=V_B=1/4`, `SE_A=SE_B=1/2`. Das gilt jetzt auch für das kleinste positive Float-Gewicht `5e-324`.
- Gewichtsverhältnis 1:2: `p_A=1/3`, `p_B=2/3`, `V=16/81`, `SE=4/9` für beide Kategorien. Die kleinsten subnormalen Gewichte liefern jetzt diese Werte.
- Drei Kategorien in zwei Strata mit nicht verschwindenden Stratumsmittelwerten und einem leeren PSU: Anteile für A/B/C `1/10`, `3/5`, `3/10`; Varianzen `149/10000`, `191/2500`, `801/10000`. Alle SE stimmen mit den Wurzeln dieser Varianzen überein. Eine ungenutzte vierte Kategorie behält Anteil, Varianz und SE null; Reihenfolge und Zähler bleiben erhalten.
- Mehrere Zeilen im selben PSU und ein leerer PSU: `W=6s`, `u=(1/4,-1/6,-1/12,0)`, `V=7/54`. Dieser Fall erkennt auch eine irrtümliche zweite Normierung der PSU-Summen.
- Zwei gültige subnormale Gewichte neben großen fehlenden und strukturell nicht gefragten Gewichten: Der Nenner bleibt `2s`; beide Anteile sind `1/2`, beide Varianzen `1/6`, die SE deren Wurzeln. Große nicht gültige Gewichte verändern den gültigen Nenner nicht; die Nullbeitrags-PSUs bleiben enthalten.
- Leere gültige Mengen, fehlende Designbasis, fehlende Designkennung und Singleton: Die jeweils vorgesehenen Status und fehlenden Varianzen/SE bleiben erhalten. Der neue Quotient wird in diesen Fällen nicht benötigt.

Die Orakel variieren gemeinsame Gewichtsskalierungen vom kleinsten positiven Float und weiteren subnormalen Vielfachen über kleine normale Gewichte bis zu großen endlichen Gewichten. Die gewählten Werte ergeben endliche Gesamtsummen. Das ist keine Behauptung einer bitgenauen Invarianz für beliebige gerundete Float-Eingaben.

Die drei Suites lassen sich direkt erneut ausführen, ohne die erhaltenen Evidenzdateien zu überschreiben:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s pipeline/tests -p test_policy_reference_v2.py -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s outputs/loop/policy-reference-v2-review -p reviewer_tests.py -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s outputs/loop/policy-reference-v2-review/round1 -p targeted_tests.py -v
```

## Grenzen, UTC und Prozessabschluss

Die Prüfung blieb auf PRV2-F01, die Rechenreihenfolge, die erlaubten Regressionen und unmittelbar mögliche neue numerische Fehler begrenzt. Keine anderen Berichte, Root-Verteidigung, State-/Handoff-Dateien, Roh- oder sonstigen lokalen Daten, Konten, Authentifizierung oder empirischen Ergebnisse wurden gelesen. Kein Git, pnpm, Installation, Claude, zusätzlicher Agent oder neue Forschung. Geschrieben wurden nur dieser neue Bericht und eigene Dateien unter `outputs/loop/policy-reference-v2-review/round1/`. Der bereits gelesene unslop-Skill wurde beim Bericht angewandt.

Eine tatsächliche Studie, Fragen-/Studienprovenienz, Designvollständigkeit oder empirische Eignung kann diese Software weiterhin nicht bescheinigen. Die synthetischen Resultate sind keine empirische Validierung. Andere Python-/Plattformversionen, empirische Daten oder externe Survey-Pakete wurden nicht geprüft. Das ist ein eigenes gezieltes Codex-Urteil ohne vorgegebene Annahme. Gleiche Modellfamilie und mögliche gemeinsame Fehlerquellen bleiben eine Grenze.

- Prüfstart: `2026-10-03T12:46:12.812874+00:00`.
- Synthetischer Lauf: `2026-10-03T12:48:24.280673+00:00` bis `2026-10-03T12:48:24.573612+00:00`; insgesamt `0.292927` Sekunden einschließlich dreier Prozessstarts. Python `3.14.7 (main, Aug 14 2026, 06:38:32) [GCC 16.2.1 20260810]`.
- Autorensuite: `0.064113` Sekunden; vorhandene eigene Suite: `0.164297` Sekunden; gezielte Orakel: `0.064370` Sekunden. Diese Laufzeiten enthalten Prozessstart und -abschluss.
- Bericht erstellt: `2026-10-03T12:49:31.405051+00:00`; seit dem ersten Zugriff rund `198.6` Sekunden einschließlich Bereitstellung des Manifests, Lesen, Tests und Dokumentation.
- Runner-PID `2432040` und Test-PIDs `2432099`, `2432104`, `2432119` wurden nach Abschluss kontrolliert: 2432040 PID absent, 2432099 PID absent, 2432104 PID absent, 2432119 PID absent. Die drei Kindprozesse wurden jeweils abgewartet und eingesammelt. Keine Hintergrunddienste, Timeouts oder nötigen Prozessabbrüche. [proc-cleanup.json](../../../outputs/loop/policy-reference-v2-review/round1/proc-cleanup.json) enthält die Kontrolle.

Gezieltes Ergebnis: PRV2-F01 geschlossen für diese Prüffassung. Keine weiteren Befunde im untersuchten Korrekturpfad. Der Erstbericht bleibt als unverändertes Urteil über v1 erhalten.
