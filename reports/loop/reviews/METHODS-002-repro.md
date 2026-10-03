# METHODS-002: unabhängiger Reproduzierbarkeits- und Schnittstellenreview

Reviewer `/root/methods002_repro`, 2026-10-03. Prüffassung ist ausschließlich `reports/loop/packages/METHODS-002/v2/manifest.json`, SHA256 `b736855447a96dcaa3f55926edf59d7eda29c19dfe90d2e752de18df8b0d78e4`.

Die Originalrechnung ist reproduzierbar. Meine erfolgreiche eigene Probe liefert für sämtliche Originalbeobachtungen und alle 16 Originalchecks exakt dieselben geparsten Werte. Die enge NACOV-Schnittstellenbehauptung trägt. Die behauptete gemeinsame externe NACOV-/WLS.V-Prüfung braucht eine Korrektur: Das Original übergibt tatsächlich `NULL` als `wls_v`. Das ist Finding M2-R01. Es betrifft diesen Nachweis, keine empirische ESS-Auswertung.

Technische Reproduktion der 16 ausgeführten Originalchecks: `BESTANDEN`. Vollständiger Nachweis beider behaupteter externer Inputs in v2: `NICHT_BESTANDEN`. Eigene zusätzliche korrigierte Schnittstellenprobe: `BESTANDEN`, keine Änderung oder Freigabe des Originals. Wissenschaftliche ESS-Design-, Modell- oder persönliche Intervallabnahme: `NICHT_GEPRÜFT`.

## Auftrag und Unabhängigkeit

Der vollständige tatsächliche Startauftrag steht hier wortgetreu:

```text
Frischer unabhängiger Reproduzierbarkeits-/Schnittstellenreview METHODS-002, kein Autor. CWD jedeShell /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. AktuellesPaket reports/loop/packages/METHODS-002/v2/manifest.json SHA b736855447a96dcaa3f55926edf59d7eda29c19dfe90d2e752de18df8b0d78e4,8Dateien/95SourceInputs. v1 nur für tatsächlichen reinen Formattransfer. LiesAGENTS/Auftrag/Issue/Vorabplan/Autorenbericht/Vollcode/Aggregate und relevante originale lavaanR/Hilfequellen. Keine aktuellen Peer-/Jurorberichte/Loopfindings/Agentlisten/SOFTWARE-Reviewerurteile/zusätzlicheKoordinatorverteidigung. Prüfe tatsächliche ReihenfolgeVorabplanCodeRun/Inputs/Runtime/16Checks/FehlerStatus, vollständigeGamma22Reihenfolge/externesNACOVundWLSVverwendet/Standardfehler vsPunkte/VersionInternalAPI. Eigene sichere reproduzierendeProbe oder unabhängige Schnittstellengegenfälle, mindestens echte eigeneRechnung, unteroutputs/loop/methods002-repro/:nurkontrollierteKopieLauncher ausoutputs/loop/methods002/run-r-trial.py OWN/Festlabels/Probe gezieltändernundDiffHashbelegen. OriginalLauncher/Outputs/Prefixniemalsändern/starten,keineConda/Install/Geräte/IOCTL/UserFiles/GlobalWrites/ESSrawlocalA/BParteiLRAntworten;R--vanilla vorhandeneBibliothekenread-onlyNNPbenannteDateirechteOwn+devnull HOMEunverändert. Quellscope/Pfadeundalle8+95vor/nachhashenkeinesperrrelevanteunbekannteQuellelesen. Originalplan16Kriterien und tatsächliche Toleranzen gegenprogrammatischenChecksprüfen;keineGrenzenlockerung. Survey4.4-2OriginalhilfeerstnachnumerischenRun gelesenbleibtposthoc; nokeinePPS/FPC/MixedDesign/Domänen/Missing/Coverage/Empirie/persönlicheIntervalleAbnahmeausSoftwareprobe. BeiFormattransferparsedJSONexactequalityundunverändertenCode/Vorabplanbestätigen. Berichtnur reports/loop/reviews/METHODS-002-repro.md plusownOutput. JederFindingM2-Rxx genaueAussage/Problem/prüfbarerOriginalbeleg/Wirkung/begründeteSchwere/KorrekturNachprüfung/VermutungsstatuskeineFehlerquote. Vollständiger tatsächlicherStartauftragwortgetreu,Modellgpt-6.1-sol ultra geerbt interneRevision/Vorgabenunknown,verfügbare/genutzteTools/tatsächlicheCommandsExit/SharedFSGrenzen. KeineweiterenAgents/Peers/CommitPush/PnpmGesamtformat. VollständigabschließenOriginalbewahrenPfadSHAKurzbefund.
```

