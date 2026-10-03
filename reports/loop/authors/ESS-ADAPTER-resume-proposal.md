# ESS-Momentadapter für die Fortsetzung

Autorenbericht vom 3. Oktober 2026, keine Erstprüfung und keine empirische Freigabe. Geschrieben wurden ausschließlich dieser Bericht und `outputs/loop/resume-adapter/`. Keine ESS-Eingabe, Antwort, Personenkennung, A/B-Datei oder Datei unter `data/raw/` beziehungsweise `data/local/` wurde gelesen. Keine Installation, Conda-Ausführung, Auth-Arbeit, weiteren Agents, Commits oder gemeinsamen Pipeline-/Forschungsänderungen.

## Gelieferter Vertrag

[ordinal-adapter.R](../../../outputs/loop/resume-adapter/ordinal-adapter.R) enthält einen kleinen funktionsbasierten Adapter. [README](../../../outputs/loop/resume-adapter/README.md) nennt vollständigen Nutzungsvertrag, Formeln, Stopps und Ausgabegrenzen. Vor Einsatz bleiben tatsächliches Kategorienmanifest, Version-/Designkodierung, Missing-Umschlüsselung und autorisierte Datenzugriffe festzulegen und zu prüfen. Das Neunitemset wird hier weder ausgewählt noch freigegeben.

Eingabe ist ein `data.frame` mit exakt neun Items in Manifestordnung, ein explizites geordnetes Kategorienmanifest und der vollständige Designrahmen mit Gewicht, PSU, Stratum und logischer Domäne. Eine gemeinsame Maske ist `domain & complete.cases(all9)`. Alle ursprünglichen Designfälle müssen endliche positive Gewichte und vollständige Designfelder haben. PSU-Kennungen in mehreren Strata, Singleton-Strata, fehlende Kategorien, unzureichende Design-df, unzureichende/rangdefiziente Momentkovarianz und numerische Grenzlösungen stoppen. Der Adapter rekonstruiert keine Kennungen, PSUs, Kategorieordnung oder Singletonregel.

Der Momentvertrag ordnet Schwellen itemweise, danach die Korrelationen spaltenweise im unteren Dreieck. Alle Gamma-/DWLS-Zeilen und -Spalten müssen dieselben Labels tragen. Die Synthetik hat 51 Schwellen und 36 Korrelationen, zusammen 87 Momente. Diese Zahl gilt für ihre 5/4/11 Kategorien in drei erfundenen Dreierblöcken.

## IF und vollständiger Design-Sandwich

Die gewichteten marginalen CDF-Verhältnisschätzer liefern Probit-Schwellen. Jede Polychorik löst den gewichteten bivariaten Rechteckscore bei diesen Schwellen. Der eigene gestapelte beobachtete Jacobian enthält die Schwelle→Korrelation-Korrektur; zentrale Score-Ableitungen verwenden Schritt 1e-5. Rechteckwahrscheinlichkeiten kommen aus pbivnorm 0.6.0, ihre Rho-Ableitung aus den vier bivariaten Normaldichten. Die Formeln stehen unmittelbar neben Code und Vertrag. Der native lavaan-OPG-Bread wird nicht als genaue beobachtete IF-Ableitung ausgegeben.

Ausgeschlossene Fälle erhalten exakt null. Alle PSUs bleiben im ursprünglichen Stratum erhalten, auch wenn eine PSU keinen vollständigen Domänenfall hat. PSU-Summen werden innerhalb des vollständigen Stratums zentriert, mit Faktor `G_h/(G_h-1)` kreuzmultipliziert und über alle Strata addiert. Das gesamte gemeinsame Gamma, einschließlich Schwellen-/Korrelations-Kreuzkovarianzen, ist `nComplete * CovMoments`. Ohne FPC ist dies eine Ultimate-PSU-Approximation mit Zurücklegen und festen Gewichten. Exakte PPS-WOR-Varianz, Kalibrierungsparameter-Unsicherheit und tatsächlicher ESS-Designzuschnitt sind damit nicht geprüft.

Die bisherige positive lavaan-DWLS-Diagonale bleibt die Punktmetrik. Der eigene beobachtete Jacobian liefert die externe inferentielle Gamma. Die entsprechende native Skalierung ist in der gepinnten [lav_samplestats.R](../../../outputs/loop/software-author/sources/lavaan/R/lav_samplestats.R), Zeilen 1402–1405, nachlesbar. Eigene gewichtete Punkte werden zusätzlich mit den nativen Momenten verglichen. `oa_fit` importiert Summary-Momente, benanntes `th.idx`, Nullmittel auf standardisierter latenter Antwortskala, Fallzahl, Gamma und DWLS; keine Fallzeilen. Tatsächlich gespeicherte Labels/Zahlen und beide Matrizen werden nach jedem CFA-/EFA-Lauf geprüft. Kein behaupteter numerisch identischer Mplus-COMPLEX-Lauf.

## Tatsächliche synthetische Ergebnisse

[Vorabplan](../../../outputs/loop/resume-adapter/plan-before-run.md), [Testcode](../../../outputs/loop/resume-adapter/test-adapter.R), [finaler Lauf](../../../outputs/loop/resume-adapter/test-004-result.json) und [Kommando/Umgebung/Hashes](../../../outputs/loop/resume-adapter/test-004-command.json) halten die Ausführung fest. 2880 erfundene Fälle, 192 PSUs, vier Strata, 2767 vollständige Domänenfälle. Vier ganze PSUs sind ausgeschlossen und bleiben Nullbeiträge; weitere synthetische Missing-Fälle betreffen alle neun Items. Gewichte sind positiv und unabhängig erzeugt.

