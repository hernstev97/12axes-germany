# ANGULAR-GROUP-REFERENCE-WIP

Autor: `angular_policy_draft`. Stand: 3. Oktober 2026, 16:12 UTC. Lokales Autorenpaket, keine unabhängige Darstellungsprüfung und keine Produktfreigabe.

## Konkreter Stand

Die vorhandene Angular-Vorbereitung erhält einen optionalen historischen Gruppenvergleich. `REVIEWED_HISTORICAL_GROUPS` aus `web/src/app/policy-draft/reviewed-historical-groups.ts` liefert die tatsächliche readonly Eingabe. Der ausdrücklich lokale Wrapper `web/src/app/research-preview/policy-preview.ts` bindet sie zusätzlich zu den bestehenden Einzelreferenzen. Routen, öffentliche Navigation, Startseite, Teststart und Produktionskonfiguration wurden nicht geändert.

Die Eingabe enthält drei getrennte Studien, alle 26 ursprünglichen Gruppen einschließlich Other und alle 174 vorgesehenen Gruppen-/Fragepaare. Genau 63 Referenzen sind nicht null: ESS5 21, ESS8 30 und ESS9 12. Die übrigen 111 Paare behalten ausschließlich ID, Zurückhaltungsstatus und `reference: null`. Sie erhalten keine Basis oder Prozente. Alle Kategoriecodes, Reihenfolgen, numerischen Originalanteile, gültigen Nenner und öffentlichen Accountingzahlen entsprechen unverändert den freigegebenen JSON-Eingaben. Es werden keine neuen ESS-Zahlen berechnet oder normalisiert.

Zwei native Auswahlfelder bestimmen Studie und historische Vergleichsgruppe. Anfangs ist keine Studie oder Gruppe gewählt. Ein Studienwechsel setzt die Gruppe zurück. Originalgruppen und deren Reihenfolge werden erhalten, ohne Ranking oder ideologische Ersatzlabels. ESS9-Druckcodes `01`–`09` und API-/Dateicodes `1`–`9` bleiben getrennt. Der Druckcode wird aus der gebundenen Originaloption über das eindeutige Originalnamenlabel bzw. den ausdrücklich gebundenen Other-Eintrag übernommen, nicht aus einem Listenindex.

Eine Frage aus einer anderen Studie erhält einen ausdrücklichen Hinweis ohne Gruppenwerte. Eine zurückgehaltene Referenz bedeutet weder null Prozent noch Mitte. Angezeigt werden je freigegebener Frage alle Originalkategorien sowie der ungewichtete gültige Fragenenner, Gesamtbasis, Missing und NotAsked getrennt. Die gewichteten Anteile verwenden den unveränderten `pspwght`-Nenner gültiger Antworten. Auswahl, Einzelantworten und Überspringgründe bleiben unabhängig in RAM. Es gibt keinen neuen Storage-, Netzwerk-, Output- oder URL-Antwortpfad.

Wahljahr und tatsächliche spätere Befragung stehen getrennt sichtbar. Quellen-Disclosure erhält Erinnerungsgrenze, 15+-Privathaushalte statt verifizierter Wählerschaft, CAPI/CAMI, die schwächere ESS5/8-Aliaszuordnung, ESS9-Appendix 3.0 gegenüber Datenausgabe 3.3, die nicht erhobenen Münchener ESS8-Antworten und das heterogene Other ohne Freitext. Quellenlinks und ESS-ERIC-/Sikt-Attribution unterscheiden Datenrechte (CC BY-NC-SA 4.0) und Dokumentationsrechte (CC BY-SA 4.0). Deutschlandauswahl, Fragenauswahl, historische Gruppierung und Gewichtung sind als Änderungen benannt.

Die Links auf öffentliche Aggregate und README sind fest an den von Root remote-verifizierten Commit `d885a54e46aa9c1675f053b81ed503b0d79e3bdd` des Repositories `https://github.com/hernstev97/12axes-germany` gebunden. Diese Remoteverifikation stammt von Root. Der Autor führte dafür keinen Git- oder Netzaufruf aus.

## Technische Authentizität

`group-reference-generator.mjs` öffnet ausschließlich seine 13 festen öffentlichen Allowlistpfade. Zuerst werden deren tatsächliche SHA256-Bytes geprüft. Rootentscheidung, beide ausdrücklich benannten Rollenentscheidungen und beide tatsächlichen Berichtbytes sind fest gepinnt. Studienausgabe, Katalog, Originalkategorien, Quellenmetadaten, Lizenzen und die exakte Übereinstimmung aller explizit freigegebenen Paare werden geprüft. Die Generatorprüfung summiert nur veröffentlichte Anteile zur Konsistenzkontrolle und prüft veröffentlichtes Accounting. Sie erzeugt keine neue Statistik.

