# Inventarabschluss und Neunerbindung für die erste Prüffassung

Autorenfassung vom 2026-10-03, nach den beiden vollständigen getrennten Codex-Erstbewertungen. Das [neue Screeninginventar](../../../data/inventar.csv) erhält alle 296 gelieferten Identitäten in ihrer ursprünglichen Reihenfolge. Die [Neunerbindung](../../../data/item-core-v1.json) enthält ausschließlich B34–B36 und B40–B45 mit Originalwortlaut, Kategorien, Einleitungen, Druckfilter, Variablenkandidat, Quellenpins und einer ausführbaren Itemmap als Vorschlag. Keine Antwortdaten, empirisch freigegebene Dimension, Norm, Testfreigabe oder Phase-0-Abnahme entsteht daraus.

## Bestand, Ersturteile und Entscheidung

Die [Methoden-Erstbewertung](../reviews/ITEM-FIRST-001-methods.md) und die [Quellen-Erstbewertung](../reviews/ITEM-FIRST-001-sources.md) beurteilen jeweils den gesamten gebundenen Bestand. Die ursprünglichen CSVs und Berichte bleiben unverändert. Die neue CSV enthält pro Identität beide vollständigen Einzelurteile einschließlich Begründung, Geltung, Originalstatus, Fundstelle, Richtung und sachlichem Polinhalt. Die übernommenen Originalsichtfelder sind durch `originalsicht_` erkennbar; ergänzte Quellenkorrekturen stehen separat. Vorherige Autorenentscheidungen bleiben als historische Felder erhalten und gelten nicht als heutige Eignungsurteile.

| Erstbewertung | JA | NEIN | UNKLAR | Unveränderter CSV-SHA-256 |
| --- | ---: | ---: | ---: | --- |
| Methoden | 88 | 182 | 26 | `c5a0be5ffffbe65bafca137f882514e4a2a89c43bbb52b83031da890d67c6921` |
| Quellen | 103 | 181 | 12 | `efeed8790f2c0ee34b21ab1b087d812e8971e4fcb967b80ee1d4bf8adf9eeb56` |

Der [berechnete Urteilsabgleich](../ITEM-FIRST-001-agreement.json) weist 280 gleiche Eignungsurteile unter 296 Identitäten aus, beobachtete Übereinstimmung 0,945946 und ungewichtetes Cohens Kappa 0,895448. In der ergänzenden Vereinigung aller nicht-NEIN-Urteile stehen 115 Identitäten, 99 gleiche Urteile und Kappa 0,521954. Dieser Teilbestand ist durch die Urteile selbst ausgewählt und kein unabhängiger Genauigkeitstest. Beide Sitzungen gehören derselben Codex-Modellfamilie an. Parallele Formulierungen, Verwaltung und gemeinsame Modellfehler begrenzen diese Zahlen. Sie messen Urteilsübereinstimmung, keine Richtigkeit, politische Neutralität oder Validität.

Alle neun Kernidentitäten erhalten zweimal JA. Von den 88 Identitäten mit zweimal JA verbleiben somit 79 außerhalb des engen V1-Vorschlags. Ihr JA wird nicht zurückgenommen: Grundregeleignung, Messbegründung und Umfang der ersten Fassung sind getrennte Entscheidungen. Vertrauen, Zustandsbewertungen, Gendergegenstände und Portraitwerte sind dadurch weder unwahr noch empirisch ungeeignet. Die vorhandenen sachlichen Ausschlussgründe werden in der CSV als Umfangs-/Messgründe geführt. Nominale Gerechtigkeitskategorien bekommen keinen künstlichen kontinuierlichen Score; Zweierpaare bekommen keine erfundene dritte Frage; Portraitähnlichkeit wird ohne eigenen PVQ-Vertrag nicht zur relativen Wertpriorität. Einzelne Umverteilungs-, EU-, Autoritäts- und Maßnahmengegenstände ersetzen keine ungeprüfte homogene Batterie. Es werden keine Konstrukte zur Rettung einer Zielzahl ergänzt.

Die verbleibenden 287 Identitäten sind für V1 ausgeschlossen; das ist ein endgültig ausgefüllter Screeningentscheid für diesen Vorschlag, keine empirische Ablehnung ihrer Inhalte. Elf Identitäten bleiben bei beiden Erstbewertungen UNKLAR. Ihre Begründungen und offenen Originalstatus bleiben erhalten. Der V1-Vorschlag behauptet kein umfassendes politisches Profil und keine zwölf Dimensionen.

