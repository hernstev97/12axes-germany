"""Pure WIP public allowlist for historical, separate second-vote references.

No I/O, CLI, gate access or publication. Root must authenticate actual complete
contract bytes, candidate/manifest/report bytes and both explicit pair approvals
outside this API. Formal decision strings are protocol guards, not scientific
evidence or protection against a hostile Python caller. Thresholds are project
display heuristics, not validated precision or anonymity guarantees.
"""

from enum import Enum
import json
from math import fsum, isfinite
import re

from pipeline.policy_analysis_v2 import PolicyAnalysisError, _validate_reference
from pipeline.policy_export_v2 import (
    ExportErrorCode as V2ErrorCode, PolicyExportError, _canonical_hash, _json_values,
    _contract as v2_study_contract,
)
from pipeline.policy_groups_v21 import _validated_contracts
from pipeline.policy_reference_v2 import Accounting, CategoricalReference, CategoryEstimate, VarianceStatus


TOLERANCE = 1e-12
STUDY_CONTRACT_BYTES_SHA256 = "8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b"
GROUP_CONTRACT_BYTES_SHA256 = "9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702"
_STUDY_OBJECT_SHA256 = "aae9eaf00a9195334251e6788eeb60f1bdbc4e6737004be8eb9089e5999c3af4"
_GROUP_OBJECT_SHA256 = "dd799a7976404931a4ce13b8a483c6b05d526e85bd5edb8c51d42f31a78a1ec0"
_PREFIXES = ("total", "eligible", "valid", "missing", "not_asked")
_ACCOUNTING_KEYS = {f"{prefix}_{kind}" for prefix in _PREFIXES for kind in ("count", "weight")}
_ROLES = (("pspwght", "primary"), ("dweight", "sensitivity"),
          ("unweighted", "sensitivity"), ("anweight", "equivalence_diagnostic"))
_PREPARED = "prepared_pending_group_result_review"
_WITHHELD = "withheld_base_or_cell_count"
_NO_VALID = "no_valid_answers"
_GROUP_KEYS = {"group_id", "party2_code", "kind", "label_en_exact_api", "label_de_original_form",
               "label_de_official_appendix", "form_option_status", "eligible_case_count", "questions"}
_QUESTION_KEYS = {"question_id", "status", "estimates", "missing_reasons", "not_asked", "sensitivity"}


class ExportErrorCode(str, Enum):
    INVALID_CONTRACT = "invalid_contract"
    INVALID_CANDIDATE = "invalid_candidate"
    INVALID_DECISION = "invalid_decision"
    HASH_MISMATCH = "hash_mismatch"


class PolicyGroupExportError(ValueError):
    """Static errors, without cell values, participant IDs or dynamic paths."""

    def __init__(self, code):
        self.code = code
        super().__init__(f"policy_group_export_error: {code.value}")


def _require(condition, code=ExportErrorCode.INVALID_CANDIDATE):
    if not condition:
        raise PolicyGroupExportError(code) from None


def _object(value, keys, code=ExportErrorCode.INVALID_CANDIDATE):
    _require(type(value) is dict and set(value) == set(keys) and all(type(k) is str for k in value), code)
    return value


def _array(value, code=ExportErrorCode.INVALID_CANDIDATE):
    _require(type(value) is list, code)
    return value


def _count(value):
    _require(type(value) is int and value >= 0)
    return value


def _number(value, *, nullable=False):
    if nullable and value is None:
        return None
    _require(type(value) in {int, float} and isfinite(value) and value >= 0)
    return value


def _close(left, right):
    # Same relative arithmetic rule as the existing pure aggregate validators.
    return abs(left - right) <= TOLERANCE * max(abs(left), abs(right))


def _hash(value, code):
    _require(type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None, code)


def _copy(value):
    return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))


def canonical_candidate_sha256(candidate) -> str:
    """Existing canonical JSON hash: sorted keys, compact, UTF-8, finite JSON.

    Numeric representations remain distinct (1 versus 1.0); array order remains
    significant. This hashes exactly the inner candidate object, not run.json.
    """
    try:
        _json_values(candidate, V2ErrorCode.INVALID_CANDIDATE)
        return _canonical_hash(candidate)
    except (PolicyExportError, ValueError, TypeError, ArithmeticError, RecursionError):
        raise PolicyGroupExportError(ExportErrorCode.INVALID_CANDIDATE) from None


