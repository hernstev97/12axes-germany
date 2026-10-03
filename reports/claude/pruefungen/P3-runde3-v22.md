# P3 Runde 3: gezielte Korrekturprüfung

Gesamturteil: **NICHT_BESTANDEN** für die sechs Restpunkte vor Festschreibung von `PLAN-V22-003`, Analyseplan v2.2 Fassung 1.2. Vier Punkte sind behoben; F08 und F10 bleiben teilweise offen. Keine neuen Findings. Kein erhebliches Finding; die beiden offenen mittleren Findings verhindern trotzdem das Bestehen der erforderlichen Checks.

Prüfdatum: 3. Oktober 2026. Branch: `research/life-93-claude-20261003`. Arbeitsbaum zu Beginn sauber. Auftragshash und Manifesthash stimmen. Alle 43 Artefakte und zehn Caches vor der Bewertung und unmittelbar vor dem Schreiben hashgleich.

| Punkt | Status | Blockiert Umfang |
| --- | --- | --- |
| P1-V22-F01 | BEHOBEN | nein |
| P1-V22-F02 | BEHOBEN | nein |
| P1-V22-F04 | BEHOBEN | nein |
| P1-V22-F08 | TEILWEISE | ja |
| P1-V22-F10 | TEILWEISE | ja |
| P2-V22-F01 | BEHOBEN | nein |

## P1-V22-F01: BEHOBEN

Getrennte private Wahl-/Parteibilanz nach Gruppenvertrag v2.1.

Runde 2 fasste Missing-Gründe und benannte Parteien/Other zusammen. Die neue Fassung trennt beides.

Auswirkung: Die ursprünglich fehlende Auflösung der privaten Ausschlüsse ist nachprüfbar.

Schweregrad: mittel. Konkrete lokale Vertrags-, Anzeigeprüfungs- oder Bindungsanforderung vor Festschreibung; kein empirisches Scheitern behauptet.

Belege:

- pipeline/v22/run_v22.py:187–239
- data/gruppenvertrag.v2.1.entwurf.json:3380–3415
- S01: Refusal, Don't know und No answer je Feld; named/Other, Blank, strukturell nicht gefragt und Inkonsistenz getrennt; unbekannte Partei auch bei Nichtwähler abgelehnt.

Korrektur: Umgesetzt; keine weitere Korrektur für diesen Restpunkt.

Nachprüfung: S01 und test_vote_party_accounting_and_inconsistency bestanden.

## P1-V22-F02: BEHOBEN

Verhältnisdiagnose nach dem Gruppenvertrag, mit gesonderter Gesamtstudien-Diagnose.

Die frühere Diagnose benutzte alle Fälle und OR statt AND sowie keinen Leerstatus. Die Korrektur beseitigt diese Abweichungen.

Auswirkung: Primärgewichte bleiben unverändert; Diagnosen entsprechen den zugesagten Fallkreisen.

Schweregrad: mittel. Konkrete lokale Vertrags-, Anzeigeprüfungs- oder Bindungsanforderung vor Festschreibung; kein empirisches Scheitern behauptet.

Belege:

- pipeline/v22/run_v22.py:242–250,286–315
- data/gruppenvertrag.v2.1.entwurf.json:3443–3452
- S02: Nichtwähler mit abweichendem Verhältnis ändern die Berechtigten-Diagnose nicht; absolute und relative Toleranz wirken beide; leere Domäne ergibt not_evaluable_no_eligible_group_cases.

Korrektur: Umgesetzt; keine weitere Korrektur für diesen Restpunkt.

Nachprüfung: S02 einschließlich synthetischem run()-Durchlauf bestanden.

## P1-V22-F04: BEHOBEN

Abbruch vor Rechnung bei vorhandenen privaten Verzeichnissen mit Gruppen-/Fremdrechten.

Runde 2 akzeptierte 0755. check_private_dir weist Gruppen-/Fremdrechte nun zurück und ändert vorhandene Rechte nicht.

Auswirkung: Die konkret beanstandeten zu offenen Verzeichnisrechte verhindern jetzt den Lauf.

