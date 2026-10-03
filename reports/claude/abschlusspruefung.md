# Abschlussprüfung LIFE-93 durch Claude

Stand: 3. Oktober 2026, etwa 22:45 UTC. Verfasst von Claude (Modellkennung laut Laufzeit `claude-opus-5-5[1m]`) im T3-Code-Thread „Politiktest wissenschaftlich fundieren“. Branch `research/life-93-claude-20261003`. Geprüfter Code- und Datenstand: Commit `7cb4fce` (danach nur dieser Bericht). Auftrag: Nachtrag „Claude: Abschlussprüfung, Ergänzungen und Übernahme“ in [LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) mit den Abschnitten 2a bis 2c.

Dieser Bericht ist ein KI-Review. Er ersetzt keine Begutachtung durch Fachleute, keine empirische Validierung und keine Freigabe durch Steven. Claude hat große Teile des hier beschriebenen Stands selbst verfasst. Wo dieser Bericht eigene Arbeit bewertet, ist er nicht unabhängig.

## 1 Kurzfassung

- **Übernommen und fortgesetzt.** Codex' Stand `e9898fb` ist übernommen ([Übernahmebericht](uebernahme.md)). Die beauftragten Arbeiten sind ausgeführt, soweit sie ohne Stevens Entscheidungen möglich waren.
- **Fragen.** Das Profil enthält jetzt 62 ESS-Fragen im deutschen Originalwortlaut statt 43. Die 19 neuen Fragen schließen dokumentierte Lücken innerhalb von acht Bereichen ([Analyseplan v2.2](../../docs/analyseplan-v2.2.md), Abschnitt 3).
- **Themenabdeckung.** Die [Matrix v2.2](../../docs/abdeckung-v2.2.md) beschreibt 14 Bereiche. Acht sind teilweise erfasst. Arbeit und Rente, Gesundheit und Pflege, Wohnen, Außen-, Verteidigungs- und Friedenspolitik, Bildung und Forschung sowie Medien und Digitalpolitik haben keine oder fast keine eigene Frage. Geeignete Fragen liegen vor allem bei GESIS. Dessen Nutzungsbedingungen verbieten die Verarbeitung mit KI-Systemen. Auch die geprüften Quellen außerhalb von GESIS schließen keine Lücke ohne Stevens Entscheidung.
- **Erklärendes Profil.** Der lokale Forschungsentwurf beschreibt die Antworten Satz für Satz, fasst Muster in Originalblöcken zusammen und stellt sieben Querbezüge nebeneinander. Er hat keinen Gesamtwert und keine Achsen, weil kein gemeinsamer Wert für diese Fragen belegt ist ([Profilregeln v1](../../docs/profilregeln-v1.md)).
- **Vergleiche und Unsicherheit.** Für 59 der 62 Fragen und 96 Wählergruppenpaare liegen geprüfte historische Anteile vor, jeweils mit einem 95-%-Bereich aus dem Stichprobendesign ([data/reference-v2.2](../../data/reference-v2.2/README.md)). Getrennt geschriebener Code kam auf dieselben Anteile und Standardfehler.
- **Prüfungen.** Getrennte Codex-Prüfagenten haben den Plan v2.2 in drei Runden geprüft. Die dritte Runde ließ zwei mittlere Anzeigepunkte teilweise offen, danach wurde der Plan nach den Prüfregeln festgeschrieben. Ein weiterer Codex-Prüfagent hat die Ergebnisse in zwei Runden geprüft, die zweite ist bestanden. Die frühere Codex-Arbeit haben Claude-Subagents nachgeprüft. Technische Prüfungen und Browserprüfungen sind grün.
- **Produktziel.** Ein breites erklärendes Einstellungsprofil zur deutschen Politik ist nur teilweise erreicht. Innerhalb der erfassten Fragen trägt die Darstellung konkrete, belegte Aussagen. Für sechs Bereiche fehlen die Daten, und die Ergebnisgestaltung, der Verständnistest und die Rechte weiterer Quellen liegen bei Steven.

