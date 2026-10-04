# K1 Runde 2: gezielte Nachprüfung der Textvorschläge

4. Oktober 2026. Gesamturteil: **BESTANDEN** für den begrenzten Nachprüfungsumfang. **K1-F01 bis K1-F05 sind KORRIGIERT.** Keine neuen Findings durch die geprüften Korrekturen. Das Urteil betrifft Textvorschläge, keine Umsetzung oder Veröffentlichungsfreigabe.

## Auftrag und Bindung

Modus `NACHPRUEFUNG`. Geprüft sind die Behebung der fünf Findings im Entwurf 2 und mögliche neue Fehler durch diese Korrekturen sowie Abschnitt 4 der Entscheidungsvorlage. Keine vollständige neue Prüfung. Der Auftrag wurde gelesen; `life93-review` und `unslop` wurden angewandt. Der vollständige Aufrufer-Prompt steht in `execution.prompt` des JSON-Urteils; die Auftragsdatei ist über ihren Hash gebunden.

Auftrag-SHA-256: `02740dafbd8a63bc8a094b71599245166c4528f1ff666c5742bb3560e9b2a323`.

Manifest-SHA-256: `85f12b2f0bfc134723c092f8709904ac8fd9237dfcc11f2b93f7da2fae33248f`.

Beide vor Beginn bestätigt. Alle 14 Manifestartefakte stimmen. Tatsächlicher und verlangter HEAD: `c171e7d8d7ebc984b03e2803f7ca25d6fd2a6217`, Branch `research/life-93-claude-20261003`. Die Arbeitskopie war anfangs sauber. Der ältere Manifestcommit `de024e3b02ff35ccd79e5d3f19407305dcafc499` bezeichnet den Paketursprung; die aktuelle Prüffassung ist über die übereinstimmenden Artefakthashes gebunden.

## Stand der Findings

| Finding | Ursprünglicher Schweregrad | Stand Runde 2 |
| --- | --- | --- |
| K1-F01 | mittel | KORRIGIERT |
| K1-F02 | mittel | KORRIGIERT |
| K1-F03 | niedrig | KORRIGIERT |
| K1-F04 | niedrig | KORRIGIERT |
| K1-F05 | niedrig | KORRIGIERT |

### K1-F01

Runde 1: Freie Lebensführung wurde auf Paarrechte verengt; das normative Prinzip zu knappen Arbeitsplätzen fehlte.

Entwurf 2 ersetzt die Paarrechts-Sammelformulierung und nennt das Arbeitsplatzprinzip ausdrücklich. KORRIGIERT. Abgleich mit Bereichsabdeckung, Plan 3.2 und Katalogeinfügung ausgeführt. Freie Lebensführung setzt keine Partnerschaft voraus; das Adoptionsrecht bleibt gesondert erkennbar. Keine neue Messform oder Personenbewertung.

Belege:

- docs/vorschlaege-texte-v1.entwurf.md:78,91: Gleichberechtigung bei knappen Arbeitsplätzen, freie Lebensführung von Schwulen und Lesben und Adoptionsrecht gleichgeschlechtlicher Paare stehen als getrennte Gegenstände im Untertitel.
- web/src/app/policy-draft/profile/area-scope.ts:69–74; docs/analyseplan-v2.2.md:44; docs/abdeckung-v2.2.md:35; web/src/app/policy-draft/policy-catalogue.ts:177 binden mnrgtjb, freehms und hmsacld.

Auswirkung: Die Verengung und die Auslassung sind im Textvorschlag behoben. Der Untertitel beschreibt Gegenstände, ohne eine Antwort zu bewerten. Der frühere Schweregrad bleibt zur Nachvollziehbarkeit dokumentiert; der Befund blockiert den Umfang jetzt nicht mehr.

### K1-F02

Runde 1: Das Verbot demokratiefeindlicher Parteien fehlte als eigenständiger Gegenstand.

Entwurf 2 nennt Parteienverbot ausdrücklich und präzisiert Demokratiemerkmale und Loyalität. KORRIGIERT. Gegen Bereichsbeschreibung, Plan und Katalogeinfügung geprüft. Die Stichwortliste bleibt eine knappe Übersicht neben Erfasst/Nicht erfasst und ersetzt keinen Originalwortlaut.

