# P1 Runde 2: Methoden-Korrekturprüfung

Gesamturteil: **NICHT_BESTANDEN** für die Festschreibung von `PLAN-V22-002`, Analyseplan v2.2 Fassung 1.1. F01, F02, F04, F08 und F10 bleiben teilweise offen. F03, F05, F06, F07 und F09 sind behoben. Keine neuen Findings.

Prüfdatum: 3. Oktober 2026. Modus: gezielte Nachprüfung. Branch zu Beginn: `research/life-93-claude-20261003`; Arbeitsbaum anfangs sauber. Auftragshash `32cf0f009f03d2d21fb424ba6883057f27131f2c95d575ad5d8c314338f87160`, Manifesthash `67506f10f9cfb2a56a352d7cec31f25671207fabd0aa421ca9fc88a3e4644eab`. Alle 40 Manifest-Eingaben stimmten zu Beginn.

**Standgrenze:** Nach der Profilprüfung änderte parallele Arbeit `profile-structure.ts`; der Abschlussstand stimmt damit nicht mehr vollständig mit dem Manifest überein. Die Einzelurteile unten beziehen sich auf die anfänglich geprüfte Fassung. Die neue Fassung wird hier nicht beurteilt.

## Status je ursprünglichem Finding

| Finding | Status | Blockiert Festschreibung |
| --- | --- | --- |
| P1-V22-F01 | TEILWEISE | ja |
| P1-V22-F02 | TEILWEISE | ja |
| P1-V22-F03 | BEHOBEN | nein |
| P1-V22-F04 | TEILWEISE | ja |
| P1-V22-F05 | BEHOBEN | nein |
| P1-V22-F06 | BEHOBEN | nein |
| P1-V22-F07 | BEHOBEN | nein |
| P1-V22-F08 | TEILWEISE | ja |
| P1-V22-F09 | BEHOBEN | nein |
| P1-V22-F10 | TEILWEISE | ja |

## P1-V22-F01: TEILWEISE

Geprüfte ursprüngliche Zusage: Der Runner übernimmt die v2.1-Gruppenzuordnung und deren Eingangsprüfung.

Vollständige Inventarprüfung und Inkonsistenzzählung funktionieren. Es fehlen die getrennten Missing-Gründe für Wahl und Partei sowie valid_named_party versus valid_other_unlabelled.

Beleg und Nachprüfung: pipeline/v22/run_v22.py:187–226; data/gruppenvertrag.v2.1.entwurf.json:3406–3413. Gegenprobe F01 in /tmp/p1-runde2-probes.py: Wahl 7/8/9 und Partei 77/88/99 jeweils nur source_missing: 3; benannte Partei und Other gemeinsam valid: 2. Other bleibt korrekt gruppierbar. Unbekannte Partei wird auch bei vote=2 abgelehnt.

Auswirkung: Die privaten Ausschlüsse sind weiterhin nicht in der vertraglich zugesagten Auflösung nachprüfbar; kein falscher Anteil belegt.

Schweregrad: mittel. Verbleibende konkrete Vertrags-, Schutz- oder Bindungslücke vor Festschreibung; kein empirischer Rechenfehler oder reale Exposition behauptet.

Korrektur: Missing-Gründe je Feld separat zählen und gültige Parteien anhand des Vertrags in named/other unterscheiden. Vollständige Bilanzen mit allen Zuständen synthetisch nachprüfen.

## P1-V22-F02: TEILWEISE

Geprüfte ursprüngliche Zusage: Gewichtsprüfungen und Diagnostik aus v2/v2.1 bleiben erhalten.

anweight wird positiv und endlich validiert. Die Verhältnisdiagnose verwendet jedoch alle deutschen Fälle, OR zwischen absoluter und relativer Toleranz und kein not_evaluable_no_eligible_group_cases. Der Gruppenvertrag verlangt eligible cases, absolute_and_relative und den Leerstatus.

