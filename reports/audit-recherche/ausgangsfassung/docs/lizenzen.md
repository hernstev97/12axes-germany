# ESS-Nutzungsrechte

Recherchefassung vom 2026-10-03. Grundlage sind die aktuell abgerufenen ESS-Bedingungen und CC-Lizenztexte. Die konkrete Veröffentlichungsprüfung und unabhängige Gegenprüfung bleiben offen.

## Daten und Dokumentation

Der ESS nennt unter [Conditions of use](https://www.europeansocialsurvey.org/contact/disclaimer) getrennte Lizenzen:

> European Social Survey data is licensed under CC BY-NC-SA 4.0

> European Social Survey documentation is licensed under CC BY-SA 4.0

Diese zwei kurzen Zitate sind der Lizenzbefund B-LIZ-001. Die Bedingungen empfehlen Verweise auf das ESS-Portal statt einer eigenen Datensatz-Veröffentlichung. Sie beschreiben auch Anforderungen für extern gespeicherte und veränderte Fassungen. Ein pauschales Weitergabeverbot folgt daraus nicht.

| Geplante Nutzung                                                              | Lizenzrahmen und Bedingungen                                                                                                                                                                                                      | Stand                                                                                                                                                   |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nichtkommerzieller öffentlicher Webtest auf Basis eigener ESS-Analyse.        | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en), §§ 2–4: nichtkommerzielle Nutzung, Quellen-/Lizenzangaben, Änderungen kenntlich machen und ShareAlike für einschlägige Bearbeitungen.          | Grundrahmen dokumentiert. Nutzungsform und konkrete Artefakte vor Veröffentlichung prüfen.                                                              |
| Veröffentlichung aggregierter Ergebnisse und Modellartefakte.                 | Dieselben Datenbedingungen, soweit das Artefakt lizenziertes Material oder eine erfasste Bearbeitung enthält. Eigene Schlussfolgerungen als eigene ausweisen; keine ESS-Billigung suggerieren.                                    | Nicht automatisch jedes Rechenergebnis rechtlich als Bearbeitung klassifizieren. Provenienz, Inhalt und Lizenzvermerk je Export prüfen.                 |
| Wörtliche deutsche Fragen, Einleitungen und Skalen aus der ESS-Dokumentation. | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en), §§ 2–3: Vervielfältigung/Weitergabe mit Attribution, Lizenzlink und gegebenenfalls Änderungs-/ShareAlike-Hinweis. Diese Lizenz hat keine NC-Klausel. | Deutscher Fragebogen/Listenheft offiziell verlinkt und abgerufen. Beim ausgewählten Katalog weitere Rechtehinweise und vollständige Attribution prüfen. |

Die Tabelle wendet die veröffentlichten Bedingungen auf die beabsichtigten Nutzungen an; sie erklärt keinen fertigen Test als freigegeben. Die Datenlizenz bleibt für ein aus Daten entwickeltes Produkt relevant, auch wenn die Dokumentationslizenz keine NC-Klausel besitzt. Eine spätere kommerzielle Nutzung braucht eine neue Prüfung.

## Konsequenz für dieses Projekt

Rohdaten werden aus Git und Webapp ausgeschlossen und vom ESS-Portal bezogen. Das ist eine zusätzliche Projektregel, gestützt durch die ESS-Empfehlung zur Verlinkung. Die Formulierung „Rohdaten nicht öffentlich (Lizenz)“ aus LIFE-93 ist für diese Arbeit zu pauschal; sie wird nicht als Lizenzverbot übernommen.

Lizenzinformationen für ESS-Material gehören an das konkrete Modell-/Dokumentationsartefakt und auf die spätere Lizenzseite. Eigener Code und eigene Texte erhalten eine gesonderte Lizenzentscheidung; die ESS-Lizenzen werden nicht pauschal auf das gesamte Repository übertragen. Noch ist keine eigene Repository-Lizenz festgelegt.

Die endgültige Datenzitation stammt aus der tatsächlich verwendeten Portal-Ausgabe samt DOI. Der allgemeine Disclaimer nennt derzeit noch Ausgabe 4.1 als Zitationsbeispiel, während das Portal 4.2 führt. Das Beispiel darf die verwendete Ausgabe nicht ersetzen. URLs, Abrufstände und Dokument-Hashes stehen in [quellen.json](quellen.json).

Steven hat einen ESS-Account gemeldet. Die konkreten Downloadbedingungen werden beim späteren Bezug dokumentiert. Es wurden weder Zugangsdaten genutzt noch Bedingungen stellvertretend akzeptiert.
