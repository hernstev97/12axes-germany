# METHODS-002 v2: unabhängige methodische Erstprüfung

Reviewer `/root/methods002_statistics`, 3. Oktober 2026. Ziel ist die synthetische Schnittstellenprobe. Ich bin nicht Autor des Pakets und habe keine aktuellen Peer- oder Jurorberichte, Loopfindings oder SOFTWARE-Reviewerurteile gelesen. Keine anderen Agents eingesetzt. Dies ist ein KI-Review, keine akademische Begutachtung.

Die mathematische Kette und die externe Schnittstelle tragen die enge Machbarkeitsaussage. Ein bestätigter Prüffehler bleibt offen: Das als marginales Schwellenorakel bezeichnete Kriterium prüft modellimplizierte Schwellen. Das ist M2-S01. Außerdem bezeichnet die Versionsakte eine kleine redaktionelle Ergänzung ungenau als ausschließliches Layout, M2-S02. Die Aussage, alle 16 vorab bezeichneten fachlich richtigen Ziele seien durch die Codechecks bestätigt, ist deshalb für v2 **NICHT_BESTANDEN**. Die tatsächlich ausgeführten 16 Autoren-Codechecks sind grün; dieser Laufbefund wird nicht bestritten.

| Prüfbereich | Urteil und Reichweite |
| --- | --- |
| Bindung des eingefrorenen Pakets | BESTANDEN: 8 Dateien und 95 SourceInputs vor und nach der eigenen Prüfung unverändert passend; Sperrpfad- und Symlinkprüfung ausgeführt. |
| SC/B-inverse/H, Schichtzentrierung, N-Skalierung, externe NACOV/WLSV-Machbarkeit | BESTANDEN für die geprüften rein ordinalen vollständigen synthetischen Fälle. |
| Behauptete Bestätigung sämtlicher 16 Vorabziele | NICHT_BESTANDEN bis zur nachgeprüften Zielgrößenkorrektur M2-S01. |
| Redaktionelle Beschreibung v1 → v2 | Korrektur offen, niedrige Schwere M2-S02; numerische Inputs und Ergebnisse unverändert. |
| Empirische ESS-Designlösung, Modellwahl, wissenschaftliche Validität | NICHT_GEPRÜFT. Dieses Paket erteilt keine entsprechende Abnahme. |
| Reproduktion aus frischem öffentlichen Checkout und vollständiger Umgebung | NICHT_GEPRÜFT; vorhandener lokaler Prefix geprüft, keine Installation oder vollständige Pipeline-Reproduktion. |

## Eingaben und Trennung

Autoritativ ist `reports/loop/packages/METHODS-002/v2/manifest.json`, SHA256 `b736855447a96dcaa3f55926edf59d7eda29c19dfe90d2e752de18df8b0d78e4`, CodeCommit `5fd7bb37e44addcc13bd6840a8ad6e4339f1c9e2`. Meine Prüfung bezieht sich auf diese Dateiinputs, nicht auf einen beliebigen späteren Arbeitsbaum. Der aufgeführte Commit allein bindet nicht die lokalen Laufzeitinputs.

Selbst gelesen wurden die eingefrorenen AGENTS-, Auftrags-, Issue-, Analyseanforderungs-, Vorabplan-, Autorenbericht- und R-Codefassungen, die Aggregatausgabe und die tragenden originalen lavaan-Dateien. Ergänzend gelesen wurden `docs/project.md`, `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md`, `docs/entscheidungen.md`, `docs/arbeitsloop.md` und `docs/lizenzen.md`. Der allgemeine Wiederaufnahmeauftrag, Zustand/Findings/Agents zu lesen, wurde in dieser abgegrenzten Erstprüfung nicht auf deren aktuelle fremde Urteile angewandt. Die ausdrückliche Trennung im Reviewerauftrag geht vor. Projektgrundlagendokumente nennen historische Audits; deren eigentliche Berichte habe ich nicht geöffnet.

