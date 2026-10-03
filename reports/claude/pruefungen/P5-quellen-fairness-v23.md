# P5: Quellen, Konstrukte und Fairness des Planentwurfs v2.3

Stand: 4. Oktober 2026 (Europe/Berlin). Erstbewertung, Paket PLAN-V23-001, Entwurf 0.2. Bericht und JSON bilden mein eigenes begrenztes KI-Review.

## Gesamturteil

**NICHT_BESTANDEN für die Festschreibung im geprüften P5-Umfang.** P5-V23-F01 ist erheblich; P5-V23-F02 und F03 sind mittel und blockieren ebenfalls diesen Umfang. P5-V23-F04 ist niedrig und blockiert ihn nicht. Der Lizenzrahmen und die geprüften Rechtsstände tragen die jeweiligen begrenzten Aussagen. Die Auswahlregeln und zwei Aussagen über die Kandidaten müssen vor Festschreibung korrigiert werden.

Ich habe keine empirische politische Verzerrung festgestellt oder geschätzt. Das negative Urteil betrifft belegte Auswahl- und Interpretationsfehler. Es genehmigt keinen Datenabruf, keine Aktivierung, keinen Export und keine Veröffentlichung.

## Bindung und Unabhängigkeit

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`. Start-HEAD und Branch waren exakt `6e164209ac2872447c2b5353f64ba5c6b6294fb3` und `research/life-93-claude-20261003`; der Arbeitsstand war sauber. Der Manifesthash war vor der Bewertung `c2c05725351ff209af158704d0896693fd480be66f4027b22125d97066566c89`. Alle 19 Einträge unter `artifacts` stimmten mit ihren SHA-256-Pins überein.

`manifest.commit` nennt `23c68565c455905b8ed1e51bd76422fc0cd56d45`, die ältere Paketbasis. Das widerspricht der angegebenen späteren Auftrags-HEAD nicht: Bewertet wurden die tatsächlich gehashten Paketbytes. Während der Prüfung setzte ein anderer Prozess HEAD auf `578adaed884a87fb0a6a1ee4137bf98547861f42` weiter. Eine reine Pfadprüfung des Commitunterschieds zeigte Änderungen an `docs/ki-protokoll.md`, `docs/project.md` und `reports/claude/fortsetzung-2026-10-04.md`. Die beiden fremden Berichte/Protokolle habe ich nicht geöffnet. Alle 19 Paketpins blieben unverändert.

Die Rechercheberichte R6/R8/R9/R10 und der Strukturbericht S1 sind ausdrücklich gepinnte Prüfgrundlagen. Ihre Schlussfolgerungen wurden nicht als Urteil über diesen Plan übernommen. Kein Urteil der anderen aktuellen Prüfrolle und keine Autorantwort gelesen. Der freigegebene Basisplan v2.2 enthält historische Reviewhinweise; sie wurden als Planhistorie gelesen. Der kurze Gedächtnisabgleich diente nur Isolation, Hashprüfung und begrenzter Urteilsform.

Keine Dateien unter `data/raw/`, `data/local/`, `outputs/`, `data/reference-*`, `reports/phasen/02-*` bis `04-*` oder `web/src/app/policy-draft/reviewed-*` gelesen. Keine externen Ergebnistabellen geöffnet. Die Ausnahme in der Manifestnotiz für Statusfelder wurde wegen des ausdrücklichen Nutzerverbots nicht genutzt. Die Zahlen in Plan Abschnitt 8 sind deshalb nicht unabhängig verifiziert.

## Befunde

### P5-V23-F01: Unterschiedliche Regeln für Anlass und Abwägung

**Erheblich, OFFEN, blocksScope=true.** Abschnitt 4 Nr. 4 erlaubt gekennzeichnete Prämissen und Begründungen, verbietet aber wertende Prämissen. Abschnitt 11 verwirft die Gegenzollfrage ST0939 allein mit „Anlass im Fragetext“. Zugleich bleibt ST0350 Item 2 zur Ukraine-Finanzierung mit reaktionsbezogener Einleitung ausgewählt. Der Plan erklärt nicht, welcher relevante Unterschied den Ausschluss trägt. Beim OECD-Item Q27 e ist eine Kosten-Nutzen-Vorgabe der Ausschlussgrund, während die KI-Frage QB12 und Q19 eine ausdrückliche Abwägung enthalten und zugelassen bleiben.

Belege: `docs/analyseplan-v2.3.entwurf.md:47-54,128,130,136,150`; `R6-eurobarometer.md:176-182,191,197-198`; R8-JSON, `kandidaten[id=R8-EB-ST0350-2]` und `kandidaten[id=R8-EB-ST0939-ZOLL]`, jeweils `wortlautDe` und `kontext`; [OECD-Kernfragebogen 2024](https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf), PDF-S. 7 und 10. Die Kontexte sind verschieden. Das Finding verlangt eine belegte Abgrenzung und behauptet nicht ihre Identität.

Auswirkung: Zustimmung zu militärischer Unterstützung wird als Frage angeboten, Zustimmung zu defensiven Zöllen wird mit einem nicht durchgängig angewandten Ausschlussgrund verworfen. Eine Arbeitszeitfrage wird wegen einer Abwägung entfernt, während andere Abwägungen erlaubt bleiben. Gleiche Auswahlstandards sind damit nicht bestätigt. Es gibt keinen Nachweis für Absicht, Parteibegünstigung oder die Größe eines Framingeffekts.

Korrektur: Vor Ergebnissicht eine gemeinsame Regel für sachlichen Anlass, wertende Prämisse, bedingte Präferenz und zweiseitige Abwägung formulieren. Die genannten Fälle nach dieser Regel begründen, ändern oder zurückstellen. Nachprüfung anhand einer neu gepinnten Plan- und Kandidatenfassung. Keine eigenen Gegenfragen erfinden und keine Originaltexte umschreiben.

### P5-V23-F02: Allgemeine Prinzipien werden pauschal als EU-Fragen eingeordnet

**Mittel, OFFEN, blocksScope=true.** Die Aussage in Zeile 138, alle elf Fragen verkleinerten Lücken „nur auf EU-Ebene“, widerspricht den eigenen Zeilen zu KI und Forschung. QB12 und beide QA7-Fragen nennen keine Ebene; sie messen eine allgemeine Regulierungspräferenz beziehungsweise Forschungsprinzipien. Bei ST0359-GELD bleibt die Ebene offen. Die Population und der Herausgeber einer EU-Erhebung legen nicht den Antwortgegenstand fest.

Belege: `docs/analyseplan-v2.3.entwurf.md:127,130,132-133,138`; `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:31-33`; `R6-eurobarometer.md:198,231`; `R8-erweiterung-aussen-digital-bildung.md:159,204,233-242`.

Korrektur: Ausdrückliche EU-Entscheidungen, allgemeine Präferenzen/Prinzipien ohne genannte Ebene und die mehrdeutige Ausgabenfrage getrennt beschreiben. Zusammenfassung, Entscheidungsvorlage und spätere Themenabdeckung müssen dieselbe Reichweite nennen. Nachprüfung aller elf Zeilen gegen diese Aussagen. Nationale Kernlücken bleiben sichtbar.

### P5-V23-F03: Die angeblich einzigen fünf OECD-Fragen sind eine unbegründete Teilauswahl

**Mittel, OFFEN, blocksScope=true.** Q19 b zu Bildung und Q19 c zu Beschäftigungsunterstützung verwenden denselben Stamm wie die fünf ausgewählten Q19-Items. Sie passen zu benannten Lücken. Die Aussage, „nur“ die fünf Fragen seien ohne Prämisse oder Begründung verfügbar, trägt der Originalfragebogen nicht. Es fehlen Ausschlussgründe und eine vollständige Nutzenabwägung.

Belege: `docs/analyseplan-v2.3.entwurf.md:21,45-54,150`; `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:37-41`; `docs/abdeckung-v2.2.md:26,36`; [OECD-Kernfragebogen 2024](https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf), PDF-S. 7, gemeinsamer Stamm Q19 a-l.

Korrektur: Mindestens Bildung und Beschäftigungsunterstützung nach denselben Regeln prüfen und aufnehmen oder konkret begründet ausschließen. Die Fünferbehauptung und die darauf gestützte Empfehlung berichtigen. Die Entscheidung gegen Quoten kann auch danach sachlich tragen; Altersgrenze, Stichprobenart und fehlender deutscher Wortlaut bleiben unverändert. Nachprüfung von Q19 a-l gegen Kandidaten-/Ausschlussliste und Entscheidungsvorlage. Nichtauswahl in der Mehrfachfrage darf später nicht automatisch als Ablehnung des Einzelbereichs gelten.

### P5-V23-F04: ESS12-Termin für Deutschland und Fragebogen zu sicher dargestellt

**Niedrig, OFFEN, blocksScope=false.** Die Entscheidungsvorlage kündigt Daten und deutschen Fragebogen für Januar 2027 an. Die ESS-Meldung nennt nur den erwarteten ersten Datenrelease. Deutschland und der deutsche Fragebogen sind zu diesem Termin nicht zugesichert. R9 nennt diese Grenze bereits.

Belege: `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:51-53`; `R9-erweiterung-sozial-wohnen-gruppen.md:22,187,345`; [ESS-Meldung vom 30. September 2026](https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027).

Korrektur: Erwarteten Ersttermin und die ungeklärte deutsche Verfügbarkeit trennen. Die positiven Voraussetzungen in Plan 11.2 bleiben bestehen; sie verhindern schon jetzt einen verfrühten Zugriff. Nachprüfung nur dieser Terminpassage.

## Konstrukte der elf Eurobarometer-Kandidaten

Diese Tabelle beurteilt die im Paket dokumentierten Konstrukte. Sie authentifiziert keinen erneut geöffneten deutschen Feldfragebogen. Die vollständige Wortlautbindung bleibt vor Aufnahme je Item erforderlich.

| Kandidat | Tragfähiger enger Gegenstand und verbleibende Grenze |
| --- | --- |
| SE037-GSVP | Gemeinsame Sicherheits-/Verteidigungspolitik; Integration auf EU-Ebene. Kein Urteil zu deutschem Wehrdienst oder Bundeswehrhaushalt. Wortlautwechsel 105.2 beachten. |
| SE037-GASP | Gemeinsame Außenpolitik; Integrationsprinzip mit deutscher Mitentscheidung im Rat. Keine konkrete nationale Außenentscheidung. |
| ST0359-ZUS | Verstärkte EU-Verteidigungszusammenarbeit; gerichtete Zustimmungsaussage. Kein eigenständiger Wunsch nach höheren Ausgaben. |
| ST0359-GELD | Mehr Verteidigungsausgaben „in der EU“; kein bestimmter EU- oder deutscher Haushalt. Die Mehrdeutigkeit ist im Plan zutreffend offen. |
| ST0350-2 | Zustimmung zur bereits beschlossenen EU-Finanzierung militärischer Ukraine-Ausrüstung mit Reaktionskontext. Einleitung vollständig mitführen; F01. |
| SP564-QC5-UA | Bedingter Ukraine-Beitritt, wenn Mitgliedschaftsvoraussetzungen erfüllt sind. Kein sofortiger bedingungsloser Beitritt. S1 nennt vier Richtungsstufen, keinen bloßen Binärcode (S1:105,111). |
| SP572-QB12-KI | Abwägung von Regulierung/Sicherheit und Einschränkungen/Risiken. Zwei angebotene Positionen, keine ausdrücklich genannte EU-Ebene. „Sorgfältig“ bleibt wertendes Framing im Original; beide Optionen nennen Konsequenzen. |
| SP572-QB5-6 | EU-Ziel für die nächsten zehn Jahre: stärkere Plattformregulierung. Zeitraum und Einleitung mitführen; keine gemessene Abwägung mit Meinungsfreiheit. |
| SP557-QA7-OA | Kostenfreier Onlinezugang zu öffentlich finanzierter Forschung; allgemeines Prinzip. Kein Maß für Bildungsföderalismus, BAföG oder Forschungsausgaben. Strukturprüfung noch ausstehend. |
| SP557-QA7-GRENZE | Unbegrenzte Untersuchungsgegenstände der Wissenschaft; allgemeines Prinzip. Daraus weder Zustimmung zu jeder Forschungsmethode noch Ablehnung jedes Ethikschutzes ableiten. Strukturprüfung noch ausstehend. |
| R9-21 / SE037 Gesundheit | Gemeinsame EU-Gesundheitspolitik; Integrationsprinzip. Kein Urteil zu Bürgerversicherung, Pflegefinanzierung oder nationaler Krankenhauspolitik. |

ST0359-ZUS/GELD, ST0350-2, Plattformregulierung und beide Forschungsprinzipien sind einseitig formulierte Zustimmungsaussagen. Die Verteidigungsauswahl häuft gemeinsame Politik, Zusammenarbeit, Mehrausgaben und militärische Unterstützung. Ein zustimmender Antwortstil könnte deshalb mehrere Antworten in dieselbe politische Richtung bewegen. Das ist ein konkretes Formatrisiko, keine festgestellte Verzerrung. Ablehnung ist in den Skalen möglich; fehlende spiegelbildliche Items machen eine Originalfrage nicht automatisch unzulässig. Keine negative Personendeutung aus Ablehnung, keine Themenwerte oder Motive ableiten. Der Plan darf diese Auswahl nicht als empirisch nachgewiesen ausgewogen darstellen.

Wertende Zielformeln bei ST0359-UA und SE035-Steuern zu erkennen, Dringlichkeit/Wichtigkeit von Maßnahmenpräferenzen zu trennen und Doppelfragen auszuschließen, ist sachlich begründet. Der Unterschied zwischen Bedingung („wenn alle Voraussetzungen erfüllt sind“) und wertender Begründung darf bestehen. F01 betrifft die nicht erklärten Maßstabswechsel, nicht diese begründeten Unterschiede.

## Rechte und Rechtsstände

ESS-Disclaimer sowie CC BY-SA und CC BY-NC-SA bestätigen den getrennten Rahmen für Dokumentation und Daten. Nichtkommerzielle Nutzung, Attribution, Änderungsvermerke und gegebenenfalls ShareAlike bleiben Voraussetzungen. Eine allgemeine Lizenz ist keine tatsächliche Freigabe eines deutschen ESS12-Exports.

Die fünf geprüften Eurobarometer-Metadatensätze weisen COM_REUSE aus. Art. 2, 4 und 6 des [Beschlusses 2011/833/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32011D0833) tragen den Tabellenweg, mit den jeweiligen Rechten und Einschränkungen. Der [Kommissionshinweis](https://commission.europa.eu/legal-notice_de) bestätigt die Weiterverwendung eigener Inhalte und den Vorbehalt für Drittrechte. Die derzeit konservative Klasse B für deutsche Feldtexte darf bleiben. Der Befund ist nicht: Fehlt eine KI-Klausel, ist jede Nutzung erlaubt.

GESIS § 4 wurde an einer Originalkopie vom 30. März 2026 auf web.archive.org gelesen. KI-Verarbeitung ist dort untersagt; Ausnahmen brauchen GESIS. Es gab keine Verbindung zu einem GESIS-Server, auch keinen Redirect. Die Livefassung wurde nicht geprüft. Eine Freigabe Stevens allein ersetzt keine Rechteklärung. Ebenso bestätigen UKDS Nr. 5 und die SOEP-Richtlinie die jeweiligen Mikrodatenstopps. SOEP erlaubt ausdrücklich öffentliche Dokumentation und Codeerstellung ohne Mikrodatenübermittlung; diese Ausnahme ist kein Datenzugang für Steven. EIB untersagt bestimmte Veröffentlichungsnutzungen ohne Erlaubnis. ZQP wurde wegen des bereits dokumentierten Verbots automatisierten Lesens nicht neu abgerufen. ifo/EBDC wurde nicht erneut an der Vertragsdatei geprüft.

Das WVS-Formular trägt die begrenzte Einordnung mit Nichtgewinnorientierung, Zitation, Publikationsmeldung und Dateiverbot für Weitergabe. Keine Formulare abgeschickt. OECD-Archivbedingungen erlauben allgemeine veröffentlichte Daten, lösen aber nicht die gesonderten Mikrodaten- und deutschen Wortlautfragen. Die Klassen bleiben nutzungs- und bezugswegbezogen; A/B/C sind hier keine Stichprobenklassen Z/T/Q.

Die Primärquellenstichprobe bestätigt neue Grundsicherung zum 1. Juli 2026 (BMAS), Tariftreue als „In Kraft“ zum 1. Mai 2026 (BMAS-Liste), GKV-Gesetz zum 30. Juli 2026 (BMG) und PNOG als laufendes Gesetzgebungsverfahren mit Kabinettsdatum 30. September 2026 (BMG). [WPflG § 2a](https://www.gesetze-im-internet.de/wehrpflg/__2a.html) verlangt eine gesonderte gesetzliche Entscheidung zur Bedarfswehrpflicht. [SGB VI § 35](https://www.gesetze-im-internet.de/sgb_6/__35.html) nennt 67 Jahre, [MiLoG § 1](https://www.gesetze-im-internet.de/milog/__1.html) verweist auf die Anpassungsverordnung vom 5. November 2025. Die konkreten Eurobeträge wurden hier nicht zusätzlich am Verordnungstext authentifiziert. Das Prüfergebnis ist keine Vollprüfung aller Rechtsbehauptungen in R8/R9.

## Entscheidungsvorlage und offene Grenzen

Die GESIS-Anfrage, der konditionierte Tabellenweg, die Zurückstellung von Quoten und die spätere ESS-Prüfung sind nachvollziehbare Optionen. Die Behauptung in Entscheidung 1:21, nur Anfrage A könne nationale Fragen öffnen, ist zu absolut: Option C ohne KI wird in Zeile 19 selbst genannt, bleibt aber ungeklärt. Bei Ablehnung der Ausnahme darf C als weiterhin klärungsbedürftige Option sichtbar bleiben. Auch IAB-OPAL bleibt laut R9:223,348 ein ungeklärter Suchweg. Daraus folgt kein zugesicherter Zugang und keine Aufforderung, Sperren zu umgehen.

Für Gruppenvergleiche ist das vorläufige Beibehalten der für alle Parteien gleichen Regel A vertretbar. Die daraus folgende ungleiche Sichtbarkeit muss sichtbar bleiben. B benötigt ausreichende sekundäre Unterdrückung; C eine vorher begründete Regel und neue Version. Keine spätere Änderung an bereits bekannten Referenzen als unangetastete Bestätigung darstellen. Die Statuszählungen und ihre Parteiverteilung wurden nicht geprüft.

Vor Festschreibung müssen F01-F03 korrigiert oder die jeweils abhängigen Kandidaten/Aussagen ausdrücklich zurückgestellt werden. F04 kann als offene Terminbegrenzung bleiben. Wortlautrechte, vollständiger deutscher Feldkontext, SP557-Struktur, Quotenfreigabe, deutscher ESS12-Release und Gruppenvertrag sind legitime spätere Voraussetzungen, solange keine abhängigen Fragen aktiviert werden. Bei Q19 sind Mehrfachauswahl, Nichtauswahl, allgemeine exklusive Ablehnung und „Can't choose / Don't know“ getrennt zu behandeln. Eine selbst angefertigte deutsche Übersetzung wäre kein belegter Originalfeldwortlaut.

Die Textvarianten aus Entscheidung 4 sind nicht Teil des Manifests und wurden nicht geöffnet. Kein UI-/Handbuchreview, Browserlauf oder Verständnistest. Die andere aktuelle Methodenprüfung ist unbekannt. Die Checks mit `requiredInScope`, die vollständigen Findings und die Grenzen stehen maschinenlesbar im JSON.

## Gelesene Dateien und SHA-256

Bei gekürzten Werkzeugausgaben wurden für die Bewertung relevante Stellen erneut gezielt ausgegeben. Ein Hash aller Bytes bedeutet kein vollständiges Inhaltsreview der Datei.

| Datei | SHA-256 | Zugriff |
| --- | --- | --- |
| `docs/analyseplan-v2.3.entwurf.md` | `f708729867aec9ca187fe7646b21a69d2f4b89e5cdf831d3146051e06018fd94` | gezielt inhaltlich gelesen |
| `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md` | `b40c52f3bfbf0e8f5ed3ca2b7937c8d2d94b3949132273cd360c3aafba5e6de6` | gezielt inhaltlich gelesen |
| `docs/abdeckung-v2.2.md` | `618012f903783c749b751cb32c8acffab1e7ca09765cd80a26a2a2c1cbeb8b70` | gezielt inhaltlich gelesen |
| `docs/quellenanfragen-v1.entwurf.md` | `066be958b89b9dc198202c3599001b20d2f61c33d8b846ba8cc3e1405da708ca` | gezielt inhaltlich gelesen |
| `docs/analyseplan-v2.2.md` | `13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8` | gezielt inhaltlich gelesen |
| `docs/profilregeln-v1.md` | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.md` | `6830b4172d606b47fc6f00214fba09d776790143c85c01529b7c33256691c24b` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json` | `23e27dd8c2c1e359fe62ff5df058fef4de749dce95ca1e6da44cec6839e49fa2` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.md` | `42aaa648a36557d33b6bb316aff007f5f79f92779aa4875acdc74516c70ba5c3` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.json` | `71e012d3b460917269153d261a4565f6bfbb34627220ee2cf14d8abf1af272d6` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/R10-quellenblocker.md` | `65d79b32748197923c9614c7e8e85f19b06f516fa0cff869dbb7d3cf2f228885` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/R10-quellenblocker.json` | `8e15381892d91f62094c68573bb32148a5df21daf24ad11415549ef94861439a` | Hash und oberste Struktur/Schlüssel |
| `reports/claude/agenten/S1-strukturpruefung-eurobarometer.md` | `15b2851d4e383a50ae064b566b1f2d6419180d3899f20007b49c07fe607295c0` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/S1-strukturpruefung-eurobarometer.json` | `f563bc2f138d67a00a9cf8fbfd80580dd3e842108d17231b44efb241edbc9575` | Hash und oberste Struktur/Schlüssel |
| `reports/claude/agenten/R5-wvs.md` | `a163be6d448ab5f9e14b54293f355a2e0cea3c19d37e92a4d0021e8af7afc969` | nur Integrität, kein Inhaltsreview |
| `reports/claude/agenten/R6-eurobarometer.md` | `58b08b2af20d70261e95e7d0d815d4c083d95e0879cef5ee864c6ee05e84e8bb` | gezielt inhaltlich gelesen |
| `reports/claude/agenten/R7-weitere-quellen.md` | `4e795f355ccd359613949a2e307f46150f31506cf817b51f1a4e232405f6fcd5` | nur Integrität, kein Inhaltsreview |
| `reports/claude/auftraege/R-erweiterung-gemeinsam.md` | `56970a37d162e3996cace441b4f41c44d7e4e3bfd408d008c13e3f9ba0898ccd` | gezielt inhaltlich gelesen |
| `data/gruppenvertrag.v2.1.entwurf.json` | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` | Hash und oberste Struktur/Schlüssel |
| `AGENTS.md` | `6d405f6baff0b692edf657dae09c933b3ef978e2f3a98d3caaf14dc7666f627f` | gezielt inhaltlich gelesen |
| `docs/project.md` | `2ff27e5aa553ea2307bd4d28da436991c5ebb3b019f316d9aae95ee81d57696a` | Startfassung gelesen; hier späterer Bytehash nach externem Commit |
| `docs/pruefregeln.md` | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` | gezielt inhaltlich gelesen |
| `docs/lizenzen.md` | `b5b0303ec23bc4bbc8dba1f59994c9ccd7cd90c76474157399cf78d616753dcb` | gezielt inhaltlich gelesen |
| `reports/claude/auftraege/P5-plan-v23-quellen-fairness.md` | `fc392d6199546c89eaafec41447ba5be0fdcf35bc78bcf045a0aef6868746fa1` | gezielt inhaltlich gelesen |
| `reports/claude/pruefungen/PLAN-V23-001-manifest.json` | `c2c05725351ff209af158704d0896693fd480be66f4027b22125d97066566c89` | gezielt inhaltlich gelesen |
| `.claude/skills/life93-review/SKILL.md` | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` | gezielt inhaltlich gelesen |
| `.claude/skills/life93-review/references/urteil-schema.json` | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` | gezielt inhaltlich gelesen |
| `.agents/skills/unslop/SKILL.md` | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` | gezielt inhaltlich gelesen |
| `/home/stevenh/.codex/memories/MEMORY.md` | `76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9` | nur Verfahrenshinweise, keine fachlichen Belege |
| `/home/stevenh/.codex/memories/skills/bounded-pinned-review/SKILL.md` | `0e77a5f081bc588972fddd6e848d39fe5ae05fcf4e2833c3ef704221e90536c6` | nur Verfahrenshinweise, keine fachlichen Belege |

Die zuerst gelesene saubere Git-Fassung von `docs/project.md` hatte SHA-256 `9f827fdd40d5f9a4239043a5fb21ec84fa93805141566ac5b68e455a63d8bba6` (über `git show 6e164209…:docs/project.md` authentifiziert). Der oben genannte aktuelle Hash gehört zum extern weitergesetzten Stand. Das Dokument ist kein Manifestartefakt. Alle 19 Manifestartefakte wurden vor und nach der Bewertung erneut gegen die vorgegebenen Pins geprüft.

## Tatsächlich geöffnete Primärquellen

Abrufe am 4. Oktober 2026 MESZ. HTTP-200-Bytehashes aus Requests; externe Dateien wurden nur im Speicher verarbeitet, nicht in `outputs/` oder anderen Verzeichnissen gespeichert. OECD-Fragebogen: SHA-256 `5672381901f57dcc2ee3e76a9b0716b6c418c3a69e1e85b804e29bb2c343ae10`, PDF-S. 7,8,10,12,13 gelesen. Seiten 12/13 sind Fragebogen/Informationsexperiment, keine Ergebnistabellen. Datenportalabrufe gaben ausschließlich Lizenzmetadaten aus; keine Distribution geöffnet.

| Quelle | Abruf | SHA-256 der empfangenen Bytes |
| --- | --- | --- |
| [ESS_release](https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027) | HTTP 200 | `fd1f7663ca6e3a2e5d1daacfa291b41f8804824c3e807b6c570554a793ea4b96` |
| [PNOG](https://www.bundesgesundheitsministerium.de/service/gesetze-und-verordnungen/detail/pflegeneuordnungsgesetz-pnog) | HTTP 200 | `561b8ca6d92c2cfb2596e5228fa0585403a5c7b90e9ba37f713eaab171ed102b` |
| [GKV](https://www.bundesgesundheitsministerium.de/service/gesetze-und-verordnungen/detail/gkv-beitragssatzstabilisierungsgesetz) | HTTP 200 | `015882bf5044fd1a51feb6267445f71671e054251eb8620c6a3e07c90e5eec78` |
| [Grundsicherung](https://www.bmas.de/DE/Arbeit/Grundsicherung-fuer-Arbeitsuchende/FAQ-zur-Umgestaltung-der-Grundsicherung-fuer-Arbeitsuchende/faq-zur-umgestaltung-der-grundsicherung-fuer-arbeitsuchende.html) | HTTP 200 | `728dbede60115fa13933bd8e118e2cb096313f676c125151fc2320f94cd99ea7` |
| [Tariftreue](https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/gesetze-und-gesetzesvorhaben.html) | HTTP 200 | `10645a4222853798b36c90ad9e70560e2f5f5e976fe2faa3b6607a6222d3b57f` |
| [Wehrpflicht](https://www.gesetze-im-internet.de/wehrpflg/__2a.html) | HTTP 200 | `47f052f208d409bae0b56c0ca8c125f2ca064c31e44caa7e259842972b7ffd59` |
| [SOEP](https://www.diw.de/de/diw_01.c.1019277.de/soep-richtlinie_zur_nutzung_von_ki_und_grossen_sprachmodellen__llms.html) | HTTP 200 | `f2aefc5318ac9147663c7e507514b7ce06f0f5eac21f40506db945e2c47d66c2` |
| [OECD_archive](https://web.archive.org/web/20261003064505id_/https://www.oecd.org/en/about/terms-conditions.html) | HTTP 200 | `280015a7bbc3aefde3b7222acbba0194aea93f4b46f93020a6b4ee4d26d3bcc5` |
| [GESIS_archive](https://web.archive.org/web/20260330121100id_/https://www.gesis.org/institut/datennutzungsbedingungen) | HTTP 200 | `3ab9b3464a7ec3f5208dd4b53fbe69b9d2eb6b302d5fb1e536991ad647060a91` |
| [CC_BY_SA](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) | HTTP 200 | `47c0a954c88d793bdefe92fb007ae3c038fb3807f1a27083433d01aa7542c0d8` |
| [CC_BY_NC_SA](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en) | HTTP 200 | `527c4e0e75a7aafe819a9ed481c227f27645736fa800f25d6d94ed37a362afd7` |
| [UKDS](https://ukdataservice.ac.uk/app/uploads/cd137-enduserlicence.pdf) | HTTP 200 | `3b4f64adef7a1fc26cda578b9a552ef0ac487f2210a40d3a8933564f61f38738` |
| [EIB](https://www.eib.org/en/terms-of-use.htm) | HTTP 200 | `47aa5d5bfd207d64603c67fd056b65e8b611edb1c13a12d056cc7f7b95a82cac` |
| [ESS](https://www.europeansocialsurvey.org/contact/disclaimer) | HTTP 200 | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` |
| [WVS](https://www.worldvaluessurvey.org/AJDownloadLicense.jsp?DOID=6609) | HTTP 200 | `831617d5da598595f4e1d1dae4dcf6184c4e6f1ea02f6d4707e6dadccce7755a` |
| [EU-Lizenzmetadaten](https://data.europa.eu/api/hub/search/datasets/s3613_105_2_std105_eng) | HTTP 200 | `711ad18d2adc0c3de64cdf25eb6281a6ebb1d2ad05f3e537179e4a985ce472e7` |
| [EU-Lizenzmetadaten](https://data.europa.eu/api/hub/search/datasets/s3378_104_1_std104_eng) | HTTP 200 | `65c0508835c5cd2bc8741ad49b868ecaeed6e279e25ea77c376d77eed2b6e096` |
| [EU-Lizenzmetadaten](https://data.europa.eu/api/hub/search/datasets/s3413_103_2_sp564_eng) | HTTP 200 | `2b2fb575d81b8fb4c873e7b377664aa0562080c0ae1f8c61f9691386a34b55f9` |
| [EU-Lizenzmetadaten](https://data.europa.eu/api/hub/search/datasets/s3682_105_1_sp572_eng) | HTTP 200 | `52bd19b039d346cdaf912e63b49dda618fdb6bbaac4de1c5e4e8054640691c3e` |
| [EU-Lizenzmetadaten](https://data.europa.eu/api/hub/search/datasets/s3227_102_1_sp557_eng) | HTTP 200 | `5ffc620e7e5da65d9134bb4800214c30c719fdcc7775acbc7025bda7864d52d2` |

Zusätzlich über web.run gelesen: Kommissionshinweis, EUR-Lex-Beschluss als PDF, CC-Texte, MiLoG § 1, SGB II § 3a, SGB VI § 35, BMAS-Gesetzesvorhaben und Pew-Nutzungsbedingungen § 13. Für Werkzeugtext ohne empfangene Originalbytes kein Bytehash behauptet. Pew erlaubt Datenauszüge mit Attribution und weiteren Bedingungen; kein Konto eingerichtet.

Fehlgeschlagene oder unvollständige Abrufe: web.run bei ESS/WVS/ESS-Release (502 oder nicht zugänglich), WPflG und SOEP (Timeout); EUR-Lex HTML (Botprüfung) und Requests HTML/PDF (202, leer); OECD live (403); recht.bund.de GKV-PDF (403). Die tragenden Aussagen wurden danach über erfolgreiche Primärabrufe, Originalarchivkopien oder den EUR-Lex-PDF-Werkzeugtext geprüft. Suchanfragen nach vier Gesetzesständen lieferten überwiegend sekundäre Treffer; sie wurden nicht als Beleg verwendet. Keine ungefragt sichtbaren politischen Befragungsergebnisse festgestellt.

## Befehle, Kontrolle und Laufzeit

Ausgeführt, jeweils lesend oder nur für meine zwei Ausgaben:

- `pwd`, `git status --short`, `git rev-parse HEAD`, `git branch --show-current`; abschließend dieselben Zustandsabfragen.
- `sha256sum reports/claude/pruefungen/PLAN-V23-001-manifest.json`; Python/Hashlib prüfte dessen vorgegebenen Hash, verbotene Pfadpräfixe, alle 19 Artefakthashes und das anfängliche Nichtvorhandensein meiner Ausgaben.
- `cat`, `nl -ba`, `sed -n`, `rg -n`, `wc -l` ausschließlich auf den oben benannten lokalen Dateien; JSON-Parsing der manifestierten Struktur und gezielte Projektion der Kandidatenfelder.
- `python3 -` mit Requests/BeautifulSoup: erlaubte Primär- und Archiv-GETs, HTTP-Status, SHA-256 und gezielte Textauszüge; Archivabrufe mit `allow_redirects=False`. Metadaten-JSON nur auf Lizenzfelder projiziert.
- `pdftotext -layout - -` über stdin/stdout für den OECD-Fragebogen und den UKDS-Lizenztext; keine temporären Quelldateien angelegt.
- `git log -3 --format='%H %s'`, `git diff --name-status 6e164209… HEAD`, `git show 6e164209…:docs/project.md` nur zur Herkunft des externen Commit-/Projektdateiwechsels.
- Modulprobe: Requests und BeautifulSoup verfügbar; jsonschema und pypdf nicht installiert; pdftotext verfügbar. Ein zu eng begrenzter eigener JSON-Metadatenabruf scheiterte beim Parsen abgeschnittener Werkzeugausgabe; unverändert mit größerem Ausgabebudget erfolgreich wiederholt.
- `apply_patch` schrieb ausschließlich `P5-quellen-fairness-v23.md` und `.json`. In-Memory-Validierung des JSON gegen das vollständige gelesene Skill-Schema, semantische Statuskontrolle, erneuter Vergleich aller Paketpins und `git diff --check` für meine Ausgaben.

Keine Commits, Pushes, Tags oder Nachrichten. `pnpm check` und v2.2-Unittests wurden nicht ausgeführt: Es wurde keine Produkt-/Rechendatei verändert; ein allgemeiner Testlauf würde zudem den ausdrücklich begrenzten Lesekorpus nicht sichern. Die hier ausgeführte Formalkontrolle ist keine methodische oder empirische Abnahme.

Modell laut expliziter T3-Laufzeit: OpenAI `gpt-6.1-sol`, Codex-Harness, high reasoning effort. Interne Revision unbekannt. Keine Claude-Prüfung und keine unabhängige zweite Modellfamilie. Ursprüngliche Nutzeranweisung und vollständiger Datei-Auftrag sind im JSON unter `execution.prompt` erhalten.
