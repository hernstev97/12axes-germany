# T2 Runde 2: gezielte technische Nachprüfung

Stand: 4. Oktober 2026. Begrenztes KI-Review durch Codex (OpenAI).

Gesamturteil: **BESTANDEN für den beauftragten Umfang**. T2-F01 bis T2-F05 sind KORRIGIERT. Keine neuen Findings durch die geprüften Korrekturen. Das Urteil bestätigt die Codebedingungen, die öffentliche Berichtskonsistenz und die ausgeführten Komponententests; es bestätigt keine erneut ausgeführten Browser- oder Datenläufe.

## Gegenstand und Bindung

Der SHA-256 des vollständig gelesenen Umfangsmanifests `reports/claude/auftraege/T2-runde2-technik.md` stimmt mit dem außerhalb der Datei übermittelten Wert überein: `13d1c6324cfc7c0ec2d9c17e15e99c326c4a8e096a38a08e6eaecee6e45603e8`.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`. Branch: `research/life-93-claude-20261003`. HEAD bei Beginn und vor Berichtsschreiben: `75c6f8b285bc8e9414b547ccbe4609e0a9592f68`.

Geprüft wurde ausschließlich der bezeichnete Korrektur-Diff `46e70be..da10fdf` und der unmittelbare Kontext der fünf Findings. `s1_struktur.py` wurde durch einen ausdrücklichen Git-Pathspec ausgeschlossen. Sein Name und seine Größe erschienen zuvor in der Diff-Dateiliste/-Statistik; sein Inhalt wurde nicht gelesen. Die bewerteten aktuellen Dateien sind gegenüber `da10fdf` unverändert.

Runde-1-Bericht und JSON waren ausdrücklich zugelassen. Beide bleiben bytegleich mit den unten gebundenen Hashes. Die Projektregeln wurden als geltende Vorgaben gelesen, weitere fachliche Recherche oder Gesamtprüfung fand nicht statt.

## Stand der Findings

| ID | Schweregrad aus Runde 1 | Zustand Runde 2 | blockiert |
| --- | --- | --- | --- |
| T2-F01 | mittel | KORRIGIERT | nein |
| T2-F02 | mittel | KORRIGIERT | nein |
| T2-F03 | mittel | KORRIGIERT | nein |
| T2-F04 | mittel | KORRIGIERT | nein |
| T2-F05 | niedrig | KORRIGIERT | nein |

### T2-F01

Radio-Ziel, :focus-visible und 2-px-Outline sind assertiert. Reset und Übersicht warten auf den Überschriftfokus, bevor der Ablauf fortgesetzt wird. Die Dokumentation nennt jetzt die konkreten Wechsel.

Fundstellen:

- scripts/check-research-engines.mjs:169-191: Tab-Suche und Assertions auf Radio-Namen, :focus-visible und solid 2px.
- scripts/check-research-engines.mjs:220-221,323-327: Fokus nach Reset auf draft-question-title und nach Übersichtwechsel vor dem Fernsprung geprüft.
- docs/validation.md:78: einzelne geprüfte Wechsel und Radio-Rahmen benannt.

Nachprüfung: Diff und aktuelle Bedingungen statisch nachgeprüft; node --check bestanden. Chromium/Firefox und synthetische Browser-Negativproben laut Auftrag nicht ausgeführt.

### T2-F02

Die Mitschrift startet vor dem Laden und bleibt bis zum letzten Prüfpunkt kumulativ. setItem/removeItem kann die Spur nicht mehr löschen. Nicht prüfbare APIs stehen im Bericht als NICHT_GEPRÜFT beziehungsweise privacy.notChecked; property-Zuweisungen sind ausdrücklich als Grenze dokumentiert.

Fundstellen:

- scripts/check-research-engines.mjs:53-84: addInitScript vor newPage/goto; Mitschrift für Storage.setItem, indexedDB.open, caches.open, serviceWorker.register und document.cookie.
- scripts/check-research-engines.mjs:104-127,166,265-267,322,333: kumulative Aufrufe und Zustände an vier Prüfpunkten; gespeicherte Aufrufliste muss leer sein.
- scripts/check-research-engines.mjs:111-115,334-339: NICHT_GEPRÜFT und privacy.notChecked statt ungeprüft leer.
- docs/validation.md:78: property-Zuweisungen localStorage.x ausdrücklich von der Mitschrift ausgenommen; Zustandsprüfung und behaupteter konkreter Lauf getrennt lesbar.

Nachprüfung: Initialisierungsreihenfolge, Lebensdauer der Aufrufliste, Assertions und NICHT_GEPRÜFT-Zweige statisch geprüft. Keine Browser-Negativprobe oder Sichtung der privaten Laufbelege.

### T2-F03

Einzelne fehlende Kategorienbereiche erscheinen als „kein 95-%-Bereich“, vollständig fehlende Gruppenbereiche mit einem eigenen Hinweis. Der angepasste Test prüft die gemischte Einzelreferenz, die Gruppe ohne Bereiche und genau eine gemeinsame Erklärung.

Fundstellen:

- web/src/app/policy-draft/policy-draft.html:520-535: fehlende Einzelkategorien mit interval-none, vollständig fehlende Bereiche mit interval-missing.
- web/src/app/policy-draft/policy-draft.html:611-627: entsprechender Gruppen-Kategoriezweig und Hinweis bei fehlenden Gruppenbereichen.
- web/src/app/policy-draft/policy-draft.html:205-215: genau eine gemeinsame Erklärung, einschließlich fehlender Bereich bedeutet keine Unsicherheit von null.
- web/src/app/policy-draft/policy-draft.spec.ts:24-30,221-249: gemischte Einzelkategorien und Gruppe ohne Bereiche samt Missing-Assertions und genau einer Erklärung.
- pnpm check: 113 Webtests in zehn Dateien bestanden, einschließlich des geänderten Komponententests.

Nachprüfung: Template gegen Analyseplan 4.2/4.3 und Referenzansicht geprüft; geänderter Komponententest im erfolgreichen pnpm check ausgeführt. Gemischte Gruppenkategorien nur statisch geprüft, nicht als zusätzlicher eigener Testfall ausgegeben; Browserprüfung ausgeschlossen.

### T2-F04

sav_gegenprobe.py entscheidet jetzt anhand von acht Prüfungen über Status und Exitcode. Duplikate und fehlerhafte Eins-zu-eins-Zuordnung führen vor der Rechnung zum negativen Abschluss; Dekoderabweichungen und Abweichungen über 1e-12 verhindern Erfolg. Die SDDF- und ESS9-Gegenproben haben passende negative Statuspfade. Die drei öffentlichen JSONs sind konsistent, und alle alten Aggregate/Laufhashes bleiben gegenüber 46e70be unverändert.

Fundstellen:

- reports/claude/kontrollrechnung/sav_gegenprobe.py:167-169,210-235: früher Abschluss bei Duplikaten/Zuordnungslücken; acht Prüfungen mit BESTANDEN/NICHT_BESTANDEN und Exit 0/1.
- reports/claude/kontrollrechnung/sav_gegenprobe.py:46-48,225-228: Toleranz 1e-12 mit Begründung der Gleitkomma-/Summationsabweichung.
- reports/claude/kontrollrechnung/sddf_gegenprobe.py:120-126,157-167; ess9_gruppen_gegenprobe.py:65-74: Zuordnungs-/Duplikatprüfung, numerischer Status und Exitcode auch für die beiden zusätzlichen Gegenproben.
- sav-gegenprobe.json, sddf-gegenprobe.json, ess9-gruppen-gegenprobe.json: Statusfelder aus gespeicherten Aggregaten konsistent; sämtliche vorbestehenden Aggregate und Laufhashes gegenüber 46e70be unverändert.
- reports/claude/kontrollrechnung/sav-gegenprobe.md:31; reports/claude/datenzugriff.md:20: Statusregel, behauptete synthetische Autorprüfung und erneuter Datenzugriff dokumentiert.

Nachprüfung: Kontrollfluss statisch geprüft, drei Python-Dateien ausschließlich per ast.parse auf Syntax geprüft; gespeicherte JSON-Aggregate und neue Statusfelder mit Inline-Python geprüft. Kein Import oder Ausführen der Datenskripte, keine privaten Dateien gelesen, synthetische Autorproben nicht unabhängig ausgeführt.

### T2-F05

„Messfehler einzelner Antworten“ steht jetzt im Text und in einer Testassertion. Der Text enthält sämtliche Ausschlüsse aus Analyseplan 4.3.

Fundstellen:

- docs/analyseplan-v2.2.md:88-90: verbindliche Ausschlüsse.
- web/src/app/policy-draft/policy-draft.html:207-214: Zeitabstand, Befragungsmodus, Nichtteilnahme, neuer Fragekontext und Messfehler einzelner Antworten ausdrücklich ausgeschlossen; persönliche Unsicherheit getrennt.
- web/src/app/policy-draft/policy-draft.spec.ts:226-229: genau eine Erklärung und Messfehlertext assertiert; Komponententest im pnpm check bestanden.

Nachprüfung: Vollständiger Abgleich der Ausschlüsse aus Analyseplan 4.3 gegen den Text; Komponententest durch pnpm check bestanden.

## Checks und Urteil

| Check | Umfang | Urteil | erforderlich |
| --- | --- | --- | --- |
| T2-R2-C01 | Manifest, Branch, HEAD und Bindung des begrenzten Korrekturstands | BESTANDEN | ja |
| T2-R2-C02 | T2-F01: gezielte Code-/Komponentennachprüfung | BESTANDEN | ja |
| T2-R2-C03 | T2-F02: gezielte Code-/Komponentennachprüfung | BESTANDEN | ja |
| T2-R2-C04 | T2-F03: gezielte Code-/Komponentennachprüfung | BESTANDEN | ja |
| T2-R2-C05 | T2-F04: gezielte Code-/Komponentennachprüfung | BESTANDEN | ja |
| T2-R2-C06 | T2-F05: gezielte Code-/Komponentennachprüfung | BESTANDEN | ja |
| T2-R2-C07 | pnpm check | BESTANDEN | ja |
| T2-R2-C08 | Syntax, öffentliche Gegenproben und Diff | BESTANDEN | ja |
| T2-R2-C09 | Eigene Browser-/Datenläufe und Autor-Negativproben | NICHT_GEPRÜFT | nein |
| T2-R2-C10 | Wissenschaftliche und menschliche Abnahmen sowie Veröffentlichung | IN_DIESER_PHASE_NICHT_ERFORDERLICH | nein |

`pnpm check` endete mit Exit 0: Formatierung, Handbuch, 20 synthetische Schemafälle, Typprüfung, 113 Webtests in zehn Dateien und Produktionsbuild bestanden. `node --check`, die ausschließlich syntaktische AST-Prüfung der drei Gegenprobenskripte, die öffentliche JSON-Konsistenzprüfung und `git diff --check` bestanden ebenfalls.

Für die neuen JSON-Statusfelder wurde nachgerechnet, ob die gespeicherten Zählungen, Abweichungen und Toleranzen dazu passen. Alle vorherigen Aggregate und Laufhashes bleiben gegenüber `46e70be` gleich. Das ist eine Prüfung der öffentlichen Berichte, keine erneute Datenrechnung und kein Beleg für ihre tatsächliche Erzeugung.

## Grenzen und Arbeitszustand

- BESTANDEN gilt ausschließlich für die gezielte Nachprüfung T2-F01 bis T2-F05 und mögliche Fehler durch die benannten Korrekturen. Keine vollständige neue Paketprüfung, keine Übernahme anderer Abnahmen.
- Browser- und Datenskripte wurden weder importiert noch ausgeführt. Keine Dateien unter data/raw/, data/local/ oder outputs/ gelesen; dortige Pfade in öffentlichen Dokumenten sind nur Text. s1_struktur.py nicht gelesen oder bewertet; sein Dateiname erschien in Git-Metadaten.
- Tatsächliche Chromium-/Firefox-Läufe, Screenshots, Browser-Negativproben, Rohdatenrechnung und synthetische Autor-Negativproben der Gegenproben sind NICHT_GEPRÜFT. Ihre Dokumentation wird nicht als eigener Laufbeleg ausgegeben.
- Die Speicherinstrumentierung erfasst benannte Methoden im Seitenkontext. Property-Zuweisungen mit anschließendem Löschen zwischen Prüfpunkten sind ausdrücklich nicht abgedeckt. Nicht verfügbare APIs sind als ungeprüft protokollierbar; ein Gesamt-PASS besagt dann keinen vollständigen Speichercheck.
- Der Test für gemischte Einzelkategorien und die Gruppe ohne Bereiche lief; der entsprechende neue Zweig für gemischte Gruppenkategorien wurde statisch nachgeprüft, ohne zusätzliche Testfixture.
- Kein wissenschaftliches, empirisches, Neutralitäts-, menschliches, Design- oder Veröffentlichungsurteil. Frühere T2-Grenzen außerhalb F01-F05 bleiben unbewertet erhalten.
- Nur die beiden beauftragten Ergebnisdateien selbst geschrieben. Der erlaubte pnpm check erzeugt übliche ignorierte Build-/Testartefakte. Keine Commits, Pushes, Tags, Delegationen oder Nachrichten an andere Personen/Agenten.
- Bei Beginn war git status --short leer. Später erschienen fremde Änderungen an s1_struktur.py und zwei unversionierte P4/P5-Aufträge; nur Statusmetadaten gesehen, keine Inhalte gelesen oder verändert. HEAD blieb 75c6f8b285bc8e9414b547ccbe4609e0a9592f68. Alle 39 gebundenen Eingaben vor dem Schreiben erneut unverändert.
- Einige Sammelausgaben der Werkzeuge wurden gekürzt; relevante Finding-Bedingungen, Gegenproben und Runde-1-Bericht wurden mit getrennten Ansichten nachgelesen. Keine fehlgeschlagenen Prüfkommandos oder Zugriffsversuche auf gesperrte Pfade.
- Memory.md nur für allgemeine Prüfabgrenzung, Zeilen 52-55; kein aktueller technischer Befund oder früheres fremdes Sachurteil daraus übernommen. Die Bewertung beruht auf Auftrag, Diff, aktuellen Dateien und ausgeführten technischen Checks.

## Ausführungsnachweis

Modell laut Laufzeit: OpenAI `gpt-6.1-sol`, high reasoning effort, Codex harness in T3 Code. Genauere interne Revision nicht nachgewiesen. Dies ist ein KI-Review.

Ursprünglicher Auftrag im Wortlaut:

```text
Act as the review sub-agent for this task.

