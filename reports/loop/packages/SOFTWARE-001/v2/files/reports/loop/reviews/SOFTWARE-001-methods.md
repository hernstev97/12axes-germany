# SOFTWARE-001: unabhängige Prüfung der Methoden- und Softwarebefunde

Erstbericht von `/root/software001_review_methods`, 2026-10-03. Laufzeitbezeichnung GPT-6.1-Sol; interne Revision unbekannt. KI-Audit, keine akademische oder empirische Freigabe.

Die enge Aussage trägt: lavaan 0.7-2 schätzt den benannten erfundenen ordinalen Einfaktor-CFA mit Designgewichten und clusterrobusten Standardfehlern. Meine neu erzeugten Antworten haben exakt den Autoren-Inputhash, ausgewählte Punktwerte und die erste marginale Schwelle stimmen überein. Die native Rechnung nutzt keine unangemeldete Stratumvariable. semTools 0.5-9 liefert die genannte Reliabilitätszahl und eine Syntaxklasse; eine gefittete Invarianzfolge oder geprüfte Reliabilitäts-/Unsicherheitskette folgt daraus nicht.

Ich fand keinen neuen erheblichen Fehler in diesen begrenzten Paketbehauptungen. Der bereits dokumentierte Einrichtungsfehler bleibt ein tatsächlicher negativer Befund. Er wird durch die folgenden Positivtests nicht geheilt.

| Bereich | Urteil und Reichweite |
| --- | --- |
| Frozen-Dateien, 79 SourceInputs und unveränderte Versionen | BESTANDEN für die dokumentierten Hashvergleiche |
| Eigene beschränkte direkte R-Ausführung | BESTANDEN für Launcher, drei verweigerte Schreiböffnungen, benannte Runtime-Pfade und Metadaten |
| Benannte synthetische numerische/API-Fälle und marginales Orakel | BESTANDEN im bezeichneten Fall |
| Originale vollständig projektlokale Einrichtung | NICHT_BESTANDEN |
| Vollständige ESS-Designfähigkeit, EFA, fitted Invarianzfolge, Reliabilitätsintervalle und persönliche Unsicherheit | NICHT_GEPRÜFT |
| Wissenschaftliche Phase-/Modell-/Releaseabnahme | NICHT_GEPRÜFT |

## Fassung, Auftrag und Trennung

Geprüft wurde ausschließlich [SOFTWARE-001/v1](../packages/SOFTWARE-001/v1/manifest.json), SHA256 `126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e`, Paket-Codecommit `0beba4738d8c0059c2b2709ae34bc9f6390a3fc8`. Die acht eingefrorenen Dateien sind die maßgebliche Fassung; alle 79 angegebenen lokalen SourceInputs sind separat gebunden. Meine Sammelkontrolle erfasste 95 Pfadprüfungen: acht Freeze-Dateien, dieselben acht Worktree-Dateien und 79 SourceInputs. Vor Modellläufen und nach den eigenen Zugriffs-/Rechenprüfungen stimmen sie jeweils mit dem Manifest überein. Die ersten lesenden Regel-/Launcher-Aufrufe lagen vor dem gespeicherten Sammelsnapshot; ich behaupte daher keinen vor dem allerersten Lesezugriff gespeicherten Vollsnapshot. Das zuerst gelesene Manifest hatte bereits den erwarteten Hash.

Ich las die eingefrorenen AGENTS, den Dauerauftrag, das vollständige ursprüngliche Issue, den Prüfauftrag, das Skript, den Quellenkatalog und den Autorenbericht. Zusätzlich las ich die vorgeschriebenen Projektregeltexte `docs/project.md`, `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md`, `docs/entscheidungen.md` und `docs/lizenzen.md`. Diese enthalten Verweise und Zusammenfassungen älterer, anderer Audits; ich öffnete keine fremden Reviewerberichte, Loopfindings oder Agentregister und keine zusätzliche Autorenverteidigung. Den Loopzustand las ich wegen der ausdrücklich begrenzten unabhängigen Erstprüfung nicht. Paketbelege einschließlich Plänen, Einrichtungsvorfall, Lock, Originalkommandos und relevanten Primärquellen waren zugänglich.