Belege:

- docs/vorschlaege-texte-v1.entwurf.md:73,92: Wichtigkeit von Demokratiemerkmalen, Regierung und Mehrheitsmeinung, Führung, Loyalität und Gesetz sowie Verbot demokratiefeindlicher Parteien.
- web/src/app/policy-draft/profile/area-scope.ts:30–35; docs/analyseplan-v2.2.md:45; docs/abdeckung-v2.2.md:29; web/src/app/policy-draft/policy-catalogue.ts:164 binden accalaw, loylead und prtyban.

Auswirkung: Die Gegenstandsübersicht enthält jetzt auch die Parteienverbotsfrage. Sie bewertet weder Befürwortung noch Ablehnung. Der frühere Schweregrad bleibt zur Nachvollziehbarkeit dokumentiert; der Befund blockiert den Umfang jetzt nicht mehr.

### K1-F03

Runde 1: Die Dimensionsvorgabe in der bestehenden Zeile eigenes Modell blieb trotz der übrigen Begriffskorrekturen stehen.

Vierte Begriffszeile ergänzt und ihre Ersetzung ausdrücklich erklärt. ESS-bezogene Zeilen werden erst bei tatsächlich eingebundener zusätzlicher Quelle angepasst. KORRIGIERT. Gesamte vorhandene Tabelle 7.3 mit den vorgeschlagenen Ersetzungen abgeglichen. Dimension wird nur bedingt für eine spätere geprüfte gemeinsame Messung beschrieben und ist in dieser Fassung nicht vorhanden. Umsetzung des Handbuchs bleibt offen.

Belege:

- docs/vorschlaege-texte-v1.entwurf.md:44,46,93: eigenes Modell = Auswahl, Ordnung, Auswertung und Deutung durch das Projekt; ausdrückliche Ersetzung der alten Dimensionszeile.
- docs/handbuch.md:266–287, insbesondere 272,273,278; docs/profilregeln-v1.md:5–9,75–81; docs/analyseplan-v2.2.md:13–21.
- docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:47 empfiehlt auch die Zeile eigenes Modell.

Auswirkung: Die vorgeschlagene Übernahme lässt in Tabelle 7.3 keine unbedingte Dimensionsvorgabe für das aktuelle Profil zurück. Der frühere Schweregrad bleibt zur Nachvollziehbarkeit dokumentiert; der Befund blockiert den Umfang jetzt nicht mehr.

### K1-F04

Runde 1: B nannte für einen künftigen Mehrquellenbestand weiterhin nur ESS; Quellenfreigabe und tatsächliche Nutzung waren nicht getrennt.

B ist ausdrücklich eine Vorlage mit vollständiger Quellenkennzeichnung; Voraussetzung ist tatsächliche Einbindung einer weiteren Quelle. KORRIGIERT für die Vorlage und die Übernahmeregel. Die gesonderten Rechte- und Planvoraussetzungen gelten weiter. Bei späterer Umsetzung muss die Quellenkennzeichnung am dann gebundenen Bestand geprüft werden; dieser Zukunftscheck ist hier nicht ausgeführt.

Belege:

- docs/vorschlaege-texte-v1.entwurf.md:14–16,94: Vorlage für mehrere Quellen; Quellenangabe je Frage und jedem Vergleich; alternativ Aufzählung aller tatsächlich verwendeten Quellen; tatsächliche Einbindung statt bloßer Freigabe.
- docs/project.md:7–14; docs/analyseplan-v2.2.md:29; docs/abdeckung-v2.2.md:88,102: gegenwärtiger ESS-Bestand und weitere Kandidaten ohne Aufnahme.
- docs/vorschlaege-texte-v1.entwurf.md:3,16 und docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:47 belassen Empfehlung A und Stevens Entscheidung.

Auswirkung: B kann einen späteren Mehrquellenbestand beschreiben, ohne ausschließlich ESS als Herkunft auszugeben oder Freigabe mit Nutzung gleichzusetzen. Der frühere Schweregrad bleibt zur Nachvollziehbarkeit dokumentiert; der Befund blockiert den Umfang jetzt nicht mehr.

### K1-F05

Runde 1: Das beabsichtigte Beschreiben durch den geplanten Test stand in B im Präsens.

