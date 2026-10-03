# Prüfung der Repository-Grundlage

Stand: 2026-10-03. Diese Prüfung betrifft die technische und gestalterische Grundlage. Sie ist keine wissenschaftliche Abnahme des geplanten Tests.

## Technische Checks

`pnpm check` prüft Formatierung, strenge TypeScript- und Angular-Templates, zwei Navigationstests und den Produktionsbuild. Die Tests prüfen Titel, Fokusführung und aktive Navigation nach einem Seitenwechsel sowie die Rückkehr aus einer unbekannten Adresse.

Die CodeRabbit-Konfiguration wurde gegen das offizielle [Konfigurationsschema](https://coderabbit.ai/integrations/schema.v2.json) validiert. Die Review-Einstellungen richten sich nach der [CodeRabbit-Dokumentation](https://docs.coderabbit.ai/reference/configuration). Ein tatsächlicher CodeRabbit-Review auf GitHub und ein gehosteter CI-Lauf haben noch nicht stattgefunden.

Alle elf Skills wurden mit der persönlichen Skills CLI eingebunden. Das Manifest enthält alle Verzeichnisse mit `SKILL.md` im zentralen Repository; die kopierten Dateien stimmen bytegenau mit der Quelle überein. Der Git-Ausschluss für Rohdaten, lokale Daten, Umgebungsdateien und lokale Screenshots wurde geprüft.

## Browserbeobachtung

Die erste Desktop-Prüfung lief in der gemeinsamen T3-Vorschau. Deren Größenwechsel brach mehrfach wegen einer verlorenen Browser-Verbindung ab. Nachdem auch `preview_open` keinen erreichbaren Automation-Host mehr meldete, folgte ein lokaler Headless-Lauf mit Playwright und Chromium 153.0.8010.12.

| Ansicht            | Breite × Höhe | Ergebnis  |
| ------------------ | ------------- | --------- |
| Desktop            | 1440 × 1060   | bestanden |
| Tablet             | 768 × 1024    | bestanden |
| Smartphone         | 390 × 844     | bestanden |
| Kleines Smartphone | 320 × 720     | bestanden |

In allen Ansichten wurden Startseite, Projektseite, Fragmentlinks, Lizenzdatei, unbekannte Adresse und Rückkehr zur Startseite geprüft. Der Sprunglink funktioniert per Tastatur. Bei einem Seitenwechsel aktualisieren sich Titel, aktive Navigation und Fokus. Unterseiten lassen sich direkt laden und neu laden.

Die geprüften Seiten haben kein horizontales Überlaufen. Bild und lokale Schriftdateien laden. Es wurden keine Laufzeitfehler, fehlgeschlagenen Anfragen oder Anfragen an externe Dienste beobachtet. Die App legte keine Einträge in LocalStorage oder SessionStorage an.

Desktop und Smartphone wurden zusätzlich anhand der Screenshots visuell geprüft. Die Screenshots und der Browserbericht liegen lokal in `outputs/`, das von Git ausgeschlossen ist. Die Prüfung ersetzt keinen Lauf auf einem physischen Smartphone.

## Offen

Fragen, Modell, Vergleichsdaten und wissenschaftliche Prüfregeln sind noch nicht umgesetzt. Auch die unabhängigen methodischen KI-Erstbewertungen, verbindliche Review-Freigaben und die Verständlichkeitsprüfung stehen aus. Das bleibt der nächste Arbeitsschritt nach dieser Grundlage.

## Überarbeitung der Gestaltung (2026-10-03)

Diese Prüfung betrifft die überarbeitete Gestaltung, die Texte, die Bilder und das neue Handbuch. Sie ist keine wissenschaftliche Abnahme.

### Technische Checks

`pnpm check` ist grün: Formatierung, Handbuch-Prüfung (`scripts/check-handbuch.mjs`: 9 Gemälde, Dateien, Nachweise, Sperrmuster, Farben, Schrift, Seitentitel), strenge Typen, 9 Tests und Produktionsbuild ohne Budget-Warnung. Neu sind sieben Galerie-Tests mit Fake-Timern, darunter mehrere Wechsel hintereinander, reduzierte Bewegung, Anhalten und Fortsetzen, das dauerhafte Anhalten bei Tastaturfokus und die Darstellung eines einzelnen Bildes ohne Steuerung. `scripts/encode-artwork.sh` erzeugt die vorhandenen WebP-Dateien aus den Originalen byte-genau neu (geprüft an „Blick auf Dresden bei Sonnenuntergang“). Die geänderte `.coderabbit.yaml` ist gegen das offizielle Schema gültig. Ein gehosteter CI- oder CodeRabbit-Lauf hat nicht stattgefunden.

### Browserbeobachtung

Lokaler Headless-Lauf mit Playwright 1.62.1 und Chromium gegen den Entwicklungsserver. Geprüft wurden Startseite, Projektseite und eine unbekannte Adresse bei 1440 × 1000, 1024 × 768, 768 × 1024, 390 × 844 und 320 × 720.

- axe-core (WCAG 2.0 bis 2.2 A/AA und Best Practices): keine Verstöße in allen 15 Kombinationen.
- Kein waagerechter Bildlauf, keine Laufzeitfehler, keine fehlgeschlagenen Anfragen, keine Anfragen an externe Dienste, keine Einträge in LocalStorage oder SessionStorage, keine defekten Bilder.
- Der Sprunglink führt auf `/projekt` zum Inhalt, ohne die Seite zu wechseln. Links im Inhaltsverzeichnis setzen den Fokus auf den Zielabschnitt. Die Primärschaltfläche hat einen sichtbaren Fokusrahmen in `--ink`.
- Die Galerie wechselte in 26 Sekunden dreimal. Bei emulierter reduzierter Bewegung wechselte sie in 10 Sekunden nicht; die Schaltfläche hieß „Bildwechsel fortsetzen“.
- Desktop, Tablet und Smartphone wurden zusätzlich anhand von Screenshots visuell geprüft, ebenso alle Galeriebilder im Passepartout.

Vier getrennte Prüfagenten (Gestaltung, Barrierefreiheit, Code, Dokumentation) mit je zwei Gegenprüfungen haben die Zwischenstände geprüft. Ihre bestätigten Befunde sind umgesetzt, darunter ein Fehler, durch den die Galerie nach dem ersten Wechsel stehen blieb. Das sind KI-Reviews und Browserbeobachtungen, keine methodische Prüfung. Ein Lauf auf einem physischen Smartphone fehlt.

Beim abschließenden Codex-Review wurden `pnpm check` und `git diff --check` erneut erfolgreich ausgeführt. Die vorhandenen Desktop- und Smartphone-Screenshots wurden visuell geprüft. In der T3-Vorschau wurden Startseite, Projektseite und der Fragmentlink zum Arbeitsstand geprüft; der Link setzte den Fokus auf `stand`. Beim Größenwechsel verlor die Vorschau wiederholt die Verbindung. Ein vollständiger erneuter Browserlauf in allen Breiten fand in diesem Review deshalb nicht statt; dafür gelten die oben dokumentierten Beobachtungen aus dem vorherigen Lauf.

## Breitenkorrektur der vorhandenen Seiten, 3. Oktober 2026

Start- und Projektseite beschreiben jetzt das breite Ziel, den historischen Neunerbestand und bekannte frühere Dateneinsicht. Bestehende Gestaltung, Navigation und Bilder bleiben erhalten; kein neuer Fragebogen oder Teststart. `pnpm check`036 exit0. In der T3-Vorschau beide Seiten bei1440×1000,1024×768,768×1024,390×844 und320×720: kein horizontaler Überlauf, je eine H1, keine defekten Sprungfragmente und axe4.13.0 ohne Verstöße oder unvollständige Prüfungen. Vier Desktop-/Smartphone-Screenshots visuell gelesen, Schrift/Gemälde und Textfluss passend. Einzelbelege in [breadth-website-technical.json](../reports/loop/breadth-website-technical.json).

Sichtbarer Tastaturfokus bleibt ungeprüft: Die verfügbare Vorschau meldet `document.hasFocus=false`. Echter200%-Zoom bleibt ebenfalls ungeprüft; frühere wirkungslose Vorschau-Tastenkürzel sind keine Abnahme. Unveränderte Galerie-/Bewegungsprüfungen wurden nicht wiederholt. Kein vollständiger WCAG-, Geräte-, Verständlichkeits-, Design- oder Methodenabschluss. Neue Inhaltsprüfung der Texte steht aus.
