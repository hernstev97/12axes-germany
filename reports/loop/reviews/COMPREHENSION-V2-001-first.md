# COMPREHENSION-V2-001: frische begrenzte Erstprüfung

Urteil: **ACCEPTED_BOUNDED**

Geprüft am 3. Oktober 2026 durch Codex. Gegenstand ist der Planentwurf `docs/verstaendnistest-v2.entwurf.md` für eine qualitative Runde mit fünf realen Personen und sechs festen Fragen. Das Urteil nimmt nur dieses normale inhaltliche Paket in dem hier beschriebenen Umfang an. Es bestätigt keine Verständlichkeit bei Menschen, keine empirische Eignung, Neutralität, Administration, UI, Erhebung, Veröffentlichung oder Releasefreigabe. Root liest diesen Erstbericht und entscheidet anschließend.

## Eingaben und tatsächliche Bytes

Arbeitsverzeichnis: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Branchbezeichnung `research/life-93-night-20261003` ausschließlich laut Auftrag; kein Git-Aufruf zur Verifikation.

Fachliche Eingaben waren ausschließlich `reports/loop/packages/COMPREHENSION-V2-001/v1/manifest.json` und dessen sieben öffentliche Artefakte. Manifest: 1.253 Bytes, SHA256 `ac438ad0d4e6285fca89714b1d05792e45a59f410bf35d07a96896cc34025017`.

| Artefakt | Tatsächliche Bytes | SHA256, mit Manifest identisch |
| --- | ---: | --- |
| `docs/verstaendnistest-v2.entwurf.md` | 18.948 | `deaf970f15970f3bd68a3bd0494c5a304e611c491a79950ddfaa642e95e85a68` |
| `docs/verstaendnistest.entwurf.md` | 7.330 | `3264a72db722ac573595bcbcc8a03e299727aaa184abe6b31a60c74e2212c1a3` |
| `docs/handbuch.md` | 36.004 | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |
| `docs/auftrag-life-93-breite-2026-10-03.md` | 5.497 | `d0a059efb9de65aec1be25b3c2d5fac3bcb61cb57b0d7af8e7d8f64ecb1fd5ed` |
| `data/politikprofil-v2.fragen.entwurf.json` | 389.900 | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `data/analysevertrag.v2.entwurf.json` | 44.741 | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| `pipeline/policy_export_v2.py` | 24.107 | `27b225b5975f0c321f08adbfa7ccab4e03dae8421f3987d0e104cf4945d0437a` |

Alle Artefakte wurden vollständig byte-gehasht. Die beiden JSON-Pins wurden vollständig geparst; der Katalog wurde fachlich gezielt auf Zustände, Originalkategorien, Kontext, Studienbindung und offene Administration geprüft. Das ist keine vollständige Neuauditierung seiner Quellen. Verlinkte Quellen, Caches und weitere Forschungsdateien wurden nicht geöffnet. Kein anderer Reviewerbericht, keine Root-Verteidigung, keine Elternhistorie oder Zustands-/Autorenberichte wurden herangezogen. Kein weiterer Prüfagent wurde beteiligt.

Eine Abweichung von der ausschließlichen Dateileseliste ist offenzulegen: Zusätzlich wurde der verfahrensbezogene Skill `/home/stevenh/projects/12axes-germany/.agents/skills/unslop/SKILL.md` für die Berichtssprache gelesen. Er ist keine fachliche Beleggrundlage. Der erste Versuch mit einem anderen Skillpfad scheiterte; Details stehen unter Prüfversuche.

## Inhaltliche Befunde

Keine erheblichen Fehler im geprüften Planentwurf festgestellt. Die folgenden IDs bezeichnen konkrete Prüfgegenstände, keine empirisch bestandenen Tests. Zeilenangaben beziehen sich auf die oben gepinnten Bytes.

