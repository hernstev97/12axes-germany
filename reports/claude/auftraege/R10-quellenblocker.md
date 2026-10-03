# Auftrag R10: Präzisierung der Quellenblocker

Lies zuerst `reports/claude/auftraege/R-erweiterung-gemeinsam.md` und folge den dortigen Regeln (Ergebnisblindheit, GESIS-Sperre, keine Anmeldungen, keine Nachrichten).

Prüfe für jede Quelle aus `docs/abdeckung-v2.2.md` (Abschnitt „Zugang und Rechte“ und Nachtrag) und aus R5–R7 die tatsächlichen Nutzungsbedingungen an der Primärquelle und ordne jede geplante Nutzung genau einer Klasse zu:

- A „ausdrücklich verboten“: Eine Regel verbietet die Nutzung wörtlich (Zitat, URL, Fassung, Datum).
- B „ungeklärte Vertragsbedingung“: Die Bedingungen regeln die Nutzung nicht eindeutig, oder sie verlangen eine Zustimmung, Registrierung oder Einzelfallerlaubnis, deren Inhalt offen ist.
- C „durch vorhandene Lizenz erlaubt“: Eine Lizenz oder Weiterverwendungsregel erlaubt die Nutzung wörtlich; nenne die Bedingungen (Namensnennung, nichtkommerziell, Kennzeichnung von Änderungen).

Geplante Nutzungen, je Quelle getrennt zu bewerten: (1) Lesen und Auswerten von Fragebögen und Methodendokumenten durch KI-Agenten, (2) Verarbeitung veröffentlichter Tabellen durch KI-Agenten, (3) Verarbeitung von Einzeldaten durch KI-Agenten oder durch von KI geschriebene Skripte, (4) Veröffentlichung zusammengefasster Anteile auf einer nichtkommerziellen öffentlichen Website, (5) Anzeige deutscher Fragewortlaute auf der Website, (6) Weitergabe von Dateien. Das Fehlen einer KI-Klausel allein begründet weder Klasse C noch Klasse B; begründe die Einordnung mit dem Wortlaut der Lizenz.

Quellen mindestens: ESS (Daten- und Dokumentationslizenz, ESS-Bedingungen), GESIS (Nutzungsbedingungen 2026 nur nach R2/R5/R6, keine neuen Abrufe), World Values Survey, Eurobarometer-Tabellen der Kommission und data.europa.eu (Beschluss 2011/833/EU, CC BY 4.0, rechtlicher Hinweis), OECD (Risks that Matter, OECD-Nutzungsbedingungen), UK Data Service (Endnutzerlizenz), Pew Research Center, Europäische Investitionsbank, ifo/EBDC, RIFS, Statistisches Bundesamt (Datenlizenz Deutschland), SOEP/DIW. Ergänze Quellen, die R8 oder R9 voraussichtlich brauchen (ESS12, Reuters Digital News Report, Munich Security Index, Körber-Stiftung), soweit Bedingungen öffentlich sind.

Bewerte zusätzlich das Eurobarometer: Welche Fragetypen betreffen nur die EU-Ebene, welche Entscheidungen Deutschlands? Wann wäre ein Bevölkerungsvergleich ohne Wählergruppen als begrenzter Vergleich geeignet (Population EU-Staatsangehörige ab 15 Jahren, Modus, Basis, Gewichtung)? Welche Angaben in den veröffentlichten Tabellen müssten vorhanden sein? Öffne dafür keine Tabellen mit Ergebnissen; stütze dich auf Methoden- und Strukturdokumente.

Ausgabe: `reports/claude/agenten/R10-quellenblocker.md` mit einer Tabelle Quelle × Nutzung × Klasse × Beleg, und `reports/claude/agenten/R10-quellenblocker.json` mit einem Eintrag je Quelle und Nutzung (`quelle`, `nutzung`, `klasse`, `zitat`, `url`, `fassung`, `abgerufen`, `begruendung`, `offen`).