Die Dateisystemtrennung ist verhaltensgebunden. Andere Agents und der Koordinator können dasselbe SharedFS lesen. Es besteht keine Zugriffssperre auf ihre Berichte. Ich beschränkte meine eigene Lektüre auf die genannten Eingaben; mit dem Koordinator tauschte ich ausschließlich Fortschritt und eigene Befunde aus. Kein Bericht eines zweiten Prüfers floss in diesen Erstbericht ein. Der R-Kindprozess hat zusätzliche Schreibbeschränkungen, jedoch keine Lesesperre. Kein Claude oder anderer Modellfamilienlauf fand in meiner Prüfung statt. Ich startete keine weiteren Agents und führte keinen Commit, Push, Merge oder Deployment aus.

## Eigene Ausführung und Schreibgrenze

Vor den eigenen R-Läufen las ich den gebundenen `outputs/loop/software-author/run-r-direct.py` und `scoped-env.json`. Mein [eigener Launcher](../../../outputs/loop/software-review-methods/run-r-direct.py) ruft das vorhandene projektlokale Rscript direkt mit `--vanilla` über `/usr/bin/setpriv --no-new-privs` und die expliziten Landlock-Schreibrechte auf. Es gab keinen Conda-Aufruf und keinen Umgebungsneuaufbau.

Erlaubte gespeicherte Schreiborte des R-Kindprozesses liegen ausschließlich unter `outputs/loop/software-review-methods/`; `/dev/null` hat nur `write-file` als Kernel-Senke. Die verwendeten Bibliotheken bleiben lesend in `outputs/loop/software-env/`. Eigene Cache-, TMP-, XDG- und Historienpfade liegen im eigenen Reviewerordner. HOME blieb `/home/stevenh`. `--vanilla` deaktivierte Benutzerprofile und Renviron; die entsprechenden Umgebungsvariablen sind innerhalb R leer. Es wird keine Benutzerhistorie geladen oder gespeichert. In `/proc/self/status` beobachtete die Probe `NoNewPrivs: 1`.

Die Probe versuchte nur nichttrunkierendes `r+b`-Öffnen dreier vorhandener Dateien: der leeren `~/.conda/environments.txt`, des eingefrorenen Manifestes und des Autoren-Synthetikinputs. Alle Öffnungen wurden mit `Permission denied` verweigert. Sie las oder schrieb keine Inhalte und erstellte keine Testdatei außen. Die nachher beobachteten Größe/mtime/ctime/Modus der benannten `.conda`-Pfade sind unverändert. R_HOME, Bibliotheken und Tempverzeichnis liegen in den vorgesehenen Projektpfaden. Die 30 installierten lavaan-Dateien, 30 semTools-Dateien und das Rscript-Binary stimmen vor und nach den Läufen mit dem gebundenen Lock überein. Ein vollständiger Syscall- oder PC-Dateisystemaudit wurde nicht durchgeführt; die ursprüngliche Außenwrite-Einrichtung wurde nicht wiederholt oder bereinigt.

## Eigene Rechenprüfung

Mein [Vorabplan](../../../outputs/loop/software-review-methods/plan-before-run.md) wurde vor den eigenen R-Läufen gespeichert. Das eigene [R-Skript](../../../outputs/loop/software-review-methods/check-methods.R) erzeugt alle Antworten aus dem dokumentierten DGP neu. Es lädt keine ESS-, A-/B-, Partei-, Links-Rechts- oder Personendateien. Der synthetische CSV-Hash ist `2360c7663743bb2078601d86068b478f654c8c298866f0cb1b23bb86bc1863f7` und stimmt exakt mit dem Autoreninput überein. Seed, RNGkind, Paketversionen und komplette Laufzeitdaten stehen im [eigenen Rechenbericht](../../../outputs/loop/software-review-methods/methods-results.json).