Modell laut Startkonfiguration `gpt-6.1-sol`, Reasoning `ultra`, geerbt. Interne Modellrevision und interne Anbieteranweisungen sind unbekannt. Es gab keine Beteiligung einer anderen Modellfamilie und keinen weiteren von mir gestarteten Agent.

Ich habe keine aktuellen Reviewer-, Juror- oder SOFTWARE-Reviewerberichte, keine Loop-Findings und keine Agentliste gelesen. Die laut AGENTS erforderlichen Projekt-, Prüf-, Analyse-, Beleg-, Entscheidungs- und Lizenzdokumente enthalten historische Auditverweise. Die dort verlinkten Berichte wurden nicht geöffnet; diese Verweise sind kein Beleg für mein Urteil. `reports/loop/state.json` und `findings.json` wurden wegen der ausdrücklichen unabhängigen Eingabegrenze nicht geöffnet. v1 wurde ausschließlich zum Transfervergleich genutzt.

Die Trennung ist organisatorisch und anhand der gelesenen Pfade nachvollziehbar. Das gemeinsame Dateisystem erlaubt Zugriff auf andere Dateien technisch weiterhin. Weder der Reviewkontext noch Landlock beweisen vollständige Read-Isolation. Es gab keine Peerkommunikation und keine nachgereichte Koordinatorverteidigung.

## Quellen und gebundene Fassung

Alle acht eingefrorenen Paketdateien wurden geprüft. Vollständiger Code ist `v2/files/pipeline/synthetic/methods-002.R`, Code-SHA `2d01a80bbe59eb1f8688706cd647b3a2ce24606ea402cb0cd726369f24c9c755`; Vorabplan `v2/files/reports/loop/METHODS-002-vorabplan.md`, SHA `3c2dc1fda00e369ae179aea34863f59d3dc5f54867a6f33ce071ba9c2a25fdec`. Gelesen wurden AGENTS, vollständiger Auftrag und Issue, Analyseanforderungen, Vorabplan, Autorenbericht, Code und Aggregate-JSON. Die vollständigen Pfade, Bytes und Hashes stehen in `outputs/loop/methods002-repro/before-hashes.json` und `after-hashes.json`.

Die 95 `sourceInputs` wurden für Integrität gehasht. Hashlesen bedeutet keine inhaltliche Freigabe aller 95 Quellen. Inhaltlich für das Urteil genutzt wurden die METHODS-002-Bindungs-, Start-, Log-, Ergebnis- und Transferdateien, der Originallauncher, die bekannte `scoped-env.json` und folgende gepinnte Originalsoftwarequellen:

- `outputs/loop/software-author/sources/lavaan/R/lav_muthen1984.R`, besonders 160–185, 204–269, 304–329 und 407–429. Sie zeigen Stackreihenfolge, Bread-Transformation, H und die Korrelationsindizes.
- `outputs/loop/software-author/sources/lavaan/R/lav_samplestats.R`, besonders 193–224, 240–271, 1217–1231 und 1395–1405. Sie trennen Nutzerinputs, native Gamma-Skalierung und den nur unter `WLS.VD` gespeicherten DWLS-Diagonalvektor.
- `outputs/loop/software-author/sources/lavaan/man/lavaan.Rd`, 88–111. Die Argumenthilfe nennt NACOV als N-fache Momentkovarianz, ihre Reihenfolge und `ov_order` bei externen Matrizen.
- `outputs/loop/software-author/sources/lavaan/R/lav_object_inspect.R`, 217–224 und 2251–2266. Der öffentliche `wls.v`-Inspektionspfad ist vom unmittelbaren internen Slotzugriff zu unterscheiden.
- `outputs/loop/methods002/survey-svyCprod.html`, Details; `survey-svyrecvar.html`, Details/Note; `supplemental-source-capture.json`. Die gespeicherte Hilfsversion ist 4.4-2.

