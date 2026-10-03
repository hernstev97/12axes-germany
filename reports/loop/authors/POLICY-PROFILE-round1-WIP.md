POLICY-PROFILE — gezielte Korrekturrunde 1 zu PP-001, 2026-10-03

Autor: Codex-Unteragent `/root/breadth_topic_frame`. Root bleibt alleiniger Koordinator. Die Korrektur beschränkt sich auf die Array-Eingabegrenze der reinen In-Memory-Bibliothek. Bestehende 13 Tests und acht neue synthetische Regressionen bestehen: 21 Tests, eine Spec-Datei, Exit 0. Nach der ausdrücklich freigegebenen Formatierung derselben zwei Dateien bestand auch der abschließende gezielte Lauf mit Exit 0. Eine unabhängige Korrekturprüfung steht noch aus; keine Empirie-, Produkt- oder Releasefreigabe.

Arbeitsort: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Der Branchname `research/life-93-night-20261003` und die Sicherung der ursprünglichen Frontendfassung im Commit `88eb7db56f00101cf76d46019661076d15deed70` wurden von Root vorgegeben. Ich habe keinen Git-Befehl ausgeführt und belege hier nur die tatsächlich verglichenen Dateibytes. Die ursprünglichen beiden Frontendpins stimmten vor der ersten Änderung mit den Auftragspins überein.

Für diese Runde wurden ausschließlich der eigene Erstbericht `reports/loop/authors/POLICY-PROFILE-WIP.md`, der ausdrücklich freigegebene Reviewer-Erstbericht `reports/loop/reviews/POLICY-PROFILE-001-first.md` und die beiden Frontenddateien inhaltlich gelesen. Andere Urteile, historische Forschung, Studienantworten, neue Roh-/lokale Daten und Zugänge wurden nicht gelesen. Die übrigen geschützten Dateien wurden nur gehasht. Der bereits gelesene `unslop`-Skill wurde für diesen Bericht weiter angewendet. Alte Prüfskripte, Beweise, Berichte und Logs wurden nicht bearbeitet.

PP-001 beschrieb zwei konkrete Eingabewege: Ein eigener Kategorieniterator konnte abweichende oder trotz ungültiger Indizes erfundene Codes liefern; ein Kategoriegetter konnte beim Einlesen die noch nicht kopierte Quelle verändern. Der Erstbericht benannte außerdem den direkten Indexzugriff der äußeren Fragenliste als Anschlussstelle. Diese Korrektur behandelt alle drei Stellen über denselben begrenzten Eingabevertrag.

Die gewählte Regel lautet: Es werden ausschließlich eigene numerische Datenfelder von Index 0 bis zur eigenen Arraylänge gelesen. `passiveArray()` prüft zunächst `Array.isArray`, liest den Deskriptor des eigenen `length`-Datenfelds und verlangt für jeden Index einen eigenen Datenfelddeskriptor. Dessen `value` wird in ein neues eingefrorenes internes Array kopiert. Fehlende Indizes sowie Elementgetter und -setter werden abgewiesen, bevor ihre Werte gelesen oder ihre Funktionen aufgerufen werden. Die Kategorien werden danach nach denselben bisherigen Regeln auf unveränderte, nichtleere eindeutige Stringcodes geprüft; Frageobjekte und Quellen behalten ihre bisherige Strukturprüfung.

Iteratoren und sonstige eigene Array-Eigenschaften werden bewusst ignoriert, ohne sie zu lesen. Ein vorhandener eigener `Symbol.iterator` darf daher von den Standardwerten abweichen; er definiert weder eine Frage noch einen Kategoriecode für diese Bibliothek. Auch ein Getter für `Symbol.iterator` wird nicht ausgewertet. Dies ist die im Auftrag erlaubte Wahl, ausschließlich numerische passive eigene Datenfelder zu verwenden, statt jedes Array mit zusätzlichen Eigenschaften pauschal abzuweisen. Ein ungültiger numerischer Elementwert bleibt ungültig, unabhängig davon, was irgendein Iterator liefern könnte. Arrays mit geerbten statt eigenen Indexfeldern beziehungsweise Lücken bleiben ebenfalls ungültig.

