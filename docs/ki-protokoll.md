# KI-Protokoll

## 2026-10-03: Repository-Grundlage

- Agent: Codex über T3 Code.
- Modellkennung laut Laufzeit: `gpt-6.1-sol`, Reasoning `max`. Eine konkrete interne Modellversion und nicht zugängliche Anbieter-Vorgaben sind unbekannt.
- Lokale CLI: `codex-cli 0.153.4`.
- Werkzeuge: Shell und Dateibearbeitung, Web-Recherche in Primärquellen, Lesen von LIFE-93 über Linear, T3-Browser für Referenz und lokale Prüfung. Keine anderen Agents eingesetzt.
- Umfang: Angular-Grundlage und Gestaltung, alle vorhandenen persönlichen Skills per CLI, technische CI und CodeRabbit-Konfiguration. Keine Datenanalyse oder methodischen Erstbewertungen.
- PR: keiner; lokale Arbeit.

Stevens Auftrag im Wortlaut:

> ich glaube ich hätte da gerne eine angular webapp. und vom design her inspiriert von dieser webseite https://contralabs.com/
>
> ich stelle mir einfach vor: schöne große und mutige serifenschrift für überschriften und fragen, kleinere sanfte serifen für texte, bilder klassicher deutscher kunst (vielleicht gezielt vorallem aus der romantik?) für stellen an denen bilder passen (vermutlich eher auf der startseite als während eines tests)... so in diesem stil. das nur schonmal als richtung für die grundlage des repos. und dann zieh dir auch bitte die ganzen skills aus dem skills repo über die skills cli in das projekt. alle bitte.
>
> claude richte ich erstmal nicht ein. dafür habe ich coderabbit.
>
> sobald die grundlage des repos steht starten wir mit den prüfregeln

Die Umsetzung folgt diesem Auftrag. CodeRabbit bleibt zunächst technischer PR-Review; die methodische Unabhängigkeit und die Prüfregeln sind offene Arbeit.

Prüfergebnisse: `pnpm check` bestanden, CodeRabbit-Schema validiert, alle elf Skills bytegenau mit ihrer Quelle verglichen. Desktop- und Smartphone-Ansichten samt Navigation und Tastaturbedienung wurden im Browser geprüft. Der ergänzende lokale Browserlauf nutzte Playwright, nachdem die gemeinsame T3-Vorschau keinen erreichbaren Automation-Host mehr meldete. Ergebnisse und Grenzen stehen in `validation.md`. Kein gehosteter CI- oder CodeRabbit-Lauf und keine wissenschaftliche Abnahme durchgeführt.
