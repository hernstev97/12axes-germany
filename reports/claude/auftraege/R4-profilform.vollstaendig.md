# Vollständiger Auftrag R4-profilform


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



Hintergrund: Der bisherige Forschungsentwurf zeigt 43 einzelne ESS-Originalfragen aus fünf Erhebungen (2010–2023) in acht Themenbereichen. Nach jeder Antwort steht nur eine kurze Umschreibung wie „Die Auswahl beschreibt Zustimmung zu dieser Aussage“ und die historische Verteilung der Antworten der Befragten in Deutschland. LIFE-93 verlangt jetzt: Aus den Antworten soll ein verständliches, fachlich begründetes persönliches Profil entstehen. Es soll erklären, welche konkreten politischen Präferenzen und Prinzipien aus den Antworten hervorgehen und wie sie in den erfassten Themen zusammenhängen. Für jede übergreifende Aussage sollen die verwendeten Antworten und ihre Beleggrundlage sichtbar sein. Unterschiedliche Fragekontexte sind zu berücksichtigen. Unterschiedliche Antworten dürfen nicht vorschnell als persönlicher Widerspruch erklärt werden. Keine Motive, moralische Bewertung, Persönlichkeit oder umfassende Ideologiezuordnung. Inhaltlich begründete Beschreibungen ohne Gesamtpunktzahl sind möglich. Dimensionen, Skalen oder zusammengesetzte Werte nur, wenn Auswahl, Interpretation und Berechnung fachlich begründet und angemessen geprüft sind. Keine Achsen, Pole, Gewichte oder Prozentpositionen nur für eine ansprechende Grafik. Aus getrennten Studienverteilungen entsteht kein gemeinsames Referenzprofil, weil die Fragen von verschiedenen Personen zu verschiedenen Zeiten beantwortet wurden.

Lies zur Orientierung `docs/empirie-plan-v2.entwurf.md` (Auswahl der 43 Fragen und Auswertungsregeln), `docs/messformen-v2.entwurf.md` und `data/politikprofil-v2.fragen.entwurf.json` (Wortlaute und Antwortkategorien). Lies keine Antwortverteilungen: nicht `data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`, `data/raw/`, `data/local/`.

Recherchiere mit Originalquellen (DOI oder Link und Seitenangabe):

1. Etablierte Messkonzepte hinter den verwendeten Fragengruppen und was die Fachliteratur über ihre Struktur sagt, zum Beispiel: Gerechtigkeitsprinzipien in ESS9 (Basic Social Justice Orientations, Hülle/Liebig/May), staatliche Verantwortung und Sozialleistungsurteile in ESS8 (Welfare-Attitudes-Modul, Roosma/Gelissen/van Oorschot u. a.), Demokratieverständnis in ESS10 bzw. ESS6 (Ferrín/Kriesi u. a.), Verpflichtung zum Gehorsam gegenüber der Polizei und Legitimität in ESS5 (Jackson/Hough u. a.), Klimapolitikunterstützung in ESS8, Einstellungen zu Zuwanderung (ESS-Kern), Gleichstellungsmaßnahmen in ESS11. Für jede Gruppe: Ist eine Zusammenfassung zu einem Wert belegt? Wenn ja, unter welchen Bedingungen (Itemsatz, Population, geprüfte Struktur)? Wenn nein, welche Beschreibung ist zulässig?
2. Methodenliteratur zur Darstellung persönlicher Ergebnisse aus Einzelfragen: Wahlhilfen und Voting Advice Applications (z. B. Kritik an räumlichen Karten und Achsen, Gemenis, Germann/Mendez, Otjes/Louwerse, Walgrave), reflektive gegenüber formativen Indizes (z. B. Diamantopoulos/Winklhofer; OECD/JRC-Handbuch), Kommunikation von Vergleichen mit Bevölkerungsverteilungen und Unsicherheit für Laien.
3. Daraus eine konkrete, begründete Empfehlung, welche Profilform die Evidenz für diesen Fragenbestand trägt. Beschreibe Regeln, wie aus den Antworten Aussagen werden (z. B. Bedingungen in Abhängigkeit von Antwortkategorien, Umgang mit „Weiß nicht“, Mitte, ausgelassenen Fragen), wie Zusammenhänge innerhalb eines Themas beschrieben werden dürfen, ohne einen unbelegten Gesamtwert zu bilden, und wie historische Vergleiche einzuordnen sind. Nenne ausdrücklich, was nicht zulässig ist.
4. Nenne repräsentative technische Antwortkombinationen, mit denen sich die Regeln später prüfen lassen (z. B. alle Fragen ausgelassen, nur Mitte, gemischte Antworten innerhalb eines Themas, Antworten an beiden Enden). Diese sind keine empirischen Personen.

Schreibe deinen Bericht nach `reports/claude/agenten/R4-profilform.md`.
