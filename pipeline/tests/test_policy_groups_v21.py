"""Synthetic fixed-fraction group oracles; no files or real study responses."""

from copy import deepcopy
import csv
from dataclasses import asdict, FrozenInstanceError
from fractions import Fraction
from io import StringIO
import json
import unittest
from unittest.mock import patch

from pipeline.policy_groups_v21 import (
    GroupErrorCode, GroupPreparationStatus, PolicyGroupsError, prepare_group_references, _validated_contracts,
)
from pipeline.policy_reference_v2 import VarianceStatus


# Identity fixture only. All response/category/provenance content below is synthetic.
STUDIES = {
    "ESS5e03_6": ("3.6", 5, "prtvcde2", "8", ("bplcdc", "dpcstrb", "hrshsnta", "dbctvrd", "lwstrob", "rgbrklw")),
    "ESS8e02_3": ("2.3", 8, "prtvede2", "9", ("gvslvol", "gvslvue", "gvcldcr", "bnlwinc", "eduunmp", "inctxff", "sbsrnen", "banhhap", "imsclbn", "wrkprbf")),
    "ESS9e03_3": ("3.3", 9, "prtvede2", "9", ("sofrdst", "sofrwrk", "sofrpr", "sofrprv")),
    "ESS10SCe03_2": ("3.2", 10, "prtvfde2", "7", ("fairelc", "dfprtal", "medcrgv", "rghmgpr", "votedir", "cttresa", "gptpelc", "gvctzpv", "grdfinc", "viepol", "wpestop", "scchpldm", "vteurmmb", "keydec", "imsmetn", "imdfetn", "impcntr")),
    "ESS11e04_2": ("4.2", 11, "prtvgde2", "55", ("gincdif", "euftf", "eqparep", "eqparlv", "freinsw", "fineqpy")),
}
MISSING = {"7": "Refusal", "8": "Don't know", "9": "No answer", "": "export_blank_unclassified"}


