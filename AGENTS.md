# Arbeit in diesem Repository

Lies vor Änderungen `docs/project.md`. Vor jeder Arbeit an Oberfläche, Bedienung, Bildern oder sichtbaren Texten `docs/handbuch.md` vollständig lesen und befolgen; es regelt Gestaltung, Texte, Bilder, Barrierefreiheit und den Prüfablauf.

## Aktueller Auftrag

Maßgeblich ist [LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) mit dem Nachtrag „Claude: Abschlussprüfung, Ergänzungen und Übernahme“ vom 3. Oktober 2026 und seinen Abschnitten 2a bis 2c. Claude hat den Codex-Stand `e9898fb` übernommen und arbeitet auf dem Branch `research/life-93-claude-20261003`. Bei Widerspruch geht der Nachtrag den älteren Aufträgen vor: [Vollauftrag](docs/auftrag-life-93-2026-10-03.md), [Fortsetzung](docs/auftrag-life-93-fortsetzung-2026-10-03.md) und [Breite](docs/auftrag-life-93-breite-2026-10-03.md). Die älteren Aufträge bleiben als Belege erhalten. Den Übernahmestand beschreibt [reports/claude/uebernahme.md](reports/claude/uebernahme.md).

Lies vor fachlicher Arbeit außerdem `docs/analyseplan-v2.2.md`, `docs/abdeckung-v2.2.md`, `docs/profilregeln-v1.md` und `docs/pruefregeln.md`.

## Inhaltliche Regeln

Keine Fragen, Dimensionen, Scores, Vergleichswerte oder wissenschaftlichen Güteaussagen erfinden. Kein sichtbarer Teststart, bevor ein tatsächlich freigegebener Test existiert. Geplante Funktionen als geplant beschreiben. Technische CI, KI-Reviews und CodeRabbit nicht als methodische Validierung ausgeben. KI-Reviews heißen KI-Reviews. Übereinstimmung von Agenten ist kein Neutralitätsnachweis.

Das Profil bleibt ein Vektor getrennter Originalfragen. Keine Achsen, Gesamtwerte, Perzentile, Ränge oder Lagerbezeichnungen ohne eigenen Plan und Prüfung. Verschiedene Studien werden nie zu gemeinsamen Personen oder Verteilungen zusammengeführt.

Regeln vor Ergebnissen: Neue Auswertungen brauchen vorher einen versionierten, geprüften Plan mit Tag. Historische Pläne, Tags, Berichte und Prüfurteile bleiben unverändert. Bekannte Daten werden nie als unberührte Bestätigung bezeichnet.

## Daten und Rechte

ESS-Rohdaten gehören nur nach `data/raw/`. Sie werden weder committed noch in die Webapp oder CI kopiert. Keine Rohdatenzeilen, Personenkennungen oder Einzelgewichte in Agent-Aufträge, Tool-Ausgaben, Berichte oder PR-Kommentare übernehmen. Private Laufergebnisse liegen unter `data/local/` und bleiben außerhalb von Git, bis ihre Veröffentlichung ausdrücklich geprüft wurde. Lizenzbedingungen für Daten und Dokumentation unterscheiden; `docs/lizenzen.md` beachten.

GESIS-Daten (GLES, ISSP, ALLBUS) nicht herunterladen oder verarbeiten, solange die KI-Klausel der GESIS-Nutzungsbedingungen nicht geklärt ist (Stopp-Meldung in LIFE-93 vom 3. Oktober 2026).

## Prüfungen

Normale inhaltliche Pakete erhalten einen passenden Prüfagenten. Wesentliche Änderungen an Messmodell und Auswertung erhalten zwei getrennte Prüfungen mit unterschiedlichen Schwerpunkten, nach Möglichkeit durch frische Codex-Prüfer, wenn Claude die Änderung verfasst hat. Prüfer bekommen frischen, begrenzten Kontext, schreiben nur ihre eigenen Berichte und kennen fremde Urteile nicht. Nach höchstens zwei erfolglosen Korrekturrunden die betroffene Aussage begrenzen, als unsicher markieren oder entfernen.

Nach Änderungen `pnpm check` ausführen. Für den Rechenweg v2.2 zusätzlich `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'`. UI-Änderungen im Browser auf Desktop- und Smartphone-Breite prüfen. Technische Checks, Browserbeobachtungen und wissenschaftliche Abnahmen getrennt berichten.

## Zusammenarbeit und Sicherung

`skills.yaml` und `.agents/skills/` werden durch die persönliche Skills CLI verwaltet. Synchronisierte Skills hier nicht von Hand bearbeiten. Relevante Skills vor ihrer Anwendung lesen.

Nur ein schreibender Koordinator. Nach Paketen und spätestens alle 30 Minuten mit Änderungen committen und den eigenen Branch verifiziert pushen. WIP kennzeichnen. Kein Push auf `main`, kein Force-Push, kein automatischer Merge und kein Deployment ohne Stevens Freigabe.

Änderungen an Designrichtung oder Produktumfang mit Steven abstimmen. Gestaltung von Test und Ergebnis, Teststart, Rechte, Veröffentlichung und der Verständnistest mit fünf Personen bleiben Stevens Entscheidungen.
