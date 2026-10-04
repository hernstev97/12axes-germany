# P4 Runde 3: gezielte Methoden-Nachprüfung des Planentwurfs v2.3

4. Oktober 2026. Begrenztes KI-Review durch Codex/OpenAI. Paket PLAN-V23-003, Analyseplan v2.3 Entwurf 0.4, Modus NACHPRUEFUNG.

## Gesamturteil

BESTANDEN im benannten Nachprüfungsumfang. P4-V23-F01 ist KORRIGIERT und blockiert diesen Scope nicht mehr. Keine neuen Findings aus den Änderungen von Fassung 0.4 im geprüften Methoden- und Reproduzierbarkeitsumfang.

Das Urteil ist keine neue Gesamtprüfung des Plans und keine empirische, wissenschaftliche, Quellen-, Neutralitäts-, Produkt- oder Releasefreigabe. P4-V23-F02 bis F06 bleiben mit dem Stand KORRIGIERT aus Runde 2 erhalten; ihre unveränderten Verfahren wurden nicht erneut vollständig geprüft. Die getrennte Rolle P5 und spätere Freigaben bleiben eigenständig.

## Bindung

Die beiden vorgegebenen Hashes wurden als erste Prüfung bestätigt:

- Auftrag: d9e089f03ed323137fc259782a96186c5334bf9dd2e06c0e9159ccef11d5780f.
- Manifest: 96b20f220f8757a24ce880eee106e9fa7cd2aca3c234410786acd32d7a6a347d.

Ausgangs-HEAD: f169a1dbc704ef50bb94f8babeb0fe55a9a7f49d. Branch: research/life-93-claude-20261003. Ausgangsstatus sauber. Die beiden eigenen Ausgabedateien waren vor dem Schreiben nicht vorhanden.

Das Manifest enthält 27 Artefakte, darunter vier P5-Berichte. Diese vier wurden weder geöffnet noch gehasht. Alle 23 zulässigen Manifestartefakte stimmen mit ihren Pins und byteweise mit dem genannten Auftragscommit überein. Der interne Manifest-Eintrag commit nennt noch 42b6068b22a0c4fd413c4dac65ed6675b4192d6a. Das ist eine Metadatengrenze, keine abweichende Prüffassung: die extern vorgegebene Manifestprüfsumme, die Artefaktpins, Entwurf 0.4 und der Auftragscommit wurden konkret gebunden.

Vorberichte bleiben unverändert. Die lokalen Eingabehashes wurden vor dem Schreiben erfasst und nach dem Schreiben erneut geprüft. Hashprüfung bedeutet keine vollständige Inhaltsprüfung.

## P4-V23-F01: KORRIGIERT

Runde 1 beanstandete die Gleichsetzung von Interviewzahl, Frageuniversum und auswertbarer Fragebasis. In Runde 2 blieb im Ausnahmeweg die Aussage bestehen, Anteile seien auf alle Befragten bezogen; auch der bestimmte Nennervergleich mit dem ESS war unbelegt. Die verlangte enge Korrektur ist jetzt umgesetzt.

Abschnitt 6 Nr. 3, Zeile 132, schreibt vor:

> Anteile und Kategorien wie veröffentlicht, einschließlich der Kategorie ‚Weiß nicht‘. Die genaue auswertbare Fragebasis und der Umgang mit Verweigerungen und sonstigen fehlenden Antworten sind nicht dokumentiert.

Das Frageuniversum „Base: All respondents“ steht getrennt als Quellenangabe. Der Text verbietet die Umrechnung auf gültige Antworten und den Nennervergleich mit dem ESS, solange die Fragebasis nicht dokumentiert ist. Er behauptet weder, dass Verweigerungen im Nenner enthalten sind, noch dass sie ausgeschlossen wurden.

Die übrigen erforderlichen Grenzen bleiben bestehen:

- Zeilen 120–129 trennen Frageuniversum, gewichtete Tabellenbasis, Interviewzahl, ungewichtete Fragebasis und Missing-Regel. Die Interviewzahl ist nur ein Wellenmerkmal.
- Zeile 131 sperrt Zahlen standardmäßig bis zur Klärung der ungewichteten Fragebasis und des Missing-Umgangs.
- Zeile 132 verlangt für eine Übernahme ohne Klärung Stevens ausdrückliche Freigabe.
- Zeilen 133–137 verbieten Normierung, Handkorrektur und selbst berechnete Unsicherheit ohne Design; die doppelte Übertragung bleibt vorgeschrieben.

