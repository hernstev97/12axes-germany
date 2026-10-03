# Begrenzte Codex-Erstprüfung POLICY-PROFILE-001

Ich habe einen reproduzierbaren Softwarebefund gefunden: PP-001 betrifft die Übernahme von Kategoriearrays. Die vorhandenen 13 Tests bestehen. Von meinen 15 zusätzlichen synthetischen Prüffällen bestehen zwölf; drei scheitern an unterschiedlichen Ausprägungen desselben Befunds. Die übrigen geprüften Zustands- und Ausgabegrenzen zeigen keinen weiteren konkreten Fehler.

Prüfdatum ist der 3. Oktober 2026. Der erste erfasste UTC-Marker nach dem anfänglichen Pinvergleich ist `2026-10-03T12:58:20Z`. Die eigenen Tests liefen von `2026-10-03T13:00:48.946Z` bis `2026-10-03T13:00:48.996Z`. Eine erste Nachprüfung der Pins war um `2026-10-03T13:01:45.746Z` abgeschlossen; der zusätzliche abschließende Vergleich nach dem Schreiben dieses Berichts steht mit eigenem UTC-Zeitstempel in [pin-check-after.json](../../../outputs/loop/policy-profile-001-review/pin-check-after.json).

Arbeitsverzeichnis war `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Der Branch `research/life-93-night-20261003` stammt aus dem Auftrag; ich habe ihn wegen des Git-Verbots nicht abgefragt. Ich las die beiden Prüffassungen, `web/package.json` und den ausdrücklich genannten unslop-Skill. Eine begrenzte Dateinamensuche nach Vitestkonfigurationen unter `web` fand keine passende Datei. Ich las keine Autorenberichte, anderen Reviews, Zustands-/Übergabedateien oder Forschungs-/Datenverzeichnisse. Alle Identitäten, Kategorien, Quellenangaben und Antwortoperationen in meinen Fällen sind erfunden.

| Prüffassung | SHA256 vor der Prüfung | SHA256 nach den Tests |
| --- | --- | --- |
| `web/src/app/research/policy-profile.ts` | `70f8b5db3bf055bb5b2ef26174f060591c9b98010b5fd1de6e101aafbd151f54` | identisch |
| `web/src/app/research/policy-profile.spec.ts` | `0592b02f76c9d8caf92b2763787f83c9f2c72b42508d1939591023c2aadea5f5` | identisch |

Der anfängliche Vergleich mit den Auftragspins ist in [pin-check-before.txt](../../../outputs/loop/policy-profile-001-review/pin-check-before.txt) festgehalten. Der Abschlussvergleich prüft dieselben erwarteten Hashes und protokolliert die tatsächlich berechneten Werte. Code, bestehende Spezifikation und Konfiguration habe ich nicht bearbeitet.

**PP-001. Kategoriearrays können andere Codes liefern und beim Einlesen Quellen verändern.** Priorität P2; im aufgerufenen Konstruktor direkt reproduziert. Die Auswirkung betrifft speziell Arrays mit überschriebenem Iterator oder Element-Getter. Für gewöhnliche Arrays mit eigenen Datenfeldern habe ich diesen Fehler nicht beobachtet.

Die Kategorieprüfung in [policy-profile.ts](../../../web/src/app/research/policy-profile.ts:137), Zeilen 137–152, prüft `Array.isArray` und die Länge, liest anschließend aber mit `for ... of`. Damit bestimmt ein eigener `Symbol.iterator`, welche Codes die Bibliothek kopiert. Die eigenen numerischen Arrayelemente müssen dabei weder den kopierten Codes entsprechen noch gültig sein. `answer()` akzeptiert später genau die kopierte Liste, siehe [policy-profile.ts](../../../web/src/app/research/policy-profile.ts:200), Zeilen 200–205.

Der erste Gegenfall übergibt ein Array mit `categories[0] === 'declared-original'`. Sein eigener Iterator liefert ausschließlich `'fabricated-code'`. Der Konstruktor übernimmt diesen anderen Code, und `answer('q-a', 'fabricated-code')` gelingt. Der zweite Gegenfall übergibt `[null]` mit demselben Iterator. Auch dieses ungültige Array akzeptiert der Konstruktor. Die beobachteten Werte stehen unverändert im Testprotokoll:

```json
{"evidence":"PP-001","inputIndex0":"declared-original","iteratorCalls":1,"acceptedCategories":["fabricated-code"],"acceptedAnswer":{"status":"answered","code":"fabricated-code"}}
{"evidence":"PP-001-invalid-index","inputIndex0":null,"acceptedCategories":["fabricated-code"]}
```

Der dritte Gegenfall nutzt ein gewöhnliches Array mit einem Getter an Index `0`. Dieser Getter setzt beim Lesen `source.studyId` auf `'changed-by-getter'`. Der Konstruktor führt ihn einmal aus und kopiert danach die geänderte Quelle. Die Reihenfolge ist in [policy-profile.ts](../../../web/src/app/research/policy-profile.ts:142), Zeilen 142–153, sichtbar. Beobachtet wurden `reads: 1`, `sourceAfter: 'changed-by-getter'` und `acceptedSource: 'changed-by-getter'`. Die Mutation stammt aus dem Aufrufer-Getter, den die Bibliothek ausführt. Dies ist kein Nachweis einer Mutation bereits ausgegebener Snapshots.

Das widerspricht der Übernahme exakt vorgegebener Originalcodes und lässt die Eingabeprüfung für nicht passive Arrays umgehen. Der Getterfall zeigt außerdem, dass die Kopie allein die Eingabegrenze während der Konstruktion nicht schützt. Ich bewerte damit keine wissenschaftliche Echtheit der Angaben. Eine solche Prüfung ist ausdrücklich nicht Teil des Auftrags.

Die Reproduktion steht in [review-cases.mjs](../../../outputs/loop/policy-profile-001-review/review-cases.mjs:285), Zeilen 285–321. Aus dem genannten Arbeitsverzeichnis genügt:

```sh
node --test outputs/loop/policy-profile-001-review/review-cases.mjs
```

Der Prozess endet mit Exitcode `1`: drei fehlgeschlagene Soll-Prüfungen zu PP-001, zwölf bestandene Fälle. [synthetic-tests.log](../../../outputs/loop/policy-profile-001-review/synthetic-tests.log) enthält die Laufzeiten, die diagnostischen Werte und die Assertions. Die vorhandene Spezifikation prüft gewöhnliche ungültige Kategorien in [policy-profile.spec.ts](../../../web/src/app/research/policy-profile.spec.ts:231), Zeilen 231–244. Ihr Getterfall in [policy-profile.spec.ts](../../../web/src/app/research/policy-profile.spec.ts:307), Zeilen 307–321, betrifft ein Quellenfeld. Überschriebene Array-Iteratoren und Element-Getter deckt sie nicht ab.

Als Korrektur sollte die Bibliothek einen klaren Vertrag für passive Eingabearrays durchsetzen. Sie kann eigene numerische Datenfelder anhand ihrer Deskriptoren lesen und Element-Getter zurückweisen, ohne den überschreibbaren Iterator aufzurufen. Dieselbe Grenze ist bei der äußeren Fragenliste sinnvoll: [policy-profile.ts](../../../web/src/app/research/policy-profile.ts:127), Zeilen 127–129, liest deren Indizes direkt. Diesen äußeren Getterfall habe ich nicht dynamisch ausgeführt; er ist eine konkrete Anschlussstelle für die Korrektur, kein zusätzlicher reproduzierter Befund. Proxy-Objekte und globale Eingriffe in Standardprototypen habe ich nicht geprüft. Die Empfehlung verspricht keine Absicherung beliebigen fremden JavaScript-Codes.

Die folgende Abdeckung beschreibt ausschließlich Softwarebeobachtungen für die geprüfte Fassung:

| Anforderung | Beobachtung und Fundstelle |
| --- | --- |
| Drei Antwortzustände, keine erzwungene Mitte oder Antwort | Alle neun Kombinationen aus Anfangszustand und `answer`/`skip`/`resetAnswer` bestanden. Navigation bei leerem und einteiligem Katalog erzeugte keine Antwort. Code Zeilen 68–69, 179–184, 200–215 und 223–237; eigene Fälle Zeilen 53–107 und 137–148. |
| Unbekannte IDs/Kategorien ohne Zustandsänderung | Unbekannte und falsch typisierte IDs bei allen fünf ID-Methoden sowie ungültige Codes warfen `PolicyProfileInputError`. Snapshot und Ergebnis blieben gleich. Code Zeilen 191–225; eigene Fälle Zeilen 109–135. |
| Originalcodes exakt | Bei passiven Arrays blieben Leerzeichen, Groß-/Kleinschreibung, `01` gegenüber `1` und verschiedene Unicodefolgen erhalten. Die Grenze bei aktiven Arrays bleibt wegen PP-001 offen. |
| Vorwärts, rückwärts und gezielt navigieren | 1.500 deterministische synthetische Operationen stimmten mit einem eigenen Zustandsmodell überein. Alte Snapshots blieben unverändert. Eigener Fall Zeilen 77–107. |
| Kopierte Eingaben und unveränderliche Ausgaben | Spätere Änderungen an gewöhnlichen Eingabearrays/-objekten änderten die Session nicht. Alle erreichbaren Objekte in geprüften Snapshots, Ergebnissen, aktuellen Fragen und Antworten waren eingefroren. Schreib-, Lösch- und Definitionsversuche an zwölf ausgewählten Stellen scheiterten. Code Zeilen 110–117, 160–164, 240–287; eigene Fälle Zeilen 150–202. Während der Konstruktion bleibt PP-001 offen. |
| Unabhängige Sessions | Antworten, Navigation und Quellenkopien zweier Sessions blieben getrennt. Eigener Fall Zeilen 204–215. |
| Einzelne vollständige Quellenangaben | Alle sechs Felder einschließlich `sourceId` sind im Ergebnis vorhanden. Fehlende, leere, falsch typisierte, geerbte oder zusätzliche Quellenfelder wurden in den geprüften Fällen zurückgewiesen. Code Zeilen 76–117; eigene Fälle Zeilen 238–269. Dies prüft Struktur, keine Echtheit. |
| Gleiche Original-/Kategoriecodes verschiedener Studien | Zwei Studien mit gleichem Originalfragecode und gleicher Antwortkategorie blieben zwei Einzelangaben mit getrennten `studyId`-Werten. Eigener Fall Zeilen 217–236. |
| Themen gruppieren nur beantwortete Angaben | Ergebnisformen und Reihenfolge entsprachen den Einzelangaben; übersprungene Angaben blieben separat. Code Zeilen 251–287. Im geprüften Modul gibt es keine Personenverknüpfung, Kovarianz-, Score- oder Faktorberechnung, keine Polung, Parteienzuordnung, Perzentile, Konfidenzintervalle oder Referenzzahlen. |
| Aktuelle Referenz `none` | Beantwortete und unbeantwortete Angaben enthielten ausschließlich `{ status: 'none' }`. Code Zeilen 70, 263 und 274; eigener Fall Zeilen 217–236. Ein konkreter Referenzvalidator wurde nicht untersucht. |
| Reine Bibliothek ohne Route/UI/IO/Persistenz | Das vollständig gelesene Modul enthält Typen, Eingabeprüfung und lokale Session-/Ergebnislogik, keine Imports, Route, UI, IO- oder Persistenzoperationen. Die Ausführung von Aufrufer-Gettern/Iteratoren bei PP-001 begrenzt die Aussage über Seiteneffektfreiheit an der Eingabegrenze. |

Alle gestarteten Prüfprozesse sind beendet und ihre Abschlussresultate wurden abgewartet:

| Prozess | Tatsächlich beobachteter Abschluss |
| --- | --- |
| `pnpm --dir web test --watch=false --include=src/app/research/policy-profile.spec.ts` | Nach der anfänglichen laufenden Session `20543` mit `write_stdin` bis zum Abschluss abgefragt. Exitcode `0`; Vitest `5.0.3`, eine Datei und 13 Tests bestanden. UTC-Buildmarker `2026-10-03T12:58:38.892Z`. Übernommene Terminalausgabe in [existing-tests.log](../../../outputs/loop/policy-profile-001-review/existing-tests.log). |
| `node --test outputs/loop/policy-profile-001-review/review-cases.mjs` | Exitcode `1`; Node `v24.21.0`, 15 Fälle vollständig abgeschlossen, zwölf bestanden, drei fehlgeschlagen, keiner ausgelassen oder abgebrochen. UTC-Marker im eigenen Log. |
| `node outputs/loop/policy-profile-001-review/verify-pins.mjs` | Nach den Tests Exitcode `0`; beide Pins identisch. Ein weiterer Abschlussvergleich nach dem Bericht wird im selben eigenen JSON-Protokoll festgehalten. |

Node meldete bei der direkten TypeScript-Ausführung eine Warnung zur automatisch erkannten Modulart. Die Datei wurde anschließend ausgeführt; es war kein Importabbruch. Die eigenen Fälle nutzen Node-Test und dessen TypeScript-Unterstützung, die bestehende Suite lief über Angular/Vitest. Ich habe keinen zusätzlichen Vitestlauf mit eigenen Dateien, keinen vollständigen Repositorycheck und keine Browserprüfung gestartet.

PP-001 bleibt zur Korrektur offen. Es gab keine Git-, Netz-, Auth-, Claude-, Installations-, Server- oder Delegationsaktion. Meine ausdrücklich geschriebenen Dateien liegen nur in diesem Bericht und `outputs/loop/policy-profile-001-review/`. Ich habe keine Produkt-, methodische oder menschliche Freigabe erteilt. Die Fälle prüfen Software mit synthetischen Angaben; sie sind keine empirische Prüfung. Diese Erstprüfung stammt aus derselben Codex-Modellfamilie. Der getrennte Lauf ohne andere Urteile begrenzt Übernahme fremder Bewertungen, stellt aber keine Unabhängigkeit zwischen Modellfamilien her.
