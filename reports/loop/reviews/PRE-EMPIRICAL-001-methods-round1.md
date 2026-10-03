# PRE-EMPIRICAL-001: Methoden-Korrekturrunde 1

Datum: 2026-10-03. Prüfer: derselbe Codex-Subagent `pre_empirical_methods`. **Urteil: ACCEPTED_BOUNDED für die Methoden-/Reproduktionsrolle vor A. PE-M01 ist behoben.** Das Urteil übernimmt die übrigen begrenzten Befunde des unveränderten Erstberichts und ergänzt ausschließlich die gezielte Korrekturprüfung sowie die unten getrennt bewertete Sensitivitätsdefinition. Kein neues Gesamtaudit, kein B-, Gruppen-, empirischer, Produkt-, Release- oder Claude-Pass.

## Fassung und Scope

Expliziter Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch `research/life-93-night-20261003`, live HEAD `a199581c1749a692d4610795ea98ee4850c44724`. Die Korrekturen lagen bei der Prüfung als Arbeitsbaumfassung auf diesem Commit vor. Maßgeblich ist `reports/loop/packages/PRE-EMPIRICAL-001/v2/manifest.json`, SHA256 `1cc1df1f65e5e4d84bee70155cd2c0ba59a5a87317ec15061101252e610bee1e`. Alle neun dort gebundenen Artefaktpins stimmten vor/nach der Prüfung. Die fremde Quellen-Errata wurde ausschließlich gehasht; ihr Inhalt und andere aktuelle Reviewerurteile wurden nicht gelesen.

Der Erstbericht blieb bytegleich, SHA256 `a6c7eb2d6fc14a6fabc85b7fc3e4def27faf66588cb4313e752784e30a416226`. Die vier Änderungen wurden gegen den konkreten Basiscommit gelesen. Betroffene Pins:

| Datei | SHA256 |
| --- | --- |
| `docs/empirie-plan-v1.entwurf.md` | `8c0eb638dc58612922ea50e2b50018ed9e8a14109822a0b3da682f8be1840a28` |
| `data/analysevertrag.v1.entwurf.json` | `c21cea472e9832f254b7e03a5625ae375b935c8f004d6d8ce8251c3b549d18a1` |
| `pipeline/ordinal/develop.R` | `d1b725b05ba43d9a3edbe4964e05ae0d5365ef951944fe1c83284967ff800e74` |
| `pipeline/ordinal/develop-config.R` | `44a74f0e59645d047f2bdc4508cc0058d0dd80ffb4a67a8963ee9e84f0f429b0` |
| `docs/sensitivitaeten-v1.entwurf.md` | `e2a279f5a94deebe56c3066eff34cb974566a9a6b8f6e54befe85433fa101c76` |

Der zusätzliche technische Vergleich gegen sämtliche alten 38 Pins ergab neben den vier vorgesehenen Korrekturen einen neuen Hash für `data/group-source-contract.v1.entwurf.json`: `14ecbf9c77e4b9eccd3dceb837bd6dbd0da49509858015bfdebf76432f9b385a`. Der erste Zusatzvergleich endete deshalb mit Assertion/Exit 1; keine R-Prüfung scheiterte. Der Koordinator bezeichnete dies anschließend als parallele Fundstellen-/Editionsmetadatenkorrektur außerhalb dieser Nachprüfung. Der neue Inhalt wurde nicht gelesen oder methodisch angenommen. Diese Nachprüfung erteilt keinen neuen Gruppenvertrags- oder Quellenpass. Nachweis in `outputs/loop/pre-empirical-methods-round1/baseline-preservation.json` und `review-environment.json`.

Keine ESS-Roh-/Privatdatei, reale Antwort, Zuteilung oder gesperrte Vergleichsvariable wurde gesucht oder gelesen. Keine Tags, Forschungsdateien, Gitstände oder Softwareinstallationen wurden verändert. Eigene Schreiborte blieben Bericht und erlaubter synthetischer Ausgabeordner. Gleiche Codex-Modellfamilie und mögliche gemeinsame Fehler bleiben ausdrücklich eine Grenze.

## PE-M01: gezielt geschlossen

Plan Zeile 60, Maschinenvertrag unter `criteria`, Konfiguration Zeilen 19–21 und Produktionscode `develop.R:198–208` verlangen jetzt übereinstimmend `lower > -1 && upper < 1`. Die vollständige Kandidaten-Faktorpaare-Familie, Alpha 0.05 und `qnorm(1-.05/(2*m))` bleiben unverändert. Keine Faktorzahl, Items, Polung, Gewichtung oder günstigere Intervallkonvention wurde in der Korrektur ausgetauscht.

Die eigene Ausführung erfolgte mit:

```text
PYTHONDONTWRITEBYTECODE=1 python3 outputs/loop/pre-empirical-methods-round1/run-targeted.py
```

