# Zweite Dekodierung der ESS5-Designdatei

Stand: 4. Oktober 2026. Verfasst von Claude. Schließt die Prüfgrenze aus E1 Runde 2 und aus dem Abschlussbericht (Abschnitt 9, Punkt 7): Designlauf und SDDF-Gegenprobe lasen `ESS5_DE_SDDF.sav` beide mit dem eigenen Leser `pipeline/v22/sav.py`.

## Vorgehen

`sav_gegenprobe.py` liest dieselbe Datei mit pyreadstat 1.3.6. pyreadstat nutzt die C-Bibliothek ReadStat, die unabhängig vom Projektcode entstanden ist. Die Umgebung ist isoliert und nicht im Repository: `uv venv outputs/claude/venv-readstat` (Python 3.11.15, von uv verwaltet), darin `pyreadstat 1.3.6` und `pandas 3.0.6`. Systemweit wurde nichts installiert. Das Skript gibt nur Zählungen und Abweichungen aus. Die privaten Läufe liest es nur. Ergebnis: [sav-gegenprobe.json](sav-gegenprobe.json).

## Ergebnis

| Prüfung                                                     | Ergebnis                                                                                                  |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Metadaten laut ReadStat                                     | 3031 Zeilen, sechs Variablen, Kodierung UTF-8, keine Variablen- oder Wertebeschriftungen                  |
| CNTRY, IDNO, PSU, SAMPPOIN, STRATIFY, PROB je Zeile         | in allen 3031 Zeilen gleich zwischen ReadStat und `sav.py`, auch die leeren SAMPPOIN-Werte                |
| Design laut ReadStat                                        | nur DE, 3031 eindeutige IDNO, 2 Strata, 168 PSUs, jede PSU in genau einem Stratum                         |
| Zuordnung zur ESS5-Hauptdatei (CSV-Leser der Kontrollrechnung V1) | 3031 von 3031 deutschen Fällen, keine Fälle nur in einer der beiden Dateien                           |
| Standardfehler mit ReadStat-Design                          | 32 Referenzen, 202 Kategorien. Größte Abweichung der Anteile 1,1e-16, der Standardfehler 0. 166 Design-Freiheitsgrade |

## Tatsächliche Unabhängigkeit

| Bestandteil                    | Designlauf (`run_v22_sddf.py`)  | Diese Gegenprobe                                       | Gemeinsam                    |
| ------------------------------ | ------------------------------- | ------------------------------------------------------ | ---------------------------- |
| Lesen der SPSS-Datei           | `sav.py` (Claude)               | ReadStat über pyreadstat                               | nichts                       |
| Lesen der ESS5-Hauptdatei      | `run_v22.read_de`               | `kontrolle.read_de` (Kontrollrechnung V1)              | Python-Modul `csv`           |
| Kodierung der Antworten        | `run_v22.classify`              | `kontrolle.classify`                                   | Vertragsdateien              |
| Gruppenbildung                 | `run_v22.vote_party_states`     | eigene Zeile in diesem Skript                          | Gruppenvertrag v2.1          |
| Anteile und Standardfehler     | `pipeline/v22/survey.py` (Claude) | `pipeline/policy_reference_v2.categorical_reference` (Codex) | Formel aus Plan v2.2, 4.2 |
| Eingabedaten                   | ESS5-CSV, SDDF                  | dieselben Dateien                                      | Dateien und ihre Hashes      |

Gemeinsam bleiben die Datendateien, die Vertragsdateien mit Codes und Gruppendefinitionen, das Verfahren aus Plan v2.2 und Claude als Verfasser beider Skripte. Ein Fehler in den Verträgen oder im Verfahren selbst würde in beiden Rechnungen gleich auftreten. Die Intervallgrenzen (t-Quantil, Logit-Transformation) vergleicht diese Gegenprobe nicht. Sie folgen aus dem Standardfehler mit `survey.py`. Die Ergebnisprüfung E1 Runde 2 hat ihre Symmetrie auf der Logitskala geprüft.

Damit ist die ESS5-Designdatei zweimal unabhängig dekodiert. Für ESS8 (CSV) war die Gegenprobe schon vorher unabhängig vom Leser des Designlaufs.