Schweregrad: mittel. Konkrete lokale Vertrags-, Anzeigeprüfungs- oder Bindungsanforderung vor Festschreibung; kein empirisches Scheitern behauptet.

Belege:

- pipeline/v22/run_v22.py:361–391
- S03: importiertes main() nur unter /tmp mit gemocktem Gate/Runner; 0755/0777 abgelehnt vor run(), Modus unverändert; neue Ausgabe 0700/0600, vorhandener Lauf und Symlink abgelehnt.

Korrektur: Umgesetzt; keine weitere Korrektur für diesen Restpunkt.

Nachprüfung: S03 und test_private_directory_checks bestanden.

## P1-V22-F08: TEILWEISE

T30 ist als Anzeigeprüfung für zurückgehaltene und leere Referenzen vollständig umgesetzt.

Der neue Komponententest beantwortet cttresa und prüft für withheld den Erhalt der eigenen Aussage und die fehlenden Zahlen. Für no_valid_answers bleibt nur ein Index-Test ohne beantwortetes Item, Vorlage oder Fehlhinweis. Der Komponententest importiert außerdem weiterhin einen echten historischen Fixture. Eine verbindlich offene no_valid_answers-Anzeigeprüfung wird nicht ausgewiesen.

Auswirkung: Die in Runde 2 verlangte vollständige synthetische Anzeigeprüfung ist weiterhin nicht belegt. Der Index-Test belegt keine Anzeige des Leerstatus. Keine Offenlegung realer Zahlen und kein empirischer Fehler behauptet.

Schweregrad: mittel. Konkrete lokale Vertrags-, Anzeigeprüfungs- oder Bindungsanforderung vor Festschreibung; kein empirisches Scheitern behauptet.

Belege:

- web/src/app/policy-draft/policy-draft.spec.ts:1–5,110–125
- web/src/app/policy-draft/reference-v22.spec.ts:20–49
- docs/profilregeln-v1.md:85; docs/analyseplan-v2.2.md: Abschnitt 9 Runde 2
- S04: identische T30-Assertions mit synthetischem withheld-Fixture bestehen. Unabhängige no_valid_answers-Index-Gegenprobe mit absichtlich mitgelieferten Zahlen entfernt Zahlen für Einzel-/Gruppeneinträge.
- S04 Anzeigegegenprobe: cttresa=9 bleibt erhalten; no_valid_answers als unverfügbarer Eintrag führt zur globalen Quellenablehnung und keinem fragebezogenen reference-withheld-Hinweis. historical-reference.ts unterstützt nur reason=withheld_base_or_cell_count.

Korrektur: Den no_valid_answers-Fall mit beantwortetem Item, fehlenden Prozentwerten, passendem Fehlhinweis und erhaltener eigener Aussage synthetisch im vorgesehenen Anzeigeweg prüfen. Alternativ diese konkrete Anzeigeprüfung vor der Festschreibung verbindlich als offen und als spätere Voraussetzung ausweisen. Den T30-Komponententest auf synthetische Referenzen umstellen, damit er ohne gesperrte Ergebnisdateien läuft.

Nachprüfung: T30 getrennt für beide Status mit ausschließlich synthetischen Eingaben ausführen; gegebenenfalls die ausdrückliche Begrenzung des Plans prüfen.

## P1-V22-F10: TEILWEISE

PLAN-V22-003 bindet die tatsächlich benötigten öffentlichen Reproduktionsabhängigkeiten der Prüffälle.

Alle in Runde 2 namentlich genannten Ergänzungen sind manifestiert. Der neu gebundene T30-Komponententest benötigt jedoch policy-draft.ts, policy-draft.html und historical-reference.ts, die weiterhin keine Manifest-Einträge besitzen. Damit bindet der Testhash nicht den tatsächlich ausgeführten Anzeige-/Bindungscode.

Auswirkung: Die Anzeigeprüfung kann bei verändertem produktivem Anzeige-/Bindungscode stattfinden, während alle Manifesthashes weiter passen. Die Bindungslücke betrifft die jetzt als erledigt beanspruchte T30-Korrektur.

