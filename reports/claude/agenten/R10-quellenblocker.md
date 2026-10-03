# R10 – Präzisierung der Quellenblocker

Stand: 4. Oktober 2026. Abrufe am 3. Oktober 2026 zwischen 22:33 und 22:52 UTC. Auftrag: `reports/claude/auftraege/R10-quellenblocker.md` mit dem gemeinsamen Teil `R-erweiterung-gemeinsam.md`. Getrennter Claude-Subagent, Branch `research/life-93-claude-20261003`.

Dieser Bericht stellt fest, was die Nutzungsbedingungen der Quellen wörtlich sagen. Er ist keine Rechtsberatung und keine Freigabe. Ob eine Regel wirksam ist oder ob gesetzliche Schranken eine Nutzung unabhängig von den Bedingungen erlauben, prüfe ich nicht. Antwortverteilungen oder andere Ergebnisse habe ich weder gesucht noch gelesen. Die maschinenlesbare Fassung steht in `reports/claude/agenten/R10-quellenblocker.json` (23 Quellen, 138 Einträge).

## 1. Kurzfassung

1. **Nur beim ESS erlaubt eine Lizenz alle sechs Nutzungen (Klasse C).** Die Daten stehen unter CC BY-NC-SA 4.0, die Dokumentation unter CC BY-SA 4.0. Bedingungen sind Namensnennung, Kennzeichnung von Änderungen, bei Daten nichtkommerzielle Nutzung und ShareAlike für Bearbeitungen. Die ESS-Benutzervereinbarung im Data Portal, die R2, R3 und R7 nicht gesehen hatten, regelt laut Programmcode des Portals nur Nutzungsstatistik, Umfragen unter Nutzenden und Kontodaten. Für ESS12 gilt derselbe Rahmen. Der deutsche Fragebogen ist aber noch nicht veröffentlicht (HTTP 404), die Daten sollen im Januar 2027 erscheinen.
2. **Ausdrückliche Verbote der KI-Verarbeitung von Einzeldaten (Klasse A)** gibt es bei drei Bereitstellern:
   - bei GESIS (§ 4, laut R2 bis R6) für alle GESIS-Bestände einschließlich Eurobarometer-Einzeldaten, EVS sowie der Daten von ZMSBw und UBA,
   - beim UK Data Service (Endnutzerlizenz 16.00, Abschnitt 5 Nr. 5) für Eurofound-Daten,
   - neu beim SOEP: „Die Nutzung von SOEP-Daten in KI-Anwendungen oder zum Training von KI-Modellen ist … nicht gestattet.“ Einzelpersonen ohne wissenschaftliche Einrichtung erhalten dort ohnehin keinen Zugang.
   
   Das ZQP untersagt auf seiner Website das automatisierte Auslesen von Inhalten. Das betrifft schon das Lesen durch Agenten.
3. **Eurobarometer-Tabellen der Kommission:** Lesen der Methodendokumente, Verarbeitung der Tabellen, Veröffentlichung zusammengefasster Anteile und Weitergabe sind nach Beschluss 2011/833/EU und CC BY 4.0 erlaubt (C). Bedingungen sind Quellenangabe, Kennzeichnung von Änderungen und das Verbot, die ursprüngliche Bedeutung zu verzerren. Einzeldaten gibt es nur über GESIS (A). Deutsche Fragewortlaute bleiben ungeklärt (B), weil die Kommission die deutschen Fragebögen nicht selbst veröffentlicht.
4. **WVS:** Die „Conditions of Use“ stellen die Dateien „without restrictions“ bereit, solange sie nicht gewinnorientiert genutzt, zitiert, jede Veröffentlichung an die WVSA gemeldet und die Dateien nicht weitergegeben werden. Das ergibt Klasse C für die Nutzungen (1) bis (4), sobald Steven dem Formular zustimmt. Bedingung b setzt die Veröffentlichung von Ergebnissen voraus. Das präzisiert R5, wo die Website-Nutzung als „nicht ausdrücklich geregelt“ vermerkt ist. Fragewortlaute (B) und Weitergabe der Dateien (A) bleiben Grenzen.
5. **Pew:** Die Datensatzlizenz (Abschnitt 13 der Terms of Use) erlaubt Verarbeitung und Veröffentlichung von Auszügen (C). Die Weitergabe vollständiger Daten ist untersagt (A). Ein deutscher Wortlaut ist nicht öffentlich (B).
6. **OECD:** Veröffentlichte OECD-Daten dürfen für jeden Zweck genutzt und geteilt werden (C). Für Fragebögen, Mikrodaten und eine deutsche Fassung gibt es keine eindeutige Regel (B).
7. **EIB:** Veröffentlichung, Anzeige und Weitergabe von Inhalten sind ohne schriftliche Erlaubnis untersagt (A).
8. **ifo und SOEP binden die Daten an wissenschaftliche Einrichtungen und verbieten die Weitergabe (A).** Die öffentlich verlinkte Vertragsvorlage des ifo Bildungsbarometers (Datei vom 08.09.2022) verlangt zusätzlich, jede Veröffentlichung vorab dem EBDC vorzulegen.
9. **Bei RIFS, Reuters Institute, Münchner Sicherheitskonferenz, Körber-Stiftung, ZMSBw-Bericht, UBA-Bericht, Vodafone Stiftung, Initiative D21 und eupinions** fand ich keine Lizenz, die eine der Nutzungen erlaubt (meist B). Digital News Report und Munich Security Index beruhen zudem auf Online-Quotenstichproben.
10. **Eurobarometer als begrenzter Vergleich:** Die meisten geprüften Präferenzfragen betreffen Politik der EU. Fragen zu Entscheidungen Deutschlands stehen nur in zwei Spezialmodulen von 2022 und in der Aussage „Deutschland sollte Flüchtlingen helfen“. Ein Vergleich mit der Bevölkerung ohne Wählergruppen ist unter den Bedingungen in Abschnitt 5.2 vertretbar. Ob die veröffentlichten Tabellen dafür genügen, ist weiter ungeprüft (Abschnitt 5.3).

## 2. Vorgehen und Regeln der Einordnung

**Klassen.** Ich ordne jede Nutzung genau einer Klasse zu und folge dabei dem Wortlaut der Regel:

- **A „ausdrücklich verboten“:** Die Regel untersagt die Nutzung wörtlich („verboten“, „nicht gestattet“, „untersagt“, „may not“, „abstain from“, „not redistributed“). Das gilt auch, wenn eine Ausnahme auf Anfrage möglich ist. Die Ausnahme ist dann vermerkt.
- **B „ungeklärte Vertragsbedingung“:** Es ist unklar, ob die Regel die Nutzung erfasst. Oder die Nutzung ist an eine Zustimmung, einen Vertrag oder eine Registrierung gebunden, deren Inhalt offen ist. Oder ich habe keine Regel gefunden. Eine Formel wie „nur nach vorheriger Zustimmung gestattet“ zählt nach der Auftragsdefinition zu B.
- **C „durch vorhandene Lizenz erlaubt“:** Eine Lizenz oder Weiterverwendungsregel erlaubt die Nutzung wörtlich. Die Bedingungen stehen in der Begründung. Eine Zustimmung mit bekanntem Inhalt, etwa beim WVS-Formular oder beim Pew-Konto, verhindert Klasse C nicht. Sie ist als Bedingung genannt und bleibt Stevens Entscheidung.

**Weitere Regeln.**

- Das Fehlen einer KI-Klausel begründet keine Klasse. Klasse C stützt sich immer auf eine Erlaubnis im Wortlaut.
- Die Klasse gilt für den genannten Bezugsweg. Andere Wege, etwa Eurofound-Dokumente über das UK Data Service statt über die Eurofound-Website, stehen unter „Offen“.
- Braucht eine Nutzung mehrere Dokumente, gilt die Klasse des am wenigsten geklärten notwendigen Teils (Beispiel OECD (1)).
- Nutzung (3) umfasst zwei Wege: Agenten verarbeiten Einzeldaten selbst, oder sie schreiben Skripte, die Menschen ausführen. Wo die Regel beide Wege unterscheidet oder ihre Reichweite offen ist, gilt die strengere Klasse; der andere Weg steht in der Begründung (GESIS, UK Data Service, SOEP).
- „Fragebögen und Methodendokumente“ meint bei Nutzung (1) die vom Bereitsteller veröffentlichten Dokumente. Ob ein Agent sie ohne Ergebnisse lesen kann, ist eine Frage der Ergebnisblindheit, nicht der Rechte. Ich vermerke sie trotzdem.

**Belege.** Wörtliche Zitate stammen aus Rohtext: mit `curl` geladenes HTML, `pdftotext` oder das XML einer DOCX-Datei. Drei Stellen beruhen nicht auf Rohtext und sind so markiert:

- die SOEP-KI-Richtlinie, gelesen über das Abrufwerkzeug, das Inhalte durch ein Hilfsmodell wiedergibt;
- die Methodik des Munich Security Index, nur aus einer Suchmaschinen-Zusammenfassung;
- das Tabellenangebot des Reuters Institute, nur aus einer Suchmaschinen-Zusammenfassung.

GESIS-Bedingungen und eupinions übernehme ich ohne neuen Abruf aus R2, R3, R5, R6 und R7.

**Ergebnisblindheit und GESIS-Sperre.**

- Ich habe keine Ergebnistabelle, keinen Bericht mit Ergebnissen, kein Codebuch und keinen Datensatz geöffnet.
- Bei den Eurobarometer-Datensätzen habe ich nur Lizenzfeld, Dateinamen und die Sätze zu den Volumes gelesen, keine sonstige Beschreibung.
- Beim ORA-Eintrag zum Digital News Report 2024 habe ich nur die Rechtefelder ausgegeben.
- Eine Suchmaschinen-Zusammenfassung zum Munich Security Index zeigte ungefragt eine Aussage über Ergebnisse für Deutschland. Ich habe sie nicht verwendet und gebe sie nicht wieder.
- GESIS-Server und Archivkopien von GESIS-Seiten habe ich nicht aufgerufen.

**Nutzungen.** (1) Lesen und Auswerten von Fragebögen und Methodendokumenten durch KI-Agenten. (2) Verarbeitung veröffentlichter Tabellen durch KI-Agenten. (3) Verarbeitung von Einzeldaten durch KI-Agenten oder durch von KI geschriebene Skripte. (4) Veröffentlichung zusammengefasster Anteile auf einer nichtkommerziellen öffentlichen Website. (5) Anzeige deutscher Fragewortlaute auf der Website. (6) Weitergabe von Dateien.

## 3. Übersicht Quelle × Nutzung

| Quelle | (1) | (2) | (3) | (4) | (5) | (6) |
| --- | --- | --- | --- | --- | --- | --- |
| ESS 1–11 | C | C | C | C | C | C |
| ESS12 | C | C | C | C | C | C |
| GESIS | B | B | A | B | B | A |
| EB Kommission | C | C | A | C | B | C |
| EB GESIS | B | B | A | B | B | A |
| WVS | C | C | C | C | B | A |
| OECD RTM | B | C | B | C | B | C |
| Eurofound/UKDS | C | C | A | C | C | A |
| Pew | C | C | C | C | B | A |
| EIB | B | B | B | A | A | A |
| ifo/EBDC | B | B | B | B | B | A |
| RIFS/SNB | B | B | B | B | B | B |
| Destatis/FDZ | C | C | B | C | C | C |
| SOEP/DIW | B | B | A | B | B | A |
| Reuters DNR | B | B | B | B | B | B |
| MSI | B | B | B | B | B | B |
| Körber | B | B | B | B | B | B |
| ZMSBw | B | B | A | B | B | B |
| UBA | B | B | A | B | B | B |
| ZQP | A | A | B | B | B | B |
| Vodafone Stiftung | B | B | B | B | B | B |
| D21 | B | B | B | B | B | B |
| eupinions | B | B | B | B | B | B |

Lesart: A = ausdrücklich verboten, B = ungeklärt, C = durch Lizenz erlaubt (mit Bedingungen). „EB Kommission“ meint den Weg über Berichte und Volumes der Kommission, „EB GESIS“ den Weg über Einzeldaten und Fragebögen bei GESIS. Für ESS12 beschreibt C den Lizenzrahmen. Deutscher Fragebogen und Daten sind noch nicht veröffentlicht.

Nicht eigens eingeordnet habe ich Quellen, die in R5 bis R7 nur am Rand vorkommen:

- CSES Modul 6: Der deutsche Beitrag stammt aus GLES und liegt damit bei GESIS.
- FRA Fundamental Rights Survey und ECFR: nicht vertieft, Stichprobe von 2019 oder online.
- BZgA-Organspendebefragung: Fragebogen nicht gesehen.
- IHSN-Katalog: nur Kopien von WVS-Fragebögen mit dem Vermerk „All Rights Reserved“, siehe WVS (1).
- Politbarometer und EVS: Teil des GESIS-Eintrags.

## 4. Belege je Quelle (Quelle × Nutzung × Klasse × Beleg)

Wiederholt sich ein Beleg innerhalb einer Quelle, verweist die Tabelle mit „wie (n)“ auf die erste Zeile.

### 4.1 European Social Survey, Runden 1–11 (ESS ERIC, Vertrieb Sikt)

