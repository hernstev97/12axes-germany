"""Synthetic aggregate oracles only; no files, respondents or study analysis."""

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
import unittest

from pipeline.policy_export_v2 import (
    ExportErrorCode, PolicyExportError, build_reviewed_reference_export,
    validate_reference_candidate,
)
from pipeline.policy_analysis_v2 import (
    MissingReasonAggregate, NotAskedAggregate, PreparationStatus,
    PreparedQuestionReferences, PreparedWeightReference, PrivateStudyReferences,
    WeightDiagnostics, expose_prepared_candidate,
)
from pipeline.policy_reference_v2 import Accounting, CategoricalReference, CategoryEstimate, VarianceStatus


STUDY = "ESS9e03_3"
IDS = [f"{STUDY}:{variable}" for variable in ("sofrdst", "sofrwrk", "sofrpr", "sofrprv")]
REASONS = ["Refusal", "Don't know", "No answer", "export_blank_unclassified"]
PREPARED = "prepared_pending_result_review"
WITHHELD = "withheld_base_or_cell_count"
NO_VALID = "no_valid_answers"


def canonical_hash(value):
    # Independent definition of the explicitly requested gate serialization.
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)
    return sha256(raw.encode('utf-8')).hexdigest()


def contract():
    """Declared synthetic provenance; authentic source bytes are NOT claimed."""
    return {
        "study_id": STUDY, "edition": "3.3", "round": 9, "country": "DE",
        "input": {"path": "data/raw/SYNTHETIC-NEVER-READ.csv", "sha256": "1" * 64,
                  "bytes": 1, "editionEvidence": "synthetic_not_verified"},
        "metadata": {"round_column": "essround", "edition_column": "edition", "expected_round": "9",
                     "expected_edition": "3.3", "normalizationRule": "integer_round_optional_dot_zero_decimal_edition_v1"},
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
        "adapter": {
            "study_id": STUDY, "edition": "3.3", "country": "DE", "country_column": "cntry", "id_column": "idno",
            "weight_columns": {"primary": "pspwght", "sensitivities": ["dweight", "anweight"]},
            "questions": [{"question_id": qid, "variable": qid.split(':')[1],
                           "categoryCodes": ["1", "2", "3", "4", "5"],
                           "missingCodes": dict(zip(["7", "8", "9", ""], REASONS)),
                           "structurallyNotAskedCodes": ["SYNTHETIC_NOT_ASKED"]} for qid in IDS],
            "design_columns": None,
        },
    }


def accounting(counts, weights, missing_count=3, missing_weight=15.0, not_asked_count=1, not_asked_weight=11.0):
    valid_count, valid_weight = sum(counts), sum(weights)
    return {"total_count": valid_count + missing_count + not_asked_count,
            "total_weight": float(valid_weight + missing_weight + not_asked_weight),
            "eligible_count": valid_count + missing_count, "eligible_weight": float(valid_weight + missing_weight),
            "valid_count": valid_count, "valid_weight": float(valid_weight),
            "missing_count": missing_count, "missing_weight": float(missing_weight),
            "not_asked_count": not_asked_count, "not_asked_weight": float(not_asked_weight)}