Beleg und Nachprüfung: pipeline/v22/run_v22.py:263–274; data/gruppenvertrag.v2.1.entwurf.json:3443–3452. Gegenprobe F02: Nur ein ausgeschlossener Nichtwähler hat ein anderes Verhältnis; Diagnose ist False trotz konstantem Verhältnis aller Berechtigten. Bei Basis 0,5 und Änderung 0,75e-12 ergibt sich relativeSpread=1,4999e-12, dennoch constantWithin1e12=True. Leere, negative, nullwertige und nichtendliche anweight werden abgelehnt.

Auswirkung: Die diagnostische Aussage weicht vom gebundenen Vertrag ab; die Primäranteile werden dadurch nicht geändert.

Schweregrad: mittel. Verbleibende konkrete Vertrags-, Schutz- oder Bindungslücke vor Festschreibung; kein empirischer Rechenfehler oder reale Exposition behauptet.

Korrektur: Gruppendiagnose auf berechtigte Fälle und erstes berechtigtes Verhältnis beziehen, beide Toleranzbedingungen und leeren Fallkreis umsetzen. Eine zusätzliche gesamtdeutsche Diagnose getrennt benennen.

## P1-V22-F03: BEHOBEN

Geprüfte ursprüngliche Zusage: Die Serialisierung akzeptiert keine Whitespace-Abweichungen.

CANON.fullmatch verhindert den bisherigen Endzeilenumbruch-Fehler für Frage-, Wahl- und Parteifelder.

Beleg und Nachprüfung: pipeline/v22/run_v22.py:60–64,113–129,187–199. Gegenproben F03: 1/1.0/1.00 akzeptiert; 1\n, Leerzeichen, +1, 1e0, 01 sowie Partei-Endzeilenumbruch abgelehnt. test_unknown_codes_fail_the_study besteht.

Auswirkung: Das belegte Serialisierungsproblem ist aufgelöst.

Schweregrad: mittel. Direkt reproduzierbare Abweichung von der vorab gebundenen Parserregel.

Korrektur: Keine weitere Korrektur für dieses Finding erforderlich.

## P1-V22-F04: TEILWEISE

Geprüfte ursprüngliche Zusage: Der Lauf schreibt ausschließlich eine private Ausgabe unter data/local/v22.

Der freie --out-Parameter entfällt; fester Pfad, Symlink-Flucht und vorhandene Ausgabe werden verhindert. Ein vorhandenes Verzeichnis mit zu offenen Rechten wird weiterhin akzeptiert, obwohl 0700 zugesagt ist.

Beleg und Nachprüfung: pipeline/v22/run_v22.py:339–359; Kopfzeilen 11–12. Gegenprobe F04: importiertes main() mit vollständig synthetischer /tmp-Wurzel, gemocktem gate/run und vorhandenem v22-Verzeichnis 0755 schreibt erfolgreich, Verzeichnis bleibt 0755; Datei erhält 0600. Symlink-Flucht wird vor mkdir und run abgelehnt, bestehende run.json nicht überschrieben.

Auswirkung: Die Verzeichniszusage bleibt falsch. 0600 schützt den Dateiinhalt im geprüften 0755-Fall; keine tatsächliche Offenlegung behauptet. Ein schreibbares vorhandenes Verzeichnis würde zusätzlich Manipulation ermöglichen.

Schweregrad: mittel. Verbleibende konkrete Vertrags-, Schutz- oder Bindungslücke vor Festschreibung; kein empirischer Rechenfehler oder reale Exposition behauptet.

Korrektur: Vor mkdir/run vorhandene private Verzeichnisrechte prüfen und bei unzureichendem Modus fest abbrechen, ohne fremde Rechte zu verändern. Bestehende 0755/0777-Verzeichnisse und neue 0700/0600-Ausgabe synthetisch prüfen.

## P1-V22-F05: BEHOBEN