Der finale Lauf besteht 35 enge Checks ohne Warnung:

| Ausgeführte Prüfung | Ergebnis |
| --- | --- |
| Echte zentrale Gewichtsperturbation: drei einzelne Fälle, kombinierter Kontrast, glatte kombinierte Richtung, gemeinsamer Gewichtsfaktor und ausgeschlossener Fall; je zwei Schritte | 14 Gegenprüfungen bestehen. Alle vollständigen Gewichte und gemeinsamen Nenner werden neu normiert. Größter Schwellen-Ableitungsfehler 6.005e-11, Korrelationsfehler 5.956e-11. Vorabgrenzen 2e-7/2e-6. |
| Gemeinsame Gewichtsskalierung mit Faktor17 | Moment- und IF-Abweichung jeweils0. |
| Eigene einfache Handrechnung der Jointkovarianz von Ratio-Mittel und zwei CDFs | Unabhängige skalare Schleifen über alle Design-PSUs und Strata. Größte Abweichung 1.355e-20. |
| Manifest/Maske/Labelvertrag/Null-PSUs | 87 konsistente Labels; vollständige Neunitemmaske; alle ausgeschlossenen Fallbeiträge0; vier Null-PSUs erhalten. |
| Native gewichtete Punkte | Größte Abweichung 3.029e-8, unter der Grenze1e-6. |
| Externer Summary-Import, Konvergenz/Postcheck und Parameterkovarianz | CFA mit drei korrelierten Faktoren df24; echte EFA1/2/3 mit df27/19/12. Geomin oblique,30 Starts,Epsilon0.001. Moment/Gamma/DWLS-Import jeweils nachgeprüft, Toleranz1e-7. |
| Stopps/Ausgabe | Achtitemmanifest, Null-/unendliche Gewichte, PSU-Nesting, Singleton, Design-df, fehlende Kategorien, ungültige Kategorien, fehlende Domäne und gesättigtes Modell werden gestoppt. Öffentliche Ausgabe ist feste Aggregat-Whitelist. |

Die Gegenprüfung verändert die tatsächlichen gewichteten Momente erneut und vergleicht sie mit IF-Vorhersagen. Sie vergleicht keine zwei Kopien derselben IF-Formel. Ihre Rechteck-CDF-Basis ist weiterhin dieselbe pbivnorm-Bibliothek; die Tests ersetzen keine unabhängige publizierte Vollherleitung, empirische Abdeckungsprüfung oder Gegenprüfung des realen ESS-Kategorien-/Designvertrags.

## Erhaltene Fehlläufe und Grenzen

`test-001`, `test-002`, `test-003` und beide Diagnoseergebnisse bleiben unverändert erhalten. Ihre produktiven und Test-Codefassungen sowie die per SHA256 zurückgebundenen Launcherfassungen sind im eigenen Outputordner archiviert. Test001 stoppte im frühen Momentweg mit festem Bibliotheksfehlercode; anschließend wurde die breite Rho-Klammer durch die kleinste numerisch gültige Klammer ersetzt. Test002 stoppte beim Summary-Import; die Diagnose zeigte fehlende Schwellen-Indexnamen. Test003 stoppte mit Bibliothekswarnung; die gesonderte Diagnose zeigte fehlendes `sample_mean` und den nicht verfügbaren `stats::vcov`-Dispatch ohne angehängtes lavaan. Die finale Fassung liefert die latenten Nullmittel explizit und fragt die Parameterkovarianz über `lavInspect` ab. Kein Fehllauf wird durch den späteren Erfolg umetikettiert.

`oa_public` exportiert nur feste erlaubte Aggregate. Standarddruck ist knapp. Bibliotheks-stdout/Warnungen/Meldungen werden unterdrückt, Fehlertexte enthalten feste Codes. Das private Objekt bleibt im lokalen Speicher und enthält Masken, umkodierte Fälle und IF-Beiträge. Allgemeine Dumps/Serialisierung dieses privaten Objekts sind ausdrücklich kein erlaubter öffentlicher Export. Das Summary-Fitobjekt enthält keine Rohfallzeilen.

Die Laufzeit ist auf R4.5.3, lavaan0.7.2 und pbivnorm0.6.0 gebunden. Direkter vorhandener Rscript-ELF, SHA256 vor/nach jedem Lauf `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`, HOME unverändert `/home/stevenh`; ausschließlich eigene Temp-/Cache-/XDG-Pfade. Die zwölf bezeichneten Child-Dateischreibrechte sind durch Landlock auf den eigenen Ordner und write-file auf `/dev/null` beschränkt. Keine vollständige Lese-/Netz-/Supervisor-/PC-Isolation. [Hashindex](../../../outputs/loop/resume-adapter/artifact-index.json) und [Inputbindungen](../../../outputs/loop/resume-adapter/input-bindings.json) binden Code, Versionen, vorherige Inputs und Ergebnisartefakte.

Keine reale ESS-Momentberechnung, Missing-Biasprüfung, Invarianz, persönliche Intervalle, A/B-Stabilität, empirische Güte oder methodische Abnahme. Der Koordinator führt `pnpm check` der gemeinsamen Prüffassung aus. Ein eigener Build mit anderen Schreiborten wurde innerhalb dieses begrenzten Autorenauftrags nicht gestartet.