def _contracts(study_contract, group_contract):
    code = ExportErrorCode.INVALID_CONTRACT
    _json_values(study_contract, V2ErrorCode.INVALID_CONTRACT)
    _json_values(group_contract, V2ErrorCode.INVALID_CONTRACT)
    # Complete object anchors reject unused/additional/mutated source fields.
    # The separately stated byte pins are NOT reconstructed from JSON objects.
    _require(_canonical_hash(study_contract) == _STUDY_OBJECT_SHA256
             and _canonical_hash(group_contract) == _GROUP_OBJECT_SHA256, code)
    studies = {study["study_id"]: study for study in study_contract["studies"]}
    grouped = {study["studyId"]: study for study in group_contract["studies"]}
    _require(len(studies) == len(grouped) == 5 and set(studies) == set(grouped), code)
    _require(sum(len(study["adapter"]["questions"]) for study in studies.values()) == 43, code)
    for identity in studies:
        v2_study_contract(studies[identity])
        _validated_contracts(studies[identity], grouped[identity])
    return studies, grouped


def _accounting(value):
    _object(value, _ACCOUNTING_KEYS)
    for prefix in _PREFIXES:
        count, weight = _count(value[prefix + "_count"]), _number(value[prefix + "_weight"])
        _require((count == 0) == (weight == 0))
    _require(value["total_count"] == value["eligible_count"] + value["not_asked_count"]
             and value["eligible_count"] == value["valid_count"] + value["missing_count"])
    _require(_close(value["total_weight"], fsum((value["eligible_weight"], value["not_asked_weight"])))
             and _close(value["eligible_weight"], fsum((value["valid_weight"], value["missing_weight"]))))
    # The existing typed validator requires float weights; keep candidate JSON
    # and its canonical numeric representation unchanged for the hash binding.
    return Accounting(**{key: float(amount) if key.endswith("_weight") else amount
                         for key, amount in value.items()})


def _reference(value, definition, study_id, total_count):
    _object(value, {"study_id", "question_id", "accounting", "estimates", "variance_status", "design"})
    _require(value["study_id"] == study_id and value["question_id"] == definition["question_id"]
             and value["design"] is None)
    accounting = _accounting(value["accounting"])
    _require(accounting.total_count == total_count)
    entries = _array(value["estimates"])
    _require(len(entries) == len(definition["categoryCodes"]))
    categories = []
    for item, code in zip(entries, definition["categoryCodes"], strict=True):
        _object(item, {"category", "count", "weight", "proportion", "variance", "standard_error"})
        _require(item["category"] == code and item["variance"] is None and item["standard_error"] is None)
        count, weight = _count(item["count"]), _number(item["weight"])
        _require((count == 0) == (weight == 0))
        if accounting.valid_count:
            proportion = _number(item["proportion"])
            _require(proportion <= 1 and _close(proportion, weight / accounting.valid_weight))
        else:
            _require(item["proportion"] is None)
            proportion = None
        categories.append(CategoryEstimate(code, count, float(weight),
                                           None if proportion is None else float(proportion), None, None))
    status = VarianceStatus.NO_VALID_RESPONSES if accounting.valid_count == 0 else VarianceStatus.NO_DESIGN_BASIS
    _require(value["variance_status"] == status.value)
    reference = CategoricalReference(study_id, definition["question_id"], accounting, tuple(categories), status, None)
    _validate_reference(reference, study_id, definition["question_id"])
    return reference