## 2 Daten-, Plan- und Modellversionen

| Gegenstand            | Version und Bindung                                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ESS5                  | Ausgabe 3.6, `ESS5e03_6.csv`, SHA-256 `bd93e915…4022e`. Design aus `ESS5_DE_SDDF.sav`, SHA-256 `dbd02a1e…74c2b48`.                                                                                                    |
| ESS8                  | Ausgabe 2.3, `ESS8e02_3.csv`, SHA-256 `5112f64f…db3684`. Design aus `ESS8SDDFe01_1.csv`, SHA-256 `bbcb3f7f…bf9e1`. Die Spalte `edition` dieser Datei nennt 1.2, der Dateiname 1.1.                                    |
| ESS9                  | Ausgabe 3.3, SHA-256 `499dffc8…b1adaa`. Design in den Daten.                                                                                                                                                          |
| ESS10 Self-completion | Ausgabe 3.2, SHA-256 `9a04d8d5…22ec6b`. Design in den Daten.                                                                                                                                                          |
| ESS11                 | Ausgabe 4.2, SHA-256 `4b0bfa73…db32dc8`. Design in den Daten.                                                                                                                                                         |
| Fragenkatalog         | v2 `data/politikprofil-v2.fragen.entwurf.json` (`5fe6b935…`), Ergänzung v2.2 `data/politikprofil-v2.2.ergaenzung.json` (`c4b0d97a…`).                                                                                 |
| Analyseplan           | v2.2, Fassung 1.2, Tag `analyseplan-v2.2` auf Commit `b6af9a47…`, lokal und auf `origin` gleich.                                                                                                                      |
| Rechenweg             | `pipeline/v22/survey.py`, `run_v22.py` (eingefroren), `run_v22_sddf.py`, `sav.py`, `export_v22.py`.                                                                                                                   |
| Private Läufe         | `data/local/v22/run.json` (`0ebe86b2…`), `data/local/v22/sddf-run.json` (`821c8db3…`). Nicht in Git. Belege in [v22-laufbeleg.json](v22-laufbeleg.json).                                                              |
| Export                | `data/reference-v2.2/*.json` nach [Exportentscheidung EXPORT-V22-001](export-v22-entscheidung.json). Bericht [04-politikprofil-v22.md](../phasen/04-politikprofil-v22.md), erzeugt von `scripts/build-v22-report.py`. |
| Modell                | Kein Messmodell. Beschreibendes Profil nach Profilregeln v1 (`docs/profilregeln-v1.md`, `web/src/app/policy-draft/profile/`).                                                                                         |
| Historische Fassungen | Neunerfassung v1 (ESS11, Teil A/B), Referenzen v2 und Gruppen v2.1 bleiben unverändert erhalten.                                                                                                                      |

## 3 Themenabdeckung und Auswahl

**Recherche.** Sieben ergebnisblinde Claude-Subagent-Berichte: R1 (Außen-, Bildungs- und Digitalpolitik), R2 (Gesundheit, Arbeit, Rente, Wohnen), R3 (Reichweite der acht bisherigen Bereiche), R4 (Form des Profils), R5 (World Values Survey und EVS), R6 (Eurobarometer), R7 (weitere Quellen). Alle Aufträge stehen im Wortlaut unter `auftraege/`, alle Berichte unverändert unter `agenten/`.

**Aufgenommen.** 19 Fragen nach den Regeln in Plan v2.2, Abschnitt 3.1: Energiequellen (sieben), Asylprüfung und Familiennachzug, Grundeinkommen, EU-weites Sozialleistungsprogramm, Vorrang von Männern bei knappen Arbeitsplätzen, Rechte gleichgeschlechtlicher Paare (zwei), starke Führung über dem Gesetz und Loyalität gegenüber der Führung, Verbot demokratiefeindlicher Parteien, zwei Pandemieabwägungen. Die Auswahl entstand ohne Sicht auf Antwortverteilungen.

