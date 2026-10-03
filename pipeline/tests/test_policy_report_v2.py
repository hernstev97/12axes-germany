"""Synthetic public shapes and fraction oracles; no response data or report IO.

Known source IDs/codes are metadata anchors. All figures, provenance prose and
review pins here are synthetic; rendered strings are discarded, never exported.
"""

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
import unittest

from pipeline.policy_report_v2 import PolicyReportError, render_historical_report


# Independent transcription of the public 43-source selection for test fixtures.
DEFINITIONS = [
    ('ESS5e03_6', '3.6', 5, [('bplcdc', 'zero10'), ('dpcstrb', 'zero10'), ('hrshsnta', 'five'),
                            ('dbctvrd', 'five'), ('lwstrob', 'five'), ('rgbrklw', 'five')]),
    ('ESS8e02_3', '2.3', 8, [('gvslvol', 'zero10'), ('gvslvue', 'zero10'), ('gvcldcr', 'zero10'),
                            ('bnlwinc', 'four'), ('eduunmp', 'four'), ('inctxff', 'five'), ('sbsrnen', 'five'),
                            ('banhhap', 'five'), ('imsclbn', 'five'), ('wrkprbf', 'four')]),
    ('ESS9e03_3', '3.3', 9, [('sofrdst', 'five'), ('sofrwrk', 'five'), ('sofrpr', 'five'), ('sofrprv', 'five')]),
    ('ESS10SCe03_2', '3.2', 10, [('fairelc', 'zero10'), ('dfprtal', 'zero10'), ('medcrgv', 'zero10'),
                               ('rghmgpr', 'zero10'), ('votedir', 'zero10'), ('cttresa', 'zero10'), ('gptpelc', 'zero10'),
                               ('gvctzpv', 'zero10'), ('grdfinc', 'zero10'), ('viepol', 'zero10'), ('wpestop', 'zero10'),
                               ('scchpldm', 'two'), ('vteurmmb', 'eu'), ('keydec', 'zero10'), ('imsmetn', 'four'),
                               ('imdfetn', 'four'), ('impcntr', 'four')]),
    ('ESS11e04_2', '4.2', 11, [('gincdif', 'five'), ('euftf', 'zero10'), ('eqparep', 'five'),
                              ('eqparlv', 'five'), ('freinsw', 'five'), ('fineqpy', 'five')]),
]
CODES = {'zero10': [str(n) for n in range(11)], 'five': ['1', '2', '3', '4', '5'],
         'four': ['1', '2', '3', '4'], 'two': ['1', '2'], 'eu': ['1', '2', '33', '44', '55', '65']}
IDS = [study + ':' + variable for study, _, _, questions in DEFINITIONS for variable, _ in questions]


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                             allow_nan=False).encode('utf-8')).hexdigest()


