# INVENTORY-004-E: unabhängige Reproduzierbarkeits-Erstprüfung

Erstbericht vom 2026-10-03. Rolle: frischer Reproduzierbarkeitsprüfer, kein Quellenautor. Der Bericht wird nach Abschluss samt SHA-256 eingefroren. Er enthält keine Autorantwort und keine Zusammenführung mit einem anderen Erstbericht.

Die zwei eigenen vollständigen Builds sind bytegleich mit der eingefrorenen öffentlichen JSON. Alle 808 Belegketten und 1.772 Referenzen sind nachvollziehbar. Die 32 technischen Identitäten und ihre gedruckten Fragebogen-Code-/Labelzeilen stimmen mit den selbst gelesenen Originalseiten überein. Die sieben Autorenmutationen wurden tatsächlich verändert und erneut abgewiesen. Die weitergehende Gegenprüfung findet allerdings zwei Lücken im Testschutz und einen kleinen Unterschied zwischen sichtbarer Lesefassung und PDF-Textlage. Diese Findings begründen keine gescheiterte empirische Analyse. Eine solche Analyse gehört nicht zu diesem Paket.

## Geprüfte Fassung und Abnahmegrenzen

Manifest: `reports/loop/packages/INVENTORY-004-E/v1/manifest.json`, SHA-256 `0d124297e3410fd108dfeb1a676cb55a9562f4aa1b5e5adc52f8ddf95de66958`. Das Manifest nennt Code-Commit `60414205eba970c5832e8ad130bb43215f0a7da6`. Alle zehn gefrorenen Dateien und 74 Source-Inputs wurden vor und nach der Prüfung gegen Hash, Bytezahl, erlaubten relativen Pfad und aufgelösten Zielpfad geprüft. Die konkrete Inputliste steht im eigenen `input-hashes-before.json` und `input-hashes-after.json`. Keine Quelle ist aus einem fremden Reviewurteil abgeleitet.

Öffentliche JSON: `data/inventar-e.ergaenzung.entwurf.json`, SHA-256 `2c7ef03dca2585bf6476eabf46f8508b3430666d30f07283bc84cd6b1978a224`, 2.064.684 Bytes. Der vollständige gefrorene Autorenbericht trägt SHA-256 `ae291d2ef209840b40f021949a79420992b68a533a8ff76af276d3c233c377ac`.

Die unveränderte Grundlage enthält 296 technische Zeilen, davon 32 E-Identitäten. Die ursprüngliche Pending-Regel aus `pipeline/inventar.py:610–628` ergibt 205 Zeilen. „296/205“ bezeichnet keine zweite CSV und keine wissenschaftliche Vollständigkeitsprüfung. Das wurde bei einer rein operativen Pfadklärung durch Root erläutert und anhand der erlaubten technischen CSV-Felder überprüft. Vor der Klärung habe ich zusätzlich Hash und technische Zeilenzahl eines historischen öffentlichen Inventar-Snapshots kontrolliert. Auch dieser enthält 296 Zeilen. Keine Fremdbewertungen wurden dabei gelesen. CSV, Provenienz und Parser sowie die anderen Ergänzungsdateien blieben unverändert; ihre Hashes stehen getrennt im Schutzprotokoll.

| Prüfbereich                                                 | Tatsächliches Urteil                      | Geltung                                                                                                                                      |
| ----------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Paketintegrität, SafePath und öffentliche Inputs            | BESTANDEN                                 | Zehn gefrorene Dateien und 74 Source-Inputs dieser Fassung.                                                                                  |
| Eigener zweimaliger vollständiger Nachbau                   | BESTANDEN                                 | Beide Builds unter ausschließlich eigenen Schreibpfaden; bytegleich zur gefrorenen JSON.                                                     |
| Alle Belegketten und Referenzen                             | BESTANDEN                                 | 808 Rechteck-/Token-/Extrakt-/Hashketten und 1.772 auflösbare Referenzen.                                                                    |
| Gedruckte Fragebogen-Zellen und aktuelle Filterannotation   | BESTANDEN                                 | Alle 32 Identitäten; eigene Originallektüre und zusätzlicher geometrischer Abgleich.                                                         |
| Sieben benannte Autorenmutationen                           | BESTANDEN                                 | Wirkliche Deltas, bytegleiche eigene Kandidaten und identische tatsächliche Fehlermeldungen.                                                 |
| Weitergehender Schutz gegen semantisch falsche Bindungen    | NICHT_BESTANDEN                           | Vier zusätzliche verfälschte Kandidaten werden vom Autorenprüfer akzeptiert; E-R01 und E-R02.                                                |
| Exakte als sichtbar bezeichnete Listenlesefassung           | NICHT_BESTANDEN_IM_KLEINEN_FORMALEN_PUNKT | Schlusszeichen auf Liste 58; E-R03. Keine veränderte Kategorienbedeutung festgestellt.                                                       |
| Individuelle Formatprüfung eigener Bericht-/JSON-Dateien    | BESTANDEN                                 | Ignoreliste ausdrücklich aufgehoben; tatsächliche Dateiverarbeitung protokolliert.                                                           |
| Gesamtprüfung mit `pnpm check`                              | NICHT_GEPRUEFT                            | Durch den engeren Erstprüfauftrag ausdrücklich untersagt; hier nicht gestartet. Der dokumentierte Autorenlauf brach zuvor im Formatcheck ab. |
| Browser- und UI-Prüfung                                     | IN_DIESER_PHASE_NICHT_ERFORDERLICH        | Keine Oberfläche geändert oder freigegeben.                                                                                                  |
| Eignung, Polung, Neutralität und Messmodell                 | NICHT_GEPRUEFT                            | Getrennte Folgeabnahmen bleiben offen.                                                                                                       |
| Ausgabe 4.2, CAPI-Ausführung und empirische Inventarabnahme | NICHT_GEPRUEFT                            | Keine Antwortdaten, Programme oder Interviewlaufprotokolle untersucht.                                                                       |