Schweregrad: mittel. Konkrete lokale Vertrags-, Anzeigeprüfungs- oder Bindungsanforderung vor Festschreibung; kein empirisches Scheitern behauptet.

Belege:

- reports/claude/pruefungen/PLAN-V22-003-manifest.json: artifacts
- web/src/app/policy-draft/policy-draft.spec.ts:1–5,110–125
- web/src/app/policy-draft/policy-draft.ts:1–46; templateUrl=policy-draft.html
- web/src/app/policy-draft/historical-reference.ts: unavailableReferences-Bindung, referenceState
- S05: Abgleich der für die isolierte T30-Ausführung tatsächlich kopierten Abhängigkeiten mit dem Manifest; Komponente, Vorlage und Referenzbinder fehlen. Ihre aktuellen Hashes sind in diesem Bericht und JSON protokolliert, nicht im eingefrorenen Paket.

Korrektur: Die öffentlichen Abhängigkeiten des T30-Tests einschließlich Komponente, Vorlage, Referenzbinder und weiterer benötigter Helper vollständig in ein neues Manifest aufnehmen. Synthetische Test-Fixtures statt gesperrter Antwortverteilungen binden; keine gesperrten Ergebnisdateien in den Auftrag aufnehmen.

Nachprüfung: Mit neuem erwarteten Manifesthash erneut alle Eingaben prüfen; Änderungen an Komponente, Vorlage und Referenzbinder müssen die Bindungsprüfung jeweils scheitern lassen.

## P2-V22-F01: BEHOBEN

Soziale Absicherung ohne unterstelltes Modell der Bedürftigkeitsprüfung.

Runde 2 behauptete ohne Bedürftigkeitsprüfung. Der feste Kontext lässt diese Frage jetzt ausdrücklich offen; Dokument- und Codetitel stimmen überein.

Auswirkung: Die Einzelantworten erhalten kein nicht erfragtes Anspruchsmodell; Grundeinkommen bleibt als anderer Gegenstand getrennt.

Schweregrad: mittel. Konkrete lokale Vertrags-, Anzeigeprüfungs- oder Bindungsanforderung vor Festschreibung; kein empirisches Scheitern behauptet.

Belege:

- web/src/app/policy-draft/profile/profile-structure.ts:161–175
- docs/profilregeln-v1.md: Querbezüge, Soziale Absicherung
- ESS8 deutscher Fragebogen PDF-S.36 E6/E7; PDF-S.43 E36; Showcards PDF-S.55 Liste 54
- S06: Profile mit ersten/letzten Kategorien der fünf Fragen und nur E6=10/E7=0 haben den korrigierten Titel und Kontext.

Korrektur: Umgesetzt; keine weitere Korrektur für diesen Restpunkt.

Nachprüfung: Originalquellen direkt gelesen; S06 nach vollständiger Initialisierung aller Antwortzustände bestanden.

## Synthetische Prüfungen und tatsächliche Ergebnisse