soll in beiden Varianten; Zeichenzahlen entsprechend angepasst. KORRIGIERT. Länge und Statusmerkmale mit Python geprüft; die Formulierungen gegen Handbuch 7.2 und 7.6 gelesen. B hat 157 Unicode-Zeichen.

Belege:

- docs/vorschlaege-texte-v1.entwurf.md:26–29,95: A enthält beschreiben soll; B enthält Er soll Antworten Frage für Frage beschreiben und ist noch nicht verfügbar.
- Unicode-Zählung ohne äußere Anführungszeichen: A = 147, B = 157; beide ≤ 160. Beide beginnen mit 12 Axes Deutschland und nennen die Nichtverfügbarkeit.
- docs/handbuch.md:260,310; docs/project.md:11,14; web/src/index.html:8–11 als unveränderte Umsetzungsfundstelle.

Auswirkung: Beide Meta-Varianten kennzeichnen das Verhalten als geplant und halten die Metadatenvorgaben ein. Der frühere Schweregrad bleibt zur Nachvollziehbarkeit dokumentiert; der Befund blockiert den Umfang jetzt nicht mehr.

## Korrekturen und Entscheidungsvorlage

Der Diff gegen `bb760f3` enthält die fünf Korrekturen, geänderte Zeichenzahlen und Änderungsnotizen. In der Entscheidungsvorlage ist nur Abschnitt 4 angeglichen. Zeile 47 empfiehlt weiterhin Statushinweis A und Meta B und ergänzt `eigenes Modell` zu den Begriffszeilen. Die Aussage, Entwurf 2 korrigiere die fünf Befunde, ist durch diese Nachprüfung bestätigt.

Die neuen Untertitel beschreiben vorhandene Gegenstände ohne politische Wertung. Die Stichwortlisten dürfen neben den vorhandenen Angaben „Erfasst“ und „Nicht erfasst“ knapp bleiben; sie ersetzen keine Originalfragen. Die Begriffskorrektur führt keine aktuelle Messdimension ein. Die Zukunftsvorlage B nennt vollständige Quellenkennzeichnung und tatsächliche Einbindung als Bedingung. Keine durch diese Änderungen neu eingeführten Fehler festgestellt.

Die korrigierten Vorschläge sind noch nicht umgesetzt. Deshalb bleiben die alten Dimensionsformulierungen im Handbuch und in der HTML-Vorlage erwartungsgemäß erhalten. Ihr Fortbestand ist kein offenes Finding dieser Vorschlagsnachprüfung. Stevens Entscheidung ist weiterhin erforderlich.

## Checks und Grenzen

- K1-R2-C01: BESTANDEN – Auftrag, Manifest, Branch-Stand und alle 14 Manifestartefakte.
- K1-R2-C02: BESTANDEN – Gezielte Nachprüfung K1-F01.
- K1-R2-C03: BESTANDEN – Gezielte Nachprüfung K1-F02.
- K1-R2-C04: BESTANDEN – Gezielte Nachprüfung K1-F03.
- K1-R2-C05: BESTANDEN – Gezielte Nachprüfung K1-F04.
- K1-R2-C06: BESTANDEN – Gezielte Nachprüfung K1-F05.
- K1-R2-C07: BESTANDEN – Neue Fehler durch Korrekturen und Angleichung von Abschnitt 4 der Entscheidungsvorlage.
- K1-R2-C08: BESTANDEN – Erhaltung der gebundenen Eingaben und der ursprünglichen K1-Berichte.

