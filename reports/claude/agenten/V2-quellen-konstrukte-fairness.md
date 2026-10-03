# V2: Nachprüfung von Quellen, Wortlauten, Konstrukten, Interpretationen und politischer Fairness

Prüfgegenstand: Codex-Stand `e9898fb423a3ba9fbe6387ed9215dbe83666aedc`, Branch `research/life-93-claude-20261003`. Prüfdatum 3. Oktober 2026, etwa 21:05–21:45 Uhr MESZ. Modus nach Skill `life93-review`: `NACHPRUEFUNG` (nachträgliche Prüfung, keine Erstbewertung im Sinne getrennter Ersturteile). Maschinenlesbares Urteil: `reports/claude/agenten/V2-urteil.json`.

Dieses Dokument ist ein begrenztes KI-Audit. Es ist keine Begutachtung durch Fachleute, keine wissenschaftliche Validierung und kein Neutralitätsnachweis.

## 1 Manifest und Bindung

Der Auftrag nennt als Manifest die Dateiliste im Stand `e9898fb`. Eine außerhalb des Pakets gesicherte Manifest-Prüfsumme lag nicht vor. Ich habe deshalb selbst ein Manifest gebildet: die Ausgabe von `sha256sum` über die 22 Dateien in der Reihenfolge des Auftrags (Format `<hash>  <pfad>\n`). SHA-256 dieses Manifesttexts: `becc9a44d762f92f1ee6f8278b10f2ed353f8f00f47d9e588af06e65fa03e3f0`. Diese Prüfsumme stammt vom Prüfer selbst und ersetzt keine vorab gesicherte Prüfsumme.

| SHA-256 | Datei |
| --- | --- |
| `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` | `data/politikprofil-v2.fragen.entwurf.json` |
| `24b5d2599e6d30dc02a6d835f5f80b5bcecf8f6014ee8f4670a703c25d3c3cbf` | `outputs/loop/breadth-data-001/sources/ess5-de-questionnaire.pdf` |
| `977475c18d2adebea6ccb7695f377fb6ed500ef087b077086305f9a2e4a7b239` | `outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf` |
| `dde02b5336b2d960c2900a8fcf5e2a0f0d254b46dcce1d9ffb785a830e096bc0` | `outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf` |
| `ae960ebcae1b12106eb3003ced1de7c88a73c9b95736efedd93fd8b320e974a5` | `outputs/loop/breadth-data-001/sources/ess9-de-questionnaire.pdf` |
| `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425` | `outputs/loop/breadth-data-001/sources/ess10-de-questionnaire.pdf` |
| `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` | `outputs/loop/breadth-data-001/sources/ess11-de-questionnaire.pdf` |
| `d55eb84799d1b99fc348e25a1bb2356594477e3d3c5b2f212d0764d4dcc8b4a3` | `web/src/app/policy-draft/item-meanings.ts` |
| `f556dbb8bf3d6a41503378fd53476356e29cd8b448f2a7e5544b5d695d8087b6` | `web/src/app/policy-draft/policy-draft.html` |
| `da3a08b61dd077c28bef3f1a38942b666bfb93afc4a1858498d9c302278aaace` | `web/src/app/policy-draft/policy-draft.ts` |
| `75ee3fcd461a8831a1a678b3e3e867dde2a00f0cf4de27f201da03699b184796` | `web/src/app/policy-draft/policy-source-details.html` |
| `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` | `web/src/app/policy-draft/public-catalogue.ts` |
| `28906eb1533bb953b43bed75a4995c907b71398f1ffcd63271c82cfdace05998` | `web/src/app/research/policy-profile.ts` |
| `ecf5af52c5b9e8f3d12b56cbe4516c1c38eb9e4373e4afb3025165cd920e33dc` | `web/src/app/pages/methodology/methodology.html` |
| `3b8244ffa1f4e19d5b7af71cc05d25de5fc662a598e9492971123474420bdba2` | `web/src/app/pages/project/project.html` |
| `b44b6d8e2741c3ef13103ea8cc6ecaaa9e2bc82eadf990e76b16c27a0a1bf4df` | `web/src/app/pages/home/home.html` |
| `470c73eb0cb3c2fa6569773035fbe5444507a7c15fd11253b306c7120d07dc7f` | `reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md` |
| `ecb731bc5caca8f554fd60be4f1176f021350b290d5dea2713fd4c0e48eed504` | `reports/phasen/03-politikprofil-v21-historische-gruppen.md` |
| `2b0cd26f8fba81bbf520b9ae3411d623f9299c9ff707aacf681bde4c65a0439f` | `docs/empirie-plan-v2.entwurf.md` |
| `0536441391becb9ac84e4b9596b20e2e0e4aab1a9aef827cbc162f8d7261238b` | `docs/messformen-v2.entwurf.md` |
| `77ae3d328c4862d1396e72207e5e1401dfa4da1f57580315e973943d3dfad945` | `docs/abdeckung-v2.md` |
| `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` | `data/gruppenvertrag.v2.1.entwurf.json` |

Bindungsprüfung:

- Zu Beginn stand `HEAD` auf `e9898fb`. Während der Prüfung hat der Koordinator zwei Commits ergänzt (`75dbae4`, `92516a1`), die nur `reports/claude/`, `pipeline/v22/fetch_ess_metadata.py` und `.prettierignore` ändern. `git diff --quiet e9898fb -- <datei>` bestätigt für alle 16 versionierten Manifestdateien und für `policy-catalogue.ts` den unveränderten Stand von `e9898fb`.
- Die sechs PDF-Dateien liegen im von Git ausgeschlossenen Ordner `outputs/`. Sie sind also nicht über den Commit gebunden. Ihre SHA-256-Werte stimmen mit den im Katalog eingetragenen `originalBytesSha256` überein (`data/politikprofil-v2.fragen.entwurf.json`, Abschnitt `sources`). Die Übereinstimmung mit den heute auf dem ESS-Server liegenden Dateien habe ich nicht geprüft (kein Netzabruf).
- Die Datei `public-catalogue.ts` stimmt in allen sichtbaren Textfeldern (`wordingDe`, `introductionsDe`, `responseStemDe`, `situationDe`, `instructionDe`, Kategorienlabels, Druckcodes) mit dem JSON-Katalog überein (eigener Vergleich mit Node, 0 Abweichungen bei 43 Angaben).

Zusätzlich gelesen, außerhalb des Manifests: `web/src/app/policy-draft/policy-catalogue.ts` (SHA-256 `640f6470bddce074d034c5ed9a18174c95e4447fb2f3c3ba6e8848a36192c984`), weil dort Rubriktitel, Anzeigewortlaut und Entwicklungshinweise entstehen. Per `grep` eingesehen: Gruppenlabels in `web/src/app/policy-draft/reviewed-historical-groups.ts` (SHA-256 `281159b645ccfc1d254b3745f3bcdab353800607223061fd76e43dced96bd175`). Außerdem `docs/project.md` (SHA-256 `686fdb0c…0080022`) und Kapitel 7 von `docs/handbuch.md` (SHA-256 `34e62abe…dca17a`) als Maßstab für sichtbare Texte.

Nicht gelesen: `data/raw/`, `data/local/`, Rohdaten, Personenkennungen. Die von Codex erzeugten `.txt`-Auszüge neben den PDF-Dateien habe ich nicht verwendet. Den Text habe ich selbst mit `pdftotext -layout` gezogen. Die CAWI-Bildschirmseiten im ESS10-PDF enthalten keinen Text. Diese Seiten habe ich mit `pdftoppm` gerendert und visuell gelesen.

## 2 Ergebnis in Kürze

Gesamtstatus für den geprüften Umfang: `NICHT_BESTANDEN`. Das betrifft die Prüfung der Texte und Interpretationen, nicht die historische Quellenarbeit insgesamt.

