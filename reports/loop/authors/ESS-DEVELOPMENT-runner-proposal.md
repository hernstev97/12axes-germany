# Ausführbarer A-Entwicklungsrunner vor Empirie

Autorenfassung vom 3. Oktober 2026. Die neue Rechenschicht ist lokal ausführbar und synthetisch geprüft; Planfreeze, neue methodische Übergangsurteile, Datengate und Veröffentlichung sind damit nicht erteilt. Geschrieben wurden ausschließlich `pipeline/ordinal/develop.R`, `develop-config.R`, dieser Bericht und `outputs/loop/resume-development-author/`. Keine ESS-Antwort, Datei unter `data/raw/` oder `data/local/`, echte A/B-Datei, Fallkennung oder gesperrte Vergleichsvariable wurde geöffnet oder gesucht. Keine Installation, Git-Aktion, Tags, weiteren Agents, Reviewdienste oder `pnpm check`; der Koordinator prüft die gemeinsame Fassung.

## Schnittstelle und fester Eingabevertrag

[`develop.R`](../../../pipeline/ordinal/develop.R) stellt `ed_main(project_root, input_A_csv, private_output_dir, authorization, retain_fits=TRUE)` und die darunterliegende `ed_run_file`-API bereit. Der generische Runtime-Wrapper muss vor dem Aufruf das echte öffentliche A-Gate, den vorgesehenen privaten A-Pfad und sämtliche Codepins prüfen. Der R-Aufruf verlangt vor einem Dateizugriff den Kontrollbeleg `decision="ACCEPTED_BOUNDED", arm="A", wrapper_verified=TRUE`. Dieser Beleg allein ist keine gegen absichtliche Umgehung geschützte Zugriffskontrolle. Es gibt im R-Modul keine Dateisuche, keinen B-Zugriff und keine automatische Veröffentlichung.

Einziger Frame: exakt `stratum,psu,weight,B34,B35,B36,B40,B41,B42,B43,B44,B45`. Designfelder sind endliche numerische Ganzzahlcodes ohne fehlende Werte; Gewichte sind endlich und positiv. Die neun Itemfelder enthalten bereits orientierte Kategorien 0 bis K−1 mit K=5/5/5/4/4/4/11/11/11 oder `NA`. Andere Spalten, ungültige Kategorien, andere Konfigurationen, Quellpinabweichungen und Versionsabweichungen stoppen mit festen Codes. Es erfolgt keine erneute semantische Umpolung. Für Momente, Struktur und alle A-Scores gilt dieselbe vollständige Neunitemdomäne. Die originalen ausgewählten Strata/PSUs bleiben einschließlich Null-Domänen-PSUs im Designrahmen.

[`develop-config.R`](../../../pipeline/ordinal/develop-config.R) hält die Konstanten als Autorenentwurf fest. H/Z/F und das zusammengefasste ZF behalten die engen, im [Planentwurf](../../../docs/empirie-plan-v1.entwurf.md) beschriebenen Inhalte; daraus wird kein allgemeiner politischer Score. M1 ist ausschließlich eine Neunitem-Einfaktordiagnose, M2 hat H plus ZF, M3 hat H/Z/F. Alle Fits nutzen dieselben neun Items, keine Kreuzladungen, Itemlöschungen oder Residualreparaturen.

## Tatsächlicher Rechenweg und Auswahl

Der Runner bindet die abgeschlossenen Kandidatenquellen `adapter_v2.R` und `support.R` bytegenau. Die Hauptpunkte sind ULS auf surveygewichteten ordinalen Schwellen und Polychoriken mit fester gelabelter Identitätsmetrik. Die nominellen lavaan-Argumente DWLS/WLSMV ändern diese tatsächlich importierte Metrik nicht. Für identifizierte Single-Group-CFA wird das eigene beobachtete Schätzgleichungs-Jacobian-Sandwich samt Residualkrümmung genutzt. Standardisierte Ladungs- und Faktorkorrelationsintervalle differenzieren die tatsächliche standardisierte Transformation. Residual-RMS nutzt das passende `I−DK`. Reliabilität ist `Var(E[S|alle eta])/Var(S)` auf beobachteten normierten Kategorien; Dominanz ist getrennt modellimpliziert und roh beobachtet `Cov(x_j,S)/(k Var(S))`, mit eigenem Design-SE auf dem vollen PSU-Rahmen. Die abgeschlossene [Support-Autorenfassung](ESS-ORDINAL-SUPPORT-proposal.md) mit echten Refit-, IF- und semTools-Oracles bleibt unverändert; diese Gegenrechnungen werden hier nicht als neue externe Abnahme ausgegeben.

