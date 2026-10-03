# Reviewer 2: Politikwissenschaft und Deutschlandbezug

Abgeschlossener unabhängiger Erstbericht zum KI-Audit LIFE-93 vom 2026-10-03. Dieser Bericht ist ein KI-Audit, kein akademisches Peer Review und keine methodische Freigabe.

## Identität, Auftrag und Prüfzeit

- Reviewer: Codex, Rolle 2, politikwissenschaftliche Grundlage und Deutschlandbezug.
- Beginn: 2026-10-03, 00:13:57 UTC, entsprechend 02:13:57 Uhr in Berlin. Ende der inhaltlichen Prüfung: 00:18:43 UTC, entsprechend 02:18:43 Uhr in Berlin. Berichtserstellung und übergreifende technische Prüfung bis 00:21:12 UTC, entsprechend 02:21:12 Uhr in Berlin.
- Zugängliche Modellangabe im gemeinsamen Auftrag: GPT-6.1-Sol, Slug `gpt-6.1-sol`, Reasoning `ultra`. Ein unabhängiger API-Nachweis der konkreten Modellrevision liegt mir nicht vor. Interne Versionen und nicht zugängliche Anbietervorgaben sind unbekannt.
- Ich erhielt den gemeinsamen Prüfauftrag, das gesicherte Issue und dieselbe eingefrorene Forschungsfassung. Ich habe keine anderen Reviewerberichte, spätere Autorantworten oder Korrekturen gelesen und keine eigenen Subagents eingesetzt. Eine andere Modellfamilie wird durch diesen Lauf nicht nachgewiesen.
- Verfügbare Werkzeugklassen waren unter anderem lokale Shell-/Dateiwerkzeuge, Webrecherche, Bildbetrachtung, Browsersteuerung und Agentenkollaboration. Tatsächlich benutzt: `functions.exec`, `exec_command`, `web__run`, `view_image`, `clock__curr_time` und `apply_patch` ausschließlich für diesen Bericht. Python prüfte Hashes und lud öffentliche Dokumente; Poppler extrahierte und renderte PDF-Seiten. `unslop` und der PDF-Skill wurden gelesen und angewandt. Browsersteuerung und Connectoren wurden nicht benutzt.

Der Prüfgegenstand ist ausschließlich `reports/audit-recherche/ausgangsfassung/`. Öffentliche Originalquellen ergänzen die Gegenprüfung. ESS-Rohantworten, lokale Zwischendaten und Personenkennungen wurden nicht geöffnet. Es gab keine Antwortanalyse, keinen Split, keine Entblindung und keine Modellentscheidung.

## Eingabefassung und Hashprüfung

Basis laut Manifest: Commit `1a7b0c38f28e27219d59380c039f9bb0446a71dd`, Branch `research/life-93-methodology`. Issue-Stand: `updatedAt 2026-10-02T22:07:24.510Z`. Manifest angelegt am 2026-10-03 um 00:13:28 UTC.

Die eigene Prüfung verglich SHA-256 und Dateigröße aller 26 Snapshot-Dateien mit dem Manifest. Ergebnis: 26 Übereinstimmungen, keine Abweichung. Auch die drei gesicherten Audit-Eingaben stimmten mit ihren Manifest-Hashes überein. Um 00:18:43 UTC bestätigte eine erneute Prüfung die unveränderten SHA-256 aller 26 Snapshot-Dateien.

| Eingabe                          | SHA-256                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `ausgangsmanifest.json`          | `dab36982ce6aac113acc2f807611e8630b546ee451684d683a096e0b4fd23cd8` |
| `pruefauftrag-gemeinsam.md`      | `ef26517dc7dd02c9e626b991275375c73a464abf074f6178baff0576390b0f8f` |
| `issue-LIFE-93.md`               | `d25ba503af100f27ac1c81706b1bd7a2a69243c09c3ecc29d32f6e1d77a54364` |
| `issue-LIFE-93.json`             | `258718010829e9fa187ea3359f6c96c6fb63758788de1e7cb8d779d986817fa7` |
| Snapshot `docs/pruefregeln.md`   | `1b10d9d7aa46a0a4e8cbc6e25c80a2b046f1cf611ab62aed6321b24af6367c77` |
| Snapshot `docs/analyseplan.md`   | `d0e1579f2e6891f097548c1c48d7cfb10f4f6f3d1bf5c0f228c25ba696ae1560` |
| Snapshot `docs/belegregister.md` | `eebb44ad32f681c6afff5165a4d840eed7221d34a28d6b95a8c8d3917865994a` |
| Snapshot `docs/quellen.json`     | `d85f080d7be311877076d637b642ee201d4da7f6e1ae3de1e0f4c0d7a0b63c30` |

