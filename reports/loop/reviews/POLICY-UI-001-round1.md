# POLICY-UI-001 – gezielte Runde 1

Entscheidung: **ACCEPTED_BOUNDED** für `POLICY-UI-001/v2` mit dem Manifest-SHA-256 `b82dfe72af5e0b9182d70276138f432b2dea0ed97fa40c3acc4863dd81b2a6e8`.

Prüfdatum: 3. Oktober 2026. Worktree: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Prüfer: Codex, Laufzeitangabe `gpt-6.1-sol`, Reasoning `ultra`.

Die drei lokalen Erstbefunde sind behoben. Die elf äußeren Pins und alle neun internen Dateihashes samt Bytezahlen stimmen vor und nach der Prüfung. Die ergänzten Samplingangaben, der eng begrenzte Textumbruch und die neue Quellenversion erzeugen im geprüften Umfang keinen neuen Blocker. Dieses Urteil gilt für den lokalen Vorschlag und die gezielt geprüften Änderungen. Es ist keine Human-Design-, Produkt-, Release-, Quellenidentitäts- oder empirische Äquivalenzabnahme.

## Prüfrahmen und erhaltene Ausgangsfassung

Der Erstbericht wurde vor dieser Runde vollständig gelesen. Sein SHA-256 bleibt `05dd80a6189acb0c48905ee0336b6db9e023bb65398933eb3b4d00738e2332e7`. Er wurde nicht überschrieben. Auch die ursprüngliche Probe bleibt bytegleich unter ihrem SHA-256 `4442d27916eb107ba63962275d257bfdb2046113684788e08f09f87f55abbfb1`. Die vollständige Handbuchlektüre und der gelesene unslop-Skill aus der Erstprüfung gelten weiter; der Handbuch-Pin ist unverändert. Der dortige Absatz „Test und Ergebnis“ steht in Zeile 147, nicht in der im Erstbericht versehentlich genannten Leerzeile 146.

Der v2-Manifest-SHA wurde zuerst aus der Datei berechnet und stimmt mit dem später nachgereichten User-Pin überein. Die Sicherung des v1-Pakets und Erstberichts im Remote-Commit `7b03f4c6ccc317a3968a1f9693a744c457f1f7e0` ist eine Angabe des Auftrags. Sie wurde ohne Git-/Remotezugriff nicht unabhängig überprüft.

Dies ist ein gezielter Folgereview nach Kenntnis des eigenen Ersturteils, kein frischer verblindeter Gesamtaudit. Gelesen wurden der erlaubte Erstbericht, die betroffenen Manifestartefakte und eigene Prüfmittel. Andere Reports, state, handoff und fremde Urteile wurden nicht geöffnet. Kein Git, Raw-/CSV-/Header-/Privatdatenzugriff, keine Antwort-/Frequenz-/Partyabfrage, kein Browser, Server, pnpm, Authzugriff, Claude oder Subagent. Der Generator wurde weder ausgeführt noch importiert. Schreibzugriffe betreffen nur eigene Dateien in `outputs/loop/policy-ui-001-review/` und diesen neuen Bericht.

Root und ich sind beide Codex. Die Runde ist keine Gegenprüfung durch eine andere Modellfamilie. Gemeinsame Fehlerquellen bleiben die Überschätzung semantischer Gleichwertigkeit und die Verwechslung technischer Konsistenz mit Quellennachweis oder empirischer Äquivalenz. Ein tatsächlicher Modellfehler von Root wurde hier nicht untersucht. Die Erklärung der früheren `prepare.py`-Anpassung stammt aus dem Auftrag; geprüft wurde der konkrete neue Dateistand.

## Abschluss der Erstbefunde

| Befund | Konkrete v2-Evidenz | Entscheidung und Umfang |
| --- | --- | --- |
| PUI-R1 | `prototype.js:50–52`: „Mehr Aus- und Weiterbildung, weniger Arbeitslosenunterstützung“. Der Absatz erhält die feste Geldsumme. `catalogue.js:979–983` enthält weiter die ursprüngliche Mengenverschiebung und Einleitung. | Geschlossen. Der Titel behauptet keinen vollständigen Ersatz der Unterstützung mehr. |
| PUI-R2 | `prototype.js:20`, `:24`, `:28`: Zustimmung oder Ablehnung der jeweiligen Aussage darüber, wann eine Gesellschaft gerecht ist. „Mehr verdienen als andere“, fehlende Gegenleistung und hohe Familienstellung bleiben enthalten. Die zugehörigen Originalaussagen stehen in `catalogue.js:440–443`, `:494–497`, `:548–551`. | Geschlossen. Die drei Sätze bleiben an die konkreten Gerechtigkeitsaussagen gebunden; keine allgemeine Maßnahme oder moralische Personeneigenschaft wird ergänzt. |
| PUI-R3 | Interner `prepare.py`-Pin `7bed0f5fe468c7daa2e8962a3174fbcd674012a035aa54dc01f9af0036795d73`, 4842 Bytes, stimmt mit Datei und äußerem Manifest. Alle neun internen Einträge passen. | Geschlossen. Kein widersprüchlicher Dateipin in der konkreten v2-Fassung. |