Tatsächlich ausgeführt wurden neun positive CFA-Fälle und acht beabsichtigte native API-Fehler. Der gemeinsame gewichtete Clusterlauf konvergierte, bestand `post.check` und lieferte endliche Schätzwerte, SE, Gamma und vcov. Die Optionen sind DWLS als Punktschätzer, ursprüngliche Anforderung WLSMV, `theta`, `std_lv=TRUE`, Designgewichte mit Normalisierung `group`, `se=robust.cluster.sem`, Tests `standard/scaled.shifted/satorra.bentler`, singlelevel. Die scaled.shifted-Ausgabe beträgt 9.44663896021339 mit df=2 und p=0.008885633854242009. Das ist beobachtete Testausgabe, keine fachliche Fit-Abnahme.

Die verglichenen 20 freien Punktparameter unterscheiden sich von der eingefrorenen Ausgabe um maximal 0. Uniforme Gewichte und Gewichtsvervielfachung um sieben ergeben in den verglichenen Statistik-, Gamma- und vcov-Komponenten Differenz null. Das Clusterargument lässt die Punktwerte und marginalen Statistiken unverändert, verändert Gamma um maximal 2.34552814583278; Clusterpermutation verändert Gamma um maximal 2.44621491083745. Die native Clusterdiagnostik zeigt öffentlich 1 und intern 96 Cluster. Die Getterquelle erklärt den singlelevel-Fallback; daraus folgt kein Fehlen der tatsächlich benutzten Clusterkorrektur.

### Marginales Schwellenorakel

Die Zielgröße ist die beobachtete marginale Sample-Schwelle, nicht der geschätzte THETA-Parameter aus `parameterEstimates`. Für jedes Item und jeden Schnitt t berechne ich unabhängig

```text
p = sum(w * I(y<=t)) / sum(w)
z = qnorm(p)
u_i = w_i * (I(y_i<=t)-p) / (sum(w) * dnorm(z))
U_g = sum(u_i in cluster g)
Var_iid = sum(u_i^2)
Var_cluster = G/(G-1) * sum((U_g-mean(U))^2)
Var_stratified = sum_h G_h/(G_h-1) * sum_g_in_h((U_g-mean_h(U))^2)
```

| Erste marginale Schwelle / Varianz | Eigene Ausgabe |
| --- | --- |
| Gewichtete Wahrscheinlichkeit Pr(y1 ≤ 1) | 0.0960996432407541 |
| Marginale Schwelle qnorm(p) | -1.30410059378739 |
| iid-Delta-Varianz | 0.00224358665077726 |
| Unstratifizierte Cluster-Taylor-Varianz | 0.00305333004725538 |
| lavaan Gamma[1,1]/n | 0.00305333004725538 |
| Taylor mit ursprünglichen vier Strata | 0.00307397478549096 |
| Taylor mit nach Beitragsgröße geordneten Strata | 0.00053625632876818 |
| Unstratifizierte / geordnete stratifizierte Varianz | 5.69378836846384 |

Die maximale Schwellenabweichung über alle 16 marginalen Schwellen ist 2.77555756156289e-16. Der vollständige 16×16-Schwellenblock von Gamma/n weicht vom eigenen Cluster-Taylor-Orakel maximal um 6.07153216591882e-18 ab; der iid-Block maximal um 3.46944695195361e-18. Diese Formeln prüfen nur marginale Schwellen und ihren Kovarianzblock. Sie prüfen weder die polychorischen Korrelationen noch das gesamte SEM-Sandwich, Intervallabdeckung, PPS oder Kalibrierungsunsicherheit.

Der zusätzliche geordnete Stratumfall ordnet die 96 Cluster nach ihrer ersten Schwellenbeitragsgröße vier gleich großen Strata zu. Er ändert keine Antworten, Gewichte oder Cluster. Die native Gamma bleibt exakt gleich; der stratifizierte Ausdruck ändert sich deutlich. Das widerlegt eine Gleichsetzung dieser nativen Gamma mit einer beliebigen stratifizierten Taylor-Rechnung. Die Zuordnung ist bewusst künstlich und antwortabhängig, kein zulässiger ESS-Stratifizierungsplan und keine Schätzung eines realen Design-Effekts. Schon der ursprüngliche synthetische Stratumfall bestätigt die engere Autorenbehauptung einer messbaren Differenz.

### Tatsächliche API-Gegenfälle

