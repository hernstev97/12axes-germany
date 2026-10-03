# GROUP-CONTRACT-V21-WIP

Stand 2026-10-03T14:35:19.323304+00:00. Eigenständiger **Entwurf**, `DRAFT_PENDING_GROUP_TRANSITION_REVIEW`; keine Freigabe für Parteiantworten, Gruppenrechnung, Veröffentlichung oder Plan-Tags. Der Vertrag definiert historische getrennte Antwortverteilungen nach selbst berichteter Bundestags-Zweitstimme. Er ist keine neue unabhängige Erstbewertung und enthält keine Antwortdaten.

## Gebundener Umfang

Die vorhandenen öffentlichen Inventare005/006 und der aktuelle43-Fragenkatalog wurden übernommen. Jede Studie bleibt getrennt; die43 Fragen behalten ihre IDs und Studienzuordnung. Alle direkt benannten API-Parteikategorien und das jeweils unbenannte Other bleiben vorab erhalten. Other ist eine heterogene Restkategorie, keine behauptete politische Einheit.

| Studie | berichtete Bundestagswahl | nationalParty2 | Fragen | erhaltene Dateikategorien / Other-Code |
|---|---:|---|---:|---|
| ESS5e03_6 | 2009 | `prtvcde2` | 6 | 8 / Other `8` |
| ESS8e02_3 | 2013 | `prtvede2` | 10 | 9 / Other `9` |
| ESS9e03_3 | 2017 | `prtvede2` | 4 | 9 / Other `9` |
| ESS10SCe03_2 | 2021 | `prtvfde2` | 17 | 7 / Other `7` |
| ESS11e04_2 | 2021 | `prtvgde2` | 6 | 10 / Other `55` |

Je Studie enthält der JSON-Vertrag `vote` und das Zweitstimmenfeld mit Feld-UUID, Metadatenversion, Dateiidentität, tatsächlicher API-Codeliste, deutscher Originalfrage samt Wahlbezug, Seiten, Instruktionen, Routing und Modevarianten. Gedruckte Codes, Datei-Codes und technische Exportleere sind getrennt. `66` bleibt strukturell nicht gestellt; Partei-Missing `77/88/99`, Vote-Missing `7/8/9` und `''` mit `export_blank_unclassified` sind keine Parteigruppen. Genuine ESS11-Parteicode `9` bleibt DiePARTEI und wird nicht aus gedrucktem `09` Other hergeleitet. Für43 Antwortfelder und die beiden Gruppenfelder gilt die vorab definierte kanonische Integer-Serialisierung; keine unbekannten Werte erraten.

## Feste Kriterien vor Gruppeninsicht

Eine Gruppe setzt Deutschland, `vote=1` und einen gültigen Zweitstimmencode derselben Studie voraus. Gültige Parteicodes bei `vote!=1` werden als Inkonsistenz separat gezählt und keiner Gruppe zugeordnet. Vote- und Parteizustände bleiben getrennte Abrechnungsachsen; Nichtwahl, Nichtberechtigung, fehlende Partei, strukturell nicht gestellt und technische Leere werden nicht repariert. Ungültige oder leere Stimmzettel sind in den CAPI-Originalinstruktionen als Vote-No behandelt; eine separate ungültige-Stimmzettel-Gruppe ist daraus nicht identifizierbar. Die SC-Instruktion zeigt diesen Zusatz nicht.

Jede Gruppe und Frage erhält ihren eigenen gültigen Nenner. Primärgewicht ist `pspwght`; ungewichtet und `dweight` sind Sensitivitäten, `anweight` ist eine Äquivalenzdiagnose. Positive endliche Gewichte und das Verhältnis `anweight/pspwght` werden über **all_eligible_group_cases** geprüft, einschließlich gruppenzugehöriger Fälle mit fehlender jeweiliger Frageantwort. Die konstante-Verhältnis-Diagnose verwendet vorab absolute und relative Toleranz1e-12; ohne geeignete Gruppenfälle ist sie nicht auswertbar. Sie ändert keine Gewichtswahl oder Gruppenauswahl. SE/CI sind nicht vorgesehen.

