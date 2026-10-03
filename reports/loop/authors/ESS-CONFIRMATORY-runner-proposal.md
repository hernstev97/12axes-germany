# Bestätigungsrunner für das eingefrorene Modell

Autorenfassung vom 3. Oktober 2026. Das neue Modul ist mit erfundenen Daten ausgeführt; es erteilt keine methodische Abnahme, A-/B-Datenfreigabe oder Veröffentlichungserlaubnis. Geschrieben wurden nur `pipeline/ordinal/confirm.R`, dieser Bericht und `outputs/loop/resume-confirmatory-author/`. Keine echte ESS-Antwort, A/B-Datei, Assignmentdatei, Datei unter `data/raw/` oder `data/local/` wurde gesucht oder geöffnet. Keine anderen aktuellen Gateurteile wurden gelesen. Keine Git-Aktion, Installation, Tags, weiteren Agents, Reviewdienste oder `pnpm check`.

Die abgeschlossenen Support-/A-Autorenberichte und historischen Runs bleiben erhalten. Der Koordinator hat vor diesen Läufen die A-Konfiguration und den A-Runner gezielt auf die beidseitige Faktorkorrelationsregel korrigiert. Dieser neue Autorenschritt bindet **diese korrigierten** A-Quellen; er schreibt sie nicht selbst. Der alte A-Bericht bleibt eine historische Fassung mit seinen damaligen Pins und wird nicht nachträglich umgedeutet.

## Fester Modellvertrag

[`confirm.R`](../../../pipeline/ordinal/confirm.R) bietet `ec_analyse(frame, freeze, cfg, pins)` rein im Speicher und `ec_main(project_root, input_csv, freeze_path, private_output_dir, authorization)` für die spätere kontrollierte Dateischnittstelle. Der vollständige Modellvertrag enthält exakt:

| Feld | Zulässiger Inhalt |
| --- | --- |
| `schema` | `life93-model-freeze-1` |
| `model` | M2 oder M3, keine neue Konkurrenzwahl |
| `scores` | Kanonisch geordnete Untermenge der Scores dieses Modells, mindestens zwei |
| `items` / `groups` | Alle neun Originalitems und die unveränderten Modellgruppen aus der festen Konfiguration |
| `config` | Inhaltlich dieselbe vollständige Konfiguration; JSON-Objektschlüsselreihenfolge und Integer-/Double-Repräsentation ändern ihre Bedeutung nicht |
| `source_code_pins` | Die vier exakt gebundenen A-Quellen develop/config/adapter_v2/support |
| `a_result` | Genau `path="reports/phasen/01-a-entwicklung.json"` und SHA256 des öffentlichen A-Trainingsartefakts |

Neue Scores, andere Items/Polungen, veränderte Gruppen, Kriterien, Quellpins, nicht öffentliche A-Referenzpfade und fremde zusätzliche Metadaten werden abgelehnt. Das A-Trainingsartefakt bewahrt die geschätzten A-Ladungen/Korrelationen als Referenz. B schätzt die freien Parameter desselben vorab bezeichneten Modells erneut. Die A-Zahlen werden **nicht** als exakte B-Parameterrestriktionen eingesetzt. Die beobachteten Scoregewichte bleiben 1/k auf fest normierten Kategorien; sie werden nicht anhand von B angepasst.

Der Dateiaufruf verlangt vor jedem Dateiread den Root-Kontrollbeleg `decision="ACCEPTED_BOUNDED", arm="B", wrapper_verified=TRUE` und `freeze_sha256`. Er prüft den Freezehash, dessen Schema/Inhalt und anschließend den Hash der festen öffentlichen A-Referenz, bevor er den B-Input liest. Ein zukünftiger positiver Rootloader/-wrapper muss tatsächliches B-Gate, unveränderten Auswahlvertrag, Eingabepfad, Blindfelder und alle Code-/Artefaktpins prüfen. Der R-Kontrollbeleg allein ist kein gegen absichtliche Umgehung geschützter Zugriffsnachweis. Die pure Speicher-API behandelt den übergebenen gültigen Freeze als Vertrag; sie kann dessen historische A-Autorität nicht aus sich selbst belegen.

