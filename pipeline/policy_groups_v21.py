"""Private WIP second-vote group preparation from caller-supplied CSV text.

No file/network/CLI operations, gates, public exports or cross-study joins.
The Root IO guard must bind the entire v2.1 envelope and source bytes before
any real use. This API checks its single-study inputs, not their authenticity.
Only eligible group members' weights are interpreted. Selected response codes
and duplicate DE identities are checked throughout the DE part of the text.
No hostile-Python isolation or automatic scientific approval is claimed.
"""

import csv
from dataclasses import dataclass
from enum import Enum
from io import StringIO
from math import isclose, isfinite
import re

from pipeline.policy_adapter_v2 import (
    _contract as adapter_contract, _identifier_present, _weight,
    PolicyAdapterError,
)
from pipeline.policy_analysis_v2 import (
    MissingReasonAggregate, NotAskedAggregate, PreparedWeightReference,
    _difference, _finite_sum, _validate_reference, PolicyAnalysisError,
)
from pipeline.policy_export_v2 import (
    _contract as study_contract, _json_values, ExportErrorCode, PolicyExportError,
)
from pipeline.policy_reference_v2 import Observation, categorical_reference
from pipeline.policy_report_v2 import _VARIABLES


# Correspond to the pinned envelope; they are not caller-selected thresholds.
GROUP_ENVELOPE_SHA256 = "9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702"
RESPONSE_SERIALIZATION_RULE = "canonical_nonnegative_integer_optional_zero_fraction_v1"
MIN_VALID_COUNT = 100
MIN_POSITIVE_CELL_COUNT = 5
RATIO_SCOPE = "all_eligible_group_cases"
RATIO_TOLERANCE = 1e-12
_RESPONSE = re.compile(r"(?:0|[1-9][0-9]*)(?:\.0+)?")
_CANONICAL_CODE = re.compile(r"(?:0|[1-9][0-9]*)")
_ROLES = (("pspwght", "primary"), ("dweight", "sensitivity"),
          ("unweighted", "sensitivity"), ("anweight", "equivalence_diagnostic"))
_VOTE_STATES = ("yes", "no", "not_eligible", "source_missing", "technical_export_blank")
_PARTY_STATES = ("valid_named_party", "valid_other_unlabelled", "structurally_not_asked",
                 "source_missing", "technical_export_blank")
_STUDY_KEYS = {
    "studyId", "edition", "round", "country", "opaqueInputReference",
    "metadataBeforeSelectedResponses", "columns", "fileMetadataReference",
    "nationalElection", "studyContext", "selectedQuestionIds", "questionDefinitionPolicy",
    "voteField", "nationalParty2Field", "groupsInDeclaredApiOrder", "eligibilityPredicate",
    "inconsistentPartyPredicate", "noGroupAssignmentForInconsistency",
    "otherIsHeterogeneousResidual", "recodeBoundary",
}
_FIELD_KEYS = {
    "variable", "fieldId", "fieldMetadataVersion", "fileReference", "fileAssociationProof",
    "apiLocation", "apiQuestionEn", "responseType", "fullDeclaredApiCodes", "validCodes",
    "sourceMissingCodes", "structurallyNotAskedCodes", "technicalBlank", "originalQuestion",
    "apiCodeSource", "mappingNotes",
}
_GROUP_KEYS = {
    "groupId", "party2Code", "kind", "labelEnExactApi", "labelDeOriginalForm",
    "labelDeOfficialAppendix", "appendixNameSourceId", "appendixNamePdfPage1Based",
    "formOptionStatus", "retainedBeforePartyAnswerInspection",
    "sameDisplayHeuristicAsEveryOtherGroup", "politicallyCoherentUnitClaimed",
}


class GroupErrorCode(str, Enum):
    INVALID_CONTRACT = "invalid_contract"
    INVALID_TEXT = "invalid_text"
    EMPTY_CSV = "empty_csv"
    INVALID_CSV = "invalid_csv"
    INVALID_HEADER = "invalid_header"
    INVALID_ROW_WIDTH = "invalid_row_width"
    INVALID_DE_ID = "invalid_de_id"
    DUPLICATE_DE_ID = "duplicate_de_id"
    UNKNOWN_DE_CODE = "unknown_de_code"
    INVALID_ELIGIBLE_WEIGHT = "invalid_eligible_weight"
    ARITHMETIC_FAILURE = "arithmetic_failure"


