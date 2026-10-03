# Feste Full-DE-Normen und vorab bezeichnete Sensitivitäten

Autorenfassung vom 3. Oktober 2026. Die neue Normschicht ist auf erfundenen Daten ausgeführt. Dieser Bericht erteilt keine Methodenabnahme, Datenfreigabe, Ergebnisannahme oder Veröffentlichungserlaubnis. Neue Dateien sind ausschließlich `pipeline/ordinal/norms.R`, `pipeline/ordinal/test-norms.R`, dieser Bericht und eigene Belege unter `outputs/loop/resume-norms-author/`. Keine realen A/B/C/FULL-, Gruppen-, Wahl-, Links-rechts-, Assignment- oder ESS-Rohdaten wurden gesucht oder gelesen. Keine fremden aktuellen Gateurteile, Git-Aktionen, Tags, Installation, Claude oder `pnpm check`.

Die abgeschlossenen Support-, A- und Confirm-Autorenberichte und ihre damaligen Quellfassungen bleiben erhalten. Der Koordinator hat `confirm.R` danach separat um die tatsächlichen fitted CFA-Schwellen und deren Labels ergänzt. Diese Normfassung bindet die neue Rootquelle `e7c8d04d…`; sie bearbeitet keine bisher gepinnte Forschungsdatei. Der alte Confirmbericht mit seinen 113 Checks und e49-Pins bleibt ein historischer Beleg.

## Speicher-API und fester Vertrag

[`norms.R`](../../../pipeline/ordinal/norms.R) bietet `en_analyse(frame, full_aggregate, pspwght)` rein im Speicher. `en_initialize(project_root)` prüft vor Import exakt fünf vorhandene Forschungsquellen und lädt deren unveränderte Helfer. `en_public(result)` liefert die feste Aggregat-Whitelist. Es gibt keinen Norm-Dateiloader, keinen Modellfit, keine Modellauswahl und keinen öffentlichen Export aus der Rechenfunktion. Ein instrumentierter `oa_fit`, der jeden Aufruf sperrt, bleibt bei der tatsächlichen synthetischen Normrechnung unbenutzt.

Der übergebene FULL-Vertrag muss `schema="life93-fixed-model-confirmation-aggregate-1"`, `arm="FULL"`, einen ausgeführten und geeigneten festen Modellfit sowie `global_model_passed=TRUE` und `CRITERIA_PASSED_PENDING_RESULT_REVIEW` enthalten. Freeze, vollständige Konfiguration, M2/M3-Modellgruppen, neun Items und Quellpins werden mit den unveränderten Confirmfunktionen geprüft. Mindestens zwei kanonisch geordnete, bereits im Freeze gewählte und in FULL beibehaltene Scores sind erforderlich. Neue Scoregruppen oder Umpolungen sind nicht möglich. Das Statuswort bleibt ein numerischer Zwischenbefund; weder dieses noch `cfg$status` ist eine empirische Freigabe.

Der Frame bleibt exakt `stratum,psu,weight,B34,B35,B36,B40,B41,B42,B43,B44,B45`, mit bereits orientierten Kategorien 0 bis K−1 für K=5/5/5/4/4/4/11/11/11. Positive endliche Originalgewichte und der vollständige ursprüngliche PSU-/Stratumrahmen werden geprüft. Eine einzige vollständige Neunitemmaske gilt für Hauptnorm, alle Varianten und jede Itemauslassung. Ein außerhalb dieser Domäne liegender Fall wird nicht durch vollständige Antworten allein auf einer Teilskala aufgenommen. Ursprüngliche Null-Domänen-PSUs bleiben erhalten.

Die pure API kann die Herkunft eines gültigen FULL-Objekts und positiver Gewichtszahlen oder dessen Übereinstimmung mit dem tatsächlichen Originalinput nicht historisch beweisen. Der zukünftige Rootwrapper muss den abgeschlossenen B/FULL-Weg, unveränderten Freeze, gebilligten FULL-Aggregathash, dieselbe private Eingabe, originale `anweight`/`pspwght`, Original-PSUs und zusätzliche Norm-/Wrapperpins vor realem Read binden. Ein synthetischer FULL-Mock ist ausschließlich eine Testeingabe. Es wurde kein tatsächliches Deutschlandartefakt erzeugt.

