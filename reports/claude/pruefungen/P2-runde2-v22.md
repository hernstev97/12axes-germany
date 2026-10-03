# P2 Runde 2: Quellen und politische Fairness

**Gesamturteil: BLOCKIERT.** Die abschließende Integritätskontrolle zeigt eine parallele Änderung an `profile-structure.ts`. Die Datei entspricht nicht mehr PLAN-V22-002. Ein neues Manifest und eine darauf bezogene Nachprüfung sind nötig. Für die zuvor vollständig hashgebundene, tatsächlich geprüfte Fassung lautet der fachliche Befund NICHT_BESTANDEN: F01 teilweise offen, F02–F05 behoben.

Prüfung am 3. Oktober 2026 auf Branch `research/life-93-claude-20261003`. Manifest: `67506f10f9cfb2a56a352d7cec31f25671207fabd0aa421ca9fc88a3e4644eab`. Auftraghash `b1464a894876371f065f8d681b680dd50e014b737b8792961a7ddf529ba4db55` stimmt. Manifest nennt Commit `691271dfdc6a02e349ee5905b4a5e591f424f311`; maßgeblich sind die Datei-Hashes. Anfangs passten alle 30 Artefakte und zehn öffentlichen Caches.

## Integritätsabweichung

```json
[
  {
    "path": "web/src/app/policy-draft/profile/profile-structure.ts",
    "expected": "bd17d664b5cab042ec134025e0ce0393bba7a84b2174e546d2e00b083aead5de",
    "actual": "d7914d299efdbedb93e2de135ce2ee88e1c96752af6b4a20c570dbb759ba7b1b"
  }
]
```

Diese Abweichung wurde vor jeglichem Berichtsschreiben erkannt; der erste Schreibaufruf brach bei seiner vorgeschalteten Hash-Assertion ab. Die danach geänderte Datei wurde nur erneut gehasht, nicht inhaltlich bewertet. Alle nachfolgenden Finding-Status beziehen sich auf die ursprüngliche gebundene Fassung.

| Finding | Korrekturstatus | Zustand | Blockiert fachlichen Umfang |
| --- | --- | --- | --- |
| P2-V22-F01 | TEILWEISE | OFFEN | ja |
| P2-V22-F02 | BEHOBEN | KORRIGIERT | nein |
| P2-V22-F03 | BEHOBEN | KORRIGIERT | nein |
| P2-V22-F04 | BEHOBEN | KORRIGIERT | nein |
| P2-V22-F05 | BEHOBEN | KORRIGIERT | nein |

## P2-V22-F01: TEILWEISE

Ursprüngliche Aussage/Entscheidung: Der Querbezug need_security bezeichnet alle vier Fragen als Absicherung bedürftiger Menschen.

Im geprüften Stand heißt der Code-Querbezug Soziale Absicherung und trennt Armut, Lebenslagen und universelles Grundeinkommen. Der Kontext ergänzt jedoch „staatliche Verantwortung für den Lebensstandard im Alter und bei Arbeitslosigkeit ohne Bedürftigkeitsprüfung“. E6/E7 spezifizieren eine solche Prüfung weder als Voraussetzung noch als Ausschluss. Fehlende Spezifikation trägt keine Behauptung eines Leistungsmodells ohne Prüfung. Die Profilregeln behalten außerdem den Titel Absicherung bei Armut und Bedarf.

Auswirkung: Einzelantworten können weiterhin einem nicht erfragten Anspruchsmodell zugeordnet werden; die Korrektur kehrt die zusätzliche Bedingung um, statt sie offen zu lassen.

Schweregrad: mittel. Fester Kontext ergänzt ein nicht erfragtes Leistungsmodell. Mittleres, lokal begrenztes Finding blockiert die Festschreibung der betroffenen Interpretation; kein Beleg eines empirischen Scheiterns des Gesamtprodukts.

Nachprüfung: S01 reproduziert den Kontext für erste und letzte Kategorien aller fünf Fragen sowie für nur E6=10/E7=0. Die Ausgabe-Assertions bestehen; der Quellenvergleich fällt für die behauptete Ausschließung der Bedürftigkeitsprüfung negativ aus.

Belege:

- web/src/app/policy-draft/profile/profile-structure.ts:161–171, ursprünglich hashgebundener Stand bd17d664…
- docs/profilregeln-v1.md:52
- outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf: PDF-S. 36 E6/E7, PDF-S. 43 E36
- data/politikprofil-v2.2.ergaenzung.json:1348–1353
- S01: zwei gegenläufige vollständige Antwortkombinationen und nur E6/E7; identischer fester Kontext.

