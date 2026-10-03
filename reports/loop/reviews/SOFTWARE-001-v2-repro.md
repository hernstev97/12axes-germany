# SOFTWARE-001 v2: unabhängige Kontrolle von Ausführungsbeschreibung und CASE-P01

Prüfer `/root/software_v2_repro`, 2026-10-03. Codex-Subagent, laut geerbtem Startauftrag `gpt-6.1-sol` mit Reasoning `ultra`. Diese Angaben stammen aus dem Auftrag beziehungsweise der Sitzungsbezeichnung. Eine unveränderliche interne Modellrevision und nicht zugängliche Anbietervorgaben sind unbekannt. KI-Audit, keine wissenschaftliche Gesamtfreigabe und kein akademisches Peer Review.

Die enge Korrektur von SOFTWARE-001-REPRO-02 besteht meine Nachprüfung. Der korrigierte Start beschreibt die tatsächlich konfigurierten Dateirechte und nennt IOCTL, Netzwerk, Lesen/Ausführen, geerbte Deskriptoren sowie den unbeschränkten Python-Supervisor als Grenzen. Meine eigene kleine R-Probe und der ausgeschriebene Commandvergleich bestätigen den konkreten Umfang. Der historische einzelne Claude-P01-Negativfall ist in der gebundenen reinen Modellantwort nachvollziehbar und formal gültig. Eine genaue Versionsbindung der CLI an den historischen Protokollstart fehlt; dies ist ein niedriges, nicht scope-blockierendes Finding. Die ursprüngliche Einrichtung bleibt NICHT_BESTANDEN.

| Gegenstand | Status | Tatsächlich geprüfter Umfang |
| --- | --- | --- |
| SOFTWARE-001-REPRO-02, neue Beschreibung und Command | BESTANDEN / KORRIGIERT | Originalkernelstellen, korrigierter Rechtevektor, zwei Allow-Regeln, ausdrückliche Grenzen und eigene R-Gegenprobe |
| Eigene begrenzte R-Probe | BESTANDEN | Ausgewählte Pfade, NoNewPrivs, ignorierte eigene Sentinels, Deskriptorziele, verweigerte Manifest-Schreiböffnung und erlaubtes Lesen |
| V2-Paket-/SourceInputbindung | BESTANDEN | Alle 18 Dateien und 123 SourceInputs vor/nach passend und unverändert |
| Ausgewählte vorhandene Runtimebindung | BESTANDEN | Rscript und je 30 Dateien aus lavaan/semTools vor/nach gegen Lock passend und unverändert |
| Historischer Claude-CASE-P01 und eigene Schema-/Bindungskontrolle | BESTANDEN | Ein erfundener Negativfall, reine Antwort BLOCKIERT, exakte Prompt-/Skill-/Schemabindung, eigene Ajv-Gegenfälle |
| Exakte CLI-Version zum Protokollstart | NICHT_GEPRÜFT | Spätere 2.1.288-Ausgabe vorhanden; keine unmittelbar laufgebundene Version-/Binarybeobachtung |
| Originale vollständig projektlokale Einrichtung | NICHT_BESTANDEN | Bestehendes SW-ENV-004 / SOFTWARE-M-01 / SOFTWARE-001-REPRO-01 unverändert |
| Neue vollständige SEM-Reproduktion | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Numerischer Code und Input unverändert; Beschreibungsreparatur erzeugt keine neue Rechenhypothese |
| Eigener Repositorycheck `pnpm check` | NICHT_GEPRÜFT | Gemeinsame Buildoutputs außerhalb meines Schreibauftrags; Koordinator um nachgelagerten Check gebeten |
| Neue Claude-Ausführung, automatischer Skill-Loader, GitHub-Setup, Forschungs-Erstbewertung, Menschen-/Neutralitäts-/Releaseabnahme | NICHT_GEPRÜFT | Durch diesen einzelnen Protokollfall und dieses Codex-Audit nicht erfüllt |

## Eingefrorene Grundlage und Zugriffstrennung

Maßgeblich ist `reports/loop/packages/SOFTWARE-001/v2/manifest.json`, SHA256 `c88656c49ce561b9d57d2e1975ef82dabeb9b745fbefb14cda1e1d415f8a5ddf`, Codecommit `5641f8103a9de703c71d01fb2688ebcc5cf82c31`. Die 18 Freeze-Dateien und 123 SourceInputs wurden anhand des Manifestes geprüft. Die Paketaussage „Dateifassung; keine Prüfung oder Freigabe aus Hashes ableiten“ bleibt zutreffend.

