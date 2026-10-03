# Vollständiger Auftrag V2-quellen-konstrukte-fairness


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



Lies vor Beginn `.claude/skills/life93-review/SKILL.md` und `.claude/skills/life93-review/references/urteil-schema.json` und folge ihnen. Modus: nachträgliche Prüfung des Codex-Stands `e9898fb` (keine Erstbewertung im Sinne getrennter Ersturteile). Manifest: Der Prüfgegenstand ist die Dateiliste unten im Stand `e9898fb`. Berechne selbst SHA-256 jeder gelesenen Datei und nenne sie.

Prüfgegenstand (lesen):
- `data/politikprofil-v2.fragen.entwurf.json`: 43 ausgewählte ESS-Originalfragen mit deutschem Wortlaut, Einleitung, Antwortkategorien, Filterführung, Fundstellen.
- Originalfragebögen: `outputs/loop/breadth-data-001/sources/ess5-de-questionnaire.pdf`, `ess8-de-questionnaire.pdf`, `ess8-de-showcards.pdf`, `ess9-de-questionnaire.pdf`, `ess10-de-questionnaire.pdf`, `ess11-de-questionnaire.pdf` (Text z. B. mit `pdftotext -layout`, falls installiert, sonst mit Python).
- Sichtbare Texte der Forschungsoberfläche: `web/src/app/policy-draft/item-meanings.ts`, `policy-draft.html`, `policy-draft.ts`, `policy-source-details.html`, `public-catalogue.ts` (nur Textfelder), `web/src/app/research/policy-profile.ts`, `web/src/app/pages/methodology/methodology.html`, `web/src/app/pages/project/project.html`, `web/src/app/pages/home/home.html`.
- Öffentliche Berichte: `reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md` und `reports/phasen/03-politikprofil-v21-historische-gruppen.md` (für Interpretationen, Gruppenbezeichnungen und Grenzen; die Zahlen selbst prüft ein anderer Agent).
- Planung: `docs/empirie-plan-v2.entwurf.md`, `docs/messformen-v2.entwurf.md`, `docs/abdeckung-v2.md`, `data/gruppenvertrag.v2.1.entwurf.json`.

Bilde dein Urteil zuerst selbst. Lies erst danach, und nur zum Vergleich in einem getrennten Abschnitt, frühere Prüf- und Entscheidungsdokumente (`reports/loop/*entscheidung*.md`, `reports/loop/reviews/`, `reports/loop/findings.json`). Dokumentiere, welche davon du gelesen hast und ob sie dein Urteil geändert hätten. Dein Ersturteil bleibt unverändert.

Prüffragen:
1. Stimmen Wortlaute, Einleitungen, Antwortkategorien, Codes, Antwortlisten und Filter mit den deutschen Originalen überein? Wurde etwas still umformuliert, gekürzt oder ergänzt? Stimmen Fundstellen?
2. Zeitabhängige Formulierungen („heute“, „derzeit“, „zurzeit“, „in den letzten …“, Bezüge auf damalige Regierungen, Preise oder Ereignisse): Welche Fragen sind betroffen, was bedeutet das für die Anzeige heute und für den Vergleich mit Antworten von 2010–2023?
3. Konstrukt und Reichweite: Beschreiben Bereichszuordnung, Titel und Erklärtexte nur, was die Frage tatsächlich erfasst? Werden Zustimmung, Wichtigkeit, Zuständigkeit und nominale Auswahl unterschieden? Tragen die acht Bereiche ihre Bezeichnung oder sind sie enger?
4. Politische Fairness: Gleiche Belegstandards und gleich sachliche Sprache für alle Antwortrichtungen? Wertende Begriffe, ungleiche Ausführlichkeit, Asymmetrien in Titeln oder Erklärungen, problematische historische Gruppenbegriffe (z. B. in Zuwanderungsfragen)? Faire Antwortmöglichkeiten einschließlich Nichtpositionskategorien? Auswahl- und Auslassungsfolgen (z. B. fehlende Themen, die einer Richtung systematisch nützen oder schaden könnten)?
5. Historische Vergleichsgruppen (Wählergruppen nach erinnerter Zweitstimme): Sind Bezeichnungen, Zeitbezug, Population und Interpretationsgrenzen korrekt und gleich behandelt?
6. Ergebnisdarstellung: Was sagen die vorhandenen Erklärtexte tatsächlich über die eigene Antwort aus? Wo fehlt eine fachlich tragfähige Erklärung?

Bericht nach `reports/claude/agenten/V2-quellen-konstrukte-fairness.md` und maschinenlesbares Urteil nach Skill-Schema in `reports/claude/agenten/V2-urteil.json`. Jede Beanstandung mit genauer Fundstelle (Datei und Zeile bzw. PDF-Seite), Problem, Auswirkung, Schweregrad und überprüfbarer Korrektur.
