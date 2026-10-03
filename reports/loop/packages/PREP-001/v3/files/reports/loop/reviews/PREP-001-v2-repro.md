# PREP-001 v2: unabhängige Nachprüfung zu Ausführbarkeit, Reproduzierbarkeit und Originalquellen

Prüfer `/root/prep_v2_repro`, 3. Oktober 2026. Geprüft ist ausschließlich das eingefrorene Paket PREP-001/v2 mit Manifest-SHA256 `9d369a50091a81cdcb4fc4f928692d05cf3c43366eb8963bc2bfe761f49c4683`.

Die fünf ursprünglichen Findings sind für den vorbereitenden Entwurf korrigiert. Eigene Ajv-Gegenfälle weisen die ursprünglichen unbelegten Erfolge und Statuswidersprüche zurück. Die Eingabegrenze trennt den identischen benannten Prüftext von fremder Bewertungshilfe; die Wiederholungsregel verlangt echte Menschen nach bedeutenden Änderungen. Sampling und VERSION-001 sind an den öffentlichen ESS-Originalstellen in der dokumentierten Reichweite bestätigt. Es bleibt kein belegtes blockierendes Finding dieses begrenzten Korrekturauftrags offen.

Das ist eine lokale Korrekturprüfung mit Codex. Sie erteilt keine methodische Modellfreigabe, tatsächliche Claude-Abnahme, menschliche Verständlichkeitsabnahme, Setup- oder Releasefreigabe.

## Tatsächlicher Startauftrag im Wortlaut

> Du bist unabhängiger PREP-001-v2-Prüfer für Ausführbarkeit, Reproduzierbarkeit und Originalquellen. Worktree ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, explizite cwd. Lies AGENTS.md, docs/auftrag-life-93-2026-10-03.md und reports/loop/issue-2026-10-03.md. Dasselbe eingefrorene Paket wie der getrennte Prüfer: reports/loop/packages/PREP-001/v2/manifest.json SHA256 9d369a50091a81cdcb4fc4f928692d05cf3c43366eb8963bc2bfe761f49c4683,21Dateien/5SourceInputs. Kriterien reports/loop/PREP-001-v2-pruefauftrag.md. Erlaubt dieses Paket, SourceInputs, v1-Paket+dessen beide Erstberichte, Korrekturentscheidungen/-bericht; keine aktuellen anderen Reviewerberichte, kein globales Findings-/Agentregister, keine Koordinatorverteidigung. Prüfe alle ursprünglichen PREP-Findings selbst; echte eigene Ajv-Negativ/Positiv-Gegenfälle inklusive unbekannter Modellrevision/ehrlicher BLOCKIERT und zukünftiger Anforderungen außerhalb des Scopes, nicht nur root-Fälle wiederholen. Prüfe formal gültiger Hash vs tatsächlich überprüfte Quelle und zulässige Status. Eigene Codex-Protokollfälle für identischen benannten Prüftext vs fremde Auswahl und Menschentestwiederholung; keine Menschen/Claude-Ergebnisse erfinden. Originalfundstellen deutsche Samplingmetadaten und VERSION-001 selbst öffnen: T3 erst preview_status/open und eigener Tab; keine fremden Tabs verändern. Nur Documentation/DOI-version/Country Documentation, NICHT Variable Viewer, Analysis, Frequenzen, Rohdateien/data/raw/local, A/B, Partei-/LR-Werte, Login, Download oder Cookie-/Storagewerte. Ausgänge nur outputs/loop/prep-v2-repro/ und reports/loop/reviews/PREP-001-v2-repro.md. Gemeinsame Forschungs-/Schema-/UI-Dateien unverändert. Original-/Source-/Endhashes, wirklich ausgeführte Kommandos und Exitcodes, Trennungsgrenzen dokumentieren. Vollständigen tatsächlichen Startauftrag wortgetreu im Bericht sichern, verfügbare Tools und tatsächlicher Modellnachweis: GPT-6.1-Sol laut Runtime, Revision unbekannt, keine andere Familie behaupten. Findings mit Aussage/Originalstelle/Rechengegenfall/Problem/Folge/begründeter Schwere/Korrektur/Nachprüfung; gleiche IDs beibehalten. Keine Zahl/Schlussfolgerung vorgeschrieben, spätere Voraussetzungen nicht als ausgeführte Fehltests behandeln. Keine weitere Agents/Commit/Push. Nach vollständigem Bericht Abschluss+Hash+Kurzbefund.

