# SOFTWARE-001 v1: unabhängige Reproduktion und Laufzeitgrenzen

Prüfer `/root/software001_review_repro`, 2026-10-03. KI-Audit durch einen echten Codex-Subagent, laut Runtime-/Startauftragsangabe GPT-6.1-Sol. Interne Modellrevision und interne Anbietervorgaben unbekannt. Kein Review durch eine andere Modellfamilie, kein akademisches Peer Review.

Die gebundenen numerischen Befunde lassen sich in der vorhandenen Laufzeit reproduzieren. Ein eigener Gegenfall und eine zusätzliche Python-Rechnung bestätigen die gewichtete marginale Schwelle und die unstratifizierte Cluster-Varianz. Die ursprüngliche Einrichtung bleibt `NICHT_BESTANDEN`. Eine zusätzliche Schutzbehauptung über IOCTL-Zugriffe ist zu weit gefasst. Wissenschaftliche ESS-Abnahmen werden nicht erteilt.

| Gegenstand | Urteil | Geltungsbereich |
| --- | --- | --- |
| Bindung der acht eingefrorenen Dateien und 79 SourceInputs | BESTANDEN | Alle SHA256 vor den eigenen Modellläufen und nach den Läufen passend und unverändert |
| Bindung der vorhandenen R-/Paketlaufzeit | BESTANDEN | Rscript-Hash, 96 Paketmetadatensätze, expliziter Lock, 60 Dateien der zwei installierten Paketbäume und fünf geladene Funktionskörper |
| Eigene enge Laufzeitprobe | BESTANDEN | Benannte Dateischreibrechte, tatsächliche Pfade, ignorierte Profile/Renviron-Sentinels, NoNewPrivs und verweigerte nichttrunkierende Schreiböffnung |
| Reproduktion des benannten Autoren-Smokes | BESTANDEN | Exakte Gleichheit der sechs numerischen Projektionen und des synthetischen CSV-Hashes |
| Eigene marginale Schwellen-/Varianzrechnung und Stratumgegenfall | BESTANDEN | Ein erfundenes Design, eine marginale Schwelle; keine vollständige SEM-Kovarianz- oder Abdeckungsprüfung |
| Ursprüngliche vollständig projektlokale Einrichtung | NICHT_BESTANDEN | Bereits dokumentierter tatsächlicher Außenwrite; spätere Positivprüfungen ändern dieses Urteil nicht |
| Behauptete IOCTL-Sperre des Autorenlaunchers | NICHT_BESTANDEN | `ioctl-dev` ist nicht Teil der behandelten Rechte |
| Tatsächlich gefittete Invarianzkette, Reliabilitätsvalidierung und ESS-Abnahme | NICHT_GEPRÜFT | Syntaxerzeugung und API-Ausgabe sind dafür keine Nachweise |
| Eigener vollständiger Repositorycheck `pnpm check` | NICHT_GEPRÜFT | Nach Einsammlung der Erstberichte beim Koordinator auszuführen; hier nur eigener Bericht und eigene Outputs erlaubt |

## Prüfgrundlage und Trennung

Autoritative Grundlage ist [manifest.json](../packages/SOFTWARE-001/v1/manifest.json), SHA256 `126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e`, Version 1, Freeze `2026-10-03T03:51:51.559390+00:00`, Codecommit `0beba4738d8c0059c2b2709ae34bc9f6390a3fc8`. Kriterien stehen in [SOFTWARE-001-pruefauftrag.md](../packages/SOFTWARE-001/v1/files/reports/loop/SOFTWARE-001-pruefauftrag.md), SHA256 `76fe53161539f80a49d7a7801484f21cb67d1575f1750248b363cf2e29971ee6`. Die eingefrorenen AGENTS, der vollständige Dauerauftrag und LIFE-93 wurden gelesen. Die ältere Einschränkung auf Quellenrecherche ersetzt diesen späteren begrenzten Softwareauftrag nicht.

