# Gezielte Nachprüfung PP-001, Runde 1

PP-001 ist für den ausdrücklich vereinbarten Arrayvertrag in der gepinnten v2-Fassung behoben. Eigene Iteratoren und sonstige Zusatzfelder bleiben unbeachtet; die Kopie nutzt eigene numerische Datenfelddeskriptoren eines dichten Arrays. Lücken und Element-Accessoren werden zurückgewiesen, ohne die geprüften Aufrufer-Getter oder Iteratoren auszuführen. Dies gilt auch für die äußere Fragenliste. Ich fand in diesem Umfang keinen neuen konkreten Softwarefehler.

Die 21 vorhandenen gezielten Vitesttests und meine 13 neuen Orakel bestehen mit Exitcode `0`. Die unveränderten Erstfälle enden tatsächlich mit Exitcode `1`, 13 bestandenen und zwei fehlgeschlagenen Fällen. Die beiden Fehler entstehen jetzt durch richtige Abweisungen, die diese alten Reproduktionen noch nicht abfangen. Ich habe sie nicht umgeschrieben und nicht als bestandene Tests gezählt. Die neuen Orakel prüfen die jeweiligen Fehlerpfade ausdrücklich.

Arbeitsverzeichnis war `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Der Branchname und die Erhaltung der ursprünglichen Codefassung in `88eb7db56f00101cf76d46019661076d15deed70` sind Auftragsangaben. Das v2-Manifest nennt denselben Commit. Ich habe weder Git abgefragt noch dessen Inhalt überprüft. Die historischen Erstpins bleiben die im Erstauftrag genannten Werte `70f8b5db3bf055bb5b2ef26174f060591c9b98010b5fd1de6e101aafbd151f54` für den Code und `0592b02f76c9d8caf92b2763787f83c9f2c72b42508d1939591023c2aadea5f5` für die Spezifikation. Diese Runde bewertet ausschließlich v2.

Vor dem Lesen und Testen verglich ich die aktuellen Hashes mit [manifest.json](../packages/POLICY-PROFILE-001/v2/manifest.json). Der UTC-Marker dieser ersten Werkzeugrunde ist `2026-10-03T13:13:54Z`; siehe [initial-pin-check.txt](../../../outputs/loop/policy-profile-001-review/round1/initial-pin-check.txt). Ein weiterer Vergleich unmittelbar vor den neuen Orakeln lief von `2026-10-03T13:16:27.147Z` bis `2026-10-03T13:16:27.148Z`. Er steht in [integrity-before.json](../../../outputs/loop/policy-profile-001-review/round1/integrity-before.json). Der Vergleich nach allen Tests und dem ersten Schreiben dieses Rundenberichts endete um `2026-10-03T13:18:52.990Z` mit Exitcode `0`. Alle vier fest vorgegebenen Hashes stimmen weiterhin; auch der Manifesthash ist unverändert. Das vollständige Ergebnis steht in [integrity-after.json](../../../outputs/loop/policy-profile-001-review/round1/integrity-after.json).

| Datei | Erwarteter und vor den Tests beobachteter SHA256 |
| --- | --- |
| `web/src/app/research/policy-profile.ts` | `28906eb1533bb953b43bed75a4995c907b71398f1ffcd63271c82cfdace05998` |
| `web/src/app/research/policy-profile.spec.ts` | `6b2b3302afe308f28f65ec9aba76c7f1b8b6d14bf9ffa9b8fbc6508f9a1c22c1` |
| Unveränderter Erstbericht | `bbc62b4ff955d92f264c63eea2f2d33370864f447495d7117b92cfc6db960b2f` |
| Unveränderte eigene Erstfälle `review-cases.mjs` | `2f36888bbb0f69f69703c17c994394c2375e61086eb885f9f7d8d3797a8f6c34` |
| V2-Manifest, eigener Ausgangsvergleich | `2ec47a2bcc53c46c867a781c334a99f66042190655e033093526711e42762551` |

Der Erstbericht stimmt vor der Runde mit dem im Manifest festgehaltenen Hash überein. Der Abschlussvergleich prüft zusätzlich seine Erhaltung und die Erhaltung des ursprünglichen Testskripts sowie des Manifests. Mein Ersturteil über die ursprüngliche Fassung bleibt unangetastet. Diese Nachprüfung ergänzt es um das Urteil zur Korrektur.

Die entscheidende Änderung ist [policy-profile.ts](../../../web/src/app/research/policy-profile.ts:125), Zeilen 125–148. `passiveArray()` liest den eigenen `length`-Deskriptor und für jeden Index unterhalb dieser Länge den eigenen Property-Deskriptor. Fehlt ein Datenwert, wirft es `PolicyProfileInputError`. Es liest weder `value[index]` noch den Aufrufer-Iterator. Zusätzliche Own-Properties werden gar nicht abgefragt. Die äußere Liste nutzt diese Grenze in Zeile 152, die Kategorien in Zeile 169. Die nachfolgende Kategorienprüfung in Zeilen 170–184 prüft die eigene Kopie auf nichtleere Stringcodes und Duplikate. Die Iteration dort betrifft das neu erzeugte interne Array, keinen Iterator des Aufrufers.

| Teil von PP-001 beziehungsweise unmittelbare Regression | Tatsächlich geprüfte Evidenz |
| --- | --- |
| Iterator liefert fremden Code | R1-01 konstruiert erfolgreich mit dem deklarierten Indexwert. `fabricated-code` wird mit unverändertem Snapshot und Ergebnis abgewiesen. Der deklarierte Code lässt sich beantworten. Iteratoraufrufe `0`. Eigene Fälle Zeilen 34–46. |
| Ungültige Kategorie hinter gültigem Iterator versteckt | `[null]`, weitere falsche Typen, leere Codes und Duplikate werden abgewiesen. Iteratoraufrufe `0`. Der unveränderte alte Null-Fall besteht jetzt ebenfalls. R1-10, Zeilen 193–207. |
| Kategorie-Getter verändert Quellen | Konstruktor wirft am numerischen Feld, Getteraufrufe `0`, `studyId` bleibt unverändert. R1-02, Zeilen 48–60. |
| Direkter Getter der äußeren Liste | Konstruktor wirft bei `questions[0]`. Getteraufrufe `0`, Quellenmodus und Kategorie bleiben unverändert. R1-03, Zeilen 62–75. |
| Eigene Iteratoren und übrige Own-Properties ignorieren | Auf beiden Arrayebenen bleiben Iteratorfunktionen sowie werfende Getter auf Symbolen und Zusatzschlüsseln unaufgerufen. Darunter `01`, `-0`, `0.0`, `1e0` und `4294967295`, die keine entsprechenden numerischen Arrayindizes sind. R1-04/R1-05, Zeilen 77–113. |
| Dichte eigene Datenfelder verlangen | Erste, mittlere und letzte Lücken werden auf beiden Ebenen abgewiesen. Lokale geerbte Datenfelder oder Getter füllen keine Lücke; die geerbten Getter bleiben unaufgerufen. R1-06/R1-08, Zeilen 115–132 und 153–171. Dafür änderte ich nur lokale Arrayprototypen, keinen globalen Prototyp. |
| Alle Element-Accessoren abweisen | Getter, Setter und kombinierte Accessoren an drei Positionen auf beiden Ebenen werden abgewiesen. Alle Aufrufzähler bleiben `0`. R1-07, Zeilen 134–151. |
| Zulässige Datenfelder erhalten | Dichte, nicht aufzählbare und eingefrorene Datenfelder werden in numerischer Reihenfolge kopiert. ` 01 `, `01` und `1` bleiben verschieden. R1-09, Zeilen 173–191. |
| Äußere Elemente weiter validieren | Ungültige eigene Elemente werden trotz eines gültig wirkenden eigenen Iterators abgewiesen. Ein leeres äußeres Array bleibt leer; leere Kategorien bleiben ungültig. R1-11/R1-12, Zeilen 209–232. |
| Kopie und Sessionverhalten nach der Änderung | Erst nach dem Konstruktor angebrachte Getter und Quellenänderungen beeinflussen die Session nicht. Frühere Snapshots, eine zweite Session, andere Antworten und Referenzstatus `none` bleiben erhalten; ausgewählte Mutationsversuche auf Ausgaben scheitern. R1-13, Zeilen 234–264. Zusätzlich bestehen die zwölf unveränderten ursprünglichen Fälle außerhalb der Reproduktionen, einschließlich 1.500 synthetischer Zustandsoperationen. |

Die neuen Fälle stehen vollständig in [targeted-cases.mjs](../../../outputs/loop/policy-profile-001-review/round1/targeted-cases.mjs). Ihre Zähler und Sollwerte sind im eigenen Testskript festgelegt. Sie nutzen nur erfundene Kategorien, Identitäten und Quellenangaben. Die drei unmittelbar zu PP-001 protokollierten Ergebnisse lauten:

```json
{"oracle":"R1-01","calls":0,"categories":["declared-original"],"acceptedAnswer":{"status":"answered","code":"declared-original"},"injectedCode":"rejected without state change"}
{"oracle":"R1-02","reads":0,"sourceAfter":"synthetic-a-invented-study","constructor":"rejected"}
{"oracle":"R1-03","reads":0,"mode":"invented-mode","indexedCategory":"declared-original","constructor":"rejected"}
```

Die vorhandenen acht zusätzlichen Fälle stehen in [policy-profile.spec.ts](../../../web/src/app/research/policy-profile.spec.ts:338), Zeilen 338–497. Ich habe die bestehenden Testdateien nicht verändert.

| Abgewarteter Prozess | Tatsächlicher Abschluss und UTC-Evidenz |
| --- | --- |
| `pnpm --dir web test --watch=false --include=src/app/research/policy-profile.spec.ts` | Exitcode `0`, 21/21 Tests bestanden. Die zunächst laufende Session `69944` wurde mit `write_stdin` bis zum Abschluss abgefragt. UTC-Buildmarker `2026-10-03T13:14:25.963Z`; [vitest.log](../../../outputs/loop/policy-profile-001-review/round1/vitest.log). |
| `node --test outputs/loop/policy-profile-001-review/review-cases.mjs` | Exitcode `1`, 13/15 bestanden, zwei fehlgeschlagen. Start `2026-10-03T13:14:25.574Z`, Ende `2026-10-03T13:14:25.634Z`; [unchanged-first-cases.log](../../../outputs/loop/policy-profile-001-review/round1/unchanged-first-cases.log). |
| `node --test outputs/loop/policy-profile-001-review/round1/targeted-cases.mjs` | Exitcode `0`, 13/13 bestanden, keiner ausgelassen oder abgebrochen. Start `2026-10-03T13:16:27.326Z`, Ende `2026-10-03T13:16:27.340Z`; [targeted-cases.log](../../../outputs/loop/policy-profile-001-review/round1/targeted-cases.log). |
| `node outputs/loop/policy-profile-001-review/round1/check-integrity.mjs before` | Exitcode `0`; alle vier fest vorgegebenen Dateihashes und die Manifestangaben stimmen. Zeitstempel im eigenen JSON. |
| `node outputs/loop/policy-profile-001-review/round1/check-integrity.mjs after` | Exitcode `0`; alle vier Dateihashes, Manifestpins und Manifest-Erhaltung bestätigt. Start `2026-10-03T13:18:52.989Z`, Ende `2026-10-03T13:18:52.990Z`. |

Die beiden Fehler der unveränderten Erstfälle bleiben im Log sichtbar. Der Fall ab Zeile 285 scheitert nun an Zeile 290 mit `unknown category for question: q-a`: Der Konstruktor bewahrt den richtigen Code, die anschließende alte Reproduktion versucht weiterhin den eingeschleusten Code zu beantworten. Der Fall ab Zeile 309 scheitert nun an Zeile 317 schon bei der Konstruktion mit `questions[0].categories[0] must be an own data field`. Er erreicht seine früheren Getter-Assertions nicht. R1-01 und R1-02 prüfen genau diese zulässigen Abweisungen und zusätzlich die Zähler und unveränderten Daten. Damit begründe ich das Korrektururteil unabhängig von einer bloßen Interpretation des alten Exitcodes.

Die beobachteten Prozessresultate sind zusätzlich in [process-results.json](../../../outputs/loop/policy-profile-001-review/round1/process-results.json) festgehalten. Alle Test- und Integritätsprozesse sind abgeschlossen; es bleibt keiner zur Beobachtung offen. Node `v24.21.0` meldete wie beim ersten Lauf eine Warnung zur erkannten Modulart und führte die Dateien danach vollständig aus. Die Vitestsuite lief mit Vitest `5.0.3`.

Diese Runde bleibt eine begrenzte Softwareprüfung von PP-001 und unmittelbaren Regressionen. Sie ist kein Gesamtaudit und keine empirische Prüfung. Proxy-Isolation, globale Prototypänderungen und die Isolation beliebigen Aufrufer-JavaScripts wurden nicht geprüft und werden nicht zugesagt. Es gab keine Einsicht in andere Urteile, Autorenberichte, state/handoff oder Forschungs-/Datenverzeichnisse und keine Git-, Auth-, Netz-, Claude-, Installations-, Server-, Agenten- oder Gesamtcheckaktion. Ich las die zwei Prüffassungen, das freigegebene Manifest und `web/package.json`; den bereits gelesenen unslop-Skill nutzte ich erneut für die Formulierungen. Ich schrieb nur diesen Rundenbericht und Dateien unter `outputs/loop/policy-profile-001-review/round1/`. Es gibt keine empirische, methodische oder Produktfreigabe. Die gleiche Codex-Modellfamilie begrenzt weiterhin die Unabhängigkeit dieser Prüfung.