def question(qid, counts=(30, 70, 0, 0, 0), status=PREPARED, weighted=True, total=104):
    # Weighted hand oracle: primary A60/B70, dweight A30/B140,
    # unweighted A30/B70, anweight A120/B140. No row data exists here.
    if weighted:
        assert tuple(counts) == (30, 70, 0, 0, 0) and total == 104 and status == PREPARED
        weights = {"pspwght": [60, 70, 0, 0, 0], "dweight": [30, 140, 0, 0, 0],
                   "unweighted": [30, 70, 0, 0, 0], "anweight": [120, 140, 0, 0, 0]}
        accounts = {
            "pspwght": accounting(counts, weights['pspwght']),
            "dweight": accounting(counts, weights['dweight'], 3, 3, 1, 1),
            "unweighted": accounting(counts, weights['unweighted'], 3, 3, 1, 1),
            "anweight": accounting(counts, weights['anweight'], 3, 30, 1, 22),
        }
        reasons = [(2, 8.0), (1, 7.0), (0, 0.0), (0, 0.0)]
        not_asked = {"count": 1, "primary_weight_sum": 11.0}
        sensitivity = {"max_abs_primary_unweighted": float(Fraction(21, 130)),
                       "max_abs_primary_dweight": float(Fraction(63, 221))}
    else:
        missing = total - sum(counts)
        weights = {key: list(counts) for key in ('pspwght', 'dweight', 'unweighted', 'anweight')}
        accounts = {key: accounting(counts, list(counts), missing, missing, 0, 0) for key in weights}
        reasons = [(missing, float(missing)), (0, 0.0), (0, 0.0), (0, 0.0)]
        not_asked = {"count": 0, "primary_weight_sum": 0.0}
        sensitivity = {"max_abs_primary_unweighted": 0.0, "max_abs_primary_dweight": 0.0}
    reference = None
    if status == PREPARED:
        reference = {
            "variance_status": "no_design_basis",
            "estimates": {
                key: {"role": 'primary' if key == 'pspwght' else 'equivalence_diagnostic' if key == 'anweight' else 'sensitivity',
                      "accounting": accounts[key], "categories": [
                          {"code": str(index + 1), "count": count, "weight_sum": float(weights[key][index]),
                           "proportion": float(Fraction(weights[key][index]) / Fraction(accounts[key]['valid_weight']))}
                          for index, count in enumerate(counts)]} for key in weights},
            "sensitivity": sensitivity,
            "anweight_equivalence_diagnostic": {"max_abs_primary_anweight": 0.0, "ratio_scope": "all_de_cases",
                                               "anweight_pspwght_ratio_min": 2.0 if weighted else 1.0,
                                               "anweight_pspwght_ratio_max": 2.0 if weighted else 1.0},
        }
    return {"source": {"study_id": STUDY, "edition": "3.3", "question_id": qid}, "status": status,
            "category_counts": [{"code": str(i + 1), "count": count} for i, count in enumerate(counts)],
            "primary_accounting": accounts['pspwght'],
            "missing_reasons": [{"reason": reason, "count": count, "primary_weight_sum": amount}
                                for reason, (count, amount) in zip(REASONS, reasons)],
            "not_asked": not_asked, "reference": reference}


def candidate(questions=None):
    return {"schema": "policy-reference-candidate-v2-wip", "study_id": STUDY, "edition": "3.3",
            "questions": questions if questions is not None else [question(qid) for qid in IDS]}


def gate(payload, source, approved=None):
    return {"schemaVersion": 1, "decision": "ALLOW_REVIEWED_HISTORICAL_REFERENCE_V2", "studyId": STUDY,
            "edition": "3.3", "candidateSha256": canonical_hash(payload), "sourceContractSha256": canonical_hash(source),
            "approvedQuestionIds": approved if approved is not None else [q['source']['question_id'] for q in payload['questions']
                                                                        if q['status'] == PREPARED],
            "reviewManifestSha256": "2" * 64,
            "reviewers": [{"role": "methods_reproducibility", "reportPath": "reports/loop/reviews/SYNTHETIC-A.md",
                           "sha256": "3" * 64, "decision": "ACCEPTED_BOUNDED"},
                          {"role": "sources_constructs_fairness", "reportPath": "reports/loop/reviews/SYNTHETIC-B.md",
                           "sha256": "4" * 64, "decision": "ACCEPTED_BOUNDED"}]}