- Nur gezielte Nachprüfung von K1-F01 bis K1-F05 und neuen Fehlern ihrer Korrekturen einschließlich Abschnitt 4 der Entscheidungsvorlage; keine vollständige neue Prüfung des Textpakets.
- BESTANDEN gilt für die Textvorschläge im gebundenen Entwurf 2. Keine Umsetzung, methodische Validierung, Begutachtung durch Fachleute, Neutralitätsgarantie, Produktabnahme oder Veröffentlichungsfreigabe. Stevens Entscheidungen bleiben offen.
- V2-urteil.json und T1-technik-browser.md nur als Bytes gehasht; keine inhaltliche Nutzung fremder Urteile. K1 Runde 1 wurde zur gezielten Findingnachprüfung gelesen.
- Kein Zugriff auf data/raw/, data/local/, outputs/ oder data/reference-*, keine Antwortverteilungen, keine GESIS-Server und keine externen Nachrichten.
- Originalfragebögen und importierte Katalogdateien nicht geöffnet. Gegenstandsabgleich nutzt die gebundenen Bereichsbeschreibungen, Katalogeinfügungen und Plan 3.2; keine erneute Originalwortlaut- oder empirische Prüfung.
- Keine neue Fundstellenprüfung des unveränderten ESS-Stichprobenabschnitts, keine erneute Prüfung der Statusnotizen in Abschnitt 6 und keine Bewertung der übrigen Erweiterungsentscheidungen. Keine Live-Abfrage von LIFE-93 oder anderen externen Quellen.
- docs/abdeckung-v2.2.md und docs/pruefregeln.md zusätzlich zum Manifest gemäß den bereitgestellten AGENTS.md-Regeln gelesen und gehasht. Ihre übrigen Aussagen sind nicht neu auditiert.
- Memory-Suche nur für Hashbindung, Erhaltung historischer Berichte und Umfangsgrenzen. Keine verlinkten Memory-Reviews geöffnet und keine historischen Urteile als Ergebnisgrundlage übernommen.
- Mehrere Sammelausgaben waren abgeschnitten. Fehlende relevante Grundlagen und Fundstellen wurden in kleineren Ausgaben nachgelesen. Nicht benötigte Ausführungsprotokolle des ersten K1-Berichts wurden nicht vollständig nachgelesen.
- Keine pnpm-, Pipeline- oder Browserprüfung: ausschließlich Berichtsausgaben sind erlaubt; keine Implementierung oder sichtbare Oberfläche wurde geändert. Technische und Browserakzeptanz werden nicht behauptet.
- jsonschema nicht installiert. JSON formal mit einem nur lesenden Python-Validator für die Schlüsselwörter des vorgegebenen Schemas geprüft; keine Installation und keine Änderung am Schema.
- Während der Prüfung entstand eine fremde Änderung an reports/claude/fortsetzung-2026-10-04.md außerhalb des Pakets. Keine Einsicht oder Änderung; die gebundenen Eingaben und HEAD blieben unverändert.

## Erhaltung und formale Kontrolle

Die abschließende Hashprüfung bestätigte alle 22 gelesenen Dateien unverändert, einschließlich der ersten K1-Berichte. HEAD blieb unverändert. Während der Prüfung erschien in `git status` eine fremde Änderung an `reports/claude/fortsetzung-2026-10-04.md`. Diese Datei wurde weder gelesen noch bearbeitet; sie gehört nicht zum Paket.

Das JSON wurde mit einem Python-Validator gegen die im Urteilsschema verwendeten Schlüsselwörter geprüft. Alle acht erforderlichen Checks sind bestanden; alle fünf historischen Findings haben `state: KORRIGIERT`, `blocksScope: false`. Die formale Kontrolle ist kein zusätzlicher fachlicher Nachweis. Nur die beiden beauftragten Berichte wurden geschrieben, ohne Commit, Tag, Push oder externe Nachricht.

## Gelesene Dateien mit SHA-256

Die Angaben trennen inhaltliches Lesen und reine Hashprüfung. Alle Manifestartefakte wurden vor der Bewertung gehasht. Zusätzliche vorgeschriebene Grundlagen und Verfahrensdateien wurden ebenfalls gehasht; sie erweitern den Bewertungsumfang nicht.

