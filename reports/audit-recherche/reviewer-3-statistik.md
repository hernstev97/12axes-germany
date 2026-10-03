# KI-Erstprüfung 3: Messmethodik und Statistik

Die gesicherte Forschungsfassung gibt noch keine statistische Freigabe vor. Das ist sachgerecht. Ich fand keinen bereits berechneten Score, keine empirisch belegte Dimension und keine bestandene psychometrische Prüfung, deren Gültigkeit hier zu beurteilen wäre. Die zentralen methodischen Quellenbefunde sind in ihrer ausdrücklich begrenzten Reichweite tragfähig. Vier spätere Anforderungen brauchen vor der jeweils abhängigen Freigabe eine konkrete Entscheidung. Sie sind keine gescheiterten ESS-Analysen.

## Identität und Prüfgrenze

- Prüfer: Codex-Subagent `/root/reviewer_3_statistik`, Rolle Messmethodik und Statistik.
- Beginn: 2026-10-03, 00:14:02 UTC. Ende: 2026-10-03, 00:19:58 UTC.
- Zugängliche Modellangabe laut gemeinsamem Eingabepaket und geerbter Elternlaufzeit: GPT-6.1-Sol, `gpt-6.1-sol`, Reasoning `ultra`. Ein eigener interner Versionsnachweis, Gewichte, Trainingsstand und nicht zugängliche Anbietervorgaben sind unbekannt. Eine andere Modellfamilie ist durch diesen Bericht nicht nachgewiesen.
- Verfügbare Werkzeuge: Shell/Dateizugriff, Web-Recherche, Uhr, lokale Bildansicht, Computer-Use-Oberfläche und die geerbten Vermittlungswerkzeuge. Benutzt: `functions.exec` mit `exec_command`, `web__run`, `clock__curr_time`, `view_image` und `apply_patch`. Die Computer-Use-Oberfläche, weitere Reviewer, Subagents und ESS-Analysewerkzeuge wurden nicht benutzt.
- Gelesene Skills: `unslop` für den Bericht und `pdf` für die Gewichtungsanleitung. Die Memory-Registry-Suche nach Projekt und LIFE-93 brachte keine Treffer; keine frühere Erinnerung wurde als Beleg genutzt.
- Andere Reviewerberichte, spätere Autorantworten und spätere Korrekturen wurden nicht gelesen. Nur diese Berichtsdatei wurde im Repository angelegt. Downloads und synthetische Arbeitsdateien liegen unter `/tmp/life93-audit-reviewer-3/`.
- ESS-Rohantworten wurden nicht geöffnet. Es gab keinen Import, Deutschlandfilter, A/B-Split, Fallzählung oder empirischen Modelllauf.

## Gesicherte Eingaben

Gemeinsamer Auftrag `reports/audit-recherche/pruefauftrag-gemeinsam.md` vollständig gelesen, anschließend Issue und Manifest. Forschungsstand ausschließlich `reports/audit-recherche/ausgangsfassung/`; Basiscommit laut Manifest `1a7b0c38f28e27219d59380c039f9bb0446a71dd`, Branch `research/life-93-methodology`, eingefroren 2026-10-03 um 00:13:28.961919 UTC. Issue-Stand `updatedAt 2026-10-02T22:07:24.510Z`.

Manifest selbst: SHA-256 `dab36982ce6aac113acc2f807611e8630b546ee451684d683a096e0b4fd23cd8`.

Die eigene SHA-256-Prüfung bestätigte alle 26 Projektdateien im Manifest einschließlich ihrer Bytezahlen und alle drei `auditInputFiles`. Ergebnis: 29 geprüft, 29 Hashübereinstimmungen, keine Abweichung. Relevant sind besonders:

