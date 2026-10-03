# Vollständiger Auftrag V1-kontrollrechnung


Kontext: Repository `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`, Ausgangsstand Commit `e9898fb423a3ba9fbe6387ed9215dbe83666aedc` (letzter Codex-Stand). Projekt „12 Axes Deutschland“: Forschungsprototyp eines deutschsprachigen Tests zu politischen Einstellungen in Deutschland, beauftragt in Linear LIFE-93. Codex (OpenAI) hat Recherche, Analyse und Website bisher erstellt. Claude (Anthropic) übernimmt jetzt Abschlussprüfung und Fortsetzung. Du bist ein frischer, getrennter Subagent mit begrenztem Auftrag. Der Koordinator führt die Ergebnisse zusammen.

Feste Regeln:

1. Schreibe nur die Dateien, die dein Auftrag ausdrücklich nennt. Keine anderen Dateien ändern. Keine Commits, Pushes, Merges, Nachrichten, Kommentare, Kontoanmeldungen oder Downloads, die eine Anmeldung oder Zustimmung zu Nutzungsbedingungen verlangen.
2. Rohdaten- und Personenschutz: `data/raw/` und `data/local/` nur lesen, wenn dein Auftrag es ausdrücklich erlaubt. Niemals Rohdatenzeilen, Personenkennungen (`idno` o. ä.), einzelne Gewichte oder private Antwortvektoren ausgeben, kopieren oder in Berichte schreiben. Nur zusammengefasste Werte.
3. Nichts erfinden. Jede Quelle selbst öffnen und die genaue Fundstelle angeben (Seite, Fragenummer, Variablenname, Abschnitt). Nicht eingesehene oder nur über Metadaten, Abstracts oder Zusammenfassungen bekannte Inhalte ausdrücklich so kennzeichnen. Unsichere Vermutungen als Vermutung markieren.
4. Ein Themenfeld ist keine empirisch nachgewiesene Dimension. Literaturplausibilität ist keine Validierung. Übereinstimmung von KI-Agenten ist kein Neutralitätsnachweis.
5. Gleiche Belegstandards für alle politischen Positionen. Streitfragen sachlich und mit den vertretenen Gegenpositionen beschreiben. Keine Motive, Charakterurteile oder Ideologielabels zuschreiben.
6. Keine erfundenen Zahlen. Keine Wahl- oder Parteienempfehlungen.
7. Schreibe deinen Bericht auf Deutsch. Am Ende des Berichts: tatsächlich geöffnete Quellen (URL oder Pfad) mit ungefährer Zugriffszeit, ausgeführte Befehle in Kurzform, Grenzen der eigenen Prüfung und das eingesetzte Modell, soweit es aus der Laufzeit bekannt ist. Eine Modellbezeichnung ohne Laufzeitbeleg als „laut Auftrag“ kennzeichnen.
8. Deine letzte Antwort an den Koordinator fasst in höchstens 25 Zeilen zusammen: Pfad der Berichtsdatei, wichtigste Befunde, offene Punkte.


## Dein Teil



Ausnahme zu Regel 2: Du darfst die fünf lokalen CSV-Dateien unter `data/raw/` mit eigenem Code lesen (ESS5 3.6, ESS8 2.3, ESS9 3.3, ESS10 Self-completion 3.2, ESS11 4.2; Pfade in `docs/reproduktion-life93-v2.md`). Gib dabei niemals Zeilen, Personenkennungen, einzelne Gewichte oder Zellbesetzungen unter 5 aus, auch nicht in Terminalausgaben. Lies nichts unter `data/local/`. Ausgaben nur als zusammengefasste Werte.

Ziel: Die bisherige Wiederholung lief mit demselben Code und denselben Eingaben. LIFE-93 verlangt eine gezielte unabhängige Kontrolle des Berechnungswegs. Deshalb:

1. Lies zuerst nur die Spezifikation: `docs/empirie-plan-v2.entwurf.md` (Abschnitte zur deskriptiven Auswertung, zum Stichprobendesign und zu den Publikationsregeln), `data/analysevertrag.v2.entwurf.json`, `data/gruppenvertrag.v2.1.entwurf.json`, `data/politikprofil-v2.fragen.entwurf.json` sowie die offizielle ESS-Gewichtungsanleitung (https://www.europeansocialsurvey.org/methodology/ess-methodology/data-processing-and-archiving/weighting und das dort verlinkte Dokument). Lies den vorhandenen Rechencode (`pipeline/`, `scripts/run-*.py`) erst, nachdem deine eigene Rechnung fertig und mit den veröffentlichten Werten verglichen ist. Dokumentiere, wann du ihn gelesen hast.
2. Schreibe eine eigene, möglichst einfache Implementierung in `reports/claude/kontrollrechnung/kontrolle.py` (nur Python-Standardbibliothek oder bereits installierte Pakete; nichts global installieren). Sie berechnet für jede der 43 Fragen und für jede Frage-Gruppen-Kombination der Wählergruppen die gewichteten Kategorienanteile nach der Spezifikation: Deutschland (`cntry`), Primärgewicht `pspwght`, Nenner nur gültige Antworten, Missing-Codes getrennt, sowie die Sensitivitäten ungewichtet und mit `dweight`. Prüfe die Datei-/Runden-/Editionsangaben in den Daten selbst.
3. Vergleiche mit den veröffentlichten Dateien `data/reference-v2/*.json` und `data/reference-groups-v21/*.json`: maximale absolute Abweichung je Frage und je Frage-Gruppen-Paar, Nennerbasis, Anwendung der Zurückhalteregeln (unter 100 gültige Antworten, beobachtete Zelle mit 1–4 ungewichteten Fällen), Behandlung leerer Exportzellen und nicht gestellter Fragen. Prüfe auch die Gewichtsdiagnose (konstantes Verhältnis `anweight`/`pspwght` innerhalb Deutschlands).
4. Prüfe die Voraussetzungen für Stichprobenunsicherheit, ohne bereits Konfidenzintervalle zu berechnen: Welche Dateien enthalten `psu` und `stratum` für Deutschland, wie viele Strata und PSUs gibt es, gibt es Strata mit nur einer PSU, welche Studien bräuchten eine zusätzliche SDDF-Datei? Nur Anzahlen ausgeben.
5. Bericht nach `reports/claude/kontrollrechnung/bericht.md`: Umfang, tatsächlich verwendete Eingaben mit SHA-256 der CSVs, Ergebnis je Frage zusammengefasst (Übereinstimmung bis auf Rundung, Abweichung mit Größe und Ursache), Punkte, die nicht unabhängig prüfbar waren. Zusätzlich eine maschinenlesbare Zusammenfassung `reports/claude/kontrollrechnung/vergleich.json` nur mit Frage-IDs, Gruppen-IDs, maximalen Abweichungen und Status, ohne zurückgehaltene Werte.

Schreibe nur in `reports/claude/kontrollrechnung/`.