| Datei | SHA-256 | Zugriff |
| --- | --- | --- |
| docs/vorschlaege-texte-v1.entwurf.md | `7c999b421d1745e058c7b12af847c100e1710411fec9a7f65289cd585bd482a6` | vollständig; Änderungen und unmittelbarer Findingkontext bewertet |
| docs/handbuch.md | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` | vollständig; Tabelle 7.3 und Textregeln für Nachprüfung genutzt |
| docs/profilregeln-v1.md | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` | vollständig; Grundlage, kein neuer Audit |
| docs/analyseplan-v2.2.md | `13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8` | vollständig; insbesondere 2 und 3.2, kein neuer Audit |
| docs/project.md | `a4a5736e1e2263bfbcbec82ade86e1190540a9523fe96e1214fb2e008b5c1c5e` | vollständig; Statusgrundlage |
| web/src/index.html | `d3dcf44566fd2c05d92b9acdf0c9d0e570b472abd3edfa7ac4face20fc15657c` | vollständig; unveränderte Umsetzungsfundstelle |
| web/src/app/policy-draft/policy-draft.html | `f25712dc8d6fbd85c5d93fa4c6db8c006fe5132282db06f922733fd9e2c94b2a` | nur Suchtreffer mit Kontext für Status, Quellenangabe und Erfasst/Nicht erfasst |
| web/src/app/policy-draft/policy-catalogue.ts | `acde504fa6f0b815d93c66a842d1a25270092713ea898df97b9e8617388a6193` | Zeilen 110–190; insbesondere Einfügungen 164 und 177 |
| web/src/app/policy-draft/profile/area-scope.ts | `4ed439fd3a1d9b9d030f8ed33b9a4d55916d07cc694bcf8a3aec6f86d338a1b1` | Zeilen 1–100; insbesondere 30–35 und 69–74 |
| reports/claude/agenten/V2-urteil.json | `622e6961b36655943f126ffa25eb7758e3d7b025fa3a1b6275630beb673d02cf` | ausschließlich Hashprüfung; kein inhaltliches Lesen |
| reports/claude/agenten/T1-technik-browser.md | `3bba4b1112db99f9938104ba82b17fdfb552d57657a5440ea4827ce7f88e3636` | ausschließlich Hashprüfung; kein inhaltliches Lesen |
| docs/entscheidungsvorlage-erweiterung-v1.entwurf.md | `00c61383702c3603ec93d24fbe79bd28e2ed7c89fb4c5bf9d9577cd1260543c2` | Diff und Zeilen 35–52; nur Abschnitt 4 bewertet |
| reports/claude/pruefungen/K1-textvorschlaege.md | `89124250b7283bf541bf408275297b83006308be7532faaccdb5f41e0523f3d8` | Findingtexte, Prüfgrundlagen und Grenzen gelesen; Ausführungsprotokoll nur teilweise sichtbar |
| reports/claude/pruefungen/K1-textvorschlaege.json | `e9ceb4aa333b8980ad4eadde6275d8bdb61425166e18119279e4cb0b5d561eba` | insbesondere alle fünf Findings; Sammelausgabe teilweise abgeschnitten |
| reports/claude/auftraege/K1-runde2-textvorschlaege.md | `02740dafbd8a63bc8a094b71599245166c4528f1ff666c5742bb3560e9b2a323` | vollständig gelesen; Auftrag oder Verfahrensdatei |
| reports/claude/pruefungen/TEXTE-V1-002-manifest.json | `85f12b2f0bfc134723c092f8709904ac8fd9237dfcc11f2b93f7da2fae33248f` | vollständig gelesen; Auftrag oder Verfahrensdatei |
| .claude/skills/life93-review/SKILL.md | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` | vollständig gelesen; Auftrag oder Verfahrensdatei |
| .claude/skills/life93-review/references/urteil-schema.json | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` | vollständig gelesen; Auftrag oder Verfahrensdatei |
| .agents/skills/unslop/SKILL.md | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` | vollständig gelesen; Auftrag oder Verfahrensdatei |
| docs/abdeckung-v2.2.md | `544deeb3055ffb174d8e3c97f6f4e5b6a640c8502113462cd3b6bcee6cb5e8f9` | vollständig; zusätzliche vorgeschriebene Grundlage, kein neuer Audit |
| docs/pruefregeln.md | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` | vollständig; zusätzliche vorgeschriebene Grundlage |
| /home/stevenh/.codex/memories/MEMORY.md | `76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9` | nur genannte rg-Treffer; Verfahrenshilfe, keine Bewertungsgrundlage |

## Ausgeführte Befehle

Alle Aufrufe liefen im vorgegebenen Arbeitsverzeichnis. Python-Skripte wurden aus Here-Documents ausgeführt und nicht als Dateien abgelegt. Die folgenden Angaben nennen die Befehle und die Funktionen der Skripte. Sammelausgaben mit Trunkierung wurden für notwendige Stellen durch kleinere Reads ergänzt.