Fundstellen: https://www.europeansocialsurvey.org/contact/disclaimer; https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en; https://creativecommons.org/licenses/by-sa/4.0/legalcode.en. Fassung: ESS-Disclaimer (HTML, SHA-256 8e0ded72…); CC-Legal-Code 4.0 (BY-NC-SA 527c4e0e…, BY-SA 47c0a954…). Abgerufen: 2026-10-03T22:33Z (Disclaimer), 22:34Z (CC-Lizenztexte).

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **C** | „European Social Survey documentation is licensed under CC BY-SA 4.0“ CC BY-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part; and produce, reproduce, and Share Adapted Material.“ Abschnitt 2(a)(4): „The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so.“ | Die Dokumentation steht unter CC BY-SA 4.0. Die Lizenz erlaubt die Vervielfältigung für jeden Zweck in allen Medien einschließlich technisch nötiger Kopien. Das Lesen und Auswerten durch einen Agenten ist eine solche Vervielfältigung. Bedingungen: Namensnennung, Lizenzhinweis, Kennzeichnung von Änderungen, ShareAlike nur bei Weitergabe bearbeiteter Fassungen. | Ob nationale Fragebögen ausdrücklich als „ESS documentation“ gelten, steht nicht im Disclaimer. Der deutsche ESS11-Fragebogen trägt keinen eigenen Rechtevermerk (Titelblatt „Deutsche Teilstudie des European Social Survey (ESS)“); er wird vom ESS selbst bereitgestellt. |
| (2) | **C** | „European Social Survey data is licensed under CC BY-NC-SA 4.0“ CC BY-NC-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and produce, reproduce, and Share Adapted Material for NonCommercial purposes only.“ | Veröffentlichte ESS-Tabellen beruhen auf den Daten und fallen, soweit sie lizenziertes Material enthalten, unter CC BY-NC-SA 4.0. Vervielfältigung und Bearbeitung sind für nichtkommerzielle Zwecke erlaubt. Bedingungen: Namensnennung, nichtkommerziell, ShareAlike für weitergegebene Bearbeitungen. | Ob einzelne ESS-Publikationen (etwa „Topline series“) eine eigene Lizenz tragen, habe ich nicht geprüft. |
| (3) | **C** | „European Social Survey data is licensed under CC BY-NC-SA 4.0“ „The data are available without restrictions, for not-for-profit purposes.“ CC BY-NC-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and produce, reproduce, and Share Adapted Material for NonCommercial purposes only.“ Abschnitt 2(a)(4): „The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so.“ | Die Datenlizenz erlaubt Vervielfältigung und Bearbeitung in allen Medien für nichtkommerzielle Zwecke. Das gilt für die Verarbeitung durch Agenten wie durch von KI geschriebene Skripte. Die ESS-Benutzervereinbarung im Data Portal (Text aus dem Programmcode des Portals) regelt nur Nutzungsstatistik, Umfragen unter Nutzenden und Kontodaten, keine Nutzungsbeschränkung. Die strengere Projektregel bleibt: keine Rohdatenzeilen in Agentenkontexten (AGENTS.md). | „NonCommercial“ heißt laut Lizenz „not primarily intended for or directed towards commercial advantage or monetary compensation“; Steven sollte den nichtkommerziellen Charakter bestätigen. Die Benutzervereinbarung habe ich nur im Programmcode gelesen, nicht in der angezeigten Fassung nach Anmeldung. |
| (4) | **C** | wie (2) | Die Lizenz erlaubt, Bearbeitungen für nichtkommerzielle Zwecke öffentlich zu machen. Bedingungen: Namensnennung mit Lizenzhinweis und Link, Kennzeichnung von Änderungen („Adapted from ESS Round X, version number X“), nichtkommerziell, ShareAlike für Bearbeitungen. | Ob zusammengefasste Anteile „Adapted Material“ sind und damit unter BY-NC-SA weitergegeben werden müssen, bleibt offen (wie R1, R2). |
| (5) | **C** | „European Social Survey documentation is licensed under CC BY-SA 4.0“ CC BY-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part; and produce, reproduce, and Share Adapted Material.“ | Fragewortlaute sind Dokumentation unter CC BY-SA 4.0 ohne NC-Klausel. Anzeige mit Namensnennung, Lizenzlink und Kennzeichnung von Änderungen ist erlaubt; geänderte Wortlaute stehen unter ShareAlike. | Wie bei (1): Status nationaler Fragebögen als Dokumentation nicht ausdrücklich bestätigt. |
| (6) | **C** | CC BY-NC-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and produce, reproduce, and Share Adapted Material for NonCommercial purposes only.“ „ESS ERIC recommends that ESS datasets are not made available on external websites. Instead, please link to datasets on the ESS Data Portal.“ | Die Lizenzen erlauben die Weitergabe (Share), bei Daten nur nichtkommerziell. Die Empfehlung, Datensätze nicht extern bereitzustellen, ist eine Empfehlung, kein Verbot. Das Projekt schließt Rohdaten aus Git, Webapp und CI ohnehin aus (AGENTS.md, docs/lizenzen.md). | Bei externer Speicherung verlangt der Disclaimer Versionsangabe und Kennzeichnung von Änderungen. |

### 4.2 ESS Runde 12 (Deutschland, Feld 2025/26)

Fundstellen: https://www.europeansocialsurvey.org/contact/disclaimer; https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf. Fassung: ESS-Disclaimer (HTML, SHA-256 8e0ded72…); CC-Legal-Code 4.0 (BY-NC-SA 527c4e0e…, BY-SA 47c0a954…); Quellfragebogen ESS12 HTTP 200; deutscher Fragebogen …/round12/fieldwork/germany/ESS12_questionnaires_DE.pdf HTTP 404. Abgerufen: 2026-10-03T22:49Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **C** | „European Social Survey documentation is licensed under CC BY-SA 4.0“ CC BY-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part; and produce, reproduce, and Share Adapted Material.“ | Der englische Quellfragebogen ist veröffentlicht und fällt unter die Dokumentationslizenz. Für Methodendokumente gilt dasselbe, sobald sie erscheinen. | Deutscher Fragebogen nicht veröffentlicht (HTTP 404, Stand 22:49 UTC). |
| (2) | **C** | „European Social Survey data is licensed under CC BY-NC-SA 4.0“ | Lizenzrahmen wie ESS 1–11. Tabellen gibt es noch nicht; laut ESS ist die erste Datenveröffentlichung für Januar 2027 geplant (R7 3.1). | Ob für ESS12 andere Bedingungen gelten, ist nicht angekündigt; bei Veröffentlichung erneut prüfen. |
| (3) | **C** | „European Social Survey data is licensed under CC BY-NC-SA 4.0“ CC BY-NC-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and produce, reproduce, and Share Adapted Material for NonCommercial purposes only.“ | Lizenzrahmen wie ESS 1–11, sobald die Daten erscheinen. | Daten noch nicht veröffentlicht; Bedingungen bei Veröffentlichung erneut prüfen. |
| (4) | **C** | wie (3) | Wie ESS 1–11. | Wie ESS 1–11; Daten noch nicht veröffentlicht. |
| (5) | **C** | wie (1) | Wie ESS 1–11, sobald der deutsche Fragebogen veröffentlicht ist. | Derzeit nicht möglich, weil der deutsche Wortlaut fehlt (HTTP 404). Eine eigene Übersetzung aus dem Quellfragebogen wäre kein Originalwortlaut. |
| (6) | **C** | CC BY-NC-SA 4.0, Abschnitt 2(a)(1): „reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and produce, reproduce, and Share Adapted Material for NonCommercial purposes only.“ „ESS ERIC recommends that ESS datasets are not made available on external websites. Instead, please link to datasets on the ESS Data Portal.“ | Wie ESS 1–11. | Wie ESS 1–11. |

### 4.3 GESIS-Bestände (GLES, ISSP, ALLBUS, Politbarometer, EVS, ZMSBw- und UBA-Daten); gesperrt

Fundstellen: https://www.gesis.org/institut/datennutzungsbedingungen (gelesen über web.archive.org/web/20260330121100/… und …/20260330154523/…/Nutzungsbedingungen.pdf laut R3, R5, R6). Fassung: GESIS-Nutzungsbedingungen „Gültig ab: 04.02.2026“, Wayback-Kopien vom 30.03.2026; GESIS-Impressum Wayback 09.09.2026 (laut R2, R3). Abgerufen: nicht neu abgerufen (GESIS-Sperre); Zitate aus R2 Abschnitt 6, R3 Abschnitt 3.2, R5 Abschnitt 3.3, R6 Abschnitt 3.3 (2026-10-03, ca. 19:30–21:20 UTC).

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | Präambel: „Die Originaldaten (im Folgenden „Datenbasis“) werden ausschließlich auf Grundlage dieser Nutzungsbedingungen bereitgestellt.“ § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“ | § 4 verbietet die KI-Verarbeitung der „Datenbasis“, die die Präambel als „Originaldaten“ bestimmt. Ob frei ladbare Fragebögen und Methodenberichte dazugehören, regeln die Bedingungen nicht (R5 3.3, R6 3.3). Das Impressum betrifft die Vervielfältigung in Publikationen, nicht das Lesen. | Klärung mit GESIS nötig. Bis dahin gilt die Projektsperre (AGENTS.md). R3, R5 und R6 haben solche Dokumente maschinell gelesen (R6 10.3). |
| (2) | **B** | Präambel: „Die Originaldaten (im Folgenden „Datenbasis“) werden ausschließlich auf Grundlage dieser Nutzungsbedingungen bereitgestellt.“ GESIS-Impressum: „Das Copyright für veröffentlichte, von GESIS selbst erstellte Objekte bleibt allein bei GESIS. Eine Vervielfältigung oder Verwendung solcher Grafiken, Tondokumente, Videosequenzen und Texte in anderen elektronischen oder gedruckten Publikationen ist ohne ausdrückliche Zustimmung von GESIS nicht gestattet.“ | GESIS veröffentlicht Häufigkeiten vor allem in Variablenberichten. Ob diese zur „Datenbasis“ gehören, ist wie bei (1) ungeregelt. | Wie (1). |
| (3) | **A** | § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“ | Die Regel verbietet die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis wörtlich. Eine Ausnahme ist nur auf Anfrage möglich, wenn der Nutzer das System allein kontrolliert und es ausschließlich wissenschaftlich nutzt. Das betrifft alle GESIS-Bestände einschließlich Eurobarometer-Einzeldaten, EVS, ZMSBw und UBA. | Ob von KI geschriebene, von Menschen ausgeführte Skripte unter das Verbot fallen, ist offen (R2 6, R3 3.3). ALLBUS 2023 braucht zusätzlich die Genehmigung des Datengebers (Kategorie C). |
| (4) | **B** | § 5: „Zulässig sind zusammenfassende Darstellungen der Daten, wie sie in wissenschaftlichen Arbeiten und Vorträgen üblich sind.“ § 1: „Soweit nicht ausdrücklich anders gekennzeichnet, stellt GESIS die Datenbasis nur für wissenschaftliche Nutzungen im Rahmen eines zeitlich befristeten Vorhabens zur Verfügung.“ | § 5 erlaubt zusammenfassende Darstellungen „wie … in wissenschaftlichen Arbeiten und Vorträgen üblich“. Ob eine dauerhafte öffentliche Website darunter fällt, regeln die Bedingungen nicht. Dazu kommen die Bindung an ein befristetes Vorhaben (§ 1), die Löschpflicht (§ 6) und die Anzeigepflicht (§ 8). | Schriftliche Klärung mit GESIS (R3 3.3). |
| (5) | **B** | GESIS-Impressum: „Das Copyright für veröffentlichte, von GESIS selbst erstellte Objekte bleibt allein bei GESIS. Eine Vervielfältigung oder Verwendung solcher Grafiken, Tondokumente, Videosequenzen und Texte in anderen elektronischen oder gedruckten Publikationen ist ohne ausdrückliche Zustimmung von GESIS nicht gestattet.“ | Das Impressum verlangt für die Verwendung von GESIS-eigenen Texten in anderen Publikationen eine Zustimmung. Ob einzelne Fragewortlaute solche Texte sind, ist offen. Für ISSP (ISSP Research Group), Politbarometer (Forschungsgruppe Wahlen) und Eurobarometer (EU) liegen die Rechte womöglich bei anderen. | Rechteinhaber je Studie klären. |
| (6) | **A** | § 4: „Eine Weitergabe der bereitgestellten Datenbasis an Dritte ist nicht gestattet.“ | Die Weitergabe der bereitgestellten Datenbasis an Dritte ist wörtlich untersagt. | Ob Dokumentationsdateien zur Datenbasis gehören, ist wie bei (1) offen. |

### 4.4 Eurobarometer: Veröffentlichungen der Europäischen Kommission (Berichte, Ergebnistabellen „Volumes“ auf data.europa.eu)