class PolicyGroupsError(ValueError):
    """Static error code; never interpolate a cell, header or identity."""

    def __init__(self, code: GroupErrorCode):
        self.code = code
        super().__init__(f"policy_groups_error: {code.value}")


class GroupPreparationStatus(str, Enum):
    NO_VALID_ANSWERS = "no_valid_answers"
    WITHHELD_BASE_OR_CELL_COUNT = "withheld_base_or_cell_count"
    PREPARED_PENDING_GROUP_RESULT_REVIEW = "prepared_pending_group_result_review"


class _PrivateRepr:
    __slots__ = ()

    def __repr__(self):
        return f"{type(self).__name__}(<private unreviewed group aggregates>)"


@dataclass(frozen=True, slots=True, repr=False)
class StateCount(_PrivateRepr):
    state: str
    count: int


@dataclass(frozen=True, slots=True, repr=False)
class ReasonCount(_PrivateRepr):
    reason: str
    count: int


@dataclass(frozen=True, slots=True, repr=False)
class GroupEligibilityDiagnostics(_PrivateRepr):
    de_case_count: int
    eligible_group_case_count: int
    vote_states: tuple[StateCount, ...]
    party_states: tuple[StateCount, ...]
    vote_source_missing_reasons: tuple[ReasonCount, ...]
    party_source_missing_reasons: tuple[ReasonCount, ...]
    # Vote and party state axes each sum to DE count; do not add the two axes.
    non_yes_vote_with_valid_party_count: int
    # Observed combination only, not a second inferred eligibility rule.
    yes_vote_with_party_not_asked_count: int


@dataclass(frozen=True, slots=True, repr=False)
class EligibleRatioDiagnostic(_PrivateRepr):
    scope: str
    case_count: int
    status: str
    ratio_min: float | None
    ratio_max: float | None
    constant_against_first_within_tolerance: bool | None
    tolerance: float


@dataclass(frozen=True, slots=True, repr=False)
class GroupQuestionSensitivity(_PrivateRepr):
    max_abs_primary_unweighted: float | None
    max_abs_primary_dweight: float | None
    max_abs_primary_anweight: float | None


@dataclass(frozen=True, slots=True, repr=False)
class PreparedGroupQuestion(_PrivateRepr):
    question_id: str
    status: GroupPreparationStatus
    estimates: tuple[PreparedWeightReference, ...]
    missing_reasons: tuple[MissingReasonAggregate, ...]
    not_asked: NotAskedAggregate
    sensitivity: GroupQuestionSensitivity


@dataclass(frozen=True, slots=True, repr=False)
class PreparedGroup(_PrivateRepr):
    group_id: str
    party2_code: str
    kind: str
    label_en_exact_api: str
    label_de_original_form: str | None
    label_de_official_appendix: str | None
    form_option_status: str
    eligible_case_count: int
    questions: tuple[PreparedGroupQuestion, ...]


@dataclass(frozen=True, slots=True, repr=False)
class PrivateGroupStudyReferences(_PrivateRepr):
    """Aggregate-only typed result; no individual IDs, rows or design keys.

    Redacted repr is a convenience, not access control. These rich aggregates
    remain private even for small cells and must not be sent to tools or UI.
    A later separately reviewed public builder is outside this API.
    """

    schema: str
    study_id: str
    edition: str
    groups: tuple[PreparedGroup, ...]
    eligibility: GroupEligibilityDiagnostics
    study_ratio_diagnostic: EligibleRatioDiagnostic


def _fail(code):
    raise PolicyGroupsError(code) from None


def _require(condition, code=GroupErrorCode.INVALID_CONTRACT):
    if not condition:
        _fail(code)


def _object(value, keys):
    _require(type(value) is dict and set(value) == keys)
    return value


