# Öffentliche Texte zum Forschungsstand v2

Stand: 2026-10-03. Autor: Codex-Subagent `angular_policy_draft`. Inhaltspaket zur anschließenden begrenzten Inhaltsprüfung und Browserprüfung durch Root; keine eigene Freigabe.

## Änderungen und Grenzen

Die Startseite, Projektseite und Methodik unterscheiden jetzt ausgeführte Forschung und offene Produktarbeit: 43 Originalangaben aus fünf historischen ESS-Studien, acht Themenrubriken, fünf getrennte Einzelstudienläufe und 42 begrenzt geprüfte Einzelreferenzen. Die alte Aussage „Vergleichswerte: Noch nicht berechnet“ entfällt. `cttresa` bleibt ausdrücklich ohne Vergleichszahlen. Die Methodik erklärt die vorab festgelegte 100/5-Darstellungsheuristik und deren fehlenden Präzisions-/Anonymitätsnachweis. Es wurden keine Analysezahlen manuell ergänzt.

Die Rubriken sind keine gemeinsamen Messdimensionen. Die Texte behaupten keine aktuelle Bevölkerungsnorm, gleichartige neue Webdurchführung, Standardfehler, Konfidenzintervalle, Parteiprogramme oder Gesamtmatches. Die historische Neunfragenfassung bleibt ein begrenztes Teilmodul. Der breite Themenbericht steht in gezielter Darstellungsprüfung; die separate historische Gruppenanalyse läuft nur für ESS5, ESS8 und ESS9. Ihre Ergebnisse und Anzeige werden ausdrücklich als ausstehend bezeichnet. Dazu wurden keine Ergebnisdateien gelesen.

Die Pflichtformel zur fehlenden Validierung, wissenschaftlichen Prüfung und Neutralitätsgarantie bleibt erhalten. Zwei getrennte Codex-Rollen werden mit ihrem begrenzten Prüfumfang und der gemeinsamen Modellfamilie benannt. Claude-Schlusskontrolle durch Steven, menschliche Gestaltungs-/Verständnis-/Releasefreigaben bleiben offen. Es gibt weiterhin keinen öffentlichen Teststart.

Geändert wurden ausschließlich:

- `web/src/app/pages/home/home.html`
- `web/src/app/pages/project/project.html`
- `web/src/app/pages/project/project.ts`: ausschließlich bestehende sichtbare `status`-Textwerte und Formatierung, wie von Root zusätzlich bestätigt.
- `web/src/app/pages/methodology/methodology.html`
- Dieser neue Bericht; eigene QA liegt im ignorierten `outputs/public-research-status-v2/`.

Styles, Routen, AppShell, Hauptnavigation, Fragenentwurf, Originalkatalog und wissenschaftliche Artefakte wurden nicht geändert. Bestehende Quellenlinks wurden ergänzt beziehungsweise auf die aktuelle öffentliche Planfassung verwiesen. Die fünf Studienzeilen der Methodik mit Ausgaben, Erhebungszeiten und Modi sind bytegleich zur Ausgangsfassung. Keine Git-, Server-, Netzwerk-, Installations-, Rohdaten- oder `data/local`-Aktionen.

## Quellen und Claimbindung

Vor Änderungen vollständig gelesen: `docs/project.md` und `docs/handbuch.md`; das Handbuch ersetzt die nicht mehr vorhandene `docs/design.md`. Zusätzlich gelesen: `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md`, `docs/entscheidungen.md`, die drei bisherigen Seitentemplates, ihre Komponenten und `.agents/skills/unslop/SKILL.md`. Die Textwerte wurden nach Handbuch Kapitel 7 und der Skill redigiert. Die alten Forschungsabschnitte wurden als historischer Plan behandelt.

| Aussage | Öffentliche Quelle und Reichweite |
| --- | --- |
| 43 Angaben, fünf Studien, acht Rubriken | `data/politikprofil-v2.fragen.entwurf.json`: ausschließlich öffentliche Studien-/Itemmetadaten maschinell nachgezählt; 43 eindeutige IDs. `docs/empirie-plan-v2.entwurf.md:15–26`, `docs/messformen-v2.entwurf.md:7`. Keine Antworten gelesen. |
| Eigene Einzelangaben ohne gemeinsames Messmodell; Inhaltslücken | `docs/empirie-plan-v2.entwurf.md:5–9`, `docs/messformen-v2.entwurf.md:21–35`, `docs/abdeckung-v2.md`. |
| Ausgaben, tatsächliche Feldzeiten, 15+-Zielpopulation, Modi, ESS8/München | Öffentliche JSON-Studienmetadaten und `docs/abdeckung-v2.md:38–43`; vorhandene Methodikliste unverändert. Zielpopulation ist kein Nachweis vollständiger tatsächlicher Abdeckung. |
| 42 Referenzen, `cttresa` ohne Zahlen, Gewicht und fehlende SE | `data/reference-v2/README.md:3–5`. Gewicht `pspwght`, gültiger Frage-Nenner, Missing/Sensitivität getrennt; keine aktuelle Norm. |
| Darstellungsheuristik, Nenner, Kontextänderungen | `docs/empirie-plan-v2.entwurf.md:28–30,42–64`. Unter 100 gültigen Antworten oder beobachtete Kategorie mit ein bis vier ungewichteten Fällen: Referenz unterdrücken, keine neue Güteschwelle behaupten. B1–B12 und B25-Nachlaufgrenze eng beschrieben. |
| Tatsächlich gesicherter Plan/Tag, fünf Läufe, zwei Rollen, laufende Gruppenanalyse und offene Abnahmen | Gesicherte Tatsachen im aktuellen Root-Auftrag. Die ursprünglichen Zukunftssätze der Quellenpläne werden nicht als heutiger Ablauf ausgegeben. Es wurde kein Tagname erfunden, kein Ersturteil zur Verteidigung gelesen und keine Gruppenfreigabe auf weitere Studien übertragen. |