## Rationale Hauptnorm und ursprüngliche Designvarianz

Für eine feste Skala wird `L=LCM(K_j−1)`, `N=sum_j(cat_j*L/(K_j−1))` und `D=k*L` berechnet. Sortierung und Gleichstände verwenden ausschließlich den ganzzahligen Zähler N auf demselben Nenner D. Theoretisch identische Scores erhalten dadurch dieselbe Normposition. Die zulässigen Nenner und Kreuzprodukte werden auf den exakten Integerbereich der R-Doubles begrenzt. Für das heterogene sechsitemige ZF sind L=30 und D=180: drei Z-Kategorien jeweils 1 und eine F-Kategorie 10 erzeugen beide N=30, Score 1/6 und denselben Gleichstand.

Je Score werden nur das sortierte Aggregatgitter, ganzzahlige Zähler/Nenner, Anzahl und Gewichtsmasse je Gitterpunkt sowie der gewichtete Midrank `(W_below+.5*W_tie)/W_complete` ausgegeben. Keine Fallscore-, Sortierpositions-, Masken-, Gewichts-, Personen-, PSU-/Stratumkey-, IF- oder Posteriorvektoren gelangen in das öffentliche Aggregat. Keine RDS-Datei wird erzeugt. Floating-Varianten binden Gleichstände an exakt gleiche berechnete Doublewerte; es gibt keine frei gewählte Epsilon-Zusammenfassung. Diese numerische Grenze wird ausdrücklich benannt.

Der rohe gewichtete Skalenmittelwert erhält eine gemeinsame Designkovarianz über sämtliche beibehaltenen Scores. Die privaten ratio-mean Beiträge sind `w_i*(S_i−mean_w)/W_complete`, außerhalb der Neunitemdomäne exakt null. `oa_taylor` summiert sie auf ursprüngliche PSUs, zentriert innerhalb jedes Stratum und verwendet G/(G−1). Die Mittelintervalle sind zweiseitige 95%-t-Intervalle mit den ursprünglichen PSU-df `sum_h(G_h−1)`. Gewichte, Kodierungen und vollständige Antwortdomäne bleiben bedingt fest; keine Kalibrierungs-, Modus-, Auswahl-, Nichtantwort- oder persönliche Messfehlerunsicherheit wird daraus abgeleitet.

Original-/Complete-/Missinganzahl und -gewicht, vollständige/fehlende Gewichtsanteile, Original-PSUs/-Strata/-df und Null-Domänen-PSUs werden aggregiert berichtet. Für jeden Gitterpunkt lautet der Missing-Bereich `[(1−r)*F_complete, (1−r)*F_complete+r]`, mit r=fehlender Gewichtsanteil. Die konstante Breite r und das vorab definierte ≤.05-Budget werden separat ausgegeben. Breite über .05 lässt die vollständige Antwortdomäne als engeren Geltungsbereich stehen und sperrt die entsprechende vollständige Zielpopulationsübertragung. Keine Verteilung der fehlenden Antworten wird erfunden.

## Jede bezeichnete Variante bleibt separat

| Variante | Festes Rechenverfahren |
| --- | --- |
| Ungewichtete Referenz | Derselbe rationale Hauptscore, nur Referenzgewichte eins; Missingbreite aus den Fallanzahlen |
| Original `pspwght` | Derselbe rationale Hauptscore, originale alternative Referenzgewichte; Missingbreite aus deren eigener Gesamtmasse. Median des beobachteten Gewichtsverhältnisses, Min/Max-Verhältnis, exakte Multiplikationsgleichheit sowie absolute/relative Rundungsabweichungen werden ausgewiesen. Keine Metadatenbehauptung wird mit tatsächlicher Dateigleichheit verwechselt |
| Gewichtete Item-z-Variante | Gewichtete Populations-SD der 0–1-Items auf der identischen Domäne; theoretische Endpunktabbildung `sum(x_j/sd_j)/sum(1/sd_j)`. SD=0/undefiniert sperrt allein diese Variante |
| Latente Variante | Ausschließlich feste eigene Skalenitems, marginaler N(0,1)-Faktor, positive standardisierte Ladungen unter 1 und die **tatsächlichen fitted Modellschwellen** aus dem unveränderten gemeinsamen CFA-Fit. Keine Konditionierung auf andere Faktoren/Gruppe. EAP im Normalmodell; anschließend erwartete Original-0–1-Scorekurve am EAP |
| Jedes Leave-one-out | Genau das vorab bezeichnete Item entfernen, restliche Items rational und gleich gewichtet mitteln; eigene Norm weiterhin auf derselben vollständigen Neunitemdomäne. Jede mögliche Auslassung wird berichtet |