Diese Regel gilt sowohl für die äußere Fragenliste als auch für jede Kategorienliste. Normale readonly-, eingefrorene und mutable Arrays mit dichten eigenen Datenfeldern bleiben zulässig. Die Rohcodes werden weder getrimmt noch verändert. Interne Iteration erfolgt nur noch auf dem neuen eigenen Datenarray, nicht auf einem übergebenen Kategorieniterator. Die öffentliche API, drei Antwortzustände, Navigation, getrennte Quellen, Unveränderlichkeit der Ausgaben, unabhängige Sessions und der explizite Referenzstatus `none` bleiben erhalten.

Die Grenze ist kein JavaScript-Sandboxvertrag. Proxies können beim Deskriptorzugriff Traps ausführen; beliebiger Aufrufercode und globale Änderungen an Standardprototypen oder Built-ins werden nicht isoliert. Es wurde kein solcher Schutz implementiert, geprüft oder versprochen. Die Regressionen setzen unveränderte globale Standardobjekte voraus und prüfen gezielt die übergebenen Arrayobjekte. Die Bibliothek bleibt ohne eigene IO-, Route-, Storage-, Auth-, Score- oder Faktoroperationen und enthält weiterhin keinen tatsächlichen Fragen- oder Referenzbestand.

Die acht neuen Regressionen prüfen konkrete Sollzustände:

- Ein Kategorienarray mit gültigen eigenen Indizes und einem Iterator für einen eingeschleusten anderen Code behält exakt die indizierten Codes. Der fremde Code wird von `answer()` abgewiesen, der vorherige Snapshot bleibt erhalten, die normale Antwort gelingt und der Iteratorzähler ist null.
- Ein Kategorienarray mit `null` an Index 0 bleibt ein Fehler, auch wenn sein Iterator einen gültigen Stringcode liefern würde. Dieser Iterator wird nullmal aufgerufen.
- Ein Kategoriegetter, der beim Lesen die Studienquelle verändern würde, wird abgewiesen. Getterzähler null; die ursprüngliche Quelle bleibt unverändert.
- Ein Getter am äußeren Fragenindex wird ebenso vor der Auswertung abgewiesen. Getterzähler null; auch hier keine Quellenmutation.
- Setter-only-Elemente in beiden Arrayebenen werden abgewiesen; Setterzähler null.
- Getter für `Symbol.iterator` auf beiden Ebenen werden nicht gelesen. Die Session enthält die erwarteten drei indizierten Fragen, eine normale Einzelantwort gelingt und der Zähler bleibt null.
- Dünne Kategorien- und Fragenarrays werden trotz bereitgestellter Iteratorersatzwerte abgewiesen; Iteratorzähler null.
- Eingefrorene normale readonly-Arrays bleiben verwendbar. Antworten, Navigation und Überspringen bleiben erhalten, während eine zweite Session vollständig unberührt und unabhängig bleibt.

Die 13 bestehenden Verhaltensprüfungen wurden inhaltlich erhalten. Die Ergänzung erfolgte in einem gesonderten `describe`-Block; die anschließende Formatierung durfte den gesamten Text der beiden Frontenddateien formatieren. Die Testdaten sind ausschließlich synthetisch. Keine Originalfragen, Studienantworten, Referenzanteile, Polungen oder empirischen Aussagen wurden ergänzt. Der Reviewer-Erstbericht und dessen ursprüngliche Bewertung wurden nicht umgeschrieben; seine getrennten Node-Prüffälle wurden in dieser Runde nicht ausgeführt.

Die tatsächlichen beendeten Läufe waren:

| Lauf | UTC-Beginn bis UTC-Ende | Wrapper-PID / Kind-PID | Ergebnis |
| --- | --- | --- | --- |
| Gezieltes Vitest vor Formatierung | `2026-10-03T13:10:46.289742+00:00` bis `2026-10-03T13:10:49.322257+00:00` | `2589612` / `2589613` | Exit 0, 21/21 Tests, eine Datei |
| Prettier auf exakt zwei Dateien | `2026-10-03T13:10:59.194280+00:00` bis `2026-10-03T13:10:59.919039+00:00` | `2591162` / `2591163` | Exit 0 |
| Gezieltes Vitest der formatierten Fassung | `2026-10-03T13:11:06.555166+00:00` bis `2026-10-03T13:11:09.291817+00:00` | `2592232` / `2592237` | Exit 0, 21/21 Tests, eine Datei |

Die Testaufrufe waren jeweils exakt:

```text
pnpm --dir web test --watch=false --include=src/app/research/policy-profile.spec.ts
```

Der ausdrücklich autorisierte Formatieraufruf war exakt:

```text
pnpm exec prettier --write web/src/app/research/policy-profile.ts web/src/app/research/policy-profile.spec.ts
```

