# BREADTH-BINDING-003 — Neun Originalfragen und deklarierte Codelisten

Eng begrenzter Quellenbinding-Folgeauftrag, 3. Oktober 2026. Alle neun angeforderten Felder sind an konkrete öffentliche Dateikataloge, aktuelle Variablenmetadaten und deutsche Originalfragen gebunden. Das ist eine Quellenfeststellung, keine Item-, Modell-, Nutzungs-, UI- oder Empirieabnahme. Das bestehende Neunermodell und frühere Vorschläge wurden nicht verändert oder neu bewertet.

`BREADTH-DATA-001-first.md` und `BREADTH-ACCESS-002.md` bleiben bytegleich. Ihre bekannten SHA256 sind `4f4634947a882e09b2e060920ca0816ebe20a28508ab8b69b4e95608fbe946ca` und `e5ac6bbbaec7c0b406afcc42ca0b654993a94245dd0c13128ab2379c517243b5`. Dieser neue Auftrag übernimmt keine Sperre des alten Planmanifests und rekonstruiert keine vollständige Ergebnisblindheit der früheren Arbeit.

## Quellen und Grenzen des Abrufs

Es wurden vier unauthentifizierte, ausschließlich lesende öffentliche Metadatenabfragen an `https://api.nsd.no/graphql` ausgeführt. Exakte Anfragekörper, Originalantwortbytes, URL, UTC, HTTP-Status und SHA256 stehen im [Quellenkatalog](../../../outputs/loop/breadth-binding-003/sourcecatalog.json). Alle vier lieferten HTTP200 ohne GraphQL-Fehler. Angefragt wurden keine Häufigkeiten, Antwortdaten, Verteilungen, Fallwerte oder Rohdatendownloads. Keine Rohdatei oder ihr Header, Authdaten, Cookies, Token, fremde Prüfer-/Ergebnisberichte, state/handoff-Dateien oder private Inputs wurden gelesen. Keine Kontakte, Installationen, Git-/pnpm-Aktionen oder Agents. `data/inventar.csv` wurde nicht benötigt und nicht gelesen.

Wiederverwendet wurden die bereits tatsächlich öffentlich abgerufenen deutschen Original-PDFs und eigene zulässige Metadaten. Die lokalen Originalbytes stimmen weiterhin mit ihren gesicherten Hashes überein:

| Original | Ursprünglicher tatsächlicher Abruf | Original-SHA256 |
| --- | --- | --- |
| [ESS11 DE Fragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf) | 03.10.2026 12:14:41.334719 UTC, HTTP200 | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| [ESS10 DE Papier-/Webdokument](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf) | 12:14:40.627299 UTC, HTTP200 | `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425` |
| [ESS10 englischer CAPI-Source, Alert06](https://europeansocialsurvey.org/sites/default/files/2023-05/ESS-Round-10-Source-Questionnaire_FINAL_Alert-06.pdf) — nur B30-Zusatz | 12:12:04.125063 UTC, HTTP200 | `ee6c967d2efbc47e0541c8ebc4ff01a6a156bea0028398aac4610ecd55abb67c` |

Aktuelle Studienmetadaten bestätigen ESS11 v226 und ESS10 v494. Die konkrete ESS11-Datei `ESS11e04_2` hat ID `242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef`, Metadatenversion 179, DOI `10.21338/ess11e04_2`. Für ESS10 wird ausdrücklich `ESS10SCe03_2` mit ID `178d1c16-db15-466e-b1a5-cea36109e089`, Metadatenversion 147, DOI `10.21338/ess10sce03_2` gebunden. Diese IDs sind Metadatenobjekte, keine Personenkennungen. Die aktuelle ESS10-Studienabfrage bestätigt denselben Dateistand wie der wiederverwendete eigene SC-Variablenkatalog. Der Face-to-face-Datensatz3.3 ersetzt die deutsche SC-Referenz nicht.

| Neuer Original-Metadatenbody | UTC, 03.10.2026 | SHA256 |
| --- | --- | --- |
| ESS11 aktueller Studien-/Dateikatalog | 12:52:44.263431, HTTP200 | `3f029f3d4759224f07a9a05b21f16ac2d13e1b29ef2b845aa056601283ea3c4d` |
| ESS10 aktueller Studien-/Dateikatalog | 12:52:44.230913, HTTP200 | `32b32cd5ac7b112f46d0978b44cfca34acf97489e2159a129c8aa26807571299` |
| ESS11 Variablenkatalog der Datei4.2 | 12:52:44.131781, HTTP200 | `0091d6206b33d4018ab2fc2891e2bf2e911a384e497d7b391631d9e19f707505` |
| Neun konkrete Variablen: Frage-/Kategorienmetadaten | 12:53:08.006366, HTTP200 | `220fcbe3063917c3ef81841c0331b57b2b969bbe4edfa5e3e1355f2e13d053d6` |

Diese Hashes identifizieren Metadatenantworten, keine CSV/SAV/DTA-Datei. Deutschland-Feldzeit/Modus aus dem eigenen öffentlichen Länderbeleg: ESS11,09.05.–21.12.2023, CAPI; ESS10,05.10.2021–04.01.2022, Papier/CAWI. Die ESS10-Originalbindung unten ist für die deutsche **Papierfassung** gesichert. Eine individuelle CAWI-Screenshot-/Routingbindung wurde hier nicht zusätzlich hergestellt. Auch tatsächliche Nichtfehlendheit der neun Felder in deutschen Fällen bleibt vor zulässigem Rohdatenzugang ungeprüft.

## Neun konkrete Bindungen

Der [9-Felder-Crosswalk](../../../outputs/loop/breadth-binding-003/nine-fields-crosswalk.json) enthält vollständigen deutschen Wortlaut, Einleitung, gedruckte Antwortoptionen, Listen-/Routingbeleg, Quellenhash, Dateiversion, Variablen-ID/Version und vollständige API-Codeliste mit `isMissing`. Zeilenumbrüche, Trennstriche und Kommaspacing wurden nur für die Lesbarkeit normalisiert. Die Originalnummern sind national; sie dürfen nicht durch englische Source-Nummern oder selbst erfundene Frage-IDs ersetzt werden.

„Maßnahme“, „Prinzip“ und „Wahrnehmung“ benennen hier nur, was die Frage verlangt. Ein allgemein geforderter staatlicher Verteilungsauftrag oder eine Zulassungsrichtung ist von einem benannten Gesetz beziehungsweise einer bestimmten Sanktion zu unterscheiden. Diese Zuordnung setzt keine Faktoren, Scores oder Itemauswahl fest. Keine der neun Fragen ist bloß eine Bestands-/Folgenwahrnehmung.

| Feld / deklarierte Antwortart | Deutsches Original und Kontext | Deutsche Anzeige gegenüber API-Exportcodes |
| --- | --- | --- |
| `gincdif`, ESS11 — **Prinzip** | B33, physische PDF-S.13, Liste13; staatliche Maßnahmen zur Verringerung der Einkommensunterschiede. Gemeinsame Zustimmungseinleitung, jede Aussage vorlesen. Allgemeiner Auftrag, kein benanntes Steuer-/Transferinstrument. | DE1–5: starke Zustimmung→starke Ablehnung,3 neutral;7 Verweigerung/8 DK. API dieselben Hauptcodes plus9 No answer. Deutsch „Staat“, API „government“: kein Anlass zu freier deutscher Neuformulierung. |
| `euftf`, ESS11 — **Prinzip / Integrationsrichtung** | B37, PDF14, Liste14. Einleitung stellt „Einigung soll weitergehen“ und „schon zu weit gegangen“ gegenüber; danach eigene Skalenposition. | DE00–10;0 zu weit,10 weitergehen;77/88Missing. API0–10 ohne führendeNull plus99 No answer. **9 ist hier ein gültiger Skalenpunkt**, kein allgemeines Missing. Die beiden Richtungsanker gehören zur Frage. |
| `eqparep`, ESS11 — **Maßnahme** | E19, PDF51, Liste64: Gesetz zur gleichen Verteilung der Bundestagssitze zwischen Frauen und Männern. Rechtliche Verpflichtung und nationaler Bundestag ausdrücklich enthalten. | DE1 sehr dafür,2 eher dafür,3 weder dafür noch dagegen,4 eher dagegen,5 sehr dagegen;7/8. API inhaltlich entsprechende Kategorien plus9 No answer; generisches „Parliament“ ersetzt den nationalen Wortlaut nicht. |
| `eqparlv`, ESS11 — **Maßnahme** | E20, PDF52, weiter Liste64: Gesetz über gleich lange bezahlte Elternzeit. **Einleitung:** Paar, beide Vollzeit, ungefähr gleicher Verdienst, neugeborenes Kind, beide mit Anspruch auf bezahlte Elternzeit. | Wie E19, API zusätzlich9 No answer. Die API-`question` allein lässt die gesamte Szenarioeinleitung weg; `preQuestion`/`filter` sind leer. API-Wortlaut allein ist daher keine vollständige Originalidentität. Kein Filter auf eigene Elternschaft im deutschen Block. |
| `freinsw`, ESS11 — **Maßnahme** | E21, PDF52, weiter Liste64: Kündigung von Mitarbeitenden wegen bei der Arbeit gegen Frauen gerichteter beleidigender Bemerkungen. Sanktion und Arbeitsplatzkontext beibehalten. | Wie E19, API zusätzlich9 No answer. Nicht durch eine Frage über Verbreitung von Sexismus oder allgemeine Meinungsfreiheit ersetzen. |
| `fineqpy`, ESS11 — **Maßnahme** | E22, PDF52, weiter Liste64: Geldstrafe für Unternehmen, wenn Männer für gleiche Arbeit besser bezahlt werden als Frauen. | Wie E19, API zusätzlich9 No answer. Gleiche Arbeit, Vergleichsrichtung und Geldstrafe sind Originalbedingungen; keine bloße Frage zur durchschnittlichen Lohnlücke. |
| `imsmetn`, ESS10 SC — **Prinzip / Zulassungspräferenz** | Papier A54, PDF7: Einleitung Zuwanderer derselben Volksgruppe oder ethnischen Gruppe wie die Mehrheit der Deutschen; anschließend wie vielen Deutschland das Leben hier erlauben soll. | DE vier Kästchen1 vielen,2 einigen,3 wenigen,4 niemandem; keine externe Listenanweisung im Papierblock. API gleiche vier Kategorien, zusätzlich7 Refusal/8 DK/9 No answer. Deutsch verwendet „Volksgruppe oder ethnische Gruppe“, API-Englisch „race or ethnic group“; keine freie Rückübersetzung. |
| `imdfetn`, ESS10 SC — **Prinzip / Zulassungspräferenz** | Papier A55, PDF7: Fortsetzung A54, nun andere Volksgruppe/ethnische Gruppe als die Mehrheit der Deutschen. Vier Optionen erneut gedruckt. | Papier1–4, API zusätzlich7/8/9. Elliptische Anschlussfrage benötigt den Zulassungskontext aus A54. Nicht als allein vollständige neue Frage aus dem API-Label kopieren. |
| `impcntr`, ESS10 SC — **Prinzip / Zulassungspräferenz** | Papier A56, PDF7: weitere Anschlussfrage zu Zuwanderern aus ärmeren Ländern außerhalb Europas; vier Optionen erneut gedruckt. | Papier1–4, API zusätzlich7/8/9. Herkunft/relative Armut gehören zur Bedingung; keine Originalfrage zum Asylverfahren oder individuellem Einkommen. Kein 6 Not applicable in diesen drei Codelisten. |

Die fünf ESS11-Fragen mit fünf Antwortstufen haben API-Missing 7/8/9; `euftf` hat stattdessen77/88/99. Dies ist eine Feldregel, keine global anwendbare Missingliste. Export-Noanswer ist eine deklarierte Datenkategorie; daraus folgt kein Auftrag, ein zusätzliches Webkästchen zu bauen. Die vier Gleichstellungsmaßnahmen teilen die Antwortliste, ihre Inhalte werden dadurch nicht identisch.

Das Interviewskript nennt bei den sechs ESS11-Feldern keine besondere Skip-/Filteranweisung im gelesenen Block. Es nennt die Listen13/14/64; separate Showcard-PDFs wurden in diesem Auftrag nicht heruntergeladen. Bei Papier A54–56 ist die Folge fortlaufendA54→A55→A56→A57 ohne dort gedruckten besonderen Filter. `API filter=null` ist keine zusätzliche Garantie, dass jede Frage jeder Person jedes Erhebungsarms gestellt wurde. Routingidentität außerhalb dieser Originalblöcke, Modusequivalenz und beobachtete deutsche Antworten bleiben offen.

| Feld | Variablen-Metadaten-ID / Version |
| --- | --- |
| `gincdif` | `41329d27-0f86-4b14-805c-5e41e62ca17a` /2 |
| `euftf` | `73d580d0-d947-43c0-8697-955308e5f774` /1 |
| `eqparep` | `e61ee38c-800f-449d-a232-5477b7510b6c` /6 |
| `eqparlv` | `aa51d9ae-6bea-4cc6-9208-d951a48338e2` /6 |
| `freinsw` | `c7b2e500-d64e-462f-a433-dda69d7b4c20` /6 |
| `fineqpy` | `4c9d0d92-71b4-4e02-82f6-e29e516b231a` /6 |
| `imsmetn` | `c79cfb20-c948-47ed-85a3-baa2f0b71ef9` /4 |
| `imdfetn` | `965b0ffd-239f-4ce6-8a93-52e5da9728ce` /4 |
| `impcntr` | `973ef0d9-dfce-46e3-8cd0-37f03d22350d` /4 |

## Kurzer Zusatz: B30 / `impdema` und Varianten

Dieser Zusatz betrifft keine Änderung der neun Felder oder der Auswahl. Er prüft nur die zusätzlich angefragte Quellenbindung. Der vorhandene englische ESS10-CAPI-Source, physische PDF-S.42–44, beschreibt `D28Order` mit fünf zufällig zuzuweisenden GruppenA–E und den jeweiligen Karten-/Hardchecks. Die FrageD28a–e fragt dasselbe „wichtigste von fünf“ Prinzipien, aber rotiert deren Antwortpositionen. Die **inhaltlichen Kategorien sind dieselben**, ihre numerischen Positionscodes sind es nicht:

| Order / Sourcefrage | Code1 | Code2 | Code3 | Code4 | Code5 |
| --- | --- | --- | --- | --- | --- |
| A /D28a | freie faire Wahlen | gleiche Behandlung vor Gericht | Schutz vor Armut | Referenden | Ansichten gewöhnlicher Menschen vor Elite |
| B /D28b | Ansichten gewöhnlicher Menschen vor Elite | freie faire Wahlen | gleiche Behandlung vor Gericht | Schutz vor Armut | Referenden |
| C /D28c | Referenden | Ansichten gewöhnlicher Menschen vor Elite | freie faire Wahlen | gleiche Behandlung vor Gericht | Schutz vor Armut |
| D /D28d | Schutz vor Armut | Referenden | Ansichten gewöhnlicher Menschen vor Elite | freie faire Wahlen | gleiche Behandlung vor Gericht |
| E /D28e | gleiche Behandlung vor Gericht | Schutz vor Armut | Referenden | Ansichten gewöhnlicher Menschen vor Elite | freie faire Wahlen |

Das deutsche **Papier B30, PDF13**, enthält genau die fünf Inhalte und Codefolge von Order A und verlangt ein Kästchen; die vorausgehende Anweisung sagt, die nächste Frage sei von allen zu beantworten. Im geöffneten SC-Dateikatalog gibt es unter den geprüften `impdem*`-/`D28Order`-Namen nur `impdema`, Metadaten-ID `0f40b66b-b728-4f11-aad6-9b8c59216804`, Version 2, Label „order A“. Seine bereits gesicherte API-Codeliste enthält1–5 sowie6 Not applicable und7/8/9 Missing. Diese deklarierten Missingcodes erklären keine tatsächlich beobachtete Variantenzuweisung.

Der englische CAPI-Source ist nicht die deutsche Self-completion-Form. Aus der dort geplanten Randomisierung werden weder fünf deutsche Papier-/Webvarianten noch tatsächliche Gruppenanteile behauptet. Die Papierform ist positiv anOrderA gebunden; CAWI-Form-/Zufallsbindung und tatsächliche Nichtanwendbarkeit wurden nicht unabhängig bestätigt. Deshalb löst diese Quellenpräzisierung die verbleibende Empirie-/Modusfrage nicht abschließend. [Belegextrakt](../../../outputs/loop/breadth-binding-003/b30-variant-source-check.json) speichert die Originalseiten42–44, Papierseite13 und den konkreten SC-Kataloganker; keine Frequenzen oder Antworten.

## Abschluss und nachgelagerter Zugang

Crosswalk-SHA256 `3c11c2bdc81c1ad5db521413747b8459acd3b363568d3cb008dd4a92cd718eae`; Quellenkatalog-SHA256 `74a644a7a9abb486e3aee9e29849ec4963a3a44a4bc30dc92f3122f2df33532b`; B30-Extrakt-SHA256 `73c3d7f6ab583009c0ac35516ac19cee3166ce9311a73d927640e39755b79acd`.

[Vorherbindung](../../../outputs/loop/breadth-binding-003/binding-before.json), [Nachherbindung](../../../outputs/loop/breadth-binding-003/binding-after.json) und [Artefakthashes](../../../outputs/loop/breadth-binding-003/artifact-hashes.json) sichern die beiden unveränderten früheren Berichte und die eigenen neuen Belege. Weitere ESS-Dateien könnten in einem getrennt autorisierten Schritt durch den Nutzer bereitgestellt werden; Zugriff und empirische Verwendung bleiben bis dahin gesperrt. Keine tatsächlichen Antworten, keine Modellprüfung, keine neue Methoden-/Rechte-/Nutzungsfreigabe, keine UI-Beobachtung. Dieser Auftrag bindet Quellenkontext und deklarierte Kategorien.