## Originallektüre und Quellenbindung

Ich habe die deutschen Fragebogenseiten 43–54, die Listen 50–67 auf Listenheft-PDF-Seiten 51–68 und die Codebook-E-Abschnitte auf PDF-Seiten 208–218 selbst textuell und visuell gelesen. Alle 41 Seiten wurden frisch aus den gepinnten PDFs in den eigenen Outputbereich gerendert. Die Fragebogenseiten tragen dieselbe gedruckte Seitenzahl; Codebook-Seiten tragen jeweils PDF-Seite minus eins; das Listenheft druckt hier keine Seitennummer. Eine zusätzliche hoch aufgelöste Originalseitenregion klärt E-R03. Die Render- und Extraktionsaufrufe stehen im eigenen `reading-command-log.json`.

Die Quellen sind [deutscher Fragebogen ESS11/2023](../../../outputs/loop/inventory004-e/ESS11_questionnaires_DE.pdf), [deutsches Listenheft ESS11/2023](../../../outputs/loop/inventory004-e/ESS11_showcards_DE.pdf) und [Codebook integrierte Ausgabe 4.1](../../../outputs/loop/inventory004-e/ESS11_appendix_a7_e04_1.pdf). Die dazugehörigen offiziellen Original-URLs sind in der gefrorenen JSON gepinnt. Ich habe keinen neuen Netzabruf als eigenen Quellenzugriff ausgegeben. Meine Prüfung betrifft die eingefrorenen, vom Autor öffentlich abgerufenen Originalbytes.

| Quelle                      | SHA-256                                                            |
| --------------------------- | ------------------------------------------------------------------ |
| ESS11-DE-QUESTIONNAIRE      | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| ESS11-DE-SHOWCARDS          | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| ESS11-CODEBOOK, Ausgabe 4.1 | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |

Die zehn gefrorenen Dateien wurden vollständig gelesen beziehungsweise, bei der vollständigen JSON, strukturell geladen, für jede Identität ausgelesen und vollständig durch die Belegprüfung verfolgt. Hinzu kamen Projektstand, Belegregister, Entscheidungen sowie die PDF- und Unslop-Skills. Anforderungen wurden aus gefrorenem AGENTS, LIFE-93-Issue, Dauerauftrag, Prüfregeln, Analyseplan, Analyseanforderungen, Lizenzen und dem E-Prüfauftrag übernommen. Der engere Erstprüfauftrag verbietet das Lesen von Loopzustand, aktuellen Fremdreviews und zusätzlichen Verteidigungen sowie Commits, Pushes und Gesamtprüfungen; diese Grenze wurde eingehalten. Die anfängliche Dateiinventur und `git status` zeigten auch fremde Dateinamen, aber deren Berichtsinhalte wurden nicht geöffnet. Es wurden keine Agentlisten abgefragt und keine weiteren Agents gestartet.

Der öffentliche Scope wurde anhand der erlaubten Pfade, Dateiarten und tatsächlichen Quellen-/Skript-/Kandidatenstruktur kontrolliert. Die Source-Inputs bestehen aus öffentlichen PDFs, deren Text-/Geometrieextrakten und Renderings, einer öffentlichen ESS-Lizenzseite, Annotationen, synthetischen Mutationen und technischen Protokollen. Die originalen und eigenen PDF-Kopien sind bytegleich. Diese Kontrolle beansprucht keine allgemeine Prüfung aller Repositorydateien.

## Selbst geprüfte besondere Quellenstellen