Ich habe keine anderen Reviewerberichte, Loopfindings, Agentregister oder zusätzliche Autorenverteidigung gelesen. Der im Paket enthaltene ursprüngliche Autorenbericht wurde als zu prüfende Behauptung gelesen. Keine ESS-Roh-/Zwischendaten, A/B-Hälften, Partei-/Links-rechts-Variablen oder realen Personenkennungen wurden gelesen. Keine Portal-, Cookie- oder Credentialabfragen. Keine weiteren Agents, Commits, Pushes, Conda-Aufrufe, Paketinstallationen, Umgebungsneuaufbauten, Außenlöschungen oder globalen Änderungen.

Die Zugriffstrennung beruhte auf diesem Auftrag, getrennten eigenen Dateien und den benannten Prozessregeln. Die Shell konnte prinzipiell weitere lesbare Dateien erreichen. Es gab keine technisch vollständige Lesesperre auf fremde Reviewdateien. Die tatsächliche Unabhängigkeit ist deshalb eine dokumentierte Arbeitsgrenze, keine behauptete Isolation aller verfügbaren Werkzeuge.

[Vorher](../../../outputs/loop/software-review-repro/input-before.json) und [nachher](../../../outputs/loop/software-review-repro/input-after.json) enthalten jeden der 87 Pfade, Soll-/Ist-SHA256 und Vergleich. Der vollständige Vorher-Snapshot entstand nach den ersten rein lesenden Orientierungszugriffen und vor eigenen R-Läufen; er ist kein rückwirkendes Zugriffsmonitoring. Alle 87 Dateien blieben danach unverändert. Die großen Installerarchive wurden nur gelesen und gehasht, nicht ausgeführt.

## Originalquellen und tatsächlich geladener Code

Die CRAN-Archive lavaan 0.7-2, SHA256 `5e6497544beca09739a91da4f82e830d6baab367c51e002bbf62c58c3bd866e7`, und semTools 0.5-9, SHA256 `8de79f0b2c4ff07e11254d60d6a3918b36beb5b5323e64be8f0bfe6d18f1ade5`, wurden selbst gelesen. R-/Rd-Dateien wurden ausschließlich nach `outputs/loop/software-review-repro/package-source/` extrahiert. Kein Aufbau und keine Installation. Die ursprünglichen URLs, Autorenzugriffszeiten und Hashes stehen im gebundenen [Quellenregister](../packages/SOFTWARE-001/v1/files/data/software-001-sources.json). Ich habe die archivierten Originalbytes geprüft, nicht die Erreichbarkeit aller URLs neu abgefragt.

Tragende Fundstellen:

- CRAN `lavaan/R/lav_muthen1984.R:218–249` bildet das Designgewicht-Sandwich mit quadratischen Gewichten und aggregiert die Scores pro Cluster. Das Cluster-Meat ersetzt die Punktschätzungs-Gewichtsmatrix nicht.
- CRAN `lavaan/R/lav_samplestats.R:1215–1232` übernimmt die Cluster-Gamma und multipliziert mit `G/(G-1)`. Hier steht keine innerhalb-Stratum-zentrierte Summe.
- CRAN `lavaan/R/lav_lavaan_step02_options.R:199–214` erlaubt den geprüften kategorialen Singlelevel-Clusterweg. Die Rd-Dokumentation `lavaan/man/lavaan.Rd:59–61` behauptet weiterhin „Currently only available for non-clustered data“. Dieses widersprechende Dokumentationsstück wurde nicht übergangen; die aktuelle Implementierung und die selbst ausgeführten Fälle tragen die engere Fähigkeitsaussage.
- CRAN `lavaan/R/lav_object_inspect.R:1403–1425` liefert bei `nlevels==1` den öffentlichen Cluster-Fallback 1. Mein neuer Gegenfall reproduziert öffentlich 1, intern 16. Im Autorenfall sind es öffentlich 1, intern und im Input 96. Die öffentliche Ausgabe wird nicht korrigiert oder als wirksame Clusterzahl interpretiert.
- CRAN `semTools/man/compRelSEM.Rd:18–26,49–59,284–313` beschreibt Kompositgewichte und die ordinale beobachtete Antwortskala. Diese Paketdokumentation ersetzt keine eigenständige Originalformelprüfung oder Reliabilitätsvalidierung.
- CRAN `semTools/man/measEq.syntax.Rd:7–11,134–142` trennt Syntaxerzeugung und `return.fit`. Der ausgeführte Autorenaufruf fordert keine gefittete Invarianzkette an.
- Gepinnter Conda-Code 26.5.2 `conda/core/path_actions.py:1132–1153` und `conda/core/envs_manager.py:45–48` erklärt den unbedingten `touch` vor dem Registrierungs-Guard. Er wurde gelesen, nicht ausgeführt.
- Gebundene Linux-Kerneldokumentation `linux-landlock.html:1029–1037,1363–1377` und lokale setpriv-Manpage `setpriv-2.42.4-local-manual.txt:136–164` tragen die hier berichtete Grenze der behandelten Zugriffsrechte.