Korrektur: Kontext etwa: „staatliche Verantwortung für einen angemessenen Lebensstandard im Alter und bei Arbeitslosigkeit; eine Bedürftigkeitsprüfung wird in diesen Fragen nicht spezifiziert“. Titel in docs/profilregeln-v1.md auf Soziale Absicherung ändern. Universelles Grundeinkommen getrennt erläutern.

## P2-V22-F02: BEHOBEN

Ursprüngliche Aussage/Entscheidung: Die lokale Auswahl ergänzt Gleichstellungsprinzipien, dokumentiert aber keine Entscheidung zu ESS8 B33A mnrgtjb.

Die fehlende Kandidatenentscheidung ist behoben. mnrgtjb ist als normatives Prinzip nach Abschnitt 3.1 aufgenommen und als Ergänzung ohne Dateneinsicht dokumentiert. Generator, Katalog, Profilregel und Abdeckung binden denselben Gegenstand.

Auswirkung: Die zuvor unbegründet ausgelassene eigenständige Facette ist enthalten. Daraus folgt kein genereller Neutralitätsnachweis.

Schweregrad: mittel. Die Auslassung betrifft einen vorhandenen, thematisch eigenständigen normativen Kandidaten und damit die vor Ergebniseinsicht zu begründende Auswahl. Das Finding verlangt keine automatische Aufnahme.

Nachprüfung: Aussage, Einleitung und deutsche Kategorien direkt gegen B33A und Liste 13 gelesen; alle gültigen Codes und englischen Labels mit API-Cache identisch. S02 bestätigt Zustimmung für 1/2, Mitte für 3 und Ablehnung für 4/5 bei unverändertem Originalsatz.

Belege:

- docs/analyseplan-v2.2.md:27–34,44
- docs/abdeckung-v2.2.md:35
- pipeline/v22/catalogue_v22.py:195–201
- data/politikprofil-v2.2.ergaenzung.json:1981 ff.
- web/src/app/policy-draft/profile/profile-rules.ts:561–569
- outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf: PDF-S. 12 B33A; ess8-de-showcards.pdf: PDF-S. 14 Liste 13
- outputs/claude/sources/ess8-candidates.json: data.search.v13
- S02: fünf Kategorien, Codes, englische Labels und ausgegebene Richtungen geprüft.

Korrektur: Aufnahme in einer neuen gebundenen Prüffassung umgesetzt; weitere Korrektur dieses Findings nicht erforderlich.

## P2-V22-F03: BEHOBEN

Ursprüngliche Aussage/Entscheidung: Die EU-Zeile nennt Finanzsolidarität pauschal unter Nicht erfasst.

Erfasst nennt jetzt das konkrete Programm mit stärkerer Finanzierung durch reichere Länder. Nicht erfasst ist ausdrücklich auf Finanzsolidarität außerhalb dieses einen Programms begrenzt.

Auswirkung: Der frühere Matrixwiderspruch ist behoben; die Antwort bleibt auf ein konkretes Paket bezogen.

Schweregrad: mittel. Erfasst/Nicht erfasst sind verbindliche Produkttexte. Der Widerspruch ist lokal korrigierbar und verlangt keine neue Analyse.

Nachprüfung: Alle drei Merkmale der Liste 55 direkt gelesen: minimaler Lebensstandard für alle Armen, Anpassung an nationale Lebenshaltungskosten, höhere Beiträge reicherer Länder. Die Matrix behauptet keine getrennte Bewertung der Merkmale oder allgemeine Finanzsolidaritätshaltung.

Belege:

- docs/abdeckung-v2.2.md:31
- data/politikprofil-v2.2.ergaenzung.json:1478–1480
- outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf: PDF-S. 44 E37
- outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf: PDF-S. 56 Liste 55

Korrektur: Beide Spalten präzisiert; keine weitere Korrektur dieses Findings erforderlich.

## P2-V22-F04: BEHOBEN

Ursprüngliche Aussage/Entscheidung: Für sämtliche sechs offenen Bereiche brauche das Projekt GESIS-Daten oder ESS12.

Die pauschale ESS12-Lösung ist entfernt. Kernfragen und Zuwanderung sind nur ein zu prüfender Aktualisierungsweg. Für die übrigen Lücken bleiben andere Quellen, Rechteklärung und weitere ergebnisblinde Recherche offen.