- Die 43 Wortlaute, Antwortkategorien, Druckcodes und Fundstellen stimmen mit den deutschen Originalen überein. Ich habe keine still umformulierte Frage und keinen falschen Code gefunden. Die Katalogarbeit ist in diesem Teil sorgfältig.
- Eine Originaleinleitung fehlt: ESS8, PDF-Seite 41, vor E33–E35. Der Katalog, die Oberfläche und Bericht 02 erklären gleichzeitig, Einleitungen blieben erhalten (F01).
- Der ESS10-Kontext der Coronapandemie fehlt für 17 Angaben. Die Fragebögen bitten ausdrücklich darum, „nach dem heutigen Stand der Dinge“ zu antworten, „auch wenn dieser durch die Pandemie anders ist als sonst“ (F02).
- Die Erklärung zu „härter bestraft … als heute“ (D33) schreibt der Antwort einer Person von 2026 einen Vergleich mit der Strafpraxis von 2010/2011 zu. Diese Person hat diesen Vergleich nicht gemacht (F03).
- Drei der acht Rubriktitel versprechen mehr, als ihre Fragen erfassen: „Wirtschaft und Verteilung“, „Demokratie und politische Autorität“ und vor allem „Bürgerrechte und Sicherheit“ (F04).
- 13 Erklärtexte lauten unabhängig von der gewählten Kategorie „beschreibt die Zustimmung“ oder „beschreibt die Unterstützung“. Wer „Lehne stark ab“ wählt, liest danach einen Satz über Zustimmung. Im ESS9-Gerechtigkeitsblock trifft das nur die Gleichverteilungsaussage (F05).
- Die sichtbaren Lückenlisten sind unvollständig und ungleich. Genannt werden Marktordnung, Überwachung, Gesundheit und Außenpolitik. Es fehlen Asyl und Grenzen, sexuelle Orientierung und vielfältige Lebensformen, reproduktive Selbstbestimmung und Autoritätswerte. Für die direkt neben ausgewählten Fragen stehenden ESS11-Fragen B34–B36 und B38–B39 fehlt eine dokumentierte Ausschlussbegründung (F09).
- Die historischen Gruppenvergleiche sind in Bezeichnung, Zeitbezug, Population und Grenzen korrekt beschrieben und für alle Parteien gleich behandelt. Es gibt nur kleinere Punkte (F13, F14).
- Antwortoptionen und Nichtpositionskategorien sind fair umgesetzt. Originalkategorien bleiben erhalten. Überspringen zählt nicht als Mitte.

## 3 Prüffrage 1: Wortlaute, Einleitungen, Kategorien, Codes, Filter, Fundstellen

Vorgehen: Jede der 43 Angaben habe ich mit dem Text der genannten PDF-Seite verglichen, die ESS10-CAWI-Seiten 93–96, 135–137, 141, 145, 146, 148 und 162 visuell. Für jede Angabe habe ich Einleitung, Stamm, Situation, Wortlaut, Anweisung, Kategorienlabels, Druckcodes und Filter verglichen. Die Antwortlisten im ESS8-Listenheft (PDF-Seiten 45, 49, 51, 54) habe ich gegen die Kategorien geprüft.

| Block | Angaben | Fundstelle (physische PDF-Seite) | Ergebnis |
| --- | --- | --- | --- |
| ESS9 G26–G29 | sofrdst, sofrwrk, sofrpr, sofrprv | ess9-de S. 97 | wörtlich, Kategorien 1–5 und 7/8 korrekt |
| ESS11 B33 | gincdif | ess11-de S. 13 | wörtlich |
| ESS8 E6–E8 | gvslvol, gvslvue, gvcldcr | ess8-de S. 36; Liste 48 im Listenheft S. 49 | wörtlich; der Druckfehler (0–9 ohne 10) ist korrekt dokumentiert, Liste 48 zeigt 0–10 |
| ESS8 E33–E35 | bnlwinc, eduunmp, wrkprbf | ess8-de S. 42; Einleitung S. 41; Liste 53 S. 54 | Wortlaute und Kategorien wörtlich, **Blockeinleitung S. 41 fehlt** (F01) |
| ESS10 B1–B12 | fairelc … wpestop, keydec | PAPI S. 10–11; CAWI S. 136–148 | wörtlich einschließlich Ellipsen; CAWI-Wortlaut korrekt erfasst |
| ESS10 B25 | scchpldm | PAPI S. 12; CAWI S. 162 | wörtlich; Filter zu B26/B28 korrekt beschrieben |
| ESS5 D18, D20 | bplcdc, dpcstrb | ess5-de S. 24–25 | wörtlich; D19 fehlt begründet (Empirieplan Z. 22) |
| ESS5 D33–D36 | hrshsnta, dbctvrd, lwstrob, rgbrklw | ess5-de S. 27 | wörtlich; D32 und D37 sind nicht ausgewählt |
| ESS10 A90 | vteurmmb | PAPI S. 10; CAWI S. 135 | wörtlich; Zuordnung 1/2/3/4/5/6 zu 1/2/33/44/55/65 dokumentiert |
| ESS11 B37 | euftf | ess11-de S. 14 | wörtlich; Druck 00–10 |
| ESS8 D30–D32 | inctxff, sbsrnen, banhhap | ess8-de S. 33; Liste 44 S. 45 | wörtlich („Haushaltgeräten“ wie im Original) |
| ESS10 A54–A56 | imsmetn, imdfetn, impcntr | PAPI S. 7; CAWI S. 93–96 | wörtlich; Anzeige-Stamm bei A55/A56 ist eine Zusammensetzung (F12) |
| ESS8 E15 | imsclbn | ess8-de S. 37; Liste 50 S. 51 | wörtlich; Punkt in Kategorie 1 wie auf Liste 50 |
| ESS11 E19–E22 | eqparep, eqparlv, freinsw, fineqpy | ess11-de S. 51–52 | wörtlich; Elternzeitszenario vollständig |

Weitere Beobachtungen, ohne Gewicht als Beanstandung:

- Die CAWI-Fassung von ESS10 hebt „im Allgemeinen“ (B1–B12, B25), „derselben“, „anderen“ und „ärmeren Ländern außerhalb Europas“ (A54–A56) durch Unterstreichung hervor (PDF-Seiten 94–96, 136–148, 162). Katalog und Website übernehmen diese Hervorhebung nicht. Für die Bedeutung ist das wichtig, weil F06 genau diesen Zusatz betrifft.
- In ESS8 CAPI wurden „Weiß nicht“ und „Antwort verweigert“ nach dem Hinweis auf PDF-Seite 2 über Buttons außerhalb des Fragefelds programmiert. Die Website bietet sie nicht als Radiooptionen an, sondern als Überspringgrund. Das passt zum Original.

## 4 Prüffrage 2: Zeitabhängige Formulierungen

| Angabe | Zeitbezug im Original | Bedeutung bei Anzeige 2026 | Folge für den Vergleich mit der historischen Referenz | Behandlung im Stand `e9898fb` |
| --- | --- | --- | --- | --- |
| hrshsnta (ESS5 D33) | „als sie heute bestraft werden“; Einleitung „Aussagen über Deutschland heute“ (S. 27) | Eine Person von 2026 vergleicht mit ihrer Wahrnehmung der Strafpraxis von 2026 | Die Referenz von 2010/2011 misst „härter als damals“. Beide Antworten haben verschiedene Bezugspunkte. | Erkannt. Die Erklärung schreibt aber der eigenen Antwort den Bezug 2010/2011 zu (F03). |
| dbctvrd, lwstrob, rgbrklw (D34–D36) | dieselbe Einleitung „über Deutschland heute“ | Aussagen sind weitgehend zeitlos. Der Rahmen „Deutschland heute“ verschiebt sich auf 2026. | geringe Verschiebung | im Katalog vermerkt (JSON Z. 7112 und Folgeangaben), auf der Website nicht |
| bnlwinc, eduunmp, wrkprbf (ESS8 E33–E35) | ausgelassene Einleitung: Änderungen „in den nächsten zehn Jahren“ (S. 41, Feldzeit 2016/2017) | Ohne Einleitung fehlt der Rahmen einer künftigen Reform | ESS8-Befragte antworteten mit diesem Rahmen, Websitebesucher ohne ihn | nicht erkannt (F01) |
| euftf (ESS11 B37) | „schon jetzt zu weit gegangen“ (2023) | Bezug ist der Integrationsstand 2026 | Bezugspunkt verschiebt sich um drei Jahre | nicht vermerkt (F17) |
| vteurmmb (ESS10 A90) | „morgen“, hypothetisch | Zeitlos formuliert | Antwortlage 2021/2022 nach dem Brexit, Vermutung zum Kontext | ausreichend |
| alle 17 ESS10-SC-Angaben | Anleitung „nach dem heutigen Stand der Dinge, auch wenn dieser durch die Pandemie anders ist als sonst“ (PAPI S. 1 und 2, CAWI S. 48); Pandemiemodul A1–A5 direkt davor; Feldzeit 5. Oktober 2021 bis 4. Januar 2022, kurz nach der Bundestagswahl im September 2021 (PAPI S. 4, A25) | Kein Pandemiekontext | Ausnahmesituation bei der Erhebung, etwa für Fragen zur Regierung (B3, B7, B25) | nicht dokumentiert (F02) |
| inctxff, sbsrnen, banhhap (ESS8 D30–D32) | „Maßnahmen in Deutschland“, Stand 2016/2017 | Bedeutung hängt von der damals und heute geltenden Politik ab, etwa bestehender CO2-Bepreisung oder Effizienzregeln (Vermutung, nicht an Quellen geprüft) | „Erhöhung der Abgaben“ kann 2016 und 2026 von verschiedenen Ausgangsniveaus aus gemeint sein | nicht vermerkt (F17) |
| gvslvol, gvslvue, gvcldcr, imsclbn, eqparep | keine Zeitwörter, aber Bezug auf bestehende Leistungen und Regeln | ähnliche Status-quo-Abhängigkeit (Vermutung) | gering bis mittel | nicht vermerkt (F17) |

