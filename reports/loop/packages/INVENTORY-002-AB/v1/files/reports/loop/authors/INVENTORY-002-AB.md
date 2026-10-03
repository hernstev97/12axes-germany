# INVENTORY-002-AB: A-/B-Quellenannotation als Entwurf

Stand 2026-10-03. Abgegrenzter Quellen-/Inventarautor, kein Reviewer und keine endgültige Item-/Polungs-Erstbewertung. Modell laut Koordinator `gpt-6.1-sol`, Denkaufwand `ultra`, geerbt. Die genaue interne Modellrevision und Anbieterregeln sind unbekannt; der Autor konnte diese Angaben nicht unabhängig introspektieren.

Die [Ergänzung](../../../data/inventar-ab.ergaenzung.entwurf.json) führt alle 52 vorhandenen A-/B-Identitäten. Sie strukturiert Originalwortlaut, Interviewcodes und Labels, Missingoptionen, Einleitungen, gedruckte Filter, Weiterleitungen und öffentliche Codebook-Metadaten. Jede tragende Feldannotation verweist auf ein eigenes Belegregister in der JSON-Datei. Die 836 Belege enthalten Quellenhash, PDF-/gedruckte Fundstelle, Region in PDF-Punkten, konkrete Originaltokens und Extrakthash. Das ist Quellenarbeit im Entwurfsstatus. Unabhängige Prüfung und Phase-1-Abnahme sind `NICHT_GEPRÜFT`.

## Tatsächlicher Startauftrag im Wortlaut

```text
Du bist abgegrenzter öffentlicher Quellen-/Inventarautor für die nächste zulässige LIFE-93-Arbeit, kein Reviewer und keine endgültige Item-/Polungs-Erstbewertung. Worktree für alleShells /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Lies AGENTS/docs/project/Arbeitsloop/dauerhaftenAuftrag/Issue und ursprüngliches technischesInventar data/inventar.entwurf.csv/provenienz sowie pipeline/inventar.py alsBestand. KeinPeer/Jurorbericht/Loopfindings/Agentregister. Bestehende296Zeilen/205technischeRestzeilen, keineSemantik-Gesamtabnahme. Auftrag eng: alle tatsächlichen A- und B-Fragen/Unterfragen (derzeit6+46Zeilen) aus den offiziellen deutschen ESS11-Originalquellen strukturiert ergänzen: offizielleVariablenzuordnung, exakterWortlautverweis, Antwortcode+Label inklspecial/Missing, Einleitung/Filter/Weiterleitung undEinzelbelege mitQuelle/PDFgedruckteSeite/Region. NichtvorhandeneZuordnungoffenstattParaphrasezuVariableüberdehnen. DeutscheQ/Showcards undCodebook4.1liegengepinntunteroutputs/loop/inventory/; beiBedarfoffizielleöffentlicheESSsourceQuestionnaires/Metadatenbeschaffenerlaubt, keineAntwortdaten/PortalAnalysis/VariableVerteilungen/DownloadsangemeldeterDaten. VariablebezeichnungenfürWahl/LR dürfenalsFrageMetadatenzwecksInventar gelesenwerden,KEINEWerte/Verteilungen. Exakte KategorienumsetzungausOriginalseitenundListenkontextselbstlesen, wichtigeSeiten visuellprüfen(PDFSkill). Alle52Identitätenführen, vollständigunterstützteClaimsund konkreteRestfragenauseinanderhalten. NeueErgänzung ausschließlich data/inventar-ab.ergaenzung.entwurf.json, reports/loop/authors/INVENTORY-002-AB.md undownSources/Skripte/TestOutputs outputs/loop/inventory002-ab/. AktiveCSV/Provenienz/Parser/Tests/andereForschungsartefakte/Website/NachtzustandNICHTändern (laufendegefroreneAudits). DatenstrukturbezeichnetjeFeldOriginalbeleg/Quellenhash/Status, keineEndeignung/Polung/DimensionoderScoreentscheidung; keineeigeneAnnotationalsunabhängigbestanden. VorabplanundAbnahmekriterienvorArbeit: vollständige52IDs,lückenloseOriginalfundstellenfürallealsbelegtmarkiertenFelder,widersprechendeFilter/Codes erhalten, source/pipeline/prüfbareGegenprobenundexakteRestliste. ReproduzierbareeigeneLesetestsgegenOriginalextrakte, nichtImplementationsspiegel; keineempirischenTests nötig. VolltextkopiennurignoreOutputs, Dokumentationslizenz belegen/anbestehendgepinntenPrimärbelegbinden, keinRohdata/raw/local/A/Bantworten/Personen/Credentials/Cookies oderglobaleWrites/Conda/Installationen. Originaleunverändert; unterschiedlicheCodebook4.1vsRoh4.2nichtbytegleichbehaupten. QuellenIDs/Fundstellengegenbelege/tatsächlichLektüre/zeitlicheGeltung dokumentieren. Reportenthältvollen tatsächlichenStartauftrag,Modelgpt-6.1-sol/ultra geerbt internunknown,Tools/Commands/actualChecks/grenzen/Paketbeleglistefürnachfolgende2Reviewer. KeinefremdenUrteile/weitereAgents/CommitPush. KonkreteArtefakteerstellen, soweitvollständigbelegbarerBestand, keinefalscheVollständigkeit. AbschlussPfadeHashesRestumfang.
```

