# Auftrag T1: Technische Prüfung, Datenschutz und vollständiger Nutzungsablauf im Browser (Ausgangsstand)

[Gemeinsame Regeln aus 00-gemeinsame-regeln.md stehen wörtlich davor.]

Prüfgegenstand ist der unveränderte Codex-Stand `e9898fb` in diesem Worktree. Lies vorher `docs/handbuch.md` vollständig (Kapitel 8 Barrierefreiheit und 10 Prüfablauf sind maßgeblich) und `docs/reproduktion-life93-v2.md`.

Erlaubt: Befehle im Repository ausführen, lokale Server auf Port 4321 (Entwicklung) und 4324 (Forschungsentwurf) starten, Chromium über das installierte `playwright-core` (falls Chromium fehlt: `pnpm exec playwright-core install chromium`, das installiert nur in den Benutzer-Cache von Playwright). Screenshots und Logs nur nach `outputs/claude-t1/` (ignoriert). Bericht nach `reports/claude/agenten/T1-technik-browser.md`. Keine Änderungen an Quellcode oder Dokumenten. Beende am Ende alle selbst gestarteten Server und prüfe, dass die Ports frei sind.

Aufgaben:
1. `pnpm check` ausführen; Python-Tests mit `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/tests` ausführen; Ergebnis je Teil berichten. R-Tests nur, wenn R installiert ist.
2. Forschungsentwurf mit `pnpm --filter politikprofil start --configuration research --host 127.0.0.1 --port 4324` starten und `/forschungsentwurf` vollständig durchgehen: alle Fragen beantworten, überspringen, zurückgehen, zurücksetzen, Ergebnisansicht, Quellen aufklappen, Gruppenvergleiche. Breiten 1440×1000, 1024×768, 768×1024, 390×844, 320×720. Waagerechter Bildlauf, Tastaturdurchgang mit sichtbarem Fokus und Sprunglink, 200-%-Zoom, reduzierte Bewegung, axe-core (im Repository installiert). Vorhandenes `scripts/check-research-browser.mjs` darfst du nutzen, prüfe aber zusätzlich selbst.
3. Grenzfälle: keine Antwort, nur „Weiß nicht“ bzw. ausgelassen, extreme Antwortmuster, Fragen mit fehlenden Vergleichsdaten (z. B. `cttresa`), schnelles Hin- und Herwechseln, Neuladen der Seite. Werden fehlende Vergleichsdaten ehrlich angezeigt? Gibt es stille Ersetzungen?
4. Datenschutz und Sicherheit: Alle Netzwerkanfragen während eines vollständigen Durchgangs protokollieren; enthält irgendeine Anfrage Antwortdaten? Werden Antworten in localStorage, sessionStorage, Cookies, IndexedDB oder URL gespeichert? Externe Ressourcen? Prüfe außerdem, ob Rohdaten, private Laufdateien oder Personenkennungen jemals in Git gelangt sind (`git log --all --stat` auf Pfade unter `data/raw`, `data/local`, große CSV-Dateien, Schlüsselwörter wie `idno`), ob Secrets im Repository liegen, ob der Produktionsbuild die Forschungsroute enthält, und den Stand der Abhängigkeiten (`pnpm audit --prod` nur, wenn ohne Anmeldung möglich). Prüfe `.github/workflows` auf Datenzugriffe.
5. Startseite, Projektseite und Methodikseite im Entwicklungsserver (Port 4321) kurz auf die gleichen Punkte und auf veraltete Statusaussagen prüfen.

Berichte getrennt: technische Prüfungen, Browserbeobachtungen, nicht geprüfte Teile. Erfinde keine Beobachtung.
