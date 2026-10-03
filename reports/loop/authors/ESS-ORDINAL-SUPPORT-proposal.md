# Ordinale Modelldiagnostik vor Empirie

Autorenfassung vom 3. Oktober 2026. Keine Übergangsprüfung, Kriterienfestschreibung oder wissenschaftliche Freigabe. Geschrieben wurden nur `pipeline/ordinal/support.R`, `test-support.R`, `run_r.py`, die gesondert autorisierte `adapter_v2.R`, dieser Bericht und `outputs/loop/resume-ordinal-support/`. Keine Datei unter `data/raw/` oder `data/local/`, keine ESS-Antwort, Personenkennung, A/B-Datei oder gesperrte Vergleichsvariable gelesen. Keine Installation, Tags, Commits, Pushes oder weiteren Agents. Der Koordinator führt `pnpm check` der gemeinsamen Fassung aus.

## Ausführbare Funktionen

[`support.R`](../../../pipeline/ordinal/support.R) ergänzt den vorhandenen Adapter. `oa_fixed_metric(adapter)` liefert eine Kopie mit exakt gelabeltem `W=I`; das Eingabeobjekt und `adapter.R` bleiben erhalten. Diese Summary-Punktschätzung ist ungewichtete kleinste Quadrate auf der Momentliste aus Schwellen und Polychoriken. lavaans nomineller DWLS/WLSMV-Aufruf beschreibt hier den verwendeten Rechenweg, keine DWLS-Diagonalmetrik der Punkte. `os_sandwich(adapter, fit)` verwendet standardmäßig den beobachteten Schätzgleichungs-Jacobian. Der ausdrücklich getrennte Parameter `bread_method="expected"` berechnet die modellrichtigkeitsbedingte Projektion zum Vergleich.

`os_standardized` liefert tatsächlich standardisierte Ladungen und Faktorkorrelationen mit normalen Delta-Intervallen. `os_score` liefert beobachtete 0–1-Score-Reliabilität, Mittelwert, beobachtete/erklärte/Fehlervarianz und modellimplizierte Itemkovarianzbeiträge, jeweils samt Design-SE/Intervall. Dreier-, Sechser- und Neunerscores auf demselben gemeinsamen Neunitemmodell sind ausführbar. Feste umgekehrte Polungen sind über explizite monotone Kategorie-Scores darstellbar. `os_raw_score` liefert daneben die tatsächliche gewichtete Rohscore-Kovarianz und Dominanz mit eigenem Taylor-Sandwich auf der vollständigen Adapter-Domäne. Eine später andere Dreier-/Normmaske braucht ihre eigene Domänenrechnung.

`os_residual_rms` berechnet RMS über die 36 residualen Polychoriken und dessen passende Design-Delta-Unsicherheit. Rotierte EFA-SE werden mit festem Fehlercode gestoppt. Die echte EFA-Punktschätzung wird separat ausgeführt. Alle Modelle bleiben auf identifizierte, unconstrained Single-Group-CFA mit THETA, positiver latenter Kovarianz, positiver Residualvarianz, lokaler Unabhängigkeit und ohne latente Regression begrenzt. Gleichheits-/Ungleichheitsrestriktionen, Mehrgruppen-/Mehrebenenmodelle und rotierte EFA-Parameterinferenz sind nicht implementiert.

Der bisherige konservative Adaptervertrag verlangt vollständig positive definite Momentkovarianz, Gamma-Rang 87 und mindestens 87 Design-df. Dieser begrenzte Auftrag hat ihn nicht erweitert. Das ist keine allgemeine methodische Begründung, weshalb singuläres Gesamt-Gamma jede identifizierte Parameterinferenz ausschließen müsste; die tatsächliche Zulassungsregel gehört in den Review.

## Schätzgleichung und Unsicherheit