Der komplette Auftrag liegt zusätzlich unter `outputs/loop/inventory002-ab/startauftrag.txt`. Es wurden keine weiteren Agents gestartet, keine fremden Urteile gelesen und keine Commits oder Pushes ausgeführt. Globale Dateien und Einstellungen blieben unberührt.

## Vorabplan und Abnahmekriterien

Der Vorabplan wurde um `2026-10-03T04:48:40.668900+00:00` in `outputs/loop/inventory002-ab/plan-before-work.json` geschrieben, bevor die Ergänzung entstand. Die Eingabeshashes stehen daneben in `baseline-input-hashes.json`. Festgelegt waren genau alle 52 IDs, Originalquelle samt Hash und präziser Region je belegtem Feld, Erhaltung widersprechender Codes/Filter, reproduzierbare Quellenlesetests mit Gegenproben sowie eine konkrete Restliste. Der Plan versprach weder unabhängige semantische Abnahme noch Itemauswahl oder empirische Evidenz.

Gelesen wurden AGENTS.md, docs/project.md, docs/arbeitsloop.md, der dauerhafte Auftrag, LIFE-93, docs/pruefregeln.md, docs/analyseplan.md, docs/belegregister.md, docs/entscheidungen.md und docs/lizenzen.md. Der aktuelle gespeicherte Issue unter `reports/loop/issue-2026-10-03.md` wurde mit dem vollständig gelesenen Issue-Snapshot verglichen. Die beiden Issue-Texte sind nach `## Ziel` identisch; aktualisiert laut Snapshot `2026-10-02T22:07:24.510Z`. `issue-input-check.json` enthält den Dateihash. Das technische Inventar, seine Provenienz und der vollständige Parser wurden als Bestand gelesen. Keine Peer-/Jurorberichte, Loopfindings oder Agentregister wurden inhaltlich gelesen. Eine kurze Memory-Suche ergab keinen projektrelevanten Treffer; keine Erinnerung wurde als Beleg genutzt.

## Quellen und zeitliche Grenze