def _question(value, definition, study_id, group_count):
    _object(value, _QUESTION_KEYS)
    _require(value["question_id"] == definition["question_id"])
    estimates = _array(value["estimates"])
    _require(len(estimates) == 4)
    references = {}
    for estimate, (weight, role) in zip(estimates, _ROLES, strict=True):
        _object(estimate, {"weight", "role", "reference"})
        _require(estimate["weight"] == weight and estimate["role"] == role)
        references[weight] = _reference(estimate["reference"], definition, study_id, group_count)
    primary = references["pspwght"]
    primary_counts = tuple(getattr(primary.accounting, prefix + "_count") for prefix in _PREFIXES)
    category_counts = tuple(item.count for item in primary.estimates)
    for weight, reference in references.items():
        _require(tuple(getattr(reference.accounting, prefix + "_count") for prefix in _PREFIXES) == primary_counts
                 and tuple(item.count for item in reference.estimates) == category_counts)
        if weight == "unweighted":
            _require(all(getattr(reference.accounting, prefix + "_weight") == getattr(reference.accounting, prefix + "_count")
                         for prefix in _PREFIXES)
                     and all(item.weight == item.count for item in reference.estimates))
    status = (_NO_VALID if primary.accounting.valid_count == 0 else
              _WITHHELD if primary.accounting.valid_count < 100 or any(0 < count < 5 for count in category_counts)
              else _PREPARED)
    _require(type(value["status"]) is str and value["status"] == status)
    reasons = _array(value["missing_reasons"])
    names = list(dict.fromkeys(definition["missingCodes"].values()))
    _require(len(reasons) == len(names))
    for reason, name in zip(reasons, names, strict=True):
        _object(reason, {"reason", "count", "primary_weight_sum"})
        _require(reason["reason"] == name)
        count, amount = _count(reason["count"]), _number(reason["primary_weight_sum"])
        _require((count == 0) == (amount == 0))
    _require(sum(reason["count"] for reason in reasons) == primary.accounting.missing_count
             and _close(fsum(reason["primary_weight_sum"] for reason in reasons), primary.accounting.missing_weight))
    not_asked = _object(value["not_asked"], {"count", "primary_weight_sum"})
    _require(_count(not_asked["count"]) == primary.accounting.not_asked_count
             and _number(not_asked["primary_weight_sum"]) == primary.accounting.not_asked_weight
             and (bool(definition["structurallyNotAskedCodes"]) or not_asked["count"] == 0))
    sensitivity = _object(value["sensitivity"], {"max_abs_primary_unweighted", "max_abs_primary_dweight", "max_abs_primary_anweight"})
    for weight in ("unweighted", "dweight", "anweight"):
        supplied = sensitivity["max_abs_primary_" + weight]
        if not primary.accounting.valid_count:
            _require(supplied is None)
        else:
            expected = max(abs(a.proportion - b.proportion) for a, b in zip(primary.estimates, references[weight].estimates, strict=True))
            _require(_number(supplied) <= 1 and abs(supplied - expected) <= TOLERANCE)
    return status, references


def _eligibility(value, groups):
    _object(value, {"de_case_count", "eligible_group_case_count", "non_yes_vote_with_valid_party_count",
                    "yes_vote_with_party_not_asked_count", "vote_states", "party_states",
                    "vote_source_missing_reasons", "party_source_missing_reasons"})
    for key in ("de_case_count", "eligible_group_case_count", "non_yes_vote_with_valid_party_count", "yes_vote_with_party_not_asked_count"):
        _count(value[key])
    _require(sum(group["eligible_case_count"] for group in groups) == value["eligible_group_case_count"])
    states = {}
    for key, expected in (("vote_states", ("yes", "no", "not_eligible", "source_missing", "technical_export_blank")),
                          ("party_states", ("valid_named_party", "valid_other_unlabelled", "structurally_not_asked", "source_missing", "technical_export_blank"))):
        entries = _array(value[key]); _require(len(entries) == len(expected))
        states[key] = {}
        for entry, name in zip(entries, expected, strict=True):
            _object(entry, {"state", "count"}); _require(entry["state"] == name)
            states[key][name] = _count(entry["count"])
        _require(sum(states[key].values()) == value["de_case_count"])
    for key, state_key in (("vote_source_missing_reasons", "vote_states"), ("party_source_missing_reasons", "party_states")):
        entries = _array(value[key]); _require(len(entries) == 3)
        for entry, reason in zip(entries, ("Refusal", "Don't know", "No answer"), strict=True):
            _object(entry, {"reason", "count"}); _require(entry["reason"] == reason); _count(entry["count"])
        _require(sum(entry["count"] for entry in entries) == states[state_key]["source_missing"])
    eligible, inconsistent = value["eligible_group_case_count"], value["non_yes_vote_with_valid_party_count"]
    votes, parties = states["vote_states"], states["party_states"]
    _require(eligible <= votes["yes"] and inconsistent <= value["de_case_count"] - votes["yes"]
             and eligible + inconsistent == parties["valid_named_party"] + parties["valid_other_unlabelled"])
    _require(sum(group["eligible_case_count"] for group in groups if group["kind"] == "named_party")
             <= parties["valid_named_party"]
             and sum(group["eligible_case_count"] for group in groups if group["kind"] == "other_unlabelled")
             <= parties["valid_other_unlabelled"])
    _require(value["yes_vote_with_party_not_asked_count"] <= parties["structurally_not_asked"]
             and eligible + value["yes_vote_with_party_not_asked_count"] <= votes["yes"])