`before-review-bindings.json` und `after-review-bindings.json` unter `outputs/loop/methods002-statistics/` enthalten sämtliche 103 tatsächlich nachgerechneten Byte-/SHA-Bindungen. Alle stimmen. Keine Traversalpfade, Symlinks oder Pfade nach `data/raw`, `data/local` beziehungsweise Reviewdateien unter diesen freigegebenen Inputs. Rscript blieb bei SHA256 `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`. Die Tabellen/Hashes sind Integritätsnachweise und keine methodische Freigabe.

V1 habe ich ausschließlich zur Nachrechnung des behaupteten Formattransfers gelesen. Der ursprüngliche R-JSON-Output, v1-JSON und v2-JSON haben exakt gleiche geparste Werte. R-Code und Vorabplan sind bytegleich. V1-Manifest-SHA `f94a4eec6539730c2d73ef5899ebf648a53d75455bc20436443be74c5047a0d4` stimmt mit der v2-Rückbindung. Berichtstextänderungen stehen unter M2-S02; `format-transfer-check.json` bewahrt den tatsächlichen Vergleich.

Die Dateitrennung ist organisatorisch. Das gemeinsame Dateisystem ist keine Informationssandbox. Es gibt keinen technischen Beweis, dass andere Agents diese eigenen Dateien nicht lesen konnten. Ich habe keine Peerbewertungen eingeholt und keine zusätzliche Autorverteidigung gelesen. Die einzigen Nachrichten gingen an den Koordinator und berichteten den eigenen Stand.

## Mathematische Gegenprüfung

Für die hier vier fünfstufigen rein ordinalen Items ist der Momentvektor 22-dimensional: vier Schwellen je Item, insgesamt 16, danach sechs Polychoriken. Die Reihenfolge innerhalb des letzten Blocks folgt der unteren Dreiecksmatrix ohne Diagonale, spaltenweise. Das dokumentiert `outputs/loop/software-author/sources/lavaan/man/lavaan.Rd:88–104`. Die Namen können die symmetrischen Korrelationen als `x1~~x2` beschriften; daraus wird kein anderer numerischer Moment als die Position (2,1).

Der gepinnte Originalcode `R/lav_muthen1984.R:160–206, 218–269, 499–540` bildet gewichtete gestapelte Fallgleichungen SC und den unteren Blockdreieck-Bread

```text
B = [A11   0]
    [A21 A22]

B^-1 = [A11^-1                      0]
       [-A22^-1 A21 A11^-1    A22^-1]

Psi = SC B^-T H^T
```

Damit gilt `crossprod(Psi) = H B^-1 crossprod(SC) B^-T H^T`. Die Fallbeiträge sind bereits Beiträge zum geschätzten Momentvektor, nicht unskalierte Einzelbeobachtungen, die später nochmals durch N geteilt werden müssten. A11/A22 sind aus gewichteten Summen aufgebaut. Bei Designgewichten trägt der Meat die quadrierten Gewichte; `lav_muthen1984.R:218–234` trennt dies ausdrücklich von Frequency-Gewichten.

In der geprüften rein ordinalen Konfiguration ist H exakt die Identität, Originalcode `264–266`. Das bestätigt die korrekte aktuelle Kette, prüft aber keine nichttriviale Transformation bei gemischt kontinuierlichen/ordinalen Items. Eine Generalisierung auf solche Items wäre ein neuer Prüfschritt, einschließlich des Vorzeichenwechsels numerischer TH-Slots in `272–285`.

Für Clustertotale `T_hg = Summe_i Psi_i` in Schicht h berechnet der Kandidat

```text
V_strat = Summe_h [G_h/(G_h-1)]
                   Summe_g (T_hg - Mittel_g T_hg)(T_hg - Mittel_g T_hg)^T
Gamma_strat = N V_strat
```

Der native ordinale Clusterpfad verwendet hingegen unzentrierte Cluster-Outerproducts und die globale Korrektur G/(G−1). Originalstellen `lav_muthen1984.R:236–247` und `lav_samplestats.R:1217–1231` tragen genau `Gamma_native = N G/(G−1) Summe_g T_g T_g^T`. Eine Schichtkorrektur ist in dieser nativen Formel nicht enthalten. Eine zufällig kleine Gesamtsumme der geschätzten Gleichungsbeiträge macht die globale Zentrierung in einem konkreten Lauf nahezu folgenlos, beseitigt aber nicht die Schichtmittel oder den Unterschied der Korrekturfaktoren.