Mit beobachteten Momenten `s`, Modellmomenten `m(beta)` und `D = dm/dbeta` lautet die bei festem `W` verwendete Schätzgleichung `psi = D' W [s-m(beta)]`. Der Hauptweg differenziert diese ganze Gleichung nach den freien Parametern. Der zentrale numerische Jacobian `J` enthält damit die residualabhängige Ableitung von `D`. `K = -J^-1 D'W` und `Vbeta = K Cov(s) K'`. Die 87 Momentlabels und alle freien Parameterlabels werden gegen den tatsächlich importierten lavaan-Fit geprüft; der lokale Parameter-Setter aktualisiert auch die THETA-Standardisierung. Die gemeinsame Momentkovarianz stammt aus dem eigenen beobachteten Adapter-Jacobian mit vollständiger Stratum-/PSU-Zentrierung. Ein natives OPG-Gamma wird nicht als Ersatz eingesetzt.

Der Vergleichsweg `Kexpected = (D'WD)^-1 D'W` lässt residuale Krümmung weg. Er ist bei korrektem Modell asymptotisch passend, aber kein allgemeiner Jacobian eines missspezifizierten Fitminimierers. Am tatsächlichen synthetischen Punkt lag seine Richtungsableitung bis 0.6146 neben den festen Identitäts-Refits. Diese Differenz bleibt sichtbar. Der Native-SE-Abgleich prüft ausschließlich diesen getrennten erwarteten Weg. lavaan 0.7.2 teilt die nicht-ML-WLS-Kovarianz durch `N-ngroups`; bei einer Gruppe erklärt deshalb `N/(N-1)` den endlichen Unterschied zu `K Cov(s) K'`, unabhängig von `gamma.vcov.mplus`.

Für Residuen gilt die tatsächliche lokale Abbildung `A = I-DK`. Ihre Kovarianz ist `A Cov(s) A'`. Bei `RMS = sqrt(mean(r^2))` ist die Ableitung nach den Korrelationsresiduen `r/(36 RMS)`. RMS unter der benannten numerischen Nulltoleranz erhält `DELTA_UNDEFINED_NEAR_ZERO` und keine SE/CI. Die Norm ist bei null nicht differenzierbar; das Modul erzeugt dort keine falsche Nullunsicherheit. Die numerische Toleranz ist kein Gütekriterium.

Alle ausgegebenen Intervalle sind rohe normale Intervalle `estimate +/- qnorm(.975)*designSE`, ohne Trunkierung. Sie berücksichtigen im vorgegebenen Rahmen die geschätzten Moment- und Modellparameter, nicht Modellwahl, Itemwahl, Rotationsunsicherheit, eine geprüfte kleine-PSU-Abdeckung oder persönliche Messunsicherheit. Ultimate-PSU mit Zurücklegen, feste Gewichte und kein FPC/PPS-WOR bleiben Grenzen. Kalibrierungs-/Nichtantwortparameterunsicherheit fehlt.

Der diagnostische DWLS-Weg hält seine aus der Stichprobe gewonnene Punktdiagonale bei allen Perturbationen fest. Unter Missspezifikation ist damit die zusätzliche Zufälligkeit eines bei jedem Stichprobenzug neu geschätzten `W` nicht berechnet. Der vor Dateneinsicht vorgeschlagene feste Identitätsweg beseitigt genau diese zusätzliche W-Ableitung. Er optimiert die Momentgewichtung nicht; höhere Effizienz oder identische Punkte gegenüber DWLS sind nicht belegt. Die Wahl von `W=I` bleibt eine Entscheidung des Koordinators und der Übergangsprüfung.

## Beobachteter Score und Dominanz