- `sha256sum reports/claude/auftraege/K1-runde2-textvorschlaege.md reports/claude/pruefungen/TEXTE-V1-002-manifest.json`; `git rev-parse HEAD`; `git status --short`; `cat reports/claude/auftraege/K1-runde2-textvorschlaege.md`.
- `cat .claude/skills/life93-review/SKILL.md`; `cat reports/claude/pruefungen/TEXTE-V1-002-manifest.json`; `cat .agents/skills/unslop/SKILL.md`; `rg -n 'gezielte|immutable|bounded|Nachprüfung' /home/stevenh/.codex/memories/MEMORY.md`.
- `python3` aus einem Here-Document: alle 14 Manifestpfade ausschließlich zur SHA-256-Kontrolle öffnen; anschließend `cat` des Urteilsschemas, von `docs/project.md` und `docs/handbuch.md`.
- `nl -ba docs/handbuch.md | sed -n '1,210p'`; `nl -ba docs/project.md | sed -n '85,200p'` (keine weiteren Zeilen); `cat docs/pruefregeln.md`.
- `nl -ba docs/handbuch.md | sed -n '211,430p'`; `nl -ba docs/project.md | sed -n '65,150p'`.
- `nl -ba reports/claude/pruefungen/K1-textvorschlaege.md`; `cat reports/claude/pruefungen/K1-textvorschlaege.json`.
- `nl -ba docs/vorschlaege-texte-v1.entwurf.md`; `git diff bb760f3 -- docs/vorschlaege-texte-v1.entwurf.md docs/entscheidungsvorlage-erweiterung-v1.entwurf.md`.
- `wc -l` für Analyseplan, Abdeckung, Profilregeln, Prüfregeln und Entscheidungsvorlage; `nl -ba docs/profilregeln-v1.md | sed -n '1,100p'`; `nl -ba docs/analyseplan-v2.2.md | sed -n '1,105p'`.
- `nl -ba docs/analyseplan-v2.2.md | sed -n '106,180p'`; `nl -ba docs/abdeckung-v2.2.md | sed -n '1,60p'`; `nl -ba docs/entscheidungsvorlage-erweiterung-v1.entwurf.md | sed -n '35,52p'`.
- `nl -ba docs/abdeckung-v2.2.md | sed -n '61,110p'`; `nl -ba docs/pruefregeln.md | sed -n '1,36p'`; `nl -ba web/src/app/policy-draft/profile/area-scope.ts | sed -n '1,100p'`; `nl -ba web/src/app/policy-draft/policy-catalogue.ts | sed -n '110,190p'`.
- `sed -n '1,19p' docs/pruefregeln.md`; `sed -n '100,102p' docs/abdeckung-v2.2.md`; `sed -n '40,65p' docs/project.md`; `nl -ba web/src/index.html`; `rg -n -C 3 'Forschungsprototyp|keine Dimension|Erfasst|Nicht erfasst|Quelle|origin' web/src/app/policy-draft/policy-draft.html`; `git branch --show-current`.
- `PYTHONDONTWRITEBYTECODE=1 python3` aus einem Here-Document: SHA-256 aller 22 gelesenen Dateien, Manifestvergleich, Unicode-Längen und Statusmerkmale beider Metatexte, UTC-Zeit, HEAD/Branch, Prüfung der Verfügbarkeit von jsonschema und der Existenz der beiden Zielberichte.
- `PYTHONDONTWRITEBYTECODE=1 python3` aus einem Here-Document: Abschlusshashes gegen die gespeicherten Pins, HEAD und `git status --short`.
- `PYTHONDONTWRITEBYTECODE=1 python3` aus einem Here-Document: Bericht und JSON erzeugen, vorgegebenes Schema formal prüfen, ausschließlich die zwei Zielberichte schreiben.
- `PYTHONDONTWRITEBYTECODE=1 python3` aus einem Here-Document: geschriebenes JSON erneut einlesen und formal prüfen, alle Eingabepins und die Findingzustände kontrollieren; `git status --short` und `git diff --stat`.

## Modell laut Laufzeit

OpenAI, `gpt-6.1-sol`, Reasoning-Einstellung `high`, laut expliziter T3-Code-/Codex-Harness-Laufzeitangabe. Eine konkrete interne Modellrevision ist nicht nachgewiesen. Interne Anbietervorgaben sind unbekannt. Dies ist ein Codex-KI-Review.