| Eingabe                     | Bestätigter SHA-256                                                |
| --------------------------- | ------------------------------------------------------------------ |
| `docs/pruefregeln.md`       | `1b10d9d7aa46a0a4e8cbc6e25c80a2b046f1cf611ab62aed6321b24af6367c77` |
| `docs/analyseplan.md`       | `d0e1579f2e6891f097548c1c48d7cfb10f4f6f3d1bf5c0f228c25ba696ae1560` |
| `docs/belegregister.md`     | `eebb44ad32f681c6afff5165a4d840eed7221d34a28d6b95a8c8d3917865994a` |
| `docs/quellen.json`         | `d85f080d7be311877076d637b642ee201d4da7f6e1ae3de1e0f4c0d7a0b63c30` |
| `issue-LIFE-93.md`          | `d25ba503af100f27ac1c81706b1bd7a2a69243c09c3ecc29d32f6e1d77a54364` |
| `pruefauftrag-gemeinsam.md` | `ef26517dc7dd02c9e626b991275375c73a464abf074f6178baff0576390b0f8f` |

Reproduktion der Hashprüfung, aus dem Repository-Verzeichnis:

```python
import hashlib, json, pathlib
r = pathlib.Path("reports/audit-recherche")
m = json.loads((r / "ausgangsmanifest.json").read_text())
for name, meta in m["files"].items():
    b = (r / "ausgangsfassung" / name).read_bytes()
    assert hashlib.sha256(b).hexdigest() == meta["sha256"]
    assert len(b) == meta["bytes"]
for name, expected in m["auditInputFiles"].items():
    assert hashlib.sha256((r / name).read_bytes()).hexdigest() == expected
```

Diese Dateiprüfung belegt die identische Eingabefassung. Sie belegt keine Blindheit, Repräsentativität oder wissenschaftliche Gültigkeit.

## Selbst kontrollierte Originalquellen

Zugriffe am 2026-10-03. Die PMC-Seiten sind öffentliche Autorenmanuskripte, soweit die Seiten sie so kennzeichnen. Ihr HTML ist eine aktuelle Zugangsfassung, keine unveränderliche Verlagsdatei. Einige `web__run`-Aufrufe lieferten reCAPTCHA oder leere PubMed-Inhalte. Direkter HTTP-Abruf des öffentlichen PMC-Volltexts gelang; der tatsächlich gelesene Umfang steht unten. Nicht gelesene Anhänge und zitierte Originalstudien gelten nicht als geprüft.