Eine historische Referenz verlangt mindestens100 ungewichtete gültige Antworten auf genau diese Frage in genau dieser Gruppe und mindestens5 Fälle in jeder positiven originalen Kategoriezelle. Nullzellen bleiben0; bei null gültigen Antworten bleiben Kategorien mit Nullzählungen und null Anteilen inventarisiert. Andernfalls bleibt die Kategorie/Gruppe vorhanden, erhält aber keine Referenz. Die Regeln gelten auch für Other. Kein Zusammenlegen, Entfernen oder nachträgliches Ändern anhand erster Gruppengrößen. Dies sind Projektheuristiken, keine validierte Präzisions- oder Anonymitätsgarantie.

## Konkrete offene Quellenbindungen

- **ESS9**: offizieller AnhangA3, Dokumentedition3.0, physische PDF-Seite21, nennt `prtvede1` ausdrücklich Erststimme und `prtvede2` Zweitstimme. Die getrennt gebundene deutsche Originalfrage liefert den Wortlaut. Dokumentedition3.0 ist kein Ersatz für Dateiedition3.3.
- **ESS5, ESS8, ESS10SC, ESS11**: die API-Paare Germany1/Germany2 und die originale Reihenfolge Erst-/Zweitstimme bilden den belegten Zuordnungsweg. Eine zusätzliche aktuelle offizielle Alias→deutscher Fragetext-Konkordanz wurde im begrenzten006-Weg nicht gefunden. Die vier Bindungen bleiben ausdrücklich WIP; der Vertrag behauptet keine stärkere Konkordanz.
- **ESS10SC**: PAPI A25/A26b auf PDF-Seite4 und die vorhandenen CAWI-Fragen auf Seiten70/72 sind getrennt gebunden. Gedrucktes Other9 versus Datei-Other7 und nicht beobachtbare dynamische Formularregeln bleiben offen; keine automatische Umcodierung. Die geprüfte öffentliche Editionshistorie endet bei3.1 und belegt keinen vollständigen Nachcodierungsvorgang für3.2.
- **ESS11**: AnhangA3, Dokumentedition4.0, PDF-Seite36 liefert die deutschen Namen dieBasis und DiePARTEI. Diese Dokumenteinträge sind getrennt von den fehlenden8/9-Auswahloptionen im deutschen B14-Bogen gebunden. Dateicodes8/9/55 sind durch die aktuelle Datei-API belegt; gedrucktes09 Other wird nicht auf9 oder55 umgerechnet. Die geprüfte öffentliche Editionshistorie endet bei3.0 und ersetzt keinen Codierungsvorgang für4.2.
- Der vorhandene B25/`scchpldm`-Scope des v2-Analysevertrags ist byteinhaltlich übernommen. Die Frage bleibt erhalten; ein ungeklärter ursprünglicher CAWI-Nachlauf oder eine neue Webgleichheit wird nicht behauptet.

Diese Grenzen erlauben einen überprüfbaren Entwurf, ersetzen aber keine späteren frischen Quellen-/Methodenentscheidungen. Keine neue Quelle wurde für diesen Auftrag gesucht.

## Zugriffskontext und Prozess

Der Quellenentwurf begann 2026-10-03T14:11:56.200718+00:00. Root meldete anschließend fünf private43-Item-v2-Marginalkandidaten aus dem Softwarelauf **14:25:06.762–14:25:18.739UTC am03.10.2026**, nach dem von Root genannten Freeze `6702f187` / Remote-Tag `analyseplan-v2`. Das ist eine mitgeteilte Provenienz, hier nicht durch Git, Gate oder private Ausgaben verifiziert. Root meldete keine semantische Öffnung der Parteifelder, keinen Gruppenvergleich und keine v2.1-Freigabe. Die Mitteilung belegt nicht, ob Root Kandidatenzahlen anschließend menschlich betrachtet hat.

Mir wurden keine Antwort-, Marginal-, Partei- oder Gruppengrößenzahlen zugeführt. Ich habe keine Rohdatei, CSV-Header oder privaten Marginalkandidaten geöffnet. Der bekannte v2-Marginalsoftwarelauf ist dennoch ausdrücklich gebunden; spätere v2.1-Auswahl oder Interpretation kann keine umfassend unberührte Bestätigung beanspruchen. Quellen, Codes und Kriterien wurden wegen der Mitteilung nicht geändert. Bei später autorisiertem CSV-Lesen können Spaltenstrings lexikalisch den Parser passieren; ein absoluter Blindheitsnachweis wird nicht behauptet.