def _text(value, *, nullable=False):
    if nullable and value is None:
        return None
    _require(type(value) is str and bool(value.strip()))
    # Preserve source labels, including the API's trailing whitespace.
    return value


def _codes(value):
    _require(type(value) is list and all(type(v) is str and _CANONICAL_CODE.fullmatch(v)
                                       for v in value) and len(set(value)) == len(value))
    return tuple(value)


def _field(value, *, party=False):
    keys = _FIELD_KEYS | ({"aliasToVoteTypeBinding", "codeHistoryStatus",
                          "automaticPrintedCodeToFileCodeMappingAllowed"} if party else set())
    _object(value, keys)
    _require(value["responseType"] == "nominal")
    valid = _codes(value["validCodes"])
    _require(bool(valid))
    source_missing = value["sourceMissingCodes"]
    not_asked = value["structurallyNotAskedCodes"]
    _require(type(source_missing) is list and type(not_asked) is list)
    missing, structural = {}, {}
    for item in source_missing:
        _object(item, {"code", "reasonApiExact"})
        _codes([item["code"]]); _text(item["reasonApiExact"])
        _require(item["code"] not in missing)
        missing[item["code"]] = item["reasonApiExact"]
    for item in not_asked:
        _object(item, {"code", "reasonApiExact", "isMissingApi"})
        _codes([item["code"]]); _text(item["reasonApiExact"])
        _require(item["isMissingApi"] is True and item["code"] not in structural)
        structural[item["code"]] = item["reasonApiExact"]
    _require(not(set(valid) & set(missing) or set(valid) & set(structural)
                 or set(missing) & set(structural)))
    blank = _object(value["technicalBlank"], {"code", "reason", "notAnApiCategory"})
    _require(blank["code"] == "" and blank["reason"] == "export_blank_unclassified"
             and blank["notAnApiCategory"] is True)
    declared = value["fullDeclaredApiCodes"]
    _require(type(declared) is list)
    labels, substantive = {}, []
    for item in declared:
        _object(item, {"code", "labelEnExactApi", "isMissingApi"})
        _codes([item["code"]]); _text(item["labelEnExactApi"])
        _require(type(item["isMissingApi"]) is bool and item["code"] not in labels)
        labels[item["code"]] = item["labelEnExactApi"]
        if item["isMissingApi"]:
            _require(item["code"] in missing or item["code"] in structural)
            _require(item["labelEnExactApi"] == (missing | structural)[item["code"]])
        else:
            substantive.append(item["code"])
    _require(tuple(substantive) == valid and set(labels) == set(valid) | set(missing) | set(structural))
    if party:
        _require(missing == {"77": "Refusal", "88": "Don't know", "99": "No answer"}
                 and structural == {"66": "Not applicable"}
                 and value["automaticPrintedCodeToFileCodeMappingAllowed"] is False)
    else:
        _require(valid == ("1", "2", "3") and not structural
                 and missing == {"7": "Refusal", "8": "Don't know", "9": "No answer"})
    return valid, missing, structural, labels