Meine unabhängige Rechnung nutzt eine vollständige direkte Inversion von B sowie eine PSU-Zuordnungsmatrix und explizite Zentrierungsprojektionen `I − 11^T/G_h`. Sie kopiert die Autorenaggregation nicht als Orakel. Die vorhandene Autorenfunktion wurde ausschließlich als einzelner geprüfter Funktionsausdruck aus dem Parsebaum ausgewertet. Der vollständige Autoren-Code und der ursprüngliche Launcher wurden nie ausgeführt.

Für eine Schwelle `tau_jk = Phi^-1(p_jk)` ist der separate gewichtete Delta-Beitrag

```text
p_jk = Summe_i w_i 1(y_ij <= k) / Summe_i w_i
phi_ijk = w_i [1(y_ij <= k) - p_jk]
          / [Summe_i w_i · Normaldichte(tau_jk)]
```

Die 16 so unabhängig berechneten Fallbeiträge und ihre Kovarianz passen zur ersten 16er-Komponente von Psi. Diese Prüfung trägt marginale Schwellen, einschließlich ihrer gegenseitigen Kovarianzen. Sie liefert keine unabhängige Herleitung der sechs Polychorikbeiträge oder vollständige SEM-/Survey-Theorie. Die volle 22×22-Parität gegen dieselbe lavaan-Version ist Implementierungsparität, kein externes theoretisches Orakel.

## Eigene synthetische Läufe und Gegenbeispiele

Meine neuen Daten haben Seed 734129, Mersenne-Twister/Inversion/Rejection, 687 vollständige erfundene Fälle, 39 PSUs in drei Schichten mit 9/13/17 PSUs, wechselnde Clustergrößen 13–23, vier fünfstufige ordinale Items mit unterschiedlichen Trennpunkten und positive erfundene Gewichte. Es wurde keine Antwortdatei gelesen und keine Personenzeile exportiert. Die Konfiguration unterscheidet sich vom Autorenbeispiel. Sie erweitert Softwarebeobachtung; sie ist kein Coverage-Experiment für ein reales Stichprobendesign.

| Eigene ausgeführte Rechnung | Beobachtung |
| --- | --- |
| Vollständige B-Inversion gegenüber internem Blockhelfer | Maximaldifferenz 1,0842e−19, keine verallgemeinerte Inverse. |
| Sieben originale Helper-Funktionskörper/-Formalargumente gegenüber laufendem Namespace | Alle identisch. Version R 4.5.3 / lavaan 0.7-2. |
| Numerischer 22er-Momentvektor gegenüber TH und spaltenweisen Polychoriken | 5,5511e−17. |
| Vollständige unzentrierte native Gamma | 4,4409e−15. |
| Aus SC und voller B-Inversion hergestellter iid-Sandwich gegenüber Original-WLS.W | 3,2526e−19. |
| Autorenaggregation gegenüber unabhängiger Zentrierungsprojektion | 1,7347e−18 auf Kovarianzskala. |
| Alle 16 separaten Delta-Fallbeiträge | 1,0408e−17. |
| Alle 16 geschichteten Schwellenkovarianzen | 1,5613e−17. |
| Tatsächliche 16 Stichprobenschwellen gegenüber qnorm-Orakel | 4,4409e−16 nach Korrektur des eigenen Prüfziels in Lauf 004. |
| Autorenartiger Vergleich modellimplizierter Schwellen gegenüber qnorm | 1,3356394e−7, über der unveränderten 1e−7-Grenze; M2-S01. |
| Externer Import beider Gamma-Matrizen, DWLS-Punkte | Importdifferenzen 0, Punktdifferenz 0. |
| Native und extern importierte native Parameterkovarianz | 2,0817e−16. |
| Globale Multiplikation der **rohen Fitgewichte** mit 11 | Gamma 1,2399e−8, Punkte 6,2099e−9, jeweils innerhalb 1e−7. Dies prüft tatsächlich den Fit und ergänzt den nur vorher re-normalisierten Autorencheck. |
| Willkürliche Cluster-/Schichtumbenennung mit geänderter Lexik und zufälliger Zeilenreihenfolge | Gamma 1,3323e−15. |
| Andere fest determinierte, antwortunabhängige Schichtpartition | Gamma 0,67528 und Parameterkovarianz 0,005493 verändert; Punkte unverändert. |
| Singleton und Cluster über Schichtgrenze | Beide mit den bezeichneten Vertragsfehlern abgewiesen. |
| Sichtbare Eigenwerte und Fitbeobachtungen | Gamma 0,04338–26,49397; Parameterkovarianz 0,0001257–0,08819; konvergiert/post.check TRUE; keine Warnungen. Keine empirische Fitabnahme. |