EFA1/2/3 werden tatsächlich mit externer identischer Moment-/Gamma-/W-Bindung geschätzt. Geomin erhält 30 Starts, epsilon .001 und Seed 2026100313; die Wiederholung Seed 2026100314. Die optimale vollständige Permutation/Vorzeichenorientierung minimiert den maximalen Abstand der standardisierten Ladungen und Faktorkorrelationen. Beide müssen zusammen höchstens 1e−4 abweichen. Die erwartete Zuordnung muss in beiden Geomin-Läufen und im tatsächlichen Oblimin-Lauf für jedes Item eine positive, betragsmäßig größte Gruppenladung mit Abstand über 1e−8 ergeben. Die beiden Toleranzen sind benannte numerische Regeln, keine empirischen Gütestandards. Oblimin nutzt im gepinnten lavaan den Standard gamma=0 und ebenfalls den Aufruf mit 30 Starts. Bei nur einem Faktor beendet lavaan die triviale Rotation intern als `method="none"`; es wird dort kein informativer Mehrstart-Rotationsbefund behauptet. Rotierte EFA-SE werden nicht berichtet.

Die folgenden Grenzen sind eigene vor Empirie vorgeschlagene Projektbudgets. Sie stammen aus dem Auftrag und Planentwurf, nicht aus einem behaupteten Literaturstandard:

| Bedingung | Tatsächlich berechnete Regel |
| --- | --- |
| Globaler Korrelationsresidual-RMS | Einseitige normale 95%-Obergrenze ≤.10. Nearzero-Delta undefiniert ⇒ unentschieden, kein automatischer Erfolg. |
| Jede standardisierte Ladung des Scores | Zweiseitiges 95%-Normalintervall, Bonferroni innerhalb des festen Scores; jede Untergrenze >0. |
| Unterscheidbarkeit der Faktoren | Zweiseitiges 95%-Normalintervall, Bonferroni über **alle** Paare des vollständigen Kandidatenmodells; jede Obergrenze <1. Die Familie wird nicht nach Scoreergebnissen reduziert. |
| Beobachtete Score-Reliabilität | Zweiseitige normale 95%-Untergrenze >.50. |
| Roh-/Modell-Dominanz | Für beide Rechnungen gesondert zweiseitige 95%-Normalintervalle, Bonferroni innerhalb des Scores; jede Obergrenze ≤.50. |
| Auswahl | Erst M2, sofern Zuordnung, globales Modell, alle Faktorpaare und mindestens zwei vollständige feste Scores passen; sonst M3 mit denselben Bedingungen. M1 reicht nie für ein Profil. |

In M3 kann H aus der vorgeschlagenen Scoremenge entfallen, wenn H seine Regeln verfehlt und Z/F beide passen. H und seine drei Items bleiben im gemeinsamen Modell und in der Domäne; auch die H–Z/H–F-Korrelationen bleiben in der dreifachen Korrelationsfamilie. Es gibt keinen ungeplanten Ersatzscore. Der Rückgabestatus heißt ausdrücklich `CANDIDATE_SELECTED_FOR_FREEZE_REVIEW` oder `NO_PROFILE_CANDIDATE`, keine finale wissenschaftliche Freigabe.

Jeder EFA-Lauf und jedes CFA-Modell erhält einen eigenen Status. Warnung, Nichtkonvergenz, Inadmissibilität, unzulässige Kovarianz oder andere Bibliotheksfehler ergeben feste Codes; Parameter werden nicht gerettet oder aus einer konkurrierenden Modellfassung kopiert. Native skalierte Fitmaße bleiben separat benannte Diagnosen; sie entscheiden die Auswahl nicht. Warnungs-/Fehlermeldungen mit möglichen Eingabewerten oder Pfaden werden abgefangen. CLI-stdout enthält ausschließlich einen festen Statuscode.

## Private Artefakte und Veröffentlichungsgrenze

Der bereitgestellte Ausgabeordner muss bereits mit Modus 0700 existieren. JSON und erfolgreiche CFA-Summary-Fits werden mit 0600 geschrieben; vorhandene reservierte Ausgaben sperren den Lauf, bevor eine neue A-Datei gelesen wird. Der Runner schreibt `development-aggregate.private.json`, `development-config.private.json` und optional `cfa-M*.private.rds` in diesen Ordner. Die RDS-Fits entstehen aus externen Summaries, enthalten im geprüften Pfad keine individuellen Data-X-Matrizen und werden nicht öffentlich kopiert. Eine spätere öffentliche JSON-Kopie braucht die gesonderte Publikationsprüfung des Koordinators. Der Runner führt diese Prüfung und Kopie nicht selbst aus.