def _ratio(value, eligible_count, all_references):
    _object(value, {"scope", "case_count", "status", "ratio_min", "ratio_max",
                    "constant_against_first_within_tolerance", "tolerance"})
    _require(value["scope"] == "all_eligible_group_cases" and _count(value["case_count"]) == eligible_count
             and type(value["tolerance"]) is float and value["tolerance"] == TOLERANCE)
    if not eligible_count:
        _require(value["status"] == "not_evaluable_no_eligible_group_cases"
                 and value["ratio_min"] is None and value["ratio_max"] is None
                 and value["constant_against_first_within_tolerance"] is None)
        return
    minimum, maximum = _number(value["ratio_min"]), _number(value["ratio_max"])
    _require(0 < minimum <= maximum and type(value["constant_against_first_within_tolerance"]) is bool)
    constant = value["constant_against_first_within_tolerance"]
    _require(value["status"] == ("constant_within_tolerance" if constant else "nonconstant_ratio"))
    # The first observed ratio is not in the aggregate. Extrema can detect
    # contradictions, but cannot reconstruct or certify the per-row diagnosis.
    if constant:
        _require(maximum - minimum <= 2 * max(TOLERANCE, TOLERANCE * max(abs(minimum), abs(maximum))))
    else:
        _require(minimum < maximum)
    for references in all_references:
        primary, diagnostic = references["pspwght"], references["anweight"]
        pairs = [(getattr(diagnostic.accounting, prefix + "_weight"), getattr(primary.accounting, prefix + "_weight"))
                 for prefix in _PREFIXES]
        pairs += [(a.weight, p.weight) for a, p in zip(diagnostic.estimates, primary.estimates, strict=True)]
        for numerator, denominator in pairs:
            if denominator:
                ratio = numerator / denominator
                _require(isfinite(ratio) and (minimum <= ratio or _close(minimum, ratio))
                         and (ratio <= maximum or _close(maximum, ratio)))


def _candidate(candidate, study, group_study):
    _object(candidate, {"schema", "study_id", "edition", "groups", "eligibility", "study_ratio_diagnostic"})
    _require(candidate["schema"] == "policy-group-reference-v21-wip"
             and candidate["study_id"] == study["study_id"] and candidate["edition"] == study["edition"])
    entries = _array(candidate["groups"])
    definitions = group_study["groupsInDeclaredApiOrder"]
    _require(len(entries) == len(definitions))
    references, prepared_pairs, values = {}, set(), []
    for entry, definition in zip(entries, definitions, strict=True):
        _object(entry, _GROUP_KEYS)
        for private, source in (("group_id", "groupId"), ("party2_code", "party2Code"), ("kind", "kind"),
                                ("label_en_exact_api", "labelEnExactApi"), ("label_de_original_form", "labelDeOriginalForm"),
                                ("label_de_official_appendix", "labelDeOfficialAppendix"), ("form_option_status", "formOptionStatus")):
            _require(entry[private] == definition[source])
        group_count = _count(entry["eligible_case_count"])
        questions = _array(entry["questions"])
        _require(len(questions) == len(study["adapter"]["questions"]))
        total_weights = {weight: [] for weight, _ in _ROLES}
        for question, declared in zip(questions, study["adapter"]["questions"], strict=True):
            status, per_weight = _question(question, declared, study["study_id"], group_count)
            pair = (definition["groupId"], declared["question_id"])
            _require(pair not in references)
            references[pair] = (status, per_weight["pspwght"])
            if status == _PREPARED:
                prepared_pairs.add(pair)
            for weight, reference in per_weight.items():
                total_weights[weight].append(reference.accounting.total_weight)
            values.append(per_weight)
        _require(all(all(_close(amount, amounts[0]) for amount in amounts) for amounts in total_weights.values()))
    _eligibility(candidate["eligibility"], entries)
    _ratio(candidate["study_ratio_diagnostic"], candidate["eligibility"]["eligible_group_case_count"], values)
    return references, prepared_pairs


def _inputs(candidate, study_contract, group_contract):
    studies, grouped = _contracts(study_contract, group_contract)
    _json_values(candidate, V2ErrorCode.INVALID_CANDIDATE)
    _require(type(candidate) is dict and candidate.get("study_id") in studies)
    study = studies[candidate["study_id"]]; group_study = grouped[candidate["study_id"]]
    references, prepared_pairs = _candidate(candidate, study, group_study)
    return study, group_study, references, prepared_pairs