## Alle 16 Eignungsdissense

Für die enge erste Fassung werden alle strittigen Identitäten ausgeschlossen. Kein Mehrheitsurteil oder Kappa entscheidet die Grundregelgrenze. Die beiden Ersturteile bleiben lesbar, und die fachliche Ambiguität wird nicht zu NEIN umetikettiert. Keine dieser Identitäten gehört zu den neun Kernitems.

Q bezeichnet den deutschen Fragebogen; die genannten Q-Seiten sind zugleich Druckseiten. Kartenangaben beziehen sich auf das deutsche Listenheft.

| Identität | Quellen | Methoden | Originalfundstelle | V1-Entscheid und tragende Grenze |
| --- | --- | --- | --- | --- |
| B2 | JA | UNKLAR | Q5; Liste5, SC6 | Ausschluss. Institutionelle Mitsprachebewertung und persönliche Wirksamkeit beziehungsweise Regierungsbezug bleiben strittig. Der bloße Ausdruck „Regierung“ begründet keine aktuelle Regierungsbewertung. |
| C9 | JA | UNKLAR | Q19; Liste24, SC25 | Ausschluss. Nationale affektive Zugehörigkeit kann Orientierung oder persönliche Identitätsbeschreibung sein. Geringe Verbundenheit beweist keine Gegenideologie. |
| C10 | JA | UNKLAR | Q20; Liste24, SC25 | Ausschluss. Europa-Verbundenheit trägt dieselbe Orientierungs-/Identitätsgrenze; keine erfundene politische Gegenidentität. |
| C30 | UNKLAR | NEIN | Q26; Liste27, SC28 | Ausschluss. Physikalische Ursache/Wissen versus subjektiver Klimaglaube bleibt die Grenze. 55 ist eine substantielle Sonderantwort außerhalb der Ordnung 01–05. |
| C35 | JA | UNKLAR | Q28; Liste30, SC31 | Ausschluss. Erwartung künftigen Handelns anderer Menschen kann gesellschaftliche Haltung oder Tatsachenprognose sein. Zufallsformat erzeugt kein zusätzliches Konstrukt. |
| C36 | JA | UNKLAR | Q28; Liste30, SC31 | Ausschluss. Erwartung staatlichen Klimahandelns ist keine ausdrückliche Maßnahmenpräferenz und keine Bewertung eines benannten amtierenden Kabinetts. |
| C38 | JA | UNKLAR | Q29; Liste31, SC32 | Ausschluss. Dieselbe Haltung-/Prognosegrenze wie C35, mit anderem Antwortformat. |
| C39 | JA | UNKLAR | Q29; Liste31, SC32 | Ausschluss. Dieselbe Haltung-/Prognosegrenze staatlichen Handelns wie C36. |
| C41 | JA | UNKLAR | Q30; Liste32, SC33 | Ausschluss. Dieselbe Haltung-/Prognosegrenze anderer Menschen; keine zusätzliche unabhängige Frage aus der Skalenvariante. |
| C42 | JA | UNKLAR | Q30–31; Liste32, SC33 | Ausschluss. Dieselbe Haltung-/Prognosegrenze staatlichen Handelns; Fortsetzung und Filter bleiben Bestandteil des Originalgegenstands. |
| I2 | JA | UNKLAR | Q93; Liste90, SC95 | Ausschluss. Wiederholte Erwartung anderer Menschen trägt dieselbe Grenze; Qualitätstestkontext allein macht die Frage nicht zur Verwaltung. |
| I3 | JA | UNKLAR | Q93–94; Liste90, SC95 | Ausschluss. Wiederholte Erwartung staatlichen Handelns; kein neuer unabhängiger Messgegenstand. |
| I5 | JA | UNKLAR | Q94; Liste91, SC96 | Ausschluss. Wiederholung der Haltung-/Prognosegrenze anderer Menschen in anderem Format. |
| I6 | JA | UNKLAR | Q94–95; Liste91, SC96 | Ausschluss. Wiederholung der Haltung-/Prognosegrenze staatlichen Handelns in anderem Format. |
| I8 | JA | UNKLAR | Q95–96; Liste92, SC97 | Ausschluss. Dieselbe Haltung-/Prognosegrenze anderer Menschen. Die leere SC-Seitenangabe im Quellen-Ersturteil bleibt historisch erhalten; die Originalkarte ist SC97. |
| I9 | JA | UNKLAR | Q96; Liste92, SC97 | Ausschluss. Dieselbe Haltung-/Prognosegrenze staatlichen Handelns. Die leere SC-Seitenangabe im Quellen-Ersturteil bleibt historisch erhalten; die Originalkarte ist SC97. |

