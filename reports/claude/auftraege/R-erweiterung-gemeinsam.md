# Gemeinsamer Teil der Recherche zum Erweiterungspaket 2025/26 (R8–R10)

Stand: 4. Oktober 2026. Auftraggeber: Claude als Koordinator von LIFE-93 im Auftrag von Steven.

Hintergrund: Das Profil „12 Axes Deutschland“ nutzt 62 Originalfragen aus fünf ESS-Befragungen (2010 bis 2023). Für sechs Bereiche fehlen eigene Fragen: Arbeit und Rente, Gesundheit und Pflege, Wohnen, Außen-, Verteidigungs- und Friedenspolitik, Bildung und Forschung, Medien und Digitalpolitik. Die Wählergruppen beruhen auf der erinnerten Zweitstimme bei den Bundestagswahlen 2009, 2013 und 2017. Lies zuerst `docs/abdeckung-v2.2.md` (Matrix und Nachtrag) und die Berichte unter `reports/claude/agenten/` R1, R2, R3, R5, R6 und R7. Baue auf ihnen auf und wiederhole keine dort schon belegte Recherche. Prüfe ihre Aussagen dort nach, wo deine Empfehlung davon abhängt.

Für jede Erhebung, die du als Kandidat nennst, dokumentiere mit Fundstelle (URL, Dokument, Seite):
1. Feldzeit, deutsche Zielpopulation (Alter, Staatsangehörigkeit, Haushalte), Stichprobenverfahren (Zufall, Register, Quote, Online-Panel), Modus, Fallzahl laut Dokumentation, Gewichte.
2. Fragenkandidaten mit Fragenummer, deutschem Wortlaut (wörtlich, falls öffentlich), Antwortkategorien, Fragekontext (Einleitung, Filter, vorangehende Fragen, eingeblendete Informationen oder Begründungen im Fragetext).
3. Zugangsweg (öffentliche Tabelle, Einzeldaten mit Anmeldung, Vertrag, nur Bericht) und die einschlägigen Nutzungsbedingungen wörtlich mit URL. Wenn keine Regel zu KI-Systemen zu finden ist, schreibe genau das und deute es weder als Erlaubnis noch als zusätzliche Genehmigungspflicht.
4. Ob eine Wahlrückerinnerung zur Bundestagswahl vom 23. Februar 2025 oder eine andere Parteifrage vorliegt, und in welcher Form.

Trenne in jedem Bereich drei Ebenen mit eigenen Belegen: aktuelle Gesetzeslage (Gesetz, Fundstelle, Stand), politische Vorschläge (wer, wo, wann) und Erhebungen, die Einstellungen dazu messen. Nenne von den Erhebungen nur Fragen und Methoden, keine Ergebnisse.

Regeln:
- Ergebnisblind: Keine Antwortverteilungen, Prozentwerte oder Ergebnisse recherchieren, lesen oder berichten. Öffne nur Fragebögen, Methoden-, Lizenz- und Rechtsdokumente. Wenn eine Quelle Fragen nur zusammen mit Ergebnissen veröffentlicht (etwa Berichte mit Grafiken), öffne sie nicht, sondern vermerke sie als „nur mit Ergebnissen veröffentlicht, Strukturprüfung durch getrennten Agenten nötig“. Ungefragt angezeigte Ergebnisse nicht verwenden und vermerken.
- GESIS-Sperre: Keine neuen Abrufe von gesis.org oder anderen GESIS-Servern, auch keine Fragebögen. GLES, ISSP, ALLBUS, Politbarometer, EVS, Eurobarometer-Einzeldaten und andere GESIS-Bestände nur mit den Angaben aus R1–R7 nennen und als gesperrt kennzeichnen.
- Keine Anmeldungen, keine Zustimmung zu Bedingungen, keine Downloads hinter Formularen, keine Nachrichten an Dritte.
- Lies nichts unter `data/raw/`, `data/local/`, `outputs/`, `data/reference-*`, `reports/phasen/02-*`, `03-*`, `04-*` und `web/src/app/policy-draft/reviewed-*`.
- Ändere keine Dateien außer deinen beiden Ausgabedateien. Keine Commits.
- Fragen aus Befragungen von Kandidierenden oder Abgeordneten begründen keine Bevölkerungsvergleiche. Fragen mit Begründung oder Prämisse im Fragetext kennzeichnen.
- Online-Quotenstichproben sind zulässige Kandidaten, aber getrennt von Zufallsstichproben zu kennzeichnen.

Ausgabe: ein Bericht auf Deutsch (sachlich, ohne Werbesprache) und eine JSON-Datei mit einem Eintrag je Fragenkandidat: `id`, `bereich`, `erhebung`, `feldzeit`, `population`, `stichprobe`, `modus`, `fallzahl`, `fragenummer`, `wortlautDe` (oder null), `antwortkategorien`, `kontext`, `zugang`, `bedingungen`, `wahlfrage`, `ebene` (national, EU, international), `belege` (URLs mit Seite), `offenePunkte`. Am Ende des Berichts: tatsächlich geöffnete Quellen mit Uhrzeit (UTC), ausgeführte Befehle, Grenzen der eigenen Prüfung, Modell laut Laufzeit.