| Fall | Beobachteter kontrollierter Fehler |
| --- | --- |
| `api_strata` | lavaan->lav_step02_options():      unknown argument: 'strata' |
| `api_stratum` | lavaan->lav_step02_options():      unknown argument: 'stratum' |
| `api_stratification` | lavaan->lav_step02_options():      unknown argument: 'stratification' |
| `api_negative_weight` | lavaan->lav_data_full():      some sampling weights are negative |
| `api_missing_weight` | lavaan->lav_data_full():      sampling.weights variable ‘w’ contains missing values |
| `api_single_cluster` | lavaan->lav_data_full():      Cluster variable ‘synthetic_cluster’ contains only 1 cluster(s); at least     two clusters are required to fit a model to clustered data. |
| `api_absent_weight` | lavaan->lav_data_full():      sampling weights variable ‘absent_weight’ not found; variable names found     in data frame are: y1 y2 y3 y4 synthetic_cluster synthetic_stratum w     w_uniform w_scaled cluster_permuted stratum_permuted |
| `api_ordinal_ml` | lavaan->lav_options_set():      missing = “ml” not available in the categorical setting |

Die Fehler entstanden aus den jeweiligen absichtlich geänderten Eingaben in der exakt gepinnten Version. Es wurden keine realen Variablennamen ausgegeben. Entfernung, zufällige Änderung und geordnete Neuzuordnung der unangemeldeten Stratumspalte ändern die verglichenen Koeffizienten, Sample-Statistiken, Gamma und vcov um null. Das `group`-Argument ist laut Dokumentation eine Modellgruppierung und wurde nicht als Survey-Stratum-Adapter ausgegeben. Dokumentierte externe `nacov`-/`wls_v`-Eingaben sind eine mögliche Erweiterungsstelle, kein geprüfter Designadapter.

## semTools und die offene Methodenkette

`compRelSEM(ord.scale=TRUE, W=...)` reproduzierte 0.776364645194645. Unit-Gewichte ergeben exakt denselben Wert wie vier gleiche Gewichte 0,0625. Das ist mit der dokumentierten Skalierungsinvarianz gleicher Kompositgewichte vereinbar. Der Header bezeichnet die Größe als modellbasierte Reliabilität beobachteter Variablen und verwendet die unrestricted Varianz im Nenner. Die konstante Verschiebung bei einer 0–1-Umrechnung ändert einen Varianzquotienten nicht; der Lauf prüft dennoch keine persönliche Unsicherheit.

Als eigener negativer semTools-Fall führte die Kombination ungleicher W und `tau.eq=TRUE` zum Fehler „Cannot calculate coefficient alpha for composite `bad` with unequal weights“. Die gepinnte Implementierung prüft diese Kombination in `R/reliability.R:1248–1253`. Ihre ordinale Berechnung läuft über `omegaCat` in Zeilen 1437–1443/2945–2989. Die Originalformel von Green/Yang, ihre hier erforderlichen Annahmen, designgerechte Reliabilitätsintervalle und Messfehlerbereiche wurden nicht unabhängig methodisch validiert.

`measEq.syntax(return.fit=FALSE)` erzeugte die Klasse `measEq.syntax` und kein lavaan-Fit. Die Syntaxhash `6ae405d6d90f845b0fce6eda6261c4eca65bf4da1bdb78e60ba886b0ac38bde0` stimmt mit dem Autorenartefakt überein. Die API-Dokumentation unterscheidet ausdrücklich Syntaxklasse und fitted `return.fit=TRUE`-Modell. Ich führte keine vollständige Invarianzfolge und keinen robusten Nestungsvergleich aus. Diese Untersuchungen bleiben NICHT_GEPRÜFT, nicht NICHT_BESTANDEN.

## Originalfundstellen und Gegenbelege

Die präzise Quellenlektüre steht zusätzlich in [sources-reviewed.json](../../../outputs/loop/software-review-methods/sources-reviewed.json). Relevante R/Rd-Dateien extrahierte ich selbst aus den gebundenen CRAN-Archiven in meinen eigenen Ordner. Alle neun betrachteten lavaan-Extrakte stimmen bytegenau mit den gebundenen Autorenextrakten überein. Geprüft wurden die genannten Funktionen und Dokumentabschnitte; weder der ganze CRAN-Code noch alle 79 SourceInputs wurden semantisch vollständig auditiert.