Drei Richtungs-Kategorien weichen ab: C30, D7 und D8. Bei C30 nennen beide Reviewer innerhalb 01–05 mehr Zuschreibung menschlicher Ursachen und schließen 55 aus dieser Ordnung aus. `STEIGEND` und `KEINE` beziehen sich somit auf unterschiedlichen Umfang. D7/D8 verbinden getrennte Getränkemengen mit Sondercodes; eine steigende Menge je Getränkeart ist keine einheitliche Ordnung des gesamten Blocks. 555 wird nicht zur Getränkemenge. Diese ausgeschlossenen Identitäten erhalten keinen V1-Score. Auch die 293 gleichen Richtungs-Kategorien beweisen keine semantisch gleichen Pole; beide Beschreibungen bleiben erhalten.

## Neun Originalitems und Itemmaps

Die deutsche Formulierung wird nicht paraphrasiert. `question_text_de` übernimmt die bereits deklarierte technische Reflowfassung; `original_wording_layout` erhält die Zeilenfolge. Die sichtbare Worttrennung „Familienmit-/glied“ bei B35 wurde bereits im Originalpaket für den Reflow zusammengefügt. Listenpräfixe und Interviewanweisungen sind separat gespeichert. Jedes vollständige historische Itemobjekt liegt unverändert in `original_package_snapshot`; sein alter Vorschlags-/Prüfstatus ist dadurch als Ausgangsstand dokumentiert und kein aktuelles Gateurteil.

Der öffentliche Druckablauf beginnt Modul B auf Q5 mit Staat und Politik. Das „AN ALLE“ vor B26 auf Q10 beendet den vorangehenden Parteifilter. Q13–16 enthalten für die neun Kernitems keinen zusätzlichen Personenfilter; der Migrationsvorspann auf Q15 gilt für B40–B45. Dieser begrenzte Druckabgleich ist keine nationale CAPI-Abnahme. Keine Parteireferenz wird aus dem früheren B25 übernommen.

| ID / Variable | Substantielle Codes | Map zum vorgeschlagenen hohen Inhalt | Q / Karte und SC-PDF | Codebook4.1 PDF / Druck |
| --- | --- | --- | --- | --- |
| B34 / `freehms` | 1–5 | `(5−x)/4`; mehr Zustimmung zur selbstbestimmten Lebensführung | Q13; Liste13, SC14 | 63 / 62 |
| B35 / `hmsfmlsh` | 1–5 | `(x−1)/4`; stärkere Ablehnung eigener hypothetischer Scham | Q13; Liste13, SC14 | 63–64 / 62–63 |
| B36 / `hmsacld` | 1–5 | `(5−x)/4`; mehr Zustimmung zu den genannten gleichen Adoptionsrechten | Q13; Liste13, SC14 | 64 / 63 |
| B40 / `imsmetn` | 1–4 | `(4−x)/3`; mehr Aufnahme der bezeichneten gleichen Volks-/ethnischen Gruppe | Q15; Liste16, SC17 | 65–66 / 64–65 |
| B41 / `imdfetn` | 1–4 | `(4−x)/3`; mehr Aufnahme der bezeichneten anderen Volks-/ethnischen Gruppe | Q15; Liste16, SC17 | 66 / 65 |
| B42 / `impcntr` | 1–4 | `(4−x)/3`; mehr Aufnahme aus ärmeren Ländern außerhalb Europas | Q15; Liste16, SC17 | 66 / 65 |
| B43 / `imbgeco` | 00–10 | `x/10`; positivere wirtschaftliche Folgenbewertung | Q16; Liste17, SC18 | 66–67 / 65–66 |
| B44 / `imueclt` | 00–10 | `x/10`; stärkere kulturelle Bereicherung | Q16; Liste18, SC19 | 67 / 66 |
| B45 / `imwbcnt` | 00–10 | `x/10`; Deutschland als besserer Ort zum Leben durch Zuwanderer | Q16; Liste19, SC20 | 67–68 / 66–67 |

