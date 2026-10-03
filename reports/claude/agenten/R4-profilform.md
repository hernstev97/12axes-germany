# R4 – Welche Form eines erklärenden Profils tragen die Belege?

Stand: 2026-10-03, Bericht eines getrennten Claude-Subagenten für den Koordinator. Ausgangsstand Commit `e9898fb423a3ba9fbe6387ed9215dbe83666aedc`, Branch `research/life-93-claude-20261003`.

Dieser Bericht ist Literatur- und Methodenarbeit. Er enthält keine Datenanalyse, keine Antwortverteilungen und keine Freigabe. Er ist keine Begutachtung durch Fachleute. Übereinstimmung mit früheren Codex-Entscheidungen belegt keine Richtigkeit.

Kennzeichnung der Quellennutzung in diesem Bericht:

- **[V]** Volltext oder die genannten Abschnitte selbst gelesen (PDF lokal unter `/tmp/r4/`, nicht im Repository).
- **[W]** Volltext nur über das Webwerkzeug gelesen; Zitate stammen aus dessen Auszug.
- **[A]** nur Abstract oder bibliografische Metadaten (OpenAlex) eingesehen.
- **[S]** nicht selbst geöffnet, nur über die genannte Sekundärquelle bekannt.

---

## Kurzfassung

1. Für keine der acht Themenrubriken trägt die Literatur einen Themenwert, eine Achse oder einen Gesamtwert für diesen Fragenbestand. Das gilt auch dort, wo die Originalentwickler eine Skala beabsichtigten: Der Itemsatz ist gekürzt, das Antwortformat gemischt, die geprüfte Population eine andere oder die Prüfung betraf Ländervergleiche statt Einzelpersonen.
2. Mehrere Moduldokumente sprechen ausdrücklich gegen eine Zusammenfassung. Für die ESS8-Fragen E33–E36 zur Zukunft des Sozialstaats nehmen die Entwickler ausdrücklich keinen gemeinsamen Faktor an (ESS8-Template S. 18–19). Die ESS11-Gleichstellungsfragen E19–E22 sind vier getrennte „simple concepts“ (ESS11-Template S. 11–12, 36–38). Die ESS9-Gerechtigkeitsfragen sind je ein manifester Indikator eines eigenen Prinzips (Adriaans/Fourré 2022, S. 3).
3. Für genau den vorhandenen Itemsatz hatten drei Blöcke eine reflektive Skalenabsicht der Entwickler: Zuwanderungszulassung A54–A56, staatliche Verantwortung E6–E8 (ESS8) und Rechtsgehorsam D34–D36 (ESS5). Nur für A54–A56 habe ich eine veröffentlichte Strukturprüfung selbst gelesen (Davidov u. a. 2015). Sie betrifft Ländermittelwerte in ESS-Runden 1–6, nicht die deutsche Selbstausfüllerfassung ESS10 und nicht die Rückmeldung an Einzelpersonen.
4. Empfohlen wird ein **belegtes Antwortprofil in drei Stufen**: Einzelaussage je Antwort, Muster innerhalb eines Originalblocks mit gleichem Antwortformat, und vorab festgelegte „Querbezüge“ zwischen Fragen mit gemeinsamem Inhaltselement. Querbezüge stellen Antworten nebeneinander und rechnen nichts.
5. Jede übergreifende Aussage zeigt ihre Beleggrundlage: beteiligte Fragen mit Studie und Jahr, gewählte Antworten, ein festes Kontextmerkmal je Frage und die Quelle der Gruppierung.
6. Unterschiedliche Antworten werden über Kontextmerkmale der Fragen erklärt, nie als Widerspruch der Person. Literatur stützt das: Gerechtigkeitsprinzipien schließen einander nicht aus (Adriaans/Fourré 2022, S. 2); Sozialstaatseinstellungen sind mehrdimensional (Roosma u. a. 2013, S. 235, 240); Antworten hängen von Frageform und aktuell präsenten Überlegungen ab (Zaller/Feldman 1992 [A]).
7. „Weder noch“ und ähnliche Kategorien werden wörtlich wiedergegeben, nie als „neutral“, „gemäßigt“ oder „Mitte“ der Person. Die mittlere Kategorie dient nachweislich auch als verdecktes „Weiß nicht“ oder als Zurückweisung der Frageprämisse (Sturgis u. a. 2014 [A]; Baka u. a. 2012 [A]; Kamoen/Holleman 2017, S. 125, 128 [V]).
8. Ausgelassene Fragen, „Weiß nicht“ und Verweigerung erzeugen keine Aussage, keine Ersatzposition und keinen Vergleich.
9. Bei 0–10-Skalen werden nur Zahl und Originalanker gezeigt. Verbale Zwischenstufen („hoch“, „eher wichtig“) wären erfunden. Bei den ESS10-Demokratiefragen dokumentieren die Entwickler starke Häufung hoher Werte (ESS10-Pilotdokumentation S. 6; ESS10-Antrag S. 9).
10. Historische Vergleiche bleiben streng itemweise: ein Anteil je Kategorie, mit Studie, Feldzeit, Population und Nenner. Kein Gesamtvergleich, keine Perzentile, keine Wörter wie „Mehrheit“ ohne Zahl (van der Bles u. a. 2019, Abschnitt 6.1.3).
11. Nebenbefunde zum vorhandenen Entwurf: Mehrere statische Erläuterungen in `web/src/app/policy-draft/item-meanings.ts` sprechen von „Zustimmung“ oder „Unterstützung“, auch wenn die Person abgelehnt hat. `hrshsnta` (D33) steht in der Gruppe `law_obligation`, gehört im ESS5-Moduldesign aber zum Konzept „Punitive attitudes“, nicht zum Rechtsgehorsam. Die ESS8-Vierer-Skalen kodieren `1 = Sehr dagegen`, die Fünfer-Skalen zu Klima und Gleichstellung `1 = Sehr dafür`.
12. Offen für Steven: ob historische Verteilungen nach jeder Antwort oder erst im Abschlussprofil erscheinen. Ein US-Experiment fand Einflüsse von Umfrageinformation auf Einstellungen (Rothschild/Malhotra 2014 [A]); die Übertragung auf diesen Test ist ungeprüft.

---

## 1 Grundlage und Vorgehen

Gelesen im Repository: `AGENTS.md`, `docs/project.md`, `docs/empirie-plan-v2.entwurf.md`, `docs/messformen-v2.entwurf.md`, `docs/abdeckung-v2.md`, `docs/konstruktakten.entwurf.md`, `docs/deutschland-literatur.entwurf.md`, Kapitel 7 von `docs/handbuch.md`, die Quellenlisten in `data/theorie-quellen.json` und `data/methoden-quellen.json` (nur Titel/DOIs), `data/politikprofil-v2.fragen.entwurf.json` (Wortlaute, Kategorien, Missing-Codes, Gruppen) und `web/src/app/policy-draft/item-meanings.ts` (statische Erläuterungstexte, keine Verteilungen).

Nicht gelesen: `data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`, `data/raw/`, `data/local/`, sowie die Berichte anderer Claude-Subagenten unter `reports/claude/agenten/`.

Die Literatur habe ich selbst über offene Quellen geladen (ESS-Website, Repositorien, Autorenseiten, Verlags-OA). Springer, ScienceDirect, OUP und Royal Society lieferten bei direktem Abruf Abfrage- oder Sperrseiten. Für diese Werke nutze ich offene Autorenfassungen, das Webwerkzeug oder nur Abstracts; die Kennzeichnung steht jeweils dabei.

Der Fragenbestand im Überblick (aus `data/politikprofil-v2.fragen.entwurf.json`):

| Antworttyp im Entwurf | Fragen | Kodierung |
| --- | --- | --- |
| Zustimmung, fünf Stufen | `sofrdst`, `sofrwrk`, `sofrpr`, `sofrprv`, `gincdif`, `hrshsnta`, `dbctvrd`, `lwstrob`, `rgbrklw` | 1 stimme stark zu … 3 weder noch … 5 lehne stark ab |
| Unterstützung, fünf Stufen | `inctxff`, `sbsrnen`, `banhhap`, `eqparep`, `eqparlv`, `freinsw`, `fineqpy` | 1 sehr dafür … 3 weder dafür noch dagegen … 5 sehr dagegen |
| Unterstützung, vier Stufen | `bnlwinc`, `eduunmp`, `wrkprbf` | 1 sehr dagegen, 2 dagegen, 3 dafür, 4 sehr dafür (keine Mitte, umgekehrte Kodierrichtung) |
| Zulassung, vier Stufen | `imsmetn`, `imdfetn`, `impcntr` | 1 vielen … 4 niemandem |
| 0–10 unipolar | `gvslvol`, `gvslvue`, `gvcldcr` (Verantwortung); B1–B12 (Wichtigkeit); `bplcdc`, `dpcstrb` (Pflicht) | nur 0 und 10 verbal beschriftet |
| 0–10 bipolar | `euftf` | 0 „Einigung ist schon zu weit gegangen“, 10 „sollte weitergehen“ |
| nominal | `scchpldm` (1/2), `vteurmmb` (1, 2, 33, 44, 55, 65), `imsclbn` (1–5) | keine Rangordnung |

---

## 2 Messkonzepte hinter den Fragengruppen (Auftragsteil 1)

### 2.1 Gerechtigkeitsprinzipien, ESS9 G26–G29 (`sofrdst`, `sofrwrk`, `sofrpr`, `sofrprv`)

**Originalkonzept.** Das ESS9-Modul ordnet die vier Fragen dem Komplexkonzept „Distributive justice: Basic normative principles“ zu und nennt vier getrennte Unterkonzepte: Gleichheit, Leistung (equity), Bedarf und Anrecht (entitlement). Jedes Unterkonzept ist als „Can be measured directly“ beschrieben. Die vier Fragen stammen aus einer ursprünglich achtteiligen Skala ([ESS9-Template „Justice and Fairness“](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS9_justice_final_module_template.pdf), S. 4, 33–36) [V]. Fußnote 31 (S. 36) definiert „social status“ ausdrücklich so, dass er aus Herkunft oder eigener Leistung stammen kann.