Die tatsächlichen Namespace-Funktionskörper und Formalparameter für `muthen1984`, `lav_samp_from_data`, `lav_inspect_cl_info`, `compRelSEM` und `measEq.syntax` sind jeweils mit dem selbst aus dem CRAN-Archiv geparsten Original identisch. Der Befund steht in [independent-result.json](../../../outputs/loop/software-review-repro/independent-result.json), `source_bindings`. Das ist stärker als ein Versionsstring, aber keine vollständige Prüfung aller geladenen Abhängigkeiten und Systembibliotheken.

[Runtimebindung vorher](../../../outputs/loop/software-review-repro/runtime-binding-before.json) und [nachher](../../../outputs/loop/software-review-repro/runtime-binding-after.json) bestätigen 60/60 Dateien der installierten lavaan-/semTools-Bäume, 96/96 Conda-Metadatensätze und den expliziten Lock. Eine Lock-Metadatengleichheit beweist keinen von mir ausgeführten sauberen Neuaufbau. Der wird hier ausdrücklich nicht behauptet.

## Eigene Ausführung und Reproduktion

Alle Shellaufrufe nutzten explizit `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003` als cwd. Der neue [Launcher](../../../outputs/loop/software-review-repro/run-r-review.py) liest den ursprünglichen `run-r-direct.py` und `scoped-env.json` vor jedem R-Aufruf erneut und prüft ihre Manifesthashes. Er ruft ausschließlich das vorhandene `outputs/loop/software-env/envs/r-smoke/bin/Rscript --vanilla` auf. SHA256 `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`.

Die Landlock-Schreibregel umfasst ausschließlich `outputs/loop/software-review-repro/`. Tmp, Cache, Data, Config, Historienpfad und Probe-Sentinels liegen dort. Die bestehenden Paketbibliotheken bleiben Lesepfade. `/dev/null` erhält als Kernel-Senke nur die benannte `write-file`-Regel. HOME blieb `/home/stevenh`. Der vorhandene Autorenlauncher mit seinen weiter gefassten Schreibpfaden wurde nicht gestartet.

Die [Probe](../../../outputs/loop/software-review-repro/probe-result.json) zeigt R 4.5.3, beide `.libPaths()` im vorhandenen Projektpräfix, eigenen Tmp-Pfad, `NoNewPrivs=1`, `CapEff=0` und ignorierte eigene Profile-/Renviron-Sentinels. `R_PROFILE_USER` und `R_ENVIRON_USER` sind innerhalb des `--vanilla`-Prozesses leer. Die nichttrunkierende `r+`-Öffnung des eingefrorenen Manifests wird mit `Permission denied` verweigert. Es wurde kein Inhalt geschrieben. Ich habe keine Benutzerdatei dafür geöffnet.

Die eingeschränkten R-Prozesse, ihr Startaufruf und eine ausgewählte Verweigerungsprobe belegen die angegebenen Dateirechte. Das Python-Supervisorprogramm selbst läuft außerhalb seiner Kindprozess-Landlock-Regel. Sein gelesener Code schreibt nur eigene Logs und eigene vorbereitende Pfade. Keine vollständige Syscall- oder Dateisystembeobachtung, keine Geräte-/Netzwerk-/IOCTL-Sperre und keine Vollständigkeitsbehauptung über den PC.