`cfg$status="AUTHOR_DRAFT_NO_EMPIRICAL_GATE"` wird aus der unveränderten Konfigurationsquelle übernommen. Weder dieses Statusfeld noch ein synthetisches Erfolgsergebnis entscheidet über Freeze- oder Gateautorität. Dafür sind die tatsächlichen Rootartefakte und Abnahmen maßgeblich. Es gibt keine Dateisuche oder automatische öffentliche Kopie.

## Genau ein Modell, genau die vorgewählten Scores

Der Inputvertrag bleibt `stratum,psu,weight,B34,B35,B36,B40,B41,B42,B43,B44,B45`. Bereits orientierte Itemkategorien sind 0 bis K−1 mit K=5/5/5/4/4/4/11/11/11; fehlende Werte bleiben `NA`. Endliche positive Gewichte, vollständige numerische Designcodes und die exakte Spaltenliste werden durch die unveränderten A-Helfer geprüft. Eine einzige vollständige Neunitemmaske gilt für Momente, Modell und Rohdominanz; alle ausgewählten ursprünglichen PSUs bleiben einschließlich Null-Domänen-PSUs im Designrahmen.

Der Runner passt nur das eingefrorene gemeinsame CFA-Modell an. EFA wird ausschließlich mit dessen Faktorzahl ausgeführt: Geomin, 30 Starts, epsilon .001, Seed 2026100313; Wiederholung Seed 2026100314 sowie Oblimin. Importprüfung, vollständiger Vorzeichen-/Permutationsabgleich, 1e−4 Wiederholtoleranz und positive betragsmäßig größte erwartete Gruppenladung mit 1e−8 Gleichstandstoleranz nutzen unveränderte A-Funktionen. Es werden weder `ed_efa_suite` für alle Faktoranzahlen noch `ed_analyse`/`ed_select` oder konkurrierende CFA-Modelle aufgerufen. Gedrehte EFA-SE werden nicht berichtet.

Alle Modellfaktoren, alle neun Items und sämtliche Faktorkorrelationspaare bleiben global erhalten, auch wenn H kein zuvor gewählter Score ist. `ed_score_criteria` wird nur auf die im Freeze ausgewählten Gruppen angewendet: Für ausgeschlossenes H werden weder eine neue H-Scorediagnostik berechnet noch H als Score hinzugefügt. Globale standardisierte H-Ladungen und H–Z/H–F-Korrelationen bleiben Bestandteile des vollständigen Modells.

Die numerischen Regeln übernehmen die korrigierte feste A-Fassung unverändert: W=I, tatsächliche ULS-Punkte auf surveygewichteten Schwellen/Polychoriken, eigenes beobachtetes Schätzgleichungs-Jacobian einschließlich Residualkrümmung, tatsächlich standardisierte Delta-Transformationen, beobachtete normalisierte Score-Reliabilität und rohe/modellimplizierte Kovarianzdominanz. Globaler Residual-RMS hat eine einseitige normale 95%-Obergrenze ≤.10. Andere Regeln verwenden zweiseitige normale 95%-Intervalle; Ladungen/Dominanz haben Bonferroni innerhalb des festen Scores, Faktorpaare Bonferroni über **alle** Paare des vollständigen Modells. Jede Faktor-Korrelationsuntergrenze muss >−1 **und** jede Obergrenze <+1 liegen. Score-Reliabilitätsuntergrenze >.50; alle Ladungsuntergrenzen >0; beide Dominanzobergrenzen ≤.50. Nearzero-RMS bleibt unentschieden. Das sind eigene Projektbudgets, keine hier neu behaupteten Literaturstandards.