Für ein ordinales Item ist `x_j = c_j0 + sum_a Delta(c_ja) I(Z_j>t_ja)`. Daher folgt die beobachtete Itemkovarianz aus den Kategorieinkrementen und `Phi2(t_ia,t_jb,rho)-Phi(t_ia)Phi(t_jb)`. Der Modellnenner verwendet die vollständige standardisierte Antwortkovarianz. Der Zähler ersetzt deren Korrelation durch die standardisierte gemeinsame Faktor-Kovarianz `Lambda Phi Lambda'`; auch dessen Diagonale bleibt unter eins. Das entspricht zwei unabhängigen Residualziehungen bei gemeinsamen Faktoren und berechnet `Var(E[S|alle eta]) / Var(S)`. Es ist keine Reliabilität latenter Antwortvariablen.

Die eigenen bivariaten CDF-Summen verwenden pbivnorm. Die tatsächlich ausgeführte semTools-Gegenrechnung verwendet `compRelSEM(..., ord.scale=TRUE, obs.var=FALSE, W=explizite 1/[k*(Kategorien-1)]-Gewichte)` und dessen mnormt-CDF. Zusätzlich wird jeder getestete Einfaktorscore unabhängig eindimensional über bedingte Normal-Kategorieerwartungen und -varianzen integriert. Der Originalvolltext von Green/Yang wurde für diese Autorenarbeit nicht neu verifiziert; der Software-Oracle und die eigene Herleitung ersetzen keine externe methodische Abnahme.

Die Dominanz ist exakt `Cov(x_j,S)/(k Var(S))`, getrennt als Modellimplikation und rohe gewichtete Rechnung. Die Roh-IF differenziert die zentrierten Verhältnis-Kovarianzen und die Varianz gemeinsam; alle ursprünglichen PSUs einschließlich vier Null-Domänen-PSUs bleiben erhalten. Die Beiträge summieren sich algebraisch zu eins. Sie müssen weder gleich noch bei umgekehrter Polung positiv sein. Gleichgewichtete Items beweisen keine Abwesenheit von Dominanz. Das Modul entscheidet keine Dominanz-, Reliabilitäts- oder RMS-Grenze.

## Tatsächliche Läufe

Die Schicht besteht den [festen Identitätslauf](../../../outputs/loop/resume-ordinal-support/test-fixed-001-result.json) und den [getrennten DWLS-Diagnoselauf](../../../outputs/loop/resume-ordinal-support/test-009-result.json), beide ohne Warnung. Die letzte [integrierte Fassung mit adapter_v2 plus fester Identitätsmetrik](../../../outputs/loop/resume-ordinal-support/test-fixed-v2-001-result.json) besteht ebenfalls 54/54 Checks ohne Warnung. 3840 erfundene Fälle, 192 PSUs, vier Strata, vier vollständig ausgeschlossene PSUs, 3760 vollständige Domänenfälle; Kategorieordnung 5/4/11 in jedem erfundenen Dreierblock. Seed 2026100321. Code, Aufruf, Umgebung, UTC-Zeit und Hashes stehen in den jeweiligen `*-command.json` und im [Hashindex](../../../outputs/loop/resume-ordinal-support/artifact-index.json).

| Enger ausgeführter Check | Fester Identitätsweg | Diagnostischer DWLS-Weg |
| --- | --- | --- |
| Gesamtergebnisse der finalen Fassungen | 54/54 BESTANDEN | 53/53 BESTANDEN |
| CFA M3/M2/M1 und echte externe EFA1/2/3 | Konvergenz/Postcheck; CFA-df24/26/27, EFA-df27/19/12; tatsächliche Momente/Gamma/W geprüft | Gleiche Modellklassen/Importprüfung |
| Native Delta gegen tatsächliche freie Parameterperturbation; beobachteter Jacobian bei 1e-5/2e-5; standardisierte Gradienten | Vorab-Rechentoleranz 2e-5 bestanden | 2e-5 bestanden |
| Echte Summary-Moment-Neufits am missfitbehafteten M3-Punkt, Richtungsableitung gegen beobachtetes K | Maximaler Parameterfehler 1.276e-5 | 1.398e-5 |
| Tatsächliche Neu-Fit-Residualableitung gegen `I-DK` | 7.782e-7 | 6.183e-7 |
| Tatsächliche Neu-Fit-RMS-Ableitung | 1.151e-6 | 1.145e-6 |
| Beobachtete 3-/6-/9-Score-Reliabilität gegen semTools und bedingte Normalintegration | Alle Gegenfälle innerhalb 2e-6; tatsächliche Unterschiede ungefähr Rundungsniveau | Gleiches Ergebnis der Gegenrechnungen |
| Rawscore-Kovarianz/Dominanz gegen unabhängig berechnete unzentrierte zweite Momente | Alle Identitäten innerhalb 1e-10 | Alle innerhalb 1e-10 |
| Nearzero-RMS, inadmissible Kovarianz, rotierte EFA-SE | Explizite Undefined-/Stopcodes | Gleiche Stopps |