- Python-Suite: 14 Tests bestanden. Alle Studiendateien der Tests stammen aus temporär erzeugten Daten.
- S01/S02/S03: eigenständige Gegenproben für Feldbilanzen, Toleranzen, Fallkreis und Ausgabepfad bestanden. Die Schreibprobe schreibt ausschließlich synthetisches JSON unter `/tmp`, auch wenn ihr Log den dort relativen Pfad `data/local/v22/run.json` nennt.
- S04: T30-Assertions des gebundenen Komponententests unverändert übernommen, den echten Fixture-Import durch eine synthetische leere Referenz mit withheld-Eintrag ersetzt. Gruppenartefakt als synthetischen leeren Stub bereitgestellt, da dessen Import sonst eine gesperrte Datei lesen würde. Nur gezielte Tests in die isolierte Angular-Kopie übernommen. Kein gesperrter Fixture gelesen oder kopiert.
- S04-Gegenproben: no_valid_answers mit absichtlich mitgelieferten synthetischen Zahlen für Einzel- und Gruppeneinträge im Index vollständig entfernt. Bei Einspeisung als unverfügbare Einzelreferenz in die vorhandene Komponente: eigene Antwort erhalten, keine Prozentwerte, globale Quellenablehnung, kein fragebezogener Fehlhinweis. Dies belegt die verbleibende Trennung zwischen Index-Test und Anzeigeweg; keine neue empirische Fehlbehauptung.
- S05: alle in Runde 2 namentlich fehlenden Abhängigkeiten nun gebunden. Tatsächlich für die Anzeigeausführung kopierte Komponente, Vorlage und Referenzbinder fehlen weiterhin im Paket. Weitere T30-Abhängigkeiten stehen in der Hash-Tabelle, etwa policy-profile.ts, group-reference.ts/-types.ts und policy-source-details.*. Reale Antwortverteilungen dürfen weiterhin nicht in das Prüfpaket.
- S06: erste und letzte Kategorien sowie nur E6/E7 geprüft; fester Kontext und Titel in allen Fällen korrekt. Die erste selbst geschriebene Gegenprobe scheiterte wegen fehlender untouched-Antwortzustände. Nach Korrektur ausschließlich des synthetischen Fixtures bestanden alle Assertions.
- Abschließender Angular-Lauf in `/tmp`: drei Testdateien, 29 Tests bestanden. Darin 23 bestehende Profiltests, zwei bestehende Referenztests, der T30-Komponententest und drei zusätzliche Gegenproben. Die grüne Suite bestätigt die technischen Beobachtungen; sie schließt F08/F10 nicht automatisch.

## Grenzen

- Gezielte KI-Korrekturprüfung von sechs Restpunkten, kein Gesamtaudit, keine empirische Validierung oder wissenschaftliche/menschliche Abnahme.
- Kein Finding erheblich. Zwei mittlere offene Findings blockieren erforderliche Checks dieser Festschreibung; daher NICHT_BESTANDEN.
- Keine Rohdaten, data/raw/, data/local/, gesperrten Antwortverteilungen oder reviewed-historical-Dateien gelesen. run_v22.py nicht als Kommandozeile ausgeführt; importiertes main() nur in synthetischer /tmp-Wurzel mit gemocktem Gate/Runner.
- Original-Angular-Gesamtsuite und pnpm check nicht ausgeführt, da sie gesperrte historische Ergebnisdateien importieren und zusätzliche Repository-Artefakte schreiben können. Isolierte Angular-Ausführung ersetzt keine vollständige unveränderte Suite und keine Browserbeobachtung.
- Vorgegebene frühere Urteile bestimmungsgemäß gelesen; keine unabhängige Erstbewertung. Keine Aussagen über tatsächliche Verteilungen oder frühere Dateneinsicht anderer Agenten.
- Nur die zwei beauftragten Berichte im Repository geschrieben. Keine Commits, Tags, Pushes, externen Nachrichten oder Freigaben. /tmp enthält synthetische Testkopien und Prüfprogramme.

## Prüfprotokoll

Modell laut Laufzeit: OpenAI `gpt-6.1-sol`, medium reasoning effort, Codex harness in T3 Code. Interne Revision unbekannt. `life93-review` und `unslop` gelesen und angewandt. Ursprünglicher Nutzerprompt und vollständiger Datei-Auftrag stehen im JSON.

Gelesene Dateien mit Hash. „Inhalt/Tests“ umfasst bei längeren Code-/Berichtsdateien gezielte Belegabschnitte oder den durch Tests geladenen Inhalt. PDFs: ESS8-Fragebogen S.36 und S.43; Showcards S.55. Sonstige Manifestdateien wurden ausschließlich gehasht. Die öffentlichen zusätzlichen Angular-Abhängigkeiten wurden für die synthetische Ausführung bytegleich kopiert. Keine gesperrte Datei in dieser Tabelle.

