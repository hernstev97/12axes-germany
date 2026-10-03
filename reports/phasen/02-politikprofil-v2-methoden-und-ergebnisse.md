# 12 Axes Deutschland: Politikprofil v2 — Methoden und historische Einzelreferenzen

**WIP / Entwurf für eine gezielte unabhängige Präsentationsprüfung.** Die öffentliche Exportentscheidung betrifft 42 historische Einzelreferenzen; alle 43 Originalfragen aus fünf getrennten Studien bleiben im Inhaltsbestand. Die Themenordnung ist keine Abnahme des Hauptprodukts, einer neuen Webadministration oder eines Releases.

## Methode und Geltungsbereich

Acht Rubriken ordnen konkrete Präferenzen, Prinzipien, Wichtigkeitsurteile und nominale Antworten. Sie sind keine empirischen Dimensionen. Es gibt keine gemeinsame Personenmatrix, keinen Faktor, Gesamtscore, persönlichen Rang, keine Partei-Gesamtübereinstimmung und keine aktuelle Bevölkerungsnorm. Die historische Referenz beantwortet allein, wie die gebundene Originalfrage in ihrer Erhebung beantwortet wurde.

Primär: Summe der pspwght gültiger Antworten einer Kategorie geteilt durch die Summe der pspwght aller gültigen Antworten derselben Frage. pspwght wird nicht nochmals mit dweight multipliziert. Nach dem gebundenen [ESS-Gewichtungsweg](https://www.europeansocialsurvey.org/methodology/ess-methodology/data-processing-and-archiving/weighting) kombiniert pspwght Designgewicht und Poststratifikation; anweight enthält zusätzlich die Bevölkerungsgrößenkomponente. Ein konstanter positiver Landesfaktor ändert Quotienten nicht. Jede Frage hat ihren eigenen gültigen Nenner. Fehlende und nichtgestellte Angaben sind ausgeschlossen und separat abgerechnet; eine leere Exportzelle heißt export_blank_unclassified. Ungewichtete und dweight-Rechnungen dienen getrennten Sensitivitäten, anweight einer Diagnose. Die maximale absolute Differenz wird in Prozentpunkten dargestellt; das Gewichtsverhältnis gilt für alle deutschen Studienfälle.

Die vorab festgelegte 100/5-Darstellungsheuristik sperrt eine Referenz unter 100 gültigen Antworten oder bei einer positiven ungewichteten Kategorie mit 1–4 Fällen; 100 und 5 liegen auf der zulässigen Seite der Grenze. Keine gültigen Antworten erzeugen ebenfalls keine Referenz. Nullbesetzte Originalkategorien bleiben erhalten. Dies sind projektspezifische Darstellungsregeln, keine wissenschaftlichen Präzisions- oder Anonymitätsgarantien. Der öffentliche Export enthält keine Zellcounts; diese Bedingung wird hier nicht unabhängig neu aus Rohdaten bewiesen. Keine Kategorienzusammenlegung und kein Itemausschluss nach Ergebnissen.

Die erste v2-Ausführung berechnet keine Standardfehler. Unsicherheit bleibt ausdrücklich nicht berechnet: keine Konfidenzintervalle und keine persönliche Messunsicherheit; fehlender SE bedeutet niemals SE=0. Gewichtung behebt Auswahl-, Nonresponse-, Kontext- und Modusverzerrungen nicht automatisch. Prozentdarstellungen sind gerundet; Kategorienanteile summieren sich vor Darstellung innerhalb 1e-12 auf eins.

Historische v1-A/B-Antworten des Neunermoduls waren bekannt. Die sechs zusätzlichen ESS11-Felder stammen aus derselben Erhebung und sind deskriptive Sekundärangaben, keine unangetastete Bestätigung. Die tatsächlichen v2-Aggregate sind diesem Berichtsautor nun bekannt. Die beiden frischen Ergebnisrollen arbeiteten getrennt, aber in derselben Codex-Modellfamilie; gemeinsame Fehler bleiben möglich und Agentenübereinstimmung ist kein Neutralitätsbeweis. Ihre Kontrolle war eine Aggregatreproduktion, keine unabhängige Rohdaten-/Downloadreproduktion oder erneute Berechnung individueller Ratioextrema.

Root dokumentiert die tatsächliche vorgelagerte Prüfung der öffentlichen und privaten Pins und hat die Fragefreigaben gebunden. Dieser Build prüft veröffentlichte Quellen-, Vertrags-, Export-, Entscheidungs- und Berichtbytes; er liest keine privaten Kandidaten oder Rohdaten. Formale Statusstrings und Hashsyntax sind allein kein Wissenschaftsnachweis. Menschliche Verständlichkeit, Fairness, Gestaltung, Claudes Schlusskontrolle, Rechte-/kommerzielle Nutzung und persönlicher Release bleiben offen.

## Verbindliche Kriterien und Belege

[Empirieplan v2](../../docs/empirie-plan-v2.entwurf.md#deskriptive-auswertung) und [Analysevertrag](../../data/analysevertrag.v2.entwurf.json) binden Primärgewicht, Kategorien, Nenner, Serialisierung, Missing, Sensitivitäten und feste Darstellungsfolgen. [Messformen](../../docs/messformen-v2.entwurf.md#begrenzte-einzelangaben-als-ausführbarer-weg) trennen Einzelangaben von formativen und reflektiven Formen. [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) verlangt Binnenabdeckung, gleiche Belegmaßstäbe und offengelegte Auslassungen; Rubriken sind keine Faktoren.

B-V2-M01: [Bollen/Lennox 1991, DOI 10.1037/0033-2909.110.2.305](https://doi.org/10.1037/0033-2909.110.2.305), im Methodenentwurf nur Abstract geprüft. B-V2-M02: [OECD/JRC 2008, gedruckte S.15–16/31–35, PDF17–18/33–37](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf): transparente Auswahl/Aggregation; Übertragung auf Personenprofile ist begrenzte methodische Ableitung. B-V2-M03: [Krosnick 1999, gedruckte S.37/40](https://web.stanford.edu/dept/communication/faculty/krosnick/docs/1999/1999%20Maximizing%20questionnaire%20quality.pdf): Antwortformat und Durchführung können Antworten beeinflussen. Keine Gleichwertigkeit einer neuen Website daraus ableiten.

[Kriesi et al. 2006, DOI 10.1111/j.1475-6765.2006.00644.x](https://doi.org/10.1111/j.1475-6765.2006.00644.x) begründet im Themenentwurf eine Suchgliederung, keine heutige deutsche Personenstruktur. [ESS6-Demokratieantrag, PDF8–16](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS6_democracy_proposal.pdf) trennt Prinzipien und Umsetzung. [Walgrave et al. 2009, S.1161–1163/1166–1168](https://medialibrary.uantwerpen.be/oldcontent/container2608/files/Walgrave%20et%20al%202009%20-%20voting%20aid%20applications.pdf) begründet Auswahlfolgenprüfungen; belgische VAA-Befunde sind kein deutscher Fairnessnachweis. Diese Literaturfundstellen stammen aus den gebundenen öffentlichen Methodenakten; keine neue Literaturprüfung in diesem Build.

Begrenzte Ergebnisentscheidungen: [Methoden](../loop/reviews/RESULTS-V2-001-methods-first.md), [Quellen/Konstrukte/Fairness](../loop/reviews/RESULTS-V2-001-sources-first.md) und [Root-Exportentscheidung](../loop/policy-v2-export-decisions.json). Deren offene Darstellungsbedingungen werden hier bearbeitet, nicht eigenständig für abgenommen erklärt.

## Getrennte Studien und historische Referenzpopulationen

### ESS5e03\_6 — Ausgabe 3\.6

European Social Survey European Research Infrastructure (ESS ERIC); Sikt – Norwegian Agency for Shared Services in Education and Research. [Daten-DOI](https://doi.org/10.21338/ess5e03_6) 10\.21338/ess5e03\_6; [Dokumentations-DOI](https://doi.org/10.21338/nsd-ess5-2010) 10\.21338/nsd\-ess5\-2010. Deutschland (DE), ESS-Runde 5.

Deklarierte Zielpopulation: All persons aged 15 and over resident within private households, regardless of their nationality, citizenship, language or legal status, in the countries as listed in the &quot;Geographical Coverage&quot;. Die gemeinsame ESS-Zielbeschreibung betrifft Personen ab 15 in Privathaushalten unabhängig von Staatsangehörigkeit, Sprache oder Rechtsstatus; sie ist keine vollständige realisierte Abdeckung. Declared target only; achieved German coverage and response availability have not been checked\.

Historische Feldzeit: 2010\-09\-15T00:00:00Z bis 2011\-02\-03T00:00:00Z; deklarierter Modus: Face\-to\-face interview: Computer\-assisted \(CAPI/CAMI\).

Datenlizenz: ess\-data\-cc\-by\-nc\-sa\-4\.0; Dokumentationslizenz: ess\-documentation\-cc\-by\-sa\-4\.0. Primärgewicht pspwght; Sensitivitäten und Frage-Nenner werden je Einzelangabe geführt. Keine Übertragung auf heutige Websitebesucher.

### ESS8e02\_3 — Ausgabe 2\.3

European Social Survey European Research Infrastructure (ESS ERIC); Sikt – Norwegian Agency for Shared Services in Education and Research. [Daten-DOI](https://doi.org/10.21338/ess8e02_3) 10\.21338/ess8e02\_3; [Dokumentations-DOI](https://doi.org/10.21338/nsd-ess8-2016) 10\.21338/nsd\-ess8\-2016. Deutschland (DE), ESS-Runde 8.

Deklarierte Zielpopulation: All persons aged 15 and over resident within private households, regardless of their nationality, citizenship, language or legal status, in the countries as listed in the &quot;Geographical Coverage&quot;. Die gemeinsame ESS-Zielbeschreibung betrifft Personen ab 15 in Privathaushalten unabhängig von Staatsangehörigkeit, Sprache oder Rechtsstatus; sie ist keine vollständige realisierte Abdeckung. Declared target only; achieved German coverage and response availability have not been checked\.

Historische Feldzeit: 2016\-08\-23T00:00:00Z bis 2017\-03\-26T00:00:00Z; deklarierter Modus: Face\-to\-face interview: Computer\-assisted \(CAPI/CAMI\).

**ESS8-München-Grenze:** München nahm an der Stichprobenziehung nicht teil; dort wurden keine Befragten gewonnen. Diese Referenz ist keine vollständig räumlich abdeckende Deutschlandnorm.

Datenlizenz: ess\-data\-cc\-by\-nc\-sa\-4\.0; Dokumentationslizenz: ess\-documentation\-cc\-by\-sa\-4\.0. Primärgewicht pspwght; Sensitivitäten und Frage-Nenner werden je Einzelangabe geführt. Keine Übertragung auf heutige Websitebesucher.

### ESS9e03\_3 — Ausgabe 3\.3

European Social Survey European Research Infrastructure (ESS ERIC); Sikt – Norwegian Agency for Shared Services in Education and Research. [Daten-DOI](https://doi.org/10.21338/ess9e03_3) 10\.21338/ess9e03\_3; [Dokumentations-DOI](https://doi.org/10.21338/nsd-ess9-2018) 10\.21338/nsd\-ess9\-2018. Deutschland (DE), ESS-Runde 9.

Deklarierte Zielpopulation: All persons aged 15 and over resident within private households, regardless of their nationality, citizenship, language or legal status, in the countries as listed in the &quot;Geographical Coverage&quot;. Die gemeinsame ESS-Zielbeschreibung betrifft Personen ab 15 in Privathaushalten unabhängig von Staatsangehörigkeit, Sprache oder Rechtsstatus; sie ist keine vollständige realisierte Abdeckung. Declared target only; achieved German coverage and response availability have not been checked\.

Historische Feldzeit: 2018\-08\-29T00:00:00Z bis 2019\-03\-04T00:00:00Z; deklarierter Modus: Face\-to\-face interview: Computer\-assisted \(CAPI/CAMI\).

Versionsgrenze: Edition 3\.3 is declared by current file metadata; a separate release\-date binding is not supplied here\.

Datenlizenz: ess\-data\-cc\-by\-nc\-sa\-4\.0; Dokumentationslizenz: ess\-documentation\-cc\-by\-sa\-4\.0. Primärgewicht pspwght; Sensitivitäten und Frage-Nenner werden je Einzelangabe geführt. Keine Übertragung auf heutige Websitebesucher.

### ESS10SCe03\_2 — Ausgabe 3\.2

European Social Survey European Research Infrastructure (ESS ERIC); Sikt – Norwegian Agency for Shared Services in Education and Research. [Daten-DOI](https://doi.org/10.21338/ess10sce03_2) 10\.21338/ess10sce03\_2; [Dokumentations-DOI](https://doi.org/10.21338/NSD-ESS10-2020) 10\.21338/NSD\-ESS10\-2020. Deutschland (DE), ESS-Runde 10.

Deklarierte Zielpopulation: All persons aged 15 and over resident within private households, regardless of their nationality, citizenship, language or legal status, in the countries as listed in the &quot;Geographical Unit&quot;. Die gemeinsame ESS-Zielbeschreibung betrifft Personen ab 15 in Privathaushalten unabhängig von Staatsangehörigkeit, Sprache oder Rechtsstatus; sie ist keine vollständige realisierte Abdeckung. Declared target only; achieved German coverage and response availability have not been checked\.

Historische Feldzeit: 2021\-10\-05T00:00:00Z bis 2022\-01\-04T00:00:00Z; deklarierter Modus: Self\-administered questionnaire: Paper; Self\-administered questionnaire: Web\-based \(CAWI\).

Versionsgrenze: File identity/DOI declare SC edition 3\.2; cached history/citation text still names 3\.1\. The inconsistency is preserved, not repaired\.

Datenlizenz: ess\-data\-cc\-by\-nc\-sa\-4\.0; Dokumentationslizenz: ess\-documentation\-cc\-by\-sa\-4\.0. Primärgewicht pspwght; Sensitivitäten und Frage-Nenner werden je Einzelangabe geführt. Keine Übertragung auf heutige Websitebesucher.

### ESS11e04\_2 — Ausgabe 4\.2

European Social Survey European Research Infrastructure (ESS ERIC); Sikt – Norwegian Agency for Shared Services in Education and Research. [Daten-DOI](https://doi.org/10.21338/ess11e04_2) 10\.21338/ess11e04\_2; [Dokumentations-DOI](https://doi.org/10.21338/ess11-2023) 10\.21338/ess11\-2023. Deutschland (DE), ESS-Runde 11.

Deklarierte Zielpopulation: All persons aged 15 and over resident within private households, regardless of their nationality, citizenship, language or legal status, in the countries as listed in the &quot;Geographical Unit&quot;. Die gemeinsame ESS-Zielbeschreibung betrifft Personen ab 15 in Privathaushalten unabhängig von Staatsangehörigkeit, Sprache oder Rechtsstatus; sie ist keine vollständige realisierte Abdeckung. Declared target only; achieved German coverage and response availability have not been checked\.

Historische Feldzeit: 2023\-05\-09 bis 2023\-12\-21; deklarierter Modus: Face\-to\-face interview: Computer\-assisted \(CAPI/CAMI\).

Datenlizenz: ess\-data\-cc\-by\-nc\-sa\-4\.0; Dokumentationslizenz: ess\-documentation\-cc\-by\-sa\-4\.0. Primärgewicht pspwght; Sensitivitäten und Frage-Nenner werden je Einzelangabe geführt. Keine Übertragung auf heutige Websitebesucher.

## Originalblock und neue Zusammenstellung

ESS10 B1–B12 fragt nach Demokratie im Allgemeinen. Originalreihenfolge: `ESS10SCe03_2:fairelc`, `ESS10SCe03_2:dfprtal`, `ESS10SCe03_2:medcrgv`, `ESS10SCe03_2:rghmgpr`, `ESS10SCe03_2:votedir`, `ESS10SCe03_2:cttresa`, `ESS10SCe03_2:gptpelc`, `ESS10SCe03_2:gvctzpv`, `ESS10SCe03_2:grdfinc`, `ESS10SCe03_2:viepol`, `ESS10SCe03_2:wpestop`, `ESS10SCe03_2:keydec`. B12/keydec gehört im Originalblock an die letzte Stelle und erhält unten die primäre EU-Rubrik. Die Themenordnung dieses Berichts ist keine neue Administration des Blocks.

**Originaleinleitung B1–B12:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Originalantwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

B13–B24 (wahrgenommene Umsetzung) werden ausgelassen. B25 ist die gesonderte historische Frage zum Mehrheitskonflikt; ihre Originalweiterleitungen B26–B29 sind ausgelassen. B30 ist ebenfalls nicht Bestandteil dieser festen Auswahl. Die neue Website-Zusammenstellung verändert Fragebogenkontext und Publikum; die operative CAWI-Folge ist nicht belegt und neue Webadministration ist unvalidiert.

## Wirtschaft und Verteilung

Gleichheit, Leistung, Bedarf, Herkunftsprivileg und staatliche Einkommensverringerung bleiben getrennte Gegenstände. Keine Gesamtposition zur Wirtschaft.

**Inhaltslücken:** Markt- und Eigentumsordnung, Wettbewerb, Steuerarten, Arbeits- und Industriepolitik bleiben unvollständig. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS9e03_3:sofrdst` — G26

Quelle: ESS9e03\_3, Ausgabe 3\.3. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Gesellschaft im Allgemeinen\. Es gibt viele unterschiedliche Ansichten darüber, was eine Gesellschaft gerecht oder ungerecht macht\. Wie sehr stimmen Sie jeder der folgenden Aussagen zu oder lehnen diese ab?

**Originalfrage / Aussage:** Eine Gesellschaft ist gerecht, wenn Einkommen und Vermögen gleichmäßig auf alle Menschen verteilt sind\.

**Originalinstruktion:** LISTE 68

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2324**; alle deutschen Studienfälle: 2358; fehlend: 34; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Stimme stark zu | 1 | 10,697032 |
| 2 | Stimme zu | 2 | 31,721251 |
| 3 | Weder noch | 3 | 23,176266 |
| 4 | Lehne ab | 4 | 28,551603 |
| 5 | Lehne stark ab | 5 | 5,853849 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 24 | 33,8275278 |
| No answer | 0 | 0 |
| Refusal | 10 | 8,82044451 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 42,64797231; primäre Gewichtssumme aller deutschen Studienfälle: 2358,00001768. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,396761; dweight 1,380543; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 3,03734467764, Maximum 3,03734525865; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G26.

[ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=a0bf64ee\-18c0\-404b\-979a\-af7d87edebb2; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

### `ESS9e03_3:sofrwrk` — G27

Quelle: ESS9e03\_3, Ausgabe 3\.3. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Gesellschaft im Allgemeinen\. Es gibt viele unterschiedliche Ansichten darüber, was eine Gesellschaft gerecht oder ungerecht macht\. Wie sehr stimmen Sie jeder der folgenden Aussagen zu oder lehnen diese ab?

**Originalfrage / Aussage:** Eine Gesellschaft ist gerecht, wenn hart arbeitende Menschen mehr verdienen als andere\.

**Originalinstruktion:** LISTE 68

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2335**; alle deutschen Studienfälle: 2358; fehlend: 23; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Stimme stark zu | 1 | 23,315468 |
| 2 | Stimme zu | 2 | 62,922044 |
| 3 | Weder noch | 3 | 9,804478 |
| 4 | Lehne ab | 4 | 3,504243 |
| 5 | Lehne stark ab | 5 | 0,453766 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 15 | 22,5720051 |
| No answer | 0 | 0 |
| Refusal | 8 | 6,81390525 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 29,38591035; primäre Gewichtssumme aller deutschen Studienfälle: 2358,00001768. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,403263; dweight 0,415612; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 3,03734467764, Maximum 3,03734525865; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G27.

[ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=40963e60\-daf0\-43fc\-bd0d\-268d153e3c86; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

### `ESS9e03_3:sofrpr` — G28

Quelle: ESS9e03\_3, Ausgabe 3\.3. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Gesellschaft im Allgemeinen\. Es gibt viele unterschiedliche Ansichten darüber, was eine Gesellschaft gerecht oder ungerecht macht\. Wie sehr stimmen Sie jeder der folgenden Aussagen zu oder lehnen diese ab?

**Originalfrage / Aussage:** Eine Gesellschaft ist gerecht, wenn sie sich um Arme und Bedürftige kümmert, unabhängig davon, was diese der Gesellschaft zurückgeben\.

**Originalinstruktion:** LISTE 68

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2335**; alle deutschen Studienfälle: 2358; fehlend: 23; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Stimme stark zu | 1 | 20,559467 |
| 2 | Stimme zu | 2 | 62,410492 |
| 3 | Weder noch | 3 | 11,135968 |
| 4 | Lehne ab | 4 | 5,269174 |
| 5 | Lehne stark ab | 5 | 0,624899 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 17 | 26,47515204 |
| No answer | 0 | 0 |
| Refusal | 6 | 5,51243604 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 31,98758808; primäre Gewichtssumme aller deutschen Studienfälle: 2358,00001768. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,468371; dweight 0,483987; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 3,03734467764, Maximum 3,03734525865; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G28.

[ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=1e28f946\-1481\-4f53\-bbc9\-e084e6a382e0; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

### `ESS9e03_3:sofrprv` — G29

Quelle: ESS9e03\_3, Ausgabe 3\.3. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Gesellschaft im Allgemeinen\. Es gibt viele unterschiedliche Ansichten darüber, was eine Gesellschaft gerecht oder ungerecht macht\. Wie sehr stimmen Sie jeder der folgenden Aussagen zu oder lehnen diese ab?

**Originalfrage / Aussage:** Eine Gesellschaft ist gerecht, wenn Menschen aus Familien mit hoher gesellschaftlicher Stellung Privilegien in ihrem Leben genießen\.

**Originalinstruktion:** LISTE 68

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2315**; alle deutschen Studienfälle: 2358; fehlend: 43; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Stimme stark zu | 1 | 0,933066 |
| 2 | Stimme zu | 2 | 11,956144 |
| 3 | Weder noch | 3 | 21,638291 |
| 4 | Lehne ab | 4 | 46,347250 |
| 5 | Lehne stark ab | 5 | 19,125249 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 34 | 49,19717503 |
| No answer | 0 | 0 |
| Refusal | 9 | 7,84344121 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 57,04061624; primäre Gewichtssumme aller deutschen Studienfälle: 2358,00001768. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,255342; dweight 1,256645; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 3,03734467764, Maximum 3,03734525865; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G29.

[ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=1b92f5da\-3d31\-468c\-a2be\-7d2bb0f37ad2; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

### `ESS11e04_2:gincdif` — B33

Quelle: ESS11e04\_2, Ausgabe 4\.2. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Bitte schauen Sie jetzt auf Liste 13 und sagen Sie mir, wie sehr Sie jeder der folgenden Aussagen zustimmen oder wie sehr Sie diese ablehnen\.

**Originalfrage / Aussage:** Der Staat sollte Maßnahmen ergreifen, um Einkommensunterschiede zu verringern\.

**Originalinstruktion:** LISTE 13; BITTE JEDE AUSSAGE VORLESEN

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2393**; alle deutschen Studienfälle: 2420; fehlend: 27; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Stimme stark zu | 1 | 20,383432 |
| 2 | Stimme zu | 2 | 47,413966 |
| 3 | Weder noch | 3 | 17,962906 |
| 4 | Lehne ab | 4 | 12,092408 |
| 5 | Lehne stark ab | 5 | 2,147288 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 24 | 35,9534377456 |
| No answer | 0 | 0 |
| Refusal | 3 | 1,60826325417 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 37,5617009997; primäre Gewichtssumme aller deutschen Studienfälle: 2419,99996939. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,864447; dweight 1,886631; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,992969752, Maximum 2,992969752; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: API ergänzt 9 No answer\. Deutsch sagt Staat, API government; keine freie Neufassung daraus ableiten\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess11\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf#page=13): physische PDF\-Seite\(n\) 13; originalQuestionId=B33.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=41329d27\-0f86\-4b14\-805c\-5e41e62ca17a; sourceFieldMetadataVersion=2; dataFileMetadataId=242aaa39\-3bbb\-40f5\-98bf\-bfb1ce53d8ef; dataFileMetadataVersion=179.

## Sozialstaat

Staatliche Verantwortung, Leistungszielgruppe und der feste Ausbildungs-/Leistungsbudgetkonflikt werden unterschieden. Kinderbetreuung zählt hier einmal als Primärgegenstand.

**Inhaltslücken:** Gesundheit, Pflege, Wohnen und konkrete Leistungserbringung sind nicht ausreichend erschlossen. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS8e02_3:gvslvol` — E6

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_responsibility; Gegenstand: principle.

**Originaleinleitung:** Menschen haben verschiedene Vorstellungen davon, wofür der Staat verantwortlich sein sollte und wofür nicht\. Sagen Sie mir bitte für jede der folgenden Aufgaben auf einer Skala von 0 bis 10, wie sehr der Staat dafür verantwortlich sein sollte\. 0 bedeutet, dass der Staat überhaupt nicht dafür verantwortlich sein sollte und 10 bedeutet, dass er voll und ganz dafür verantwortlich sein sollte\.

**Antwortstamm:** Sollte der Staat erstens dafür verantwortlich sein…

**Originalfrage / Aussage:** …einen angemessenen Lebensstandard im Alter sicherzustellen?

**Originalinstruktion:** INT\.: LISTE 48 VORLEGEN UND BIS FRAGE E8 LIEGEN LASSEN\. INT\.: BITTE VORLESEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2833**; alle deutschen Studienfälle: 2852; fehlend: 19; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Der Staat sollte dafür überhaupt nicht verantwortlich sein | 0 | 0,929460 |
| 1 | 1 | 1 | 0,262262 |
| 2 | 2 | 2 | 0,828238 |
| 3 | 3 | 3 | 2,211287 |
| 4 | 4 | 4 | 2,955448 |
| 5 | 5 | 5 | 8,854134 |
| 6 | 6 | 6 | 8,102770 |
| 7 | 7 | 7 | 17,223193 |
| 8 | 8 | 8 | 24,933323 |
| 9 | 9 | 9 | 11,950116 |
| 10 | Der Staat sollte dafür voll und ganz verantwortlich sein | 10 | 21,749769 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | Antwort verweigert | 77 |
| 88 | Don&\#x27;t know | Weiß nicht | 88 |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 17 | 18,71189679 |
| No answer | 0 | 0 |
| Refusal | 2 | 2,7960211 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 21,50791789; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,375537; dweight 1,558302; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: The questionnaire table prints 0–9, omitting 10 despite its 0–10 introduction and upper anchor\. Original Liste 48 and the API both include 10; the code is not inferred from a score\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=36): physische PDF\-Seite\(n\) 36; originalQuestionId=E6.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=7a2e25a8\-5d2b\-416a\-a77b\-9753aea54ee8; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=49): physische PDF\-Seite\(n\) 49; listLabelDe=Liste 48.

### `ESS8e02_3:gvslvue` — E7

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_responsibility; Gegenstand: principle.

**Originaleinleitung:** Menschen haben verschiedene Vorstellungen davon, wofür der Staat verantwortlich sein sollte und wofür nicht\. Sagen Sie mir bitte für jede der folgenden Aufgaben auf einer Skala von 0 bis 10, wie sehr der Staat dafür verantwortlich sein sollte\. 0 bedeutet, dass der Staat überhaupt nicht dafür verantwortlich sein sollte und 10 bedeutet, dass er voll und ganz dafür verantwortlich sein sollte\.

**Antwortstamm:** Sollte der Staat erstens dafür verantwortlich sein…

**Originalfrage / Aussage:** …einen angemessenen Lebensstandard für Arbeitslose sicherzustellen?

**Originalinstruktion:** INT\.: LISTE 48 VORLEGEN UND BIS FRAGE E8 LIEGEN LASSEN\. INT\.: BITTE VORLESEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2821**; alle deutschen Studienfälle: 2852; fehlend: 31; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Der Staat sollte dafür überhaupt nicht verantwortlich sein | 0 | 0,957529 |
| 1 | 1 | 1 | 0,358624 |
| 2 | 2 | 2 | 2,470499 |
| 3 | 3 | 3 | 8,311749 |
| 4 | 4 | 4 | 8,785447 |
| 5 | 5 | 5 | 23,806755 |
| 6 | 6 | 6 | 14,021888 |
| 7 | 7 | 7 | 15,430020 |
| 8 | 8 | 8 | 14,344578 |
| 9 | 9 | 9 | 4,126467 |
| 10 | Der Staat sollte dafür voll und ganz verantwortlich sein | 10 | 7,386443 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | Antwort verweigert | 77 |
| 88 | Don&\#x27;t know | Weiß nicht | 88 |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 27 | 28,09451124 |
| No answer | 0 | 0 |
| Refusal | 4 | 4,7537504 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 32,84826164; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,450873; dweight 0,829518; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: The questionnaire table prints 0–9, omitting 10 despite its 0–10 introduction and upper anchor\. Original Liste 48 and the API both include 10; the code is not inferred from a score\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=36): physische PDF\-Seite\(n\) 36; originalQuestionId=E7.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=962d9df9\-c6c6\-459e\-baba\-65fa16802b76; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=49): physische PDF\-Seite\(n\) 49; listLabelDe=Liste 48.

### `ESS8e02_3:gvcldcr` — E8

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_responsibility; Gegenstand: principle.

**Originaleinleitung:** Menschen haben verschiedene Vorstellungen davon, wofür der Staat verantwortlich sein sollte und wofür nicht\. Sagen Sie mir bitte für jede der folgenden Aufgaben auf einer Skala von 0 bis 10, wie sehr der Staat dafür verantwortlich sein sollte\. 0 bedeutet, dass der Staat überhaupt nicht dafür verantwortlich sein sollte und 10 bedeutet, dass er voll und ganz dafür verantwortlich sein sollte\.

**Antwortstamm:** Sollte der Staat erstens dafür verantwortlich sein…

**Originalfrage / Aussage:** …ausreichende Kinderbetreuungsmöglichkeiten für berufstätige Eltern sicherzustellen?

**Originalinstruktion:** INT\.: LISTE 48 VORLEGEN UND BIS FRAGE E8 LIEGEN LASSEN\. INT\.: BITTE VORLESEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2837**; alle deutschen Studienfälle: 2852; fehlend: 15; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Der Staat sollte dafür überhaupt nicht verantwortlich sein | 0 | 0,257218 |
| 1 | 1 | 1 | 0,000000 |
| 2 | 2 | 2 | 0,444753 |
| 3 | 3 | 3 | 1,043053 |
| 4 | 4 | 4 | 1,580483 |
| 5 | 5 | 5 | 4,018106 |
| 6 | 6 | 6 | 3,944668 |
| 7 | 7 | 7 | 10,212946 |
| 8 | 8 | 8 | 24,260739 |
| 9 | 9 | 9 | 18,271182 |
| 10 | Der Staat sollte dafür voll und ganz verantwortlich sein | 10 | 35,966851 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | Antwort verweigert | 77 |
| 88 | Don&\#x27;t know | Weiß nicht | 88 |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 13 | 13,68190651 |
| No answer | 0 | 0 |
| Refusal | 2 | 3,130869 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 16,81277551; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 2,700755; dweight 0,920638; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: The questionnaire table prints 0–9, omitting 10 despite its 0–10 introduction and upper anchor\. Original Liste 48 and the API both include 10; the code is not inferred from a score\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=36): physische PDF\-Seite\(n\) 36; originalQuestionId=E8.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=e07f9665\-727d\-4e02\-90d9\-cc833c1f76d6; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=49): physische PDF\-Seite\(n\) 49; listLabelDe=Liste 48.

### `ESS8e02_3:bnlwinc` — E33

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_support; Gegenstand: measure.

**Originalfrage / Aussage:** Wären Sie dagegen oder dafür, dass nur noch die Personen mit den niedrigsten Einkommen staatliche Sozialleistungen erhalten würden, während Personen mit einem mittleren oder hohen Einkommen auf sich selbst gestellt wären?

**Originalinstruktion:** INT\.: LISTE 53 VORLEGEN UND BIS FRAGE E35 LIEGEN LASSEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2772**; alle deutschen Studienfälle: 2852; fehlend: 80; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dagegen | 1 | 15,533608 |
| 2 | Dagegen | 2 | 45,295734 |
| 3 | Dafür | 3 | 34,301251 |
| 4 | Sehr dafür | 4 | 4,869407 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 75 | 76,53536747 |
| No answer | 0 | 0 |
| Refusal | 5 | 4,7626426 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 81,29801007; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,797643; dweight 1,967407; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=42): physische PDF\-Seite\(n\) 42; originalQuestionId=E33.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=45ff83b1\-9869\-4e52\-944d\-9d41ef7cb451; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=54): physische PDF\-Seite\(n\) 54; listLabelDe=Liste 53.

### `ESS8e02_3:eduunmp` — E34

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_support; Gegenstand: measure.

**Originaleinleitung:** Stellen Sie sich jetzt vor, dass zur Bewältigung der Arbeitslosigkeit eine feste Geldsumme zur Verfügung steht\.

**Originalfrage / Aussage:** Wären Sie dagegen oder dafür, dass der Staat mehr für die Aus\- und Weiterbildung von Arbeitslosen ausgibt, aber dafür weniger Arbeitslosenunterstützung zahlt?

**Originalinstruktion:** INT\.: LISTE 53 VORLEGEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2757**; alle deutschen Studienfälle: 2852; fehlend: 95; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dagegen | 1 | 4,376158 |
| 2 | Dagegen | 2 | 34,979894 |
| 3 | Dafür | 3 | 51,988998 |
| 4 | Sehr dafür | 4 | 8,654950 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 86 | 84,33402326 |
| No answer | 0 | 0 |
| Refusal | 9 | 7,81540677 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 92,14943003; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,594693; dweight 0,785603; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=42): physische PDF\-Seite\(n\) 42; originalQuestionId=E34.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=17a2ea46\-23de\-438c\-80d1\-02d1915d4e26; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=54): physische PDF\-Seite\(n\) 54; listLabelDe=Liste 53.

