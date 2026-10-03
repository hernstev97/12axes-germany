"""Pure public presentation of separate, bounded historical group exports.

No file access, estimator or publication. Actual public/reviewer/Root bytes are
authenticated by the fixed CLI before this in-memory formatter is called.
The omitted private cell counts cannot be rechecked from weighted proportions.
"""

from enum import Enum
from math import fsum, isfinite
import re

from pipeline.policy_export_v2 import _canonical_hash, _json_values, ExportErrorCode
from pipeline.policy_group_export_v21 import (
    _contracts, _source, GROUP_CONTRACT_BYTES_SHA256, STUDY_CONTRACT_BYTES_SHA256,
)
from pipeline.policy_report_v2 import _percentage
from pipeline.policy_thematic_report_v2 import _md, _sources_and_items, _source_refs, _https


STUDY_IDS = ("ESS5e03_6", "ESS8e02_3", "ESS9e03_3")
GROUP_COUNTS = (8, 9, 9)
PAIR_COUNTS = (21, 30, 12)
CATALOGUE_OBJECT_SHA256 = "ebbfc85c566f87c7b5530a7afa673be0f4dc7e70666cebdb9e3ee2e9375b441b"
ROOT_DECISION_BYTES_SHA256 = "544f31f83cac1e258ed13559c04373430a5ac0d792c4380421a32bb623ef42bc"
MANIFEST_FIRST_SHA256 = "dddbcda2fe8a18f46a45ee812100508d9c3ed10c5cca8c8d391be648e474b13a"
MANIFEST_ROUND1_SHA256 = "47aa3e3f3cf6043cc81bf25bf6b1228bc007f4a12c3e2866337d91161f114382"
REVIEWERS = {
    "methods_reproducibility": (
        "reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1.md",
        "324a7faad5f7c2bb4d8acb2850073a6ac2bcce9607ef3e38c4bd9e668cf3f496",
        "reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1-decision.json",
        "3c99d784d23f070a77a843bb0848f26b16e4f795f951ce60d70346edf389e53a",
        MANIFEST_ROUND1_SHA256,
    ),
    "sources_constructs_fairness": (
        "reports/loop/reviews/GROUP-RESULTS-V21-001-sources-first.md",
        "1d359b82b828ba085705d0fcb6803d5b84a46a15de9ed24e06512cccdcfed058",
        "reports/loop/reviews/GROUP-RESULTS-V21-001-sources-decision.json",
        "b13ae786173c280caf7d1c70f2eccc5015d87b3842fb256575f4f5fb2e95f960",
        MANIFEST_FIRST_SHA256,
    ),
}
_EXPORT_KEYS = {"schemaVersion", "status", "studyId", "edition", "groupContractSha256",
                "studyContractSha256", "candidateSha256", "reviewManifestSha256", "source", "scope", "groups"}
_GROUP_KEYS = {"id", "party2Code", "kind", "labelEnExactApi", "labelDeOriginalForm", "labelDeOfficialAppendix",
               "appendixNameSourceId", "appendixNamePdfPage1Based", "formOptionStatus", "heterogeneousUnlabelledOther", "questions"}
_NULL = {"no_valid_answers", "withheld_base_or_cell_count", "result_review_withheld"}
_REFERENCE_KEYS = {"weight", "validCount", "totalCount", "missingCount", "notAskedCount", "categories", "uncertainty"}


class ReportErrorCode(str, Enum):
    INVALID_INPUT = "invalid_input"
    INVALID_EXPORT = "invalid_export"
    INVALID_DECISION = "invalid_decision"
    SOURCE_BINDING = "source_binding"


class PolicyGroupReportError(ValueError):
    def __init__(self, code):
        self.code = code
        super().__init__("policy_group_report_error: " + code.value)


def _require(condition, code=ReportErrorCode.INVALID_EXPORT):
    if not condition:
        raise PolicyGroupReportError(code) from None


def _object(value, keys, code=ReportErrorCode.INVALID_EXPORT):
    _require(type(value) is dict and set(value) == set(keys), code)
    return value


def _array(value, code=ReportErrorCode.INVALID_EXPORT):
    _require(type(value) is list, code)
    return value


def _hash(value, code=ReportErrorCode.INVALID_EXPORT):
    _require(type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None, code)