| Datei | Zugriff | SHA-256 |
| --- | --- | --- |
| `docs/analyseplan-v2.2.md` | Inhalt/Tests | `2be4c3194aab52f5da78f27acda30ebb6ff7c775a42c15eafd26b466e04a3d60` |
| `docs/profilregeln-v1.md` | Inhalt/Tests | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` |
| `docs/abdeckung-v2.2.md` | Inhalt/Tests | `f3f03912f38dc7149b73739bc18fa9bcec59c65f6cb77edfd130be3c8e2d1b10` |
| `data/politikprofil-v2.2.ergaenzung.json` | nur Hash | `c4b0d97aeaf10868001199cb3f7f135a6fb8ec28d63b58f7f222ff7e0acd71ac` |
| `pipeline/v22/survey.py` | Inhalt/Tests | `ef9011c5a9b9792373f7c9395d4e5db17a4381dab648480b2276ddac15a982bc` |
| `pipeline/v22/run_v22.py` | Inhalt/Tests | `b07d5bd8e9306dc7db2b0f1e72af9207d00ca255ea3b0c3c2f58d9f87925e1fd` |
| `pipeline/v22/catalogue_v22.py` | nur Hash | `f259365c04bdd8d783a90acbd5291838efb07b76e567b9de139197840568f2fc` |
| `pipeline/v22/test_survey.py` | Inhalt/Tests | `dacdde363044981d575636447f6e206f89a0325353c8cc7b9a7898e1ca8ed011` |
| `pipeline/v22/test_run_v22.py` | Inhalt/Tests | `e893eadbf46c64c0b96739dff16105be7f83529d3c1cc317df546ab44f46667c` |
| `pipeline/v22/fetch_ess_metadata.py` | nur Hash | `82952e3d660b75d4540b6b5a1a136e4dc7c26899294f0d96aeb22fd600bd6da5` |
| `web/src/app/policy-draft/profile/profile-rules.ts` | Inhalt/Tests | `b07a153e0d9236c049048995a4122982df199c0c1781b44f2f8c8425b30905a2` |
| `web/src/app/policy-draft/profile/profile-structure.ts` | Inhalt/Tests | `fb133d063a3a35fb94a337e5ee42eeb1647462df09b4bcfe7340c1baba40aadb` |
| `web/src/app/policy-draft/profile/profile-engine.ts` | Inhalt/Tests | `1b11d598a1743b611d2359fd354a03fc8bd90522293c6fa89c23c928b0b897fa` |
| `web/src/app/policy-draft/profile/profile-engine.spec.ts` | Inhalt/Tests | `fef14891d4c8cd59ae9e85297dc2af6f836ea3c4e2e56ba06f244088c0afa966` |
| `web/src/app/policy-draft/policy-catalogue.ts` | Inhalt/Tests | `9efc5f67a66952a86c1c427c83c5b40a557104b1573e7997470fff61259745f9` |
| `data/analysevertrag.v2.entwurf.json` | nur Hash | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| `data/gruppenvertrag.v2.1.entwurf.json` | Inhalt/Tests | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `docs/empirie-plan-v2.entwurf.md` | nur Hash | `2b0cd26f8fba81bbf520b9ae3411d623f9299c9ff707aacf681bde4c65a0439f` |
| `reports/claude/agenten/R1-themen-aussen-bildung-digital.md` | nur Hash | `0389cd71c40d89ff62fcb093825312392abee0ae206ac868124d51a4e15cfba2` |
| `reports/claude/agenten/R2-themen-gesundheit-arbeit-wohnen.md` | nur Hash | `207aa6bbae3680f7a52721f4a2f7abb82b03690c24b0e120e687a37a1564e11b` |
| `reports/claude/agenten/R3-themen-reichweite.md` | nur Hash | `1ed197088a6f215fa1cea397a6faec5a9da5f70307db3cb06dc4ec790dbf27ec` |
| `reports/claude/agenten/R4-profilform.md` | nur Hash | `8ea2b9ff837b6431d55acd051b45d5cba69eea3df1049878f748fe0655eddfa2` |
| `reports/claude/kontrollrechnung/bericht.md` | nur Hash | `f53ef3500e1d702a85fac9ca1d2186eea940fd0e0366cab22d40fdb4eaa501d1` |
| `reports/claude/agenten/V2-quellen-konstrukte-fairness.md` | nur Hash | `b7cb60fcd3f9febdd66e80ac3bf2221c8a9dcfd1af6d74a43de9f68cdc97cebb` |
| `pipeline/v22/export_v22.py` | nur Hash | `839765b1a8287141f8176ab988e86ab4deca7d712d84d53287b943c164d6eee1` |
| `web/src/app/policy-draft/profile/area-scope.ts` | Inhalt/Tests | `4ed439fd3a1d9b9d030f8ed33b9a4d55916d07cc694bcf8a3aec6f86d338a1b1` |
| `reports/claude/pruefungen/P1-methoden-v22.md` | nur Hash | `d479242f5d075b23f9379bf6dbce9cf8199f8a29f6236d446578b57c17eadb00` |
| `reports/claude/pruefungen/P1-methoden-v22.json` | nur Hash | `070af35fcb0ffc7c626e4bea40b142095ad9383ceb5f701965d94d75bd618a87` |
| `reports/claude/pruefungen/P2-quellen-fairness-v22.md` | nur Hash | `5d5efeb3819e6d163489d82b9b3a8b4b7b515a9891f750dbe9229302441a84f3` |
| `reports/claude/pruefungen/P2-quellen-fairness-v22.json` | nur Hash | `689e681c53699d104514cfbc71921818ed3ae5f8b8683e489a365e8568673012` |
| `reports/claude/pruefungen/P1-runde2-v22.md` | Inhalt/Tests | `48b8955cc77f3d993fa04de46cdd14d43d5a59e36f463fa2c0383c2b48513f15` |
| `reports/claude/pruefungen/P1-runde2-v22.json` | nur Hash | `58fe08601e18aa03145c2b479fbb57c1f6f9394e03743072d9f3da5690d15736` |
| `reports/claude/pruefungen/P2-runde2-v22.md` | Inhalt/Tests | `9b80b4c1ef8fdf8588971f94e157b187f3c3d6704474cfc3e1d5b98a9201fa8c` |
| `reports/claude/pruefungen/P2-runde2-v22.json` | nur Hash | `4d68528c8cfeaf30a444efde89b863fdf55e8b8aa74215e35fc9e4b55fac6d72` |
| `web/src/app/policy-draft/public-catalogue-v22.ts` | Inhalt/Tests | `bc99055a10fb559cf2802d9a579ef3f07a3c8a77bdcc8556a2b08655d9d499cf` |
| `web/src/app/policy-draft/public-catalogue.ts` | Inhalt/Tests | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |
| `web/src/app/policy-draft/catalogue-types.ts` | Inhalt/Tests | `2599cfdf5c77ed912a85926b4e37a025b7d3661d1085749d27dbb5dc8be42822` |
| `web/src/app/policy-draft/generate-public-catalogue-v22.mjs` | nur Hash | `a9854873edaf9086bf4741e6bd966e2ce98c4f73f599922e488744713b02535a` |
| `web/src/app/policy-draft/reference-v22.ts` | Inhalt/Tests | `3790cd14e136cbd701bbc4124bcdcfbff29d6647bac66012e9794c9c662a8574` |
| `web/src/app/policy-draft/reference-v22.spec.ts` | Inhalt/Tests | `f6e0a28b52f033d6efbcebe76166090ebebf0e27c73a713d3725425d4b3f22b1` |
| `web/src/app/policy-draft/policy-draft.spec.ts` | Inhalt/Tests | `074cc930062087164c2d661da18622a14c402c3d9e04a1a3904ff95296ae080b` |
| `web/src/app/policy-draft/policy-catalogue.spec.ts` | nur Hash | `d869f049f04b608ceed0020afbd500faa4739519e21ba06b06d75304ad87a829` |
| `pipeline/policy_reference_v2.py` | Inhalt/Tests | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `outputs/loop/breadth-data-001/sources/ess5-de-questionnaire.pdf` | nur Hash | `24b5d2599e6d30dc02a6d835f5f80b5bcecf8f6014ee8f4670a703c25d3c3cbf` |
| `outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf` | Inhalt/Tests | `977475c18d2adebea6ccb7695f377fb6ed500ef087b077086305f9a2e4a7b239` |
| `outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf` | Inhalt/Tests | `dde02b5336b2d960c2900a8fcf5e2a0f0d254b46dcce1d9ffb785a830e096bc0` |
| `outputs/loop/breadth-data-001/sources/ess10-de-questionnaire.pdf` | nur Hash | `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425` |
| `outputs/loop/methods/SURVEY-MANUAL.pdf` | nur Hash | `87b0ea7088e0dfd587b4c4efacd38db68db8268a986a130c1a868ce2088bac2c` |
| `outputs/claude/sources/ess8-candidates.json` | nur Hash | `279f9c31b4236b71f4a820de7a2b519989ec796ad49ba4f2bde210c108d94168` |
| `outputs/claude/sources/ess10sc-candidates.json` | nur Hash | `2a5927d1ec1d322b2a127ff0c2c35862cbae8fc1ae39767aee410ff910ef8394` |
| `outputs/claude/sources/ess10sc-candidates-2.json` | nur Hash | `9ed9a9739dfe64b2cd8ebf2cc4cec8960ce29179b25d2013e90ff0dac53a038a` |
| `outputs/claude/sources/ess5-candidates.json` | nur Hash | `4b0247142d37697b4193e3373a37174849bcc16552d9764e34a51169170795a8` |
| `outputs/loop/breadth-access-002/sources/ess10sc-file-metadata.json` | nur Hash | `d9e6d606fb3b897d33d04f3247dbe5160d11f108a76fca6547a773e2c1ba0a57` |
| `package.json` | Inhalt/Tests | `451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7` |
| `web/package.json` | Inhalt/Tests | `77db8383e6c64f65fe04638c46ba3b7f9b40040d95f0ad3ced1471fb475d60f7` |
| `web/angular.json` | Inhalt/Tests | `91c9042107b35de10321454587d64abbd7cd18cd25ea345319dd0378b8337ed8` |
| `web/tsconfig.json` | Inhalt/Tests | `b6445b51aafffbe2fed1026bbe83c8bdf1f9194c928f6bad0db9bad66fa10b4a` |
| `web/tsconfig.app.json` | Inhalt/Tests | `73644210146f8c2f7fac8504404fe21c36a9650df7587ba9e971fc36e5138f4f` |
| `web/tsconfig.spec.json` | Inhalt/Tests | `7aeb8799d7e1d086d16d7b238769f664cfa73b3d135318df5dcc441fdc6a7e87` |
| `web/src/app/policy-draft/policy-draft.ts` | Inhalt/Tests | `fac85532a2a4320023058ead915868982fac409355b609d111e2faf4a03e39e3` |
| `web/src/app/research/policy-profile.ts` | Inhalt/Tests | `28906eb1533bb953b43bed75a4995c907b71398f1ffcd63271c82cfdace05998` |
| `web/src/app/policy-draft/historical-reference.ts` | Inhalt/Tests | `58eb05517a43a4d3ea0a62c20f06c39857ca242e50748d3bce1a0f17a33683ab` |
| `web/src/app/policy-draft/group-reference-types.ts` | Inhalt/Tests | `539ca2854b8839a7e76590b56ca91f652350093582e68524dea9fe4575a85388` |
| `web/src/app/policy-draft/group-reference.ts` | Inhalt/Tests | `13d26f381c234f6d78a4687f0002528adf284eae722fa78e506ee1a942c5ca47` |
| `web/src/app/policy-draft/policy-source-details.ts` | Inhalt/Tests | `add8b2721004e120d71e7574d119bdd2ec84b5373c7b2b497d53e74e46a2f659` |
| `web/src/app/policy-draft/policy-source-details.html` | Inhalt/Tests | `3ebaf5bf8145005ad9706ce42bacd8660cffb15daf152ae4001da4ccf539fdb2` |
| `web/src/app/policy-draft/policy-source-details.scss` | Inhalt/Tests | `98ba630fb6527743e449750fbffde418f28b5993a208e37455205aec2c997f8b` |
| `web/src/app/policy-draft/policy-draft.html` | Inhalt/Tests | `0288b1e44f356e848a0e4864f7f22fea76090c93dfc4f3561fb7cfbc9c504c1d` |
| `web/src/app/policy-draft/policy-draft.scss` | Inhalt/Tests | `3b7e894c8b2e93029fe1da0136adf9d197adaa43a1a55e62c25b016eba2b07ce` |
| `reports/claude/auftraege/P3-runde3-gezielt.md` | Inhalt/Tests | `d983154afb1c800ce196092fb7abaee5e7c06ee26e4ede8b9fc0cf7e168212b8` |
| `reports/claude/pruefungen/PLAN-V22-003-manifest.json` | Inhalt/Tests | `6a575293673604ed52c83403f86a0b9993b0ce6fefaf929e1e1077a3bdfcde2c` |
| `.claude/skills/life93-review/SKILL.md` | Inhalt/Tests | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | Inhalt/Tests | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `.agents/skills/unslop/SKILL.md` | Inhalt/Tests | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `docs/project.md` | Inhalt/Tests | `7cfa1d4046eb30ae4b29728c49fa90baff89f40e56199b8eff0a738ca004e270` |
| `docs/pruefregeln.md` | Inhalt/Tests | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` |
| `docs/handbuch.md` | Inhalt/Tests | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |

Ausgeführte Befehle und Prüfzwecke:

- `cat reports/claude/auftraege/P3-runde3-gezielt.md`; `sha256sum` des Auftrags und Manifests.
- `git status --short`; `git branch --show-current`.
- `cat`, `sed -n`, `head`, `nl -ba`, `rg -n` für Skills, Schema, Projektregeln, Plan, Profilregeln, Abdeckung, Runde-2-Berichte und die oben ausgewiesenen Code-/Testabschnitte.
- `python3 -`: Manifest mit hashlib prüfen, 53 Inputhashes vor Bewertung und Schreiben erneut abgleichen; Manifestmitgliedschaft gegen die tatsächlich kopierten T30-Abhängigkeiten prüfen; ausschließlich die zwei Berichte schreiben.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'`: 14 Tests, OK.
- `PYTHONDONTWRITEBYTECODE=1 python3 /tmp/p3-v22-probes.py`: S01–S03, bestanden; Programmhash `510705df15876d002d02acdcf6ec33f9f8ffb973760b476dfaab750bd12ed3af`.
- `pdftotext -f 36 -l 36 -layout outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf -`; entsprechend S.43. `pdftotext -f 55 -l 55 -layout outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf -`. Font-Weight-Warnung bei Showcards; alle sechs Merkmale lesbar.
- `python3 /tmp/p3-prepare-angular.py`: isolierte Kopie ausschließlich öffentlicher Abhängigkeiten, selektierte Tests und synthetische Stubs; Programmhash `2b9f2ca8b8435cbb655dab7990403c864311ae22739621b986491f0466c41f44`.
- Erster `pnpm --dir /tmp/p3-v22-angular --filter politikprofil test --watch=false` verweigert einen automatischen Installationsversuch wegen Node-Modules-Symlink; keine Module entfernt. Versuch mit `--verify-deps-before-run=false` als CLI-Option verweigert, da unbekannte Option. `rg` im installierten pnpm-Code zeigt den unterstützten Umgebungsparameter.
- `pnpm_config_verify_deps_before_run=false pnpm --dir /tmp/p3-v22-angular --filter politikprofil test --watch=false`: zuerst 27 Tests bestanden, dann zwei Läufe mit fehlerhaftem eigenem S06-Fixture. Nach dessen Korrektur abschließend 29 Tests bestanden. Keine Abhängigkeiten installiert oder Repositorydateien geändert.
- `node` mit Ajv Draft 2020 für das JSON-Urteil; abschließend Hashkontrolle und `git status --short`. Schemaergebnis wird getrennt vom fachlichen Urteil geprüft.