Geprüfte ursprüngliche Zusage: Das Tag analyseplan-v2.2 bindet die geprüfte Festschreibung vor der Rechnung.

Das Gate bindet lokalen und entfernten Tag-Commit sowie die sechs festgeschriebenen Plan-, Vertrags- und Rechendateien. run() ist ausdrücklich Bibliothek für synthetische Tests, kein Zugriffsgate.

Beleg und Nachprüfung: pipeline/v22/run_v22.py:15–16,305–336,339–351; docs/analyseplan-v2.2.md:119. Gegenprobe F05 im isolierten /tmp-Git-Repository: fehlender Tag und abweichender origin-Tag abgelehnt; passender Lightweight-Tag akzeptiert; jede der sechs einzelnen Dateimutationen abgelehnt. Keine Tags im Projekt erzeugt, keine echte Datei geöffnet.

Auswirkung: Die konkret beanstandete bloße Tag-Existenzprüfung ist ersetzt. Ein Tag ist weiterhin kein Nachweis menschlicher oder wissenschaftlicher Freigabe.

Schweregrad: erheblich. Existenz allein sichert die zentrale Reihenfolge Prüfung/Festschreibung/abhängige Analyse nicht.

Korrektur: Keine weitere Korrektur für das ursprüngliche Finding erforderlich; spätere Freigaben bleiben getrennt.

## P1-V22-F06: BEHOBEN

Geprüfte ursprüngliche Zusage: Jeder deutsche Katalogtext wird automatisch mit dem Original-PDF abgeglichen.

Zusätzliche gültige Kategorien werden vor Ausgabe gegen das Fragebogen-PDF geprüft und ausdrücklich ihrem Code zugeordnet.

Beleg und Nachprüfung: pipeline/v22/catalogue_v22.py:318–334. Gegenprobe F06: falscher Code-55-Text scheitert am Originaltextabgleich; richtiger Text mit Code 54 scheitert an label/code binding mismatch. Unveränderter catalogue_v22.py --check besteht.

Auswirkung: Der konkrete ungeprüfte Zusatzcode und die ignorierte extraValid-Codeangabe sind behoben.

Schweregrad: mittel. Nachgewiesene Lücke in einer ausdrücklich zugesagten Quellenprüfung.

Korrektur: Keine weitere Korrektur für dieses Finding erforderlich.

## P1-V22-F07: BEHOBEN

Geprüfte ursprüngliche Zusage: Der Querbezug Absicherung bei Armut und Bedarf enthält basinc; Plan und Profilregeln nennen dieselbe feste Struktur.

basinc ist Teil des Querbezugs social_protection; Plan, Dokumentation und Code enthalten sieben Querbezüge und dieselben Mitglieder.

Beleg und Nachprüfung: web/src/app/policy-draft/profile/profile-structure.ts:152–230 der anfänglich manifestgebundenen Fassung; docs/profilregeln-v1.md:49–57; docs/analyseplan-v2.2.md:101. Profiltest sofrpr=1/basinc=4 besteht mit zwei Antworten; zusätzlich alle sieben dokumentierten Mitgliedermengen maschinell gegen die Regeln verglichen.

Auswirkung: Die fehlende Frage und falsche Anzahl aus dem ursprünglichen Finding sind behoben. Die Tabelle nennt weiterhin den alten Titel Absicherung bei Armut und Bedarf; dies ändert die hier geprüften Mitglieder nicht und ist kein zusätzliches P1-Blockfinding.

Schweregrad: mittel. Konkrete Abweichung des vorab festzulegenden Profilvertrags.

Korrektur: Keine weitere Korrektur für den ursprünglichen P1-Mitglieder-/Anzahlbefund erforderlich.

## P1-V22-F08: TEILWEISE

Geprüfte ursprüngliche Zusage: T01–T30 sind in profile-engine.spec.ts umgesetzt.

