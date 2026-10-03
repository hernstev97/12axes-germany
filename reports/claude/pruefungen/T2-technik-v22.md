# T2: technisches Fortsetzungspaket v2.2

Stand: 4. Oktober 2026. Begrenztes KI-Review durch Codex (OpenAI).

Gesamturteil: **NICHT_BESTANDEN**. Drei mittlere Findings begrenzen die beanspruchte Browserabdeckung und die Vollständigkeit der Intervallanzeige. Zwei weitere Findings betreffen den Fehlerstatus der SAV-Gegenprobe und einen ausgelassenen Erklärungssatz. Kein erhebliches Finding. Die neue Dekodierung ist unabhängig vom eigenen SAV-Leser; die veröffentlichten Gegenprobenzahlen sind untereinander konsistent. Die technischen Checks bestehen.

## Gegenstand und Bindung

Umfangsmanifest: `reports/claude/auftraege/T2-technik-nachpruefung.md`, vor Beginn geprüft mit SHA-256 `9918287bff8439a917ac7d38a93c0b25ed4f56c8e9d1bf1a3179a188d988984a`.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`. Branch: `research/life-93-claude-20261003`. HEAD bei Beginn: `d44422720b2316da02aa01f54799d653dbae7de2`.

Geprüfter Stand:

- Basis: `b5a53ff79b11da53b59d007f96ad269d04496d0b`.
- SAV-Paket: `5765b369af007c0c29474c116e466cab84e10926`.
- Browserpaket: `122f69a1d11fd43fa4375968c174f366bdc82130`.
- Anzeige/Textentwurf: `b4641a9bd5227de41688eac4b4db94f152b1e8cc`.

Die zwölf Umfangsdateien sind bei Prüfungsbeginn gegenüber b4641a9 unverändert. Der zusätzliche Commit d3276f3 im Bereich b5a53ff..b4641a9 betrifft Rechercheaufträge und wird nicht bewertet. Bereits vorhandene unversionierte R8-/R9-Dateien sowie die während der Prüfung hinzugekommene R10-Datei wurden nicht gelesen oder verändert. Der Schemamodus PR_REVIEW bezeichnet hier die angeforderte Paketprüfung; kein PR wurde erstellt oder bearbeitet.

## Antworten auf die Prüffragen

1. Die ReadStat-Dekodierung ruft pyreadstat.read_sav auf. sav.py wird ausschließlich für den getrennten Feldvergleich importiert. Die anschließende Designrechnung verwendet die ReadStat-Zeilen, kontrolle.read_de/classify und Codex' categorical_reference. Die Tabelle gemeinsamer Bestandteile stimmt: dieselben Datendateien, öffentliche Verträge, Python-csv-Modul und Verfahren; Claude verfasste beide Kontrollskripte. Intervallgrenzen werden ausdrücklich nicht unabhängig berechnet. Die [pyreadstat-Primärdokumentation](https://github.com/Roche/pyreadstat) bestätigt die Anbindung an ReadStat. Das öffentliche JSON trägt nur Metadaten, Zählungen und Abweichungen, keine Fallkennungen oder Einzelgewichte. Der aktuelle explizite Ausgabepfad ist eine reguläre Datei; private Läufe werden nur gelesen. F04 begrenzt den automatischen Fehlerstatus. Die tatsächliche Rohdatenrechnung wurde nicht wiederholt.

2. check-public-zoom.mjs verwendet echten Tab-Zoom, kontrolliert den Faktor mit getZoom und DPR, verlangt die halbe CSS-Breite und schließt CSS-Zoom aus. Es prüft Überlauf beim Durchscrollen, axe, Sprunglink und die durchlaufenen Tab-Stopps. check-research-engines.mjs durchläuft alle aus der Oberfläche ermittelten Fragen, ändert eine Antwort, setzt eine zurück, überspringt eine, geht zurück, öffnet Ergebnisse/Gruppen/Übersicht und springt zur letzten Frage. Netzwerk und gesendete WebSocket-Frames werden nach dem Laden beobachtet. Fokus- und Speicherabdeckung sind jedoch enger als dokumentiert (F01/F02). Die dokumentierten Zahlen 62/59/406 sind protokollierte Werte, keine exakten Soll-Assertions des Skripts. WebKit/Safari, echte Geräte, menschliche Screenreaderprüfung und Hochkontrast sind ehrlich als ungeprüft gekennzeichnet. Die genannten Versions- und Bibliotheksangaben sowie tatsächlichen Browserläufe wurden hier nicht unabhängig verifiziert.

3. Die neue Erklärung steht genau einmal im Ergebniszweig; die beiden lokalen Erklärungen sind entfernt. Der Komponententest bestätigt genau eine Erklärung mit Einzel- und Gruppenbereichen. Einzelreferenzen ohne jeden Bereich bleiben als fehlend gekennzeichnet; no_valid_answers bleibt ohne Zahlen. Gruppen ohne Bereiche und einzelne ausfallende Kategorienbereiche haben dagegen keine ausdrückliche Missing-Markierung (F03). Der Plan verlangt außerdem den Ausschluss von Messfehlern einzelner Antworten; dieser Teil fehlt im gemeinsamen Text (F05). Das ist keine Änderung des Messmodells, sondern eine Anzeige-/Textprüfung.

4. Fundstellen und Zitate im Vorschlagsentwurf stimmen. Pflichttext und die beiden folgenden Absätze passen zum lokal erhaltenen LIFE-93-Wortlaut und zum aktuellen Template. Meta-Beschreibung und Handbuchbegriffe sind korrekt zitiert; die vorgeschlagenen Zeichenlängen betragen tatsächlich 141 und 151. Die aktuelle [ESS-Samplingseite](https://www.europeansocialsurvey.org/methodology/sampling) bestätigt beide englischen Zitatfragmente, die Zufallsauswahl und den Ausschluss von Quoten und Ersatz. Der ursprüngliche URL leitet dorthin weiter. Der öffentliche Katalog enthält den München-Ausfall und die Grenze ungeprüfter erreichter Abdeckung. Bereichsnamen und Inhaltsbeschreibungen sind in den genannten Codefundstellen vorhanden. V2-F04/F11/F13/F15 und T1 Abschnitt 4 wurden nur zum Nachweis der ausdrücklich angegebenen Fundstellen ausschnittsweise gelesen; daraus wurde kein fremdes Gesamturteil übernommen. Die vorgeschlagenen Änderungen werden als offen ausgewiesen; Abschnitt 6 nennt die bereits umgesetzten Ausnahmen gesondert.

## Checks

| Check | Umfang | Urteil | erforderlich |
| --- | --- | --- | --- |
| T2-C01 | Manifest, Branch, HEAD und Bindung des Prüfgegenstands | BESTANDEN | ja |
| T2-C02 | Unabhängigkeit und Aussagegrenzen der zweiten SAV-Dekodierung | BESTANDEN | ja |
| T2-C03 | Ausgabe und private Schreibpfade der SAV-Gegenprobe | BESTANDEN | ja |
| T2-C04 | Browsercode gegen dokumentierte technische Abdeckung | NICHT_BESTANDEN | ja |
| T2-C05 | Planmäßige gemeinsame Intervallerklärung, fehlende Bereiche und Tests | NICHT_BESTANDEN | ja |
| T2-C06 | Sachliche Fundstellen und Zitate im Vorschlagstext | BESTANDEN | ja |
| T2-C07 | pnpm check | BESTANDEN | ja |
| T2-C08 | Synthetische Tests Rechenweg v2.2 | BESTANDEN | ja |
| T2-C09 | Eigene Ausführung von Browser-/Datenskripten und Sichtung privater Browserbelege | NICHT_GEPRÜFT | nein |
| T2-C10 | Wissenschaftliche, menschliche, Design- oder Veröffentlichungsabnahme | IN_DIESER_PHASE_NICHT_ERFORDERLICH | nein |

Beide `pnpm check`-Läufe endeten mit Exit 0, einschließlich des Laufs nach dem ersten Berichtsschreiben: Formatierung, Handbuch, 20 synthetische Schemafälle, Typen, 113 Webtests in zehn Dateien und Produktionsbuild bestanden. Die 21 synthetischen Python-Tests endeten ebenfalls mit Exit 0. `git diff --check` für die zwölf Umfangsdateien ohne Befund. Grüne technische Checks schließen die folgenden inhaltlich geprüften Testlücken nicht.

## Findings

### T2-F01: mittel, blockiert den beanspruchten Prüfumfang

Aussage: docs/validation.md, Abschnitt 4. Oktober: „Fokus nach jedem Ansichtswechsel auf der Überschrift. … Alle bestanden.“ Das Skript kündigt außerdem einen sichtbaren Fokusrahmen des ersten Radios an.

Problem: check-research-engines.mjs speichert radioFocus, prüft aber weder Radio-Ziel noch focusVisible noch Rahmen. Beim Zurücksetzen wird nur der Radiozustand geprüft; beim Wechsel zur Fragenübersicht nur das Vorhandensein der Überschrift. Die Fokusassertion für diesen Ansichtswechsel fehlt. Die Dokumentation beschreibt damit mehr native Fokusprüfung, als dieses Skript durchführt.

Auswirkung: Ein fehlender Radio-Fokusrahmen oder ein ausgebliebener Fokuswechsel zur Übersicht kann trotz PASS unentdeckt bleiben. Kein tatsächlicher Fokusfehler der Oberfläche ist damit nachgewiesen.

Schweregrad: Betrifft die behauptete Schließung einer technischen Prüfgrenze und die Tastaturbedienung; keine neue wissenschaftliche Aussage und kein nachgewiesener Laufzeitdefekt.

Korrektur: Für das erste Radio Ziel, :focus-visible und sichtbaren Rahmen assertieren. Nach Reset und vor dem Klick aus der Übersicht den jeweiligen Fokus prüfen. Alternativ die dokumentierte Abdeckung auf die tatsächlich assertierten Wechsel begrenzen.

Nachprüfung: Autor führt das korrigierte Skript in Chromium und Firefox aus. Eine synthetisch entfernte Radio-Fokusregel und ein unterbundener Übersicht-Fokus müssen den Lauf scheitern lassen.

Fundstellen:

- scripts/check-research-engines.mjs:108-127 (Tab-Suche und ring nur protokolliert)
- scripts/check-research-engines.mjs:155-169 (Reset ohne Fokusassertion)
- scripts/check-research-engines.mjs:253-256 (Übersicht ohne headingFocused)
- docs/validation.md:78
- web/src/app/policy-draft/policy-draft.spec.ts:327-371 (jsdom-Tests ersetzen keine native Browserprüfung)

Sicherheit: BELEGT. Zustand: OFFEN. blocksScope: true.

### T2-F02: mittel, blockiert den beanspruchten Prüfumfang

Aussage: check-research-engines.mjs: „privacy (no request after load, nothing stored)“; docs/validation.md: „nichts in Storage, Cookies, IndexedDB, Cache oder Service Worker“.

Problem: Netzwerk und gesendete WebSocket-Frames werden fortlaufend beobachtet. Speicher, Cookies, Datenbanken, Cache und Service-Worker-Registrierungen werden dagegen erst am Ende einmal gezählt. Eine Antwort kann zuvor gespeichert und wieder entfernt worden sein, ohne dass dieser Check anschlägt. Außerdem gilt bei fehlender IndexedDB-/Cache-/Service-Worker-Prüfmöglichkeit der Wert 'n/a' ausdrücklich als Erfolg; ungeprüfte Speicherung wird nicht getrennt ausgewiesen.

Auswirkung: Der Browsercheck belegt den beobachteten Netzwerkdurchgang und den erfassten Endzustand, aber keine lückenlose Aussage, dass während des Durchgangs nichts gespeichert wurde. Dies ist eine Prüflücke, kein Nachweis eines Datenabflusses.

Schweregrad: Die Datenschutzbehauptung ist stärker als die erhobene Browserbeobachtung. Die vorhandenen setItem-/fetch-Spies in den Komponententests decken nur einen Teil der APIs ab.

Korrektur: Entweder Speicheroperationen ab vor dem Laden beobachten bzw. instrumentieren und relevante Zustände nach den Schritten prüfen, oder die Aussage ausdrücklich auf den leeren Endzustand beschränken. Nicht verfügbare APIs als NICHT_GEPRÜFT melden und in die dokumentierte Reichweite übernehmen.

Nachprüfung: Autor prüft eine synthetische setItem/removeItem-Folge sowie einen Lauf ohne indexedDB.databases. Die erste muss beim Anspruch 'nie gespeichert' auffallen; der zweite darf IndexedDB nicht als geprüft leer ausgeben.

Fundstellen:

- scripts/check-research-engines.mjs:59-66 (laufende Netzwerkbeobachtung)
- scripts/check-research-engines.mjs:260-278 (einmalige Endabfrage, 'n/a' akzeptiert)
- scripts/check-research-engines.mjs:9
- docs/validation.md:78

Sicherheit: BELEGT. Zustand: OFFEN. blocksScope: true.

### T2-F03: mittel, blockiert den beanspruchten Prüfumfang

Aussage: Auftrag Frage 3: „fehlende Bereiche weiter als fehlend markiert“; Analyseplan v2.2, 4.2: „Ein fehlender Bereich wird als fehlend angezeigt, nie als null.“

Problem: Der Hinweis .interval-missing bleibt für eine Einzelreferenz ohne jeden Bereich erhalten. In der Gruppenanzeige fehlt ein entsprechender Hinweis vollständig. Der bestehende synthetische ESS8-Gruppenfall elgcoal hat interval: null und ausschließlich null-Grenzen, zeigt aber nur Prozentwerte. Der angepasste Test prüft dort sechs Kategorien und keine lokale Erklärung, nicht die Kennzeichnung fehlender Bereiche. Zusätzlich verschwinden einzelne fehlende Kategorienbereiche innerhalb einer sonst mit Bereichen versehenen Einzelreferenz kommentarlos, weil der Hinweis nur bei !reference.hasIntervals erscheint.

Auswirkung: Lesende erkennen bei Gruppen und gemischten Kategorien nicht ausdrücklich, dass ein Bereich fehlt und keine Unsicherheit von null gemeint ist. Diese Lücke besteht bereits im Ausgangsstand; sie wird durch das Paket und seine Tests nicht geschlossen.

Schweregrad: Verbindliche Interpretationsregel für die vorhandene Anzeige, mit einem bereits vorhandenen synthetischen Gegenfall. Kein Fehler der berechneten Anteile oder Standardfehler nachgewiesen.

Korrektur: Fehlende Grenzen bei Gruppen und bei einzelnen Kategorien sichtbar als nicht verfügbar markieren, mit der Abgrenzung zu null Unsicherheit. Die gemeinsame Erklärung weiterhin nur einmal je Ergebnisansicht anzeigen. Tests für eine Gruppenreferenz ohne Bereiche und eine Referenz mit gemischten vorhandenen/fehlenden Grenzen ergänzen.

Nachprüfung: Komponententests müssen Missing-Markierungen für beide Fälle und genau eine gemeinsame Erklärung prüfen; anschließend autorisierte Browserprüfung der Ergebnisansicht.

Fundstellen:

- web/src/app/policy-draft/policy-draft.html:518-538 (Einzelkategorien und Hinweis nur bei vollständig fehlenden Bereichen)
- web/src/app/policy-draft/policy-draft.html:590-616 (Gruppenkategorien ohne Missing-Zweig)
- web/src/app/policy-draft/policy-draft.spec.ts:85-101 (Gruppenfixture ohne Bereiche)
- web/src/app/policy-draft/policy-draft.spec.ts:235-242 (fehlende Missing-Assertion)
- pipeline/v22/survey.py:169-180,196-201 (null-Grenzen sind vorgesehene Ausfälle)
- docs/analyseplan-v2.2.md:82

Sicherheit: BELEGT. Zustand: OFFEN. blocksScope: true.

### T2-F04: mittel, nicht blockierend für den begrenzten Umfang

Aussage: sav_gegenprobe.py prüft feldweise Dekodergleichheit, Eins-zu-eins-Zuordnung und Abweichungen der Anteile/Standardfehler.

Problem: Die Gegenprobe sammelt Differenzen und Duplikatzahlen, macht sie aber nicht zu einem negativen Prozessstatus. return 1 gibt es nur bei IDs, die ausschließlich in einer Datei vorkommen. Mehrfach vorhandene IDs können gleiche ID-Mengen ergeben; Designduplikate werden im Dictionary überschrieben. Unterschiedliche Decoderfelder und beliebig große berechnete Abweichungen führen weiterhin zu return 0.

Auswirkung: Bei späterer Wiederholung reicht Exit 0 nicht als Bestätigung. Die öffentlich gespeicherten Nullbefunde des vorliegenden Laufs werden dadurch nicht widerlegt.

Schweregrad: Reproduzierbarer Prüfmechanismus kann bei materiellen Gegenbefunden Erfolg signalisieren. Nicht blockierend für den konkret dokumentierten, manuell lesbaren Nullbefund.

Korrektur: Expliziten Gesamtstatus mit vorab begründeter numerischer Toleranz bilden. Zeilenzahl, je Feld Differenzen, Duplikate und Eins-zu-eins-Zuordnung prüfen; bei Verletzung aggregierten Bericht mit negativem Exitcode schreiben.

Nachprüfung: Synthetische Decoderabweichung, doppelte ID bei gleichen Mengen und Standardfehlerabweichung müssen negativ enden. Nur synthetische Daten nutzen.

Fundstellen:

- reports/claude/kontrollrechnung/sav_gegenprobe.py:79-100 (Vergleich ohne Fehlerstatus)
- reports/claude/kontrollrechnung/sav_gegenprobe.py:137-146 (Designduplikate gezählt, Dictionary überschrieben)
- reports/claude/kontrollrechnung/sav_gegenprobe.py:159-167 (nur Mengendifferenzen verhindern Erfolg)
- reports/claude/kontrollrechnung/sav_gegenprobe.py:176-186,203-207 (Maxima ohne Toleranzentscheidung)
- reports/claude/kontrollrechnung/sav-gegenprobe.json (dokumentierter Lauf enthält keine dieser Abweichungen)

Sicherheit: BELEGT. Zustand: OFFEN. blocksScope: false.

### T2-F05: niedrig, nicht blockierend für den begrenzten Umfang

Aussage: Die gemeinsame Erklärung soll Analyseplan v2.2, Abschnitt 4.3, vollständig umsetzen.

Problem: Der neue gemeinsame Text zählt Zeitabstand, Befragungsmodus, Nichtteilnahme und neuen Fragekontext auf. Der im Plan ausdrücklich genannte Ausschluss von „Messfehler[n] einzelner Antworten“ fehlt. „Keine Unsicherheit der eigenen Antwort“ grenzt persönliche Unsicherheit ab, nennt aber den Messfehler der historischen Befragungsantworten nicht.

Auswirkung: Die Erklärung nennt die Grenzen der Stichprobenbereiche nicht vollständig. Die grundlegende Abgrenzung zur eigenen Antwort bleibt richtig.

Schweregrad: Begrenzte Textauslassung, bereits im alten Einzelreferenztext vorhanden; kein neuer Rechenfehler. Die Prüfung der Anzeige scheitert unabhängig davon an T2-F03.

Korrektur: Den Ausschluss von Messfehlern einzelner Antworten in die einmalige Erklärung aufnehmen und im Texttest prüfen.

Nachprüfung: Textabgleich gegen alle Ausschlüsse aus Abschnitt 4.3; Komponententest der gemeinsamen Erklärung.

Fundstellen:

- docs/analyseplan-v2.2.md:88-90
- web/src/app/policy-draft/policy-draft.html:206-213
- web/src/app/policy-draft/policy-draft.spec.ts:224-226,250-252 (nur Ausschnitte der Erklärung assertiert)

Sicherheit: BELEGT. Zustand: OFFEN. blocksScope: false.

## Grenzen

- Codeprüfung mit öffentlichem SAV-Bericht und Browserdokumentation, keine unabhängige Wiederholung der tatsächlichen Rohdaten-/Browserläufe. Tatsächliche Browserzahlen, Screenshots, WebKit-Systembibliotheken und lokale ReadStat-Umgebung nicht verifiziert.
- Alle fünf Findings offen: drei mittlere blockieren die beanspruchte technische Abdeckung (F01-F03); F04 mittel und F05 niedrig blockieren den begrenzten dokumentierten Nullbefund nicht. Kein erhebliches Finding, kein belegter Rohdatenabfluss und kein widerlegter Standardfehler.
- Vorhandene fremde Urteile nur dort ausschnittsweise gelesen, wo docs/vorschlaege-texte-v1.entwurf.md sie ausdrücklich als Fundstelle benennt. Keine methodische Erstbewertung; keine fremden R8/R9/R10-Berichte gelesen.
- Unabhängigkeit der Dekodierung ist keine Unabhängigkeit der Verträge, Datengrundlage, Stichprobenformel oder Autorenfamilie; keine Neutralitäts- oder Validierungsaussage.
- Der gemeinsame hasIntervals-Guard prüft alle indexierten Eingaben, nicht nur sichtbare Referenzen. Er kann deshalb eine Erklärung auch ohne gerade sichtbaren Bereich anzeigen. Für korrekt gebundene v2.2-Eingaben ist keine Anzeige eines Bereichs ohne gemeinsame Erklärung im aktuellen Code nachgewiesen; keine zusätzlich behauptete Formatvalidierung.
- Browsercode erkennt viele Ablauffehler, aber nicht alle: Zurückgehen/Fernsprung prüfen nur Zahl angekreuzter Radios statt exaktem erhaltenen Code; Überspringen prüft nicht den gespeicherten Grund im Ergebnis; eigene Markierungen nur über Gesamtsumme; Referenz-/Intervallzahlen sind Messwerte und werden nur grob (>50, >Referenzen), nicht als 59/406 assertiert.
- Ein Gesamt-PASS des Engineskripts setzt keine erfolgreich gestartete Engine voraus. Die vorhandene Dokumentation weist WebKit dennoch korrekt aus; sie wird damit nicht als Safari-Prüfung übernommen.
- Normale SAV-Ausgabe ist aggregiert. Ungefangene Ausnahmen bei ungültigen Gewichtstexten können Python-Fehlermeldungen mit Literalen erzeugen; Fehlermeldungssicherheit für alle beschädigten Eingaben wird nicht als vollständig geprüft bestätigt. Öffentliche Zieldatei regulär; keine generelle Symlink-Sperre implementiert.
- Nur die beiden verlangten Ergebnisdateien redaktionell geschrieben. Der ausdrücklich erlaubte pnpm-Check erzeugt übliche ignorierte Build-/Testartefakte. Fremde unversionierte Dateien bleiben unangetastet.
- Die Memory-Abfrage diente nur der allgemeinen Trennung technischer Checks und wissenschaftlicher Abnahme; die Bewertung stützt sich auf den aktuell geprüften Auftrag und Code.

## Ausführungsnachweis

Modell laut Laufzeit: gpt-6.1-sol (OpenAI), T3 Code über Codex harness, high reasoning effort. Interne Revision nicht nachgewiesen; interne Anbietervorgaben unbekannt. Dies ist ein KI-Review, keine Fachbegutachtung.

Ursprünglicher Auftrag im Wortlaut:

```text
Act as the review sub-agent for this task.