Fundstellen: https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32011D0833; https://commission.europa.eu/legal-notice_de; https://data.europa.eu/api/hub/search/datasets/<id>; https://data.europa.eu/en/legal-notice. Fassung: Beschluss 2011/833/EU, ABl. L 330 vom 14.12.2011, S. 39 (HTML SHA-256 dad161fa…); rechtlicher Hinweis der Kommission (SHA-256 8da7a495…, identisch mit R6); Lizenzfeld der Datensätze STD104, STD105, SP564, SP565, SP572 („COM_REUSE“) und SP527, SP529 („CC_BY_4_0“). Abgerufen: 2026-10-03T22:35Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **C** | Beschluss 2011/833/EU, Art. 4: „Alle Dokumente stehen zur Weiterverwendung zur Verfügung: a) für kommerzielle oder nichtkommerzielle Zwecke unter den in Artikel 6 festgelegten Bedingungen; b) gebührenfrei …; c) ohne Einzelbeantragung …“. Art. 3 Nr. 2: „„Weiterverwendung“: die Nutzung von Dokumenten durch natürliche oder juristische Personen für kommerzielle oder nichtkommerzielle Zwecke, die sich von den ursprünglichen Zwecken, für die die Dokumente erstellt wurden, unterscheiden.“ Rechtlicher Hinweis der Kommission: „Sofern nicht anders (z. B. in individuellen Copyright-Vermerken) angegeben, werden im Eigentum der Kommission befindliche Inhalte auf dieser Website zu den Bedingungen der Lizenz Creative Commons Attribution 4.0 International (CC BY 4.0) zur Verfügung gestellt. Dies bedeutet, dass die Weiterverwendung mit ordnungsgemäßer Nennung der Quelle und unter Hinweis auf Änderungen gestattet ist.“ | Methodendokumente der Kommission (Seite „About“, Technische Spezifikationen in den Berichten) sind Kommissionsdokumente. Ihre Nutzung ist nach Art. 4 ohne Antrag erlaubt; „Weiterverwendung“ umfasst jede Nutzung zu anderen als den ursprünglichen Zwecken. Bedingungen nach Art. 6 Abs. 2 und CC BY 4.0: Quelle nennen, Änderungen kennzeichnen, Sinn nicht verzerren. | Die Kommission veröffentlicht für 2022–2026 keine deutschen Fragebögen (R6 2.1). Technische Spezifikationen stehen in Berichten mit Ergebnissen; sie dürften nur nach einem ergebnisblinden Verfahren gelesen werden. |
| (2) | **C** | data.europa.eu, Lizenzfeld je Datensatz: {"id": "COM_REUSE", "label": "European Commission reuse notice", "resource": "http://data.europa.eu/eli/dec/2011/833/oj"} (STD104, STD105, SP564, SP565, SP572); "CC_BY_4_0" (SP527, SP529). Beschluss 2011/833/EU, Art. 4: „Alle Dokumente stehen zur Weiterverwendung zur Verfügung: a) für kommerzielle oder nichtkommerzielle Zwecke unter den in Artikel 6 festgelegten Bedingungen; b) gebührenfrei …; c) ohne Einzelbeantragung …“. Art. 3 Nr. 2: „„Weiterverwendung“: die Nutzung von Dokumenten durch natürliche oder juristische Personen für kommerzielle oder nichtkommerzielle Zwecke, die sich von den ursprünglichen Zwecken, für die die Dokumente erstellt wurden, unterscheiden.“ Art. 6 Abs. 2: „a) die Verpflichtung des Nutzers, die Quelle des Dokuments anzugeben; b) die Verpflichtung, die ursprüngliche Bedeutung oder Botschaft des Dokuments nicht verzerrt darzustellen; c) den Haftungsausschluss der Kommission für jegliche Folgen der Weiterverwendung.“ | Die Volumes tragen die Lizenzangabe „European Commission reuse notice“ mit Verweis auf den Beschluss oder CC BY 4.0. Beide erlauben die Nutzung einschließlich maschineller Verarbeitung ohne Einzelantrag. Bedingungen: Quelle nennen, ursprüngliche Bedeutung nicht verzerren, Haftungsausschluss, bei CC BY Änderungen kennzeichnen. | Fragen aus Modulen des Europäischen Parlaments: Dessen Hinweis verlangt laut R6 3.2 die Wiedergabe des ganzen Elements und bei Teilwiedergabe den Link. Ausschluss nach Art. 2 Abs. 2 Buchst. b (geistiges Eigentum Dritter) ist bei den geprüften Datensätzen nicht vermerkt. |
| (3) | **A** | § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“ | Die Kommission veröffentlicht keine Einzeldaten (R6 2.1: Dateitypen SAVRAW und CSVRAW existieren, sind ab 2022 aber nicht belegt). Der einzige Weg führt über GESIS, deren § 4 die KI-Verarbeitung verbietet. | Siehe Eintrag „Eurobarometer über GESIS“. |
| (4) | **C** | Beschluss 2011/833/EU, Art. 4: „Alle Dokumente stehen zur Weiterverwendung zur Verfügung: a) für kommerzielle oder nichtkommerzielle Zwecke unter den in Artikel 6 festgelegten Bedingungen; b) gebührenfrei …; c) ohne Einzelbeantragung …“. Art. 3 Nr. 2: „„Weiterverwendung“: die Nutzung von Dokumenten durch natürliche oder juristische Personen für kommerzielle oder nichtkommerzielle Zwecke, die sich von den ursprünglichen Zwecken, für die die Dokumente erstellt wurden, unterscheiden.“ Art. 6 Abs. 2: „a) die Verpflichtung des Nutzers, die Quelle des Dokuments anzugeben; b) die Verpflichtung, die ursprüngliche Bedeutung oder Botschaft des Dokuments nicht verzerrt darzustellen; c) den Haftungsausschluss der Kommission für jegliche Folgen der Weiterverwendung.“ Rechtlicher Hinweis der Kommission: „Sofern nicht anders (z. B. in individuellen Copyright-Vermerken) angegeben, werden im Eigentum der Kommission befindliche Inhalte auf dieser Website zu den Bedingungen der Lizenz Creative Commons Attribution 4.0 International (CC BY 4.0) zur Verfügung gestellt. Dies bedeutet, dass die Weiterverwendung mit ordnungsgemäßer Nennung der Quelle und unter Hinweis auf Änderungen gestattet ist.“ | Die Weiterverwendung für nichtkommerzielle Zwecke ist ohne Antrag erlaubt. Bedingungen: Quelle nennen, Sinn nicht verzerren (Art. 6 Abs. 2 Buchst. b), Haftungsausschluss; keine Weiterverwendung zur Täuschung (Art. 2 Abs. 4). | Das Verzerrungsverbot betrifft auch die Darstellung: Eine Frage zur EU-Ebene darf nicht als Haltung zur deutschen Politik erscheinen (Abschnitt 5 des Berichts). |
| (5) | **B** | GESIS-Seite „Data & Documentation“ laut R6 3.3: „Eurobarometer questionnaires are reproduced with the licence granted by the European Commission, DG Communication … (© European Communities).“ Beschluss 2011/833/EU, Art. 2 Abs. 1: gilt für öffentliche Dokumente, „die von der Kommission oder von öffentlichen und privaten Stellen in ihrem Namen erstellt werden“. | Die Rechte an den Fragetexten liegen bei der EU. Fragebögen, die in ihrem Auftrag entstanden sind, fallen nach Art. 2 Abs. 1 grundsätzlich unter den Beschluss. Die Kommission hat die deutschen Fassungen aber nicht selbst veröffentlicht; zugänglich sind nur GESIS-Kopien. Ob deutsche Datenanhänge der Kommission den vollständigen Feldwortlaut enthalten, ist ungeprüft, weil sie Ergebnisse zeigen. | Bestätigung durch das Eurobarometer-Team (R6 8) oder ergebnisblinde Strukturprüfung der deutschen Datenanhänge durch einen getrennten Agenten. |
| (6) | **C** | wie (1) | Der Beschluss enthält keine Weitergabebeschränkung; CC BY 4.0 erlaubt das Teilen. Bedingungen wie bei (2). | – |

### 4.5 Eurobarometer über GESIS (Einzeldaten, deutsche Länderfragebögen, Basisfragebögen); gesperrt

Fundstellen: https://www.gesis.org/institut/datennutzungsbedingungen (gelesen über web.archive.org/web/20260330121100/… und …/20260330154523/…/Nutzungsbedingungen.pdf laut R3, R5, R6). Fassung: GESIS-Nutzungsbedingungen „Gültig ab: 04.02.2026“, Wayback-Kopien vom 30.03.2026; GESIS-Impressum Wayback 09.09.2026 (laut R2, R3); Zugangskategorie „0“/„Open“ laut R6 2.2 und 3.3. Abgerufen: nicht neu abgerufen (GESIS-Sperre); Zitate aus R2 Abschnitt 6, R3 Abschnitt 3.2, R5 Abschnitt 3.3, R6 Abschnitt 3.3 (2026-10-03, ca. 19:30–21:20 UTC).

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | Präambel: „Die Originaldaten (im Folgenden „Datenbasis“) werden ausschließlich auf Grundlage dieser Nutzungsbedingungen bereitgestellt.“ GESIS-Seite „Data & Documentation“ laut R6 3.3: „Eurobarometer questionnaires are reproduced with the licence granted by the European Commission, DG Communication … (© European Communities).“ Beschluss 2011/833/EU, Art. 2 Abs. 1: gilt für öffentliche Dokumente, „die von der Kommission oder von öffentlichen und privaten Stellen in ihrem Namen erstellt werden“. | Die deutschen Fragebögen lassen sich laut R6 ohne Anmeldung laden. Ob sie zur „Datenbasis“ zählen, ist offen; die Rechte an den Texten liegen bei der EU. | Projektsperre bis zur Klärung mit GESIS. |
| (2) | **B** | Präambel: „Die Originaldaten (im Folgenden „Datenbasis“) werden ausschließlich auf Grundlage dieser Nutzungsbedingungen bereitgestellt.“ | GESIS veröffentlicht keine eigenen Eurobarometer-Ergebnistabellen außer Variablenberichten; deren Status ist wie bei GESIS (2) offen. | Für Tabellen ist der Weg über die Kommission vorzuziehen. |
| (3) | **A** | § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“ § 3: „Für jede Bereitstellung der Datenbasis durch GESIS ist die Registrierung und die Zustimmung zu diesen Nutzungsbedingungen durch den Nutzer / die Nutzerin erforderlich.“ | Auch die Kategorie „Open“ verlangt Registrierung und Zustimmung; § 4 gilt ohne Vorbehalt (R6 3.3). | Ausnahme nur auf Anfrage bei GESIS. |
| (4) | **B** | § 5: „Zulässig sind zusammenfassende Darstellungen der Daten, wie sie in wissenschaftlichen Arbeiten und Vorträgen üblich sind.“ § 1: „Soweit nicht ausdrücklich anders gekennzeichnet, stellt GESIS die Datenbasis nur für wissenschaftliche Nutzungen im Rahmen eines zeitlich befristeten Vorhabens zur Verfügung.“ | Wie GESIS (4). | Wie GESIS (4). |
| (5) | **B** | GESIS-Seite „Data & Documentation“ laut R6 3.3: „Eurobarometer questionnaires are reproduced with the licence granted by the European Commission, DG Communication … (© European Communities).“ Beschluss 2011/833/EU, Art. 2 Abs. 1: gilt für öffentliche Dokumente, „die von der Kommission oder von öffentlichen und privaten Stellen in ihrem Namen erstellt werden“. GESIS-Impressum: „Das Copyright für veröffentlichte, von GESIS selbst erstellte Objekte bleibt allein bei GESIS. Eine Vervielfältigung oder Verwendung solcher Grafiken, Tondokumente, Videosequenzen und Texte in anderen elektronischen oder gedruckten Publikationen ist ohne ausdrückliche Zustimmung von GESIS nicht gestattet.“ | Rechte bei der EU, Bezugsquelle GESIS. Ob GESIS für die Anzeige eine Zustimmung beansprucht, ist offen. | Klärung mit der Kommission und gegebenenfalls GESIS. |
| (6) | **A** | § 4: „Eine Weitergabe der bereitgestellten Datenbasis an Dritte ist nicht gestattet.“ | Wörtliches Weitergabeverbot für die Datenbasis. | – |

### 4.6 World Values Survey (WVSA, worldvaluessurvey.org), insbesondere Welle 7 Deutschland 2017/18

Fundstellen: https://www.worldvaluessurvey.org/AJDownloadLicense.jsp?DOID=6609. Fassung: Formular „Conditions of Use“ zur Datei „WVS7 Questionnaire Germany 2017 German.pdf“ (HTML SHA-256 831617d5…); Wortlaut identisch mit R5 3.1. Abgerufen: 2026-10-03T22:34Z (Formular nicht abgeschickt).

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **C** | „These data files are available without restrictions, provided: a) that they are used for non-profit purposes; b) correct citations are provided and sent to the World Values Survey Association for each publication of results based in part or entirely on these data files; c) the data files themselves are not redistributed; d) proper citation to the WVS data is included into the references list of the publication …“ | Dieselben „Conditions of Use“ gelten für jeden Download, auch für den deutschen Fragebogen (DOID 6609). Sie stellen die Dateien „without restrictions“ bereit, solange die Bedingungen a bis d erfüllt sind. Das Lesen durch einen Agenten ist eine solche Nutzung. Bedingungen: Steven füllt das Formular aus und stimmt zu (Name, Institution, E-Mail, Projekttitel, Zweck), nicht gewinnorientierte Nutzung, Zitation. | „non-profit purposes“ ist nicht definiert. Die Bedingungen sprechen von „data files“; ob Fragebogen-PDFs gemeint sind, ist nicht ausdrücklich gesagt. Die von R5 genutzten IHSN-Kopien tragen „All Rights Reserved“; für diesen Weg wäre die Lage ungeklärt. |
| (2) | **C** | wie (1) | Ergebnisberichte werden laut WVS-Seite „Documentation“ ebenfalls über die Registrierung und die „non-redistribution data use license“ abgegeben (R5 2). Es gelten dieselben Bedingungen. | Wie (1). |
| (3) | **C** | wie (1) | Die Bedingungen erlauben die Nutzung der Datendateien ohne weitere Einschränkung, solange sie nicht gewinnorientiert ist, zitiert, gemeldet und nicht weitergegeben wird. Eine Unterscheidung nach Werkzeugen gibt es nicht. | Definition „non-profit“; bei der gemeinsamen EVS/WVS-Datei ist offen, ob GESIS-Bedingungen für den EVS-Teil gelten (R5 3.4) – diesen Weg nicht nutzen. |
| (4) | **C** | wie (1) | Bedingung b setzt die „publication of results“ voraus und knüpft sie an Zitation und Meldung an die WVSA. Das präzisiert R5 3.1, wo die Website-Nutzung als „nicht ausdrücklich geregelt“ vermerkt ist. | Wie eine dauerhaft geänderte Website gemeldet und zitiert wird, sollte mit der WVSA abgestimmt werden. |
| (5) | **B** | „These data files are available without restrictions, provided: a) that they are used for non-profit purposes; b) correct citations are provided and sent to the World Values Survey Association for each publication of results based in part or entirely on these data files; c) the data files themselves are not redistributed; d) proper citation to the WVS data is included into the references list of the publication …“ Seitenfuß: „Copyright @2020 World Values Survey Association“ (R5 3.1). | Die Bedingungen regeln nur Datendateien und Ergebnisse, nicht die Wiedergabe von Fragetexten. Der deutsche Fragebogen entstand für GESIS (R5 4); wer die Rechte an der Übersetzung hält, ist offen. | Klärung mit der WVSA (R5 11). |
| (6) | **A** | „c) the data files themselves are not redistributed;“ | Die Weitergabe der Datendateien ist wörtlich ausgeschlossen. | – |

### 4.7 OECD Risks that Matter (RTM) und OECD-Nutzungsbedingungen