Die Website stellt die Herkunft jeder Angabe sichtbar dar (Feldzeit, Modus, „keine aktuelle Bevölkerungsnorm für 2026“). Das ist gut. Der Zeitbezug einzelner Formulierungen wird aber nur bei D33 ausdrücklich behandelt. Ausgerechnet dort zieht die Erklärung den falschen Schluss.

## 5 Prüffrage 3: Konstrukt und Reichweite

Die Erklärtexte unterscheiden Antworttypen meist richtig. Die ESS10-Angaben nennen „Wichtigkeit“, E6–E8 das „gewünschte Ausmaß staatlicher Verantwortung“, D18/D20 das „empfundene Pflichtausmaß“, Maßnahmen „Unterstützung“, A90/B25/E15 die nominale Auswahl. Die Methodikseite nennt dagegen nur „Zustimmung, Wichtigkeit und nominale Auswahl“ (methodology.html Z. 35–37). Zuständigkeit, Pflicht, Befürwortung und Zulassungsumfang fehlen dort (F16).

Tragen die acht Rubriken ihre Bezeichnung?

| Rubrik (policy-catalogue.ts Z. 6–15) | Tatsächlicher Inhalt | Urteil |
| --- | --- | --- |
| Wirtschaft und Verteilung (5) | vier Gerechtigkeitsprinzipien (ESS9 G26–G29) und eine Zustimmung zu staatlicher Einkommensangleichung (ESS11 B33) | enger: Verteilungsgerechtigkeit und Umverteilung. Keine Frage zu Markt, Eigentum, Steuern, Arbeit oder Wettbewerb (F04) |
| Sozialstaat (5) | Verantwortung für Alter, Arbeitslose, Kinderbetreuung; Zielgruppenbeschränkung; Budgetkonflikt Weiterbildung gegen Leistung | trägt die Bezeichnung als Ausschnitt. Lücken (Gesundheit, Pflege) sind in Bericht 02 benannt. |
| Demokratie und politische Autorität (12) | Wichtigkeit von elf Prinzipien „für die Demokratie im Allgemeinen“ (B1–B11) und Mehrheit gegen Regierungsplan (B25) | enger: Demokratieverständnis und Responsivität. Keine Frage zu Autorität, Gehorsam oder Führung. Die passenden ESS11-Fragen B38/B39 stehen auf derselben Seite wie das ausgewählte B37 (F04, F09) |
| Bürgerrechte und Sicherheit (6) | Pflichtgefühl gegenüber Polizei (2), Strafverschärfung (1), Rechtsbefolgung (3) | enger und anders: Rechtsbefolgung, Polizei und Strafen. Keine einzige Frage zu Bürgerrechten im Sinn von Freiheitsrechten, Datenschutz oder Überwachung (F04) |
| Europäische Integration (3) | Referendum, Integrationsrichtung, nationale statt EU-Entscheidung als Demokratieprinzip | trägt die Bezeichnung als Ausschnitt |
| Klima und Energie (3) | drei Klimaschutzinstrumente | enger: Klimaschutzinstrumente. Energieversorgung und Energieträger fehlen (in Bericht 02 benannt) |
| Migration (4) | Zulassungsumfang für drei Gruppen, Bedingungen für Sozialleistungsrechte | trägt die Bezeichnung als Ausschnitt. Asyl, Grenze, Integration und Staatsbürgerschaft fehlen. Auf der Website steht das nicht (F09). |
| Gleichstellungs- und Familienpolitik (5) | vier verpflichtende oder sanktionierende Maßnahmen zur Gleichstellung von Frauen und Männern; eine Familienleistung mit Steuerfolge | Ausschnitt. Alle vier ESS11-Fragen messen Zustimmung zu Pflicht- oder Sanktionsmaßnahmen, nicht Zustimmung zum Ziel Gleichstellung. Wer das Ziel teilt, aber gesetzlichen Zwang ablehnt, erscheint hier als „dagegen“ (F04). |

Die Pflichtbereiche stammen aus Stevens Auftrag (Empirieplan Z. 9; project.md Z. 31). Die Rubriken dürfen deshalb als geplante Bereiche bestehen bleiben. Als Überschrift über einzelnen Ergebnissen versprechen drei Titel aber eine Breite, die die Fragen nicht haben. Eine Umbenennung der Rubriken berührt den Produktumfang und braucht Stevens Entscheidung.

## 6 Prüffrage 4: Politische Fairness

Was fair umgesetzt ist:

- Alle Originalkategorien bleiben erhalten, mit Mittelkategorie dort, wo das Original eine hat, und ohne Mittelkategorie bei den Vierstufenskalen (E33–E35, A54–A56). Die Nichtpositionskategorien bei A90 (leerer oder ungültiger Stimmzettel, Nichtwahl, nicht stimmberechtigt) erscheinen als eigene Optionen. Überspringen hat drei Gründe und wird ausdrücklich nicht als Mitte oder Gegenposition gewertet (policy-draft.html Z. 122–134, 380–386).
- Bericht 02 behandelt alle 43 Angaben mit denselben Textbausteinen. Bericht 03 behandelt alle 26 Gruppen gleich, auch „Other“.
- Die Erklärtexte enthalten keine Motive, Charakterurteile oder Ideologielabels. Bericht 02 schließt Populismus- und Autoritarismuslabels für Personen ausdrücklich aus (Z. 769).

Asymmetrien und Probleme:

1. Richtungsabhängige Erklärtexte (F05): 13 Texte sprechen von „Zustimmung“ oder „Unterstützung“ und passen nur zu einer Antwortrichtung. Im ESS9-Block erhält nur die Gleichverteilungsaussage diese Form („beschreibt die Zustimmung zur gleichmäßigen Verteilung … als Gerechtigkeitsprinzip“, item-meanings.ts Z. 6). Leistung, Bedarf und Herkunftsprivileg erhalten die neutrale Form „Zustimmung oder Ablehnung der Aussage“ (Z. 10, 14, 18).
2. Ungleich verteilte Vorbehalte (F07): „Daraus folgt keine allgemeine Eigenschaft der Person“ steht nur bei „Durchsetzung des Volkswillens“ (Z. 86), nicht bei den 42 anderen Angaben. „Sie belegt keine tatsächlichen Zuwanderungsfolgen“ steht nur bei einer der drei Zulassungsfragen (Z. 146). „Eine bestimmte Steuer- oder Eigentumsordnung folgt daraus nicht“ steht nur bei gincdif (Z. 22). Einzelne Vorbehalte an einzelnen Antworten können wie ein Warnschild wirken. Ob Nutzer sie so lesen, ist eine Vermutung und nur mit Verständnistests zu klären.
3. Gruppenbegriff „Volksgruppe oder ethnische Gruppe“ (F08): Der Originalbegriff bleibt richtigerweise erhalten. Die Website nennt ihn „historische Originalformulierung“ (Z. 142), obwohl die Fassung von 2021 stammt. Sie erklärt nicht, dass er laut den im Katalog gespeicherten API-Metadaten die deutsche Übersetzung von „race or ethnic group“ ist (JSON Z. 9050, 9251). Die Titel „Zulassung der im Original genannten gleichen Gruppe“ und „… anderen Gruppe“ sind ohne die Frage nicht verständlich. Die dritte Zulassungsfrage nennt ihre Gruppe dagegen ausdrücklich. Vermutung: Ein Teil der Befragten versteht „Zuwanderer derselben Volksgruppe wie die Mehrheit der Deutschen“ als Spätaussiedler. Das wäre eine deutsche Besonderheit, die die Vergleichbarkeit mit der englischen Ausgangsfrage berührt.
4. Auswahl und Auslassung (F09): Die Website nennt als Lücken Marktordnung, digitale Überwachung, Gesundheit/Pflege und Außenpolitik (methodology.html Z. 46–47; project.html Z. 246–248). In den Projektdokumenten stehen weitere Lücken, die auf der Website fehlen: Asyl- und Grenzmaßnahmen, konkrete gemeinsame EU-Politik (Empirieplan Z. 9), vielfältige Lebensformen, reproduktive Selbstbestimmung (abdeckung-v2.md Z. 26; Bericht 02 Z. 3076), Föderalismus und Parteienfinanzierung (Bericht 02 Z. 771). Neben ausgewählten Fragen stehen in denselben Originalblöcken nicht ausgewählte Fragen:
   - ESS11 B34–B36 (Lebensführung und Adoptionsrecht von Schwulen und Lesben, Scham), S. 13, neben B33,
   - ESS11 B38–B39 (Gehorsam und Respekt vor Autorität als Erziehungswert, Loyalität gegenüber der politischen Führung), S. 14, neben B37,
   - ESS10 A57–A59 (wahrgenommene Folgen der Zuwanderung), S. 7,
   - ESS8 E9–E14 (wahrgenommene Folgen von Sozialleistungen), S. 36–37,
   - ESS5 D19, D32, D37, S. 24 und 27.
   Für D19, B13–B24, E9–E14 und A57–A59 gibt es eine dokumentierte Begründung (Empirieplan Z. 20, 22, 28; Abdeckung Z. 20). Für B34–B36 und B38–B39 habe ich in den Manifestdateien keine gefunden. Vermutung: B34–B36 fehlen, weil die ESS11-Antworten des v1-Moduls bekannt sind (Empirieplan Z. 36). Das steht so aber nicht da. Ob diese Lücken eine Richtung begünstigen, kann ich ohne Daten nicht sagen und behaupte es nicht. Sichtbar ungleich ist die Offenlegung: Die Website nennt wirtschafts-, überwachungs- und gesundheitspolitische Lücken, die gesellschaftspolitischen und migrationspolitischen nicht.
