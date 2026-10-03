POLICY-PROFILE-WIP — technische Vorbereitung, 2026-10-03

Autor: Codex-Unteragent `/root/breadth_topic_frame`. Auftrag: eine begrenzte TypeScript-Bibliothek für getrennte kategoriale Einzelangaben. Root bleibt alleiniger Koordinator. Dieser Bericht ist die gesonderte Erstfassung für diesen Auftrag; frühere Themen- und Rechenberichte bleiben unverändert.

Die Bibliothek und 13 synthetische Vitest-Tests sind geschrieben. Der gezielte Testlauf endete mit Exit 0. Das Ergebnis ist ein WIP für lokale Antwortverwaltung, ohne wissenschaftliche, fachliche, gestalterische oder Produktfreigabe. Es gibt keine eingebauten Fragen, Originalkategorien, Referenzanteile oder festgelegten Themen.

Arbeitsort: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Der vom Koordinator bezeichnete Branch ist `research/life-93-night-20261003`; ich habe keinen Git-Befehl ausgeführt und deshalb keinen aktuellen Branch- oder Commitstand selbst bestätigt.

Gelesene lokale Arbeitsgrundlagen: `AGENTS.md`, `docs/project.md`, `web/package.json`, `web/tsconfig.json`, `web/tsconfig.spec.json`, `web/angular.json` und `web/src/app/art/art-gallery.spec.ts`. Die bestehenden Tests verwenden Vitest-Globals und den Angular-Builder `@angular/build:unit-test`. Keine UI- oder Gestaltungsebene wurde bearbeitet. Andere neue Autorenurteile, Datenautorenberichte oder Forschungsberichte wurden für diesen Auftrag nicht gelesen.

Die beiden neuen Dateien sind:

| Datei | SHA-256 nach dem Testlauf |
| --- | --- |
| `web/src/app/research/policy-profile.ts` | `70f8b5db3bf055bb5b2ef26174f060591c9b98010b5fd1de6e101aafbd151f54` |
| `web/src/app/research/policy-profile.spec.ts` | `0592b02f76c9d8caf92b2763787f83c9f2c72b42508d1939591023c2aadea5f5` |

`PolicyProfileSession` hält den Zustand ausschließlich im Speicher ihrer Instanz. Die Bibliothek hat keine Imports und verwendet keine Datei-, Netzwerk-, Storage-, Cookie-, Analyse- oder Auth-Schnittstelle. Sie ist nicht an eine Route, eine UI oder einen sichtbaren Teststart gebunden. Es existiert keine Serialisierungs- oder Personenverknüpfungsfunktion.

Jede übergebene Frage besteht aus einer global eindeutigen `id`, genau einem `primaryTheme`, einer nichtleeren Liste eindeutiger ursprünglicher Stringcodes und einem eigenen `source`-Objekt. Dieses Objekt enthält getrennt `studyId`, `originalQuestionId`, `sourceId`, `time`, `population` und `mode`. Die Objekte haben ein geschlossenes Feldschema. Fehlende, zusätzliche, nicht als Datenfelder gespeicherte oder typfalsche Felder führen zu `PolicyProfileInputError`.

IDs und Quellenfelder müssen nichtleere Strings ohne äußeren Leerraum sein. `time`, `population` und `mode` sind erforderliche, unveränderte Beschreibungen des Aufrufers. Sie werden strukturell geprüft; eine Datumsinterpretation, eine belegte Studienpopulation, eine instrumentengerechte Modusbeschreibung oder die Echtheit einer Quellenkennung kann diese Bibliothek nicht prüfen. Diese inhaltlichen Prüfungen bleiben beim künftigen Quellen- und Fragebogenauftrag. Eine Version kann Teil der übergebenen Quellenkennung sein; hier wird keine Quellenversion erfunden.

Die Codes bleiben exakt erhalten, einschließlich vorhandenen äußeren Leerraums, sofern der Code nicht nur Leerraum enthält. Es gibt kein Trimmen, keine Umkodierung, keinen reservierten numerischen Missing-Code, keine Fallnormalisierung und keine Links-/Rechts- oder andere Polung. Doppelte globale Frage-IDs, doppelte Codes einer Frage sowie doppelte `originalQuestionId` innerhalb derselben `studyId` sind Fehler. Derselbe Original-Fragencode oder Kategoriecode in unterschiedlichen Studien ist zulässig und führt zu getrennten Einträgen. Diese Identitätsregel setzt voraus, dass der Aufrufer für tatsächlich verschiedene Studien und Originalfragen passende Kennungen vergibt; sie löst keine Quellenkonflikte selbst.