Der [Vorabplan](../../../outputs/loop/software-review-repro/plan-before-run.md), SHA256 `443b2e6212c923c3dd56eb2851d2e0320478811ec2c51d1669ad80fccbf3d08b`, entstand vor diesen Läufen.

| Aufruf | Start bis Ende UTC | Exit | Ergebnis |
| --- | --- | --- | --- |
| `python3 outputs/loop/software-review-repro/run-r-review.py runtime-probe <own>/probe.R <project>` | 04:10:38.279560 bis 04:10:38.393626 | 0 | Eigene Pfad-/Profil-/Schreiböffnungskontrolle bestanden |
| `python3 outputs/loop/software-review-repro/run-r-review.py replication <own>/replication.R <project> <own>/replication-result.json` | 04:11:02.629358 bis 04:11:04.246170 | 0 | Alle 17 benannten Autorenfälle und numerischen Projektionen reproduziert |
| `python3 outputs/loop/software-review-repro/run-r-review.py independent <own>/independent.R <project>` | 04:12:39.128958 bis 04:12:39.995035 | 1 | Eigene falsche CRAN-Funktions-/Dateinamen im Bindungscheck; kein fertiger Gegenfallreport |
| `python3 outputs/loop/software-review-repro/run-r-review.py independent-corrected <own>/independent.R <project>` | 04:13:17.622301 bis 04:13:18.537918 | 0 | Korrigierter Bindungscheck und marginaler Gegenfall bestanden; Rangwarnungen erhalten |
| `python3 outputs/loop/software-review-repro/run-primitive.py` | 04:14:23.925210 bis 04:14:23.989050 | 0 | Zweite primitive Rechnung mit Python-Standardbibliothek bestanden |

`<project>` ist der oben genannte absolute Worktreepfad; `<own>` ist dessen `outputs/loop/software-review-repro`. Jeder vollständige tatsächliche Argumentvektor einschließlich setpriv-Rechten, cwd, Zeit und Exitcode steht in den jeweiligen `*-command.json`; stdout/stderr in den gleichnamigen `.log`. Die erste fehlgeschlagene eigene Fassung und ihr Befehl/Log bleiben als `independent-first-attempt.*` erhalten. [own-repair.json](../../../outputs/loop/software-review-repro/own-repair.json) hält den Fehler und die Korrektur fest. Weder der Datengenerator noch die primitive Rechnung wurden wegen ihrer Zahlen geändert.

[replication-adaptation.json](../../../outputs/loop/software-review-repro/replication-adaptation.json) dokumentiert exakt eine Änderung an der eingefrorenen Skriptkopie: den festen Outputpfad. Der ausführbare abgeleitete Hash ist `84ac28925879fd41797e60673db9fb91598399152b862fecadc348ead7dfd28c`. Der kopierte JSON-Bericht behält ursprüngliche Autorenlabels und Quellpfadlabels; er wird deshalb nur als numerisches Vergleichsartefakt genutzt. Seine Laufzeitangaben und der geänderte Outputpfad verhindern eine behauptete Rohbyte-Gleichheit der gesamten Reportdatei.

[replication-comparison.json](../../../outputs/loop/software-review-repro/replication-comparison.json) belegt dagegen exakte Gleichheit der vollständigen Abschnitte `input`, `cases`, `contrasts`, `firstThresholdOracle`, `optionalSemTools` und `technicalChecks`. Die synthetische CSV ist byteidentisch, SHA256 `2360c7663743bb2078601d86068b478f654c8c298866f0cb1b23bb86bc1863f7`. Die originalen und eigenen erwarteten negativen API-Fälle wurden tatsächlich ausgeführt; ein zurückgewiesenes Argument ist kein fehlender Lauf.

## Unabhängige Zahlen und Gegenfall

Die zusätzliche [Python-Rechnung](../../../outputs/loop/software-review-repro/primitive.py) nutzt `statistics.NormalDist.inv_cdf`, `math.fsum` und eigene explizite Cluster-/Stratumsummen. Sie importiert weder lavaan noch Autorenfunktionen. Sie rechnet einmal am selbst reproduzierten Autoreninput und einmal am neuen eigenen Input. Alle Werte stammen aus [primitive-result.json](../../../outputs/loop/software-review-repro/primitive-result.json).

