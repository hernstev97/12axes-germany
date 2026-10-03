# Arbeit in diesem Repository

Lies vor Änderungen `docs/project.md`. Vor jeder Arbeit an Oberfläche, Bedienung, Bildern oder sichtbaren Texten `docs/handbuch.md` vollständig lesen und befolgen; es regelt Gestaltung, Texte, Bilder, Barrierefreiheit und den Prüfablauf.

Der aktuelle Auftrag ist die Repository-Grundlage: Angular-Webapp, Startseite, Gestaltung, Skills CLI und CodeRabbit-Konfiguration. Steven möchte die wissenschaftlichen Prüfregeln anschließend gesondert schärfen. Claude vorerst nicht einrichten. Die ältere Claude-Setup-Vorgabe in LIFE-93 ist durch diese Entscheidung vom 2026-10-03 für den aktuellen Arbeitsschritt überholt.

Keine Fragen, Dimensionen, Scores, Vergleichswerte oder wissenschaftlichen Güteaussagen erfinden. Kein sichtbarer Teststart, bevor ein tatsächlich freigegebener Test existiert. Geplante Funktionen als geplant beschreiben. CodeRabbit-Reviews und technische CI nicht als methodische Validierung ausgeben.

ESS-Rohdaten gehören nur nach `data/raw/`. Sie werden weder committed noch in die Webapp oder CI kopiert. Auch lokale Zwischendaten bleiben außerhalb von Git, bis ihre Veröffentlichung ausdrücklich geprüft wurde.

`skills.yaml` und `.agents/skills/` werden durch die persönliche Skills CLI verwaltet. Synchronisierte Skills hier nicht von Hand bearbeiten. Relevante Skills vor ihrer Anwendung lesen.

Nach Änderungen `pnpm check` ausführen. UI-Änderungen zusätzlich im Browser auf Desktop- und Smartphone-Breite prüfen. Technische Checks, Browserbeobachtungen und wissenschaftliche Abnahmen getrennt berichten.

Änderungen an Designrichtung oder Produktumfang mit Steven abstimmen. Keine Deployment- oder Merge-Freigabe aus dem Auftrag zur lokalen Repository-Grundlage ableiten.