def _contract_inputs(study, group_study):
    # Plain acyclic JSON only; unused provenance is never copied to the result.
    _json_values(study, ExportErrorCode.INVALID_CONTRACT)
    _json_values(group_study, ExportErrorCode.INVALID_CONTRACT)
    definitions = study_contract(study)
    adapter = adapter_contract(study["adapter"])
    _object(group_study, _STUDY_KEYS)
    identity = adapter._study_id
    _require(group_study["studyId"] == identity and group_study["edition"] == adapter._edition
             and group_study["round"] == study["round"] and group_study["country"] == "DE")
    expected_ids = [f"{identity}:{v}" for v in _VARIABLES[identity]]
    _require([q["question_id"] for q in definitions] == expected_ids
             and group_study["selectedQuestionIds"] == expected_ids)
    _require(group_study["metadataBeforeSelectedResponses"] == study["metadata"])
    _require(group_study["questionDefinitionPolicy"] ==
             "exact_category_order_missing_and_notAsked_codes_in_pinned_v2_catalogue_and_analysis_adapter_by_question_id")
    _require(study["responseSerialization"]["rule"] == RESPONSE_SERIALIZATION_RULE)
    for q in adapter._questions:
        _codes(list(q._category_codes)); _codes(list(q._not_asked_codes))
        _codes([code for code, _ in q._missing_codes if code != ""])
    columns = _object(group_study["columns"], {"country", "duplicateDetectionId", "vote", "party2"})
    _require(columns["country"] == "cntry" and columns["duplicateDetectionId"] == "idno"
             and columns["vote"] == "vote")
    party_column = _text(columns["party2"])
    _require(group_study["voteField"]["variable"] == columns["vote"]
             and group_study["nationalParty2Field"]["variable"] == party_column)
    occupied = {"cntry", "idno", "pspwght", "dweight", "anweight",
                *(q._variable for q in adapter._questions)}
    _require(columns["vote"] not in occupied and party_column not in occupied | {"vote"})
    _, vote_missing, _, _ = _field(group_study["voteField"])
    valid_party, party_missing, party_structural, party_labels = _field(
        group_study["nationalParty2Field"], party=True)
    groups = group_study["groupsInDeclaredApiOrder"]
    _require(type(groups) is list and len(groups) == len(valid_party))
    other_count = 0
    for group, code in zip(groups, valid_party, strict=True):
        _object(group, _GROUP_KEYS)
        _require(group["party2Code"] == code and group["groupId"] == f"{identity}:second_vote:{code}")
        _require(group["labelEnExactApi"] == party_labels[code])
        _require(group["kind"] == ("other_unlabelled" if party_labels[code] == "Other" else "named_party"))
        other_count += group["kind"] == "other_unlabelled"
        for key in ("labelDeOriginalForm", "labelDeOfficialAppendix"):
            _text(group[key], nullable=True)
        _text(group["formOptionStatus"])
        _require(group["retainedBeforePartyAnswerInspection"] is True
                 and group["sameDisplayHeuristicAsEveryOtherGroup"] is True
                 and group["politicallyCoherentUnitClaimed"] is False)
        if group["kind"] == "other_unlabelled":
            _require(group["labelDeOriginalForm"] is None and group["labelDeOfficialAppendix"] is None)
    _require(other_count == 1)
    common = [{"field": "country", "equals": "DE"}]
    _require(group_study["eligibilityPredicate"] == {"all": common + [
        {"field": "vote", "inCodes": ["1"]}, {"field": "party2", "inCodes": list(valid_party)}]})
    _require(group_study["inconsistentPartyPredicate"] == {"all": common + [
        {"field": "vote", "notInCodes": ["1"]}, {"field": "party2", "inCodes": list(valid_party)}]})
    _require(group_study["noGroupAssignmentForInconsistency"] is True
             and group_study["otherIsHeterogeneousResidual"] is True)
    return adapter, groups, party_column, vote_missing, party_missing, party_structural


def _validated_contracts(study, group_study):
    """Pure preflight for a later Root guard, with value-free static failures.

    Validates computational fields; inert source metadata remains under the
    externally authenticated envelope pin. This is not an empirical gate.
    """
    try:
        return _contract_inputs(study, group_study)
    except PolicyGroupsError as error:
        code = error.code
    except (PolicyAdapterError, PolicyExportError, ValueError, TypeError, KeyError,
            AttributeError, ArithmeticError, RecursionError):
        code = GroupErrorCode.INVALID_CONTRACT
    # Raise outside the handler: do not retain lower-level value-bearing context.
    _fail(code)


def _response(value):
    if value == "":
        return ""
    if _RESPONSE.fullmatch(value) is None:
        _fail(GroupErrorCode.UNKNOWN_DE_CODE)
    return value.split(".", 1)[0]


def _question_answer(raw, question):
    code = _response(raw)
    if code in question._category_codes:
        return code, True, False, None
    missing = dict(question._missing_codes)
    if code in missing:
        return None, True, True, missing[code]
    if code in question._not_asked_codes:
        return None, False, False, None
    _fail(GroupErrorCode.UNKNOWN_DE_CODE)


