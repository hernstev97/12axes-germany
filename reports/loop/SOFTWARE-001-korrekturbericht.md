# SOFTWARE-001: begrenzte Korrektur der Ausführungsbeschreibung

Korrekturautor `/root/software001_correction`, 2026-10-03. Codex-Subagent; Laufzeitbezeichnung gemäß gespeichertem Arbeitsloop GPT-6.1-Sol. Interne Modellrevision und interne Anbietervorgaben unbekannt. Dies ist eine Autorenkorrektur nach beiden abgeschlossenen Erstberichten, keine unabhängige Nachprüfung und keine akademische Freigabe.

SOFTWARE-001-REPRO-02 wird vollständig angenommen. Der ursprüngliche Launcher behandelte kein `ioctl-dev`; seine Behauptung einer IOCTL-Sperre war falsch. Der neue Launcher und sein tatsächliches Commandlog beschreiben ausschließlich die konfigurierten Dateirechte und deren Grenzen. Die eigene sichere Runtimeprobe sowie der separate Commandvergleich bestanden. Das Finding ist durch den Autor korrigiert; die unabhängige Nachprüfung der Korrektur bleibt `NICHT_GEPRÜFT`.

Die erhebliche ursprüngliche Setupverletzung SW-ENV-004 / SOFTWARE-M-01 / SOFTWARE-001-REPRO-01 bleibt `NICHT_BESTANDEN`. Dieser Bericht benennt weder den früheren Lauf um noch heilt er dessen Außenwrite. Keine wissenschaftliche Voraussetzung wird hier erfüllt erklärt.

| Gegenstand                                                       | Status                                           | Reichweite                                                                                           |
| ---------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| SOFTWARE-001-REPRO-02                                            | Durch Autor korrigiert; unabhängig NICHT_GEPRÜFT | Begrenzter neuer Launcher und präzise Commandbeschreibung                                            |
| Originale vollständig projektlokale Einrichtung                  | NICHT_BESTANDEN                                  | Tatsächlich dokumentierter ungewollter Außenwrite, Originalbelege erhalten                           |
| Eigene Runtime-/Pfad-/NoNewPrivs-Probe                           | BESTANDEN                                        | Beobachtete Pfade, eigene Sentinels, genau eine verweigerte Manifest-Schreiböffnung                  |
| Tatsächliches Commandlog gegen Vorab-Rechtevektor                | BESTANDEN                                        | Exakter Argumentvektor, zwei Allow-Regeln, explizite Grenzen der Beschreibung                        |
| Gebundene Originaleingaben und Erstberichte vor/nach             | BESTANDEN                                        | Benannte SHA256- und ausgewählte Runtime-Dateivergleiche                                             |
| Neuer numerischer Smoke                                          | IN_DIESER_PHASE_NICHT_ERFORDERLICH               | Numerischer Code/Input unverändert; dieser Korrekturauftrag betrifft nur Ausführungsbeschreibung     |
| Eigener vollständiger Repositorycheck `pnpm check`               | NICHT_GEPRÜFT                                    | Gemeinsame Buildoutputs liegen außerhalb des erlaubten Schreibbereichs; beim Koordinator angefordert |
| ESS-, Modell-, Plan-, andere Modellfamilien- und Releaseabnahmen | NICHT_GEPRÜFT                                    | Ihre Voraussetzungen und bestehenden Gates bleiben unverändert                                       |

## Grundlage, Rolle und Originalerhaltung

Grundlage ist `reports/loop/packages/SOFTWARE-001/v1/manifest.json`, SHA256 `126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e`, Paket-Codecommit `0beba4738d8c0059c2b2709ae34bc9f6390a3fc8`. Die acht eingefrorenen Dateien sind maßgeblich; die 79 SourceInputs sind separat gebunden. Die beiden Erstberichte wurden vollständig gelesen, nachdem sie abgeschlossen waren. Der Autor verwendet sie zur Fehlerbearbeitung und gibt diese Lektüre nicht als unabhängiges Review aus.