Fundstellen: https://www.oecd.org/en/about/terms-conditions.html (live HTTP 403; gelesen über web.archive.org/web/20261003064505id_/…); https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf; https://webfs.oecd.org/Els-com/RtM/OECD-Risks-That-Matter-2022-Core-Questionnaire.pdf. Fassung: OECD Terms and Conditions, Wayback-Kopie vom 03.10.2026 06:45 UTC (SHA-256 280015a7…); RTM-Kernfragebögen 2024 (5672381901f57dcc…) und 2022 (9ad7870bc403f6c4…); Working Paper 324 (bd09930f1c601989…). Abgerufen: 2026-10-03T22:36Z–22:37Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | Abschnitt 1.1: „most OECD written content published as of 1 July 2024 is licensed under a Creative Commons Attribution BY 4.0 licence (CC BY 4.0).“ – „Some OECD written content may be licensed under different terms. You should always check the copyright notice of the written content to confirm which licence applies.“ Kernfragebogen 2022: Vermerk „Restricted Use – À usage restreint“ (19 Fundstellen); Kernfragebogen 2024: kein Lizenz- oder Copyright-Vermerk. Working Paper 324: „This work is made available under the Creative Commons Attribution 4.0 International licence.“ | Das Methodenpapier steht ausdrücklich unter CC BY 4.0 (für sich Klasse C). Für die Fragebögen gilt „most … content“ nur als Regelfall; der Fragebogen 2022 trägt einen Einschränkungsvermerk, der von 2024 gar keinen. Die Regel ist für den notwendigen Teil also nicht eindeutig. | Lizenz der Fragebögen bei der OECD bestätigen lassen. |
| (2) | **C** | Abschnitt 3, Permitted Use: „Except where additional restrictions apply as stated above, you can extract from, download, copy, adapt, print, distribute, share and embed Data for any purpose, even for commercial use. You must give appropriate credit to the OECD …“ | Für OECD-Daten erlaubt Abschnitt 3 Herunterladen, Kopieren, Bearbeiten und Teilen für jeden Zweck. Bedingungen: OECD mit der zugehörigen Zitation nennen, Quellenpflicht an Unterlizenzen weitergeben, Einschränkungen in den Metadaten prüfen. | Ob die veröffentlichten RTM-„Statlinks“ als „Data“ gelten und Deutschland nach allen Kategorien ausweisen, ist ungeprüft (Ergebnisblindheit, R7 7). |
| (3) | **B** | Working Paper 324, PDF-S. 21–22: „use of the public use microdata files is protected and governed by specified terms and conditions, including that: users must prevent any and all actions aimed at or likely to result in the re-identification …; users must implement appropriate measures to secure the data; users are prohibited from the presentation or publication of individual entries …“ Datenseite laut R7 3.2: „To request access to the anonymised Public Use Microdata, please contact …“ | Die Bedingungen für die Mikrodaten sind nur als Auszug bekannt; Zugang auf Anfrage. Ob die Pflicht zur Datensicherung eine Verarbeitung durch Cloud-Agenten ausschließt, ist offen. | Vollständige PUF-Bedingungen anfordern (Anfrage braucht Stevens Freigabe). |
| (4) | **C** | wie (2) | Für Anteile aus veröffentlichten OECD-Daten gilt Abschnitt 3. Werden Anteile aus den Mikrodaten berechnet, gilt Klasse B wie bei (3). | Eignung der Tabellen und Online-Quotenstichprobe 18–64 sind methodische, keine rechtlichen Fragen (R7 3.2). |
| (5) | **B** | Abschnitt 1.1: „most OECD written content published as of 1 July 2024 is licensed under a Creative Commons Attribution BY 4.0 licence (CC BY 4.0).“ – „Some OECD written content may be licensed under different terms. You should always check the copyright notice of the written content to confirm which licence applies.“ | Einen deutschen Fragebogen hat die OECD nicht veröffentlicht (R7 3.2). Ohne Freigabe einer deutschen Fassung gibt es keinen Originalwortlaut, dessen Lizenz man prüfen könnte. | OECD um die deutsche Fassung und ihre Lizenz bitten. |
| (6) | **C** | wie (2) | Veröffentlichte Daten dürfen geteilt und verbreitet werden (Abschnitt 3). | Für die Mikrodaten sind Weitergaberegeln unbekannt. |

### 4.8 Eurofound (Website) und UK Data Service (Endnutzerlizenz für Eurofound-Daten)

Fundstellen: https://www.eurofound.europa.eu/en/legal-information (live HTTP 429; Wayback 20250725103733); https://ukdataservice.ac.uk/app/uploads/cd137-enduserlicence.pdf. Fassung: Eurofound „Legal information“, Wayback 25.07.2025 („© … Eurofound, 2025“); UKDS End User Licence „CD137-EndUserLicence_16.00w“, Version 16.00, PDF erstellt 17.04.2026, geändert 29.04.2026 (SHA-256 3b4f64ad…, identisch mit R7). Abgerufen: 2026-10-03T22:37Z–22:38Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **C** | Eurofound: „The reuse of any information of this website is authorised for commercial and non-commercial purposes, under the following conditions: The re-user is obliged to acknowledge the source of the document. The original meaning or the message of the documents should not be distorted. Eurofound cannot be held liable for any consequence stemming from the reuse.“ Wiederverwendung ist definiert als „reproduction of textual data and multimedia items which are the property of Eurofound or of third parties and for which Eurofound holds the rights of use“. | Fragebögen und Methodendokumente auf der Eurofound-Website dürfen mit Quellenangabe und ohne Sinnentstellung vervielfältigt werden; das deckt das Lesen durch Agenten. | Werden dieselben Dokumente über das UKDS unter der Endnutzerlizenz bezogen, gilt dort Nr. 5 (die „Data Collection“ umfasst laut Definition „Dataset(s), Documentation, Metadata“), also Klasse A. Live-Seite HTTP 429; Fassung von 2025. |
| (2) | **C** | Eurofound: „The reuse of any information of this website is authorised for commercial and non-commercial purposes, under the following conditions: The re-user is obliged to acknowledge the source of the document. The original meaning or the message of the documents should not be distorted. Eurofound cannot be held liable for any consequence stemming from the reuse.“ | Von Eurofound veröffentlichte Ergebnisse dürfen mit Quellenangabe weiterverwendet werden. | Wie (1). |
| (3) | **A** | EUL Abschnitt 5 Nr. 5: „To abstain from using any Online Data Tools in connection with your use of the Data Collection(s), unless explicit written permission is granted by the Data Service Provider.“ Definition: „Online Data Tools: Any software, application, system or platform that operates via the internet or a cloud-based service and is used to process, analyse, manipulate or generate data and other types of content, including but not limited to tools that employ ‘artificial intelligence’ (AI) technologies …“ | Die Lizenz verbietet den Einsatz internetgestützter oder cloudbasierter Werkzeuge einschließlich KI im Zusammenhang mit der Datennutzung, außer mit schriftlicher Erlaubnis. | „in connection with your use“ ist weit gefasst; ob auch von KI geschriebene, lokal ausgeführte Skripte darunter fallen, ist offen. |
| (4) | **C** | Eurofound: „The reuse of any information of this website is authorised for commercial and non-commercial purposes, under the following conditions: The re-user is obliged to acknowledge the source of the document. The original meaning or the message of the documents should not be distorted. Eurofound cannot be held liable for any consequence stemming from the reuse.“ EUL Nr. 11: Pflicht, in „any publication, whether printed, electronic or broadcast“ Datenurheber und Bereitsteller zu nennen. | Anteile aus von Eurofound veröffentlichten Ergebnissen sind mit Quellenangabe zulässig. Die Endnutzerlizenz setzt Veröffentlichungen voraus (Nr. 8, 11, 12) und verlangt Zitation, Meldung der Bibliografie und Geheimhaltungsregeln. | Werden Anteile aus UKDS-Daten berechnet, darf das nicht mit KI-Werkzeugen geschehen (siehe (3)). |
| (5) | **C** | Eurofound: „The reuse of any information of this website is authorised for commercial and non-commercial purposes, under the following conditions: The re-user is obliged to acknowledge the source of the document. The original meaning or the message of the documents should not be distorted. Eurofound cannot be held liable for any consequence stemming from the reuse.“ Seite „About Eurofound's surveys“ laut R7: „The methodology and questionnaires used in Eurofound's pan-European surveys are freely available for use by other researchers, subject to certain copyright conditions“. | Fragebögen auf der Eurofound-Website fallen unter die Wiederverwendungsregel (Quellenangabe, keine Sinnentstellung). | Ob der deutsche EQLS-2016-Fragebogen auf der Eurofound-Website liegt oder nur beim UKDS, ist ungeprüft (R7 3.5); „certain copyright conditions“ ist nicht näher bestimmt. |
| (6) | **A** | EUL Abschnitt 5 Nr. 4: „Not to give access to the Data Collection(s), in whole or in part, or to any Dataset(s) derived from the Data Collection(s) (including synthetic Dataset(s)), except to Registered Users …“ | Die Weitergabe der Datensammlung und abgeleiteter Datensätze ist außer an registrierte Nutzende wörtlich ausgeschlossen. | Für Dokumente von der Eurofound-Website gilt die Wiederverwendungsregel (Klasse C). |

### 4.9 Pew Research Center, Global Attitudes Survey

Fundstellen: https://www.pewresearch.org/about/terms-and-conditions/. Fassung: Terms of Use, „Effective Date: 05/25/2018“ (HTML SHA-256 d0be6b87…). Abgerufen: 2026-10-03T22:38Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **C** | Abschnitt 1: „you may access, print, copy, reproduce, cite, link, display, download, distribute, broadcast, transmit, publish, license, transfer, sell, modify, create derivatives of, or otherwise exploit the Content, provided that all copies display all copyright and other applicable notices … and provided further that you do not use the Content in any manner that implies … a Center endorsement …“ | Die Nutzungslizenz für „Content“ erlaubt Kopieren, Vervielfältigen und jede sonstige Verwertung mit Copyright-Hinweisen und ohne Anschein einer Billigung. | Öffentliche Fragetexte stehen nur in Topline-Dokumenten mit Ergebnissen (R7 3.3); Lesen nur nach ergebnisblindem Verfahren. Abschnitt 3 verbietet „unauthorized automated means to compile information“; Dateien sollten daher nicht von Agenten gesammelt, sondern einzeln bezogen werden (Vermutung). |
| (2) | **C** | wie (1) | Wie (1). | Wie (1). |
| (3) | **C** | Abschnitt 13: „license to access, copy, reproduce, cite, link, display, download, distribute, broadcast, transmit, publish, modify, create derivatives of, or otherwise exploit the survey datasets …, provided that: any reproduction, display, distribution, broadcast, transmission, or publication of the Data is limited to excerpts and may not be reproduced, displayed, distributed, broadcast, transmitted, or published in full or substantially in full …“ Abschnitt 13: „you must include the following disclaimer with your use of any Data: “Pew Research Center bears no responsibility for the analyses or interpretations of the data presented here. …”“ | Abschnitt 13 lizenziert Datensätze ausdrücklich zur Vervielfältigung, Bearbeitung und sonstigen Verwertung. Bedingungen: Konto mit Zustimmung zu den Bedingungen (Steven), nur Auszüge weitergeben, Hinweise erhalten, Zitation, Pflicht-Haftungsausschluss, keine Reidentifikation (Abschnitt 14). | Ob das Konto zusätzliche Bedingungen enthält, ist ohne Anmeldung nicht prüfbar. Parteivariable und deutscher Fragebogen im Datenpaket ungeprüft. |
| (4) | **C** | wie (3) | Veröffentlichung von Auszügen ist erlaubt. Bedingungen: Zitation nach Abschnitt 2, Haftungsausschluss im Wortlaut, kein Anschein einer Billigung. | – |
| (5) | **B** | Abschnitt 1: „you may access, print, copy, reproduce, cite, link, display, download, distribute, broadcast, transmit, publish, license, transfer, sell, modify, create derivatives of, or otherwise exploit the Content, provided that all copies display all copyright and other applicable notices … and provided further that you do not use the Content in any manner that implies … a Center endorsement …“ Für Übersetzungen ist der Hinweis „Pew Research Center has published the original content in English but has not reviewed or approved this translation.“ Pflicht (R7 3.3). | Ein öffentlicher deutscher Fragebogen wurde nicht gefunden. Eine eigene Übersetzung wäre kein Originalwortlaut. | Prüfen, ob Datenpakete den deutschen Fragebogen enthalten. |
| (6) | **A** | Abschnitt 13: „license to access, copy, reproduce, cite, link, display, download, distribute, broadcast, transmit, publish, modify, create derivatives of, or otherwise exploit the survey datasets …, provided that: any reproduction, display, distribution, broadcast, transmission, or publication of the Data is limited to excerpts and may not be reproduced, displayed, distributed, broadcast, transmitted, or published in full or substantially in full …“ Abschnitt 1: „Under no circumstances may the Content be reproduced in principal part, mirrored, catalogued, framed, displayed simultaneously with another site or otherwise republished in its entirety or in principal part without the express written permission of the Center …“ | Die Weitergabe vollständiger oder wesentlicher Teile der Daten und Inhalte ist wörtlich ausgeschlossen; nur Auszüge sind erlaubt. | – |

### 4.10 Europäische Investitionsbank, Climate Survey

Fundstellen: https://www.eib.org/en/terms-of-use.htm; https://www.eib.org/en/publications-research/eib-open-data. Fassung: EIB Terms of use (HTML SHA-256 47aa5d5b…); Seite „EIB open data“ (cb76a612…). Abgerufen: 2026-10-03T22:38Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | „You may not modify, publish, transmit, display, participate in the transfer or sale, create derivative works, or in any way commercially exploit the content of this website without the express prior written permission of EIB and/or the copyright owner or except as otherwise expressly permitted under copyright law.“ | Lesen und Auswerten sind nicht aufgezählt. Ob die Übermittlung an einen KI-Anbieter als „transmit“ gilt, ist offen. | Fragebögen nur englisch (R7 3.4). |
| (2) | **B** | wie (1) | Wie (1). | Wie (1). |
| (3) | **B** | „You may not modify, publish, transmit, display, participate in the transfer or sale, create derivative works, or in any way commercially exploit the content of this website without the express prior written permission of EIB and/or the copyright owner or except as otherwise expressly permitted under copyright law.“ Seite „EIB open data“: „All of this data is openly available to the public.“ | Die Einzeldaten sind frei ladbar, aber ohne eigene Lizenz. „openly available“ beschreibt den Zugang, keine Nutzungserlaubnis. Ob Auswertungen „derivative works“ sind, ist offen. | Schriftliche Klärung mit der EIB. |
| (4) | **A** | wie (1) | Veröffentlichen, Anzeigen und Bearbeiten von Inhalten der Website sind ohne vorherige schriftliche Erlaubnis wörtlich untersagt. | Ob gesetzliche Schranken für einzelne Zahlen greifen („except as otherwise expressly permitted under copyright law“), ist eine Rechtsfrage. |
| (5) | **A** | wie (1) | Anzeige von Fragetexten ist „display“ von Website-Inhalten. Außerdem gibt es keine deutsche Fassung. | – |
| (6) | **A** | wie (1) | „transmit, participate in the transfer“ ist ohne Erlaubnis untersagt. | – |

### 4.11 ifo Bildungsbarometer (LMU-ifo Economics & Business Data Center, EBDC)