## Eingaben, Laufzeit und Trennungsgrenzen

Die Prüfung nutzt die 21 eingefrorenen v2-Dateien und fünf bezeichneten SourceInputs, die v1 samt ihren beiden Originalerstberichten sowie die dokumentierten Korrekturentscheidungen. Der v1-Manifesthash ist `152785d06f322a1e95b6503b9b78ed2ff768373852899f4f027ab7f2c6add66a`. Die v2-Dateikopien sind gegenüber dem angegebenen Code-Commit maßgeblich. Der Commit allein belegt keine Ausführung, Quellenlektüre oder weitere Eingabe.

Vor den Gegenfällen wurden sämtliche Paketdateien, SourceInputs, beide ursprünglichen Berichte und beide Korrekturdokumente gehasht. Alle Manifestbindungen und Bytezahlen stimmten. Der erste Hashstand wurde nach der Eingangslektüre von Auftrag, Issue und Manifest, aber vor der sachlichen Paketprüfung und vor den synthetischen Läufen erstellt. Vollständige Pfade, Zeitpunkte, Bytezahlen und Hashes stehen in [hashes-before.json](../../../outputs/loop/prep-v2-repro/hashes-before.json). Der abschließende Stand ist in [hashes-after.json](../../../outputs/loop/prep-v2-repro/hashes-after.json) separat gesichert. Die Originaldateien wurden nicht überschrieben oder formatiert.

Die tatsächliche Laufzeitangabe im Startauftrag ist GPT-6.1-Sol. Interne Revision und nicht zugängliche Anbietervorgaben bleiben unbekannt. Die Prüfung lief durch diesen Codex-Agent; es wurde keine andere Modellfamilie eingesetzt oder behauptet. Für die ausführbaren Prüfungen sind Node `v24.21.0` und die bereits installierte Ajv `8.20.0` selbst abgefragt. Beide Schemas wurden mit Draft 2020-12, `strict: true` und `allErrors: true` kompiliert. Es wurde keine Software installiert.

Das [Werkzeuginventar](../../../outputs/loop/prep-v2-repro/tool-inventory.json) enthält die in dieser Sitzung angebotenen Toolnamen und die tatsächlich genutzten Werkzeuge. Genutzt wurden Shell-/Dateiwerkzeuge und T3 `preview_status`, `preview_open`, `preview_snapshot`, `preview_click`, `preview_press`, `preview_wait_for`, `preview_evaluate` und `preview_navigate`. Der verpflichtende Schreibskill `unslop` wurde gelesen und auf diesen Bericht angewandt. Die eingefrorene LIFE-93-Skill wurde als Prüfgegenstand und Protokollregel gelesen; ihr tatsächlicher Claude-Loader wurde nicht aufgerufen.

Ich habe keine neuen anderen Reviewerberichte, kein globales Findings-/Agentregister und keine Koordinatorverteidigung gelesen. Der sichtbare Agentkontext enthält die geltenden Anweisungen und diesen begrenzten Startauftrag. Eine technische Zugriffssandbox bestand nicht: Agents teilen Dateisystem und Browser. Die eingehaltene Eingabegrenze ist daher eine Auftragsgrenze, kein technischer Isolationsnachweis. Die konkrete Fork-Einstellung ist im eigenen Kontext nicht selbst auslesbar.

Alle eigenen Schreibzugriffe gingen in diesen Bericht und `outputs/loop/prep-v2-repro/`. Gemeinsame Forschungs-, Schema- und UI-Dateien wurden nicht verändert. Es gab keinen weiteren Agent, Commit, Push, Merge, Download, Login, Versand oder Menschenkontakt. ESS-Rohdateien, lokale Antworten, A/B, Partei-/Links-Rechts-Werte und Personenkennungen wurden nicht geöffnet.

## Status nach Umfang