## Demokratie und politische Autorität

Normative Wichtigkeit für Demokratie im Allgemeinen und die einzelne Regierungsreaktion bei Mehrheitskonflikt sind keine wahrgenommene Umsetzung und keine objektive Demokratiequalität. Kein Populismus- oder Autoritarismuslabel für Personen.

**Inhaltslücken:** Föderalismus, kommunale Mitbestimmung, Parteienfinanzierung und weitere konkrete Machtkonflikte bleiben offen. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS10SCe03_2:fairelc` — B1

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** \.\.\.dass Wahlen zum nationalen Parlament frei und fair sind?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass Wahlen zum nationalen Parlament frei und fair sind?

**Dokumentierte Formabweichung/-gleichheit:** Same substantive wording and anchors; CAWI repeats the shared PAPI stem in the individual question\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8414**; alle deutschen Studienfälle: 8725; fehlend: 311; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 0,905717 |
| 1 | 1 | 1 | 0,145193 |
| 2 | 2 | 2 | 0,439448 |
| 3 | 3 | 3 | 0,566388 |
| 4 | 4 | 4 | 0,935634 |
| 5 | 5 | 5 | 7,643832 |
| 6 | 6 | 6 | 2,320230 |
| 7 | 7 | 7 | 4,192510 |
| 8 | 8 | 8 | 7,838707 |
| 9 | 9 | 9 | 7,805365 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 67,206977 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 311 | 356,7272016 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 356,7272016; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 3,817506; dweight 3,845505; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10; originalQuestionId=B1.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=1d235449\-4271\-46d0\-951f\-c0b50ef9223b; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 137; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B1.

### `ESS10SCe03_2:dfprtal` — B2

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** \.\.\.dass sich die verschiedenen politischen Parteien inhaltlich klar voneinander unterscheiden?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass sich die verschiedenen politischen Parteien inhaltlich klar voneinander unterscheiden?

**Dokumentierte Formabweichung/-gleichheit:** Same substantive wording and anchors; CAWI repeats the shared PAPI stem in the individual question\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8358**; alle deutschen Studienfälle: 8725; fehlend: 367; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 2,755530 |
| 1 | 1 | 1 | 0,466244 |
| 2 | 2 | 2 | 2,048307 |
| 3 | 3 | 3 | 2,892045 |
| 4 | 4 | 4 | 2,571723 |
| 5 | 5 | 5 | 15,823833 |
| 6 | 6 | 6 | 9,123427 |
| 7 | 7 | 7 | 15,980443 |
| 8 | 8 | 8 | 17,553553 |
| 9 | 9 | 9 | 7,216830 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 23,568066 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 367 | 423,67997024 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 423,67997024; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,290668; dweight 1,280132; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10; originalQuestionId=B2.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=548ea0d0\-6b88\-4ef1\-ac64\-077e4732cb0c; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 138; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B2.

### `ESS10SCe03_2:medcrgv` — B3

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die Medien das Recht haben, Kritik an der Regierung zu üben?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die Medien das Recht haben, Kritik an der Regierung zu üben?

**Dokumentierte Formabweichung/-gleichheit:** CAWI repeats the full shared PAPI B1–B12 stem in the individual question, including &quot;für die Demokratie im Allgemeinen&quot;; no omission of this phrase is present on physical PDF page 139\. PAPI presents the shared stem and ellipsis\-prefixed item separately; CAWI joins them into one question\. Both full response anchors remain explicit\. Static wording correspondence only; no empirical mode\-equivalence claim\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8459**; alle deutschen Studienfälle: 8725; fehlend: 266; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 1,056176 |
| 1 | 1 | 1 | 0,246209 |
| 2 | 2 | 2 | 0,470148 |
| 3 | 3 | 3 | 0,700729 |
| 4 | 4 | 4 | 0,920768 |
| 5 | 5 | 5 | 7,525226 |
| 6 | 6 | 6 | 3,477835 |
| 7 | 7 | 7 | 7,538992 |
| 8 | 8 | 8 | 13,406794 |
| 9 | 9 | 9 | 9,885726 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 54,771398 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 266 | 302,5594856 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 302,5594856; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 2,528520; dweight 2,505113; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B3.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=e397b55d\-0313\-4c81\-a221\-c8e907ba976c; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 139; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B3.

### `ESS10SCe03_2:rghmgpr` — B4

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die Rechte von Minderheiten geschützt werden?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die Rechte von Minderheiten geschützt werden?

**Dokumentierte Formabweichung/-gleichheit:** CAWI repeats the full shared PAPI B1–B12 stem in the individual question, including &quot;für die Demokratie im Allgemeinen&quot;; no omission of this phrase is present on physical PDF page 140\. PAPI presents the shared stem and ellipsis\-prefixed item separately; CAWI joins them into one question\. Both full response anchors remain explicit\. Static wording correspondence only; no empirical mode\-equivalence claim\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8403**; alle deutschen Studienfälle: 8725; fehlend: 322; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 0,720369 |
| 1 | 1 | 1 | 0,256803 |
| 2 | 2 | 2 | 0,872339 |
| 3 | 3 | 3 | 1,238332 |
| 4 | 4 | 4 | 1,745440 |
| 5 | 5 | 5 | 9,170440 |
| 6 | 6 | 6 | 4,893639 |
| 7 | 7 | 7 | 8,991114 |
| 8 | 8 | 8 | 16,122583 |
| 9 | 9 | 9 | 11,237237 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 44,751705 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 322 | 371,4958802 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 371,4958802; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,731694; dweight 1,758292; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B4.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=ab67a489\-9972\-45a4\-a485\-2e207c744e15; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 140; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B4.

### `ESS10SCe03_2:votedir` — B5

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die Bürger bei den wichtigsten politischen Sachfragen durch direkte Volksabstimmungen das letzte Wort haben?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die Bürger bei den wichtigsten politischen Sachfragen durch direkte Volksabstimmungen das letzte Wort haben?

**Dokumentierte Formabweichung/-gleichheit:** CAWI repeats the full shared PAPI B1–B12 stem in the individual question, including &quot;für die Demokratie im Allgemeinen&quot;; no omission of this phrase is present on physical PDF page 141\. PAPI presents the shared stem and ellipsis\-prefixed item separately; CAWI joins them into one question\. Both full response anchors remain explicit\. Static wording correspondence only; no empirical mode\-equivalence claim\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8408**; alle deutschen Studienfälle: 8725; fehlend: 317; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 1,893621 |
| 1 | 1 | 1 | 0,883709 |
| 2 | 2 | 2 | 2,293969 |
| 3 | 3 | 3 | 3,077896 |
| 4 | 4 | 4 | 2,537886 |
| 5 | 5 | 5 | 11,313267 |
| 6 | 6 | 6 | 6,773244 |
| 7 | 7 | 7 | 11,940698 |
| 8 | 8 | 8 | 17,700335 |
| 9 | 9 | 9 | 10,130628 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 31,454746 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 317 | 365,82096013 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 365,82096013; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,709266; dweight 1,730528; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B5.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=9f85c3fe\-97f1\-473b\-ad14\-7b601058f825; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 141; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B5.

### `ESS10SCe03_2:cttresa` — B6

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die Gerichte alle Menschen gleich behandeln?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die Gerichte alle Menschen gleich behandeln?

**Dokumentierte Formabweichung/-gleichheit:** CAWI repeats the full shared PAPI B1–B12 stem in the individual question, including &quot;für die Demokratie im Allgemeinen&quot;; no omission of this phrase is present on physical PDF page 142\. PAPI presents the shared stem and ellipsis\-prefixed item separately; CAWI joins them into one question\. Both full response anchors remain explicit\. Static wording correspondence only; no empirical mode\-equivalence claim\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Weiterhin nicht freigegeben:** `withheld_base_or_cell_count`. Keine Zahlenreferenz. Null bedeutet keine verfügbare Referenz und niemals einen Anteil von null.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | keine Referenz |
| 1 | 1 | 1 | keine Referenz |
| 2 | 2 | 2 | keine Referenz |
| 3 | 3 | 3 | keine Referenz |
| 4 | 4 | 4 | keine Referenz |
| 5 | 5 | 5 | keine Referenz |
| 6 | 6 | 6 | keine Referenz |
| 7 | 7 | 7 | keine Referenz |
| 8 | 8 | 8 | keine Referenz |
| 9 | 9 | 9 | keine Referenz |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | keine Referenz |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B6.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=4206c15f\-6ea3\-4beb\-a289\-781e472ba908; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 142; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B6.

### `ESS10SCe03_2:gptpelc` — B7

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass Regierungsparteien bei Wahlen abgestraft werden, wenn sie schlechte Arbeit geleistet haben?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass Regierungsparteien bei Wahlen abgestraft werden, wenn sie schlechte Arbeit geleistet haben?

**Dokumentierte Formabweichung/-gleichheit:** CAWI repeats the full shared PAPI B1–B12 stem in the individual question, including &quot;für die Demokratie im Allgemeinen&quot;; no omission of this phrase is present on physical PDF page 143\. PAPI presents the shared stem and ellipsis\-prefixed item separately; CAWI joins them into one question\. Both full response anchors remain explicit\. Static wording correspondence only; no empirical mode\-equivalence claim\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8315**; alle deutschen Studienfälle: 8725; fehlend: 410; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 1,374780 |
| 1 | 1 | 1 | 0,390956 |
| 2 | 2 | 2 | 1,390832 |
| 3 | 3 | 3 | 1,772670 |
| 4 | 4 | 4 | 2,087656 |
| 5 | 5 | 5 | 10,884063 |
| 6 | 6 | 6 | 6,515876 |
| 7 | 7 | 7 | 9,729479 |
| 8 | 8 | 8 | 18,229904 |
| 9 | 9 | 9 | 11,540043 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 36,083742 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 410 | 463,03377012 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 463,03377012; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,745758; dweight 0,740982; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B7.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=c254ddab\-31e3\-42d3\-b3ec\-ac5098729ed2; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 143; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B7.

### `ESS10SCe03_2:gvctzpv` — B8

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die Regierung alle Bürger vor Armut schützt?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die Regierung alle Bürger vor Armut schützt?

**Dokumentierte Formabweichung/-gleichheit:** Same substantive wording and anchors; CAWI repeats the shared PAPI stem in the individual question\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8466**; alle deutschen Studienfälle: 8725; fehlend: 259; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 0,974033 |
| 1 | 1 | 1 | 0,232046 |
| 2 | 2 | 2 | 1,144753 |
| 3 | 3 | 3 | 1,991619 |
| 4 | 4 | 4 | 1,652720 |
| 5 | 5 | 5 | 7,334949 |
| 6 | 6 | 6 | 5,540363 |
| 7 | 7 | 7 | 10,403250 |
| 8 | 8 | 8 | 17,116056 |
| 9 | 9 | 9 | 11,487900 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 42,122311 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 259 | 283,58370682 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 283,58370682; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 2,103412; dweight 2,097965; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B8.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=2184a764\-e849\-45a2\-87cc\-9d999b14c074; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 144; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B8.

### `ESS10SCe03_2:grdfinc` — B9

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die Regierung Maßnahmen ergreift, um Einkommensunterschiede zu verringern?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die Regierung Maßnahmen ergreift, um Einkommensunterschiede zu verringern?

**Dokumentierte Formabweichung/-gleichheit:** Same substantive wording and anchors; CAWI repeats the shared PAPI stem in the individual question\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8428**; alle deutschen Studienfälle: 8725; fehlend: 297; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 2,409358 |
| 1 | 1 | 1 | 0,902063 |
| 2 | 2 | 2 | 2,554891 |
| 3 | 3 | 3 | 3,628579 |
| 4 | 4 | 4 | 3,164363 |
| 5 | 5 | 5 | 12,484370 |
| 6 | 6 | 6 | 8,891946 |
| 7 | 7 | 7 | 12,480496 |
| 8 | 8 | 8 | 17,617764 |
| 9 | 9 | 9 | 7,502159 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 28,364011 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 297 | 333,85220274 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 333,85220274; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,845264; dweight 1,849799; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B9.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=d363ff5c\-6b5c\-4e8a\-892d\-be07cbac1bd3; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 145; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B9.

### `ESS10SCe03_2:viepol` — B10

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die Ansichten gewöhnlicher Menschen Vorrang vor den Ansichten der politischen Elite haben?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die Ansichten gewöhnlicher Menschen Vorrang vor den Ansichten der politischen Elite haben?

**Dokumentierte Formabweichung/-gleichheit:** CAWI repeats the full shared PAPI B1–B12 stem in the individual question, including &quot;für die Demokratie im Allgemeinen&quot;; no omission of this phrase is present on physical PDF page 146\. PAPI presents the shared stem and ellipsis\-prefixed item separately; CAWI joins them into one question\. Both full response anchors remain explicit\. Static wording correspondence only; no empirical mode\-equivalence claim\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8163**; alle deutschen Studienfälle: 8725; fehlend: 562; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 3,973486 |
| 1 | 1 | 1 | 0,672340 |
| 2 | 2 | 2 | 2,264415 |
| 3 | 3 | 3 | 2,842873 |
| 4 | 4 | 4 | 2,985422 |
| 5 | 5 | 5 | 24,705674 |
| 6 | 6 | 6 | 8,887116 |
| 7 | 7 | 7 | 12,220345 |
| 8 | 8 | 8 | 14,987826 |
| 9 | 9 | 9 | 7,429204 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 19,031299 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 562 | 620,95388399 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 620,95388399; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,451977; dweight 1,477691; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B10.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=965a4991\-2cb5\-4979\-8ecf\-3db042a96065; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 146; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B10.

### `ESS10SCe03_2:wpestop` — B11

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass sich der Wille des Volkes immer durchsetzt?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass sich der Wille des Volkes immer durchsetzt?

**Dokumentierte Formabweichung/-gleichheit:** Same substantive wording and anchors; CAWI repeats the shared PAPI stem in the individual question\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8331**; alle deutschen Studienfälle: 8725; fehlend: 394; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 1,338356 |
| 1 | 1 | 1 | 0,387172 |
| 2 | 2 | 2 | 1,190988 |
| 3 | 3 | 3 | 2,774623 |
| 4 | 4 | 4 | 3,147614 |
| 5 | 5 | 5 | 17,077429 |
| 6 | 6 | 6 | 9,576423 |
| 7 | 7 | 7 | 13,997838 |
| 8 | 8 | 8 | 18,334910 |
| 9 | 9 | 9 | 9,405413 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 22,769234 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 394 | 422,41643007 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 422,41643007; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,043150; dweight 1,039032; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B11.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=8483ef44\-33de\-481e\-b5db\-280ef9787252; sourceFieldMetadataVersion=2; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 147; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B11.

### `ESS10SCe03_2:scchpldm` — B25

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: nominal; Gegenstand: principle.

**Originaleinleitung:** Manchmal ist die Regierung anderer Meinung als die große Mehrheit der Bevölkerung, wenn es darum geht, was für das Land am besten ist\.

**Originalfrage / Aussage:** Welche der beiden Aussagen auf dieser Liste beschreibt, was aus Ihrer Sicht für die Demokratie im Allgemeinen am besten ist?

**Originalinstruktion:** Bitte markieren Sie nur ein Kästchen\.

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Manchmal ist die Regierung anderer Meinung als die große Mehrheit der Bevölkerung, wenn es darum geht, was für das Land am besten ist\.

**CAWI-Originalfrage:** Welche der beiden Aussagen beschreibt, was aus Ihrer Sicht für die Demokratie im Allgemeinen am besten ist?

**Dokumentierte Formabweichung/-gleichheit:** CAWI omits &quot;auf dieser Liste&quot;, the paper\-only single\-box instruction and printed jump arrows\. Same two alternatives, with no terminal period in the displayed CAWI labels\.

**Originalrouting:** PAPI answer 1 → B26; answer 2 → B28 on page 13\.

B25 ist ausschließlich als statische historische Einzelfrage gebunden. PAPI: Antwort 1 → B26 (PDF12), Antwort 2 → B28 (PDF13). B26–B29 fehlen in der Auswahl. Die CAWI-Seite PDF162 belegt keinen operativen bedingten Nachlauf. Eine neue Webfolge zur nächsten ausgewählten Frage bleibt unvalidiert und benötigt menschliche Gestaltung und Verständnisprüfung; keine Originaladministrationsäquivalenz.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8118**; alle deutschen Studienfälle: 8725; fehlend: 607; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Die Regierung sollte ihre Pläne ändern und darauf reagieren, was die große Mehrheit der Bevölkerung denkt\. | 1 | 89,142198 |
| 2 | Die Regierung sollte an ihren Plänen festhalten \- unabhängig davon, was die große Mehrheit der Bevölkerung denkt\. | 2 | 10,857802 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 1 | Die Regierung sollte ihre Pläne ändern und darauf reagieren, was die große Mehrheit der Bevölkerung denkt | keiner gedruckt |
| 2 | Die Regierung sollte an ihren Plänen festhalten \- unabhängig davon, was die große Mehrheit der Bevölkerung denkt | keiner gedruckt |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| No answer | 607 | 632,61430296 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 632,61430296; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,041681; dweight 1,052039; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Original PAPI B25 routes answer 1 to B26 below on physical PDF page 12 and answer 2 to B28 on page 13\. B26–B29 are deliberately absent from the fixed draft\. The open limitation concerns original follow\-up reproduction or approval of a new web administration\. Static B25 wording/categories and a separate historical B25 reference remain distinct tasks; no reproduced administration, empirical validity or publication approval is certified\. API declares only 9 No answer as missing\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=12): physische PDF\-Seite\(n\) 12; originalQuestionId=B25.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=ab1b6274\-a3bf\-4586\-ac6c\-ca462eb07a96; sourceFieldMetadataVersion=3; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=162): physische PDF\-Seite\(n\) 162; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B25.

## Bürgerrechte und Sicherheit

Pflichtgefühl gegenüber Polizei, Strafverschärfung und Rechtsbindung sind einzelne historische Gegenstände. Bei härteren Strafen bezeichnet ‚heute‘ den damaligen Kontext 2010/2011.

**Inhaltslücken:** Digitale Überwachung, Datenschutz, konkrete Sicherheitsanlässe und Strafverfahrensgarantien sind nicht umfassend enthalten. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS5e03_6:bplcdc` — D18

