# P5 Runde 3: Quellen, Konstrukte und Fairness des Plans v2.3

4. Oktober 2026, Europe/Berlin. Gezielte Nachprüfung durch Codex/OpenAI, PLAN-V23-003, Entwurf 0.4. Kein neuer Gesamtaudit.

## Gesamturteil

**BESTANDEN im benannten P5-Runde-3-Umfang.** P5-V23-F02 und P5-V23-F05 sind korrigiert. Die unmittelbar geänderten Regeln führen im geprüften Umfang keinen neuen belegten Quellen-, Konstrukt- oder Fairnessfehler ein.

| Finding | Stand Runde 3 | Bisheriger Schweregrad | Blockiert diesen Umfang |
| --- | --- | --- | --- |
| P5-V23-F02 | KORRIGIERT | mittel | nein |
| P5-V23-F05 | KORRIGIERT | mittel | nein |

Das Urteil betrifft nur diese Korrekturen und ihre unmittelbaren Folgen. Es entscheidet weder die getrennte Methodenprüfung noch die Festschreibung des gesamten Plans. F01, F03 und F04 werden nicht erneut bewertet. Keine empirische, juristische, menschliche oder Releaseabnahme und kein Neutralitätsnachweis.

## Prüffassung und Integrität

Auftrag und Manifest wurden vor der Bewertung gegen die in der Nutzernachricht genannten Hashes geprüft. Beide stimmen. Start-HEAD war `f169a1dbc704ef50bb94f8babeb0fe55a9a7f49d`, Branch `research/life-93-claude-20261003`, Arbeitsstand sauber. Das Manifest nennt die ältere Paketbasis `42b6068b22a0c4fd413c4dac65ed6675b4192d6a`; sie ist ein Vorfahr der Start-HEAD. Bewertet wurden die tatsächlichen gepinnten Bytes: Plan Entwurf 0.4 und Entscheidungsvorlage Entwurf 2.

Alle 23 zulässigen Manifestartefakte wurden vor Bewertung, vor Schreiben und abschließend geprüft. Die vier P4-Berichte sind ausdrücklich ausgeschlossen; sie wurden weder geöffnet noch gehasht. Die P5-Vorgängerberichte bleiben bytegleich. Nicht jedes gehashte Artefakt wurde inhaltlich gelesen; die Liste unten trennt beides.

Während der Prüfung setzte ein anderer Prozess HEAD auf `d70a91302aa7b47f5827c2b71b3576a56cbfdcf5`. Der reine Pfadvergleich zur Start-HEAD nennt ausschließlich `reports/claude/fortsetzung-2026-10-04.md`. Dessen Inhalt wurde nicht geöffnet. Alle zulässigen Paketpins blieben unverändert. Keine fremde aktuelle Prüfung gelesen und keine Urteile aus der anderen Rolle übernommen. Historische Prüfstatushinweise im erlaubten Plan sind keine eigenen Nachprüfungen.

## P5-V23-F02: KORRIGIERT

Der verbliebene Fehler aus Runde 2 lag in der Folge der Entscheidungsvorlage: Alle Eurobarometer-Fragen sollten dort pauschal als EU-Ebene erscheinen. Zeile 33 verlangt jetzt die Kennzeichnung je Frage nach Plan 4.4 und nennt dieselbe Aufteilung wie die Kandidatenliste:

- sechs Entscheidungen auf EU-Ebene,
- den Ukraine-Beitritt als EU-Entscheidung mit Zustimmung Deutschlands,
- die allgemeine KI-Präferenz ohne genannte Ebene,
- die Verteidigungsausgabenfrage mit offener Ebene.

Der Abdeckungsnachtrag begrenzt die historische pauschale Aussage ausdrücklich für v2.3. Die frühere Aussage bei Entscheidung 2 bleibt als damaliger Stand erhalten. Die neue Formulierung „überwiegend Entscheidungen auf EU-Ebene“ ist mit der Liste vereinbar. Beide zurückgestellten Forschungsprinzipien bleiben im Plan ohne Ebene. Nationale Kernlücken werden weiterhin sichtbar offengelassen.

Damit stimmen Plan, Entscheidungsvorlage und Abdeckungsnachtrag im beanstandeten Punkt überein. Allgemeine Präferenzen erhalten keine nachträglich unterstellte EU-Ebene. Der Befund betrifft die dokumentierten Konstrukte; keine erneute Vollauthentifizierung aller deutschen Eurobarometer-Fragen.

