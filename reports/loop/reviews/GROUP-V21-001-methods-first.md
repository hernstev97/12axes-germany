# GROUP-V21-001: getrennte Erstbewertung Methoden und Reproduzierbarkeit

3. Oktober 2026. Rolle `methods_reproducibility`. Prüfgegenstand ist ausschließlich `GROUP-V21-001/v1` mit Manifest-SHA256 `73868d634da6a47fc7e5e72c858a4e93479785b892ffd6de65fda0c4243726a4`.

## Ersturteil

`ACCEPTED_BOUNDED` für die Methoden- und Softwareseite des beschriebenen Übergangs. Die expliziten Studienkennungen dieser Rolle sind `ESS5e03_6`, `ESS8e02_3`, `ESS9e03_3`, `ESS10SCe03_2` und `ESS11e04_2`. Ich habe keinen erheblichen Implementierungsfehler gefunden, der die gepinnte reine Gruppenkalkulation oder den beschriebenen Guard unter dessen angegebenem Protokollmodell blockiert.

Dieses Urteil erstellt keinen Gate, keine Planfestschreibung und keine Rohdatenfreigabe. Neue Parteisemantik bleibt bis zur Annahme durch Root und zum eigenen vollständigen v2.1-Gate gesperrt. Die zweite getrennte Rolle muss ihren Quellen- und Bedeutungsumfang selbst beurteilen. Root muss die akzeptierten Studienumfänge schneiden und die tatsächlichen Berichtsbytes binden. Das Ersturteil bestätigt weder empirische Güte noch Neutralität, Produkt-, Veröffentlichungs- oder Releaseannahme.

## Lesebasis und tatsächliche Bytepins

Ich las das aktuelle Manifest und prüfte die SHA256 aller 51 darin genannten Artefakte gegen ihre tatsächlich gelesenen Bytes. Alle stimmen. Die vollständigen erwarteten und beobachteten Hashwerte stehen in `outputs/loop/group-v21-methods-review/byte-pins.json`. Für den Kern gelten folgende beobachteten SHA256:

| Artefakt | Beobachteter SHA256 |
| --- | --- |
| `data/gruppenvertrag.v2.1.entwurf.json` | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `data/analysevertrag.v2.entwurf.json` | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `pipeline/policy_groups_v21.py` | `9b680b07385cefc665a54e583cf4b44f03d1305b2829a724fb9afbd7103284b6` |
| `pipeline/policy_group_access_v21.py` | `a662e216c82085ab0a059056715ea880e3d9c63ba8ade9efaff2b5e7881a2f58` |
| `pipeline/policy_access_v2.py` | `f2c26b2895f1730a344fde41fee63a960b9ff30f63a68a7beefb82a33e6366db` |
| `pipeline/policy_adapter_v2.py` | `3159243bc6f536359c896e414e8f418955b51e7504e38f3add62a811b0e5500e` |
| `pipeline/policy_analysis_v2.py` | `d7d23c99b84d352f161ea607f575155594ecd1ff365ad89e8f2624b4f9500309` |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/policy_export_v2.py` | `27b225b5975f0c321f08adbfa7ccab4e03dae8421f3987d0e104cf4945d0437a` |
| `pipeline/policy_report_v2.py` | `53d68f23f2bf7c57c95e2bdd55ae0059da4dfe8598bcbd12e2681206a9e4d6ea` |
| `pipeline/tests/test_policy_groups_v21.py` | `e60f7df0b3c5989d6fbc688358af8c7c0a93ef57ceb1b6caafbf8c062d3ebddd` |
| `pipeline/tests/test_policy_group_access_v21.py` | `27130d07b1f573ef0d0113459a19b66676bb93a84afb7aea1ffeb8896d915c8d` |

Die 32 Quellencaches wurden als gepinnte öffentliche Dokumentation und Metadaten behandelt. Ihre Byteidentität wurde vollständig geprüft. Für die Recheninventur verglich ich außerdem alle im Vertrag referenzierten `voteField`- und `nationalParty2Field`-Metadaten mechanisch mit den gepinnten Originalcodelisten. Feldkennung, Metadatenversion, Variablenname sowie Codes, exakte API-Labels, Missingkennzeichen und Reihenfolge stimmen. Für jede Studie entspricht das Gruppeninventar genau den gültigen API-Parteicodes in deren Reihenfolge und enthält genau eine erhaltene Other-Gruppe. Die Einzelprüfungen stehen in `inventory-metadata-consistency.json` im eigenen QA-Verzeichnis. Das ist keine Abnahme der nationalen Bedeutungs- oder Aliasbindung.

Der ausdrücklich gepinnte Erratumbeleg `reports/loop/authors/BREADTH-GROUP-SOURCES-005-erratum.md` wurde als begrenzte Ausnahme gelesen. Sein tatsächlicher SHA256 ist `fcd487d0248fb8784f7d5072cbc2fc2e47b972b96037efe370c7fd3e68f20a20`. Er korrigiert einen historischen Zugangssatz aus Auftrag005 anhand einer Root-Mitteilung und bezeichnet sich selbst als nicht unabhängig auditierten Zugangsbeleg. Die spätere v2-Laufmitteilung ist im eigenen KnownDataContext-Pin gebunden: `outputs/loop/group-contract-v21/known-data-context.json`, tatsächlicher SHA256 `a20e066d7400826142cdcd8ace27bb0c8df6d48d3101bfebb3acd4d03b305c92`. Ich behandelte beide als deklarierte Zugangslage, nicht als Ergebnis- oder Reviewerurteil. Keine anderen Autoren-, Reviewer-, Zustands-, Handoff- oder Verteidigungsberichte wurden gelesen.

Zusätzlich las ich ausschließlich den vorgeschriebenen Sprachskill `/home/stevenh/projects/12axes-germany/.agents/skills/unslop/SKILL.md` als Verfahrenszugriff. Es gab keinen Zugriff auf Elternhistorie oder Erinnerungsdateien. Die importierten Projektmodule und Tests wurden direkt aus ihren gepinnten Quelldateien geladen; Paket-`__init__` und Bytecodecache wurden dabei nicht gelesen oder geschrieben.

## Geprüfte Kalkulation

`policy_groups_v21.py:266–323` prüft das vollständige deklarierte Gruppeninventar, die eindeutige Other-Gruppe und die identische Regelzuordnung. Gruppen werden weder nach beobachteter Größe ausgewählt noch zusammengelegt. Die API behält auch leere Gruppen und alle ursprünglichen Antwortkategorien. Other bleibt ein heterogener Rest ohne Kohärenzbehauptung.

Eligibility verlangt `DE`, `vote == 1` und einen gültigen nationalen Parteicode der zweiten Stimme. `policy_groups_v21.py:430–458` zählt gültige Parteiangaben bei jeder Nicht-Ja-Wahlantwort als Inkonsistenz und weist diese Fälle keiner Gruppe zu. Es gibt keine Reparatur, Imputation oder zusätzliche Gruppe für ungültige Stimmzettel. Die Wahlzustandsachse und die Parteizustandsachse summieren jeweils auf die DE-Basis; der Inkonsistenzzähler beschreibt eine beobachtete Kombination. Die beiden Achsen werden nicht als disjunkte Teilmengen addiert. Quellenmissing, strukturell nicht gefragt und technischer Exportblank bleiben getrennt.

Für jede Kombination aus Studie, Gruppe und Item erzeugt `policy_groups_v21.py:372–395` getrennte Referenzen. Der primäre Nenner enthält ausschließlich die `pspwght`-Gewichte gültiger Antworten dieses Items in dieser Gruppe. Missing und nicht gefragt sind in der eigenen Buchführung, außerhalb dieses gültigen Nenners. Die Sensitivitäten verwenden dieselben Fälle und Kategorien mit `dweight` beziehungsweise ungewichtet; `anweight` bleibt Äquivalenzdiagnose. Die Wiederverwendung von `categorical_reference` bindet die Summe der gültigen Kategoriegewichte an den gültigen Nenner, siehe `policy_reference_v2.py:205–247`. Die Prüfung in `policy_analysis_v2.py:319–354` kontrolliert Buchführungsidentitäten und Kategorienanteile.

Alle eligible Gruppenfälle brauchen positive endliche `pspwght`, `dweight` und `anweight`, einschließlich Fällen mit ausschließlich fehlenden oder nicht gefragten Itemantworten. Gewichte außerhalb dieser Eligibility werden nicht interpretiert. Das Verhältnis `anweight / pspwght` wird genau einmal je Studie über alle eligible Gruppenfälle gebildet, einschließlich Other und Itemmissing, siehe `policy_groups_v21.py:459–476`. Nichtkonstanz bleibt eine private Diagnose und ändert weder Fälle, primäre Gewichte, Auswahl noch Status. Numerisch nicht darstellbare Verhältnisse oder Summen führen zu einem statischen Studienabbruch.

Die festen Schwellen 100 gültige Fälle und 5 Fälle in jeder positiven ursprünglichen Kategorie verwenden ungewichtete Itemfälle. Nullkategorien bleiben mit Nullanteil erhalten, sofern ein gültiger Nenner besteht. Bei keinem gültigen Nenner sind die Anteile `None`, später JSON `null`; sie werden nicht zu Null umgedeutet. Kein Ergebnis wird als geprüft oder öffentlich markiert. Design, Varianz und Standardfehler bleiben leer; Konfidenzintervalle, Pools, Gesamtdistanz und gemeinsame Personenverknüpfungen werden nicht erzeugt.

Politische Gleichbehandlung wurde für jede deklarierte Gruppe aller fünf Studien mit identischen synthetischen Grenzfällen geprüft. Die Testfälle wechseln ausschließlich den Gruppencode bei identischer Fall- und Antwortstruktur. Named- und Other-Gruppen erhalten dieselben Schwellen, Inventar- und Missingregeln. Das prüft die Gleichheit der Softwarekriterien und beweist keine inhaltliche Neutralität.

## Geprüfter I/O-Guard

Der v2.1-Runner verwendet einen eigenen Gatepfad, eine eigene Freigabeentscheidung und `analyseplan-v2.1`. `policy_group_access_v21.py:341–414` verlangt exakt die zwei Rollen, positive Gateentscheidungen, eindeutige Reportpfade und deren tatsächlich gelesene, nicht leere Berichtsbytes mit passenden Hashes. Der Gate enthält eine explizite, eindeutige `allowedStudyIds`-Liste; eine ausgeschlossene Studie scheitert vor Rohdatenzugriff. Alte v1-/v2-Gates und frühere Runner werden nicht als Gruppenfreigabe benutzt.

Vor dem ersten Rohpfadzugriff bindet der Guard Manifest, beide Verträge, Katalog, Planfestschreibungsbytes, Commit-/Tagangaben, die 32 Quellencaches, zusätzliche feste Referenzen und die ausführenden Modulquelldateien. Die Gruppenregeln, Quellenidentitäten und studienspezifischen Bindungen sind zusätzlich als feste Projektionen geprüft. Öffentliche Artefaktpfade werden vor ihrem jeweiligen Lesen geprüft; Roh-/Local-/Zustandspfade können nicht als Zusatzpin eingeschleust werden. Die Runtimeprüfung kontrolliert sowohl die zum Import dokumentierten Quelldateihashes als auch die aktuelle Quelldateiversion.

Erst danach liest `policy_group_access_v21.py:617–620` die Rohbytes und kontrolliert den opaken Hash sowie die Bytezahl vor UTF-8-Decodierung. Der wiederverwendete reine Metadatenhelfer prüft alle DE-Zeilen auf Runde und Edition, bevor die Gruppenkalkulation Parteifelder interpretiert, siehe `policy_access_v2.py:365–379`. Lexikalische CSV-Traversierung fremder Spalten ist deklariert; umfassende Blindheit wird nicht behauptet. Die enge Ganzzahl-/Nullbruchregel akzeptiert keine führenden Nullstellen, wissenschaftliche Schreibweise, Vorzeichen, fremden Literale oder getrimmte Antwortcodes. Gedruckte Fragebogencodes werden nicht automatisch in Dateicodes umgewandelt.

Pfadkomponenten und Blätter werden descriptorrelativ mit `O_NOFOLLOW` geöffnet; der Runner akzeptiert nur reguläre Dateien. Die Fehlernachrichten enthalten feste Codes statt Personenkennungen, Header oder Zellen. Die Serialisierung in `policy_group_access_v21.py:431–530` nennt Aggregate explizit und traversiert weder Personenrecords noch allgemeine Dataclass-Dumps. Ein Recordobjekt oder ein behaupteter öffentlicher Fragezustand wird zurückgewiesen.

Der private Writer prüft 0700 für seine Local-Unterverzeichnisse und 0600 für Dateien. Er schreibt eine eigene exklusive temporäre Datei, synchronisiert sie und ersetzt das Ziel atomar. Bei einem Abbruch vor dem Ersetzen bleiben alte Bytes erhalten. Scheitert die Verzeichnissynchronisierung danach, versucht er die eigene alte Hardlinkkopie wiederherzustellen; bei zusätzlichem Wiederherstellungsfehler bleibt diese private Kopie erhalten. Namenskollisionen führen nicht zum Löschen fremder temporärer Dateien. Das ist eine kontrollierte Rückrollgrenze, keine Garantie gegen gleichzeitig feindlich eingreifende Prozesse oder beliebige Dateisystemausfälle.

## Prüfläufe

Ausgeführt wurde `PYTHONDONTWRITEBYTECODE=1 python outputs/loop/group-v21-methods-review/qa_review.py`. Der eigene Runner lenkte die vorhandene I/O-Testsuite auf `outputs/loop/group-v21-methods-review/synthetic-repositories` um und verweigerte jeden Gruppenlauf mit einem anderen Root. Alle künstlichen Repositories, ihre künstlichen Rohdaten-, Gate-, Freeze- und privaten Dateien entstanden ausschließlich unter diesem eigenen QA-Verzeichnis. Die Fixtures lasen oder kopierten keine echten ESS-Roh-/Localdateien. Die Repository-Leseschranke erlaubte gepinnte Quelldateien, das Manifest und eigene QA-Artefakte.

| Suite | Tests | Ergebnis |
| --- | ---: | --- |
| Vorhandene reine Gruppentests | 18 | bestanden |
| Vorhandene Guardtests | 43 | bestanden |
| Eigene unabhängige Gegenfälle | 9 | bestanden |

Keine Fehler, Fehlschläge oder übersprungenen Tests. Die vollständigen Logs und die maschinenlesbare Zusammenfassung stehen im eigenen QA-Verzeichnis. Die eigenen Gegenfälle prüfen einen separaten Bruchrechnungsorakel für zwei Items mit unterschiedlichen Missing-/Not-asked-Nennern, sämtliche Gruppen unter denselben Schwellen, Nichtkonstanz ausschließlich in einer vollständig itemmissing Other-Gruppe, alle Nicht-Ja-Inkonsistenzen, ungültige Gewichte bei Itemmissing/Not-asked, Quellenbyte- und Reportbytedrift vor Rohzugriff, einen letzten DE-Rundenfehler vor früherer ungültiger Parteisemantik und Rückrollen beim ersten privaten Output ohne vorhandene Altdatei.

Es gab keinen echten Studienlauf, tatsächlichen Gate-/Freeze-Zugriff, Git-/Tag-/HTTP-/Auth-/Installations-/Server-/Exportzugriff. `pnpm check` wurde innerhalb dieser Erstbewertung nicht ausgeführt, weil es fachliche Dateien außerhalb der festgelegten Pin-Lesebasis einbeziehen würde. Gemeinsame Forschungs-, Implementierungs- und UI-Dateien wurden nicht geändert. Die technischen Tests sind synthetische Softwarebelege und keine empirisch bestandenen Prüfungen.

## Konkrete offene Grenzen

Erhebliche negative Befunde: keine unter der geprüften gepinnten Kalkulation und dem dokumentierten Protokollmodell. Folgende Grenzen bleiben Bestandteil der Annahme; sie sind keine Stilbeanstandungen.

- `GROUP-V21-METHODS-L01`: Nationale Bedeutungs-, Alias-, Modus- und historische Codebindungen benötigen das eigene Urteil der Quellenrolle. Der mechanische Codelistenabgleich und die Bindung vorhandener Dokumentbytes schließen die im Vertrag selbst genannten Concordance-/Recodegrenzen nicht. Die PDFs wurden auf Byteidentität geprüft; ich beanspruche keine vollständige erneute Primärquellenprüfung.
- `GROUP-V21-METHODS-L02`: Der Guard bindet Berichtsbytes und vom Gate behauptete Entscheidungen. Er liest kein Entscheidungs-JSON und authentifiziert weder Revieweridentität noch die Bedeutung eines Markdownurteils. Root muss die tatsächlichen Urteile, ihre positiven Studienumfänge und die Übereinstimmung mit dem Gate vorab prüfen. Ebenso sind Commit-/Tagangaben und externe Pins Vertrauensvoraussetzungen; die Software verifiziert keine Remote-Git-Provenienz. Quelldateihashes schützen nicht gegen beliebig veränderte Pythonobjekte oder einen feindlichen privilegierten Aufrufer.
- `GROUP-V21-METHODS-L03`: Echte Dateiedition, Antwortliterale, DE-Identitätseindeutigkeit, eligible Gewichte, Gruppengrößen, tatsächliche Nenner und anweight-Verhältnisse wurden nicht geprüft. Bei späterem autorisiertem Zugriff können die vorgesehenen statischen Abbrüche auftreten. Synthetische Erfüllung ersetzt diese Beobachtung nicht.
- `GROUP-V21-METHODS-L04`: 100/5 sind feste Projektregeln für die spätere Darstellung und keine nachgewiesene Präzisions- oder Anonymitätsgarantie. Kleine und leere Gruppen bleiben als private Kandidaten erhalten. Eine spätere Veröffentlichung braucht eigene getrennte Ergebnisurteile und Roots explizite Aggregatexportentscheidung.
- `GROUP-V21-METHODS-L05`: Bekannte historische v1-A/B-Werte und der deklarierte v2-Marginallauf verhindern die Behauptung eines umfassend unberührten Bestätigungssatzes. Das eigene Ersturteil wurde vor Parteisemantik und ohne andere Ersturteile oder Root-Verteidigung formuliert. Gleiche Codexfamilie und gemeinsame Quellen erlauben gemeinsame Fehler; daraus folgt keine wissenschaftliche Unabhängigkeit oder bestätigte Neutralität.

Die eigene Annahme reicht somit bis zur gepinnten, getrennten, privaten deskriptiven Gruppenkalkulation nach vollständiger v2.1-Übergangsfreigabe. Neue Parteisemantik bleibt bis zur Rootannahme gesperrt.