Die zusätzlichen Codebook-Fortsetzungsseiten stehen ausdrücklich im neuen Binding. Das alte Neunerpaket referenzierte jeweils die Startseite; die ursprünglichen Angaben bleiben im Snapshot erhalten. Integrierte englische CARD-Nummern werden nicht als deutsche Listennummern ausgegeben.

Bei B35 ist `FALLEND` in beiden Ersturteilen korrekt auf mehr Zustimmung zur Schamaussage bezogen. Die vorgeschlagene Map ist `STEIGEND` zum anderen, ausdrücklich benannten hohen Inhalt: stärkere Ablehnung dieser Aussage. Code1 erhält 0, Code5 erhält 1. Keine Zustimmung zu Scham wird als hohe Rechtszustimmung ausgegeben. Bei B34/B36 erhalten Code1 den Wert1 und Code5 den Wert0. Bei B40–B42 bedeutet Code1 viele und Code4 niemanden erlauben. Geringer Umfang belegt keine allgemeine Feindseligkeit; hoher Umfang keine grenzenlose Aufnahme aller Menschen. Bei B43–B45 bleiben die originalen Gegenanker erhalten; die Zwischenstufen erhalten keine erfundenen Wortlabels oder bewiesene Neutralitätsbedeutung.

Die lineare 0–1-Abbildung behandelt die Kategorienabstände rechnerisch als gleich. Das ist eine eigene Scoringannahme aus dem Projektauftrag, kein aus dem Fragebogen bewiesenes Intervallniveau. Die Gruppen HOMO-3, MIG-AUF-3 und MIG-FOL-3 sind enge konkurrierende Messhypothesen. Keine Gesamtmittelung, Mindestantwortregel, Norm oder persönliche Unsicherheit ist in dieser Autorensynthese freigegeben. B35 bleibt eine hypothetische persönliche Reaktion; B34/B36 sind andere Antwortgegenstände. Herkunftsgruppen, Wirtschaft, Kultur und die breite Ortsbewertung bleiben unterscheidbar.

## Missing: gedruckte Antworten, Dateikonvention und Routing

Q13/Q15 drucken 7 für Verweigerung und 8 für Weiß-nicht; Q16 druckt 77/88. **9 beziehungsweise 99 sind in diesen deutschen Kernblöcken nicht gedruckt.** Das [ESS11-Datenprotokoll Edition1.5](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/source/ESS11_data_protocol_e01_5.pdf), Abschnitt C1, PDF-/Druckseite14, definiert 7/77 als Refusals, 8/88 als Don't know und 9/99 als No answer für anderweitig unerklärtes Missing. Diese Ebenen sind im JSON getrennt. Die Dateikonvention ergibt für die sechs kleinen Skalen `integrated_file_missing_codes=[7,8,9]` und für B43–B45 `[77,88,99]`. Damit ist weder ihr tatsächliches Vorkommen noch der Ausgabe4.2-Abgleich behauptet. Keine Missingantwort erhält einen Score.

Dasselbe Protokoll definiert 6/66 für wegen Routing unanwendbare Fragen. Die Codes stehen separat unter `protocol_not_applicable_codes`. Im gebundenen Kern-Druckablauf wurde kein solcher Personenfilter gefunden. Ein 6/66-Importwert ist deshalb als unerwartete Routing-/Metadatendifferenz zu melden und nicht still in eine zulässige Antwort oder gewöhnliche Kern-Nichtantwort umzuwandeln. Leere CSV-Zellen, `NA`, `NaN` und `.` sind nach äußerer Whitespace-Bereinigung lexikalisches Missing, keine Antwortkategorien. Das Binding behauptet nicht, dass jeder generische Code oder jedes Token tatsächlich in der Datei vorkommt.

## Tatsächliche Korrekturen und offene Quelldefekte

