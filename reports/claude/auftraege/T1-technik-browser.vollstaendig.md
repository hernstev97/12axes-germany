# Vollständiger Auftrag T1-technik-browser


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



Prüfgegenstand ist der unveränderte Codex-Stand `e9898fb` in diesem Worktree. Lies vorher `docs/handbuch.md` vollständig (Kapitel 8 Barrierefreiheit und 10 Prüfablauf sind maßgeblich) und `docs/reproduktion-life93-v2.md`.

Erlaubt: Befehle im Repository ausführen, lokale Server auf Port 4321 (Entwicklung) und 4324 (Forschungsentwurf) starten, Chromium über das installierte `playwright-core` (falls Chromium fehlt: `pnpm exec playwright-core install chromium`, das installiert nur in den Benutzer-Cache von Playwright). Screenshots und Logs nur nach `outputs/claude-t1/` (ignoriert). Bericht nach `reports/claude/agenten/T1-technik-browser.md`. Keine Änderungen an Quellcode oder Dokumenten. Beende am Ende alle selbst gestarteten Server und prüfe, dass die Ports frei sind.

Aufgaben:
1. `pnpm check` ausführen; Python-Tests mit `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/tests` ausführen; Ergebnis je Teil berichten. R-Tests nur, wenn R installiert ist.
2. Forschungsentwurf mit `pnpm --filter politikprofil start --configuration research --host 127.0.0.1 --port 4324` starten und `/forschungsentwurf` vollständig durchgehen: alle Fragen beantworten, überspringen, zurückgehen, zurücksetzen, Ergebnisansicht, Quellen aufklappen, Gruppenvergleiche. Breiten 1440×1000, 1024×768, 768×1024, 390×844, 320×720. Waagerechter Bildlauf, Tastaturdurchgang mit sichtbarem Fokus und Sprunglink, 200-%-Zoom, reduzierte Bewegung, axe-core (im Repository installiert). Vorhandenes `scripts/check-research-browser.mjs` darfst du nutzen, prüfe aber zusätzlich selbst.
3. Grenzfälle: keine Antwort, nur „Weiß nicht“ bzw. ausgelassen, extreme Antwortmuster, Fragen mit fehlenden Vergleichsdaten (z. B. `cttresa`), schnelles Hin- und Herwechseln, Neuladen der Seite. Werden fehlende Vergleichsdaten ehrlich angezeigt? Gibt es stille Ersetzungen?
4. Datenschutz und Sicherheit: Alle Netzwerkanfragen während eines vollständigen Durchgangs protokollieren; enthält irgendeine Anfrage Antwortdaten? Werden Antworten in localStorage, sessionStorage, Cookies, IndexedDB oder URL gespeichert? Externe Ressourcen? Prüfe außerdem, ob Rohdaten, private Laufdateien oder Personenkennungen jemals in Git gelangt sind (`git log --all --stat` auf Pfade unter `data/raw`, `data/local`, große CSV-Dateien, Schlüsselwörter wie `idno`), ob Secrets im Repository liegen, ob der Produktionsbuild die Forschungsroute enthält, und den Stand der Abhängigkeiten (`pnpm audit --prod` nur, wenn ohne Anmeldung möglich). Prüfe `.github/workflows` auf Datenzugriffe.
5. Startseite, Projektseite und Methodikseite im Entwicklungsserver (Port 4321) kurz auf die gleichen Punkte und auf veraltete Statusaussagen prüfen.

Berichte getrennt: technische Prüfungen, Browserbeobachtungen, nicht geprüfte Teile. Erfinde keine Beobachtung.
