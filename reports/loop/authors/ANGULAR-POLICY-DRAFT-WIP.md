# Angular-v2-Fragen- und Ergebnisvorbereitung

Stand: 2026-10-03. Eigenständiger Codex-Autorauftrag im Worktree `life93-night-20261003`, Branch laut Koordinator `research/life-93-night-20261003`. WIP, unroutiert, keine Produkt-, Gestaltungs-, Daten- oder Veröffentlichungsfreigabe.

## Autorauftrag und tatsächlicher Zugriff

Root beauftragte eine konkrete Angular-OnPush-Standalone-Komponente mit Template, SCSS und öffentlichem 43-Fragen-Metadatenadapter. Schreibbereich: ausschließlich der neue Ordner `web/src/app/policy-draft/` und dieser Bericht. Root bleibt Koordinator für gemeinsame Dateien, Forschung, Integration, Browserprüfung und Git. Keine Routes, Navigation, Startseite, App-Hülle oder Produktionskonfiguration geändert. Keine Git-, Deployment-, Claude-, Installations- oder Browserdienstaktion ausgeführt.

Persönlich gelesen wurden:

- `AGENTS.md`, `docs/project.md`, `docs/handbuch.md` vollständig; `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md`, `docs/entscheidungen.md` vollständig in Abschnitten. Historische Regeln wurden nicht als neue Daten- oder Modellfreigabe benutzt.
- `web/src/app/research/policy-profile.ts` vollständig, der Anfang der vorhandenen `policy-profile.spec.ts`, `app.spec.ts` bis einschließlich der Navigationstests.
- `web/src/app/app.ts`, `app.html`, `app.scss`, `web/src/styles.scss`, die vorhandene Methodikseite und Startseite mit ihren Komponenten, Templates und SCSS. Wortmarke, Bundesflagge, Startseitenlink, Statusleiste und Fußzeile bleiben in der vorhandenen App-Hülle. Die neue Komponente setzt diese Hülle voraus und wiederholt sie nicht.
- `prototypes/policy-v2/prototype.js` vollständig; öffentliche Katalogmetadaten, Originalwortlaute, Einleitungen, Antwortlisten, Gruppenfolge und Quellen aus `prototypes/policy-v2/catalogue.js`. Die große Katalogdatei wurde in Abschnitten und als gezielte öffentliche Itemprojektion gelesen; anschließend programmatisch vollständig übernommen und abgeglichen.
- Nach ausdrücklicher Pfadfreigabe durch Root ausschließlich `data/politikprofil-v2.fragen.entwurf.json` als öffentliche Instrument-/API-Metadatenquelle. Die Datei ist kein Antwortdatensatz. Keine weiteren Datenpfade verwendet.
- `package.json`, `web/package.json`, `web/tsconfig.app.json`, `web/tsconfig.spec.json` und zur Diagnose `scripts/check-handbuch.mjs`. Keine gemeinsamen Konfigurationen geändert.
- `.agents/skills/unslop/SKILL.md` aus dem Hauptcheckout und der kurze Handbuch-/Gestaltungsabschnitt in der persönlichen `MEMORY.md`. Aktuelle Dateien im Worktree waren maßgeblich.

Keine Dateien aus `data/raw/` oder `data/local/`, keine CSV/Header/Antwortzeilen, historischen Referenzstatistiken, anderen Erstberichte, Reviewerurteile oder Koordinationszustände persönlich gelesen. Der Prüflauf `pnpm check` verwendete die vorhandenen allgemeinen Formatierungsregeln und brach bei fremden Formatbefunden ab; es gab keine Ausgabe solcher Dateninhalte.

Der wörtliche Phase-6-Statushinweis und der Zusatz bis zur Verständnisprüfung wurden von Root aus dem lokal erhaltenen Issuewortlaut geliefert. Der Autor hat die Issue-Datei nicht selbst geöffnet und keinen aktuellen Linear-/Webzugriff durchgeführt. Nur dieser begrenzte Wortlaut wurde übernommen; der historische Phasenauftrag wurde nicht reaktiviert.