| ID | Befund am Original | Behandlung |
| --- | --- | --- |
| FI-C01 / D30 | Q41 als Text und Bild: Code1 „Ja, heute noch“, Code2 „Ja, früher einmal“. Codebook4.1 PDF200/Druck199 bestätigt currently/previously. Die eingefrorene Originalsicht weist Code1 falsch „Ja, früher einmal“ zu und lässt Code2 leer. | Die neue effektive Kategorienzelle ist korrigiert. Die ursprüngliche Zelle und Erstberichte bleiben erhalten. Nur diese Labels sind gezielt abgenommen; kein Gesundheits-Messitem und keine volle D30-/CAPI-Abnahme. |
| FI-C02 / E6 | Q45 als Text und Bild trägt E6. Eingefrorene Originalsicht, Grundinventar sowie Wortlaut-, Kategorien- und Kontextmetadaten nennen bereits45. Der Quellen-Erstbericht behauptet dagegen eine alte Originalsichtseite46. | Finale Fundstelle45 bestätigt. Keine erfundene Q46→45-Korrektur der eingefrorenen Zelle. Die unzutreffende Berichtsbeschreibung bleibt historisch sichtbar und wird hier begrenzt. Keine vollständige E6-Abnahme. |
| FI-O01 / D29 | Q41 druckt für01–11 tatsächlich „WEITER MIT D29“, also den Selbstsprung. CB200 nennt E28/CARD54, der deutsche Q41 D28/Liste46. | Offene nationale Routing-/CAPI-Frage. Keine ersatzweise Route erfunden; englische Referenzen nicht mit deutschem Druck gleichgesetzt. D29 bleibt als Gesundheitslage ausgeschlossen. |
| FI-O02 / E1 | Q43 enthält keinen gedruckten Verweigerungscode. SC51/Liste50 zeigt „Möchte nicht antworten“. | Offene Code-/Darstellungsdifferenz. Keine ergänzte7 oder andere Zahl. E1 bleibt Selbstbezeichnung außerhalb V1. |

Der Quellen-Erstbericht enthält außerdem den Satz mit „sechsundzwanzig ursprünglichen Quellen-/Entwurfsstatus“. Die gesonderte Errata-Datei streicht diese unbelegte Zahl, ohne ein Urteil zu ändern. Die Zusammenführung nutzt nur die sachliche Aussage: Übernommene Quellen-/Entwurfsstatus sind keine bestandenen Prüfungen. Initialbericht und dessen Hash bleiben unverändert; die Errata ist im neuen Inputmanifest gebunden.

Die überlagerten Listenheft-Textlayer bleiben eine dokumentierte Importgrenze. Für die hier gebundenen Listen13/16/17/18/19 wurden die sichtbaren Karten erneut gelesen. Daraus folgt keine vollständige visuelle Karten- oder Kategorienprüfung der übrigen287. Die zwei Erstbewertungen berichteten eigene begrenzte Quellenlektüren; ihre Eignungsurteile sind keine pauschale zellenweise Freigabe des gesamten extrahierten Katalogs. In der neuen CSV sind die neun engen Kernabgleiche, die D30-Labelkorrektur, die E6-Seitenverifikation und die weiterhin nicht vollständig geprüften Quellenzellen ausdrücklich verschieden.

## Grenzen des 296er Bestands

C44 und R werden nicht ergänzt. Der gepinnte Fragebogen nennt sie in Q2; die dokumentierten Druckübergänge Q31 C43→D/Q32 und Q96 I9/Q97 K1–K4/Q98J tragen keinen gedruckten zusätzlichen Fragenblock. Ursache der Inhaltsverzeichnisdifferenz sowie nationale CAPI-/Rekrutierungsunterlagen bleiben ungeprüft. Es gibt keinen erfundenen C44-/R-Wortlaut oder Code.

V1 ist dagegen auf Q98 vor J1 belegt: „Bitte in dieser Liste markieren, wie dieses Interview durchgeführt wurde.“ Der Interviewer ordnet ohne die befragte Person persönlich zu Hause, persönlich außerhalb oder per Video zu. Diese nominale Verwaltungsfrage steht gesondert außerhalb296 und erhält NEIN/KEINE; keine Ergänzung zum Einstellungsbestand. Das Neunerbinding übernimmt diese Randgrenzen; ein ergänzendes Arbeitsprotokoll hält den Verwaltungswortlaut und die ungeprüfte Variablenzuordnung fest. Keine Vollständigkeit des tatsächlich eingesetzten nationalen Instruments wird behauptet.

## Quellen und Rechte am öffentlichen Artefakt

Herausgeber der Originaldokumentation ist European Social Survey ERIC. Deutsche Teilstudie des ESS, Welle11/2023, „Zusammen|Leben heute“; ESS Data Archive, ESS11-Codebook Ausgabe4.1. Die strukturierten Auszüge und der technische Reflow tragen [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), Quellen-/Änderungsvermerk und keine ESS-Billigung. Die eigene Auswahl, numerische Map und Beurteilung sind Autorenannotation. Die gesonderte Datenlizenz [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) bleibt für ESS-Daten relevant; hier werden keine Daten veröffentlicht. Keine Pauschallizenz für das Gesamtrepository abgeleitet.