| Gegenstand | Status | Tatsächlicher Nachweis |
| --- | --- | --- |
| Frozen-Paket und SourceInputs | BESTANDEN | SHA256 und Bytezahlen stimmen; Anfangs- und Endkontrolle separat gebunden. |
| PREP-M-01 und PREP-R-F02, formaler Schutz von BESTANDEN | BESTANDEN | 35 eigene Ajv-Fälle sowie fünf direkt reproduzierte v1-Gegenfälle; erforderliche Nicht-Erfolge und offene blockierende Findings verhindern positiven Status. |
| PREP-M-02, Prüfgegenstand und fremde Bewertungshilfe | BESTANDEN | Eigene synthetische Dateien tatsächlich gelesen und nach der v2-Regel entschieden. |
| PREP-M-03 und PREP-R-F01, menschliche Wiederholung | BESTANDEN für die vorbereitete Regel | Sieben eigene Änderungsszenarien decken Bedeutung, Unsicherheit, Beispiele, Gruppen und begrenzte Unverändertheit ab. Keine Menschenantwort. |
| Deutsche Sampling-Zusammenfassung | BESTANDEN für die öffentlichen Aussagen | Eigene Originallektüre von Country documentation → Germany → Details und Universe. |
| VERSION-001 | BESTANDEN für die öffentliche Versionsnotiz | Eigenes Öffnen von Documentation → DOI and version information. Enger dokumentarischer Schluss bestätigt. |
| Tatsächliche Rohdatei-/Header-/Designcodegleichheit, vollständiges Inventar | NICHT_GEPRÜFT | Keine Rohdatei geöffnet; öffentliche Versionsmetadaten beweisen diese Eigenschaften nicht. |
| Tatsächliche Claude-Ausführung, andere Modellfamilie und Workflowsteuerung | NICHT_GEPRÜFT | Kein Claude-Lauf oder Workflowtest in dieser Nachprüfung. |
| Vollständige Setup-Abnahme | BLOCKIERT gemäß vorbereiteter Übergabe | Persönliche Einrichtung und echte Pflichtcheck-/Test-PR-Abnahme bleiben Voraussetzungen. Historische Zugriffslogs wurden nicht als aktueller Nachweis übernommen. |
| Empirische Modellabnahmen, echte fünf Personen, vollständige Website-/Releaseabnahme | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Außerhalb dieses Pakets. Die späteren Voraussetzungen bleiben offen. |

## Eigene ausführbare Schema- und Bindungsgegenfälle

[Schema-Prüfcode](../../../outputs/loop/prep-v2-repro/schema-tests.cjs) und [vollständige Ergebnisse](../../../outputs/loop/prep-v2-repro/schema-results.json) enthalten 35 eigene Fälle. Die Fixture mit bekanntem Modellslug und unbekannter Revision ist gültig. Auch ehrlich unbekannte Anbieter-/Modellangaben sind darstellbar, sofern der Modellbeleg die Grenze benennt. `BLOCKIERT` ohne Manifest, Eingabehashes und ausgeführte Checks wird angenommen. Das verlangt keine erfundenen Pflichtwerte.

Ein positiver Status scheitert ohne Manifestfeld, mit null oder falsch langem Manifesthash, ohne Eingabehashes, ohne erforderlichen bestandenen Check, mit leeren oder bloß weißen Beleg-/Prompttexten und bei offenen blockierenden Findings. Ein erforderlicher zusätzlicher Check mit jedem der vier Nicht-Erfolgsstatus wird zurückgewiesen. Dieselben vier Status eines ausdrücklich späteren, nicht erforderlichen Checks sind bei einem begrenzten Erfolg zulässig. Ein außerhalb des Umfangs geführtes erhebliches Finding bleibt ebenfalls darstellbar; es wird dadurch nicht erledigt.

Die ursprünglichen Fehler wurden zusätzlich direkt an beiden eingefrorenen Schemas reproduziert: fehlende Erfolgsmindestbelege, leere Ausführungsbelege, erforderlicher negativer Check, offenes erhebliches blockierendes Finding und leere Findingtexte. V1 nahm diese fünf Eingaben an, v2 wies sie zurück. Der eigene [Vergleichscode](../../../outputs/loop/prep-v2-repro/original-counterexamples.cjs) und [dessen Ergebnisse](../../../outputs/loop/prep-v2-repro/original-counterexample-results.json) sichern diesen Vergleich. Der eingefrorene Koordinator-Prüfcode mit 18 Fällen wurde zusätzlich ausgeführt; seine Fälle ersetzen meine eigenen nicht.