Source-first v1 wird ehrlich wiederverwendet. Der Generator prüft die Bindung an das originale v1-Manifest, den gezielten Methoden-Round1-Entscheid zu v2, ausschließlich zwei geänderte öffentliche Pfaddeskriptoren und die Gleichheit der unveränderten Manifestdeskriptoren. Keine Manifest-, Report- oder Privatpfade werden dynamisch nachgeladen. Die drei privaten Deskriptoren werden allein als öffentliche Manifestmetadaten verglichen. Kein privater Pfad wurde geöffnet, gelistet, stattiert oder gehasht. Roots Aussagen zu tatsächlichen privaten Bytes werden als authentisch gebundene Rootaussagen erhalten, nicht als eigene Nachprüfung ausgegeben.

Zur Laufzeit akzeptiert das optionale Input ausschließlich dieselbe tief gefrorene generierte Artefaktinstanz. Formgleiche Klone und eingespielte Zahlen werden vollständig abgelehnt. Diese bewusste Begrenzung verhindert, dass ein plausibles caller-Objekt eine wissenschaftliche Freigabe vortäuscht. Ein neuer geprüfter Datenstand benötigt erneut feste Pins, Generierung und Paritätsprüfung. Die globale Buildkonfiguration wurde nicht geändert; Root muss die eigene Paritätsprüfung bei Integration mitführen:

```sh
node web/src/app/policy-draft/group-reference-generator.mjs --write
node web/src/app/policy-draft/group-reference-generator.mjs --check
node --test web/src/app/policy-draft/group-reference-generator.test.mjs
```

## Tatsächlich gelesene Dateien

Für diesen Auftrag vollständig gelesen: `docs/handbuch.md`, `docs/project.md`, aktuelles `AGENTS.md`, `docs/auftrag-life-93-breite-2026-10-03.md`, `data/reference-groups-v21/README.md`, die drei öffentlichen Gruppen-JSONs, Root-Gruppenentscheidung, beide unten gepinnten Rollenentscheidungen, Methoden-Round1-Bericht und Quellen-Erstbericht sowie beide tatsächlichen öffentlichen Manifestdateien. Die privaten Deskriptoren wurden nicht verfolgt.

Vorhandene Umsetzung gelesen: `policy-draft.ts`, `.html`, `.scss`, `.spec.ts`, `catalogue-types.ts`, `policy-catalogue.ts`, `historical-reference.ts`, `policy-source-details.html` und die tatsächliche Wrapperdatei `research-preview/policy-preview.ts`. Der öffentliche Originalfragenkatalog und der unveränderte öffentliche TS-Katalog wurden als feste Bindung gelesen bzw. gehasht. `web/package.json` und Root-`package.json` dienten den tatsächlichen Checkbefehlen. Frühere Autorenberichte wurden ausschließlich zur Erhaltungsprüfung gehasht. Kein anderer Ergebnisreview, keine Rohdaten, kein privater Kandidat und keine wissenschaftliche Neuauswertung wurden gelesen bzw. ausgeführt. Ein zusätzlicher begrenzter Inventar-Hilfsagent konnte wegen des aktiven Threadlimits nicht gestartet werden; daraus wird keine getrennte Bewertung abgeleitet.

## Feste öffentliche Eingabepins

