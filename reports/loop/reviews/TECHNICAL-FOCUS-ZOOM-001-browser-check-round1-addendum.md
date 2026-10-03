# TECHNICAL-FOCUS-ZOOM-001: Zusatz zur Runde 1

Datum: 2026-10-03, 18:28:12 UTC. Derselbe Codex-Prüfagent. Gezielte statische Prüfung der zuletzt gemeldeten Präzisierungen an `scripts/check-research-browser.mjs`.

SHA-256: `642825797fc15b57355ad1169f19f5b25f30d17e7e58c189c0135b7836977f70`.

Der Bericht `TECHNICAL-FOCUS-ZOOM-001-browser-check-round1.md` war bereits gesichert und bleibt unverändert. Die folgenden Punkte ergänzen ihn. Das Urteil bleibt bestehen: Die vier Erstbefunde sind im begrenzten technischen Umfang behoben; kein blockierender Codebefund aus diesen Präzisierungen.

- `379–381` trimmt das Textlabel der gewählten Gruppenoption vor dem Vergleich mit dem gerenderten Hinweis. Dadurch verfälschen führende oder abschließende Leerzeichen das `startsWith`-Prädikat nicht mehr. Die vom Koordinator gemeldete Timeout-Beobachtung wurde von mir nicht selbst ausgeführt oder überprüft.
- `32–34` berechnet den SHA-256 der ausgeführten Skriptdatei vor dem Browserstart und schreibt ihn in den Laufbericht. `148` trennt den Namen des Fokuschecks als `check` vom Elementtext als `label`. Damit überschreibt der Elementtext nicht mehr den Checknamen im Fokusprotokoll.
- `462–469` nutzt auch für `failure.png` den CDP-Aufnahmeweg mit `fromSurface: false` und `captureBeyondViewport: false`. Die frühere Anmerkung der Runde 1 zum abweichenden Fehler-Screenshotweg ist damit überholt. Fehlermeldung, Exitcode und FAIL-Bericht bleiben erhalten, wenn die Diagnoseaufnahme selbst scheitert.

Keine Runtime- oder Pixelbeobachtung durch diesen Agenten. Kein Browser, Server, Testlauf oder Zugriff auf fremde Reviewerberichte, Rohdaten oder private Ausgaben. Nur dieser Zusatzbericht wurde geschrieben. Die unabhängige Ausführung und Sichtprüfung bleiben beim Koordinator; wissenschaftliche und menschliche Abnahmen sind nicht Gegenstand dieses Urteils.
