# Gemeinsame Regeln für alle Claude-Subagents (Übernahme LIFE-93, 3. Oktober 2026)

Dieser Block steht wörtlich am Anfang jedes Auftrags in diesem Ordner.

---

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

---