S1, Zeilen 12–14 und 158–163, meldet die ungewichtete Fragebasis und Missing-Behandlung als nicht dokumentiert. Die Anfrage an das Eurobarometer-Team, Zeile 60, fragt sie weiterhin ausdrücklich an. Damit ersetzt der korrigierte Hinweis keine unbekannte Größe durch eine Behauptung.

Die synthetische Gegenprobe nutzt ausschließlich erfundene Größen: 100 Personen im Frageuniversum, zehn Verweigerungen und zehn Weiß-nicht-Antworten. Frageuniversum und Weiß-nicht-Kategorie allein entscheiden nicht zwischen einem Nenner von 100 und einem von 90. Die neue Formulierung legt sich auf keinen davon fest. Der Inline-Lauf bestätigte die Textgrenzen und die zwei rechnerisch unterscheidbaren Möglichkeiten. Das ist eine Prüfung der Planregel, kein Test eines vorhandenen Extraktors.

Der ursprüngliche Schweregrad mittel bleibt historische Einordnung. Es besteht kein verbliebener Fehler von F01 im geprüften Text. Keine weitere Plankorrektur für dieses Finding erforderlich. Eine spätere Anzeige muss den vorgeschriebenen Hinweis und die Freigabegrenze tatsächlich einhalten.

## Unmittelbare Folgen der Änderungen von Fassung 0.4

Der erlaubte Vergleich war git diff f2c8d0d -- docs/. Die Änderungen betreffen den Hauptplan, die Entscheidungsvorlage und den Nachtrag zur Abdeckung.

Die neue Statusdefinition in Abschnitt 4.6 verlangt belegte Bedingungen 4.1 Nr. 1 bis 6 und 8 für vorgeschlagene Kandidaten. Fehlender deutscher Originalwortlaut führt zur Zurückstellung; eine eigene Übersetzung genügt nicht. Abschnitt 11.3 und die Entscheidungsvorlage setzen das für alle zehn Q19-Items um. Rechteklärung, Klasse-Q-Grundsatzentscheidung und Originalwortlaut bleiben gesonderte Voraussetzungen. Die unveränderte Regel, ein nicht gewähltes Mehrfachauswahl-Item nicht als Ablehnung auszulegen, bleibt erhalten.

SP568 QC9 bleibt ausgeschlossen, nun wegen des Wichtigkeitsformats laut R6/R8. Die Zuschreibung ist im Plan ausdrücklich genannt. R6 Zeile 204 und der R8-JSON-Eintrag R8-EB-SP568-QC9 tragen diese begrenzte Grundlage; derselbe Eintrag nennt den fehlenden deutschen Wortlaut und nicht zitierte Kategorien. Ich bestätige hier die Regelbindung und den fortbestehenden Ausschluss. Eine unabhängige Bestätigung der deutschen Originalskala erfolgte nicht. Aus der Änderung folgt keine neue Aufnahme oder Wortlautfreigabe.

Die Entscheidungsvorlage, Zeile 33, und der Abdeckungsnachtrag, Zeile 99, unterscheiden jetzt die Geltungsbereiche je Frage. Das bleibt eine Kennzeichnung getrennter Einzelreferenzen. Es schafft keine gemeinsame Population, Verteilung oder nationale Abdeckung. Der frühere Text ist als damaliger Stand begrenzt; im Nachtrag ist die für v2.3 geltende Zuordnung ausdrücklich benannt.

Registerfestschreibung, ergebnisblinde Auswahl, Grenzen der technischen Rolle, doppelte Übertragung, Designgrenzen, ESS12-Vertrag und die Freigabefolge bleiben erhalten (Plan Zeilen 104–106, 131–148 und 173–177). Keine neuen Methoden- oder Reproduzierbarkeitsfindings im benannten Änderungsumfang. Das ist kein Urteil über die P5-Findings und keine erneute Auswahlprüfung aller Kandidaten.

## Checks

| Check | Urteil | requiredInScope |
| --- | --- | --- |
| P4-R3-PIN | BESTANDEN | true |
| P4-R3-F01 | BESTANDEN | true |
| P4-R3-DELTA | BESTANDEN | true |
| P4-R3-LATER | IN_DIESER_PHASE_NICHT_ERFORDERLICH | false |

Das JSON hält F01 sowohl in findings.state als auch in ratings.correctionStatus als KORRIGIERT fest, mit blocksScope false. Nur F01 wird erneut als Finding beurteilt.