Auswirkung: Eine unbelegte Schließung sämtlicher sechs Lücken durch ESS12 wird nicht mehr versprochen.

Schweregrad: mittel. Die Zukunftsaussage widerspricht den herangezogenen Recherchegrenzen; sie betrifft den Plan für das Produkt, nicht die Wortlaute der 18 Fragen.

Nachprüfung: Korrigierte Aussagen mit den einschlägigen gebundenen R1–R3-Abschnitten abgeglichen. R3 beschreibt Kern-/Zuwanderungsfragen und fehlende deutsche Fassung; R1/R2 tragen keine ESS12-Lösung für ihre übrigen Bereiche. Kein erneuter Live-Abruf der externen ESS12-Quellen.

Belege:

- docs/abdeckung-v2.2.md:55
- docs/analyseplan-v2.2.md:48
- reports/claude/agenten/R1-themen-aussen-bildung-digital.md:153,159,262–263
- reports/claude/agenten/R2-themen-gesundheit-arbeit-wohnen.md:53
- reports/claude/agenten/R3-themen-reichweite.md:107–115

Korrektur: Zukunftsaussage auf dokumentierte Gegenstände begrenzt; keine weitere Korrektur dieses Findings erforderlich.

## P2-V22-F05: BEHOBEN

Ursprüngliche Aussage/Entscheidung: Die Profilregeln nennen basinc im Querbezug Absicherung; der Analyseplan nennt sechs Querbezüge.

Die Anzahl beträgt sieben. Sämtliche sieben Variablenlisten in Dokument und Code stimmen überein; basinc ist im Querbezug enthalten. Die verbleibende Titelabweichung wird unter F01 beurteilt.

Auswirkung: Die ursprünglich unklare Fragenzusammenstellung ist eindeutig gebunden.

Schweregrad: niedrig. Begrenzte Versions-/Dokumentationsabweichung ohne eigenen Nachweis einer politischen Verzerrung.

Nachprüfung: S03 extrahiert die sieben Markdown-Variablenlisten und vergleicht sie positionsweise mit den tatsächlich geladenen TypeScript-Regeln. Alle Assertions bestehen. S01 erzeugt fünf Antworten einschließlich basinc.

Belege:

- docs/analyseplan-v2.2.md:101
- docs/profilregeln-v1.md:49–57
- web/src/app/policy-draft/profile/profile-structure.ts:152–230, ursprünglich hashgebundener Stand bd17d664…
- S03: sieben Tabellenzeilen, sieben Code-Regeln, sämtliche Variablenlisten identisch; S01 enthält basinc.

Korrektur: Anzahl und Mitgliedschaft angeglichen. Die Titelkorrektur bleibt unter F01 offen.

## Synthetische Gegenproben

Ein `node -`-Aufruf transpiliert ausschließlich `profile-engine.ts`, `profile-rules.ts` und `profile-structure.ts` im Arbeitsspeicher mit dem vorhandenen TypeScript-Modul. Keine Imports des Gesamtkatalogs oder historischer Referenzen; keine Compilerdateien geschrieben.

- S01: fünf synthetische Items von social_protection. Je eine Kombination der ersten bzw. letzten gültigen Kategorien; dritte Kombination nur E6=10 und E7=0. Alle erzeugen denselben Kontext mit „ohne Bedürftigkeitsprüfung“. Vollständige Profile enthalten basinc. Die Ausgabe-Assertions bestehen, der fachliche Originalquellenvergleich fällt negativ aus.
- S02: alle fünf mnrgtjb-Kategorien gegen API-Code und englisches Label; tatsächlich ausgegebener Originalsatz unverändert, Richtung 1/2 positiv, 3 Mitte, 4/5 negativ. Alle Assertions bestehen.
- S03: sieben Markdown-Tabellenzeilen und sieben Code-Regeln; alle Variablenlisten positionsweise identisch. Alle Assertions bestehen.

F03/F04 sind direkte Quellen- und Dokumentationsprüfungen ohne Rechentest. Keine technischen Assertions als Beleg wissenschaftlicher Gültigkeit ausgegeben.

## Grenzen