## Quellenpins

| Datei | SHA-256 |
| --- | --- |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `prototypes/policy-v2/catalogue.js` | `05f9d24c2c0ac6ca4d0532a8a22bb71070b5eca0d4317b442fa705f215a2a0cf` |
| `prototypes/policy-v2/prototype.js` | `7fc49855b514cf358b70274868536b4c6dc67424f8d77ea13af11dde26a59def` |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |
| `docs/project.md` | `50fd74dc5612293f22591e679856dbb09745ef2ff9a217ff5583b219cf224328` |
| `web/src/app/research/policy-profile.ts` | `28906eb1533bb953b43bed75a4995c907b71398f1ffcd63271c82cfdace05998` |

Die genannten Ausgangsdateien wurden nicht verändert. `public-catalogue.ts` ist eine eingefrorene lokale Projektion des öffentlichen Vorlagenkatalogs mit zusätzlich ausdrücklich gebundenen API-/Exportcodes und Feld-/Dateimetadaten aus dem gepinnten öffentlichen JSON. Sie enthält alle 43 Originalfragen und 315 Originaloptionen, ihre ursprünglichen Texte und die getrennten Druckcodes. Missing- und Nicht-gestellt-Metadaten bleiben separat. Öffentlich deklarierte Stichprobendokumentation ist Quellenkontext, keine neu gerechnete Referenzverteilung.

`verify-public-catalogue.mjs` liest nur diese öffentliche Metadatendatei und den Adapter. Der Abgleich prüft Hash, Vollständigkeit, Frageidentität, Wortlaut, Einleitungen, Stamm, Situation, Originalanweisung, Gruppenzuordnung, Antwortformat, alle Kategorien einschließlich expliziter Druck-/Exportcodezuordnung, Missing-/Nicht-gestellt-Codes und Metadatenbindung. Er schreibt keine Dateien und öffnet keine Antwortdaten. Node 24 meldet für `stripTypeScriptTypes` eine ExperimentalWarning; der Prüflauf bestand.

## Konkrete Vorbereitung

`PolicyDraft` nutzt Signals, `input()`, `OnPush` und `PolicyProfileSession`. Es gibt kein Routing, kein Antwort-Output, keine Speicherung, keine Netzwerkschnittstelle und keine Antwortcodierung in URLs. Antworten und explizite Überspringgründe liegen nur in der Komponenteninstanz. Neuladen oder Schließen verwirft die Sitzung.

Native Radiofelder stehen in einem Fieldset mit Legend und gebundenem Originalkontext. Vor-/Zurückgehen beantwortet und überspringt keine Frage. Übersicht, ausdrückliches Überspringen, Zurücksetzen, Teilresultat und Bearbeitung einzelner Originalfragen sind vorhanden. Nach Ansichtswechseln oder Fragenwechseln folgt der Fokus der gerenderten Überschrift mit `preventScroll`. Eine Aussage zum vollständig geprüften Browser-/Hilfsmittelverhalten wird daraus nicht abgeleitet.

B1–B12 bleiben als zusammenhängender Block in ihrer Originalfolge. B12 `keydec` erscheint erst im Ergebnis primär unter europäischer Integration. Die vollständige Demokratieeinleitung bleibt sichtbar. Die Auslassung von B13–B24 und die neue Durchführung sind benannt. B25 benennt ursprüngliche Weiterleitung B26/B28, Auslassung B26–B29 und die neue unbedingte Folge. Die Elternzeitfrage behält das vollständige Doppelverdiener-/Neugeborenenszenario. Die historische Bedeutung von „heute“ in der Strafpraxisfrage bleibt begrenzt.

Das Ergebnis enthält alle 43 getrennten Angaben unter acht Rubriken. Unberührt, beantwortet und bewusst übersprungen bleiben unterscheidbar. Überspringgründe werden keinem ESS-Missing-Code gleichgesetzt. Die nominalen EU-Kategorien für leeren Stimmzettel, ungültige Wahl, Nichtwahl und fehlende Stimmberechtigung bleiben Originalkategorien. Es gibt keine gemeinsamen Dimensionen, Summenwerte, Ideologiezuordnung, Parteimatches, Konfidenzintervalle oder aktuelle Norm.

