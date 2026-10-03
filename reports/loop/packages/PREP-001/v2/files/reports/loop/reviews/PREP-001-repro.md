# PREP-001: unabhängiger Erstbericht zu Reproduzierbarkeit, Zugriff und Datenschutz

Erstprüfung am 2026-10-03 im Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Geprüft ist ausschließlich PREP-001/v1 mit Manifest-SHA256 `152785d06f322a1e95b6503b9b78ed2ff768373852899f4f027ab7f2c6add66a`. Dieser Bericht erteilt keine Gesamtfreigabe, Setup-Abnahme, wissenschaftliche Validierung oder Phase-9-Abnahme.

Die zwölf eingefrorenen Dateien und das bezeichnete öffentliche SourceInput stimmen vor und nach den synthetischen Prüfungen mit ihren Prüfsummen überein. Die öffentliche Originalseite bestätigt die beiden deutschen Sampling-Domänen. Zwei Vorbereitungsregeln brauchen eine Korrektur: die Wiederholung des Verständnistests nach bedeutenden Änderungen und die maschinelle Zurückweisung unbelegter beziehungsweise widersprüchlicher Urteile.

## Prüfumfang und Status

| Geprüfter Umfang | Status | Tatsächlicher Befund |
| --- | --- | --- |
| Manifest, zwölf eingefrorene Dateifassungen und öffentliches SourceInput | BESTANDEN | Alle Hashes und Bytezahlen stimmen vor und nach den Tests. |
| Verständnistest: echte Menschen, fünf feste Fragen, spätere Beispielregel, Schlüssel und Releasebindung, Datenschutzvorgaben | BESTANDEN | Als vorbereitende Regeln vorhanden. Keine Menschen oder Ergebnisse erfunden. Keine praktische Durchführung behauptet. |
| Verständnistest: verbindliche Wiederholung mit Menschen nach bedeutenden Änderungen | NICHT_BESTANDEN | Im ausgeführten Dokumentabgleich fehlt die verlangte Regel. R-F01. |
| Deutsche Designmetadaten: zwei Domänen, Zielpopulation und Zeitbezug an der Originalseite | BESTANDEN | Eigene öffentliche Portal-Lektüre. Die Sampling-Aussagen sind getragen; die Zielpopulation und Zeitgrenzen stehen im gebundenen SourceInput. |
| Rohvariablenzuordnung, Einschlusswahrscheinlichkeiten, Split-, Varianz- oder Softwareentscheidungen | NICHT_GEPRÜFT | Die gelesene Zusammenfassung liefert diese Festlegungen nicht. Keine Antwortdaten oder Header geöffnet. |
| Skill: Textregeln für Manifest, Quellen, Trennung der Erstbewertungen, Status und Findings | BESTANDEN | Die Regeln unterscheiden Erstbewertung und PR-Review und verlangen fehlende Prüfungen offen zu halten. |
| Drei harmlose synthetische Codex-Protokollfälle | BESTANDEN | Fehlendes Manifest, fehlende Originalquelle und kontaminierte Erstbewertung führten zu Sperre beziehungsweise offener Quellenprüfung. Kein Claude-Lauf. |
| Schema: Kompilierbarkeit, Pflichtfelder, Hashsyntax und fünf Statuswerte | BESTANDEN | Vorhandene Ajv 8.20.0, Draft 2020-12, strikt kompiliert; Positiv- und Struktur-Negativfixtures ausgeführt. |
| Schema: nachprüfbare Mindestbelege und Widerspruchsschutz für BESTANDEN | NICHT_BESTANDEN | Ausgeführte Randfälle werden trotz fehlender oder widersprüchlicher Mindestbelege angenommen. R-F02. |
| Tatsächliche Claude-Skill-Ausführung und getrennte Prüfung durch andere Modellfamilie | NICHT_GEPRÜFT | Kein Claude-Aufruf durch diesen Reviewer. Codex-Protokollfälle ersetzen diese Prüfung nicht. |
| Vollständige GitHub-App-/Workflow-/Pflichtcheck-Abnahme | BLOCKIERT | Im Paket ausdrücklich offen; weder eingerichtet noch live geprüft. Frühere Zugriffslogs sind keine aktuelle Setup-Abnahme. |
| Modellfreigabe, reale ESS-Analyse, fünf menschliche Antworten und Release | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Für dieses Vorbereitungspaket nicht erwartet. Die späteren Voraussetzungen bleiben unerfüllt beziehungsweise ungeprüft. |
| Technischer Repository-Check | BESTANDEN | `pnpm check`, Exit 0; Format, Handbuch, Typen, neun Tests und Build bestanden. Keine methodische Aussage daraus. |