def fixtures():
    sources, exports = [], []
    for study, edition, round_number, variables in DEFINITIONS:
        questions = []
        for variable, group in variables:
            missing = {'9': 'No answer', '': 'export_blank_unclassified'} if group == 'two' else {
                '77' if group in ('zero10', 'eu') else '7': 'Refusal',
                '88' if group in ('zero10', 'eu') else '8': "Don't know",
                '99' if group in ('zero10', 'eu') else '9': 'No answer', '': 'export_blank_unclassified'}
            questions.append({'question_id': study + ':' + variable, 'variable': variable,
                              'categoryCodes': list(CODES[group]), 'missingCodes': missing,
                              'structurallyNotAskedCodes': []})
        doi = '10.21338/' + study.lower()
        provenance = {'dataDoi': doi, 'dataDoiUrl': 'https://doi.org/' + doi,
                      'documentationDoi': doi + '-synthetic-doc', 'documentationDoiUrl': 'https://doi.org/' + doi + '-synthetic-doc',
                      'populationDeclaredEn': 'SYNTHETIC declared target; not a source claim.',
                      'populationCoverageLimit': 'SYNTHETIC unverified coverage.',
                      'fieldwork': [{'start': 'SYNTHETIC-start', 'end': 'SYNTHETIC-end',
                                     'modesDeclaredEn': ['SYNTHETIC-mode']}],
                      'samplingProceduresDeclaredEn': ['SYNTHETIC sampling only; no design basis.'],
                      'dataLicenseId': 'SYNTHETIC-data-license', 'documentationLicenseId': 'SYNTHETIC-document-license',
                      'versionNotes': ['SYNTHETIC version note.'], 'sourceRefs': ['SYNTHETIC-source-' + study]}
        if round_number == 8:
            provenance['samplingProceduresDeclaredEn'] = ['SYNTHETIC fixture of Munich coverage limitation; not empirical evidence.']
        source = {'study_id': study, 'edition': edition, 'round': round_number, 'country': 'DE',
                  'input': {'path': 'data/raw/SYNTHETIC-NEVER-OPEN.csv', 'sha256': '1' * 64, 'bytes': 1,
                            'editionEvidence': 'synthetic_not_verified'},
                  'adapter': {'study_id': study, 'edition': edition, 'country': 'DE', 'country_column': 'cntry',
                              'id_column': 'idno', 'weight_columns': {'primary': 'pspwght', 'sensitivities': ['dweight', 'anweight']},
                              'questions': questions, 'design_columns': None},
                  'metadata': {'round_column': 'essround', 'edition_column': 'edition', 'expected_round': str(round_number),
                               'expected_edition': edition, 'normalizationRule': 'integer_round_optional_dot_zero_decimal_edition_v1'},
                  'responseSerialization': {'rule': 'canonical_nonnegative_integer_optional_zero_fraction_v1',
                                            'emptyCellReason': 'export_blank_unclassified'}, 'provenance': provenance}
        exported = []
        for definition in questions:
            reasons = [{'reason': reason, 'count': 0, 'primaryWeightSum': 0.0}
                       for reason in dict.fromkeys(definition['missingCodes'].values())]
            reasons[0].update(count=2, primaryWeightSum=8.0)
            reasons[-1].update(count=1, primaryWeightSum=7.0)
            # Hand oracle: A30/B70, primary sums A60/B70 => 6/13,7/13.
            proportions = [float(Fraction(6, 13)), float(Fraction(7, 13))] + [0.0] * (len(definition['categoryCodes']) - 2)
            reference = {'weight': 'pspwght', 'validCount': 100, 'totalCount': 103, 'missingCount': 3, 'notAskedCount': 0,
                         'categories': [{'code': code, 'proportion': proportion} for code, proportion in
                                        zip(definition['categoryCodes'], proportions)],
                         'missingReasons': reasons, 'missingWeight': 15.0, 'allDEWeight': 145.0,
                         'sensitivity': {'maxAbsUnweighted': float(Fraction(21, 130)), 'maxAbsDweight': float(Fraction(63, 221))},
                         'anweightEquivalenceDiagnostic': {'maxAbsDifference': 0.0, 'ratioScope': 'all_de_cases',
                                                          'ratioMin': 2.0, 'ratioMax': 2.0}, 'uncertainty': None}
            exported.append({'id': definition['question_id'], 'status': 'reviewed_historical_reference', 'reference': reference})
        exports.append({'schemaVersion': 2, 'status': 'reviewed_historical_descriptive_reference', 'studyId': study,
                        'edition': edition, 'sourceContractSha256': digest(source), 'candidateSha256': '2' * 64,
                        'reviewManifestSha256': '3' * 64, 'questions': exported})
        sources.append(source)
    return sources, exports