Lies und befolge den Auftrag in /home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c/reports/claude/auftraege/T2-runde2-technik.md vollständig. Arbeitsverzeichnis ist dieser Worktree. Der Auftrag ist das Umfangsmanifest; sein SHA-256 lautet 13d1c6324cfc7c0ec2d9c17e15e99c326c4a8e096a38a08e6eaecee6e45603e8. Prüfe ihn vor Beginn. Stand beim Auftrag: HEAD 75c6f8b285bc8e9414b547ccbe4609e0a9592f68 auf dem Branch research/life-93-claude-20261003. Schreibe nur die beiden im Auftrag genannten Ergebnisdateien. Keine Commits, Pushes, Tags oder Nachrichten. Nichts unter data/raw/, data/local/ oder outputs/ lesen. Am Ende fasse Gesamturteil und Stand der Findings in wenigen Sätzen zusammen.
```

### Gelesene Dateien mit SHA-256

Die Liste bindet vollständig oder ausschnittsweise gelesene Dateien einschließlich Textsuchtreffern. Bei ergänzenden Regeln und Sicherheitssuchen bedeutet ein Hash keine vollständige fachliche Neubewertung. Transitive pnpm-Eingaben werden durch den technischen Lauf erfasst und nicht als manuell vollständig gelesene Dateien ausgegeben. Die ersten 29 Pins wurden vor der inhaltlichen Diff-Nachprüfung erfasst, die weiteren zehn beim ergänzenden Zugriff; alle 39 vor dem Berichtsschreiben erneut verglichen.

| Datei | SHA-256 |
| --- | --- |
| `reports/claude/auftraege/T2-runde2-technik.md` | `13d1c6324cfc7c0ec2d9c17e15e99c326c4a8e096a38a08e6eaecee6e45603e8` |
| `.claude/skills/life93-review/SKILL.md` | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `.agents/skills/unslop/SKILL.md` | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `reports/claude/pruefungen/T2-technik-v22.md` | `5bc82e7e331a2fdb32a833ed5ef8bc8d798f1ad3968f96decd574c7f0e9ba588` |
| `reports/claude/pruefungen/T2-technik-v22.json` | `5e600e209335569e856cc0782e6b66b82034398cb893148c3ca862c5304b0dcf` |
| `docs/project.md` | `9f827fdd40d5f9a4239043a5fb21ec84fa93805141566ac5b68e455a63d8bba6` |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |
| `docs/analyseplan-v2.2.md` | `13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8` |
| `docs/abdeckung-v2.2.md` | `618012f903783c749b751cb32c8acffab1e7ca09765cd80a26a2a2c1cbeb8b70` |
| `docs/profilregeln-v1.md` | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` |
| `docs/pruefregeln.md` | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` |
| `package.json` | `451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7` |
| `web/package.json` | `77db8383e6c64f65fe04638c46ba3b7f9b40040d95f0ad3ced1471fb475d60f7` |
| `scripts/check-handbuch.mjs` | `ebb9815ee0341fab5ad8aa58f01dec459dcdc08b75ca87f5a81707bab50e2813` |
| `scripts/check-review-schema.mjs` | `2575997f720f0c440fc54a9ccc15a2bd8c8fb69638dab8c03cf8b9fdaf810166` |
| `scripts/check-research-engines.mjs` | `2c51e60ea6ff5bf184ac71cfc1f5a868b68b1ddff3a495021a660d3ab8770ae7` |
| `docs/validation.md` | `04b23203eacf00b0299b26fea97acb8dc410514bc2b10a83914e7d64cc2a1c39` |
| `reports/claude/datenzugriff.md` | `14081a45864c8a4ab4d1e0be1d5739c32a039fce5af4140248389e5c0a2742bf` |
| `reports/claude/kontrollrechnung/ess9-gruppen-gegenprobe.json` | `d72311f935a9e1a7027916c8e76dfd874863a4f1cadebe14cf36241df75bc9b2` |
| `reports/claude/kontrollrechnung/ess9_gruppen_gegenprobe.py` | `9a24b36788635e024672a47f127409c6ae60dbdcf29385ce8ea60b38b0182cfe` |
| `reports/claude/kontrollrechnung/sav-gegenprobe.json` | `a1ea8934e40cf26a0cb3c898be296114f81eacea072c3021e6678fdcc9da42bb` |
| `reports/claude/kontrollrechnung/sav-gegenprobe.md` | `fd6091951c76c4fc84c0f2f4beb722c5e7a89ceeb94cd72086cc981a676caef4` |
| `reports/claude/kontrollrechnung/sav_gegenprobe.py` | `d6f9427d766e0d24962ef953be64d07cab03b8e3e8a0fa3857f5a8004acd9b79` |
| `reports/claude/kontrollrechnung/sddf-gegenprobe.json` | `0998b5f9ac2904b29d77f2050b905d1166e324f7c0bba5f8860e234de524e9ba` |
| `reports/claude/kontrollrechnung/sddf_gegenprobe.py` | `f70b0d753b927277ef0ed9180b782d466d55208fe355967437112a1eef872a63` |
| `web/src/app/policy-draft/policy-draft.html` | `f25712dc8d6fbd85c5d93fa4c6db8c006fe5132282db06f922733fd9e2c94b2a` |
| `web/src/app/policy-draft/policy-draft.spec.ts` | `5e35eed8fc3c3d8fff2cb65bd28ca96b977c40cceb7fc00ea050d455e2850969` |
| `web/src/app/policy-draft/policy-draft.ts` | `f26b1a53e40e80ed12a1a32c2c754876c938d50ee6f1110ef99f67ddc64fad09` |
| `.prettierignore` | `08a4df06f736d54e36b84502d1452185812e04966191918a39d299523d3c2531` |
| `web/angular.json` | `91c9042107b35de10321454587d64abbd7cd18cd25ea345319dd0378b8337ed8` |
| `web/src/app/policy-draft/generate-references-v22.mjs` | `754c20ce770a53f7e0f8cbfe64de0d4cf826a008d02a3f136328817eaeb03b96` |
| `web/src/app/policy-draft/generate-public-catalogue-v22.mjs` | `a9854873edaf9086bf4741e6bd966e2ce98c4f73f599922e488744713b02535a` |
| `web/src/app/policy-draft/group-reference-generator.test.mjs` | `7891c73f95af6f33ea745524d716b8c395bd5421d3ce193b31c5fbe17e87008c` |
| `web/src/app/policy-draft/group-reference-generator.mjs` | `f12a6e8eb528d9776741b8cab5cb327e5d5714d951fd3dfa157075832ad93a9f` |
| `web/src/app/policy-draft/generate-reviewed-references.mjs` | `e7389ab3b21e6584b4ce30eb00fd8c196e849577e0e0b971bce118ee6b1d565a` |
| `web/src/app/policy-draft/verify-public-catalogue.mjs` | `b9156684e80949abbd4223708334159a5945b226ed674b6f158f072ed80450f7` |
| `web/src/app/policy-draft/reference-generator.test.mjs` | `0165d5d945ec01061e87dfb5c40ba22b6efd758c308bf967ecd3090d437676f9` |
| `/home/stevenh/.codex/memories/MEMORY.md` | `76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9` |

### Ausgeführte Befehle und Werkzeuge

Einzelbefehle aus zusammengefassten Shellaufrufen sind getrennt aufgeführt; wiederholte Lektüre wegen gekürzter Ausgaben wird nicht mehrfach gezählt. `<sechs Umfangspfade>` bezeichnet wörtlich die sechs Pathspecs aus dem Manifest. Inline-Python ist als Kurzform gekennzeichnet und hat ausschließlich die benannten öffentlichen Dateien, Regeln oder Memory-Datei gelesen.

```text
sha256sum reports/claude/auftraege/T2-runde2-technik.md
cat reports/claude/auftraege/T2-runde2-technik.md
rg -n 'bounded|begrenz|Pins|T2-runde|immutable' /home/stevenh/.codex/memories/MEMORY.md
sed -n '45,60p' /home/stevenh/.codex/memories/MEMORY.md
cat .claude/skills/life93-review/SKILL.md
cat .agents/skills/unslop/SKILL.md
git status --short
git branch --show-current
git rev-parse HEAD
cat reports/claude/pruefungen/T2-technik-v22.md
cat reports/claude/pruefungen/T2-technik-v22.json
cat .claude/skills/life93-review/references/urteil-schema.json
cat docs/project.md
cat package.json
cat web/package.json
git diff --stat 46e70be..da10fdf -- <sechs Umfangspfade aus Manifest>
git diff --name-only 46e70be..da10fdf -- <sechs Umfangspfade aus Manifest>
python3 - <<'PY' ... SHA-256 der ersten 29 benannten Eingaben; git diff da10fdf für die bewerteten aktuellen Artefakte ... PY
cat docs/handbuch.md
cat docs/analyseplan-v2.2.md
cat docs/abdeckung-v2.2.md
cat docs/profilregeln-v1.md
cat docs/pruefregeln.md
git diff 46e70be..da10fdf -- <sechs Umfangspfade> ':(exclude)reports/claude/kontrollrechnung/s1_struktur.py'
git diff 46e70be..da10fdf -- reports/claude/kontrollrechnung/ docs/validation.md reports/claude/datenzugriff.md ':(exclude)reports/claude/kontrollrechnung/s1_struktur.py'
cat scripts/check-handbuch.mjs
cat scripts/check-review-schema.mjs
nl -ba scripts/check-research-engines.mjs
nl -ba reports/claude/kontrollrechnung/sav_gegenprobe.py
nl -ba reports/claude/kontrollrechnung/sddf_gegenprobe.py
nl -ba reports/claude/kontrollrechnung/ess9_gruppen_gegenprobe.py
nl -ba web/src/app/policy-draft/policy-draft.html | sed -n '190,222p;490,560p;575,650p'
nl -ba web/src/app/policy-draft/policy-draft.spec.ts | sed -n '1,120p;175,270p'
rg -n -A 16 -B 8 'hasIntervals|intervals|references' web/src/app/policy-draft/policy-draft.ts
nl -ba web/src/app/policy-draft/policy-draft.spec.ts | sed -n '34,120p;175,260p'
cat reports/claude/kontrollrechnung/sav-gegenprobe.json
cat reports/claude/kontrollrechnung/sddf-gegenprobe.json
cat reports/claude/kontrollrechnung/ess9-gruppen-gegenprobe.json
cat reports/claude/kontrollrechnung/sav-gegenprobe.md
nl -ba reports/claude/datenzugriff.md
cat .prettierignore
cat web/angular.json
rg -n 'data/(raw|local)|outputs/|readFile|readdir|node:fs|child_process' web/src scripts/check-handbuch.mjs scripts/check-review-schema.mjs web/package.json
sed -n '140,215p' scripts/check-handbuch.mjs
sed -n '44,65p' docs/abdeckung-v2.2.md
pnpm check
python3 - <<'PY' ... zehn ergänzende Eingabehashes; ast.parse der drei Skripte; JSON-Status-/Aggregatprüfung und Vergleich mit git show 46e70be:<drei öffentliche JSON-Pfade> ... PY
node --check scripts/check-research-engines.mjs
sed -n '65,81p' docs/abdeckung-v2.2.md
nl -ba docs/validation.md | sed -n '68,82p'
python3 - <<'PY' ... Runde-1-Status, IDs, Schweregrade und Zustände aus dem ausdrücklich erlaubten T2-JSON ... PY
python3 - <<'PY' ... erneuter SHA-256-Vergleich aller 39 Eingaben; git rev-parse HEAD; git status --short ... PY
git diff --check 46e70be..da10fdf -- <sechs Umfangspfade> ':(exclude)reports/claude/kontrollrechnung/s1_struktur.py'
sed -n '45,72p' docs/pruefregeln.md
```

`write_stdin` wartete auf den erlaubten pnpm-Lauf. Anschließend schreibt `apply_patch` ausschließlich die beiden beauftragten Ergebnisdateien. Die Abschlusskontrolle validiert das konkrete JSON mit Ajv2020 gegen das gelesene Urteilsschema, prüft die fünf Zustände und Berichtskonsistenz und vergleicht erneut sämtliche Eingabehashes. Git-Status und Ergebnisdatei-Hashes werden abschließend abgefragt; fremde Dateien bleiben unangetastet.

```text
node --input-type=module - <<'JS' ... Ajv2020(strict:true, allErrors:true), Schema und konkretes Runde-2-JSON; fünf korrigierte Findings; SHA-256-Abgleich aller 39 Eingaben und Berichtskonsistenz ... JS
git status --short
git diff --name-only
git rev-parse HEAD
sha256sum reports/claude/pruefungen/T2-runde2-technik-v22.md reports/claude/pruefungen/T2-runde2-technik-v22.json
```

Modell laut Laufzeit: `gpt-6.1-sol` (OpenAI), high reasoning effort.