Lies und befolge den Auftrag in /home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c/reports/claude/auftraege/T2-technik-nachpruefung.md vollständig. Arbeitsverzeichnis ist dieser Worktree. Der Auftrag ist das Umfangsmanifest; sein SHA-256 lautet 9918287bff8439a917ac7d38a93c0b25ed4f56c8e9d1bf1a3179a188d988984a. Prüfe ihn vor Beginn. Stand beim Auftrag: HEAD d44422720b2316da02aa01f54799d653dbae7de2 auf dem Branch research/life-93-claude-20261003; der Prüfgegenstand sind die im Auftrag genannten Commits. Schreibe nur die beiden im Auftrag genannten Ergebnisdateien. Keine Commits, Pushes, Tags oder Nachrichten. Nichts unter data/raw/, data/local/ oder outputs/ lesen. Am Ende fasse Gesamturteil und Findings in wenigen Sätzen zusammen.
```

Das geprüfte Manifest enthält den vollständig gelesenen Detailauftrag; seine Bytes sind unten gebunden. Keine Commits, Pushes, Tags, Delegationen oder Nachrichten an andere Personen/Agenten. Keine Ausführung von Browser- oder Datenskripten und keine Lektüre unter data/raw/, data/local/ oder outputs/.

### Gelesene Dateien mit SHA-256

Die Liste bindet vollständig oder ausschnittsweise gelesene sowie per Textsuche eingesehene Dateien. Ein Hash bindet die Datei, ohne zu behaupten, dass bei ergänzenden Fundstellen jede Zeile bewertet wurde. Automatische pnpm-Transitivabhängigkeiten werden durch den ausgeführten Check erfasst, nicht als vollständig manuell gelesene Dateien ausgegeben.

| Datei | SHA-256 |
| --- | --- |
| `reports/claude/auftraege/T2-technik-nachpruefung.md` | `9918287bff8439a917ac7d38a93c0b25ed4f56c8e9d1bf1a3179a188d988984a` |
| `.claude/skills/life93-review/SKILL.md` | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `.agents/skills/unslop/SKILL.md` | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `docs/project.md` | `9f827fdd40d5f9a4239043a5fb21ec84fa93805141566ac5b68e455a63d8bba6` |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |
| `docs/analyseplan-v2.2.md` | `13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8` |
| `docs/abdeckung-v2.2.md` | `32ddf3bb238b430037cdefbb032f0829fe16adc3dea1090afd061bd3fbf3b8da` |
| `docs/profilregeln-v1.md` | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` |
| `docs/pruefregeln.md` | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` |
| `reports/claude/kontrollrechnung/sav_gegenprobe.py` | `c06f4e4e7c4a14c3e329d5570748979cf0d7908ad73722374c6ddd573ad21f50` |
| `reports/claude/kontrollrechnung/sav-gegenprobe.md` | `92d077c83f5c93e473ebeccf3c5c8610fd1f3356b5118f51f4840f57bbb73deb` |
| `reports/claude/kontrollrechnung/sav-gegenprobe.json` | `53ba62b458c5b20802fb15a7f8553b166345d3594e2e7a60a3d1a16e5027f7a3` |
| `reports/claude/datenzugriff.md` | `e94248228379e1ae707b0b6856a040b2dc4f581149edb31cb9c4c0abf6d36acb` |
| `scripts/serve-dist.mjs` | `dcf54ca6b9cb31d0f100ceac9a538df83b7159cd5fc82b0fb3a10dcbe818e20d` |
| `scripts/check-public-zoom.mjs` | `7f65018bb9714f34e2e9c9c62188ca64fe549c2254b9f0bef62367c8e33fbc50` |
| `scripts/check-research-engines.mjs` | `0bee444fafc239ee02a372240bf235ade4e6b4bd92412356cb706ea05c6a0874` |
| `docs/validation.md` | `6554747d68ba0463493a0d62220195cf36104bf6610803e35991e2fa556f1ffc` |
| `docs/vorschlaege-texte-v1.entwurf.md` | `f1ed0b3844096c9af5e0c56064ed75b6b2b1918be7a6223053e3d829f82b2b2a` |
| `web/src/app/policy-draft/policy-draft.html` | `028bf30f8de8aef7072479d287cc03104218906972958556cecb0615cf9773ca` |
| `web/src/app/policy-draft/policy-draft.ts` | `f26b1a53e40e80ed12a1a32c2c754876c938d50ee6f1110ef99f67ddc64fad09` |
| `web/src/app/policy-draft/policy-draft.spec.ts` | `6a20406dc1ab55b9eee10df0ed5abb69a6609bfba67dedc921b69fbdd3c75661` |
| `web/src/app/policy-draft/reference-v22.ts` | `3790cd14e136cbd701bbc4124bcdcfbff29d6647bac66012e9794c9c662a8574` |
| `package.json` | `451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7` |
| `web/package.json` | `77db8383e6c64f65fe04638c46ba3b7f9b40040d95f0ad3ced1471fb475d60f7` |
| `.prettierignore` | `08a4df06f736d54e36b84502d1452185812e04966191918a39d299523d3c2531` |
| `scripts/check-handbuch.mjs` | `ebb9815ee0341fab5ad8aa58f01dec459dcdc08b75ca87f5a81707bab50e2813` |
| `scripts/check-review-schema.mjs` | `2575997f720f0c440fc54a9ccc15a2bd8c8fb69638dab8c03cf8b9fdaf810166` |
| `pipeline/v22/sav.py` | `2783682169b5f62a354b5384f758327aa86e6e8a7dd1e3ccd6b682d174c54216` |
| `reports/claude/kontrollrechnung/kontrolle.py` | `53c0de1ed255f03fa77ffbddb1027a7e351bd77326b8c430820fd16dc7649246` |
| `pipeline/v22/run_v22.py` | `b07d5bd8e9306dc7db2b0f1e72af9207d00ca255ea3b0c3c2f58d9f87925e1fd` |
| `pipeline/v22/run_v22_sddf.py` | `60d6904c421b8b9bee0408b8c803a43f7783025ba50661e9a63454c1d87ddf66` |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/v22/survey.py` | `ef9011c5a9b9792373f7c9395d4e5db17a4381dab648480b2276ddac15a982bc` |
| `pipeline/v22/test_survey.py` | `dacdde363044981d575636447f6e206f89a0325353c8cc7b9a7898e1ca8ed011` |
| `pipeline/v22/test_export_v22.py` | `ed9039cf2a5b0df6381649edbe098cc419597e38380ec5b9297a16b85018d4ee` |
| `pipeline/v22/test_run_v22.py` | `e893eadbf46c64c0b96739dff16105be7f83529d3c1cc317df546ab44f46667c` |
| `pipeline/v22/test_run_v22_sddf.py` | `906fd5f0a7c4bf6222a99238b77f8c7ce999149f975c90b009d5c28f394336d3` |
| `reports/loop/issue-2026-10-03.md` | `7c369ffe6b48487855b621f2c52af7a21923849289de049aba6f067fafc0a397` |
| `docs/auftrag-life-93-2026-10-03.md` | `beb4f2313454fd0d8c0fab7dd6243dbc9616a18335d9254fcbb09d74b459bdf6` |
| `web/src/index.html` | `d3dcf44566fd2c05d92b9acdf0c9d0e570b472abd3edfa7ac4face20fc15657c` |
| `reports/claude/agenten/V2-urteil.json` | `622e6961b36655943f126ffa25eb7758e3d7b025fa3a1b6275630beb673d02cf` |
| `reports/claude/agenten/T1-technik-browser.md` | `3bba4b1112db99f9938104ba82b17fdfb552d57657a5440ea4827ce7f88e3636` |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `data/politikprofil-v2.2.ergaenzung.json` | `c4b0d97aeaf10868001199cb3f7f135a6fb8ec28d63b58f7f222ff7e0acd71ac` |
| `web/src/app/pages/home/home.html` | `b227eda07cc05d085fc674c0f2731fd8e1c82108fcecbe81dc1bc052752f72d5` |
| `web/src/app/pages/methodology/methodology.html` | `343284a595b33e337adfae5febe418b5e354e00a71f5f9fc1b6aadc7cca0bdc1` |
| `web/src/app/policy-draft/profile/area-scope.ts` | `4ed439fd3a1d9b9d030f8ed33b9a4d55916d07cc694bcf8a3aec6f86d338a1b1` |
| `web/src/app/policy-draft/policy-catalogue.ts` | `acde504fa6f0b815d93c66a842d1a25270092713ea898df97b9e8617388a6193` |
| `https://www.europeansocialsurvey.org/methodology/sampling (HTML, urllib Abruf)` | `b590ff5edc7a0c260be9e6c76c4b3063b1b2d69d98b4c40d87242777d4595cd3` |