| ID | Befund und Fundstelle |
| --- | --- |
| C01 | Fünf reale Personen, sechs unveränderte Fragen F1–F6, feste Reihenfolge, keine KI-Personen als Ersatz: v2-Plan Z. 7–9, 23–31, 35–40. Unterschiedliche Lese-/digitale Erfahrungen sind ein Auswahlziel, keine Zufallsstichprobe oder politische Quotierung. |
| C02 | F1 trennt gewählte Originalkategorie, Themenordnung und berechnete gemeinsame Messdimension. Geordnete Originalantworten behalten ihre Bedeutung; Codes werden nicht zu zusätzlichen Punkten. M1/M2 erfassen die konkreten Fehlannahmen: Z. 7, 35, 54–55. Der Analysevertrag nennt `separate_categorical_responses`; Themen werden dadurch nicht zu Messdimensionen. |
| C03 | F2 verlangt Frage, historische Studie/Edition und Erhebungszeit. Der gültige Nenner ist ausdrücklich die Summe der Primärgewichte der gültigen Antworten der getrennten deutschen Studienbasis. Missing und tatsächlich nicht gestellte Angaben gehören nicht hinein; die lokale Markierung verändert die Referenz nicht: Z. 36, H1/H2 Z. 56–57. Im Exportpin entspricht `proportion` dem Kategoriegewicht geteilt durch `accounting.valid_weight`, Z. 238–245. Primärgewicht im Vertrag und Export ist `pspwght`. |
| C04 | F3 und S1–S3 unterscheiden unberührt, lokalen Skip, ausdrücklich gewählte Kategorie, historische Missing-Gründe, unklassifizierte Leerstelle und fehlende Referenz: Z. 37, 58–60. Es gibt keinen Mittelwert-/Nullersatz. Fehlende Referenz bedeutet weder null Prozent noch Löschung der eigenen Auswahl. Alle 43 Katalog-/Vertragslisten haben leere Nicht-gestellt-Codelisten; der Plan behauptet keine beobachteten Routingfälle. `vteurmmb` Code 65 bleibt die gültige Originaloption „Nicht stimmberechtigt“, Z. 81. |
| C05 | F4 verbietet aktuelle Bevölkerungsnorm, gemeinsame latente Position und Parteimatch. Fehlende Intervalle bedeuten keine Fehlerfreiheit; Gewichtssensitivitäten sind keine persönliche Unsicherheit oder Konfidenzintervalle: Z. 38, U1/U2/P1 Z. 61–63. Der Export setzt `uncertainty` auf `None`, Z. 435. Der Plan erklärt auch, dass die Anzeigeheuristiken keine Präzisions-/Anonymitätsgarantie sind und ESS8 München nicht vollständig abdeckt, Z. 81. |
| C06 | Version, Erläuterungen, Gerätebreite, Lesefassung, Beispielzustände und tatsächliche Referenzpins müssen vor der ersten Person gebunden werden: Z. 13–19. Die technische Zustandsvorführung ist deterministisch und verwendet nur gültige Originalkategorien. Für F2 reicht sie ausdrücklich nicht. Mindestens eine separat freigegebene historische Referenz sowie die übrigen Fallarten sind Voraussetzung der vollständigen Runde. Gleiche Version und gleiches Vorführskript gelten für alle, Z. 25. |
| C07 | F1–F4 erhalten jeweils ein begründetes Urteil. Eigene Worte genügen; fehlende Kernpunkte werden nicht als verstanden ergänzt. Eine konkrete falsche Schlussfolgerung hat Vorrang vor zutreffenden Teilstücken. Teilweise, nicht einordenbare und fehlende Erklärungen bleiben getrennt, Z. 31, 42–48, 73. Unklare Codierungen bleiben bis zur getrennten begründeten Zweitbeurteilung offen. Es gibt keine Summe und keinen persönlichen Bestanden-Status, Z. 50. |
| C08 | Wiederkehrende Missverständnisse werden nach derselben konkreten Aussage bei mindestens zwei verschiedenen Personen gezählt. Bloß gleiche Kennungen oder wiederholte Aussagen derselben Person reichen nicht: Z. 69. Ein schweres Einzelmissverständnis verlangt dokumentierte Klärung; Mehrheitsmeinung hebt es nicht auf, Z. 71. F5/F6 werden einzeln geprüft, ohne Richtig/falsch- oder Punktwertung, Z. 39–40, 73. Politische Zustimmung ist kein Kriterium. |
| C09 | Einverständnis und freiwillige Teilnahme/Antworten sind vorgesehen. T1–T5 benötigen keine Zuordnungsliste; Namen, Kontakte, eigene politische Antworten, Parteipräferenzen, Aufzeichnungen und Gerätekennungen werden nicht geführt. Unaufgefordert genannte Identität oder politische Position wird ausgelassen; öffentliche Zitate brauchen gesonderte Entscheidung nach Einverständnis und Prüfung: Z. 23–27. Die Personen erklären das technische Beispiel, keinen eigenen politischen Antwortvektor. |
| C10 | Die qualitative Grenze ist korrekt: keine Verständlichkeitsquote, Skalenvalidierung, repräsentative Fairness oder Agentenvalidierung, Z. 9, 69, 73–75. B25-Nachlauf und neue Webadministration bleiben offen, Z. 19, 83. Die zwei offenen B25-Felder im Katalog und die getrennte historische/Website-Grenze im Analysevertrag werden nicht durch den Verständnistest erledigt. Menschliche UI-, Vorführ- und Durchführungsentscheidung bleibt bei Steven. |

