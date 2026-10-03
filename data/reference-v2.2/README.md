# Historische ESS-Referenzen v2.2

Die fünf JSON-Dateien sind getrennte, geprüfte historische Kategorienanteile für Deutschland nach dem [Analyseplan v2.2](../../docs/analyseplan-v2.2.md). Keine Rohdaten, keine gemeinsame Personenmatrix und keine aktuelle Bevölkerungsnorm.

Inhalt:

- Einzelreferenzen für alle 62 Fragen des Profils: die 43 Fragen aus v2 und die 19 neuen Fragen aus v2.2. 59 tragen Zahlen. `ESS10SCe03_2:cttresa`, `ESS8e02_3:elghydr` und `ESS8e02_3:elgnuc` bleiben nach der Regel 100/5 ohne Zahlen.
- Gruppenpaare nach erinnerter Zweitstimme mit den Gruppendefinitionen aus v2.1 für ESS5, ESS8 und ESS9. 96 Paare tragen Zahlen, 194 bleiben ohne Zahlen. ESS10- und ESS11-Gruppen sind ausgeschlossen.
- Für jede Kategorie mit einem Anteil zwischen 0 und 1 ein 95-%-Bereich (Taylor-Linearisierung, Logit-Intervall, Freiheitsgrade aus PSUs minus Strata). ESS9, ESS10 Self-completion und ESS11 enthalten das Design in den Daten. Für ESS5 und ESS8 stammen Strata und PSUs aus den Designdateien des ESS (SDDF), siehe `designSource`.

Der Bereich beschreibt nur die Unsicherheit durch die damalige Zufallsstichprobe unter vereinfachenden Annahmen. Er enthält keinen Zeitabstand, keinen Moduswechsel, keine Nichtteilnahme und keinen neuen Fragekontext. Nahe 0 und 100 % kann er die Unsicherheit unterschätzen.

Herkunft und Prüfung: [Laufbeleg](../../reports/claude/v22-laufbeleg.json), [Ergebnisprüfung Runde 1](../../reports/claude/pruefungen/E1-ergebnis-v22.md) und [Runde 2](../../reports/claude/pruefungen/E1-runde2-ergebnis-v22.md) (KI-Reviews durch Codex), [Exportentscheidung](../../reports/claude/export-v22-entscheidung.json), [Bericht](../../reports/phasen/04-politikprofil-v22.md). Erzeugt mit `python3 pipeline/v22/export_v22.py release`. Die Anteile der in v2 und v2.1 veröffentlichten Referenzen sind unverändert. Die Dateien unter `data/reference-v2/` und `data/reference-groups-v21/` bleiben als historische Fassungen erhalten.

Datenquelle: European Social Survey European Research Infrastructure (ESS ERIC); Archiv Sikt – Norwegian Agency for Shared Services in Education and Research. Diese Datenableitungen stehen unter [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Rohdaten werden weder mitgeliefert noch in die Website kopiert.

- ESS5, Ausgabe 3.6: [Datensatz](https://doi.org/10.21338/ess5e03_6). Designdatei: ESS5 SDDF Deutschland (`ESS5_DE_SDDF.sav`).
- ESS8, Ausgabe 2.3: [Datensatz](https://doi.org/10.21338/ess8e02_3). Designdatei: ESS8 SDDF (`ESS8SDDFe01_1.csv`).
- ESS9, Ausgabe 3.3: [Datensatz](https://doi.org/10.21338/ess9e03_3).
- ESS10 Self-completion, Ausgabe 3.2: [Datensatz](https://doi.org/10.21338/ess10sce03_2).
- ESS11, Ausgabe 4.2: [Datensatz](https://doi.org/10.21338/ess11e04_2).

Die Exportentscheidung ist keine Freigabe der Website, des Tests oder einer Veröffentlichung durch Steven und keine methodische Validierung.