Ein zusätzliches von Hand nachgerechnetes Beispiel hat fünf erfundene PSU-Beiträge `(1,2), (3,−1), (4,3)` in Schicht a und `(−2,5), (2,7)` in Schicht b. Unzentrierte Outerproducts sind `[[34,15],[15,88]]`; die globale G/(G−1)-Korrektur ergibt `[[42.5,18.75],[18.75,110]]`. Die geschichtete Rechnung ergibt `[[23,8.5],[8.5,17]]`, exakt durch die Autorenfunktion bestätigt. Schichtzentrierung ist hier sichtbar eine andere Rechnung und nicht durch einen Austausch des globalen Korrekturfaktors erledigt.

Die drei ursprünglichen Fehlstatus bleiben erhalten. Lauf 001, Exit 1, enthält zunächst zusätzlich einen eigenen Labelvergleichsfehler: Ich erwartete für symmetrische Korrelationen `x2~~x1` statt der tatsächlich kanonischen Schreibweise `x1~~x2`. Numerische Reihenfolge war bereits richtig. Lauf 002, Exit 1, korrigiert diese eigene Zeichenfolge, bleibt aber beim Schwellenkriterium rot. Lauf 003, Exit 1, prüft eine vermutete Gewichtsnormierungs-/Rundungsursache. Die beiden Normalisierungen differieren zwar um 2,22e−16, erklären aber den Befund nicht: auch die exakten native@Data-Gewichte reproduzieren die separaten marginalen TH, nicht die modellimplizierten th. Diese Hypothese wurde widerlegt. Erst die Originallektüre der Inspect-Funktion weist das falsche Prüfobjekt nach.

Lauf 004, Exit 0, behält Daten, Seed und Toleranzen und korrigiert **nur mein eigenes** Schwellenkriterium auf die tatsächlich beobachteten Stichprobenmomente. Alle 26 eigenen Checks bestehen dann. Die unveränderte frühere Modellimpliziert-Abweichung bleibt unter `correctedTargetDiagnostics` sichtbar. Das ist ein Nachweis der vorgeschlagenen Korrektur, keine nachträgliche Änderung oder Abnahme des Autorenpakets.

## Findings

### M2-S01: Das marginale Schwellenorakel fragt modellimplizierte Schwellen ab

**Betroffene Aussage:** Vorabplan Zeile 14 verlangt alle 16 marginalen Schwellen; Autorenbericht Zeile 14 und die pauschale 16-Kriterien-Behauptung in Zeile 5 geben ihre Übereinstimmung mit gewichteten qnorm-Wahrscheinlichkeiten als bestätigt aus.

**Problem und Originalfundstelle:** `pipeline/synthetic/methods-002.R:105–109` setzt `observed_thresholds <- lavInspect(native, 'th')`. Die gepinnte originale `outputs/loop/software-author/sources/lavaan/R/lav_object_inspect.R:1893–1900` liefert dafür `object@implied$th` beziehungsweise bei bedingten Modellen `res.th`. Das sind modellimplizierte Schwellen. Die Stichprobenmomente stehen gemäß derselben Datei `2207–2210` in `object@SampleStats@WLS.obs`. Das aktuelle freie Schwellenmodell bringt beide Größen numerisch nahe zusammen, ersetzt aber die verlangte Zielgröße nicht.