Gelesen wurden aktuelle und eingefrorene AGENTS, der vollständige eingefrorene Dauerauftrag und LIFE-93, der SOFTWARE-001-Prüfauftrag, das vollständige Manifest, die vorgeschriebenen Projekt-/Prüfregel-/Analyseplan-/Beleg-/Entscheidungsdateien, Arbeitsloop und Lizenzregeln, beide SOFTWARE-001-Erstberichte, Originallauncher und Scoped-Environment, gebundene ursprüngliche Vorher-/Nachher- und Außenwrite-Belege, Lock sowie die unten genannten Originalquellen. Loopzustand und andere Reviewerberichte wurden aufgrund des begrenzten Korrekturauftrags nicht geöffnet.

Alle Shellaufrufe verwendeten ausdrücklich `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003` als cwd. Branch bei der Ausgangskontrolle war `research/life-93-night-20261003`; vorhandene Änderungen an gemeinsamen Zustandsdateien blieben unberührt. Neue Dateien liegen nur in `outputs/loop/software-correction/` und dieser Berichtdatei. Originalquellen, Launcher, Logs, numerische Skripte/Inputs, eingefrorene Dateien und Erstberichte wurden nicht überschrieben oder formatiert. Kein Commit, Push, Merge, Deployment oder zusätzlicher Agent.

Die anfängliche Dateiinventarsuche und ein gebündelter Leseaufruf erzeugten abgeschnittene Toolausgaben. Die maßgeblichen Dokumente, beide vollständigen Erstberichte und das Manifest wurden anschließend gezielt ohne abgeschnittene Ausgabe gelesen. Die leichte Memory-Registrysuche ergab keinen Treffer und Exit 1; es wurde kein Befund aus Memory übernommen. Die ersten rein lesenden Orientierungsaufrufe und `apply_patch`-Vorbereitungen sind im Tooltranskript nachvollziehbar, aber ihre UTC-Zeit wurde nicht zusätzlich in einem lokalen Kommandolog erfasst. Der Vorhersnapshot ist deshalb ausdrücklich ein Snapshot vor dem R-Lauf, kein rückwirkender Nachweis über den allerersten Zugriff oder sämtliche PC-Änderungen.

## Angenommenes Finding und selbst geprüfte Originalfundstellen

Die betroffene Originalaussage steht in `outputs/loop/software-author/run-r-direct.py:48,55`: Der Kommentar und die erzeugte Metadatenbeschreibung versprechen eine IOCTL-Grenze. Der tatsächliche Rechtevektor in Zeilen 38–39 und in den gebundenen finalen Commandlogs enthält kein `ioctl-dev`. Der unveränderte Originallauncher hat SHA256 `0da51b3c55476e0b0a166c042d4c1b52270e5a673d4ecddb6b533592c3ce0ee5`; `scoped-env.json` hat SHA256 `455d22cf4273d80b027e69377680c7c54e4b335fbd9888ceb3193511d25e44ed`. Vor dem eigenen R-Start las der neue Launcher beide Originaldateien erneut vollständig und verifizierte diese Bindung.