| Pfad | SHA256 |
| --- | --- |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `web/src/app/policy-draft/public-catalogue.ts` | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |
| `data/reference-groups-v21/README.md` | `60ba830a02d4371214c29627f255add74d22d70f8f268d83cbeb6c346500342f` |
| `data/reference-groups-v21/ESS5e03_6.json` | `343d06f921f5a943e742f304255726302b71162fb55d8c73b73d11f2f184b19a` |
| `data/reference-groups-v21/ESS8e02_3.json` | `fda4e3dab0546ba25ebb2c265d0d930830615697b023fce2075e41c6a562ff3a` |
| `data/reference-groups-v21/ESS9e03_3.json` | `a1e7f8b116da9d055ffffb2dc5eb2af04e43524962433a9b032f09cbd8b5d093` |
| `reports/loop/policy-group-v21-export-decisions.json` | `544f31f83cac1e258ed13559c04373430a5ac0d792c4380421a32bb623ef42bc` |
| `reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1-decision.json` | `3c99d784d23f070a77a843bb0848f26b16e4f795f951ce60d70346edf389e53a` |
| `reports/loop/reviews/GROUP-RESULTS-V21-001-sources-decision.json` | `b13ae786173c280caf7d1c70f2eccc5015d87b3842fb256575f4f5fb2e95f960` |
| `reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1.md` | `324a7faad5f7c2bb4d8acb2850073a6ac2bcce9607ef3e38c4bd9e668cf3f496` |
| `reports/loop/reviews/GROUP-RESULTS-V21-001-sources-first.md` | `1d359b82b828ba085705d0fcb6803d5b84a46a15de9ed24e06512cccdcfed058` |
| `reports/loop/packages/GROUP-RESULTS-V21-001/v1/manifest.json` | `dddbcda2fe8a18f46a45ee812100508d9c3ed10c5cca8c8d391be648e474b13a` |
| `reports/loop/packages/GROUP-RESULTS-V21-001/v2/manifest.json` | `47aa3e3f3cf6043cc81bf25bf6b1228bc007f4a12c3e2866337d91161f114382` |

## Eigene geschriebene Dateien und endgültige Pins

Ausschließlich die folgenden elf Quell-/Testdateien sowie dieser neue Bericht wurden geschrieben. Eigene QA liegt unter `outputs/loop/angular-group/` mit 0700 für den Ordner und 0600 für Dateien.

| Pfad | SHA256 |
| --- | --- |
| `web/src/app/policy-draft/group-reference-generator.mjs` | `f12a6e8eb528d9776741b8cab5cb327e5d5714d951fd3dfa157075832ad93a9f` |
| `web/src/app/policy-draft/group-reference-generator.test.mjs` | `7891c73f95af6f33ea745524d716b8c395bd5421d3ce193b31c5fbe17e87008c` |
| `web/src/app/policy-draft/group-reference-types.ts` | `539ca2854b8839a7e76590b56ca91f652350093582e68524dea9fe4575a85388` |
| `web/src/app/policy-draft/group-reference.spec.ts` | `31e2f3911f6d687bfb48e83de9ce1fa5820d94d591099e71f695ffc32957e044` |
| `web/src/app/policy-draft/group-reference.ts` | `13d26f381c234f6d78a4687f0002528adf284eae722fa78e506ee1a942c5ca47` |
| `web/src/app/policy-draft/reviewed-historical-groups.ts` | `281159b645ccfc1d254b3745f3bcdab353800607223061fd76e43dced96bd175` |
| `web/src/app/policy-draft/policy-draft.ts` | `ee0267535f812e572a9c15859722bd2449f7681a06f54f52aeece2fe3a09b0fc` |
| `web/src/app/policy-draft/policy-draft.html` | `f556dbb8bf3d6a41503378fd53476356e29cd8b448f2a7e5544b5d695d8087b6` |
| `web/src/app/policy-draft/policy-draft.scss` | `e4f914532aec5cf1e10e392b1a53229f934ceb9179775d2ca2097d0fd6161e30` |
| `web/src/app/policy-draft/policy-draft.spec.ts` | `a7acd030dd1f86787559a8f113896fb9928e266f48d2bd916cdc70fd7771dd87` |
| `web/src/app/research-preview/policy-preview.ts` | `52832ad57f51c62a6aa2f9600626cad71b78657938e709fbac8737939d49cccd` |

## Tatsächliche Checks und Fehler

- Vier Node-Generatorprüfungen bestehen. Sie prüfen den geschlossenen öffentlichen Satz, veränderte echte Anteile, erfundene Rollen-/Reportbindungen, Originalberichtbyteänderung, vollständige Quellparität, alle 63 Referenzen/111 Nullreferenzen und die generierten Bytes.
- 47 gezielte Angular-Tests in vier Dateien bestehen. Darin 26 Komponententests und zwei neue Gruppenbindungschecks. Native Auswahl, ursprüngliche Reihenfolge, Originalcodes, unveränderte angezeigte Anteile, Accounting, fremde Studien, Other ohne Zahlen, Studienwechsel, Ablehnung eingeschleuster Referenzen, unabhängige Antwortnavigation und fehlende Storage-/Fetch-/URL-Antwortpfade sind geprüft. Bestehende Fokus-/Scrolltests bleiben erhalten.
- Abschließender Typecheck (`ngc` App und `tsc` Specs) besteht. Scoped Prettiercheck für alle elf Dateien besteht. Handbuchcheck besteht mit 46 Quelldateien. `pnpm --filter politikprofil build --configuration research` besteht, fertig um 16:10:47.798 UTC.
- Tatsächlicher erster Handbuchfehler: sichtbare Semikolons in neuer HTML-Prosa. Die entsprechenden Aussagen wurden getrennte Sätze. Danach bestand der Check.
- Tatsächlicher erster Angularfehler: 46 von 47 Tests bestanden. Nach Bearbeiten und Rückkehr war die gespeicherte Gruppenwahl noch in RAM vorhanden, das neu erzeugte native Select zeigte jedoch die leere Option. Ursache war die Bindungsreihenfolge vor Erzeugung dynamischer Optionen. Explizite `selected`-Bindungen an Studien-/Gruppenoptionen korrigieren den sichtbaren Zustand. Der vollständige gezielte Lauf bestand danach mit 47 Tests.