**Strukturbefund.** Die BSJO-Langfassung hat drei, die Kurzfassung zwei Items je Prinzip. In LINOS-1, SOEP-IS 2012 und ALLBUS 2014 ergaben Hauptkomponentenanalysen vier Faktoren. Die Autoren empfehlen Mittelwerte oder Faktorwerte **je Prinzip**, nicht über die Prinzipien hinweg (Liebig/Hülle/May, [SOEPpapers 831, 2016](https://www.diw.de/documents/publikationen/73/diw_01.c.530548.de/diw_sp0831.pdf), S. 7 Tabelle 2, S. 13–14, S. 23–24; PDF-S. 9, 15–16, 25–26) [V]. Die Zeitschriftenfassung Hülle/Liebig/May 2018 (DOI [10.1007/s11205-017-1580-x](https://doi.org/10.1007/s11205-017-1580-x)) war geschlossen; ich habe nur die Arbeitspapierfassung gelesen.

Für ESS9 gilt: „each item serves as a manifest indicator of one justice principle“. Die vier Prinzipien schließen einander nicht aus; Zustimmung zu Leistung und Bedarf zugleich ist als „Boulding principle“ beschrieben. Ob „entitlement“ ein eigenes Grundprinzip ist, ist in der Literatur weniger einig (Adriaans/Fourré 2022, [DOI 10.1186/s42409-022-00040-3](https://doi.org/10.1186/s42409-022-00040-3), S. 2 mit Fn. 2, S. 3) [V]. In der CRONOS-Panelwiederholung (Estland, Großbritannien, Slowenien, nicht Deutschland) lagen die Test-Retest-ICC je Item zwischen 0,32 und 0,65. Nach Zusammenfassung in Zustimmung/weder noch/Ablehnung stimmten 60 bis 82 % der Wiederholungsantworten überein. Die Autoren folgern, die Items erkennen Zustimmung oder Ablehnung verlässlich, den Grad aber weniger (S. 6–7) [V].

**Zusammenfassung zu einem Wert belegt?** Nein. Über die vier Prinzipien gibt es keinen gemeinsamen Wert; sie sind getrennte Dimensionen. Je Prinzip liegt nur ein Item vor, eine Teilskala ist daher ebenfalls nicht möglich.

**Zulässige Beschreibung.** Je Prinzip Zustimmung, „weder noch“ oder Ablehnung mit dem gewählten Originallabel. Auf Blockebene darf das Profil auflisten, welchen Prinzipien zugestimmt und welche abgelehnt wurden, und festhalten, dass gleichzeitige Zustimmung zu mehreren Prinzipien bekannt ist. Kein „dominantes Prinzip“ als Typ, kein Gegensatzpaar Gleichheit gegen Leistung. Die Stärke („stark“) wird wörtlich gezeigt, aber nicht weiter gedeutet.

### 2.2 Staatliche Einkommensverringerung, ESS11 B33 (`gincdif`)

Im ESS8-Welfare-Template steht dieselbe Kernfrage neben `dfincac` und `smdfslv`; die Entwickler erwarteten dort einen gemeinsamen latenten Faktor „Beliefs about inequality“ (ESS8-Template S. 24–25) [V]. Diese beiden Partnerfragen sind nicht im Bestand, und `gincdif` stammt hier aus ESS11. **Kein Wert belegt.** Zulässig ist nur die Einzelaussage zur Zustimmung oder Ablehnung staatlicher Maßnahmen gegen Einkommensunterschiede.

### 2.3 Staatliche Verantwortung, ESS8 E6–E8 (`gvslvol`, `gvslvue`, `gvcldcr`)

**Originalkonzept.** Die drei Fragen bilden das Konzept „Attitudes towards welfare state scope and responsibilities (AttScope)“. Die Entwickler erwarten positive Zusammenhänge, weil die Unterkonzepte „together indicate the overarching construct AttScope“ ([ESS8-Template Welfare](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS8_welfare_final_module_template.pdf), S. 8–9) [V]. Für die Wiederholung kürzten sie lange Batterien auf „the two or three strongest items only, i.e. the absolute minimum to estimate measurement models“ (S. 32) [V].

**Strukturbefund.** Roosma/Gelissen/van Oorschot prüften eine Sechs-Item-Fassung („range“, ESS4 D15–D20) in 22 Ländern einschließlich Deutschland und fanden partielle skalare Invarianz; sie bildeten Summenwerte (Roosma u. a. 2013, [DOI 10.1007/s11205-012-0099-4](https://doi.org/10.1007/s11205-012-0099-4), S. 241–243; die Lirias-PDF trägt keine Seitenzahlen, die Zählung folgt dem Zeitschriftenbeginn S. 235) [V]. Dieselbe Studie zeigt eine sehr hohe Unterstützung für diese Dimension im europäischen Pool (Tabelle 2, S. 244) und betont die Mehrdimensionalität von Sozialstaatseinstellungen (S. 235, 240). Eine veröffentlichte Strukturprüfung der ESS8-Dreierfassung für Deutschland habe ich nicht gefunden und nicht gelesen.

**Zusammenfassung belegt?** Nur als Entwicklerabsicht und für eine längere Vorgängerfassung. Für diese Webfassung **nicht belegt**. Ein späterer Wert bräuchte einen eigenen Plan mit deutscher ESS8-Prüfung.

**Zulässige Beschreibung.** Die drei Zahlen nebeneinander mit Ankern. Gleich oder unterschiedlich, und welche Gruppe den höchsten oder niedrigsten Wert erhielt. Das Template begründet die Gruppenunterscheidung inhaltlich: Die Solidaritätsdebatten betreffen die „deservingness“ bestimmter Gruppen wie Arbeitslose und erwerbstätige Eltern (S. 3–4) [V]. Unterschiede zwischen Alter, Arbeitslosigkeit und Kinderbetreuung sind daher eine inhaltliche Unterscheidung und kein Widerspruch.

### 2.4 Sozialstaatsreformen, ESS8 E33–E35 (`bnlwinc`, `eduunmp`, `wrkprbf`)

Die Entwickler schreiben zu jedem dieser Unterkonzepte: „We do not hypothesize that the sub concepts are interrelated in a linear way (e.g. constituting a single factor). Instead, we do expect that a typology can be constructed … How these combinations look like precisely, is an empirical question.“ (ESS8-Template S. 18–19) [V]. Jede Frage enthält eine ausdrückliche Gegenleistung oder Folge: Selektivität mit Folgen für mittlere und hohe Einkommen, Umschichtung bei fester Geldsumme, zusätzliche Leistungen trotz „deutlich höherer Steuern für alle“ (S. 17–19).

**Kein Wert und keine Typzuordnung belegt.** Die erwartete Typologie ist nach dem Template eine offene empirische Frage. Zulässig sind drei Einzelaussagen, jeweils mit der genannten Folge als Kontextmerkmal.

### 2.5 Demokratieverständnis, ESS10 B1–B12 und B25

**Originalkonzept.** Das ESS6-Modul unterschied sechs Dimensionen, darunter elektorale, liberale, soziale und direktdemokratische; die Auswertung der Topline beschränkt sich auf diese vier (Ferrín/Kriesi, [ESS Topline Results Issue 4](https://www.europeansocialsurvey.org/sites/default/files/2023-06/TL4-Democracy-English.pdf), S. 3 mit Tabelle 1) [V]. Die ESS10-Wiederholung ergänzte ein „populistisches“ Modell und eine EU-Mehrebenenfrage. Die Pilotdokumentation ordnet zu: B5 `votedir` direkte Demokratie; B1 `fairelc`, B2 `dfprtal`, B3 `medcrgv`, B4 `rghmgpr`, B6 `cttresa`, B7 `gptpelc`, B12 `keydec` und B25 `scchpldm` liberales Modell; B10 `viepol` und B11 `wpestop` populistisches Modell; B8 `gvctzpv` und B9 `grdfinc` soziales Modell ([ESS10-Pilotdokumentation, 5. Juli 2023](https://www.europeansocialsurvey.org/sites/default/files/2024-02/ESS10_Democracy_Pretest_Pilot.pdf), S. 2–3, 8, 15, 28, 38, 65–66, 77, 94) [V]. Der ältere ESS10-Antrag führte die Responsivitätsfrage (heute B25) dagegen im populistischen Modell (Antrag S. 13). Die Zuordnung ist also selbst nicht stabil.

**Strukturbefund.** Für ESS6 beschreibt der ESS10-Antrag eine liberale Skala aus zwölf, in der Kürzung sechs Items. Gerechnet wurde mit Mokken-Skalierung dichotomisierter Items (Loevinger H 0,62 bzw. 0,63, Cronbachs α 0,91 bzw. 0,84 im europäischen ESS6-Pool; [ESS10-Antrag](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS10_democracy_proposal.pdf), S. 11–12) [V]. Die gekürzte Sechserliste enthielt die Gerichtskontrolle der Regierung. Diese Frage wurde in ESS10 gestrichen (Pilotdokumentation S. 2, „Horizontal accountability (DROPPED)“), dafür kam die Pressefreiheit hinzu. Die Kennwerte gelten also nicht für den hier vorhandenen Itemsatz. Das soziale Modell hat zwei, das direkte eines, das populistische hier zwei Items.

Drei dokumentierte Messprobleme sind für die Profilform wichtig:

- **Deckeneffekt.** „The mean importance of almost all views items is above 8, and variance is relatively low“ (ESS10-Antrag S. 9). Die Entwickler werteten Wichtigkeitsfragen teils als 10 gegen 0–9 aus (Pilotdokumentation S. 6) [V].
- **Formatbruch.** Fragen im Trade-off-Format wie B25 „cannot be combined with the other three scales, since the pattern of answers is totally different due to the format“ (ESS10-Antrag S. 10) [V].
- **Unfertiges Populismuskonzept.** Die Messung sei „a work in progress“ (Pilotdokumentation S. 78) [V].

Zur EU-Frage B12 notiert die Pilotdokumentation nur eine „very slight positive correlation“ mit der Einigungsfrage im Pilot in Österreich und Großbritannien (S. 35). Die Vorgängerfrage aus ESS6 „does not scale well with the other items of the liberal democracy model“ (S. 29) [V].

Die Vorstellungen von Ferrín/Kriesi 2016 (Buch) und Kriesi/Saris/Moncagatta 2016 kenne ich nur über diese ESS-Dokumente [S].

**Zusammenfassung belegt?** Nein, weder als Demokratiewert noch als Modellwerte. Kein „Populismuswert“.

**Zulässige Beschreibung.** Die elf Zahlen B1–B11 mit Ankern (B12 erscheint unter EU, mit Verweis auf den Block). Musteraussagen nur innerhalb des Blocks: welche Aspekte den höchsten und den niedrigsten gewählten Wert erhielten, oder dass alle gleich bewertet wurden. Die Modellzuordnung der Entwickler darf als Lesehilfe erscheinen, gekennzeichnet als „Zuordnung laut ESS-Modulentwicklern“, ohne Werte je Modell. B25 wird als gewählte Alternative beschrieben, mit dem Hinweis, dass die Originalanschlussfragen fehlen. Jede Frage trägt das Kontextmerkmal „Wichtigkeit für die Demokratie im Allgemeinen, keine Bewertung Deutschlands“.

### 2.6 Pflicht gegenüber der Polizei, ESS5 D18 und D20 (`bplcdc`, `dpcstrb`)

**Originalkonzept.** D18–D20 messen „Obligation to obey the police“, ein reflektives Unterkonzept. Zusammen mit „moral alignment“ und „perceived legality“ bildet es die formativ verstandene „perceived legitimacy of the police“ ([ESS5-Template](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS5_final_trust_in_police_courts_.pdf), S. 4–5, 20, 22–23) [V]. Ob Pflicht und moralische Übereinstimmung gemeinsam skalieren, nennen die Entwickler „an empirical question“ (S. 20). Die ESS5-Topline beschreibt dieselben drei Legitimitätsdimensionen ([ESS Topline Issue 1](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS5_toplines_issue_1_trust_in_justice.pdf), S. 7) [V].

**Strukturbefund und Kritik.** D19 fehlt im Bestand; vorhanden sind zwei von drei Items. Jackson fasst Tankebes Einwand zusammen: Menschen können eine Pflicht zum Gehorsam auch aus „prudential and/or instrumental“ Gründen empfinden; Forschende könnten das fälschlich als Legitimität deuten (Jackson 2018, [Autorenfassung](https://researchonline.lse.ac.uk/id/eprint/87538/1/Jackson_Norms%20Normativity_Author.pdf), S. 9; Annual Review of Law and Social Science 14, 145–165) [V]. Jackson u. a. 2011 und 2012 habe ich nur als Abstract gesehen [A].

**Zusammenfassung belegt?** Nein. Mit zwei Items fehlt sowohl der vollständige Pflichtindikator als auch jede Legitimitätskomponente außer der Pflicht.

**Zulässige Beschreibung.** Zwei Zahlen mit Ankern „überhaupt nicht meine Pflicht“ und „voll und ganz meine Pflicht“. Die Fragen unterscheiden sich im Anlass: Widerspruch gegen eine Entscheidung (D18) gegenüber missbilligter Behandlung (D20). Keine Aussage über Legitimitätsglauben, Vertrauen oder Autoritätshaltung.

### 2.7 Gesetzesbindung und Strafen, ESS5 D33–D36 (`hrshsnta`, `dbctvrd`, `lwstrob`, `rgbrklw`)

**Originalkonzept.** D34–D36 messen „Obligation to obey the law and court decisions“ als reflektives Unterkonzept mit drei Items; D36 ist gegenläufig formuliert (ESS5-Template S. 4, 25–26) [V]. D33 gehört nicht dazu. Es ist ein Indikator des formativen Konzepts „Punitive attitudes“, zusammen mit einer Fallvignette D38, die nicht im Bestand ist (S. 4, 31–32) [V]. Die Entwickler kritisieren Items vom Typ „People who break the law should be given stiffer sentences“ selbst: Sie trennen den Wunsch zu strafen nicht von Einstellungen zum Justizsystem (S. 31). Für England und Wales berichten Hough u. a., die meisten Befragten unterschätzten die Härte der damaligen Strafpraxis ([MoJ Analytical Series 2013](https://eprints.lse.ac.uk/50440/1/Jackson_Attitudes_sentencing_trust_2013.pdf), S. 1) [V]. Ob das für Deutschland 2010/11 galt, habe ich nicht geprüft. Im ESS4-Welfare-Modul bildeten eine ähnliche Strafhärtefrage, eine Frage zur Gehorsamserziehung in Schulen und eine Frage zur Haft Terrorverdächtiger keinen starken gemeinsamen Faktor „Autoritarismus“ (α = 0,55 nach Mewes/Mau 2012; zitiert im ESS8-Template S. 32 [V], Originalstudie [S]).

**Zusammenfassung belegt?** Für D34–D36 besteht eine Skalenabsicht der Entwickler. Eine deutsche Strukturprüfung habe ich nicht gelesen. Für diese Webfassung **kein Wert**. D33 ist ein Einzelindikator eines anderen Konzepts.

**Zulässige Beschreibung.** Vier Einzelaussagen. Zustimmung zu „Alle Gesetze müssen strikt befolgt werden“ und zu „Manchmal muss man das Gesetz brechen, um das Richtige zu tun“ ist mit dem Kontextmerkmal „allgemeine Regel gegenüber Ausnahmefall ‚manchmal‘“ zu beschreiben, nicht als Widerspruch. D33 trägt immer das Kontextmerkmal „Vergleich mit Strafen in Deutschland zur Feldzeit 2010/11“. Keine Wörter wie „punitiv“, „autoritär“ oder „rechtstreu“.

### 2.8 Klimapolitische Maßnahmen, ESS8 D30–D32 (`inctxff`, `sbsrnen`, `banhhap`)

Das ESS8-Template führt die drei Fragen unter „Non-activist behaviours“: „tacit public support and acceptance of policies“; sie werden allen Befragten gestellt ([ESS8-Template Climate](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS8_climate_final_module_template.pdf), S. 10, 23–24) [V]. Eine Skalenaussage zu diesem Unterkonzept fand ich dort nicht. Die offizielle Topline berichtet die drei Maßnahmen getrennt als „push“ (Abgabe), „pull“ (Förderung) und Regulierung mit deutlich unterschiedlicher Zustimmung in Europa (Poortinga u. a., [ESS Topline Issue 9](https://www.europeansocialsurvey.org/sites/default/files/2023-06/TL9_Climate-Change-English.pdf), S. 13–14) [V]. Das Review von Drews/van den Bergh beschreibt, dass weniger zwingende „pull“-Maßnahmen meist mehr Zustimmung finden als „push“-Maßnahmen wie Steuern und Regulierung (Climate Policy 16(7), 855–876, Abschnitt 3.1, [Repositoriumsfassung](https://riuma.uma.es/bitstreams/f5a93e49-4abc-4d61-a6f4-3e37cefe9ef6/download) PDF-S. 7) [V].

**Kein Wert belegt.** Zulässig: Einzelaussagen je Instrument und die Blockaussage, ob die Antworten zwischen Abgabe, Förderung und Verkaufsverbot unterscheiden. Kein „Klimaschutzwert“.

### 2.9 Zuwanderung, ESS10 A54–A56 (`imsmetn`, `imdfetn`, `impcntr`) und ESS8 E15 (`imsclbn`)

**A54–A56.** Diese drei Kernfragen sind die am besten geprüfte Mehritemskala im Bestand. Davidov u. a. testeten sie als eine latente Variable über 35 Länder und sechs ESS-Runden (2002–2013), nur mit im Wohnland geborenen Befragten. Exakte skalare Invarianz scheiterte in vielen Ländern, approximative bayesianische Invarianz hielt (Davidov u. a. 2015, Public Opinion Quarterly 79(S1), 244–266; [Autorenfassung](https://lirias.kuleuven.be/retrieve/698f3cef-16ad-44f8-92d3-4ec4fa2453e7) S. 2, 15–16, 20) [V]. Die Prüfung zielt auf Vergleiche von Ländermittelwerten. Die ESS7-Topline dokumentiert eine stabile Rangfolge bevorzugter Zuwanderergruppen in allen 21 Ländern ([ESS Topline Issue 7, Heath/Richards](https://www.europeansocialsurvey.org/sites/default/files/2023-06/TL7-Immigration-English.pdf), S. 5) [V]. Unterschiede zwischen den drei Gruppen sind also inhaltlich bedeutsam und kein Messrauschen.

Eigene methodische Anmerkung, nicht aus den Quellen: Ein Ein-Faktor-Modell mit drei Indikatoren ist in einer einzelnen Gruppe gerade identifiziert und dort nicht auf Passung prüfbar. Die Davidov-Prüfung stützt sich auf Mehrgruppenrestriktionen.

**Zusammenfassung belegt?** Ja, aber nur unter anderen Bedingungen: ESS-Runden 1–6 im persönlichen Interview, Einheimische, Ländervergleich. Für die deutsche Selbstausfüllerfassung ESS10-SC, für Webnutzende und für individuelle Rückmeldung ist sie **nicht geprüft**. Empfehlung: im ersten Profil kein Wert. Ein späterer Wert wäre der am ehesten begründbare Kandidat, mit eigenem Plan.

**Zulässige Beschreibung.** Die drei gewählten Kategorien wörtlich. Blockaussage: gleiche Antwort für alle drei Gruppen oder Unterschiede, mit ordinaler Richtung („für die Gruppe X mehr Zuwanderung erlaubt als für Y“). Keine Gründe, keine Haltung zu Gruppen.

**E15 `imsclbn`.** Das ESS8-Template führt die Frage als einfaches Konzept „Welfare Chauvinism“ (S. 29) [V]. Reeskens/van Oorschot behandeln sie als nominal und schätzen multinomiale Modelle. Ihre Kategorienamen lauten Bedingung Aufenthalt, Gegenseitigkeit, Staatsbürgerschaft und Ausschluss (IJCS 53(2), 2012, S. 124–126, [Lirias](https://lirias.kuleuven.be/retrieve/187cf8c2-dd5e-481d-a272-fbbc606b4040)) [V]. Zulässig: die gewählte Bedingung als Satz. Das Modul-Etikett „Wohlfahrtschauvinismus“ ist eine Konzeptbezeichnung der Forschung und darf nicht als Personenbeschreibung erscheinen.

### 2.10 Europäische Integration (`vteurmmb`, `keydec`, `euftf`)

Die drei Fragen haben drei Aufgaben: hypothetische Abstimmung über die Mitgliedschaft, Wichtigkeit nationaler Entscheidungen für Demokratie im Allgemeinen, Richtung der Einigung auf 0–10. Boomgaarden u. a. fanden fünf Dimensionen von EU-Einstellungen (European Union Politics 12(2), 2011, 241–266) [A]. Hobolt/de Vries 2016 habe ich nur als Abstract gesehen [A]. Der ESS10-Pilot zeigt nur eine sehr schwache Korrelation zwischen B12 und der Einigungsfrage (Pilotdokumentation S. 35) [V].

**Kein Wert belegt.** Drei Einzelaussagen. Die Kategorien 33, 44, 55 und 65 von `vteurmmb` sind eigene Antworten (leer, ungültig, Nichtwahl, nicht stimmberechtigt) und werden nie als Mitte oder Position zwischen Verbleib und Austritt beschrieben.

### 2.11 Gleichstellungsmaßnahmen, ESS11 E19–E22, und Familienleistungen ESS8 E35

Das ESS11-Template führt E19 (QUOTA), E20 (EQLEAVE), E21 (FIREHAR) und E22 (FINEPAY) als getrennte einfache Konzepte. Zu E21 und E22 erwarten die Entwickler geringere Zustimmung, weil die Maßnahmen als „extreme response“ gesehen werden können ([ESS11-Template](https://europeansocialsurvey.org/sites/default/files/2024-06/r11_gender_module_design_template_final.pdf), S. 11–12, 36–38; SHA-256 `091bea62…5a84f`, identisch mit der Bindung in `docs/konstruktakten.entwurf.md`) [V]. Die Entwicklerpublikation Alexander u. a. 2026 ist im Repository verzeichnet; ich habe sie nicht geöffnet.

**Kein Wert belegt.** Vier Einzelaussagen, jeweils mit dem konkreten Mittel als Kontextmerkmal (gesetzliche Sitzverteilung, gesetzliche Pflicht zu gleich langer Elternzeit im Doppelverdienerszenario, Kündigung, Geldstrafe). Ablehnung eines Mittels belegt keine Ablehnung des Ziels. Das ist meine Ableitung aus dem Wortlaut und der Entwicklererwartung, keine geprüfte Aussage. E35 `wrkprbf` bleibt eine Paketfrage mit „deutlich höhere Steuern für alle“ (ESS8-Template S. 19).

### 2.12 Übersicht

| Gruppe | Skalenabsicht der Entwickler | Selbst gelesene Strukturprüfung | Wert in diesem Projekt | Zulässige Blockaussage |
| --- | --- | --- | --- | --- |
| ESS9 G26–G29 | vier getrennte Prinzipien | vier Faktoren in BSJO-Langfassungen (DE) | nein | Liste nach Prinzip |
| ESS11 B33 | in ESS8 mit zwei anderen Items | – | nein | Einzelaussage |
| ESS8 E6–E8 | ja (AttScope) | Sechs-Item-Vorgänger ESS4 | nein | gleich/unterschiedlich nach Gruppe |
| ESS8 E33–E35 | ausdrücklich kein Faktor | – | nein | keine |
| ESS10 B1–B11 | Modelle, ESS6 Mokken | ESS6-Pool, anderer Itemsatz | nein | höchster/niedrigster Wert, Lesehilfe Modell |
| ESS10 B25 | Trade-off-Format | nicht kombinierbar | nein | Einzelaussage |
| ESS5 D18, D20 | ja (3 Items), Teil formativer Legitimität | – | nein | beide Zahlen, Anlass |
| ESS5 D34–D36 | ja (3 Items) | – | nein | Einzelaussagen, Kontext |
| ESS5 D33 | formativ mit D38 | – | nein | Einzelaussage |
| ESS8 D30–D32 | nicht angegeben | Topline berichtet getrennt | nein | gleich/unterschiedlich nach Instrument |
| ESS10 A54–A56 | ja | Davidov u. a. 2015 (Länder, Runden 1–6) | v1 nein, später prüfbar | gleich/unterschiedlich nach Gruppe |
| ESS8 E15 | einfaches Konzept | nominal (Reeskens/van Oorschot) | nein | Einzelaussage |
| EU A90, B12, B37 | drei Aufgaben | Pilot: sehr schwacher Zusammenhang B12/B37 | nein | drei Einzelaussagen |
| ESS11 E19–E22 | vier einfache Konzepte | – | nein | Einzelaussagen |

---

## 3 Methodenliteratur zur Darstellung persönlicher Ergebnisse (Auftragsteil 2)

### 3.1 Wahlhilfen, Karten und Achsen

Germann/Mendez/Wheatley/Serdült zeigen am Beispiel smartvote 2007, dass a priori festgelegte Kartenachsen die Eindimensionalität verfehlen können. Ohne Eindimensionalität und Reliabilität „the positionings of both users and the political elite cannot be unambiguously interpreted“ (Acta Politica 50, 214–238, S. 216; [Autorenfassung](https://michagermann.github.io/publication/germannmendezwheatleyserduelt2015/GermannMendezWheatleySerduelt2015.pdf)) [V]. Sie berichten, dass Gemenis sowie Louwerse/Otjes den Links-rechts-Achsen des EU Profiler mangelnde Eindimensionalität nachwiesen, weil die Items allein theoretisch zugeordnet waren (S. 217) [V; die zitierten Studien selbst S]. Die smartvote-Karten (zweidimensionale smartmap, achtdimensionale smartspider) waren „invariably determined ex-ante“ (S. 222). Die Ex-ante-smartmap verfehlte die Eindimensionalität (S. 231–232). Ein Item mehreren Skalen zuzuordnen nennen die Autoren „bad practice“ (S. 234, Anm. 8). Ihre Lösung, die „dynamische Skalenvalidierung“, prüft Karten an frühen Nutzerdaten (S. 214).

Rosema/Anderson/Walgrave fassen zusammen: Die Auswahl der Aussagen verändert die Empfehlung, und ein anderer Rechenweg hätte bei der Mehrheit der Nutzenden eine andere beste Übereinstimmung ergeben. Otjes/Louwerse fanden laut dieser Zusammenfassung zwei Mängel: dieselben räumlichen Rahmen in nicht vergleichbaren Kontexten und eine begrenzte Reliabilität der Skalen (Electoral Studies 36, 240–243, S. 240–242, [Repositoriumsfassung](https://ris.utwente.nl/ws/files/6933388/Rosema%20Anderson%20%20Walgrave%202014%20ES.pdf)) [V; Otjes/Louwerse 2014 und Louwerse/Rosema 2014 selbst S]. Walgrave/Nuytemans/Pepermans simulierten 500.000 Aussagenkombinationen; verschiedene Auswahlen begünstigten verschiedene Parteien (West European Politics 32(6), 2009) [A].

Kamoen/Holleman zeigen an 60 kognitiven Interviews und Antworten von 357.858 Nutzenden kommunaler Wahlhilfen: Bei Verständnisproblemen wählen Nutzende oft „neutral“ oder „keine Meinung“. Semantische Probleme führen eher zu „keine Meinung“, pragmatische eher zu „neutral“. Neutrale Antworten gehen in die Übereinstimmungsrechnung ein, „keine Meinung“ nicht; das verzerrt die Empfehlung (Survey Research Methods 11(2), 125–140, S. 125, 128, [OJS](https://ojs.ub.uni-konstanz.de/srm/article/download/6728/6489)) [V]. Baka u. a. fanden in einer kleinen griechischen Studie, dass die Mitte Wissenslücken, Dilemmata und die Zurückweisung von Annahmen der Aussage ausdrückt [A].

**Übertragung.** Dieses Projekt sucht keine Parteiübereinstimmung. Jede Achse oder Karte hätte aber dasselbe Problem: Die 43 Fragen stammen aus fünf Befragungen mit verschiedenen Personen. Eine gemeinsame Struktur lässt sich mit ESS-Daten gar nicht prüfen, und eine Validierung an Webnutzenden würde eine selbstausgewählte Gruppe zur Norm machen. Das ist meine Ableitung.

### 3.2 Reflektive, formative und zusammengesetzte Messung

Bollen/Bauldry unterscheiden Effektindikatoren, kausale Indikatoren und Kompositindikatoren. Laut dem Auszug des Webwerkzeugs ist ein Komposit „an exact linear combination“ ohne Störterm; Kompositindikatoren „do not necessarily have conceptual unity“; die theoretische Rahmung bestimmt die Messform (Psychological Methods 16(3), 2011, [PMC3889475](https://pmc.ncbi.nlm.nih.gov/articles/PMC3889475/)) [W]. Das OECD/JRC-Handbuch verlangt zuerst einen theoretischen Rahmen („What is badly defined is likely to be badly measured“). Es nennt Gewichte „essentially value judgements“ und warnt, dass gleiche Gewichte für Variablen Dimensionen mit mehr Variablen mehr Gewicht geben ([OECD/JRC 2008](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf), S. 13–14 Box 1, S. 22–23, S. 31–32; SHA-256 identisch mit der Bindung in `docs/messformen-v2.entwurf.md`) [V]. Diamantopoulos/Winklhofer beschreiben eigene Gütekriterien für formative Indizes (Journal of Marketing Research 38(2), 2001) [A]. Edwards (2011) und Howell/Breivik/Wilcox (2007) halten formative Messung für problematisch und empfehlen, wo möglich, reflektive Modelle [A].

**Übertragung.** Für einen formativen Themenindex müsste das Projekt einen inhaltlich vollständigen Konstruktrahmen definieren. Die Fragen wurden aber nach Verfügbarkeit, Rechten und Breite gewählt (`docs/empirie-plan-v2.entwurf.md`), nicht als vollständige Indikatoren eines Konstrukts. Die Itemzahl je Thema reicht von drei (Klima) bis zwölf (Demokratieblock); gleiche Gewichtung würde das Gewicht der Themen aus der Auswahl ableiten. Ein reflektiver Wert setzt eine geprüfte Struktur voraus, und die fehlt (Abschnitt 2). Bleibt nur ein Komposit „ohne begriffliche Einheit“. Für eine erklärende Personenbeschreibung ist das keine Grundlage.

### 3.3 Einzelantworten, Kontext und scheinbare Widersprüche

- Zaller/Feldman: Viele Menschen haben zu einer Frage mehrere, teils widerstreitende Überlegungen und antworten mit dem, was gerade präsent ist; kleine Formänderungen verschieben Antworten (AJPS 36(3), 1992) [A].
- Ansolabehere/Rodden/Snyder: Einzelitems tragen viel Messfehler. Erst der Mittelwert vieler Items eines breit definierten Bereichs zeigt stabile Präferenzen (APSR 102(2), 2008) [A]. Für dieses Profil folgt daraus Vorsicht bei Einzelantworten, aber kein Freibrief zur Mittelung: Die Studie setzt viele Items desselben Bereichs voraus, hier sind es eins bis vier je Unterthema aus verschiedenen Befragungen.
- Treier/Hillygus: Einstellungssysteme sind mehrdimensional; viele Menschen sind in einem Bereich liberal und in einem anderen konservativ („cross-pressured“) (POQ 73(4), 2009) [A]. Feldman/Johnston: mindestens zwei Dimensionen (Political Psychology 35(3), 2014) [A].
- Roosma u. a.: Menschen können Ziele und Reichweite des Sozialstaats unterstützen und seine Effizienz kritisieren (S. 235, 240) [V].
- Adriaans/Fourré: Zustimmung zu mehreren Gerechtigkeitsprinzipien zugleich ist erwartbar (S. 2) [V].
- Sturgis/Roberts/Smith: Nachfragen zeigten, dass die Mitte überwiegend als „face-saving don't know“ gewählt wurde (Sociological Methods & Research 43(1), 2014) [A].

### 3.4 Vergleiche mit Bevölkerungsverteilungen und Unsicherheit

- van der Bles u. a. zeigen: Verbale Mengen- und Wahrscheinlichkeitswörter werden sehr unterschiedlich verstanden. „Most“ oder „majority“ werden um 60 % gelesen, wo 90 bis 100 % gemeint sind. Zahlen neben Worten verringern das (Royal Society Open Science 6, 181870, Abschnitt 6.1.3) [V]. Die Autoren unterscheiden direkte Unsicherheit über eine Zahl von indirekter Unsicherheit über die Qualität der Evidenz. Letztere wird meist als Liste von Einschränkungen kommuniziert (Abschnitt 4.1.3). Sie raten, die Größe der Unsicherheit von der Größe des Befunds zu trennen, und halten fest, dass offengelegte Unsicherheit Vertrauen nicht zwingend senkt (Box 5a) [V].
- Trevena u. a. empfehlen für Entscheidungshilfen, stets die Bezugsgruppe (Nenner) zu nennen, ein durchgehend gleiches Format zu nutzen und wechselnde Nenner zu vermeiden (BMC Med Inform Decis Mak 13(Suppl 2), S7, S. 1, 4) [V]. Die Übertragung aus der Medizin ist meine.
- Rothschild/Malhotra: In einem US-Experiment veränderten Informationen über die Unterstützung von Politikmaßnahmen individuelle Einstellungen, je nach Thema unterschiedlich stark (Research & Politics 1(2), 2014) [A].

---

## 4 Empfehlung: das belegte Antwortprofil (Auftragsteil 3)

### 4.1 Entscheidung

Die Evidenz trägt für diesen Fragenbestand ein **regelbasiertes, beschreibendes Antwortprofil ohne Rechenwerte**. Es erklärt, was die Antworten wörtlich sagen. Es ordnet sie nach Thema, beschreibt Muster innerhalb gleich formatierter Originalblöcke und stellt vorab begründete Querbezüge nebeneinander. Es misst keine Eigenschaft der Person.

Das entspricht den vorhandenen Projektentscheidungen (`docs/empirie-plan-v2.entwurf.md`, Abschnitt „Produkt und Messmodell“; `docs/messformen-v2.entwurf.md`). Die Literatur aus Abschnitt 2 und 3 liefert dafür jetzt konkrete Gründe je Fragengruppe.

### 4.2 Aufbau

**Stufe 1: Einzelaussage.** Jede beantwortete Frage erhält eine Aussage nach Abschnitt 4.3. Daneben stehen Wortlaut, gewählte Originalkategorie, Studie, Feldzeit und Kontextmerkmal.

**Stufe 2: Blockmuster.** Für Originalblöcke mit identischem Antwortformat und derselben Einleitung beschreibt das Profil, ob die Antworten gleich sind oder sich unterscheiden und in welcher Richtung. Zulässige Blöcke: G26–G29 (ESS9), E6–E8 (ESS8), B1–B11 (ESS10), D18/D20 (ESS5), D34–D36 (ESS5), D30–D32 (ESS8), A54–A56 (ESS10), E19–E22 (ESS11). Für E33–E35 gibt es keine Blockaussage, weil die drei Fragen verschiedene Tauschgeschäfte enthalten und die Entwickler keinen gemeinsamen Faktor annehmen.

**Stufe 3: Querbezug.** Eine vorab festgelegte, begründete Zusammenstellung von Fragen aus verschiedenen Blöcken oder Studien mit gemeinsamem Inhaltselement. Querbezüge zeigen die Antworten nebeneinander und erklären per Kontextsatz, worin sich die Fragen unterscheiden. Sie bewerten nichts und zählen nichts zusammen.

Vorschlag für eine erste Liste, jeweils vor Nutzung von einer frischen Rolle auf Inhalt und Fairness zu prüfen:

| Querbezug | Fragen | Gemeinsames Element | Unterschied im Kontextsatz |
| --- | --- | --- | --- |
| Einkommensunterschiede | `sofrdst` (ESS9), `gincdif` (ESS11), `grdfinc` (ESS10) | Verringerung von Einkommensunterschieden | Merkmal einer gerechten Gesellschaft; Auftrag an den Staat; Wichtigkeit für Demokratie im Allgemeinen |
| Absicherung bei Armut und Bedarf | `sofrpr` (ESS9), `gvctzpv` (ESS10), `gvslvol`, `gvslvue` (ESS8) | Absicherung Bedürftiger | Gerechtigkeitsmerkmal ohne Gegenleistung; Demokratiebestandteil; staatliche Verantwortung je Gruppe |
| Volksentscheid und Mehrheitswille | `votedir`, `viepol`, `wpestop`, `scchpldm` (alle ESS10) | Gewicht der Bevölkerungsmehrheit | drei Wichtigkeitsfragen; eine Wahl zwischen zwei Regierungsreaktionen |
| Recht, Gerichte, Polizei | `cttresa` (ESS10), `dbctvrd`, `lwstrob`, `rgbrklw`, `bplcdc`, `dpcstrb` (ESS5) | Bindung an Recht und Behörden | Wichtigkeit gleicher Behandlung; Zustimmung zu Regeln; eigene Pflicht gegenüber Polizei |
| Vereinbarkeit von Arbeit und Familie | `gvcldcr`, `wrkprbf` (ESS8), `eqparlv` (ESS11) | Betreuung und Erwerbsarbeit von Eltern | Verantwortung; Leistungen trotz höherer Steuern; gesetzliche Pflicht zu gleich langer Elternzeit |
| Europäische Union | `vteurmmb`, `keydec` (ESS10), `euftf` (ESS11) | EU | hypothetische Abstimmung; Demokratieprinzip; Richtung der Einigung |

Querbezüge über Migration und Minderheitenrechte oder über Gleichheitsprinzip und Gleichstellungsmaßnahmen empfehle ich nicht. Die Gegenstände sind verschieden, und die Verbindung würde eine Deutung nahelegen, die keine Frage stellt.

### 4.3 Regeln: von der Antwort zur Aussage

Grundsätze für alle Fragen:

1. Die Aussage nutzt den Originalwortlaut der gewählten Kategorie und den Gegenstand der Frage. Sie ist eine reine Funktion der Antwortcodes und einer vorab geprüften Texttabelle. Dieselbe Eingabe ergibt denselben Text.
2. Richtung kommt aus dem Kategorienlabel, nie aus der Codezahl. Code 1 bedeutet bei `bnlwinc` „Sehr dagegen“ und bei `inctxff` „Sehr dafür“.
3. Keine Aussage über Eigenschaften, Gründe, Gefühle oder Stabilität der Person. Formulierungen beschreiben „die Antwort“ oder „die Antworten“, ohne direkte Anrede (Handbuch Kapitel 7.1).
4. Jede Frage hat ein festes **Kontextmerkmal** aus ihrem Wortlaut. Beispiele: „Wichtigkeit für die Demokratie im Allgemeinen“ (B1–B12); „Vergleich mit Strafen zur Feldzeit 2010/11“ (D33); „bei fester Geldsumme, weniger Arbeitslosenunterstützung“ (E34); „auch wenn das deutlich höhere Steuern für alle bedeuten würde“ (E35); „gesetzliche Pflicht für beide Eltern, Doppelverdienerszenario“ (E20); „Kündigung als Folge“ (E21); „Geldstrafe für Unternehmen“ (E22); „hypothetische Volksabstimmung morgen“ (A90); „Merkmal einer gerechten Gesellschaft, kein Staatsauftrag“ (G26–G29); „Verantwortung des Staates, keine Ausgabenhöhe“ (E6–E8); „eigene Pflicht trotz Widerspruch bzw. missbilligter Behandlung“ (D18/D20).

Regeln je Antworttyp:

| Antworttyp | Aussageform | Beispiel ohne Anrede |
| --- | --- | --- |
| Zustimmung oder Unterstützung, fünf Stufen | Kategorien 1–2 bzw. 4–5 als Zustimmung/Ablehnung oder dafür/dagegen; das gewählte Label steht in Klammern; 3 nach Abschnitt 4.4 | „Ablehnung der Aussage ‚Eine Gesellschaft ist gerecht, wenn hart arbeitende Menschen mehr verdienen als andere‘ (gewählt: ‚Lehne ab‘).“ |
| Unterstützung, vier Stufen | 1–2 dagegen, 3–4 dafür; Hinweis, dass keine Mitte angeboten war | „Dafür, staatliche Sozialleistungen nur noch für die niedrigsten Einkommen zu gewähren, mit der genannten Folge für mittlere und hohe Einkommen (gewählt: ‚Dafür‘).“ |
| Zulassung, vier Stufen | Label wörtlich, keine Zusammenfassung zu „eher offen“ | „Gruppe aus ärmeren Ländern außerhalb Europas: ‚Ein paar wenigen erlauben‘.“ |
| 0–10 unipolar | Zahl mit beiden Ankern; Ankertext nur bei 0 oder 10; keine verbalen Zwischenstufen | „Staatliche Verantwortung für einen angemessenen Lebensstandard von Arbeitslosen: 4 (0 = überhaupt nicht, 10 = voll und ganz).“ |
| 0–10 bipolar (`euftf`) | Zahl mit beiden Polen; unter 5 „näher an ‚Einigung ist schon zu weit gegangen‘“, über 5 „näher an ‚Einigung sollte weitergehen‘“, 5 als „Wert 5 zwischen beiden Endpunkten“ | „Europäische Einigung: 7, näher an ‚Einigung sollte weitergehen‘.“ |
| nominal | gewählte Alternative als Satz | „Gleiche Rechte auf Sozialleistungen für Zugewanderte erst, nachdem sie mindestens ein Jahr gearbeitet und Steuern bezahlt haben.“ |

Zur Begründung der Klassen bei Fünferskalen: Adriaans/Fourré fanden die Richtung verlässlicher als den Grad (S. 6–7). Für 0–10-Skalen habe ich keine vergleichbare Untersuchung gelesen. Ich empfehle dort deshalb keine Klassen. Die ESS10-Entwickler dichotomisierten Wichtigkeit als 10 gegen 0–9 (Pilotdokumentation S. 6). Das ist eine Auswertungskonvention für Bevölkerungsanalysen, keine geprüfte Bedeutung für Einzelpersonen, und sollte nicht in Personentexte übernommen werden.

### 4.4 Fehlende Antworten, „Weiß nicht“, Mitte und Nichtpositionskategorien

- **Übersprungen, „Weiß nicht“, keine Angabe.** Keine Aussage, keine Ersatzantwort, kein Vergleich. Die Frage erscheint in einer Liste „ohne inhaltliche Antwort“. Der Grund wird getrennt geführt, wenn die Website ihn erfasst. Ein historischer Vergleich entfällt. In den ESS-Interviewfassungen stehen „(Refusal)“ und „(Don't know)“ in Klammern, also als nicht vorgelesene Codes (zum Beispiel ESS9-Template S. 34); in der deutschen ESS10-Papierfassung druckt A54 nur die Kategorien 1–4 (`mappingNotes` im Fragenentwurf). Ein sichtbares Website-Feld „Weiß nicht“ ist damit nicht vergleichbar.
- **Mittlere Kategorie bei Fünferskalen** („Weder noch“, „Weder dafür noch dagegen“). Wörtlich wiedergeben: „weder Zustimmung noch Ablehnung gewählt“. Einmal je Profil erklären: Die Kategorie kann Unentschiedenheit, fehlende Meinung oder Zurückweisung der Frageannahme ausdrücken; welcher Grund vorliegt, erfasst die Frage nicht (Sturgis u. a. [A]; Baka u. a. [A]; Kamoen/Holleman S. 125, 128 [V]). Nie „neutral“, „gemäßigt“, „ausgewogen“ oder „Mitte“ als Beschreibung der Person. Die Mitte zählt in Blockmustern weder als Zustimmung noch als Ablehnung.
- **Wert 5 auf 0–10.** Eine Zahl wie jede andere, keine Mitte im Sinne einer Position. Bei bipolarem `euftf` nach der Regel in 4.3.
- **Nichtpositionskategorien** (`vteurmmb` 33, 44, 55, 65): eigene Aussage, zum Beispiel „Antwort: würde nicht wählen“. Nie zwischen Verbleib und Austritt einordnen.
- **Teilweise beantwortete Blöcke und Querbezüge.** Blockmuster nur aus beantworteten Fragen. Formulierungen mit „alle“ lauten „alle beantworteten“. Ein Querbezug erscheint erst ab zwei beantworteten Fragen; die fehlenden werden genannt.
- **Abdeckung.** Die Zahl beantworteter Fragen je Thema darf als Abdeckungsangabe erscheinen („9 von 12 Fragen beantwortet“). Sie ist kein Wert und darf nicht als Balken neben Themen stehen, der wie eine Position aussieht.

### 4.5 Zusammenhänge innerhalb eines Themas ohne Gesamtwert

Erlaubte Musteraussagen, jeweils mit Liste der beteiligten Antworten:

- **Gleich oder unterschiedlich.** „Die drei Antworten zur staatlichen Verantwortung sind gleich (jeweils 7).“ oder „… unterscheiden sich: Alter 10, Arbeitslose 4, Kinderbetreuung 8.“
- **Ordinaler Vergleich gleich formatierter Antworten.** „Für Zugewanderte derselben Volksgruppe wie die Mehrheit wurde mehr Zuwanderung erlaubt als für Zugewanderte aus ärmeren Ländern außerhalb Europas.“
- **Höchster und niedrigster Wert im Block** (B1–B11): beide Fragen und Zahlen nennen; bei Gleichstand alle gleichrangigen nennen.
- **Zusammentreffen mehrerer Zustimmungen** (G26–G29): „Zustimmung zu Gleichheit und zu Leistung; beide Prinzipien schließen einander nicht aus.“ Mit Quellenverweis.
- **Prinzip und Maßnahme** (über `responseContentType` `principle`/`measure` im Entwurf): Wenn eine Prinzipienfrage und eine Maßnahmenfrage desselben Querbezugs verschieden beantwortet wurden, nennt der Kontextsatz das zusätzliche Element der Maßnahme (Kosten, Zwang, Zielgruppe). Er sagt nicht, welches Element den Unterschied verursacht hat.

Nicht erlaubt: Mittelwerte, Summen, Anteile eigener Zustimmungen („3 von 4 Prinzipien“), Mehrheitsregeln, Typen, Etiketten für das Thema, Farben oder Balken, die eine Gesamtrichtung suggerieren.

### 4.6 Beleggrundlage sichtbar machen

Jede Aussage auf Stufe 2 oder 3 trägt eine Belegzeile:

- **Belegart:** Einzelfrage, Fragenblock oder Querbezug.
- **Fragen:** Kennung, Kurztitel, Studie, Feldzeit, Modus (zum Beispiel „ESS10, Selbstausfüller Papier/Web, Okt. 2021–Jan. 2022“).
- **Gewählte Antworten:** Originallabels oder Zahlen.
- **Kontextmerkmale:** je Frage.
- **Grund der Zusammenstellung:** „Originalblock laut ESS-Moduldokumentation“ mit Fundstelle, oder „Zusammenstellung durch das Projekt; keine geprüfte gemeinsame Struktur“.

So bleibt für Lesende sichtbar, dass ein Querbezug eine redaktionelle Ordnung ist und keine Messung.

### 4.7 Historische Vergleiche

- Nur itemweise und nur für inhaltliche Antworten. Format: „In der ESS-Befragung in Deutschland [Feldzeit] wählten [x] % der Befragten mit inhaltlicher Antwort dieselbe Kategorie (gewichtete Schätzung).“ Dazu die vollständige Verteilung aller Kategorien, damit kein Mehrheits- oder Außenseiterbild entsteht.
- Feste Begleitangaben: Studie, Ausgabe, Feldzeit, Population, Modus, Nenner nur inhaltliche Antworten. Gleiches Zahlenformat im ganzen Profil (Trevena u. a. S. 1, 4).
- Keine Mengenwörter ohne Zahl (van der Bles u. a. 6.1.3). Kein „typisch“, „ungewöhnlich“, „Mehrheitsmeinung“.
- Kein Vergleich über mehrere Fragen hinweg, auch nicht innerhalb eines Themas: Die Referenzen stammen von verschiedenen Personen und Jahren, und gemeinsame Antwortmuster sind in den Daten nicht beobachtbar. Ausnahme wäre nur ein später eigens geplanter Vergleich innerhalb einer einzigen Studie.
- Unsicherheit: ein fester Satz, dass Anteile Schätzungen aus einer Stichprobe sind und kein Stichprobenfehler ausgewiesen wird (entspricht `docs/empirie-plan-v2.entwurf.md`). Kein Intervall ohne gebundene Berechnung, nie „±0“.
- Zeitbezug sichtbar: Die Verteilungen sind keine heutige Norm für Websitebesuchende.
- Platzierung als offene Entscheidung für Steven: Verteilungen nach jeder Antwort können spätere Antworten beeinflussen (Rothschild/Malhotra [A], US-Experiment, Übertragung ungeprüft). Die ESS-Befragten sahen keine Verteilungen. Vorschlag: Vergleiche erst im Abschlussprofil oder nach Abschluss eines Themas zeigen.

### 4.8 Nicht zulässig

- Gesamtwert, Themenwert, Index, Mittelwert, Summe oder Faktorwert über Fragen, auch innerhalb eines Themas.
- Achsen, Pole, Karten, Spinnennetz- oder Radardiagramme, Positionsbalken, Prozentpositionen, Perzentile, Ränge gegenüber der Bevölkerung.
- Ideologie- und Lagerbezeichnungen für Personen oder Antwortmuster: links, rechts, liberal, konservativ, progressiv, libertär, autoritär, populistisch, etatistisch, marktliberal, euroskeptisch, nationalistisch, feministisch und ähnliche. Auch Konzeptnamen aus Moduldokumenten wie „Wohlfahrtschauvinismus“, „punitiv“ oder „Populismus“ nicht als Personenbeschreibung.
- Motive, Gefühle, Persönlichkeit, moralische Wertungen („solidarisch“, „streng“, „tolerant“, „demokratisch“, „rechtstreu“).
- „Widerspruch“, „inkonsistent“, „ambivalent“, „unentschlossen“, „neutral“, „gemäßigt“ als Beschreibung der Person.
- Imputation fehlender Antworten, Mitte als Ersatz, „Weiß nicht“ als Position.
- Verrechnung oder gemeinsames Referenzprofil aus verschiedenen Studien; Ähnlichkeitsmaße zur Bevölkerung oder zu Wählergruppen; „nächste Partei“.
- Richtung aus Codezahlen; doppelte Zählung von `gvcldcr` oder `keydec` in Mengenangaben.
- Gewichtung von Themen nach Fragenzahl.
- Aussagen über Stabilität oder Wahrheit einer Einstellung; Urteile, ob eine Antwort richtig ist.
- Persönliche Messunsicherheit oder Intervalle ohne gebundene Berechnung.
- Bezeichnungen wie „validiert“ oder „wissenschaftlich geprüft“ für das Profil.

### 4.9 Später mögliche Erweiterungen, jeweils nur mit eigenem Plan

- **A54–A56 als Zulassungswert.** Voraussetzungen: deutsche ESS10-SC-Daten, ordinales Messmodell, Prüfung der Übertragbarkeit auf Webnutzung, getrennte Darstellung neben den drei Einzelantworten, Freigabe durch Steven. Auch dann bliebe die Gruppenunterscheidung inhaltlich wichtig (ESS7-Topline S. 5).
- **E6–E8 und D34–D36.** Skalenabsicht der Entwickler liegt vor; eine Strukturprüfung für Deutschland müsste zuerst gelesen oder durchgeführt werden.
- **Typologie E33–E35.** Die Entwickler nennen sie eine offene empirische Frage; ohne eigene Analyse keine Typzuordnung.

---

## 5 Technische Prüffälle (Auftragsteil 4)

Synthetische Eingaben, keine empirischen Personen. Erwartung „keine Aussage X“ bedeutet: der Text darf X nicht enthalten.

| ID | Eingabe | Erwartung | Darf nicht |
| --- | --- | --- | --- |
| T01 | Alle 43 Fragen übersprungen | Hinweis „keine inhaltlichen Antworten“, Liste aller Fragen, keine Block- oder Querbezugsaussage, kein Vergleich | Profiltext, Themenaussage, Prozentangabe |
| T02 | Nur Mitte: alle Fünferskalen 3, alle 0–10-Skalen 5, Viererskalen und nominale übersprungen | Wörtliche Mitte-Aussagen, Erklärtext zur Mitte genau einmal, Zahlen „5“ ohne Deutung | „neutral“, „gemäßigt“, „Mitte“ als Personenbeschreibung, Richtung |
| T03 | Alle Fragen „Weiß nicht“ bzw. „keine Angabe“, soweit angeboten | Wie T01, Grund getrennt gelistet | Vergleich mit ESS-Missing-Anteilen |
| T04 | Alle Codes = 1 (alle Fragen, auch Viererskalen und nominal, soweit Code 1 gültig) | Gegensätzliche Richtungen je nach Frage korrekt: `bnlwinc` „sehr dagegen“, `inctxff` „sehr dafür“, `imsmetn` „vielen erlauben“ | Einheitliche Richtung über Codes, „Widerspruch“ |
| T05 | Alle niedrigsten Kategorien bzw. 0 | Anker-Text „überhaupt nicht …“ bei 0; `euftf` 0 „Einigung ist schon zu weit gegangen“ | Gegenhaltung aus unipolarer 0 |
| T06 | Alle höchsten Kategorien bzw. 10 | Demokratieblock: „alle beantworteten Aspekte mit 10“ ohne Rangfolge | Zählung von Zehnern als Wert |
| T07 | G26 = 1, G27 = 1, G28 = 5, G29 = 5 | Zustimmung Gleichheit und Leistung, Ablehnung Bedarf und Herkunftsprivileg; Satz, dass Prinzipien einander nicht ausschließen | „widersprüchlich“, „dominantes Prinzip“, Typ |
| T08 | G26 = 1, G29 = 1 (übrige übersprungen) | Beide Zustimmungen, kein Kommentar zur Kombination außer dem Standardsatz | Wertung, Motiv |
| T09 | E6 = 10, E7 = 0, E8 = 5 | Blockaussage „unterscheiden sich“ mit drei Zahlen | „sozialstaatsnah“, Mittelwert 5 |
| T10 | E6 = E7 = E8 = 7 | „gleich (jeweils 7)“ | verbale Stufe „eher hoch“ |
| T11 | E33 = 4, E34 = 1, E35 = 4 | Drei Einzelaussagen mit Kontextmerkmalen | Blockmuster, Typ |
| T12 | G26 = 1, B33 = 5, B9 = 8 | Querbezug Einkommensunterschiede mit drei Antworten und Kontextsatz zu den drei Aufgaben | „Widerspruch“, verrechnete Richtung |
| T13 | B5 = B10 = B11 = 10, B4 = B6 = 2 | Höchste und niedrigste Werte genannt, Lesehilfe Modellzuordnung | „populistisch“, „illiberal“, Modellwerte |
| T14 | B25 = 1, B11 = 0 | Zwei Einzelaussagen, Querbezug mit Formathinweis | Rechnung über beide Formate |
| T15 | D18 = 10, D20 = 0 | Zwei Zahlen, Kontext Widerspruch gegenüber Behandlung | „Legitimität“, „autoritätsgläubig“ |
| T16 | D33 = 1, D35 = 1, D36 = 1 | Drei Aussagen; D33 mit Zeitkontext 2010/11; D35/D36 mit Kontext „allgemeine Regel/Ausnahme manchmal“ | „punitiv“, „autoritär“, „Widerspruch“ |
| T17 | A90 = 55, B37 = 10, B12 = 10 | „würde nicht wählen“; zwei Zahlen; Querbezug EU ohne Wert | Einordnung zwischen Verbleib und Austritt, EU-Wert |
| T18 | A90 = 65 | „nicht stimmberechtigt“ als eigene Antwort | „neutral“, Austausch durch Missing |
| T19 | A54 = 1, A55 = 4, A56 = 4 | Blockaussage mit ordinaler Richtung je Gruppe | Gründe, Gruppeneinstellung, Summenwert |
| T20 | A54 = A55 = A56 = 2 | „gleiche Antwort für alle drei Gruppen“ | Zulassungswert |
| T21 | E15 = 5 und separat E15 = 1 | Satz zur gewählten Bedingung | Rangposition „streng/großzügig“, Modul-Etikett |
| T22 | D30 = 5, D31 = 1, D32 = 3 | Instrumentweise Aussagen, Blockaussage „unterscheiden sich nach Instrument“ | Klimawert |
| T23 | E19 = 1, E22 = 5 | Zwei Einzelaussagen, Kontext Mittel | „gegen Gleichstellung“ |
| T24 | Nur das Thema Klima beantwortet | Profil nur für Klima, Abdeckungsangabe, keine Querbezüge | Aussagen zu anderen Themen |
| T25 | Querbezug mit nur einer beantworteten Frage | Kein Querbezug, Einzelaussage bleibt | „alle“-Formulierung |
| T26 | Ungültige Codes: 6 auf Fünferskala, 11 auf 0–10, 9 bei A54, 3 bei B25 | Fehler, keine Aussage | stille Umkodierung |
| T27 | Dieselbe Eingabe zweimal, andere Beantwortungsreihenfolge | Identischer Text | reihenfolgeabhängige Aussagen |
| T28 | Thema nur mit Mitte plus eine gerichtete Antwort | Aussage nur zur gerichteten Antwort, Mitte wörtlich | Themenrichtung aus einer Antwort |
| T29 | Alle Zustimmungsfragen „stimme stark zu“, alle übrigen übersprungen | Labels mit „stark“ wörtlich, keine verstärkenden Zusatzsätze | „Zustimmungstendenz“, Hinweis auf Antwortstil |
| T30 | Vergleichsanzeige bei Referenzstatus `withheld_base_or_cell_count` oder `no_valid_answers` | Kein Prozentvergleich, Hinweis auf fehlende Referenz, Aussage zur eigenen Antwort bleibt | Ersatzvergleich, zusammengelegte Kategorien |

---

## 6 Nebenbefunde zum vorhandenen Entwurf

1. **Statische Texte unterstellen Zustimmung.** In `web/src/app/policy-draft/item-meanings.ts` lauten die Erläuterungen zu `sofrdst`, `gincdif`, `dbctvrd`, `lwstrob`, `rgbrklw` „Die Auswahl beschreibt die Zustimmung …“, zu `inctxff`, `sbsrnen`, `banhhap`, `eqparep`, `eqparlv`, `freinsw`, `fineqpy`, `wrkprbf` „… die Unterstützung …“. Bei Ablehnung ist das sachlich falsch. Bei `sofrwrk`, `sofrpr`, `sofrprv` steht korrekt „Zustimmung oder Ablehnung“. Abhilfe: antwortabhängige Aussage nach Abschnitt 4.3. Ich habe die Datei nicht geändert.
2. **D33 in falscher Gruppe.** `ESS5e03_6:hrshsnta` trägt `groupId: law_obligation` zusammen mit D34–D36. Im ESS5-Design gehört D33 zu „Punitive attitudes“ (Template S. 4, 31–32), D34–D36 zu „Obligation to obey the law and court decisions“ (S. 25–26). Für Ablauf und Matrixkontext ist die Gruppe unschädlich. Für Blockaussagen darf D33 nicht mit D34–D36 zusammengefasst werden.
3. **Gegenläufige Kodierrichtung.** Viererskalen E33–E35 (`1 = Sehr dagegen`) gegenüber Fünferskalen D30–D32 und E19–E22 (`1 = Sehr dafür`). Jede Implementierung braucht eine labelbasierte Richtungstabelle (Prüffall T04).
4. **Mehrfachzuordnung.** `keydec` (Demokratieblock, primär EU) und `gvcldcr` (primär Sozialstaat, sekundär Familie) dürfen in mehreren Abschnitten erscheinen, aber in keiner Mengen- oder Abdeckungsangabe doppelt zählen. Germann u. a. nennen Mehrfachzuordnung zu Skalen „bad practice“ (S. 234, Anm. 8); für ein rein beschreibendes Profil ist doppelte Anzeige mit Verweis vertretbar.
5. **Verteilung nach jeder Antwort.** Siehe 4.7. Die Entscheidung betrifft Produktumfang und Gestaltung und gehört zu Steven.

---

## 7 Grenzen dieser Prüfung

- Keine systematische Literaturübersicht. Gezielte Suche nach Originaldokumenten der ESS-Module und einigen Schlüsselstudien in etwa einer halben Stunde.
- Mehrere zentrale Werke kenne ich nur als Abstract oder über Sekundärquellen: Hülle/Liebig/May 2018 (Zeitschriftenfassung), Gemenis 2013, Otjes/Louwerse 2014, Louwerse/Rosema 2014, Germann/Mendez 2016, Walgrave u. a. 2009, Diamantopoulos/Winklhofer 2001, Sturgis u. a. 2014, Zaller/Feldman 1992, Ansolabehere u. a. 2008, Treier/Hillygus 2009, Jackson u. a. 2011 und 2012, Boomgaarden u. a. 2011, Ferrín/Kriesi 2016, Kriesi/Saris/Moncagatta 2016, Mewes/Mau 2012. Aussagen dazu reichen nicht über Abstract oder Sekundärzitat hinaus.
- Bollen/Bauldry 2011 nur über den Auszug des Webwerkzeugs; die Zitate dort habe ich nicht gegen das PDF geprüft.
- Keine deutsche Strukturprüfung für E6–E8, D18–D20 oder D34–D36 gefunden. Das heißt nicht, dass keine existiert.
- Die Wirkung von Profiltexten auf Laien ist ungeprüft. Die Empfehlungen zu Formulierungen und Vergleichsanzeige brauchen einen Verständnistest mit Menschen.
- Ich habe keine Antwortdaten gesehen und keine Verteilungen gelesen. Ob die vorgeschlagenen Blockaussagen in der Praxis oft „unterscheiden sich“ ergeben, ist unbekannt.
- Literaturplausibilität ist keine Validierung, und meine Übereinstimmung mit früheren Codex-Entscheidungen ist kein Neutralitätsnachweis.

---

## 8 Tatsächlich geöffnete Quellen

Zugriff am 2026-10-03 zwischen etwa 19:05 und 19:25 UTC. Lokale Kopien unter `/tmp/r4/` (außerhalb des Repositorys, nicht veröffentlicht).

Repository (gelesen): `AGENTS.md`; `docs/project.md`; `docs/empirie-plan-v2.entwurf.md`; `docs/messformen-v2.entwurf.md`; `docs/abdeckung-v2.md`; `docs/konstruktakten.entwurf.md`; `docs/deutschland-literatur.entwurf.md`; `docs/handbuch.md` (Kapitel 7, Ausschnitte); `data/politikprofil-v2.fragen.entwurf.json`; `data/theorie-quellen.json` und `data/methoden-quellen.json` (nur Titel/DOIs); `web/src/app/policy-draft/item-meanings.ts`; Dateiliste `web/src/app/policy-draft/`; `reports/claude/auftraege/00-gemeinsame-regeln.md`, `R4-profilform.md`, `R4-profilform.vollstaendig.md`.

Volltext oder Abschnitte selbst gelesen [V]:

- ESS9 Template Justice and Fairness: https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS9_justice_final_module_template.pdf
- Liebig/Hülle/May, SOEPpapers 831: https://www.diw.de/documents/publikationen/73/diw_01.c.530548.de/diw_sp0831.pdf
- Adriaans/Fourré 2022: https://miss.psychopen.eu/index.php/miss/article/download/11131/9701
- ESS8 Template Welfare: https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS8_welfare_final_module_template.pdf
- Roosma/Gelissen/van Oorschot 2013: https://lirias.kuleuven.be/retrieve/fb851f72-dc05-4eb3-92f6-da6e98aad99f
- ESS10 Demokratie-Antrag: https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS10_democracy_proposal.pdf
- ESS10 Pretest-/Pilotdokumentation: https://www.europeansocialsurvey.org/sites/default/files/2024-02/ESS10_Democracy_Pretest_Pilot.pdf
- ESS Topline Issue 4 (Ferrín/Kriesi): https://www.europeansocialsurvey.org/sites/default/files/2023-06/TL4-Democracy-English.pdf
- ESS5 Template Trust in Police & Courts: https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS5_final_trust_in_police_courts_.pdf
- ESS Topline Issue 1 (Trust in Justice): https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS5_toplines_issue_1_trust_in_justice.pdf
- Jackson 2018, Autorenfassung: https://researchonline.lse.ac.uk/id/eprint/87538/1/Jackson_Norms%20Normativity_Author.pdf
- Hough/Bradford/Jackson/Roberts 2013: https://eprints.lse.ac.uk/50440/1/Jackson_Attitudes_sentencing_trust_2013.pdf
- ESS8 Template Climate: https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS8_climate_final_module_template.pdf
- ESS Topline Issue 9 (Klima): https://www.europeansocialsurvey.org/sites/default/files/2023-06/TL9_Climate-Change-English.pdf
- Drews/van den Bergh, Repositoriumsfassung: https://riuma.uma.es/bitstreams/f5a93e49-4abc-4d61-a6f4-3e37cefe9ef6/download
- Davidov u. a. 2015, Autorenfassung: https://lirias.kuleuven.be/retrieve/698f3cef-16ad-44f8-92d3-4ec4fa2453e7
- ESS Topline Issue 7 (Zuwanderung): https://www.europeansocialsurvey.org/sites/default/files/2023-06/TL7-Immigration-English.pdf
- Reeskens/van Oorschot 2012: https://lirias.kuleuven.be/retrieve/187cf8c2-dd5e-481d-a272-fbbc606b4040
- ESS11 Gender Template: https://europeansocialsurvey.org/sites/default/files/2024-06/r11_gender_module_design_template_final.pdf
- Germann u. a. 2015, Autorenfassung: https://michagermann.github.io/publication/germannmendezwheatleyserduelt2015/GermannMendezWheatleySerduelt2015.pdf
- Rosema/Anderson/Walgrave 2014: https://ris.utwente.nl/ws/files/6933388/Rosema%20Anderson%20%20Walgrave%202014%20ES.pdf
- Kamoen/Holleman 2017: https://ojs.ub.uni-konstanz.de/srm/article/download/6728/6489
- OECD/JRC 2008: https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf
- van der Bles u. a. 2019, Volltext-XML über Europe PMC: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6549952/fullTextXML
- Trevena u. a. 2013: https://kops.uni-konstanz.de/server/api/core/bitstreams/5dad1c68-cebc-40ff-9113-0d0b64e2dc14/content

Über das Webwerkzeug [W]: Bollen/Bauldry 2011, https://pmc.ncbi.nlm.nih.gov/articles/PMC3889475/

Nur Abstract oder Metadaten über die OpenAlex-API [A]: Walgrave/Nuytemans/Pepermans 2009 (10.1080/01402380903230637); Diamantopoulos/Winklhofer 2001 (10.1509/jmkr.38.2.269.18845); Sturgis/Roberts/Smith 2014 (10.1177/0049124112452527); Zaller/Feldman 1992 (10.2307/2111583); Ansolabehere/Rodden/Snyder 2008 (10.1017/S0003055408080210); Treier/Hillygus 2009 (10.1093/poq/nfp067); Feldman/Johnston 2014 (10.1111/pops.12055); Baka/Figgou/Triga 2012 (10.1504/ijeg.2012.051306); Jackson u. a. 2011 (10.1177/1477370811411458); Jackson u. a. 2012 (10.1093/bjc/azs032); Boomgaarden u. a. 2011 (10.1177/1465116510395411); Hobolt/de Vries 2016 (10.1146/annurev-polisci-042214-044157); Rothschild/Malhotra 2014 (10.1177/2053168014547667); Edwards 2011 (10.1177/1094428110378369); Howell/Breivik/Wilcox 2007 (10.1037/1082-989X.12.2.205). Für Otjes/Louwerse 2014, Louwerse/Rosema 2014 und Hülle u. a. 2018 lieferte OpenAlex nur Metadaten ohne Abstract.

Geladen, aber nicht inhaltlich ausgewertet: ESS9 Topline Issue 10, ESS4 Welfare Template, ESS6 Demokratie-Template, ESS8 Welfare-Antrag, Gemenis/van Ham (Preprint).

Gescheitert (Sperr- oder Abfrageseite, Status 403 oder Weiterleitung zur Anmeldung): Springer-PDFs (Hülle u. a. 2018, Germann u. a. 2015, Gemenis 2013), OUP (IJPOR-BSJO-Artikel), ScienceDirect (Otjes/Louwerse), RUG- und Utwente-Dateien, Sage (Rothschild/Malhotra), Royal Society, Annual Reviews, Europe-PMC-PDF-Render. Keine Anmeldung, kein Zustimmungsdialog.

## 9 Ausgeführte Befehle (Kurzform)

- `git log`, `ls`, `wc`, `cat`, `sed` und Python-Ausgaben auf die oben genannten Repositorydateien; Python-Auszug aller 43 Items mit Wortlaut, Kategorien und Missing-Codes aus dem Fragen-JSON.
- `curl` auf die oben genannten öffentlichen URLs nach `/tmp/r4/`; `curl` auf `api.openalex.org` für Metadaten, Abstracts und offene Fundorte; `curl` auf Europe PMC REST.
- `pdftotext`, `pdfinfo`, zwei kleine Python-Hilfen (`pg.py` für Mustersuche je PDF-Seite, `page.py` für Seitenauszüge), `sha256sum`.
- WebSearch für Fundorte; WebFetch für Bollen/Bauldry (erfolgreich), Springer und ScienceDirect (gescheitert).
- Keine Änderung an Repositorydateien außer diesem Bericht. Keine Commits.

## 10 Modell

Claude Opus 5.5 mit 1M-Kontext, Modellkennung `claude-opus-5-5[1m]`, laut Laufzeitangabe im Systemkontext dieser Sitzung.