Für die erste Schwelle wird `p = sum(w*I(y<=1))/sum(w)` und `t = Phi^-1(p)` berechnet. Die linearisierte Einflussgröße ist `u_i = w_i*(I_i-p)/(sum(w)*phi(t))`. Für Cluster werden diese Größen zu `U_c` summiert. Unstratifiziert folgt `G/(G-1)*sum((U_c-mean(U))^2)`. Im Stratumfall werden die Clustersummen innerhalb jedes Stratum zentriert und mit dem jeweiligen `G_h/(G_h-1)` multipliziert. Diese Rechnung prüft eine marginale Schwelle; sie setzt keine Gültigkeit des vollständigen Faktorenmodells voraus.

| Marginaler Befund | Reproduzierter Autoreninput | Neuer eigener Input |
| --- | --- | --- |
| Fälle / Cluster / Strata | 1440 / 96 / 4 | 640 / 16 / 4 |
| Gewichtete Wahrscheinlichkeit | 0.09609964324075411 | 0.18504672897196262 |
| Schwelle | -1.3041005937873873 | -0.8962983166223311 |
| IID-Varianz | 0.0022435866507772607 | 0.005575603046505007 |
| Unstratifizierte Cluster-Varianz | 0.003053330047255381 | 0.017193783364767862 |
| Stratifizierte Cluster-Varianz | 0.0030739747854909615 | 0.003684210444489242 |
| Unstratifiziert / stratifiziert | 0.9932840248615497 | 4.666884159803067 |

Die Python-Schwelle liegt im Autorenfall nur `2.665e-15` von der R-Rechnung entfernt. Die unstratifizierte Cluster-Varianz liegt nur `8.674e-19` von der gespeicherten lavaan-Gamma/n entfernt. Das reproduziert die tatsächlich berichtete Aussage, ohne sich allein auf einen Autorenvergleichshash zu stützen.

Der neue eigene Seed ist `730164`, mit 16 unabhängigen erfundenen Clustern und je 40 Fällen. Die latente Lage unterscheidet sich bewusst nach vier Strata. Gewichte sind bewusst antwortabhängig: 3 bei `z1<=2`, sonst 1. Das ist ein Gegenfall, keine Nachbildung eines ESS-Designs. Eigener CSV-Hash `60b7068b76bfa1402abd9997b1ec2bfff7306d44b667b27771014d6d5d938af0`.

Die native Gamma/n beträgt im eigenen gewichteten Clusterfall `0.0171937833647679` und stimmt mit der selbst berechneten unstratifizierten Varianz bis `5.899e-17` überein. Sie bildet die deutlich kleinere innerhalb-Stratum-zentrierte Varianz nicht ab. Das Ändern der bloßen Stratumspalte verändert Koeffizienten, Gamma und vcov exakt um null. Alle drei native Argumente `strata`, `stratum`, `stratification` liefern selbst geprüft `unknown argument`.

Gewichtete gegenüber ungewichteten Koeffizienten unterscheiden sich im eigenen Fall um maximal `0.95807450767131663`. Das Hinzufügen des Clusterarguments verändert die Punktschätzung um null, Gamma um maximal `31.647813646643563` und vcov um maximal `0.21949041275216036`. Permutierte Cluster verändern Gamma, lassen die Punktschätzung gleich. Globale Gewichtsskalierung um neun verändert bei expliziter Normalisierung keinen dieser verglichenen Werte. Die Befunde passen zum gelesenen Implementierungsweg.

Der eigene 16-Cluster-Gegenfall erzeugt vcov-Warnungen mit kleinsten Eigenwerten etwa `-1.30e-15` beziehungsweise `-4.66e-17`. Mit nur 16 Clustern kann das zentrierte Cluster-Meat höchstens Rang 15 haben, während es 22 Sample-Statistiken und 20 freie Parameter gibt. Konvergenz und `post.check=TRUE` sind deshalb hier keine vollständige PSD-/SEM- oder Inferenzabnahme. Die Warnungen stehen in beiden eigenen Logs. Die marginale Schwellenvarianz bleibt separat nachrechenbar. Eine größere Clusterzahl und vollständige Matrix-/Testprüfung wäre neue Arbeit, kein hier ausgeführter bestandener Check.