- E1: Fragebogenseite 43 druckt 1, 2, 3 und 8. Liste 50 nennt die Verweigerungsoption ohne gedruckten numerischen Code. Die Annotation erfindet keinen Code. Codebook-PDF-Seite 208 nennt die deutsche Anonymisierung und verweist auf Country documentation; ihre konkrete Umsetzung in Datenedition 4.2 ist hier nicht belegt.
- E6/E7: Fragebogenseite 45 verlangt eine zufällig erzeugte Reihenfolge. Beide Items behalten getrennte Selbstbeschreibungen. Daraus folgt weder eine beobachtete CAPI-Ausführung noch eine komplementäre oder politische Skala.
- E8M/E8W sowie E9–E11M/W: Die deutschen Filter auf Seiten 46–48 und die Codebookfilter auf Seite 211 stimmen für die Männerformulierung mit E1 = 1 und für die Frauenformulierung mit E1 = 2 überein. Gemeinsame Variablen führen die getrennten technischen Formulierungen zusammen, ohne ihren gedruckten Ablauf zu beseitigen.
- E9–E11: Antwort 4 ist ein eigener fehlender Erfahrungsbezug, nicht Antwort 3, Verweigerung oder Skalenmitte. Die deutsche medizinische Kategorie 4 enthält tatsächlich die auffällige positive Formulierung „habe versucht“. Codebook-Seite 211 druckt eine englische Formulierung mit fehlendem Arztbesuch beziehungsweise Behandlungsversuch. Die bei `unfairly treated` gedruckte Referenz 86 ist sichtbar. Ich habe ihren zugehörigen Erläuterungstext nicht aufgelöst. Die Annotation lässt beide Probleme offen; keine Bedeutungsreparatur oder empirische Missingentscheidung bestätigt.
- E12/E13: Die gemeinsame Einleitung auf Seite 49 gilt für die beiden genannten Situationen und trägt den aktuellen Deutschlandbezug. E14 stellt die eigene allgemeine Polizeifrage. Die drei Kategorien benennen eine Richtung der wahrgenommenen Behandlung und Gleichbehandlung, ohne durch ihre Codefolge eine ordinale Einstellungsachse zu begründen.
- E20: Seite 52 enthält das vollständige Paarbeispiel mit Vollzeitarbeit, ungefähr gleichem Einkommen, neugeborenem Kind und Anspruch auf bezahlte Elternzeit. Dieser Kontext ist vorhanden.
- E26: Liste 66 auf PDF-Seite 67 enthält die Definition mit verbalem, nonverbalem und körperlichem Verhalten, anzüglichen Bemerkungen/Gesten und unerwünschten Berührungen. Die vollständige Definition ist im Itemkontext und Listenobjekt erhalten.
- E2–E8, E9–E14, E15–E18, E19–E22 und E23–E28 haben unterschiedliche Antwortgegenstände. Die Autorenbeschreibung trennt Selbstbeschreibung, persönlich empfundene Erfahrung, wahrgenommene Lage, bewertete Folgen, Maßnahmen/Sanktionen und geschlechtsbezogene Zuschreibungen. Auch E25-Lohnwahrnehmung, E27-Schutzforderung und E28-moralische Zuschreibung bleiben verschieden. Gemeinsame Einleitung oder Skala wird nicht als umfassende Gender-Dimension freigegeben.