Die Ausgabe der Erläuterungen bleibt an `answered` gebunden (`prototype.js:517–542`). Unberührte und übersprungene Angaben erhalten weiterhin keine politische Interpretation. Die gewählte Originalkategorie steht unmittelbar beim Text. Acht Themenrubriken bleiben als Ordnung konkreter Angaben mit ausdrücklichem Ausschluss einer bestätigten Dimension oder eines gemeinsamen Scores erhalten (`:556–577`). Diese Runde stellt kein Neutralitätszertifikat aus.

## Generator und Pinbildung

Der statisch gelesene und mit Python-AST untersuchte Generator löst `Path(__file__).resolve().parents[2]` tatsächlich zum angegebenen Worktree auf (`prepare.py:9`). Er projiziert weiterhin nur die aufgeführten öffentlichen Instrumentfelder und zulässigen Originalkategorien; neu ist das deklarierte Samplingfeld der Studie (`:34–39`). Keine neue Rohdaten-/Antwortquelle ist im Generatorcode eingeführt.

Der Formatierungsaufruf nennt genau sechs eigene öffentliche Artefakte: `catalogue.js`, `foundation.css`, `index.html`, `prototype.js`, `prototype.css`, `source-binding.json` (`:87–92`). Es gibt keinen pauschalen Formatierungsaufruf über das Repository. `check=True` verlangt einen erfolgreichen Formatierungslauf, bevor der Generator das interne Manifest schreibt. Die nachfolgende Dateiinventur enthält aktuell neun Dateien, einschließlich des Generators und der beiden Schriftartefakte; `manifest.json` selbst ist ausgeschlossen (`:93–98`). Für jeden Eintrag liest der Code die tatsächlichen Bytes zur SHA-256-Bildung und nutzt die tatsächliche Dateigröße.

Die aktuelle Inventur wurde unabhängig mit den neun internen Manifesteinträgen verglichen: Dateimenge, SHA-256 und Bytezahl passen vollständig. Dies prüft den Code und das vorliegende Produkt seiner Ausführung. Ob eine zukünftige Generatorausführung erfolgreich durchläuft, wurde nicht getestet. Insbesondere wurde kein Prettier-/pnpm-Lauf durch diesen Reviewer ausgelöst.

## Sampling, Quellenversion und begrenzte Konsistenzprüfung

`catalogue.js:75–76` enthält den deklarierenden ESS8-Samplingtext einschließlich des Satzes „there are no survey participants in Munich“. Die neue deutsche Zeile ordnet die fehlende Erfassung ausdrücklich der ESS8-Stichprobendokumentation zu (`prototype.js:359–364`). Sie behauptet keine aktuelle Bevölkerungsnorm oder vollständige Abdeckung. Der Hinweis zur Gewichtung behauptet keine Wiederherstellung der nicht erhobenen Antworten.

Der Originaltext aller fünf Studien wird als Stichprobendokumentation in einem eigenen Details-Element über `node('p', text)` wiedergegeben (`:366–369`). Die Probe bestätigt die genaue Wiedergabe der lokalen Samplingstrings und dass die eigene Münchner Grenzbenennung nur bei ESS8 erscheint. Die deklarierte Zielpopulation bleibt von erreichter Abdeckung getrennt (`:353–358`). Historische Grenze, offene Modusäquivalenz, Originalformen, Erhebungszeiten und der ESS10-Versionswiderspruch werden weiter getrennt dargestellt. Es gibt keine neue Aussage über heutige Repräsentativität, aktuelle Vergleichsnormen oder bestandene CI.

Der neue Ursprungshash `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` stimmt zwischen Katalog und `source-binding.json` überein. Die Originalquelle liegt außerhalb der erlaubten Artefakte. Dass die zugrunde liegende Quellenkorrektur ausschließlich CAWI betraf, ist daher keine durch diesen Lauf unabhängig bewiesene Provenienztatsache. Es wurde keine erneute Vollquellenrecherche begonnen.