## Findings

### SOFTWARE-001-REPRO-01: ursprüngliche Einrichtungsgrenze tatsächlich verletzt

Aussage: Die ursprüngliche Einrichtung sollte vollständig projektlokal bleiben. Tatsächlich entstand die neue leere `~/.conda/environments.txt`; der dokumentierte Birth-Zeitpunkt des Elternordners liegt ebenfalls im Create-Intervall.

Beleg: Gebundene `user-file-baseline.json` meldet die Datei vorher fehlend; `user-file-after-create.json` meldet sie geändert. `outside-write-incident.json` nennt Datei, Größe null und die Metadatengrenze des ursprünglichen Snapshots. `conda-create-command.json` meldet Exit 0 und das Intervall `03:26:56.744281–03:27:10.484014 UTC`. Die dokumentierte Birth-Zeit `03:27:09.605112471 UTC` liegt darin. Gepinnter `conda/core/path_actions.py:1139–1144` berührt die Datei vor dem `register_envs`-Guard in `envs_manager.py:45–48`. `conda-context.log` bestätigt `register_envs=false`, enthält aber zugleich einen Benutzerpfad in `envs_dirs`.

Problem und Folge: Ein explizites Präfix und Registrierungs-Flags reichen nicht als Schutz gegen jeden Außenwrite. Dieser reale Verstoß entwertet die ursprüngliche Einrichtungsabnahme. Die Nachweise umfassen benannte Pfade und Quellen, keinen vollständigen Syscall-Audit. Der ursprüngliche Snapshot erfasste die Datei, nicht die Existenz des Elternordners; dessen Neubildung wird mit Zeitmetadaten gestützt, nicht als unmittelbare Vorher-/Nachherbeobachtung ausgegeben.

Schwere: hoch für die verbindliche Schutzanforderung an den PC. Dokumentiert sind eine leere Datei und ein Elternordner; ein größerer Schaden wird nicht behauptet. Das Finding ist im Paket bereits zutreffend als `NICHT_BESTANDEN` ausgewiesen, nicht ein neu verschwiegener Autorenfehler.

Korrektur und Nachprüfung: Historische Fehlbewertung beibehalten, Originalartefakte erhalten, keinen Außen-Cleanup ausführen. Weitere Rechnungen nur über die enge direkt gestartete Laufzeit. Jede zukünftige Installation benötigt vor ihrer Ausführung eine getrennte, tatsächlich durchsetzbare und geprüfte Schreibgrenze; fehlt sie, bleibt der Aufbau blockiert. Meine engere Probe und Reproduktion bestehen für ihren eigenen Geltungsbereich und heilen diesen früheren Verstoß nicht.

### SOFTWARE-001-REPRO-02: IOCTL-Sperre überbehauptet

Aussage: `run-r-direct.py:48` beschreibt „no ioctl permission“, die erzeugte Metadatenzeile `:55` und die gebundenen finalen `*-command.json` behaupten „no ... ioctl access“.

Beleg: Die tatsächliche Liste der behandelten Dateirechte in `run-r-direct.py:38–39` und den Befehlen enthält kein `ioctl-dev`. Die gebundene Kerneldokumentation `linux-landlock.html:1029–1033` erklärt ausdrücklich, dass nicht aufgeführte Zugriffsrechte durch dieses Ruleset nicht verweigert werden. `:1363–1377` beschreibt `LANDLOCK_ACCESS_FS_IOCTL_DEV` gesondert und begrenzt es auf neu geöffnete Geräte-Dateideskriptoren. Die lokale setpriv-Manpage `:136–164` bestätigt die Auswahl behandelte Rechte/Allow-Regeln.

Problem und Folge: Eine `/dev/null:write-file`-Regel erteilt kein ausdrücklich aufgeführtes IOCTL-Recht; daraus folgt aber keine erzwungene IOCTL-Sperre. Die protokollierte Garantie geht über die konfigurierte Kontrolle hinaus. Benannte Dateischreibgrenzen und verweigerte Schreiböffnung bleiben separat belegt. Es gibt keinen Befund einer tatsächlich ausgeführten schädlichen Geräteoperation.