- Gesamturteil BLOCKIERT wegen nachträglicher Hashabweichung. Die Finding-Status dokumentieren den zuvor vollständig gebundenen und tatsächlich geprüften Stand; für diesen wäre das fachliche Urteil NICHT_BESTANDEN wegen F01. Keine Bewertung der parallel geänderten Fassung.
- Gezielte KI-Nachprüfung, kein neues Gesamtaudit, keine empirische Validierung oder Releasefreigabe. Kein Finding der Stufe erheblich; das offene mittlere Finding blockiert dennoch den erforderlichen Interpretationscheck.
- Keine Rohantworten, data/raw/, data/local/, gesperrte Verteilungen oder reviewed-historical-Dateien gelesen. run_v22.py nicht ausgeführt. Nur synthetische Profile verwendet.
- Das frühere P2-Urteil wurde bestimmungsgemäß gelesen. P1-Urteile, R4, V2-Fairnessbericht und Kontrollrechnung ausschließlich gehasht, nicht inhaltlich gelesen.
- F02: ohne Dateneinsicht ist eine dokumentierte Autorangabe; diese Nachprüfung beweist nicht die vollständige Zugriffshistorie anderer Agenten.
- F04 stützt sich auf gezielte gebundene R1–R3-Abschnitte. Externe Originalquellen und ESS12-Veröffentlichungstermin nicht erneut live verifiziert.
- Keine Implementierungsänderungen, Browserprüfung, volle Test-Suite oder pnpm check: nur die beauftragten Reviewberichte geschrieben. Breite Checks sind nicht Teil dieser Nachprüfung und können weitere Dateien schreiben.
- Keine Commits, Tags, Pushes oder externen Nachrichten. Zwei vor Berichtsschreiben beobachtete ungetrackte Dateien generate-references-v22.mjs und reference-v22.ts weder gelesen noch verändert.
- Titelabweichung und neue Formulierung unter der ursprünglichen ID F01 beurteilt, kein doppeltes neues Finding. Keine weiteren festschreibungsrelevanten oder durch Korrekturen verursachten Probleme belegt.

## Prüfprotokoll

Modell laut Laufzeit: OpenAI `gpt-6.1-sol`, medium reasoning effort, Codex harness in T3 Code. Interne Revision unbekannt. Projekt-Skill `life93-review` und `unslop` gelesen und angewandt. Das JSON enthält den Datei-Auftrag und Inputhashes.

Gelesene Dateien mit Hash: „Inhalt“ umfasst bei Rechercheberichten und Code die gezielten Belegabschnitte, bei PDFs die genannten Seiten. Trunkierte Ausgaben gelten nicht als vollständige Lektüre. Unabhängige P1-Urteile wurden ausschließlich gehasht. Die Tabelle enthält die vor der Bewertung gebundenen Hashes; der spätere abweichende Hash steht oben.