| Aussage | Präzise Originalfundstelle | Grenze / Gegenbeleg |
| --- | --- | --- |
| Gewichtete ordinale Cluster-NACOV wird berechnet | lavaan 0.7-2 CRAN-Archiv: `R/lav_muthen1984.R:219–247`; `R/lav_samplestats.R:1215–1233`; `R/lav_lavaan_step02_options.R:199–230` | Independent marginaler Schwellenblock bestätigt; kein vollständiger SEM-/Survey-Theorienachweis |
| Gewichtsinterpretation und Normalisierung | Dasselbe Archiv, `man/lavOptions.Rd:248–274` | Design-/frequency-Gewichte sind unterschiedliche Rechenannahmen; nur design im hier freigegebenen Hauptfall |
| Native Stratumgrenze und externe Matrixeingaben | Dasselbe Archiv, `man/lavaan.Rd:7–14,85–111`; tatsächliche API-Gegenfälle | Drei Namen abgewiesen; keine Aussage, jede externe Erweiterung sei unmöglich |
| Gegenläufige Dokumentaussage | Dasselbe Archiv, `man/lavaan.Rd:59–63` behauptet nur non-clustered Gewichte | Veraltete pauschale Einschränkung wird durch Quelle und Lauf widerlegt. Der Autorenbericht legt sie bereits offen |
| Clustergetter ergibt 1 im singlelevel-Fall | Dasselbe Archiv, `R/lav_object_inspect.R:1402–1434` | Intern und im frisch erzeugten Input 96; nicht als fehlende Clusterkorrektur fehlinterpretieren |
| Beobachtete ordinale Reliabilität und explizite W | semTools 0.5-9 CRAN-Archiv, `man/compRelSEM.Rd:14–58,124–159`; `R/reliability.R:1248–1253,1403–1447,2945–2989` | API-Verträglichkeit, keine Formel-/Abdeckungs-/Intervallabnahme |
| Syntax ist standardmäßig kein Fit | Dasselbe Archiv, `man/measEq.syntax.Rd:7–11,89–94,134–148` | Eigene Klassenprobe bestätigt; group ist keine Survey-Stratifikation |
| Leere Außen-Datei trotz register_envs=false | Conda 26.5.2 `conda/core/path_actions.py:1132–1155`, `conda/core/envs_manager.py:26–47` | `verify()` berührt die Datei vor dem Guard in `register_env`; historischer Vorgang nicht neu ausgeführt |