`item-meanings.ts` übernimmt die begrenzten Erläuterungen der lokalen Vorlage. Zwei Erläuterungen und ein Titel wurden für die Handbuchsprache enger formuliert: `votedir` nennt den ursprünglichen Volksabstimmungsgegenstand ohne zusätzliches generisches Personenwort; `gvctzpv` heißt „Schutz vor Armut als Demokratieprinzip“ und verweist ausdrücklich auf die Originalaussage. Die vollständig sichtbaren Originalfragen und ihren Bezugsrahmen wurden nicht umformuliert. Diese Redaktion ist keine wissenschaftliche Textfreigabe.

`PolicySourceDetails` zeigt Urheber/Archiv, nationale Originalinstrumente und PDF-Seiten, Daten-/Dokumentations-DOI, Ausgabe, tatsächliche historische Zeiten, Modi, 15+-Zielpopulation und deren Grenzen. ESS8 München, fehlende Wiederherstellung durch Gewichtung und ESS10-Self-completion gegenüber der Interviewausgabe bleiben sichtbar. Der überlieferte ESS10-Zitationswiderspruch 3.1/3.2 wird erhalten. Dokumentationslizenz CC BY-SA 4.0 und Datenlizenz CC BY-NC-SA 4.0 bleiben getrennt.

Alle Layout-/Farb-/Schriftwerte nutzen vorhandene Klassen und Tokens. Es gibt keine Gemälde und keine neuen Farben. Die Komponentenstile sind 1983 bzw. 540 Bytes groß und bleiben jeweils unter vier kB. Eine konkrete Browserbeobachtung bei 320 Pixeln oder 200 Prozent Zoom liegt hier noch nicht vor.

## Vorbereitete historische Eingabe

`historicalReferences` ist standardmäßig `null`. Keine tatsächlichen historischen Vergleichszahlen sind eingebunden. Eine spätere Integration muss zuerst authentische, gesondert freigegebene zusammengefasste Referenzen bereitstellen.

Die technische Eingabebindung prüft Kataloghash, Item, Studie, Variable, Originalfrage, Ausgabe, DOI, Instrumentquellen, Feld-/Dateimetadaten, Gewicht `pspwght`, Nenner gültiger Einzelantworten und vollständige Originalexportcodes. Druckcodes werden niemals als Listenindices oder automatisch als Exportcodes gedeutet. Beispiel: `euftf` Druckcode `00` ist ausdrücklich an Exportcode `0` gebunden. Auch Exportcode `9` bleibt dort eine reguläre Kategorie und wird nicht mit einem Missing-Code verwechselt.

Nur mathematisch vollständige Kategorieanteile mit endlichen Werten im Intervall 0–1 und positiver ganzzahliger gültiger Fallzahl sind technisch darstellbar. Die Summenprüfung nutzt eine rein technische Rundungstoleranz von `1e-6`; sie ist kein empirischer Güteschwellenwert. Unpassende Quellen, zusätzliche Score-/Freigabefelder, doppelte Kategorien oder Missing-Codes werden verworfen. Ein technisches `bound` bestätigt nur Metadatenpassung. Es erzeugt keine methodische oder Veröffentlichungsfreigabe und nennt die Referenz nicht „freigegeben“.

Die Tests verwenden ausdrücklich synthetische Anteile allein für diesen technischen Adapter. Diese Werte liegen nur in `.spec.ts` und behaupten weder eine tatsächliche historische Verteilung noch eine Freigabe. Die normale Komponente erhält keine solchen Werte.