Vitest meldete Version 5.0.3. Beide Testläufe liefen mit `--watch=false`. Alle drei Kindprozesse wurden durch ihre Wrapper vollständig abgewartet; die Tool-Sessions endeten mit Exit 0. Es wurde kein Server oder eigener Hintergrunddienst gestartet und kein fremder Prozess gesteuert. Aufrufe, UTC-Marker, PIDs, Exitcodes und Ausgaben liegen ausschließlich unter `outputs/loop/policy-profile-round1/` in den Dateien `targeted-vitest-before-format-run.json`/`.log`, `prettier-exact-files-run.json`/`.log` und `targeted-vitest-final-run.json`/`.log`. Der Formatierbeleg enthält auch die Codehashes unmittelbar davor und danach.

Der Vorab-Pinprozess hatte PID `2579989`, Zeitmarker `2026-10-03T13:09:23.568089+00:00`, Exit 0. Die Nachher-Codekontrolle hatte PID `2595920`, Zeitmarker `2026-10-03T13:11:36.303252+00:00`, Exit 0. Diese kurzen Python-Prozesse dienten nur Hash-/Evidenzarbeiten und der Prozesssteuerung der ausdrücklich erlaubten Befehle. Es gab keinen Python-Studienlauf oder Datenimport.

Die beiden autorisiert geänderten Frontenddateien haben folgende Pins:

| Datei | Vorher | Nach Korrektur und Formatierung |
| --- | --- | --- |
| `web/src/app/research/policy-profile.ts` | `70f8b5db3bf055bb5b2ef26174f060591c9b98010b5fd1de6e101aafbd151f54` | `28906eb1533bb953b43bed75a4995c907b71398f1ffcd63271c82cfdace05998` |
| `web/src/app/research/policy-profile.spec.ts` | `0592b02f76c9d8caf92b2763787f83c9f2c72b42508d1939591023c2aadea5f5` | `6b2b3302afe308f28f65ec9aba76c7f1b8b6d14bf9ffa9b8fbc6508f9a1c22c1` |

Die ausdrücklich geschützten Erstberichte und Python-/Adapterdateien blieben bytegleich:

| Datei | Unveränderter SHA-256 |
| --- | --- |
| `reports/loop/authors/POLICY-PROFILE-WIP.md` | `f9c6e925472ef89e1cb74f3208b3954aa52a330bd464a5ba2bb8b137757f175f` |
| `reports/loop/reviews/POLICY-PROFILE-001-first.md` | `bbc62b4ff955d92f264c63eea2f2d33370864f447495d7117b92cfc6db960b2f` |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/tests/test_policy_reference_v2.py` | `01ddfaa79b3fedf1cc10d79b547a38622827fa218a29bd921f896e39568d5ad8` |
| `pipeline/policy_adapter_v2.py` | `3159243bc6f536359c896e414e8f418955b51e7504e38f3add62a811b0e5500e` |
| `pipeline/tests/test_policy_adapter_v2.py` | `43759f87d216d5c0f1c1ae28db60cf640b680f09913a56c8b0cd0c126ce5f829` |

Auch die zusätzlich gepinnten eigenen historischen Berichte `BREADTH-TOPICS-001-first.md`, `POLICY-REFERENCE-V2-WIP.md`, `POLICY-REFERENCE-V2-round1-WIP.md` und `POLICY-ADAPTER-WIP.md` blieben unverändert. Vorher-/Nachher-Belege sind `pins-before.json` und `pins-after-code.json` im eigenen neuen Outputordner. Der abschließende Beleg ergänzt diesen Bericht und die endgültigen Codepins, ohne alte Evidenz zu überschreiben.

Es gab keine Netz-, Auth-, Claude-, Git-, Installations-, Server- oder Agentenaktion und keinen vollständigen Repositorycheck. UI, Quellenbindung, Originalkategorien, Fragenverständnis, fachliche Breite, Referenzschema, tatsächliche Studiendaten und finale Designzustimmung wurden nicht bearbeitet oder freigegeben. Root erstellt das neue Manifest und beauftragt die gezielte unabhängige Nachprüfung von PP-001. Die eigenen synthetischen Regressionen begründen die technische Korrektur für den dokumentierten Arrayvertrag; sie ersetzen weder diese Nachprüfung noch wissenschaftliche Validierung. Autor und Erstprüfer gehören derselben Codex-Modellfamilie an, mit möglichen gemeinsamen Fehlerquellen.