Der tatsächliche Dateiabgleich bleibt getrennt. Die Fixture `formal-hash-passes-but-wrong-real-file` mit 64 gültigen Hexzeichen ist schemafähig. Ihr angegebener Hash stimmt aber nicht mit der tatsächlich gelesenen synthetischen Datei überein. Der ausgeführte Vergleich erkennt das. Das Schema kann außerdem den formalen Status `NICHT_BESTANDEN` ohne negativen Check speichern; gemäß Skill:32 ist ein solches inhaltliches Urteil unzulässig. Der eigene Grenzfall dokumentiert diese verbleibende Formalgrenze, ohne ihn als zulässige Sachbewertung zu übernehmen. Die Korrektur behauptet keinen vollständigen semantischen Auswerter. Ein künftiger Workflow muss Statusbegründung, richtige Scope-Zuordnung, echte Dateibindung und tatsächlich gelesene Quellen separat kontrollieren.

Im Protokollfall `MISSING-ORIGINAL-DESPITE-VALID-HASH` stimmen Manifest und Metadatenhash tatsächlich. Das Öffnen der ausdrücklich bezeichneten synthetischen Originalquelle endet trotzdem mit `FileNotFoundError`. Ich führe den Quellencheck deshalb als `NICHT_GEPRÜFT` und die davon abhängige positive Aussage als `BLOCKIERT`. Ein korrekter Hash ersetzt keine Originallektüre. Ebenso ist die Aussage einer fehlenden Quelle kein empirisch widerlegter Befund.

## Nachprüfung der ursprünglichen Findings

Alle kurzen Dateipfade dieser Abschnitte meinen die eingefrorene Kopie unter `reports/loop/packages/PREP-001/v2/files/`, außer wenn v1 ausdrücklich genannt ist. Die ursprünglichen Repro-Kennungen `R-F01` und `R-F02` werden nach der im Paket dokumentierten Zuordnung als PREP-R-F01 beziehungsweise PREP-R-F02 geführt; die ursprünglichen Berichte bleiben erhalten.

### PREP-M-01: unbelegter positiver Status

Die ursprüngliche Aussage verlangt ein vollständiges maschinenlesbares Urteil, v1-`SKILL.md:28–32`. V1-`urteil-schema.json:25,39–63` erlaubte den belegten Erfolg ohne Manifest, Checks, Eingabehashes, Prompt und Modellevidenz. Das war eine mittlere Vorbereitungslücke, weil späterer Schemaerfolg keine prüfbare Mindestgrundlage sicherte; es war kein beobachteter Workflow-Fehlpass.

V2-`urteil-schema.json:261–264,267–329` verlangt nichtleere Texte und bedingte Erfolgsmindestfelder. Mein kombinierter Originalgegenfall ist in v1 gültig und in v2 ungültig. Die zusätzlichen eigenen Leerstellen-, Pflichtcheck- und ehrlichen Blockiertfälle zeigen, dass die Korrektur unbelegte Erfolge zurückweist und offene Grenzen weiter abbildet. Befund KORRIGIERT für diesen formalen Vertrag. Echte Quellen-/Dateibindung und Workflowwirkung bleiben separat zu prüfen.

### PREP-R-F02: widersprüchliche oder leere Mindestbelege

Der ursprüngliche Repro-Bericht beanstandete den Widerspruch zwischen einem Gesamt-BESTANDEN und negativen erforderlichen Checks beziehungsweise erheblichen offenen Findings sowie leere Pflichttexte. Originalproblem und mittlere Schwere betreffen die maschinelle Vorbereitung, nicht eine bereits laufende Abnahme.

V2-`urteil-schema.json:110,132–150,159–235,291–346` ergänzt Erforderlichkeit, Findingstatus und Sperrbedingungen. Die direkten Originalgegenfälle reproduzieren den v1-Fehler und scheitern in v2. Meine zusätzlichen Fälle prüfen einen nur optionalen Erfolg, einen niedrigen, aber ausdrücklich blockierenden offenen Befund, einen widersprüchlich noch blockierenden korrigierten Befund und alle vier erforderlichen Nicht-Erfolgsstatus. Die beabsichtigten Sperren greifen. Spätere Anforderungen außerhalb des Umfangs bleiben darstellbar. Befund KORRIGIERT in demselben begrenzten Sinn wie PREP-M-01; der formale Hash-Grenzfall ist ausdrücklich keine Quellenabnahme.

### PREP-M-02: benannter Prüftext gegenüber fremdem Vorschlag