5. Gleichlaufende Polung innerhalb von Rubriken: Alle drei Klimafragen, alle vier ESS11-Gleichstellungsfragen und alle drei Zulassungsfragen haben dieselbe Richtung („dafür“ beziehungsweise „vielen erlauben“). Ohne Gesamtwert ist das kein Rechenproblem. Für die Wahrnehmung eines Ergebnisses unter einer Rubrik wie „Gleichstellungs- und Familienpolitik“ zählt es trotzdem (siehe F04).

## 7 Prüffrage 5: Historische Vergleichsgruppen

Geprüft habe ich `data/gruppenvertrag.v2.1.entwurf.json`, policy-draft.html Z. 202–355 und 450–504, Bericht 03 sowie die Wahlfragen in den Originalen (ESS5 S. 7–8, ESS8 S. 8–9, ESS9 S. 8–9, ESS10 S. 4).

- Bezeichnungen: Die sichtbaren Gruppenlabels entsprechen den deutschen Formlabels, einschließlich „Bündnis90/Die Grünen“ ohne Leerzeichen in ESS8 (S. 9). Nur der Rest heißt englisch „Other“, während das Original „Andere Partei EINTRAGEN“ druckt (F13). Die Website erklärt „Other“ als heterogenen Rest (Z. 260–265).
- Zeitbezug: Die Website nennt erinnerte Wahl (September 2009, 2013, 2017) und Befragungszeit und sagt, dass die Antworten aus der späteren Befragung stammen (Z. 249–254). Das ist korrekt. Die Wahlfrage lautet in allen drei Studien „bei der letzten Bundestagswahl im September …“. Wer absichtlich ungültig gewählt hat, wurde als „Nein“ erfasst (ESS5 S. 7, ESS8 S. 8, ESS9 S. 8). Damit gehört diese Person zu keiner Gruppe.
- Population: Die Website sagt korrekt, dass die Studien Menschen ab 15 in Privathaushalten befragten und keine verifizierte Wählerschaft abbilden (Z. 267–272). Die Zweitstimme ist selbst angegeben und nicht überprüft (Z. 256–259). ESS8 München ist benannt.
- Gleichbehandlung: Für alle Gruppen gilt dieselbe 100/5-Regel. Sie erzeugt aber eine ungleiche Sichtbarkeit (F14). In ESS5 sind für CDU/CSU alle sechs Gruppen-Frage-Paare veröffentlicht, für FDP zwei, für Die Republikaner, NPD und „Other“ keines (Bericht 03 Z. 149–573). Für die SPD mit rund 500 gültigen Antworten ist dpcstrb zurückgehalten, für Bündnis 90/Die Grünen mit rund 260 veröffentlicht. Die Regel reagiert also auf dünn besetzte Kategorien der 0–10-Skalen, nicht nur auf kleine Gruppen. Außerdem gibt es Gruppenvergleiche nur für ESS5-, ESS8- und ESS9-Angaben, also für 20 der 43 Angaben. Für Demokratie, EU, Zuwanderungszulassung und die ESS11-Gleichstellungsfragen gibt es keine. Welche Parteien zu welchem Thema erscheinen, hängt damit an der Studie: AfD-Gruppen gibt es nur für Sozialstaat, Klima, imsclbn, wrkprbf und Gerechtigkeitsprinzipien, nicht für Polizei und Strafen.
- Interpretationsgrenzen: Keine Rangfolge, keine Nähe, keine Punkte, keine Partei-Zuordnung, keine heutigen Parteiprogramme (Z. 243–247; Bericht 03 Z. 7). Das ist sachlich und für alle Parteien gleich.

Urteil: Prüffrage 5 ist für den sichtbaren Text bestanden. F13 und F14 sind niedrig.

## 8 Prüffrage 6: Ergebnisdarstellung

Die Ergebnisansicht zeigt je Angabe: Titel, Herkunft, Status, „Gewählte Originalkategorie: …“ und einen festen Erklärtext (policy-draft.html Z. 372–378). Danach folgen, falls vorhanden, die historische Kategorienverteilung und der Gruppenvergleich.

Was die Texte über die eigene Antwort sagen: Sie benennen den Gegenstand der Frage, nicht die Bedeutung der gewählten Kategorie. Das ist ehrlich und vermeidet Überdeutung. Es hat aber vier Lücken:

1. Der Text hängt nicht von der Antwort ab. Bei 13 Angaben passt er nur zu Zustimmung oder Unterstützung (F05).
2. Die eigene Kategorie ist in der historischen Verteilung nicht markiert (Z. 401–408 und 460–467). Nutzer müssen selbst suchen, wie häufig ihre Antwort damals war. Ein Satz wie „Diese Kategorie wählten in ESS9 (2018/2019) … % der gültigen Antworten (gewichtet)“ mit Zahlen aus dem Export würde die Referenz nutzbar machen (F10).
3. Bei 0–10-Skalen und Wichtigkeitsfragen fehlt ein Hinweis, was niedrige Werte bedeuten. Bei B1–B11 heißt ein niedriger Wert „nicht wichtig für die Demokratie im Allgemeinen“, nicht Ablehnung des Inhalts. Fünf der Erklärtexte lassen diesen Zusatz weg (F06).
4. Bei zeitabhängigen Angaben fehlt eine tragfähige Erklärung (D33: F03; E33–E35: F01; ESS10: F02).

Zusätzlich widerspricht sich der Statustext: „Dimensionen und Auswertung sind ein eigenes Modell dieses Projekts“ (Z. 172–173) neben „Sie berechnet keine gemeinsamen Dimensionen“ (Z. 182–183) (F11).

## 9 Beanstandungen

Schweregrade: `erheblich` = verfälscht eine zentrale Aussage oder blockiert eine Funktion; `mittel` = sichtbarer sachlicher Fehler oder Auslassung mit Folgen für Deutung oder Vergleich; `niedrig` = Ungenauigkeit ohne wesentliche Deutungsfolge. Ich habe kein Finding als `erheblich` eingestuft.

### F01 – ESS8-Einleitung vor E33–E35 fehlt (mittel, belegt)

- Fundstelle: Original ess8-de-questionnaire.pdf, S. 41 unten: „Als Reaktion auf veränderte wirtschaftliche und gesellschaftliche Rahmenbedingungen könnte es sein, dass Staat und Regierung in den nächsten zehn Jahren Änderungen bei den Sozialleistungen vornehmen.“ Danach folgen auf S. 42 E33–E35. Katalog: `data/politikprofil-v2.fragen.entwurf.json` Z. 2409 (`bnlwinc.introductionsDe: []`), Z. 10392 (`wrkprbf.introductionsDe: []`); `eduunmp` hat nur das Szenario „feste Geldsumme“. Gegenaussagen: JSON Z. 7 („An omitted introductory stem must not be silently removed“), Bericht 02 Z. 3391 („Einleitungen … bleiben erhalten“), methodology.html Z. 135, policy-catalogue.ts Z. 61. Die Website zeigt bei E33 und E35 „Der Katalog enthält für diese Einzelangabe keine zusätzliche Einleitung“ (policy-draft.html Z. 79–83). Bericht 02 Z. 643–650 und 3328–3336 enthält keine Einleitung.
- Problem: Eine Originaleinleitung fehlt ohne Hinweis. E35 steht außerdem als letzte Frage unter Gleichstellung, getrennt vom gemeinsamen Liste-53-Block.
- Auswirkung: Die ESS8-Befragten beantworteten E33–E35 als Fragen zu möglichen Reformen in den nächsten zehn Jahren. Die Websitefassung stellt sie ohne diesen Rahmen. Das mindert die Vergleichbarkeit mit den historischen Anteilen von drei Angaben. Die Aussage, Einleitungen blieben erhalten, ist an dieser Stelle falsch.
- Korrektur: Einleitung als `introductionsDe` für bnlwinc mit Fundstelle S. 41 aufnehmen, als Blockkontext für eduunmp und wrkprbf vermerken. Website, `public-catalogue.ts` und Bericht 02 neu erzeugen. Prüfen, ob E35 im Fragenablauf bei E33/E34 bleiben soll.
- Nachprüfung: `pdftotext -f 41 -l 41 -layout` auf das ESS8-PDF; `jq '.items[]|select(.variable|test("bnlwinc|eduunmp|wrkprbf"))|.introductionsDe'`; `grep -c Rahmenbedingungen` in Katalog, `public-catalogue.ts` und Bericht 02 > 0.