Reproduzierbarer Kern der Prüfung, ohne Zugriff auf Rohdaten:

```python
import hashlib, json
from pathlib import Path

root = Path("reports/audit-recherche")
manifest = json.loads((root / "ausgangsmanifest.json").read_text())
for name, expected in manifest["files"].items():
    path = root / "ausgangsfassung" / name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected["sha256"]
    assert path.stat().st_size == expected["bytes"]
for name, expected in manifest["auditInputFiles"].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
```

Vollständig inhaltlich gelesen wurden der gemeinsame Prüfauftrag und das Issue sowie im Snapshot `docs/project.md`, `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md`, `docs/quellen.json`, `docs/entscheidungen.md`, `docs/datenlage.md`, `docs/ki-protokoll.md`, `docs/reviews/README.md`, die beiden Phase-0-Berichte und die Platzhalter unter `model/` und `pipeline/`. Die übrigen Dateien waren Gegenstand der Hashprüfung, keiner fachlichen Vollprüfung.

## Tatsächlicher Forschungsstand

Es gibt keine vorgeschlagenen Dimensionen, keine Itemzuordnungen und keine freigegebenen Ergebnisinterpretationen. Das erklären `docs/project.md:32`, `docs/belegregister.md:3–18` und `model/README.md:3–5` übereinstimmend. Die Dateien `docs/erwartungsmodell.md`, `docs/themenabdeckung.md` und `data/inventar.csv` fehlen in der Ausgangsfassung. Das ist nachvollziehbar als noch ausstehende Arbeit dokumentiert, etwa in `docs/analyseplan.md:37` und `docs/project.md:36`.

Damit lässt sich keine vorhandene Dimension als zu breit, politisch einseitig oder empirisch untragfähig beanstanden. Ebenso wenig lässt sich eine Dimension bestätigen. Die nachfolgend geprüften Originalitems sind Beispiele für spätere Abgrenzungen, keine Auswahlvorschläge des Projekts und keine neue Dimensionenliste.

Die vorhandene Quellenliste enthält ESS-Dokumentation, Nutzungsbedingungen, eine Anbieterbeschreibung und methodische Literatur. Ein ausgearbeiteter politikwissenschaftlicher Bezugsrahmen ist darin noch nicht vorhanden. Die neue Literatur in diesem Bericht gehört zur unabhängigen Recherche dieses Reviewers; sie wird nicht nachträglich als vorhandene Grundlage des Autors ausgegeben.

## Selbst geprüfte öffentliche Quellen

Zugriff am 2026-10-03 zwischen 00:14 und 00:18 UTC. HTML-Seiten wurden im zugänglichen Abschnitt gelesen; sie sind keine unveränderlichen Ausgaben. Neue Downloads und Bilder liegen ausschließlich in `/tmp/life93-audit-reviewer-2/`.