V1-`SKILL.md:12` verbot vorgeschlagene Namen pauschal. Das widersprach der erlaubten identischen Textfassung aus LIFE-93:91 und konnte den zu prüfenden Titel selbst ausschließen. Die mittlere Schwere lag in verschiedenen oder unnötig blockierten Erstgrundlagen, nicht in beobachtetem Claude-Fehlverhalten.

V2-`SKILL.md:12` erlaubt Bezeichnungen im identischen vollständigen Prüfgegenstand und verbietet zusätzliche fremde Bewertungs-, Auswahl- und Namenshilfe. Meine tatsächlich gelesenen künstlichen Pakete führen zu folgenden Entscheidungen:

| Eigener Fall | Codex-Entscheidung |
| --- | --- |
| Identischer Text mit „Regel Alpha“, ohne fremde Hilfe | Als benannter Prüfgegenstand zulässig; keine neue Namensentscheidung getroffen. |
| Derselbe Text plus synthetische fremde Auswahlhilfe | Erstbewertung gestoppt, Exposition protokolliert, BLOCKIERT. |
| Unabhängige neue Namensarbeit plus fremder Vorschlag | BLOCKIERT; derselbe Ausgangstext hebt die Kontamination nicht auf. |
| Dokumentierte Urteile im ausdrücklich bezeichneten PR_REVIEW | Als Revieweingaben zulässig; ersetzt keine Erstbewertung. |

Die Hashes und gelesenen Texte stehen in [protocol-input-observations.json](../../../outputs/loop/prep-v2-repro/protocol-input-observations.json), meine Entscheidungen in [codex-protocol-decisions.json](../../../outputs/loop/prep-v2-repro/codex-protocol-decisions.json). Befund KORRIGIERT als Protokollregel. Alle Fälle liefen im selben Codex-Kontext. Das beweist weder zwei unexponierte reale Modellläufe noch Claude-Befolgung.

### PREP-M-03: Wiederholung des menschlichen Verständnistests

V1-`docs/verstaendnistest.entwurf.md:43–47` nannte erneute unabhängige Prüfung und Freigabe, jedoch keine Auslöser für erneute Menschenantworten. Die mittlere Vorbereitungslücke konnte spätere Verständlichkeitsaussagen an eine überholte Fassung binden. Es gab keinen ausgeführten negativen Menschentest.

V2-`docs/verstaendnistest.entwurf.md:47–51` bindet Änderungen von Bedeutung, Unsicherheitsart, Beispielwerten, Gruppenvergleich und Erklärung an eine neue eingefrorene Seite, Manifest und Schlüssel sowie fünf echte Personen. Mein Szenario eines Wechsels vom Modellvariantenbereich zum Stichprobenintervall verlangt diese Wiederholung; bloßes KI-Review genügt nicht. Neue Beispielwerte lösen sie auch bei unveränderten Fragen aus. Bedeutungsgleiche Schreibkorrekturen haben eine eng begrenzte Ausnahme mit zwei unabhängigen Unverändertheitsprüfungen. Befund KORRIGIERT für die Vorbereitung.

### PREP-R-F01: Versionsbindung echter Menschenbefunde nach Korrekturen

Dasselbe ursprüngliche Problem bleibt unter seiner Repro-Kennung erhalten. Originalfundstelle war v1-`docs/verstaendnistest.entwurf.md:43` gegenüber dem eingefrorenen Erstprüfauftrag. Problem, Folge und mittlere Schwere entsprechen PREP-M-03. Die Korrektur ist nicht allein wegen des Autorentscheids akzeptiert, sondern anhand des neuen Wortlauts und eigener Fälle geprüft.

Meine weiteren Szenarien betreffen einen historischen Gruppenvergleich, der fälschlich zur heutigen Parteiposition umgedeutet wird, eine Erklärung, die zur Bewertung richtiger Haltung wird, einen noch ungeprüften Linkwechsel und einen nachgewiesen unveränderten Teilbefund. Bedeutungsänderungen invalidieren den betroffenen menschlichen Befund. Zusätzlich müssen fachlich falsche Interpretationen korrigiert werden; eine Menschentestwiederholung macht sie nicht zulässig. Beim Linkwechsel bleibt Unverändertheit offen. Ein identischer Teilbefund kann mit belegter Bedeutung und altem Versionsverweis erhalten bleiben.