Die Anzahl der Fragen, Themen und Kategorien hat keine hier festgelegte wissenschaftliche Vorgabe. Auch ein leerer Katalog ist zulässig: Er hat keine aktuelle Frage, keine Antworten und kein Profil. Eine Rubrik ist nur ein Gruppierungsschlüssel. Daraus entsteht keine Messdimension, kein gemeinsamer Faktor und keine Behauptung thematischer Vollständigkeit.

Antworten unterscheiden genau drei Zustände: `untouched`, `skipped` und `answered` mit einem gültigen Originalcode. Anfangs ist jede Frage `untouched`. Navigation verändert keinen Antwortzustand und erzwingt keine Vollständigkeit. `answer(id, code)` ersetzt nur diese Einzelantwort; `skip(id)` setzt sie ausdrücklich auf übersprungen; `resetAnswer(id)` setzt sie ausdrücklich auf unberührt zurück. Es gibt keine automatische Mitte oder automatische Beantwortung. Ungültige IDs und Codes werden vor jeder Zustandsänderung abgewiesen.

`next()` und `previous()` bewegen die interne Position innerhalb des Katalogs. Am Anfang beziehungsweise Ende bleiben sie ohne Änderung. `goTo(id)` ermöglicht eine frühere Antwort gezielt wieder aufzurufen. Diese internen Regeln sind technische Vorbereitung und legen kein späteres Bedienmuster fest. Antwortänderungen setzen weder die Navigation noch andere Antworten zurück.

`snapshot()` liefert einen eingefrorenen Stand mit der aktuellen Frage-ID sowie jeder Frage und ihrem Antwortzustand. Eingabedaten werden beim Anlegen kopiert und eingefroren; spätere Änderungen am ursprünglichen Katalog können Quellen und erlaubte Codes deshalb nicht ändern. Früher ausgegebene Snapshots bleiben auch nach späteren Antwortänderungen erhalten. Verschiedene Instanzen haben getrennte Antwort- und Navigationszustände.

`result()` gruppiert ausschließlich tatsächlich beantwortete Einzelangaben nach dem übergebenen Primärthema. Jede Angabe führt ihre Frage-ID, ihren unveränderten Code und ihr eigenes vollständiges Quellenobjekt mit. Die Reihenfolge folgt den tatsächlich beantworteten Einträgen in Katalogreihenfolge. Unbeantwortete Fragen stehen gesondert mit `untouched` oder `skipped` und ihrer Quelle. Für sie entsteht kein numerischer Profilwert. Die Ausgabe enthält keine Scores, Perzentile, Referenzanteile, Intervalle, Parteifarben oder Gemeinsamkeiten zwischen Personen aus Studien.

Bei jeder Angabe und jeder unbeantworteten Frage ist eine fehlende Referenz explizit als `reference: { status: 'none' }` angegeben. Der im Auftrag optionale Referenzvalidator bleibt offen. Ohne konkret festgelegtes, quellspezifisch geprüftes Referenzartefaktschema wäre ein Validator mit Nennersemantik, kategorialem Abgleich und Summentoleranz ein zusätzlicher ungeprüfter Vertrag. Diese Erstfassung nimmt deshalb kein Artefakt entgegen. Es wurden weder Demoanteile noch Denominator-Metadaten oder vermeintlich passende Referenzen eingebaut. Vor einer Ergänzung müssen Studien-/Fragenbindung, exakte Kategorien, gültige und fehlende Nenner, fehlende beziehungsweise nichtgestellte Angaben und eine begründete Toleranz eigens festgelegt und geprüft werden.

Die 13 Tests benutzen ausschließlich frei erkennbare synthetische Kennungen wie `synthetic-study-a` und `a-code-1`. Sie prüfen:

- Vor- und Zurücknavigation, Erhaltung früherer Antworten sowie Änderung einer früheren Antwort bei unveränderten anderen Antworten und unverändertem alten Snapshot.
- Die gesonderten Zustände unberührt, übersprungen, beantwortet und ausdrücklich zurückgesetzt; eine Ausgabe bei vollständig fehlenden Antworten ohne Zahl oder Ersatzcode.
- Konkrete erwartete Einzelantworten mit den jeweils richtigen Quellen bei zwei Studien, wiederholten Original-Fragencodes und unterschiedlichen Kategorien; keine Zusammenführung über gleiche Codes oder gemeinsame Rubriken.
- Unbekannte Fragen und Kategorien, Code-Schreibweise und äußeren Leerraum als Fehler; der komplette vorherige Zustand bleibt dabei unverändert.
- Leere Kataloge, Navigationsgrenzen und voneinander unabhängige Sitzungen.
- Doppelte globale IDs, doppelte Originalfrage innerhalb einer Studie, doppelte oder fehlende Kategorien, Nichtstringcodes, fehlende/typfalsche/zusätzliche Quellenfelder, ungültige Frage- und Themenfelder sowie lückenhafte Arrays.
- Schutz vor nachträglicher Änderung der Eingabekategorien und Herkunft, eingefrorene Ausgabedaten und Abweisung von Quellen-Gettern vor ihrer Auswertung.

Die Tests sind Verhaltensprüfungen mit fest formulierten erwarteten Zuständen und Herkunftsangaben. Sie lesen keine Studienantworten und liefern keine Empirie. Sie prüfen auch keine Verständlichkeit tatsächlicher Fragen, Repräsentativität, fachliche Abdeckung oder empirische Dimensionalität.

Der einzige Node-/pnpm-Lauf dieses Auftrags war:

```text
pnpm --dir web test --watch=false --include=src/app/research/policy-profile.spec.ts
```

Beginn: `2026-10-03T12:52:07.929674+00:00`, Ende: `2026-10-03T12:52:10.396125+00:00`. Der Python-Standardbibliothekswrapper hatte PID `2458693`, der gestartete pnpm-Prozess PID `2458694`. Der Wrapper wartete auf den Testprozess. Ergebnis: Exit 0; eine Testdatei und 13 Tests bestanden, Vitest v5.0.3. Der konkrete Ausgabemitschnitt liegt unter `outputs/loop/policy-profile/targeted-vitest.log`; Aufruf, Zeitpunkte, PIDs und Exitcode liegen unter `targeted-vitest-run.json` im selben Ordner. Der Aufruf verwendete `--watch=false` und beendete sich regulär. Ich habe keinen Server oder eigenen Hintergrunddienst gestartet, keinen fremden Prozess gesteuert und nichts installiert.

Zusätzliche kurze Python-Prozesse führten ausschließlich lokale Hash-/Evidenzarbeiten für diesen Auftrag aus. Der Vorab-Pinprozess PID `2441052` endete mit Exit 0. Die anschließende Hashkontrolle endete ebenfalls mit Exit 0. Es gab keine Datenanalyse oder Python-Ausführung der Rechenbibliothek.

Vorher-/Nachher-Pins liegen in `outputs/loop/policy-profile/pins-before.json` und `pins-after-code.json`. Alle zwölf vorher gepinnten Dateien waren nach dem Testlauf bytegleich. Darunter befinden sich die Arbeitsgrundlagen, die bestehenden Testkonventionen und die folgenden ausdrücklich geschützten Dateien:

| Geschützte Datei | Unveränderter SHA-256 |
| --- | --- |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/tests/test_policy_reference_v2.py` | `01ddfaa79b3fedf1cc10d79b547a38622827fa218a29bd921f896e39568d5ad8` |
| `reports/loop/authors/BREADTH-TOPICS-001-first.md` | `f9dfe17df6795d0a7b82918c5d956421645249036e3ee22257a88a1044d58f5b` |
| `reports/loop/authors/POLICY-REFERENCE-V2-WIP.md` | `32bb7cc12e0f4f9437e80e7d2fe9ad6aff26a7ab95b3f14b957a06c9111c910a` |
| `reports/loop/authors/POLICY-REFERENCE-V2-round1-WIP.md` | `97b90a494440388afb322bc11b6f53e84668ee1265317d67ea8dd6822ceb493e` |

Ein voller `pnpm check`, ein gesonderter Gesamt-Typecheck, ein Build-/Browseraudit und wissenschaftliche Prüfungen wurden nicht ausgeführt: Der delegierte Auftrag erlaubte gezielt bestehende Vitest-Testläufe und beschränkte die Dateiarbeit. Die sichtbare Produktoberfläche und die gemeinsame Frontendstruktur wurden nicht geändert. Root kann diese Erstfassung getrennt prüfen und gegebenenfalls in einen eigenen Vorbereitungsplan aufnehmen. Fragenverständnis, Originalkategorien, Quellenbegründung, Breitenentscheidung, Referenzschema und finale Designzustimmung bleiben externe offene Aufgaben.