Die [offizielle 0.7-Historie](https://lavaan.ugent.be/history/dot7.html) beschreibt unter Version 0.7-2 die gewichtete Gamma. Das [offizielle kategoriale Tutorial](https://lavaan.ugent.be/tutorial/cat.html) erklärt DWLS-Punktwerte, robuste WLSMV-Ausgaben und die fehlende kategoriale FIML-Unterstützung. Beide gebundenen HTML-Fassungen wurden gelesen, die offiziellen URLs zusätzlich am 2026-10-03 über `web.run` geöffnet. Die [Linux-Landlock-Dokumentation](https://docs.kernel.org/userspace-api/landlock.html), Abschnitte Regeln und Durchsetzung, und die gebundene lokale setpriv-Manpage Zeilen 73–83/136–163 erklären die zusätzliche Kindprozessbeschränkung. Web-Suchtreffer oder fremde Zusammenfassungen dienen nicht als Ersatz für diese Primärquellen.

## Belegtes Finding

### SOFTWARE-M-01 / bestehender SW-ENV-004: Die originale Einrichtung verletzte den eigenen Schreibumfang

Betroffene Aussage ist das ursprüngliche Vorab-Abnahmekriterium einer vollständig projektlokalen Einrichtung. `plan-before-run.md` erwartete, dass bestätigtes `register_envs=false` den Benutzerpfad beseitigt; `standalone-plan-before-run.md` verlangte einen Guard vor jedem Zugriff. Tatsächlich zeigt das gebundene Conda-Create-Kommando Exit 0 innerhalb 03:26:56.744281Z–03:27:10.484014Z, und `outside-write-incident.json`/die vorigen Snapshots dokumentieren eine vorher fehlende, danach leere `~/.conda/environments.txt`. Datei-/Verzeichnis-Birth-Zeit liegt in diesem Intervall. Die originale Elternverzeichnis-Existenz wurde nicht vorher separat gesichert; dieser Teil bleibt auf die Zeitmetadaten begrenzt.

Das konkrete Problem liegt vor dem Registrierungs-Guard: Conda 26.5.2 `RegisterEnvironmentLocationAction.verify()` ruft `touch(..., mkdir=True)` auf. `register_env()` prüft `register_envs` erst später. Die tatsächlich gelesene Konfiguration `false` ist daher kein hinreichender Beleg für eine vollständig projektlokale Einrichtung.

Schwere hoch für die ursprüngliche Einrichtungsabnahme, weil ein ausdrücklich ausgeschlossener Benutzerpfad geschrieben wurde. Keine erfundene Verletzung von Antwortdaten oder Geheimnissen. Das Finding ist im eingefrorenen Autorenbericht bereits anerkannt und korrekt mit NICHT_BESTANDEN bewertet. Ich erhebe es nicht als neuen Defekt der inzwischen ausdrücklich erlaubten, beschränkten R-Ausführung.

Korrektur ist die dauerhafte Erhaltung des negativen Setupstatus und die Unterlassung weiterer unbeschränkter Conda-Aufrufe. Ein künftiger neuer Installationsnachweis braucht eine vor dem Installer aktive, separat geprüfte Schreibbeschränkung oder einen nachweisbar nebenwirkungsfreien anderen Weg. Eine neue Setup-Abnahme darf nicht rückwirkend den alten Lauf umbenennen. Nachprüfung: eigene direkte Probe, Quellcodegegenprüfung und benannte Metadatenvergleichung durchgeführt, alle engeren Kontrollen bestanden. Keine Außenlöschung oder neue Einrichtung durchgeführt; originale Setup-Abnahme bleibt NICHT_BESTANDEN.

Die fehlende native Stratifikation und die ungeprüfte weitergehende Methodenkette sind korrekt ausgewiesene Grenzen des Pakets. Sie verlangen vor abhängigen ESS-Schritten weitere Belege, sind hier aber keine als ausgeführt behaupteten Fehltests. Es gibt kein weiteres ergebniswirksames Korrektur-Finding gegen die eingefrorenen engen Claims.

## Tatsächliche Kommandos, Werkzeuge und Abbruchgrenzen

Alle Shell-Aufrufe hatten explizit den CWD `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Der R-Kindprozess arbeitete in meinem eigenen Outputordner. Seine vollständigen Argumentvektoren, Environmentwerte ohne Secrets, Start-/Endzeiten, Skript-/Rscript-Hashes und Exitcodes stehen in den eigenen `*-command.json`-Dateien. Primäre Ausführung:

```sh
python -B outputs/loop/software-review-methods/run-r-direct.py boundary-probe outputs/loop/software-review-methods/boundary-probe.R
python -B outputs/loop/software-review-methods/run-r-direct.py methods-check outputs/loop/software-review-methods/check-methods.R
python -B outputs/loop/software-review-methods/finalize-evidence.py
```

Beide R-Launcher-Kommandos und die Abschlusskontrolle lieferten Exit 0. Die Probe war Voraussetzung des Modelllaufs; bei unerwartet erlaubtem Öffnen oder nichtlokalen Pfaden wäre ausschließlich dieser abhängige Lauf gestoppt worden.

Vorbereitung und Lektüre nutzten `cat`, `rg`, `nl`, `sed`, `find`, `sha256sum`, kleine `python -B`-Helfer und gezielte `apply_patch`-Schreibvorgänge ausschließlich in eigene Outputs. Archive wurden mit `tarfile.extractfile` gezielt gelesen und einzelne bekannte R/Rd-Dateien in eigene Outputs geschrieben. Weder Archivskripte noch Installer wurden ausgeführt. Eine `cat`-Lektüre der anfänglich falsch ohne `files/` angesprochenen Freeze-Pfade lieferte Exit 1; die richtigen Pfade wurden danach vollständig gelesen. Die optionale Memory-Registrysuche ergab keinen Treffer und Exit 1; es wurde kein Projektbefund aus Memory übernommen. Ein Python-Vergleichshelfer scheiterte einmal mit Exit 1, weil JSON die benannten R-Koeffizienten als Liste serialisiert; der korrigierte Helfer verglich die explizite Reihenfolge vier freier Ladungen plus 16 Schwellen und bestand mit Exit 0. Das waren Lese-/Helferfehler, keine fehlgeschlagenen CFA-Läufe.

Tatsächlich genutzte Werkzeuge: `functions.exec` mit `exec_command`, `apply_patch`, `write_stdin` und `web__run`; `collaboration.send_message` für eigene Fortschritte an den Koordinator. Der verfügbare Computer-Use-Zugang wurde nicht genutzt. Der Skill `unslop` wurde gelesen und auf den eigenen Bericht angewandt; synchronisierte Skills blieben unverändert. Keine weitere Modellfamilie, kein anderer Revieweragent und kein Providerreview wurden als Prüfbeleg benutzt. Paketlaufzeit laut eigener Probe: R version 4.5.3 (2026-03-11), lavaan 0.7-2, semTools 0.5-9 und die weiteren konkret ausgegebenen Bibliotheken. Interne Modellrevision des prüfenden Agents unbekannt.

Repositorykontrolle `pnpm check` lief mit Exit 0. Formatprüfung, Handbuch-/Review-Schemakontrolle, Typecheck, neun Tests und Produktionsbuild bestanden. Das vollständige eigene Log liegt unter `outputs/loop/software-review-methods/pnpm-check.log`; Aufruf, Zeit und Exitcode unter `pnpm-check-command.json`. Keine UI-Änderung, daher keine neue Browser-UI-Abnahme. Ein technischer Repositorycheck verändert die wissenschaftlichen Status nicht.

## Artefakte und SHA256

Eigene Ausführungsbelege liegen ausschließlich unter `outputs/loop/software-review-methods/`. Zahlen in diesem Bericht wurden durch `generate-report.py` aus dem tatsächlich erzeugten JSON eingefügt. Die Erstberichtdatei wird nach ihrem erstmaligen Abschluss nicht automatisch formatiert oder überschrieben. Der Abschlussmanifest enthält den finalen Berichtshash und den nachgelagerten Repositorycheck.

| Eigenes Artefakt | SHA256 |
| --- | --- |
| `plan-before-run.md` | `204e718a544155cbbd1b6a71bdfd2c7a60980ecbd3c5425c0e941373921ddd94` |
| `run-r-direct.py` | `d3858701f5c858f08b0aea7f0efd652b566f3c0ed6e8a969285a4ccbe8112c88` |
| `boundary-probe.R` | `8fbbe422c7b7765ee16b08089a89209c4c462d65f9ce7437ac532918338911b7` |
| `boundary-probe-command.json` | `4456687f095029f6d7cb06a3504f0804a0008856a438aed54e76c04ac8b68ede` |
| `boundary-probe.json` | `d77bcc852ef5ec1bb0861b654e9f0c31534b89353189602332ba779f4e4cdd4c` |
| `check-methods.R` | `4c39266244aec09e59f6c88d2b104a84bcfc8823bf913a256b38ee837dece26f` |
| `methods-check-command.json` | `b310362b6e1731ec282f64bfaea069b38a255ad9eeea8ffc302cf7e5f9a9dc30` |
| `methods-results.json` | `5a59b85ec7944ebb026f059498746fb31af4aeba691c359b2ecdf86b1e65a9c6` |
| `synthetic-input.csv` | `2360c7663743bb2078601d86068b478f654c8c298866f0cb1b23bb86bc1863f7` |
| `threshold-invariance-syntax.txt` | `6ae405d6d90f845b0fce6eda6261c4eca65bf4da1bdb78e60ba886b0ac38bde0` |
| `author-independent-comparison.json` | `5c4afc1e641edf60dff4f5e3a269b94e5c159e175baf7392f1be1689af573a33` |
| `hashes-before.json` | `1ab8e6e185c1054774d4e1883153a465dc25f72c08895503ba27b98a082b8736` |
| `hashes-after.json` | `b459110fdaa810fe9b1863337e2c3e93019467fafdc0cfe99d49e375b29be153` |
| `archive-runtime-before.json` | `1b6f67a8e37e9ab4ecf25d010c756d27f17b2ce8caf9a495f12b56839a1784e1` |
| `runtime-after.json` | `ec89b43b1ee23e175f348fc7f3fe6a1e61a6316a771c5745fa478598c3d23101` |
| `outside-metadata-before.json` | `6b96df4ebd61f75cdd77be5e8eee107c24882f3fd6c25e4bd5ad69ba54310bdd` |
| `outside-metadata-after.json` | `bffed125dd61ac5d09d61c6b2a9173ac94482be1eabb459ab0ad074509903766` |
| `sources-reviewed.json` | `91988fdb60c4c1555a629efac0617dc1a8cb0bff7adcadd8320fcb4270ddbcc4` |
| `startauftrag.txt` | `a4969cc13cd58647f087c286b9448bf824576b8ad1ab4e051219a7f268896187` |

## Vollständiger tatsächlicher Startauftrag

```text
Du bist unabhängiger SOFTWARE-001-Prüfer für Methoden, Softwarefähigkeit und Primärquellen. Worktree ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, explizite cwd. Lies AGENTS, Auftrag und Issue aus dem eingefrorenen Paket reports/loop/packages/SOFTWARE-001/v1/manifest.json SHA256 126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e. Dasselbe Paket für zwei Reviewer:8Dateien/79 SourceInputs; Kriterien reports/loop/SOFTWARE-001-pruefauftrag.md. Keine fremden Reviewerberichte/Loopfindings/Agentregister oder zusätzliche Autorenverteidigung lesen. Paket und lokale gebundene SourceInputs einschließlich Primärquellen/CRAN-Code/Laufzeitlock/Originalkommandos selbst prüfen. Quelle gewichtete ordinale Cluster-CFA in lavaan0.7-2, native Stratumgrenzen, erste marginale Schwelle, Gamma-Taylor-Vergleich, semTools-API versus tatsächlich ungeprüfte Invarianz-/Reliabilitätskette. Führe eigene begrenzte Rechen-/API-Gegenfälle tatsächlich aus. Kein ESS/data/raw/local/A/B/Partei/LR/echte Personen, keine Portal-Analysis oder Cookie-/Storagewerte. KEIN Conda/Umgebungsneuaufbau oder globaler Write. Vor Ausführung vorhandenes outputs/loop/software-author/run-r-direct.py und scoped-env.json lesen. Nur direkte vorhandene projektlokale Rscript --vanilla-Ausführung mit setpriv Landlock/no-new-privs und eigenen Projektwritepfaden; eigenen Launcher in outputs/loop/software-review-methods/ vorbereiten, gezielt eigene Ausgaben/Cache/Tmp erlauben, ursprüngliche Autorenoutputs/Sources und eingefrorene Dateien nicht überschreiben. HOME unverändert, Userprofile/Renviron/Rhistory deaktiviert. Keine erweiterten Rechte/Sicherheitsumgehung. Außenwrite-Setup bleibt NICHT_BESTANDEN; numerische enge Positivtests heilen ihn nicht. Grenze selbst prüfen; bei nicht kontrollierbarer Ausführung nur abhängigen Lauf blockieren. Eigenbericht reports/loop/reviews/SOFTWARE-001-methods.md plus eigene synthetische/public Outputs. Vollständigen tatsächlichen Startauftrag wortgetreu, Tools/Modelle tatsächlich dokumentieren (GPT-6.1-Sol laut Runtime, interne Revision unbekannt), Hashes vor/nach, Kommandos/Exitcodes/Prüfresultate/Originalfundstellen. Findings konkrete Aussage, Gegenbeleg/Fundstelle, Problem/Folge, begründete Schwere, Korrektur/Nachprüfung; keine vorgegebene Menge. Zukünftige empirische Abnahmen nicht als ausgeführte Fehltests behandeln. SharedFS-Verhaltenstrennung offenlegen, keine andere Modellfamilie behaupten. Keine weiteren Agents/Commit/Push. Vollständig schließen und Bericht+Hash+Kurzbefund melden.
```
