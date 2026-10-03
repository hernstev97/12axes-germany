# AGGREGATE-EXPORT-001: technische Erstprüfung

Datum 2026-10-03, Codex-Subagent `pre_empirical_methods`. **Urteil: KORREKTUR_ERFORDERLICH für den neuen automatischen Aggregatexport.** AE-01 betrifft ausschließlich die behauptete exakte Schema-/Offenlegungssperre. Dies ist kein erneutes fachliches Gesamtaudit und ändert keine abgeschlossene Methodenbewertung, A-Entwicklungsregel oder wissenschaftliche Aussage.

## Prüffassung und tatsächliche Ausführung

Expliziter Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch `research/life-93-night-20261003`, live HEAD `a199581c1749a692d4610795ea98ee4850c44724`. Der neue Exporthelfer lag als Arbeitsbaumfassung vor. Eingabepins vor/nach identisch:

| Eingabe | SHA256 |
| --- | --- |
| `pipeline/aggregate_export.py` | `fe4a54aa13297758bb76e0933a7ae6ea6338abbc4ea953ae7ed9a5ede70d3cfb` |
| `pipeline/r_runtime.py` | `40168392ac69960d2b532f721aaaca4abc82317f8304f7145056537d8a901fce` |
| `reports/loop/aggregate-publication-contract.json` | `5697f76078548ee5620aeddbb8c2d6741a90b3032e9d8610e5137f0cf58486a2` |
| erlaubtes erfundenes Root-Entwicklungsaggregat | `6bf81743ddc8c884950184666d578ac574037eeb1207c717152e51e26fe6c4a2` |

Ich las nur den neuen Helfer, die relevanten öffentlichen Runtime-Grenzen, den Veröffentlichungsvertrag und das ausdrücklich synthetische Aggregat unter `outputs/loop/r-runtime/root-development-correlation-round1-001/`. Keine aktuellen fremden Urteile, echten ESS-Roh-/Privatdateien, Antworten oder privaten Runreceipts wurden geöffnet. Eigene Testprojekte liegen vollständig unter `outputs/loop/aggregate-export-review/`; ihre darin nachgebildeten `data/local`- und `reports`-Pfade sind erfundene Testartefakte. Keine gemeinsame Forschungsdatei oder echte öffentliche Phasenausgabe wurde geschrieben. Beide Methodenberichte blieben unverändert. Keine Installation, Gitmutation oder pnpm-Ausführung.

Tatsächliche Befehle im genannten Worktree:

```text
python3 pipeline/aggregate_export.py --help
PYTHONDONTWRITEBYTECODE=1 python3 -m pipeline.aggregate_export --help
PYTHONDONTWRITEBYTECODE=1 python3 outputs/loop/aggregate-export-review/probes.py
PYTHONDONTWRITEBYTECODE=1 python3 outputs/loop/aggregate-export-review/probes-v2.py
```

Der direkte Pfadaufruf scheitert vor der Argumentverarbeitung an `ModuleNotFoundError: No module named 'pipeline'`, Zeile 18. Der Modulaufruf `python3 -m pipeline.aggregate_export` ist ausführbar und kann als konkrete Aufrufroute dienen. Das ist kein zusätzlicher erheblicher Forschungsblocker.

Beide eigenen Probeprogramme liefen mit Exit 0; das bedeutet erfolgreiche Erfassung der Proben, nicht Bestehen aller erwarteten Sperren. Der erste Exportfluss-Test war zu früh an `PRIVATE_PARENT_MODE` gestoppt, weil ein von meinem Treiber angelegter Zwischenordner 0755 hatte. Der unveränderte erste Befund bleibt in `probe-result.json` erhalten. `probes-v2.py` nutzt neue eigene Testordner mit korrigierter 0700-Grenze. Sein Originalergebnis steht in `probe-result-v2.json`. Treiberhashes, Eingabepins und Scope stehen in `execution-receipt.json` sowie `pins-before.json`/`pins-after.json`.

## AE-01: bekannte Wörter ersetzen kein exaktes Aggregatschema

**Schwere:** erheblich für die automatische Veröffentlichungssperre. **Fundstellen:** `aggregate_export.py:56–88`, besonders die globale Schlüsselprüfung Zeilen 70–72 und universelle Listenbegrenzung Zeilen 76–79; außerdem die unvollständige Pinprüfung Zeilen 107–108.

Nur die oberste Ebene sowie wenige Moment-/Modellfelder sind exakt gebunden. Unterhalb davon darf jedes global bekannte Wort an jedem Ort auftreten. Jede Liste bis Länge 87 wird unabhängig von ihrer Bedeutung akzeptiert. Pflichtfelder, Zahlen-/Containerarten und skalenabhängige Matrixgrößen fehlen. Der Export kopiert die angenommene Struktur anschließend unverändert.

**Konkrete synthetische Gegenproben:**