**Ausgelassen, mit Grund (Plan v2.2, 3.2).** ESS8 E21–E32 (Zufallsvignetten mit eigenen Nennern), weitere Verteilungsfragen zum selben Gegenstand, weitere Pandemiefragen, Wahrnehmungs- und Bewertungsfragen, Fragen zu Erziehungswerten und eigener Scham.

**Gesperrt.** GLES, ISSP, ALLBUS, EVS, Eurobarometer-Einzeldaten, ZMSBw und UBA wegen § 4 der GESIS-Nutzungsbedingungen. Die Stopp-Meldung steht als Kommentar in LIFE-93. Quellen beim UK Data Service sperrt die Endnutzerlizenz für KI-Werkzeuge ebenfalls (R7 3.5).

**Quellen außerhalb von GESIS.** Steven hat ein externes KI-Review weitergegeben. Die Prüfung steht im Nachtrag zur Matrix. Kurz: Der WVS ergänzt Prinzipienfragen in vorhandenen Bereichen, braucht aber eine Klärung mit der WVSA. Die Eurobarometer-Tabellen der Kommission enthalten Fragen zur EU-Ebene und keine Wahlfrage. Online-Quotenstichproben wie OECD Risks that Matter bräuchten Stevens Grundsatzentscheidung.

**Bewertung.** Die Matrix unterscheidet vollständige, teilweise und fehlende Abdeckung und trennt Datenlücken von bewussten Ausschlüssen. Für Außen-, Verteidigungs- und Friedenspolitik sowie Medien und Digitalpolitik fand keine Recherche eine tragfähige Bevölkerungsfrage ohne Rechteklärung. Diese Lücken sind auf Methodikseite, Startseite und in der Ergebnisansicht sichtbar.

## 4 Erklärendes Profil (Abschnitt 2a)

**Form.** R4 kam zu dem Schluss, dass weder die Literatur noch die Daten einen gemeinsamen Wert für diese Fragen tragen. Die Fragen stammen aus fünf Befragungen mit verschiedenen Personen. Für zwei Blöcke nehmen die ESS-Entwickler ausdrücklich keinen gemeinsamen Faktor an. Deshalb beschreibt das Profil auf drei Stufen: eine Aussage je Frage, Muster innerhalb von Originalblöcken mit gleicher Antwortliste und sieben Querbezüge mit Kontextsatz. Begründung in den Profilregeln v1 und Plan v2.2, Abschnitt 5.

**Umsetzung.** `web/src/app/policy-draft/profile/` mit Richtungstabellen je Frage. Die Richtung kommt aus der Beschriftung, nie aus der Codezahl. Jede Aussage trägt ein festes Kontextmerkmal. Je Bereich zeigt die Ansicht „Erfasst“ und „Nicht erfasst“, dazu die sechs Bereiche ohne eigene Fragen. Die eigene Kategorie ist in der historischen Verteilung und im Gruppenvergleich markiert.

**Technische Antwortkombinationen.** Die Tests T01 bis T30 in `profile-engine.spec.ts` und `reference-v22.spec.ts` prüfen synthetische Kombinationen: leere Antworten, Überspringen, alle angebotenen Kategorien jeder Frage, gleiche und gegensätzliche Blockantworten, Querbezüge mit einer und mehreren Antworten, verbotene Begriffe wie Lagerbezeichnungen, zurückgehaltene Referenzen. Ein neuer Test prüft, dass jede zitierte Aussage wörtlich im gebundenen Katalog steht. Synthetische Kombinationen sind keine Personen und keine Validierungsdaten.

**Verständnistest.** Der [Zusatz 0.3](../../docs/verstaendnistest-v2.2.entwurf.md) bezieht Fragen F1 und F4 und vier neue Fehlinterpretationen auf diese Darstellung. Durchgeführt ist er nicht. Null Menschen wurden befragt.

