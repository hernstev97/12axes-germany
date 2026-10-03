# Arbeit in diesem Repository

Lies vor Änderungen `docs/project.md` und bei UI-Arbeit `docs/design.md`.

Die Repository-Grundlage steht. Der aktuelle Auftrag ist die öffentliche Quellenrecherche und das Schärfen der wissenschaftlichen Prüfregeln. Lies dafür zusätzlich `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md` und `docs/entscheidungen.md`.

Steven möchte vorerst ausschließlich CodeRabbit; die methodische Freigabe bleibt offen. Claude und weitere Review-Dienste nicht einrichten, keinen zusätzlichen Auftrag an eine andere Modellfamilie vorbereiten. Die ältere Claude-Setup-Vorgabe in LIFE-93 wird für diesen Arbeitsschritt nicht ausgeführt. Die Anforderungen an getrennte Erstbewertungen und methodische Gegenprüfung werden dadurch nicht für erfüllt erklärt oder abgeschwächt.

Keine Fragen, Dimensionen, Scores, Vergleichswerte oder wissenschaftlichen Güteaussagen erfinden. Kein sichtbarer Teststart, bevor ein tatsächlich freigegebener Test existiert. Geplante Funktionen als geplant beschreiben. CodeRabbit-Reviews und technische CI nicht als methodische Validierung ausgeben.

ESS-Rohdaten gehören nur nach `data/raw/`. Sie werden weder committed noch in die Webapp oder CI kopiert. Keine Rohdatenzeilen oder Personenkennungen in Agent-Aufträge, Tool-Ausgaben oder PR-Kommentare übernehmen. Auch lokale Zwischendaten bleiben außerhalb von Git, bis ihre Veröffentlichung ausdrücklich geprüft wurde. Lizenzbedingungen für Daten und Dokumentation unterscheiden; `docs/lizenzen.md` beachten.

Öffentliche Dokumentation und Literatur dürfen recherchiert werden. Keine endgültige Item-/Modellentscheidung, ESS-Analyse, Entblindung oder Präregistrierungs-/Modell-Tags, bevor die erforderlichen Entscheidungen und Abnahmen vorliegen. Der Analyseplan ist aktuell ein Entwurf. Quellenversionen, präzise Fundstellen, Zugriffe und Grenzen im Belegregister, Quellenkatalog und KI-Protokoll festhalten. Ausgefallene oder nicht durchgeführte Prüfungen bleiben offen.

`skills.yaml` und `.agents/skills/` werden durch die persönliche Skills CLI verwaltet. Synchronisierte Skills hier nicht von Hand bearbeiten. Relevante Skills vor ihrer Anwendung lesen.

Nach Änderungen `pnpm check` ausführen. UI-Änderungen zusätzlich im Browser auf Desktop- und Smartphone-Breite prüfen. Technische Checks, Browserbeobachtungen und wissenschaftliche Abnahmen getrennt berichten.

Änderungen an Designrichtung oder Produktumfang mit Steven abstimmen. Keine Deployment- oder Merge-Freigabe aus dem Auftrag zur lokalen Repository-Grundlage ableiten.

Steven hat anschließend ausdrücklich ein KI-Audit durch fünf echte Codex-Subagents und einen getrennten Juror beauftragt. Dieser lokale Audit-Auftrag ist autorisiert; ein Claude-Setup oder eine andere Modellfamilie wird daraus nicht abgeleitet. Ausgangsfassung und Erstberichte unter `reports/audit-recherche/` nicht überschreiben oder automatisch formatieren. Formale Anforderungspräzisierungen nicht als empirisch bestandene Prüfungen ausgeben. Die Phase-0-Planfestschreibung verlangt keine persönliche Statistik-Abnahme durch Steven.