def contracts(identity="ESS9e03_3"):
    edition, round_number, party_column, other, variables = STUDIES[identity]
    metadata = {"round_column": "essround", "edition_column": "edition", "expected_round": str(round_number),
                "expected_edition": edition, "normalizationRule": "integer_round_optional_dot_zero_decimal_edition_v1"}
    questions = [{"question_id": f"{identity}:{v}", "variable": v, "categoryCodes": ["1", "2", "3"],
                  "missingCodes": dict(MISSING), "structurallyNotAskedCodes": ["6"]} for v in variables]
    study = {
        "study_id": identity, "edition": edition, "round": round_number, "country": "DE",
        "input": {"path": "SYNTHETIC_UNOPENED_PRIVATE_PATH", "sha256": "1" * 64, "bytes": 1,
                  "editionEvidence": "synthetic_no_provenance_claim"},
        "adapter": {"study_id": identity, "edition": edition, "country": "DE", "country_column": "cntry",
                    "id_column": "idno", "weight_columns": {"primary": "pspwght", "sensitivities": ["dweight", "anweight"]},
                    "questions": questions, "design_columns": None},
        "metadata": metadata,
        "responseSerialization": {"rule": "canonical_nonnegative_integer_optional_zero_fraction_v1",
                                  "emptyCellReason": "export_blank_unclassified"},
        "provenance": {
            "dataDoi": "synthetic", "dataDoiUrl": "synthetic", "documentationDoi": "synthetic",
            "documentationDoiUrl": "synthetic", "populationDeclaredEn": "synthetic",
            "populationCoverageLimit": "synthetic", "fieldwork": [{"start": "synthetic", "end": "synthetic",
                                                                       "modesDeclaredEn": ["synthetic"]}],
            "samplingProceduresDeclaredEn": ["synthetic"], "dataLicenseId": "synthetic",
            "documentationLicenseId": "synthetic", "versionNotes": [], "sourceRefs": ["synthetic"],
        },
    }
    party_codes = [str(n) for n in range(1, (10 if other == "55" else int(other)))] + [other]
    party_labels = {code: "Other" if code == other else f"synthetic-named-{code}" for code in party_codes}

    def field(variable, *, party=False):
        valid = party_codes if party else ["1", "2", "3"]
        labels = party_labels if party else {"1": "Yes", "2": "No", "3": "Not eligible to vote"}
        missing = {"77": "Refusal", "88": "Don't know", "99": "No answer"} if party else {k: v for k, v in MISSING.items() if k}
        structural = {"66": "Not applicable"} if party else {}
        result = {
            "variable": variable, "fieldId": "synthetic", "fieldMetadataVersion": 1, "fileReference": {},
            "fileAssociationProof": "synthetic", "apiLocation": None, "apiQuestionEn": "synthetic",
            "responseType": "nominal",
            "fullDeclaredApiCodes": [{"code": k, "labelEnExactApi": v, "isMissingApi": False} for k, v in labels.items()]
                                      + [{"code": k, "labelEnExactApi": v, "isMissingApi": True} for k, v in (structural | missing).items()],
            "validCodes": valid, "sourceMissingCodes": [{"code": k, "reasonApiExact": v} for k, v in missing.items()],
            "structurallyNotAskedCodes": [{"code": k, "reasonApiExact": v, "isMissingApi": True} for k, v in structural.items()],
            "technicalBlank": {"code": "", "reason": "export_blank_unclassified", "notAnApiCategory": True},
            "originalQuestion": {}, "apiCodeSource": {}, "mappingNotes": [],
        }
        if party:
            result.update(aliasToVoteTypeBinding={}, codeHistoryStatus="synthetic",
                          automaticPrintedCodeToFileCodeMappingAllowed=False)
        return result

    groups = [{"groupId": f"{identity}:second_vote:{code}", "party2Code": code,
               "kind": "other_unlabelled" if code == other else "named_party", "labelEnExactApi": party_labels[code],
               "labelDeOriginalForm": None if code == other else f"synthetic-option-{code}",
               "labelDeOfficialAppendix": None, "appendixNameSourceId": None, "appendixNamePdfPage1Based": None,
               "formOptionStatus": "synthetic", "retainedBeforePartyAnswerInspection": True,
               "sameDisplayHeuristicAsEveryOtherGroup": True, "politicallyCoherentUnitClaimed": False} for code in party_codes]
    group_study = {
        "studyId": identity, "edition": edition, "round": round_number, "country": "DE",
        "opaqueInputReference": {}, "metadataBeforeSelectedResponses": deepcopy(metadata),
        "columns": {"country": "cntry", "duplicateDetectionId": "idno", "vote": "vote", "party2": party_column},
        "fileMetadataReference": {}, "nationalElection": {}, "studyContext": {},
        "selectedQuestionIds": [q["question_id"] for q in questions],
        "questionDefinitionPolicy": "exact_category_order_missing_and_notAsked_codes_in_pinned_v2_catalogue_and_analysis_adapter_by_question_id",
        "voteField": field("vote"), "nationalParty2Field": field(party_column, party=True),
        "groupsInDeclaredApiOrder": groups,
        "eligibilityPredicate": {"all": [{"field": "country", "equals": "DE"}, {"field": "vote", "inCodes": ["1"]},
                                        {"field": "party2", "inCodes": party_codes}]},
        "inconsistentPartyPredicate": {"all": [{"field": "country", "equals": "DE"}, {"field": "vote", "notInCodes": ["1"]},
                                             {"field": "party2", "inCodes": party_codes}]},
        "noGroupAssignmentForInconsistency": True, "otherIsHeterogeneousResidual": True, "recodeBoundary": None,
    }
    return study, group_study


def row(study, index, *, vote="1", party="1", first="1", second=None,
        primary=1, dweight=1, anweight=2, country="DE"):
    answers = [first] * len(study["adapter"]["questions"])
    if second is not None:
        answers[1] = second
    return [country, f"SYNTHETIC_PRIVATE_ID_{index}", str(vote), str(party), str(primary), str(dweight), str(anweight), *answers]


def csv_text(study, group, rows, extra=False):
    stream = StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(["cntry", "idno", "vote", group["columns"]["party2"], "pspwght", "dweight", "anweight",
                     *(q["variable"] for q in study["adapter"]["questions"]), *( ["unselected"] if extra else [])])
    writer.writerows([r + (["uninterpreted-private-free-text"] if extra else []) for r in rows])
    return stream.getvalue()


def prepare(rows, study=None, group=None, *, extra=False):
    if study is None:
        study, group = contracts()
    return prepare_group_references(csv_text(study, group, rows, extra), study, group)