Gelesen wurden eingefrorene AGENTS, der vollständige Dauerauftrag, LIFE-93, beide SOFTWARE-Prüfaufträge, Manifest, beide ausdrücklich zugelassenen historischen SOFTWARE-Erstberichte, Annahmeentscheidung und Korrekturbericht. Die Lektüre der historischen Erstberichte war Teil dieses Reparaturauftrags; sie ist keine neue unabhängige Erstprüfung ihrer numerischen Ergebnisse. Tragende zusätzliche Inputs waren Original- und Korrekturlauncher, Scoped-Environment, gebundener Laufzeitlock, Kernel-/setpriv-Originalstellen, ausgewählte Conda-Originalstellen sowie die vorgesehenen Claude-P01-Dateien. Alle 123 SourceInputs wurden gehasht; daraus folgt keine semantische Vollprüfung sämtlicher Archive und Logs.

Aktuelle v2-Reviewerurteile, FOUNDATION-/Juror-/PREP-Berichte, Agentlisten, Loopfindings und zusätzliche Autorenverteidigung außerhalb des Pakets wurden nicht gelesen. Kein Zugriff auf ESS-Rohdaten, lokale Antwortdaten, A/B, Partei-/LR-Werte, Portal-/Credential-/Cookie-/Financial-Diagnostik. Die gebundenen historischen Benutzerdatei-Snapshots wurden als Belege gelesen; die Benutzerdateien selbst wurden weder geöffnet noch neu gehasht. Provider-Envelope/stdout und Debug wurden weder gelesen noch neu gehasht. Die in der bereinigten Ausführungsmetadatei gespeicherten stdout-/stderr-Digests bleiben übernommene Metadaten.