Quelle: ESS5e03\_6, Ausgabe 3\.6. Antwortform: ordered\_obligation; Gegenstand: principle.

**Originaleinleitung:** Und nun ein paar Fragen zu Ihren Pflichten, die Sie gegenüber der Polizei in Deutschland haben\. Benutzen Sie Liste 33\. 0 bedeutet &quot;überhaupt nicht meine Pflicht&quot; und 10 &quot;voll und ganz meine Pflicht&quot;\.

**Antwortstamm:** In welchem Ausmaß betrachten Sie es als Ihre Pflicht\.\.\.

**Originalfrage / Aussage:** \.\.\.\.die Entscheidungen der Polizei zu akzeptieren, auch wenn Sie damit nicht einverstanden sind?

**Originalinstruktion:** INT\.: BITTE VORLESEN

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **3000**; alle deutschen Studienfälle: 3031; fehlend: 31; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 0 | 5,197813 |
| 1 | 1 | 1 | 1,300746 |
| 2 | 2 | 2 | 3,201017 |
| 3 | 3 | 3 | 4,501459 |
| 4 | 4 | 4 | 4,687201 |
| 5 | 5 | 5 | 14,095420 |
| 6 | 6 | 6 | 8,072538 |
| 7 | 7 | 7 | 13,023386 |
| 8 | 8 | 8 | 19,221545 |
| 9 | 9 | 9 | 9,286777 |
| 10 | Voll und ganz meine Pflicht | 10 | 17,412099 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | Weiß nicht | 98 |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 31 | 41,23935771 |
| No answer | 0 | 0 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 41,23935771; primäre Gewichtssumme aller deutschen Studienfälle: 3030,99999773. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,513223; dweight 0,468163; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,33519029291, Maximum 2,33519078289; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: The original block also contains D19, which is outside this fixed draft; originalOrderInGroup retains the gap\. Printed Weiß nicht=98 maps to API 88; API also declares 77 Refusal and 99 No answer\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=24): physische PDF\-Seite\(n\) 24; originalQuestionId=D18.

[ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=73c3aeb5\-3281\-47ef\-b23f\-46f648815110; sourceFieldMetadataVersion=2; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

### `ESS5e03_6:dpcstrb` — D20

Quelle: ESS5e03\_6, Ausgabe 3\.6. Antwortform: ordered\_obligation; Gegenstand: principle.

**Originaleinleitung:** Und nun ein paar Fragen zu Ihren Pflichten, die Sie gegenüber der Polizei in Deutschland haben\. Benutzen Sie Liste 33\. 0 bedeutet &quot;überhaupt nicht meine Pflicht&quot; und 10 &quot;voll und ganz meine Pflicht&quot;\.

**Antwortstamm:** In welchem Ausmaß betrachten Sie es als Ihre Pflicht\.\.\.

**Originalfrage / Aussage:** \.\.\.\.zu tun, was die Polizei Ihnen sagt, auch wenn Sie die Art und Weise, wie die Polizei Sie behandelt, nicht gut finden?

**Originalinstruktion:** INT\.: BITTE VORLESEN

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2977**; alle deutschen Studienfälle: 3031; fehlend: 54; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 0 | 3,272497 |
| 1 | 1 | 1 | 1,313455 |
| 2 | 2 | 2 | 4,044556 |
| 3 | 3 | 3 | 6,360588 |
| 4 | 4 | 4 | 7,064620 |
| 5 | 5 | 5 | 16,645189 |
| 6 | 6 | 6 | 10,085152 |
| 7 | 7 | 7 | 14,027014 |
| 8 | 8 | 8 | 15,713557 |
| 9 | 9 | 9 | 8,167322 |
| 10 | Voll und ganz meine Pflicht | 10 | 13,306051 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | Weiß nicht | 98 |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 54 | 64,56130598 |
| No answer | 0 | 0 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 64,56130598; primäre Gewichtssumme aller deutschen Studienfälle: 3030,99999773. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,880330; dweight 0,503673; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,33519029291, Maximum 2,33519078289; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: The original block also contains D19, which is outside this fixed draft; originalOrderInGroup retains the gap\. Printed Weiß nicht=98 maps to API 88; API also declares 77 Refusal and 99 No answer\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=24): physische PDF\-Seite\(n\) 24, 25; originalQuestionId=D20.

[ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=6fb0f716\-95a9\-43d4\-8d9e\-044e9c25462a; sourceFieldMetadataVersion=2; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

### `ESS5e03_6:hrshsnta` — D33

Quelle: ESS5e03\_6, Ausgabe 3\.6. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Benutzen Sie Liste 41 und sagen Sie mir bitte, wie sehr Sie den folgenden Aussagen über Deutschland heute zustimmen oder wie sehr Sie diese ablehnen\.

**Originalfrage / Aussage:** Menschen, die das Gesetz brechen, sollten viel härter bestraft werden, als sie heute bestraft werden\.

**Originalinstruktion:** INT: BITTE JEDE AUSSAGE VORLESEN UND ANTWORT EINTRAGEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2947**; alle deutschen Studienfälle: 3031; fehlend: 84; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | stimme stark zu | 1 | 18,251231 |
| 2 | stimme zu | 2 | 43,386312 |
| 3 | weder noch | 3 | 24,170214 |
| 4 | lehne ab | 4 | 11,934650 |
| 5 | lehne stark ab | 5 | 2,257593 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 84 | 99,38760742 |
| No answer | 0 | 0 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 99,38760742; primäre Gewichtssumme aller deutschen Studienfälle: 3030,99999773. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,896009; dweight 0,692187; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,33519029291, Maximum 2,33519078289; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Original matrix D32–D37 includes adjacent items outside this fixed draft\. &quot;Deutschland heute&quot; is the original 2010/11 context, not a contemporary website\-validity claim\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D33.

[ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=fc7ed212\-da9f\-4e06\-a918\-43d6757dd3cc; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

### `ESS5e03_6:dbctvrd` — D34

Quelle: ESS5e03\_6, Ausgabe 3\.6. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Benutzen Sie Liste 41 und sagen Sie mir bitte, wie sehr Sie den folgenden Aussagen über Deutschland heute zustimmen oder wie sehr Sie diese ablehnen\.

**Originalfrage / Aussage:** Alle haben die Pflicht, ein abschließendes Gerichtsurteil zu akzeptieren\.

**Originalinstruktion:** INT: BITTE JEDE AUSSAGE VORLESEN UND ANTWORT EINTRAGEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2993**; alle deutschen Studienfälle: 3031; fehlend: 38; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | stimme stark zu | 1 | 12,804673 |
| 2 | stimme zu | 2 | 48,195350 |
| 3 | weder noch | 3 | 15,544837 |
| 4 | lehne ab | 4 | 19,623834 |
| 5 | lehne stark ab | 5 | 3,831306 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 38 | 43,7543185 |
| No answer | 0 | 0 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 43,7543185; primäre Gewichtssumme aller deutschen Studienfälle: 3030,99999773. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,757054; dweight 0,306463; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,33519029291, Maximum 2,33519078289; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Original matrix D32–D37 includes adjacent items outside this fixed draft\. &quot;Deutschland heute&quot; is the original 2010/11 context, not a contemporary website\-validity claim\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D34.

[ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=1f210987\-0fca\-4fbe\-aaef\-2ad611f0bad1; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

### `ESS5e03_6:lwstrob` — D35

Quelle: ESS5e03\_6, Ausgabe 3\.6. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Benutzen Sie Liste 41 und sagen Sie mir bitte, wie sehr Sie den folgenden Aussagen über Deutschland heute zustimmen oder wie sehr Sie diese ablehnen\.

**Originalfrage / Aussage:** Alle Gesetze müssen strikt befolgt werden\.

**Originalinstruktion:** INT: BITTE JEDE AUSSAGE VORLESEN UND ANTWORT EINTRAGEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **3013**; alle deutschen Studienfälle: 3031; fehlend: 18; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | stimme stark zu | 1 | 15,669069 |
| 2 | stimme zu | 2 | 57,872748 |
| 3 | weder noch | 3 | 15,224297 |
| 4 | lehne ab | 4 | 9,773788 |
| 5 | lehne stark ab | 5 | 1,460098 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 18 | 20,28924403 |
| No answer | 0 | 0 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 20,28924403; primäre Gewichtssumme aller deutschen Studienfälle: 3030,99999773. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,540793; dweight 0,682876; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,33519029291, Maximum 2,33519078289; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Original matrix D32–D37 includes adjacent items outside this fixed draft\. &quot;Deutschland heute&quot; is the original 2010/11 context, not a contemporary website\-validity claim\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D35.

[ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=955e2117\-2b74\-4632\-aba9\-0338fbff655f; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

### `ESS5e03_6:rgbrklw` — D36

Quelle: ESS5e03\_6, Ausgabe 3\.6. Antwortform: ordered\_agreement; Gegenstand: principle.

**Originaleinleitung:** Benutzen Sie Liste 41 und sagen Sie mir bitte, wie sehr Sie den folgenden Aussagen über Deutschland heute zustimmen oder wie sehr Sie diese ablehnen\.

**Originalfrage / Aussage:** Manchmal muss man das Gesetz brechen, um das Richtige zu tun\.

**Originalinstruktion:** INT: BITTE JEDE AUSSAGE VORLESEN UND ANTWORT EINTRAGEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2922**; alle deutschen Studienfälle: 3031; fehlend: 109; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | stimme stark zu | 1 | 6,259541 |
| 2 | stimme zu | 2 | 43,377585 |
| 3 | weder noch | 3 | 19,209689 |
| 4 | lehne ab | 4 | 24,243095 |
| 5 | lehne stark ab | 5 | 6,910091 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 109 | 129,49996084 |
| No answer | 0 | 0 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 129,49996084; primäre Gewichtssumme aller deutschen Studienfälle: 3030,99999773. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,872929; dweight 0,610029; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,33519029291, Maximum 2,33519078289; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Original matrix D32–D37 includes adjacent items outside this fixed draft\. &quot;Deutschland heute&quot; is the original 2010/11 context, not a contemporary website\-validity claim\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D36.

[ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=d6c06eff\-700d\-438b\-ae82\-92f0238328c4; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

## Europäische Integration

Mitgliedschaftsszenario, nationale Zuständigkeit als Demokratieprinzip und Integrationsumfang bleiben getrennt. Leerer/ungültiger Stimmzettel, Nichtwahl und Nichtstimmberechtigung sind gültige Originaloptionen, keine politische Mitte und kein EU-Gesamtscore.

**Inhaltslücken:** Gemeinsame Fiskal-, Sozial- und Außenpolitik sowie institutionelle Gestaltung und Solidarität sind unvollständig. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS10SCe03_2:vteurmmb` — A90

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: nominal; Gegenstand: principle.

**Originaleinleitung:** Stellen Sie sich vor, morgen würde eine Volksabstimmung in Deutschland über die Mitgliedschaft in der Europäischen Union stattfinden\.

**Originalfrage / Aussage:** Würden Sie für die Fortsetzung der Mitgliedschaft Deutschlands in der Europäischen Union oder für einen Austritt Deutschlands aus der Europäischen Union stimmen?

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Stellen Sie sich vor, morgen würde eine Volksabstimmung in Deutschland über die Mitgliedschaft in der Europäischen Union stattfinden\.

**CAWI-Originalfrage:** Würden Sie für die Fortsetzung der Mitgliedschaft Deutschlands in der Europäischen Union oder für einen Austritt Deutschlands aus der Europäischen Union stimmen?

**Dokumentierte Formabweichung/-gleichheit:** Same six labels and scenario\. CAWI radios display no numeric codes; export 33/44/55/65 must not be replaced by visual ordinal positions\.

**Originalrouting:** PAPI A87 option 6 routes directly to A90; other A87 answers pass A88/A89 before A90\. No eligibility filter printed at A90; answer 6 Nicht stimmberechtigt is offered\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8389**; alle deutschen Studienfälle: 8725; fehlend: 336; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Fortsetzung der Mitgliedschaft in der Europäischen Union | 1 | 77,040226 |
| 2 | Austritt aus der Europäischen Union | 2 | 9,544770 |
| 33 | Würde einen leeren Stimmzettel abgeben | 3 | 3,443446 |
| 44 | Würde ungültig wählen | 4 | 1,218798 |
| 55 | Würde nicht wählen | 5 | 4,380817 |
| 65 | Nicht stimmberechtigt | 6 | 4,371942 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 1 | Fortsetzung der Mitgliedschaft in der Europäischen Union | keiner gedruckt |
| 2 | Austritt aus der Europäischen Union | keiner gedruckt |
| 33 | Würde einen leeren Stimmzettel abgeben | keiner gedruckt |
| 44 | Würde ungültig wählen | keiner gedruckt |
| 55 | Würde nicht wählen | keiner gedruckt |
| 65 | Nicht stimmberechtigt | keiner gedruckt |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 336 | 374,00364272 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 374,00364272; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 3,720294; dweight 3,716425; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: PAPI printed 1/2/3/4/5/6 maps to file 1/2/33/44/55/65\. 55 is non\-voting and 65 is ineligibility; neither is a remain/leave position\. API explicitly treats all six as valid \(isMissing=false\)\. 65 is an offered ineligibility response, not proof of a skipped/not\-asked item; notAskedCodes stays empty\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10; originalQuestionId=A90.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=9ef51a31\-8a4f\-4f70\-9034\-fa76a3517ffc; sourceFieldMetadataVersion=7; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=135): physische PDF\-Seite\(n\) 135; originalForm=CAWI screenshots; contentCorrespondenceToPapi=A90.

### `ESS10SCe03_2:keydec` — B12

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_importance; Gegenstand: principle.

**Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**Antwortstamm:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist,…

**Originalfrage / Aussage:** …dass die wichtigsten Entscheidungen von den nationalen Regierungen getroffen werden und nicht von der Europäischen Union?

**Originalinstruktion:** B1\-12

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Nun einige Fragen zur Demokratie\. Nachher werden wir Sie fragen, wie die Demokratie in Deutschland funktioniert, zunächst möchten wir Sie aber bitten, darüber nachzudenken, wie wichtig aus Ihrer Sicht bestimmte Dinge für die Demokratie im Allgemeinen sind\.

**CAWI-Originalfrage:** Bitte geben Sie an, wie wichtig es aus Ihrer Sicht für die Demokratie im Allgemeinen ist, dass die wichtigsten Entscheidungen von den nationalen Regierungen getroffen werden und nicht von der Europäischen Union?

**Dokumentierte Formabweichung/-gleichheit:** Same substantive wording and anchors; CAWI repeats the shared PAPI stem in the individual question\.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8247**; alle deutschen Studienfälle: 8725; fehlend: 478; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 | 2,018849 |
| 1 | 1 | 1 | 0,620768 |
| 2 | 2 | 2 | 2,527423 |
| 3 | 3 | 3 | 3,505007 |
| 4 | 4 | 4 | 2,531131 |
| 5 | 5 | 5 | 19,395190 |
| 6 | 6 | 6 | 8,585386 |
| 7 | 7 | 7 | 12,701026 |
| 8 | 8 | 8 | 17,684455 |
| 9 | 9 | 9 | 8,943189 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 | 21,487577 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 0 | Überhaupt nicht wichtig für die Demokratie im Allgemeinen | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Äußerst wichtig für die Demokratie im Allgemeinen | 10 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 88 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 478 | 544,41022453 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 544,41022453; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,504553; dweight 1,528861; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Importance for democracy in general: not a report on democratic performance in Germany\. Full B1–B12 order and shared lead\-in retained\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=10): physische PDF\-Seite\(n\) 10, 11; originalQuestionId=B12.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=b3717bf9\-0cdb\-42ef\-a605\-c1096077a050; sourceFieldMetadataVersion=3; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=136): physische PDF\-Seite\(n\) 136, 148; originalForm=CAWI screenshots; contentCorrespondenceToPapi=B12.

### `ESS11e04_2:euftf` — B37

Quelle: ESS11e04\_2, Ausgabe 4\.2. Antwortform: ordered\_direction; Gegenstand: principle.

**Originaleinleitung:** Jetzt kommen wir zum Thema Europäische Union\. Manche Leute sagen, dass die europäische Einigung weiter gehen soll\. Andere sagen, dass sie schon jetzt zu weit gegangen ist\.

**Originalfrage / Aussage:** Welche Zahl der Skala auf Liste 14 beschreibt Ihre Einschätzung am besten?

**Originalinstruktion:** LISTE 14

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2360**; alle deutschen Studienfälle: 2420; fehlend: 60; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 0 | Einigung ist schon zu weit gegangen | 00 | 4,842340 |
| 1 | 1 | 01 | 1,832382 |
| 2 | 2 | 02 | 6,131495 |
| 3 | 3 | 03 | 5,360916 |
| 4 | 4 | 04 | 6,232469 |
| 5 | 5 | 05 | 21,845681 |
| 6 | 6 | 06 | 9,458164 |
| 7 | 7 | 07 | 12,280719 |
| 8 | 8 | 08 | 14,932335 |
| 9 | 9 | 09 | 5,959529 |
| 10 | Einigung sollte weitergehen | 10 | 11,123971 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 77 | Refusal | Antwort verweigert | 77 |
| 88 | Don&\#x27;t know | Weiß nicht | 88 |
| 99 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 54 | 77,4399292916 |
| No answer | 0 | 0 |
| Refusal | 6 | 3,44067172706 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 80,8806010187; primäre Gewichtssumme aller deutschen Studienfälle: 2419,99996939. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,972800; dweight 1,949776; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,992969752, Maximum 2,992969752; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: DE zeigt 00–10, API 0–10 ohne führende Null; API ergänzt 99 No answer\. Code 9 ist hier regulär, nicht Missing\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess11\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf#page=14): physische PDF\-Seite\(n\) 14; originalQuestionId=B37.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=73d580d0\-d947\-43c0\-8697\-955308e5f774; sourceFieldMetadataVersion=1; dataFileMetadataId=242aaa39\-3bbb\-40f5\-98bf\-bfb1ce53d8ef; dataFileMetadataVersion=179.

## Klima und Energie

Drei konkrete Instrumente: fossile Abgabe, Erneuerbarenförderung und Verkaufsverbot. Unterstützung eines Instruments bedeutet keine gesamte Energieposition.

**Inhaltslücken:** Versorgungssicherheit, Netze, Speicher und Energieträgerwahl bleiben offen. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS8e02_3:inctxff` — D30

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_support; Gegenstand: measure.

**Originaleinleitung:** Wie sehr sind Sie für oder gegen die folgenden Maßnahmen in Deutschland zur Reduzierung des Klimawandels?

**Originalfrage / Aussage:** Erhöhung der Abgaben auf fossile Brennstoffe wie Öl, Gas und Kohle\.

**Originalinstruktion:** INT\.: BITTE LISTE 44 VORLEGEN\. INT\.: BITTE VORLESEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2814**; alle deutschen Studienfälle: 2852; fehlend: 38; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dafür | 1 | 8,867298 |
| 2 | Eher dafür | 2 | 29,388720 |
| 3 | Weder dafür noch dagegen | 3 | 24,207853 |
| 4 | Eher dagegen | 4 | 28,445499 |
| 5 | Sehr dagegen | 5 | 9,090630 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 34 | 43,70013839 |
| No answer | 0 | 0 |
| Refusal | 4 | 4,40090245 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 48,10104084; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,250522; dweight 0,931934; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=33): physische PDF\-Seite\(n\) 33; originalQuestionId=D30.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=d5cf7d14\-16c1\-42b7\-883b\-1f894d883fa9; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=45): physische PDF\-Seite\(n\) 45; listLabelDe=Liste 44.

### `ESS8e02_3:sbsrnen` — D31

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_support; Gegenstand: measure.

**Originaleinleitung:** Wie sehr sind Sie für oder gegen die folgenden Maßnahmen in Deutschland zur Reduzierung des Klimawandels?

**Originalfrage / Aussage:** Verwendung öffentlicher Gelder zur Förderung erneuerbarer Energiequellen wie Wind\- oder Sonnenenergie\.

**Originalinstruktion:** INT\.: BITTE LISTE 44 VORLEGEN\. INT\.: BITTE VORLESEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2826**; alle deutschen Studienfälle: 2852; fehlend: 26; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dafür | 1 | 39,129085 |
| 2 | Eher dafür | 2 | 46,292220 |
| 3 | Weder dafür noch dagegen | 3 | 6,651349 |
| 4 | Eher dagegen | 4 | 5,778983 |
| 5 | Sehr dagegen | 5 | 2,148363 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 21 | 25,37707929 |
| No answer | 0 | 0 |
| Refusal | 5 | 4,97097555 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 30,34805484; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,337153; dweight 0,198567; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=33): physische PDF\-Seite\(n\) 33; originalQuestionId=D31.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=63374869\-47d9\-466e\-8478\-28e5df0fcaea; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=45): physische PDF\-Seite\(n\) 45; listLabelDe=Liste 44.

### `ESS8e02_3:banhhap` — D32

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_support; Gegenstand: measure.

**Originaleinleitung:** Wie sehr sind Sie für oder gegen die folgenden Maßnahmen in Deutschland zur Reduzierung des Klimawandels?

**Originalfrage / Aussage:** Ein gesetzliches Verbot für den Verkauf von Haushaltgeräten mit der schlechtesten Energieeffizienz\.

**Originalinstruktion:** INT\.: BITTE LISTE 44 VORLEGEN\. INT\.: BITTE VORLESEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2828**; alle deutschen Studienfälle: 2852; fehlend: 24; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dafür | 1 | 35,204944 |
| 2 | Eher dafür | 2 | 33,872496 |
| 3 | Weder dafür noch dagegen | 3 | 13,718261 |
| 4 | Eher dagegen | 4 | 13,017479 |
| 5 | Sehr dagegen | 5 | 4,186819 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 20 | 23,65970939 |
| No answer | 0 | 0 |
| Refusal | 4 | 3,69755975 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 27,35726914; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,303954; dweight 0,540618; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=33): physische PDF\-Seite\(n\) 33; originalQuestionId=D32.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=c8bdf3e2\-f614\-4608\-bc3f\-b1f9a680898b; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=45): physische PDF\-Seite\(n\) 45; listLabelDe=Liste 44.

