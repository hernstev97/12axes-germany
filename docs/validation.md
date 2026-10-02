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