Fundstellen: https://www.ifo.de/ebdc-datensaetze/ifo-bildungsbarometer-2021-suf (live Bot-Prüfung; Wayback 20240603090649); Vertragsvorlage https://www.ifo.de/sites/default/files/ebdc-data-secure/bibaro/20220908%20Datennutzungsvertrag%20Bildungsbarometer.docx. Fassung: Datensatzseite ifo Bildungsbarometer 2021 SUF, Wayback 03.06.2024; „Datennutzungsvertrag zur Nutzung der Daten des ifo Bildungsbarometers für externe Datennutzer*innen (Scientific Use File)“, Dateiname mit Datum 08.09.2022 (DOCX SHA-256 c9ded2f9…). Abgerufen: 2026-10-03T22:41Z–22:42Z (Vertragsvorlage über das Abrufwerkzeug als Datei gespeichert, Text lokal aus der DOCX gelesen).

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | „Die Nutzung der Daten des ifo Bildungsbarometers ist nur für wissenschaftliche Zwecke bestimmt. … Für die Datennutzung muss ein projektspezifischer Nutzungsantrag beim EBDC gestellt werden. … Das Codebuch steht unten zum Download bereit.“ | Für Working Paper, Codebuch und ReadMe habe ich keine Lizenz gefunden. Die Zweckbindung bezieht sich auf die Daten. | Live-Seiten hinter Bot-Prüfung; Stand der Wayback-Kopie 2024. |
| (2) | **B** | wie (1) | Für veröffentlichte Ergebnisse des ifo Instituts habe ich keine Nutzungsregel geprüft. | ifo-Nutzungsbedingungen der Website nicht erreichbar. |
| (3) | **B** | Vertrag § 1: „Die vom EBDC zur Verfügung gestellten Daten werden ausschließlich für wissenschaftliche Zwecke verwendet.“ – „Der*die Datenempfangende verpflichtet sich, die Daten nicht, auch nicht in modifizierter Form, an Dritte weiterzugeben oder diesen zugänglich zu machen.“ | KI ist nicht erwähnt. Ob die Verarbeitung durch einen Cloud-Agenten die Daten „Dritten zugänglich“ macht, ist eine Auslegungsfrage. Der Vertrag setzt eine „Wissenschaftliche Einrichtung“ und die Unterschrift einer vorgesetzten Forschungsbereichsleitung voraus. | Ob Steven ohne wissenschaftliche Einrichtung Vertragspartner sein kann; Klärung beim EBDC. |
| (4) | **B** | Vertrag § 3: „Alle aus den Daten resultierenden Publikationen sind dem EBDC zur Prüfung vorzulegen, bevor sie veröffentlicht werden.“ Vertrag § 1: „Die vom EBDC zur Verfügung gestellten Daten werden ausschließlich für wissenschaftliche Zwecke verwendet.“ – „Der*die Datenempfangende verpflichtet sich, die Daten nicht, auch nicht in modifizierter Form, an Dritte weiterzugeben oder diesen zugänglich zu machen.“ | Veröffentlichungen brauchen eine vorherige Prüfung durch das EBDC; Nutzung nur für wissenschaftliche Zwecke. Ob eine öffentliche Website wissenschaftlich ist, ist offen. | – |
| (5) | **B** | wie (1) | Die deutschen Wortlaute stehen laut R7 im Codebuch. Die Wayback-Kopie verlinkt das Codebuch öffentlich; eine Lizenz fehlt. | Codebuch nicht geöffnet (kann Häufigkeiten enthalten). |
| (6) | **A** | wie (3) | Weitergabe an Dritte, auch in modifizierter Form, ist vertraglich ausgeschlossen. | – |

### 4.12 RIFS Potsdam / Kopernikus-Projekt Ariadne, Soziales Nachhaltigkeitsbarometer

Fundstellen: https://www.rifs-potsdam.de/de/impressum; https://ariadneprojekt.de/impressum/; https://www.rifs-potsdam.de/en/output/publications/2022/soziales-nachhaltigkeitsbarometer-der-energie-und-verkehrswende-2021-daten. Fassung: RIFS-Impressum (HTML SHA-256 b6e0af5f…); Ariadne-Impressum (840b018c…); Publikationsseite Daten- und Methodenbericht 2021. Abgerufen: 2026-10-03T22:42Z–22:43Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | RIFS-Impressum: „Copyright: GFZ Helmholtz-Zentrum für Geoforschung; Alle Rechte vorbehalten.“ – „Texte, Bilder, Grafiken, Sound und Videos sowie deren Anordnung auf der Website des RIFS Potsdam unterliegen dem Schutz des Urheberrechts und anderer Schutzgesetze.“ Daten- und Methodenbericht 2021 laut R7: „Der Fragebogen ist frei zugänglich“. | „frei zugänglich“ beschreibt den Zugang, keine Nutzungserlaubnis. Eine Lizenz habe ich weder im Fragebogen (R7) noch in den Impressen von RIFS und Ariadne gefunden. | Anfrage beim RIFS (Freigabe durch Steven). |
| (2) | **B** | wie (1) | Wie (1). | Wie (1). |
| (3) | **B** | FDZ Ruhr laut R7: „The data sets are available free of charge for scientific purposes as a Scientific Use File (SUF) Off-site.“ (nur Wellen 2017–2019) | Für 2021–2023 ist kein Datenzugang belegt; der SUF-Vertrag für 2017–2019 ist nicht gesehen. | FDZ-Ruhr-Seite um 22:43 UTC nicht erreichbar. |
| (4) | **B** | wie (1) | Keine Nutzungsregel für Ergebnisse gefunden. | – |
| (5) | **B** | wie (1) | Deutsche Wortlaute öffentlich, aber ohne Lizenz. | – |
| (6) | **B** | wie (1) | Keine Regel gefunden; „Alle Rechte vorbehalten“ gilt für die Website. | – |

### 4.13 Statistisches Bundesamt (Destatis) und Forschungsdatenzentren der Statistischen Ämter

Fundstellen: https://www.destatis.de/DE/Service/Impressum/copyright-allgemein.html; https://www.destatis.de/DE/Service/Impressum/copyright-genesis-online.html; https://www.govdata.de/dl-de/by-2-0; https://www.forschungsdatenzentrum.de/de/zugang. Fassung: Copyright allgemein (d8ccbd4a…), Copyright Genesis-Online (c3dafa09…), Datenlizenz Deutschland – Namensnennung – Version 2.0, FDZ-Seite „Zugang“. Abgerufen: 2026-10-03T22:43Z–22:44Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **C** | Copyright allgemein: „Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellennachweis gestattet.“ – „Die Weiterverwendung ist sowohl für nicht gewerbliche als auch gewerbliche Zwecke erlaubt. … Es bedarf keiner ausdrücklichen Genehmigung durch unser Haus. Eine Quellenangabe ist jedoch erforderlich.“ | Veröffentlichungen und Website-Inhalte dürfen mit Quellenangabe vervielfältigt und weiterverwendet werden. Bedingungen: Destatis als Herausgeber nennen, Änderungen kenntlich machen, Rechte Dritter beachten. | Destatis erhebt keine politischen Einstellungen; die Quelle ist nur für Kontext oder Bevölkerungsrandwerte relevant. |
| (2) | **C** | dl-de/by-2-0: „(1) Jede Nutzung ist unter den Bedingungen dieser „Datenlizenz Deutschland – Namensnennung – Version 2.0“ zulässig. Die bereitgestellten Daten und Metadaten dürfen für die kommerzielle und nicht kommerzielle Nutzung insbesondere vervielfältigt, ausgedruckt, präsentiert, verändert, bearbeitet sowie an Dritte übermittelt werden …“ | GENESIS-Tabellen stehen unter dl-de/by-2-0, die jede Nutzung einschließlich Bearbeitung und Übermittlung an Dritte erlaubt. Bedingungen: Quellenvermerk mit Lizenzhinweis und Link, Änderungen kennzeichnen. | – |
| (3) | **B** | FDZ: „Gemäß § 16 (6) des Bundesstatistikgesetzes (BStatG) dürfen die Forschungsdatenzentren nur „Hochschulen oder sonstigen Einrichtungen mit der Aufgabe unabhängiger wissenschaftlicher Forschung“ einen Zugang zu amtlichen Mikrodaten gewähren.“ | Zugang zu Mikrodaten nur für Hochschulen und unabhängige Forschungseinrichtungen. Die Vertragsbedingungen der Scientific Use Files einschließlich möglicher KI- oder Cloud-Regeln habe ich nicht gesehen. | Ohne wissenschaftliche Einrichtung kein Zugang. |
| (4) | **C** | dl-de/by-2-0: „(1) Jede Nutzung ist unter den Bedingungen dieser „Datenlizenz Deutschland – Namensnennung – Version 2.0“ zulässig. Die bereitgestellten Daten und Metadaten dürfen für die kommerzielle und nicht kommerzielle Nutzung insbesondere vervielfältigt, ausgedruckt, präsentiert, verändert, bearbeitet sowie an Dritte übermittelt werden …“ Copyright allgemein: „Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellennachweis gestattet.“ – „Die Weiterverwendung ist sowohl für nicht gewerbliche als auch gewerbliche Zwecke erlaubt. … Es bedarf keiner ausdrücklichen Genehmigung durch unser Haus. Eine Quellenangabe ist jedoch erforderlich.“ | Wie (2). | – |
| (5) | **C** | wie (1) | Für Destatis-Veröffentlichungen gilt die allgemeine Freigabe mit Quellenangabe. | Gegenstand fehlt weitgehend: keine Einstellungsfragen. |
| (6) | **C** | wie (4) | Weitergabe mit Quellenangabe erlaubt. | – |

### 4.14 Sozio-oekonomisches Panel (SOEP, FDZ SOEP am DIW Berlin), einschließlich SOEP-IS

Fundstellen: https://www.diw.de/de/diw_01.c.601584.de/datenzugang.html (live HTTP 403; Wayback 20260928132819); Richtlinie https://www.diw.de/de/diw_01.c.1019277.de/soep-richtlinie_zur_nutzung_von_ki_und_grossen_sprachmodellen__llms.html; Mustervertrag https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.43548.de/soep_vertrag_contract_international_2020.pdf (Wayback 20260122124758). Fassung: Seite „Datenzugang“, Wayback 28.09.2026 (HTML SHA-256 597c4774…); KI-Richtlinie ohne Datum, nur über Abrufwerkzeug gelesen; Mustervertrag „soep_vertrag_contract_international_2020.pdf“ (f0d510f5…). Abgerufen: 2026-10-03T22:44Z–22:47Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | KI-Richtlinie laut Abrufwerkzeug (nicht im Rohtext geprüft): „Derzeit dürfen Large Language Models (LLMs) und andere KI-Tools nicht verwendet werden, um SOEP-Daten zu verwalten, zu verarbeiten oder zu analysieren.“ – „Die Nutzung von LLMs mit öffentlich zugänglichen Dokumentationen, Codebüchern, studienbezogenen Metadaten sowie aggregierten Gruppen- oder Populationsschätzungen ist zulässig.“ – „Die Nutzung eines LLM zur Erstellung von Analysecode ist zulässig, solange keine SOEP-Mikrodaten an das LLM übermittelt oder hochgeladen werden.“ | Laut Abrufwerkzeug erlaubt die SOEP-KI-Richtlinie die Nutzung von LLMs mit öffentlicher Dokumentation; das wäre Klasse C. Den Wortlaut konnte ich nicht im Rohtext prüfen (direkter Abruf HTTP 403, keine Archivkopie). Deshalb vorläufig B. | Rohtext der Richtlinie sichern; Lizenz der SOEP-Fragebögen nicht geprüft. |
| (2) | **B** | wie (1) | Wie (1): Laut Abrufwerkzeug sind aggregierte Gruppen- oder Populationsschätzungen für LLMs zulässig. | Wie (1). |
| (3) | **A** | „Wichtig: Die Nutzung von SOEP-Daten in KI-Anwendungen oder zum Training von KI-Modellen ist gemäß unserer SOEP-Richtlinie zur Nutzung von KI und großen Sprachmodellen (LLMs) nicht gestattet. Bei Verstößen behalten wir uns rechtliche Schritte vor.“ „Einzelpersonen (ohne Affiliation) kann kein Zugriff auf die SOEP-Daten gewährt werden.“ – „Außerhalb einer wissenschaftlichen Einrichtung können Sie leider grundsätzlich nicht mit den SOEP-Daten arbeiten.“ | Die Nutzung von SOEP-Daten in KI-Anwendungen ist wörtlich „nicht gestattet“ (im Rohtext der Archivkopie geprüft). Laut Abrufwerkzeug erlaubt die Richtlinie, Analysecode von einem LLM schreiben zu lassen, solange keine Mikrodaten übermittelt werden. Zugang erhalten aber nur wissenschaftliche Einrichtungen, keine Einzelpersonen. | Für den Skriptweg Rohtext der Richtlinie prüfen. Befund ist neu gegenüber R1–R7 (R7: SOEP „nicht geprüft“). |
| (4) | **B** | „Einzelpersonen (ohne Affiliation) kann kein Zugriff auf die SOEP-Daten gewährt werden.“ – „Außerhalb einer wissenschaftlichen Einrichtung können Sie leider grundsätzlich nicht mit den SOEP-Daten arbeiten.“ Mustervertrag Ziffer 2.4: „Die Daten dürfen ausschließlich in folgendem Forschungsvorhaben eingesetzt werden …“ | Veröffentlichungen sind im Rahmen eigener wissenschaftlicher Forschung vorgesehen (Ziffern 2.7, 2.8). Ob eine öffentliche Website dazu zählt und ob das Projekt Vertragspartner sein kann, ist offen. | – |
| (5) | **B** | Seite „Datenzugang“: Hinweis auf „unsere Fragebögen“; kein Lizenzvermerk gesehen. | Für SOEP-Fragebögen habe ich keine Lizenz geprüft. | – |
| (6) | **A** | Mustervertrag Ziffer 2.3: „Der Datenempfänger verpflichtet sich, die SOEP-Daten nicht an andere Personen − außer den unter 2.4 genannten datenschutzrechtlich verpflichteten Mitarbeitern am Forschungsvorhaben − oder an andere Einrichtungen weiterzugeben oder sie ihnen zugänglich zu machen. Dies gilt auch für modifizierte Daten.“ Ziffer 2.9: „… die Weitergabe des von uns gelieferten Datensatzes grundsätzlich nicht erlaubt ist.“ | Weitergabe ist vertraglich ausgeschlossen. | Der gelesene Mustervertrag ist die internationale Fassung von 2020; die aktuelle deutsche Fassung kann abweichen. |

### 4.15 Reuters Institute Digital News Report (deutsche Teilstudie mit dem Leibniz-Institut für Medienforschung | Hans-Bredow-Institut)