## Tatsächlich ausgeführte Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| `pnpm --filter politikprofil typecheck` | BESTANDEN nach Korrektur der Testdateien. Angular- und strenge TypeScript-Prüfung der Komponenten bestanden. |
| `pnpm --filter politikprofil test --watch=false --include 'src/app/policy-draft/*.spec.ts'` | BESTANDEN: drei Dateien, 23 Tests. Letzter Lauf nach der Textkorrektur begann am 2026-10-03 um 14:40:00 UTC und dauerte 4,51 Sekunden. |
| `node web/src/app/policy-draft/verify-public-catalogue.mjs` | BESTANDEN: 43 Originalfragen und alle 315 expliziten Druck-/Exportcodebindungen gegen den gepinnten öffentlichen Katalog. |
| `pnpm exec prettier --check web/src/app/policy-draft` | BESTANDEN. Nur eigene Dateien wurden formatiert. |
| `pnpm check:handbuch` | NICHT_BESTANDEN: der Originaltextadapter enthält das historische Quellenwort „Bürger“. Root behandelt eine präzise Originalquellenausnahme separat. |
| `pnpm check` | NICHT_BESTANDEN: allgemeiner Formatcheck meldete `docs/verstaendnistest-v2.entwurf.md` und `reports/loop/policy-v2-export-decisions.json`, außerhalb des Autorbereichs. Keine dieser Dateien geändert. Nachfolgende Checkstufen wurden in diesem Lauf nicht erreicht. |
| Browser/Desktop/Smartphone/320 px/Zoom/Tastatur/reduzierte Bewegung/axe | NICHT_GEPRÜFT durch diesen Autor. Kein Browserdienst gestartet. Root prüft die spätere Einbettung. |
| Empirische, methodische, menschliche Gestaltungs-/Verständnis-/Veröffentlichungsfreigaben | NICHT_GEPRÜFT durch diesen Autor, keine Abnahme erklärt. |

Die 23 Tests prüfen Auswahl und Erhaltung beim Zurückgehen, unabhängige Bearbeitung, unberührt gegenüber bewusst übersprungen, Teilresultat und Rückkehr zur Originalfrage, native Radio-/Fieldsetbindung, Fokusführung, 43 vollständige Ergebnisangaben, leere Referenzen, URL-/Storage-/Fetchfreiheit des getesteten lokalen Durchgangs, Druck-/Exportcodebindung, vollständiges Elternzeitszenario, B1–B12/B25 und Ablehnung fremder Quellen, Missing-Codes, doppelter Kategorien oder zusätzlicher Scorefelder. Storage-/Fetch-Spies im jsdom-Lauf sind begrenzte technische Checks, keine vollständige Browsernetzwerk-/Speicherabnahme.

Frühere Fehler bleiben dokumentiert: Der erste Testbuild scheiterte an fehlenden Node-Typen in einem Paritätstest und einer absichtlich ungültigen TypeScript-Typumwandlung. Ein Versuch mit lokaler Node-Typreferenz scheiterte ebenfalls, weil diese Typdefinition nicht installiert ist. Keine Installation oder globale Konfigurationsänderung vorgenommen. Der Quellenparitätstest wurde deshalb als gesondertes Node-Skript ausgeführt; die Angular-Specs benötigen keine Node-APIs. Ein erster Aufruf des Paritätsskripts hatte einen um eine Ebene zu hohen Repositorypfad und scheiterte mit ENOENT, ohne Daten zu öffnen. Nach Pfadkorrektur bestand der Lauf. Zwei sichtbare Semikolons und generisches Personenwort in eigenen Erläuterungen wurden korrigiert. Originaltexte wurden weder sprachlich geglättet noch mit Escapes vor der Prüfung verborgen.

## Offene Integration und Abnahmen

Root muss die präzise Handbuchchecker-Ausnahme, den globalen Check, die Einbettung mit vorhandener Hülle und den Browserablauf prüfen. Die Entwicklungskomponente bleibt unroutiert. Die Gestaltung von Fragen und Ergebnissen, Verständnisprüfungen mit Menschen, die menschlichen Design-/Releasefreigaben und die abschließende Kontrolle bleiben offen. Neue Referenzeingaben benötigen einen gesonderten fachlichen und Veröffentlichungsabgleich. Die Vorbereitung ist technisch konkret prüfbar und kein freigegebener Test.
