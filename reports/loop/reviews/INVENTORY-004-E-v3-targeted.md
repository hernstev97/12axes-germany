# INVENTORY-004-E v3: gezielte Nachprüfung

2026-10-03. Reviewer `/root/resume_e_binding_review`, frischer begrenzter Kontext. Geprüftes Manifest `reports/loop/packages/INVENTORY-004-E/v3/manifest.json`, SHA-256 `0c113eb12e3f1c51a1a89b47a5d0f9b5c6d22e6ab2589edbf2abed3152d55f31`, Reparaturrunde 2.

## Urteil

`BESTANDEN` für den festen Dokumentationsregressionsschutz gegen die nachgewiesenen Restfälle von E-R02 und die doppelt berichtete Listenreferenzlücke E2-S01/E2-R01. Kein neuer erheblicher Befund im beauftragten Umfang. Die aktuelle Annotation war schon in den gültigen v2-Quellenreviews im konkret gelesenen Originalumfang richtig. v3 repariert den Schutz gegen bestimmte spätere Änderungen; es liefert keine neue Item-, CAPI-, Messmodell- oder empirische Freigabe.

Die 32 unveränderten Identitäten bestehen im kombinierten `validate_semantics(annotation, pages)`. Sämtliche zehn zuvor akzeptierten relevanten Fehlerkandidaten aus den beiden historischen Nachberichten scheitern jetzt. Darüber hinaus scheitern die erhaltenen zehn bereits abgewiesenen Gegenfälle und 16 eigenständig ausgewählte Mutationen. Eine gewünschte Anzahl oder Fehlerquote gab es nicht. Der bekannte Austausch der Reihenfolge vollständiger, intern richtiger Codebook-Zeilen bleibt akzeptiert und außerhalb des behaupteten Schutzumfangs.

## Eingaben und Prüffassung

Alle acht direkten Manifestpins wurden vor und nach der Prüfung gegen SHA-256 und Bytezahl geprüft. Die Originalannotation trägt weiterhin `0c031abd7be58e14c91360db4e2a438b0b211e1116dd2f1b84ebab612931f6de`. Die drei neuen Artefakte sind:

| Artefakt | SHA-256 |
| --- | --- |
| `pipeline/annotations/e_source_binding_v3.py` | `ca416110f31c7ec7d5374d5e72f0e06bb5354570cca7481bf07b8554f81c9277` |
| `pipeline/annotations/e_source_bindings_v3.json` | `6264d24b85e487b03fd81a96b67c1de662099530e255e969b85fc263e66d9d28` |
| `pipeline/tests/test_e_source_binding.py` | `b9b2f3487de4d8776b92834b051a5e4062a6dac516f2c5582f6cacbde03675f7` |

Gelesen wurden die aktuellen AGENTS- und Fortsetzungsregeln, die für diesen begrenzten Auftrag relevanten Projektregeln, der vollständige neue Code und Testcode sowie der historische v2-Quellenvertrag. Aus `INVENTORY-004-E-v2-sources.md` und `INVENTORY-004-E-v2-repro.md` wurden gezielt die ursprünglichen Restbefunde, Originalfundstellen, Gegenfälle und Reichweitengrenzen genutzt. Diese zwei Berichte sind notwendige historische Fehlerbelege. Andere aktuelle Urteile, Loop-Findinginhalte und Autorenverteidigung wurden nicht gelesen. Der ebenfalls gepinnte Endauswertungsbericht wurde nur auf Bytes/Hash geprüft, nicht inhaltlich gelesen.

Die gültigen v2-Originallektüren werden weiterverwendet. Keine erneute visuelle Prüfung aller 41 Seiten und kein neues Gesamtinventaraudit. Für die technische Quellenpositionskontrolle wurden die drei bytegeprüften öffentlichen Original-PDFs mit frischem `pdftotext -bbox-layout` ausschließlich in den eigenen Ordner extrahiert. Es gab keinen Netzabruf und keinen Zugriff auf Antwort-, Roh- oder lokale Zwischendaten.

## E-R02 in Runde 2

Die neue Fassung bindet je Frage das vollständige Kontextarray einschließlich Text, primärer und weiterer Verweise, Typ, Ursprung, Quellenanker und annotierter Geltung an die geprüfte Originalannotation. Nur Schlüssel `status` bleiben aus dieser Inhaltsprojektion ausgeschlossen. Ein unabhängiger Nachbau der Projektion mit `hashlib` und `json` stimmt für alle 32 Fragen mit dem Katalog überein. Jeder gegenwärtige Pflichtkontext ist ein tatsächlich vorhandenes Objekt mit einem einzelnen primären Beleg, richtigem Originaltext und passendem Geltungsbereich; eine bloß angehängte Pflicht-ID reicht nicht.