Die gebundene [offizielle Linux-Kerneldokumentation](https://docs.kernel.org/userspace-api/landlock.html), lokale Datei `outputs/loop/software-author/sources/linux-landlock.html`, SHA256 `1c258549336d01df7163ef551674b314c9e6b81ae4b9f26c3b4d80336ab87875`, wurde an den Originalstellen selbst gelesen. Zeilen 1029–1037 erklären die explizit behandelten Rechte und die historische REFER-Ausnahme. Zeilen 1228–1242 erklären die Durchsetzung auf dem aufrufenden Thread und die NoNewPrivs-Voraussetzung. Zeilen 1363–1377 nennen IOCTL_DEV gesondert und begrenzen seine Wirkung auf neu geöffnete Geräte; vorhandene Deskriptoren bleiben eine Grenze. Das Originalregister dokumentiert den ursprünglichen Abruf am 2026-10-03 um 03:40:20.630865 UTC. Hier wurden die gebundenen Bytes gelesen, kein neuer Webstand abgerufen.

Die gesamte gebundene lokale `setpriv-2.42.4-local-manual.txt`, SHA256 `64235fe477c56e490266ee037b387ba6329a12b4e92e53b5802052da14819d4b`, wurde selbst gelesen. Zeilen 73–83 erklären NoNewPrivs und Vererbung; Zeilen 136–164 unterscheiden behandelte Kategorien von erlaubten Teilrechten. Zeilen 197–198 nennen den Fehlerausgang 127, wenn eine Option nicht angewandt werden kann. Das Originalregister nennt den lokalen Abruf 03:40:20.687450 UTC. Die tatsächlich installierte Version wurde zusätzlich lesend mit `setpriv --version` geprüft.

Für die unveränderte erhebliche Setupverletzung wurden die gebundenen Conda-26.5.2-Originalquellen ebenfalls gelesen: `conda-core-path_actions.py:1132–1155` ruft `touch` in `verify()` auf; `conda-core-envs_manager.py:26–52` setzt den `register_envs`-Guard erst in `register_env`. Die gebundenen historischen Snapshots dokumentieren die vorher fehlende und nachher leere `~/.conda/environments.txt`. Die Elternverzeichnis-Neubildung ist über dokumentierte Birth-Zeiten gestützt; dessen Existenz wurde im damaligen Vorhersnapshot nicht unmittelbar beobachtet. Keine Benutzerdatei wurde für den neuen Gegenfall geöffnet und keine Außenbereinigung vorgenommen.

Der Fehlergrad von REPRO-02 bleibt mittel. Die unzutreffende Schutzbehauptung ist belegt, eine schädliche Geräteoperation ist nicht beobachtet. Die bereits reproduzierten numerischen Befunde werden durch diesen Beschreibungsfehler nicht widerlegt. Maßgeblich sind Originalcode, tatsächlicher Rechtevektor und Dokumentation, keine Mehrheit der Reviewer.

## Neue begrenzte Ausführung und eigener Vorabplan

Der [Vorabplan](../../outputs/loop/software-correction/plan-before-run.md), SHA256 `215343e17af44a23fa7eb48ecdee59f9b49a0b7a7a2fceac080002824dca811a`, entstand vor der Runtimeprobe und wurde im Startlog gebunden. Der neue [Launcher](../../outputs/loop/software-correction/run-r-correction.py) ist eine getrennte Korrekturfassung. Der ursprüngliche Launcher wurde hier nicht ausgeführt. Es gab kein Conda, keinen Installer, keine Paketinstallation und keinen Umgebungsneuaufbau.

Der Kindprozess startet ausschließlich das vorhandene direkte `outputs/loop/software-env/envs/r-smoke/bin/Rscript --vanilla`. Rscript-SHA256 vor und nach: `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`. Seine behandelten Dateirechte sind wörtlich:

```text
write-file,remove-dir,remove-file,make-char,make-dir,make-reg,make-sock,make-fifo,make-block,make-sym,refer,truncate
```

Genau eine Allow-Regel erlaubt diese Rechte unter `outputs/loop/software-correction/`. Eine zweite erlaubt ausschließlich `/dev/null:write-file`. Es gibt keine Regel für den Autorenordner, den bestehenden Umgebungspfad, den Bericht oder einen Benutzerpfad. HOME blieb `/home/stevenh`. TMP/TEMP/TMPDIR, XDG Cache/Data/Config, R-Cache und Historienpfad liegen im eigenen Ordner. Die vorhandenen Paketbibliotheken sind Lesepfade.

Der vollständige tatsächliche Argumentvektor mit dem absoluten Rscript-/Skriptpfad, cwd, sicher ausgewählten Environmentwerten, Start-/Endzeit und Exitcode steht in [runtime-probe-command.json](../../outputs/loop/software-correction/runtime-probe-command.json). Seine Kontrolle vergleicht die gespeicherte Ausführung mit einem separat ausgeschriebenen Sollvektor aus dem Vorabplan; sie importiert die Launcherdefinition nicht. Alle 15 darin benannten Kriterien bestanden. Die Kontrolle ist eine Autorenprüfung und keine unabhängige Sicherheitsabnahme.

Die Beschreibung sagt ausdrücklich, dass ausschließlich die aufgeführten Dateirechte behandelt werden. Lesen, Ausführen und unaufgeführte Rechte werden dadurch nicht vollständig kontrolliert. Geerbte Deskriptoren bleiben eine Grenze. Hier ist stdin eine Pipe mit leerem Input; stdout und stderr gehen in das eigene Log. `close_fds=True` ist keine Behauptung, alle möglichen Deskriptorwirkungen seien geprüft.

Der Python-Supervisor läuft außerhalb der Landlock-Regel seines R-Kindprozesses. Seine Schreibpfade folgen dem gelesenen eigenen Code; die Shell-/Agentwerkzeuge haben keine vollständige technische Isolation auf diesen Ordner. Netzwerk, Geräte und IOCTLs werden nicht vollständig kontrolliert. `ioctl-dev` ist weder konfiguriert noch getestet. Kein absichtlicher Geräte-IOCTL-Test fand statt. Es gibt keine vollständige Syscall-Aufzeichnung, Dateisystembeobachtung oder Sicherheitsgarantie für den PC.

## Tatsächliche Probe und Rechenreichweite

Der R-Kindprozess lief von `2026-10-03T04:36:47.310868+00:00` bis `2026-10-03T04:36:47.475091+00:00` mit Exit 0. [runtime-probe-result.json](../../outputs/loop/software-correction/runtime-probe-result.json) und das Log enthalten die tatsächlich beobachteten Werte. Die Probe bestätigte `R version 4.5.3 (2026-03-11)`, `NoNewPrivs=1`, `CapEff=0000000000000000`, eigenes cwd/tempdir sowie R_HOME und beide Bibliothekpfade im vorhandenen Projektpräfix. Eigene Profile-/Renviron-Sentinels wurden ignoriert; R_PROFILE_USER und R_ENVIRON_USER waren im `--vanilla`-Prozess leer. Ein fester eigener Testtext wurde ausschließlich im eigenen Ordner gespeichert.

Der einzige neue Öffnungsgegenfall war `file(<eingefrorenes Projektmanifest>, open="r+b")`. Er ist nichttrunkierend. Die Öffnung wurde mit `Permission denied` verweigert; die Verbindung kam nicht zustande. Es wurde kein Inhalt geschrieben oder für diese Probe gelesen. Der Manifesthash blieb `126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e`. Wäre die Öffnung erlaubt gewesen, hätte das Skript die Verbindung ohne Schreiboperation geschlossen und die eigene Abnahme zurückgewiesen. Eine Benutzerdatei wurde hierfür nicht geöffnet.

Es wurden weder numerischer CFA-Code noch synthetischer Input verändert und keine neue numerische Rechnung ausgeführt. Die gebundenen numerischen Artefakte blieben byteidentisch. Die vorhandenen Erstberichte behalten ihre enge Reichweite; sie werden nicht als neue Korrekturtests ausgegeben. Vollständige ESS-Designfähigkeit, fitted Invarianzfolge, Reliabilitäts-/Unsicherheitsvalidierung, EFA und wissenschaftliche Gates erhalten durch diese Korrektur keinen positiven Status.

## Ausgeführte Schritte, Zeit und Werkzeuge

Die lesende Orientierung und Vorabplan-/Codeerstellung ging den folgenden aufgezeichneten Schritten voraus. Drei Python-Dateien wurden zunächst mit `compile()` ohne Bytecode-Ausgabe syntaktisch geprüft, Exit 0. Eine Quellenfundstelle der setpriv-Fehlerregel wurde vor Ausführung von 207–209 auf die tatsächlich gelesenen Zeilen 197–198 präzisiert; es war kein Fehlversuch der Runtimeprobe. Alle nachstehenden Checkschritte wurden einmal ausgeführt.

| Schritt         | UTC-Intervall                                                         | Exit |
| --------------- | --------------------------------------------------------------------- | ---- |
| `before`        | 2026-10-03T04:36:40.531184+00:00 bis 2026-10-03T04:36:40.745396+00:00 | 0    |
| `sources`       | 2026-10-03T04:36:40.807458+00:00 bis 2026-10-03T04:36:40.871805+00:00 | 0    |
| `runtime-probe` | 2026-10-03T04:36:47.287169+00:00 bis 2026-10-03T04:36:47.501410+00:00 | 0    |
| `check-command` | 2026-10-03T04:36:53.135467+00:00 bis 2026-10-03T04:36:53.167533+00:00 | 0    |
| `after`         | 2026-10-03T04:36:53.199383+00:00 bis 2026-10-03T04:36:53.413699+00:00 | 0    |

Aufruf jeweils `python -B outputs/loop/software-correction/run-step.py <schritt>`. Die einzelnen `step-*-command.json` und `step-*.log` speichern die vollständigen tatsächlichen Kindaufrufe, cwd, Intervalle, Exitcodes und Ausgabe. Das innere setpriv-/R-Kommando steht zusätzlich ungekürzt im Runtime-Commandlog. Die versionsermittelnden Leseaufrufe `setpriv --version`, `uname -sr`, `python -B --version` und ihre Intervalle/Exitcodes liegen in `sources-reviewed.json`; alle endeten mit Exit 0.

Tatsächlich genutzte Agentwerkzeuge waren `functions.exec` mit `exec_command` und `apply_patch`, außerdem `collaboration.send_message` an den Koordinator. Lokale Werkzeuge waren Bash, `rg`, `cat`, `sed`, `nl`, Python 3.14.7, setpriv from util-linux 2.42.4, Linux 7.2.8-1-cachyos und R 4.5.3 mit dem vorhandenen jsonlite für JSON-Ausgabe. Der bestehende Node-/Prettier-Aufruf formatiert ausschließlich diese neue Berichtdatei; sein eigener Command-/Exitbeleg liegt im Korrekturordner. Der Skill `unslop` wurde gelesen und angewandt, nicht verändert. Kein Browser, Webdownload, anderer Modellanbieter oder zusätzliche Agentrolle. Der genaue interne Modellstand wurde nicht durch eine Anbieterabfrage verifiziert.

`pnpm check` wurde vom Korrekturautor nicht ausgeführt. Der begrenzte Schreibauftrag erlaubt keine gemeinsamen Build-/Websiteoutputs. Der Koordinator wurde vor der Ausführung um den nachgelagerten Repositorycheck gebeten. Eine ausgelassene Prüfung ist hier NICHT_GEPRÜFT; ältere erfolgreiche Checks bleiben Fremdbelege für ihre damaligen Fassungen. Keine UI-Änderung und kein neuer UI-Browsercheck.

Die gezielte Formatierung der neuen Berichtdatei verwendet das vorhandene Prettier 3.8.1 direkt ohne pnpm-Aufruf. Der Formatter erhält eine eigene Kindprozess-Dateigrenze für den Korrekturordner und ausschließlich `write-file,truncate` auf dieser Berichtdatei; die R-Laufzeitregeln bleiben unverändert. Der Formatbeleg nennt Vorher-/Nachherhash, tatsächliche Aufrufe, UTC-Intervalle und Exitcodes. `report-generation.json` bewahrt den Hash der ursprünglichen generierten Fassung vor dieser gezielten Text-/Formatbearbeitung; der neue Abschlussmanifest bindet die endgültige Fassung.

## Hashbindung und neuer Reviewumfang

[input-before.json](../../outputs/loop/software-correction/input-before.json) und [input-after.json](../../outputs/loop/software-correction/input-after.json) erfassen jeweils 97 Pfadprüfungen: acht Freeze-Dateien, acht Worktree-Spiegel, 79 SourceInputs und beide abgeschlossenen Erstberichte. Alle gebundenen Sollhashes passen; alle benannten Dateien sind vor/nach identisch. Zusätzlich stimmen 61 Runtime-Dateien mit dem gebundenen Lock überein und blieben unverändert: Rscript sowie die jeweils 30 Dateien der lavaan-/semTools-Bäume. Die Regeldateien sind separat als benannte Kontrollinputs erfasst. Dies ist kein vollständiger Systembibliotheken- oder Neuaufbaunachweis.

| Unveränderter Erstbericht                      | SHA256                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------ |
| `reports/loop/reviews/SOFTWARE-001-methods.md` | `ca760060394771edee9ba9b11dd69985dc84133bcd14216314e32d7eb667a802` |
| `reports/loop/reviews/SOFTWARE-001-repro.md`   | `6ba249b8423e74d4afb778d01eeb702207f284ce8f8563039ef8e31740b04ac0` |

Die neue Fassung wird mit `outputs/loop/software-correction/review-package-manifest.json` eingefroren. Dieser Abschlussmanifest enthält alle eigenen Belege einschließlich Generator-/Schrittdateien, ihren Bytes/SHA256 und dem finalen Berichtshash. Er verweist auf das unveränderte SOFTWARE-001/v1 und die Vorher-/Nachherbindungen; er hasht sich selbst nicht. Sein eigener Hash wird dem Koordinator nach dem Freeze gemeldet. Eine Hashfestschreibung ist keine unabhängige Nachprüfung.

| Eigenes Kernartefakt             | SHA256                                                             |
| -------------------------------- | ------------------------------------------------------------------ |
| `plan-before-run.md`             | `215343e17af44a23fa7eb48ecdee59f9b49a0b7a7a2fceac080002824dca811a` |
| `startauftrag.txt`               | `d37f01c34d2e1a74a55ab0bbcb0af1cf3538e07efba1f2063a19ebdc1a391b6b` |
| `run-r-correction.py`            | `8076ba0b236766d81178dca16e995894f3f1efb50a65f382dec4b720457d692b` |
| `runtime-probe.R`                | `5ac1b8235a172cf5f36e8f305f161ce05ea24c68c2337dd77998f830fb3dbf3b` |
| `profile-sentinel.R`             | `ea8617728055a8b844faa650d7a78fb2d1701b211e5fdb37696e3e6b611765bd` |
| `Renviron-sentinel`              | `ac3623c7d8421dc1d773587ef8a7ca621baea4ff09579516bef4424ce264d7ac` |
| `evidence.py`                    | `e5e7d3b966f7f59558714a2f4f1aa83e693d1a8dfb1c80845c2585286a319816` |
| `run-step.py`                    | `fe2d10af0681e08edc34533120645a40bf467f47efe197569781fdb5013c95b8` |
| `input-before.json`              | `07becb1302ec60ca944a0341fd7c764eaff7defc8f9dbde1f75b6f076ed75e01` |
| `input-after.json`               | `9590a1f92f57a0d9f5d8a36f1d6eeb7e3e2a33af1e9c23d1a0184c054958d2fb` |
| `sources-reviewed.json`          | `a7e249d74720aeb7b1912b860945776e1e4a1f74ed3fcaa58259a72590bd6d35` |
| `runtime-probe-command.json`     | `2c61b4a2135adb1416b5d396e06b734563748c5a7c1703964087f3de2fd86dbe` |
| `runtime-probe-result.json`      | `ef5300198288e95620a514ec2edf375dcd88ad62940f5658c847ed9b0c1364b2` |
| `runtime-probe.log`              | `2a018aa940eda28678d0fef0ef53ae8b23f30047c854d6c2b0b8e9046aefd3ce` |
| `command-description-check.json` | `682d621ace1893531ea4a5dc472dc023562baf18872779e8fd65599d4d2b9251` |
| `owned-runtime-probe.txt`        | `522133df8fbc324528436646b60bef2f55e9a0f3f9706573f9e258749bb5ac82` |
| `generate-report.py`             | `948701e969a7cb61606a78d87493f47e37ad92cce55a16cb590deecaf503b5d1` |

Der neue Review soll die Annahme von REPRO-02, den tatsächlichen begrenzten Launcher/Commandtext, Originalfundstellen, Probe und Hasherhaltung gegenprüfen. Der Status bis dahin bleibt durch Autor korrigiert / unabhängig NICHT_GEPRÜFT. Die erhebliche ursprüngliche Einrichtung bleibt NICHT_BESTANDEN; wissenschaftliche und andere Modellfamilien-Abnahmen bleiben offen.

## Vollständiger tatsächlicher Startauftrag

```text
Du bist begrenzter Korrekturautor SOFTWARE-001 nach Abschluss beider unabhängigen Erstberichte, kein Reviewer. Shell-CWD /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Lies AGENTS, Auftrag/Issue, eingefrorenes SOFTWARE-001/v1 Manifest SHA126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e, beide abgeschlossenen reports/loop/reviews/SOFTWARE-001-methods.md und SOFTWARE-001-repro.md vollständig sowie originale gebundene Kernel-/setpriv-Quellen. Der Koordinator nimmt SOFTWARE-001-REPRO-02 voll an (mittel): IOCTL-Verbot nicht konfiguriert, kein schädlicher IOCTL beobachtet; ursprüngliche Setupverletzung SW-ENV-004/SOFTWARE-M-01/REPRO-01 bleibt NICHT_BESTANDEN. Erstelle nachvollziehbare begrenzte Korrekturfassung: eigenen neuen Launcher unter outputs/loop/software-correction/ mit Schreibrechten ausschließlich eigenen Ordner+dev/null, direkte bestehende Rscript--vanilla-Laufzeit, HOME unverändert, keine Conda/Installation/globalen oder user Writes/keine Rechteausweitung. Vorhandene Originallauncher/-logs/Reports und eingefrorene Inputs NICHT ändern. Keine zusätzliche Gerätesperre versprechen/konfigurieren: korrigiere Beschreibung auf tatsächlich behandelte Dateirechte, unlisted/Readdescriptors/supervisor/keine Netzwerk-/Geräte-/IOCTL-Vollkontrolle ausdrücklich begrenzen. Eigene präzise Vorabkriterien vor Ausführung, kleiner sicherer Runtime/NoNewPrivs/Pfad-Check und nichttrunkierender Öffnungs-Gegenfall am eingefrorenen Projektmanifest (keine Benutzerdatei öffnen), tatsächliches generiertes Commandlog gegen rights-Vektor kontrollieren. Keine Geräte-IOCTLs ausführen. NumericSmoke braucht nur erneut laufen, falls numerischer Code/Input tatsächlich geändert wird (nicht beauftragt). SOURCE/Input hashes vor/nach, vollständige Schritte/Zeiten/Exit/Tools/Modelle/Grenzen sichern. Schreiben nur outputs/loop/software-correction/ und reports/loop/SOFTWARE-001-korrekturbericht.md; Bericht schließt Finding nur als durch Autor korrigiert/unabhängig noch NICHT_GEPRÜFT, wissenschaftliche Gates unverändert. Keine andere Reviews/Forschung/Website/Loopstate, ESS/Rohantworten/A/B/Partei/LR, Credential/Cookies/Portal-Analysis, neue Agents/Commit/Push. Vollständigen tatsächlichen Startauftrag wortgetreu im Bericht. Erhebliche ursprüngliche Setupverletzung weder umbenennen noch heilen. Originalquellen selbst prüfen, kein Mehrheitsbeweis. Abschluss vollständiger neuer korrigierter Bericht und eindeutige Belegliste/Hashes für ein neues eingefrorenes Reviewpaket.
```