Ein read-only Hilfsagent `public_claim_inventory` hat ausschließlich die fünf benannten öffentlichen Quellen inventarisiert. Er bestätigte dieselben Metadatenzählungen und Zeit-/Versionsgrenzen, änderte keine Dateien und ist beendet. Dies ersetzt den noch ausstehenden unabhängigen Inhaltsreview nicht.

Offener Quellenunterschied, ohne Richtigkeitsurteil: `data/reference-v2/README.md:11` nennt für die ESS11-Dokumentation `10.21338/nsd-ess11-2023`; `data/politikprofil-v2.fragen.entwurf.json:735–737` nennt `10.21338/ess11-2023` einschließlich des überlieferten Zitationstexts. Beide nennen für den Datensatz dieselbe DOI `10.21338/ess11e04_2`. Die Seiten verwenden diese übereinstimmende Daten-DOI; die Dokumentationsdifferenz bleibt zur getrennten Primärklärung bei Root. Keine Quelle wurde als falsch bezeichnet. Der ESS10-SC-Unterschied zwischen tatsächlicher Ausgabe/DOI 3.2 und teilweise überliefertem Zitationstext 3.1 bleibt unverändert in den öffentlichen Quellen.

## Tatsächliche technische Checks

- Erster `pnpm check`: **Exit 1 beim globalen Formatter**, Warnungen zu `reports/loop/group-v21-access-disclosure.json` und `reports/loop/group-v21-run-receipts.json`. Diese parallelen, bereits gepinnten Dateien wurden weder gelesen noch geändert. Root erhält ihre Originalbytes über explizite Formatterausnahmen. Der fehlgeschlagene Gesamtlauf bleibt dokumentiert; spätere Root-Checks werden hier nicht vorweggenommen.
- Erster eigener Handbuchcheck: **Exit 1**, Semikolon im neuen Startseitentext. In zwei Sätze korrigiert. Abschließender `pnpm check:handbuch`: **Exit 0**, neun Gemälde, 43 Quelldateien und Seitentitel bestanden.
- Eigener Scopecheck zunächst mit **Exit 1**: Er behandelte zusätzliche Formatierungs-Kommas in `project.ts` als Logikänderung. Nach Normalisierung dieser optionalen Kommas: **Exit 0**. Seitenstruktur, IDs, Kunstbindungen und Primäraktionen unverändert; TS außerhalb der Textwerte semantisch unverändert; historische Studienliste bytegleich; 43/5/8-Metadaten bestätigt. Skript und Ergebnis liegen nur in ignorierter QA.
- `pnpm exec prettier --check` für die vier geänderten Seitendateien und abschließend zusätzlich diesen Bericht: **Exit 0**.
- `pnpm typecheck`: **Exit 0**, Angular- und Spec-Typecheck bestanden.
- `pnpm test`: **Exit 0**, **71/71 Tests** in sechs Dateien; Bundleabschluss `2026-10-03T15:34:05.796Z`, Testdauer 6,82 s. Keine zusätzlichen Tests für reine Textwerte geschrieben.
- `pnpm build`: **Exit 0**, normaler Produktionsbuild, Abschluss `2026-10-03T15:34:07.250Z`.

Kein Browser wurde gestartet. Desktop-/Smartphone-Layout, Zoom, Tastatur und axe sind für diese Textfassung noch durch Root zu beobachten. Technische Checks und Metadatenzählung sind keine sachliche, wissenschaftliche oder menschliche Abnahme. Die vier Seitendateien bleiben nach diesem Paket für die feste Inhaltsprüfung unverändert.

## SHA256 der geprüften Fassung

| Datei | SHA256 |
| --- | --- |
| `home/home.html` | `c2530f88e3e1491333c24e0ccb4e12341ac11a8de987e96ee8c71bbd99b510fc` |
| `project/project.html` | `2fd16b5fecd8792804a4420985a5c6c837ea75c9e07bc048fda4fd726d13b137` |
| `project/project.ts` | `d7f09ba634b61f13c6f07657e78b05fb16a672a48d2eb0627d9b911c3e3cabcf` |
| `methodology/methodology.html` | `5bfb0ee79cd9dfd2714cd53492652281db562d4da907e70a3f6127dc73321f99` |
| `docs/project.md` | `50fd74dc5612293f22591e679856dbb09745ef2ff9a217ff5583b219cf224328` |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |
| `docs/abdeckung-v2.md` | `77ae3d328c4862d1396e72207e5e1401dfa4da1f57580315e973943d3dfad945` |
| `docs/empirie-plan-v2.entwurf.md` | `2b0cd26f8fba81bbf520b9ae3411d623f9299c9ff707aacf681bde4c65a0439f` |
| `docs/messformen-v2.entwurf.md` | `0536441391becb9ac84e4b9596b20e2e0e4aab1a9aef827cbc162f8d7261238b` |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `data/reference-v2/README.md` | `a2917e6b57c59e96298345e526e9311de82b1422cfbb9a8bb1cfabc0684ba57c` |