def validate_group_reference_candidate(candidate, study_contract, group_contract) -> None:
    """Validate one detached inner aggregate object, without promotion or IO."""
    try:
        _inputs(candidate, study_contract, group_contract)
    except PolicyGroupExportError:
        raise
    except (PolicyExportError, PolicyAnalysisError, ValueError, TypeError, KeyError,
            AttributeError, ArithmeticError, RecursionError):
        raise PolicyGroupExportError(ExportErrorCode.INVALID_CANDIDATE) from None


def _decision(value, candidate, study, prepared_pairs):
    code = ExportErrorCode.INVALID_DECISION
    _json_values(value, V2ErrorCode.INVALID_DECISION)
    _object(value, {"schemaVersion", "decision", "studyId", "edition", "candidateSha256",
                    "groupContractSha256", "studyContractSha256", "reviewManifestSha256",
                    "approvedGroupQuestionIds", "reviewers"}, code)
    _require(type(value["schemaVersion"]) is int and value["schemaVersion"] == 1
             and value["decision"] == "ALLOW_REVIEWED_HISTORICAL_GROUP_REFERENCES_V21"
             and value["studyId"] == study["study_id"] and value["edition"] == study["edition"], code)
    for key in ("candidateSha256", "groupContractSha256", "studyContractSha256", "reviewManifestSha256"):
        _hash(value[key], code)
    _require(value["candidateSha256"] == _canonical_hash(candidate)
             and value["groupContractSha256"] == GROUP_CONTRACT_BYTES_SHA256
             and value["studyContractSha256"] == STUDY_CONTRACT_BYTES_SHA256, ExportErrorCode.HASH_MISMATCH)
    approved = set()
    for pair in _array(value["approvedGroupQuestionIds"], code):
        _object(pair, {"groupId", "questionId"}, code)
        _require(type(pair["groupId"]) is str and type(pair["questionId"]) is str, code)
        key = (pair["groupId"], pair["questionId"])
        _require(key not in approved and key in prepared_pairs, code)
        approved.add(key)
    reviewers = _array(value["reviewers"], code); _require(len(reviewers) == 2, code)
    roles, paths = set(), set()
    for reviewer in reviewers:
        _object(reviewer, {"role", "reportPath", "sha256", "decision"}, code)
        role, path = reviewer["role"], reviewer["reportPath"]
        _require(type(role) is str and type(path) is str and role not in roles and path not in paths
                 and re.fullmatch(r"reports/loop/reviews/[A-Za-z0-9][A-Za-z0-9_.-]*\.md", path) is not None
                 and reviewer["decision"] == "ACCEPTED_BOUNDED", code)
        _hash(reviewer["sha256"], code)
        roles.add(role); paths.add(path)
    _require(roles == {"methods_reproducibility", "sources_constructs_fairness"}, code)
    return approved


def _source(study, group_study, group_contract):
    provenance = study["provenance"]
    party = group_study["nationalParty2Field"]
    source_ids = {"ess-disclaimer-current", party["apiCodeSource"]["sourceId"],
                  party["originalQuestion"]["questionnaireSourceId"],
                  group_study["voteField"]["originalQuestion"]["questionnaireSourceId"]}
    concordance = party["aliasToVoteTypeBinding"]["officialConcordanceSourceId"]
    if concordance is not None:
        source_ids.add(concordance)
    source_ids.update(group["appendixNameSourceId"] for group in group_study["groupsInDeclaredApiOrder"]
                      if group["appendixNameSourceId"] is not None)
    documents = [{key: source[key] for key in ("id", "publicUrl", "retrievedUtc", "originalBytesSha256",
                                               "documentMetadataId", "documentMetadataVersion", "licenseClass")}
                 for source in group_contract["sources"] if source["id"] in source_ids]
    _require({source["id"] for source in documents} == source_ids, ExportErrorCode.INVALID_CONTRACT)
    def field(original):
        return {key: original[key] for key in ("variable", "fieldId", "fieldMetadataVersion", "fileReference",
                                                "apiLocation", "apiQuestionEn", "originalQuestion", "mappingNotes")}
    return _copy({
        "country": "DE", "election": group_study["nationalElection"],
        "populationDeclaredEn": provenance["populationDeclaredEn"],
        "populationCoverageLimit": provenance["populationCoverageLimit"], "fieldwork": provenance["fieldwork"],
        "dataDoi": provenance["dataDoi"], "dataDoiUrl": provenance["dataDoiUrl"],
        "documentationDoi": provenance["documentationDoi"], "documentationDoiUrl": provenance["documentationDoiUrl"],
        "dataLicenseId": provenance["dataLicenseId"], "documentationLicenseId": provenance["documentationLicenseId"],
        "attribution": group_contract["sourceRights"]["documentation"]["attribution"],
        "catalogue": group_contract["references"]["catalogue"],
        "voteField": field(group_study["voteField"]), "nationalParty2Field": field(party),
        "aliasToVoteTypeBinding": party["aliasToVoteTypeBinding"],
        "codeHistoryStatus": party["codeHistoryStatus"],
        "automaticPrintedCodeToFileCodeMappingAllowed": False,
        "recodeBoundary": group_study["recodeBoundary"], "documents": documents,
    })