class PolicyReportTests(unittest.TestCase):
    def setUp(self):
        self.sources, self.exports = fixtures()

    def fail_safe(self, exports=None, sources=None):
        with self.assertRaises(PolicyReportError) as raised:
            render_historical_report(self.exports if exports is None else exports,
                                     self.sources if sources is None else sources)
        self.assertRegex(str(raised.exception), '^policy_report_error: [a-z_]+$')

    def question_section(self, text, qid):
        return text.split('### `' + qid + '`\n', 1)[1].split('\n### ', 1)[0].split('\n## ', 1)[0]

    def test_independent_43_id_selection_all_categories_and_fraction_oracle(self):
        self.assertEqual(len(IDS), 43)
        text = render_historical_report(self.exports, self.sources)
        for qid in IDS:
            self.assertEqual(text.count('### `' + qid + '`'), 1)
            self.assertEqual(text.count('| `' + qid + '` |'), 1)
        self.assertEqual(text.count(' — Edition '), 5)
        section = self.question_section(text, 'ESS5e03_6:bplcdc')
        # Explicit decimal rendering of independent rational hand results.
        self.assertIn('| 0 | 46,153846 |', section)
        self.assertIn('| 1 | 53,846154 |', section)
        self.assertIn('| 10 | 0,000000 |', section)
        self.assertIn('| `ESS5e03_6:bplcdc` | Referenz im Export freigegeben | 100 | 103 | 3 | 0 | 15 | 145 | 0,161538461538 | 0,285067873303 | 0 | 2 | 2 |', text)
        self.assertIn('| export\\_blank\\_unclassified | 1 | 7 |', section)
        for source, export in zip(self.sources, self.exports):
            for definition in source['adapter']['questions']:
                section = self.question_section(text, definition['question_id'])
                for code in definition['categoryCodes']:
                    self.assertIn('| ' + code + ' |', section)
        self.assertNotIn('SYNTHETIC-NEVER-OPEN', text)

    def test_all_null_n0_withheld_and_unapproved_do_not_make_numbers(self):
        for export in self.exports:
            for index, q in enumerate(export['questions']):
                q['status'] = ['no_valid_answers', 'withheld_base_or_cell_count', 'result_review_withheld'][index % 3]
                q['reference'] = None
        text = render_historical_report(self.exports, self.sources)
        self.assertNotIn('46,153846', text)
        self.assertNotIn('Referenz im Export freigegeben', text)
        for qid in IDS:
            section = self.question_section(text, qid)
            self.assertIn('Weiterhin nicht freigegeben:', section)
            self.assertIn('Keine Zahlenreferenz.', section)
            self.assertIn('Originalcodes aus dem Quellenvertrag (keine Anteile):', section)
            self.assertNotIn('Gewichteter Anteil', section)
        self.assertEqual(text.count('### `ESS10SCe03_2:scchpldm`'), 1)

    def test_studies_remain_separate_with_second_fraction_oracle(self):
        for q in self.exports[1]['questions']:
            ref = q['reference']
            ref['categories'][0]['proportion'] = float(Fraction(5, 11))
            ref['categories'][1]['proportion'] = float(Fraction(6, 11))
            ref['allDEWeight'] = 125.0
            ref['sensitivity'] = {'maxAbsUnweighted': float(Fraction(17, 110)), 'maxAbsDweight': float(Fraction(52, 187))}
        text = render_historical_report(self.exports, self.sources)
        self.assertIn('| 0 | 46,153846 |', self.question_section(text, 'ESS5e03_6:bplcdc'))
        self.assertIn('| 0 | 45,454545 |', self.question_section(text, 'ESS8e02_3:gvslvol'))
        self.assertIn('| 1 | 54,545455 |', self.question_section(text, 'ESS8e02_3:gvslvol'))
        self.assertNotIn('Gesamt aller Studien', text)

    def test_rounded_all_weight_does_not_erase_tiny_valid_reference(self):
        # Valid sums A60e-300/B70e-300 still give 6/13,7/13. Missing sums
        # 8e299+2e299 dominate total=1e300 in binary floating arithmetic.
        # Public form omits validWeight; equal all/missing floats are possible.
        for export in self.exports:
            for question in export['questions']:
                ref = question['reference']
                ref['missingReasons'][0]['primaryWeightSum'] = 8e299
                ref['missingReasons'][-1]['primaryWeightSum'] = 2e299
                ref['missingWeight'] = ref['allDEWeight'] = 1e300
        text = render_historical_report(self.exports, self.sources)
        self.assertIn('| 0 | 46,153846 |', self.question_section(text, 'ESS5e03_6:bplcdc'))

    def test_deterministic_permutations_and_inputs_immutable(self):
        original = deepcopy((self.sources, self.exports))
        text = render_historical_report(self.exports, self.sources)
        self.assertEqual((self.sources, self.exports), original)
        reversed_sources, reversed_exports = deepcopy((self.sources[::-1], self.exports[::-1]))
        for export in reversed_exports:
            for q in export['questions']:
                q['reference']['missingReasons'].reverse()
        self.assertEqual(render_historical_report(reversed_exports, reversed_sources), text)

    def test_known_historical_boundary_methods_and_bound_metadata(self):
        text = render_historical_report(self.exports, self.sources)
        self.assertIn('v1-A/B', text)
        self.assertIn('sechs zusätzlich ausgewählten ESS11-Felder', text)
        self.assertIn('keine unberührte Bestätigung', text)
        self.assertIn('100 gültige Fälle', text)
        self.assertIn('mindestens fünf Fälle', text)
        self.assertIn('keine Standardfehler', text)
        self.assertIn('unter allen deutschen Fällen', text)
        self.assertIn('Munich coverage limitation', text)
        self.assertIn('SYNTHETIC declared target', text)
        self.assertIn('SYNTHETIC version note', text)
        self.assertIn('SYNTHETIC-mode', text.replace('\\-', '-'))
        self.assertIn('[10\\.21338/ess5e03\\_6](https://doi.org/10.21338/ess5e03_6)', text)
        self.assertNotIn('validiert', text)
        self.assertNotIn('neutral', text)

    def test_five_studies_and_exact_global_selection_required(self):
        self.fail_safe(exports=self.exports[:-1])
        self.fail_safe(sources=self.sources[:-1])
        duplicated = deepcopy(self.exports)
        duplicated[-1] = duplicated[0]
        self.fail_safe(exports=duplicated)
        duplicated_sources = deepcopy(self.sources)
        duplicated_sources[-1] = duplicated_sources[0]
        self.fail_safe(sources=duplicated_sources)
        for source_field in ['variable', 'question_id']:
            changed = deepcopy(self.sources)
            changed[0]['adapter']['questions'][0][source_field] = 'foreign'
            self.fail_safe(sources=changed)

    def test_shifted_sources_and_unmatched_hashes_fail(self):
        changed = deepcopy(self.exports)
        changed[0]['sourceContractSha256'] = self.exports[1]['sourceContractSha256']
        self.fail_safe(exports=changed)
        changed = deepcopy(self.sources)
        changed[0]['provenance']['populationCoverageLimit'] = 'changed source scope'
        self.fail_safe(sources=changed)
        changed = deepcopy(self.exports)
        changed[0]['edition'] = '2.3'
        self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['questions'][0]['id'] = 'ESS8e02_3:gvslvol'
        self.fail_safe(exports=changed)

    def test_unknown_or_private_status_never_renamed_as_released(self):
        for status in ['prepared_pending_result_review', 'published', 'reviewed', 'unknown']:
            changed = deepcopy(self.exports)
            changed[0]['questions'][0]['status'] = status
            self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['status'] = 'policy-reference-candidate-v2-wip'
        self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['questions'][0]['reference'] = None
        self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['questions'][0]['status'] = 'no_valid_answers'
        self.fail_safe(exports=changed)

    def test_extra_private_keys_all_export_object_levels_fail(self):
        paths = [[], ['questions', 0], ['questions', 0, 'reference'], ['questions', 0, 'reference', 'categories', 0],
                 ['questions', 0, 'reference', 'missingReasons', 0], ['questions', 0, 'reference', 'sensitivity'],
                 ['questions', 0, 'reference', 'anweightEquivalenceDiagnostic']]
        for path in paths:
            with self.subTest(path=path):
                changed = deepcopy(self.exports)
                current = changed[0]
                for part in path: current = current[part]
                current['private_idno'] = 'SYNTHETIC-SECRET'
                self.fail_safe(exports=changed)

    def test_visible_arithmetic_missing_and_ratio_errors_fail(self):
        cases = [(['validCount'], 99), (['validCount'], True), (['totalCount'], 104),
                 (['missingWeight'], 16.0), (['allDEWeight'], float('nan')),
                 (['categories', 0, 'proportion'], .5), (['categories', 1, 'proportion'], float('inf')),
                 (['missingReasons', 0, 'count'], 3), (['missingReasons', 0, 'reason'], 'unknown'),
                 (['sensitivity', 'maxAbsUnweighted'], 1.1),
                 (['anweightEquivalenceDiagnostic', 'ratioScope'], 'valid_only'),
                 (['anweightEquivalenceDiagnostic', 'ratioMin'], 0.0)]
        for path, value in cases:
            with self.subTest(path=path):
                changed = deepcopy(self.exports)
                current = changed[0]['questions'][0]['reference']
                for part in path[:-1]: current = current[part]
                current[path[-1]] = value
                self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['questions'][0]['reference']['missingReasons'].pop()
        self.fail_safe(exports=changed)

    def test_category_order_zero_removal_and_question_order_fail(self):
        changed = deepcopy(self.exports)
        changed[0]['questions'].reverse()
        self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['questions'][0]['reference']['categories'].reverse()
        self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['questions'][0]['reference']['categories'].pop()
        self.fail_safe(exports=changed)

    def test_only_bound_https_doi_links_and_escaped_metadata(self):
        for url in ['http://doi.org/10.21338/ess5e03_6', 'https://evil.invalid/10.21338/ess5e03_6',
                    'https://doi.org@evil.invalid/10.21338/ess5e03_6', 'https://doi.org/10.21338/other',
                    'javascript:alert(1)']:
            changed = deepcopy(self.sources)
            changed[0]['provenance']['dataDoiUrl'] = url
            self.fail_safe(sources=changed)
        sources, exports = deepcopy((self.sources, self.exports))
        sources[0]['provenance']['populationDeclaredEn'] = '<script>alert(1)</script> [bad](https://evil.invalid) | cell'
        exports[0]['sourceContractSha256'] = digest(sources[0])
        text = render_historical_report(exports, sources)
        self.assertNotIn('<script>', text)
        self.assertIn('&lt;script&gt;', text)
        self.assertNotIn('[bad](https://evil.invalid)', text)
        self.assertIn('\\| cell', text)

    def test_custom_and_cyclic_payloads_static_errors(self):
        class CustomDict(dict):
            pass
        changed = deepcopy(self.exports)
        changed[0] = CustomDict(changed[0])
        self.fail_safe(exports=changed)
        changed = deepcopy(self.exports)
        changed[0]['private'] = changed
        self.fail_safe(exports=changed)
        self.fail_safe(exports={})
