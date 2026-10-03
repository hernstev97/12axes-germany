# Auftrag T2: Prüfung des technischen Fortsetzungspakets vom 4. Oktober 2026

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude hat am 4. Oktober 2026 technische Prüfgrenzen geschlossen und den lokalen Forschungsentwurf geändert. Du prüfst dieses Paket. Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema und folge ihnen. Modus: Paketprüfung. Dieser Auftrag ist das Umfangsmanifest; seinen SHA-256 nennt die Nachricht des Auftraggebers.

## Prüfgegenstand

Die Commits `5765b36`, `122f69a` und `b4641a9` gegenüber `b5a53ff` (`git diff b5a53ff..b4641a9`):

1. Zweite Dekodierung der ESS5-Designdatei: `reports/claude/kontrollrechnung/sav_gegenprobe.py`, `sav-gegenprobe.json`, `sav-gegenprobe.md`, Eintrag in `reports/claude/datenzugriff.md`.
2. Browserprüfungen: `scripts/serve-dist.mjs`, `scripts/check-public-zoom.mjs`, `scripts/check-research-engines.mjs`, Abschnitt vom 4. Oktober 2026 in `docs/validation.md`.
3. Änderung im Forschungsentwurf: `web/src/app/policy-draft/policy-draft.html`, `.ts`, `.spec.ts` (Erklärung der 95-%-Bereiche einmal je Ansicht nach Plan v2.2, Abschnitt 4.3).
4. `docs/vorschlaege-texte-v1.entwurf.md` nur auf sachliche Richtigkeit der Fundstellen.

## Regeln

Schreibe nur `reports/claude/pruefungen/T2-technik-v22.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten. Nichts unter `data/raw/`, `data/local/` oder `outputs/` lesen und nichts ausführen, was diese Pfade liest. Du darfst `pnpm check` und `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'` ausführen. Browser- und Datenskripte führst du nicht aus; prüfe sie im Code und gegen die dokumentierten Ergebnisse.

## Prüffragen

1. Ist die zweite Dekodierung tatsächlich unabhängig vom eigenen Leser `pipeline/v22/sav.py`, soweit `sav-gegenprobe.md` es behauptet? Stimmen die Aussagen über gemeinsame Bestandteile? Gibt das Skript nur Zählungen und Abweichungen aus, keine Kennungen oder Rohwerte? Überschreibt es nichts Privates?
2. Prüfen die Browserskripte, was `docs/validation.md` ihnen zuschreibt (echter Tab-Zoom statt CSS-Zoom, Datenschutz nach dem Laden, Antwortänderung, Zurücksetzen, Überspringen, Gruppenvergleich, Fokus)? Gibt es Lücken, bei denen ein Fehler unentdeckt bliebe? Ist die Kennzeichnung von WebKit, physischen Geräten und Screenreadern ehrlich?
3. Ist die UI-Änderung planmäßig und vollständig (Erklärung genau einmal je Ansicht, kein Bereich ohne Erklärung, fehlende Bereiche weiter als fehlend markiert)? Decken die Tests das ab?
4. Stimmen die Fundstellen und Zitate in `docs/vorschlaege-texte-v1.entwurf.md`?

Ausgabe: Bericht und JSON-Urteil. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