**Erfüllt das das Produktziel?** Teilweise. Die Ansicht erklärt konkret, welche Präferenzen und Prinzipien die Antworten innerhalb der erfassten Fragen ausdrücken, und nennt die Grenzen jeder Aussage. Sie ist kein breites Einstellungsprofil, weil sechs Bereiche fast fehlen. Eine grafische oder verdichtete Darstellung wäre nur mit einem eigenen geprüften Plan vertretbar. Die Gestaltung von Test und Ergebnis ist nicht freigegeben.

## 5 Historische Vergleiche und Unsicherheit (Abschnitt 2b)

- **Zeit, Kontext und Population.** Jeder Vergleich nennt Studie, Feldzeit, Modus und die Population (Menschen ab 15 Jahren in Privathaushalten). `hrshsnta` („heute“) und `euftf` („schon jetzt“) tragen einen Hinweis zum verschobenen Bezugspunkt. Weitere status-quo-abhängige Fragen tragen einen allgemeinen Hinweis. Geänderte Rechtslagen stehen nur mit Quelle da: Kernkraft (§ 7 Abs. 1e AtG), Eheöffnung 2017, Familiennachzug zu subsidiär Schutzberechtigten (§ 104 Abs. 14 AufenthG). Die ESS10-Anleitung zur Pandemie erscheint bei allen ESS10-Fragen.
- **Aktuellere Instrumente.** ESS12 erscheint für Deutschland ab Januar 2027, ohne neue Fragen für die sechs Lücken. Aktuellere Bevölkerungsfragen zu Verteidigung, Rente und Gesundheit liegen bei GESIS oder in Online-Quotenstichproben (R1, R2, R7).
- **Stichprobenunsicherheit.** 95-%-Bereiche nach Plan v2.2, Abschnitt 4: Taylor-Linearisierung, Logit-Intervall, Freiheitsgrade aus PSUs minus Strata. ESS5: 2 Strata, 168 PSUs. ESS8: 20 Strata, 180 PSUs. ESS9: 89 und 178. ESS10 Self-completion: 89 und 179. ESS11: 25 und 500. Grenze nahe 0 und 1 dokumentiert. Keine persönliche Messunsicherheit.
- **Stevens Frage zur ESS5-Datei.** `ESS5_DE_SDDF.sav` ist die richtige Datei: 3031 Zeilen, alle `cntry = DE`, jede `idno` genau einmal und deckungsgleich mit den 3031 deutschen Fällen von ESS5 Ausgabe 3.6. `dweight` ist innerhalb jeder SDDF-PSU konstant. `PROB` reproduziert `dweight` nicht und wird nach Plan nicht verwendet.
- **Unabhängige Kontrollrechnungen.** V1 rechnete alle v2- und v2.1-Werte mit eigenem Code nach (Abweichung höchstens 1,1e-16). Die neuen Fragen und die Standardfehler von ESS9, ESS10 und ESS11 prüften `kontrolle.py` und Codex' `categorical_reference` (Abweichung 0). Die ESS5/ESS8-Bereiche prüft `sddf_gegenprobe.py` mit dem Einlesen der Kontrollrechnung V1 und Codex' Funktion (Anteile 1,1e-16, Standardfehler 0), die zwölf ESS9-Gruppenpaare `ess9_gruppen_gegenprobe.py` (Abweichung 0). Damit hat jeder veröffentlichte Standardfehler eine zweite Rechnung. Beide Rechnungen nutzen dieselben Datendateien. Nicht unabhängig ist der SPSS-Leser `sav.py`: Beide Rechnungen nutzen ihn für ESS5. Die vollständige `idno`-Deckung und die Konstanz von `dweight` je PSU stützen ihn, beweisen aber nicht jede Zuordnung.

## 6 Prüfungen der Forschung