Alle Shellaufrufe hatten ausdrücklich den Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003` als cwd. Meine neuen Dateien liegen nur in `outputs/loop/software-v2-repro/` und dieser Berichtdatei. Die eigentlichen R-Kinder arbeiten im eigenen Outputordner. Kein Originaloutput, Originallauncher, eingefrorenes Paket oder Runtimefile wurde verändert. Kein Conda, Installer, Paketaufbau, Geräte-IOCTL, Außen-Cleanup, Commit, Push, Merge, Deployment oder weiterer Agent.

Die Trennung beruht auf dem begrenzten Auftrag und meinem Zugriffsverhalten. SharedFS und Shellwerkzeuge sind nicht technisch auf dieses Paket lesebeschränkt. Andere Agents und der Koordinator können dieselben Dateien erreichen. Der Python-Supervisor liegt außerhalb der Kindprozess-Landlock-Regel. Das ist keine vollständige Geräte-, Netzwerk-, Lese-, Deskriptor- oder PC-Isolation.

Der vollständige Vorhersnapshot entstand nach rein lesender Orientierung einschließlich erster Manifest-/Regellektüre und vor der eigenen R-Probe. Er ist kein rückwirkendes Monitorprotokoll des allerersten Zugriffs. Die allererste explizite Manifestberechnung ergab bereits den erwarteten SHA256. Die Pfadprüfung schloss absolute Manifestpfade, Traversal, raw/local/debug-Pfade und Symlinkausbrüche aus. Die vorgegebenen SourceInputs sind öffentliche Softwarequellen oder ausgewiesene künstliche Laufzeit-/Protokollbelege; keine unbekannte Rohquelle wurde zum Hashen geöffnet.

## Originalfundstellen und REPRO-02

Selbst gelesen wurde die gebundene [Linux-Kerneldokumentation](https://docs.kernel.org/userspace-api/landlock.html), lokale Datei `outputs/loop/software-author/sources/linux-landlock.html`, SHA256 `1c258549336d01df7163ef551674b314c9e6b81ae4b9f26c3b4d80336ab87875`. Zeilen 1029–1037 unterscheiden explizit behandelte Rechte von unaufgeführten Zugriffen und nennen die historische REFER-Ausnahme. Zeilen 1228–1242 erklären die Durchsetzung auf dem aufrufenden Thread und NoNewPrivs. Zeilen 1363–1377 nennen IOCTL_DEV als gesondertes Recht und begrenzen es auf neu geöffnete Geräte; vorbestehende stdin/stdout/stderr bleiben davon unberührt. Dies ist die lokal gebundene Originalfassung, kein neu abgerufener Webstand.

Die gesamte gebundene lokale `setpriv-2.42.4-local-manual.txt`, SHA256 `64235fe477c56e490266ee037b387ba6329a12b4e92e53b5802052da14819d4b`, wurde gelesen. Zeilen 73–83 erklären NoNewPrivs und Vererbung, 136–164 unterscheiden behandelte Zugriffskategorien und konkrete Allow-Regeln; 197–198 nennen Abbruch ohne Programmstart bei fehlgeschlagener Option. Mein eigener lesender `setpriv --version` meldet util-linux 2.42.4, `uname -sr` Linux 7.2.8-1-cachyos.

SOFTWARE-001-REPRO-02 betrifft die genaue historische Aussage `run-r-direct.py:48` „no ioctl permission“ und die Metadatenzeile 55 „no ... ioctl access“. Der Originallauncher in Zeilen 38–39 enthält kein ioctl-dev. Die Originalquellen tragen diese Beanstandung. Schwere bleibt mittel: falsche Beschreibung einer Schutzgrenze, ohne beobachtete schädliche Geräteoperation oder Widerlegung numerischer Befunde.

Die konkrete Korrektur steht in `outputs/loop/software-correction/run-r-correction.py:17,80–101`: zwölf ausgeschriebene Dateirechte, ein eigener Verzeichnisbaum und `/dev/null:write-file`; ausdrückliche Einschränkungen für unaufgeführte Rechte, Deskriptoren und Supervisor. Meine Nachprüfung vergleicht den vollständigen erzeugten Autorencommand und meinen eigenen Command jeweils mit einem unabhängig ausgeschriebenen Sollvektor in `check-bindings-corrected.py`. Alle diese Kontrollen bestehen. Der falsche historische Originaltext bleibt als Original erhalten; die neue Korrekturfassung hebt seine Fehler nicht aus der Historie auf. REPRO-02 ist für diese neue Beschreibung KORRIGIERT.

Der unveränderte Außenwrite bleibt SW-ENV-004 / SOFTWARE-M-01 / SOFTWARE-001-REPRO-01. Exakte Aussage ist die ursprünglich geforderte vollständig projektlokale Einrichtung. Die gebundenen Snapshots melden `.conda/environments.txt` vorher fehlend und nachher als neue leere Datei. `outside-write-incident.json` nennt die begrenzten Metadatennachweise und den historischen NICHT_BESTANDEN-Status. Conda 26.5.2 `conda-core-path_actions.py:1132–1155` ruft `touch` in verify auf; `conda-core-envs_manager.py:26–52` setzt den register_envs-Guard erst später. Damit ist die Auswirkung auf die ursprüngliche Einrichtungsabnahme nachvollziehbar. Schwere weiterhin erheblich wegen des tatsächlich ausgeschlossenen Benutzerpfad-Writes, ohne Behauptung größerer Schäden. Korrektur/Nachprüfung bleiben negative Historie erhalten, keine Außenbereinigung oder neue Conda-Ausführung, spätere sichere R-Proben getrennt. Das Finding wird weder umbenannt noch als geheilt geschlossen.

## Eigene kleine tatsächliche R-Gegenprobe

`plan-before-run.md` entstand vor den ausführbaren Proben. Die neue Kopie von `run-r-correction.py` ändert nur OWN auf meinen Outputordner sowie Manifestpfad/-Sollhash auf v2. Die Kopie der R-Probe prüft v2 statt v1 und ergänzt ein bewusst zulässiges gewöhnliches Manifestlesen sowie Beobachtung der drei Deskriptorziele. `adaptation.json` enthält Original-/Eigenhashes und vollständige Diffs; die beiden ursprünglichen Sentinels wurden unverändert kopiert. Kein numerischer Code wurde angepasst.

Der vollständige tatsächliche R-Argumentvektor lautet:

```json
[
  "/usr/bin/setpriv",
  "--no-new-privs",
  "--landlock-access",
  "fs:write-file,remove-dir,remove-file,make-char,make-dir,make-reg,make-sock,make-fifo,make-block,make-sym,refer,truncate",
  "--landlock-rule",
  "path-beneath:write-file,remove-dir,remove-file,make-char,make-dir,make-reg,make-sock,make-fifo,make-block,make-sym,refer,truncate:/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/software-v2-repro",
  "--landlock-rule",
  "path-beneath:write-file:/dev/null",
  "/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/software-env/envs/r-smoke/bin/Rscript",
  "--vanilla",
  "/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/software-v2-repro/runtime-probe.R",
  "/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003",
  "/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/software-v2-repro",
  "/home/stevenh"
]
```

Nur die zwölf benannten Dateirechte werden behandelt. Genau zwei Allow-Regeln erlauben sie im eigenen Outputbaum und ausschließlich write-file für `/dev/null`. Kein ioctl-dev und keine Netzwerkzugriffskategorie sind konfiguriert. Rscript wurde mit `--vanilla` direkt aus dem bestehenden Präfix gestartet. Der Rscript-SHA256 ist vor/nach `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`. HOME blieb `/home/stevenh`. TMP, Cache, XDG, Historien- und Sentinelpfade liegen im eigenen Ordner; vorhandene Bibliotheken sind Lesepfade.

Der R-Lauf 2026-10-03T05:17:19.731237+00:00 bis 2026-10-03T05:17:19.895662+00:00 endete mit Exit 0. Ergebnis `runtime-probe-result.json` meldet R 4.5.3, NoNewPrivs=1 und CapEff=0000000000000000. Alle 17 konkreten Checks bestanden. Eigene Profile/Renviron-Sentinels wurden ignoriert; die beiden Variablen waren im Vanilla-Prozess leer. Der eigene feste Text wurde erzeugt. Die nichttrunkierende r+b-Öffnung des v2-Manifestes scheiterte mit Permission denied, ohne Verbindung und ohne Inhaltsoperation. Gewöhnliches readLines desselben öffentlichen Manifestes war möglich. Das zeigt die erklärte Grenze des nicht behandelten read-file-Rechts. Kein Benutzerfile wurde für den Gegenfall geöffnet.

stdin zeigte eine Pipe; stdout und stderr zeigten genau auf das eigene runtime-probe.log. `close_fds=True` und diese drei Beobachtungen beweisen keine Vollkontrolle aller möglichen geerbten Deskriptorwirkungen. `/dev/null` ist nur eine benannte Ausnahme des behandelten write-file-Rechts. Auch der R-Lauf beweist weder IOCTL-Sperre noch vollständige Netzwerk-/Geräte-/Syscall-Kontrolle.

## Unveränderte historische Zahlen und Runtime

`input-before.json` und `input-after.json` vergleichen tatsächlich alle 141 Manifesteinträge mit Sollbytes und SHA256, vor/nach identisch. `runtime-before.json` und `runtime-after.json` lesen 61 benannte bestehende Runtimefiles gegen `environment-lock.json`: Rscript und je 30 lavaan-/semTools-Dateien. Sie stimmen sämtlich und bleiben unverändert. Dies ist keine vollständige Prüfung aller Runtimeabhängigkeiten oder ein sauberer Neuaufbaunachweis.

Die historische Korrektur hatte ihrerseits Vorher-/Nachhersnapshots mit 97 Zeilen. Meine tatsächliche Prüfung vergleicht deren gespeicherte Einzelhashes mit den jetzt selbst berechneten v2-Hashes, ohne ungelistete v1-Dateien zu öffnen. Alle 97 passenden historischen Records stimmen, einschließlich numerischem Skript, synthetischem Input und eingefrorenem numerischem Bericht; die historischen Korrektursnapshots sind untereinander gleich. Doppelte Spiegelrecords sind Records, keine zusätzlichen unabhängigen Dateien.

Der numerische Pipelinehash bleibt `47a71a6dfb280b93d0c4eeca5df6d9ea1822343d7defe737cc1f5bfce803133c`, synthetischer Input `2360c7663743bb2078601d86068b478f654c8c298866f0cb1b23bb86bc1863f7`, numerischer Freezebericht `574f5fc6b1db09aa136a388696aa2bcb60e3ef8bc94faadccec46acc88bf35fc`. Die beiden abgeschlossenen Erstberichte wurden vollständig gelesen und sind gegen ihre gebundenen Hashes unverändert. Ich wiederholte ihre SEM-Rechnungen nicht. Hier geprüft ist tatsächliche Bytekontinuität, keine frische Zahlenreproduktion. Vollständige ESS-Designfähigkeit, fitted Invarianzfolge, Reliabilitäts-/Unsicherheitsvalidierung und Forschungsgates bekommen keinen neuen positiven Status.

## Der tatsächliche einzelne Claude-P01-Fall

Der vollständige gebundene Prompt `claude-protocol-001-auftrag.txt` wurde gelesen. Sein erster Absatz bezeichnet ausdrücklich einen erfundenen CASE-P01, setzt SYNTHETISCHE_SKILLPRUEFUNG, enthält keine menschlichen Antworten oder Originalbelege und verlangt genau ein JSON ohne erfundene Lektüre, Hashberechnung, fremden Review oder interne Modellrevision. Eine Laborbeschreibung liegt nicht als Prüftext vor; lediglich die hypothetische Behauptung zuverlässigen Alpha-Verständnisses ist genannt. Kein Forschungsitem wurde bewertet.

Eigene Bytes-/Hashvergleiche bestätigen Prompt gegen prompt.txt, reine Antwort gegen result.txt, Skill/Schema gegen die Vorabplanhashes sowie die wortgetreue Einbettung beider Texte in den Prompt. Die exakten Digests sind Prompt `b97b751888e6eb4e970e703db523283544afe7871428d48195c48342588d9e88`, Skill `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6`, Schema `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` und reine Antwort `3babe6618c546014ccbceed314a88de904f1dd4a1233d16d22f8d92deec32388`.

Der Vorabplan ist datiert vor der gespeicherten Ausführung. Der bereinigte Original-Ausführungsbeleg meldet 04:36:25.487004–04:37:05.296644 UTC, Exit 0, keinen Timeout/Fehler, --model claude-opus-5-5, leere --tools und keine Sessionpersistenz. modelUsageIds nennt claude-opus-5-5 sowie claude-haiku-4-5-20251001. Hauptmodell- und Nebenmodellbezeichnungen in der eingefrorenen öffentlichen Ausführungsdatei sind ergänzende Koordinatorfelder; ich prüfe ihre Konsistenz zu angefordertem Modell und den ursprünglichen Usage-IDs, keine unabhängige Anbieterattestation. Die reine Modellantwort unterscheidet ihre eigene Modell-Selbstauskunft ausdrücklich vom externen Laufzeitnachweis. Interne Revision und Vorgaben bleiben null/unbekannt.

Die ursprüngliche bereinigte `outputs/loop/claude-protocol-001/execution.json` hat SHA256 `4f9197974890bab4a9562aae617c70d1af0593fcfb86493116fd5f82086bf6b7`; die eingefrorene angereicherte Datei `aa979562f0eab7dfe04d00214e5cb7850baea5b2b26edbb88e3a7d26d8f2fedf`. Sie sind absichtlich nicht bytegleich. Alle ursprünglichen Felder außer präzisierter scope-Formulierung sind gleich; genau vier zusätzliche Felder heißen checksByCoordinator, resultSha256, evidencedMainModel und auxiliaryModelObserved. Beide Fassungen sind separat im Manifest gebunden. Eigenständige Inhaltsprüfung und tatsächliche Hashberechnung ersetzen das bloße Übernehmen der Koordinator-Checks.

Die reine Antwort steht auf BLOCKIERT mit null Manifest, leeren inputHashes/tools/findings und unbekannter interner Revision. C1-MANIFEST, C2-EINGABEBINDUNG, C3-ORIGINALBELEGE und C4-MENSCHLICHE-VERSTAENDLICHKEIT sind jeweils BLOCKIERT und requiredInScope=true; C5-RELEASE-FREIGABE ist ausdrücklich außerhalb des Umfangs. Die exakten IDs im JSON sind `C1-VORAUSSETZUNG-MANIFEST`, `C2-EINGABEBINDUNG`, `C3-ORIGINALBELEGE`, `C4-MENSCHLICHE-VERSTAENDLICHKEIT` und `C5-RELEASE-FREIGABE`, alle eindeutig. Zeilen 70–78 unterscheiden fehlende Voraussetzungen von einer empirischen Widerlegung und begrenzen Loader-/Menschen-/Wissenschaftsaussagen.

Diese Antwort erfüllt die vorab genannten Negativfallkriterien. Das ist ein einzelner tatsächlicher, historischer Modelllauf. Ich führte keinen neuen Claude-Aufruf durch. Der Fall zeigt keine allgemeine Protokolltreue, politische Neutralität, automatische Skillauflösung, fachliche Erstbewertung, vollständige Forschungskontrolle, Menschentests oder GitHub-Workflowausführung. Ein explizit eingefügter Skilltext ist kein Loadernachweis.

## Eigene Ajv-strict-Kontrolle

Der gebundene historische Validator `validate.mjs` wurde gelesen. Er kompiliert die lokale Skill-Schemadatei mit Ajv2020 strict:true, allErrors:true und validiert die reine result.json. Sein gespeicherter Exit 0 und der Logdigest stimmen mit dem tatsächlich gelesenen `validate.log` überein. Der historische Validator prüft formale Schemaangaben; die Koordinatorchecks sind separat.

Mein `check-schema.mjs` lädt ausschließlich die eingefrorene Schemadatei und die ursprüngliche reine Modellantwort. Der unabhängige neue Lauf endet mit Exit 0. Alle 17 Fälle entsprechen den Vorabkriterien; darunter 14 erwartete Zurückweisungen. Vollständige Ajv-Fehler und tatsächliche Befunde stehen in `schema-countercases.json`.

| Gegenfall | Erwartung | Tatsächlich |
| --- | --- | --- |
| `actual-unchanged-Claude-P01` | gültig | gültig |
| `synthetic-positive-format-only` | gültig | gültig |
| `passed-null-manifest` | zurückweisen | zurückgewiesen |
| `passed-empty-input-hashes` | zurückweisen | zurückgewiesen |
| `passed-no-checks` | zurückweisen | zurückgewiesen |
| `passed-no-required-green-check` | zurückweisen | zurückgewiesen |
| `passed-required-blocked-check` | zurückweisen | zurückgewiesen |
| `passed-required-failed-check` | zurückweisen | zurückgewiesen |
| `passed-empty-evidence` | zurückweisen | zurückgewiesen |
| `passed-open-blocking-finding` | zurückweisen | zurückgewiesen |
| `corrected-still-blocks` | zurückweisen | zurückgewiesen |
| `outside-scope-still-blocks` | zurückweisen | zurückgewiesen |
| `unknown-top-level-field` | zurückweisen | zurückgewiesen |
| `missing-required-in-scope` | zurückweisen | zurückgewiesen |
| `malformed-input-hash` | zurückweisen | zurückgewiesen |
| `passed-outside-scope-blocked-check` | gültig | gültig |
| `internal-instructions-claimed` | zurückweisen | zurückgewiesen |

Die positive künstliche Formatvariante benutzt bewusst erfundene gültige SHA256-Strings. Dass das Schema sie akzeptiert, ist eine demonstrierte Grenze, kein belegter Inputhash und kein bestandener Forschungsfall. Dass ein späterer, requiredInScope=false-Check offen bleiben darf, ist scopegerechtes Verhalten. Eine Schemaannahme ersetzt weder echte Bindung noch fachliche Wahrheit oder tatsächliche Workflowsteuerung.

## Neues nicht blockierendes Finding

### SOFTWARE-001-V2-REPRO-01: genaue CLI-Version nicht unmittelbar an den Protokollstart gebunden

Exakte betroffene Aussage ist `SOFTWARE-001-runde1-entscheidungen.md:9`: „Claude Code 2.1.288 wurde ... ausgeführt.“

Überprüfbarer Beleg: Die eingefrorene `claude-protocol-001-execution.json:3–4,14,26–41` nennt den Protokolllauf 04:36:25–04:37:05 UTC und den Programmpfad, enthält aber keinen laufgebundenen CLI-Versions- oder Executablehash. `outputs/loop/claude-protocol-001/cli-version.json:14–19` dokumentiert `--version` am gleichen Pfad erst 04:47:29 UTC mit Exit 0 und stdout „2.1.288 (Claude Code)“. Meine Bindungskontrolle bestätigt diese tatsächlich gespeicherten Angaben, ohne die CLI erneut aufzurufen.

Problem: Die spätere Versionsausgabe beweist die bestehende CLI-Version zum Zeitpunkt dieser Abfrage. Die unmittelbare Gleichheit mit dem rund elf Minuten früheren Protokollprogramm ist im vorgegebenen Paket nicht nachgewiesen. Es gibt keinen Beleg für einen Versionswechsel; ich behaupte keine falsche oder andere tatsächlich eingesetzte Version.

Wirkung und Schwere: niedrig, BELEGT als zeitliche Provenienzlücke, blocksScope=false. Die genaue Versionsaussage sollte enger sein. Die exakte Prompt-/Antwortbindung, beobachtete BLOCKIERT-Antwort und korrigierte Dateirechte werden dadurch nicht widerlegt; keine wissenschaftliche Freigabe hängt hier an einer CLI-Version.

Konkrete Korrektur: Die bestehende Aussage präzisieren auf „gleicher CLI-Pfad; nachgelagerte Versionsabfrage am 04:47:29 UTC meldete 2.1.288; keine unmittelbar an den Protokollstart gebundene Version“. Originale unverändert lassen. Bei einem später ausdrücklich beauftragten neuen Protokollfall vor Start CLI-Version und Binaryhash binden und nachher erneut vergleichen. Für diese Dokumentationskorrektur braucht es keinen neuen Claude-Lauf.

Nachprüfung: In einer neuen gebundenen Fassung kontrollieren, dass zeitlich spätere Versionsabfrage und historische Protokollausführung getrennt beschrieben sind. Das Finding bleibt OFFEN gegen die genaue Versionsformulierung; es blockiert diese beiden engen technischen Prüfumfänge nicht.

## Tatsächliche Kommandos, Fehler und Werkzeuge

Die folgenden Schritte wurden einzeln über `python3 -B outputs/loop/software-v2-repro/run-step.py <schritt>` ausgeführt. Jede eigene `*-step-command.json` speichert den vollständigen tatsächlichen inneren argv, root-cwd, Zeit und Exit. Der R-Start speichert zusätzlich den oben vollständigen setpriv-/R-argv und ausgewählte sichere Umgebungswerte. Die Logdateien enthalten unverändert stdout/stderr.

| Schritt | UTC-Intervall | Exit |
| --- | --- | --- |
| `runtime-before` | `2026-10-03T05:17:19.604893+00:00` bis `2026-10-03T05:17:19.668916+00:00` | 0 |
| `runtime-probe` | `2026-10-03T05:17:19.704030+00:00` bis `2026-10-03T05:17:19.918120+00:00` | 0 |
| `schema` | `2026-10-03T05:17:19.961122+00:00` bis `2026-10-03T05:17:20.075088+00:00` | 0 |
| `setpriv-version` | `2026-10-03T05:17:34.559050+00:00` bis `2026-10-03T05:17:34.560393+00:00` | 0 |
| `kernel-version` | `2026-10-03T05:17:34.583822+00:00` bis `2026-10-03T05:17:34.585132+00:00` | 0 |
| `python-version` | `2026-10-03T05:17:34.611332+00:00` bis `2026-10-03T05:17:34.612750+00:00` | 0 |
| `node-version` | `2026-10-03T05:17:34.645947+00:00` bis `2026-10-03T05:17:34.661906+00:00` | 0 |
| `runtime-after` | `2026-10-03T05:19:49.058215+00:00` bis `2026-10-03T05:19:49.122344+00:00` | 0 |
| `input-after` | `2026-10-03T05:19:49.150731+00:00` bis `2026-10-03T05:19:49.365208+00:00` | 0 |

Bindungskontrolle zunächst `python3 -B outputs/loop/software-v2-repro/check-bindings.py`, Exit 1: Meine eigene zu starke Annahme einer bytegleichen Original-/Freeze-Ausführungsmetadatei traf nicht zu. Beide Versionen waren bereits korrekt separat gebunden; die erlaubte Anreicherung wurde danach einzeln verglichen. Die Erstfassung und ihr Ergebnis bleiben erhalten. `python3 -B outputs/loop/software-v2-repro/check-bindings-corrected.py`, Exit 0, liefert 42 tatsächliche Checks und 97 historische Hashvergleiche. `own-check-repair.json` nennt die genaue Differenz und Reparatur. In der ursprünglichen gebündelten Shell war der letzte Leseaufruf erfolgreich; deren Exit 0 ist kein Erfolg des ersten Bindungshelfers. Kein R-/Claude-/Schemafehltest wurde damit verdeckt oder wiederholt.

Rein lesende Orientierung nutzte pwd, rg --files, cat, sed, nl und Python-JSON-/SHA256-Helfer. Eine erste Manifestlisten-Ausgabe behandelte files fälschlich als Liste; der Helfer scheiterte mit TypeError/Exit 1 und wurde unmittelbar durch die korrekte Dictionary-Lektüre ersetzt. Zwei anfängliche gebündelte Toolausgaben waren abgeschnitten; die vollständigen tragenden Dokumente und Quellenstellen wurden danach gezielt gelesen. Diese ersten Orientierungskommandos und inline-Python-Erstellungen sind im tatsächlichen Tooltranskript dokumentiert; ihre Zeiten wurden nicht rückwirkend erfunden und kein zusätzlicher vollständiger lokaler Shellmitschnitt behauptet.

Die Toolverfügbarkeits-Sicherung scheiterte zunächst rein im JavaScript-Wrapper wegen fehlendem TextEncoder, danach vor Prozessstart wegen zu langer Argumentliste beim Versuch, alle Beschreibungen zu schreiben. Die korrigierte reine Namenliste enthält 633 tatsächlich verfügbare nested Toolnamen. Diese beiden Fehler führten zu keinem Forschungs-/Runtimeaufruf. `tool-availability.json` enthält die verfügbaren Toolnamen und deklarierten Top-Level-Werkzeuge; es ist keine Agent-/Sitzungsliste.

Genutzte Agentwerkzeuge waren ausschließlich functions.exec mit exec_command sowie collaboration.send_message an den Koordinator für eigene Fortschritte, Findings und Checkbedarf. Lokal: Bash, pwd, mkdir, rg, cat, sed, nl, Python 3.14.7, setpriv/util-linux 2.42.4, Linux 7.2.8-1-cachyos, R 4.5.3/jsonlite und Node v24.21.0 mit vorhandenem Ajv. Kein Webdownload, Browser, Providerwerkzeug, zweiter Modellanbieter, zusätzliche Agentrolle oder Memoryquelle. Der synchronisierte Skill unslop wurde gelesen und für diesen Bericht angewandt, nicht geändert.

`pnpm check` wurde nicht von mir ausgeführt. Ein vollständiger Build würde gemeinsame Outputs außerhalb meines ausdrücklich erlaubten Ordners erzeugen. Der Koordinator wurde um den nachgelagerten Repositorycheck nach Sammlung unveränderter Berichte gebeten. Technische Fremdchecks sind keine eigenen Checks und keine methodische Abnahme. Keine UI-Änderung, daher kein neuer Desktop-/Smartphone-Browsercheck. Kein Formatter wurde auf gemeinsame oder historische Berichte angewandt. Diese neue Berichtdatei wird nach Abschluss unverändert erhalten.

## Eigene Abschlussartefakte

Alle eigenen Belege liegen in `outputs/loop/software-v2-repro/`. `artifacts.json` bindet die vollständige abgeschlossene eigene Dateiliste und diese Berichtdatei; er hasht sich selbst nicht. Die folgenden Kernhashes wurden beim Berichtaufbau tatsächlich berechnet:

| Artefakt | SHA256 |
| --- | --- |
| `startauftrag.txt` | `ec99cc81e8487f00c5ed731f0f5445d3d66ecc9134e1f77902e24c26ed284a8b` |
| `plan-before-run.md` | `2db410cab53bf2a26c6513f28697641d27d5dfbe4c27d9252b4ab2ccc7faf820` |
| `adaptation.json` | `09fc5716c902fe47a80fc308cc62fbdb12429bf6ae23aeb1728dab5d323eebb2` |
| `input-before.json` | `180ee1b5d744e03de492f465613ccc7366ace8fb4ef2c7a924affcffdbbee0f0` |
| `input-after.json` | `1f76a6c4eb50bba796eb527068c6f20d97221e4c48a38f68edc5ce61f64a493e` |
| `runtime-before.json` | `039af87ebaf71acdb518e8f5bf18d41aa2cc62adbd8ba0efee66a5b8fbbad584` |
| `runtime-after.json` | `deeb3bf8a47e25bd31a0e7bd232601fb531844177d47ecc8c03b78f5c7306fdf` |
| `run-r-correction.py` | `7bd3d86d5d518cfcfd50bda3e0f479cb15314c8748dfb4d4697caaca0bcdda7a` |
| `runtime-probe.R` | `67139761f1af8424ee195aa423c3491c0e2c6dedbdd0ad8abbc3ecd1e0ec4574` |
| `runtime-probe-command.json` | `e7d18531064d3cfaf952e602dc9ffd9815d815d546453e61514478dfc9bd39cd` |
| `runtime-probe-result.json` | `681d3766cea0784ec30a2b4101660e3f78e4b2d2a15674251547d46643c5908c` |
| `check-schema.mjs` | `ec8fc07bf582417e46477d77b8e164707a317a8cef1726375567014d3a229fa8` |
| `schema-countercases.json` | `ab6615aafa3ed8dcda88f9a01526b3c8e70f6ca25266cfbaf525f0b3f14010fe` |
| `check-bindings.py` | `a59a55a069d77f1057d98a77f1a388e99a3a748ce0052de6592c1e4b91e4912f` |
| `bindings-result.json` | `ae5b8feb52ad32d6f455e897d33635eb6dbe4f6fa4e2c16d3129c11ea6dd6aaf` |
| `check-bindings-corrected.py` | `436ef3c0d8bae93ae7f6fd92a0b6781c3025cb1362b849a39f8a8adc4edeec54` |
| `bindings-result-corrected.json` | `98aaa26e0b1d37d5bb703dd1943bbb0c2e62e36fa58bd888677bd90c25924154` |
| `own-check-repair.json` | `ca600f47663613bb4e6d4a69d38ff6dd093a5946a11f17bb765f06e32ec68080` |
| `tool-availability.json` | `82ad9926b4381f4100042d00f6f5e33dfe47afe626793e6b57e9c867a5b865e0` |

## Vollständiger tatsächlicher Startauftrag

```text
Frische unabhängige Nachprüfung von SOFTWARE-001/v2: Reproduzierbarkeit der engen IOCTL-Beschreibungskorrektur und des tatsächlich ausgeführten einzelnen Claude-Protokollfalls. CWD jeder Shell ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Prüfpaket reports/loop/packages/SOFTWARE-001/v2/manifest.json SHA c88656c49ce561b9d57d2e1975ef82dabeb9b745fbefb14cda1e1d415f8a5ddf,18Dateien/123SourceInputs. Lies AGENTS/Auftrag/Issue und SOFTWARE-001-v2-pruefauftrag im Paket. Erlaubte historische Erstberichte SOFTWARE-001-methods.md und -repro.md, Entscheidung/Korrekturbericht. Keine aktuellen v2-Reviewerurteile, FOUNDATION/Juror/PREP-Reviewerberichte, Agentlisten/Findings/Autorenverteidigung außerhalb definiertem Paket. Keine weiteren Agents, keine raw/local/A/B-/Partei-/LR-Antworten. Hash-/Pfadprüfung vor und nach, sichere öffentliche und rein synthetische Quellen; keine unklare Rohquelle zum Hashen öffnen. Originalkernelbelege lesen und launcher/rechte/Descriptor/Supervisor-Grenzen prüfen. Eigene möglichst kleine tatsächliche R-Gegenprobe über neue Kopie/gezielte Anpassung des korrigierten Starts ausschließlich in outputs/loop/software-v2-repro/; bestehende Outputs/Launcher/Runtime niemals überschreiben, R --vanilla unverändertes HOME, genannte child-Dateirechte/NNP, keine Conda-/Install-/Geräte-/Userdatei-/Globalwrites. Nicht behaupten IOCTL komplett kontrolliert oder historischen Außenwrite geheilt. Laufzeit vorhandener Prefix read-only. Historische numerische Tests auf Unverändertheit prüfen, keine unbegründete Wiederholung unveränderter SEM-Pipeline. Tatsächlicher Claude-P01: originalen gebundenen vollständigen Prompt, reine Modellantwort, sanitized execution, Validator und Nachweis lesen. Keine Provider-Envelope stdout/debug/Auth/Financials, keinen neuen Claude-Aufruf. Prüfe tatsächliche Formulierung, IDs/Prüfsummen, Model claude-opus-5-5 vs Nebenmodell, Version2.1.288, Ergebnisse und Grenzen: nur ein erfundener Protokollfall, keine Forschungs-Erstbewertung/Claude-Loader/GitHub-Setup/Menschentest/Neutralitätsgarantie. Eigene Ajv-strict Gegenfälle und wirkliche Hashvergleiche, Modellbericht vs Harnessnachweis unterscheiden. Bericht nur reports/loop/reviews/SOFTWARE-001-v2-repro.md plus eigener Outputordner. Jedes Finding mit genauer Aussage, Fundstelle überprüfbarem Beleg, Wirkung, begründeter Schwere, konkrete Korrektur und Nachprüfung. Tatsächlichen vollständigen Startauftrag unverändert, Modell gpt-6.1-sol ultra geerbt interneRevision/Vorgabenunknown, verfügbare/genutzte Tools und tatsächliche Kommandos/Exit/Grenzen SharedFS dokumentieren. Status BESTANDEN nur ausgeführter konkreter Scope; keine Findingquote. Nicht peerreview/andereFamilie wissenschaftlich. Vollständigen Bericht abschließen, unverändert erhalten und Pfad SHA Ergebnis senden. Kein Commit/Push/Gesamtformatierung.
```