Vorab gewählte Scores können nur bleiben oder entfallen. Globale Verletzung, ein gescheiterter Fit oder weniger als zwei weiterhin passende Scores ergibt `NO_PUBLIC_PROFILE` und eine leere für Profile behaltene Scoreliste. Individuell erfolgreiche Scorekennwerte bleiben dabei diagnostische Zahlen, keine durch den globalen Fehler hindurch geretteten Profilbehauptungen. Ein rein numerischer Erfolg heißt `CRITERIA_PASSED_PENDING_RESULT_REVIEW`. Es gibt keine Parameterrettung, Itemlöschung, Umpolung, Ersatzscore- oder Konkurrenzmodellwahl. Einzelne EFA-/CFA-Ausfälle behalten feste Fehlercodes.

## Späterer Full-DE-Weg und private Ausgabe

Dieselbe Rechenschicht unterstützt optional `arm="FULL"`. Der Dateikontrollbeleg muss zusätzlich `B_step_completed=TRUE` und die kanonische mindestens zweielementige `B_retained_scores`-Untermenge des unveränderten Freeze enthalten. Full-DE prüft nur diese noch zulässigen Scores; ein in B entfallenes H kann auch bei anschließend guten H-Daten nicht wieder aufgenommen werden. B mit weniger als zwei behaltenen Scores öffnet diesen Profilweg nicht. Der Rootloader muss vor der realen Full-Anwendung den abgeschlossenen B-Schritt, den unveränderten Freeze und die originalen Full-DE-Gewichte/den vollständigen Originalrahmen bestätigen. R allein kann die Provenienz der übergebenen positiven Gewichtszahlen nicht beweisen. Die Full-DE-Diagnose enthält A/B und wird ausdrücklich nicht als unabhängige neue Bestätigung bezeichnet.

Ausgabeordner müssen bereits mit 0700 existieren. Der Runner erzeugt ausschließlich `confirmation-aggregate.private.json` und `confirmation-config.private.json` mit 0600 und verweigert Überschreibung vor Inputread. Er exportiert keine RDS-Fits oder Fallobjekte. stdout enthält ausschließlich feste Erfolgs-/Fehlercodes; potenziell werte- oder pfadhaltige Bibliotheksmeldungen werden unterdrückt und als feste Codes behandelt.

Die Aggregat-Whitelist besteht aus Arm/Scope, unverändertem Freeze/Config, öffentlichen Codepins, Fall-/PSU-/Stratum- und Fehlanzahlen, fehlender Gewichtsmasse, 87 expliziten Momentlabels/Punktmatrizen, der einzigen gewählten EFA-Struktur, standardisierten CFA-Punkten/Intervallen, Diagnosen, nur vorab ausgewählten Score-Kovarianzen/Kriterien sowie Bestätigungsstatus. Keine Einzelzeilen, vollständigen Masken, Gewichtsvektoren, Personen-/PSU-/Stratumkeys, persönlichen Scores, Fallbeiträge, privaten Adapter-/Fitobjekte oder RDS-Dateien werden ausgegeben. Öffentliche Ergebniskopien bleiben der späteren Rootpublikationsprüfung vorbehalten.

## Tatsächliche Checks

Der [Hauptlauf test-001](../../../outputs/loop/resume-confirmatory-author/test-001-checks.json) besteht **113/113** Assertions, exit0, UTC 11:13:00–11:13:38 am 3. Oktober 2026. [Laufbeleg](../../../outputs/loop/resume-confirmatory-author/test-001-command.json), archivierte Quellen und Hashindex liegen im eigenen ignorierten Ordner. Keine echte Bestätigungsstichprobe wurde verwendet. Alle sieben Hauptfälle haben 7680 erfundene Fälle, 192 PSUs in vier Strata, vier vollständig fehlende PSUs, 7520 vollständige Neunitemfälle und 87 Momente. M2/M3-Samen sind 2026100341/42; schwaches H nutzt 2026100326, schwaches Z 2026100344. Starke Ladungen .82, schwache .25. Die Zufallsfaktoren enthalten einen gemeinsamen und einen PSU-Anteil.