class PolicyExportTests(unittest.TestCase):
    def setUp(self):
        self.source, self.payload = contract(), candidate()
        self.decision = gate(self.payload, self.source)

    def assert_invalid(self, payload=None, source=None, decision=None, code=None):
        with self.assertRaises(PolicyExportError) as raised:
            build_reviewed_reference_export(self.payload if payload is None else payload,
                                           self.source if source is None else source,
                                           self.decision if decision is None else decision)
        self.assertRegex(str(raised.exception), r'^policy_export_error: [a-z_]+$')
        if code:
            self.assertEqual(raised.exception.code, code)

    def test_100_case_fraction_oracle_and_public_allowlist(self):
        result = build_reviewed_reference_export(self.payload, self.source, self.decision)
        self.assertEqual(set(result), {'schemaVersion', 'status', 'studyId', 'edition', 'sourceContractSha256',
                                      'candidateSha256', 'reviewManifestSha256', 'questions'})
        self.assertEqual([q['id'] for q in result['questions']], IDS)
        ref = result['questions'][0]['reference']
        self.assertEqual(set(ref), {'weight', 'validCount', 'totalCount', 'missingCount', 'notAskedCount', 'categories',
                                   'missingReasons', 'missingWeight', 'allDEWeight', 'sensitivity',
                                   'anweightEquivalenceDiagnostic', 'uncertainty'})
        self.assertEqual((ref['validCount'], ref['totalCount'], ref['missingCount'], ref['notAskedCount']), (100, 104, 3, 1))
        self.assertEqual(ref['categories'], [{'code': '1', 'proportion': float(Fraction(6, 13))},
                                            {'code': '2', 'proportion': float(Fraction(7, 13))},
                                            {'code': '3', 'proportion': 0.0}, {'code': '4', 'proportion': 0.0},
                                            {'code': '5', 'proportion': 0.0}])
        self.assertAlmostEqual(ref['sensitivity']['maxAbsUnweighted'], float(Fraction(21, 130)))
        self.assertAlmostEqual(ref['sensitivity']['maxAbsDweight'], float(Fraction(63, 221)))
        self.assertEqual((ref['missingWeight'], ref['allDEWeight']), (15.0, 156.0))
        self.assertEqual(ref['anweightEquivalenceDiagnostic'], {'maxAbsDifference': 0.0, 'ratioScope': 'all_de_cases',
                                                               'ratioMin': 2.0, 'ratioMax': 2.0})
        self.assertIsNone(ref['uncertainty'])
        self.assertEqual(set(ref['categories'][0]), {'code', 'proportion'})
        self.assertNotIn('SYNTHETIC-NEVER-READ', json.dumps(result))
        self.assertNotIn('category_counts', json.dumps(result))
        self.assertNotIn('weight_sum', json.dumps(result))

    def test_actual_analysis_candidate_shape_compatibility(self):
        prepared_questions = []
        for q in self.payload['questions']:
            refs = []
            for weight, item in q['reference']['estimates'].items():
                estimates = tuple(CategoryEstimate(c['code'], c['count'], c['weight_sum'], c['proportion'], None, None)
                                  for c in item['categories'])
                reference = CategoricalReference(STUDY, q['source']['question_id'], Accounting(**item['accounting']),
                                                 estimates, VarianceStatus.NO_DESIGN_BASIS, None)
                refs.append(PreparedWeightReference(weight, item['role'], reference))
            prepared_questions.append(PreparedQuestionReferences(q['source']['question_id'],
                PreparationStatus.PREPARED_PENDING_RESULT_REVIEW, tuple(refs),
                tuple(MissingReasonAggregate(r['reason'], r['count'], r['primary_weight_sum']) for r in q['missing_reasons']),
                NotAskedAggregate(1, 11.0), WeightDiagnostics(float(Fraction(21, 130)), float(Fraction(63, 221)), 0.0, 2.0, 2.0)))
        original = expose_prepared_candidate(PrivateStudyReferences(STUDY, '3.3', tuple(prepared_questions)))
        self.assertEqual(original, self.payload)
        validate_reference_candidate(original, self.source)

    def test_input_and_output_are_detached_and_unchanged(self):
        before = deepcopy((self.payload, self.source, self.decision))
        result = build_reviewed_reference_export(self.payload, self.source, self.decision)
        self.assertEqual((self.payload, self.source, self.decision), before)
        result['questions'][0]['reference']['categories'][0]['code'] = 'changed'
        result['questions'][0]['reference']['missingReasons'][0]['reason'] = 'changed'
        self.assertEqual((self.payload, self.source, self.decision), before)

    def test_99_100_and_4_5_boundaries_and_no_valid_nulls(self):
        payload = candidate([
            question(IDS[0], (30, 69, 0, 0, 0), WITHHELD, False),
            question(IDS[1], (4, 96, 0, 0, 0), WITHHELD, False),
            question(IDS[2], (5, 95, 0, 0, 0), PREPARED, False),
            question(IDS[3], (0, 0, 0, 0, 0), NO_VALID, False),
        ])
        result = build_reviewed_reference_export(payload, self.source, gate(payload, self.source))
        self.assertEqual([q['status'] for q in result['questions']],
                         [WITHHELD, WITHHELD, 'reviewed_historical_reference', NO_VALID])
        for index in (0, 1, 3):
            self.assertEqual(result['questions'][index], {'id': IDS[index], 'status': payload['questions'][index]['status'],
                                                        'reference': None})
        self.assertEqual(result['questions'][2]['reference']['categories'][0]['proportion'], float(Fraction(1, 20)))

    def test_subset_review_retains_every_item_without_stats(self):
        decision = gate(self.payload, self.source, [IDS[2]])
        result = build_reviewed_reference_export(self.payload, self.source, decision)
        self.assertEqual(len(result['questions']), 4)
        self.assertEqual(result['questions'][0], {'id': IDS[0], 'status': 'result_review_withheld', 'reference': None})
        self.assertEqual(result['questions'][2]['status'], 'reviewed_historical_reference')
        decision['approvedQuestionIds'] = []
        self.assertTrue(all(q['reference'] is None for q in build_reviewed_reference_export(self.payload, self.source, decision)['questions']))

    def test_valid_altered_candidate_with_old_hash_fails(self):
        changed = deepcopy(self.payload)
        changed['questions'][0]['missing_reasons'].reverse()  # valid different list serialization
        self.assert_invalid(payload=changed, code=ExportErrorCode.HASH_MISMATCH)

    def test_whole_source_provenance_hash_and_identity_binding(self):
        changed = deepcopy(self.source)
        changed['provenance']['populationCoverageLimit'] = 'different synthetic scope'
        self.assert_invalid(source=changed, code=ExportErrorCode.HASH_MISMATCH)
        for field, value in [('study_id', 'ESS9'), ('edition', '3.4'), ('round', 8), ('country', 'FR')]:
            changed = deepcopy(self.source)
            changed[field] = value
            self.assert_invalid(source=changed, code=ExportErrorCode.INVALID_CONTRACT)

    def test_sampling_source_prose_is_preserved_without_trimming(self):
        changed = deepcopy(self.source)
        changed['provenance']['samplingProceduresDeclaredEn'] = [' synthetic source prose \n']
        before = deepcopy(changed)
        result = build_reviewed_reference_export(self.payload, changed, gate(self.payload, changed))
        self.assertEqual(changed, before)
        self.assertEqual(result['sourceContractSha256'], canonical_hash(changed))

    def test_question_order_identity_category_order_and_reasons_bound(self):
        paths = [(['questions'], 'reverse'),
                 (['questions', 0, 'source', 'question_id'], 'foreign:id'),
                 (['questions', 0, 'category_counts', 0, 'code'], 'PRIVATE-CODE'),
                 (['questions', 0, 'missing_reasons', 0, 'reason'], 'PRIVATE-REASON')]
        for path, value in paths:
            with self.subTest(path=path):
                changed = deepcopy(self.payload)
                current = changed
                for part in path[:-1]: current = current[part]
                if value == 'reverse': current[path[-1]].reverse()
                else: current[path[-1]] = value
                self.assert_invalid(payload=changed)
        changed = deepcopy(self.source)
        changed['adapter']['questions'][0]['categoryCodes'].reverse()
        self.assert_invalid(source=changed, decision=gate(self.payload, changed))
        changed = deepcopy(self.payload)
        changed['questions'][0]['missing_reasons'].pop()
        self.assert_invalid(payload=changed)

    def test_private_keys_rejected_at_every_candidate_object_level(self):
        paths = [[], ['questions', 0], ['questions', 0, 'source'], ['questions', 0, 'category_counts', 0],
                 ['questions', 0, 'primary_accounting'], ['questions', 0, 'missing_reasons', 0],
                 ['questions', 0, 'not_asked'], ['questions', 0, 'reference'],
                 ['questions', 0, 'reference', 'estimates'], ['questions', 0, 'reference', 'estimates', 'pspwght'],
                 ['questions', 0, 'reference', 'estimates', 'pspwght', 'accounting'],
                 ['questions', 0, 'reference', 'estimates', 'pspwght', 'categories', 0],
                 ['questions', 0, 'reference', 'sensitivity'],
                 ['questions', 0, 'reference', 'anweight_equivalence_diagnostic']]
        for path in paths:
            with self.subTest(path=path):
                changed = deepcopy(self.payload)
                current = changed
                for part in path: current = current[part]
                current['private_idno'] = 'SYNTHETIC-SECRET'
                self.assert_invalid(payload=changed, code=ExportErrorCode.INVALID_CANDIDATE)

    def test_private_keys_rejected_at_every_contract_and_gate_object_level(self):
        for path in [[], ['input'], ['adapter'], ['adapter', 'weight_columns'], ['adapter', 'questions', 0],
                     ['metadata'], ['responseSerialization'], ['provenance'], ['provenance', 'fieldwork', 0]]:
            changed = deepcopy(self.source)
            current = changed
            for part in path: current = current[part]
            current['private'] = 'SYNTHETIC-SECRET'
            self.assert_invalid(source=changed, code=ExportErrorCode.INVALID_CONTRACT)
        for path in [[], ['reviewers', 0]]:
            changed = deepcopy(self.decision)
            current = changed
            for part in path: current = current[part]
            current['private'] = 'SYNTHETIC-SECRET'
            self.assert_invalid(decision=changed, code=ExportErrorCode.INVALID_DECISION)

    def test_status_cannot_promote_suppressed_or_pretend_review(self):
        for value in ['reviewed_historical_reference', 'published', 'unknown']:
            changed = deepcopy(self.payload)
            changed['questions'][0]['status'] = value
            self.assert_invalid(payload=changed)
        changed = candidate([question(qid, (4, 96, 0, 0, 0), WITHHELD, False) for qid in IDS])
        changed['questions'][0]['status'] = PREPARED
        self.assert_invalid(payload=changed)

    def test_scalar_and_arithmetic_accounting_corruption_fails(self):
        paths = [(['questions', 0, 'primary_accounting', 'valid_count'], True),
                 (['questions', 0, 'primary_accounting', 'total_weight'], float('inf')),
                 (['questions', 0, 'primary_accounting', 'total_count'], 105),
                 (['questions', 0, 'missing_reasons', 0, 'primary_weight_sum'], 9.0),
                 (['questions', 0, 'not_asked', 'count'], 0),
                 (['questions', 0, 'reference', 'estimates', 'pspwght', 'categories', 0, 'proportion'], .5),
                 (['questions', 0, 'reference', 'estimates', 'dweight', 'categories', 0, 'count'], 31),
                 (['questions', 0, 'reference', 'estimates', 'unweighted', 'categories', 0, 'weight_sum'], 31.0),
                 (['questions', 0, 'reference', 'sensitivity', 'max_abs_primary_dweight'], .5),
                 (['questions', 0, 'reference', 'anweight_equivalence_diagnostic', 'ratio_scope'], 'valid_only'),
                 (['questions', 0, 'reference', 'anweight_equivalence_diagnostic', 'anweight_pspwght_ratio_min'], 3.0)]
        for path, value in paths:
            with self.subTest(path=path):
                changed = deepcopy(self.payload)
                current = changed
                for part in path[:-1]: current = current[part]
                current[path[-1]] = value
                self.assert_invalid(payload=changed)

    def test_exact_four_roles_and_common_study_denominators(self):
        changed = deepcopy(self.payload)
        changed['questions'][0]['reference']['estimates']['dweight']['role'] = 'primary'
        self.assert_invalid(payload=changed)
        changed = deepcopy(self.payload)
        del changed['questions'][0]['reference']['estimates']['anweight']
        self.assert_invalid(payload=changed)
        changed = deepcopy(self.payload)
        changed['questions'][0] = question(IDS[0], (30, 69, 0, 0, 0), WITHHELD, False, 103)
        self.assert_invalid(payload=changed)

    def test_fake_gate_roles_paths_pins_ids_and_decision_fails(self):
        mutations = [('schemaVersion', True), ('decision', 'ACCEPTED'), ('studyId', 'ESS5e03_6'),
                     ('candidateSha256', '0' * 64), ('sourceContractSha256', '0' * 64),
                     ('reviewManifestSha256', 'BAD'), ('approvedQuestionIds', [IDS[0], IDS[0]]),
                     ('approvedQuestionIds', ['foreign:id'])]
        for key, value in mutations:
            changed = deepcopy(self.decision)
            changed[key] = value
            self.assert_invalid(decision=changed)
        for key, value in [('role', 'sources_constructs_fairness'), ('decision', 'APPROVED'),
                           ('sha256', 'not-a-pin'), ('reportPath', 'reports/loop/reviews/../private.md'),
                           ('reportPath', '/tmp/review.md'), ('reportPath', 'reports/loop/authors/report.md'),
                           ('reportPath', 'reports/loop/reviews/SYNTHETIC-B.md')]:
            changed = deepcopy(self.decision)
            changed['reviewers'][0][key] = value
            self.assert_invalid(decision=changed)
        changed = deepcopy(self.decision)
        changed['reviewers'].pop()
        self.assert_invalid(decision=changed)

    def test_withheld_and_no_valid_cannot_be_approved_or_carry_reference(self):
        payload = candidate([question(qid, (0, 0, 0, 0, 0), NO_VALID, False) for qid in IDS])
        self.assert_invalid(payload=payload, decision=gate(payload, self.source, [IDS[0]]))
        payload['questions'][0]['reference'] = self.payload['questions'][0]['reference']
        self.assert_invalid(payload=payload)

    def test_cyclic_and_custom_payloads_fail_with_static_error(self):
        changed = deepcopy(self.payload)
        changed['questions'][0]['private'] = changed
        self.assert_invalid(payload=changed)
        class CustomDict(dict):
            pass
        self.assert_invalid(payload=CustomDict(self.payload))
        changed = deepcopy(self.payload)
        changed['questions'][0]['primary_accounting']['valid_count'] = 10 ** 1000
        self.assert_invalid(payload=changed)


if __name__ == '__main__':
    unittest.main()