def _status(reference):
    if not reference.accounting.valid_count:
        return GroupPreparationStatus.NO_VALID_ANSWERS
    if reference.accounting.valid_count < MIN_VALID_COUNT or any(
            0 < cat.count < MIN_POSITIVE_CELL_COUNT for cat in reference.estimates):
        return GroupPreparationStatus.WITHHELD_BASE_OR_CELL_COUNT
    return GroupPreparationStatus.PREPARED_PENDING_GROUP_RESULT_REVIEW


def _group_questions(adapter, members):
    result = []
    for index, question in enumerate(adapter._questions):
        estimates = []
        for weight, role in _ROLES:
            observations = tuple(Observation(answer[0], 1.0 if weight == "unweighted" else weights[weight],
                                             answer[1], answer[2], None)
                                 for weights, answers in members for answer in [answers[index]])
            reference = categorical_reference(study_id=adapter._study_id, question_id=question._question_id,
                                              categories=question._category_codes, observations=observations,
                                              design_basis=None)
            _validate_reference(reference, adapter._study_id, question._question_id)
            estimates.append(PreparedWeightReference(weight, role, reference))
        primary, dweight, unweighted, anweight = [value.reference for value in estimates]
        reasons = tuple(dict.fromkeys(reason for _, reason in question._missing_codes))
        missing = tuple(MissingReasonAggregate(
            reason, sum(answers[index][3] == reason for _, answers in members),
            _finite_sum(weights["pspwght"] for weights, answers in members if answers[index][3] == reason),
        ) for reason in reasons)
        result.append(PreparedGroupQuestion(
            question._question_id, _status(unweighted), tuple(estimates), missing,
            NotAskedAggregate(primary.accounting.not_asked_count, primary.accounting.not_asked_weight),
            GroupQuestionSensitivity(_difference(primary, unweighted), _difference(primary, dweight),
                                     _difference(primary, anweight)),
        ))
    return tuple(result)


