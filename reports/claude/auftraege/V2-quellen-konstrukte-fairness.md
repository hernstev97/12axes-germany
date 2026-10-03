# Auftrag V2: Nachträgliche Prüfung von Quellen, Wortlauten, Konstrukten, Interpretationen und politischer Fairness

[Gemeinsame Regeln aus 00-gemeinsame-regeln.md stehen wörtlich davor.]

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