Fundstellen: https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/methodology; https://ora.ox.ac.uk/objects/uuid:219692c0-85ce-4cab-9cbc-d3cdffabf62b. Fassung: Methodikseite DNR 2025 (HTML SHA-256 ca841394…); ORA-Datensatz DNR 2024 (nur Rechtefelder gelesen). Abgerufen: 2026-10-03T22:47Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | ORA, Rechtefelder zum DNR 2024: „Copyright holder: Reuters Institute for the Study of Journalism“ – „Rights statement: © Reuters Institute for the Study of Journalism“ – „Licence: Terms and Conditions of Use for Oxford University Research Archive“. Methodik 2025: „Research was conducted by YouGov using this online questionnaire …“ – „Samples were assembled using nationally representative quotas …“ | Die Berichte stehen unter Copyright ohne offene Lizenz; die ORA-Nutzungsbedingungen habe ich nicht gelesen. Der veröffentlichte Fragebogen ist ein englischer Export. | Lizenz der HBI-Veröffentlichungen nicht geprüft; Methodik: Online-Quotenstichprobe von YouGov (keine Zufallsstichprobe). |
| (2) | **B** | wie (1) | Tabellen gibt es laut Suchergebnis nur auf Anfrage für Forschende. | – |
| (3) | **B** | wie (1) | Keine öffentlichen Einzeldaten; Bedingungen einer Abgabe unbekannt. | – |
| (4) | **B** | wie (1) | Keine Nutzungsregel für Ergebnisse gefunden. | – |
| (5) | **B** | wie (1) | Ein deutscher Fragebogen wurde nicht gefunden. | – |
| (6) | **B** | wie (1) | Keine Regel gefunden. | – |

### 4.16 Munich Security Index (Münchner Sicherheitskonferenz, Erhebung Kekst CNC)

Fundstellen: https://securityconference.org/impressum/; https://api.crossref.org/works?query.bibliographic=Munich+Security+Report+2026. Fassung: MSC-Impressum (HTML SHA-256 dd422acf…); Crossref-Metadaten DOI 10.47342/jwie5806 ohne Lizenzfeld. Abgerufen: 2026-10-03T22:48Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | Kein Lizenz- oder Nutzungsvermerk im MSC-Impressum gefunden; Crossref-Eintrag „Munich Security Report 2026: Under Destruction“ (10.47342/jwie5806) ohne Lizenzangabe. Methodik nur aus einer Suchmaschinen-Zusammenfassung: Online-Panels, Quoten, etwa 1.000 Erwachsene je Land, Feld 5.–25.11.2025 (nicht selbst geprüft). | Keine Lizenz oder Nutzungsregel gefunden. | Die Indexfragen messen Risikowahrnehmungen; Eignung als Präferenzfrage fraglich (Prüfung R8). |
| (2) | **B** | wie (1) | Wie (1). | – |
| (3) | **B** | wie (1) | Kein Datenangebot und keine Bedingungen gefunden. | – |
| (4) | **B** | wie (1) | Wie (1). | – |
| (5) | **B** | wie (1) | Wie (1); deutscher Fragebogen nicht gefunden. | – |
| (6) | **B** | wie (1) | Wie (1). | – |

### 4.17 Körber-Stiftung, The Berlin Pulse

Fundstellen: https://koerber-stiftung.de/impressum/. Fassung: Impressum Körber-Stiftung (HTML SHA-256 e4d91f60…); Berlin Pulse 2025/26 laut R7: „© Körber-Stiftung 2025“. Abgerufen: 2026-10-03T22:48Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | „Alle Texte, Bilder, Grafiken und das Layout dieser Website unterliegen dem Urheberrecht der Körber-Stiftung oder Dritter. Jegliche Vervielfältigung, Weitergabe oder sonstige Nutzung ist nur mit Quellenangabe (Körber-Stiftung) und – soweit erforderlich – nach vorheriger Zustimmung der Rechteinhaber zulässig.“ | „soweit erforderlich“ lässt offen, wann eine Zustimmung nötig ist. | Anfrage bei der Körber-Stiftung (Freigabe durch Steven). |
| (2) | **B** | wie (1) | Wie (1). | – |
| (3) | **B** | wie (1) | Kein Datenangebot gefunden (R7 3.7). | – |
| (4) | **B** | wie (1) | Wie (1). | – |
| (5) | **B** | wie (1) | Wie (1); Wortlaute nur in Berichten mit Ergebnissen (nicht geöffnet). | – |
| (6) | **B** | wie (1) | Wie (1). | – |

### 4.18 ZMSBw-Bevölkerungsbefragung (Bericht auf zms.bundeswehr.de; Daten bei GESIS)

Fundstellen: https://www.bundeswehr.de/de/impressum; Bericht: https://zms.bundeswehr.de/resource/blob/5990826/…/zmsbw-forschungsbericht-139-bevoelkerungsbefragung-2025-data.pdf (laut R7). Fassung: Impressum Bundeswehr, Abschnitt Urheberrecht (HTML SHA-256 3c41a5d0…); Forschungsbericht 139 laut R7: „© ZMSBw 2025“, Daten bei GESIS (PDF-S. 94). Abgerufen: 2026-10-03T22:50Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | „Eine Vervielfältigung, Veröffentlichung oder sonstige Verwendung solcher Seiten, oder Teilen davon, in elektronischen oder gedruckten Publikationen, auch im Internet, oder zu unternehmerischen Zwecken ist nur nach vorheriger Zustimmung gestattet.“ – „Unzulässig ist das automatische oder sonst nicht vom individuellen Interesse an dem jeweiligen Inhalt geprägte Auslesen des Archivs oder anderer Datenbanken dieser Seiten zum Zwecke der Speicherung. Die Inhalte dürfen ohne gesonderte Einwilligung lediglich für den privaten, nicht gewerblichen oder ausschließlich bundeswehrinternen Gebrauch abgerufen, heruntergeladen, gespeichert und ausgedruckt werden …“ | Abrufen und Speichern für privaten, nicht gewerblichen Gebrauch sind erlaubt; die Verarbeitung durch einen KI-Agenten ist nicht geregelt. Das Verbot automatischen Auslesens zielt auf Archive und Datenbanken zur Speicherung. | Annahme: Das Bundeswehr-Impressum gilt auch für zms.bundeswehr.de. |
| (2) | **B** | wie (1) | Wie (1). | – |
| (3) | **A** | § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“ | Die Einzeldaten liegen laut Bericht bei GESIS (R7 3.6); dort gilt § 4. | – |
| (4) | **B** | wie (1) | Veröffentlichung von Teilen im Internet „nur nach vorheriger Zustimmung“; Inhalt einer Zustimmung offen. | Anfrage beim ZMSBw (Freigabe durch Steven). |
| (5) | **B** | wie (1) | Wie (4). | – |
| (6) | **B** | wie (1) | Für den Bericht wie (4); für Datendateien gilt GESIS (Klasse A). | – |

### 4.19 Umweltbundesamt, Umweltbewusstseinsstudie (Bericht; Daten bei GESIS)

Fundstellen: https://www.umweltbundesamt.de/datenschutz-haftung-urheberrecht. Fassung: UBA-Seite „Datenschutz, Haftung und Urheberrecht“, Abschnitt C (HTML SHA-256 8a4f5211…); Bericht UBA-Texte 01/2026 laut R7 ohne Lizenzvermerk im Impressum. Abgerufen: 2026-10-03T22:50Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | „Soweit nicht anders gekennzeichnet, stehen vom Umweltbundesamt selbst erstellte Objekte, Grafiken, Tondokumente, Videosequenzen und Texte auf dieser Website unter einer Creative Commons Namensnennung – Nicht kommerziell – keine Bearbeitungen 4.0 International Lizenz.“ – „Soweit nicht anders gekennzeichnet, ist die Nutzung von Daten im Sinne des § 12a EGovG zulässig.“ | Für vom UBA selbst erstellte Texte gilt CC BY-NC-ND 4.0; das erlaubte nichtkommerzielle Vervielfältigung (dann Klasse C). Ob der Studienbericht vom UBA selbst stammt oder von beauftragten Instituten, habe ich nicht geprüft. | Autorschaft und Rechtevermerk des Berichts prüfen. |
| (2) | **B** | wie (1) | Wie (1); ob Tabellen „Daten im Sinne des § 12a EGovG“ sind, ist offen. | – |
| (3) | **A** | § 4: „Die Nutzung von KI-Systemen für die Verarbeitung der Datenbasis, die dem Nutzer / der Nutzerin von GESIS bereitgestellt wird, ist verboten. Für den Fall, dass der Nutzer / die Nutzerin die Kontrolle (alleinige Verfügung und Verantwortung) über das KI-System hat und das KI-System ausschließlich zu wissenschaftlichen Zwecken genutzt wird, können im Einzelfall Ausnahmen auf Anfrage durch GESIS zugelassen werden.“ | Einzeldaten im GESIS-Archiv (R7 3.6, Studiennummer nur aus Suchergebnis). | – |
| (4) | **B** | wie (1) | Wie (1). | – |
| (5) | **B** | wie (1) | CC BY-NC-ND erlaubt unveränderte Wiedergabe, falls der Bericht darunter fällt; Fragebogen nicht geprüft. | – |
| (6) | **B** | wie (1) | Wie (1); Datendateien: GESIS (A). | – |

### 4.20 Zentrum für Qualität in der Pflege (ZQP), Befragungen und Berichte

Fundstellen: https://www.zqp.de/impressum/. Fassung: Impressum ZQP, Abschnitt Urheberrecht (HTML SHA-256 0372d92d…). Abgerufen: 2026-10-03T22:48Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **A** | „Die automatisierte Erfassung, das Auslesen oder das Speichern von Daten und Inhalten für die kommerzielle oder nicht-kommerzielle Nutzung ist ohne ausdrückliche Zustimmung untersagt.“ | Automatisiertes Erfassen und Auslesen von Inhalten ist ohne ausdrückliche Zustimmung wörtlich untersagt, auch für nichtkommerzielle Nutzung. Das Lesen durch einen KI-Agenten ist automatisiertes Auslesen. | Zustimmung wäre möglich. Methoden der ZQP-Befragungen habe ich nicht geprüft (Aufgabe R9). |
| (2) | **A** | wie (1) | Wie (1). | – |
| (3) | **B** | „Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.“ | Kein Datenangebot geprüft. | – |
| (4) | **B** | wie (3) | Verwertung außerhalb gesetzlicher Schranken braucht eine schriftliche Zustimmung. | – |
| (5) | **B** | wie (3) | Wie (4). | – |
| (6) | **B** | wie (3) | Wie (4). | – |

### 4.21 Vodafone Stiftung Deutschland, Befragungen

Fundstellen: https://www.vodafone-stiftung.de/impressum/. Fassung: Impressum Vodafone Stiftung (HTML SHA-256 a126ecea…). Abgerufen: 2026-10-03T22:48Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | „Jede Form der Vervielfältigung, Bearbeitung, Verbreitung sowie jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung und ausdrücklichen Genehmigung der Vodafone Stiftung. Hiervon ausgenommen sind lokale Downloads oder Ausdrucke zum privaten, nicht kommerziellen Gebrauch.“ | Ausgenommen sind nur lokale Downloads und Ausdrucke für privaten Gebrauch; ob die Verarbeitung durch einen Agenten darunter oder unter gesetzliche Schranken fällt, ist offen. | – |
| (2) | **B** | wie (1) | Wie (1). | – |
| (3) | **B** | wie (1) | Kein Datenangebot geprüft. | – |
| (4) | **B** | wie (1) | Schriftliche Zustimmung nötig, Inhalt offen. | – |
| (5) | **B** | wie (1) | Wie (4). | – |
| (6) | **B** | wie (1) | Wie (4). | – |

### 4.22 Initiative D21, D21-Digital-Index

Fundstellen: https://initiatived21.de/impressum; https://initiatived21.de/publikationen/d21-digital-index. Fassung: Impressum Initiative D21 (HTML SHA-256 e466f6c6…); Seite D21-Digital-Index (61de386d…, kein Lizenztext gefunden). Abgerufen: 2026-10-03T22:48Z, 22:52Z.

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | Impressum, Abschnitt „Urheber- und Kennzeichenrecht“: allgemeiner Haftungs- und Urheberrechtstext ohne Lizenz oder Nutzungserlaubnis; auf der Seite zum D21-Digital-Index kein Lizenzvermerk gefunden. | Keine Nutzungsregel gefunden; nur Impressum geprüft. | Lizenzvermerke in den Berichten nicht geprüft. |
| (2) | **B** | wie (1) | Wie (1). | – |
| (3) | **B** | wie (1) | Kein Datenangebot geprüft. | – |
| (4) | **B** | wie (1) | Wie (1). | – |
| (5) | **B** | wie (1) | Wie (1). | – |
| (6) | **B** | wie (1) | Wie (1). | – |

### 4.23 eupinions (Bertelsmann Stiftung); nur nach R7

Fundstellen: https://eupinions.eu/de/about; https://eupinions.eu/fileadmin/files/Projekte/eupinions/Open_Data_Agreement.pdf (laut R7). Fassung: Datenvertrag, PDF-Fassung 29.09.2020 (laut R7). Abgerufen: nicht neu abgerufen; Zitate aus R7 Abschnitt 3.7 (2026-10-03, ca. 21:15–21:22 UTC).

| Nutzung | Klasse | Beleg (wörtlich) | Begründung | Offen |
| --- | --- | --- | --- | --- |
| (1) | **B** | Datenvertrag Ziffer 2.2 laut R7: „The data must only be used for the data recipient's own research. In particular, using the data for any other scientific or commercial use is forbidden.“ Website laut R7: „prior permission from the Bertelsmann Stiftung … is required for any use of information offered here“. | Für jede Nutzung der Website-Inhalte ist eine vorherige Erlaubnis nötig; Inhalt offen. | – |
| (2) | **B** | wie (1) | Wie (1). | – |
| (3) | **B** | wie (1) | Daten nur für eigene Forschung des Empfängers; KI nicht geregelt. Ob eine öffentliche Website „own research“ ist, ist offen. | Stichprobentyp laut R7 vermutlich Online-Quote. |
| (4) | **B** | wie (1) | Wie (3). | – |
| (5) | **B** | wie (1) | Wie (1). | – |
| (6) | **B** | wie (1) | Weitergaberegel des Vertrags in R7 nicht zitiert. | – |

## 5. Eurobarometer: Geltungsbereich der Fragen und Eignung als begrenzter Vergleich

Grundlage sind die Fragen, die R6 in Abschnitt 6 mit Kennung, Welle und Seite belegt hat. Neue Fragebögen habe ich nicht geöffnet, weil sie bei GESIS liegen. Strukturangaben stammen aus den Datensatzbeschreibungen auf data.europa.eu, der Seite „About“ des Eurobarometers und den Technischen Spezifikationen, die R6 zitiert. Einschlägige Vertragsartikel habe ich im konsolidierten EU-Vertrag geprüft (ABl. C 202 vom 7.6.2016).

### 5.1 Welche Fragen betreffen die EU-Ebene, welche Entscheidungen Deutschlands?