Fundstellen: `docs/analyseplan-v2.3.entwurf.md:84-90,189-203`; `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:27-33`; `docs/abdeckung-v2.2.md:83,94,100`. Der technische Zeilenabgleich bestätigt neun vorgeschlagene Fragen und die Aufteilung 6/1/1/1. Diese Zählung ist keine wissenschaftliche Validierung.

## P5-V23-F05: KORRIGIERT

Plan 4.6 definiert vorgeschlagen jetzt anhand der belegten Sachbedingungen 4.1 Nr. 1 bis 6 und 8. Offene Freigaben und Klärungen nach Nr. 7 sowie Abschnitten 6 und 10 werden davon getrennt. Eine noch prüfbare oder erfüllbare Sachbedingung führt zur Zurückstellung. Für den deutschen Originalwortlaut gilt ausdrücklich: offizielle Fassung belegen und prüfen; eine eigene Übersetzung erfüllt die Bedingung nie.

In 11.3 sind sämtliche zehn OECD-Q19-Items b-j und l einzeln zurückgestellt, mit demselben fehlenden deutschen Feldwortlaut als Grund. Der Absatz trennt zusätzlich Mikrodatenbedingungen und Stevens Grundsatzentscheidung zu Klasse Q. Entscheidungsvorlage Zeile 37 übernimmt die Zurückstellung. Die Quellenanfrage lässt die deutsche Fassung und ihre Website-Rechte weiterhin offen. Die Frage ist damit nicht durch eine bloße Quellen- oder Quotenfreigabe automatisch vorgeschlagen.