Der Katalog bindet auch die vollständigen Originalbelegobjekte. Damit sind Quellenart, Seite, Rechteck, Tokens, Extrakt und Extrakthash festgeschrieben. Alle 70 tatsächlich gebundenen Belege wurden gegen die frischen Originaltokens und ihre ursprüngliche Geometrie geprüft, einschließlich der Listenanweisungsbelege. Ein kohärent auf eine andere echte Originalstelle umgebundener Beleg scheitert vor der historischen Mengenprüfung.

Die erhaltenen Fälle scheitern mit konkreten Abweisungen:

| Historischer Fehler | Tatsächlicher Abweisungsgrund |
| --- | --- |
| E8W-Filter entfernt, Pflicht-ID am Modulintro ergänzt | `E8W: reviewed context/text/type/origin/applicability binding changed` |
| E13-Einleitung entfernt, Pflicht-ID am Modulintro ergänzt | Gleiche Inhaltsbindungsabweichung bei E13 |
| E8W-Männerfilter primär, Frauenfilter nur sekundär | Inhaltsbindungsabweichung bei E8W |
| E8W-Beleg samt Text auf echte E8M-Stelle umgebunden | `E-v3: reviewed original evidence changed: QCTX-E8W-filter` |
| E13-Modulintro primär, notwendiges gemeinsames Intro nur sekundär | Inhaltsbindungsabweichung bei E13 |
| E8W-Filter als Einleitung typisiert | Inhaltsbindungsabweichung bei E8W |
| E10M-geerbter Filter als direkt bezeichnet | Inhaltsbindungsabweichung bei E10M |
| Zusätzlicher widersprechender E8W-Männerfilter | Inhaltsbindungsabweichung bei E8W |

Tragende Originalpositionen bleiben DE46 vor E8M, DE47 vor E8W sowie vor E9M und DE49 vor E12. Eigene weitere Fälle verändern unter anderem die Itemgeltung, den geerbten Quellenanker, die Geltungsbehauptung, zusammengehörige Ursprungsmetadaten oder nur die Rechteckgrenze bei gleichbleibendem Text. Sie werden ebenfalls abgewiesen. Entfernte Filteraufhebung „AN ALLE“, Randomisierungsanweisung, E20-Vignette und E26-Definition scheitern. Die Prüfung bestätigt deren dokumentarischen Erhalt, keine ausgeführte Interviewsteuerung.

E-R02 ist in diesem ausdrücklich begrenzten Regressionsumfang repariert. Eine allgemeine Erkennung semantisch gleichwertiger neuer Kontexte wird nicht behauptet; auch eine sachlich richtige neue Formulierung oder Kontextstruktur benötigt einen neuen konkreten Inhaltsstand.

## E2-S01/E2-R01

Listennummer, PDF-Seite, sichtbare Kategorienreferenzen und vollständiger Seitenbeleg werden je Frage gemeinsam an die geprüfte Originalseite gebunden. Zusätzlich sind die betreffenden Originalbelegobjekte gepinnt.

Beide erhaltenen E19-Einzelfeldfälle, `SC-L65-page` beziehungsweise `SC-L67-page` als Beleg des weiterhin richtigen Liste-64-Wortlauts, scheitern mit `E19: visible card evidence is not the reviewed original page`. Das nachträgliche Anhängen einer falschen Listenreferenz sowie das kohärente Umlegen des unter `SC-L64-page` gespeicherten Belegs auf Liste 65 scheitern ebenfalls. Die ursprüngliche E19-Seite bleibt Liste 64/PDF65; die fremden Seiten sind Liste 65/PDF66 und Liste 67/PDF68. Die richtige Basis samt allen 18 unterschiedlichen Listenfassungen besteht kombiniert. Beide Kennungen beschreiben dieselbe reparierte Quellenreferenzlücke.

## Umfang des kombinierten Aufrufs

Die fünf portablen Unit-Testmethoden bestehen. Mein eigener Lauf prüft zusätzlich den kombinierten v2/v3-Aufruf, die tatsächliche v2-Delegation und einen manipulierten Katalogpin. Der manipulierte Katalog wird mit `binding contract pin mismatch` abgewiesen. Ein kontrollierter v2-Fehler wird durch `validate_semantics` weitergegeben.

Zwei echte Mutationen zeigen, warum der kombinierte Aufruf notwendig bleibt: Umgekehrte sichtbare E19-Labels und umgekehrte E14-Antwortcodeobjekte bestehen den reinen Bindungsschutz, scheitern kombiniert an `sichtbare Listenlabels` beziehungsweise `Originalcodeset`. Das ist eine geprüfte Reichweitengrenze, kein Befund gegen den eng benannten v3-Schutz. Die CLI meldet ausschließlich `REVIEWED_DOCUMENT_REGRESSION_GUARD_ONLY`; ihr erfolgreicher Lauf darf nicht als vollständige Quellenprüfung ausgegeben werden.

Top-Level-Status sowie die Textstatusfelder sämtlicher Kontexte und sichtbarer Kategorien wurden gemeinsam geändert. Der kombinierte Aufruf akzeptiert weiterhin alle 32 Fragen. Diese Administration erfordert damit keinen neuen Inhaltsreview. Eine Katalogneuerzeugung aus geänderten Originalbytes wird dagegen erwartungsgemäß verweigert: Der Generator darf den festen Originalpin nicht ohne neue geprüfte Grundlage ersetzen.

