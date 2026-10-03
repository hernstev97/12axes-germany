# PRE-CONFIRMATORY-001: Quellen-, Konstrukt- und Fairness-Erstprüfung vor B

Datum: 3. Oktober 2026. Ersturteil: **ACCEPTED_BOUNDED** für den bezeichneten Quellen-/Interpretationsvertrag vor B. Keine B-Bestätigung, Messvalidierung, Bevölkerungsnorm, Gruppenfreigabe oder Produktfreigabe.

## Prüffassung und Zugang

Geprüft wurde `PRE-CONFIRMATORY-001/v1`, Rolle `sources-construct-fairness`, im Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Bezeichnete Fassung: `modell-v1` auf `c9aadb4b610bac0c90ed8ceb409949b0222863df`. AGENTS.md, docs/project.md, Paketanforderungen und Manifest wurden zuerst gelesen, anschließend die 19 Rollenartefakte und notwendige offizielle öffentliche Quellen. Der zusätzlich erlaubte Beleg `reports/loop/model-tag-v1.json` nennt denselben lokalen und Remote-Commit. Seine zwei Dateipins passen zu den aktiven Modell-/A-Dateien. Ich habe keine Git-Kommandos ausgeführt und behaupte keine eigene frische Remote-Prüfung.

Alle 19 Rollenpins stimmen vor und nach der Prüfung mit dem Manifest überein; alle Dateien blieben unverändert. Belege: [pins-before.json](../../../outputs/loop/pre-confirmatory-sources/pins-before.json), [pins-after.json](../../../outputs/loop/pre-confirmatory-sources/pins-after.json).

Keine anderen aktuellen Erstberichte gelesen. Kein Zugriff auf `data/raw/`, `data/local/`, private Receipts, Armzuordnung, Antworten oder reale B-/C-/FULL-/politische Daten. Öffentlicher A-Aggregatbericht und öffentliche Variablen-/Wertdefinitionen wurden gelesen. Keine gemeinsame Forschungsdatei, Originalbericht, Installation oder Repository-Konfiguration geändert. Geschrieben wurden nur dieser Erstbericht und mein eigener Belegordner.

## Nachgeprüfte Quellenbindung

Sechs offizielle Quellen wurden erneut per öffentlichem GET geladen, jeweils HTTP 200. Die fünf PDF-Hashes und der Disclaimer-Hash entsprechen den vorhandenen Bindings. [Abrufprotokoll](../../../outputs/loop/pre-confirmatory-sources/source-access.json) enthält URLs, UTC-Zeiten, Bytes und SHA-256. Fragebogen, Listenheft und Codebook wurden an den konkreten Fundstellen abgeglichen. Zehn relevante Seiten wurden zusätzlich gerendert und visuell gelesen; Textauszüge und Bilder liegen im eigenen Belegordner.

| Items | Originalfundstelle | Kategorien und korrekt gerichtete Abbildung |
| --- | --- | --- |
| B34/B36 | Deutscher Fragebogen PDF/Druck 13; Listenheft PDF 14, Liste 13; Codebook 4.1 PDF 63–64/Druck 62–63 | Zustimmung 1–5; `(5-x)/4` |
| B35 | Dieselbe Fragebogenseite/Karte; Codebook PDF 63–64 | Gleiche Zustimmungskategorien, umgekehrte Schamaussage; `(x-1)/4` |
| B40–B42 | Fragebogen PDF/Druck 15; Listenheft PDF 17, Liste 16; Codebook PDF 65–66/Druck 64–65 | Vier Umfangsstufen; `(4-x)/3` |
| B43–B45 | Fragebogen PDF/Druck 16; Listenheft PDF 18–20, Listen 17–19; Codebook PDF 66–68/Druck 65–67 | 0–10, negativ zu positiv; `x/10` |

Die Wortlaut-/Kategorienbindung passt zur engen Bedeutung des Kernvertrags. Einleitungen, Vorleseanweisungen und der fortgeltende An-alle-Druckkontext sind erhalten. Das bestätigt den gelesenen Druckablauf, keine nationale CAPI- oder Webmodus-Abnahme. Quelle: [deutscher Fragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), bezeichnete Seiten; [Listenheft](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf), bezeichnete Karten.

