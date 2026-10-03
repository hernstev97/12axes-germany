# Auftrag S1: Strukturprüfung veröffentlichter Eurobarometer-Tabellen (technische Rolle)

Du bist die getrennte technische Rolle nach dem Entwurf `docs/analyseplan-v2.3.entwurf.md`, Abschnitte 4, 6 und 10. Die Auswahlrolle (Claude als Koordinator und Planautor) darf keine Antwortverteilungen sehen. Deine Ausgaben dürfen deshalb keine Anteile, Prozentwerte, Mittelwerte, Rangfolgen oder Aussagen über Ergebnisse enthalten, auch nicht indirekt („die meisten stimmen zu“). Ungewichtete und gewichtete Fallzahlen (Basis) sind erlaubt.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`. Lies zuerst `reports/claude/agenten/R10-quellenblocker.md` Abschnitte 4 (Eurobarometer) und 5, `reports/claude/agenten/R6-eurobarometer.md` Abschnitte 2, 4 und 6, `reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.md` Abschnitt 6.3 und 6.7.

Rechtsrahmen: Nach R10 erlaubt die Weiterverwendungsregel der Kommission (Beschluss 2011/833/EU, teils CC BY 4.0) die Verarbeitung der von der Kommission veröffentlichten Tabellen durch Agenten. Nutze nur Dateien, die die Kommission selbst ohne Anmeldung veröffentlicht (data.europa.eu, europa.eu/eurobarometer). Keine GESIS-Server, keine Einzeldaten, keine Anmeldung, keine Nachrichten.

## Gegenstand

Die Tabellen („Volumes“, insbesondere A und C, sonst die verfügbaren) zu diesen Erhebungen, soweit veröffentlicht: Standard-Eurobarometer 104 und 105, Spezial-Eurobarometer 559, 564, 565 und 572, Flash-Eurobarometer 561, dazu die in R6 und R10 genannten Trendfragen SE035, SE037, SE038, SE040, SE050, ST0350, ST0359 und ST0939 in der jeweils jüngsten Welle 2025/26.

## Vorgehen

1. Lade die Dateien nach `outputs/claude/s1/` (von Git ausgeschlossen). Notiere URL, Dateiname, Größe, SHA-256 und Lizenzangabe.
2. Schreibe ein Skript `reports/claude/kontrollrechnung/s1_struktur.py` (nur Python-Standardbibliothek oder die isolierte Umgebung `outputs/claude/venv-readstat` mit pandas; für xlsx darfst du dort `openpyxl` nachinstallieren). Es gibt aus jeder Datei nur Struktur aus: Blattnamen, Tabellenköpfe, Spaltenköpfe, Zeilenbeschriftungen, Beschriftungen von Basiszeilen, Fußnoten. Jeder Zellinhalt, der eine Zahl ist, wird durch `#` ersetzt, außer in Zeilen, deren Beschriftung eine Basis oder Fallzahl bezeichnet. Öffne die Dateien nicht anders und gib nie unmaskierte Werte aus.
3. Lies die Technischen Spezifikationen der Wellen für Feldzeit, Modus, Population, Stichprobe und Gewichtung in Deutschland. Diese Dokumente enthalten keine Ergebnisse. Wenn doch, nur die Methodenseiten lesen.

## Ausgabe

`reports/claude/agenten/S1-strukturpruefung-eurobarometer.md` und `.json`. Je Erhebung und je Frage (Kennung wie in der Tabelle) ein Eintrag mit genau diesen Feldern, ohne Werte:

`erhebung`, `welle`, `datei`, `sha256`, `lizenz`, `frageKennung`, `frageTextInTabelle` (Sprache angeben), `spalteDeutschlandGesamt` (ja/nein/nur West und Ost), `kategorienEinzeln` (Liste der Beschriftungen), `weissNichtGetrennt` (ja/nein), `verweigertGetrennt` (ja/nein/nicht vorhanden), `zusammengefassteKategorien` (Liste), `basisUngewichtetDeutschland` (Zahl oder „fehlt“), `basisGewichtetDeutschland` (Zahl oder „fehlt“), `filterOderSplit` (Text), `gewichtungDeutschland` (Text aus der Tabelle oder Spezifikation), `feldzeitDeutschland`, `modusDeutschland`, `rundung`, `gliederungsmerkmaleVolumeC` (Liste der Beschriftungen, ohne Werte), `zuordnungZumFragebogen` (eindeutig/unklar), `bedingungenR10Abschnitt5_3` (je Punkt 1–9: erfüllt, nicht erfüllt, ungeprüft), `offen`.

Am Ende des Berichts: geöffnete Quellen mit Uhrzeit (UTC), ausgeführte Befehle, Grenzen, Modell laut Laufzeit, und die ausdrückliche Bestätigung, dass der Bericht keine Ergebniswerte enthält. Ändere keine anderen Dateien, keine Commits.