Als gezielte Revisionskontrolle wurden alle 43 `wordingDe`-Strings und sämtliche 315 Kategorien mit den in der Erstprüfung gelesenen lokalen v1-Texten verglichen: Beschriftungen, gedruckte Codes, semantische Rollen, Antworttypen und Katalogreihenfolge stimmen. Die drei betroffenen Gerechtigkeitseinleitungen, der feste Budgetkontext und das vollständige Elternzeitszenario wurden zusätzlich geprüft. Das bestätigt diese Originaltext-/Kategorieninvarianten; es ist kein vollständiger Bytevergleich der im Remote-Commit archivierten Quellen oder aller Herkunftsfelder. Quellen-/Datenidentität bleibt eine getrennte Frage.

Die CSS-Ergänzung betrifft `.page-title`, `.section-title`, `.result-item h3` und `legend` mit `overflow-wrap: anywhere` und `hyphens: auto` (`prototype.css:11–16`). Die angezeigten Originalfragen werden dadurch nicht umgeschrieben. Eine tatsächlich passende Darstellung bei schmaler Inhaltsbreite wurde ohne Browser nicht beobachtet.

Die im Erstbericht benannten offenen Integrations- und Handbuchfragen behalten ihren begrenzten Status. Das unveränderte Handbuch erlaubt damit keine automatische Test-/Ergebnis-Designfreigabe. Der deutliche lokale Entwurfsstatus und die Pflichttexte sind weiter vorhanden. Es wurde kein neuer Forschungsblock aus einer Stil- oder Integrationsfrage gemacht.

## Tatsächliche Prüfungen und ein Fehler in der eigenen Probe

Die zwölf vorhandenen Code-/DOM-Prüfgruppen wurden unverändert wiederverwendet. Nur der Leser für das durch Prettier formatierte JavaScript-Literal und der neue Evidenzdateiname wurden angepasst. Das Objekt wird in einem isolierten VM-Kontext ohne bereitgestellte APIs gelesen und anschließend als JSON-Wert in den Prüfkontext übernommen. Kein Generator wird dabei ausgeführt.

Vier gezielte Prüfgruppen ergänzen die Korrekturtexte, Originaltext-/Kategorieninvarianten, Samplingwiedergabe und CSS-Regel. Sie sind Revisionskontrollen dieser Änderung, kein neuer Gesamtaudit.

| Prüfung | Tatsächlicher Befund |
| --- | --- |
| Manifest-Pin | Selbst berechnet; stimmt mit User-Pin vor/nach. |
| Äußere Pins | 11/11 vor/nach gültig und unverändert. |
| Interne Hashes/Bytezahlen | 9/9 vor/nach gültig und unverändert. |
| Generator | AST-Prüfung der sechs Formatierungsziele, Reihenfolge vor Hashbildung, Worktreeauflösung und aktueller Neun-Dateien-Inventur bestanden; nicht ausgeführt. |
| Zwölf vorhandene Gruppen | Bestanden: 43 Items, acht Rubriken, 315 Kategorien, B1–B12, B25-Fortgang, nominale Sonderkategorien, drei Zustände, vollständiges Teilergebnis, Skalenanker, sichere Text-/Linkbildung, keine beobachteten Network-/Storage-API-Aufrufe und frische Sitzung. |
| Vier gezielte Gruppen | Bestanden: Korrekturtexte; 43 Originalfragen und 315 Kategorien; Samplingstrings und ESS8-Zuordnung; konkrete Umbruchregel. |
| Originalbericht und ursprüngliche Probe | Erwartete SHA-256 vor/nach unverändert. |

Beim ersten Lauf bestand die ursprüngliche Zwölf-Gruppen-Suite. Die erste neue Gruppe scheiterte danach an einer von mir falsch konstruierten Erwartungsformulierung: „dass eine Gesellschaft ist gerecht“. Der tatsächliche UI-Satz „dass eine Gesellschaft gerecht ist“ war korrekt. Der fehlerhafte Prüfcode wurde als `round1-probe-attempt1.cjs` erhalten und der beobachtete Fehler mit Exitcode 1 in `round1-probe-attempt1-error.json` festgehalten. Nur die Nebensatzbildung der Erwartung wurde korrigiert; keine Manifestdatei oder UI-Datei wurde verändert.