Der Treiber `targeted.R` nutzt den vorhandenen gepinnten Runtime und Landlock-Schreibrechte nur im eigenen Ordner sowie `/dev/null`; HOME blieb unverändert. Runtimepins stimmen vor/nach überein. Vollständiger Kindbefehl, Treiberhash, Codepins und Exit 0 stehen in `targeted-command.json`; Originalergebnisse in `targeted-result.json`.

Alle acht gezielten Assertions bestanden:

- Derselbe admissible negative CFA-Grenzfall mit Seed `2026100371` konvergiert, besteht `post.check` und hat weiterhin einen positiven kleinsten latenten Eigenwert `0.0036818273`. Die Korrelation `−0.99631817`, SE `0.01049236` und das Intervall `[−1.01688282, −0.97575353]` sind unverändert. Die tatsächliche korrigierte Produktionsfunktion `ed_model_evaluation` gibt nun für das Paar und die vollständige Paarregel `FALSE` aus. Die EFA war in dieser isolierten Grenzprobe ausdrücklich nicht beurteilt und wurde als nicht eligible übergeben.
- Zwei frische vollständige Entwicklungsrechnungen mit erfundenen gewöhnlichen positiven Faktoren wählen tatsächlich M2 mit H/ZF beziehungsweise M3 mit H/Z/F. Ihre EFA-, Score- und übrigen Modellanforderungen laufen mit. Alle vorgesehenen Paare bestehen beide Intervallgrenzen. M2 behält Familie 1, M3 Familie 3 und jeweils das ursprüngliche Quantil.
- Beide normalen Rechnungen behalten die konkrete Neuner-Complete-Case-Domäne, 87 Momente, alle 192 ursprünglichen PSUs und vier Null-Domänen-PSUs.
- Die unten beschriebene Item-z-Algebra stimmt in einer eigenen numerischen Gegenprobe bis unter `1e-15`.

Der gebundene frische Root-Receipt bestätigt zusätzlich Exit 0 und stabile Runtimepins. Mein Urteil stützt sich für PE-M01 auf die eigene Ausführung. Die übrige erste Methodenprüfung wurde weder wiederholt noch abgeschwächt. **Kein offenes Finding aus PE-M01 verbleibt.** Die erforderlichen anderen Rollenurteile, echten Gate-/Tagbindungen und privaten Importbedingungen bleiben Voraussetzungen der tatsächlichen A-Ausführung.

## Sensitivitätsdefinition: getrennte begrenzte Annahme

`docs/sensitivitaeten-v1.entwurf.md:5–19` ist als vorabhängiger Zielvertrag für die spätere Full-DE-Sensitivitätsrechnung hinreichend bestimmt und vertretbar. Das ist eine Annahme der Definition, kein Software- oder empirischer Stabilitätspass.

Ungewichtete Referenz und `pspwght` verändern die Referenzgewichte, während die persönliche Hauptscoreformel gleich bleibt. Die auf theoretische Endpunkte abgebildete Item-z-Variante ergibt tatsächlich `sum(x_j/sd_j)/sum(1/sd_j)`; die gewichteten Mittelwerte kürzen sich. Null-/undefinierte Streuung sperrt diese Variante. Somit werden keine unbeschränkten z-Werte mit dem 0–1-Budget verglichen.

Die latente Variante ist ausdrücklich die Originalscorekurve **am posterioren Faktormittelwert**, mit nur den jeweiligen festen Skalenitems und dem marginalen Faktor des gemeinsamen Modells. Sie ist damit eine benannte modellabhängige Diagnose. Sie wird nicht als posteriorer Erwartungswert des beobachteten Scores, persönliches Fehlerintervall oder neuer Hauptscore ausgegeben. Die gemeinsame Neuner-Referenz bleibt bestehen. Der festgelegte Golub-Welsch-Pfad mit 81/161/321 Knoten, Lograumrechnung, 161/321-Kurventoleranz `1e-6` und offenem Befund bei Numerikfehlern verhindert einen frei nach Ergebnissen gewählten Rechenweg. Die verlangte unabhängige Integrationsgegenprüfung und konkrete Parameter-/Ausführungspins müssen vor ihrer echten Anwendung vorliegen. Hier wurde diese spätere Quadratursoftware nicht implementiert oder angenommen.

Leave-one-out benennt alle festen Auslassungen; Rotation kontrolliert Struktur statt eine erfundene alternative Rohscoreformel zu liefern. Missing-Worst-Case behält die im Hauptplan benannte Verteilungsgrenze. Varianten 1–5 erhalten jeweils ihre eigene Midrankreferenz auf denselben Fällen; die betroffene Masse wird anhand der ursprünglichen gewichteten vollständigen Referenz bestimmt. Fehlende Ausführbarkeit zählt nicht als Stabilität. Die Budgets bleiben deklarierte Projektentscheidungen. **Keine zusätzliche fachliche Präzisierung oder neuer A-Blocker ergab sich aus dieser begrenzten Zielvertragsprüfung.** Die späteren tatsächlichen Variantenwerte, ihre Softwareprüfung und sämtliche empirischen Aussagen bleiben offen.