T14, neue Blockmuster und offeredCategories sind geprüft. Die behauptete vollständige T30-Abdeckung durch den cttresa-Komponententest fehlt weiterhin.

Beleg und Nachprüfung: docs/profilregeln-v1.md:85; web/src/app/policy-draft/profile/profile-engine.spec.ts:332–390; web/src/app/policy-draft/policy-draft.spec.ts:357–392; reports/claude/agenten/R4-profilform.md:365. Der angeführte Test nutzt einen realen Referenzfixture, wählt für cttresa keine eigene Antwort, setzt keinen synthetischen no_valid_answers-Fall und prüft keinen Erhalt der eigenen Aussage. 23 Profiltests inklusive T14 bestehen im TypeScript-/Assertion-Adapter.

Auswirkung: Die Dokumentation erklärt eine unvollständige Anzeigeprüfung als vollständig abgedeckt. Dies beweist keinen Fehler der Anzeige selbst.

Schweregrad: mittel. Verbleibende konkrete Vertrags-, Schutz- oder Bindungslücke vor Festschreibung; kein empirischer Rechenfehler oder reale Exposition behauptet.

Korrektur: T30 synthetisch für withheld_base_or_cell_count und no_valid_answers mit beantwortetem Item prüfen: keine Prozentwerte, Fehlhinweis, eigene Aussage erhalten. Alternativ diese konkrete Anzeigeprüfung verbindlich als offen ausweisen.

## P1-V22-F09: BEHOBEN

Geprüfte ursprüngliche Zusage: Der 95-%-xlogit-Bereich beschreibt die Stichprobenunsicherheit unter dokumentierten Annahmen.

Die Nahe-Rand-Unterdeckung und fehlende Garantie effektiver Fallzahl bzw. nominaler Abdeckung sind ausdrücklich beschrieben.

Beleg und Nachprüfung: docs/analyseplan-v2.2.md:83; Originalmanual outputs/loop/methods/SURVEY-MANUAL.pdf, PDF-S.94. Gegenprobe F09: 100 Fälle, fünf seltene Antworten, stark konzentrierte Gewichte, df=99 ergeben Anteil 0,91356 und Bereich 0,58930–0,98732. Keine Abdeckungsvalidierung daraus abgeleitet.

Auswirkung: Die fehlende Einschränkung ist korrigiert. Das methodische Risiko bleibt ausdrücklich benannt und ist damit kein offener Dokumentationsbefund.

Schweregrad: mittel. Dokumentationsgrenze eines vertretbaren Standardverfahrens, kein nachgewiesener Rechenfehler.

Korrektur: Keine neue Methode oder ergebnisabhängige Schwelle verlangt.

## P1-V22-F10: TEILWEISE

Geprüfte ursprüngliche Zusage: Das Manifest bindet die vollständigen Eingaben des reproduzierbaren Prüfpakets.

Der ESS10-Dateimetadatencache ist jetzt manifestiert und alle Katalogquellen sind im Builder gepinnt. Benötigte Reproduktionsabhängigkeiten fehlen weiterhin im Manifest.

Beleg und Nachprüfung: pipeline/v22/catalogue_v22.py:38–48,293–296; PLAN-V22-002-manifest.json:166–167. Gegenprobe F10: abweichender Metadatenhash vor Build abgelehnt. Ungebunden bleiben pipeline/policy_reference_v2.py aus test_survey.py:15–17 sowie catalogue-types.ts, public-catalogue.ts, public-catalogue-v22.ts aus policy-catalogue.ts:2–5. policy-draft.spec.ts mit der behaupteten T30-Prüfung ist ebenfalls nicht manifestiert.

Auswirkung: Die Quellenbindung des Katalogs ist hergestellt; das veröffentlichte Prüfpaket bindet weiterhin nicht die vollständige tatsächlich benötigte Testgrundlage.

Schweregrad: mittel. Verbleibende konkrete Vertrags-, Schutz- oder Bindungslücke vor Festschreibung; kein empirischer Rechenfehler oder reale Exposition behauptet.

