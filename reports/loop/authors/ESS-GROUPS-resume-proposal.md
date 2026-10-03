# ESS-Gruppenvergleich: ausführbarer Vorschlag

Autorenbericht, 3. Oktober 2026; keine Erstprüfung oder empirische Abnahme. Geprüft wurden öffentliche Primärquellen und ausschließlich erfundene Daten in der vorhandenen isolierten R-Laufzeit. Keine Datei aus `data/raw/` oder `data/local/`, keine ESS-Antwort, Wahl-/LR-Verteilung, Kennung oder Designzeile wurde gelesen. Änderungen beschränken sich auf diesen Bericht und `outputs/loop/resume-group-methods/`.

## Entscheidungsvorschlag

Für den fachlich noch offenen Kandidaten B34–B36/B40–B45 ist eine gemeinsame ordinale Gruppenrechnung praktisch ausführbar. Gruppen, die dieselben PSUs teilen, brauchen eine **volle gemeinsame Momentkovarianz**. Der gruppenweise `nacov`-Import in lavaan transportiert deren Crossblöcke nicht. Er kann die DWLS-Punktrechnung tragen; seine unveränderten robusten Gruppen-SE und Fit-/Nestungstests dürfen hier nicht als gemeinsame Designrechnung verwendet werden.

Ein identifiziertes Anker-CFA, erwartete beobachtete Dreierscores am festen gemeinsamen η-Raster und deren gemeinsame Delta-Kovarianz wurden tatsächlich synthetisch gerechnet. Die Aussage bleibt an die vorab begründete Ankerwahl gebunden. Für ESS ist noch kein Anker fachlich freigegeben. Vollständig gleichgesetzte Itemfunktionen liefern automatisch gleiche Scores und sind kein positiver Äquivalenzbeleg.

P09 sollte zwei Veröffentlichungsumfänge ausdrücklich unterscheiden: historische **Antwortmittel des fest codierten Scores** mit Designintervallen und die zusätzliche Interpretation als vergleichbares Konstruktprofil. Letztere benötigt die Modell-/Anker-/Äquivalenzgates unten. Eine enger beschriftete Antwortdarstellung ist eine spätere menschliche Designentscheidung; keine stillschweigende Aufhebung des gespeicherten Auftrags.

## Gemeinsamer Designweg