Maßgeblich ist der Wortlaut der Frage: Wer soll handeln? Daneben steht, wer nach den Verträgen entscheidet.

| Fragetyp | Beispiele (Kennung laut R6) | Ebene | Anmerkung |
| --- | --- | --- | --- |
| Gemeinsame EU-Politikfelder | SE037: „Eine gemeinsame Verteidigungs- und Sicherheitspolitik der EU-Mitgliedstaaten“, „Eine gemeinsame Außenpolitik …“, gemeinsame Einwanderungs-, Energie-, Klima- und Gesundheitspolitik, digitaler Binnenmarkt, Euro | EU | Gefragt ist, ob es eine gemeinsame EU-Politik geben soll, nicht wie Deutschland handeln soll. In der Gemeinsamen Außen- und Sicherheitspolitik beschließt der Rat grundsätzlich einstimmig (Art. 31 Abs. 1 EUV), Deutschland stimmt also mit. Diese Mitwirkung misst die Frage nicht. |
| Bewertung ergriffener EU-Maßnahmen | ST0350: „Die EU hat als Reaktion auf die russische Invasion in der Ukraine eine Reihe von Maßnahmen ergriffen. Inwieweit stimmen Sie jeder dieser Maßnahmen zu …?“ (Sanktionen, Finanzierung militärischer Ausrüstung, Aufnahme von Kriegsflüchtlingen, Bewerberstatus) | EU, rückblickend | Die Einleitung rahmt die Maßnahmen als bereits beschlossen. Die Items haben sich zwischen den Wellen geändert (R6 6.1). |
| Aussagen über die EU als Akteur | ST0359 („Die Zusammenarbeit auf EU-Ebene sollte bei Verteidigungsfragen verstärkt werden“, Koordinierung der Beschaffung, Produktionskapazitäten); SE050 (Finanzmittel der EU); SE035 Item 5 (Besteuerung großer Technologieunternehmen „in der EU“); SP572 QB5 Item 6 (Plattformregulierung, „Die EU sollte … mit EU-Mitgliedstaaten zusammenarbeiten“); SP565 QD10 (EU-Ziel Klimaneutralität 2050); SE038 (Gemeinsames Europäisches Asylsystem, EU-Außengrenzen); ST0939 Item 2 (Zölle der EU) | EU, teils mit Mitgliedstaaten | Sie eignen sich für den Bereich Europäische Integration und als EU-Bezug in Außen-, Digital- und Klimapolitik. Nationale Streitfragen ersetzen sie nicht. |
| Mehrdeutige Ebene | ST0359 „In der EU sollte mehr Geld für Verteidigung ausgegeben werden“ (EU-Haushalt oder Summe der Mitgliedstaaten?); SE035 Item 4 „Jeder EU-Mitgliedstaat sollte einen Mindestlohn für Arbeitnehmer haben“ (Regel für alle Staaten, für Deutschland nur mittelbar); SP535 QB15 „Gleichgeschlechtliche Ehen sollten in ganz Europa erlaubt sein“ | unklar | Nur mit sichtbarem Hinweis auf die offene Ebene. Sonst wäre die Darstellung verzerrt (Art. 6 Abs. 2 Buchst. b Beschluss 2011/833/EU). |
| Erweiterung | SE037 Item Erweiterung; SP564 QC3 und QC5 (Beitritt je Bewerberland) | EU mit nationaler Zustimmung | Der Rat beschließt einstimmig, und das Beitrittsabkommen „bedarf der Ratifikation durch alle Vertragsstaaten“ (Art. 49 EUV). Damit betrifft die Frage auch eine Entscheidung Deutschlands, obwohl sie nur die EU nennt. |
| Entscheidungen Deutschlands | SP529 QC5b (Ausgaben „der deutschen Bundesregierung“ für Gesundheit, Pflege, Renten, Bildung, Wohnen; 2022, mit eingeblendeten Pro-Kopf-Ausgaben); SP527 QA16 (Maßnahmen „in Deutschland“, 2022); SP527 QA3 Item 3 („Deutschland muss keine Maßnahmen ergreifen …“, 2022); SE040 Item 2 („Deutschland sollte Flüchtlingen helfen“, Standardwellen ab 99.4) | national | Inhaltlich am nächsten an den sechs Lücken, aber von 2022 und bei QC5b mit Informationsvorgabe. Die Frage nennt die Bundesregierung auch für Bereiche, deren Ausgaben andere Ebenen oder Sozialversicherungen tragen können. Wie Befragte das verstehen, ist offen. |
| Ohne Ebene (Grundsätze) | SP572 QB12 (KI-Regulierung als Abwägung); SP557 QA7 (offener Zugang zu Forschungsergebnissen, Grenzen der Forschung); SP538 QC11 (Tempo des Wandels); SP565 QD11 Item 2 (Förderung sauberer Energien statt fossiler Subventionen); SP535 QB17 und QB18; SP545 QD6 Item 5 (Quoten in der Politik) | allgemein | Geeignet, wenn der Fragetext keine Prämisse setzt. Bei SP535 QB17 (Schulunterricht) nennt die Frage keine entscheidende Ebene. |

### 5.2 Wann ein Vergleich mit der Bevölkerung ohne Wählergruppen vertretbar wäre

Wählergruppen sind mit dem Eurobarometer nicht möglich, weil die geprüften Wellen keine Frage zur Bundestagswahl enthalten (R6 1). Ein begrenzter Vergleich „Ihre Antwort und die Antworten der Befragten in Deutschland“ wäre vertretbar, wenn alle folgenden Bedingungen erfüllt sind:

1. **Population benennen.** Befragt werden Personen ab 15 Jahren mit der Staatsangehörigkeit eines EU-Mitgliedstaats, die in Deutschland wohnen (R6 4). Das ist weder die Wahlbevölkerung noch die ESS-Population (ab 15 Jahren, unabhängig von der Staatsangehörigkeit, R3 3.1). Eurobarometer- und ESS-Werte dürfen nicht zu einer gemeinsamen Verteilung verbunden werden (AGENTS.md).
2. **Modus prüfen.** Nur Wellen mit persönlichem Interview in Deutschland verwenden. EB 102.2 hatte in Deutschland auch Videointerviews (CAVI) mit unbekannter Aufteilung. Flash Eurobarometer 574 beruht auf einer Online-Quotenstichprobe. Beide wären auszuschließen oder getrennt zu kennzeichnen (R6 4). Für EB 101.3 und 101.4 ist der Modus in Deutschland nicht geprüft.
3. **Wortlaut.** Die Website zeigt den deutschen Feldwortlaut mit Einleitung, Antwortvorgaben und Reihenfolge. Dafür ist die Rechtefrage zu Nutzung (5) zu klären (Klasse B). Items mit eingeblendeter Information (SP529 QC5b) nur mit derselben Information, sonst nicht.
4. **„Weiß nicht“.** Im Interview wird „Weiß nicht“ nicht vorgelesen, sondern nur spontan erfasst (R6 5). Der Plan muss vorher festlegen, wie die Website diese Antwort anbietet. Die Tabelle muss ihren Anteil ausweisen, damit eine Basis mit und ohne „Weiß nicht“ nachvollziehbar ist.
5. **Basis und Filter.** Die Frage wurde in Deutschland allen Befragten gestellt, nicht nur einem Teil (Filter, Split). Die ungewichtete Fallzahl für Deutschland ist bekannt.
6. **Gewichtung.** Für Deutschland gesamt ist das Gewicht dokumentiert. Ost und West werden getrennt gezogen; laut GESIS-Readme (R6 4) brauchen Ergebnisse für Deutschland eine Gewichtung nach Bevölkerungsgröße.
7. **Unsicherheit.** Die Technische Spezifikation nennt nur eine Faustregel (bei 1.500 Fällen und 50 % etwa ±2,5 Prozentpunkte, R6 4). Designeffekte und ein Designgewicht fehlen. Intervalle wären Näherungen; der Plan müsste die Berechnung vorab festlegen.
8. **Zeitbezug.** Feldzeit nennen. Bei geänderten Itemtexten den Wortlaut der Welle zeigen, aus der die Werte stammen. Bei rückblickenden Items (Maßnahmen „ergriffen“, Bewerberstatus) den Stand seither prüfen.
9. **Ebene kennzeichnen.** Bei Fragen der Typen „EU-Politikfelder“, „EU-Maßnahmen“, „EU als Akteur“ und „Erweiterung“ steht sichtbar, dass sie die EU-Ebene betreffen. Sie schließen die nationalen Lücken nicht, etwa Wehrdienst, Bundeswehr oder Rüstungsexporte (R6 6.1).
10. **Regeln vor Ergebnissen.** Auswahl, Basis und Darstellung werden ergebnisblind festgelegt und geprüft, bevor jemand Werte sieht (AGENTS.md).

Folgerung je Fragetyp:

- Fragen zu EU-Politikfeldern, EU-Maßnahmen, der EU als Akteur und zur Erweiterung eignen sich als begrenzter Vergleich zu einer EU-Frage, wenn die Bedingungen 1 bis 10 erfüllt sind.
- Fragen mit mehrdeutiger Ebene eignen sich nur mit Hinweis.
- Fragen zu Entscheidungen Deutschlands passen inhaltlich am besten, sind aber vier Jahre alt und zum Teil an Informationsvorgaben gebunden. Sie wären einzeln zu prüfen.
- Grundsatzfragen ohne Ebene eignen sich, wenn der Fragetext keine Begründung oder Prämisse enthält.

### 5.3 Welche Angaben die veröffentlichten Tabellen enthalten müssten

**Bekannt aus Strukturdokumenten:**

- Volume A enthält „frequencies and means … of (weighted) replies for each country or territory“.
- Volume C enthält „(labelled) weighted frequencies and means … for each country or territory surveyed separately and cross-tabulated by some 20 socio-demographic, socio-political or other variables (including a regional breakdown)“.
- Volume D und AP enthalten Veränderungen gegenüber früheren Wellen.

So steht es in den Datensatzbeschreibungen von STD105 und SP572, gelesen um 22:35 UTC. Die Seite „About“ sagt: „In most cases, respondents for Eurobarometer surveys are selected randomly and the total sample is weighted …“ und „Each survey publication contains technical specifications and explanations on the methodology and sample size used in each of the countries or territories surveyed, as well as information on confidence levels.“ Für STD105 gibt es nur eine Datei „volumes C_EU27.zip“, für STD104 drei Teildateien nach Ländergruppen.

**Für einen Vergleich nötig und bisher ungeprüft:**

1. Eine Spalte für Deutschland gesamt, nicht nur für West und Ost oder die EU.
2. Alle Antwortkategorien einzeln, einschließlich spontanem „Weiß nicht“ und gegebenenfalls „Verweigert“. Zusammengefasste Kategorien nur zusätzlich.
3. Basis je Frage für Deutschland: ungewichtete und gewichtete Fallzahl sowie der Hinweis, ob alle oder nur ein Teil der Befragten gefragt wurden.
4. Das für Deutschland gesamt verwendete Gewicht.
5. Eine Fragekennung, die eindeutig zur Fragenummer und internen Kennung des deutschen Fragebogens passt.
6. Feldzeit und Modus für Deutschland, aus der Technischen Spezifikation derselben Welle.
7. Rundung und Umgang mit fehlenden Werten.
8. Fassung oder Veröffentlichungsdatum der Datei und die Lizenzangabe.
9. Für Volume C die Liste der Gliederungsmerkmale. Gruppen nach Links-Rechts-Einstufung wären eine neue Vergleichsform und bräuchten einen eigenen Plan.

Diese Punkte kann nur eine getrennte Strukturprüfung klären. Vorschlag: Ein Skript gibt aus den Volumes nur Blattnamen, Spaltenköpfe, Zeilenbeschriftungen und die Beschriftung der Basiszeilen aus und blendet alle Anteilswerte aus. Ob und von wem das geschieht, entscheidet Steven.

## 6. Präzisierungen gegenüber R1 bis R7 und `docs/abdeckung-v2.2.md`

1. **SOEP (neu).** Die Seite „Datenzugang“ des DIW verbietet die Nutzung von SOEP-Daten in KI-Anwendungen (Archivkopie vom 28.09.2026, Rohtext). Einzelpersonen ohne wissenschaftliche Einrichtung erhalten keinen Zugang. R7 hatte das SOEP nicht geprüft. Ohne wissenschaftliche Einrichtung und mit KI-Verarbeitung der Einzeldaten ist das SOEP damit für R9 kein Weg.
2. **ESS Data Portal.** Die Benutzervereinbarung („ESS User Agreement“) steht im Programmcode des Portals. Sie behandelt nur Nutzungsstatistik, Umfragen unter Nutzenden und Kontodaten. Die offene Frage aus R2, R3 und R7 nach Bedingungen im Portal ist damit teilweise beantwortet. Die nach der Anmeldung angezeigten Felder („restrictions“, „disclaimer“) habe ich nicht gesehen.
3. **WVS.** R5 vermerkt die Veröffentlichung zusammengefasster Ergebnisse als „nicht ausdrücklich geregelt“. Bedingung b setzt die „publication of results“ aber voraus und knüpft sie an Zitation und Meldung. Offen bleiben die Definition von „non-profit“ und die Frage, wie eine dauerhaft geänderte Website zu melden ist.
4. **ifo Bildungsbarometer.** R7 schreibt, die Codebücher seien „erst mit dem Vertrag zugänglich“. Die Archivkopie der Datensatzseite vom 03.06.2024 verlinkt Codebuch, ReadMe und Vertragsvorlage dagegen öffentlich („Das Codebuch steht unten zum Download bereit“). Das Codebuch habe ich nicht geöffnet. Die Vertragsvorlage verlangt eine wissenschaftliche Einrichtung, die Unterschrift einer vorgesetzten Person und die Vorlage jeder Veröffentlichung beim EBDC.
5. **UK Data Service.** Die Definition „Data Collection“ umfasst „Dataset(s), Documentation, Metadata“. Das Verbot von Online- und KI-Werkzeugen erfasst damit auch Dokumentation, die unter der Endnutzerlizenz bezogen wurde. Die Fundstelle heißt genau „Abschnitt 5, Nr. 5“ (R7 nennt sie „Ziffer 5.5“).
6. **Eurobarometer, Lizenzfelder.** Bestätigt: STD104, STD105, SP564, SP565 und SP572 tragen „COM_REUSE“ (Beschluss 2011/833/EU), SP527 und SP529 tragen „CC_BY_4_0“. Laut rechtlichem Hinweis von data.europa.eu stehen nur die Metadaten des Portals unter CC0; für die Dateien gilt die Lizenz des jeweiligen Datensatzes.
7. **OECD.** Die Archivkopie der Bedingungen vom 03.10.2026 stimmt in den zitierten Abschnitten mit R7 überein. Eine KI-Regel enthält sie nicht. Bestätigt sind der Vermerk „Restricted Use“ im Fragebogen 2022 und das Fehlen eines Vermerks im Fragebogen 2024.
8. **UBA.** R7 vermerkt, das Impressum des Berichts nenne keine Lizenz. Die Website des UBA stellt eigene Texte jedoch unter CC BY-NC-ND 4.0, soweit nicht anders gekennzeichnet, und erlaubt die Nutzung von Daten nach § 12a EGovG. Ob der Studienbericht vom UBA selbst stammt, ist offen.
9. **ZMSBw.** Neben „© ZMSBw 2025“ (R7) gilt das Impressum der Bundeswehr. Veröffentlichung von Teilen im Internet ist danach „nur nach vorheriger Zustimmung gestattet“. Annahme: Das Impressum erfasst auch zms.bundeswehr.de.
10. **Pew.** `docs/abdeckung-v2.2.md` nennt „Pew nur mit Konto“. Ergänzung: Abschnitt 13 der Terms of Use lizenziert die Datensätze zur Verarbeitung und zur Veröffentlichung von Auszügen. Vollständige Weitergabe ist ausgeschlossen.
11. **ZQP und Vodafone Stiftung (für R9 und R8).** Das ZQP untersagt das automatisierte Auslesen seiner Inhalte ohne Zustimmung, auch für nichtkommerzielle Zwecke. Agenten sollten ZQP-Seiten deshalb nicht selbst auslesen, bis eine Zustimmung vorliegt. Die Vodafone Stiftung verlangt für Verwertung außerhalb gesetzlicher Schranken eine schriftliche Zustimmung.