Der [OECD-Kernfragebogen 2024, PDF-Seite 7](https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf#page=7) wurde direkt geöffnet und zusätzlich im Arbeitsspeicher gehasht. Sein Hash entspricht dem Pin in Plan 11. Er belegt den englischen Q19-Block, die gemeinsame Zahlungsbereitschaft und die getrennten exklusiven Nichtwahl-/Nichtwissenoptionen. Er belegt keinen deutschen Feldwortlaut. „Nur englisch“ wird hier als Stand des belegten Pakets verstanden, nicht als Nachweis, dass nie eine deutsche Feldfassung existierte. Die bestehende Grenze zur Nichtauswahl bleibt unverändert: daraus folgt keine Ablehnung des Einzelbereichs.

Fundstellen: `docs/analyseplan-v2.3.entwurf.md:49-58,98-106,140,215-230`; `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:37-41`; `docs/quellenanfragen-v1.entwurf.md:78-80`; OECD-PDF S. 7. Das Finding ist korrigiert durch zutreffende Zurückstellung, nicht durch nachträglich behauptete Verfügbarkeit der deutschen Fassung.

## Unmittelbare Änderungen und neue Fehler

### Statusmodell und SP568 QC9

Das Entfernen von „Wortlaut fehlt“ als eigenständigem Ausschlussgrund passt zum neuen Statusmodell. Eine fehlende, später belegbare deutsche Fassung führt zur Zurückstellung. Ein zusätzlich belegter inhaltlicher oder Format-Ausschlussgrund kann dennoch einen Ausschluss tragen. Dieselbe Unterscheidung gilt für alle politischen Positionen; eine neue partei- oder positionsabhängige Sonderregel wurde nicht eingeführt.

SP568 QC9 bleibt nun wegen des Formats ohne Gegenposition ausgeschlossen. R6 Zeile 204 bezeichnet den Gegenstand als Wichtigkeit von Transparenzmaßnahmen im Online-Wahlkampf und nennt den Frage-/Seitenbezug `ZA9129_q_de`, S. 56. R8 nennt im entsprechenden JSON-Kandidaten eine Wichtigkeitsskala laut R6 und hält den deutschen Wortlaut sowie die Kategorienliste weiterhin für unbelegt. Der Plan markiert diesen Quellenbezug ausdrücklich und nennt das Wortlautdefizit weiterhin. Der Formatgrund ist damit anhand der gepinnten Dokumentation nachvollziehbar und passt zu 4.3.

Das ist eine dokumentarische Prüfung der neuen Begründung. R8 übernimmt R6 und liefert keine zweite unabhängige Bestätigung. Der vollständige deutsche Feldtext und seine Antwortliste wurden nicht direkt authentifiziert; kein GESIS-Zugriff. Insbesondere wurde nicht behauptet, der niedrige Wichtigkeitspol belege eine ausdrückliche Ablehnungsposition. Ohne gegenteiligen Beleg wird aus dieser Zugangsgrenze kein neuer Fehler erfunden. Der direkte Originalabgleich ist im JSON separat als NICHT_GEPRÜFT und nicht erforderlich für diesen begrenzten Konsistenzcheck ausgewiesen.

Fundstellen: `docs/analyseplan-v2.3.entwurf.md:78,98-106,201,271`; `reports/claude/agenten/R6-eurobarometer.md:204`; R8-JSON, `kandidaten[id=R8-EB-SP568-QC9]`, Felder `wortlautDe`, `antwortkategorien`, `kontext`, `eignung`, `wortlautQuelle`. Die damalige R8-Empfehlung wird nicht stillschweigend überschrieben.

### Geänderter Tabellenhinweis

Der geänderte Hinweis in Plan 6 Nr. 3 behauptet keine bekannte auswertbare Fragebasis und keinen bekannten Nennerunterschied zum ESS. Er trennt das dokumentierte Frageuniversum vom ungeklärten Umgang mit fehlenden Antworten. Daraus folgt im P5-Interpretationsumfang kein neuer belegter Fehler. Die tragende Tabellenstruktur und der separate Methodenbefund werden hier nicht erneut geprüft. Keine Ergebnistabelle geöffnet.

Keine neuen Findings im gezielten Umfang. Quellenstopps, Wortlautbedingung, eingefrorenes Itemregister und Sperre bis zur Festschreibung bleiben erhalten. Das bestätigt Planregeln, keine ausgeführte Datenverarbeitung.

## Zugriff, Grenzen und technische Prüfung

Keine Dateien unter `data/raw/`, `data/local/`, `outputs/` oder `data/reference-*` geöffnet. Keine GESIS-Server und keine externen Ergebnistabellen. Keine Delegation und keine externen Nachrichten. Gedächtnisabgleich und Prüfskills wurden nur für Isolation, Hashbindung und begrenzte Urteilsform genutzt.

Einige anfangs zu große Toolausgaben wurden gekürzt. Die maßgeblichen Findings, JSON-Felder, Regelabschnitte und geänderten Passagen wurden anschließend gezielt erneut gelesen. Kein Quellenabruf scheiterte. Python `jsonschema` ist nicht verfügbar; `check-jsonschema` und `ajv` wurden nicht gefunden. Statt einer Installation wurde das eigene JSON im Arbeitsspeicher gegen die vom Urteilsschema verwendeten Strukturregeln und seine Urteilsbedingungen geprüft. Dieser Check belegt nur formale Konsistenz.

`pnpm check`, Pipeline-Tests und Browserprüfungen wurden nicht ausgeführt. Es gibt keine Implementierungsänderung; der Auftrag erlaubt ausschließlich die zwei Ergebnisdateien und keine weiteren Schreibvorgänge. Eigene Schreibvorgänge betrafen nur diese beiden Dateien. Der Abschlussstatus enthält außerdem zwei parallel entstandene P4-Runde-3-Dateien; deren Inhalte wurden nicht geöffnet. Keine Commits, Tags oder Pushes.

## Gelesene Dateien und Hashes

„Inhalt“ umfasst vollständige oder gezielte Text-/JSON-Lektüre; „nur Hash“ bezeichnet reine Pinprüfung ohne Ausgabe des Inhalts. P4-Dateien sind aus beiden Kategorien ausgeschlossen. Die Hashes stehen auch im JSON unter `execution.inputHashes`. OECD-Download und PDF-Auszug blieben im Arbeitsspeicher.

| Datei/Quelle | Zugriff | SHA-256 |
| --- | --- | --- |
| `.agents/skills/unslop/SKILL.md` | Inhalt | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `.claude/skills/life93-review/SKILL.md` | Inhalt | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | Inhalt | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `/home/stevenh/.codex/memories/MEMORY.md` | Inhalt | `76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9` |
| `/home/stevenh/.codex/memories/skills/bounded-pinned-review/SKILL.md` | Inhalt | `0e77a5f081bc588972fddd6e848d39fe5ae05fcf4e2833c3ef704221e90536c6` |
| `data/gruppenvertrag.v2.1.entwurf.json` | nur Hash | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `docs/abdeckung-v2.2.md` | Inhalt | `544deeb3055ffb174d8e3c97f6f4e5b6a640c8502113462cd3b6bcee6cb5e8f9` |
| `docs/analyseplan-v2.2.md` | Inhalt | `13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8` |
| `docs/analyseplan-v2.3.entwurf.md` | Inhalt | `c8af28353e85161e617aa1f29ed65afb5cedfc34350c6e8fde0aef8ca8114bef` |
| `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md` | Inhalt | `43a38f7ce21c19d7194a214805057aec7f8476f3df7cd7bd49d2dbbc4aad0bd8` |
| `docs/profilregeln-v1.md` | Inhalt | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` |
| `docs/project.md` | Inhalt | `2ff27e5aa553ea2307bd4d28da436991c5ebb3b019f316d9aae95ee81d57696a` |
| `docs/pruefregeln.md` | Inhalt | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` |
| `docs/quellenanfragen-v1.entwurf.md` | Inhalt | `d9a4b0b67a73a1669ad07fed7461237cb08c0df0b0f1eacb02b4918a2727e972` |
| `https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf` | Primärquelle, PDF S. 7 | `5672381901f57dcc2ee3e76a9b0716b6c418c3a69e1e85b804e29bb2c343ae10` |
| `reports/claude/agenten/R10-quellenblocker.json` | nur Hash | `8e15381892d91f62094c68573bb32148a5df21daf24ad11415549ef94861439a` |
| `reports/claude/agenten/R10-quellenblocker.md` | nur Hash | `65d79b32748197923c9614c7e8e85f19b06f516fa0cff869dbb7d3cf2f228885` |
| `reports/claude/agenten/R5-wvs.md` | nur Hash | `a163be6d448ab5f9e14b54293f355a2e0cea3c19d37e92a4d0021e8af7afc969` |
| `reports/claude/agenten/R6-eurobarometer.md` | Inhalt | `58b08b2af20d70261e95e7d0d815d4c083d95e0879cef5ee864c6ee05e84e8bb` |
| `reports/claude/agenten/R7-weitere-quellen.md` | nur Hash | `4e795f355ccd359613949a2e307f46150f31506cf817b51f1a4e232405f6fcd5` |
| `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json` | Inhalt | `23e27dd8c2c1e359fe62ff5df058fef4de749dce95ca1e6da44cec6839e49fa2` |
| `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.md` | Inhalt | `6830b4172d606b47fc6f00214fba09d776790143c85c01529b7c33256691c24b` |
| `reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.json` | nur Hash | `71e012d3b460917269153d261a4565f6bfbb34627220ee2cf14d8abf1af272d6` |
| `reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.md` | nur Hash | `42aaa648a36557d33b6bb316aff007f5f79f92779aa4875acdc74516c70ba5c3` |
| `reports/claude/agenten/S1-strukturpruefung-eurobarometer.json` | nur Hash | `f563bc2f138d67a00a9cf8fbfd80580dd3e842108d17231b44efb241edbc9575` |
| `reports/claude/agenten/S1-strukturpruefung-eurobarometer.md` | nur Hash | `15b2851d4e383a50ae064b566b1f2d6419180d3899f20007b49c07fe607295c0` |
| `reports/claude/auftraege/P5-runde3-plan-v23.md` | Inhalt | `229e8fc53500591958cc6d0bd2ea5691d5f9ea584c28359f08ef7cf19e12def8` |
| `reports/claude/auftraege/R-erweiterung-gemeinsam.md` | nur Hash | `56970a37d162e3996cace441b4f41c44d7e4e3bfd408d008c13e3f9ba0898ccd` |
| `reports/claude/pruefungen/P5-quellen-fairness-v23.json` | Inhalt | `d5393faca0fdaf80ac906621b94fc0dad498b25ce1877d0220ef650d4f1d8878` |
| `reports/claude/pruefungen/P5-quellen-fairness-v23.md` | Inhalt | `bbd1b5cd21370863d95bdb3d1056ae9634ed52554d253189d30fa0e05e69f25d` |
| `reports/claude/pruefungen/P5-runde2-quellen-fairness-v23.json` | Inhalt | `36b0a23d1c292d7ea8528cb4c7d02d85b4cfe4dc5c57fa2c0b48cf0dbd73cb8d` |
| `reports/claude/pruefungen/P5-runde2-quellen-fairness-v23.md` | Inhalt | `1ca5f460dd6303e7b85043c2ceb057b71d3430e4b1eb8dfe461e826e89b19ef9` |
| `reports/claude/pruefungen/PLAN-V23-003-manifest.json` | Inhalt | `96b20f220f8757a24ce880eee106e9fa7cd2aca3c234410786acd32d7a6a347d` |

## Ausgeführte Befehle und Werkzeuge

Die Lese-, Hash-, Quellen- und Schreibbefehle endeten mit Exit 0; ebenso `pdftotext` und der Git-Abstammungscheck. Verfügbarkeitsproben meldeten fehlende Validatoren. Der erste Abschluss-Scopecheck endete mit Exit 1: Er erwartete fälschlich ausschließlich die zwei eigenen untracked Dateien im gemeinsamen Worktree. Inzwischen waren zusätzlich `P4-runde3-methoden-v23.md` und `.json` erschienen. Nur ihre Pfade wurden gesehen, keine Inhalte gelesen oder gehasht. Der korrigierte Check erlaubt diese fremden Pfade und prüft den eigenen Schreibumfang. Die Schema-Prüfung mit zwei verworfenen Negativkontrollen sowie alle Input-/Vorgängerhashprüfungen waren bereits vor dieser eigenen Assertion bestanden. Kein Paketfehler.

- `sha256sum reports/claude/auftraege/P5-runde3-plan-v23.md reports/claude/pruefungen/PLAN-V23-003-manifest.json` vor Beginn; später SHA-256 per Python `hashlib` für zulässige Manifestartefakte und gelesene Zusatzdateien, gegen Manifest bzw. eigene Inputhashes vor und nach Schreiben.
- `git status --short`, `git rev-parse HEAD`, `git branch --show-current`; `git merge-base --is-ancestor 42b6068b22a0c4fd413c4dac65ed6675b4192d6a HEAD` über Python; `git diff f2c8d0d -- docs/`; nach fremder HEAD-Änderung `git diff --name-status f169a1dbc704ef50bb94f8babeb0fe55a9a7f49d HEAD`. Der letzte Vergleich gab nur Pfade aus.
- `cat` für Auftrag, Manifest, Prüfskill, Urteilsschema, unslop, project.md, P5-Runde-1/-2-Berichte und Basisregeln. `nl -ba … | sed -n …` für Planabschnitte 1–116, 115–159, 177–272, 197–230, Entscheidungsvorlage 24–43, Quellenanfragen 70–85, P5-Erstbericht 1–100 und Prüfregeln 43–60. `wc -l` für Basisdokumente und P5-Erstbericht.
- `rg -n -C 5 'SP568|QC9|Wichtigkeit|importance'` nur in R6 und R8; gezielte Python-JSON-Auszüge zu F02/F05 und R8-QC9. Für gekürzte Ausgaben erneute Python-/sed-Auszüge, teils mit zusammengezogenen Leerzeichen der Tabellen: Abdeckung 24–80 und 69–77, Prüfregeln 40–60, Plan 117–140 und 263–271.
- Gedächtnisabgleich: `rg -n 'bounded|begrenz|immutable|Pins|Prüf' …/MEMORY.md`, `nl -ba …/MEMORY.md | sed -n '50,59p'`, `cat …/skills/bounded-pinned-review/SKILL.md`; Hashprüfung der beiden Gedächtnisdateien. Keine fachlichen Fremdurteile aus Rollout-Dateien gelesen.
- `web.run open` auf den OECD-Kernfragebogen; `urllib.request.urlopen` auf exakt dieselbe HTTPS-URL, HTTP 200 ohne abweichende Ziel-URL; SHA-256 des PDF im Arbeitsspeicher; `pdftotext -f 7 -l 7 - -` über stdin/stdout.
- `rg --files .claude/skills/life93-review`, `command -v check-jsonschema || true`, `command -v ajv || true`; Python-Importprobe für `jsonschema`, mit abgefangenem ImportError. Keine Pakete installiert.
- Python-Standardbibliotheksprüfungen: neun vorgeschlagene EB-Zeilen mit Geltungsbereich 6/1/1/1; zehn OECD-Items b-j/l mit Zurückstellungsgrund; Berichtserzeugung nur in den beiden erlaubten Pfaden; anschließende JSON-Schema-Struktur-/Urteilskontrolle und Input-/Vorgängerhashprüfung. Kein QA-Skript und keine andere Datei geschrieben.

## Modell laut Laufzeit

OpenAI, `gpt-6.1-sol`, Codex-Harness in T3 Code, Reasoning `high`, laut bereitgestellter Laufzeitangabe. Interne Modellrevision und Anbieterregeln nicht bekannt. Der Nutzerprompt steht im JSON, der ergänzende Auftrag ist durch seinen vollständigen Dateiinhalt und SHA-256 gebunden.

Berichtserstellung (UTC): `2026-10-04T00:25:56.009244+00:00`.