## Auftrag, Laufzeit und Trennung

Ich erhielt die folgende vollständige konkrete Reviewer-Aufgabe. Weder andere Erstberichte noch eine Autorenverteidigung oder der vorherige Dialog wurden als Prüfeingabe gelesen:

> Du bist unabhängiger PREP-001-Erstprüfer (Reproduzierbarkeit/Sicherheit/Datenschutz). Arbeite ausschließlich im Zielworktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Lies zuerst AGENTS.md und unslop SKILL dort. Gemeinsame Forschungs-/Vorbereitungsdateien nicht verändern. Schreibe ausschließlich deine eigene Datei reports/loop/reviews/PREP-001-repro.md sowie eigene öffentliche/synthetische Belege unter outputs/loop/prep-repro/. Andere Reviewerberichte, Autorenverteidigung und Dialoghistorie NICHT lesen. Dein Prüfpaket reports/loop/packages/PREP-001/v1/manifest.json SHA256 152785d06f322a1e95b6503b9b78ed2ff768373852899f4f027ab7f2c6add66a; darin alle zwölf Dateien und ein öffentlicher SourceInput. Anforderungen aus eingefrorenem LIFE-93/mandat und reports/loop/preparation-pruefauftrag.md lesen. Prüfe ALLE drei Entwürfe unabhängig: (1) Phase9-Verständnistestprotokoll: wirkliche fünf Menschen, feste fünf Fragen, fiktives Beispiel noch nicht erfunden, Antwortschlüssel/Releasebindung vor Versand, Datenschutz und Korrekturregeln; keine Simulation als menschliches Ergebnis. (2) Deutsche Designmetadaten: Original-Portal selbst lesen und Behauptungen/fehlende Details/mischdesign/zeitliche Grenzen kontrollieren, keine Rohdaten öffnen. (3) .claude Review-Skill samt JSONschema: Format/Reviewgrenzen, Erstbewertung versus PR-Review, fehlende Manifest-/Quellen-/Modellbelege, Bestanden-Status, tatsächliche Executability und Zugriffsrisiken. Führe drei harmlose synthetische Protokollfälle aus: fehlendes Manifest, unzugängliche Quelle, kontaminierte Erstbewertung. Das sind Codex-Protokolltests, NICHT Claude-Verhalten oder echte andere Modellfamilienprüfung. Prüfe Schema mit passenden Positiv-/Negativfixtures soweit Werkzeuge verfügbar, keine Installation globaler Software. Zugriffsregel: keine data/raw, data/local, B, Partei-/Linksrechtswerte, IDs, politischen Antworten, Cookies, Credentials oder fremden Dateien lesen. Browser für öffentliche Quellen zuerst T3 preview_status, bei geschlossenem preview_open, eigene Tab-ID behalten; keine Cookie-Werte. Keine Nachrichten an Personen, CI/GitHubSetup/Publikation, Skilländerung oder Commit. Dokumentiere tatsächlichen vollständigen Auftrag, Modellslug gpt-6.1-sol/ultra sofern tatsächlicher Runtime bestätigt, Werkzeuge/Beleg-Hashes/Trennungsgrenzen. Finding nur belegt, genaue Aussage+Fundstelle+Problem+Auswirkung+Schwerebegründung+Korrektur+Nachprüfung; offene Fragen kennzeichnen, kein Sollfehleranteil. Status BESTANDEN/NICHT_BESTANDEN/NICHT_GEPRÜFT/BLOCKIERT/IN_DIESER_PHASE_NICHT_ERFORDERLICH mit konkretem Prüfumfang, keine Gesamtfreigabe. Alle zwölf Hashes vor/nach prüfen. Original Erstbericht nach Abschluss nicht ändern. Sende fertigen Bericht mit SHA256.