Befund KORRIGIERT für die Wiederholungsregel. Meine sieben Änderungsszenarien sind Regelprüfungen ohne reale Texte, Antworten oder Testpersonen. Die zwei späteren Unverändertheitsprüfungen wurden dadurch nicht vorweggenommen. Phase 9 bleibt NICHT_GEPRÜFT.

## Eigene Originallektüre: Sampling und VERSION-001

Zuerst wurde T3 `preview_status` genutzt. Es meldete den gemeinsamen bestehenden Tab `tab_g`; dieser wurde nicht bedient. Anschließend erzeugte `preview_open(reuseExistingTab:false)` meinen eigenen Hintergrundtab `tab_h`. Alle folgenden Browseraktionen nannten `tab_h` ausdrücklich.

Country documentation → Germany → Details → Sampling procedure wurde am 3. Oktober 2026 um 04:00:49 UTC selbst gelesen, Universe um 04:01:06 UTC. Die [eigene Samplingdatei](../../../outputs/loop/prep-v2-repro/sampling-original.json) und [Universe-Datei](../../../outputs/loop/prep-v2-repro/universe-original.json) sichern Navigationsstelle und Abrufzeit. Der öffentliche [ESS-Deutschlandabschnitt](https://ess.sikt.no/en/study/412db4fe-c77a-4e98-8ea4-6c19007f551b) trägt die beiden unterschiedlichen Auswahlbereiche und die begrenzte Aussage L-DESIGN-001: ungeclusterte systematische Personenauswahl in den 15 größten Gemeinden, danach die andere Domäne mit 166 PPS-Gemeinden. Zielpopulation sind Personen ab 15 in Privathaushalten. Die deutsche Feldzeit reicht vom 9. Mai bis 21. Dezember 2023. Die Zusammenfassung legt tatsächliche Designcodes, Ersatzregeln, gemeinsame Einschlusswahrscheinlichkeiten und den Varianzalgorithmus nicht fest. L-DESIGN-002 bleibt auf diese Quellenreichweite begrenzt.

Documentation → DOI and version information wurde um 04:02:05 UTC selbst geöffnet und gelesen. Der [eigene Versionsbeleg](../../../outputs/loop/prep-v2-repro/version-original.json) bestätigt Edition 4.2 vom 2. Juli 2026 und die dort genannte ukrainische Übersetzungskorrektur bei B39/loylead. Im veröffentlichten 4.2-Änderungsabschnitt ist keine deutsche Änderung genannt. Edition 4.1 ist vom 13. Januar 2026; 4.0 vom 19. November 2025 enthält die deutsche Stratumkorrektur. Quelle ist die [öffentliche ESS-Versionsdokumentation](https://ess.sikt.no/en/datafile/242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef).

VERSION-001, `docs/ess-versionsabgleich.entwurf.md:5–9`, ist als enger Dokumentationsschluss gerechtfertigt: Die Versionsnummer 4.1 allein belegt keinen Widerspruch zu den veröffentlichten deutschen 4.2-Änderungen. Die tatsächliche lokale Codebuchfassung wurde hier nicht neu geprüft. Weder Vollständigkeit der Release Notes noch bytegleiche deutsche Rohdateien, vollständige Inventargleichheit oder richtige Designzuordnung werden daraus abgeleitet. Die ältere deutsche Stratumkorrektur muss beim später autorisierten Dateizugriff berücksichtigt werden.

Der [ausgeführte Textabgleich](../../../outputs/loop/prep-v2-repro/source-comparison.json) bestätigt, dass die selbst gelesenen relevanten Originalabschnitte zu den gebundenen SourceInputs passen. Er ist kein Rohdatenvergleich. Diese zusätzliche Versionsprüfung wurde nach dem ursprünglichen v1-Prüfauftrag ausgeführt und ist keine rückwirkend vorab festgelegte Analyse.

Es wurden ausschließlich öffentliche Dokumentationsansichten geöffnet. Variable Viewer, Analysis, Frequenzen, Login und Download blieben unbenutzt. Ein anfänglicher T3-Snapshot lieferte automatisch Browserdiagnostik einschließlich einer Tracking-Request-URL; sie wurde weder ausgewertet noch in eigene Quellenbelege übernommen. Danach wurden nur öffentliche sichtbare Texte und passende Bedienelemente ausgelesen. Cookie-/Storagewerte wurden nicht gezielt gelesen oder verändert. Eine eigene Tab-ID beweist keine getrennten Browserprofile.

## Ausgeführte Kommandos und technische Prüfung

Alle Shellaufrufe nannten den autorisierten Worktree als `workdir`. Das [Kommandoregister](../../../outputs/loop/prep-v2-repro/command-ledger.json) hält die tatsächlichen Lese- und Prüfkommandos samt beobachteten Exitcodes fest. Die vollständigen eigenen Skripte liegen neben ihren Ergebnissen.

| Kommando | Exitcode | Begrenztes Ergebnis |
| --- | --- | --- |
| `node outputs/loop/prep-v2-repro/schema-tests.cjs` | 0 | 35 eigene formale Fälle und eigener echter Hash-Gegenabgleich. |
| `python outputs/loop/prep-v2-repro/protocol-checks.py` | 0 | Fünf synthetische Pakete tatsächlich gelesen; fehlende Quelle protokolliert; sieben Änderungsszenarien erzeugt und gelesen. |
| `node outputs/loop/prep-v2-repro/original-counterexamples.cjs` | 0 | Fünf v1-Fehler direkt reproduziert und durch v2 zurückgewiesen. |
| `node reports/loop/packages/PREP-001/v2/files/scripts/check-review-schema.mjs` | 0 | Die 18 eingefrorenen Koordinatorfälle zusätzlich ausgeführt. |
| Python-Hash- und Originaltextabgleiche | 0 | Paketbindungen und öffentliche Abschnittsgleichheit; keine wissenschaftliche Abnahme. |

`pnpm check` wurde nach der eigenen Berichtsänderung tatsächlich ausgeführt und endete mit Exit 0. Formatprüfung, Handbuchprüfung, Schemafälle, Typenprüfung, neun App-Tests und Build bestanden. [Ausführungsdatensatz](../../../outputs/loop/prep-v2-repro/technical-check.json) und [vollständiges Log](../../../outputs/loop/prep-v2-repro/pnpm-check.log) sichern Auftrag, Zeiten, Exitcode und Loghash. Die technische Prüfung begründet keine methodische, Claude- oder menschliche Abnahme. Es wurden keine UI-Dateien oder sichtbaren App-Texte geändert; daher wurde kein Desktop-/Smartphone-Appcheck als Teil dieser Korrekturprüfung ausgegeben.

## Original-, Source- und Endhashes

| Artefakt | SHA256 am Eingang |
| --- | --- |
| v1-Originalerstbericht Methoden | `58a47122c373af60575d436eec857ec9bc6a41c0bf87ad27447337e14e9b032f` |
| v1-Originalerstbericht Reproduzierbarkeit | `5c12d63a093992d293adf7c8552f46208da26ddc23cc957a74a9abbee6a41d94` |
| Korrekturentscheidungen | `556997421c851ab32cb4e495b5bfa30200f4f83e1e19b71eda2dfc5ffbd38400` |
| Korrekturbericht | `a2714d4a3b2304158359c7722c9413834b84704725600f4b03aa712511a4626c` |
| SourceInput: design/portal-capture.json | `c67d91f51575396a8ac28f0b587da5c56693fc6723c86187f88c9da9e56c1f38` |
| SourceInput: preparation-correction/schema.log | `70462e69c066eebac6c3162ed4202f5c7a91aa9e6265f3b17ab93902458c82ae` |
| SourceInput: preparation-correction/schema.json | `00ce9e665eda984cfda29b654d31a5243b425ba19eda61770db4417abca841ed` |
| SourceInput: preparation-correction/codex-protocol-reading.json | `8e63cedf36572c8e0a5bf674635d3e6e08671fe51b349acce27e8fc57345d41c` |
| SourceInput: version/ess11-4.2-capture.json | `ad77d489d255f9f14d6b4a97631572a422d755b386f7ffbd036e1377a2c50c93` |

Der Endabgleich bestätigt sämtliche 45 erfassten Manifest-, Paket-, Source- und Originalpfade als unverändert zum Eingang; auch alle Manifestbindungen stimmen. Eigene Belege werden separat in [evidence-hashes.json](../../../outputs/loop/prep-v2-repro/evidence-hashes.json) gehasht. Der abschließende Berichthash wird nach vollständiger Fertigstellung berechnet und an den Koordinator übergeben; er wird nicht als selbstreferenzieller Inhalt dieses Berichts eingetragen.
