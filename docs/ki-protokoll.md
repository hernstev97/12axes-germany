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

## 2026-10-03: Überarbeitung der Gestaltung

- Agent: Claude Code über T3 Code.
- Modellkennung laut Laufzeit: `claude-opus-5-5` (Kontext 1M). Interne Modellversion und nicht zugängliche Anbieter-Vorgaben sind unbekannt.
- Werkzeuge: Shell und Dateibearbeitung, Web-Recherche, Lesen von LIFE-93 über Linear, lokaler Headless-Browser (Playwright mit Chromium) für Referenz und Prüfung, ImageMagick. Workflows mit Teilagenten desselben Modells recherchierten Gemälde, Provenienz und Flaggenfarben, schrieben drei getrennt erzeugte Textfassungen, führten sie in einer Jury zusammen und prüften Texte, Gestaltung, Barrierefreiheit, Code und Dokumentation. Übereinstimmung zwischen Teilagenten desselben Modells ist kein Beleg.
- Umfang: Name, Gestaltung, Texte und Bilder der Website, Schriftpaket (Libre Baskerville statt Fraunces und Newsreader), Gestaltungs- und Texthandbuch, zugehörige Dokumentation. Keine Datenanalyse, keine methodischen Erstbewertungen.
- PR: keiner; lokale Arbeit.

Stevens Auftrag im Wortlaut:

> ich möchte, dass du die webseite überarbeitest. zur info: das hier (https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) ist der task an dem grade von gpt 6.1 sol gearbeitet wird. die webseite hat es grundlegend schon aufgebaut und der allgemeine stil soll auch so bleiben. also großer wert auf serifen-ästhetik legen und romantische deutsche kunst. ich möchte es aber auch etwas "offizieller" (?) aussehen lassen. also es sieht grade EXTREM vibe coded aus. es sind viele gpt-isms drin. die schriftart, die vielen kleinen fast schon esotherisch wirkenden all-caps sätze, die wordings. es soll neutraler sein und nicht so ... ja .. esotherisch. außerdem möchte ich dass nicht nur ein gemälde zu sehen ist sondern immer wieder andere. ich denke als schriftart würde ich gerne libre baskerville verwenden. die deutschlandflagge soll auch zu sehen sein (am besten oben beim namen des projekts) und das projekt soll auch einfach nur (erstmal) 12 axes Deutschland heißen. bitte gestalte das einmal richtig konsequent durch und bleibe aber beim gleichen spirit.
>
> achso und https://contralabs.com/ war ursprünglich die design/spirit-inspiration

Stevens anschließender Handbuchauftrag im Wortlaut:

> du hast hier scheinbar extrem viel arbeit in das redesign gesteckt. baue daraus ein handbuch anhand dessen neue agents in zukunft die seite gestalten und texte schreiben müssen. die ganze UI/UX soll anhand dieses handbuchs geführt werden können

## 2026-10-03: Abschluss von Gestaltung und Handbuch

- Agent: Codex über T3 Code, `gpt-6.1-sol`, Reasoning `max`.
- Umfang: Prüfung des Chatkontexts, des Redesigns und des Handbuchs; Ergänzung der Browserbefehle, der Schriftgrößenskala und der Ausnahmen für Bild-Platzhalterfarben; Aktualisierung der Prüfberichte. Keine Änderung der Gestaltung oder des Produktumfangs.
- Prüfungen: `pnpm check` und `git diff --check` bestanden. Eigene Desktop-Stichprobe in der T3-Vorschau und visuelle Prüfung der vorhandenen Screenshots; der Größenwechsel der Vorschau brach wiederholt ab. Einzelheiten und Grenzen stehen in `validation.md`. Keine wissenschaftliche Abnahme.

Stevens Abschlussauftrag im Wortlaut:

> dann mach das noch und schiebs dann direkt zu main