**Wirkung und belegte Schwere:** Mittel, auf die Prüfverdrahtung begrenzt. Im Autoren-Seed wird ein anderes Objekt innerhalb der Toleranz getroffen. Der eigene Datensatz zeigt einen Fehlstatus von 1,3356394e−7 bei unveränderter Grenze 1e−7, während die tatsächlichen Stichprobenschwellen bis 4,44e−16 passen. Damit hängt dieser Check unnötig von der Modelloptimierung ab und beweist das geplante marginale Orakel nicht direkt. Keine bestätigte Verfälschung von Psi, Schichtkovarianz oder NACOV; deren getrennte Gegenrechnungen bestehen. Ich leite daraus kein Scheitern der engen Importmachbarkeit ab.

**Korrektur und Nachprüfung:** Den Stichprobenschwellenblock aus `lavInspect(native, 'wls.obs')` anhand der ausdrücklichen, überprüften Momentlabels abgreifen, alternativ den passend dokumentierten SampleStats-TH-Vektor. Keine blind angenommenen Indizes bei später geänderter Item-/Momentkonfiguration. Den Modellimpliziert-Vergleich kann man zusätzlich als separaten Fitbefund behalten. Gleiche Kriterien/Toleranz, Originalseed und eigener Seed müssen neu laufen; Code, Aggregate und Autorenbericht als neue Version einfrieren, v2 erhalten. Mein Lauf 004 bestätigt die konkrete Zielgrößenkorrektur auf dem eigenen Seed, Autorstand weiterhin unkorrigiert.

**Vermutungsstatus:** Kein Verdacht. API-Bedeutung am Originalcode und Verhalten im sicheren eigenen Lauf bestätigt. Eine zunächst geprüfte Rundungshypothese war falsch und steht weiterhin im Prüfverlauf.

### M2-S02: Der als reiner Formattransfer bezeichnete Berichtswechsel enthält Textzusätze

**Betroffene Aussage:** Manifestfeld `correctionScope` nennt ausschließlich Formatierung. Autorenbericht v2 Zeile 33 behauptet ausschließlich Berichtslayout und JSON-Einrückung.

**Problem und Originalfundstelle:** Der erlaubte v1/v2-Bytevergleich zeigt außer Tabellenlayout/Markdown-Escaping eine präzisierte SHA-Zuordnung in Autorenbericht Zeile 5 und einen neuen sachlichen Absatz über Formatcheck, Outputbindung und v2 am Ende. `format-transfer-check.json` hält fest: geparste JSON-Werte, R-Code und Plan gleich, Berichtsinhalt auch nach Entfernen allen Whitespace nicht gleich. Die Befunde widersprechen keiner numerischen Ergebnisgleichheit, wohl aber dem absoluten Wort „ausschließlich“ beim Berichtslayout.

**Wirkung und belegte Schwere:** Niedrig. Der vollständige Prüfumfang und die numerische Gleichheit sind gut dokumentiert; die Veränderungen präzisieren Provenienz und ändern keine Formel, Kriterien oder Ergebnisse. Kein Grund, die numerischen Prüfungen deswegen erneut als ungeprüft zu behandeln. Eine präzise Änderungsakte sollte jedoch Textpräzisierungen von Byteformatierung unterscheiden.

**Korrektur und Nachprüfung:** In einer neuen Änderungsnotiz den Umfang als „numerische Eingaben unverändert; JSON-/Markdown-Formatierung und redaktionelle Provenienzergänzung im Bericht“ benennen. Originale v1/v2-Artefakte bewahren. Diff und geparste JSON-Gleichheit nachprüfen; kein neuer numerischer Lauf allein wegen dieser Dokumentkorrektur erforderlich.

**Vermutungsstatus:** Bestätigter Textvergleich; keine behauptete versteckte numerische oder methodische Änderung.

## API-, Design- und Reproduktionsgrenzen