Korrektur: Benötigte öffentliche Helper und Profilkataloge sowie den zuständigen synthetischen T30-Test in ein neues Manifest aufnehmen; verbotene Antwortverteilungen nicht in diesen Prüfauftrag ziehen. Bindung vor Nachprüfung prüfen.

## Grenzen und Abschlussstand

- Gezielte KI-Korrekturprüfung, kein neues Gesamtaudit, keine wissenschaftliche oder menschliche Abnahme und keine Freigabe für Rechnung, Export oder Release.
- Keine Rohdaten, privaten Ergebnisse oder gesperrten Antwortverteilungen gelesen. run_v22.py nicht als CLI ausgeführt. Importiertes main() nur mit /tmp-Wurzel und gemocktem Gate/Runner für synthetischen Pfadtest.
- T30-Komponententest nur statisch gelesen, nicht ausgeführt: seine Imports würden gesperrte historische Antwortverteilungen lesen. Kein Browser-/Verständnistest.
- Profiltests per TypeScript transpileModule und eigenem Node-Assertion-Adapter im Speicher ausgeführt, nicht Vitest.
- pnpm check nicht ausgeführt: Build schreibt zusätzliche Artefakte und Gesamttests importieren gesperrte Antwortverteilungen. Der spezielle Prüfauftrag begrenzt Schreiben auf diese zwei Berichte.
- Alle 30 Artefakte und zehn Caches waren zu Beginn hashgleich. Fremde P2-Berichte und andere nicht benötigte Manifestberichte ausschließlich gehasht, nicht inhaltlich gelesen.
- Parallel änderte sich nach Profilprüfung profile-structure.ts: erwarteter Hash bd17d664b5cab042ec134025e0ce0393bba7a84b2174e546d2e00b083aead5de, Abschluss-Hash d7914d299efdbedb93e2de135ce2ee88e1c96752af6b4a20c570dbb759ba7b1b. Urteil und Status beziehen sich ausschließlich auf den anfänglich gebundenen Stand. Neuer Stand benötigt eigenes Paket; keine positive Aussage über ihn.
- Während der Prüfung erschienen fremde untracked generate-references-v22.mjs und reference-v22.ts. Nicht gelesen oder verändert. Keine eigenen Commits, Tags, Pushes oder Nachrichten an Dritte.

## Ausgeführte Befehle

- Zuerst `cat reports/claude/auftraege/P1-runde2-methoden.md`, danach `sha256sum` des Auftrags.
- `cat`, `nl -ba`, `sed`, `head`, `rg` und `ls` für die unten aufgeführten öffentlichen Methoden-, Software- und Instrumentdateien. Keine gesperrten Suchpfade.
- Python/hashlib: erwarteter Manifesthash, alle 30 Artefakt- und zehn Cachehashes; Abschlussprüfung identifiziert ausschließlich die dokumentierte Drift.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'`: zwölf Tests, OK.
- `PYTHONDONTWRITEBYTECODE=1 python3 pipeline/v22/catalogue_v22.py --check`: bytegleich.
- `PYTHONDONTWRITEBYTECODE=1 python3 /tmp/p1-runde2-probes.py`: synthetische Eingänge, Bilanzen, Verhältnisdiagnostik, importiertes main mit /tmp-Wurzel, Gate im isolierten Git-Repository, Katalogmutationen im Speicher und gewichteter Randfall. Zwei erste Anläufe brachen wegen eines für ESS5/ESS9 falsch angenommenen synthetischen Other-Codes 55 ab; Fixture gegen das gelesene ESS9-Inventar auf 9 korrigiert, vollständiger letzter Lauf erfolgreich. Keine Produktdatei geändert.
- `pdftotext -f 94 -l 94 -layout outputs/loop/methods/SURVEY-MANUAL.pdf -`: Originalwarnung geprüft.
- `node /tmp/p1-runde2-profile.cjs`: erlaubnisbegrenzter In-memory-Loader, 23 Original-Profiltests und Vergleich der sieben Dokumentations-/Regelmitgliedermengen bestanden.
- `git branch --show-current`, `git status --short`: Anfangsstand und fremde Abschlussdateien erfasst.
- Erstellung ausschließlich dieser beiden Berichte; anschließend Ajv-2020-Schemaprüfung, Prettier-Formatierung und Formatprüfung ausschließlich der beiden Berichte.