Weitere Onlinelektüre: https://github.com/Roche/pyreadstat, öffentliches README per web.run; keine lokal gespeicherte Datei und deshalb kein erfundener Datei-Hash. Die ESS-HTML-Prüfsumme bezieht sich auf die im RAM geladenen Antwortbytes. Memory: MEMORY.md, gezielte Suche und Zeilen 52–60, nur allgemeine Prüfabgrenzung; keine aktuelle technische Tatsache daraus übernommen.

### Ausgeführte Befehle und Werkzeuge

Die folgende Liste nennt Shellaufrufe in Ausführungsreihenfolge. Wiederholte Teilansichten dienen der Behandlung abgeschnittener Werkzeugausgaben. Bei langen Dateilisten und inline Python steht ausdrücklich eine Kurzform; diese Aufrufe waren reine Text-/Hashprüfungen und lasen ausschließlich die oben gebundenen zulässigen Dateien. Die beiden fehlerhaften Seitenpfade wurden nach Dateisuche korrigiert (rg Exit 2), keine Zugriffsgrenze umgangen.

```text
sha256sum reports/claude/auftraege/T2-technik-nachpruefung.md
cat reports/claude/auftraege/T2-technik-nachpruefung.md
rg -n 'LIFE-93|Claude|Prüf|review' /home/stevenh/.codex/memories/MEMORY.md
cat .agents/skills/unslop/SKILL.md
cat .claude/skills/life93-review/SKILL.md
git status --short; git branch --show-current; git rev-parse HEAD; git diff --stat b5a53ff..b4641a9; git log --oneline b5a53ff..b4641a9
cat docs/project.md docs/analyseplan-v2.2.md docs/abdeckung-v2.2.md docs/profilregeln-v1.md docs/pruefregeln.md
cat docs/handbuch.md
sed -n '52,60p' /home/stevenh/.codex/memories/MEMORY.md
cat .claude/skills/life93-review/references/urteil-schema.json
wc -l docs/project.md docs/handbuch.md docs/analyseplan-v2.2.md docs/abdeckung-v2.2.md docs/profilregeln-v1.md docs/pruefregeln.md
cat docs/analyseplan-v2.2.md
cat docs/handbuch.md
sed -n '1,180p' docs/handbuch.md
sed -n '70,166p' docs/analyseplan-v2.2.md
cat docs/pruefregeln.md docs/profilregeln-v1.md
cat docs/pruefregeln.md
cat docs/abdeckung-v2.2.md
git diff b5a53ff..b4641a9 -- web/src/app/policy-draft/policy-draft.html web/src/app/policy-draft/policy-draft.ts web/src/app/policy-draft/policy-draft.spec.ts docs/validation.md
cat reports/claude/kontrollrechnung/sav_gegenprobe.py reports/claude/kontrollrechnung/sav-gegenprobe.md reports/claude/kontrollrechnung/sav-gegenprobe.json
cat scripts/check-public-zoom.mjs scripts/serve-dist.mjs
cat scripts/check-research-engines.mjs
cat docs/vorschlaege-texte-v1.entwurf.md
cat package.json web/package.json
git diff b4641a9 -- <zwölf Umfangsdateien gemäß Hashliste>
cat .prettierignore scripts/check-handbuch.mjs scripts/check-review-schema.mjs
rg -n 'read_|open\(|Path\(|data/|outputs/|run\(|subprocess|__main__' pipeline/v22/test_*.py
cat reports/claude/datenzugriff.md
cat web/src/app/policy-draft/reference-v22.ts
sed -n '190,330p' web/src/app/policy-draft/policy-draft.html
sed -n '430,650p' web/src/app/policy-draft/policy-draft.html
cat web/src/app/policy-draft/policy-draft.ts
cat web/src/app/policy-draft/policy-draft.spec.ts
pnpm check
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'
sed -n '375,450p' web/src/app/policy-draft/policy-draft.spec.ts
sed -n '1,190p' web/src/app/policy-draft/policy-draft.html
sed -n '330,430p' web/src/app/policy-draft/policy-draft.html
sed -n '650,780p' web/src/app/policy-draft/policy-draft.html
cat pipeline/v22/sav.py
sed -n '1,155p' reports/claude/kontrollrechnung/kontrolle.py
rg -n 'csv|def read_de|def classify|def vote_party|categorical_reference|survey|sav' pipeline/v22/run_v22.py pipeline/v22/run_v22_sddf.py pipeline/policy_reference_v2.py
python3 - <<'PY' … Zeichenlängen der beiden vorgeschlagenen Metabeschreibungen mit len prüfen … PY
rg -n 'Forschungsprototyp|Phase 6|Dimensionen und Auswertung' docs/auftrag-life-93-2026-10-03.md reports/loop/issue-2026-10-03.md web/src/index.html
python3 - <<'PY' … urllib.request.urlopen(ESS-Sampling-URL, timeout=25), SHA-256 des HTML und Kontext der Zitatfragmente; nur RAM … PY
sed -n '164,180p' reports/loop/issue-2026-10-03.md
cat web/src/index.html
rg -n 'V2-F04|V2-F11|V2-F15|V2-F13|sampling|München' <benannte Fundstellen, zunächst mit zwei nicht vorhandenen Seitenpfaden>
rg --files web/src/app | rg '(home|method|scope|catalogue)'
sed -n '230,252p' reports/claude/agenten/V2-urteil.json
sed -n '358,380p' reports/claude/agenten/V2-urteil.json
sed -n '394,452p' reports/claude/agenten/V2-urteil.json
rg -n '^##|Dimension|Meta|160' reports/claude/agenten/T1-technik-browser.md
sed -n '510,540p' data/politikprofil-v2.fragen.entwurf.json
sed -n '1,155p' pipeline/v22/run_v22_sddf.py
sed -n '77,140p' pipeline/v22/run_v22.py
sed -n '205,242p' pipeline/v22/run_v22.py
rg -n 'repräsentativ|European Social' web/src/app/pages/home/home.html web/src/app/pages/methodology/methodology.html
cat web/src/app/policy-draft/profile/area-scope.ts
sed -n '1,45p' web/src/app/policy-draft/policy-catalogue.ts
rg -n 'interval|reference|estimate|lower|upper' pipeline/policy_reference_v2.py pipeline/v22/survey.py
rg -n 'radioFocus|headingFocused|Zur Fragenübersicht|stored =|value ===|checked\(\).count|ownMarks|questions =|dont-know|loaded =|report.status' scripts/check-research-engines.mjs
rg -n 'interval-note|interval-missing|category.lower|groupInterval|hasIntervals|keine Unsicherheit|interval: null|elgcoal|pair!' web/src/app/policy-draft/policy-draft.html web/src/app/policy-draft/policy-draft.ts web/src/app/policy-draft/policy-draft.spec.ts
rg -n 'duplicates|linkage|decoderComparison|Abweichung|return 0|return result|write_text|return 1' reports/claude/kontrollrechnung/sav_gegenprobe.py
sed -n '180,220p' pipeline/v22/survey.py
git status --short
git rev-parse b5a53ff 5765b36 122f69a b4641a9
rg --files pipeline/v22 -g 'test_*.py'
git diff --check b5a53ff..b4641a9 -- <zwölf Umfangsdateien>
python3 - <<'PY' … is_symlink/is_file der öffentlichen sav-gegenprobe.json … PY
python3 - <<'PY' … SHA-256 der 49 ausdrücklich benannten öffentlichen Eingabedateien … PY
nl -ba docs/analyseplan-v2.2.md | sed -n '76,96p'
nl -ba docs/validation.md | tail -n 14
nl -ba web/src/app/policy-draft/policy-draft.spec.ts | sed -n '323,377p'
```