Schwere: mittel. Die unzutreffende Schutzbehauptung betrifft die verlässliche Beschreibung der Ausführungsgrenze. Die ausgeführten R-Skripte sind eng begrenzt und erzeugen überprüfbare eigene Outputs; numerische Befunde werden dadurch nicht widerlegt.

Korrektur: In einer neuen Korrekturfassung die Behauptung auf die tatsächlich behandelten Dateirechte begrenzen. Ungelistete Zugriffsarten, Lesen/Ausführen und geerbte Deskriptoren offen nennen. Die eingefrorenen Originalprotokolle unverändert lassen. Wenn eine ausdrückliche Gerätesperre benötigt wird, ist sie als neuer separater Kontrollschritt zu konfigurieren und zu prüfen; ich habe keine Geräte-IOCTLs ausgeführt.

Nachprüfung: Den neuen Launcher und seine erzeugte Beschreibung gegen den tatsächlichen Rechtevektor prüfen. Eine Aussage über IOCTL-Sperren benötigt `ioctl-dev`-Handling, eine passende Kernel-/setpriv-Unterstützung sowie eine begrenzte sichere Prüfung und die Deskriptorgrenzen. Mein eigener Launcher behauptet diese zusätzliche Sperre nicht. Keine globale Sicherheitsänderung ist erforderlich oder autorisiert.

## Grenzen und nächster Schritt

Der erfolgreiche CFA-Smoke belegt einen konkreten numerischen Softwareweg mit gewichteten ordinalen Daten und clusterrobusten Standardfehlern. Die native Stratumgrenze ist durch Originalcode, negative API-Aufrufe und den neuen Gegenfall belegt. Ein externes `nacov`-/`wls_v`-Interface ist keine bereits geprüfte Survey-Erweiterung.

Die reproduzierte `compRelSEM`-Ausgabe `0.776364645194645` belegt API-Kompatibilität und einen erzeugten Koeffizienten. Die reproduzierte THETA-/Wu.Estabrook-Syntax belegt Syntaxerzeugung. Keine Originalformel-/Designintervalle-/persönliche Unsicherheitsvalidierung und keine numerisch gefittete Invarianzfolge. EFA, Abdeckungsstudien, robuste Nestungsvergleiche und ESS-Modellentwicklung bleiben `NICHT_GEPRÜFT`; sie werden nicht als gescheiterte ausgeführte Tests bezeichnet.

Ein vollständiger Neuaufbau wurde nicht durchgeführt und war untersagt. Der Conda-Einrichtungsvorfall wurde anhand seiner gebundenen Belege und Originalquelle geprüft; ich habe ihn nicht wiederholt und die Außen-Datei nicht verändert. Ein Bericht über sämtliche Dateisystemänderungen wird nicht abgegeben.

Tatsächlich genutzte Agent-Werkzeuge waren `functions.exec` mit `exec_command` und `collaboration.send_message` an den Koordinator. Lokale Hilfsmittel waren Bash, `rg`, `sed`, `cat`, `nl`, `wc`, Python 3.14.7, setpriv/util-linux 2.42.4, R 4.5.3, lavaan 0.7-2, semTools 0.5-9, jsonlite, `sha256sum` und Prettier 3.8.1. Die Schreibregeln von `unslop` wurden gelesen und angewandt. Es gab keinen frischen Webdownload, Browserlauf oder zweiten Modellanbieter.

`pnpm check` wurde von mir nicht ausgeführt. Sein vollständiger Build würde gemeinsame Projektoutputs außerhalb meines freigegebenen Schreibbereichs erzeugen. Der Koordinator soll ihn nach Einsammlung der unveränderten Erstberichte ausführen. Zwei direkte Prettier-Aufrufe auf meiner Berichtsdatei (`--write`, danach `--check`) endeten mit Exit 0; `.prettierignore` schließt `reports/loop/reviews/` jedoch ausdrücklich aus. Die Datei wurde dabei nicht formatiert und erhielt keine eigenständige Formatabnahme. Dieser übersprungene Dateicheck gilt nicht als bestanden. Der gebundene erfolgreiche Autorencheck bleibt technische Fremdevidenz und wird hier nicht als eigener Repositorycheck ausgegeben. UI-Arbeit fand nicht statt; kein neuer UI-Browsercheck ist für diesen Bericht erforderlich.