| Erfundenes Szenario / eingefrorene Auswahl | Tatsächliche Ausgabe | RMS-Obergrenze einseitig95 |
| --- | --- | --- |
| Echtes M2 / H,ZF | Kriterien passen, H/ZF bleiben | .01236443 |
| Echtes M3 / H,Z,F | Kriterien passen, H/Z/F bleiben | .01012317 |
| Schwaches H / H,Z,F | H entfällt, Z/F bleiben | .01732941 |
| Schwaches H / nur Z,F | Nur Z/F geprüft, H wird nicht hinzugefügt | .01732941 |
| Starkes H / nur Z,F | Auch das gute H wird nicht hinzugefügt | .01012317 |
| Schwaches Z / nur Z,F | Nur F passt: `NO_PUBLIC_PROFILE` | .00902169 |
| Drei starke Trios / eingefrorenes M2 | Globaler Strukturfehler: kein Profil, kein Wechsel zu M3 | .19154806 |

Im schwachen H-Fall liegt die echte Reliabilitätsuntergrenze H=.13582678; Z=.80881157 und F=.83677416 bleiben passend. Im schwachen Z-Fall Z=.11782054/F=.83958989, bei weiterhin passendem globalen M3: der Zweidimensionsvertrag sperrt das Profil tatsächlich. Beim strukturell falschen eingefrorenen M2 passen beide individuellen Reliabilitäten H=.82815365/ZF=.69080721; dennoch sperren RMS/Zuordnung alle Profilbehauptungen. Der größte tatsächliche Geomin-Wiederholabstand im Hauptlauf ist 2.254e−5 und bleibt innerhalb der unveränderten 1e−4-Regel.

Instrumentierte unveränderte Fithelfer belegen pro Fall exakt drei EFA-Läufe der eingefrorenen Faktorzahl und genau einen CFA-Fit des eingefrorenen Modells. Die Instrumentierung verändert keine numerischen Ergebnisse. Auf denselben tatsächlichen Moment-/Designobjekten stimmt die neue CFA-Rechnung mit der korrigierten A-Helferrechnung exakt in standardisierter Inferenz, RMS-Intervall, vollständiger Korrelationsfamilie und Scorekriterien überein. Weitere Checks prüfen Freeze-/Quell-/Kategorie-/Spaltenfehler, fremde Metadaten, kanonische Scoreauswahl, keine Wiederaufnahme in FULL, Gateablehnung vor allen nicht existenten Pfaden, die tatsächliche B-/FULL-Dateischnittstelle, 0600-Rechte, ausschließlich JSON/kein RDS, Überschreibschutz und Freeze-/A-Referenz-Hashmutation vor einem nicht existenten B-Input. Der gefälschte öffentliche A-Trainingsreferenzbaum liegt ausschließlich im eigenen `outputs/loop`-Ordner; kein echtes `reports/phasen/01-a-entwicklung.json` wurde angelegt oder gelesen.

Zwei zusätzliche eigene negative Diagnosen bleiben unverändert erhalten. `inspect-001` nutzt erfundene latente rho−.996/Seed 2026100351 und ergibt einen zulässigen CFA-Punkt −.99261325 mit Design-SE .00275035 und CI[−.99800384;−.98722266]. Dieses Intervall **kreuzt −1 nicht**; seine Korrelationsregel passt. Andere globale Regeln sperren trotzdem ein Profil. Dieser Lauf ist kein Beleg eines kreuzenden Intervalls.

Die bereits abgeschlossene `inspect-002` verwendet denselben vorher beschriebenen Generator/Seed mit latenter rho−.9995. Tatsächlicher zulässiger CFA-Punkt −.99583599, Design-SE .00259192, zweiseitiges 95%-CI[−1.00091605;−.99075592]. Die beidseitige Korrelationsregel ergibt ausdrücklich `FALSE`; Ausgabe `NO_PUBLIC_PROFILE`. Die frühere alleinige Obergrenzenregel wäre für dieses konkrete Intervall wahr gewesen. Hier werden weder Intervallgrenzen geklippt noch Fitparameter gerettet. Die beiden Proben waren eigene erfundene Daten, kein importierter Reviewerfall. Keine weitere Grenzfallsuche oder Testausweitung wurde vorgenommen. Die Hauptlauf mit 113 Checks und beide Proben verwenden exakt dieselbe neue Modulquellfassung; die zusätzliche Probe ist separat dokumentiert und erhöht die Zahl der Hauptassertions nicht.