def weighted_100(study, *, count=100, a_count=30, party="1", scale=1):
    # A30*2+B70*1=130; dweight A30*1+B70*2=170; anweight=2*primary.
    return [row(study, i, party=party, first="1" if i < a_count else "2",
                primary=(2 if i < a_count else 1) * scale,
                dweight=(1 if i < a_count else 2) * scale,
                anweight=(4 if i < a_count else 2) * scale) for i in range(count)]


def refs(question):
    return {value.weight: value.reference for value in question.estimates}


class PolicyGroupsTests(unittest.TestCase):
    def safe_error(self, call, code):
        with self.assertRaises(PolicyGroupsError) as caught:
            call()
        self.assertEqual(str(caught.exception), f"policy_groups_error: {code.value}")
        self.assertEqual(caught.exception.args, (f"policy_groups_error: {code.value}",))
        self.assertIs(caught.exception.code, code)
        self.assertIsNone(caught.exception.__cause__)
        self.assertIsNone(caught.exception.__context__)

    def test_weighted_100_fixed_fraction_oracle_and_original_zero_category(self):
        s, g = contracts()
        result = prepare(weighted_100(s), s, g)
        question = result.groups[0].questions[0]
        self.assertIs(question.status, GroupPreparationStatus.PREPARED_PENDING_GROUP_RESULT_REVIEW)
        references = refs(question)
        for weight, expected in [("pspwght", Fraction(6, 13)), ("dweight", Fraction(3, 17)),
                                 ("unweighted", Fraction(3, 10)), ("anweight", Fraction(6, 13))]:
            reference = references[weight]
            self.assertAlmostEqual(reference.estimates[0].proportion, float(expected))
            self.assertEqual(reference.estimates[2].count, 0)
            self.assertEqual(reference.estimates[2].proportion, 0)
            self.assertIs(reference.variance_status, VarianceStatus.NO_DESIGN_BASIS)
            self.assertIsNone(reference.design)
            self.assertTrue(all(e.variance is None and e.standard_error is None for e in reference.estimates))
        self.assertEqual(references["pspwght"].accounting.valid_weight, 130)
        self.assertEqual(references["dweight"].accounting.valid_weight, 170)
        self.assertAlmostEqual(question.sensitivity.max_abs_primary_unweighted, float(Fraction(21, 130)))
        self.assertAlmostEqual(question.sensitivity.max_abs_primary_dweight, float(Fraction(63, 221)))
        self.assertEqual(question.sensitivity.max_abs_primary_anweight, 0)
        self.assertEqual(result.study_ratio_diagnostic.scope, "all_eligible_group_cases")
        self.assertEqual((result.study_ratio_diagnostic.ratio_min, result.study_ratio_diagnostic.ratio_max), (2, 2))

    def test_missing_reasons_blank_notasked_and_two_question_denominators_hand_oracle(self):
        s, g = contracts()
        rows = weighted_100(s)
        for i in range(60, 100):
            rows[i][8] = "7"  # second question; Q1 remains valid.
        for index, code, weight in [(100, "7", 3), (101, "8", 5), (102, "9", 7),
                                    (103, "", 11), (104, "6", 13)]:
            rows.append(row(s, index, first=code, second="6", primary=weight, anweight=2 * weight))
        result = prepare(rows, s, g)
        q1, q2 = result.groups[0].questions[:2]
        primary1, primary2 = refs(q1)["pspwght"], refs(q2)["pspwght"]
        self.assertEqual(primary1.accounting.valid_count, 100)
        self.assertEqual(primary1.accounting.valid_weight, 130)
        self.assertEqual(primary1.accounting.total_count, 105)
        self.assertEqual(primary1.accounting.total_weight, 169)
        self.assertEqual(primary1.accounting.missing_count, 4)
        self.assertEqual(primary1.accounting.missing_weight, 26)
        self.assertEqual([(r.reason, r.count, r.primary_weight_sum) for r in q1.missing_reasons],
                         [("Refusal", 1, 3), ("Don't know", 1, 5), ("No answer", 1, 7),
                          ("export_blank_unclassified", 1, 11)])
        self.assertEqual((q1.not_asked.count, q1.not_asked.primary_weight_sum), (1, 13))
        self.assertEqual(primary2.accounting.valid_count, 60)
        self.assertEqual(primary2.accounting.valid_weight, 90)
        self.assertAlmostEqual(primary2.estimates[0].proportion, float(Fraction(2, 3)))
        self.assertEqual(primary2.accounting.missing_count, 40)
        self.assertEqual(primary2.accounting.not_asked_count, 5)
        self.assertEqual(result.study_ratio_diagnostic.case_count, 105)

    def test_fixed_99_100_and_4_5_boundaries_named_and_other_identical(self):
        s, g = contracts()
        for party in ["1", "9"]:
            for n, a, status in [(99, 30, GroupPreparationStatus.WITHHELD_BASE_OR_CELL_COUNT),
                                 (100, 4, GroupPreparationStatus.WITHHELD_BASE_OR_CELL_COUNT),
                                 (100, 5, GroupPreparationStatus.PREPARED_PENDING_GROUP_RESULT_REVIEW)]:
                with self.subTest(party=party, n=n, a=a):
                    result = prepare(weighted_100(s, count=n, a_count=a, party=party), s, g)
                    group = next(x for x in result.groups if x.party2_code == party)
                    self.assertIs(group.questions[0].status, status)
                    self.assertIsNotNone(refs(group.questions[0])["pspwght"].estimates[0].proportion)
                    self.assertEqual(len(result.groups), 9)

    def test_zero_groups_all_missing_and_no_de_inventory_never_adapter_failure(self):
        s, g = contracts()
        for rows in [[], [row(s, 0, country="FR", vote="secret", party="secret", first="secret")],
                     [row(s, 0, vote="2", party="66", primary="not interpreted")]]:
            result = prepare(rows, s, g)
            self.assertEqual(len(result.groups), 9)
            self.assertEqual(result.eligibility.eligible_group_case_count, 0)
            self.assertEqual(result.study_ratio_diagnostic.status, "not_evaluable_no_eligible_group_cases")
            self.assertIsNone(result.study_ratio_diagnostic.ratio_min)
            for group in result.groups:
                self.assertEqual(group.eligible_case_count, 0)
                self.assertEqual(len(group.questions), 4)
                for question in group.questions:
                    self.assertIs(question.status, GroupPreparationStatus.NO_VALID_ANSWERS)
                    self.assertEqual([(e.count, e.proportion) for e in refs(question)["pspwght"].estimates],
                                     [(0, None), (0, None), (0, None)])
        result = prepare([row(s, 0, first="7"), row(s, 1, first="")], s, g)
        question = result.groups[0].questions[0]
        self.assertEqual(refs(question)["pspwght"].accounting.missing_count, 2)
        self.assertIs(question.status, GroupPreparationStatus.NO_VALID_ANSWERS)

    def test_routing_axes_missing_reasons_and_non_yes_inconsistencies_not_added_as_total(self):
        s, g = contracts()
        states = [("1", "1"), ("1", "9"), ("2", "66"), ("3", "66"), ("7", "77"),
                  ("8", "88"), ("9", "99"), ("", ""), ("2", "1"), ("7", "1"), ("1", "66"), ("1", "")]
        rows = [row(s, i, vote=v, party=p, primary=1 if i < 2 else "PRIVATE_BAD_WEIGHT")
                for i, (v, p) in enumerate(states)]
        result = prepare(rows, s, g)
        diag = result.eligibility
        self.assertEqual((diag.de_case_count, diag.eligible_group_case_count), (12, 2))
        self.assertEqual([(x.state, x.count) for x in diag.vote_states],
                         [("yes", 4), ("no", 2), ("not_eligible", 1), ("source_missing", 4), ("technical_export_blank", 1)])
        self.assertEqual([(x.state, x.count) for x in diag.party_states],
                         [("valid_named_party", 3), ("valid_other_unlabelled", 1), ("structurally_not_asked", 3),
                          ("source_missing", 3), ("technical_export_blank", 2)])
        self.assertEqual([(x.reason, x.count) for x in diag.vote_source_missing_reasons],
                         [("Refusal", 2), ("Don't know", 1), ("No answer", 1)])
        self.assertEqual(diag.non_yes_vote_with_valid_party_count, 2)
        self.assertEqual(diag.yes_vote_with_party_not_asked_count, 1)
        self.assertEqual(sum(group.eligible_case_count for group in result.groups), 2)

    def test_study_ratio_scope_includes_question_missing_and_other_group_not_excluded_de(self):
        s, g = contracts()
        rows = [row(s, 0, primary=2, dweight=1, anweight=4),
                row(s, 1, first="7", primary=3, anweight=12),
                row(s, 2, party="9", first="8", primary=5, anweight=30),
                row(s, 3, vote="2", party="66", primary="nan", anweight="inf")]
        result = prepare(rows, s, g)
        diag = result.study_ratio_diagnostic
        self.assertEqual((diag.case_count, diag.ratio_min, diag.ratio_max), (3, 2, 6))
        self.assertFalse(diag.constant_against_first_within_tolerance)
        self.assertEqual(diag.status, "nonconstant_ratio")
        self.assertEqual(refs(result.groups[0].questions[0])["pspwght"].accounting.valid_count, 1)
        self.assertEqual(result.groups[-1].eligible_case_count, 1)

    def test_small_private_fraction_anweight_difference_not_a_selection_rule(self):
        s, g = contracts()
        result = prepare([row(s, 0, primary=1, dweight=2, anweight=4),
                          row(s, 1, first="2", primary=2, dweight=1, anweight=2)], s, g)
        q = result.groups[0].questions[0]
        self.assertAlmostEqual(refs(q)["pspwght"].estimates[0].proportion, float(Fraction(1, 3)))
        self.assertAlmostEqual(refs(q)["dweight"].estimates[0].proportion, float(Fraction(2, 3)))
        self.assertAlmostEqual(q.sensitivity.max_abs_primary_anweight, float(Fraction(1, 3)))
        self.assertEqual((result.study_ratio_diagnostic.ratio_min, result.study_ratio_diagnostic.ratio_max), (1, 4))
        self.assertIs(q.status, GroupPreparationStatus.WITHHELD_BASE_OR_CELL_COUNT)

    def test_weight_scale_and_row_permutation_preserve_shares_counts_and_scope(self):
        s, g = contracts()
        original = prepare(weighted_100(s), s, g)
        transformed = prepare(list(reversed(weighted_100(s, scale=7))), s, g)
        self.assertEqual(original.eligibility, transformed.eligibility)
        self.assertEqual(original.study_ratio_diagnostic, transformed.study_ratio_diagnostic)
        a, b = original.groups[0].questions[0], transformed.groups[0].questions[0]
        self.assertEqual(a.status, b.status)
        for weight in ["pspwght", "dweight", "unweighted", "anweight"]:
            self.assertEqual([c.proportion for c in refs(a)[weight].estimates], [c.proportion for c in refs(b)[weight].estimates])
        self.assertEqual(refs(b)["pspwght"].accounting.valid_weight, 910)

    def test_all_five_separate_studies_43_ids_and_code_9_not_other_in_ess11(self):
        results = []
        for identity in STUDIES:
            s, g = contracts(identity)
            other = STUDIES[identity][3]
            results.append(prepare([row(s, "same-ID", party=other)], s, g))
        self.assertEqual(sum(len(r.groups[0].questions) for r in results), 43)
        self.assertEqual(len({q.question_id for r in results for q in r.groups[0].questions}), 43)
        self.assertEqual([len(r.groups) for r in results], [8, 9, 9, 7, 10])
        s, g = contracts("ESS11e04_2")
        result = prepare([row(s, 0, party="9"), row(s, 1, party="55")], s, g)
        self.assertEqual([(x.party2_code, x.kind, x.eligible_case_count) for x in result.groups[-2:]],
                         [("9", "named_party", 1), ("55", "other_unlabelled", 1)])
        self.safe_error(lambda: prepare([row(s, 0, party="09")], s, g), GroupErrorCode.UNKNOWN_DE_CODE)
        s, g = contracts("ESS10SCe03_2")
        self.safe_error(lambda: prepare([row(s, 0, party="9")], s, g), GroupErrorCode.UNKNOWN_DE_CODE)

    def test_strict_decimal_zero_serialization_no_trim_no_printed_code_conversion(self):
        s, g = contracts()
        r = row(s, 0, vote="1.00", party="1.0", first="2.000", primary=" 3 ")
        result = prepare([r], s, g)
        self.assertEqual(refs(result.groups[0].questions[0])["pspwght"].estimates[1].proportion, 1)
        for bad in ["01", "1e0", "1.1", " 1", "1 ", "-1", "+1", "PRIVATE_UNKNOWN_CELL"]:
            self.safe_error(lambda bad=bad: prepare([row(s, 0, party=bad)], s, g), GroupErrorCode.UNKNOWN_DE_CODE)
        self.safe_error(lambda: prepare([row(s, 0, vote="2", party="66", first="PRIVATE_UNKNOWN_CELL")], s, g),
                        GroupErrorCode.UNKNOWN_DE_CODE)

    def test_duplicate_identity_safe_error_even_for_noneligible_and_exact_quoted_ids(self):
        s, g = contracts()
        rows = [row(s, 0), row(s, 0, vote="2", party="66")]
        self.safe_error(lambda: prepare(rows, s, g), GroupErrorCode.DUPLICATE_DE_ID)
        quoted = row(s, 0)
        quoted[1] = 'PRIVATE_ID_WITH,"QUOTES"\nand newline'
        result = prepare([quoted], s, g, extra=True)
        self.assertEqual(result.eligibility.de_case_count, 1)
        duplicated = deepcopy(quoted)
        self.safe_error(lambda: prepare([quoted, duplicated], s, g), GroupErrorCode.DUPLICATE_DE_ID)
        other = deepcopy(quoted); other[1] += " "
        self.assertEqual(prepare([quoted, other], s, g).eligibility.de_case_count, 2)

    def test_non_de_contents_ignored_but_every_row_width_and_header_strict(self):
        s, g = contracts()
        foreign = row(s, 0, country="FR", vote="PRIVATE_UNKNOWN", party="PRIVATE_UNKNOWN", first="PRIVATE_UNKNOWN",
                      primary="nan", dweight="bad", anweight="inf")
        foreign[1] = ""
        result = prepare([row(s, 0), foreign], s, g)
        self.assertEqual(result.eligibility.de_case_count, 1)
        self.safe_error(lambda: prepare([foreign[:-1]], s, g), GroupErrorCode.INVALID_ROW_WIDTH)
        text = csv_text(s, g, [row(s, 0)])
        self.safe_error(lambda: prepare_group_references(text.replace("idno", "cntry", 1), s, g), GroupErrorCode.INVALID_HEADER)
        self.safe_error(lambda: prepare_group_references(text.replace("idno", "", 1), s, g), GroupErrorCode.INVALID_HEADER)
        self.safe_error(lambda: prepare_group_references(text.replace("pspwght", "wrong", 1), s, g), GroupErrorCode.INVALID_HEADER)
        self.safe_error(lambda: prepare([row(s, 0) + ["secret"]], s, g), GroupErrorCode.INVALID_ROW_WIDTH)
        self.safe_error(lambda: prepare_group_references("", s, g), GroupErrorCode.EMPTY_CSV)
        self.safe_error(lambda: prepare_group_references(3, s, g), GroupErrorCode.INVALID_TEXT)

    def test_eligible_weights_positive_finite_and_arithmetic_failure_static(self):
        s, g = contracts()
        for bad in ["nan", "inf", "-inf", "0", "-1", "bad"]:
            for field in ["primary", "dweight", "anweight"]:
                self.safe_error(lambda bad=bad, field=field: prepare([row(s, 0, **{field: bad})], s, g),
                                GroupErrorCode.INVALID_ELIGIBLE_WEIGHT)
        self.safe_error(lambda: prepare([row(s, 0, primary=1e308, anweight=1e308),
                                        row(s, 1, primary=1e308, anweight=1e308)], s, g), GroupErrorCode.ARITHMETIC_FAILURE)

    def test_invalid_contract_source_selection_or_other_relabel_safe_error(self):
        mutations = [lambda s, g: g.update(edition="wrong"),
                     lambda s, g: g["selectedQuestionIds"].reverse(),
                     lambda s, g: g["groupsInDeclaredApiOrder"].pop(),
                     lambda s, g: g["groupsInDeclaredApiOrder"][-1].update(kind="named_party"),
                     lambda s, g: g["groupsInDeclaredApiOrder"][0].update(labelEnExactApi="Other"),
                     lambda s, g: g.update(noGroupAssignmentForInconsistency=False),
                     lambda s, g: g.update(minimumValidQuestionCount=1),
                     lambda s, g: g["voteField"]["technicalBlank"].update(notAnApiCategory=1),
                     lambda s, g: g["nationalParty2Field"].update(automaticPrintedCodeToFileCodeMappingAllowed=True),
                     lambda s, g: s["adapter"]["questions"][0].update(categoryCodes=["01", "2", "3"]),
                     lambda s, g: s["responseSerialization"].update(rule="arbitrary")]
        for mutation in mutations:
            s, g = contracts(); mutation(s, g)
            self.safe_error(lambda: prepare_group_references("", s, g), GroupErrorCode.INVALID_CONTRACT)

    def test_preflight_static_on_malformed_nested_fields_and_literal_vote_unknown(self):
        s, g = contracts()
        g["nationalParty2Field"] = {}
        self.safe_error(lambda: _validated_contracts(s, g), GroupErrorCode.INVALID_CONTRACT)
        s, g = contracts()
        self.safe_error(lambda: prepare([row(s, 0, vote="PRIVATE_UNKNOWN_VOTE")], s, g), GroupErrorCode.UNKNOWN_DE_CODE)
        r = row(s, 0); r[1] = " \t "
        self.safe_error(lambda: prepare([r], s, g), GroupErrorCode.INVALID_DE_ID)
        text = csv_text(s, g, []) + 'DE,"PRIVATE_UNCLOSED_QUOTE'
        self.safe_error(lambda: prepare_group_references(text, s, g), GroupErrorCode.INVALID_CSV)

    def test_subnormal_positive_weights_keep_fixed_one_third_group_share(self):
        s, g = contracts()
        tiny = float.fromhex("0x0.0000000000001p-1022")
        result = prepare([row(s, 0, primary=tiny, dweight=tiny, anweight=tiny),
                          row(s, 1, first="2", primary=2 * tiny, dweight=2 * tiny, anweight=2 * tiny)], s, g)
        self.assertAlmostEqual(refs(result.groups[0].questions[0])["pspwght"].estimates[0].proportion,
                               float(Fraction(1, 3)))
        self.assertEqual((result.study_ratio_diagnostic.ratio_min, result.study_ratio_diagnostic.ratio_max), (1, 1))

    def test_ratio_tolerance_is_diagnostic_and_does_not_change_eligibility(self):
        s, g = contracts()
        close = prepare([row(s, 0, anweight=2), row(s, 1, anweight=2 + 1e-12)], s, g)
        distant = prepare([row(s, 0, anweight=2), row(s, 1, anweight=2 + 1e-9)], s, g)
        self.assertTrue(close.study_ratio_diagnostic.constant_against_first_within_tolerance)
        self.assertFalse(distant.study_ratio_diagnostic.constant_against_first_within_tolerance)
        self.assertEqual(close.eligibility, distant.eligibility)
        self.assertEqual(close.groups[0].questions[0].status, distant.groups[0].questions[0].status)

    def test_results_detached_immutable_redacted_and_no_identifier_rows_private_paths_or_io(self):
        s, g = contracts(); before_s, before_g = deepcopy(s), deepcopy(g)
        r = row(s, 0); r[1] = "NEVER_RETURN_OR_REPR_PRIVATE_ID"
        with patch("builtins.open", side_effect=AssertionError("file IO is forbidden")):
            result = prepare([r], s, g, extra=True)
        self.assertEqual(s, before_s); self.assertEqual(g, before_g)
        encoded = json.dumps(asdict(result))
        for forbidden in ["NEVER_RETURN_OR_REPR_PRIVATE_ID", "SYNTHETIC_UNOPENED_PRIVATE_PATH",
                          "uninterpreted-private-free-text", "idno", '"rows"', '"records"', '"design_keys"']:
            self.assertNotIn(forbidden, encoded)
            self.assertNotIn(forbidden, repr(result))
        self.assertEqual(set(asdict(result)), {"schema", "study_id", "edition", "groups", "eligibility", "study_ratio_diagnostic"})
        self.assertNotIn("reviewed", result.schema)
        with self.assertRaises(FrozenInstanceError):
            result.edition = "changed"
        g["groupsInDeclaredApiOrder"][0]["labelDeOriginalForm"] = "changed"
        self.assertEqual(result.groups[0].label_de_original_form, "synthetic-option-1")