### F02 – ESS10-Pandemiekontext ist nicht dokumentiert (mittel, belegt)

- Fundstelle: ess10-de-questionnaire.pdf PAPI S. 1 („Bitte beantworten Sie alle Fragen nach dem heutigen Stand der Dinge, auch wenn dieser durch die Pandemie anders ist als sonst“), S. 2 (dieselbe Anleitung vor A6, davor Pandemiemodul A1–A5), CAWI S. 48 (gleiche Anleitung, Unterstreichung „nach dem heutigen Stand der Dinge“). Feldzeit laut Katalog 5. Oktober 2021 bis 4. Januar 2022. Wahlfrage S. 4 nennt die Bundestagswahl im September 2021. Im Katalog, in `policy-source-details.html`, in methodology.html Z. 91–99 und in Bericht 02 Z. 65–75 kommt „Pandemie“ nicht vor.
- Problem: Für 17 Angaben fehlt ein Teil des Originalkontexts, der ausdrücklich für alle Fragen ab A6 galt.
- Auswirkung: Wer heutige Antworten neben die Anteile von 2021/2022 stellt, weiß nicht, dass damals eine Ausnahmelage ausdrücklich angesprochen war und der Fragebogen mit Fragen zur Pandemiebekämpfung begann. Das betrifft vor allem Fragen zu Regierung und Mehrheit (B3, B7, B8, B25).
- Korrektur: Einen studienbezogenen Kontextvermerk für ESS10SCe03_2 mit Fundstellen (PAPI S. 1, 2; CAWI S. 48) in den Katalog aufnehmen. Auf der Website unter „Historische Grenze“ und in Bericht 02 im ESS10-Abschnitt anzeigen. Sachlich bleiben, keine Vermutung über die Wirkungsrichtung.
- Nachprüfung: `grep -c Pandemie` im Katalog und in Bericht 02 > 0; Browseransicht einer ESS10-Frage zeigt den Vermerk.

### F03 – Erklärung zu „härter bestraft … als heute“ schreibt der eigenen Antwort einen falschen Bezug zu (mittel, belegt)

- Fundstelle: item-meanings.ts Z. 100–103 („Die Auswahl bezieht sich auf wesentlich härtere Strafen als im historischen Originalkontext 2010/2011. Das Wort ‚heute‘ bezeichnet dort keinen Vergleich mit 2026.“); policy-catalogue.ts Z. 58–60; Original ess5-de S. 27, D33.
- Problem: Die Frage erscheint 2026 unverändert mit „als sie heute bestraft werden“. Eine Person, die 2026 antwortet, kann nur mit ihrem eigenen Bild der Strafpraxis von 2026 vergleichen. Die Ergebnisansicht behauptet, ihre Auswahl beziehe sich auf 2010/2011. Das stimmt nur für die historischen Befragten. „Wesentlich härter“ steht außerdem für das Original „viel härter“.
- Auswirkung: Die eigene Antwort wird falsch beschrieben. Der Vergleich mit der ESS5-Verteilung setzt zwei verschiedene Bezugspunkte nebeneinander, ohne das zu sagen.
- Korrektur: Erklärung aufteilen. Eigene Antwort: „Die Auswahl gibt an, wie sehr der Aussage zugestimmt wird, dass Menschen, die das Gesetz brechen, viel härter bestraft werden sollten als heute. ‚Heute‘ meint bei einer Antwort auf dieser Website die Gegenwart.“ Historische Referenz: „Die Befragten von 2010/2011 bezogen ‚heute‘ auf die damalige Strafpraxis. Beide Antworten haben deshalb verschiedene Bezugspunkte.“ Alternativ D33 nur als historische Referenz zeigen und aus der Webdurchführung nehmen. Das ist eine Inhaltsentscheidung für Steven.
- Nachprüfung: Text in item-meanings.ts und policy-catalogue.ts lesen; Ergebnisansicht im Browser nach Antwort „Lehne stark ab“ prüfen.

### F04 – Rubriktitel sind breiter als ihr Inhalt (mittel, belegt)

- Fundstelle: policy-catalogue.ts Z. 6–15; sichtbar in policy-draft.html Z. 66 und 362–369, methodology.html Z. 42–45, project.html Z. 41–45, home.html Z. 76–78.
- Problem: „Wirtschaft und Verteilung“ enthält keine Wirtschaftsordnungsfrage. „Demokratie und politische Autorität“ enthält keine Autoritätsfrage. „Bürgerrechte und Sicherheit“ enthält keine Bürgerrechtsfrage, sondern Rechts- und Polizeigehorsam sowie Strafverschärfung. Unter „Gleichstellungs- und Familienpolitik“ messen alle ESS11-Fragen Zustimmung zu Pflicht- und Sanktionsmaßnahmen. Der Hinweis „Diese Rubrik ordnet konkrete Originalangaben“ (Z. 366–369) und die Lückenabsätze in Bericht 02 mildern das, die Website-Rubriken selbst nicht.
- Auswirkung: Ein Ergebnis unter „Bürgerrechte“ legt nahe, wenig Pflichtgefühl gegenüber der Polizei sei eine Bürgerrechtsposition und viel Pflichtgefühl eine Sicherheitsposition. Das erfasst die Frage nicht. Unter „Gleichstellung“ kann Ablehnung einer Quote als Ablehnung von Gleichstellung gelesen werden.
- Korrektur: Für die Ergebnisansicht beschreibende Untertitel nach dem tatsächlichen Inhalt, etwa „Verteilungsgerechtigkeit und Umverteilung“, „Demokratieverständnis und Responsivität“, „Rechtsbefolgung, Polizei und Strafen“, „Gesetzliche Gleichstellungsmaßnahmen und Familienleistungen“. Die Auftragsbereiche bleiben als geplante Abdeckung bestehen. Je Rubrik eine Zeile „Erfasst: … Nicht erfasst: …“. Entscheidung über Rubriknamen bei Steven.
- Nachprüfung: Rubriktitel und Untertitel gegen die Fragenliste je Rubrik lesen; Browseransicht der Ergebnisseite.

### F05 – Richtungsabhängige Erklärtexte (mittel, belegt)

- Fundstelle: item-meanings.ts Z. 6 (sofrdst), 22 (gincdif), 106 (dbctvrd), 110 (lwstrob), 114 (rgbrklw), 130 (inctxff), 134 (sbsrnen), 138 (banhhap), 158 (eqparep), 162 (eqparlv), 166 (freinsw), 170 (fineqpy), 174 (wrkprbf). Anzeige nach jeder Antwort in policy-draft.html Z. 377–378.
- Problem: „Die Auswahl beschreibt die Zustimmung …“ und „… die Unterstützung …“ erscheinen auch nach „Lehne stark ab“ oder „Sehr dagegen“. Im ESS9-Block bekommt nur die Gleichverteilungsaussage diese Form, die anderen drei die neutrale.
- Auswirkung: Die eigene Antwort wird bei 13 von 43 Angaben für eine Antwortrichtung falsch beschrieben. Die ungleiche Form im Gerechtigkeitsblock ist eine sprachliche Asymmetrie zwischen Positionen.
- Korrektur: Einheitlich richtungsneutral, etwa „Die Auswahl gibt an, wie stark die Aussage … befürwortet oder abgelehnt wird“ oder „… wie sehr die Maßnahme … befürwortet oder abgelehnt wird“. sofrdst an die Form von sofrwrk/sofrpr/sofrprv angleichen.
- Nachprüfung: `grep -nE "beschreibt die (Zustimmung|Unterstützung)" web/src/app/policy-draft/item-meanings.ts` liefert 0 Treffer.

### F06 – Fünf Demokratie-Erklärungen lassen „für die Demokratie im Allgemeinen“ weg (niedrig, belegt)