Ausführung durch den tatsächlich beauftragten Codex-Subagent. Der Auftrag nennt `gpt-6.1-sol/ultra` unter der Bedingung einer Laufzeitbestätigung. Eine unabhängig auslesbare Modell- oder Reasoning-Metadatenquelle stand mir nicht zur Verfügung. Daher sind konkreter Runtime-Slug, Effort und interne Revision hier nicht bestätigt. In den synthetischen Ergebnissen bleibt `model` null; die Auftragsangabe steht ausdrücklich getrennt davon. Nicht zugängliche interne Anbietervorgaben sind unbekannt. Dieser Bericht beschreibt ein KI-Audit, keine Fachbegutachtung.

Genutzt wurden `functions.exec`, die dort angebotenen `exec_command`, `apply_patch` und `write_stdin`, Python-Standardbibliothek, `rg`, Node.js, die bereits installierte Ajv 8.20.0, `pnpm check`, T3 `preview_status`/`preview_open`/`preview_snapshot`/`preview_evaluate` und `web.run` für öffentliche Originaldokumentation. Kein Werkzeug oder Softwarepaket wurde installiert. Verfügbare Shell-, Datei- und Netzwerkkapazitäten wurden durch diese Aufgabenregel begrenzt; sie waren keine technische Sandbox. Der Skill stellt das selbst klar.

Nach dem ersten T3-Status wurde ein eigener Tab `tab_e` mit `reuseExistingTab:false` erzeugt. Interaktionen betrafen ausschließlich Country documentation > Germany > Details sowie Universe, scope and method. Kein Login, Datafile, Analysebereich oder Cookie-Aufruf. Ein anfänglicher Snapshot lieferte automatisch Browserdiagnostik einschließlich einer Tracking-Request-URL. Ich habe diese weder ausgewertet noch in Belege oder Bericht übernommen. Danach wurden nur sichtbare öffentliche Metadatentexte gezielt ausgelesen. Die eigene Portaldatei enthält keine solchen Browserdiagnostikdaten.

Die Zugriffsgrenze gegenüber Rohdaten und fremden Erstberichten wurde eingehalten. Gelesen wurden das eingefrorene Paket, das ausdrücklich freigegebene öffentliche SourceInput, die von AGENTS verlangten allgemeinen Projektregeln und die eigenen synthetischen Dateien. Die leichte Suche im Memory-Register lieferte keinen Treffer; daraus wurde kein Sachbefund übernommen. Es gab keine Nachrichten an Menschen, Kontoeinrichtung, Veröffentlichung, GitHub-Mutation, Skilländerung oder eigenen Commit. Der Repository-Check erzeugt seine üblichen ignorierten Build-/Cacheartefakte, keine Änderungen an gemeinsamen Forschungsdateien.

## Nachweise zu den drei Gegenständen

Alle nachfolgenden Dateifundstellen meinen die Kopie unter `reports/loop/packages/PREP-001/v1/files/`, soweit nicht ausdrücklich ein eigener Belegpfad genannt wird. Das Paket bindet den Vollauftrag, den Issue-Stand vom 2026-10-03 und den vorab formulierten Prüfauftrag. Die Prüfung wählt keine Items, Namen, Dimensionen oder Verfahren aus.

### Verständnistest

`docs/verstaendnistest.entwurf.md:3–9` hält Phase 9, konkrete Beispielwerte und menschliche Antworten offen. Die Beispielregel entspricht LIFE-93:174. Die fünf Fragen in Zeilen 19–23 decken die Inhalte aus LIFE-93:205 ab. Die Ergänzung für eine Seite ohne angezeigten Bereich wahrt die bereits vorgesehene Möglichkeit fehlender tragfähiger persönlicher Unsicherheitsintervalle in LIFE-93:143; sie erfindet kein Intervall.

Der Schlüssel soll vor Versand mit Fragen, Beispiel und Release-Manifest eingefroren werden, Zeilen 29–31. Der Entwurf verlangt zwei getrennte Bewertungen und dokumentierte Uneinigkeit. Er erklärt Einigkeit nicht als Verständnisbeleg. Die 2-von-5-Regel verlangt dieselbe konkrete Fehlinterpretation; einzelne erhebliche Fehler und jede Unklarheits-/Einseitigkeitskritik werden ebenfalls geprüft, Zeilen 33–35. Fehlende Antworten zählen nicht als Zustimmung.