Die feste Aggregat-Whitelist enthält Konfiguration/öffentliche Codepins, Fall-/PSU-/Stratumanzahlen, Itemfehlzahlen und fehlende Gewichtsmasse, die 87 expliziten Momentlabels und Punktmatrizen, EFA-Matrizen mit Item-/Faktorachsen, standardisierte CFA-Punkte/Parameterintervalle, Modelldiagnosen, Score-Kovarianzen und Kriterienstatus. Sie enthält keine Einzelzeilen, vollständigen Masken, Gewichtsvektoren, Personen-/PSU-/Stratumkeys, individuellen Scores, Fallbeiträge, Adapterschätzerobjekte oder privaten Fallobjekte. Der synthetische Prüftreiber kontrolliert diese Struktur rekursiv und die maximale numerische Aggregatlänge.

## Ausgeführte synthetische Integration

Der finale [Prüflauf test-003](../../../outputs/loop/resume-development-author/test-003-checks.json) besteht **82/82** Assertions, exit0, UTC 10:54:09–10:54:44 am 3. Oktober 2026. Der [Aufrufbeleg](../../../outputs/loop/resume-development-author/test-003-command.json) bindet vor Ausführung Treiber, erfundene Fixture, Launcher, beide neuen Module und die unveränderten Adapter-/Supportquellen. 7680 erfundene Fälle, 192 PSUs, vier Strata; vier PSUs haben ausschließlich fehlende erfundene Items. 7520 vollständige Fälle und 188 beitragende vollständige PSUs verbleiben. Gruppenkategorien sind H=5, Z=4, F=11. Seeds 2026100324/25/26, starke Ladungen .82, schwaches H .25; ein gemeinsamer und ein PSU-Anteil erzeugen eine sinnvolle Designkovarianz. Diese Daten sind keine ESS-Imitation oder empirische Evidenz für die geplanten Konstrukte.

| Erfundenes Szenario | Tatsächliche Auswahl | RMS-Obergrenze einseitig95 | Reliabilitätsuntergrenzen zweiseitig95 | Geomin-Wiederholabstand |
| --- | --- | --- | --- | --- |
| H plus ein gemeinsames ZF | M2, H/ZF | .00900686 | H .81173666; ZF .90381888 | 9.56e−8 |
| Drei starke Trios | M3, H/Z/F | .01012498 | H .82261460; Z .81570720; F .84038597 | 2.33e−7 |
| Schwaches H, starke Z/F | M3, Z/F | .01732941 | H .13582678 **verfehlt** .50; Z .80881157; F .83677416 | 4.65e−7 |

Alle genannten Auswahlzweige erfüllen die tatsächliche Oblimin-Zuordnung. Modell-/Rohdominanzobergrenzen der ausgewählten starken Scores liegen höchstens .33927 beziehungsweise .33927 in den Drei-Faktor-Szenarien; im Sechser-ZF höchstens .18393. Die schwache H-Reliabilität scheitert tatsächlich, obwohl andere Kriterien desselben Scores passen. Der gemeinsame M3-Fit bleibt gültig und alle drei Faktorpaare werden weiterhin geprüft.

Weitere tatsächliche Assertions prüfen: Ein-/Drei-/Sechser-Familienquantile, beobachtete Reliabilitätsidentität, Rohdominanzsumme eins, Vorzeichen-/Permutationsabgleich, Ablehnung einer uneindeutigen Itemzuordnung, M2-Vorrang bei zwei geeigneten Kandidaten, Ablehnung nur einer passenden Dimension, unentschiedenen Nearzero-Auswahlstatus, feste Quellen-Whitelist gegen fremde Metadaten, Gateablehnung vor einer nicht existenten Eingabe, feste CLI-Ausgaben, tatsächliche private Dateischnittstelle, 0600-Rechte, keine Data-X-Fälle im externen Summary-RDS, unveränderte JSON nach Überschreibversuch und Ablehnung unsicherer Ausgaberechte vor dem Dateilesen.

Die echte Drei-Faktor-EFA und CFA-M3 des **Zwei-Faktor**-Szenarios melden `ORDINAL_ADAPTER_LIBRARY_WARNING`; der Oblimin-Dreifaktorlauf dort meldet `ESS_DEVELOPMENT_LIBRARY_WARNING`. Diese überdimensionierten Ausfälle bleiben im Aggregat und Log erhalten. Es wird keine Warnung in einen Konvergenzerfolg umbenannt. M2 wird mit seinem tatsächlich erfolgreichen Fit gewählt. M1 ist in allen drei Szenarien diagnostisch ausgeführt und ungeeignet; im schwachen Szenario verfehlt zusätzlich dessen Ladungsregel. Keine Kriteriengrenze wurde zum Bestehen gelockert.