Die folgenden Quellen sind in `data/item-core-v1.json` mit ihren URLs, Fassungen und Hashes enthalten. Der Bericht ist damit nicht allein von ignorierten Scratchlinks abhängig. Die Originaldateien waren zuvor öffentlich mit HTTP200 geladen worden; dieser Autor hat dieselben gepinnten lokalen öffentlichen Dokumente gelesen. Ein frischer GET oder eine aktuell neueste Fassung wird nicht behauptet.

| Quelle / Fassung | Tragende Fundstelle | SHA-256 |
| --- | --- | --- |
| [Deutscher Fragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), Welle11/2023 | Q5/10/13/15/16; Korrekturen Q41/43/45; V1 Q98 | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| [Deutsches Listenheft](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf), Runde11/2023 | Listen13/16/17/18/19 auf SC14/17/18/19/20; E1 Liste50, SC51 | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| [Codebook](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf), Ausgabe4.1 | PDF63–68/Druck62–67; D30 PDF200/Druck199 | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |
| [Datenprotokoll](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/source/ESS11_data_protocol_e01_5.pdf), Edition1.5, Oktober2023 | C1, PDF-/Druck14 | `b5176742b84ab503070e21f7ffaa9ff1a126e1e0e39354c25d810dd80eda77f7` |
| [ESS-Disclaimer](https://www.europeansocialsurvey.org/contact/disclaimer), HTML-Abrufstand2026-10-03 | Conditions of use | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` |

Die Originalsicht ist öffentlich unter [ITEM-FIRST-001/v1](../packages/ITEM-FIRST-001/v1/originalitems.json) erhalten, SHA-256 `243e50bac14689c6739288f35bb2b6d45dedb911e37693c0ef4dc565be305030`. Das Manifest trägt `6d6bad17cd27ee92dc402cf5e7ef67df4de582a50a3dcdbc3aacb76c4d883501`, der Erstbewertungsvertrag `ee2460223083cc910515b3c7fac890fff9433c7b3d414fb8786f9ed3d021f55d`. Weitere Inputpins stehen im Binding. Die publizierte Quellenbindung ersetzt keinen tatsächlichen Ausgabe4.2-Importabgleich.

## Tatsächlicher Prüfumfang und verbleibende Gates

Dieser Autor las Q13/15/16, SC14/17/18/19/20, Q10 und die gezielten Korrekturquellen Q41/45 sowie Protokoll14 als Text und Bild. Q5/14/43/98 und CB63–68/200 wurden als Text gelesen; E1 SC51 zusätzlich als Bild. Die Randbefunde C44/R wurden aus den zuvor gezielt geprüften Übergängen und beiden Erstberichten übernommen, ohne eine erneute vollständige PDF-Lektüre zu behaupten. Die restlichen287 wurden nicht neu vollständig zellenweise geprüft.

Die Strukturkontrolle prüft 296 eindeutige Identitäten in Originalreihenfolge, unveränderte Eingabepins und Originalfelder, beide vollständigen Ersturteile, genau16 dokumentierte Dissense, ausschließlich neun Kernidentitäten, unveränderte Neuner-Snapshots/Originaltext-Hashes, gültige substanzielle Zahlenmengen und Scoremaps samt Gegenrichtung B35. Nichtantworten sind von allen Maps ausgeschlossen. Diese Kontrollen prüfen Übernahme und numerische Bindung, keine Messgüte. Der erste Bildzugriff über eine nicht installierte Python-Bibliothek scheiterte vor einer Dateierzeugung; vorhandene `pdftotext`/`pdftoppm` erledigten die gezielte Lektüre. Keine Installation vorgenommen.

Die zwei getrennten Übergangsprüfungen vor Empirie, Planfestschreibung, Ausgabe4.2-Abgleich und der Mess-/Missing-/Designvertrag bleiben Aufgabe des Koordinators. Keine persönliche Statistik-Abnahme durch Steven hinzugefügt. Claude-Schlusskontrolle ist verschoben und nicht bestanden; menschliches Verständnis, Webmodusübertragung und Releasefreigaben bleiben offen. Kein Rohdaten-/`data/local/`-/Antwortzugriff, kein Revieweraufruf, kein Commit, Staging, Push, Tag, Merge oder Deployment durch diesen Autor. Die gemeinsame Prüfung `pnpm check` führt der Koordinator nach Übernahme aus. Keine UI geändert.