| Prüfung                          | Prüfer                                    | Ergebnis                                                                                                                                                                                                                                        |
| -------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| V1 Kontrollrechnung v2/v2.1      | Claude-Subagent                           | Alle 42 Einzelreferenzen und 63 Gruppenpaare bestätigt. Befund: `anweight`/`pspwght` außer in ESS11 nicht innerhalb 1e-12 konstant, Wirkung auf Anteile höchstens 8,9e-10 ([Bericht](kontrollrechnung/bericht.md)).                             |
| V2 Quellen, Konstrukte, Fairness | Claude-Subagent                           | 17 Findings zum Codex-Stand. Stand jetzt siehe Abschnitt 6.1.                                                                                                                                                                                   |
| T1 Technik, Browser, Datenschutz | Claude-Subagent                           | Radiofehler bei sehr schnellen Eingaben, instabiles Browserskript, fehlender Netzwerktest, veraltete Statustexte. Alle behoben (Abschnitt 7).                                                                                                   |
| P1/P2 Plan v2.2, Runde 1 und 2   | zwei frische Codex-Prüfer (`gpt-6.1-sol`) | Runde 1 NICHT_BESTANDEN (15 Findings), Runde 2 Restpunkte. Korrekturtabellen im Plan, Abschnitt 9.                                                                                                                                              |
| P3 Plan v2.2, Runde 3            | frischer Codex-Prüfer                     | P1-F01, F02, F04, P2-F01 bestätigt behoben. Offen blieben P1-F08 und F10 (Anzeige). Danach Festschreibung mit Tag. P1-F08 ist inzwischen durch einen Komponententest für `no_valid_answers` abgedeckt. P1-F10 bleibt eine dokumentierte Grenze. |
| E1 Ergebnisse vor dem Export     | frischer Codex-Prüfer                     | NICHT_BESTANDEN: vorzeitiger Reviewstatus, falsche Kategorienreihenfolge bei 0–10-Skalen, fehlender Zellnachweis.                                                                                                                               |
| E1 Runde 2                       | frischer Codex-Prüfer, hohe Denktiefe     | BESTANDEN. Alle drei Findings korrigiert, keine neuen. Empfehlung 59 Einzelreferenzen und 96 Paare. Grenze: gemeinsamer SPSS-Leser.                                                                                                             |
| Seitentexte                      | Claude-Subagent                           | Siehe Abschnitt 6.2.                                                                                                                                                                                                                            |

Jede Prüfung ist ein KI-Review. Codex ist eine andere Modellfamilie als Claude. Die Claude-Subagents prüften die frühere Codex-Arbeit als andere Modellfamilie, Claudes eigene Ergänzungen aber als dieselbe. Übereinstimmung ist kein Neutralitätsnachweis.

### 6.1 Stand der V2-Findings