| Quelle und Fassung                                                                                                                                                                                                                                                          | Tatsächlich geprüfte Fundstellen                                                                                                                                                                                                                                  | Befund und Grenze                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Kaminska: ESS-Gewichtungsleitfaden V1.2, 06.07.2023](https://stessrelpubprodwe.blob.core.windows.net/data/methodology/ESS_weighting_data_1_2.pdf)                                                                                                                          | Abschnitte 2, 3, 4.1–4.3 und 5 textuell; Abschnitt 3 zusätzlich vollständig als gerenderte PDF-Seite 6, gedruckte Seite 4, visuell geprüft.                                                                                                                       | `anweight` ist der empfohlene Ausgangspunkt; `psu` und `stratum` sind die Designindikatoren. Punkt- und Varianzschätzung sind zu unterscheiden. Der Leitfaden ist kein Nachweis einer funktionierenden ordinalen CFA-Implementierung. PDF: 200.908 Bytes, SHA-256 `6b9c04b70b8f231de1b9040e4afcfc9387fc95e4a1d15ec0496aa7638f8528e5`, identisch mit Quellenkatalog.                                                                       |
| [Flora/Curran 2004, DOI 10.1037/1082-989X.9.4.466](https://pmc.ncbi.nlm.nih.gov/articles/PMC3153362/)                                                                                                                                                                       | Abstract; „The Current Study“; „Continuous Latent Response Distributions“; „Ordinal Observed Distributions“; „Model Specifications“; „Data Generation and Analysis“; „Implications for Applied Research“; „Study Limitations and Directions for Future Research“. | Simulation mit zwei und fünf Kategorien, vier einfachen Ein-/Zweifaktormodellen, Stichprobengrößen 100/200/500/1.000, korrekt spezifizierten Modellen und homogenen Ladungen. Robustes WLS schnitt unter diesen Bedingungen günstiger ab als volles WLS. Die Autoren begrenzen die Generalisierung ausdrücklich. Das ist kein universeller Schätzer-, EFA-, Missing-, Survey-Design- oder Fit-Cutoff-Nachweis.                            |
| [Putnick/Bornstein 2016, DOI 10.1016/j.dr.2016.06.004](https://pmc.ncbi.nlm.nih.gov/articles/PMC5145197/)                                                                                                                                                                   | „Testing Measurement Invariance“; „Configural invariance“ einschließlich Absatz zu nachträglichen Änderungen; „Scalar invariance“; „Parameterization and Model Identification“; „Fit of Measurement Invariance Models“.                                           | Trägt B-METH-003: Gruppenvergleichbarkeit und explorativer Status datengetriebener Modelländerungen. Der ausführliche Beispielablauf nutzt kontinuierliche Items; Variationen für andere Skalen werden genannt. Er ist kein vollständiger Entscheidungsvertrag für die geplanten ordinalen Rohscores.                                                                                                                                     |
| [McNeish 2018, DOI 10.1037/met0000144, Autoreninstitution ASU](https://asu.elsevierpure.com/en/publications/thanks-coefficient-alpha-well-take-it-from-here/)                                                                                                               | Abstract und bibliografische Angaben. PubMed-Zugang lieferte in diesem Lauf keinen verwertbaren Abstract.                                                                                                                                                         | Bestätigt die enge Aussage, dass Alpha-Annahmen geprüft werden müssen. Volltextverfahren, Rechenformeln und Softwareanhang nicht geprüft.                                                                                                                                                                                                                                                                                                 |
| [Raykov/Marcoulides, online 2017, Heft 2019, DOI 10.1177/0013164417725127](https://pmc.ncbi.nlm.nih.gov/articles/PMC6318747/)                                                                                                                                               | Abstract; „Misinterpretation of the Relationship Between Coefficient Alpha and Reliability“; „Should We Really Abandon the Use of Coefficient Alpha?“.                                                                                                            | Die Gegenposition in B-METH-004 ist korrekt erfasst. Brauchbarkeit von Alpha ist an Modellbedingungen gebunden, insbesondere den behandelten Einfaktormodellen und Fehlerbeziehungen. Die Quelle begründet weder einen pauschalen Alpha-Cutoff noch die Reliabilität eines hier noch unbekannten Scores.                                                                                                                                  |
| [Wu/Estabrook 2016, DOI 10.1007/s11336-016-9506-0](https://pmc.ncbi.nlm.nih.gov/articles/PMC5458787/)                                                                                                                                                                       | Abstract, Einleitung, Abschnitt 2.2 und Abschnitt 10.                                                                                                                                                                                                             | Ordinale Invarianzmodelle brauchen passend gewählte Identifikationsbedingungen. Verschiedene Ausgangsrestriktionen können verschiedene Prüfentscheidungen erzeugen. Partielle Invarianz wird vom Artikel nicht vollständig gelöst. Neue ergänzende Quelle dieses Audits, bisher nicht im Projektkatalog.                                                                                                                                  |
| [Tse/Lai/Zhang, online 29.11.2023, Heft 2024, DOI 10.3758/s13428-023-02247-6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11133089/)                                                                                                                                           | Abstract; „The current study“; „Observed mean comparison“; „Factor mean comparison“; Simulationsdesign, Datengenerierung und Analyse; Diskussion; Grenzen.                                                                                                        | Unterscheidet Vergleiche beobachteter ordinaler Mittelwerte und latenter Mittelwerte. Unter den behandelten Itemfaktormodellen können ungleiche spezifische Varianzen beobachtete Mittelwerte verzerren, obwohl Ladungen und Schwellen gleich sind. Die Simulation betrifft ausgewählte Einfaktormodelle; sie prüft nicht das deutsche ESS-Design, beliebige Faktorenstrukturen oder die künftige Webübertragung. Neue ergänzende Quelle. |
| [Green/Yang 2009, DOI 10.1007/s11336-008-9099-3, Verlagsseite](https://www.cambridge.org/core/journals/psychometrika/article/abs/reliability-of-summed-item-scores-using-structural-equation-modeling-an-alternative-to-coefficient-alpha/ADD66755CCF95B949428F8DB97AFB1B0) | Abstract und bibliografische Angaben.                                                                                                                                                                                                                             | Unterscheidet Reliabilität tatsächlich summierter Itemwerte von linearen SEM-Verfahren bei nichtlinearer Beziehung zwischen Faktoren und Itemwerten. Volltext und konkrete Schätzformeln nicht zugänglich geprüft. Daher nur Grundlage für weiteren Prüfbedarf, keine fertige Verfahrensempfehlung. Die 2025-Anzeige der Verlagsplattform ist nicht das Erscheinungsjahr des Artikels.                                                    |

## Ausgeführte Untersuchungen und Startbedingungen

| Untersuchung                                          | Ergebnis                                                                                                                                                                                                                          | Aussagegrenze                                                                                                                                                                                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hashprüfung und Versionsabgleich                      | Alle Manifest-Einträge stimmen.                                                                                                                                                                                                   | Technische Eingabesicherung.                                                                                                                                                                                                             |
| Auswahlregeln gegen LIFE-93, Phase 1                  | R07–R09 und P02 verlangen vollständigen Katalog, Einzelbegründungen, konkurrierende Erwartungen und getrennte Ersturteile. Das entspricht dem Auftrag.                                                                            | Kein Katalog vorhanden; keine tatsächliche Auswahl bewertet.                                                                                                                                                                             |
| Blindheit und explorativ/bestätigend                  | R06/R10, Plan Z. 13–22 und P03 trennen A/B und politische Prüfvariablen, frieren Modelle vor B ein und kennzeichnen Änderungen danach als explorativ. Die dokumentierte frühere öffentliche Aggregat-Exposition wird offengelegt. | Zugriffsschutz existiert noch nicht; aus Dokumenten und Tags folgt kein tatsächlicher Schutz. Eine Zeilenteilung innerhalb gemeinsamer PSUs schafft keine statistische Unabhängigkeit. Dieser Punkt ist in P03 bereits zutreffend offen. |
| Ordinale Verfahren und zentrale Literaturbehauptungen | B-METH-001 bis B-METH-004 sind in ihrer begrenzten Form gestützt. Insbesondere wird Flora/Curran nicht als fertige Methodenentscheidung ausgegeben.                                                                               | Kein Verfahren ausgewählt, keine Softwareausführung, keine Kennwerte.                                                                                                                                                                    |
| Gewichtung und Stichprobendesign                      | ESS-Ausgangspunkt und gesonderte designgerechte Unsicherheit sind richtig getrennt. P04/P07 verlangen Softwarefähigkeit, PSU-/Schichtbehandlung und Freiheitsgrade.                                                               | Header-Vorhandensein aus dem Dateieingangsbericht belegt weder gültige Designwerte noch die Implementierung. Rohdaten hierfür nicht geprüft.                                                                                             |
| Missing, Unsicherheit, Dominanz und Instabilität      | P05–P12 und R12–R18 halten Entscheidungen offen und nennen Begrenzung/Ausschluss. Drei synthetische Gegenbeispiele präzisieren die Anforderungen; Ergebnisse unten.                                                               | Keine tatsächlichen Missing-Muster, dominanten ESS-Items oder instabilen Wählergruppenbefunde festgestellt.                                                                                                                              |
| Startgate gegen LIFE-93                               | Der Start ist offen: Plan Z. 3/52, Projekt Z. 19/32/36 und Phasenbericht Z. 24/32–36 stimmen überein. Die dokumentierte Entscheidung nur CodeRabbit erfüllt die getrennten Erstbewertungen anderer Modellfamilien nicht.          | Dieses Audit ändert dieses organisatorische Gate nicht. Es ist weder Phase-0-Abnahme noch Ersatz für die späteren Itemurteile.                                                                                                           |

Die erlaubte nächste Arbeit bleibt öffentliche Katalog- und Literaturrecherche. Vollständiger Import, Split, Modellbildung, Entblindung und Analyse-/Modell-Tags folgen erst den tatsächlich erfüllten Voraussetzungen. Ich habe die Rechteklärung nicht abschließend rechtlich geprüft.

Technische Konsistenz heißt hier, dass Eingaben identisch sind und Rechenregeln korrekt umgesetzt werden. Reliabilität betrifft die Wiederholungs-/Messkonsistenz des festgelegten Scores unter begründeten Annahmen. Validität betrifft die Evidenz für seine konkrete Interpretation. Neutralität betrifft Auswahl, Begriffe und gleiche Prüfmaßstäbe. Keine dieser Fragen wird allein durch die anderen beantwortet. Die Arbeitsfassung hält diese Grenzen bereits sichtbar. Ihr späterer politischer Neutralitätsstatus wurde nicht geprüft.

## Findings

### R3-F01: Invarianz muss zur beobachteten ordinalen Auswertung passen

- Betroffen: `reports/audit-recherche/ausgangsfassung/docs/analyseplan.md:43–45`, P08–P10; `docs/pruefregeln.md:39–43`, R13/R15/R17; B-METH-003. Abhängige Vorgaben: `reports/audit-recherche/issue-LIFE-93.md:138–143` und `:161–164`.
- Status: spätere Anforderung. Der Entwurf behauptet nicht, dass skalare Invarianz bereits genügt oder bestanden sei.
- Problem und Beleg: Der geplante Hauptscore ist ein Mittelwert beobachteter 0–1-Kategorien. Das ist eine andere Zielgröße als ein latenter Faktormittelwert. Tse/Lai/Zhang, „Observed mean comparison“ und „Factor mean comparison“, zeigen unter ihrem ordinalen Itemfaktormodell, warum die Anforderungen auseinanderfallen. Wu/Estabrook, Abschnitt 10, begründen zusätzlich die Bedeutung ordinaler Identifikation. Eine allgemeine Invarianzliste reicht deshalb nicht als spätere Freigaberegel.
- Schweregrad: erheblich für konstruktbezogene Gruppen- und Näheaussagen. Ein passender CFA-Fit könnte einen unpassenden Scorevergleich sonst unbeabsichtigt freigeben. Keine gegenwärtige empirische Aussage wird hier widerlegt.
- Folge: Rohscoreunterschiede dürfen ohne diesen Nachweis nicht allein als Unterschiede des zugrunde gelegten Konstrukts interpretiert werden. Rein beschreibende Unterschiede in konkret berichteten Antworten brauchen einen entsprechend engeren Text.
- Konkrete Korrektur: P09/P10 um die Zielgröße jeder Prüfung erweitern. Für ordinale Items Schwellen, Ladungen, spezifische Varianzen, Identifikation und den erlaubten Vergleich ausdrücklich festlegen. Vorab entscheiden, welche praktisch relevanten Folgen partieller Nichtinvarianz die Scoreaussage begrenzen oder sperren. Keine unbesehene Übernahme eines kontinuierlichen Standardablaufs und kein universeller Cutoff. Einen Wechsel zu latenten Hauptscores nicht stillschweigend vornehmen, da LIFE-93 den einfachen Score vorgibt.
- Erneute Prüfung: Vor Datenzugriff denselben freigegebenen Entscheidungsvertrag an synthetischen Fällen mit gleichen latenten Mittelwerten, aber ungleichen Schwellen beziehungsweise spezifischen Varianzen prüfen. Die Regel muss irreführende konstruktbezogene Rohscorevergleiche sperren oder auf den belegten beschreibenden Geltungsbereich begrenzen. Nach Freigabe die tatsächlichen ordinalen Gruppenbefunde mit designgerechter Präzision prüfen.

### R3-F02: Mindestantworten allein sichern keine gemeinsame Norm

- Betroffen: `reports/audit-recherche/ausgangsfassung/docs/analyseplan.md:40/43`, P05/P08; `docs/pruefregeln.md:39–41`, R13–R15. LIFE-93 `:142` fordert dieselbe Mindestantwortregel für Web- und ESS-Fälle.
- Status: spätere Anforderung.
- Problem und Beleg: Bei Mittelung verfügbarer Antworten können unterschiedliche ausgelassene Items den gemessenen Inhalt verändern. Eine gemeinsame Mindestzahl verhindert das nicht. Eigene, ausschließlich synthetische Gegenrechnung: Ein Teilscore von 0,5 hat in einer Vollscore-Norm eine empirische Verteilungsposition von 0,25 und in der Norm desselben beantworteten Itemteils eine Position von 0,75. Das Beispiel beweist keine geeignete Missing-Strategie; es widerlegt die Annahme, Mindestanzahl und gleicher Zahlenbereich allein würden dieselbe Normbedeutung sichern.
- Schweregrad: erheblich für persönliche Perzentile mit ausgelassenen Items. Der normative Bezug kann sich ändern, obwohl die technische Auswertung die vereinbarte Formel korrekt erfüllt.
- Folge: Ein persönliches Perzentil kann sonst auf einer anderen Fragenkombination beruhen als seine Referenzverteilung. Ebenso kann der Ausschluss bestimmter ESS-Fälle die tatsächlich normierte Population einschränken.
- Konkrete Korrektur: In P05/P08 festlegen, ob vollständige Skalen erforderlich sind oder wie erlaubte Antwortmuster vergleichbar werden. Normierungsverfahren, tatsächlich vertretene Referenzpopulation und Unterdrückung bei unzureichender Information je erlaubtem Muster bestimmen. Gleiche Antwortzahlen mit verschiedenen Itemidentitäten ausdrücklich prüfen. Keine automatische Empfehlung zur Imputation; dafür fehlen derzeit Items und begründete Mechanismen.
- Erneute Prüfung: Den Entscheidungsvertrag zunächst mit synthetischen Teilantwortmustern testen, einschließlich selektiv ausgelassener Items und strukturbedingt nicht gestellter Fragen. Später Abdeckung, Präzision und Sensitivität der zulässigen Muster dokumentieren. Unprüfbare Muster müssen die vorgesehene Anzeigegrenze auslösen.

### R3-F03: Rangstabilität braucht auch gemeinsame Stichprobenunsicherheit

- Betroffen: `reports/audit-recherche/ausgangsfassung/docs/analyseplan.md:42/46–47`, P07/P11/P12; `docs/pruefregeln.md:40/43`, R14/R17; LIFE-93 `:143/154/162–163`.
- Status: spätere Anforderung.
- Problem und Beleg: Stabilität unter Modellvarianten beantwortet nicht, ob eine Nähe-Reihenfolge gegenüber Stichprobenschwankungen stabil ist. Die allgemeine Unsicherheitsforderung in P11 muss hierfür noch operationalisiert werden. Eigener mathematischer Beleg: Bei zwei Schätzern mit marginalem Standardfehler 0,1 beträgt der Standardfehler ihrer Differenz je nach Korrelation 0,04472 oder 0,19494 für die synthetischen Korrelationen 0,9 beziehungsweise −0,9. Dieselben marginalen Fehler liefern unterschiedliche Sicherheit für eine Reihenfolge. Dies ist keine Annahme über die tatsächlichen ESS-Kovarianzen.
- Schweregrad: mittel. Betrifft die optionale Nähe-Reihenfolge; das inhaltliche Dimensionsprofil kann ohne Rangliste bestehen.
- Folge: Getrennte Gruppenintervalle und eine unter wenigen Rechenvarianten gleichbleibende Reihenfolge können eine unsichere Rangfolge verdecken.
- Konkrete Korrektur: P11 um ein gemeinsames designgerechtes Verfahren für Gruppen-/Normschätzungen und die daraus abgeleiteten Distanzen erweitern. Wiederholungen oder analytische Varianzrechnung müssen die Abhängigkeit der Schätzer erhalten. Stichproben-, persönliche Mess- und Modellentscheidungsunsicherheit getrennt ausweisen und begründen, welche davon in die Rangentscheidung eingehen. Vorab definierte Anzeige- oder Unterdrückungsregel ohne unbegründeten Standardgrenzwert.
- Erneute Prüfung: Synthetische Fälle mit fast gleichen Gruppenabständen, ungleichen Präzisionen und unterschiedlichen Abhängigkeiten durch das spätere Verfahren laufen lassen. Es muss unzureichend abgesicherte Reihenfolgen unterdrücken. Erst später designgerechte ESS-Auswertung ausführen.

### R3-F04: Reliabilität und persönlicher Messbereich müssen den exportierten Score betreffen

- Betroffen: `reports/audit-recherche/ausgangsfassung/docs/analyseplan.md:41/43`, P06/P08; `docs/pruefregeln.md:33/39–40`, R12–R14; B-METH-004 und B-MODEL-001.
- Status: spätere Anforderung; die gegenwärtige Auswahl des Kennwerts ist ausdrücklich offen.
- Problem und Beleg: Ein Reliabilitätskennwert aus einem ordinalen Faktorverfahren muss dem tatsächlich exportierten gleichgewichteten Kategorie-Mittelwert zugeordnet werden. Ein Kennwert für zugrunde gelegte kontinuierliche Antwortvariablen ist nicht ohne weitere Begründung der Kennwert dieses beobachteten Scores. Green/Yang, Abstract, behandelt genau diese Unterscheidung nichtlinearer Beziehungen für summierte Itemwerte; sein Volltext wurde hier nicht geprüft. Raykov/Marcoulides zeigen, dass Kennwertinterpretation an konkrete Modellbedingungen gebunden ist. Keiner dieser Zugänge liefert bereits einen geprüften persönlichen Intervallalgorithmus für dieses Projekt.
- Schweregrad: erheblich für einen persönlichen Messunsicherheitsbereich oder eine Aussage zur Reliabilität des Webscores. Ein allgemeines Reliabilitätsetikett kann sonst eine Sicherheit suggerieren, die für die angezeigte Größe nicht belegt ist.
- Folge: Modellfit, Reliabilität eines latenten Modells und persönliche Unsicherheit dürfen keine austauschbaren Freigaben sein. Der nicht empirisch geprüfte Wechsel von ESS-Interview zu Webbeantwortung bleibt eine weitere Übertragungsgrenze, wie R21 bereits vorsieht.
- Konkrete Korrektur: Zielscore, Itemgewichte, erlaubte Missing-Muster, Referenzpopulation, Fehlermodell und Maßstab des Kennwerts festlegen. Einen persönlichen Bereich nur bei geprüften Voraussetzungen und Verfahren ausgeben. Ohne tragfähige Evidenz die in LIFE-93 vorgesehene engere Darstellung mit sichtbarer offener Messunsicherheit entscheiden; kein Ersatzintervall aus Modellvarianten erzeugen.
- Erneute Prüfung: Zunächst passende Volltextmethoden und Softwareverfahren kontrollieren. Mit synthetischen ordinalen Antwortmodellen prüfen, ob das Verfahren den Fehler des exportierten Scores schätzt und im begründeten Anwendungsbereich seine vorgesehenen Eigenschaften besitzt. Empirische Reliabilitätswerte und deren Unsicherheit erst nach Analysestart berechnen; daraus keine Validität oder Webmodus-Validierung ableiten.

## Synthetische Gegenrechnungen und Grenzen

Aufruf tatsächlich ausgeführt:

```text
python /tmp/life93-audit-reviewer-3/synthetische-pruefung.py
```

Skript-SHA-256 `4b104202c5095dd3c95c5cdf09c9a371be0cb9ae2b9bf54a9f2c193729291d6c`. Damit die Belege auch nach Verlust der temporären Datei wiederholbar bleiben, genügt folgende unabhängige Kurzfassung derselben Rechnungen:

```python
from math import sqrt

def score(values):
    valid = [v for v in values if v is not None]
    return sum(valid) / len(valid)

def cdf(reference, value):
    return sum(v <= value for v in reference) / len(reference)

reference = [(v, 1.0) for v in (0.0, 0.25, 0.5, 0.75)]
partial = score((0.5, None))
print(partial)
print(cdf([score(x) for x in reference], partial))
print(cdf([x[0] for x in reference], partial))
print([score((0.5, v)) for v in (0.0, 0.5, 1.0)])
print([score((0.5,)) for _ in range(3)])
print([sqrt(0.1**2 + 0.1**2 - 2*r*0.1**2) for r in (0.9, -0.9)])
cases = ((0.0, 0.25, 1.0), (0.0, None, 0.75), (0.5, 0.5, None))
print(max(abs(score([None if v is None else 1-v for v in x])
              - (1-score(x))) for x in cases))
```

Ergebnisse: Teilscore 0,5; Verteilungsposition 0,25 gegen die Vollnorm und 0,75 gegen die passende Teilnorm. In einem zweiten Beispiel änderte nur ein Item seine Werte, obwohl beide dieselben rechnerischen Gewichte hatten: vollständige Scores 0,25/0,5/0,75, ohne dieses Item nur 0,5. Gleiche Gewichte sichern daher keine empirisch gleiche Bedeutung oder Dominanz; P06/P12 müssen die bereits verlangte Leave-one-out-Prüfung konkretisieren. Die oben beschriebenen Differenzstandardfehler wurden berechnet. Bei drei festen Missing-Masken bestätigte die Rechnung die algebraische Rohscorespiegelung bis zum Gleitkommafehler `1,11 × 10⁻¹⁶`.

Dies sind Rechenbeispiele mit vollständig erfundenen Werten. Sie sind keine Tests der Projektpipeline, keine Monte-Carlo-Validierung, keine Bevölkerungsergebnisse und keine neuen Items. Die Skriptdatei liegt ausschließlich im eigenen temporären Arbeitsbereich. Die Beispiele zeigen, welche Mechanismen eine spätere Prüfung abdecken muss. Sie legen keine Schwelle und kein Analyseverfahren fest.

Nicht ausgeführt: ESS-Import- und Designwertprüfung; alle EFA/CFA-, Reliabilitäts-, Invarianz-, Missing-, Norm-, Dominanz- und Sensitivitätsanalysen; technische Implementierungsprüfung von Survey-/Ordinalverfahren; tatsächliche Schutzprüfung von B; Wählergruppenbildung; persönliches Messintervall; Rangstabilitätsanalyse; Webmodus- oder Verständlichkeitsprüfung. Fehlende Themenliteratur und das vollständige Frageninventar wurden hier nicht nachträglich erstellt.

Die Startbedingungen bleiben offen. Ein zulässiger nächster Auftrag kann die Originalquellen und Entscheidungsverträge für P04–P12 vertiefen sowie den deutschen Fragenbestand dokumentieren. Endgültige Item- und Modellentscheidungen brauchen weiterhin die verlangten getrennten Bewertungen und Abnahmen. Dieser Bericht erteilt keine Gesamtfreigabe.

## Technischer Abschluss dieses Berichts

Die eigene Berichtsdatei wurde mit `pnpm exec prettier --write reports/audit-recherche/reviewer-3-statistik.md` formatiert. `pnpm check` wurde anschließend ausgeführt und brach im globalen Formatcheck ab: sieben Dateien des gemeinsamen Audit-Eingangs beziehungsweise Protokolls waren nicht Prettier-konform (`00-eingangspruefung.json`, `01-eingang-wiederholbar.json`, `agent-protokoll.json`, `issue-LIFE-93.json`, `issue-LIFE-93.md`, `pruefauftrag-gemeinsam.md`, `werkzeuge.json`). Diese Dateien wurden wegen der unabhängigen Prüfgrenze nicht verändert und ihre Inhalte nicht zusätzlich als Forschungsgrundlage gelesen. Typecheck, Tests und Build liefen nach diesem Abbruch nicht. Die gesonderte Prüfung `pnpm exec prettier --check reports/audit-recherche/reviewer-3-statistik.md` wurde ausgeführt und bestand. Der globale Formatbefund ist ein technischer Abschlussbefund, kein methodisches Finding.