Zusätzlich web.run: Öffnen des ursprünglichen ESS-Sampling-URL (nicht abrufbar), eine Suchabfrage nach den beiden Zitatfragmenten, Öffnen des weitergeleiteten ESS-URL (502) und der pyreadstat-Primärdokumentation. Die ESS-Fundstellen wurden danach direkt über urllib aus der Originalseite geprüft. Keine Suchergebnisfassung wurde als Volltextprüfung ausgegeben.

Werkzeugabfragen write_stdin warteten auf den ausdrücklich erlaubten pnpm-Check. Abschließend werden nur die beiden verlangten Berichte per Python geschrieben, das JSON mit Ajv2020 gegen das Urteilsschema validiert, alle Eingabehashes erneut verglichen und Git-Diff/Status auf fremde Änderungen kontrolliert. Der zweite pnpm check nach dem ersten Berichtsschreiben endete ebenfalls mit Exit 0 (113 Webtests und Produktionsbuild). Die Ergebnisdateien werden anschließend ausschließlich zur Aufnahme dieses Ausführungsbefunds und des beobachteten fremden HEAD-Wechsels ergänzt; geprüftes Produkt und Prüfurteil ändern sich dadurch nicht.


### Abschlusszustand

Während der Prüfung änderte der andere Koordinator HEAD auf `46e70be3699ee013648f6bec7729c54055b599aa`. Die Commit-Dateilisten weisen ausschließlich sachfremde Rechercheaufträge/-berichte und einen Quellenanfragenentwurf aus (`44da2d0`, `46e70be`). Diese Inhalte wurden nicht gelesen. Alle 49 lokalen Eingabehashes bleiben unverändert, ebenso die zwölf Umfangsdateien gegenüber b4641a9. Der Arbeitsbaum hat keine Änderungen an bereits versionierten Dateien durch diesen Review. Die beiden T2-Dateien sind unversioniert; übrige unversionierte Dateien gehören fremder Arbeit.

Zusätzliche Abschlussbefehle:

```text
node --input-type=module - <<'JS' … Ajv2020(strict:true, allErrors:true), Urteilsschema und T2-JSON; Fehler führen zu Exit 1 … JS
python3 - <<'PY' … erneuter SHA-256-Vergleich aller lokalen execution.inputHashes; keine Abweichung … PY
pnpm check
git status --short
git diff --name-only
git rev-parse HEAD
git log --oneline --name-only d44422720b2316da02aa01f54799d653dbae7de2..HEAD
python3 - <<'PY' … Eingabehashvergleich nach fremdem HEAD-Wechsel; keine Abweichung … PY
python3 - <<'PY' … nur die beiden erlaubten Ergebnisdateien um bestätigten Abschlussbefund ergänzen … PY
node --input-type=module - <<'JS' … abschließende Schema-, Hash- und Berichtskonsistenzprüfung … JS
```

Modell laut Laufzeit: OpenAI `gpt-6.1-sol`, high reasoning effort, Codex harness in T3 Code. Genauere interne Revision unbekannt.