Die öffentliche ESS-HTML-Quelle mit SHA-256 `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` wurde unabhängig als HTML gelesen. Unter [Conditions of use](https://www.europeansocialsurvey.org/contact/disclaimer) stehen die getrennten Daten- und Dokumentationslizenzen, die in der JSON genannt sind. Auch die Dokumentationszitation und ihr Studien-DOI wurden im Originalabschnitt nachgelesen. Die konkrete lokale Extraktdatei stimmt mit ihrem Hash überein. Datenlizenz CC BY-NC-SA 4.0 und Dokumentationslizenz CC BY-SA 4.0 werden getrennt geführt. Attribution, Dokumentversionen und Bearbeitungshinweis sind vorhanden. Eine spätere Exportfassung und ihre Veröffentlichung bleiben gesondert zu prüfen. Dies ist keine rechtsfachliche Freigabe.

## Eigener Nachbau und Gegenprüfung

Die originalen drei Skripte wurden niemals an ihren Livepfaden gestartet. Ich habe sie bytegleich in `outputs/loop/inventory004-e-repro/sandbox/outputs/loop/inventory004-e/` kopiert. Dadurch löst ihr vorhandener `Path(__file__).resolve().parents[3]` ausschließlich auf die eigene `sandbox/` auf. CSV und Provenienz, gepinnte Baseline-PDF-Pfade, die drei eigenen PDF-Kopien, Lizenz-HTML und Lizenzextrakt sowie die gefrorene öffentliche JSON wurden ebenfalls unter genau diesen relativen Pfaden kopiert. Es gab keine inhaltliche Codeänderung der drei Autorenskripte.

Vor dem Start wurden ROOT, OUT, Default-Target, PUBLIC, PDF-Cache, Mutationsziel, Logziele und beide Reproduktionsziele gelesen und auf den eigenen absoluten Bereich aufgelöst. `path-inspection.json` bestätigt alle Schreibziele. „sandbox“ ist dabei lediglich der Name meiner eigenen Pfadkopie; keine Betriebssystem-Zugriffssperre wurde eingerichtet. `pnpm exec prettier` fand aus diesem Verzeichnis den bestehenden Formatter 3.8.1. Keine Installation fand statt.

Der Aufruf des eigenen `reproduce.py` führte zweimal den vollständigen eigenen `build.py` aus. Beide Läufe endeten mit Exit 0. Beide erzeugten 32 Identitäten und 808 Belege, denselben SHA-256 wie die gefrorene JSON und vollständige Bytegleichheit. Auch die eigene Kopie von `read-tests.py` endete mit Exit 0. Exakte Befehle, CWD, stdout, stderr und Exits stehen in `command-log.json` und im eigenen `sandbox/outputs/loop/inventory004-e/reproduction-result.json`.

Die zusätzlich selbst geschriebene `audit.py` extrahiert die Original-PDFs unabhängig neu. Sie verfolgt sämtliche 808 registrierten Rechtecke, Originaltokens, Extrakte, SHA-256 und gedruckten Seiten sowie alle 1.772 Belegverweise. Die zusätzliche Zellprüfung findet die gedruckten E-Fragekennungen direkt im Original und gewinnt daraus die Seiten- und Fragebereiche; sie übernimmt nicht die Builder-SPECS. Zu jeder gedruckten Codezeile prüft sie das konkrete Code-Token und alle links davon in derselben vertikalen Zeile gehörenden Labeltokens einschließlich Fortsetzungen. Ein bloß vorhandenes Wort auf derselben Seite genügt nicht. Vollständige Originalkontexte, erwartete Filter, Listenpositionen und sichtbare Kategorien werden zusätzlich gegen die selbst gelesenen Quellen geprüft. Codebook-Variablenanfänge, offizielle Locations und alle gedruckten englischen Antwortzeilen wurden getrennt kontrolliert.

Die sieben Autorenkandidaten wurden vollständig geladen und rekursiv gegen die gefrorene JSON verglichen. Jeder hatte tatsächlich ein Delta. Eigene Kandidaten aus der eigenen Skriptausführung stimmen jeweils mit dem Originalkandidaten überein; Hash und identische konkrete Fehlermeldung wurden erneut geprüft. Die Einzelpfade des Deltas und tatsächlichen Fehler stehen in `author-mutations-independent.json`.

Fünf weitere vollständige synthetische Kandidaten wurden nur im eigenen Bereich geschrieben. Der Autorenprüfer wurde ausschließlich aus seiner eigenen Kopie importiert. Vier falsche Kandidaten akzeptiert er, den Listenwechsel E11W auf E10W weist er ab. Der unabhängige Zusatzprüfer weist alle fünf ab. Er lässt beim Mutationstest nur den separat berichteten, bereits bekannten Schlusszeichenunterschied auf Liste 58 passieren, damit dieser den später geprüften Gegenfall nicht verdeckt. Die unveränderte Ausgangsfassung wurde zuvor ausdrücklich im strikten Modus geprüft; E-R03 blieb dabei sichtbar. Ein Durchlauf mit dieser eng benannten Ausnahme ist keine vorbehaltlose Abnahme der Lesefassung.

| Eigener Gegenfall                           | Tatsächlich veränderte Bindung                                                     | Autorenprüfer                             | Eigener Zusatzprüfer                   |
| ------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------- |
| E12-referenzierte-labelzellen-vertauscht    | Beide vollständigen Labelobjekte mit Text und Belegverweisen zu Code 1/2 getauscht | AKZEPTIERT                                | ABGEWIESEN: falsche Original-Codezeile |
| E8W-direktfilter-entfernt                   | Direktfilter-Kontext entfernt; übrige Quellen unverändert                          | AKZEPTIERT                                | ABGEWIESEN: notwendiger Kontext fehlt  |
| E19-sichtbare-listenpole-vertauscht         | Erste und letzte sichtbare Kategorie auf Liste 64 getauscht                        | AKZEPTIERT                                | ABGEWIESEN: sichtbare Listenlabels     |
| E8M-codebookfilter-und-zuweisung-veraendert | Männerzuweisung auf E1 = 2 und ungebundener Codebookfiltertext passend verfälscht  | AKZEPTIERT                                | ABGEWIESEN: Originalvariantenfilter    |
| E11W-liste57-durch56                        | Vollständige Listenannotation durch E10W-Liste ersetzt                             | ABGEWIESEN: Frage fehlt im Originalheader | ABGEWIESEN: falsche Listenposition     |

## Findings

### E-R01: konsistent vertauschte Labels und sichtbare Listenlabels umgehen die Testbindung

Betroffene Aussage ist der technische Schutz von Frage-/Code-/Labelbezügen und Listenlesefassungen durch `read-tests.py`. Originalfundstellen: deutscher Fragebogen Seite 49, E12-Codezeilen 1/2; Liste 64 auf Listenheft-PDF-Seite 65. Registrierte Belege sind `E12-code-1`, `E12-label-1`, `E12-code-2`, `E12-label-2` und `SC-L64-page`.

Der Prüfer gleicht den jeweiligen Labelwert nur mit dem im Kandidaten angegebenen Beleg ab und prüft für Code und Label lediglich dieselbe PDF-Seite. Die geometrische Zuordnung zur Codezeile fehlt. Tauscht der Gegenfall die vollständigen Labelobjekte einschließlich ihrer echten Belege, bleiben alle 808 Quellenketten korrekt und das falsche Richtungslabel wird akzeptiert. Ebenso prüft er den Inhalt von `sichtbare_kategorien_de` gar nicht. Vertauschte Pole von Liste 64 werden akzeptiert, obwohl Header, Seite und Rohbeleg weiterhin korrekt sind. Beide Gegenfälle wurden tatsächlich geschrieben und geprüft; Kandidatenhashes, Deltas und Ergebnisse stehen in `additional-mutations.json`.

Die aktuelle Fragebogenzuordnung wurde von mir selbst bestätigt; ich behaupte keine schon vertauschten E12-Codes in der eingefrorenen Fassung. Das Problem betrifft den Schutz künftiger Änderungen und die Reichweite eines positiven Lesetests. Er kann eine sachlich gegensätzliche Bindung passieren lassen. Schwere: mittel, weil eine erhebliche Bedeutungsänderung technisch als bestanden erscheinen könnte, während die geprüfte Fassung überwiegend richtig gebunden ist und ausdrücklich Entwurf bleibt.

Korrektur: Fragebereich, Codezelle und zugehörige Labelregion geometrisch verbinden; Quellverweise nicht allein anhand des veränderten Kandidaten akzeptieren. Für die sichtbaren Listenfassungen einen separat versionierten, unabhängig an den Renderings geprüften Transkriptionsvertrag einführen oder ihren Inhalt ausdrücklich außerhalb des automatischen Prüfumfangs führen. Nachprüfung: beide hier erhaltenen Gegenfälle müssen scheitern; alle 32 ursprünglichen Code-/Labelbindungen und 18 Original-Listenfassungen erneut prüfen. Zwei Builds müssen weiterhin bytegleich sein.

### E-R02: Kontextvollständigkeit und Codebookfilterwortlaut sind nicht geschützt

Betroffene Aussage ist die automatische Kontext-/Filter- und Variantenprüfung. Originalfundstellen: deutscher Fragebogen Seite 47, E8W-Direktfilter mit E1 = 2; Seite 46, E8M-Direktfilter mit E1 = 1; Codebook-PDF-Seite 211, Filter zu `impbemw`. Registrierte Belege sind `QCTX-E8W-filter`, `QCTX-E8M-filter` und `CB41-impbemw-filter`.

Der Kontextloop prüft nur noch vorhandene Einträge. Entfernt der Gegenfall den kompletten E8W-Direktfilter, entsteht keine Fehlermeldung. Bei Varianten prüft der Autorentest außerdem den Zuweisungswert gegen `cb['filter'][0]['wert']`, ohne diesen Filterwortlaut mit seinem echten Belegextrakt abzugleichen. Eine gemeinsam verfälschte E8M-Zuweisung und ein passend veränderter Codebookfiltertext werden deshalb akzeptiert, während der echte Originalbeleg unverändert E1 = 1 zeigt. Die beiden Kandidaten, tatsächlichen Deltas und Ergebnisse sind in `additional-mutations.json` erhalten.

Die aktuellen Filter in der gefrorenen Annotation stimmen mit der Originallektüre überein. Der Fehler ist die Möglichkeit, fehlenden Kontext und konsistent verfälschte Quellenmetadaten als bestanden zu behandeln. Das kann die Zugangsbedingungen eines Items verändern. Schwere: mittel, weil Filter für die Antwortpopulation und spätere Webübertragung erforderlich sind, der aktuelle Quellenentwurf aber die richtigen Filter noch enthält.

Korrektur: je Identität die erforderlichen Kontexte und deren Geltung aus einem unveränderten Originalablauf prüfen; den konkreten Codebookfilterwert an seinen Originalextrakt binden. Die Zuweisung zusätzlich gegen die deutsche Originalfilterbedingung prüfen. Nachprüfung: Entfernung von Direkt- und übernommenen Filtern, Entfernung der gemeinsamen E12/E13-Einleitung sowie gemeinsam verfälschte Filter/Zuweisungen müssen Fehler erzeugen. E6/E7-Anweisung, E20-Vignette und E26-Definition müssen weiterhin vollständig bleiben. Kein Test darf dadurch tatsächliche CAPI-Ausführung behaupten.

### E-R03: sichtbare Lesefassung von Liste 58 übernimmt ein nicht sichtbar gerendertes Schlusszeichen

Betroffene Felder sind `listenheft.sichtbare_kategorien_de.wert[2]` bei E12 und E13, als `VISUELL_GELESENE_TRANSKRIPTION_REVIEW_OFFEN` bezeichnet. Originalfundstelle ist Liste 58, Listenheft-PDF-Seite 59, dritte Kategorie. Die vollständige Originalseite und ihr Beleg `SC-L58-page` wurden geprüft.

Die PDF-Textlage enthält am Ende das Token `behandelt.` bei X 209.070–293.130 und Y 339.258300–363.828300. Die frisch gerenderte sichtbare Kategorie endet dagegen ohne erkennbaren Punkt. Das wurde zusätzlich in einer Originalseitenregion mit 200 dpi überprüft. Der Textlayer-Beleg ist als solcher richtig erhalten; er ist aber kein Beweis des exakt sichtbaren Schlusszeichens. Die als sichtbar bezeichnete Lesefassung übernimmt den Punkt in beiden Listenobjekten. Die Quelle des Unterschieds im PDF wurde nicht geklärt; eine bestimmte Ursache wird nicht behauptet.

Wirkung ist eine minimale formale Abweichung des angeblich sichtbaren Originals. Die Kategorienbedeutung, Codes und Filter ändern sich dadurch nicht. Schwere: niedrig. Der Befund illustriert allerdings konkret die Grenze zwischen PDF-Tokenlage und sichtbarer Lesefassung.

Korrektur: den Punkt in der sichtbaren Lesefassung entfernen oder den Unterschied ausdrücklich als ungeklärte sichtbare Transkriptionsgrenze dokumentieren; den originalen Roh-Tokenextrakt unverändert behalten. Nachprüfung: Liste 58 frisch aus denselben Originalbytes rendern und beide E12/E13-Listenobjekte gegen die sichtbare dritte Kategorie prüfen. Das darf keine nachträgliche Reparatur anderer Originalformulierungen auslösen.

## Werkzeuge, Befehle und Laufgrenzen

Modell gemäß Startauftrag: geerbtes Codex `gpt-6.1-sol`, Reasoning `ultra`, keine Modellüberschreibung. Interne Anbieterrevision und nicht offengelegte Modellvorgaben sind unbekannt. Organisatorisch getrennte Erstprüfung derselben Modellfamilie ist ein KI-Audit, kein akademisches Peer Review, keine unabhängige Modellfamilienprüfung und keine Neutralitätsgarantie. Das Shared Filesystem stellt keine technische Reviewer-Sandbox bereit. Meine Pfadkopie isoliert Schreibziele, nicht Zugriffsrechte. Andere Arbeiten konnten gleichzeitig im Worktree stattfinden; positive Befunde beziehen sich ausschließlich auf die kontrollierten Hashes.

Angeboten waren Shell-/Dateiwerkzeuge, Web- und Bildwerkzeuge, Computer Use, Bildgenerierung, Zeitwerkzeuge, MCP-/Plugin-/Ressourcenwerkzeuge, Zielverwaltung und Collaboration. Tatsächlich genutzt wurden `functions.exec` mit `exec_command`, `write_stdin`, `apply_patch` und `view_image` sowie `collaboration.send_message` für die operative Pending-Zählungsfrage und die Abschlussmeldung. Keine andere Modellfamilie, keine weiteren Agents, kein Browser-/Portal-Analysis-Zugriff, keine Installation, kein Commit oder Push. Keine ESS-Rohdaten, lokalen Antwortdateien, Personenkennungen, A/B-Hälften, Partei-/Links-Rechts-Antwortwerte, Verteilungen, Zugangsdaten oder Secrets wurden gelesen oder ausgegeben.

Alle Shell-Aufrufe hatten das explizite Worktree-CWD. Die eigenen Reproduktions-Unterprozesse hatten das explizite CWD der eigenen Pfadkopie. Alle Patchziele waren absolut und lagen im erlaubten Worktree. Schreibziele beschränkten sich auf diesen Bericht und `outputs/loop/inventory004-e-repro/`. Die originale JSON, Pakete, Autorenoutputs, Parser, CSV und Provenienz blieben unangetastet. Die eigenen synthetischen Kandidaten enthalten öffentliche Dokumentationsannotation, keine Antworten.

Die relevanten ausführbaren Aufrufe und ihre vollständigen Ergebnisse sind in den eigenen `command-log.json`, `reading-command-log.json`, `independent-command-log.json` und `format-command-log.json` festgehalten. Die zwei Builderaufrufe, der Lesetest, alle 47 initialen Extraktions-/Renderaufrufe, der zusätzliche Renderausschnitt und die unabhängige Prüfung endeten mit Exit 0. Erwartete Gegenfall-`ValueError`s wurden kontrolliert aufgefangen und protokolliert. Der strikte Listencheck meldet ausdrücklich E12/Liste 58; er wird als nicht bestandene exakte sichtbare Transkription ausgewiesen, nicht als gescheiterter Skriptstart. Es gab keinen fehlgeschlagenen Nachbau und keine Installation zur Fehlerumgehung.

Weitere tatsächliche Shell-Lesungen waren `pwd`, `git branch --show-current`, `git status --short`, `rg --files`, `cat`, das Lesen der technischen Pending-Regel mit `sed`, `command -v` und eigene `python3`-Hash-/Strukturprüfungen. Sie endeten mit Exit 0. Einige umfangreiche kombinierte Toolausgaben wurden durch das Ausgabebudget gekürzt; die erforderlichen Anforderungen und Quellenseiten wurden danach einzeln vollständig gelesen. Dies wird nicht als ursprüngliche vollständige Toolausgabe ausgegeben. `git status` diente nur der Zustandskontrolle, nicht als Fremdberichtlektüre.

Der protokollierte Autoren-`pnpm check` endete mit Exit 1 wegen der Formatwarnung für die Koordinationsdatei. Seine nachfolgenden Handbuch-, Schema-, Typ-, Test- und Buildchecks wurden in diesem Aufruf nicht erreicht. Der Autor berichtet diese Grenze zutreffend. Ich habe keinen Ersatz-Gesamtlauf gestartet. Meine Formatprüfung hebt `.prettierignore` mit `--ignore-path /dev/null` auf, prüft die Parsererkennung und verarbeitet ausschließlich meinen Bericht sowie meine ausdrücklich benannten JSON-Ausgaben. Ein normaler Exit 0 auf ignorierten `data/`, `outputs/` oder `reports/loop/reviews/` wäre kein Formatnachweis.

## Offene Folgeabnahmen und Abschluss

Ausgabe 4.2 einschließlich Anonymisierung und Sondercodes, E1-Verweigerungszuordnung, die medizinische Kategorie-4-Bedeutung, Referenz 86, tatsächliche CAPI-Ausführung, endgültige Eignung/Ausschlüsse/Polung, Konstrukte, Neutralität, Messmodell, empirische Prüfungen, Webmodusübertragung und konkrete Veröffentlichung bleiben offen. Diese späteren Anforderungen wurden in dieser Erstprüfung weder ersetzt noch als heute gescheiterte Untersuchungen bewertet.

Der Erstbericht und sein eigener Index bilden die abgeschlossene organisatorisch getrennte Prüfung ab. Für die technischen Verbesserungen sind die erhaltenen Gegenfälle konkret nachprüfbar. Ein positiver Nachbau erteilt keine methodische oder öffentliche Freigabe.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger Reproduzierbarkeits-Erstprüfer INVENTORY-004-E, kein Autor. Ausschließlich Worktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, Branch research/life-93-night-20261003. Shell workdir explizit; ALLE apply_patch Ziele absolut im Worktree, toolcwd sonst Originalrepo. Paket reports/loop/packages/INVENTORY-004-E/v1/manifest.json SHA2560d124297e3410fd108dfeb1a676cb55a9562f4aa1b5e5adc52f8ddf95de66958,10files74sources. Lies sämtliche gefrorenen Anforderungen/Issue/AGENTS/Auftrag/Prüfregeln/Analyseplan/anforderungen/Lizenzen/E-Prüfauftrag/vollständigenAutorenbericht/neueJSON. Keine aktuellen Peerberichte/Loopfindings/Agentlisten/Verteidigungen oder weitereAgents. Eigene Dateien ausschließlich outputs/loop/inventory004-e-repro/ und reports/loop/reviews/INVENTORY-004-E-repro.md. Hash/SafePath/Publicscope10+74Inputs vor/nach. Alle32EIdentitäten/808Belegketten selbstnachverfolgen; wesentliche deutscheQ43–54/Listen50–67PDF51–68/CodebookE208–218Originalseiten selbsttextuellundvisuelllesen PDFSkill. Code/Label/Sonderantwort, Kontext/Filter, Variantenadministration, E1Refusalohnumerisch/Liste vsFrage, E8–11M/WE1Zuordnung, E6/7RandomisierungnurAnweisung, E9–11Kategorie4NichtErfahrung&auffälligerOriginalE9CodebookFootnote86, E12/13gemeinsameDEEinleitung/E14Antwortgegenstand, E20Vignette,E26Liste66Definition, unterschiedlicheAntwortgegenständekeineumfassendeGenderDimension. Zweimal eigener kompletter bytegleicherBuildernachbau aus exaktOwnumgebundenenKopien, allefestenROOT/OWN/TARGET/Cache/Log/ReproductionPfadeinspizieren bevorStart. NIEMALS originalBuild/read-tests/reproduce direktstarten; überschreibtLiveOutputs. Original296/205CSV/Parser/Provenienz/andereModule/Paket/AutorenOutputs bleibenunverändert. 7Autorenmutationen wirklichMutation/Kandidat/Fehlerprüfen; eigene zusätzlicheMutationen gegenLabels/Filters/Listen/Geometrie ggfValidatorGrenzenoffen, TokensalleinekeinSourcezellenbeweis. IndividuelleFormatchecknurmitwirklichverarbeitetenOwnDateien; data/outputs/reviewsPrettierignoriertExit0keinFormatbeweis. KeineESSraw/local/Personen/A/B/ParteiLRAntwortwerte/Verteilungen/PortalAnalysis/Creds/Secrets/globalWrites/CondaInstall/CommitPush/Gesamtformat/pnpmGesamtlauf. FinalEignungPolungNeutralität4.2Messmodell/empirischeInventarabnahmenbleibenoffen, SpäteresnichtalsgescheiterteAnalyseausgeben. E-RxxFindings präziseAussage/Originalfundstelle/Problem/Wirkung/begründeteSchwere/KorrekturkonkreteNachprüfung, Vermutungenklar, keineQuote. TatsächlichenStartauftragwortgetreu; Modellgpt-6.1-sol ultra geerbtkeineOverrides interneRevisionunknown, Toolsangebot/Nutzung/BefehleExitsFehlläufe/SharedFSkeinSandbox dokumentieren. Frischorganisatorischgetrennte gleicheCodexfamilieKI-AuditkeinakademischesPeerReview/Neutralitätsgarantie. ErstberichtimmutablevollständigabschließenSHA+eigenerIndexmeldend.
```

## Einzelabdeckung aller 32 Identitäten

Die Seiten und Zeilenanzahlen stammen aus den ausgeführten eigenen Prüfskripten. Leere Zwischenlabels sind bei den 0–6-Skalen tatsächlich unbeschriftete Originalzellen. Die Werte in dieser Tabelle sind technische Dokumentationsmetadaten.

| Identität | Offizielle Variable | Fragebogen-PDF | Liste | Original-Codezeilen | Codebook-PDF-Abschnitte |
| --------- | ------------------- | -------------- | ----- | ------------------- | ----------------------- |
| E1        | `nobingnd`          | 43             | 50    | 4                   | 208                     |
| E2        | `likrisk`           | 43             | 51    | 9                   | 208                     |
| E3        | `liklead`           | 44             | 51    | 9                   | 208, 209                |
| E4        | `sothnds`           | 44             | 51    | 9                   | 209                     |
| E5        | `actcomp`           | 45             | 51    | 9                   | 209, 210                |
| E6        | `mascfel`           | 45             | 52    | 9                   | 210                     |
| E7        | `femifel`           | 46             | 53    | 9                   | 210                     |
| E8M       | `impbemw`           | 46             | 54    | 9                   | 210, 211                |
| E8W       | `impbemw`           | 47             | 54    | 9                   | 210, 211                |
| E9M       | `trmedmw`           | 47             | 55    | 6                   | 211                     |
| E10M      | `trwrkmw`           | 47             | 56    | 6                   | 211                     |
| E11M      | `trplcmw`           | 48             | 57    | 6                   | 211, 212                |
| E9W       | `trmedmw`           | 48             | 55    | 6                   | 211                     |
| E10W      | `trwrkmw`           | 48             | 56    | 6                   | 211                     |
| E11W      | `trplcmw`           | 48             | 57    | 6                   | 211, 212                |
| E12       | `trmdcnt`           | 49             | 58    | 5                   | 212                     |
| E13       | `trwkcnt`           | 49             | 58    | 5                   | 212                     |
| E14       | `trplcnt`           | 49             | 59    | 5                   | 212, 213                |
| E15       | `eqwrkbg`           | 50             | 60    | 9                   | 213                     |
| E16       | `eqpolbg`           | 50             | 61    | 9                   | 213                     |
| E17       | `eqmgmbg`           | 51             | 62    | 9                   | 213, 214                |
| E18       | `eqpaybg`           | 51             | 63    | 9                   | 214                     |
| E19       | `eqparep`           | 51             | 64    | 7                   | 214                     |
| E20       | `eqparlv`           | 52             | 64    | 7                   | 214, 215                |
| E21       | `freinsw`           | 52             | 64    | 7                   | 215                     |
| E22       | `fineqpy`           | 52             | 64    | 7                   | 215, 216                |
| E23       | `wsekpwr`           | 53             | 65    | 7                   | 216                     |
| E24       | `weasoff`           | 53             | 65    | 7                   | 216                     |
| E25       | `wlespdm`           | 53             | 65    | 7                   | 216, 217                |
| E26       | `wexashr`           | 54             | 66    | 7                   | 217                     |
| E27       | `wprtbym`           | 54             | 67    | 7                   | 217                     |
| E28       | `wbrgwrm`           | 54             | 67    | 7                   | 217, 218                |