Geomin/Oblimin bleiben Strukturdiagnosen des festen FULL-Modells. Sie erzeugen hier weder einen neuen persönlichen Score noch eine alternative Normformel.

Jede ausgeführte Variante erhält ihre eigene Norm und ihren eigenen Vergleich mit dem Hauptvertrag. Vergleichsmassen verwenden immer die **ursprünglichen vollständigen Originalgewichte**, auch bei anderer Referenzgewichtung. Strikte Rohscoreabweichung >.05 oder Perzentilabweichung >5 bei mindestens .05 ursprünglicher Gewichtsmasse führt zu `CONTRACT_DEPENDENCE_BUDGET_EXCEEDED`; andernfalls `WITHIN_SPECIFIED_BUDGETS`. Rationale Rohscorevergleiche verwenden ganzzahlige Kreuzprodukte. Eine nicht ausführbare Variante erhält `UNSUPPORTED` und einen festen Fehlercode, keinen Stabilitätserfolg. Die Budgetzahlen sind eigene vorab gewählte Ansprüche, keine universellen Literaturstandards oder persönlichen Unsicherheitsintervalle.

## Deterministische EAP-Numerik

Die Normalquadratur verwendet unverändert 81/161/321 Golub-Welsch-Knoten. Die symmetrische Jacobi-Matrix hat offdiagonal sqrt(j). Die äquivalenten Christoffel-Gewichte aus der normalisierten Hermite-Rekursion vermeiden verlorene kleine erste Eigenvektorkomponenten; es wird weder ein Gewicht abgeschnitten noch ein günstiges Gitter nachgewählt. Normalrechtecke werden durch Log-CDF/Log-Survival-Differenzen mit `expm1` berechnet, posterior mit Row-Max-Zentrierung im Lograum summiert. Ungültige oder numerisch undefinierte Rechtecke/Posterioren bleiben feste offene Fehlercodes.

Alle tatsächlich vorkommenden vollständigen Antwortmuster werden nur privat im Speicher ausgewertet. Öffentlich stehen Musteranzahl, drei Knotenzahlen und maximale Scorekurvenabweichungen 81/161 und 161/321. Der 321-Punkt wird nur verwendet, wenn die maximale 161/321-Kurvenabweichung höchstens 1e−6 ist. Der EAP ist kein persönlicher CI; Parameter-/Modellunsicherheit wird nicht durch diese numerische Toleranz abgebildet. Kein Rescuemodell, Parameterclip oder nachträgliche Gitterverfeinerung.

## Tatsächliche fokussierte Synthetikchecks

Der finale [test-004](../../../outputs/loop/resume-norms-author/test-004-checks.json) besteht **45/45** Assertions, exit0, UTC 11:38:03–11:38:09 am 3. Oktober 2026. Der [Laufbeleg](../../../outputs/loop/resume-norms-author/test-004-command.json) bindet alle zehn tatsächlichen Quellen/Fixture/Plan/Entry vor dem Start; Rscript und SOFTWARE-001-Manifest stimmen auch danach. Reproduzierbarer öffentlicher Entry ist [`test-norms.R`](../../../pipeline/ordinal/test-norms.R), aufgerufen unter dem vorhandenen gepinnten Runtimeprefix durch den eigenen Scoped-Launcher. Ein frisches eigenes Label ist nötig; keine Überschreibung. Der zukünftige generische Rootwrapper ist nicht Bestandteil dieses Pakets.