Der aktuelle breite Auftrag hat Vorrang. Seine Z. 15–19 trennen Themen, Messmodelle und historische Studien; Z. 23 und 29 regeln begrenzte Paketprüfungen und offene menschliche Freigaben. Der historische Verständnistest beschreibt Dimensionen, Perzentile und Wählergruppen. Das ist keine zulässige v2-Ergebnisform; der v2-Plan ersetzt Fragen/Schlüssel und legt eine eigene technische Beispielregel fest, Z. 3, 17, 79. Ältere Handbuchbegriffe werden ausdrücklich begrenzt. Die ältere Zeichenfolge `boundaries.ClaudeAndHumans` im Analysevertrag begründet hier keine Claude-Voraussetzung. Der aktuelle breite Auftrag sagt „Keine weiteren Claude-Versuche“. Eine persönliche Statistikabnahme wird für die Planannahme nicht erfunden.

## Eigene Gegenfälle zur Anwendung der Regeln

Die folgenden Fälle sind ausschließlich synthetische Aussagen über Regeln. Sie sind keine Befragtenantworten, keine simulierten Personen und kein Nachweis tatsächlichen Verständnisses.

| ID | Gegenfall | Bewertung nach dem gepinnten Schlüssel |
| --- | --- | --- |
| SYN01 | Die Erklärung nennt die gewählte Kategorie, sagt aber, ihre Nummer sei ein berechneter Profilpunkt. | F1 konkrete Fehlinterpretation M1; der zutreffende Teil hebt den Fehler nicht auf. |
| SYN02 | Die Erklärung erkennt den historischen Zeitpunkt, erklärt aber alle Studienfälle einschließlich Missing zum gültigen Nenner. | F2 konkrete Fehlinterpretation H2. |
| SYN03 | Die Erklärung nennt nur Frage/Studie, lässt Gewichtung und Nenner offen und behauptet nichts Falsches. | F2 teilweise zutreffend. Fehlende Kernpunkte dürfen nicht ergänzt werden. |
| SYN04 | Die Erklärung setzt fehlende Referenz gleich null Prozent; alternativ setzt sie einen lokalen Skip gleich historisch nicht gestellt. | F3 konkrete Fehlinterpretation S2 beziehungsweise S3. |
| SYN05 | Die Erklärung behandelt einen Gewichtssensitivitätswert als persönliches Konfidenzintervall. | F4 konkrete Fehlinterpretation U2; als nicht ausgewiesene Sicherheit zusätzlich schwerer Einzelfall nach Z. 71. |
| SYN06 | Keine Erklärung zu F2. | Fehlende Antwort; weder Verständnis noch Missverständnis. Die Runde behält den Nenner fünf. |
| SYN07 | Eine Person wiederholt H2 mehrfach; zwei andere Aussagen unter H2 enthalten verschiedene falsche Annahmen. | Wiederholungen zählen nicht als weitere Personen. Gleiches H2 allein löst die Zwei-Personen-Regel nicht aus. |
| SYN08 | Ein einzelner begründeter Fairnesshinweis steht gegen vier „keine Auffälligkeit“-Angaben. | Einzelprüfung des Hinweises; keine Mehrheitsfreigabe oder Neutralitätsbehauptung. |

Die Regeln tragen diese Gegenfälle ohne Änderung des Schlüssels. Sie liefern keine Erhebungsbelege.

## Offene Durchführungsvoraussetzungen und optionale Redaktion

OFF01: Eine konkrete menschlich gebilligte UI und ein tatsächlich gebundenes Vorführskript sind in diesem Paket nicht enthalten. Der Plan legt die Zustandsregel, Fallabdeckung, Gleichbehandlung und spätere Bindung fest. Er wird durch dieses Ersturteil nicht zu einer unmittelbar durchführbaren UI-Prüfung. Vor der ersten Person müssen die konkrete Navigations-/Vorführfolge und alle sichtbaren Erläuterungen anhand Z. 13–25 feststehen.

OFF02: Kein tatsächlich freigegebener Referenzexport wurde in dieser Erstprüfung gelesen. F2 bleibt ohne eine solche Anzeige offen. Das ist im Entwurf ausdrücklich benannt und kein Grund, empirische Zahlen zu erfinden.