Vorläufe bleiben erhalten: `inspect-001` führte die drei Szenarien erfolgreich aus. `test-001` und `test-002` bestanden 79/79 vor dem Zusatz dreier expliziter JSON-Labelchecks. Der erste Autorlauncher hatte die Fixture noch nicht in seiner vorab gehashten Quellenliste; dies ist eine begrenzte Reproduzierbarkeitslücke dieses ersten Laufbelegs. `test-002` und der maßgebliche `test-003` archivieren und binden die Fixture vollständig vor Ausführung. Die spätere kleine Sourceänderung fügt ausschließlich explizite Momentlabels hinzu; Numerik und Grenzwerte bleiben gleich. Alle historischen Quellfassungen und Laufbelege bleiben erhalten. Der unabhängige generische Wrapper hat ebenfalls einen selbst erzeugten M3-Lauf ausgeführt; seine endgültige Wiederholung und sein eigener Bericht gehören zum separaten Runtime-Auftrag.

## Pins, Primärsoftware und verbleibende Grenzen

| Finale Quelle | SHA256 |
| --- | --- |
| `pipeline/ordinal/develop.R` | `a263f93fde5d71dd169a011faf7319f10d5d578c79f87b0894756be762a9bac8` |
| `pipeline/ordinal/develop-config.R` | `0ad5794876b98b9a99cb3567e2d04112e241341d99597d7a011f9095c8a65a4a` |
| Unverändert: `adapter_v2.R` | `8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b` |
| Unverändert: `support.R` | `b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22` |
| Unverändert: `test-support.R` | `2083f0fff96f67477bb211b11aa50d1315987cb3a7b0e12bc73588adfcea96bd` |
| Unverändert: `run_r.py` | `16e757398580d61f457bbd573de452c73aee6ced72aebd5550c5a5cc33906256` |
| Unverändert: Original `adapter.R` | `d4db3819c15a8da6c4b11f515de8d939afd13de7970326900577912874726ad3` |
| Unverändert: abgeschlossener Supportbericht | `efd25d20fce881f0e96359a928c6732f22297bb2043d10e07a5d85cb4f1f8011` |

Die vorhandene SOFTWARE-001/v1-Umgebung bleibt R4.5.3/lavaan0.7.2/pbivnorm0.6.0/jsonlite2.0.0; Rscript SHA256 `152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec`, Manifest SHA256 `126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e`. Rscript, Manifest und ursprüngliche Launcher-/Umgebungspins werden vor/nach Ausführung geprüft. Der neue eigene Autorlauncher liegt nur im ignorierten Outputordner. `setpriv`/Landlock begrenzt die bezeichneten zwölf Child-Schreibrechte auf diesen Autorordner und write-file auf `/dev/null`; HOME bleibt unverändert. Temp-/Cache-/XDG-Dateien liegen im Autorordner. Das ist keine vollständige Lese-, Netzwerk-, Geräte-, Supervisor- oder PC-Isolation. Es gibt keinen Conda-Aufruf und keine globale Installation.

Zusätzlich gelesen wurde ausschließlich bereits lokal gebundener primärer lavaan0.7.2-Quellcode: `lav_options_default.R`, Z.257–287 (Geomin epsilon .001, Oblimin gamma0, rstarts30; SHA256 `aeb604ff0411c7fa4c9f49f9486c30727463ace0850e75d4e5064f1014a8e2c6`), `lav_matrix_rotate.R`, Z.38–52 (triviale Einfaktordrehung; SHA256 `99f62ab4a47818d9d6ea8633c9bf75dea07c77e99a904adea0cd8986405e8276`). Der übrige Rechenweg beruht auf den erhaltenen, quellengebundenen Modulen und der eigenen Implementierung. Keine neue externe Literatur oder methodische Gesamtprüfung wird als abgeschlossen ausgegeben.

Die Intervalle bleiben normale Delta-Approximationen bedingt auf Modell, feste Kodierung und Gewichte. Sie berücksichtigen weder Modellwahl in A, kleine-PSU-Abdeckung, Kalibrierungs-/Gewichtsschätzunsicherheit, rekonstruierte PPS-WOR/FPC-Varianzen, Rotationsinferenz noch persönliche Messunsicherheit. W=I ist möglicherweise ineffizienter als passende DWLS-Gewichte. Der konservative Adaptervertrag verlangt volle Moment-SPD und mindestens87 Design-df; dies ist eine geerbte Softwarezulassung, keine allgemeine Notwendigkeitsbehauptung. Nearzero-RMS bleibt unentschieden. Numerisch besetzte zu kleine Rechtecke und andere nicht zulässige Adapter-/Modellfälle stoppen. Echte ESS-Läufe, B-Bestätigung, Normierung, Messinvarianz und Veröffentlichung sind in diesem Auftrag nicht erfolgt.