| ID     | Originalquelle und Fundstelle                                                                                                                                                                                                                                                                                                                                                                                                       | Tatsächlicher Zugang und Grenze                                                                                                                                                                                                                                                               |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R2-Q01 | [Deutscher ESS11-Fragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), PDF-/gedruckte S. 7–8, 13–16, 51–54, 85 und 89; zusätzlich S. 4–6, 11–12 textuell                                                                                                                                                                                                         | Eigener Download, Hashgleichheit mit `ESS11-DE-QUESTIONNAIRE`; genannte Seiten mit Ausnahme der ausdrücklich nur textuellen Seiten gerendert und visuell gelesen. Kein vollständiges Frageninventar, kein vollständiger Filter-/Listenheft-Abgleich.                                          |
| R2-Q02 | Kriesi et al. 2006, [Globalization and the transformation of the national political space](https://onlinelibrary.wiley.com/doi/10.1111/j.1475-6765.2006.00644.x), DOI `10.1111/j.1475-6765.2006.00644.x`; HTML-Abschnitte „Abstract“, „Research design“, Deutschlandabschnitt zu Abbildungen 3a/3b und Schlussfolgerungen                                                                                                           | Zugängliche Volltextabschnitte selbst gelesen. Untersuchung des politischen Angebots und älterer Wahlkämpfe; kein Nachweis der Struktur deutscher individueller ESS11-Einstellungen.                                                                                                          |
| R2-Q03 | Caughey, O’Grady und Warshaw 2019, [Policy Ideology in European Mass Publics, 1981–2016](https://www.cambridge.org/core/journals/american-political-science-review/article/policy-ideology-in-european-mass-publics-19812016/EC5CCE297E0EE5CC108EB87C4240E4A9), DOI `10.1017/S0003055419000157`; „Abstract“, „Introduction“, „Survey data and issue domains“                                                                        | HTML-Volltextabschnitte gelesen. Aggregiertes, zeitübergreifendes Messmodell aus mehreren Befragungsprogrammen; keine Übernahme als individuelle ESS11-Testskala gerechtfertigt.                                                                                                              |
| R2-Q04 | Malka, Lelkes und Soto 2019, [Are Cultural and Economic Conservatism Positively Correlated?](https://www.colby.edu/wp-content/uploads/2019/06/Malka_et_al_2019.pdf), DOI `10.1017/S0007123417000072`; PDF-S. 1, 6, 13–16 / gedruckte S. 1045, 1050, 1057–1060                                                                                                                                                                       | PDF-Text im Webwerkzeug zugänglich; Abstract sowie Abschnitte zu politischem Engagement und bedingten Zusammenhängen gelesen. Eigener HTTP-Download scheiterte mit 403; daher kein lokaler PDF-Hash. Anhänge und Replikation nicht geprüft. WVS-Befunde sind kein ESS11-Deutschland-Ergebnis. |
| R2-Q05 | Schwartz, [A Proposal for Measuring Value Orientations across Nations](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS_core_questionnaire_human_values.pdf), Kapitel 7 der zugänglichen ESS-Kopie; „The Nature of Values“, „Correcting for Response Tendencies“, „Estimation of value orientation scores“; PDF-S. 4–5, 17, 30 / gedruckte S. 262–263, 275, 288                                                 | Eigener Download; Definition und Auswertungsabschnitte textuell gelesen, S. 17 und 30 visuell bestätigt. Die Kopie trägt keinen von mir gesicherten Veröffentlichungs-/Revisionsstand. Kein vollständiger Review aller darin berichteten Validierungsstudien.                                 |
| R2-Q06 | Alexander et al. 2026, [Measuring sexism and gender attitudes in Round 11 of the European Social Survey](https://www.cambridge.org/core/journals/european-political-science/article/measuring-sexism-and-gender-attitudes-in-round-11-of-the-european-social-survey/3D2ABF95726D5D098B539EBEB25A7806), DOI `10.1017/S1682098326100435`; „Abstract“, „The need for measures…“, „Challenges in measuring gender attitudes and sexism“ | Selbst gelesene HTML-Abschnitte des Beitrags des Entwicklungsteams, online 23.04.2026. Berichtet verschiedene Konstrukte, unipolare Sexismusskalen und Formatgrenzen. Ergänzende Validierungsstudien und Länderergebnisse nicht nachgeprüft.                                                  |
| R2-Q07 | [GLES Querschnitt 2021, Nachwahl, ZA7701](https://access.gesis.org/dbk/74259), Studienbeschreibung und Fragebogendokumentation, Fragebogenfassung 1.2 vom 12.05.2023, Bezug auf Datenversion 2.1.0; PDF-/gedruckte S. 111, 115, 121, `q40`, `q43`, `q48`                                                                                                                                                                            | Öffentliches Instrument, selbst heruntergeladen, textuell und visuell geprüft. Keine GLES-Rohdaten geöffnet. Datiertes Hilfsmittel für den Themenabgleich; kein vollständiger oder verbindlicher Katalog deutscher Politik.                                                                   |
| R2-Q08 | Fuchs und Klingemann 1990, [The Left-Right Schema](https://www.degruyterbrill.com/document/doi/10.1515/9783110882193.203/html), DOI `10.1515/9783110882193.203`, Buchkapitel S. 203–234                                                                                                                                                                                                                                             | Verlagsmetadaten geprüft. Volltext verlangt Authentifizierung und war nicht zugänglich. Deshalb nur konkret benannter weiterer Literaturbedarf, kein inhaltlich geprüfter Befund.                                                                                                             |

Weitere Suchtreffer, unter anderem zu Converse und Oesch/Rennwald, werden nicht als geprüfte Belege verwendet. Das [ESS11-Designpapier des Gender-Moduls](https://europeansocialsurvey.org/sites/default/files/2024-06/r11_gender_module_design_template_final.pdf) wurde heruntergeladen und sein Inhaltsverzeichnis gelesen, aber nicht als vollständig geprüfte Konstruktgrundlage benutzt.

| Eigener öffentlicher Download                 | Bytes     | SHA-256                                                            |
| --------------------------------------------- | --------- | ------------------------------------------------------------------ |
| `ESS11_questionnaires_DE.pdf`                 | 1.304.009 | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| `ESS_core_questionnaire_human_values.pdf`     | 411.213   | `b5aaa9e2f2acdb6de41efc1b9bbaa34285b89d65a5f935391b67c7b367e1bf39` |
| `ZA7701_cdb.pdf`                              | 2.105.742 | `3f8d75a0e230ce423dea2cb7979554198f083f6f7f32859e3d4bb61116a232b9` |
| `r11_gender_module_design_template_final.pdf` | 624.216   | `091bea628cec0b15a84f66204e06ca4136b0dd9c799b45fea2b51fb5f2cb52a7` |

## Ausgeführte Untersuchungen und Ergebnis

### Konkurrierende Erklärungen

Ich habe geprüft, ob die Ausgangsfassung bereits eine bestimmte Achsenzahl oder politische Theorie festlegt. Ergebnis: nein. P02 und R09 verlangen konkurrierende Erwartungen; die später notwendigen Literaturentscheidungen sind ausdrücklich offen.

Die selbst recherchierten Quellen liefern verschiedene mögliche Erwartungen, keine fertige Auswahl:

- Ein gemeinsamer Links-Rechts-Faktor ist eine prüfbare Konkurrenzhypothese aus dem Auftrag. R2-Q08 muss dafür noch inhaltlich geprüft werden. Die Selbstverortung auf einer Links-Rechts-Skala bleibt gemäß Auftrag eine externe Prüfvariable und ersetzt keine Itemdefinition.
- Wirtschaftliche und kulturelle Konflikte sind bei Kriesi et al. unterscheidbar. Die Daten betreffen Parteienwettbewerb. Die Deutschlanddarstellung bezieht sich auf 1976 und 1994–2002. Daraus lässt sich eine Erwartung ableiten, aber keine heutige Personenmessung. R2-Q02, „Research design“ und Abbildungen 3a/3b.
- Caughey et al. unterscheiden wirtschaftliche, gesellschaftliche und migrationsbezogene Bereiche; wirtschaftliche Forderungen werden außerdem nach ihrem Bezug zum bestehenden Politikstand getrennt. Das ist eine Alternative zu einer einzigen Achse. Ihre Gruppenschätzungen bestätigen keine individuellen Skalen dieses Projekts. R2-Q03, „Survey data and issue domains“.
- Malka et al. liefern Gegenbelege zur Annahme, kulturelle und wirtschaftliche Positionen müssten überall gleichgerichtet zusammenhängen. Kontext und politisches Engagement gehören zur Erklärung. Diese Befunde rechtfertigen weder eine erzwungene gemeinsame Achse noch die Annahme, beide Bereiche seien stets unabhängig. R2-Q04, S. 1045 und 1050.
- Schwartz beschreibt persönliche Wertprioritäten und deren Beziehungen. Das ist ein anderer Gegenstand als konkrete politische Forderungen. Er darf als eigener theoretischer Rahmen untersucht werden, aber nicht ohne zusätzlichen Beleg als Ersatz für ein politisches Gesamtprofil dienen. R2-Q05, „The Nature of Values“.

Auch eine geringe oder nur thematisch begrenzte gemeinsame Struktur muss ein zulässiges Ergebnis bleiben. Keine dieser Quellen verlangt zwölf Dimensionen. Das Projekt erlaubt bereits das Scheitern des Produktziels und den Ausschluss ungeeigneter Dimensionen, siehe B-OPEN-001 und R12.

### Inhaltliche Reichweite konkreter Originalfragen

Die folgende Tabelle prüft ausgewählte Quelleninhalte. Sie ist kein vollständiges Inventar und benennt keine vorgeschlagenen Projektdimensionen. Die Interpretationsgrenzen sind mein fachliches Urteil über die geprüften Wortlaute, keine empirischen Ergebnisse.

| Originalfundstelle in R2-Q01        | Tatsächlich angesprochener Inhalt                                                                 | Ohne weitere Evidenz nicht gedeckt                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| B33, S. 13                          | Staatliche Verringerung von Einkommensunterschieden                                               | Vollständige wirtschaftspolitische Orientierung                |
| B34–B36, S. 13                      | Einstellungen zu schwulen und lesbischen Menschen, einschließlich Adoption und persönlicher Scham | Allgemeiner gesellschaftlicher Liberalismus                    |
| B37, S. 14                          | Gewünschter Fortgang europäischer Einigung                                                        | Außenpolitisches Gesamtprofil                                  |
| B40–B42 gegenüber B43–B45, S. 15–16 | Zulassung von Zuwanderung gegenüber wahrgenommenen Folgen                                         | Gleichsetzung beider Inhalte; umfassende Migrationspolitik     |
| E19–E22 gegenüber E23–E28, S. 51–54 | Bestimmte Gesetze gegenüber unterschiedlichen geschlechtsbezogenen Vorstellungen                  | Eine ungeprüfte einheitliche Haltung oder politische Identität |
| H1/H2, S. 85/89                     | Ähnlichkeit zu Personenporträts mit Wertbezug                                                     | Direkte Zustimmung zu politischen Maßnahmen                    |

Ein weiterer bestätigter Quellenbefund betrifft den historischen Vergleich: B13/B14 nennen die Bundestagswahl September 2021 und getrennte Erst-/Zweitstimmen. B-ESS-005 ist in diesem Umfang durch meine Originalprüfung bestätigt. Das ist keine Bestätigung der noch offenen Variablenwahl, Nachkodierung oder Gruppenbildung. Der Snapshot begrenzt den Vergleich bereits korrekt auf berichtete Wahlentscheidungen und behauptet keine Parteiprogramme oder aktuellen Präferenzen, R16.

### Deutschlandbezogene Themenabdeckung

Die geplante Übersicht fehlt noch. Ich habe deshalb keine vollständige Abdeckung bestätigt und keine endgültige Lückenliste behauptet. Der Vergleich ausgewählter Instrumente zeigt aber, wie die Prüfung aussehen muss: Die GLES fragt ausdrücklich nach Steuern gegenüber Sozialleistungen und nach Klimapolitik, R2-Q07, `q40` und `q48`. Ein Einkommensgleichheitsitem oder ein persönlicher Wert mit Umweltbezug deckt solche Forderungen nicht automatisch ab. Das ist eine Prüfanforderung, kein Beleg, dass sämtliche entsprechenden ESS11-Inhalte bereits ausgeschlossen oder vollständig durchsucht wurden.

Die Übersicht braucht eine begründete Themenquelle mit Datum, dann für jedes Thema die Unterscheidung zwischen ESS-Angebot, eigener Auswahl und zulässiger Aussage. Eine Wahlstudie allein definiert weder alle gesellschaftlichen Streitfragen noch deren normative Wichtigkeit. Aktuelle Themenwichtigkeit und die für historische Vergleiche relevante Themenabdeckung sind getrennt zu dokumentieren. Für weitere Bereiche, etwa konkrete Sicherheits-, Außen-, Wohnungs- oder Digitalpolitik, bleibt eine fachlich belegte Prüfung offen; diese Beispiele sind zusätzliche Recherchefragen, keine festgelegten Dimensionen.

## Findings

### R2-F01: Politischer Bezugsrahmen und konkurrierende Erwartungen stehen noch aus

- Betroffener Gegenstand: Snapshot `docs/analyseplan.md:37`, P02; `docs/pruefregeln.md:30`, R09; `docs/belegregister.md:47–49`, B-DEC-002 und B-OPEN-001. Im Issue: Phase 1, Zeilen 117–120.
- Status: **Spätere Anforderung.** Die Dokumente geben diesen Schritt selbst als offen aus. Kein nachgewiesener Fehler einer vorhandenen Dimension.
- Problem und Beleg: Ohne Themenübersicht und Erwartungsmodell ist noch nicht prüfbar, ob die spätere Auswahl theoretisch begründet, deutschlandbezogen und gegenüber Alternativen vertretbar ist. Die drei dafür vorgesehenen Dateien fehlen im Snapshot. Reproduzierbar mit `Path(...).exists()`; Ergebnis für `docs/erwartungsmodell.md`, `docs/themenabdeckung.md` und `data/inventar.csv` jeweils `False`. R2-Q02 bis R2-Q04 zeigen, dass unterschiedliche Untersuchungsebenen und Strukturerwartungen zu berücksichtigen sind.
- Schweregrad: **Mittel im gegenwärtigen Recherchepaket.** Die Lücke betrifft die Nachprüfbarkeit der späteren Modellwahl. Eine endgültige Item-/Modellentscheidung ist bereits durch P02/R09 und die offenen Abnahmen blockiert. Öffentliche Recherche kann weitergehen.
- Folge: Aus ESS-Herkunft oder später guter Modellgüte darf noch kein politisch umfassendes oder fachlich passendes Profil abgeleitet werden.
- Konkrete Korrektur: Den bereits geplanten Bezugsrahmen ausarbeiten. Je Ansatz Konstrukt, Untersuchungsebene, Deutschland-/Zeitbezug, erwartete Itemzuordnung, Gegenbefunde und prüfbare Alternative nennen. Quellen zum Parteienangebot und zur individuellen Einstellung getrennt ausweisen. Literatur darf auch eine begrenzte oder schwache Struktur erwarten lassen.
- Erneute Prüfung: Gegenprüfer prüft jede tragende theoretische Zuordnung an der Originalfundstelle und den Abgleich jedes Themas mit dem vollständigen ESS-Inventar. Keine Auswahlentscheidung allein aus den Beispielen dieses Berichts ableiten.

### R2-F02: Aufnahmeregel benötigt eine Abgrenzung verschiedener Arten von Einstellung

- Betroffener Gegenstand: Snapshot `docs/pruefregeln.md:28`, R07; `docs/analyseplan.md:37`, P02; Issue Zeile 116, Aufnahme und Ausschlüsse.
- Status: **Begründete Unsicherheit.** Die Regel ist vor endgültiger Anwendung noch nicht konkret genug für Grenzfälle. Es ist kein falsch aufgenommenes Item nachgewiesen.
- Problem und Beleg: „Einstellung zu einer politischen oder gesellschaftlichen Streitfrage oder zu einem Wert“ lässt offen, wie Positionsforderungen, wahrgenommene gesellschaftliche Verhältnisse, Institutionenvertrauen und Bewertungen bestehender Zustände unterschieden werden. R2-Q01 enthält diese verschiedenen Gegenstände. R2-Q06 unterscheidet im Gender-Modul ausdrücklich politische Forderungen, Wahrnehmungen und weitere Konstrukte. Solche Antworten können alle forschungsrelevant sein; sie messen deswegen nicht dasselbe.
- Schweregrad: **Mittel.** Die Unklarheit kann eine begrenzte Inhaltsaussage und spätere Zuordnung beeinträchtigen; aktuell gibt es noch keine davon abhängige Auswertung.
- Folge: Ein Faktor aus Bewertungen bestehender Verhältnisse könnte später irrtümlich als gewünschte Politik oder allgemeine Haltung erklärt werden. Der Ausschluss amtierender Regierungsbewertungen allein verhindert diese Verwechslung nicht.
- Konkrete Korrektur: Im Inventar pro Item den Antwortgegenstand und den Typ der Aussage erfassen. Vorab regeln, welche Typen Messitems, Kontext-/Prüfvariablen oder ausgeschlossen sind und wann verschiedene Typen gemeinsam ein Konstrukt tragen dürfen. Die Entscheidung verlangt eine Begründung; Wahrnehmungsitems sind nicht pauschal als „Wissen“ auszuschließen.
- Erneute Prüfung: Die getrennten Erstprüfer wenden die ergänzte Regel auf Grenzfälle und anschließend auf jedes inventarisierte Item an. Namens- und Ergebnisprüfung muss nachweisen, dass Forderungen, Wahrnehmungen und Bewertungen nicht unbemerkt gleichgesetzt werden.

### R2-F03: Konstruktbreite und Bedeutung beider Skalenenden müssen je Dimension belegt werden

- Betroffener Gegenstand: Snapshot `docs/pruefregeln.md:30,33,50`, R09/R12/R19; `docs/analyseplan.md:37,41`, P02/P06; Issue Zeilen 70, 129 und 132.
- Status: **Spätere Anforderung.** Die allgemeine Interpretationsregel ist richtig. Ihre Erfüllung lässt sich erst an tatsächlichen Itemgruppen und Texten prüfen.
- Problem und Beleg: Enge Themen tragen keine umfassende politische Orientierung. Auch ein niedriger Wert muss nicht die gegenteilige Haltung messen. Ein konkreter Gegenbeleg zur automatisch bipolaren Deutung steht in R2-Q06, „Challenges in measuring gender attitudes and sexism“: Die dort beschriebenen Sexismusskalen werden als unipolar erläutert. Das Fehlen der erfassten Einstellung beweist keine entgegenstehende Haltung. Die Quellenprüfung bestätigt damit die Notwendigkeit von R19; sie beweist noch keine Ungültigkeit einer Projektskala.
- Schweregrad: **Erheblich für eine davon abhängige Dimensions- oder Textfreigabe.** Eine unzutreffende breite Überschrift oder erfundene Gegenposition würde den Aussagegehalt des Ergebnisses verändern. Die gegenwärtige Recherche bleibt zulässig.
- Folge: Rechenpolung und technische Spiegelsymmetrie könnten sonst als Begründung einer inhaltlichen Gegenhaltung missverstanden werden. Ein Perzentil behebt dieses Problem nicht.
- Konkrete Korrektur: Jede spätere Dimension erhält eine Konstruktakte mit tatsächlichem Inhalt, ausgelassenen Teilaspekten, erlaubten und ausgeschlossenen Interpretationen. Ausdrücklich festhalten, ob sie bipolar oder unipolar verstanden wird und welche Evidenz die Skalenenden trägt. Gegebenenfalls die Überschrift enger fassen oder auf eine Dimension verzichten. Wissenschaftliche Konstruktnamen und nutzersichtbare Beschreibungen unterscheiden, ohne die wissenschaftliche Quelle zu beschönigen.
- Erneute Prüfung: Jede Überschrift, Polbeschreibung und Ergebnisdeutung wird gegen Wortlaute und Konstruktliteratur geprüft. Ein bloßer Faktorfit, eine Reliabilität oder Übereinstimmung zwischen KI-Urteilen zählt nicht als Bestätigung der Bedeutung. Bei unzureichender Evidenz bleibt die betroffene Freigabe offen.

### R2-F04: Persönliche Werte verlangen bei Aufnahme einen eigenen Interpretations- und Auswertungsvertrag

- Betroffener Gegenstand: Snapshot `docs/pruefregeln.md:28,39`, R07/R13; `docs/analyseplan.md:43`, P08; `docs/belegregister.md:48`, B-MODEL-001.
- Status: **Spätere Anforderung, bedingt durch eine Aufnahme von Portrait-Value-Items.** Noch ist kein solches Item ausgewählt. Die 0–1-Mittelung ist als eigene, noch ungeprüfte Annahme korrekt gekennzeichnet.
- Problem und Beleg: Die Zulassung von „Werten“ und eine allgemeine Mittelungsregel klären noch nicht, ob ein späterer Wertscore absolute Zustimmung oder relative Priorität ausdrücken soll. R2-Q05 erläutert in „Correcting for Response Tendencies“ und „Estimation of value orientation scores“ die Korrektur individueller Skalenverwendung und die Bedeutung relativer Prioritäten. Ein einfaches Maß darf nicht ohne Prüfung die Bedeutung einer anderen Auswertung übernehmen.
- Schweregrad: **Mittel.** Betroffen wären Scorebedeutung und Nachprüfbarkeit einer begrenzten Wertinterpretation; die Bedingung ist derzeit nicht eingetreten.
- Folge: Ein Werteprofil könnte sonst persönliche Antworttendenzen mit inhaltlichen Prioritäten verwechseln oder unbelegte politische Forderungen ableiten.
- Konkrete Korrektur: Bei geplanter Aufnahme die originale Konstrukt- und Auswertungsliteratur prüfen. Den beanspruchten Scoreinhalt festlegen und seine Vereinbarkeit mit der Produktvorgabe begründen. Alternativen, engere Aussagen oder Ausschluss offenlassen; keine Änderung der Rechenregel ohne den vorgesehenen Entscheidungsprozess.
- Erneute Prüfung: Fachliche Gegenprüfung des Auswertungsvertrags und später der tatsächlich implementierten Formel. Erst danach empirische Prüfung nach freigegebenem Plan. Bis dahin kein freigegebenes Wertprofil und keine politische Schlussfolgerung aus Portraitwerten.

## Grenzen und nächste erlaubte Arbeit

Ich habe weder die vollständige deutsche Themenabdeckung noch alle Originalfragen und Filter geprüft. Meine Literaturrecherche ist eine begründete Auswahl zentraler Ansätze und Gegenbelege, kein systematischer Review. Der Volltext zu Fuchs/Klingemann sowie weiterführende aktuelle Deutschlandstudien bleiben Literaturbedarf. Statistik, Lizenzen, Barrierefreiheit und technische Forschungszugriffssperren sind nicht Gegenstand dieses Rollenurteils. Kein ausstehender Prüfungsschritt wird hier als bestanden ausgewiesen.

Die überprüfte Ausgangsfassung stellt ihren vorläufigen Status glaubwürdig dar. Sie setzt keine feste Achsenzahl voraus und begrenzt historische Wählergruppenvergleiche angemessen. Ich finde in meinem Prüfbereich keine belegte falsche Dimension oder bereits überzogene Ergebnisinterpretation. Vier Findings benennen offene Konkretisierungen und spätere Anforderungen. Das ist keine Gesamtfreigabe.

Die nächste erlaubte Arbeit ist ein vollständiges öffentliches Frageninventar, ein datierter Deutschland-Themenrahmen und ein quellengestütztes Erwartungsmodell mit konkurrierenden Zuordnungen. Alle bisherigen Auswahl- und Analysegates bleiben bestehen. Dieser Bericht autorisiert keine endgültige Itemauswahl, ESS-Auswertung, Entblindung oder Veröffentlichung eines Tests.

## Technische Berichtskontrolle

Die eigene Berichtsdatei wurde mit `pnpm exec prettier --write reports/audit-recherche/reviewer-2-politikwissenschaft.md` formatiert. `pnpm check` wurde anschließend ausgeführt und endete mit Exitcode 1 bei `format:check`. Prettier meldete sieben andere Audit-Dateien: `00-eingangspruefung.json`, `01-eingang-wiederholbar.json`, `agent-protokoll.json`, `issue-LIFE-93.json`, `issue-LIFE-93.md`, `pruefauftrag-gemeinsam.md` und `werkzeuge.json`. Diese Dateien wurden nicht verändert. Typprüfung, Tests und Build wurden wegen der vorgeschalteten fehlgeschlagenen Formatprüfung nicht ausgeführt. Dieser technische Befund ist keine Aussage zur wissenschaftlichen Grundlage.