Die vorhandene jsdom-Testdouble für `scrollIntoView` zeichnet Ziel, Reihenfolge und Optionen auf. jsdom hat keine echte Layout-/Scrollbeobachtung. Dieses Paket erfindet keinen Browser- oder Sichtbarkeitsbeleg. Allgemeines `pnpm check` wurde auf Rootauftrag während paralleler Schreibarbeit nicht ausgeführt; Root übernimmt diesen Integrationscheck. Kein Server, Browser, Git, Installations-, Auth-, Netz- oder Claude-Aufruf erfolgte.

## Unverändert und weiterhin offen

Die geschützten Einzelreferenzdateien, der öffentliche Originalkatalog mit 43/315 Zuordnungen, Kataloghelper und die vorherigen Autorenberichte bleiben unverändert. Nachher-Hashes stimmen mit den vor Auftrag gesicherten Hashes überein:

| Pfad | Unveränderter SHA256 |
| --- | --- |
| `web/src/app/policy-draft/generate-reviewed-references.mjs` | `e7389ab3b21e6584b4ce30eb00fd8c196e849577e0e0b971bce118ee6b1d565a` |
| `web/src/app/policy-draft/reviewed-historical-references.ts` | `d1f0e17dcffe6b40df3664ed6ddbe34cb849a456d036af1c6ab607ab0dad03f2` |
| `web/src/app/policy-draft/public-catalogue.ts` | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |
| `web/src/app/policy-draft/reference-binding.ts` | `07a928b852be0abb47025ecd2aa64af3c9db32fd36b3c564716dbed55ab69dfb` |
| `web/src/app/policy-draft/policy-catalogue.ts` | `640f6470bddce074d034c5ed9a18174c95e4447fb2f3c3ba6e8848a36192c984` |
| `web/src/app/policy-draft/historical-reference.ts` | `58eb05517a43a4d3ea0a62c20f06c39857ca242e50748d3bce1a0f17a33683ab` |
| `reports/loop/authors/ANGULAR-POLICY-DRAFT-WIP.md` | `a0f1474a8360045f7b5800c0a1b3f5dbf102dd15c7aa62cdf74bac8766a6425d` |
| `reports/loop/authors/ANGULAR-REFERENCE-BINDING-WIP.md` | `051a4b933bf2da29b9291a1380f47980831f206e27568abdb41b101e9f98ab43` |
| `reports/loop/authors/ANGULAR-SCROLL-ROUND1.md` | `38ce7d12a9757ed6e6493385f13061f52ac633831eeed43a925de6ad0e318b8b` |

Root führt die frische Integration, unabhängige begrenzte Darstellungs-/Quellenprüfung und den tatsächlichen Browserharness auf Desktop und Smartphone aus. Native Selects, Umbruch bei 320px, Quellenzugang, Edit-Fokus/Sichtbarkeit und Gleichbehandlung aller Gruppen benötigen dort echte Beobachtung. Menschliche Verständlichkeits-/Designannahme, Stevens Claude-Schlusskontrolle, rechtsfachliche/kommerzielle Prüfung und Releaseentscheidung stehen aus.

Keine aktuelle Parteiposition, persönliche Parteizuordnung, Norm, Präzisions-/Anonymitätsvalidierung, neue Administration, SE/CI, Punktzahl, Ranking, Nähe, Pooling oder Gesamtempfehlung wird aus diesem technischen Paket abgeleitet. Source-first-Reuse ist keine neue Erstbewertung. Beide bereits gebundenen Ergebnisrollen gehören zur Codex-Familie und können gemeinsame Fehler teilen. Dieses Paket ist konkret prüfbare Vorbereitung und bleibt WIP.