Der bereits dokumentierte Hauptweg verwendet `anweight`, veröffentlichte `psu/stratum`, Ultimate-PSU-Varianz ohne FPC und feste Gewichte. Der ESS-Leitfaden V1.2, §3/4.1 und Box5, trägt diese benannte Approximation. Exakte PPS-WOR-Varianz, Kalibrierungs- und Nichtantwortfehler werden damit nicht zugesichert. [ESS-Leitfaden](https://stessrelpubprodwe.blob.core.windows.net/data/methodology/ESS_weighting_data_1_2.pdf), [vorheriger Autorenbefund](ESS-METHODS-resume-proposal.md).

Je Gruppe die gewichteten 87 Schwellen-/Polychorikmomente und ihre Fallbeiträge berechnen; Beiträge außerhalb der Gruppe sind null. Alle Gruppenbeiträge zu einem Vektor stapeln, **über die ursprünglichen gemeinsamen PSUs** summieren und innerhalb Stratum zentrieren:

`V_m = sum_h G_h/(G_h−1) * crossprod(U_h − mean(U_h))`.

Ein analytisch leerer Domänen-PSU bleibt mit Nullbeitrag enthalten. Ein tatsächlich einzelner ursprünglicher PSU im Stratum löst im Hauptweg einen Fehler aus. Keine gruppenweise neue PSU-Liste, kein zeilenweiser Resampling-/Split-Ersatz. [Asparouhov2005](https://www.statmodel.com/download/webnotes/mplusnote72.pdf), S.421–425, Gl.3/4/6; [survey4.4-2](https://search.r-project.org/CRAN/refmans/survey/html/surveysummary.html), Details zu Domänen und Kovarianzen. Das survey-Paket wurde nicht ausgeführt.

Für zwei Gruppen entstehen 174 Momente. lavaan0.7-2 verlangt je Gruppe `NACOV_g=n_g*V_gg` und eine WLS-Matrix; eine Schnittstelle für `V_gh` ist nicht dokumentiert. Eigene Nachrechnung: `D` ist der öffentliche Moment-Jacobian, `W=blockdiag((n_g/n)*W_g)`. Die Gleichheitsmatrix H wird aus `parTable()` rekonstruiert, Z spannt ihren Nullraum auf. `B=Z*(Z' D'WD Z)^−1*Z'`, `K=B D'W`, **`V_beta=K V_m K'`**. Keine Inversion des gesamten, möglicherweise rangdefizienten `V_m`. Voraussetzungen sind identifizierter Tangentialraum, endliche positive Bread und exakt gleiche Moment-/Parameterordnung. Nichtlineare oder andere Restriktionen sind durch diesen einfachen H-Parser nicht abgedeckt. [Gepinnte Hilfe](../../../outputs/loop/software-author/sources/lavaan/man/lavaan.Rd), Z.88–106; [lavInspect](../../../outputs/loop/software-author/sources/lavaan/man/lavInspect.Rd), Z.357–387/461–468; [Informationsimplementation](../../../outputs/loop/software-author/sources/lavaan/R/lav_model_information.R), Z.638–730.

Die Probe verwendet den vorhandenen versionsgebundenen lavaan-Moment-IF-Kandidaten `SC B^-T H^T`. Das ist kein unabhängiger Nachweis des neuen gewichteten ordinalen EE-/Jacobian-Algorithmus, den die Fortsetzung gesondert implementiert und prüft. Derselbe IF-Kandidat darf nicht als unabhängiger Goldstandard für diesen neuen Algorithmus gelten.

## Ordinale Identifikation

THETA, `std.lv` und `semTools::measEq.syntax(ID.cat="Wu.Estabrook.2016")` sind lokal ausführbar. Zuerst Schwellen, anschließend Ladungen, Interzepte und Residualvarianzen prüfen; die jeweils entbehrlichen Identifikationsbindungen freigeben. Nicht einfach Restriktionen zur vollständig fixierten Ausgangsfassung addieren. Die 5/4/11-Kategorien erlauben hier getrennte Schwellenrestriktionen. [Wu/Estabrook2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5458787/), §5.8/6/10; [semTools0.5-9](https://cran.r-project.org/web/packages/semTools/semTools.pdf), `measEq.syntax`, S.71–75. Wu/Estabrook löst partielle Invarianz ausdrücklich nicht.

Synthetische Zweigruppenmodelle, jeweils drei korrelierte Faktoren und alle neun Items:

| Stufe | df | Freie Tangentialdimension = Jacobianrang | Freigabe in Gruppe2 |
| --- | ---: | ---: | --- |
| Konfigural | 48 | 126 | Faktorlage0/Varianz1; Iteminterzepte0/Residualvarianzen1 als Identifikation |
| Schwellen | 81 | 93 | Neun Iteminterzepte und Residualvarianzen |
| Zusätzlich Ladungen | 87 | 87 | Drei Faktorvarianzen |
| Zusätzlich Interzepte | 93 | 81 | Drei Faktormittel; Iteminterzepte wieder gleich |
| Zusätzlich Residuen | 102 | 72 | Itemresidualvarianzen wieder gleich |

Alle fünf Modelle konvergierten mit zulässigem Postcheck. Die vollständigen synthetischen Parameter-/Restriktionstabellen und Syntax stehen unter `v3-parameters-*`/`v3-syntax-*`; H/Z werden im gespeicherten Code daraus explizit gebildet. Native gruppenweise skalierte χ²-Werte wurden **nicht** als gemeinsame Fitprüfung oder voneinander subtrahiert. Eine korrekt gemeinsame robuste Fit-/Nestungsprüfung ist in diesem Paket nicht implementiert; Parameter- und Kovarianzfähigkeit allein ersetzt sie nicht.

## Tatsächlich gerechneter Score-Mapping-Vergleich

Für den beobachteten 0–1-Dreierscore gilt bei lokaler Unabhängigkeit im Probitmodell:

`E[S_d|η,g] = (1/3) sum_j (1/(C_j−1)) sum_t Φ((ν_jg + λ_jg*η − τ_jtg)/sqrt(θ_jg))`.

Die Facetten sind unipolar; Kategorieabstände der Darstellung sind festgelegt, Faktorwerte ersetzen den Score nicht. Dass lediglich skalare Gleichheit ordinale beobachtete Mittel nicht ausreichend absichert, ist im Primärartikel einschließlich Residual-DIF gezeigt. [Tse/Lai/Zhang2024](https://link.springer.com/article/10.3758/s13428-023-02247-6), S.3117–3139, Abschnitte zu strikter Invarianz und beobachteten versus Faktormitteln; Appendix.

**Gemeinsame Metrik der Probe:** q1/q4/q7 wurden vor Lauf2 ausschließlich synthetisch als invariant gesetzt: gleiche Ladung und sämtliche Schwellen, Iteminterzept0 und Residualvarianz1. Referenzfaktoren Mittel0/Varianz1; fokale Mittel/Varianzen frei. Übrige Ladungen/Schwellen sind zwischen Gruppen frei; deren Interzept0/Residualvarianz1 identifiziert nur die willkürliche Itemantwortmetrik. So können ihre bedingten Antwortfunktionen differieren. Der Ankerweg hat df65 und Rang109/109. Er ist eine explizite Autorenkonstruktion, keine von Wu/Estabrook behauptete partielle Invarianzlösung. Anker-DIF wird darin vorausgesetzt ausgeschlossen und nicht selbst geprüft.

Die 15 Gruppenunterschiede Δ am Raster `{-2,-1,0,1,2}` erhalten `V_Δ=J V_beta J'`. Eigene analytische Ableitungen nach Ladung, Interzept, Schwellen und Residualvarianz wurden mit `numDeriv` gegengerechnet. Faktormittel/-varianzen werden beim **festen gemeinsamen η** nicht in die bedingte Funktion eingesetzt. Für die festgelegte Familie von 15 Kontrasten berechnet die Probe:

`U=max_l[|Δ_l| + t_(1−.05/(2*15), ν)*SE(Δ_l)]`, hier `ν=PSUs−Strata=156`.

Bonferroni benötigt keine Unabhängigkeit der Kontraste. Nominale gemeinsame Abdeckung folgt jedoch nur soweit die einzelnen Design-/Delta-Intervalle ausreichend kalibriert sind. Das ist eine vorgeschlagene asymptotische Prüfung, kein ausgeführter Abdeckungsnachweis. Bei mehr Gruppen muss die **gesamte vorab bestimmte Familie** in den Nenner; kein nachträgliches Herausnehmen ungünstiger Paare. Aussagen bleiben auf das Raster und die Ankerannahmen begrenzt.

Die Probe erzielt `max|Δ|=0.052906`, `U=0.107261`: das eigene konservative Darstellungsbudget0.05 wird **nicht bestanden**, obwohl der Generator invariant ist. Eine einzelne API-Probe kalibriert daher weder Erkennungsleistung noch Fehlentscheidungsrate. Ein analytischer Gegenfall mit gleichen Ladungen/Schwellen/Interzepten und Residual-SD1 versus2 verändert die erwarteten beobachteten Scores am selben Raster um bis0.133245. Die im strikt gleichgesetzten Modell gefundene Differenz≈0 ist dagegen erzwungen und kein Zertifikat.

## Veröffentlichungsgates und genaue Ausfallfolgen

1. **Historische Antwortmittel:** vorab historisch richtige Wahlfrage, Zeitraum, Filter, Kategorien und vollständige Itemmaske festlegen; keine heutige Parteibedeutung unterstellen. Für die erste gemeinsame Modell-/Scoreprüfung die identische Neunitem-Vollmaske verwenden. Abweichende Dreiermasken benötigen eine eigene deklarierte Zielpopulation. Ungültige/fehlende Gruppenantworten ausschließen und den Ausfall berichten. Designgültigkeit, Singletonregel und reproduzierbare gemeinsame Moment-/Scorekovarianz müssen bestanden sein.
2. **Designintervall:** gemeinsam geschätzte Verhältniskennzahlen `mu_g=sum(w I_g S)/sum(w I_g)` und Beiträge `u_ig=w_i I_g(S_i−mu_g)/sum(w I_g)` mit sämtlichen ursprünglichen PSUs. Gruppen-/Referenzunterschiede verwenden `V_g+V_h−2Cov(g,h)`. 95%-t-Intervalle mit festgelegten Designfreiheitsgraden; mindestens50 vollständige Rohfälle und Halbbreite≤0.05 als **eigene** Kleingruppen-/Darstellungsregeln, keine Literaturgarantie. Leere Domäne, nicht schätzbare Varianz oder zu breite Intervalle: betreffenden Wert auslassen. Die offizielle [survey-Hilfe](https://search.r-project.org/CRAN/refmans/survey/html/surveysummary.html), `confint(df=degf(design))`, dokumentiert die t-Option; kein lokaler survey-Lauf.
3. **Konstruktbezogenes Gruppenprofil:** zusätzlich zulässige gemeinsame Struktur, Identifikations-/Restriktionsprüfung bis zur strikten beobachteten Vergleichbarkeit, korrekt gemeinsame Modelldiagnostik, fachlich **vor Antworten** begründete Anker und positive, in passenden ordinalen Design-Szenarien kalibrierte Mapping-Äquivalenz. Vorschlag `U<0.05`; Nichtsignifikanz genügt nicht. Ankervarianten nur vorab fachlich setzen und vollständig berichten; keine DIF-optimierte Auswahl. Ein Budget-/Modellfehler suspendiert nur das betroffene Gruppen-/Facettenprofil und eine daraus abgeleitete gemeinsame Normaussage. Partielle skalare Invarianz oder latente Mittel sind kein Ersatzhauptscore.
4. **Beschriftung und Missing:** Designintervalle quantifizieren Stichprobenunsicherheit der festgelegten historischen Antwortdomäne, keinen persönlichen Messfehler und keine Nichtantwort-/Modusverzerrung. Ohne zusätzliche geprüfte Missing-/Nichtantwortannahmen bleibt die Aussage auf vollständig Antwortende mit gültiger historischer Gruppenangabe begrenzt. Eine Antwortmittel-Darstellung darf keine latenten Konstruktmittel, aktuelle Wählerschaft oder kausale Gruppenwirkung vortäuschen. Diese Einschränkung und die endgültige Darstellungsentscheidung bleiben menschlich zu entscheiden.

Wirklich offen sind damit der unabhängige reale ordinal-Moment-IF-Nachweis, gemeinsame robuste Fit-/Nestungsrechnung, die ESS-Ankerbegründung und designbezogene Intervall-/Äquivalenzkalibrierung. Es fehlt kein zusätzliches Statistikpaket oder erfundener persönlicher Statistiktermin. Fehlende P09-Freigabe blockiert konstruktbezogene Gruppenpublikation; Quellenarbeit, nationale Strukturanalyse und die Vorbereitung des engeren Antwortumfangs bleiben möglich.

## Ausführungsbelege und Fehler

R4.5.3/lavaan0.7-2/semTools0.5-9 aus der vorhandenen Laufzeit, direkt `Rscript --vanilla`; kein Conda, keine Installation, kein Auth-/Commit-/Push-Auftrag. Seed2026100314, 3200 erfundene Fälle, 160PSUs/4Strata, beide erfundene Gruppen in jedem PSU, positive unabhängige Gewichte, keine Missingwerte. Keine Zeilenexporte. Landlock begrenzt die zwölf ausgewiesenen Child-Schreibrechte auf den eigenen Outputordner plus `/dev/null`; keine vollständige Netz-/Read-/Supervisorisolierung behauptet.

Der erste Lauf hatte trotz Exit0 fünf fehlgeschlagene Algebraflags. Ursache: native lavaan-VCOV verwendet bei DWLS zusätzlich den Nenner `n−G`. [Quellcode](../../../outputs/loop/software-author/sources/lavaan/R/lav_model_vcov.R), Z.209–226/750–753. Lauf2 entfernte **nur im nativen Vergleich** den Faktor `n/(n−G)`; der eigene Taylor-Sandwich erhält diesen zusätzlichen Faktor nicht. Lauf3 ergänzte die analytische Ableitung. Erstfassungen, Fehler, Vorabpläne und Logs bleiben erhalten; Seed und Toleranzen wurden nicht gelockert. Letzter Lauf: zwölf enge Checks bestanden, keine Warnung, **kein bestandenes Vergleichbarkeitsgate**.

| Gegenrechnung | Tatsächliches Ergebnis |
| --- | --- |
| Gemeinsame174Momentkovarianz | Rang156; maximaler Crossblock0.00173737 |
| Gewichtete Momentpunkte | Differenz≤3.41e−8 |
| Eigene Nullraum-Bread gegen öffentlichen Inspector | Differenz≤8.53e−14 |
| Block-Sandwich gegen korrekt skalierten nativen VCOV | Differenz≤6.39e−16 |
| Analytischer Score-Jacobian gegen Richardson | Differenz1.88e−8; Delta-VCOV-Differenz2.47e−11 |
| Score-Differenzintervalle gemeinsame PSUs | Halbbreiten0.0176–0.0193 statt falsch unabhängig0.0293–0.0316 |
| Tatsächlicher Singleton | Fehler erkannt; keine Nullvarianz-/Poolingrettung |

[Quellenregister](../../../outputs/loop/resume-group-methods/source-ledger.json) enthält vollständige SHA256, UTC-Zugriffe, Versionen, URLs und lokale Fundorte. Wu-Livezugriff scheiterte an reCAPTCHA; gelesen wurde die vorhandene Primärkopie, HTML-SHA256 `32cf963946fa00970a18612d37c5bbc49347fd244329a1ee832b82eea9575730`. Die zusätzliche Online-semTools-Hilfe rendert0.5-6; die ausgeführte Syntax wird durch den gepinnten0.5-9-Manual und dessen Quelle belegt. Fünf direkte neue Quellenabrufe waren HTTP200.

[Finaler Code](../../../outputs/loop/resume-group-methods/runtime-group-v3.R), SHA256 `5dd66c5417d76329c5354ae2e7c6cdb395d85ce96ef69701e42efcd6f82999e3`; [Ergebnis](../../../outputs/loop/resume-group-methods/runtime-group-v3-result.json), `ea0760c4cb55560d9cb296a5b9996a91852f555ddd953b486ea2cf427ecfcc00`; [Kommando/Umgebung](../../../outputs/loop/resume-group-methods/runtime-group-v3-command.json), `aca9a63055f30a4de46c4aaadaa91836f6524ca3b11ed5ee776c27af669faf35`. Rscript-Hash vor/nach: `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`. Kein gemeinsamer Plan oder Code geändert. Eigener Berichtformatcheck; der Koordinator führt den gemeinsamen Repositorycheck aus.