def _prepare(csv_text, adapter, definitions, party_column, vote_missing, party_missing, party_structural):
    _require(type(csv_text) is str, GroupErrorCode.INVALID_TEXT)
    members = {group["party2Code"]: [] for group in definitions}
    kinds = {group["party2Code"]: group["kind"] for group in definitions}
    vote_counts = dict.fromkeys(_VOTE_STATES, 0)
    party_counts = dict.fromkeys(_PARTY_STATES, 0)
    vote_reasons = dict.fromkeys(dict.fromkeys(vote_missing.values()), 0)
    party_reasons = dict.fromkeys(dict.fromkeys(party_missing.values()), 0)
    de_count = inconsistent = yes_not_asked = 0
    seen_ids, ratios = set(), []
    required = {"cntry", "idno", "vote", party_column, "pspwght", "dweight", "anweight",
                *(q._variable for q in adapter._questions)}
    with StringIO(csv_text, newline="") as stream:
        reader = csv.reader(stream, strict=True)
        try:
            header = next(reader)
        except StopIteration:
            _fail(GroupErrorCode.EMPTY_CSV)
        _require(bool(header) and all(_identifier_present(name) for name in header)
                 and len(set(header)) == len(header) and required <= set(header), GroupErrorCode.INVALID_HEADER)
        positions = {name: i for i, name in enumerate(header)}
        for cells in reader:
            _require(len(cells) == len(header), GroupErrorCode.INVALID_ROW_WIDTH)
            if cells[positions["cntry"]] != "DE":
                continue
            identity = cells[positions["idno"]]
            _require(_identifier_present(identity), GroupErrorCode.INVALID_DE_ID)
            _require(identity not in seen_ids, GroupErrorCode.DUPLICATE_DE_ID)
            seen_ids.add(identity)
            de_count += 1
            vote = _response(cells[positions["vote"]])
            party = _response(cells[positions[party_column]])
            if vote in ("1", "2", "3"):
                vote_state = {"1": "yes", "2": "no", "3": "not_eligible"}[vote]
            elif vote in vote_missing:
                vote_state = "source_missing"
                vote_reasons[vote_missing[vote]] += 1
            elif vote == "":
                vote_state = "technical_export_blank"
            else:
                _fail(GroupErrorCode.UNKNOWN_DE_CODE)
            if party in members:
                party_state = "valid_other_unlabelled" if kinds[party] == "other_unlabelled" else "valid_named_party"
            elif party in party_structural:
                party_state = "structurally_not_asked"
            elif party in party_missing:
                party_state = "source_missing"
                party_reasons[party_missing[party]] += 1
            elif party == "":
                party_state = "technical_export_blank"
            else:
                _fail(GroupErrorCode.UNKNOWN_DE_CODE)
            vote_counts[vote_state] += 1
            party_counts[party_state] += 1
            inconsistent += vote != "1" and party in members
            yes_not_asked += vote == "1" and party in party_structural
            answers = tuple(_question_answer(cells[positions[q._variable]], q) for q in adapter._questions)
            if vote != "1" or party not in members:
                continue
            try:
                weights = {name: _weight(cells[positions[name]]) for name in ("pspwght", "dweight", "anweight")}
            except PolicyAdapterError:
                _fail(GroupErrorCode.INVALID_ELIGIBLE_WEIGHT)
            ratio = weights["anweight"] / weights["pspwght"]
            _require(isfinite(ratio) and ratio > 0, GroupErrorCode.ARITHMETIC_FAILURE)
            ratios.append(ratio)
            # Identity is used only above; never store it with computational rows.
            members[party].append((weights, answers))
    if ratios:
        constant = all(isclose(ratio, ratios[0], rel_tol=RATIO_TOLERANCE, abs_tol=RATIO_TOLERANCE)
                       for ratio in ratios)
        diagnostic = EligibleRatioDiagnostic(RATIO_SCOPE, len(ratios),
                                             "constant_within_tolerance" if constant else "nonconstant_ratio",
                                             min(ratios), max(ratios), constant, RATIO_TOLERANCE)
    else:
        diagnostic = EligibleRatioDiagnostic(RATIO_SCOPE, 0, "not_evaluable_no_eligible_group_cases",
                                             None, None, None, RATIO_TOLERANCE)
    groups = tuple(PreparedGroup(
        group["groupId"], group["party2Code"], group["kind"], group["labelEnExactApi"],
        group["labelDeOriginalForm"], group["labelDeOfficialAppendix"], group["formOptionStatus"],
        len(members[group["party2Code"]]), _group_questions(adapter, members[group["party2Code"]]),
    ) for group in definitions)
    eligibility = GroupEligibilityDiagnostics(
        de_count, len(ratios), tuple(StateCount(state, count) for state, count in vote_counts.items()),
        tuple(StateCount(state, count) for state, count in party_counts.items()),
        tuple(ReasonCount(reason, count) for reason, count in vote_reasons.items()),
        tuple(ReasonCount(reason, count) for reason, count in party_reasons.items()), inconsistent, yes_not_asked,
    )
    return PrivateGroupStudyReferences("policy-group-reference-v21-wip", adapter._study_id,
                                       adapter._edition, groups, eligibility, diagnostic)


def prepare_group_references(csv_text, study_contract, group_study_contract) -> PrivateGroupStudyReferences:
    """Prepare exactly one study's full predeclared group/question inventory.

    Contracts are respectively ``studies[n]`` from the v2 and v2.1 envelopes.
    The whole-envelope rules are fixed constants here; Root authenticates the
    complete pinned envelope externally. Header/row shape and all DE selected
    codes are strict. Weights outside eligible groups are not interpreted.
    Empty groups, including a valid CSV header with no DE cases, are retained.
    The once-only ratio diagnosis covers all eligible group members in this
    study, including members missing any/all policy responses. All question
    estimates remain private; pending status never promotes to reviewed/public.
    No design columns are interpreted and every SE/variance remains None.
    """
    args = _validated_contracts(study_contract, group_study_contract)
    try:
        return _prepare(csv_text, *args)
    except PolicyGroupsError as error:
        code = error.code
    except csv.Error:
        code = GroupErrorCode.INVALID_CSV
    except (PolicyAnalysisError, ValueError, TypeError, KeyError, AttributeError, ArithmeticError):
        code = GroupErrorCode.ARITHMETIC_FAILURE
    _fail(code)