- Unter `models.M3.scores.H.raw_components.item_covariance` ersetzte ich die erwartete 3×3-Kovarianz durch zwanzig erfundene Neuner-Antwortvektoren. `validate()` akzeptiert sie. Auch der vollständige Exportfluss mit synthetisch nachgebildetem erfolgreichen A-Receipt exportiert diese Vektoren in die eigene Testausgabe.
- `counts.values` mit zehn erfundenen Neuner-Vektoren und `counts.item_missing_counts.B34` als Antwortliste werden ebenfalls angenommen. Beide verletzen den bezeichneten Aggregatvertrag, obwohl ihre Schlüssel global bekannt und ihre Zahlen endlich sind.
- Das Entfernen des Pflichtcontainers `models.M3.scores` wird angenommen.
- Ein leeres `source_code_pins` wird angenommen und tatsächlich exportiert. Die Prüfung `all(... for k in aggregate['source_code_pins'])` ist bei leerer Menge wahr; die öffentliche Ausgabe verliert dadurch ihre vier vorgesehenen Entwicklungs-Codebindungen.

Dies behauptet keine tatsächliche ESS-Offenlegung oder einen Fehler der unveränderten geprüften R-Ausgabe. Es zeigt, dass der zusätzliche Helfer die verlangte exakte Schema-/Versehentlichkeitsgrenze selbst nicht hält. Die Gegenproben benötigen keine verschlüsselten Payloads, Secrets oder Umgehung fremder Dateirechte.

**Genau blockiert:** Annahme und automatische Anwendung dieses neuen Exporthelfers als exakte öffentliche Aggregatsperre. A-Import, private A-Entwicklung und unabhängige Arbeit werden dadurch nicht neu blockiert. Jede reale Veröffentlichung bleibt zusätzlich eine konkrete Prüfung durch den Koordinator.

**Minimale Korrektur:** erlaubte und erforderliche Felder je Pfad und Statuszweig festlegen; unbekannte oder falsch platzierte Felder stoppen. Counts müssen die vorgesehenen skalaren Ganzzahlen tragen. Moment-, EFA-, CFA- und Scorearrays müssen ihre konkreten Item-/Faktor-/Schwellengrößen haben, zum Beispiel H-Kovarianz 3×3, statt einer allgemeinen 87er-Grenze. Erfolgs-/Fehlerzweige erhalten ihre jeweiligen Pflichtfelder. `source_code_pins` muss genau die vier vorgesehenen Entwicklungsartefakte mit gültigen SHA256 und vollständigem Receiptabgleich enthalten. Die gezeigten Injektionen müssen danach vor jeder öffentlichen Kopie stoppen; das vorhandene synthetische Original muss weiter akzeptiert werden. Kein Statistik-Gate oder wissenschaftlicher Grenzwert muss dafür ergänzt werden.

## Grenzen, die bereits tragen

Der Aufruf von `runtime.preflight_private(root)` steht vor dem privaten Runreceipt und vor dem Aggregatlesen. Der öffentliche Runtime prüft zuvor Gate-/Review-/Remote-Tag-/Codebindungen; anschließend bindet er Quelle, private Eingabereceipts, Zuteilung und A-Input. Der neue Helfer verlangt `development-a`, Exit 0, Runtime-Probe 0, korrektes Label, identische aktuelle Autorisierung und identische aktuelle Entwicklungscodehashes, bevor er das Aggregat öffnet. Danach bindet er die Aggregatbytes an das Runinventar. Der zweite Preflight steht vor der öffentlichen Ausgabe; bestehende Ziele werden nicht überschrieben.

In meinem eigenen nachgebildeten Exportfluss wurde der reale Preflight ausdrücklich gemockt. Damit wurden keine echten Tags oder privaten ESS-Eingaben geprüft. Die Ereignisfolge des Normalfalls lautet `preflight → aggregate-read → preflight`. Falscher Runstage, Fehlerexit, fehlgeschlagene Runtime-Probe, Autorisierungsdrift und Codedrift stoppen jeweils ohne Aggregatlesen oder Ausgabe. Falscher Aggregathash stoppt vor semantischem JSON-Lesen. Diese sechs negativen Flussproben bestanden. Das normale erfundene Aggregat wird mit ESS-Zitation, Datenlizenz und Änderungen ausgegeben. Unbekannte neue Schlüssel, PSU-Listen im bezeichneten Countfeld, NaN, ein privater Pfadstring und eine Liste über 87 werden schon jetzt verworfen.

Mutable Receipts und das gemeinsame Dateisystem bleiben eine benannte Vertrauensgrenze. Die Rolle prüft einen Schutz gegen versehentliche falsche Struktur und Offenlegung, keine absolute adversarielle Sicherheit. Gleiche Codex-Modellfamilie und mögliche gemeinsame Fehler bleiben offen. Nach gezielter Schema-/Pin-Korrektur genügt eine Nachprüfung dieser Fälle; ein neues Methoden-Gesamtaudit ist nicht erforderlich.