| Finding                                   | Stand                                                                                                                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F01 Einleitung vor ESS8 E33–E35           | behoben in der Anzeige (`display-additions.ts`), Quelle PDF-Seite 41                                                                                                    |
| F02 ESS10-Pandemieanleitung               | behoben für alle ESS10-Fragen, Test in `policy-catalogue.spec.ts`                                                                                                       |
| F03 „heute“ bei `hrshsnta`, „viel härter“ | behoben                                                                                                                                                                 |
| F04 Bereichstitel gegenüber Inhalt        | teilweise: „Erfasst“ und „Nicht erfasst“ je Bereich. Neue Untertitel entscheidet Steven                                                                                 |
| F05 richtungsneutrale Aussagen            | behoben durch kategorieabhängige Sätze                                                                                                                                  |
| F06 „für die Demokratie im Allgemeinen“   | behoben                                                                                                                                                                 |
| F07 uneinheitliche Einzelvorbehalte       | teilweise: allgemeiner Satz einmal, feste Kontextmerkmale je Frage                                                                                                      |
| F08 „Volksgruppe oder ethnische Gruppe“   | behoben: Übersetzungshinweis an A54 und A55 und im Blockmuster                                                                                                          |
| F09 weitere Lücken, ESS11 B34–B39         | behoben: Lücken je Bereich, Begründung in Plan v2.2                                                                                                                     |
| F10 eigene Kategorie markieren            | behoben                                                                                                                                                                 |
| F11 Pflichttext „mehrere Dimensionen“     | Steven                                                                                                                                                                  |
| F12 Anzeigezusammensetzungen              | behoben: „erstens“ nur bei E6, Wiederholung bei A55/A56 gekennzeichnet, A54 in der Übersicht mit Titel. B25 „auf dieser Liste“ steht so in der gebundenen Papierfassung |
| F13 Restgruppe „Other“                    | behoben: „Andere Partei (heterogener Rest)“ mit Herkunft beider Bezeichnungen                                                                                           |
| F14 ungleiche Sichtbarkeit von Gruppen    | teilweise: Hinweis je Gruppe mit Zahl der verfügbaren Vergleiche. Die Wirkung der Regel 100/5 bei 0–10-Skalen ist nicht gesondert untersucht                            |
| F15 „repräsentativ“                       | Steven (Handbuch-Pflichtbegriff)                                                                                                                                        |
| F16 Aufzählung der Antworttypen           | entfallen: Die neue Methodikseite enthält diese Aufzählung nicht mehr                                                                                                   |
| F17 status-quo-abhängige Fragen           | behoben in der Anzeige, Rechtsänderungen nur mit Quelle                                                                                                                 |

### 6.2 Prüfung der Seitentexte

Ein getrennter Claude-Subagent las die neuen Texte von Start-, Projekt- und Methodikseite und den Nachtrag zur Matrix gegen die Belege, das Handbuch und auf Neutralität. Er fand 17 Befunde, sechs mittel und elf niedrig, keinen hohen, und keine ungleiche Bewertung politischer Positionen. Die mittleren Befunde betrafen eine zu knappe Darstellung des Prüfablaufs (mehrere Prüfagenten, Planrunde 3 nicht bestanden, Festschreibung nach den Prüfregeln), überhöhte Formulierungen zu WVS, Eurobarometer und GESIS, die Zuordnung der Fragen zu nur acht der 14 Bereiche und das fehlende „begrenzt“ bei den KI-Reviews. Alle 17 sind eingearbeitet. Für Befund 7 kam eine Gegenprobe der zwölf ESS9-Gruppenpaare hinzu. Für Befund 17 bindet `web/src/app/pages/page-facts.spec.ts` die von Hand gesetzten Zahlen an Katalog und Export. Der Prüfer gehört zur selben Modellfamilie wie der Autor.

## 7 Technik und Nutzungsablauf

**Technische Prüfungen** (am geprüften Commit):

- `pnpm check`: Formatierung, Handbuchregeln, Review-Schema, Typen, 113 Angular-Tests, Produktionsbuild. Grün.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'`: 21 Tests, grün. Codex' Suite `pipeline/tests`: 325 Tests, grün.
- `node web/src/app/policy-draft/generate-references-v22.mjs --check` und `python3 scripts/build-v22-report.py --check`: Bytevergleich bestanden.
- `pnpm audit`: keine bekannten Schwachstellen.