OFF03: B25-/Modus-/Quellennutzung, Personenauswahl, Einverständnis, Durchführung, Auswertung, eventuelle Wiederholung und Veröffentlichung bleiben offen. Keine dieser Entscheidungen wird durch Agentenübereinstimmung ersetzt. Unvollständige Erklärungen erlauben keinen nachträglichen Verständlichkeitsnachweis; sie sind sichtbar zu berichten und in einem offenen Befund zu begründen.

STIL01, optional: Für den späteren Teilnehmerwortlaut könnte „historische Prozentreferenz“ in F2 durch „Prozentangabe aus der damaligen Erhebung“ ersetzt werden. Der jetzige Begriff ist kein erheblicher inhaltlicher Fehler. Eine solche Änderung müsste vor der Runde Teil des festgeschriebenen Fragenstands sein.

STIL02, optional: Den umfangreichen Bewertungsschlüssel könnte die spätere Testleitung als Arbeitsblatt mit einzelnen Kernpunkten lesen. Zusätzliche Punkte oder ein persönlicher Gesamtscore wären damit nicht erlaubt. Das ist eine Darstellungspräferenz, keine geforderte Korrektur dieses Pakets.

## Prüfbelege, fehlgeschlagene Versuche und Grenzen

Eigene strukturelle Belege liegen unter `outputs/loop/comprehension-v2-001-review/first-review-structural.py` und `first-review-structural.json`. Lauf: Exit 0, `PASS_STRUCTURAL_ONLY`, 19 Prüfungen, keine fehlgeschlagene Assertion. Geprüft wurden unter anderem alle sieben Dateipins, 43 gleiche eindeutige Katalog-/Vertrags-IDs, sämtliche Kategorie-/Missing-/Nicht-gestellt-Listen, B1–B12-Kontext, offene B25-Bindungen, F1–F6 und die zehn Fehlerkennungen. Der Exportpin wurde statisch als Python geparst, ohne seine außerhalb des Pakets liegenden Abhängigkeiten zu importieren.

ATT-01: Der erste Skill-Leseversuch unter `/home/stevenh/.agents/skills/unslop/SKILL.md` scheiterte mit Exit 1 und `No such file or directory`. Danach wurde der katalogisierte oben offengelegte Verfahrensskill gelesen.

ATT-02: Die kombinierte Handbuch-/Exportausgabe wurde vom Werkzeug gekürzt, ursprünglicher Umfang 17.169 Tokens. Fehlende Handbuchzeilen 207–378 und Exportzeilen 1–171 wurden gezielt erneut ausgegeben; die anderen Bereiche waren bereits sichtbar.

ATT-03: Eine zu große Katalogausgabe wurde gekürzt, ursprünglicher Befehlsumfang 57.876 Tokens; auch die Orchestrierung kürzte. ATT-04: Eine weitere kombinierte Item-/Kontextausgabe wurde gekürzt, ursprünglicher Befehlsumfang 11.985 Tokens; auch hier kürzte die Orchestrierung. Diese Ausgaben gelten nicht als vollständig gelesene Detailbelege. Die fachlich benötigten Bereiche wurden gezielt nachgelesen, darunter Items 32–43, B25, Studienzeiten/-modi, Kategoriegruppen und alle B1–B12-Einleitungs-/Stem-Bindungen. Vollständige JSON-Prüfungen ergänzen dies; eine lückenlose erneute Quellenauthentifizierung wird nicht behauptet. Alle vier Versuche und ihre Grenzen bleiben im eigenen JSON-Prüfbeleg vermerkt.

Keine Rohdaten, CSV-Header, privaten Aggregate, Personenantworten, externen Dienste oder Kontakte wurden geöffnet oder genutzt. Keine Erhebung, Git-Operation, Installation oder gemeinsame Artefaktänderung. `pnpm check`, Pipeline-Lauf und Browserprüfung wurden wegen der ausdrücklich auf sieben Pins begrenzten Leseberechtigung nicht ausgeführt. Damit bleiben technische App-/Runtime-/Browserchecks ungeprüft; dieser Bericht gibt dafür keinen Ersatzbefund aus.

Geschrieben wurden ausschließlich dieser Erstbericht und die eigenen strukturellen Belege im erlaubten Ausgabeordner. Die sieben geprüften Pins wurden nicht verändert. Kein automatischer Annahme-, Publikations- oder Freigabeschritt folgt aus dem Urteil.