Meine Artefakte liegen ausschließlich unter `outputs/loop/software-review-repro/`, dieser Erstbericht ausschließlich unter `reports/loop/reviews/SOFTWARE-001-repro.md`. Eine Hashliste der eigenen abgeschlossenen Artefakte liegt in `outputs/loop/software-review-repro/artifacts.json`. Die Entscheidung über das Gesamtpaket und die Bearbeitung der Findings erfolgen erst nach Einsammlung der unabhängigen Berichte.

## Vollständiger tatsächlicher Startauftrag

```text
Du bist zweiter unabhängiger SOFTWARE-001-Prüfer für Reproduktion, Laufzeitbindung, Schreibgrenzen und Evidenz. Worktree ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, explizite cwd. AGENTS, Auftrag/Issue aus eingefrorenem Paket lesen. Gleiches SOFTWARE-v1-Prüfmanifest reports/loop/packages/SOFTWARE-001/v1/manifest.json SHA256 126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e,8Dateien/79SourceInputs; Kriterien reports/loop/SOFTWARE-001-pruefauftrag.md. Keine fremden aktuellen/anderen Reviewerberichte, Loopfindings/Agentregister oder Autorverteidigung lesen. Prüfe originale gebundene Quellen, CRAN-Paket/Code, Locks, Cmdlogs, actualNumerics und Einstellungsgrenzen selbst. Führe eigene begrenzte Reproduktion und unabhängigen numerischen Gegenfall aus (keine bloße Zustimmung zum Autorenhash): eigene primitive Schwellen-/Varianzrechnung sowie Cluster/Gewicht/Stratum-Auswirkungen. Kein ESS/data/raw/local/A/B/Partei/LR/Personendaten, keine Portal-Analysis/Cookie-/Credentialabfragen. KEIN Conda, Neuaufbau, globale/user Writes, systemweite Einstellungen/Löschungen oder Rechteausweitung. Vor jeder Ausführung outputs/loop/software-author/run-r-direct.py und scoped-env.json lesen; eigens angepassten Launcher in outputs/loop/software-review-repro/ verwenden, vorhandenes direktes projektlokales Rscript --vanilla mit setpriv Landlock/no-new-privs und nur eigene Schreibpfade für Output/Tmp/Cache. Eingefrorene gemeinsame Artefakte/Autorenoutputs nicht überschreiben. HOME unverändert, Userprofile/Renviron/Rhistory deaktiviert. Falls Grenzen unkontrollierbar, betroffenen Lauf blockieren. Ungewollter ursprünglicher Conda-Außenwrite bleibt NICHT_BESTANDEN; spätere enge Positivprüfung darf ihn nicht heilen. Prüfe Herkunft und Logreichweite, kein vollständiges Dateisystemmonitoring behaupten. Nur eigener Bericht reports/loop/reviews/SOFTWARE-001-repro.md und ownOutputs. Vollständiger tatsächlicher Startauftrag wortgetreu; tatsächliche Werkzeuge/Modelle (GPT-6.1-Sol laut Runtime; interne Revision unbekannt), Input/Sources/BeforeAfterhashes, echte Kommandos/Exitcodes/Ergebnisse/Grenzen dokumentieren. Findings genaue Aussage, Fundstelle/Rechengegenfall, Problem/Folge/begründete Schwere/Korrektur/Nachprüfung; keine Zahl/Schlussfolgerung vorgeschrieben. Numerische CFA, Invarianzsyntax, compRelSEM-Ausgabe belegen unterschiedliche Dinge; keine wissenschaftliche Gesamtfreigabe/andereFamilie. Zukünftige Anforderungen keine gescheiterten ausgeführten Tests. Keine weiteren Agents/Commit/Push. Vollständig abschließen, Bericht+SHA+Kurzbefund.
```