Die Refit-Gegenrechnung verwendet BFGS mit `reltol=1e-13`, maximal 20000 Iterationen und echte `+/-0.00025`-Summary-Perturbationen. Der Prüfwert 2e-5 wurde nach früheren Fehlläufen nicht gelockert. Standardisierte Punkte/Gradienten und CIs sind tatsächlich berechnet; keine Ladung oder Konstruktaussage wird dadurch empirisch freigegeben. Zweiter Geomin-Seed, Oblimin-Vergleich, externe Abdeckungsstudie und reale ESS-Läufe wurden hier nicht ausgeführt.

## Begrenzte Adapter-v2-Korrektur

[`adapter.R`](../../../pipeline/ordinal/adapter.R) bleibt bytegleich mit SHA256 `d4db3819c15a8da6c4b11f515de8d939afd13de7970326900577912874726ad3`. Sein erhaltener rho0.95-/11-Kategorien-Gegenfall stoppt `ORDINAL_ADAPTER_RECTANGLE_PROBABILITY`, auch wenn winzige Rechtecke nicht besetzt sind.

Die gesonderte Kandidatenfassung [`adapter_v2.R`](../../../pipeline/ordinal/adapter_v2.R) gibt unbesetzten Zellen exakt null Scorebeitrag. Besetzte Wahrscheinlichkeit `<=1e-12` stoppt weiterhin; keine positive Zellwahrscheinlichkeit wird geklippt, ersetzt oder renormiert. Endlichkeit und Gesamtsumme bleiben geprüft. Ausschließlich bei unbesetzten CDF-Differenzen wird begrenzte Auslöschung bis `-1e-12` zugelassen. Ein alleinstehender Rechteckaufruf ohne Belegungsinformation bleibt streng. Die gleichen endlichen Innenendpunkte bis `|rho|=.98` werden nun einzeln auf numerische Gültigkeit geprüft; nur ein echtes inneres Score-Vorzeichenintervall darf eine Wurzel liefern. Keine Randlösung wird gerettet.

Die v2-Kandidatenfassung besteht [alle 35 unveränderten Baselinechecks](../../../outputs/loop/resume-ordinal-support/test-adapter-v2-001-result.json) und [35 zusätzliche starke Gegenchecks](../../../outputs/loop/resume-ordinal-support/test-strong-v2-001-result.json), jeweils ohne Warnung. Die starken gemeinsamen Neunitemfälle enthalten 5/4/11 Kategorien, rho0.85 und rho0.95, 192 PSUs in vier Strata und vier Null-Domänen-PSUs. Tatsächliche Polychoriken 0.8361–0.8621 beziehungsweise 0.9450–0.9553. Native Punktbindung maximal 2.014e-9 beziehungsweise 8.318e-10. Echte vollständige Moment-Neuschätzung nach Einzel-, Kontrast-, glatten, Skalen- und ausgeschlossenen Gewichtsrichtungen bei zwei Schritten trifft die eigene IF maximal 2.687e-10 beziehungsweise 1.954e-10. Die bisherigen Vorab-Toleranzen 2e-7/2e-6 bleiben erhalten. Baseline prüft weiterhin vollständige Masken, Stratum-/PSU-Handkovarianz, externe EFA/CFA-Importe und Stopps.

