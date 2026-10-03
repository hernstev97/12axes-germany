# Bindung der neun Kernfelder an ESS11 Ausgabe 4.2

Autorenbericht vom 3. Oktober 2026. Ausschließlich öffentliche Versions-/Kodierungsbindung, keine neue Item-Eignungsentscheidung, empirische Importprüfung oder methodische Abnahme. Der vorhandene Kernvertrag und die abgeschlossenen Gruppenartefakte bleiben unverändert.

## Ergebnis des begrenzten Abgleichs

Alle neun Felder sind in den offiziellen integrierten Metadaten von **ESS11 Ausgabe 4.2** enthalten. Gültige Zahlenwerte, Nichtantwortcodes, englische Antwortlabels und Codebook-Locations stimmen mit dem in [item-core-v1.json](../../../data/item-core-v1.json) abgelegten 4.1-/Protokoll-Quellenvertrag überein. Die exakten 4.2-Wortlabels und Antwort-Missing-Flags sind im neuen [Versionsbinding](../../../data/core-integrated-4.2-binding.json) vollständig enthalten. Keine fehlende Variable und kein Kodierungsmismatch in diesem Quellenabgleich.

Die Dateimetadaten nennen `ESS11e04_2`, kuratierte Ausgabe 4.2, interne Metadatenversion 179 und DOI [10.21338/ess11e04_2](https://doi.org/10.21338/ess11e04_2), veröffentlicht am 2. Juli 2026. Quelle ist das [offizielle ESS-Dateiportal](https://ess.sikt.no/en/datafile/242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef). Die internen Variablenversionen in der Tabelle sind Metadatenversionen, keine ESS-Datenausgaben.

| Item und Originalfeld | Metadatenversion | Original-Location | Gültige ganze Werte | Nichtantwortcodes | SHA-256 der originalen öffentlichen Metadatenantwort |
| --- | --- | --- | --- | --- | --- |
| B34 `freehms` | 2 | B33-36 | 1–5 | 7/8/9 | `c63b28029ee083b1dcb8351c83bfd1026e8d3c729465f23ab92a6779cdaca428` |
| B35 `hmsfmlsh` | 2 | B33-36 | 1–5 | 7/8/9 | `922fd03c15242073fc1e997dcde89e3ddf1bb5e4f539f0ae33ad6366868a9080` |
| B36 `hmsacld` | 2 | B33-36 | 1–5 | 7/8/9 | `915cfd6553a22cc99cb06a3116dde3c6d8b4fc9c073c6c5e5e591cfffdf8ccff` |
| B40 `imsmetn` | 3 | B40 | 1–4 | 7/8/9 | `2c188c9a30d43477eb5f1817876745e8368230d5a8ad63ede2653a5ccaffb89b` |
| B41 `imdfetn` | 2 | B41 | 1–4 | 7/8/9 | `6768052d91ab0a8dbaad1fd83c479442e1a5fa81ba6a581a8d1bb971e0e9a3e3` |
| B42 `impcntr` | 2 | B42 | 1–4 | 7/8/9 | `58df3dda9912dac67e27c13dd178ac0d9f4ba3caa0a83da13bdd3472fd759769` |
| B43 `imbgeco` | 1 | B43 | 0–10 | 77/88/99 | `5d825f3d9a2a1d77daa3c953bd2133719c03bbcfb28f7cee843104f9cc157937` |
| B44 `imueclt` | 1 | B44 | 0–10 | 77/88/99 | `57707c650a4af7b065827b52c82c63b572c62d457f6bf6dfed46f3c3a40ddd4b` |
| B45 `imwbcnt` | 1 | B45 | 0–10 | 77/88/99 | `2b568ea6f7f149d989976c2b05041af9e8ed967ad32a6e001daa0937949c22c9` |

Für B34–B36 sind 1–5 die fünf Zustimmungsstufen, mit 1 stärkerer Zustimmung und 5 stärkerer Ablehnung. B40–B42 haben vier Aufnahmeumfang-Kategorien, von 1 viele bis 4 niemand. B43–B45 haben 0–10, mit den Originalankern negativ bei 0 und positiv bei 10. Die Zwischenwerte sind reine Zahlenlabels. Es wird keine neue Wortbedeutung für die Mitte oder eine neue Polung erzeugt. Das ist nur die bestätigte Kodierungsrichtung, keine gebündelte Konstrukt- oder Scorefreigabe.

7/77 bezeichnet Verweigerung, 8/88 „weiß nicht“ und 9/99 keine Antwort. Der API-Wortlaut für Verweigerung ist singular `Refusal`; die allgemeine Protokollbeschreibung verwendet `Refusals`. Beide Originalangaben bleiben erhalten. Der öffentliche 4.2-Codelistensatz dieser neun Felder enthält **keinen** „Not applicable“-Code. Die allgemeinen Protokollcodes 6/66 dürfen deshalb nicht als tatsächlich dokumentierter struktureller Missingcode dieser Kernfragen ausgegeben werden. Ein späterer unerwarteter Wert oder leerer Systemtoken bleibt eine gesonderte Import-/Filterprüfung und erhält keinen Score.

Die englischen Wertlabels wurden exakt mit den einzelnen öffentlichen Codebook-4.1-Abschnitten verglichen. Die deutschen Originalantworten bleiben die separat gepinnten Quellen aus dem Kernvertrag; englische Metadaten ersetzen ihre Übersetzung nicht. Für B34–B36 lautet die gemeinsame Codebook-Location `B33-36`; die Zuordnung zu den einzelnen deutschen Fragen stammt weiter aus dem unveränderten Originalpaket. Die öffentlichen Filterfelder sind hier leer. Das ist keine positive Zertifizierung des tatsächlichen deutschen CAPI-Routings.

## Reproduzierbare Quelle und unveränderte Eingänge

Die neuen Abrufe verwenden [die offizielle Portal-Metadaten-API](https://api.nsd.no/graphql), allein mit `search.dataFileMetadata` und `search.variableMetadata`. Die minimalen Abfragen enthalten Felddefinitionen und Codelisten, **keine** `analysis`-Abfrage, tabellarischen Antwortzahlen oder Personenkennungen. Requests und unveränderte Responses liegen unter `outputs/loop/resume-group-contract/core-version/sources/`; Quelle, UTC-Zeiten, HTTP-Status, Bytes und SHA-256 stehen im [Abrufprotokoll](../../../outputs/loop/resume-group-contract/core-version/metadata-access.json). Alle zehn HTTP-Abrufe waren 200; jede Codeliste ist vollständig paginiert.

Der verwendete unveränderte Kernvertrag hat SHA-256 `01dee3b72d72c074e2bf913b4791e8016acce591de3fffa120ab40eae2fb1b3e`. Für den Vergleich wurden ausschließlich Variablennamen, zulässige Werte, Missingcodes und öffentliche Quellen-Locations projiziert. Die darin eingebetteten Ersturteile und Scorevorschläge wurden nicht als Beleg dieses Bindings genutzt. Originalquelle des 4.1-Wertlabelabgleichs ist [Appendix A7](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf), SHA-256 `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35`, PDF63–68/Druck62–67. Die jeweils zugehörigen Textabschnitte wurden erneut gelesen und separat gehasht. Kein neuer PDF-Abruf oder umfassender visueller Review behauptet.

Die abgeschlossenen Gruppenartefakte wurden vor und nach diesem Nachtrag gehasht und blieben identisch:

- `ESS-GROUP-CONTRACT-proposal.md`: `8ef6bb020f6debfbc0674e6b4480d0918a0c2651571b87399426c088acebe0c5`.
- `group-source-contract.v1.entwurf.json`: `df6b808c8191f42c450bfc4206863df24768d8b10f589598e84fc1f18e3ec929`.

Die technische Kontrolle besteht aus sieben Quellenbedingungen je Feld sowie dem 4.2-Dateibinding, vollständigen Codelisten, Request-/Response-Hashes und dem Erhalt der älteren Artefakte. Sie bestätigt die **öffentlich definierten** Codes. Keine lokale CSV, Antwortzeile, Häufigkeit, politische Verteilung, Kennung oder Datei in `data/raw/` beziehungsweise `data/local/` wurde geöffnet. Kein Git-Schreibzugriff, Tag, Commit, Push, Paketinstallation oder `pnpm check` durch diesen Autor.

## Grenze und Lizenz

Dieser Nachtrag schließt die bisher offene öffentliche **4.2-Variablen-/Wertdefinitionsbindung** für die neun Felder. Tatsächliches CSV-Parsing, Spaltenvorhandensein, beobachtete Codevorkommen, Filterwidersprüche und Format-/Missingtokens der lokalen Datei bleiben offen. Auch nationale CAPI-Implementierung, Webmodus, Messmodell, Aggregation, Eignung und menschliche Verständlichkeit werden dadurch nicht validiert. Der Koordinator kann den begrenzten Nachweis übernehmen; ein historischer Satz „4.2 noch ungeprüft“ im unveränderten Kernvertrag bleibt als früherer Stand erhalten und wird durch diesen gesonderten Beleg präzisiert.

Attribution: European Social Survey ERIC / The ESS Data Archive, ESS11 integrated file edition 4.2, öffentliche Variablenmetadaten; Appendix A7 Codebook edition 4.1. Offizielle Dokumentation steht laut [ESS-Bedingungen](https://www.europeansocialsurvey.org/contact/disclaimer) unter CC BY-SA 4.0. Strukturierung und Vergleichsflags sind eigene Änderungen von 12 Axes Deutschland, keine ESS-Billigung. Die separate Datenlizenz CC BY-NC-SA 4.0 wird nicht auf diesen reinen Dokumentationsbeleg umgedeutet; keine Antwortdaten werden veröffentlicht.