Der generierte Katalog ist strukturell identisch und trägt den gleichen kanonischen SHA-256 `7d894a7461b330332dcdfc3c1114b733c10dde3292b104f19b44f4b3676e27f5`. Seine Bytefassung unterscheidet sich wegen der Arrayformatierung vom kompakt formatierten Paketkatalog; bytegleiche Ausgabe wird nicht behauptet.

## Befehle, Exits und Belege

Jeder Shellaufruf nutzte explizit den Worktree als `workdir`. Alle Writes liegen unter `outputs/loop/resume-e-review/` oder in diesem neuen Bericht. Python lief mit `-B`; keine historischen Reader oder deren Mainblöcke wurden importiert oder gestartet. Die drei gelesenen Module haben keine schreibenden Importaktionen. Die CLI des geprüften neuen Moduls wurde nur ohne Ausgabepfad oder mit einem absoluten eigenen Ausgabepfad gestartet.

| Ausgeführter Aufruf | Exit und Ergebnis |
| --- | --- |
| `cat`, `sed`, `rg`, `sha256sum` sowie begrenzte Inline-Python-Auslesungen | 0; lokale Regeln, Code, gezielte alte Fehlerbelege und Pins |
| `python3 -B /…/outputs/loop/resume-e-review/review.py`, erster Lauf | 1; eigene zu strenge Bytegleichheitsannahme beim anders formatierten Katalog, keine Inhaltsabweichung |
| Derselbe eigene Lauf nach Korrektur der Prüfannahme | 0; Basis, erhaltene und eigene Gegenfälle, Statusänderungen und Pins |
| Drei `pdftotext -bbox-layout <gepinnte Original-PDF> <eigener Extrakt>` | Je 0; vollständige konkrete Pfade in `commands.json` |
| `python3 -B -m unittest pipeline.tests.test_e_source_binding -v` | 0; fünf Testmethoden bestanden |
| `python3 -B /…/pipeline/annotations/e_source_binding_v3.py` | 0; ausschließlich Bindungsschutz |
| Derselbe CLI-Aufruf mit `--generate /…/outputs/loop/resume-e-review/generated-contract.json` | 0; JSON- und kanonische Hashgleichheit |
| Generator mit `--annotation <eigene statusgeänderte Fassung> --generate <eigener Zielpfad>` | 1, erwartet; Originalbytepin verletzt, keine Ausgabedatei erzeugt |
| `python3 -B /…/outputs/loop/resume-e-review/supplement.py` | 0; unabhängige Projektion und alle 70 gebundenen Originalgeometrien |
| Eigener Inline-Python-Vergleich von reinem und kombiniertem Schutz | 0; beide Grenzen tatsächlich belegt |

Nachprüfbare Ergebnisse stehen in `baseline.json`, `historical-cases.json`, `own-cases.json`, `administrative-status.json`, `independent-projection-and-geometries.json`, `combined-boundary.json`, `generation-comparison.json`, `commands.json` und `pins-after.json` im eigenen Ordner. Die Gegenfälle sind tatsächlich gegenüber der Originalannotation verändert; Deltapfade, Kandidathashes und konkrete Fehler werden gespeichert. Die neuen Mutationen sind durch `review.py` reproduzierbar. `pnpm check` liegt gemäß Auftrag beim Koordinator; hier wurden keine gemeinsamen Buildausgaben geschrieben.

## Grenzen und Trennung

Dieser Review übernimmt keine Ausgabe-4.2-Abnahme, keine Eignung/Polung/Konstruktentscheidung, keine Messvalidität, keine allgemeine Semantikgarantie und keine ausgeführte CAPI- oder empirische Prüfung. Die Quelle der an die reine Funktion übergebenen `pages` bleibt Callerpflicht; mein Lauf erfüllt sie mit bytegeprüften Original-PDFs und daraus frisch gewonnenen eigenen Extrakten. Die alten sieben offenen Punkte bleiben unverändert offen. Historische Fassungen, Originalberichte und gemeinsame Forschungsdateien wurden nicht verändert.

Modell gemäß geerbtem Auftrag: Codex `gpt-6.1-sol`, ohne Modellwechsel; interne Revision und nicht offengelegte Modellvorgaben sind unbekannt. Gleiche Familie und frischer begrenzter Kontext können gemeinsame Fehlerquellen haben. Das gemeinsame Dateisystem ist keine technische Isolation. Verwendet wurden lokale Shell-, Datei- und Collaboration-Werkzeuge; unslop wurde vor der Berichtsfassung gelesen und angewandt. Keine zusätzlichen Agents, andere Modellfamilie, Installation, Authentifizierung, Commits oder Pushes. Dies ist ein begrenzter KI-Nachreview eines Dokumentationsschutzes, keine wissenschaftliche Gesamtfreigabe.