- Fundstelle: item-meanings.ts Z. 54 (medcrgv), 62 (votedir), 66 (cttresa), 70 (gptpelc), 86 (wpestop). Original ESS10 PAPI S. 10 (Stamm), CAWI S. 136–148 (Unterstreichung „im Allgemeinen“).
- Problem: Die Frage misst Wichtigkeit für die Demokratie im Allgemeinen. Die Erklärung „nennt die Wichtigkeit gleicher Behandlung aller Menschen durch Gerichte“ klingt nach allgemeiner Wichtigkeit.
- Auswirkung: Ein niedriger Wert kann als Geringschätzung des Inhalts gelesen werden. Gemeint ist, dass die Person den Inhalt für kein Merkmal von Demokratie hält.
- Korrektur: Bei allen B-Angaben „für die Demokratie im Allgemeinen“ ergänzen.
- Nachprüfung: Alle Texte der zwölf `democracy_norms`-Angaben enthalten „Demokratie im Allgemeinen“ oder „Demokratieprinzip“.

### F07 – Vorbehalte nur an einzelnen Antworten (niedrig, Ungleichheit belegt, Wirkung Vermutung)

- Fundstelle: item-meanings.ts Z. 22, 46, 78, 86, 146.
- Problem: Allgemeine Vorbehalte stehen an einzelnen Angaben, etwa „Daraus folgt keine allgemeine Eigenschaft der Person“ nur bei wpestop.
- Auswirkung: Vermutung: Nutzer lesen einen Vorbehalt an einer einzelnen Antwort als Hinweis, diese Antwort sei heikel.
- Korrektur: Den allgemeinen Satz einmal für alle Angaben in die Ergebnisansicht stellen (Status und Grenzen, Z. 189–192, sagt das schon teilweise). Itemspezifische Vorbehalte nur dort, wo der Inhalt sie wirklich verlangt, und dann nach derselben Regel für vergleichbare Angaben.
- Nachprüfung: Liste der Sätze mit „folgt“, „belegt keine“, „bewertet keine“ in item-meanings.ts gegen eine schriftliche Regel prüfen.

### F08 – Gruppenbegriff in Zuwanderungsfragen ohne Erklärung, Titel unklar (mittel; Befund belegt, Verständnisfolge Vermutung)

- Fundstelle: item-meanings.ts Z. 140–147; Original ESS10 PAPI S. 7, CAWI S. 94–95; JSON Z. 9050 und 9251 (`apiQuestionEn` „same/different race or ethnic group“).
- Problem: „historische Originalformulierung“ ist für eine Fassung von 2021 irreführend. Es fehlt der Hinweis, dass „Volksgruppe oder ethnische Gruppe“ die deutsche ESS-Übersetzung von „race or ethnic group“ ist und das Projekt den Begriff zur Vergleichbarkeit übernimmt, ohne sich ihn zu eigen zu machen. Die Titel nennen die Gruppe nicht.
- Auswirkung: Ein historisch belasteter Begriff steht ohne Einordnung in einer Projektoberfläche. Die Ergebnisliste ist für diese zwei Angaben ohne Öffnen der Quelle nicht lesbar. Vermutung: Befragte verstehen den Begriff unterschiedlich, etwa als Spätaussiedler.
- Korrektur: Titel „Zuwanderung derselben Volksgruppe oder ethnischen Gruppe wie die Mehrheit (Originalbegriff)“ und entsprechend „… einer anderen …“. Einordnung: „Originalbegriff der deutschen ESS-Fassung von 2021, Übersetzung von ‚race or ethnic group‘. Das Projekt übernimmt ihn unverändert, um mit den damaligen Antworten vergleichen zu können. Befragte können ihn unterschiedlich verstehen.“ Die Unterstreichung „derselben“/„anderen“ aus der CAWI-Fassung prüfen.
- Nachprüfung: Texte lesen; Verständnistest mit Menschen, ob der Begriff und die Titel verstanden werden.

### F09 – Lücken auf der Website unvollständig und ungleich offengelegt; Ausschluss von B34–B36 und B38–B39 unbegründet (mittel, belegt)

- Fundstelle: methodology.html Z. 46–47; project.html Z. 246–248; Empirieplan Z. 9, 28, 36; abdeckung-v2.md Z. 26; Bericht 02 Z. 771, 2750, 3076; Originale ess11-de S. 13 (B34–B36), S. 14 (B38–B39).
- Problem: Die Website nennt einige Lücken und lässt andere weg, die in den eigenen Dokumenten stehen. Für zwei Blöcke direkt neben ausgewählten Fragen fehlt eine Ausschlussbegründung.
- Auswirkung: Leser überschätzen die Breite im gesellschaftspolitischen Bereich und in der Migration. Die Rubrik „politische Autorität“ hat keine Frage, obwohl im selben Fragebogen geeignete stehen.
- Korrektur: Auf der Methodikseite je Rubrik die Lücken aus Bericht 02 („Inhaltslücken“) übernehmen. Im Empirieplan begründen, warum B34–B36 und B38–B39 nicht ausgewählt sind, oder ihre Aufnahme als getrennte Einzelangaben mit Steven klären. Bei bekannten v1-Antworten gilt der Hinweis aus Empirieplan Z. 36 entsprechend.
- Nachprüfung: Lückenliste der Website gegen Bericht 02 und abdeckung-v2.md abgleichen; `grep -n "B38\|B34" docs/empirie-plan-v2.entwurf.md` > 0.

### F10 – Ergebnisansicht verbindet eigene Antwort nicht mit der Referenz (mittel, belegt)

- Fundstelle: policy-draft.html Z. 376–378, 393–408, 450–467; Empirieplan Z. 64 („Die eigene Antwort wird mit ihrer konkreten Bedeutung beschrieben“).
- Problem: Die eigene Kategorie ist in der historischen Verteilung nicht markiert. Es gibt keinen Satz zur Bedeutung der Skalenenden und keine Einordnung der gewählten Kategorie.
- Auswirkung: Die geplanten „Erklärungen zu den erfragten Einstellungen“ (home.html Z. 39) fehlen in der Ergebnisansicht weitgehend. Nutzer müssen Vergleiche selbst ziehen und können dabei die Nenner missverstehen.
- Korrektur: Eigene Kategorie in Verteilung und Gruppenvergleich mit Text kennzeichnen, nicht nur mit Farbe. Ein generierter Satz mit dem Anteil dieser Kategorie aus dem Export, nicht von Hand. Je Antworttyp ein kurzer, für beide Richtungen gleich gebauter Satz zur Bedeutung der Skala.
- Nachprüfung: Browserprüfung auf Desktop- und Smartphone-Breite; Zahl im Satz gegen den Export.

### F11 – Statustext widerspricht sich bei „Dimensionen“ (niedrig, Widerspruch belegt, Herkunft Vermutung)

- Fundstelle: policy-draft.html Z. 172–175 gegen Z. 182–183. Handbuch 7.7 verlangt für Ergebnisseiten den Statushinweis aus LIFE-93 im Wortlaut. Ob Z. 172–175 dieser Wortlaut ist, habe ich nicht geprüft.
- Korrektur: Steven entscheidet, ob der Pflichttext für eine Fassung ohne Dimensionen angepasst wird, etwa „Auswahl, Rubriken und Auswertung sind ein eigenes Modell dieses Projekts“.
- Nachprüfung: Text lesen; LIFE-93-Wortlaut vergleichen.

### F12 – Anzeigewortlaut mit nicht gekennzeichneten Zusammensetzungen (niedrig, belegt)

- Fundstelle: JSON Z. 1932 und 2172 („Sollte der Staat erstens …“ bei E7 und E8); JSON Z. 9163 und 9367 (Stamm „Wie vielen von ihnen sollte Deutschland erlauben, hier zu leben? Sollte Deutschland es…“ bei A55/A56, im PAPI S. 7 nicht wiederholt, im CAWI S. 95–96 nur „Sollte Deutschland es…“); policy-catalogue.ts Z. 81–85; JSON Z. 6343 („auf dieser Liste“ bei B25, CAWI ohne); policy-draft.html Z. 156 (Übersicht zeigt bei A54 nur „Wie vielen von ihnen …“ ohne Gruppe).
- Problem und Auswirkung: Keine inhaltliche Änderung, aber nicht gekennzeichnete Anpassungen in einer Ansicht, die „Originalfragen“ verspricht. In der Übersicht ist A54 ohne Gruppenangabe nicht verständlich.
- Korrektur: „erstens“ bei E7/E8 weglassen und als Anpassung kennzeichnen, oder den ersten Stamm nur bei E6 zeigen. Bei A55/A56 die CAWI-Form verwenden. Bei B25 die CAWI-Form oder einen Hinweis. In der Übersicht bei A54 die Einleitung mit Gruppenangabe zeigen.
- Nachprüfung: Anzeige im Browser gegen PAPI/CAWI-Seiten.

