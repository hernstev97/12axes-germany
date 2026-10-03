# Vollständiger Auftrag R5-wvs


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


## Gemeinsamer Teil der Alternativen-Recherche

Hintergrund: Das Profil „12 Axes Deutschland“ nutzt Originalfragen aus ESS-Befragungen. Für sechs Bereiche fehlen eigene Fragen: Arbeit und Rente, Gesundheit und Pflege, Wohnen, Außen-/Verteidigungs-/Friedenspolitik, Bildung und Forschung, Medien und Digitalpolitik. Auch innerhalb vorhandener Bereiche fehlen wichtige Gegenstände (siehe `docs/abdeckung-v2.2.md`, Spalte „Nicht erfasst“). Geeignete Fragen aus GLES, ISSP und ALLBUS liegen bei GESIS. Die GESIS-Nutzungsbedingungen verbieten in §4 die Verarbeitung mit KI-Systemen ohne Ausnahme. Steven hat ein externes KI-Review (GPT-6.1-Sol) eingeholt. Es nennt den World Values Survey und das Eurobarometer als Alternativen und empfiehlt eine systematische Prüfung einschließlich Nutzungsrechten und Themenabdeckung. Prüfe diese Aussagen selbst; übernimm sie nicht.

Anforderungen an jede Quelle:
1. Zugang: Wer stellt die Daten bereit (direkt oder über GESIS)? Ist eine Anmeldung nötig? Gibt es Einzeldaten oder nur veröffentlichte Tabellen?
2. Nutzungsbedingungen wörtlich mit URL: kommerzielle/nichtkommerzielle Nutzung, Veröffentlichung zusammengefasster Ergebnisse auf einer öffentlichen Website, Anzeige deutscher Fragewortlaute, Weitergabe von Dateien, ausdrücklich: gibt es eine Regel zu KI-Systemen oder automatisierter Verarbeitung? Wenn keine Regel gefunden wurde, genau so berichten (nicht als Erlaubnis deuten).
3. Deutschland: Erhebungsjahre, Feldzeit, Population, Stichprobe (Zufall oder Quote), Modus, Fallzahl laut Dokumentation, Gewichte.
4. Deutsche Fragebögen: Fundort, Sprache, Fragenummern; Wortlaut für relevante Fragen wörtlich mit Fundstelle.
5. Themenabdeckung: Welche Originalfragen decken die sechs fehlenden Bereiche und die größten Lücken innerhalb der vorhandenen Bereiche ab? Nur politische Präferenzen oder Prinzipien, keine Wahrnehmungen, Vertrauensfragen, Bewertungen der Regierung oder eigenes Verhalten.
6. Eignung als Vergleich: Reicht eine veröffentlichte Tabelle (Anteile je Kategorie für Deutschland mit Basis und Gewichtung), oder braucht es Einzeldaten? Für Wählergruppen braucht es Einzeldaten.
7. Konkrete Empfehlung je Bereich mit Priorität, Voraussetzungen und offenen Fragen für Steven.

Ergebnisblind: Recherchiere und berichte keine Antwortverteilungen, Prozentwerte oder Ergebnisse. Öffne keine Tabellen mit Ergebnissen, nur Fragebögen, Methoden- und Rechtsdokumente. Wenn eine Seite ungefragt Ergebnisse zeigt, nutze sie nicht und vermerke das. Lies nicht `data/reference-*`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-*` und nichts unter `data/raw/` oder `data/local/`. Lade keine Daten herunter, die eine Anmeldung oder Zustimmung zu Bedingungen erfordern.

## Dein Teil

Prüfe den World Values Survey (WVS), insbesondere Welle 7 (Deutschland 2018) und frühere Wellen mit Deutschland, sowie die European Values Study (EVS 2017) und die gemeinsame EVS/WVS-Datei. Kläre ausdrücklich, welche dieser Dateien direkt über worldvaluessurvey.org und welche über GESIS bereitgestellt werden. Prüfe für Deutschland besonders Fragen zu staatlicher Überwachung (Video, E-Mail/Internet, Datensammlung), Wirtschaftsordnung (Wettbewerb, staatliches Eigentum, Einkommensgleichheit), Umwelt gegen Wachstum, Zuwanderungspolitik, Demokratieformen (starke Führung, Expertenregierung, Armee) und Gleichstellung. Prüfe, ob es Fragen zu den sechs fehlenden Bereichen gibt. Schreibe nach `reports/claude/agenten/R5-wvs.md`.