## Grenzen und tatsächlicher Zugriff

- Begrenzte Nachprüfung von P4-V23-F01 und unmittelbaren Methoden-/Reproduzierbarkeitsfolgen der Änderungen 0.3 zu 0.4. Keine neue Gesamtprüfung; P4-F02 bis F06 werden nicht neu abgenommen.
- Kein Urteil über P5-Findings. Keine P5-Berichte geöffnet oder gehasht. Ihre Pfade im Manifest und die Autorzusammenfassung im erlaubten Plan/Diff waren sichtbar.
- Keine Dateien unter data/raw/, data/local/ oder outputs/ gelesen. Keine data/reference-* Dateien geöffnet; keine lokalen Antwortverteilungen oder externen Ergebnistabellen gelesen, keine GESIS-Server aufgerufen.
- Kein Abruf von Originalquellen in diesem Lauf. F01 wird an Plantext, P4-Vorberichten, gepinntem Strukturbericht S1 und Anfrage geprüft. SP568 QC9 nur als ausdrücklich R6/R8 zugeschriebene Ausschlussgrundlage geprüft; deutsche Originalskala nicht unabhängig bestätigt.
- Manifest enthält 27 Artefakte, davon 23 ohne P5. Nur diese 23 wurden vor der abschließenden Bewertung gegen ihre Manifesthashes und den genannten Commit gebunden; vier P5-Artefakte absichtlich ausgelassen. Weitere Eingaben separat gehasht.
- Der commit-Eintrag des Manifests ist 42b6068b22a0c4fd413c4dac65ed6675b4192d6a; der Auftrag nennt f169a1dbc704ef50bb94f8babeb0fe55a9a7f49d. Alle 23 zulässigen Manifestartefakte sind am genannten Auftragscommit bytegleich; die authentifizierte Manifestnotiz und der Hauptplan nennen Entwurf 0.4.
- Mehrere Sammelausgaben wurden gekürzt; Hauptplan, F01 und tragende Fundstellen wurden anschließend gezielt erneut gelesen. Andere Teile der Vorberichte dienen nur als Kontext.
- Memory-Register nur für prozedurale Grenzen konsultiert, keine Rolloutberichte geöffnet. Daraus stammt kein fachliches Urteil über v2.3.
- Keine technische Sandbox behauptet. Hash-/JSON-Funktionen lesen Datei-Bytes; das ist keine vollständige Inhaltsprüfung.
- Kein pnpm check, Pipeline- oder Browserlauf, keine Implementierung geändert. Nur eigene Prüfberichte, gezielte Textassertionen, synthetische Gegenprobe, Schema-/Urteilsprüfung und Hashkontrollen.
- JSONSchema-Bibliothek nicht installiert; kein Installationsversuch. Formale Kontrolle mit einem Inline-Validator für sämtliche im vorliegenden Schema verwendeten Validierungsregeln.
- BESTANDEN gilt nur für diesen Plan-Nachprüfungsumfang. Keine empirische Validierung, Neutralitäts-, Humanexperten-, Produkt-, Quellen-, Export- oder Releasefreigabe. Stevens Entscheidungen und spätere Prüfungen bleiben Voraussetzungen.
- Nur die zwei autorisierten Ausgabedateien geschrieben. Keine Commits, Tags, Pushes, Delegation oder Nachrichten an Dritte.

## Gelesene Eingaben mit Hash

„Gelesen“ umfasst vollständige Texte, begrenzte Ausschnitte, Suchtreffer und gezielte JSON-Projektionen. Die P4-Berichte wurden nur im erlaubten Rollenumfang gelesen; F01 wurde gezielt erneut aufgerufen. Die Rechercheberichte wurden an den tragenden Stellen gelesen, nicht neu insgesamt geprüft. Das Memory-Register lieferte nur prozedurale Hinweise (Zeilen 52–55); keine Rollouts wurden geöffnet.