## Migration

Zulassungsumfang für die ausdrücklich genannten Gruppen und Bedingungen gleicher Sozialleistungsrechte bleiben verschieden. Historische Gruppenbegriffe werden zitiert; keine Motive oder tatsächlichen Migrationsfolgen daraus ableiten. Die nominalen Bedingungen werden nicht zu Aufenthaltsdauer oder Ideologiepunkten umgerechnet.

**Inhaltslücken:** Schutz-/Asylpolitik, Staatsbürgerschaft, Teilhabe und konkrete Grenz-/Abschiebemaßnahmen bleiben unvollständig. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS10SCe03_2:imsmetn` — A54

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_permission; Gegenstand: principle.

**Originaleinleitung:** Bei den folgenden Fragen geht es um Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\.

**Originaleinleitung:** Zunächst geht es um die Zuwanderer, die derselben Volksgruppe oder ethnischen Gruppe angehören wie die Mehrheit der Deutschen\.

**Originalfrage / Aussage:** Wie vielen von ihnen sollte Deutschland erlauben, hier zu leben? Sollte Deutschland es…

**Originalinstruktion:** PAPI: vier direkt gedruckte Kästchen, keine externe Listenanweisung im gelesenen Block\.

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Bei den folgenden Fragen geht es um Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\.

**CAWI-Originalfrage:** Zunächst geht es um die Zuwanderer, die derselben Volksgruppe oder ethnischen Gruppe angehören wie die Mehrheit der Deutschen\. Wie vielen von ihnen sollte Deutschland erlauben, hier zu leben? Sollte Deutschland es\.\.\.

**Dokumentierte Formabweichung/-gleichheit:** Same four category labels\. CAWI A55/A56 explicitly repeats &quot;Sollte Deutschland es\.\.\.&quot;; the PAPI A55/A56 stem continues the A54 response task\.

**Originalrouting:** PAPI A54 → A55 → A56 → A57; no filter/jump printed between A54–A56\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8480**; alle deutschen Studienfälle: 8725; fehlend: 245; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Vielen erlauben, herzukommen und hier zu leben | 1 | 33,607216 |
| 2 | Einigen erlauben | 2 | 53,184293 |
| 3 | Ein paar wenigen erlauben | 3 | 11,820790 |
| 4 | Niemandem erlauben | 4 | 1,387702 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 1 | Vielen erlauben, herzukommen und hier zu leben | keiner gedruckt |
| 2 | Einigen erlauben | keiner gedruckt |
| 3 | Ein paar wenigen erlauben | keiner gedruckt |
| 4 | Niemandem erlauben | keiner gedruckt |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 8 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 245 | 259,05920376 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 259,05920376; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 2,513067; dweight 2,523866; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: DE\-PAPI druckt nur 1–4; API ergänzt 7 Refusal,8 Don’t know,9 No answer\. API\-englisch race/ethnic group ist kein Auftrag, den deutschen Volksgruppe/ethnischeGruppe\-Wortlaut frei neu zu übersetzen\.

Quellen-/Codegrenze: Direct recheck of German PAPI page 7 corrects the prior BINDING003 abbreviated option\-3 transcription: official PAPI and CAWI both say &quot;Ein paar wenigen erlauben&quot;\. The historical report remains unchanged\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=7): physische PDF\-Seite\(n\) 7; originalQuestionId=A54.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=c79cfb20\-c948\-47ed\-85a3\-baa2f0b71ef9; sourceFieldMetadataVersion=4; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=93): physische PDF\-Seite\(n\) 93, 94; originalForm=CAWI screenshots; contentCorrespondenceToPapi=A54.

### `ESS10SCe03_2:imdfetn` — A55

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_permission; Gegenstand: principle.

**Originaleinleitung:** Bei den folgenden Fragen geht es um Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\.

**Antwortstamm:** Wie vielen von ihnen sollte Deutschland erlauben, hier zu leben? Sollte Deutschland es…

**Originalfrage / Aussage:** Wie ist das mit Zuwanderern, die einer anderen Volksgruppe oder ethnischen Gruppe angehören als die Mehrheit der Deutschen?

**Originalinstruktion:** PAPI: vier direkt gedruckte Kästchen, keine externe Listenanweisung im gelesenen Block\.

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Bei den folgenden Fragen geht es um Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\.

**CAWI-Originalfrage:** Wie ist das mit Zuwanderern, die einer anderen Volksgruppe oder ethnischen Gruppe angehören als die Mehrheit der Deutschen? Sollte Deutschland es\.\.\.

**Dokumentierte Formabweichung/-gleichheit:** Same four category labels\. CAWI A55/A56 explicitly repeats &quot;Sollte Deutschland es\.\.\.&quot;; the PAPI A55/A56 stem continues the A54 response task\.

**Originalrouting:** PAPI A54 → A55 → A56 → A57; no filter/jump printed between A54–A56\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8436**; alle deutschen Studienfälle: 8725; fehlend: 289; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Vielen erlauben, herzukommen und hier zu leben | 1 | 20,090724 |
| 2 | Einigen erlauben | 2 | 49,146890 |
| 3 | Ein paar wenigen erlauben | 3 | 26,268985 |
| 4 | Niemandem erlauben | 4 | 4,493400 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 1 | Vielen erlauben, herzukommen und hier zu leben | keiner gedruckt |
| 2 | Einigen erlauben | keiner gedruckt |
| 3 | Ein paar wenigen erlauben | keiner gedruckt |
| 4 | Niemandem erlauben | keiner gedruckt |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 8 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 289 | 310,37761221 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 310,37761221; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,613875; dweight 1,633804; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: DE\-PAPI nur 1–4; API zusätzlich 7/8/9 Missing\. Kein Code 6/Notapplicable in dieser Codeliste\.

Quellen-/Codegrenze: Same response task continues from A54; the same\-group lead\-in applies only to A54, not to A55/A56\.

Quellen-/Codegrenze: Direct recheck of German PAPI page 7 corrects the prior BINDING003 abbreviated option\-3 transcription: official PAPI and CAWI both say &quot;Ein paar wenigen erlauben&quot;\. The historical report remains unchanged\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=7): physische PDF\-Seite\(n\) 7; originalQuestionId=A55.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=965b0ffd\-239f\-4ce6\-8a93\-52e5da9728ce; sourceFieldMetadataVersion=4; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=93): physische PDF\-Seite\(n\) 93, 95; originalForm=CAWI screenshots; contentCorrespondenceToPapi=A55.

### `ESS10SCe03_2:impcntr` — A56

Quelle: ESS10SCe03\_2, Ausgabe 3\.2. Antwortform: ordered\_permission; Gegenstand: principle.

**Originaleinleitung:** Bei den folgenden Fragen geht es um Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\.

**Antwortstamm:** Wie vielen von ihnen sollte Deutschland erlauben, hier zu leben? Sollte Deutschland es…

**Originalfrage / Aussage:** Und wie ist das mit Zuwanderern, die aus den ärmeren Ländern außerhalb Europas kommen?

**Originalinstruktion:** PAPI: vier direkt gedruckte Kästchen, keine externe Listenanweisung im gelesenen Block\.

**Gebundene Form:** PAPI and cached CAWI screenshots.

**CAWI-Originaleinleitung:** Bei den folgenden Fragen geht es um Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\.

**CAWI-Originalfrage:** Und wie ist das mit Zuwanderern, die aus den ärmeren Ländern außerhalb Europas kommen? Sollte Deutschland es\.\.\.

**Dokumentierte Formabweichung/-gleichheit:** Same four category labels\. CAWI A55/A56 explicitly repeats &quot;Sollte Deutschland es\.\.\.&quot;; the PAPI A55/A56 stem continues the A54 response task\.

**Originalrouting:** PAPI A54 → A55 → A56 → A57; no filter/jump printed between A54–A56\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **8456**; alle deutschen Studienfälle: 8725; fehlend: 269; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Vielen erlauben, herzukommen und hier zu leben | 1 | 20,335261 |
| 2 | Einigen erlauben | 2 | 49,219270 |
| 3 | Ein paar wenigen erlauben | 3 | 24,664572 |
| 4 | Niemandem erlauben | 4 | 5,780898 |

**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):

| Exportcode | CAWI-Originallabel | Angezeigter Code |
| --- | --- | --- |
| 1 | Vielen erlauben, herzukommen und hier zu leben | keiner gedruckt |
| 2 | Einigen erlauben | keiner gedruckt |
| 3 | Ein paar wenigen erlauben | keiner gedruckt |
| 4 | Niemandem erlauben | keiner gedruckt |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 8 | Don&\#x27;t know | nicht gedruckt / nicht gebunden | nicht gedruckt |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 0 | 0 |
| No answer | 269 | 282,73989168 |
| Refusal | 0 | 0 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 282,73989168; primäre Gewichtssumme aller deutschen Studienfälle: 8725,00002643. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,939574; dweight 0,957156; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 0,821515460572, Maximum 0,821515625425; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: DE\-PAPI nur 1–4; API ergänzt 7/8/9 Missing\. Kein Code 6/Notapplicable in dieser Codeliste\.

Quellen-/Codegrenze: Same response task continues from A54; the same\-group lead\-in applies only to A54, not to A55/A56\.

Quellen-/Codegrenze: Direct recheck of German PAPI page 7 corrects the prior BINDING003 abbreviated option\-3 transcription: official PAPI and CAWI both say &quot;Ein paar wenigen erlauben&quot;\. The historical report remains unchanged\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=7): physische PDF\-Seite\(n\) 7; originalQuestionId=A56.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=973ef0d9\-dfce\-46e3\-8cd0\-37f03d22350d; sourceFieldMetadataVersion=4; dataFileMetadataId=178d1c16\-db15\-466e\-b1a5\-cea36109e089; dataFileMetadataVersion=147.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf#page=93): physische PDF\-Seite\(n\) 93, 96; originalForm=CAWI screenshots; contentCorrespondenceToPapi=A56.

### `ESS8e02_3:imsclbn` — E15

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: nominal; Gegenstand: principle.

**Originalfrage / Aussage:** Wenn Sie nun einmal an Menschen denken, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\. Was glauben Sie: Wann sollten sie die gleichen Rechte auf Sozialleistungen bekommen wie die Bürger, die bereits hier leben? Bitte wählen Sie von Liste 50 die Antwortmöglichkeit, die Ihrer Sichtweise am nächsten kommt\.

**Originalinstruktion:** INT\.: NUR EINE NENNUNG MÖGLICH\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2808**; alle deutschen Studienfälle: 2852; fehlend: 44; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sofort bei ihrer Ankunft\. | 1 | 11,162658 |
| 2 | Nachdem sie ein Jahr in Deutschland gelebt haben, unabhängig davon, ob sie gearbeitet haben oder nicht\. | 2 | 13,071538 |
| 3 | Erst nachdem sie mindestens ein Jahr gearbeitet und Steuern bezahlt haben\. | 3 | 50,202570 |
| 4 | Sobald sie deutsche Staatsbürger geworden sind\. | 4 | 23,269540 |
| 5 | Sie sollten niemals die gleichen Rechte bekommen\. | 5 | 2,293694 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 33 | 36,61152132 |
| No answer | 0 | 0 |
| Refusal | 11 | 10,25852 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 46,87004132; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,523083; dweight 0,805356; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Nominal conditions are retained in source order; work/tax/citizenship conditions are not recoded into a time score\. Category 1 ends with a period on Liste 50; the questionnaire table does not print that period\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=37): physische PDF\-Seite\(n\) 37; originalQuestionId=E15.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=53086955\-504b\-4fc0\-84f9\-96941928bf38; sourceFieldMetadataVersion=1; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=51): physische PDF\-Seite\(n\) 51; listLabelDe=Liste 50.

## Gleichstellungs- und Familienpolitik

Konkrete Eingriffe und Erwerbs-/Familienfinanzierung bleiben Einzelmaßnahmen. Elternzeit enthält das vollständige Doppelverdiener-, Verdienst-, Neugeborenen- und Anspruchsszenario; Familienleistungen behalten die ausdrücklich höhere Steuerlast.

**Inhaltslücken:** Reproduktive Selbstbestimmung, vielfältige Lebensformen, Behinderung und weitere Diskriminierungsgründe sind unvollständig. Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und [feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).

### `ESS11e04_2:eqparep` — E19

Quelle: ESS11e04\_2, Ausgabe 4\.2. Antwortform: ordered\_support; Gegenstand: measure.

**Originalfrage / Aussage:** Bitte sagen Sie anhand der Liste 64: Inwieweit sind Sie für oder gegen ein Gesetz, welches eine gleiche Verteilung der Sitze im Bundestag zwischen Frauen und Männern vorschreibt?

**Originalinstruktion:** LISTE 64

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2367**; alle deutschen Studienfälle: 2420; fehlend: 53; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dafür | 1 | 14,138145 |
| 2 | Eher dafür | 2 | 25,751863 |
| 3 | Weder dafür noch dagegen | 3 | 30,084732 |
| 4 | Eher dagegen | 4 | 19,203591 |
| 5 | Sehr dagegen | 5 | 10,821669 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 49 | 67,0130368322 |
| No answer | 0 | 0 |
| Refusal | 4 | 6,52636018395 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 73,5393970162; primäre Gewichtssumme aller deutschen Studienfälle: 2419,99996939. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 3,779088; dweight 3,760437; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,992969752, Maximum 2,992969752; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: API ergänzt 9 No answer und sagt Parliament generisch, DE ausdrücklich Bundestag\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess11\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf#page=51): physische PDF\-Seite\(n\) 51; originalQuestionId=E19.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=e61ee38c\-800f\-449d\-a232\-5477b7510b6c; sourceFieldMetadataVersion=6; dataFileMetadataId=242aaa39\-3bbb\-40f5\-98bf\-bfb1ce53d8ef; dataFileMetadataVersion=179.

### `ESS11e04_2:eqparlv` — E20

Quelle: ESS11e04\_2, Ausgabe 4\.2. Antwortform: ordered\_support; Gegenstand: measure.

**Situation:** Stellen Sie sich ein Paar vor, bei dem beide Vollzeit arbeiten und ungefähr gleich viel verdienen\. Jetzt haben sie ein neugeborenes Kind\. Beide haben Anspruch auf bezahlte Elternzeit, wenn sie eine Zeitlang nicht arbeiten, um sich um ihr Kind zu kümmern\.

**Originalfrage / Aussage:** Bitte benutzen Sie weiter Liste 64\. Inwieweit sind Sie für oder gegen ein Gesetz, welches beiden Elternteilen vorschreibt, gleich lange bezahlte Elternzeit zu nehmen, um ihr Kind zu betreuen?

**Originalinstruktion:** WEITER LISTE 64

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2394**; alle deutschen Studienfälle: 2420; fehlend: 26; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dafür | 1 | 17,960429 |
| 2 | Eher dafür | 2 | 21,650116 |
| 3 | Weder dafür noch dagegen | 3 | 17,477349 |
| 4 | Eher dagegen | 4 | 24,794416 |
| 5 | Sehr dagegen | 5 | 18,117690 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 23 | 34,3424255401 |
| No answer | 0 | 0 |
| Refusal | 3 | 5,01263843477 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 39,3550639749; primäre Gewichtssumme aller deutschen Studienfälle: 2419,99996939. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 3,145521; dweight 3,153542; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,992969752, Maximum 2,992969752; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: API ergänzt 9 No answer\. API\-question allein enthält die Paar\-/Arbeits\-/Verdienst\-/Neugeborenen\-/Anspruchseinleitung nicht; preQuestion/filter sind leer, kein Ersatz für den Originalkontext\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess11\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf#page=52): physische PDF\-Seite\(n\) 52; originalQuestionId=E20.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=aa51d9ae\-6bea\-4cc6\-9208\-d951a48338e2; sourceFieldMetadataVersion=6; dataFileMetadataId=242aaa39\-3bbb\-40f5\-98bf\-bfb1ce53d8ef; dataFileMetadataVersion=179.

### `ESS11e04_2:freinsw` — E21

Quelle: ESS11e04\_2, Ausgabe 4\.2. Antwortform: ordered\_support; Gegenstand: measure.

**Originalfrage / Aussage:** Bitte benutzen Sie weiter Liste 64\. Inwieweit sind Sie dafür oder dagegen, dass Mitarbeitenden gekündigt wird, die bei der Arbeit Frauen gegenüber beleidigende Bemerkungen machen?

**Originalinstruktion:** WEITER LISTE 64

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2383**; alle deutschen Studienfälle: 2420; fehlend: 37; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dafür | 1 | 30,659102 |
| 2 | Eher dafür | 2 | 41,451395 |
| 3 | Weder dafür noch dagegen | 3 | 16,304896 |
| 4 | Eher dagegen | 4 | 9,619847 |
| 5 | Sehr dagegen | 5 | 1,964760 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 29 | 39,5101490468 |
| No answer | 0 | 0 |
| Refusal | 8 | 5,07159970701 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 44,5817487538; primäre Gewichtssumme aller deutschen Studienfälle: 2419,99996939. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 0,409528; dweight 0,453823; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,992969752, Maximum 2,992969752; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: API ergänzt 9 No answer; übrige deklarierte Kategorien inhaltlich entsprechend, keine empirische Übersetzungsäquivalenz bescheinigt\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess11\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf#page=52): physische PDF\-Seite\(n\) 52; originalQuestionId=E21.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=c7b2e500\-d64e\-462f\-a433\-dda69d7b4c20; sourceFieldMetadataVersion=6; dataFileMetadataId=242aaa39\-3bbb\-40f5\-98bf\-bfb1ce53d8ef; dataFileMetadataVersion=179.

### `ESS11e04_2:fineqpy` — E22

Quelle: ESS11e04\_2, Ausgabe 4\.2. Antwortform: ordered\_support; Gegenstand: measure.

**Originalfrage / Aussage:** Bitte benutzen Sie weiter Liste 64\. Inwieweit sind Sie dafür oder dagegen, dass Unternehmen eine Geldstrafe zahlen müssen, wenn sie Männer für die gleiche Arbeit besser bezahlen als Frauen?

**Originalinstruktion:** WEITER LISTE 64

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2375**; alle deutschen Studienfälle: 2420; fehlend: 45; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dafür | 1 | 29,414280 |
| 2 | Eher dafür | 2 | 37,004323 |
| 3 | Weder dafür noch dagegen | 3 | 20,112426 |
| 4 | Eher dagegen | 4 | 10,698963 |
| 5 | Sehr dagegen | 5 | 2,770009 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 32 | 46,0836859494 |
| No answer | 0 | 0 |
| Refusal | 13 | 15,0508907884 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 61,1345767379; primäre Gewichtssumme aller deutschen Studienfälle: 2419,99996939. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 1,972744; dweight 1,962319; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,992969752, Maximum 2,992969752; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: API ergänzt 9 No answer; deutsche Frage enthält präzise Vergleichsrichtung Männer werden besser bezahlt\.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess11\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf#page=52): physische PDF\-Seite\(n\) 52; originalQuestionId=E22.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=4c9d0d92\-71b4\-4e02\-82f6\-e29e516b231a; sourceFieldMetadataVersion=6; dataFileMetadataId=242aaa39\-3bbb\-40f5\-98bf\-bfb1ce53d8ef; dataFileMetadataVersion=179.

### `ESS8e02_3:wrkprbf` — E35

Quelle: ESS8e02\_3, Ausgabe 2\.3. Antwortform: ordered\_support; Gegenstand: measure.

**Originalfrage / Aussage:** Wären Sie dagegen oder dafür, dass Staat und Regierung zusätzliche Sozialleistungen einführen, die es erwerbstätigen Eltern erleichtern, Arbeit und Familie zu vereinbaren, auch wenn das deutlich höhere Steuern für alle bedeuten würde?

**Originalinstruktion:** INT\.: LISTE 53 VORLEGEN\.

**Gebundene Form:** National CAPI interview script.

**Originalrouting:** No special filter/jump printed at this item in the inspected national block\.

**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**

Gültiger Antwortnenner: **2765**; alle deutschen Studienfälle: 2852; fehlend: 87; strukturell nicht gestellt: 0. Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.

Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.

| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |
| --- | --- | --- | --- |
| 1 | Sehr dagegen | 1 | 3,370546 |
| 2 | Dagegen | 2 | 34,302644 |
| 3 | Dafür | 3 | 54,159640 |
| 4 | Sehr dafür | 4 | 8,167170 |

**Technischer Missing-Kontext, keine politischen Antwortoptionen:**

| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |
| --- | --- | --- | --- |
| 7 | Refusal | Antwort verweigert | 7 |
| 8 | Don&\#x27;t know | Weiß nicht | 8 |
| 9 | No answer | nicht gedruckt / nicht gebunden | nicht gedruckt |
| leere Exportzelle | export\_blank\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |

Strukturelle Nichtgestellt-Codes: keine im gebundenen Adapter. Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.

**Missing-Abrechnung auf alle deutschen Studienfälle:**

| Grund | Anzahl | Summe der primären Gewichte |
| --- | --- | --- |
| Don&\#x27;t know | 77 | 91,91575153 |
| No answer | 0 | 0 |
| Refusal | 10 | 9,22887527 |
| export\_blank\_unclassified | 0 | 0 |

Primäre fehlende Gewichtssumme: 101,1446268; primäre Gewichtssumme aller deutschen Studienfälle: 2852,00000435. Keine Imputation und keine Missing-Mitte.

**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: ungewichtet 2,476243; dweight 1,226316; anweight-Diagnose 0,000000. anweight/pspwght-Verhältnis: Minimum 2,49980899765, Maximum 2,49980947373; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.

**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, keine Latentskala und keine neue Politikposition.

Quellen-/Codegrenze: Categories use exported file codes; printed German form codes are retained separately\. Missing labels are not substantive political options\.

**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=42): physische PDF\-Seite\(n\) 42; originalQuestionId=E35.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=93a84094\-1c22\-476c\-9ed8\-41c96c142465; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=54): physische PDF\-Seite\(n\) 54; listLabelDe=Liste 53.

## Quellen- und Nachnutzungsregister

Originalwortlaute, Instruktionen und Kategorien sind Transkriptionen aus den benannten deutschen ESS-Instrumenten. Layoutumbrüche und Trennungen am Zeilenende werden nach der Katalogregel normalisiert; Einleitungen, Ellipsen, Stämme, Szenarien und nationale Anpassungen bleiben erhalten. Die hier dargestellte Zusammenstellung, Methodenprosa, Rubriken und Tabellen sind Projektbearbeitungen, keine unveränderte Neuauflage eines ESS-Fragebogens. Dokumentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en); Datenableitungen: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en). ESS ERIC/Sikt sind Quellengeber, keine Billigung dieses Projekts. [Lizenzakte](../../docs/lizenzen.md) und [Datenattribution](../../data/reference-v2/README.md) bleiben maßgeblich; keine pauschale Rechts- oder kommerzielle Nutzungsfreigabe.

Gebundener Katalog: `data/politikprofil-v2.fragen.entwurf.json`, SHA256 `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4`. Abrufzeit und HTTP-Status unten stammen aus früheren Quellenbindungen; dieser Build führt keinen Netzwerkabruf durch.

[ess\-disclaimer\-current](https://europeansocialsurvey.org/contact/disclaimer): Official data and documentation license notice; früherer Abruf UTC 2026\-10\-03T12:39:49\.677113\+00:00; HTTP 200; SHA256 `b5201b2deefd86d7f87a8dfb11dfdd30fd4f9afb8cbbb51b9254dd58bfa5ab8a`; Lizenzkennung keine eigene Kennung gebunden.

[ess\-prospectus\-access\-doc](https://www.europeansocialsurvey.org/sites/default/files/2024-04/prospectus_updated.pdf): Official portal registration and format description; früherer Abruf UTC 2026\-10\-03T12:43:04\.169908\+00:00; HTTP 200; SHA256 `2b87077a3d81f7fe6086d1136548d5a8d66aaafa5ea3227ba6ef34cbec38cb5f`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess\-public\-de\-mode\-metadata](https://api.nsd.no/graphql): Public German fieldwork/mode/sampling metadata; früherer Abruf UTC 2026\-10\-03T12:16:28\.755964\+00:00; HTTP 200; SHA256 `2bf2a0cf1ec2696483a17ea7bdd02763255ef4afbed305829ff6f7b8436074c1`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess10\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf): German original questionnaire; früherer Abruf UTC 2026\-10\-03T12:14:40\.627299\+00:00; HTTP 200; SHA256 `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess10\-study\-access\-metadata](https://api.nsd.no/graphql): Public declared study universe/citations/access metadata; früherer Abruf UTC 2026\-10\-03T12:17:07\.479551\+00:00; HTTP 200; SHA256 `ea3f3a252be74c99e7260b2f906e21f7f06612ac4b15ac7fedb982d749770d66`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess10\-study\-current](https://api.nsd.no/graphql): Public current study/file identities; früherer Abruf UTC 2026\-10\-03T12:37:22\.747295\+00:00; HTTP 200; SHA256 `99c1662190d5d79d0efe20f30ed678497a216184a37282e374e06a746e5cc3d9`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess10sc\-file\-metadata](https://api.nsd.no/graphql): Public API declared file and variable metadata; früherer Abruf UTC 2026\-10\-03T12:37:22\.345777\+00:00; HTTP 200; SHA256 `d9e6d606fb3b897d33d04f3247dbe5160d11f108a76fca6547a773e2c1ba0a57`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess10sc\-original\-codelists\-direct](https://api.nsd.no/graphql): Public API declared variables and full code lists; früherer Abruf UTC 2026\-10\-03T12:38:58\.912040\+00:00; HTTP 200; SHA256 `1d61d3620f41871d3d4aacb9b30e6d34e845cdf620a0e05b0c1c33bbf735c680`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess11\-current\-study](https://api.nsd.no/graphql): Public current study/file identities; früherer Abruf UTC 2026\-10\-03T12:52:44\.263431\+00:00; HTTP 200; SHA256 `3f029f3d4759224f07a9a05b21f16ac2d13e1b29ef2b845aa056601283ea3c4d`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess11\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf): German original questionnaire; früherer Abruf UTC 2026\-10\-03T12:14:41\.334719\+00:00; HTTP 200; SHA256 `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess11\-file\-variable\-catalogue](https://api.nsd.no/graphql): Public API declared file and variable metadata; früherer Abruf UTC 2026\-10\-03T12:52:44\.131781\+00:00; HTTP 200; SHA256 `0091d6206b33d4018ab2fc2891e2bf2e911a384e497d7b391631d9e19f707505`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess11\-study\-access\-metadata](https://api.nsd.no/graphql): Public declared study universe/citations/access metadata; früherer Abruf UTC 2026\-10\-03T12:17:07\.665608\+00:00; HTTP 200; SHA256 `19736f79eeabef664298fb1d0b23a94007716d7a41d1e7f84679e85797963430`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf): German original questionnaire; früherer Abruf UTC 2026\-10\-03T12:14:38\.908875\+00:00; HTTP 200; SHA256 `24b5d2599e6d30dc02a6d835f5f80b5bcecf8f6014ee8f4670a703c25d3c3cbf`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess5\-file\-metadata](https://api.nsd.no/graphql): Public API declared file and variable metadata; früherer Abruf UTC 2026\-10\-03T12:39:49\.842239\+00:00; HTTP 200; SHA256 `a6f232bfdff538b29db3f79fba6d8a452852012db26d0993fec9933f778d29da`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): Public API declared variables and full code lists; früherer Abruf UTC 2026\-10\-03T12:40:28\.429549\+00:00; HTTP 200; SHA256 `fd07c44fa7e09359d2f0c43c37429d4f6f83061d03412bed030ef3a88913cc29`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess5\-study\-access\-metadata](https://api.nsd.no/graphql): Public declared study universe/citations/access metadata; früherer Abruf UTC 2026\-10\-03T12:17:06\.134526\+00:00; HTTP 200; SHA256 `6a58c03724731f75f84b2d4814956394d9b55b67dd3a5a72231da0d381565dc0`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess5\-study\-current](https://api.nsd.no/graphql): Public current study/file identities; früherer Abruf UTC 2026\-10\-03T12:38:58\.767802\+00:00; HTTP 200; SHA256 `6a58c03724731f75f84b2d4814956394d9b55b67dd3a5a72231da0d381565dc0`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf): German original questionnaire; früherer Abruf UTC 2026\-10\-03T12:14:39\.927363\+00:00; HTTP 200; SHA256 `977475c18d2adebea6ccb7695f377fb6ed500ef087b077086305f9a2e4a7b239`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf): German original response lists; früherer Abruf UTC 2026\-10\-03T12:23:12\.855249\+00:00; HTTP 200; SHA256 `dde02b5336b2d960c2900a8fcf5e2a0f0d254b46dcce1d9ffb785a830e096bc0`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess8\-file\-metadata](https://api.nsd.no/graphql): Public API declared file and variable metadata; früherer Abruf UTC 2026\-10\-03T12:37:22\.388985\+00:00; HTTP 200; SHA256 `99d5e0bf071ae4fd6ee946a64f8e152a5d72341ef575c1c3325e78c21b70a050`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): Public API declared variables and full code lists; früherer Abruf UTC 2026\-10\-03T12:38:58\.925493\+00:00; HTTP 200; SHA256 `d42123466306f52bbdd21557d829aa38418d9b705e27917e084ca38f9936f6d9`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess8\-sddf\-metadata](https://api.nsd.no/graphql): Public declared sample\-design\-file metadata; früherer Abruf UTC 2026\-10\-03T12:38:32\.267721\+00:00; HTTP 200; SHA256 `eab237d972b3ce655cbe2bda77600e514c39e9f2b115f4d161a31d19d7f6622a`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess8\-study\-access\-metadata](https://api.nsd.no/graphql): Public declared study universe/citations/access metadata; früherer Abruf UTC 2026\-10\-03T12:17:07\.089786\+00:00; HTTP 200; SHA256 `1a17f742d7529fe535f0e0b93973e1b74198a1a8781fbf196a7c1ec702346ce7`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess8\-study\-current](https://api.nsd.no/graphql): Public current study/file identities; früherer Abruf UTC 2026\-10\-03T12:37:22\.491435\+00:00; HTTP 200; SHA256 `7dd3204782e7a42324416c57f17a0f5e357ba1308f3cfc05bdab04e0eb2c8d52`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf): German original questionnaire; früherer Abruf UTC 2026\-10\-03T12:14:40\.302351\+00:00; HTTP 200; SHA256 `ae960ebcae1b12106eb3003ced1de7c88a73c9b95736efedd93fd8b320e974a5`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess9\-file\-metadata](https://api.nsd.no/graphql): Public API declared file and variable metadata; früherer Abruf UTC 2026\-10\-03T12:37:22\.350553\+00:00; HTTP 200; SHA256 `8eb100eb4b0dad2a8e7ae5525cc255a4f428d6d18e0cce235de75a021f195bfd`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): Public API declared variables and full code lists; früherer Abruf UTC 2026\-10\-03T12:38:58\.823141\+00:00; HTTP 200; SHA256 `cc0594fcd2d4d347da5fded389ddf49ca7b4736b0ad97ce2871a20f8180a441f`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess9\-study\-access\-metadata](https://api.nsd.no/graphql): Public declared study universe/citations/access metadata; früherer Abruf UTC 2026\-10\-03T12:17:07\.288291\+00:00; HTTP 200; SHA256 `d32903b14ad1018552ce3b50183d50825ff8b5b90dc28c5bc93e127430a8812f`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[ess9\-study\-current](https://api.nsd.no/graphql): Public current study/file identities; früherer Abruf UTC 2026\-10\-03T12:37:22\.603532\+00:00; HTTP 200; SHA256 `6bbeb34b89c028e6c1712981c0a6072e5fc8f58178509e83d658676e4b7d144f`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

[nine\-fields\-original\-codelists](https://api.nsd.no/graphql): Public API declared nine\-variable metadata and full code lists; früherer Abruf UTC 2026\-10\-03T12:53:08\.006366\+00:00; HTTP 200; SHA256 `220fcbe3063917c3ef81841c0331b57b2b969bbe4edfa5e3e1355f2e13d053d6`; Lizenzkennung ess\-documentation\-cc\-by\-sa\-4\.0.

## Reproduktion und offene Voraussetzungen

Der lokale Build `PYTHONDONTWRITEBYTECODE=1 python scripts/build-policy-v2-report.py` bindet ausschließlich die fest gepinnten veröffentlichten Exporte, Katalog-/Quellen-/Methodenbytes und RESULTS-V2-001-Berichte/Entscheidungen. `--check` prüft Bytegleichheit des erzeugten Artefakts. Der unveränderte technische Renderer prüft die geschlossene öffentliche Exportform. Das ist reproduzierbare Darstellung veröffentlichter Aggregate, keine neue unabhängige Rohreproduktion.

Marktordnung, Außen-/Verteidigungs-/Friedenspolitik und die oben genannten Binnenfacetten bleiben Quellen-/Produktlücken. GLES und ISSP bleiben mögliche getrennte Ergänzungswege mit eigenen Rechten, Populationen und Versionen; hier entsteht keine neue Referenz dafür. Der Themenbericht bleibt bis zur gezielten unabhängigen Präsentationsprüfung WIP. Hauptproduktbreite, menschlicher Verständnistest, endgültige Gestaltung, Claude-Schlusskontrolle und persönlicher Release sind weiterhin offen.
