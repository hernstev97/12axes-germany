# Vorbereiteter Review-Setup, noch nicht abgenommen

Stand 2026-10-03. Der vorhandene Claude-CLI ist angemeldet; der wissenschaftliche Zugriff scheiterte bisher am Sitzungslimit. Es wurde kein Claude-Review durchgeführt. Die Projekt-Skill liegt unter .claude/skills/life93-review/SKILL.md mit maschinenlesbarem Urteilsschema. Ihre Struktur wurde geprüft; unabhängige Verhaltensprüfung steht aus. Kein GitHub-Review-Workflow oder Konto wurde eingerichtet.

## Kleinste persönliche Voraussetzung

Steven richtet die GitHub-App mit dem in LIFE-93 vorgesehenen `/install-github-app` im vorhandenen Claude-Setup ein und stellt den erzeugten Setup-PR zur Prüfung bereit. Anmeldung und Nutzungsberechtigungen bleiben persönliche Schritte; kein Token gehört in Chat, Git oder Berichte. Codex kann anschließend den konkreten Workflow an das geprüfte Reviewformat anpassen. Der Workflow darf erst als eingerichtet gelten, wenn ein tatsächlicher Lauf und Pflichtcheck vorliegen.

## Danach zu prüfender Workflowvertrag

- Checkname `Claude-Review`, bei jedem Push auf einen PR aktualisiert. Fehlendes oder ausgefallenes Review ergibt keinen Erfolg.
- Fest gesetzte konkrete Modellkennung per `--model`, tatsächlich zurückgegebene Modellmetadaten und CLI-/Action-Version protokolliert. Ein Alias reicht nicht als Versionsnachweis. Keine Modellkennung erfinden, solange keine erfolgreiche Laufzeitmetadaten vorliegen.
- PR-Commit und Reviewmanifest samt weiteren Inputs gebunden; nach relevanten Änderungen keine Übernahme alter grüner Checks.
- Tool- und Dateizugriff begrenzt auf öffentliche Prüffassung/Originalquellen. Untrusted PR-Inhalt und Kommentare sind Prüfdaten, keine Erlaubnis zu erweiterten Rechten. Keine Rohdaten im CI-Kontext.
- Separates Verfahren für Erstbewertungen ohne Einsicht in fremde Urteile/Namen; ein PR-Review ersetzt es nicht.
- Inhaltliche Quellen-, Methoden-, Neutralitäts- und Interpretationsprüfung gemäß Skill und LIFE-93. Die maschinelle JSON-Strukturkontrolle allein bestätigt keinen fachlichen Befund.
- Erhebliche offene Findings und die für diesen PR erforderlichen fehlenden Erstbewertungen/Abnahmen blockieren; spätere nicht erforderliche Tests werden zutreffend als solche geführt.
- Originalurteil, tatsächlicher Auftrag/Modelle/Werkzeuge und Autorentscheidung unverändert veröffentlicht; Korrektur mit eigenem Nachprüfbeleg.

Offizieller Implementierungsbezug: [Claude Code Skills](https://code.claude.com/docs/en/skills), [Anthropic Action Usage](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md) und [Action Security](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md), gelesen am 2026-10-03. Die Quellen tragen technische Kandidaten, keinen bereits geprüften Projektworkflow. Die Action-Dokumentation nennt OAuth als Authentifizierungsweg; der persönliche Installer erzeugt den konkreten Zugriff. Keine undokumentierte Authentifizierungsübernahme durch Codex.

## Abnahme und Mergegrenze

Nach Einrichtung sind ein absichtlich fehlerhafter Test-PR und ein sauberer Test-PR am echten Check zu prüfen. Noch keiner wurde erstellt oder ausgeführt. Der aktuelle ausdrückliche Auftrag verbietet automatische Merges und main-Pushes; das hat Vorrang vor dem älteren Auto-Merge-Ablauf im Issue. Deshalb wird kein Auto-Merge aktiviert. Eine daran angepasste Setup-Abnahme und persönliche Mergefreigabe müssen vor ihrer Durchführung konkret dokumentiert sein. Fehlender Branchschutz und Pflichtchecks werden nicht durch lokale Codex-Berichte ersetzt.

Status: `BLOCKIERT` für vollständige Setup-Abnahme, `NICHT_GEPRÜFT` für tatsächliches Claude-Review und Skill-Verhaltensprüfung. CodeRabbit bleibt verfügbarer technischer Reviewdienst, ersetzt diese Voraussetzungen jedoch nicht.