| Eingabe | SHA-256 |
| --- | --- |
| docs/analyseplan-v2.3.entwurf.md | c8af28353e85161e617aa1f29ed65afb5cedfc34350c6e8fde0aef8ca8114bef |
| docs/entscheidungsvorlage-erweiterung-v1.entwurf.md | 43a38f7ce21c19d7194a214805057aec7f8476f3df7cd7bd49d2dbbc4aad0bd8 |
| docs/abdeckung-v2.2.md | 544deeb3055ffb174d8e3c97f6f4e5b6a640c8502113462cd3b6bcee6cb5e8f9 |
| docs/quellenanfragen-v1.entwurf.md | d9a4b0b67a73a1669ad07fed7461237cb08c0df0b0f1eacb02b4918a2727e972 |
| docs/analyseplan-v2.2.md | 13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8 |
| docs/profilregeln-v1.md | 3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23 |
| reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.md | 6830b4172d606b47fc6f00214fba09d776790143c85c01529b7c33256691c24b |
| reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json | 23e27dd8c2c1e359fe62ff5df058fef4de749dce95ca1e6da44cec6839e49fa2 |
| reports/claude/agenten/S1-strukturpruefung-eurobarometer.md | 15b2851d4e383a50ae064b566b1f2d6419180d3899f20007b49c07fe607295c0 |
| reports/claude/agenten/R6-eurobarometer.md | 58b08b2af20d70261e95e7d0d815d4c083d95e0879cef5ee864c6ee05e84e8bb |
| reports/claude/pruefungen/P4-methoden-v23.md | e1aecf135e7bb3cf3a56a55459b25f24f3f09a4349e788278fefc20568292355 |
| reports/claude/pruefungen/P4-methoden-v23.json | 2b6df5d37b09bc481cafce926e36e4827c842147910e93a51abe1c346d18462d |
| reports/claude/pruefungen/P4-runde2-methoden-v23.md | 4c7e509df82136784262d87e29281ab039f5eded359d94c1db5bf420b8b0b5f8 |
| reports/claude/pruefungen/P4-runde2-methoden-v23.json | f2d541fcf8bca2d1d215e9d11f4ddb139b48a708637d0b432c965d8cca38df4b |
| reports/claude/auftraege/P4-runde3-plan-v23.md | d9e089f03ed323137fc259782a96186c5334bf9dd2e06c0e9159ccef11d5780f |
| reports/claude/pruefungen/PLAN-V23-003-manifest.json | 96b20f220f8757a24ce880eee106e9fa7cd2aca3c234410786acd32d7a6a347d |
| .claude/skills/life93-review/SKILL.md | 90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6 |
| .claude/skills/life93-review/references/urteil-schema.json | 5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9 |
| .agents/skills/unslop/SKILL.md | c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56 |
| docs/project.md | 2ff27e5aa553ea2307bd4d28da436991c5ebb3b019f316d9aae95ee81d57696a |
| docs/pruefregeln.md | 29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233 |
| /home/stevenh/.codex/memories/MEMORY.md | 76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9 |

## Nur gehashte Manifestartefakte

Keine inhaltliche Prüfung dieser Dateien in Runde 3.

| Eingabe | SHA-256 |
| --- | --- |
| reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.md | 42aaa648a36557d33b6bb316aff007f5f79f92779aa4875acdc74516c70ba5c3 |
| reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.json | 71e012d3b460917269153d261a4565f6bfbb34627220ee2cf14d8abf1af272d6 |
| reports/claude/agenten/R10-quellenblocker.md | 65d79b32748197923c9614c7e8e85f19b06f516fa0cff869dbb7d3cf2f228885 |
| reports/claude/agenten/R10-quellenblocker.json | 8e15381892d91f62094c68573bb32148a5df21daf24ad11415549ef94861439a |
| reports/claude/agenten/S1-strukturpruefung-eurobarometer.json | f563bc2f138d67a00a9cf8fbfd80580dd3e842108d17231b44efb241edbc9575 |
| reports/claude/agenten/R5-wvs.md | a163be6d448ab5f9e14b54293f355a2e0cea3c19d37e92a4d0021e8af7afc969 |
| reports/claude/agenten/R7-weitere-quellen.md | 4e795f355ccd359613949a2e307f46150f31506cf817b51f1a4e232405f6fcd5 |
| reports/claude/auftraege/R-erweiterung-gemeinsam.md | 56970a37d162e3996cace441b4f41c44d7e4e3bfd408d008c13e3f9ba0898ccd |
| data/gruppenvertrag.v2.1.entwurf.json | 9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702 |

## Ausgeführte Befehle und Werkzeuge

Alle Shellaufrufe liefen über functions.exec/exec_command. Python lief mit PYTHONDONTWRITEBYTECODE=1; kein Prüfsystem oder Hilfsskript wurde als weitere Datei angelegt.