Die kleine Handrechnung enthält fünf ursprüngliche PSUs in zwei Strata, einen vollständigen Null-Domänen-PSU und ursprüngliche df=3. Die ZF-Gitterpunkte 0,1/6,1 mit Massen 1,5,4 ergeben Midranks .05,.35,.8. Die separat berechnete vollständige stratumzentrierte Mittelkovarianz stimmt mit `oa_taylor` überein. Gewichtsfaktor 17 ändert weder Kovarianz noch CDF; absolute aggregierte Massen skalieren entsprechend. Fehlmasse 5/15 erzeugt exakt Breite 1/3, während die ungewichtete Variante 1/5 berichtet. Jeder Drei-/Sechsitemscore und sämtliche Zwei-/Fünfitemauslassungen verwenden weiterhin dieselben vier vollständigen Neunitemfälle.

Die Handdaten zeigen auch tatsächliche positive/negative Budgetzweige: ungewichtete ZF-Norm ist bei 100% ursprünglicher Masse perzentilabhängig, während bloße Gewichtsskalierung 2 exakt dasselbe Ergebnis liefert. Eine .0001-Abweichung im ersten `pspwght` bleibt als Rundungsdiagnose sichtbar. Invalides `pspwght`, überlaufende alternative Gesamtmasse, nicht endlicher Missinganteil, SD=0, Ladung=1 und falsche Modellschwellenlabels ergeben die bezeichneten festen Ablehnungs-/Variantencodes; andere ausführbare Varianten bleiben erhalten. Leere vollständige Domäne liefert jeden Haupt-/Varianten-/LOO-Befund explizit als nicht ausführbar. Arm B und weniger als zwei FULL-Scores werden zurückgewiesen.

Normalquadraturmomente 1,0,1,3,15 bestehen bei allen drei Knotenzahlen mit 1e−10-Toleranz. Unabhängiges R `integrate()` integriert direkt das Produkt normaler ordinaler Rechteckwahrscheinlichkeiten mit der Normaldichte; rel.tol 1e−10, abs.tol 1e−30, bis 5000 Unterteilungen. Es verwendet weder die Logrechteckroutine noch die Quadraturknoten/-gewichte. Die Gegenfälle liefern:

| Erfundenes Modell / höchste drei Kategorien | Unabhängiger EAP | Originalkurve am EAP | Tatsächlicher 161/321-Kurvenabstand |
| --- | --- | --- | --- |
| Ladung .7, Schwellen −.5/0/.5 | 1.4075591250268056 | .8829968337296041 | 0 |
| Ladung .85, Schwellen 4/5/6 | 6.589815860620051 | .6988619726285862 | 3.33e−16 |

321-Quadratur und unabhängige Integration stimmen bis ungefähr 1e−15 überein, innerhalb der vorab gesetzten 2e−6-Orakeltoleranz. Die absichtlich scharfe Probe Ladung .9999/Schwellen .05/.15/.3 bleibt dagegen **wirklich nicht ausführbar**: 161/321-Kurvenabstand .6541264018798953, `ESS_NORMS_EAP_STABILITY`. Es wurde nichts angepasst, um daraus einen Erfolg zu machen.

Der tatsächliche synthetische FULL-M3-Fit nutzt den vorher beschriebenen erfundenen Seed 2026100342, n=7680, 192 PSUs, vier Strata, vier vollständig fehlende PSUs und 7520 vollständige Neunitemfälle; df=188. Die unveränderte Confirmrechnung besteht ihre eigenen Kriterien und stellt echte fitted Schwellen bereit. Die Normen erzeugen 13/10/31 H/Z/F-Gitterpunkte; Missingbreite .02071000127. Alle EAP-Varianten bestehen die 161/321-Toleranz mit Maximalabstand 3.33e−16. Die rohen Mittel-SE H/Z/F sind .00525503/.00517581/.00475629; ihre t-Kritik ist 1.97266269.

Numerische Ausführbarkeit ist kein Stabilitätsurteil: In diesen erfundenen Daten überschreiten die latenten Varianten das .05-Rohbudget bei H/Z/F für **22.46%/39.89%/21.35%** der ursprünglichen vollständigen Gewichtsmasse. Alle neun Leave-one-out-Varianten sind ebenfalls vertragsabhängig. Ungewichtete Referenz, bloße `pspwght`-Skalierung und gewichtete z-Varianten bleiben innerhalb der bezeichneten Massenbudgets. Diese getrennten Resultate werden unverändert ausgegeben; kein Gesamtstabilitätsclaim oder günstige Variantenauswahl.