### F13 – Gruppenlabel „Other“ englisch (niedrig, belegt)

- Fundstelle: reviewed-historical-groups.ts Z. 1078, 2489, 3196 (außerhalb Manifest, per grep); Bericht 03 Z. 543, 1335, 1716; Originale ESS5 S. 8, ESS8 S. 9, ESS9 S. 9 („Andere Partei EINTRAGEN“).
- Korrektur: „Andere Partei (heterogener Rest)“; API-Label in den Quellendetails belassen.
- Nachprüfung: Auswahlliste im Browser.

### F14 – Gleiche Regel, ungleiche Sichtbarkeit der Gruppen (niedrig, belegt)

- Fundstelle: Bericht 03 Z. 149–573 (ESS5: CDU/CSU sechs von sechs Paaren, FDP zwei, Die Republikaner, NPD und Other keines); policy-draft.html Z. 493–503.
- Problem: Die 100/5-Regel greift bei 0–10-Skalen oft wegen einzelner dünner Kategorien, auch bei großen Gruppen. Welche Parteien zu welchem Thema erscheinen, hängt an der Studie.
- Auswirkung: Vermutung: Nutzer deuten fehlende Vergleiche als Aussage über eine Partei. Die Website erklärt Fehlen bereits als Folge der Regel, nicht als null Prozent.
- Korrektur: Je Studie eine Übersicht, für welche Angaben Gruppenvergleiche bestehen, mit dem Satz, dass die Lücken aus einer für alle gleichen Darstellungsregel und der Studienzuordnung folgen. Die Regelwirkung bei 11-stufigen Skalen gehört zur Methodenprüfung (V1).
- Nachprüfung: Übersicht gegen Bericht 03.

### F15 – „repräsentative wissenschaftliche Befragung“ (niedrig, offene Frage)

- Fundstelle: policy-draft.html Z. 21; methodology.html Z. 58–59; project.html Z. 75–76; home.html Z. 71. Handbuch 7.3 schreibt diese Formel vor. Gegen: JSON `populationCoverageLimit` („achieved German coverage … have not been checked“), ESS8 München.
- Korrektur: Steven entscheidet, ob die Formel durch eine prüfbare Beschreibung ersetzt wird, etwa „Befragung auf Grundlage von Zufallsstichproben aus Melderegistern“ (Stichprobenbeschreibungen im Katalog).

### F16 – Methodikseite nennt nicht alle Antworttypen (niedrig, belegt)

- Fundstelle: methodology.html Z. 35–37 gegen Empirieplan Z. 7 („Zustimmung, Wichtigkeit, Zuständigkeit und nominale Auswahl“).
- Korrektur: „Zustimmung, Befürwortung von Maßnahmen, Wichtigkeit, staatliche Zuständigkeit, Pflichtgefühl, Zulassungsumfang und nominale Auswahl beschreiben unterschiedliche Gegenstände.“

### F17 – Status-quo-abhängige Angaben ohne Hinweis (niedrig, Vermutung)

- Fundstelle: euftf (ess11-de S. 14, „schon jetzt“); D30–D32 (ess8-de S. 33); E6–E8, E15, E19.
- Problem: Diese Angaben beziehen sich auf die damals geltende Politik. Ob und wie sich die Rechtslage seitdem geändert hat, habe ich nicht an Quellen geprüft.
- Korrektur: Eine Liste der status-quo-abhängigen Angaben mit dem allgemeinen Hinweis, dass sich der Bezugspunkt seit der Erhebung verändert haben kann. Konkrete Rechtsänderungen nur mit Quelle nennen.

## 10 Checks

| Check | Pflicht im Umfang | Status | Grundlage |
| --- | --- | --- | --- |
| C1 Wortlaute, Kategorien, Druck-/Exportcodes, Filter der 43 Angaben | ja | BESTANDEN | Abschnitt 3 |
| C2 Einleitungen und Kontexte vollständig | ja | NICHT_BESTANDEN | F01, F02 |
| C3 Fundstellen (Seite, Fragenummer) | ja | BESTANDEN | Abschnitt 3 |
| C4 Zeitbezüge erkannt und richtig dargestellt | ja | NICHT_BESTANDEN | F03, F02, F01, F17 |
| C5 Konstrukt und Reichweite von Rubriken, Titeln, Erklärtexten | ja | NICHT_BESTANDEN | F04, F06, F16 |
| C6 Sprache und Symmetrie der Erklärtexte | ja | NICHT_BESTANDEN | F05, F07, F08 |
| C7 Antwortoptionen und Nichtpositionskategorien | ja | BESTANDEN | Abschnitt 6 |
| C8 Offenlegung von Auswahl und Auslassungen | ja | NICHT_BESTANDEN | F09 |
| C9 Historische Vergleichsgruppen | ja | BESTANDEN | Abschnitt 7, F13/F14 niedrig |
| C10 Ergebnisdarstellung erklärt die eigene Antwort tragfähig | ja | NICHT_BESTANDEN | F03, F05, F10, F11 |
| C11 Zahlen der Referenzen | nein | IN_DIESER_PHASE_NICHT_ERFORDERLICH | prüft V1 |
| C12 Menschliche Verständlichkeit | nein | NICHT_GEPRÜFT | keine Tests mit Menschen |

## 11 Vergleich mit früheren Prüf- und Entscheidungsdokumenten