**Browserbeobachtungen** (lokales Chromium über `playwright-core`, `scripts/check-research-browser.mjs`): der vollständige Ablauf durch alle 62 Fragen, Ergebnis, Gruppenvergleich, Quellen und Übersicht in neun Ansichten (1440, 1024, 768, 390 und 320 Pixel Breite, dazu vier Ansichten mit echtem 200-%-Zoom). Je Ansicht 85 Tastatur-Fokusprüfungen und fünf axe-Läufe ohne Verstoß, kein waagerechter Bildlauf, reduzierte Bewegung emuliert. Seit T1 prüft das Skript auch den Datenschutz: keine Anfrage und kein WebSocket-Frame nach dem Laden, nichts in Storage, Cookies, IndexedDB, Cache oder Service Worker, unveränderte URL. Ohne die v2.2-Daten lief das Skript dreimal vollständig grün. Mit den eingebundenen v2.2-Daten lief es einmal vollständig grün. Ein früherer Lauf mit den Daten hing, weil Codeänderungen den Entwicklungsserver während des Laufs neu luden. Er wurde abgebrochen und wiederholt. Gezielte Bildschirmfotos zeigen Anteile und Bereiche mit einer Nachkommastelle, die markierte eigene Antwort und den Gruppenhinweis. Öffentliche Seiten: `pnpm check:browser` hat Startseite, Projektseite, Methodikseite und Fehlerseite in fünf Breiten geprüft (Reflow, Pixeldichte, Tastatur, Galerie) und ist bestanden. Echter 200-%-Browserzoom ist für diese Seiten in diesem Lauf nicht geprüft.

**Behobene technische Fehler:** Radiozustand bei Eingaben schneller als ein Renderzyklus (T1), instabiles Browserskript und fehlender Netzwerktest (T1), Rundung von Anteil und Bereich auf eine Nachkommastelle (Plan 4.3), Exportstatus und Kategorienreihenfolge (E1).

**Nicht geprüft:** physische Smartphones, Firefox, Safari, Screenreader, Touch, Hochkontrastmodus, ausgelieferter Produktionsbuild im Browser. axe-core deckt nur einen Teil von WCAG 2.2 AA ab.

**Datenschutz und Sicherheit.** Die Website speichert und überträgt keine Antworten. Rohdaten und private Läufe liegen unter ignorierten Pfaden. Kein Commit enthält Dateien aus `data/raw/` oder `data/local/`. Die T3-Checkpoints erfassen nur nicht ignorierte Dateien (T1 3.5). Alle privaten Zwischendateien dieser Übernahme liegen unter ignorierten Pfaden.

## 8 Datenzugriff

Die Rohdatenzugriffe dieser Übernahme stehen in [datenzugriff.md](datenzugriff.md). Teil B der Neunerfassung v1 hat Claude nicht neu ausgewertet. Die Antworten der 43 v2-Fragen waren durch Codex' Läufe bekannt. Die 19 neuen Fragen wurden ohne Sicht auf ihre Antworten ausgewählt, ihre Daten liegen aber in denselben, bereits genutzten Dateien. Keine Rechnung dieser Übernahme gilt als Bestätigung an unberührten Daten. Eine frühe Terminalausgabe der Kontrollrechnung V1 enthielt Statuszählungen von Wahl und Partei. Sie steht in keiner Berichtsdatei, nur im lokalen Werkzeugcache (dokumentiert im KI-Protokoll).

## 9 Offene Punkte und Einschränkungen

1. **Sechs Bereiche ohne Fragen.** Das breite Produktziel ist ohne neue Quellen nicht erreichbar.
2. **GESIS und weitere Quellen.** Klärung durch Steven (Nachtrag zur Matrix, Entscheidungen 1 bis 5).
3. **Gestaltung von Test und Ergebnis.** Nicht freigegeben. Der Forschungsentwurf nutzt nur vorhandene Klassen.
4. **Verständnistest.** Vorbereitet (Pläne 0.1, 0.2, Zusatz 0.3), nicht durchgeführt.
5. **Setup-Abnahme aus LIFE-93** (Branch-Schutz, Pflicht-Checks „CI“ und „Claude-Review“, Test-PRs) ist nicht erfüllt. Ein Claude-Review per GitHub Action existiert nicht.
6. **P1-V22-F10.** Der T30-Komponententest nutzt die veröffentlichten v2-Referenzen, die das Prüfpaket nicht band. Dokumentierte Grenze.
7. **SPSS-Leser.** Eigene Implementierung ohne zweite unabhängige Dekodierung der ESS5-Designdatei.
8. **`anweight`-Diagnose.** Das Verhältnis zu `pspwght` ist außer in ESS11 nicht bis 1e-12 konstant (V1). Plan v2.2 hält es privat fest. Die Anteile berührt das nicht.
9. **Steven-Entscheidungen aus V2.** Bereichsuntertitel (F04), Pflichttext zu Dimensionen (F11), Begriff „repräsentativ“ (F15), Meta-Beschreibung (T1).
10. **Webfassung.** Die neue Zusammenstellung ist keine geprüfte gleichwertige Durchführung der Originalbefragungen.