Die006-Expositionsgrenze bleibt erhalten: öffentliche externe nationale Wahlanteilsspalten und Parteibeschreibungen waren im früheren Dokumentzugriff sichtbar, keine ESS-Antwortverteilungen oder Gruppenfälle. In diesem Entwurf wurden solche Werte nicht übernommen; alle API-Parteien bleiben unabhängig davon erhalten. Der005-Ausgangssatz über bereits gelesene neue43 Marginals wird nur mit seinem unveränderten Erratum gelesen. Die neue datierte Mitteilung aktualisiert den Zugriffszustand, ohne005 oder006 umzuschreiben. Root und Quellenautor gehören derselben Codex-Modellfamilie an; dieser Beitrag ist kein unabhängiges Ersturteil oder Nachweis politischer Neutralität.

Tatsächlich ausgeführt wurden lokale Python-Prozesse zur Quellenkompilation, zum geschlossenen Schema-/Quellencheck und zu synthetischen Beispielen sowie begrenzte Text-/JSON-Lese- und SHA256-Vergleichsschritte. Der Compiler öffnet nur die erlaubten öffentlichen Katalog-/Vertrags-/Inventardateien und hasht32 bereits gecachte öffentliche Dokument-/Metadatenartefakte; URLs, ursprüngliche Abruf-UTC, HTTP-Status und Originalhashes stehen in `sources`. **Kein neuer HTTP-Abruf**, kein Roh-I/O, kein Git, pnpm, Installer, Server, Authzugriff oder Kontakt. Reale Header-/Edition-/Codevorkommen wurden nicht geprüft. Die nachfolgende Tabelle enthält ausschließlich aus dem öffentlichen v2-Vertrag kopierte opake Inputreferenzen; sie ist kein erneuter Rohhash- oder amtlicher Checksum-Nachweis.

| Studie | referenzierter Rohpfad, hier nicht geöffnet | Bytes laut v2-Vertrag | SHA256 laut v2-Vertrag |
|---|---|---:|---|
| ESS5e03_6 | `data/raw/ess5-ed3.6/ESS5e03_6.csv` | 69880337 | `bd93e915c2033a43bc41328fc3f4df13278b8079f8e071f98a11770f25b4022e` |
| ESS8e02_3 | `data/raw/ess8-ed2.3/ESS8e02_3.csv` | 47692954 | `5112f64fd65df229e353c82ef0f3593b568654ea76f854639f6527bca8db3684` |
| ESS9e03_3 | `data/raw/ess9-ed3.3/ESS9e03_3.csv` | 59670184 | `499dffc823859b621902b23859dc456e214772e97158bbd01cdb8eff93b1adaa` |
| ESS10SCe03_2 | `data/raw/ess10-sc-ed3.2/ESS10SCe03_2.csv` | 27241140 | `9a04d8d52b53cfe8136d0cb238d21647fcd3539d21b339498a38035aec22ec6b` |
| ESS11e04_2 | `data/raw/ess11-ed4.2/ESS11e04_2.csv` | 82693775 | `4b0bfa73fa86bcf9f868b0a6145f96504a40d7e3f2deeb3e822555993ab32dc8` |

Die ersten vier Inputevidenzen bleiben `user_file_label_plus_gated_metadata_check`, ESS11 bleibt `historical_v1_identity_plus_gated_metadata_check`. Keine historische Datei wird als neue Nutzerbereitstellung umgelabelt.

## Mechanische Checks und Fortsetzung

**44 Checks bestanden**: aktuelle Quellen-/Feld-/Code-/Dateireferenz-Konsistenz, fünf getrennte Studien,43 eindeutige Fragen, alle Other-Kategorien, disjunkte gültige/Missing/NotAsked-Gruppen, Code-Reihenfolge, opake Inputpins, aktuelle Katalogbindung, KnownDataContext; außerdem negative Schemaänderungen und ausschließlich synthetische Eligibility-, Missing-, Serialisierungs-, Zellzahl- und Gewichtskontextfälle. Das geschlossene Snapshot-Schema sichert diesen Entwurf mechanisch; es ist keine produktive Laufzeitvalidierung oder wissenschaftliche Prüfung. Compiler und Checker sind eigene Prüfarbeitsartefakte, kein Gruppen-I/O-Runner oder Analyseimplementierung.