Abschnitte 1–10 und `V2-urteil.json` waren abgeschlossen, bevor ich frühere Prüf- und Entscheidungsdokumente geöffnet habe. Belegt durch Prüfsummen um 21:25–21:28 Uhr: Abschnitte 1–10 dieses Berichts (Text bis vor die Überschrift „## 11“) SHA-256 `d9e8870db865d07ad51031105ed1a9b4e68c08ced163f13cb9e76fc7da63370f`, `V2-urteil.json` SHA-256 `622e6961b36655943f126ffa25eb7758e3d7b025fa3a1b6275630beb673d02cf`. Beide habe ich danach nicht mehr geändert. Vorher kannte ich nur Dateinamen, die in Manifestdateien verlinkt sind (etwa `RESULTS-V2-001-sources-first.md` in Bericht 02 Z. 25), nicht deren Inhalt.

Gelesen, etwa 21:28–21:36 Uhr:

- vollständig: `reports/loop/reviews/EMPIRICAL-V2-001-sources-first.md`, `EMPIRICAL-V2-001-sources-round1.md`, `reports/loop/EMPIRICAL-V2-001-entscheidung.md`, `reports/loop/reviews/RESULTS-V2-001-sources-first.md`, `POLICY-UI-001-first.md`, `reports/loop/POLICY-UI-001-entscheidung.md`, `reports/loop/reviews/COMPREHENSION-V2-001-first.md`, `reports/loop/COMPREHENSION-V2-001-entscheidung.md`;
- größtenteils: `POLICY-UI-001-round1.md` (ohne Hash-Tabellen);
- nur Kopf und gezielte Suchtreffer: `RESULTS-V2-001-sources-presentation-round1.md`, `RESULTS-V2-001-sources-presentation-p01-p02-round1.md`, `WEBSITE-BREADTH-002-first.md`, `GROUP-RESULTS-V21-001-sources-first.md`, `GROUP-PRESENTATION-V21-001-first.md`, `GROUP-V21-001-sources-first.md`, je eine Fundzeile aus `FOUNDATION-001-politics.md` und `INVENTORY-002-AB-sources.md`;
- `reports/loop/findings.json`: Struktur, alle Einträge mit Kennung, Herkunft, Status und gekürzter Begründung, Stichwortsuche;
- alle übrigen Dateien unter `reports/loop/reviews/` und `reports/loop/*entscheidung*.md`: nur Dateinamen und Stichwortsuche (Rahmenbedingungen, Pandemie, heute, Bürgerrechte, Volksgruppe, Zustimmung, B34, B38, Gehorsam, Other, repräsentativ, im Allgemeinen, erstens, Lücke), kein Volltext.

Abgleich je Befund:

| Eigener Befund | Frühere Dokumente | Hätte es mein Urteil geändert? |
| --- | --- | --- |
| F01 Einleitung ESS8 S. 41 | Nicht erhoben. EMPIRICAL-V2-001-sources-first und GROUP-RESULTS-V21-001-sources-first nennen für E33–E35 nur PDF-Seite 42. Keine Fundstelle zu „Rahmenbedingungen“ in Reviews, Entscheidungen oder findings.json. | Nein. Neuer Befund. |
| F02 Pandemiekontext ESS10 | Nicht erhoben, null Treffer für „Pandemie“. | Nein. Neuer Befund. |
| F03 „heute“ bei D33 | POLICY-UI-001-first nennt die Erklärung „Zeitbasis ausdrücklich geklärt“. RESULTS-V2-001-sources-first: „‚Heute‘ … meint den damaligen Kontext“. Beide prüfen die historische Referenz, nicht die Antwort einer Person von 2026. | Nein. Ich widerspreche dieser früheren Bewertung ausdrücklich. |
| F04 Rubriktitel | EMPIRICAL-V2-001-sources-first, EV2-SRC-F03, beschreibt dieselbe Enge der Rubriken als „Inhaltsgrenze, kein Gesamtblocker“. Es nennt dort auch, dass Unterstützung einer Paritätsregel kein allgemeines Gleichstellungsurteil ist. Die Folge war eine Lückenangabe in Bericht 02, nicht eine Änderung der Website-Titel. | Nein. Gleiche Beobachtung, andere Konsequenz. Ich halte die Titel selbst für korrekturbedürftig. |
| F05 richtungsabhängige Texte | POLICY-UI-001-first, PUI-R2, ließ drei Gerechtigkeitstexte auf „Zustimmung oder Ablehnung“ umstellen und hielt sofrdst für bereits richtig. So entstand die Asymmetrie im ESS9-Block. Die Texte mit „Unterstützung“ hat die Prüfung als passend bewertet. | Nein. Die Vorgeschichte erklärt die Asymmetrie, behebt sie aber nicht. |
| F06 „im Allgemeinen“ | EV2-SRC-F01 fand dieselbe Auslassung im CAWI-Wortlaut des Katalogs, inzwischen korrigiert. In den Erklärtexten der Website wurde sie nicht geprüft. | Nein. Bestätigt eher die Bedeutung des Zusatzes. |
| F07 Einzelvorbehalte | POLICY-UI-001-first wertet den Vorbehalt bei wpestop positiv. | Nein. Andere Bewertung, Schweregrad bleibt niedrig. |
| F08 Gruppenbegriff | POLICY-UI-001-first akzeptiert „historische Originalformulierung“ und sieht keine moralische Benennung. Die Übersetzungsfrage ist nicht erhoben. | Nein. |
| F09 Lücken, B34–B36, B38–B39 | EV2-SRC-F03 listet Asyl, andere Lebensformen und reproduktive Selbstbestimmung als Lücken. Das deckt sich mit den Dokumenten, nicht mit der Website. B38/B39 wurden in frühen v1-Prüfungen bewertet (FOUNDATION-001-politics Z. 84, INVENTORY-002-AB-sources Z. 78), aber nach den gelesenen Stellen nicht als Ausschluss aus v2. | Nein. |
| F10 Ergebnisansicht | COMPREHENSION-V2-001 plant einen Verständnistest. Die konkrete Erklärung der eigenen Antwort wurde in den gelesenen Prüfungen nicht als Lücke erhoben. | Nein. |
| F11–F17 | Keine entsprechenden früheren Befunde gefunden. Die Gruppenprüfungen bestätigen gleiche Behandlung und Originallabels, wie in C9. | Nein. |

Ergebnis des Abgleichs: Kein früheres Dokument hätte ein eigenes Finding aufgehoben. Die früheren Codex-Quellenprüfungen haben Wortlaut, Codes und Kategorien sehr gründlich geprüft. Das deckt sich mit meinem Check C1. Ihre Prüfung endete aber an den gelisteten Frageseiten. Den übergreifenden Kontext (S. 41, Pandemieanleitung) und die Bedeutung der Erklärtexte für die Antwort einer heutigen Person haben sie nicht geprüft. Mein Ersturteil bleibt unverändert.

## 12 Geöffnete Quellen, Befehle, Grenzen, Modell

Geöffnete Quellen (lokale Pfade; Zugriffszeit 3. Oktober 2026, MESZ):

- 21:05: `reports/claude/auftraege/V2-quellen-konstrukte-fairness.vollstaendig.md`, `00-gemeinsame-regeln.md`, `V2-quellen-konstrukte-fairness.md`, `auftraege.sha256`; `.claude/skills/life93-review/SKILL.md` und `references/urteil-schema.json`.
- 21:06–21:08: `docs/project.md`; `data/politikprofil-v2.fragen.entwurf.json` (vollständig über `jq`-Auszüge aller 43 Angaben, Studien- und Quellenabschnitte).
- 21:06–21:17: die sechs Original-PDFs unter `outputs/loop/breadth-data-001/sources/`. Text mit `pdftotext -layout`, gelesene Seiten: ESS5 S. 7, 8, 23–27; ESS8 S. 1, 2, 8, 9, 33, 35–37, 41–43; ESS8-Listenheft S. 45, 49, 51, 54; ESS9 S. 8, 9, 96–98; ESS10 PAPI S. 1–4, 7, 10–13; ESS10 CAWI als Bild S. 37–52 (Übersicht), 93–96, 135, 136, 141, 148, 162; ESS11 S. 13, 14, 48–53.
- 21:10–21:20: `web/src/app/policy-draft/item-meanings.ts`, `policy-draft.html`, `policy-draft.ts`, `policy-source-details.html`, `policy-catalogue.ts` (außerhalb Manifest), `public-catalogue.ts` (Kopf, Ende, Textfelder per Node-Vergleich), `web/src/app/research/policy-profile.ts`, `web/src/app/pages/methodology/methodology.html`, `project/project.html`, `home/home.html`; `reviewed-historical-groups.ts` und `group-reference.ts` nur per grep.
- 21:12–21:20: `docs/abdeckung-v2.md`, `docs/empirie-plan-v2.entwurf.md`, `docs/messformen-v2.entwurf.md`, `data/gruppenvertrag.v2.1.entwurf.json` (Schlüsselfelder, Studien, Gruppen, Wahlfragen), `reports/phasen/02-…md` (Kopf, Studienabschnitte, Rubrikeinleitungen, E33/E34/D33/E35, Register, Schluss; die 43 Tabellen nur stichprobenartig), `reports/phasen/03-…md` (Kopf, Zeitbezüge, ESS5-Gruppenabschnitte vollständig, übrige per awk/grep).
- 21:20: `docs/handbuch.md` Kapitel 7.
- 21:28–21:36: frühere Prüf- und Entscheidungsdokumente wie in Abschnitt 11.

Keine Webseiten abgerufen. Keine Rohdaten, `data/raw/`, `data/local/` oder Personenkennungen geöffnet.

Ausgeführte Befehle in Kurzform: `sha256sum` über Manifest- und Zusatzdateien; `git rev-parse`, `git log`, `git diff --quiet e9898fb -- <datei>`, `git diff --stat e9898fb HEAD`, `git check-ignore`; `pdftotext -layout` in `/tmp/v2review/`; `pdfinfo`; Python-Seitenausgabe aus den Textdateien; `pdftoppm -r 50/60` und `montage` für CAWI-Seiten; `jq` für Katalog und Gruppenvertrag; `node` zum Vergleich `public-catalogue.ts` gegen Katalog und zur Schemaprüfung von `V2-urteil.json` mit dem im Repository vorhandenen Ajv (2020-12, `strict:false`), Ergebnis gültig; `grep`, `awk`, `sed` für Fundstellen und Zählungen in Bericht 03. Geschrieben habe ich nur `reports/claude/agenten/V2-quellen-konstrukte-fairness.md` und `reports/claude/agenten/V2-urteil.json`, dazu Hilfsdateien in `/tmp/v2review/` außerhalb des Repositorys. Keine Commits.

Grenzen der eigenen Prüfung:

- Keine vorab gesicherte Manifest-Prüfsumme, siehe Abschnitt 1.
- PDF-Dateien sind nicht über Git gebunden. Gegen den Server habe ich sie nicht abgeglichen.
- Keine Prüfung der Zahlen, keine Browserprüfung. Aussagen zur sichtbaren Anzeige beruhen auf Templates und Quelltext. Ob Angular etwa leere Zustände anders rendert, habe ich nicht beobachtet.
- Englische Quellfragebögen nicht geöffnet. „race or ethnic group“ stammt aus den im Katalog gespeicherten API-Metadaten.
- Bericht 02 und 03 nicht Zeile für Zeile gelesen. Die Tabellen habe ich nur auf Struktur und Gleichbehandlung geprüft.
- Wirkungen auf Nutzer (F07, F08, F14, F17) sind Vermutungen. Klären können das nur Tests mit Menschen.
- Ein einzelner KI-Prüfer einer anderen Modellfamilie als Codex. Übereinstimmung oder Abweichung mit Codex-Prüfungen belegt weder Richtigkeit noch Neutralität.

Eingesetztes Modell: laut Systemangabe der Laufzeitumgebung „Opus 5.5“, Modell-ID `claude-opus-5-5[1m]`, Anbieter Anthropic. Die interne Revision ist unbekannt. Laut Auftrag: Claude (Anthropic) als getrennter Subagent.