## 7. Offene Punkte und Entscheidungen für Steven

Jede Anfrage bei Dritten und jede Zustimmung zu Bedingungen braucht Stevens Freigabe. Ich habe keine gestellt.

1. **Eurobarometer, Kommissionsweg.** Die Rechte erlauben Tabellenverarbeitung und Veröffentlichung von Anteilen (C). Steven entscheidet, ob eine ergebnisblinde Strukturprüfung nach Abschnitt 5.3 stattfindet. Für deutsche Fragewortlaute wäre eine Bestätigung des Eurobarometer-Teams nötig. Die Fragen dafür stehen in R6 Abschnitt 8.
2. **WVS.** Steven müsste bestätigen, dass das Projekt „non-profit“ ist, das Formular selbst ausfüllen und den Bedingungen zustimmen. Bei der WVSA zu klären: Anzeige deutscher Fragetexte, Form der Meldung einer Website, Rechte an der deutschen Übersetzung.
3. **GESIS.** Eine Ausnahme nach § 4 bleibt Voraussetzung für alle GESIS-Bestände. Zu klären wären auch die Fragen aus R3 3.3 und R6 8: ob Fragebögen zur Datenbasis gehören, ob eine Website zulässig ist, Befristung, Löschpflicht.
4. **Pew.** Ein Konto bedeutet Zustimmung zu den Terms of Use. Die Daten dürften danach verarbeitet und in Auszügen veröffentlicht werden. Ein deutscher Wortlaut fehlt.
5. **OECD.** Vollständige Bedingungen der Mikrodaten, Lizenz der Fragebögen und die deutsche Fassung anfragen.
6. **SOEP, ifo, Destatis.** Alle drei setzen eine wissenschaftliche Einrichtung voraus. Ohne eine solche Einrichtung gibt es keinen Zugang zu Einzeldaten.
7. **EIB.** Veröffentlichung und Anzeige sind ohne schriftliche Erlaubnis untersagt.
8. **Übrige Quellen (B).** Ohne Erlaubnis der Rechteinhaber keine Nutzung über Lesen hinaus. Bei ZQP gilt das schon für das Lesen durch Agenten.
9. **Juristische Prüfung.** Folgende Fragen beantwortet dieser Bericht nicht:
   - Sind einzelne Fragetexte urheberrechtlich geschützt?
   - Greifen gesetzliche Schranken, etwa für Text und Data Mining (§ 44b UrhG) oder Zitate (§ 51 UrhG)?
   - Sind Berichte von Bundesbehörden amtliche Werke (§ 5 UrhG)?
   - Sind Website-Bedingungen gegenüber Lesenden wirksam?
   - Ist ein KI-Anbieter, der Daten verarbeitet, ein „Dritter“ im Sinne von Weitergabeklauseln (ifo, SOEP, OECD)?

## 8. Nachweise

### 8.1 Tatsächlich geöffnete Quellen (3. Oktober 2026, UTC)

Lokal: `AGENTS.md` (Systemkontext), `reports/claude/auftraege/R10-quellenblocker.md`, `R-erweiterung-gemeinsam.md`, `R8-…`, `R9-…`, `docs/abdeckung-v2.2.md`, `docs/lizenzen.md`, Auszüge aus `docs/project.md`, R1 Abschnitt 6, R2 Abschnitt 6, R3 Abschnitte 3.1–3.3, R5, R6 und R7 vollständig.

| Zeit | Quelle | Ergebnis |
| --- | --- | --- |
| 22:33 | https://www.europeansocialsurvey.org/contact/disclaimer | 200, SHA-256 8e0ded72… |
| 22:33 | europeansocialsurvey.org: /about/privacy-and-data-protection/website-and-data-users, /data-portal, /methodology/data-and-documentation-availability, /news/article/way-you-access-our-data-changing | 200; nur die erste Seite ausgewertet |
| 22:34 | https://www.europeansocialsurvey.org/about/faq | 200 |
| 22:34 | https://ess.sikt.no/en/, /env.js, /assets/index-Db1MnlBi.js | 200; Text „ESS User Agreement“ aus dem Programmcode (SHA-256 c987bd66…) |
| 22:34 | creativecommons.org Legal Code BY-NC-SA 4.0, BY-SA 4.0, BY 4.0 | 200 |
| 22:34 | https://www.worldvaluessurvey.org/AJDownloadLicense.jsp?DOID=6609 | 200, Formular nicht abgeschickt |
| 22:35 | https://www.worldvaluessurvey.org/documents/RULES_AND_PROCEDURES_FOR_WVSA_PIs_IN_WAVE_8.pdf | 200, SHA-256 5797d4fa… |
| 22:35 | EUR-Lex CELEX:32011D0833 (DE) | 200, SHA-256 dad161fa… |
| 22:35 | https://commission.europa.eu/legal-notice_de | 200, SHA-256 8da7a495… |
| 22:35 | data.europa.eu API für s3613_105_2_std105_eng, s3378_104_1_std104_eng, s3682_105_1_sp572_eng, s3413_103_2_sp564_eng, s3472_103_2_sp565_eng, s2652_97_4_sp529_eng, s2672_97_4_sp527_eng | nur Lizenz, Dateinamen und Sätze zu Volumes |
| 22:35 | https://data.europa.eu/en/legal-notice | 200 |
| 22:35–22:36 | europa.eu/eurobarometer: Startseite, runtime-Bündel, src_app_features_about_about_module_ts.4514644fc63dcdf2.js | 200, SHA-256 95e006b7… |
| 22:36 | oecd.org/en/about/terms-conditions.html live | 403; Wayback-Verzeichnis; Kopie 20261003064505 gelesen |
| 22:36 | webfs.oecd.org RTM-Kernfragebögen 2024 und 2022 | nur Vermerke gesucht |
| 22:36 | OECD Working Paper 324 (oecd.org/content/dam/…/5eebe551-en.pdf) | PDF-S. 1–4 und 21–22 |
| 22:37 | https://ukdataservice.ac.uk/app/uploads/cd137-enduserlicence.pdf | 200, SHA-256 3b4f64ad… |
| 22:37–22:38 | eurofound.europa.eu/en/legal-information | live 429; Wayback 20250725103733 |
| 22:38 | https://www.pewresearch.org/about/terms-and-conditions/ | 200 |
| 22:38 | eib.org: /en/terms-of-use.htm, /en/surveys/climate-survey/all-resources, /en/publications-research/eib-open-data | 200 |
| 22:39 | ifo.de/en/ebdc, ifo.de/ebdc-datensaetze/ifo-bildungsbarometer-2021-suf | Bot-Prüfung (3.038 Byte) |
| 22:39 | konsortswd.de/en/services/research/all-datacentres/ebdc/ | 200 |
| 22:41 | Wayback 20240603090649 der ifo-Datensatzseite 2021 SUF | gelesen |
| 22:41–22:42 | Vertragsvorlage „20220908 Datennutzungsvertrag Bildungsbarometer.docx“ | live Bot-Prüfung; über das Abrufwerkzeug als Datei gespeichert, Text lokal aus `word/document.xml` |
| 22:42 | rifs-potsdam.de Publikationsseite SNB 2021 Daten, /de/impressum; ariadneprojekt.de/impressum/; snb.ariadneprojekt.de/impressum | 200, 200, 200, 404 |
| 22:43 | rwi-essen.de FDZ-Seite Social Sustainability Barometer | keine Antwort |
| 22:43 | destatis.de copyright-genesis-online, copyright-allgemein; govdata.de/dl-de/by-2-0 | 200 |
| 22:44 | forschungsdatenzentrum.de/de/zugang, /de/scientific-use-files | 200 |
| 22:44 | diw.de Datenzugang live | 403; Abrufwerkzeug; Wayback 20260928132819 (Rohtext) |
| 22:45–22:46 | diw.de SOEP-KI-Richtlinie | live 403; zweimal Abrufwerkzeug; keine Archivkopie |
| 22:46 | SOEP-Mustervertrag 2020 | live 403; Wayback 20260122124758 |
| 22:47 | reutersinstitute.politics.ox.ac.uk: /digital-news-report/2025/resources (404), /terms-and-conditions (404), /digital-news-report/2025/methodology (200), /privacy-policy (200) | – |
| 22:47 | ora.ox.ac.uk Datensatz DNR 2024 | nur Rechtefelder |
| 22:48 | securityconference.org /en/imprint/, /impressum/, /en/legal-notice/ (404); api.crossref.org Suche „Munich Security Report 2026“; api.datacite.org (Antwort nicht auswertbar) | – |
| 22:48 | koerber-stiftung.de/impressum/; initiatived21.de/impressum; zqp.de/impressum/; vodafone-stiftung.de/impressum/ | 200 |
| 22:49 | Kopfabfragen ESS12-Quellfragebogen (200), deutscher ESS12-Fragebogen (404), deutscher ESS11-Fragebogen (200) | – |
| 22:49 | deutscher ESS11-Fragebogen (stessrelpubprodwe.blob.core.windows.net/…/ESS11_questionnaires_DE.pdf) | Titelseite und Suche nach Rechtevermerken |
| 22:50 | EUR-Lex CELEX:12016M/TXT (DE), Art. 29, 31, 49 EUV | 200 |
| 22:50 | bundeswehr.de/de/impressum; umweltbundesamt.de/impressum, /nutzungsbedingungen (404), /datenschutz-haftung-urheberrecht | – |
| 22:52 | initiatived21.de/publikationen/d21-digital-index | kein Lizenztext gefunden |

Websuchen (nur zum Finden von Seiten): ESS-Portalbedingungen; WVS und KI; EBDC-Vertrag; Destatis-Lizenz; SOEP-Vertrag und KI; Reuters-Datenzugang; Munich-Security-Index-Methodik. Die letzte Zusammenfassung zeigte ungefragt eine Ergebnisaussage; nicht verwendet.

### 8.2 Ausgeführte Befehle (Kurzform)

- `curl` für Seiten, PDFs und APIs nach `/tmp/r10`; Kopfabfragen mit `curl -sI`; Wayback-Verzeichnisabfragen.
- Python-Skripte für HTML-zu-Text, DOCX-Text und JSON-Metadaten; `pdftotext`, `pdfinfo`, `sha256sum`, `grep`, `sed`.
- Abrufwerkzeug (WebFetch) viermal: ifo-Vertragsvorlage (nur Datei gespeichert), DIW-Datenzugang, zweimal DIW-KI-Richtlinie.
- Ein Python-Skript erzeugt aus einer gemeinsamen Datenstruktur die JSON-Datei und die Tabellen in Abschnitt 4.
- Keine Anmeldung, kein abgeschicktes Formular, keine Zustimmung zu Bedingungen, kein Download von Daten, Codebüchern oder Ergebnistabellen, keine Nachricht an Dritte, keine Git-Befehle mit Schreibwirkung. Geschrieben habe ich nur diese Datei und die JSON-Datei.

### 8.3 Grenzen der Prüfung

- Keine Rechtsberatung. Ob Website-Bedingungen gelten und ob gesetzliche Schranken greifen, ist nicht geprüft.
- Mehrere Fassungen stammen aus Archivkopien (OECD, Eurofound, ifo, DIW, SOEP-Vertrag). Die Live-Fassungen können abweichen.
- Nur über das Abrufwerkzeug gelesen: SOEP-KI-Richtlinie. Nur aus Suchergebnissen: MSI-Methodik und das Tabellenangebot des Reuters Institute.
- Nicht gesehen habe ich Bedingungen, die erst nach Anmeldung oder auf Anfrage erscheinen:
  - Felder im ESS-Portal nach der Anmeldung,
  - Bedingungen der OECD-Mikrodaten,
  - Pew-Konto,
  - aktueller EBDC-Vertrag,
  - Verträge für Scientific Use Files von FDZ und FDZ Ruhr,
  - ORA-Nutzungsbedingungen.
- Ebenfalls nicht geprüft: Lizenzen in einzelnen Berichten von D21, Vodafone Stiftung, ZQP und HBI.
- GESIS-Bedingungen und eupinions stammen nur aus R2 bis R7. Ich habe sie nicht neu geprüft.
- Die Struktur der Eurobarometer-Tabellen ist ungeprüft (Abschnitt 5.3).
- Die Ebenen in Abschnitt 5.1 beruhen auf dem Wortlaut der Fragen und auf Art. 31 und 49 EUV. Weitere Zuständigkeiten, etwa für Handel, Mindestlohn oder Bildung, habe ich nicht mit Rechtsquellen belegt.
- Übereinstimmung mit R1 bis R7 ist kein Richtigkeitsnachweis; alle Berichte stammen von Claude-Subagents.

### 8.4 Modell

Laut Laufzeitumgebung: Claude Opus 5.5, Modellkennung `claude-opus-5-5[1m]`, als Subagent in Claude Code.