- sha256sum reports/claude/auftraege/P4-runde3-plan-v23.md reports/claude/pruefungen/PLAN-V23-003-manifest.json.
- cat des Auftrags, Manifests, life93-review/SKILL.md, urteil-schema.json und unslop/SKILL.md.
- git status --short; git branch --show-current; git rev-parse HEAD; git diff f2c8d0d -- docs/.
- rg -n mit P4, PLAN-V23, bounded und begrenz im Memory-Register; sed -n 52,58p desselben Registers.
- cat, nl -ba, sed und wc -l auf docs/project.md, pruefregeln.md, profilregeln-v1.md, analyseplan-v2.2.md, abdeckung-v2.2.md, analyseplan-v2.3.entwurf.md, entscheidungsvorlage-erweiterung-v1.entwurf.md und den zwei P4-Markdown-Vorberichten. Mehrere Sammelausgaben wurden gekürzt; der Hauptplan wurde danach in 1–175 und 176–285 aufgeteilt, F01 in Runde 1 (66–88) und Runde 2 (1–48) erneut gelesen.
- rg -n für P4-V23-F01, Überschriften, Base, fehlend, QC9 und S1 in den zwei P4-Berichten, S1, R6, R8 und Quellenanfragen; danach rg -n -F QC9 ausschließlich in R6. Keine Suche in ausgeschlossenen Datenordnern.
- nl -ba mit sed-Ausschnitten: S1 1–20 und 150–170; Quellenanfragen 49–65; R6 236–266 und Treffer 204; R8 156–173 und 234–242; Entscheidungsvorlage 1–75; Prüfregeln 40–61.
- Inline-Python: Manifest laden, vier P5-Pfade ausschließen, SHA-256 aller übrigen 23 Artefakte vergleichen; git show f169a1dbc704ef50bb94f8babeb0fe55a9a7f49d:<Pfad> gegen Arbeitsdateibytes prüfen. ALL_ALLOWED_MANIFEST_PINS_OK 23; COMMIT_MATCH_FOR_ALLOWED_ARTIFACTS True.
- Inline-Python: ausschließlich F01 und zugehörige ratings aus den zwei erlaubten P4-JSONs ausgeben; R8-JSON auf den Eintrag R8-EB-SP568-QC9 projizieren.
- Inline-Python: importlib.util.find_spec für jsonschema ergab False; 31 lokale Eingabehashes erfassen; Abwesenheit der eigenen Ausgabedateien prüfen; F01-Textassertionen und synthetische Nennergegenprobe durchführen. F01_TEXT_ASSERTIONS_OK.
- functions.apply_patch: ausschließlich P4-runde3-methoden-v23.md und P4-runde3-methoden-v23.json anlegen.
- Abschließendes Inline-Python: JSON gegen alle verwendeten Schlüsselwörter des Urteilsschemas prüfen; erforderliche Checks, Finding-/Rating-Konsistenz und Berichtstext kontrollieren; alle 31 Eingabehashes erneut vergleichen. git status --short und git diff --name-only prüfen den abschließenden Schreibumfang. Diese formalen Prüfungen sind keine fachliche Validierung.

## Abschlusskontrolle bei paralleler Arbeit

Während der Abschlusskontrolle wechselte HEAD durch fremde parallele Arbeit auf d70a91302aa7b47f5827c2b71b3576a56cbfdcf5. Die zwei P5-Runde-3-Dateien wurden zusätzlich als fremde untracked Pfade sichtbar, ohne Inhaltszugriff. Alle 31 gebundenen Eingabehashes blieben unverändert. Der erste Abschlussprüflauf bestand Schema, drei negative Schemaproben, Urteilskonsistenz und Hashvergleich, scheiterte danach an seiner zu strengen Assertion eines unveränderten HEAD. Danach wurde die konkrete Artefaktbindung statt HEAD-Stabilität kontrolliert; keine eigene Commitoperation.

Die anschließende Kontrolle verlangt weiterhin bytegleiche Eingaben, keine Änderungen an getrackten Dateien und die zwei eigenen Ausgaben. Fremde P5-Pfade werden nur als Pfade erfasst. Der Befund betrifft die Prüfumgebung; die gepinnte fachliche Prüffassung hat sich nicht geändert.

## Modell laut Laufzeit

OpenAI, Codex-Harness in T3 Code, gpt-6.1-sol mit high reasoning effort laut Laufzeitmetadaten. Konkrete interne Modellrevision unbekannt. Keine Claude-Ausführung, kein weiterer Prüfagent. Der ursprüngliche Nutzerprompt ist im JSON unter execution.prompt erhalten; der zusätzliche Auftragsinhalt ist durch den oben genannten Hash gebunden.