| Datei | Zugriff | SHA-256 |
| --- | --- | --- |
| `reports/claude/auftraege/P2-runde2-quellen-fairness.md` | Inhalt | `b1464a894876371f065f8d681b680dd50e014b737b8792961a7ddf529ba4db55` |
| `.claude/skills/life93-review/SKILL.md` | Inhalt | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | Inhalt | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `.agents/skills/unslop/SKILL.md` | Inhalt | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `docs/project.md` | Inhalt | `7cfa1d4046eb30ae4b29728c49fa90baff89f40e56199b8eff0a738ca004e270` |
| `docs/pruefregeln.md` | Inhalt | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` |
| `reports/claude/pruefungen/PLAN-V22-002-manifest.json` | Inhalt | `67506f10f9cfb2a56a352d7cec31f25671207fabd0aa421ca9fc88a3e4644eab` |
| `docs/analyseplan-v2.2.md` | Inhalt | `bd8b23339f85d78e51ca5fc4e2e14d03c2beec1324f0e27b56382626f94a1e29` |
| `docs/profilregeln-v1.md` | Inhalt | `b880088d2221c2da3baab236be61b9970561c0ef25c67a753534f6ee4905a727` |
| `docs/abdeckung-v2.2.md` | Inhalt | `f3f03912f38dc7149b73739bc18fa9bcec59c65f6cb77edfd130be3c8e2d1b10` |
| `data/politikprofil-v2.2.ergaenzung.json` | Inhalt | `c4b0d97aeaf10868001199cb3f7f135a6fb8ec28d63b58f7f222ff7e0acd71ac` |
| `pipeline/v22/survey.py` | nur Hash | `ef9011c5a9b9792373f7c9395d4e5db17a4381dab648480b2276ddac15a982bc` |
| `pipeline/v22/run_v22.py` | nur Hash | `a4c3ab0a78dcd44ae3f90b4e16df8ff07511a6e677bbaebd036cc232cd5a6ae4` |
| `pipeline/v22/catalogue_v22.py` | Inhalt | `f259365c04bdd8d783a90acbd5291838efb07b76e567b9de139197840568f2fc` |
| `pipeline/v22/test_survey.py` | nur Hash | `dacdde363044981d575636447f6e206f89a0325353c8cc7b9a7898e1ca8ed011` |
| `pipeline/v22/test_run_v22.py` | nur Hash | `74738a170672057de58ebc0e5b7cb8474ffc6f8581a8b767adffab4889c490b4` |
| `pipeline/v22/fetch_ess_metadata.py` | nur Hash | `82952e3d660b75d4540b6b5a1a136e4dc7c26899294f0d96aeb22fd600bd6da5` |
| `web/src/app/policy-draft/profile/profile-rules.ts` | Inhalt | `b07a153e0d9236c049048995a4122982df199c0c1781b44f2f8c8425b30905a2` |
| `web/src/app/policy-draft/profile/profile-structure.ts` | Inhalt | `bd17d664b5cab042ec134025e0ce0393bba7a84b2174e546d2e00b083aead5de` |
| `web/src/app/policy-draft/profile/profile-engine.ts` | Inhalt | `1b11d598a1743b611d2359fd354a03fc8bd90522293c6fa89c23c928b0b897fa` |
| `web/src/app/policy-draft/profile/profile-engine.spec.ts` | nur Hash | `901e4e1207fe9596681f70a3877e2a017b21222bf5ead063bcf205c19b1ea23b` |
| `web/src/app/policy-draft/policy-catalogue.ts` | nur Hash | `9efc5f67a66952a86c1c427c83c5b40a557104b1573e7997470fff61259745f9` |
| `data/analysevertrag.v2.entwurf.json` | nur Hash | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| `data/gruppenvertrag.v2.1.entwurf.json` | nur Hash | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `docs/empirie-plan-v2.entwurf.md` | nur Hash | `2b0cd26f8fba81bbf520b9ae3411d623f9299c9ff707aacf681bde4c65a0439f` |
| `reports/claude/agenten/R1-themen-aussen-bildung-digital.md` | Inhalt | `0389cd71c40d89ff62fcb093825312392abee0ae206ac868124d51a4e15cfba2` |
| `reports/claude/agenten/R2-themen-gesundheit-arbeit-wohnen.md` | Inhalt | `207aa6bbae3680f7a52721f4a2f7abb82b03690c24b0e120e687a37a1564e11b` |
| `reports/claude/agenten/R3-themen-reichweite.md` | Inhalt | `1ed197088a6f215fa1cea397a6faec5a9da5f70307db3cb06dc4ec790dbf27ec` |
| `reports/claude/agenten/R4-profilform.md` | nur Hash | `8ea2b9ff837b6431d55acd051b45d5cba69eea3df1049878f748fe0655eddfa2` |
| `reports/claude/kontrollrechnung/bericht.md` | nur Hash | `f53ef3500e1d702a85fac9ca1d2186eea940fd0e0366cab22d40fdb4eaa501d1` |
| `reports/claude/agenten/V2-quellen-konstrukte-fairness.md` | nur Hash | `b7cb60fcd3f9febdd66e80ac3bf2221c8a9dcfd1af6d74a43de9f68cdc97cebb` |
| `pipeline/v22/export_v22.py` | nur Hash | `839765b1a8287141f8176ab988e86ab4deca7d712d84d53287b943c164d6eee1` |
| `web/src/app/policy-draft/profile/area-scope.ts` | nur Hash | `4ed439fd3a1d9b9d030f8ed33b9a4d55916d07cc694bcf8a3aec6f86d338a1b1` |
| `reports/claude/pruefungen/P1-methoden-v22.md` | nur Hash | `d479242f5d075b23f9379bf6dbce9cf8199f8a29f6236d446578b57c17eadb00` |
| `reports/claude/pruefungen/P1-methoden-v22.json` | nur Hash | `070af35fcb0ffc7c626e4bea40b142095ad9383ceb5f701965d94d75bd618a87` |
| `reports/claude/pruefungen/P2-quellen-fairness-v22.md` | Inhalt | `5d5efeb3819e6d163489d82b9b3a8b4b7b515a9891f750dbe9229302441a84f3` |
| `reports/claude/pruefungen/P2-quellen-fairness-v22.json` | Inhalt | `689e681c53699d104514cfbc71921818ed3ae5f8b8683e489a365e8568673012` |
| `outputs/loop/breadth-data-001/sources/ess5-de-questionnaire.pdf` | nur Hash | `24b5d2599e6d30dc02a6d835f5f80b5bcecf8f6014ee8f4670a703c25d3c3cbf` |
| `outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf` | Inhalt | `977475c18d2adebea6ccb7695f377fb6ed500ef087b077086305f9a2e4a7b239` |
| `outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf` | Inhalt | `dde02b5336b2d960c2900a8fcf5e2a0f0d254b46dcce1d9ffb785a830e096bc0` |
| `outputs/loop/breadth-data-001/sources/ess10-de-questionnaire.pdf` | nur Hash | `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425` |
| `outputs/loop/methods/SURVEY-MANUAL.pdf` | nur Hash | `87b0ea7088e0dfd587b4c4efacd38db68db8268a986a130c1a868ce2088bac2c` |
| `outputs/claude/sources/ess8-candidates.json` | Inhalt | `279f9c31b4236b71f4a820de7a2b519989ec796ad49ba4f2bde210c108d94168` |
| `outputs/claude/sources/ess10sc-candidates.json` | nur Hash | `2a5927d1ec1d322b2a127ff0c2c35862cbae8fc1ae39767aee410ff910ef8394` |
| `outputs/claude/sources/ess10sc-candidates-2.json` | nur Hash | `9ed9a9739dfe64b2cd8ebf2cc4cec8960ce29179b25d2013e90ff0dac53a038a` |
| `outputs/claude/sources/ess5-candidates.json` | nur Hash | `4b0247142d37697b4193e3373a37174849bcc16552d9764e34a51169170795a8` |
| `outputs/loop/breadth-access-002/sources/ess10sc-file-metadata.json` | nur Hash | `d9e6d606fb3b897d33d04f3247dbe5160d11f108a76fca6547a773e2c1ba0a57` |

Ausgeführte Befehle (Python-/Node-Inlineprogramme mit ihrem jeweiligen Prüfzweck):

- `cat reports/claude/auftraege/P2-runde2-quellen-fairness.md`; `sha256sum reports/claude/auftraege/P2-runde2-quellen-fairness.md`.
- `git branch --show-current`; `git status --short`.
- `cat`, `nl -ba`, `sed -n` für Skill, Schema, unslop, Projekt-/Prüfregeln, drei Plandokumente, das frühere P2-Urteil und die oben bezeichneten Code-/Rechercheabschnitte.
- `python3 -`: Manifest und alle 40 Eingabehashes prüfen; alte Findings und mnrgtjb-Metadaten extrahieren; vor dem Schreiben erneut Hashes prüfen. Dieser Schreibversuch brach mit AssertionError für profile-structure.ts ab, ohne Dateien zu schreiben. Danach separate Hashgegenprobe und Schreiben dieser beiden Berichte mit dokumentierter Abweichung.
- `rg -n -C 6` zu mnrgtjb, basinc und Bedürftigkeitsformulierungen; `rg -n` zu Katalogdefinitionen und dem geänderten Querbezug.
- `pdftotext -f 12 -l 12 -layout outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf -`; entsprechende Aufrufe für S. 36 und S. 43–44.
- `pdftotext -f 56 -l 56 -layout outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf -`; entsprechender Aufruf für S. 14. Font-Weight-Warnung bei S. 56; alle drei Merkmale und vier Antwortkategorien im Text vorhanden.
- `node -`: TypeScript transpileModule, eingeschränkter In-Memory-Modullader und Node assert für S01–S03. Keine Schreiboperation, alle Assertions bestanden.
- `node -`: anfänglicher Ajv-Pfad unter web/node_modules nicht verfügbar (MODULE_NOT_FOUND); auch Python jsonschema fehlte. `rg --files --hidden --no-ignore node_modules/.pnpm -g 2020.js` fand Ajv 8.20.0. Erneuter Node-Aufruf mit diesem Pfad: Schema BESTANDEN, getrennt vom fachlichen Urteil.
- Abschließend `python3 -` und `git status --short` für JSON-/Berichtskontrolle und Dateistatus. Nur die zwei Berichte durch diesen Prüfer geschrieben.

Abschließender Dateistatus zeigte zusätzlich die beiden P1-runde2-Berichte aus paralleler Arbeit; weder gelesen noch verändert.