NACOV erwartet N mal die asymptotische Kovarianz der Stichprobenmomente und ihre dokumentierte Reihenfolge. Der externe Punktfit braucht dieselben Momente und dieselbe DWLS-Gewichtsmatrix. Die [offizielle kategoriale Hilfe](https://lavaan.ugent.be/tutorial/cat.html) und [Schätzerhilfe](https://lavaan.ugent.be/tutorial/est.html) stützen die Trennung von DWLS-Punkten und robuster SE-/Testkorrektur. Die Importparität begründet keine Eignung eines gelieferten Gamma für ein bestimmtes Design.

Eine eigene Negativkontrolle kehrt die numerischen NACOV-Positionen um und versieht sie trotzdem mit den korrekten alten Labels. Der Import übernimmt auch diese bewusst falsche Matrix mit Differenz 0; die Parameterkovarianz weicht dann um 0,14423 ab. Namen retten einen numerisch falsch zugeordneten Input hier nicht. Der Aufrufer muss Reihenfolge und Zielgröße garantieren. In der aktuellen Vier-Item-Konfiguration ist die numerische Reihenfolge durch die vollständige Parität bestätigt. Bei anderer Daten-/Modellreihenfolge ist insbesondere die dokumentierte Umschaltung von `ov_order` auf „data“ bei gelieferten Matrizen zu beachten, `lavaan.Rd:105–111`.

Die Aggregationsfunktion verlangt global eindeutige Clusterlabels mit einer Schichtzuordnung. Lokal wiederverwendete PSU-Nummern müssten vorab mit der Schicht verschlüsselt werden; automatische Behandlung ist hier nicht geprüft. Singleton-Abweisung erfindet zutreffend keine Lonely-PSU-Regel. Sie ist zugleich keine Lösung für kleine Domänen, Certainty-PSUs oder ausfallende PSUs. Aus der Zentrierung folgt Rang höchstens `Summe_h(G_h−1) = G−H`; im Autorfall 92, im Eigenfall 36. Positive Eigenwerte in diesen Fällen sagen nichts über 22-Moment-Designs mit weniger unabhängigen PSU-Beiträgen. Es wurde keine Coverage-Simulation, kein Bias-/Intervallabdeckungstest und keine small-df-Referenzverteilungsprüfung durchgeführt.

Das antwortsortierte alternative Autor-Schichtdesign ist ein ausdrücklich adversariales, erfundenes Beispiel. Eine reale Designzuordnung darf nicht anhand von Antwortmitteln rekonstruiert werden. Mein zweites Schichtdesign ist antwortunabhängig fest zugeordnet und prüft denselben Rechenmechanismus. Weder eines dieser Beispiele noch geänderte Standardfehler beweist die richtige deutsche Designzuordnung.

Die gepinnte originale [survey-Hilfe svyCprod](https://search.r-project.org/CRAN/refmans/survey/html/svyCprod.html), angezeigte Version 4.4-2, Details, beschreibt Schichtzentrierung und Korrekturen. [svyrecvar](https://search.r-project.org/CRAN/refmans/survey/html/svyrecvar.html), Details/Note, benennt weitere Voraussetzungen für multistufige Designs und PPS/FPC. Diese Originalhilfe wurde im Autorenverlauf laut Capture erst nach dem ersten Lauf gelesen. Sie ist nachträgliche begrenzte Quellenstützung, keine rückwirkende Präregistrierung und kein ausgeführter Vergleich mit survey 4.4-2. Ich habe die gepinnten Dokumente und ihre Originalseiten selbst gelesen; keine neue Behauptung eines survey-Paketlaufs.

PPS, FPC, Kalibrierung/Gewichtsunsicherheit, deutsche Mischung geclusterter und ungeclusterter Gemeinden, Missing-/Filtermuster, kleine Domänen, Invarianz, Reliabilität beobachteter Scores, persönliche Intervalle und Webübertragung bleiben ungeprüft. Auch die vorhandenen Fit-Teststatistiken sind Ausgaben der Software und keine empirisch bestandene Modellgüte oder Validität. Meine Prüfung schließt keines der offenen P04/P07/P09/P13-Gates des Analyseplans.

Das eingefrorene Paket bindet zahlreiche lokale `outputs/`-Inputs, den vorhandenen Prefix und interne versionsgebundene Funktionen. Hashes allein liefern fehlende lokale Dateien in einem frischen Checkout nicht. Ich habe weder Installation noch Conda oder eine komplette ursprüngliche Umgebungserzeugung ausgeführt. Sieben tragende installierte Helperkörper stimmen mit den Originalquellen; nicht jede installierte Abhängigkeit wurde vollständig neu aufgebaut oder auditiert. Gesamt-Reproduzierbarkeit bleibt außerhalb der beobachteten lokalen Rechenpfade offen. Die aktuelle Probe ist keine stabile öffentliche Analyse-API und kein endgültiger ESS-Analysevertrag.

## Tatsächliche Werkzeuge, Kommandos und Schreibgrenzen

Modellbezeichnung aus dem tatsächlichen Startauftrag: gpt-6.1-sol, ultra geerbt. Interne Revision, Anbieteranweisungen und exakte interne Modellvorgaben unbekannt. Verfügbare Werkzeuge im Kontext umfassen functions-Orchestrierung mit Shell, Dateibearbeitung, Web/Quellen, Ressourcen/Ziel-/Bildwerkzeugen, Clock, Collaboration und Browser-UI. Nicht sämtliche verzögert ladbaren Fähigkeiten wurden inventarisiert. Tatsächlich genutzt: `functions.exec`, `exec_command`, `apply_patch`, `web__run`, `collaboration.send_message`. Keine Toolnutzung für zusätzliche Agents, UI, Commit, Push, pnpm oder Installation. Der stets anwendbare Skill „unslop“ wurde aus `/home/stevenh/projects/12axes-germany/.agents/skills/unslop/SKILL.md` gelesen und auf meinen Bericht angewandt. Die kurze MEMORY.md-Suche ergab keine passende Erinnerung; keine Erinnerungsfakten übernommen.

Arbeitsverzeichnis für die Shell war ausschließlich `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Wesentliche tatsächlich ausgeführte Kommandos:

```text
python3 outputs/loop/methods002-statistics/check-bindings.py before-review   # Exit 0
python3 outputs/loop/methods002-statistics/run-r-statistics.py statistics-001       # Exit 1
python3 outputs/loop/methods002-statistics/run-r-statistics-002.py statistics-002   # Exit 1
python3 outputs/loop/methods002-statistics/run-r-statistics-003.py statistics-003   # Exit 1
python3 outputs/loop/methods002-statistics/run-r-statistics-004.py statistics-004   # Exit 0
python3 outputs/loop/methods002-statistics/check-bindings.py after-review    # Exit 0
```

Die jeweiligen `statistics-00x-command.json` enthalten den vollständigen tatsächlichen Child-Argv, cwd, Start-/Endzeit, Scope, Umgebungsvariablen, Exit und Skript-/Launcherhashes. `execution-ledger.json` bündelt sie ohne Antwortdaten. Die eigene Launcheranpassung änderte gegenüber dem gelesenen Original nur Own-Pfad und feste Dateilabels; Rechte und Runtimebindung bleiben gleich. Vor jedem numerischen Lauf existierte ein eigener Vorabplan beziehungsweise eine begründete Diagnoseergänzung mit Hash. Erste Fassungen, Kommandos, Logs und Ergebnisse bleiben unverändert.

Der Child-Aufruf startet direkt vorhandenes Rscript mit `--vanilla`, HOME `/home/stevenh`, NNP und Landlock. Behandelte Rechte: `write-file,remove-dir,remove-file,make-char,make-dir,make-reg,make-sock,make-fifo,make-block,make-sym,refer,truncate`. Erlaubt sind diese Rechte ausschließlich im eigenen `outputs/loop/methods002-statistics/`; zusätzlich `write-file` auf `/dev/null`. Eigene Skripte schreiben nur dort, der Python-Supervisor ebenfalls. R-Bibliotheken/Prefix wurden nicht geändert. Es gab keinen Installer/Conda, keine globale Konfiguration, keine Systemwrite- oder zusätzlichen Geräteaktionen.

Unbehandelte Read-/Execute-Zugriffe, Netzwerk, Geräte/IOCTL und geerbte Deskriptoren sind dadurch nicht vollständig kontrolliert. Der Python-Supervisor steht außerhalb der Child-Landlock-Regel; seine Pfadbindung wurde am Code geprüft, nicht durch eine vollständige PC-Sandbox erzwungen. Ich habe keine Nutzerdateiinhalte, ESS/raw/local, A/B-Antworten oder Partei-/Links-rechts-Werte gelesen. Keine Vollständigkeitsbehauptung für Syscall- oder PC-Überwachung.

Hilfslektüre nutzte `rg` und Python mit expliziten Pfaden; das öffentliche lavaan-Tarball wurde in Python gelesen, zwei tragende Originaldateien ausschließlich in den eigenen Outputs gespeichert. Zwei eigene Lesehelfer endeten mit Exit 1, ohne Mutation: ein nummerierter Druck versuchte nach dem tatsächlichen Dateiende von `lav_muthen1984.R` weiterzulesen; ein JSON-Druck nahm ein durch R-NULL entfallenes optionales `error`-Feld an. Die korrigierten Leseaufrufe wurden durchgeführt. Einige anfängliche kombinierte Toolausgaben waren abgeschnitten; relevante Dokumente und Quellenbereiche wurden danach einzeln gelesen. Diese Helferfehler sind keine Autorenfehler und kein numerischer Laufbefund.

Live öffentlich abgefragt wurden ausschließlich die genannten vier Originalseiten, alle zugänglich. `source-ledger.json` nennt Zugriff, Fundstelle, Dokumentversion und Grenzen. Die zur früheren Autorenlektüre gemeldeten unzugänglichen R-Forge-Seiten wurden von mir nicht als gelesen oder geprüft verbucht.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger methodischer Reviewer der synthetischen Schnittstellenprobe METHODS-002, kein Autor. Shell-CWD /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Aktuelles eingefrorenes Paket reports/loop/packages/METHODS-002/v2/manifest.json SHA b736855447a96dcaa3f55926edf59d7eda29c19dfe90d2e752de18df8b0d78e4,8Dateien/95SourceInputs; v1 nur für nachgewiesenen Formattransfer erlaubt. AGENTS/Auftrag/Issue/Vorabplan/Autorenbericht/Code/Aggregate und tragende originale lavaan-R/Hilfequellen selbstlesen. Keine anderen aktuellen Peer-/Jurorberichte/Loopfindings/Agentlisten/SOFTWARE-Reviewerbewertungen oder zusätzliche Verteidigung. Selbst mathematische Kette SC/Binverse/H, Momentreihenfolge/N-Skalierung, unzentrierterNativepfad vsSchichtzentrierung/G_hKorrektur, externeNACOV/WLSVImport, gewichtete16Schwellenorakel, globaleGewichtsskalierung/Umbenennung/singleton/crossStratum/alternativePartition kritisch prüfen. Eigene Gegenrechnungen an anders erfundenen Zahlen mindestens, nachBedarfsicherer eigenerR-Lauf durch geprüfteKopieLauncheroutputs/loop/methods002/run-r-trial.py mitnurOwnPfad/Festlabelnangepasst;Originalnieausführen/überschreiben, keineConda/Install/SystemWrites/Geräte/UserFile/ESS/raw/local/A/Bantworten/ParteiLRwerte. R --vanilla vorhandenPrefixREADONLY/NNP/benannteDateirechte ownOutputs+devnull,HOMEunverändert, Read/Netz/IOCTL/SupervisorGrenzenoffen. EigeneOutputs nur outputs/loop/methods002-statistics/ und reports/loop/reviews/METHODS-002-statistics.md. Alle8+95Bindungenvor/nachmitSperrpfadprüfung; public/syntheticnur. 16AutorenChecksundfitwarnungen sindSoftwareevidenzkeine empirischeValidität/Designcoverage. DokumentationvonSurvey4.4-2 nacherstemLaufgelesennichtpräregistriert;keinePPS/FPC/MixedDesign/kleineDomänen/Missing/Invarianz/persönlicheIntervalleFreigabe. Gesamtreproduzierbarkeits/ApiGrenzendokumentieren. JederFindingID M2-Sxx genaueAussage/Problem/Originalfundstelle/Wirkung/begründeteSchwere/KorrekturNachprüfung/Vermutungsstatus,keineFindingquote. Vollständiger tatsächlicher Startauftragwortgetreu;Modelgpt-6.1-sol ultra geerbt internunknown;verfügbare/genutzteTools tatsächlicheKommandosExitScope/SharedFSGrenzen. KeineweiterenAgents/Peers/CommitPush/GesamtFormat/Pnpm. VollständigabschließenOriginalberichtbewahrenPfadSHAKurzbefund.
```