def build_reviewed_group_reference_export(candidate, study_contract, group_contract, decision) -> dict:
    """Build a detached closed public object under an externally verified Root decision.

    Null references carry no private bases, weights, ratios or proportions.
    A nonnull reference requires both a fresh explicit pair approval and 100/5.
    Complete contract objects are anchored to the current public source draft;
    byte-level verification and actual reviewer intent remain Root duties.
    """
    validate_group_reference_candidate(candidate, study_contract, group_contract)
    try:
        candidate, study_contract, group_contract = _copy(candidate), _copy(study_contract), _copy(group_contract)
        _json_values(decision, V2ErrorCode.INVALID_DECISION)
        decision = _copy(decision)
        study, group_study, references, prepared_pairs = _inputs(candidate, study_contract, group_contract)
        approved = _decision(decision, candidate, study, prepared_pairs)
        groups = []
        for definition in group_study["groupsInDeclaredApiOrder"]:
            questions = []
            for question_id in group_study["selectedQuestionIds"]:
                pair = (definition["groupId"], question_id)
                status, primary = references[pair]
                reference = None
                if pair in approved:
                    status = "reviewed_historical_reference"
                    accounting = primary.accounting
                    reference = {"weight": "pspwght", "validCount": accounting.valid_count,
                                 "totalCount": accounting.total_count, "missingCount": accounting.missing_count,
                                 "notAskedCount": accounting.not_asked_count,
                                 "categories": [{"code": item.category, "proportion": item.proportion} for item in primary.estimates],
                                 "uncertainty": None}
                elif status == _PREPARED:
                    status = "result_review_withheld"
                questions.append({"id": question_id, "status": status, "reference": reference})
            groups.append({"id": definition["groupId"], "party2Code": definition["party2Code"], "kind": definition["kind"],
                           "labelEnExactApi": definition["labelEnExactApi"],
                           "labelDeOriginalForm": definition["labelDeOriginalForm"],
                           "labelDeOfficialAppendix": definition["labelDeOfficialAppendix"],
                           "appendixNameSourceId": definition["appendixNameSourceId"],
                           "appendixNamePdfPage1Based": definition["appendixNamePdfPage1Based"],
                           "formOptionStatus": definition["formOptionStatus"],
                           "heterogeneousUnlabelledOther": definition["kind"] == "other_unlabelled", "questions": questions})
        return {"schemaVersion": 1, "status": "reviewed_historical_descriptive_group_reference",
                "studyId": study["study_id"], "edition": study["edition"],
                "groupContractSha256": decision["groupContractSha256"], "studyContractSha256": decision["studyContractSha256"],
                "candidateSha256": decision["candidateSha256"], "reviewManifestSha256": decision["reviewManifestSha256"],
                "source": _source(study, group_study, group_contract),
                "scope": {"basis": "historical_same_study_policy_responses_grouped_by_recalled_Bundestag_second_vote",
                          "timeReference": group_contract["boundaries"]["answersTimeReference"],
                          "populationReference": group_contract["boundaries"]["historicalSelfReportInEachSurvey15Plus"],
                          "partyRecallAndModeLimit": group_contract["boundaries"]["partyRecallAndModeLimit"],
                          "independentNorm": False, "currentPartyPositions": False, "partyScores": False,
                          "personsOrStudiesPooled": False, "precisionOrAnonymityValidated": False}, "groups": groups}
    except PolicyGroupExportError:
        raise
    except (PolicyExportError, PolicyAnalysisError, ValueError, TypeError, KeyError,
            AttributeError, ArithmeticError, RecursionError):
        raise PolicyGroupExportError(ExportErrorCode.INVALID_DECISION) from None