## 10 Vorschlag zur Abnahme durch Steven

**Jetzt fertig und prüfbar:**

- Plan v2.2 mit Tag, Rechenweg, private Läufe mit Belegen, geprüfter Export `data/reference-v2.2` und Bericht 04.
- Themenmatrix v2.2 mit Nachtrag zu Quellen außerhalb von GESIS.
- Beschreibendes Antwortprofil im lokalen Forschungsentwurf mit 95-%-Bereichen, markierter eigener Antwort, Bereichsangaben und Quellenhinweisen.
- Aktualisierte Start-, Projekt- und Methodikseite, README, Projektstand und KI-Protokoll.

**Welche Aussagen der Stand trägt:**

- „Bei dieser Frage wählten damals x % der Befragten in Deutschland dieselbe Kategorie“, mit Feldzeit, Population, Modus und 95-%-Bereich, als historische Beschreibung.
- Beschreibende Sätze über die eigene Antwort, Muster innerhalb eines Originalblocks und das Nebeneinander in Querbezügen.
- Je Bereich, welche Fragen er enthält und welche Streitfragen fehlen.

**Welche Aussagen er nicht trägt:** eine Gesamtposition, Achsen, Lagerbezeichnungen, Nähe zu Parteien, eine aktuelle Bevölkerungsnorm, eine Aussage über die Wirkung oder Güte der Webfassung, eine wissenschaftliche Validierung.

**Vor einer Veröffentlichung fehlen:**

1. Stevens Entscheidung zur Gestaltung von Test und Ergebnis.
2. Der Verständnistest mit fünf Menschen nach Zusatz 0.3 und seine Auswertung.
3. Entscheidungen zu GESIS und weiteren Quellen, wenn das Profil breiter werden soll.
4. Die Entscheidungen aus Abschnitt 9, Punkt 9.
5. Die Setup-Abnahme oder eine bewusste Entscheidung, sie zu ersetzen.
6. Stevens Freigabe für Merge und Deployment. Diese Übernahme hat nichts nach `main` gemergt und nichts veröffentlicht.

**Empfohlene Reihenfolge:** Zuerst diesen Branch lesen und den Forschungsentwurf lokal ansehen (`pnpm dev:research`, `/forschungsentwurf`). Dann über die Gestaltung entscheiden, danach den Verständnistest durchführen. Die GESIS-Anfrage kann parallel laufen.

## 11 Übergabe

- Aufträge im Wortlaut: `reports/claude/auftraege/`, Prüfsummen in `auftraege.sha256`.
- Agentenberichte: `reports/claude/agenten/`. Prüfberichte und Manifeste: `reports/claude/pruefungen/`. Kontrollrechnungen: `reports/claude/kontrollrechnung/`.
- Reproduktion: `python3 pipeline/v22/run_v22.py` und `python3 pipeline/v22/run_v22_sddf.py` brauchen die ESS-Dateien unter `data/raw/` und schreiben nur nach `data/local/v22/`. Beide verweigern den Lauf, wenn bereits ein privater Lauf existiert. `python3 pipeline/v22/export_v22.py candidate` und `release` erzeugen Kandidaten und Export. Für einen neuen Export braucht es eine neue Ergebnisprüfung und eine neue Exportentscheidung.
- Nächste Schritte für einen Agenten: nach Stevens Entscheidungen einen neuen versionierten Plan für zusätzliche Quellen, danach dieselbe Prüffolge wie für v2.2.