Die elf in `pins-before.json` gebundenen erlaubten Kontext-/Quellenartefakte sind bei `pins-after.json` am2026-10-03T14:34:00.661758+00:00 bytegleich geblieben. Aktueller Katalog: `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4`; aktueller v2-Analysevertrag: `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b`. Hieraus wird keine geprüfte Konstanz sämtlicher fremder22-Pin-/UI-/historischer Artefakte abgeleitet; sie wurden nicht geöffnet oder verändert.

Der Entwurf hält Einwohner in privaten Haushalten ab15Jahren der jeweiligen Erhebung und deren historische Selbstberichte getrennt. Keine verifizierten Wahlergebnisse, heutige Parteipositionen, aktuelle Wahlrechtsprüfung, unabhängige Norm, über Studien zusammengeführte Personen oder heutige Besucherpopulation. Antworten stammen aus der jeweiligen Erhebung, nicht automatisch vom Wahltag; Erinnerungsabstand, Mode und wechselnde Parteienlisten bleiben Grenzen. Keine Scores, Gesamtdistanz, nächste Partei, Wahlvorhersage, AI-Wähler oder Personenmatrix.

Dokumentation `CC BY-SA 4.0` und Daten `CC BY-NC-SA 4.0` sind mit Quellenattribution und Belegen getrennt. Dokumentzugriff gewährt keine Daten- oder kommerzielle Freigabe. Quellenspezifische Zitierung, Weitergabe und Veröffentlichung bleiben gesondert zu prüfen.

Root kann den fertigen Entwurf unverändert in die folgende feste v2.1-Implementierungs-/Prüffassung nehmen. Vor Parteiantwortinsicht sind zwei frische getrennte Rollen (`methods_reproducibility`, `sources_constructs_fairness`) am selben Paket und ein eigener Übergang nötig. Die spätere Gruppenimplementierung, Laufzeitreproduktion und Ergebnis-/Publikationsabnahme sind offen. Kein v1-/v2-Gate wird als Gruppenfreigabe geerbt; keine Eigenannahme.

## Eigene Artefakthashes

| Artefakt | SHA256 |
|---|---|
| `data/gruppenvertrag.v2.1.entwurf.json` | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `outputs/loop/group-contract-v21/known-data-context.json` | `a20e066d7400826142cdcd8ace27bb0c8df6d48d3101bfebb3acd4d03b305c92` |
| `outputs/loop/group-contract-v21/build_contract.py` | `153016c491b870bfbe1499b3b823e6bec2a7f1d4a6bf7c7c403ba779a57dd80e` |
| `outputs/loop/group-contract-v21/check_contract.py` | `a3787449a5485a71638073868bf8468702d23068a0d9f819c1993996ba5b4a46` |
| `outputs/loop/group-contract-v21/schema.json` | `e2ac85d9a807cec642ac9212ff19acdc86a911be392bd8f4482a228af5588438` |
| `outputs/loop/group-contract-v21/synthetic-fixtures.json` | `5a9cc5068b33ac97568857c4fb0f6f036bb05fdee359c8420a30535fb19dc01d` |
| `outputs/loop/group-contract-v21/validation.json` | `c7065db5d06048c1b3531561b011228b32b472af1d3abeab1d7d48347f32f9c5` |
| `outputs/loop/group-contract-v21/pins-before.json` | `2143915a968e2582de6fcbe4c384fd09ae711a95877192cf01c749ad70e10c78` |
| `outputs/loop/group-contract-v21/pins-after.json` | `ad821c2415df5fa262ac8a694b0069c651bc06980f3fca500da1f239aab6c075` |

Der Berichtshash und die endgültige Liste eigener Artefakte stehen anschließend in `outputs/loop/group-contract-v21/artifact-hashes.json`; der Bericht enthält keinen Selbsthash.