Das belegt den benannten Softwaregegenfall, keine allgemeine Grenzkorrelations- oder sparse-cell-Sicherheit. Besetzte winzige/ausgelöschte Zellen, Randlösungen und andere numerisch nicht identifizierbare Fälle bleiben Stopps. Nutzung der Kandidatenfassung wartet auf Bindung durch den Koordinator und den vorgesehenen Review vor Empirie.

## Erhaltene Fehler und Primärfundstellen

Alle Vorläufe bleiben erhalten. `test-001` scheiterte vor Ausführung am Parsefehler `else1`. `test-002` verwarf fälschlich die festen THETA-Skalierungszeilen. `test-003` benutzte den nicht angehängten `stats::coef`-Dispatch; `test-004` fehlte `add_labels=TRUE` im gepinnten Coef-Inspector. `test-005` hatte im Test den N-1-Faktor und das semTools-Rückgabeformat falsch behandelt. `test-006` verfehlte mit Default-Refits die strenge Ableitungsgrenze. `test-007` stoppte wegen Nichtkonvergenz eines zu streng gesetzten NLminb-Oracles. `test-008` bestand die korrigierte Refit-Gegenrechnung; `test-009` wiederholte sie mit der finalen gemeinsamen Fassung. Zwei frühe API-Inspektionen scheiterten ebenfalls und sind erhalten. Nichts davon wird nachträglich als bestanden ausgegeben. Archivierte Codefassungen entsprechen den Laufhashes.

Gelesene Original-Softwarequellen sind versionsgebunden und im [Inputregister](../../../outputs/loop/resume-ordinal-support/input-bindings.json) gehasht:

| Primärquelle | Tatsächlich gelesene Fundstelle |
| --- | --- |
| lavaan0.7.2 `lav_model_utils.R` | Freie Parameter und Setter, Z.7–152; THETA-Delta aktualisieren |
| lavaan0.7.2 `lav_model_implied.R` / `lav_model_wls.R` | Modellmomente und kategoriale Schwellen-/Korrelationsordnung, Z.1–87 / 6–50 |
| lavaan0.7.2 `lav_object_inspect.R` | Coef-Labels und Reihenfolge, Z.3300–3332 |
| lavaan0.7.2 `lav_model_vcov.R` | Erwarteter Sandwich, Z.184–230; nicht-ML-Nenner, Z.725–753 |
| lavaan0.7.2 `lav_model_estimate.R` | NLminb-/BFGS-Kontrollwerte, Z.664–684 / 775–807 |
| semTools0.5.9 `R/reliability.R` aus dem vorhandenen Originaltarball | `compRelSEM`/`omegaCat`, Z.2945–2994; standardisierte gemeinsame Faktoren, beobachteter Modellnenner, tatsächliche mnormt-CDF |
| Vorhandene ESS-Adapter-/Methoden-Autorenfassungen | Eingabevertrag, volle Designkovarianz und vorhandene Grenzen; keine neue ESS-Datenlektüre |

Keine neue externe Literatur wurde als vollständig geprüft ausgegeben. Die direkte vorhandene Rscript-Datei, SOFTWARE-001/v1-Manifest und ursprüngliche Launcher-/Umgebungsdateien wurden vor und nach den Läufen gehasht. HOME bleibt unverändert. Temp-/Cache-/XDG-Dateien liegen im eigenen Outputordner. Der öffentliche Wrapper schränkt die bezeichneten zwölf Child-Schreibrechte per `setpriv`/Landlock auf diesen Ordner und write-file auf `/dev/null` ein. Er behauptet keine vollständige Lese-, Netzwerk-, Geräte-, Supervisor- oder PC-Isolation. Keine globalen Installationen und kein Conda-Aufruf.