Historie bleibt sichtbar: `inspect-001` bestand die reinen Quadraturproben; `test-001` brach nach der ersten rationalen Prüfung an der **falsch angeordneten erfundenen Testheaderliste** ab. Die neue Testfixture wurde danach auf die vorhandene exakte Spaltenliste geordnet. `test-002` bestand 40/40, `test-003` nach festen Überlauf-/Labelchecks 44/44. `test-004` ergänzt die tatsächliche 0700/0600-Exportprüfung. Alle Vorfassungen, Logs und Quellenarchive bleiben erhalten. Frühere synthetische Dateien hatten zunächst normale umask-Rechte; ausschließlich im eigenen Ordner wurden die Metadaten auf 0700/0600 gesetzt. Der finale Launcher verwendet umask077. Keine realen oder individuellen Daten waren dort vorhanden.

## Pins und offene Grenzen

| Quelle | SHA256 |
| --- | --- |
| Neue `norms.R` | `ea360f0f76e889a8d872488cc2c20b1f62936ddea18ca0160ca9c14bce4b1e32` |
| Neuer öffentlicher `test-norms.R` | `f91ea9c3c67188943215ad34b4b4f28921a2ad206949a47c968562669a254b52` |
| Root-`confirm.R` mit fitted Schwellen | `e7c8d04d8010c456c5db6d9902353a37786737b201cf9a160d082f40a84bddad` |
| Unveränderte `develop.R` | `d1b725b05ba43d9a3edbe4964e05ae0d5365ef951944fe1c83284967ff800e74` |
| Unveränderte `develop-config.R` | `44a74f0e59645d047f2bdc4508cc0058d0dd80ffb4a67a8963ee9e84f0f429b0` |
| Unveränderte `adapter_v2.R` | `8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b` |
| Unveränderte `support.R` | `b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22` |

Der [eigene Hashindex](../../../outputs/loop/resume-norms-author/artifact-index.json) bindet Bericht, Code, vollständige Laufartefakte und alle 50 archivierten Quellbindungen. Er prüft deren tatsächliche Bytes. Der Normaggregat-Inhalt kopiert die fünf Herkunftspins des FULL-Fits; der zukünftige Ausführungsbeleg muss zusätzlich Normcode und Wrapper binden. Es gibt keine rekursive Selbsthashbehauptung im Ergebnisobjekt.

SOFTWARE-001/v1 bleibt unverändert: R4.5.3/lavaan0.7.2/pbivnorm0.6.0/jsonlite2.0.0. Rscript SHA256 `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`, Manifest SHA256 `126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e`. HOME bleibt unverändert; eigene Temp-/Cache-/XDG-Pfade. Der Child verwendet die vorhandenen zwölf Landlock-Schreibrechte ausschließlich für den eigenen Outputordner und write-file für `/dev/null`. Das behauptet keine allgemeine Lese-, Netzwerk-, Geräte- oder Supervisorisolation.

Primärgrundlagen sind der [konkrete Empirieplan](../../../docs/empirie-plan-v1.entwurf.md), der [Sensitivitätsrechenvertrag](../../../docs/sensitivitaeten-v1.entwurf.md), die tatsächlich gepinnten R-Helfer und R-Basis-/stats-Implementierungen `eigen`, `pnorm` und `integrate` des vorhandenen Runtimeprefix. Der [Supportbericht](ESS-ORDINAL-SUPPORT-proposal.md) bewahrt die gebundenen ursprünglichen Softwarefundstellen und Refit-/Observed-Score-Orakel. Dieses Paket führt keine neue Literaturfreigabe oder Abdeckungsstudie durch.

Keine persönliche CI, Modell-/Parameter-/Gewichtsschätzunsicherheit, Kalibrierung, PPS-WOR/FPC-Rekonstruktion, Missingidentifikation oder reale Normstichprobenprüfung wird durch synthetische Numerik ersetzt. Normpositions-Stichprobenintervalle werden hier nicht berechnet; der implementierte designgerechte t-Bereich betrifft ausschließlich aggregierte rohe Mittel. Bei numerisch ununterstützter Variante bleibt deren Diagnose offen. Reale FULL-Anwendung, Zugriffswrapper, Veröffentlichung und folgende Methodenprüfung stehen außerhalb dieses abgeschlossenen Autorenschritts.