def _count(value):
    _require(type(value) is int and value >= 0)
    return value


def _pairs(value):
    code = ReportErrorCode.INVALID_DECISION
    pairs = []
    for item in _array(value, code):
        _object(item, {"groupId", "questionId"}, code)
        _require(type(item["groupId"]) is str and type(item["questionId"]) is str, code)
        pairs.append((item["groupId"], item["questionId"]))
    _require(len(pairs) == len(set(pairs)), code)
    return pairs


def _scope(group_contract):
    boundaries = group_contract["boundaries"]
    return {"basis": "historical_same_study_policy_responses_grouped_by_recalled_Bundestag_second_vote",
            "timeReference": boundaries["answersTimeReference"],
            "populationReference": boundaries["historicalSelfReportInEachSurvey15Plus"],
            "partyRecallAndModeLimit": boundaries["partyRecallAndModeLimit"],
            "independentNorm": False, "currentPartyPositions": False, "partyScores": False,
            "personsOrStudiesPooled": False, "precisionOrAnonymityValidated": False}


def _decisions(root, role_decisions):
    code = ReportErrorCode.INVALID_DECISION
    _object(root, {"schemaVersion", "decidedAtUtc", "decision", "scope", "rootReadCompleteOriginalSourceFirstAndMethodsFirstAndTargetedRound1",
                   "actual64Public3PrivateBytesVerified", "sourceFirstReuse", "reviewDecisionFiles", "studyDecisions", "publicFiles", "sameModelFamilyLimit"}, code)
    _require(type(root["schemaVersion"]) is int and root["schemaVersion"] == 1
             and root["decision"] == "ALLOW_REVIEWED_HISTORICAL_GROUP_REFERENCES_V21"
             and root["rootReadCompleteOriginalSourceFirstAndMethodsFirstAndTargetedRound1"] is True
             and root["actual64Public3PrivateBytesVerified"] is True
             and type(root["decidedAtUtc"]) is str
             and re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+\+00:00", root["decidedAtUtc"]) is not None, code)
    _require(type(root["scope"]) is str and type(root["sameModelFamilyLimit"]) is str, code)
    reuse = _object(root["sourceFirstReuse"], {"sourceManifestPath", "sourceManifestSha256", "targetedMethodsManifestPath", "targetedMethodsManifestSha256",
                                            "changedPaths", "unchangedPublicPins", "unchangedPrivatePins", "meaning"}, code)
    _require(reuse["sourceManifestPath"] == "reports/loop/packages/GROUP-RESULTS-V21-001/v1/manifest.json"
             and reuse["targetedMethodsManifestPath"] == "reports/loop/packages/GROUP-RESULTS-V21-001/v2/manifest.json"
             and reuse["sourceManifestSha256"] == MANIFEST_FIRST_SHA256
             and reuse["targetedMethodsManifestSha256"] == MANIFEST_ROUND1_SHA256
             and reuse["changedPaths"] == ["pipeline/policy_group_export_v21.py", "pipeline/tests/test_policy_group_export_v21.py"]
             and type(reuse["unchangedPublicPins"]) is int and reuse["unchangedPublicPins"] == 62
             and type(reuse["unchangedPrivatePins"]) is int and reuse["unchangedPrivatePins"] == 3
             and type(reuse["meaning"]) is str, code)
    _require(root["reviewDecisionFiles"] == [{"path": info[2], "sha256": info[3]} for info in REVIEWERS.values()], code)
    _object(role_decisions, REVIEWERS, code)
    approvals = {}
    for role, info in REVIEWERS.items():
        value = _object(role_decisions[role], {"schemaVersion", "role", "reviewManifestSha256", "decision", "approvedGroupQuestionIdsByStudy", "concreteFindingIds"}, code)
        _require(type(value["schemaVersion"]) is int and value["schemaVersion"] == 1 and value["role"] == role
                 and value["decision"] == "ACCEPTED_BOUNDED" and value["reviewManifestSha256"] == info[4], code)
        _object(value["approvedGroupQuestionIdsByStudy"], STUDY_IDS, code)
        findings = _array(value["concreteFindingIds"], code)
        _require(bool(findings) and all(type(f) is str for f in findings) and len(findings) == len(set(findings)), code)
        approvals[role] = {sid: _pairs(value["approvedGroupQuestionIdsByStudy"][sid]) for sid in STUDY_IDS}
    studies, files = {}, {}
    for value in _array(root["studyDecisions"], code):
        _object(value, {"schemaVersion", "decision", "studyId", "edition", "candidateSha256", "groupContractSha256", "studyContractSha256", "reviewManifestSha256", "approvedGroupQuestionIds", "reviewers"}, code)
        sid = value["studyId"]
        _require(type(sid) is str and sid in STUDY_IDS and sid not in studies
                 and type(value["schemaVersion"]) is int and value["schemaVersion"] == 1
                 and value["decision"] == root["decision"], code)
        _require(value["reviewers"] == [{"role": role, "reportPath": info[0], "sha256": info[1], "decision": "ACCEPTED_BOUNDED"}
                                        for role, info in REVIEWERS.items()], code)
        for key in ("candidateSha256", "groupContractSha256", "studyContractSha256", "reviewManifestSha256"):
            _hash(value[key], code)
        _require(value["groupContractSha256"] == GROUP_CONTRACT_BYTES_SHA256
                 and value["studyContractSha256"] == STUDY_CONTRACT_BYTES_SHA256
                 and value["reviewManifestSha256"] == MANIFEST_ROUND1_SHA256, code)
        pairs = _pairs(value["approvedGroupQuestionIds"])
        _require(all(approvals[role][sid] == pairs for role in REVIEWERS), code)
        studies[sid] = value
    for value in _array(root["publicFiles"], code):
        _object(value, {"path", "sha256", "studyId", "approvedPairCount", "declaredGroupCount"}, code)
        sid = value["studyId"]
        _require(type(sid) is str and sid in STUDY_IDS and sid not in files
                 and value["path"] == "data/reference-groups-v21/" + sid + ".json", code)
        _hash(value["sha256"], code)
        index = STUDY_IDS.index(sid)
        _require(type(value["approvedPairCount"]) is int and value["approvedPairCount"] == PAIR_COUNTS[index]
                 and type(value["declaredGroupCount"]) is int and value["declaredGroupCount"] == GROUP_COUNTS[index], code)
        files[sid] = value
    _require(tuple(studies) == tuple(files) == STUDY_IDS, code)
    return studies


def _reference(value, question):
    _object(value, _REFERENCE_KEYS)
    _require(value["weight"] == "pspwght" and value["uncertainty"] is None)
    valid, total, missing, not_asked = (_count(value[key]) for key in ("validCount", "totalCount", "missingCount", "notAskedCount"))
    _require(valid >= 100 and valid + missing + not_asked == total
             and (bool(question["structurallyNotAskedCodes"]) or not_asked == 0))
    entries = _array(value["categories"])
    _require(len(entries) == len(question["categoryCodes"]))
    shares = []
    for entry, category in zip(entries, question["categoryCodes"], strict=True):
        _object(entry, {"code", "proportion"})
        proportion = entry["proportion"]
        _require(entry["code"] == category and type(proportion) in {int, float}
                 and isfinite(proportion) and 0 <= proportion <= 1)
        shares.append(proportion)
    _require(abs(fsum(shares) - 1) <= 1e-12)
    return total


def _validate_exports(exports, study_contract, group_contract, catalogue, root, role_decisions):
    for value in (exports, study_contract, group_contract, catalogue, root, role_decisions):
        _json_values(value, ExportErrorCode.INVALID_CONTRACT)
    studies, grouped = _contracts(study_contract, group_contract)
    _require(_canonical_hash(catalogue) == CATALOGUE_OBJECT_SHA256, ReportErrorCode.SOURCE_BINDING)
    sources, items = _sources_and_items(catalogue, list(studies.values()))
    decisions = _decisions(root, role_decisions)
    _require(len(_array(exports)) == 3)
    for value, sid, group_count, pair_count in zip(exports, STUDY_IDS, GROUP_COUNTS, PAIR_COUNTS, strict=True):
        _object(value, _EXPORT_KEYS)
        decision, study, grouping = decisions[sid], studies[sid], grouped[sid]
        _require(type(value["schemaVersion"]) is int and value["schemaVersion"] == 1
                 and value["status"] == "reviewed_historical_descriptive_group_reference"
                 and value["studyId"] == sid and value["edition"] == study["edition"] == decision["edition"])
        for key in ("candidateSha256", "groupContractSha256", "studyContractSha256", "reviewManifestSha256"):
            _require(value[key] == decision[key])
        _require(_canonical_hash(value["source"]) == _canonical_hash(_source(study, grouping, group_contract))
                 and _canonical_hash(value["scope"]) == _canonical_hash(_scope(group_contract)), ReportErrorCode.SOURCE_BINDING)
        groups = _array(value["groups"]); _require(len(groups) == group_count)
        approved = []
        for group, original in zip(groups, grouping["groupsInDeclaredApiOrder"], strict=True):
            _object(group, _GROUP_KEYS)
            fields = {"id": "groupId", "party2Code": "party2Code", "kind": "kind", "labelEnExactApi": "labelEnExactApi",
                      "labelDeOriginalForm": "labelDeOriginalForm", "labelDeOfficialAppendix": "labelDeOfficialAppendix",
                      "appendixNameSourceId": "appendixNameSourceId", "appendixNamePdfPage1Based": "appendixNamePdfPage1Based",
                      "formOptionStatus": "formOptionStatus"}
            _require(all(group[key] == original[source] for key, source in fields.items())
                     and type(group["heterogeneousUnlabelledOther"]) is bool
                     and group["heterogeneousUnlabelledOther"] == (original["kind"] == "other_unlabelled"), ReportErrorCode.SOURCE_BINDING)
            questions = _array(group["questions"])
            _require(len(questions) == len(study["adapter"]["questions"]))
            group_totals = set()
            for question, definition in zip(questions, study["adapter"]["questions"], strict=True):
                _object(question, {"id", "status", "reference"})
                _require(question["id"] == definition["question_id"] and type(question["status"]) is str)
                if question["status"] == "reviewed_historical_reference":
                    group_totals.add(_reference(question["reference"], definition))
                    approved.append((group["id"], question["id"]))
                else:
                    _require(question["status"] in _NULL and question["reference"] is None)
            _require(len(group_totals) <= 1)
        _require(approved == _pairs(decision["approvedGroupQuestionIds"]) and len(approved) == pair_count,
                 ReportErrorCode.INVALID_DECISION)
    return studies, grouped, sources, items


def _render(exports, study_contract, group_contract, catalogue, root, roles):
    studies, grouped, sources, items = _validate_exports(exports, study_contract, group_contract, catalogue, root, roles)
    lines = ["# Historische Gruppenreferenzen v2.1", "", "Stand der gebundenen Rootentscheidung: " + _md(root["decidedAtUtc"]) + ". Darstellung: WIP, noch ohne eigene Darstellungsabnahme.", "",
             "Die drei öffentlichen Ableitungen aus dem [European Social Survey (ESS)](https://www.europeansocialsurvey.org/) enthalten 63 begrenzt freigegebene Gruppen-/Fragepaare. Eine Gruppe umfasst Befragte, die nach eigener Angabe bei der jeweils genannten Bundestagswahl dieselbe Zweitstimmenkategorie gewählt haben. Alle 26 Originalgruppen einschließlich des unbenannten, heterogenen Other bleiben in API-Reihenfolge erhalten.", "",
             "Die politischen Antworten stammen aus der jeweiligen Befragungszeit, nicht vom erinnerten Wahltag. Sie beschreiben weder aktuelle Parteiprogramme noch überprüfte Wahlergebnisse, heutige Wahlberechtigte oder eine unabhängige Norm. Es werden keine Personen oder Parteicodes über Studien verbunden. Es entstehen keine Scores, Ranglisten, Parteimatches, Konfidenzintervalle oder Wahlprognosen.", "",
             "Jeder Anteil hat seinen eigenen gültigen Frage-Nenner innerhalb der betreffenden historischen Gruppe. `validCount` ist ungewichtet; die Kategorieanteile sind mit `pspwght` gewichtet. Gesamt-, Missing- und Nichtgestellt-Zahlen stammen unverändert aus der freigegebenen Einzelreferenz. Missing/Nichtgestellt gehen nicht in den gültigen Anteilsnenner ein. Sechs Nachkommastellen sind Anzeigeformat, kein Präzisionsnachweis; sichtbare gerundete Anteile werden nicht auf 100 % umgerechnet.", "",
             "Eine Gruppe erfordert `vote=1` und einen gültigen nationalen Zweitstimmen-Dateicode. Nichtwahl, Nichtberechtigung, Partei-Missing, strukturelles Nichtgestellt und technische Exportleere bleiben unzugeordnet. Eine gültige Parteikategorie zusammen mit anderer Wahlteilnahme wird nicht korrigiert oder erraten und bildet keine Gruppe. Für diese unzugeordneten Zustände werden hier keine Fallzahlen veröffentlicht.", "",
             "Die vorab festgelegten Grenzen von mindestens 100 gültigen Antworten und mindestens fünf Fällen in jeder positiven Originalkategoriezelle wurden vorgelagert geprüft. Die öffentliche Ableitung enthält keine Zellcounts, aus denen dieser Bericht die Fünferregel erneut prüfen könnte. Echte Nullkategorien bleiben erhalten. Nullreferenzen veröffentlichen keine kleinen Basen, Anteile oder Gewichtssummen. Die Grenzen sind Darstellungsheuristiken, keine validierte Präzisions- oder Anonymitätsgarantie. `uncertainty: null` bedeutet: keine Standardfehler oder Konfidenzintervalle berechnet.", "",
             "Zielpopulation sind Personen ab 15 Jahren in privaten Haushalten der jeweiligen Erhebung, nicht die Wahlbevölkerung. ESS8 erfasste München nicht; Gewichtung ergänzt keine dort nicht erhobenen Antworten. ESS5/8 haben eine schwächere zusätzliche Alias-/Zweitstimmenkonkordanz als ESS9. Gedruckte Formcodes werden nicht automatisch zu Dateicodes umgedeutet. Other wird keiner konkreten Partei zugeordnet.", "",
             "ESS10-SC und ESS11 sind für diesen Gruppenweg wegen offener Quellenbindungen ausgeschlossen. Ihre Einzelreferenzen bleiben getrennt davon. Das breite Hauptprodukt umfasst weiterhin 43 Originalfragen in acht Inhaltsrubriken. Vollständige Originalfragen, Einleitungen, Szenarien, Listen, Routing und Kategorien: [Fragenkatalog](../../data/politikprofil-v2.fragen.entwurf.json) und [vollständiger Themenbericht](02-politikprofil-v2-methoden-und-ergebnisse.md). Die folgenden Frageverzeichnisse wiederholen diese langen Kontexte nicht je Gruppe.", "",
             "Die [Rootentscheidung](../loop/policy-group-v21-export-decisions.json) bindet die tatsächlichen öffentlichen Ableitungen und ausdrückliche Paarfreigaben beider KI-Rollen. [Methoden-Nachprüfung](../loop/reviews/GROUP-RESULTS-V21-001-methods-round1.md) und [Quellen-Ersturteil](../loop/reviews/GROUP-RESULTS-V21-001-sources-first.md) gehören zur gleichen Codex-Modellfamilie; gemeinsame Fehler bleiben möglich. Die engere Methoden-Korrekturfassung erweitert das unverändert weitergenutzte Quellenurteil nicht. Menschenprüfung, Websitegestaltung, Claude-Schlusskontrolle und Releasefreigabe stehen aus. Das Projekt ist weder validiert noch wissenschaftlich geprüft und kann keine Neutralität garantieren.", "",
             "Datenquelle und Attribution: European Social Survey European Research Infrastructure (ESS ERIC); Archiv Sikt – Norwegian Agency for Shared Services in Education and Research. Die abgeleiteten Antworten unterliegen [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), die Originaldokumentation getrennt [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Nichtkommerzielle Bedingung, Namensnennung und Weitergabe unter gleichen Bedingungen bleiben erhalten. Änderungen gegenüber dem ESS: Deutschland-/Fragenauswahl, Gruppierung nach erinnerter Zweitstimme und formatierte gewichtete Originalkategorieanteile. Die Softwarelizenz ersetzt keine Datenrechte. Details: [Lizenzakte](../../docs/lizenzen.md), [öffentliche Ableitungen](../../data/reference-groups-v21/README.md), [Gruppenvertrag](../../data/gruppenvertrag.v2.1.entwurf.json).", "",
             "## Studien und Zeitbezüge", "", "| Studie / Ausgabe | Befragungszeit | Erinnerte Bundestagswahl | Originalgruppen | Freigegebene Paare |", "| --- | --- | --- | --- | --- |"]
    for value, group_count, pair_count in zip(exports, GROUP_COUNTS, PAIR_COUNTS, strict=True):
        source = value["source"]
        times = "; ".join(period["start"][:10] + " bis " + period["end"][:10] for period in source["fieldwork"])
        lines.append("| " + value["studyId"] + " / " + _md(value["edition"]) + " | " + times + " | " + str(source["election"]["year"]) + " | " + str(group_count) + " | " + str(pair_count) + " |")
    for value in exports:
        sid, source = value["studyId"], value["source"]
        lines += ["", "## " + sid + " – Ausgabe " + _md(value["edition"]), "",
                  "[Daten-DOI](" + _https(source["dataDoiUrl"]) + ") " + _md(source["dataDoi"]) + "; [Dokumentations-DOI](" + _https(source["documentationDoiUrl"]) + ") " + _md(source["documentationDoi"]) + ". Erinnerte Bundestagswahl: " + str(source["election"]["year"]) + ".", ""]
        for period in source["fieldwork"]:
            lines += ["Politische Antwortzeit: " + _md(period["start"]) + " bis " + _md(period["end"]) + "; deklarierter Modus: " + _md("; ".join(period["modesDeclaredEn"])) + ".", ""]
        party = source["nationalParty2Field"]
        lines += ["Nationaler Gruppenanker: `vote=1` und gültiger Dateicode in `" + party["variable"] + "`. Originalfrage " + _md(party["originalQuestion"]["questionId"]) + ": „" + _md(party["originalQuestion"]["wordingDe"]) + "“. Wahlteilnahmefrage: „" + _md(source["voteField"]["originalQuestion"]["wordingDe"]) + "“.", "",
                  "Parteifeld-UUID: `" + party["fieldId"] + "`, Metadatenversion " + str(party["fieldMetadataVersion"]) + "; Datei-ID: `" + party["fileReference"]["id"] + "`, Metadatenversion " + str(party["fileReference"]["metadataVersion"]) + ".", "",
                  "Konkordanzstatus: " + _md(source["aliasToVoteTypeBinding"]["status"]) + ". " + _md(source["aliasToVoteTypeBinding"]["limit"]) + " Gedruckte Codes bleiben gesondert; automatische gedruckter-Code/Dateicode-Gleichsetzung: ausgeschlossen.", "",
                  "### Fragenverzeichnis", "",
                  "Originalfrage und gültige Kategorien gelten für alle folgenden Gruppen derselben Studie. Einleitungen, Bedingungen und vollständiger Kontext stehen im verlinkten Katalog und Themenbericht.", ""]
        national_documents = {document["id"]: document for document in source["documents"]}
        for field in (source["voteField"], party):
            original = field["originalQuestion"]
            document = national_documents[original["questionnaireSourceId"]]
            pages = original["pdfPages1Based"]
            url = _https(document["publicUrl"]) + "#page=" + str(pages[0])
            lines += ["Nationaler Originalbeleg für `" + field["variable"] + "`: [" + _md(original["questionnaireSourceId"]) + "](" + url + "), physische PDF-Seite(n) " + ", ".join(map(str, pages)) + ".", ""]
        for question_id in grouped[sid]["selectedQuestionIds"]:
            item = items[question_id]
            lines += ["#### `" + question_id + "` – Original " + _md(item["originalQuestionId"]), "",
                      "„" + _md(item["wordingDe"]) + "“", "",
                      "| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |", "| --- | --- | --- |"]
            for category in item["categories"]:
                lines.append("| " + _md(category["code"]) + " | " + _md(category["labelDe"]) + " | " + _md(category["printedCodeDe"] if category["printedCodeDe"] is not None else "kein gebundener gedruckter Code") + " |")
            lines += ["", "Fundstellen: " + " ".join(_source_refs(item, sources)), ""]
        lines += ["### Gruppen in Originalreihenfolge", ""]
        for group in value["groups"]:
            label = group["labelDeOriginalForm"] or group["labelDeOfficialAppendix"] or group["labelEnExactApi"]
            lines += ["#### " + _md(label) + " – Dateicode " + _md(group["party2Code"]), "",
                      "Gruppen-ID: `" + group["id"] + "`. API-Label: „" + _md(group["labelEnExactApi"]) + "“. Deutsches Formlabel: " + (_md(group["labelDeOriginalForm"]) if group["labelDeOriginalForm"] is not None else "nicht gebunden") + ". Deutsches Appendix-Label: " + (_md(group["labelDeOfficialAppendix"]) if group["labelDeOfficialAppendix"] is not None else "nicht gebunden") + ".", ""]
            if group["heterogeneousUnlabelledOther"]:
                lines += ["Other ist die unbenannte, heterogene Originalkategorie; keine konkrete Partei und keine einheitliche politische Gruppe.", ""]
            for question in group["questions"]:
                lines += ["Frage `" + question["id"] + "`:", ""]
                reference = question["reference"]
                if reference is None:
                    labels = {"no_valid_answers": "Keine gültige Antwortverteilung veröffentlicht",
                              "withheld_base_or_cell_count": "Verteilung nach fester Basis-/Zellenregel zurückgehalten",
                              "result_review_withheld": "Keine ausdrückliche Ergebnis-Paarfreigabe"}
                    lines += [labels[question["status"]] + " (`" + question["status"] + "`); keine veröffentlichte Basis oder Anteile.", ""]
                    continue
                lines += ["Gültiger Frage-Nenner, ungewichtet: " + str(reference["validCount"]) + "; Gesamtbasis dieser Frage: " + str(reference["totalCount"]) + "; Missing: " + str(reference["missingCount"]) + "; nicht gestellt: " + str(reference["notAskedCount"]) + ". Kategorieanteile: `pspwght`; Unsicherheit: `null`.", "",
                          "| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |", "| --- | --- | --- |"]
                for category, declaration in zip(reference["categories"], items[question["id"]]["categories"], strict=True):
                    lines.append("| " + _md(category["code"]) + " | " + _md(declaration["labelDe"]) + " | " + _percentage(category["proportion"]) + " % |")
                lines.append("")
    lines += ["## Öffentliche Reproduktion", "",
              "`PYTHONDONTWRITEBYTECODE=1 python scripts/build-policy-group-report-v21.py build` erzeugt ausschließlich diesen öffentlichen Bericht. `--check` vergleicht seine Bytes; `--help` liest keine Berichtseingaben. Feste lokale Pfade und Hashes binden drei öffentliche Exporte, Verträge, Katalog, Rootentscheidung, beide tatsächlichen Bericht-/Entscheidbytes und alle importierten Bibliotheken. Es werden keine Rohdaten oder privaten Aggregate nachgeladen. Diese Reproduktion prüft öffentliche Bytes und Formatierung, nicht die ursprüngliche Rohrechnung.", ""]
    lines += ["| Fester öffentlicher Input | SHA256 der ganzen Datei |", "| --- | --- |",
              "| Rootentscheidung | `" + ROOT_DECISION_BYTES_SHA256 + "` |",
              "| Studienvertrag v2 | `" + STUDY_CONTRACT_BYTES_SHA256 + "` |",
              "| Gruppenvertrag v2.1 | `" + GROUP_CONTRACT_BYTES_SHA256 + "` |",
              "| Originalfragenkatalog | `" + group_contract["references"]["catalogue"]["sha256"] + "` |"]
    for info in root["publicFiles"]:
        lines.append("| `" + info["path"] + "` | `" + info["sha256"] + "` |")
    lines += ["", "Die weiteren festen Bericht-/Entscheid- und Bibliothekspins stehen vollständig im [Reproduktionsskript](../../scripts/build-policy-group-report-v21.py). Von Metadaten genannte Roh-/Privatpfade sind keine Lesepfade dieses Schritts.", ""]
    return "\n".join(lines).rstrip() + "\n"


def render_historical_group_report(study_exports, analysis_contract, group_contract, catalogue,
                                   root_decision, review_decisions) -> str:
    """Return deterministic Markdown; caller must authenticate actual bytes.

    Closed identities/nulls/denominators/shares are checked; no new statistic.
    Pure arguments or ACCEPTED strings do not constitute fresh reviewer intent.
    """
    try:
        return _render(study_exports, analysis_contract, group_contract, catalogue,
                       root_decision, review_decisions)
    except PolicyGroupReportError:
        raise
    except Exception:
        raise PolicyGroupReportError(ReportErrorCode.INVALID_INPUT) from None
