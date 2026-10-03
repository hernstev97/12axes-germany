# Phase 0: technische Erfassung der bereitgestellten Datei

Stand 2026-10-03. Lokale Vorbereitung, keine Analyse oder methodische Abnahme. Der Forschungsplan bleibt Arbeitsfassung 0.1. Steven stellte die Datei bereit; Herkunft und Bedingungen des persönlichen Downloads wurden nicht stellvertretend bestätigt.

## Tatsächlich geprüft

| Merkmal                                | Befund                                                                                                                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pfad                                   | `data/raw/ess11-ed4.2/ESS11e04_2.csv`                                                                                                                                                       |
| Größe                                  | 82.693.775 Bytes                                                                                                                                                                            |
| SHA-256                                | `4b0bfa73fa86bcf9f868b0a6145f96504a40d7e3f2deeb3e822555993ab32dc8`                                                                                                                          |
| Formatprüfung                          | Kommagetrennt, lesbar mit `utf-8-sig`; 691 eindeutige Headerfelder. Erster Datensatz besitzt dieselbe Feldzahl.                                                                             |
| Globale Metadaten aus erstem Datensatz | `essround = 11`, `edition = 4.2`, `proddate = 02.07.2026`. Keine Prüfung über sämtliche Datensätze.                                                                                         |
| Erwartete Spalten                      | `anweight`, `pspwght`, `psu`, `stratum`, Länder-/ID-/Metadaten- und dokumentierte Wahl-/Links-rechts-Felder im Header vorhanden. Nur Vorhandensein geprüft, keine Personenwerte ausgegeben. |
| Git                                    | Datei ignoriert, nicht getrackt; Datei während der Prüfung nicht geändert.                                                                                                                  |
| Lokaler Prüfbeleg                      | `data/local/ess11-file-arrival-2026-10-03.json`, ebenfalls außerhalb von Git.                                                                                                               |

Erfasst am 2026-10-02 um 23:56:39 UTC, entsprechend 2026-10-03 um 01:56:39 in Berlin. Die Prüfung nutzte ein lokales Python-Skript für Datei-Hash, Header und eine feste Positivliste globaler Metadaten; Git-Ausschluss mit `git check-ignore` und Tracking mit `git ls-files` geprüft. Stand der Dokumentation im [Arbeitsmanifest](00-recherche-2026-10-03-stand.json).

## Grenzen und Zugriff

Zum Metadatenlesen wurde der erste CSV-Datensatz lokal verarbeitet. Nur die drei globalen Metadatenfelder gelangten in die Tool-Ausgabe. Keine Antworten oder Personenkennungen ausgegeben; keine Verteilungen, Gruppenzahlen, Landfilter, Scores oder A/B-Aufteilung berechnet. Die Mess-/Wahlvariablen wurden ausschließlich anhand ihrer Headernamen auf Vorhandensein geprüft.

Die Prüfung bestätigt einen lokal vorhandenen, zur angeforderten Ausgabe passenden Dateistand. Sie prüft weder alle CSV-Datensätze noch Vollständigkeit und Übereinstimmung mit einer offiziellen Referenzprüfsumme. Die Datei bleibt unverändert. Keine Aussage zur Tragfähigkeit von Dimensionen oder Gruppenvergleichen.

Die methodische Freigabe und der vollständig begründete, öffentlich eingefrorene Analyseplan bleiben offen. Öffentliche Originalfragen und Literatur können unabhängig davon weiter recherchiert werden.