Die offiziellen Seiten [Categorical data](https://lavaan.ugent.be/tutorial/cat.html), Abschnitt Endogenous categorical variables, und [Estimators and more](https://lavaan.ugent.be/tutorial/est.html), Abschnitt Estimators, wurden zusätzlich über das Webtool gelesen. Sie trennen DWLS-Punkte von robusten Standardfehlern und Tests. Diese Lektüre während meines Reviews nach den eigenen Läufen ist keine rückwirkende Vorabregistrierung des Autorenlaufs. Keine Aussage über den aktuellen ESS-Datensatz wurde daraus abgeleitet.

Keine Dateien in `data/raw/` oder `data/local/`, keine A/B-, Partei-, Links-rechts- oder menschlichen Antwortdaten wurden gelesen. Die eigene R-Probe erzeugt alle Antwortwerte im Arbeitsspeicher aus demselben ausdrücklich erfundenen Generator.

## Reihenfolge, Runtime und Formattransfer

`before-run-bindings.json` wurde laut gespeicherter UTC-Zeit um 05:12:28.002333 erzeugt. Sein Plan- und Codehash stimmen mit v2 und dem Startkommando überein. `trial-001-command.json` nennt Start 05:12:28.092663, Ende 05:12:28.958773, Exit 0, passenden Rscript-, Probe- und Launcherhash. `after-run-bindings.json` um 05:13:01.437025 bestätigt unveränderte gebundene Eingaben. Der Log enthält alle 16 Checks. Das trägt die dokumentierte Reihenfolge dieser vorhandenen Artefakte. Selbst dokumentierte Zeitstempel sind keine vollständige forensische Garantie gegen einen unprotokollierten früheren Lauf. Im Prüfpaket gibt es keinen Beleg eines früheren numerischen Fehlversuchs.

Die eigene Laufzeit bestätigt R 4.5.3, lavaan 0.7-2, jsonlite 2.0.0, OpenBLAS 0.3.34, festgelegte RNG-Einstellungen, Locale C.UTF-8, UTC und jeweils einen BLAS-/OMP-Thread. Der Rscript-Hash vor und nach jedem eigenen Start ist `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`. Der Originalcode verlangt genau lavaan `0.7.2`, verweigert Generalized Inverses der beiden Bread-Blöcke und bezeichnet `muthen1984`/`lav_m84_b_inv` ausdrücklich als interne versionsgebundene Funktionen. Es wird keine stabile öffentliche API aus ihnen abgeleitet.

`format-equality.json` bestätigt bytegleichen numerischen Code und Vorabplan zwischen v1 und v2 sowie exakte geparste Gleichheit von v1-JSON, v2-JSON und der ursprünglichen R-Ausgabe. Raw-SHA ist `4e4d5219c22dc9d8360e26fc1407eebf1a72a8678e21258786e852f2172c4c22`, formatierter öffentlicher SHA `0f0caabd4dbb9a9e5947e13eed2fbbab0622430ea7d65ccb0c803b8dbf100639`. Der Bericht erhielt zusätzlich die Hashklarstellung und den Absatz zum Formatablauf. Deshalb sind nicht alle Berichtstextbytes oder sämtliche Textaussagen bloß neu eingerückt; die numerische Rechnung, Kriterien und Ergebnisse wurden tatsächlich nicht geändert. Kein numerischer Nachlauf wird aus diesem Transfer allein erforderlich.

Die Survey-Hilfen wurden laut Capture erst um 05:18:37.988863 beziehungsweise 05:18:38.263909 abgerufen, nach dem numerischen Lauf. Der Autor nennt das in Zeile 27 ausdrücklich. Es bleibt post hoc. Weder diese Hilfe noch meine Rechnung prüft einen survey-Paketlauf oder bestätigt PPS, FPC, Mischdesign, Domänen, Missing, finite Coverage oder empirische Intervallgüte.

## Die 16 tatsächlichen Checks gegen den Vorabplan

Bezug für alle Codezeilen ist die unveränderte eingefrorene Datei `v2/files/pipeline/synthetic/methods-002.R`. Der Plan hat sechs zusammenfassende Prüfabsätze; der vor dem Run gehashte Code setzt sie mit den folgenden 16 benannten Checks um. Es gibt keine gelockerte numerische Grenze.

| Check | Code | Tatsächliche Regel | Eigene Reproduktion |
| --- | --- | --- | --- |
| `full_native_gamma` | 75–77 | vollständige Gamma-Differenz ≤ 1e-7 | 3.774758283725532e-15 |
| `finite_dimension` | 83–84 | genau 22×22 und vollständig endlich | wahr |
| `symmetry` | 85 | max. absolute Symmetriedifferenz ≤ 1e-7 | wahr |
| `threshold_covariance_oracle` | 87–104 | alle 16×16 Schwellenkovarianzen ≤ 1e-7 | 4.7704895589362195e-18 |
| `all_weighted_thresholds` | 105–109 | sämtliche 16 gewichteten Schwellen ≤ 1e-7 | 6.135126118245182e-8 |
| `external_native_gamma_import` | 112–114 | gespeicherte externe native Gamma ≤ 1e-7 | wahr |
| `external_stratified_gamma_import` | 113–115 | gespeicherte externe geschichtete Gamma ≤ 1e-7 | wahr |
| `same_dwls_point_estimates` | 116–117 | sämtliche Koeffizienten ≤ 1e-7 | 0 |
| `stratum_change_changes_covariance` | 120–125 | max. absolute Gamma-Änderung > 1e-7 | 2.181457427275821 |
| `stratum_change_keeps_points` | 126–127 | Koeffizienten ≤ 1e-7 | wahr |
| `renaming_invariant` | 128–129 | gemeinsame reine Umbenennung ≤ 1e-7 | wahr |
| `weight_scale_invariant` | 130–133 | gemeinsame Gewichtsmultiplikation mit 7 ≤ 1e-7 | 0 |
| `singleton_rejected` | 134–136 | genau vorgesehene Singleton-Fehlermeldung | wahr |
| `cross_stratum_cluster_rejected` | 137–139 | genau vorgesehene Mapping-Fehlermeldung | wahr |
| `finite_estimates_and_se` | 156 | sämtliche est und se endlich | wahr |
| `converged_and_admissible` | 157 | Konvergenz und Postcheck wahr | wahr |

Eigenwerte, Spaltensummen, Warnungen und Kovarianzdifferenzen sind Beobachtungen. Positive Eigenwerte sind hier ausgegeben, keine separat vorab festgelegte wissenschaftliche Güteschwelle. Der Code erfindet keine Fit-Cutoffs. Die ursprüngliche erfolgreiche Ausgabe hat keine `error`-Eigenschaft: R entfernt einen Listeneintrag bei Zuweisung von NULL. Das ist vom Fehlerstatus eines fehlgeschlagenen Laufs zu unterscheiden.

Die Abschlussformel in 165–166 verlangt keine Fehler, wenigstens einen Check und ausschließlich bestandene vorhandene Checks. Sie prüft nicht selbst, dass genau die erwarteten 16 Namen vorhanden sind. Meine reine Statusgegenrechnung demonstriert das mit einer künstlich unvollständigen Liste; in der aktuellen Fassung sind alle 16 vorhanden und wurden tatsächlich ausgeführt. Das ist eine Härtungsmöglichkeit, kein Beleg eines fehlenden aktuellen Checks. Warnungen werden aufgezeichnet, machen nach der ursprünglichen Regel aber nicht automatisch einen technischen Fehlschlag. Im Original und in meiner erfolgreichen Probe sind sie leer.

## Eigene Rechnung und Gegenfälle

Sämtliche eigenen Artefakte liegen ausschließlich unter `outputs/loop/methods002-repro/`. Die kopierten Launcher ändern nur OWN und feste Lauf-/Probe-/Lognamen. `launcher.diff`, `launcher-002.diff`, `launcher-003.diff` und die vor jedem Start geschriebene Hashbindung belegen das. Landlock-Rechte, `--vanilla`, NNP, HOME-Prüfung, installierter Prefix, Timeout, Descriptorregeln und Supervisorlogik bleiben übernommen. Probeänderungen und Reparaturgründe stehen in `probe.diff`, `probe-002.diff`, `probe-003.diff` und den vorab gespeicherten Reparaturvermerken.

Der zuerst gespeicherte eigene Plan wird nicht überschrieben. Meine zusätzlichen Prüfungen hatten dieselbe absolute Grenze 1e-7. Fehlversuche bleiben sichtbar:

| Eigener Start | UTC-Zeiten im jeweiligen Kommando | Exit | Tatsächlicher Befund |
| --- | --- | --- | --- |
| `python outputs/loop/methods002-repro/run-r-repro.py repro-001` | `repro-001-command.json` | 1 | Alle 16 Originalchecks bestanden. Eigene WLS.V-Änderung scheiterte an meiner Matrixannahme. |
| `python outputs/loop/methods002-repro/run-r-repro-002.py repro-002` | `repro-002-command.json` | 1 | Eigene Messung zeigt WLS.V-Länge 0. Zusätzlicher Gewichtsnutzungstest blieb negativ; meine Stringrückgabe wurde außerdem als Fehler interpretiert. |
| `python outputs/loop/methods002-repro/run-r-repro-003.py repro-003` | 05:41:24.503407 bis 05:41:25.719730 UTC | 0 | Alle 16 Originalchecks und alle 13 eigenen konkreten Kontrollchecks bestanden; keine Warnung. |

Meine erste Reparaturerklärung war zu früh: Der Diagonalvektor liegt in `WLS.VD`, während `WLS.V[[1]]` tatsächlich NULL ist. Der zweite Reparaturvermerk korrigiert diese eigene Erklärung ausdrücklich. Beide früheren Probeskripte, Kommandos, Logs und Ergebnisdateien bleiben erhalten. Die Originalgrenzen wurden nie angepasst. Ein Python-Lese-/Transferkommando endete ebenfalls mit Exit 1, weil ich bei einer erfolgreichen R-Ausgabe fälschlich `x['error']` erwartet hatte; die Transferdatei war zuvor vollständig geschrieben. Die späteren Prüfungen verwenden den optionalen Fehlerwert korrekt.

Die vollständige Momentreihenfolge wurde gegen die Originalhilfe und tatsächliche Runtime geprüft:

```text
y1|t1 y1|t2 y1|t3 y1|t4
y2|t1 y2|t2 y2|t3 y2|t4
y3|t1 y3|t2 y3|t3 y3|t4
y4|t1 y4|t2 y4|t3 y4
y1~~y2 y1~~y3 y1~~y4 y2~~y3 y2~~y4 y3~~y4
```

Das ist zunächst der itemweise Schwellenstack und danach die untere Korrelationsdreiecksmatrix spaltenweise. Im reinen ordinalen Beispiel fehlen Slopes und kontinuierliche Varianzen. Die tatsächlichen `wls.obs`-Namen sind exakt gleich. Mein unabhängiger Aggregator benutzt eine explizite PSU-Indikatormatrix und pro Schicht `I − 11'/G_h`, dann `N G_h/(G_h−1)`. Für die gesamten 22×22 Momente liegt seine maximale Differenz zur Kandidatenaggregation bei `1.3322676295501878e-15`. Die Fallbeiträge selbst stammen weiterhin aus lavaan; dies ist keine unabhängig hergeleitete vollständige Polychorik- oder SEM-Theorie.

Mit wirklich übergebenem 22-elementigem `WLS.VD`-Input ergeben sich gegenüber der Originalrechnung identische Punkte und Parameterkovarianzen, Differenz jeweils 0. Reine Verdopplung von NACOV bei festem tatsächlich externem Gewicht lässt die Punkte gleich, verdoppelt die Parameterkovarianz exakt und erzeugt das erwartete SE-Verhältnis sqrt(2), maximale Differenz `2.220446049250313e-16`. Der robuste Skalierungsfaktor verdoppelt sich von `0.42316525729042326` auf `0.8463305145808465`; die korrigierte Teststatistik ändert sich. Damit wird NACOV tatsächlich für Unsicherheit und Test verwendet, nicht bloß gespeichert.

Der gezielt veränderte echte WLS.VD-Input wird exakt übernommen und verändert Koeffizienten um maximal `0.01893318245569131`. Das belegt seine tatsächliche Wirkung in meinem Zusatzlauf. Ein absichtlich rückwärts permutierter NACOV-Input mit mitpermutierten Dimnames wird positional übernommen, gespeicherte Differenz zum falschen Input 0. Die Namen reparieren die falsche Reihenfolge nicht; der Parameterkovarianzunterschied zum korrekten Fit ist `0.031602569613956105`. Dieses falsche Beispiel ist ein Schnittstellengegenfall, keine zulässige Designalternative. Der Originalfall hat nach meiner Reihenfolgenprüfung die richtige Anordnung.

## Finding M2-R01

Betroffene Aussage: Vorabplan Zeile 15 nennt die externe dokumentierte `nacov`-/`wls_v`-Schnittstelle. Autorenbericht Zeile 9 behauptet, der Punktfit behalte dieselbe DWLS-Gewichtsmatrix, und Zeile 25 bezeichnet die numerischen Ergebnisse als Nachweis der Schnittstellenbehauptung. Das Paket präsentiert damit einen Versuch mit gemeinsam extern übergebener Gamma und WLS.V.

Konkretes Problem: `external()` in Originalcode 110–111 übergibt `native@SampleStats@WLS.V[[1L]]`. Dieser Wert ist unter dem aktuellen nativen DWLS-Fit NULL. Der externe Aufruf erhält somit `wls_v = NULL`, worauf lavaan die Gewichtung erneut aus den Daten berechnet. Die zwei importbezogenen Originalchecks prüfen nur Gamma. Die Punktekonstanz beweist hier keinen externen WLS.V-Import.

Prüfbarer Originalbeleg: `lav_samplestats.R:1402–1405` schreibt im DWLS-Zweig nur `wls_vd[[g]]`; das Schreiben der vollen `wls_v` ist auskommentiert. `lav_samplestats.R:193–195` setzt für NULL `wls_v_user = FALSE`; 213–223 zeigt dagegen die tatsächliche Behandlung eines Nutzervektors oder einer Matrix. Die unabhängige aktuelle Runtimebeobachtung ist `repro-003-result.json`, `reviewInterface.originalWlsVInputIsNULL = true` und `originalDiagonalLength = 22`. `repro-002-result.json` erhält die vorherige direkte Messung der Länge 0 des Originalinputs. `repro-003` liefert erst im ausdrücklich zusätzlichen Aufruf einen wirklich externen Input.

Wirkung: NACOV-Import, geschichtete Kandidatenkovarianz, native Gamma-Reproduktion und numerische Punktgleichheit bleiben belegt. Nicht belegt ist der im Original behauptete Test beider externen Inputs. Der Fehler verändert in diesem Beispiel keine Originalpunkte, weil die erneut berechneten DWLS-Gewichte dieselben sind. Er kann eine defekte oder gar nicht benutzte Gewichtsschnittstelle verbergen. Aus den 16 grünen Checks darf diese zusätzliche Aussage nicht abgeleitet werden.

Schweregrad: `MITTEL`, erheblich für die konkrete behauptete doppelte Schnittstellenprüfung. Das Problem muss vor deren positivem Abschluss behoben oder der Anspruch ausdrücklich auf NACOV begrenzt werden. Kein Befund einer falschen ESS-Varianz, kein Datenschutzvorfall und kein Grund, die tatsächlich bestandenen 16 Vergleiche zurückzunehmen.

Korrektur und Nachprüfung: Einen nichtleeren korrekt geordneten 22×22-Input aus dem öffentlichen `lavInspect(native, 'wls.v')` oder den ausdrücklich versionsgebundenen WLS.VD-Diagonalvektor übergeben. Dimension/Länge, Endlichkeit, Reihenfolge und tatsächliche gespeicherte Übernahme kontrollieren; als Gegenfall einzelne Korrelationsgewichte ändern und ihre numerische Wirkung nachweisen. Den ursprünglichen Lauf und Plan erhalten, Änderung als technische Reparatur nach Ergebniskenntnis kennzeichnen, Grenzen unverändert lassen und Paket neu einfrieren. Alternativ den Bericht auf den tatsächlich ausgeführten NACOV-Test beschränken. Meine erfolgreiche Zusatzrechnung zeigt die Machbarkeit der Korrektur; sie repariert und ersetzt nicht das eingefrorene Original.

Vermutungsstatus: `BELEGT`, keine bloße Vermutung. Keine Fehlerquote wurde vorgegeben oder gesucht.

## Werkzeuge, Kommandos und Grenzen

Verfügbar waren `functions.exec` einschließlich 633 angezeigter verschachtelter Werkzeugnamen, die separaten Funktionen-, Clock-, Collaboration- und Computer-Use-Schnittstellen. Das Namensinventar steht in `outputs/loop/methods002-repro/tool-inventory.json`; Verfügbarkeit ist keine Nutzung. Tatsächlich genutzt wurden `functions.exec`, darin `exec_command`, `write_stdin` und `web__run`. Shellhilfen waren Python 3, `pwd`, `rg`, `cat`, `nl` und `sed`; der numerische Kindprozess verwendet ausschließlich das vorhandene Rscript und setpriv. `write_stdin` pollte zwei bereits gestartete eigene Shellsessions. Keine Collaboration-, Computer-Use-, Installations-, Claude-, Conda- oder Gerätewerkzeuge wurden genutzt.

Jeder Shellaufruf hatte explizit CWD `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Die ausgeführten numerischen Aufrufe und Exitcodes stehen vollständig oben; jedes `repro-00x-command.json` enthält zusätzlich die vollständige tatsächliche setpriv-/Rscript-Argumentliste, Umgebung und Start-/Endzeit. Originallauncher wurde nur gelesen und kopiert, niemals gestartet.

Die weiteren tatsächlichen Shellaufrufe bestanden aus den oben benannten `cat`-/`nl`-/`sed`-Lektüren, einem begrenzten `rg --files` für AGENTS/Manifest/Methodenpfade, `rg -n` an den genannten Original-R-Dateien sowie Python-Heredocs für vor/nach-Hashes, den exakten JSON-/Texttransfervergleich, eigene Launcher-/Probe-/Planerstellung, das Lesen der eigenen Ergebnisse und das Werkzeugnamensinventar. Alle beendeten sich mit Exit 0 außer dem dokumentierten `error`-KeyError im Transfer-/Lesekommando. Die drei R-Starts und ihre zwei eigenen numerischen Fehlversuche sind nicht hinter dieser Zusammenfassung verborgen. Schreiben der Probeskripte war kein eigener R-Lauf; vor jedem tatsächlichen R-Start wurden die fertigen Inhalte gehasht. Die exakten endgültigen Skripte, Änderungen und Startargv erlauben ihre Nachrechnung ohne erneutes Starten des Originals.

Der R-Kindprozess hat NNP, unverändertes HOME und die übernommenen zwölf benannten Dateirechte nur unter dem eigenen Ordner sowie write-file auf `/dev/null`. Die vorhandenen Bibliotheken bleiben für diese behandelten Rechte schreibgeschützt. Netzwerk, Read/Execute, IOCTL, alle Gerätetypen, vererbte Deskriptoren und der Python-Supervisor sind damit nicht vollständig kontrolliert. Ich habe keine entsprechenden Nutzerdaten-/Geräte-/Globalwrite-Proben ausgeführt. Es wird kein vollständiger PC- oder Prefix-Audit behauptet.

Keine Gitbefehle, Commits oder Pushes ausgeführt. Keine Gesamtformatierung und keine UI-Prüfung; es gab keine UI-Änderung. `pnpm check > outputs/loop/methods002-repro/pnpm-check.log 2>&1` wurde ausgeführt und endete mit Exit 1: `format:check` meldet ausschließlich `reports/loop/state.json`. Diese außerhalb des unabhängigen Reviewumfangs liegende Datei wurde weder geöffnet noch korrigiert. Handbuch-/Schema-Prüfung, Typecheck, Tests und Build wurden durch die AND-Verknüpfung nicht ausgeführt, Status `NICHT_GEPRÜFT`. Das ist eine technische Integrationsgrenze, kein methodisches Urteil.

Die abschließende Hashprüfung bestätigt alle acht Paketdateien und alle 95 gebundenen Eingaben bytegleich zu Manifest und Vorabstand, 103 von 103, einschließlich des unveränderten v2-Manifests. `after-hashes.json` und `final-status.json` halten Abschlussbindung und Checkstatus fest. Dieser Review schließt keine ausdrücklich offenen wissenschaftlichen Voraussetzungen.