Der anschließende Lauf `node outputs/loop/policy-ui-001-review/round1-probe.cjs` endete mit Exitcode 0: **16 Prüfgruppen bestanden, 0 Fehler**. Darin enthalten sind dieselben zwölf bisherigen Gruppen und vier gezielte Ergänzungen. Die Proben nutzen synthetische lokale Auswahlzustände, keine Antworten realer Befragter. „315“ zählt öffentliche Antwortkategorien und ist keine Datenfrequenz.

Es gab keine Browserbeobachtung, native Radio-/Tastaturprüfung, tatsächliche Layout-/Fokus-/Scrollprüfung, axe-/Screenreaderprüfung, Browser-CSP-/Network-/Storage-Beobachtung, CI-/Buildprüfung, Quellenabnahme oder empirische Untersuchung. Die erfolgreichen VM-/DOM-Shape-Prüfungen ersetzen nichts davon. Der Root führt seine Browserverifikation separat durch.

## Pins und Evidenz

Manifest: `reports/loop/packages/POLICY-UI-001/v2/manifest.json`, SHA-256 `b82dfe72af5e0b9182d70276138f432b2dea0ed97fa40c3acc4863dd81b2a6e8`. Nachprüfung vor Berichtserstellung: `2026-10-03T14:20:33.138041+00:00`.

| Manifestartefakt | Tatsächlicher SHA-256 vor/nach |
| --- | --- |
| `prototypes/policy-v2/assets/libre-baskerville-latin-wght-normal.woff2` | `22219fb90e3b9bd28debd1825fe8d9a0154a0e31f8b3fa601ac1a0a5aa5e6d1b` |
| `prototypes/policy-v2/assets/libre-baskerville-license.txt` | `8490e863633e537100d6d18755d994ea30b0b44741876a17809d28becf45ce11` |
| `prototypes/policy-v2/catalogue.js` | `05f9d24c2c0ac6ca4d0532a8a22bb71070b5eca0d4317b442fa705f215a2a0cf` |
| `prototypes/policy-v2/foundation.css` | `97853bc6912eaa3a722b0ea3707f61aca418a77a7f69ec602aaca9a4a60dceca` |
| `prototypes/policy-v2/index.html` | `f1240f743ed8346b304f6f0d5f56f0999c7919ecca10e237239d514b92e07881` |
| `prototypes/policy-v2/manifest.json` | `a6ed88a85d4ab4682862ae5d3abca8add173decb5b22db7e8ce61939c7963366` |
| `prototypes/policy-v2/prepare.py` | `7bed0f5fe468c7daa2e8962a3174fbcd674012a035aa54dc01f9af0036795d73` |
| `prototypes/policy-v2/prototype.css` | `0fca11378c7f5ebceb7129e65e780d849b465daf8a2a46924d9582cc9f4a9cd0` |
| `prototypes/policy-v2/prototype.js` | `7fc49855b514cf358b70274868536b4c6dc67424f8d77ea13af11dde26a59def` |
| `prototypes/policy-v2/source-binding.json` | `3bef7c33b813127cdb361d1bc9d37ef7b2b9e70ba82435bc9840ad4afac42eea` |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |

Neue eigene Evidenz unter `outputs/loop/policy-ui-001-review/`:

| Datei | SHA-256 |
| --- | --- |
| `round1-probe.cjs` | `53a3569323e1243b1cd66ec74d643d4f9961f733600b73f96a386160f8b424d1` |
| `round1-probe-result.json` | `02d8dae4e775f633e31c7984c7ca389be540d1baf32fb925663f68f04efeb628` |
| `round1-generator-check.json` | `dfb9445fe436c5617469356a0be41074d7431ffa7f2fec35405125ed215a6a75` |
| `round1-pins-before.json` | `f5691143ba2b03e8b73cc20da505825c12aa5929358afed78801d81568f393d9` |
| `round1-pins-after.json` | `f30efa69fa072bacd9cb4f6f575a872fe02aff4a4dd648f803e617b8d170ad47` |
| `round1-probe-attempt1.cjs` | `bfb52553a4a905cc880b3b5ea866515e633a3141e8a60a4744856ea87e59a140` |
| `round1-probe-attempt1-error.json` | `2e40252bb166eb01ac40c524b1c74b69de519a3da42800377631d95862cf0b00` |

Keine zusätzliche Korrektur innerhalb des gezielten lokalen Prüfauftrags erforderlich. Der Erstbericht und die gepinnten Artefakte bleiben unverändert.