## Gelesene Eingaben mit SHA-256

Auch indirekt gelesene Katalog-/Testabhängigkeiten sind aufgeführt. R4, Komponententest und einige Hilfsdateien nur in relevanten Ausschnitten; PDF-Handbuch S.94 und Katalog-PDFs an den Fundstellen. Nicht inhaltlich gelesene Manifestberichte fehlen hier bewusst; ihre Hashprüfung war vollständig. Der Hash von profile-structure.ts ist der gelesene Anfangsstand, die spätere Drift steht oben. Installierte Werkzeugpakete sind keine manifestierten fachlichen Eingaben.

| Datei | SHA-256 |
| --- | --- |
| `reports/claude/pruefungen/PLAN-V22-002-manifest.json` | `67506f10f9cfb2a56a352d7cec31f25671207fabd0aa421ca9fc88a3e4644eab` |
| `reports/claude/auftraege/P1-runde2-methoden.md` | `32cf0f009f03d2d21fb424ba6883057f27131f2c95d575ad5d8c314338f87160` |
| `.claude/skills/life93-review/SKILL.md` | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `.agents/skills/unslop/SKILL.md` | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `docs/project.md` | `7cfa1d4046eb30ae4b29728c49fa90baff89f40e56199b8eff0a738ca004e270` |
| `docs/pruefregeln.md` | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` |
| `docs/analyseplan-v2.2.md` | `bd8b23339f85d78e51ca5fc4e2e14d03c2beec1324f0e27b56382626f94a1e29` |
| `docs/profilregeln-v1.md` | `b880088d2221c2da3baab236be61b9970561c0ef25c67a753534f6ee4905a727` |
| `docs/abdeckung-v2.2.md` | `f3f03912f38dc7149b73739bc18fa9bcec59c65f6cb77edfd130be3c8e2d1b10` |
| `reports/claude/pruefungen/P1-methoden-v22.md` | `d479242f5d075b23f9379bf6dbce9cf8199f8a29f6236d446578b57c17eadb00` |
| `reports/claude/pruefungen/P1-methoden-v22.json` | `070af35fcb0ffc7c626e4bea40b142095ad9383ceb5f701965d94d75bd618a87` |
| `reports/claude/agenten/R4-profilform.md` | `8ea2b9ff837b6431d55acd051b45d5cba69eea3df1049878f748fe0655eddfa2` |
| `data/gruppenvertrag.v2.1.entwurf.json` | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `data/politikprofil-v2.2.ergaenzung.json` | `c4b0d97aeaf10868001199cb3f7f135a6fb8ec28d63b58f7f222ff7e0acd71ac` |
| `pipeline/v22/run_v22.py` | `a4c3ab0a78dcd44ae3f90b4e16df8ff07511a6e677bbaebd036cc232cd5a6ae4` |
| `pipeline/v22/survey.py` | `ef9011c5a9b9792373f7c9395d4e5db17a4381dab648480b2276ddac15a982bc` |
| `pipeline/v22/test_run_v22.py` | `74738a170672057de58ebc0e5b7cb8474ffc6f8581a8b767adffab4889c490b4` |
| `pipeline/v22/test_survey.py` | `dacdde363044981d575636447f6e206f89a0325353c8cc7b9a7898e1ca8ed011` |
| `pipeline/v22/catalogue_v22.py` | `f259365c04bdd8d783a90acbd5291838efb07b76e567b9de139197840568f2fc` |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `web/src/app/policy-draft/policy-catalogue.ts` | `9efc5f67a66952a86c1c427c83c5b40a557104b1573e7997470fff61259745f9` |
| `web/src/app/policy-draft/catalogue-types.ts` | `2599cfdf5c77ed912a85926b4e37a025b7d3661d1085749d27dbb5dc8be42822` |
| `web/src/app/policy-draft/public-catalogue.ts` | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |
| `web/src/app/policy-draft/public-catalogue-v22.ts` | `bc99055a10fb559cf2802d9a579ef3f07a3c8a77bdcc8556a2b08655d9d499cf` |
| `web/src/app/policy-draft/profile/profile-engine.ts` | `1b11d598a1743b611d2359fd354a03fc8bd90522293c6fa89c23c928b0b897fa` |
| `web/src/app/policy-draft/profile/profile-rules.ts` | `b07a153e0d9236c049048995a4122982df199c0c1781b44f2f8c8425b30905a2` |
| `web/src/app/policy-draft/profile/profile-structure.ts` | `bd17d664b5cab042ec134025e0ce0393bba7a84b2174e546d2e00b083aead5de` |
| `web/src/app/policy-draft/profile/profile-engine.spec.ts` | `901e4e1207fe9596681f70a3877e2a017b21222bf5ead063bcf205c19b1ea23b` |
| `web/src/app/policy-draft/policy-draft.spec.ts` | `c0eada8c2d7f2588a4da8bb04767b27a9e8d330165fef4b42896084897442cd9` |
| `package.json` | `451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7` |
| `web/package.json` | `77db8383e6c64f65fe04638c46ba3b7f9b40040d95f0ad3ced1471fb475d60f7` |
| `scripts/check-review-schema.mjs` | `2575997f720f0c440fc54a9ccc15a2bd8c8fb69638dab8c03cf8b9fdaf810166` |
| `outputs/loop/breadth-data-001/sources/ess5-de-questionnaire.pdf` | `24b5d2599e6d30dc02a6d835f5f80b5bcecf8f6014ee8f4670a703c25d3c3cbf` |
| `outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf` | `977475c18d2adebea6ccb7695f377fb6ed500ef087b077086305f9a2e4a7b239` |
| `outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf` | `dde02b5336b2d960c2900a8fcf5e2a0f0d254b46dcce1d9ffb785a830e096bc0` |
| `outputs/loop/breadth-data-001/sources/ess10-de-questionnaire.pdf` | `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425` |
| `outputs/loop/methods/SURVEY-MANUAL.pdf` | `87b0ea7088e0dfd587b4c4efacd38db68db8268a986a130c1a868ce2088bac2c` |
| `outputs/claude/sources/ess8-candidates.json` | `279f9c31b4236b71f4a820de7a2b519989ec796ad49ba4f2bde210c108d94168` |
| `outputs/claude/sources/ess10sc-candidates.json` | `2a5927d1ec1d322b2a127ff0c2c35862cbae8fc1ae39767aee410ff910ef8394` |
| `outputs/claude/sources/ess10sc-candidates-2.json` | `9ed9a9739dfe64b2cd8ebf2cc4cec8960ce29179b25d2013e90ff0dac53a038a` |
| `outputs/claude/sources/ess5-candidates.json` | `4b0247142d37697b4193e3373a37174849bcc16552d9764e34a51169170795a8` |
| `outputs/loop/breadth-access-002/sources/ess10sc-file-metadata.json` | `d9e6d606fb3b897d33d04f3247dbe5160d11f108a76fca6547a773e2c1ba0a57` |

## Modell laut Laufzeit

OpenAI, Codex-Harness in T3 Code, `gpt-6.1-sol`, Reasoning-Effort `medium`. Interne Modellrevision und interne Anbieterregeln sind nicht nachgewiesen. Dies ist ein KI-Review.