| Quellen-ID             | Offizielle Quelle                                                                                                                         | SHA-256                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| ESS11-DE-QUESTIONNAIRE | [ESS11_questionnaires_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf) | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| ESS11-DE-SHOWCARDS     | [ESS11_showcards_DE.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf)           | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| ESS11-CODEBOOK         | [ESS11_appendix_a7_e04_1.pdf](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf)            | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |
| ESS-CONDITIONS-OF-USE  | [ess-disclaimer.html](https://www.europeansocialsurvey.org/contact/disclaimer)                                                            | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` |

Die drei PDFs waren bereits am 2026-10-03 um 01:16 UTC vom offiziellen ESS-Blob bezogen worden. Der ursprüngliche Downloadnachweis `outputs/loop/inventory/downloads.json` nennt jeweils genaue UTC-Zeit, HTTP 200 und Hash. Der Lizenzpin führt zusätzlich den gesicherten Zugriff `2026-10-03T01:45:13.074558+00:00`. Dieser Autor hat die vorhandenen Pins lokal neu gelesen und gehasht. Er hat keine neue Netzabfrage, keinen Portal-Analysebefehl und keinen Download angemeldeter Daten ausgeführt.

Die lokalen Originalfundstellen sind Fragebogen PDF-/gedruckte S. 3–16, Listenheft PDF-S. 2–20, LISTE 1–19, und Codebook PDF-S. 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 21, 22, 38, 39, 40, 45, 46, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, gedruckt 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 20, 21, 37, 38, 39, 44, 45, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67 of 551. Das Listenheft trägt keine gedruckte Seitennummer; die JSON bezeichnet die Liste als gedruckten Locator und lässt `gedruckte_seite` null. Der allein für die Reihenfolge belegte Übergang von B45 zu C1 nutzt Fragebogen PDF-/gedruckte S. 17; C1-Antworten sind nicht Bestandteil der Ergänzung.

Die Quelle bleibt Codebook Ausgabe 4.1. Der Datenkandidat 4.2 wurde weder geöffnet noch für diese Annotation geprüft. Die Ergänzung behauptet keine Bytegleichheit oder bereits bestätigte Datenkodierung zwischen 4.1 und 4.2.

## Inhalt und belegte Grenzen

Wortlaut-Locator des bestehenden Inventars wurden als Kandidaten übernommen und mit einer frischen Originalextraktion token- und positionsgenau abgeglichen. Ausgegeben werden ausschließlich die verifizierten Originaltokens. Der Wortlaut behält deutsche Schreibweise, sichtbare Trennstriche, Zeilenumbrüche, Einleitungen im Item und Listendirektiven. Intervieweranweisungen und geerbte Gruppeneinleitungen stehen getrennt. Zum Beispiel bleibt bei B14a die Nachfrage zur Partei des Kandidaten als eigener Beleg erhalten.

Antwortcodes und Wortlabels stammen aus den gelesenen deutschen Originalzellen. Vertikale Beschriftungen werden mit ihrem tatsächlichen Code und möglichen Folgezeilen erfasst. Tabellenantworten nennen eigenen Zeilencode und geteilten Spaltenkopf. Numerische Zwischenstufen einer 0–10-Skala erhalten null als Wortlabel, weil das Original nur Zahlen zeigt. Führende Nullen der Interviewcodes bleiben erhalten. Die offene Stunden-/Minuteneingabe von A1/A3 wird nicht in erfundene Antwortkategorien oder Min-/Max-Grenzen gezwungen.

Die Listen wurden einzeln gelesen. Mehrere Listen-PDF-Seiten besitzen verschobene doppelte Textlagen, die in der Textextraktion zwei Kopien erzeugen, aber auf der gerenderten Karte eine Liste zeigen. Originalextrakte bleiben erhalten. `fragebogenkategorien_zum_kartenabgleich` bezeichnet ausdrücklich die Interviewbeschriftungen; daraus entsteht keine neue Kartenskala oder zusätzliche Missingoption. Die sichtbaren Karten wurden mit den Fragebogenlabels abgeglichen.

Offizielle Variablennamen und `Location` stammen aus den konkreten Codebook-Einträgen. Bei Sammel-Locations wie B6–12a, B15–18, B33–36 und B38–39 bleibt die Einzelzuordnung ein kenntlich gemachter Autorenabgleich von Originalinhalten. Die Ergänzung erfindet keine offizielle deutsche Crosswalk-Tabelle. Zwei Wahl-Unterfragen bleiben ausdrücklich offen: B14DE1/B14DE2 heißen im Codebook nur Germany1/2. Ein direkter Beleg für Erststimme/B14a → prtvgde1 und Zweitstimme/B14b → prtvgde2 ist in diesen Pins nicht enthalten. Die Variablen stehen deshalb als Kandidaten, das bestätigte Zuordnungsfeld bleibt leer.

Interview- und Codebook-Labels bleiben getrennte Felder. Bei B14a, B14b und B24 bedeutet Interviewcode09 „Andere Partei“. Das Codebook nennt dagegen 08 für dieBasis, 09 für Die PARTEI und 55 für Other. Die Ergänzung schreibt keinen stillen 1:1-Import oder fertige Rekodierung vor. B25 nennt im gedruckten Filter auch B24=08, obwohl die Antwortliste zu B24 keine08 druckt. Beide Originalbefunde stehen unverändert nebeneinander. Bei B13 bleibt „Nicht wahlberechtigt“ eine gedruckte inhaltliche Sonderantwort, getrennt von Verweigerung/Weiß nicht. Die Anweisung, einen ungültigen oder leeren Wahlzettel als Nein zu codieren, bleibt als Intervieweranweisung erhalten.

Das Codebook führt in diesen A-/B-Variableneinträgen keine Missingcode-Liste. Es gibt deshalb keine ergänzten „No answer“- oder „Not applicable“-Codes. Das Daten-Missingfeld bleibt für jede Identität offen. Die Fragebogen-Missingoptionen sind dagegen einzeln mit ihren Originalcodes belegt.

## Alle Identitäten

Die Zahl gültiger Interviewkategorien bezeichnet gedruckte Kategorien, keine Antwortdaten. A1/A3 sind offene Zeitfelder; dort ist die Zahl enumerierter Kategorien null.

| Inventar-ID | Offizielle Variable/Kandidat | Zuordnung       | Fragebogen PDF / gedruckt | Enumerierte Kategorien | Interview-Missingcodes |
| ----------- | ---------------------------- | --------------- | ------------------------- | ---------------------- | ---------------------- |
| A1          | nwspol                       | Autorenabgleich | 3 / 3                     | 0                      | 7777, 8888             |
| A2          | netusoft                     | Autorenabgleich | 3 / 3                     | 5                      | 7, 8                   |
| A3          | netustm                      | Autorenabgleich | 3 / 3                     | 0                      | 7777, 8888             |
| A4          | ppltrst                      | Autorenabgleich | 4 / 4                     | 11                     | 77, 88                 |
| A5          | pplfair                      | Autorenabgleich | 4 / 4                     | 11                     | 77, 88                 |
| A6          | pplhlp                       | Autorenabgleich | 4 / 4                     | 11                     | 77, 88                 |
| B1          | polintr                      | Autorenabgleich | 5 / 5                     | 4                      | 7, 8                   |
| B2          | psppsgva                     | Autorenabgleich | 5 / 5                     | 5                      | 7, 8                   |
| B3          | actrolga                     | Autorenabgleich | 5 / 5                     | 5                      | 7, 8                   |
| B4          | psppipla                     | Autorenabgleich | 6 / 6                     | 5                      | 7, 8                   |
| B5          | cptppola                     | Autorenabgleich | 6 / 6                     | 5                      | 7, 8                   |
| B6          | trstprl                      | Autorenabgleich | 7 / 7                     | 11                     | 77, 88                 |
| B7          | trstlgl                      | Autorenabgleich | 7 / 7                     | 11                     | 77, 88                 |
| B8          | trstplc                      | Autorenabgleich | 7 / 7                     | 11                     | 77, 88                 |
| B9          | trstplt                      | Autorenabgleich | 7 / 7                     | 11                     | 77, 88                 |
| B10         | trstprt                      | Autorenabgleich | 7 / 7                     | 11                     | 77, 88                 |
| B11         | trstep                       | Autorenabgleich | 7 / 7                     | 11                     | 77, 88                 |
| B12         | trstun                       | Autorenabgleich | 7 / 7                     | 11                     | 77, 88                 |
| B13         | vote                         | Autorenabgleich | 7 / 7                     | 3                      | 7, 8                   |
| B14a        | prtvgde1                     | offen; Kandidat | 8 / 8                     | 8                      | 77, 88                 |
| B14b        | prtvgde2                     | offen; Kandidat | 8 / 8                     | 8                      | 77, 88                 |
| B15         | contplt                      | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B16         | donprty                      | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B17         | badge                        | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B18         | sgnptit                      | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B19         | pbldmna                      | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B20         | bctprd                       | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B21         | pstplonl                     | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B22         | volunfp                      | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B23         | clsprty                      | Autorenabgleich | 9 / 9                     | 2                      | 7, 8                   |
| B24         | prtclgde                     | Autorenabgleich | 10 / 10                   | 8                      | 77, 88                 |
| B25         | prtdgcl                      | Autorenabgleich | 10 / 10                   | 4                      | 7, 8                   |
| B26         | lrscale                      | Autorenabgleich | 10 / 10                   | 11                     | 77, 88                 |
| B27         | stflife                      | Autorenabgleich | 11 / 11                   | 11                     | 77, 88                 |
| B28         | stfeco                       | Autorenabgleich | 11 / 11                   | 11                     | 77, 88                 |
| B29         | stfgov                       | Autorenabgleich | 11 / 11                   | 11                     | 77, 88                 |
| B30         | stfdem                       | Autorenabgleich | 11 / 11                   | 11                     | 77, 88                 |
| B31         | stfedu                       | Autorenabgleich | 12 / 12                   | 11                     | 77, 88                 |
| B32         | stfhlth                      | Autorenabgleich | 12 / 12                   | 11                     | 77, 88                 |
| B33         | gincdif                      | Autorenabgleich | 13 / 13                   | 5                      | 7, 8                   |
| B34         | freehms                      | Autorenabgleich | 13 / 13                   | 5                      | 7, 8                   |
| B35         | hmsfmlsh                     | Autorenabgleich | 13 / 13                   | 5                      | 7, 8                   |
| B36         | hmsacld                      | Autorenabgleich | 13 / 13                   | 5                      | 7, 8                   |
| B37         | euftf                        | Autorenabgleich | 14 / 14                   | 11                     | 77, 88                 |
| B38         | lrnobed                      | Autorenabgleich | 14 / 14                   | 5                      | 7, 8                   |
| B39         | loylead                      | Autorenabgleich | 14 / 14                   | 5                      | 7, 8                   |
| B40         | imsmetn                      | Autorenabgleich | 15 / 15                   | 4                      | 7, 8                   |
| B41         | imdfetn                      | Autorenabgleich | 15 / 15                   | 4                      | 7, 8                   |
| B42         | impcntr                      | Autorenabgleich | 15 / 15                   | 4                      | 7, 8                   |
| B43         | imbgeco                      | Autorenabgleich | 16 / 16                   | 11                     | 77, 88                 |
| B44         | imueclt                      | Autorenabgleich | 16 / 16                   | 11                     | 77, 88                 |
| B45         | imwbcnt                      | Autorenabgleich | 16 / 16                   | 11                     | 77, 88                 |

## Tatsächlich ausgeführte Prüfungen

| Prüfung                                                                        | Tatsächliches Ergebnis                                                                                       | Grenze                                                                                                                                                     |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quellendateihashes und frische `pdftotext -bbox-layout`-Extraktion             | BESTANDEN; alle Quellenpins und 836 Belege passen                                                            | Prüft identische öffentliche Quelle und konkrete Tokens/Regionen, keine wissenschaftliche Eignung                                                          |
| Eigene Lesetests mit vorab gelesenen deutschen Codes/Labels für jede Identität | BESTANDEN; 7532 begrenzte Assert-Ereignisse, kein verbleibender Fehlschlag                                   | Der Zähler ist kein Qualitätsmaß und kein unabhängiger Review                                                                                              |
| Zweiter Builderlauf                                                            | BESTANDEN; Exit 0 und byteidentische JSON                                                                    | Reproduktion desselben Autorenartefakts, keine weitere Abnahme                                                                                             |
| Gegenproben                                                                    | BESTANDEN; vertauschte B2-Beschriftung, umgekehrter EU-Endpunkt und erfundener B24-Code werden abgewiesen    | In-memory-Mutationen; Originale und endgültiges Artefakt bleiben unverändert                                                                               |
| Originalparser im eigenen Ausgabecache, ohne Build der aktiven Artefakte       | BESTANDEN; 296 Bestandszeilen, 205 technische Restzeilen                                                     | Bestandscheck erklärt semantische Inventarabnahme und Listenheftkategorien weiter NICHT_GEPRÜFT; kein rechnerischer Abzug der Ergänzung von den Restzeilen |
| `pnpm check`                                                                   | BESTANDEN; Exit 0, Formatprüfung, Handbuch-/Review-Schema-Prüfung, Typecheck, Tests und Build                | Technische Repositoryprüfung; keine UI-Änderung oder empirische Abnahme                                                                                    |
| Visuelle Autorlektüre                                                          | DURCHGEFÜHRT: Q PDF-S.3–16, Karten PDF-S.2–20, Codebook PDF-S.12, 21, 22, 38, 39, 40, 45, 46, 59, 63, 64, 65 | Eigene Quellenlektüre, keine unabhängige Annahme                                                                                                           |
| Empirische ESS-Untersuchung                                                    | IN_DIESER_PHASE_NICHT_ERFORDERLICH; nicht ausgeführt                                                         | Quellenannotation braucht keine Antwortdaten; keine Ergebnisbehauptung                                                                                     |
| Zwei nachfolgende unabhängige Reviewer / getrennte Modellfamilie / Phase1      | NICHT_GEPRÜFT                                                                                                | Kein eigener Quellencheck ersetzt diese Abnahmen                                                                                                           |

Die ersten Lesetests fanden fehlende frühe Kategorien in sieben zunächst zu hoch gesetzten Antwortregionen. B1–B5 sowie B41/B42 wurden am Original erneut gelesen und die Regionsanfänge korrigiert. `read-tests-first-failed.json` erhält diesen echten Fehllauf. Der endgültige Lauf prüft auch diese Kategorien. Frühere Builderläufe stoppten außerdem an zwei nicht passenden Caption-Grenzen und einer abgeschnittenen ersten Zeile; die finalen Grenzen tragen die kompletten Originalbeschriftungen. Eine Syntaxkorrektur am eigenen Lesetester ging dem ersten ausgeführten Test voraus. Kein solcher Fehllauf wird als unabhängig bestandene Prüfung dargestellt.

Die eingesetzten Tools waren `functions.exec` mit `exec_command` und `write_stdin`, `functions.view_image`, Python-Standardbibliothek, Poppler `pdftotext`/`pdftoppm` sowie bestehendes Node/pnpm/Prettier. Die Skills `unslop` und `pdf` wurden vor Anwendung gelesen. Keine Installation, kein Conda, kein Browser-/Webzugriff, keine zusätzliche Modellfamilie. Werkzeugversionen stehen in `tool-versions.json`. Die ursprünglichen Quellen wurden nicht bearbeitet.

## Reproduktion und Paketbelege für zwei Reviewer

Der folgende tatsächlich ausgeführte Aufruf regeneriert nur die eigene Ergänzung und die eigenen Outputs aus den unveränderten öffentlichen Pins:

```bash
bash outputs/loop/inventory002-ab/reproduce.sh
```

Das Skript enthält folgende Quellen-/Builder-Aufrufe:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003
pdftotext -bbox-layout outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab/questionnaire.bbox.html
pdftotext -layout outputs/loop/inventory/ESS11_questionnaires_DE.pdf outputs/loop/inventory002-ab/questionnaire.layout.txt
pdftotext -bbox-layout outputs/loop/inventory/ESS11_showcards_DE.pdf outputs/loop/inventory002-ab/showcards.bbox.html
pdftotext -layout outputs/loop/inventory/ESS11_showcards_DE.pdf outputs/loop/inventory002-ab/showcards.layout.txt
pdftotext -bbox-layout outputs/loop/inventory/ESS11_appendix_a7_e04_1.pdf outputs/loop/inventory002-ab/codebook.bbox.html
pdftotext -layout outputs/loop/inventory/ESS11_appendix_a7_e04_1.pdf outputs/loop/inventory002-ab/codebook.layout.txt
python3 outputs/loop/inventory002-ab/build_ab.py
python3 outputs/loop/inventory002-ab/read_tests.py
```

Der separate Bestandscheck lief mit:

```bash
python3 pipeline/inventar.py check --cache outputs/loop/inventory002-ab/baseline-check-cache
pnpm check
```

Ein zweiter tatsächlicher Builderlauf reproduzierte die JSON byteidentisch; `final-reproduction-check.json` enthält Vorher-/Nachherhash und Exitstatus.

Die vier Pins wurden für diesen Bestandscheck unter den Originaldateinamen in den eigenen Cache kopiert. Der Check schreibt seine Extrakte und `check-current.json` ausschließlich dorthin. Aktive CSV, Provenienz und Parser bleiben bitgleich mit den Baselinehashes.

Das definierte Prüfpaket umfasst die neue JSON-Datei, diesen Autorenbericht und folgende eigenen Dateien unter `outputs/loop/inventory002-ab/`: `plan-before-work.json`, `baseline-input-hashes.json`, `issue-input-check.json`, `startauftrag.txt`, `build_ab.py`, `read_tests.py`, `reproduce.sh`, `read-tests.json`, `read-tests-first-failed.json`, `final-reproduction-check.json`, `visual-reading.json`, `tool-versions.json`, `baseline-pipeline-check.log`, `baseline-check-cache/check-current.json`, `pnpm-check.log` sowie die drei frischen Text-/BBox-Extrakte und gerenderten genannten Originalseiten. Die Quellen sind im ursprünglichen Inventarcache und im eigenen Bestandscheckcache identisch gepinnt. `package-hashes.json` nennt alle tatsächlich bereitgestellten Paketdateien und Hashes. Der Paketindex kann den eigenen Hash nicht rekursiv enthalten.

Reviewer sollen die unveränderte Ergänzung gegen die Originale prüfen, insbesondere Interviewcode/Caption-Zellen, Karten-Textlagen, Gruppen-/Filterübernahme, den offenen Wahlcrosswalk und die Erhaltung der Partei-/08-Konflikte. Dieser Bericht enthält keine Reviewerurteile oder gewünschte Reviewerentscheidung. Die unabhängige Prüfung bleibt beim Koordinator.

## Exakte Restliste und Übergabegrenze

In der JSON stehen 61 konkrete Restpunkte mit Frage-ID und Originalbelegen. Davon sind 52 die gemeinsamen Versions-/Daten-Missinggrenzen für jede A-/B-Identität. Hinzu kommen zwei Wahlcrosswalks B14a/B14b, drei Partei-Codeübertragungen B14a/B14b/B24, zwei Erfassungen des Originalkonflikts B24/B25 und zwei Zeitfeld-Kodierungsabgleiche A1/A3. Diese Punkte sind nicht empirisch geprüft und werden nicht durch die Eigenchecks geschlossen.

Alle endgültigen Eignungs-, Polungs-, Konstrukt-, Dimensions- und Scoreentscheidungen fehlen weiterhin. Der übrige ESS-Inventarbestand wird mit dieser Ergänzung nicht als vollständig strukturiert bezeichnet. Eine Integration in das aktive Inventar, das globale Beleg-/Quellen-/KI-Protokoll oder die Website fand bewusst noch nicht statt; der Koordinator kann das eingefrorene Autorenpaket nach den verlangten unabhängigen Prüfungen beurteilen.

JSON-SHA-256: `9554a568c1a08fe7d6676960dd7e41d2b50d1ad7c16c5d8d33bfed4edc44c138`. Aktive Eingangshashes stehen in `baseline-input-hashes.json`; die Eigenprüfung bestätigt für CSV, Provenienz und Parser unveränderte Bytes. Keine Antwortdaten, Personenkennungen, Credentials, Cookies, Antworten aus Teil A/B, Parteiverteilungen oder Selbsteinstufungswerte wurden gelesen oder ausgegeben. Lesen und Strukturieren der öffentlichen Variablenmetadaten war auf den expliziten Inventarauftrag beschränkt.