Edition 4.2, DOI und Veröffentlichung am 2. Juli 2026 wurden direkt im öffentlichen [Dateiportal](https://ess.sikt.no/en/datafile/242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef), Documentation → DOI and version information, gelesen. Die 4.2-Änderung betrifft die ukrainische Übersetzung von B39; 4.0 nennt die deutsche Stratumkorrektur. Das rechtfertigt keine Behauptung bytegleicher deutscher Dateien. Die 4.1-Codebookfassung wird im Paket zutreffend als solche geführt.

Zusätzlich habe ich über die offizielle öffentliche [Metadaten-API](https://api.nsd.no/graphql) ausschließlich Schema und `search.dataFileMetadata`/`search.variableMetadata` abgefragt. Kein `analysis`-Feld und keine Antwortzahlen. Die Dateidefinition nennt 4.2 und interne Metadatenversion 179. Alle neun Felder, gültigen Werte und Missing-Flags stimmen mit dem Kernvertrag überein. Vollständige `fullCodeList`-Antworten vermeiden eine unvollständige Pagination. Für die neun Kernfelder enthalten sie keinen als nicht anwendbar definierten Code. Verweigerung, Weißnicht und keine Antwort sind von Sachantworten getrennt; 9/99 werden nicht zu gedruckten deutschen Antworten erklärt. [Requests, Responses und Vergleich](../../../outputs/loop/pre-confirmatory-sources/core-and-vote-metadata-checks.json) belegen diesen engen Abgleich. CSV-Vorkommen und Parsing wurden nicht kontrolliert.

## A-Auswahl und Reichweite

`data/modell-v1.json` bindet tatsächlich M2, H/ZF, dieselben neun Items, Gruppen, Namen, Konfiguration und A-Quellpins. `a_result.path` und SHA-256 führen exakt zu `reports/phasen/01-a-entwicklung.json`, einschließlich tatsächlicher A-Ladungs-/Korrelationsreferenz. Die maschinenlesbare Konfiguration ist mit der im A-Bericht identisch. Der Plan legte M2 vor M3 und die gemeinsame EFA-Zuordnung vor A fest; der Modellfreeze erweitert weder Items noch politische Bedeutung.

Im öffentlichen A-Bericht ist M2 zulässig, beide Scores bestehen seine bezeichneten Kriterien und die Zwei-Faktor-Zuordnung besteht Haupt-/Wiederholungs-/Obliminkontrolle. Die RMS-Obergrenze beträgt 0.08172360600729839 bei dem eigenen Budget 0.10. M1 verfehlt RMS und Mindestdimensionenzahl. M3 hat zwar die kleinere RMS-Obergrenze 0.05091304667763669, doch seine Drei-Faktor-EFA-Läufe sind fehlgeschlagen. Der feste Auswahlschritt wählt M2; er belegt weder die Wahrheit eines Zweifaktorkonstrukts noch die Widerlegung dreier Faktoren. PB-S02 hält die dafür nötige Interpretationsgrenze fest.

Die Bezeichnungen H und ZF bleiben vertretbar, solange die Erläuterung aus dem Plan mitgeführt wird: H verbindet zwei Rechts-/Lebensführungsaussagen mit einer hypothetischen familiären Schamreaktion. ZF verbindet den erfragten Aufnahmeumfang mit wahrgenommenen Folgen. Sie sind keine allgemeine Liberalitäts-, Moral-, Links-rechts-, Asyl- oder Parteiprogrammskala. Niedrige Antworten belegen keine zusätzlichen Motive oder Identitäten. Das Zusammenfassen verdeckt mögliche Unterschiede der einzelnen Gegenstände; der Vertrag benennt diese Gegenalternative. Die A-Auswahl ist bedingte explorative Entwicklung, kein gegenwärtiger persönlicher Test.

Der deutsche Erhebungsbezug ist 9. Mai bis 21. Dezember 2023, persönlich erhobene Interviews. Der rundenweite Zeitraum reicht bis Dezember 2024; er darf nicht als deutsche Feldzeit übernommen werden. Die im [Studienportal](https://ess.sikt.no/en/study/412db4fe-c77a-4e98-8ea4-6c19007f551b), Universe, gelesene Zielpopulation umfasst 15+-Personen in Privathaushalten ohne Staatsangehörigkeitsbeschränkung. Zielpopulation und tatsächliche Teilnahme sind verschieden. [Länderbericht 4.0](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_country_documentation_report_e04.pdf), PDF/Druck 79–80/86/88, bestätigt Feldzeit, persönlichen Modus und 2.420 gültige Interviews, dokumentiert Nonresponse/Sprachbarrieren und verneint Bundeslandrepräsentativität. Die landesweite Feldarbeitsreserve im Länderbericht ist eine andere Größe als die eigene vier-PSU-Reserve C.

A betrifft nur 23 Strata und die festgelegte vollständige Neunantwortdomäne. Seine fehlende Gewichtsmasse 0.07606427187065797 entspräche bereits einer Worst-Case-Breite von 7.606427187065797 Perzentilpunkten innerhalb dieses Arms. Das überschreitet das eigene Fünf-Punkte-Budget; A liefert somit keine vorbehaltlose Bevölkerungsposition. Es ist auch kein gemessener FULL-Befund. Die A-Entscheidung nennt die Grenze, verlangt eine eigene vollständige Rechnung und unterstellt keine MCAR/MAR-Situation. Der Plan schließt eine als Deutschland bezeichnete 23-Strata-Norm ohne sachlich bestimmbaren Geltungsbereich aus; C/FULL enthalten A/B und sind keine zusätzliche unabhängige Bestätigung.

## Gruppen, Fairness und Rechte

Die historische Wahlbindung ist sachgerecht: B13 verweist auf September 2021, B14a/B14b trennen Erst-/Zweitstimme und gelten bei Wahlteilnahme. Ungültige/leere Stimmzettel zählen nach der nationalen Anweisung zu Nein. Die öffentliche 4.2-Definition von `prtvgde2` unterscheidet die nachkodierten Parteien von der ursprünglichen offenen Antwort und enthält 55 sowie 66/77/88/99. Ein eigener Vergleich der öffentlichen Code-/Label-/Missingdefinitionen mit dem Gruppenvertrag besteht. Quellen: Fragebogen PDF/Druck 7–8, [Codebook 4.1](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf), PDF 21–22/Druck 20–21, und genannte öffentliche API.

Der Vertrag behandelt dies als retrospektive Selbstauskunft, keine heutige Wahlabsicht, nachgewiesene Stimmabgabe oder Parteiposition. Gruppenlabels und Algorithmen werden vor Antworten fixiert; Parteien stehen alphabetisch, Nähe-Ranglisten und Gesamtmatches entfallen. Das binäre erfasste Geschlecht wird nicht mit vollständiger Geschlechtsidentität gleichgesetzt, Berlin nicht in Ost/West geraten, unklassifizierbare Bildungswerte nicht zu fehlender Zustimmung gemacht. Diese Festlegungen sind faire, überprüfbare Grenzen. Sie sind noch keine empirisch bestandenen Gruppenprüfungen.

Antwortmittel und latente Konstruktvergleiche bleiben ausdrücklich getrennt. Strikte modellbedingte Vergleichbarkeitsprüfungen, die positive Kurvenäquivalenz, vollständige gemeinsame Kovarianz und Präzisionsregeln sind als Voraussetzungen bezeichnet; gemeinsame affine DIF bleibt unidentifiziert. Kein großer p-Wert oder synthetisches Ergebnis wird zum Vergleichbarkeitsbeweis erklärt. Norm-/Gruppensoftware und reale Gruppenbefunde gehören zum späteren Paket und wurden hier nicht geprüft.

Die [ESS-Bedingungen](https://www.europeansocialsurvey.org/contact/disclaimer), Conditions of use, unterscheiden Daten unter CC BY-NC-SA 4.0 und Dokumentation unter CC BY-SA 4.0. Der Kernkatalog führt Attribution, Quellen, Änderungen und die Dokumentationslizenz; der A-Aggregatbericht trägt separate Datenattribution, DOI, Lizenz und Änderungserläuterung. Die Lizenzakte übernimmt die 4.1-Beispielzitation des Disclaimers nicht als verwendete Ausgabe. Die offiziellen [BY-SA-Lizenzbedingungen](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en), §§2–4, und [BY-NC-SA-Bedingungen](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en), §§1–4, wurden nachgelesen. Kein blanket Lizenzwechsel für eigenen Code, keine ESS-Billigung, keine abschließende rechtliche Produktfreigabe.

Zwei getrennte Codex-Rollen gehören derselben Modellfamilie an. Frischer begrenzter Kontext verhindert das Lesen anderer Ersturteile, beseitigt aber keine gemeinsamen Modellfehler, unbekannten Anbieterregeln oder die gemeinsame Dateisystemumgebung. Der Vertrag beansprucht keine absolute politische Neutralität. Ich prüfe seine belegten Maßnahmen und Grenzen; ich bestätige keine solche absolute Eigenschaft.

## Befunde und kleinste Korrekturen

### PB-S01: allgemeiner 6/66-Text ist für die 0–10-Items ungenau

Fundstelle: `data/item-core-v1.json`, `items[id=B43/B44/B45].not_applicable_policy`. Der allgemeine Text nennt 6/66 unerwartet. Bei B43–B45 ist 6 eine gültige Sachantwort; die zugehörigen `allowed_values`, Scoremaps und `protocol_not_applicable_codes:[66]` sind dagegen richtig. Das offizielle Codebook/4.2-Codelistenbinding bestätigt dies.

Schwere/Folge: gering, echte Dokumentationsinkonsistenz, keine bloße Stilfrage. Sie rechtfertigt keine Umkodierung oder Entfernung der gültigen Antwort 6. Die numerische Quellen-/Scorebindung dieses Pakets ist korrekt; der Befund blockiert das bezeichnete B-Modell in dieser Quellenrolle nicht. Die tatsächliche Parserentscheidung bleibt Sache der Methoden-/Reproduzierbarkeitsrolle.

Kleinste Korrektur: ergänzendes öffentliches Erratum zum unverändert erhaltenen Kernvertrag: bei B34–36/B40–42 ist 6 unerwartet; bei B43–45 ist 66 unerwartet, 6 gültig. Keine Kategorien, Pole, Modelle oder Erfolgsgrenzen ändern.

### PB-S02: fehlgeschlagene M3-EFA nicht als Gegenbeweis darstellen

Fundstellen: `reports/phasen/01-a-entscheidung.md:7`; A-JSON `efa.3.runs`. Haupt-/Wiederholung melden `ORDINAL_ADAPTER_LIBRARY_WARNING`, Oblimin `ESS_DEVELOPMENT_LIBRARY_WARNING`, jeweils `FAILED`. Es gibt hier keine erfolgreich berechnete Drei-Faktor-Zuordnung mit beobachtetem inhaltlichem Gegenbefund.

Schwere/Folge: gering, nichtblockierende Präzisierung der Ergebniserläuterung. Die feste Regel verlangt positive Unterstützung, die für M3 fehlt, und wählt ohnehin das zulässige M2 zuerst. Der Bericht bewahrt die Fehler. Kein nachträglicher Rettungslauf ist für die jetzige Wahl nötig.

Kleinste Korrektur vor einer weitergehenden Ergebnisdarstellung: explizit schreiben, dass M3 wegen fehlgeschlagener EFA-Ausführung nicht zulässig war; keine Aussage, die Daten hätten drei Faktoren widerlegt oder zwei Faktoren als einzige mögliche Struktur bewiesen.

Kein fachlich erheblicher Quellen-/Konstrukt-/Fairness-Fehler, der den unveränderten M2-Vertrag vor B sperrt, wurde gefunden. Stilwünsche, eine breitere Themenbatterie oder zusätzliche Modelltags sind keine Blocker dieses Urteils.

## Ausgeführte Checks und verbleibende Grenze

| Check | Tatsächliches Ergebnis |
| --- | --- |
| Rollenpins vor/nach | Exit 0; 19/19 passend und unverändert |
| Sechs öffentliche Originalabrufe | Exit 0; je HTTP 200 und bekannte Hashes |
| PDF-Textauszüge und zehn Renderings | Exit 0; zehn Bilder visuell gelesen |
| Eigener öffentlicher Vertragscheck | Endfassung Exit 0; 50 Assertions, [Skript](../../../outputs/loop/pre-confirmatory-sources/check-public-contract.py)/[Ausgabe](../../../outputs/loop/pre-confirmatory-sources/public-contract-checks.json) |
| Erster Lauf desselben eigenen Checks | Exit 1; mein Test schloss fälschlich jede numerische 6 aus. Auf Missingstatus/Quellenlabel korrigiert; kein Projektfehler aus diesem Exit abgeleitet |
| Direkter Abruf einer CC-HTML-Kopie | Exit 1, HTTP 403. Offizielle Lizenztexte anschließend erfolgreich im Webwerkzeug gelesen; kein lokaler Kopiernachweis behauptet |
| ESS-Portal | Documentation und Universe tatsächlich im Chrome-Browser gelesen; IAB nicht verfügbar, kein Analysis-/Login-/Downloadzugriff |

[Quellenbeobachtungen](../../../outputs/loop/pre-confirmatory-sources/source-observations.json) halten die tatsächlichen Zugriffe und Grenzen fest. Keine empirische Neuberechnung, CI, Produktbrowserprüfung oder Norm-/Gruppenimplementierung ausgeführt. Dieses Urteil ergänzt die getrennte Methodenrolle; erst beide hinreichend begrenzten positiven Urteile und das ausführbare B-Zugriffsgate erlauben den vorgesehenen B-Schritt. B-/FULL-Befunde und ihre Übertragung in Aussagen benötigen die späteren echten Rechnungen und getrennten Übergangsprüfungen.