## Pins und Grenzen

| Gebundene Quelle | SHA256 |
| --- | --- |
| Neue `pipeline/ordinal/confirm.R` | `e49dd12622f73f1e8ec5f22f458eae958a2a5b9a23cc9114a92ad2e3406602cf` |
| Rootkorrigierte `develop.R` | `d1b725b05ba43d9a3edbe4964e05ae0d5365ef951944fe1c83284967ff800e74` |
| Rootkorrigierte `develop-config.R` | `44a74f0e59645d047f2bdc4508cc0058d0dd80ffb4a67a8963ee9e84f0f429b0` |
| Unveränderte `adapter_v2.R` | `8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b` |
| Unveränderte `support.R` | `b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22` |
| Erhaltener A-Autorenbericht | `c00ae6f4584300b4b07530f82a091445aaf193ba52a0ea2edd39ca36e4c9a8f5` |
| Erhaltener Supportbericht | `efd25d20fce881f0e96359a928c6732f22297bb2043d10e07a5d85cb4f1f8011` |

Die vier Dependency-Pins werden geprüft, bevor deren R-Code importiert wird. Das zukünftige B-Gate bindet zusätzlich `confirm.R`, Loader/Wrapper und die öffentlich eingefrorenen Artefakte. Vorherige `adapter.R`, `test-support.R`, `run_r.py`, abgeschlossene Berichte und historische Laufarchive wurden durch diesen Auftrag nicht geändert.

Es wird die vorhandene SOFTWARE-001/v1-Umgebung benutzt: R4.5.3/lavaan0.7.2/pbivnorm0.6.0/jsonlite2.0.0. Rscript SHA256 `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`, Manifest SHA256 `126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e`. Aufruf-/Quell-/Umgebungspins und Rscript/Manifest werden vor und nach jedem Lauf gebunden. HOME bleibt unverändert. Der eigene Autorlauncher beschränkt die bezeichneten zwölf Child-Schreibrechte mittels `setpriv`/Landlock auf den eigenen Outputordner und write-file auf `/dev/null`; eigene Temp-/Cache-/XDG-Pfade. Keine allgemeine Lese-, Netzwerk-, Geräte-, Supervisor- oder PC-Isolation wird behauptet. Keine globale Installation, kein Conda-Aufruf.

Primärgrundlagen sind die unveränderten, quellengebundenen Adapter-/Supportfunktionen, die korrigierten A-Funktionen und der aktuelle öffentliche Plan-B-Absatz. Der [Supportbericht](ESS-ORDINAL-SUPPORT-proposal.md) bewahrt die ursprünglichen lavaan-/semTools-Quellfundstellen und tatsächlichen Refit-/IF-/Observed-Score-Oracles. Hier wurde keine neue Literaturprüfung, Abdeckungsstudie oder fremde methodische Freigabe durchgeführt.

Alle Intervalle bleiben normale Delta-Approximationen bedingt auf den festen Modellvertrag, Kodierungen und Gewichte. WR-Ultimate-PSU, keine Kalibrierungs-/Gewichtsschätzunsicherheit, keine rekonstruierte PPS-WOR/FPC-Varianz, keine persönlichen Unsicherheitsintervalle oder Rotations-SE. Der konservative Adaptervertrag volle Moment-SPD/mindestens 87 Design-df bleibt erhalten; W=I kann ineffizienter sein. Echte B-Bestätigung, reale Full-DE-Übertragung, Normierung, Messinvarianz, Gruppenvergleiche, Rootloader/-runtime und Ergebnisveröffentlichung wurden in diesem Autorenschritt nicht ausgeführt. Das neue Modul wartet auf die vorgesehene B-Übergangsmethodenprüfung.