Die Einladung nennt die Veröffentlichung ohne Namen. Zeilen 25 und 39–41 begrenzen die Eingaben auf die Beispielseite, schließen politische Eigenprofile aus und verlangen Redaktion sowie Inhaltsprüfung vor Veröffentlichung. Das ist ein zulässiger vorbereitender Schutz, keine bereits bewiesene Anonymisierung. Für den späteren Lauf müssen auch indirekt identifizierende Freitexte entfernt werden und die redigierte Antwortfassung mit der Bewertung verbunden bleiben. Ob die konkreten Antworten dann veröffentlichbar sind, ist heute NICHT_GEPRÜFT. Es wurden keine Antworten erhoben oder Nachrichten versandt.

Der Abschluss enthält eine neue Textversion, unabhängige Prüfung und Stevens Freigabe. Die ausdrücklich verlangte erneute Prüfung mit Menschen nach bedeutenden Änderungen fehlt jedoch. Sie wird durch einen KI-Review nicht erfüllt. Siehe R-F01.

### Deutsche Designmetadaten

Am 2026-10-03 um 03:02:59 UTC habe ich den [Deutschland-Dialog des ESS-Portals](https://ess.sikt.no/en/study/412db4fe-c77a-4e98-8ea4-6c19007f551b) selbst gelesen. Der eigene Beleg `outputs/loop/prep-repro/portal-independent.json` hält Sampling und den Länder-/Zeitkontext fest. Das Portal nennt Melderegister als Frame. Die 15 größten Gemeinden bilden die erste Domäne; dort erfolgt systematische, ungeclusterte Individualauswahl mit proportionaler Schichtung nach Gemeinde. In der übrigen Bundesrepublik werden 166 Gemeinden als PSUs proportional zur Zahl der Menschen ab 15 gewählt, danach jeweils gleich viele Individuen zufällig ausgewählt. Die pauschale Portal-Kategorie „Multistage“ ersetzt diese konkrete Domänenbeschreibung nicht. Die Aussagen L-DESIGN-001 und L-DESIGN-002 in `LOOP-003-design-metadaten.json:11–16` bleiben in dieser Reichweite.

Die gemeinsame Universe-Sektion wurde anschließend selbst gelesen, 03:04:31 UTC. Sie umfasst Menschen ab 15 in Privathaushalten unabhängig von Staatsangehörigkeit, Sprache und Rechtsstatus. Das trägt weder eine ausschließliche Erwachsenen- noch eine ausschließlich wahlberechtigte Zielpopulation. Der Deutschland-Dialog nennt 09.05.2023 bis 21.12.2023 und Face-to-face CAPI/CAMI. Der allgemeine Rundenzeitraum 08.03.2023 bis 01.12.2024 ist keine deutsche Feldzeit. Das ist historischer Erhebungskontext, keine Aussage über aktuelle Einstellungen.

Die kurze Design-JSON nennt Zielpopulation und deutsche Feldzeit nicht selbst, ihr gebundenes SourceInput enthält sie jedoch. Bei einer späteren Übernahme in Quellenkatalog und Belegregister müssen diese Grenzen explizit mitgeführt werden. Hieraus leite ich keinen belegten falschen Designbefund ab.

Die Zusammenfassung bestimmt keine konkrete Zuordnung zu deutschen PSU-/Stratumvariablen in Ausgabe 4.2 und keine Ersatz-/Gemeinsamkeitswahrscheinlichkeiten oder vollständige Schichtenallokation. Die Seite ist kein vollständiges Stichprobenprotokoll. Ein generischer SRS-Bootstrap oder eine fertige Split-/Varianzentscheidung folgt daraus nicht. Die vorläufige Konsequenz im Artefakt ist entsprechend begrenzt. Rohdaten, Header und individuelle Werte wurden nicht gelesen.

### Skill, Schema und Setup-Übergabe

Der Skill verlangt Modus, Aufgabe, freigegebene Eingaben, Manifest und extern gesicherten Manifesthash, Zeile 10. Zeilen 12 und 14 unterscheiden unabhängige Erstbewertung von PR-Review und binden neue Bewertungen an neue Eingabefassungen. Zeile 18 verlangt eigene Originallektüre. Zeile 30 unterscheidet alle fünf Status; Zeile 32 verlangt tatsächliche Laufzeitangaben und hält Aliase von Modellversionen auseinander. Findingfelder sind in Text und Schema benannt. Es gibt keine Befugnis zu Accounts, Commits oder Veröffentlichung.

Die [offizielle Skill-Dokumentation](https://code.claude.com/docs/en/skills) bestätigt Projektpfad, YAML-Frontmatter und unterstützende Dateien. Der vorhandene Pfad, Name und Beschreibung sind daher technisch plausibel. Der Text enthält keine dynamische Shell-Injektion oder zusätzliche Toolfreigabe. Ein Skill ist aber eine Anweisung; selbst `allowed-tools` wäre laut Anbieter keine allgemeine Zugriffssperre. Tatsächliche Loaderfunktion, frischer Claude-Kontext und Zugriffsbeschränkungen wurden nicht ausgeführt. Die Erstbewertung muss später in einer separat gesicherten Sitzung stattfinden. Eine bloße Anwendung im vorhandenen Autorenchat reicht dafür nicht. Fundstellen der eigenen öffentlichen Kopie: `public-sources/claude-skills.md:146`, `:387–388`, `:569–571`, `:736–763`.

Die [Action-Usage-Dokumentation](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md) bestätigt OAuth als technischen Authentifizierungsweg und die Übergabe von CLI-Argumenten. Die [Security-Dokumentation](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md) verlangt vorsichtigen Umgang mit untrusted PR-Kontext, Workflowrechten und Secrets. Das ist ein Anbieterbezug, kein Nachweis eines vorhandenen Projektworkflows. Fundstellen der gespeicherten Kopien: `action-usage.md:58`, `:67`, `:102–105`; `action-security.md:11–35`. Die Übergabe hält diese Umsetzung, den tatsächlichen Modellnachweis und die Test-PRs ausdrücklich offen. Kein eigener Zugriff auf Anmeldung, Secrets oder GitHub-Konfiguration.

Die Schemaausführung zeigte eine konkrete Grenze: Pflichtschlüssel und Syntax werden geprüft, aber mehrere deterministisch unzureichende Befunde bleiben zulässig. Ein fachlicher Review kann diese Widersprüche erkennen; das Schema tut es nicht. R-F02 begrenzt sich auf diese maschinelle Prüfung und behauptet keinen Fehlpass eines bestehenden Workflows.

## Tatsächlich ausgeführte synthetische Prüfungen

Die öffentlichen künstlichen Fälle enthalten keine politischen Fragen, Antworten oder menschlichen Profile. Ihre Requests, Inputdateien und Ergebnisse stehen unter `outputs/loop/prep-repro/protocol/`. Ich habe sie unter den Regeln des eingefrorenen Skills tatsächlich gelesen und entschieden. Das sind Codex-Protokolltests in dieser Sitzung. Sie beweisen weder Claude-Verhalten noch stabile Befolgung in anderen Sitzungen.

| Fall | Tatsächliche Operation | Beobachtete Entscheidung |
| --- | --- | --- |
| P-MISSING-MANIFEST | Request enthält weder Manifestpfad noch erwarteten Manifesthash. Keine inhaltliche Bewertung begonnen. | BLOCKIERT nach Skill:10/14. |
| P-SOURCE-MISSING | Manifest- und Metadatenhash neu berechnet, beide passend. Bezeichnete synthetische Originaldatei tatsächlich zu lesen versucht: FileNotFoundError. | Quellencheck NICHT_GEPRÜFT; davon abhängige Bewertung BLOCKIERT nach Skill:18/30. |
| P-CONTAMINATED-FIRST | Manifest- und Inputhash neu berechnet, beide passend. Eine als rein synthetisch markierte fremde Bewertung entdeckt. | ERSTBEWERTUNG gestoppt und Exposition protokolliert; BLOCKIERT nach Skill:12. Synthetisches BESTANDEN nicht übernommen. |

Das Schema wurde mit `node outputs/loop/prep-repro/schema-tests.cjs` am 2026-10-03, 03:05:54 UTC ausgeführt. Die vorhandene Ajv 8.20.0 konnte Draft 2020-12 mit `strict:true` und `allErrors:true` kompilieren. Ausgeführt wurden 18 Format- und Randfixtures, einschließlich sämtlicher fünf Statuswerte. Vollständige Struktur und ein korrekt blockiertes Urteil ohne Manifest wurden angenommen. Ein unbekannter Status, ein unzulässiger Hash, fehlender Prompt, erfundene interne Vorgaben, ein zusätzliches Top-Level-Feld und ein Finding ohne Belege wurden zurückgewiesen.

Die fünf semantischen Randfixtures wurden trotz bewusst verletzter Mindestanforderungen angenommen: bestanden ohne Manifest/Checks, leere Ausführungsnachweise, bestanden trotz negativem Check im selben Umfang, bestanden mit erheblichem offenem Finding im selben Umfang und leere Findingtexte. Der positive Status dieser synthetischen Eingaben ist kein Ergebnis des Projekts. Die fehlgeschlagene Erwartung betrifft ausschließlich die Fähigkeit des gegenwärtigen Schemas, diese Eingaben zurückzuweisen. Keine Fehlerquote oder empirische Güteaussage wird daraus berechnet.

## Belegte Findings

### R-F01: Erneuter menschlicher Test nach bedeutenden Änderungen fehlt

- Aussage/Entscheidung: Der Entwurf bereitet den vollständigen Verständnistest und seinen Abschluss vor; nach Korrekturen sollen Website und Interpretationen unabhängig geprüft und von Steven freigegeben werden.
- Fundstelle: `docs/verstaendnistest.entwurf.md:39–47`, besonders Zeile 43; Anforderung `reports/loop/preparation-pruefauftrag.md:7` verlangt Wiederholung nach bedeutenden Änderungen. Vollauftrag, Abschnitt „Menschliche Voraussetzungen und Abschluss“, unterscheidet echte menschliche Beiträge von Agent-Simulationen.
- Belegtes Problem: Im gesamten ausgeführten Dokumentabgleich steht keine Regel, wann fünf echte Menschen die geänderte Ergebnis-/Textfassung erneut sehen. Die Schlussregel nennt nur unabhängige Prüfung, Freigabe und Deployment. Ein KI-Review kann damit die ausdrücklich verlangte Wiederholung scheinbar abschließen.
- Auswirkung: Die Aussagen zum Verständnis beziehen sich später möglicherweise nur auf eine frühere Textfassung. Eine bedeutend überarbeitete Darstellung könnte mit einem überholten menschlichen Befund verknüpft bleiben.
- Schweregrad: mittel. Es ist eine belegte Protokolllücke vor einer noch nicht begonnenen menschlichen Prüfung. Sie blockiert die vollständige Bereitschaft dieses Protokolls für Phase 9; sie beweist keinen misslungenen Test und blockiert keine unabhängige Quellenrecherche.
- Korrektur: Vor Versand festlegen, welche Änderungen als bedeutend gelten und eine erneute Prüfung mit fünf echten Menschen an der neuen Release-/Schlüsselfassung auslösen. Ursprüngliche Antworten und Bewertungen erhalten; neue Runde getrennt dokumentieren. Der Statushinweis muss den getesteten Umfang und seine Version treffen.
- Nachprüfung: Neue eingefrorene Protokollfassung unabhängig gegen die Anforderung lesen. Mit einem harmlosen Änderungsbeispiel prüfen, dass eine neue Ergebnisbedeutung oder wesentliche Textänderung eine neue menschliche Runde verlangt; reine Formatkorrekturen begründet abgrenzen. Dies bleibt ein Regeltest, kein menschliches Testergebnis.
- Sicherheit: BELEGT.

### R-F02: Schema akzeptiert unbelegte und widersprüchliche Urteile

- Aussage/Entscheidung: `SKILL.md:28–32` fordert vollständige Findings, tatsächliche Ausführungsbelege und BESTANDEN nur im erfüllten geprüften Umfang; das Urteil soll dem JSONschema entsprechen.
- Fundstelle: `urteil-schema.json:25`, `:39–50`, `:53–64`, `:83–92`, `:97`; eigene ausführbare Belege `schema-tests.cjs`, `schema-results.json` und die fünf `semantic-*`-Fixtures unter `outputs/loop/prep-repro/fixtures/`.
- Belegtes Problem: `manifestSha256` darf bei BESTANDEN null sein; Checks und Inputhashes dürfen leer sein. Prompt, Modellbeleg und die Findingtexte akzeptieren leere Strings. Es gibt keine Konsistenzregel zwischen dem Gesamtstatus und negativen erforderlichen Checks beziehungsweise offenen erheblichen Findings desselben Umfangs. Der tatsächliche Ajv-Lauf nahm alle fünf beschriebenen widersprüchlichen Mindestfälle an.
- Auswirkung: Ein schema-valides Urteil besitzt nicht zuverlässig die vom Skill verlangten prüfbaren Mindestbelege. Eine spätere Automatisierung, die nur JSONvalidität und Gesamtstatus liest, könnte einen unbelegten Erfolg übernehmen. Kein solcher Workflow ist hier vorhanden oder geprüft; die zukünftige Gefahr darf nicht als bereits erfolgter Fehlpass beschrieben werden.
- Schweregrad: mittel. Die maschinelle Vorbereitungsregel verfehlt belegbar ihren Mindestschutz. Vor Verwendung als Pflichtcheck ist die Lücke zu schließen. Die fachliche Quellenlektüre und die korrekt blockierten Codex-Protokollfälle werden dadurch nicht rückwirkend ungültig.
- Korrektur: Für Pflichttexte nichtleere Inhalte und sinnvolle Belegmengen verlangen. Für BESTANDEN im tatsächlich geprüften Umfang mindestens Manifestbindung und dokumentierte Checks verlangen. Einen expliziten ausführbaren Urteilsguard definieren oder passende Schema-Bedingungen hinzufügen, die fehlende Pflichtbelege und widersprüchliche erforderliche Checks/offene erhebliche Findings zurückweisen. Scope-/Erforderlichkeitsangaben müssen verhindern, dass spätere hier nicht erforderliche Prüfungen fälschlich blockieren. Null-Modellwerte bei ehrlich fehlender Runtimekenntnis dürfen zulässig bleiben, wenn die Grenze konkret dokumentiert ist. Eine JSONkontrolle wird dadurch weiterhin keine fachliche Validierung.
- Nachprüfung: Die vorhandenen Positiv- und Negativfixtures gegen die korrigierte eingefrorene Fassung beziehungsweise den Guard neu ausführen. Zusätzlich einen rechtmäßigen Erfolg mit außerhalb des Umfangs offenen späteren Prüfungen prüfen. Ursprüngliche Ergebnisse erhalten; danach echte Claude-Loader-/Verhaltenstests und Workflowprüfungen separat durchführen.
- Sicherheit: BELEGT.

## Grenzen und zulässige Fortsetzung

Die Sampling-Zusammenfassung darf nach dokumentierter Paketentscheidung mit Zielpopulation, Feldzeit und offenen Designfragen in Quellenkatalog und Belegregister übernommen werden. Sie eröffnet keine Antwortdatenanalyse. Das Verständnistestprotokoll und der maschinelle Urteilsvertrag können mit den beiden benannten Korrekturen weiter vorbereitet werden. Ein vollständiges Setup, eine Modell-/Itementscheidung, Entblindung oder Veröffentlichung folgt daraus nicht.

Offen bleiben die praktische Anonymisierung konkreter menschlicher Freitexte, die tatsächliche Claude-Laufzeit und andere Modellfamilie, die technische Zugriffstrennung, der echte Workflow und Pflichtcheck sowie alle empirischen Voraussetzungen. Die Quellenkopien vom veränderlichen `main` und der Anbieterwebsite sind durch Inhaltsprüfsummen gesichert; eine bestimmte Action-Commitversion oder installierte Claude-Version wurde nicht nachgewiesen. Historische Zugriffs-/GitHub-Logs im Paket wurden nicht live erneuert.

## Prüfsummen

Die folgenden zwölf Hashes wurden vor den synthetischen Läufen und danach unverändert beobachtet. Auch Bytezahlen stimmen mit dem Manifest. Der erste Hashcheck erfasste keinen eigenen Uhrzeitwert; der spätere Check ist in `integrity-after.json` datiert.

| Eingefrorener Pfad | SHA256 vor/nach |
| --- | --- |
| reports/loop/preparation-pruefauftrag.md | c16e9841cb7c002358a1c522b1b54edc33b8c5a88ff42feeb6f174c3c5b8895b |
| reports/loop/issue-2026-10-03.md | 7c369ffe6b48487855b621f2c52af7a21923849289de049aba6f067fafc0a397 |
| AGENTS.md | ccf07493ac34e1d63cfa018580f13443d96373b9ede0907754f487f9ed535d7c |
| docs/auftrag-life-93-2026-10-03.md | beb4f2313454fd0d8c0fab7dd6243dbc9616a18335d9254fcbb09d74b459bdf6 |
| docs/handbuch.md | 34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a |
| docs/verstaendnistest.entwurf.md | 118f2c08fc1581f8e7e02dbcffc0fdd14587667d8b866e90196a57a13858f2fe |
| .claude/skills/life93-review/SKILL.md | a7b26a52ffaf7945f6fdbf9d20206d92aab72802b4e36da522677ac061a6c935 |
| .claude/skills/life93-review/references/urteil-schema.json | b11e99c5f0fedf8d126ef953950328edcb6415247060c1471882416b32703fd1 |
| docs/reviews/setup-vorbereitung.md | c579a248c090aa9188c4624a455176cf00173987f6de28725d507f4cdc923171 |
| reports/loop/LOOP-003-design-metadaten.json | ee56ce023b1fe4ca605b6e1d9e07e2da76fee1ce9595e5b5f516e4d6184eb618 |
| reports/loop/setup-access.json | 5d60abd9b96ec8c4032100774a773f0cdc937c887496d99edb35e1aaba60227a |
| reports/loop/claude-access.json | f05261982e93d6286a2ab653cb9cfbe0e0f75edecdb14971a83bc78c0a9e2d46 |

Das SourceInput ist nicht in `files/` dupliziert. Es liegt am ausdrücklich freigegebenen Pfad `outputs/loop/design/portal-capture.json`; SHA256 vor/nach `c67d91f51575396a8ac28f0b587da5c56693fc6723c86187f88c9da9e56c1f38`, 6678 Byte. Sein Hash wurde vor Lektüre kontrolliert. Daraus entsteht keine zusätzliche Freigabe.

| Eigener Beleg | SHA256 |
| --- | --- |
| outputs/loop/prep-repro/portal-independent.json | 8856371669b7e27adb940a2bdfc0285f3fd84a07ff96a0e5ceb0cf011aa1814f |
| outputs/loop/prep-repro/schema-tests.cjs | 5ac3f98d0cb3131f40e5a716abf610c348febc1cd820e7d1a151a78d371a00b5 |
| outputs/loop/prep-repro/schema-results.json | c3ec17f44bf323089832be0e062bf5c33ac1bb3a0f9e54da395b60a027330997 |
| outputs/loop/prep-repro/protocol/requests.json | af41a0f1ed8b75f86fe41302435d64a0a23ec26a806062744ede8889e125a171 |
| outputs/loop/prep-repro/protocol/protocol-results.json | 0f22e22f68d2cc4eaea4993500f258d5ff759513021e1de6a7b45cc72d3a0910 |
| outputs/loop/prep-repro/integrity-after.json | 7aff0c7847e1f24c9904a0e804d3c556afdda1606417fe725a3ba909b334b14f |
| outputs/loop/prep-repro/public-source-register.json | 1dc0a5fd42110360dea26f5d3f5dc0a490eab0f39abfb8d5b4573064a3169aad |
| outputs/loop/prep-repro/technical-check.json | f70abab8ae869f6299f347767714056c1941bfcc9512abac648bced080dec95e |

Der öffentliche Quellenregisterbeleg bindet URL, Abrufzeit, Bytezahl und Hash der eigenen Anbieter-Dokumentkopien. Diese bleiben lokale öffentliche Prüfbelege; ihre Speicherung ist keine Veröffentlichung oder Einrichtung. Der Erstbericht wird nach Übergabe nicht geändert. Korrekturen und Nachprüfungen benötigen eigene Artefakte.
