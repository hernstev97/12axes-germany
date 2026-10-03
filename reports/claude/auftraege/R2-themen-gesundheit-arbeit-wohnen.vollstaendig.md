# Vollständiger Auftrag R2-themen-gesundheit-arbeit-wohnen


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


## Gemeinsamer Teil der Themenrecherche

Ziel des Produkts laut LIFE-93: ein verständliches, thematisch breites Einstellungsprofil zur deutschen Politik. Fragen sollen unverändert aus etablierten, dokumentierten Befragungen stammen; Vergleichswerte nur aus tatsächlich erhobenen Daten mit Erhebungszeit, Population und Kontext. Eigene oder umformulierte Fragen sind Entwicklungsbedarf und kein Ersatz. Der ESS ist keine Obergrenze: GLES, ISSP, ALLBUS, weitere ESS-Runden, Eurobarometer und andere etablierte Instrumente dürfen geprüft werden. Fragen aus Befragungen von Kandidierenden begründen keine Vergleichswerte für die Bevölkerung.

Ergebnisblinde Recherche: Recherchiere und berichte keine Antwortverteilungen, Prozentwerte, Mittelwerte oder Parteiergebnisse aus Befragungen. Lies nicht `data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts` und keine Dateien unter `data/raw/` oder `data/local/`.

Lokal vorhanden und damit sofort auswertbar sind ausschließlich diese ESS-Ausgaben (integrierte Dateien, Deutschland enthalten): ESS5 Ausgabe 3.6 (Feldzeit DE 2010/11), ESS8 2.3 (2016/17), ESS9 3.3 (2018/19), ESS10 Self-completion 3.2 (DE 2021/22, Papier/Web), ESS11 4.2 (2023). Für ESS8 und ESS5 fehlen lokal die Stichprobendesigndateien (SDDF). Alles andere müsste Steven nach Anmeldung herunterladen.

Öffentliche deutsche ESS-Fragebögen liegen lokal als PDF unter `outputs/loop/breadth-data-001/sources/` (ess5-, ess8-, ess9-, ess10-, ess11-de-questionnaire.pdf, ess8-de-showcards.pdf). Die bisherige Themenmatrix steht in `docs/abdeckung-v2.md` und der bisherige 43-Fragen-Bestand in `docs/empirie-plan-v2.entwurf.md` (Abschnitt „Konkrete Auswahl“). Diese beiden Dateien darfst du lesen, aber bilde dein Urteil selbst und prüfe ihre Angaben, statt sie zu übernehmen.

Für jeden dir zugewiesenen Bereich liefern:

1. Relevante Streitfragen in Deutschland, ungefähr 2021–2026, belegt mit fachlichen Quellen. Geeignet sind politikwissenschaftliche Literatur, Studiendokumentationen (z. B. GLES), Wahlprogramme 2025 nur als Beleg für „Partei X fordert Y“ und die Thesen des Wahl-O-Mat der Bundeszentrale für politische Bildung zur Bundestagswahl 2025 als Beleg, dass eine Streitfrage im Wahlkampf zur Wahl stand. Keine Wertung der Positionen.
2. Verfügbare Originalfragen mit deutscher Formulierung: Studie, Archivnummer/DOI, Datenversion, Fragenummer, Variablenname (wenn dokumentiert), Seite im deutschen Fragebogen, Antwortskala, Filter, Feldzeit, Population, Modus. Zuerst prüfen, welche Fragen in den lokal vorhandenen ESS-Ausgaben existieren. Danach GLES 2025 (Vor- und Nachwahl-Querschnitt, Rolling Cross-Section, Panelwellen), ISSP (u. a. 2016 Role of Government V, 2019 Social Inequality V, 2020 Environment IV, 2021 Health and Health Care II, 2022 Family, 2023 National Identity IV, 2024 Digital Societies, soweit deutsche Fragebögen öffentlich sind), ALLBUS (2021, 2023, 2024), ESS-Runden 1–11 und ESS12, falls veröffentlicht, Eurobarometer und Politbarometer.
3. Zugang und Rechte je Studie: Zugangskategorie, ob zusammengefasste Ergebnisse auf einer öffentlichen, nichtkommerziellen Website veröffentlicht werden dürfen, ob deutsche Fragewortlaute auf der Website angezeigt werden dürfen, und was offen bleibt. Wörtliche Zitate der Bedingungen mit URL.
4. Bewertung je Bereich: vollständig, teilweise oder nicht abgedeckt. Fehlende Daten getrennt von bewussten inhaltlichen Ausschlüssen begründen. Erlaubte Interpretation: konkrete Einzelangabe, gemeinsame Dimension oder formativer Wert, jeweils nur mit Begründung. Verbleibende Lücken.
5. Konkrete, priorisierte Empfehlung: welche Originalfragen als erste Ergänzung tragfähig sind (Aktualität, Deutschlandbezug, Zugang, Rechte), welche davon sofort mit den lokalen ESS-Ausgaben auswertbar wären und welche Dateien Steven herunterladen müsste (Archivnummer, Version, Format).

## Dein Teil



Deine Bereiche, jeweils mit eigenem Abschnitt:

- Gesundheit und Pflege (u. a. staatliche Verantwortung für Gesundheitsversorgung, Bürgerversicherung/zwei Versicherungssysteme, Finanzierung, Zuzahlungen, Pflegeversicherung, Pflegekräfte, Krankenhausreform, Impfpflicht als historischer Konflikt)
- Arbeit und Rente (u. a. Rentenniveau, Renteneintrittsalter, Finanzierung der Rente, Mindestlohn, Arbeitszeit, Gewerkschaften/Tarifbindung, Arbeitslosenunterstützung/Bürgergeld nur soweit nicht schon Sozialstaat, Fachkräfte)
- Wohnen (u. a. Mietpreisbremse/Mietendeckel, sozialer Wohnungsbau, Enteignung großer Wohnungsunternehmen als Volksentscheidsthema, Wohneigentumsförderung, Bauvorschriften, Grundsteuer)

Prüfe für jeden Bereich ausdrücklich, ob er innerhalb der vorhandenen Rubriken (Wirtschaft und Verteilung, Sozialstaat) angemessen erfasst wird oder eine eigene Ergänzung braucht, und begründe das.

Schreibe deinen Bericht nach `reports/claude/agenten/R2-themen-gesundheit-arbeit-wohnen.md`.
