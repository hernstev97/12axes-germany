"""Predeclared grouping tests, entirely invented full-frame CSV."""
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from pipeline import group_access as g,empirical_access as a,stage_access as s
from pipeline.tests.test_stage_access import contract,invented_rows


def fixture(mutate=None):
    rows=invented_rows(tuple((h,20) for h in range(1,26)))
    header=[*a.METADATA,'pspwght',*[i['variable'] for i in contract()['items']],
            'invented_unused_identifier',*g.FIELDS]
    for i,row in enumerate(rows):
        row[-1]='NEVER_READ_IDENTIFIER'
        row.extend([str([15,29,30,44,45,59,60,99][i%8]),str(1+i%2),str(1+i%7),'1',
            ['DE4','DE1','DE3'][i%3],str([0,5,10][i%3]),'1',str(1+i%9)])
    # A different country has no parseable protected source fields.
    rows.append(['ZZ','11','4.2','02.07.2026','BAD','BAD','BAD','BAD',*(['BAD']*9),'BAD',*(['BAD']*8)])
    if mutate:mutate(header,rows)
    stream=io.StringIO(newline='');writer=csv.writer(stream);writer.writerow(header);writer.writerows(rows)
    b=stream.getvalue().encode();return b,hashlib.sha256(b).hexdigest()


class Groups(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=json.loads(Path('data/group-source-contract.v1.entwurf.json').read_text())
    def run_frame(self,mutate=None):
        b,h=fixture(mutate);return g.group_frame(b,self.source,contract(),h)
    def test_original_order_same_full_mask_and_no_identifier(self):
        header,rows,levels,diag,full=self.run_frame()
        self.assertEqual(header,list(g.FAMILIES));self.assertEqual(len(rows),500)
        self.assertTrue(all(x['status']=='EXECUTED' for x in diag.values()))
        self.assertNotIn('NEVER_READ_IDENTIFIER',str(rows))
        b,h=fixture();hh,rr,_=s.full_frame(b,contract(),h)
        self.assertEqual(full,s._csv_payload(hh,rr))
    def test_boundaries_binary_sex_es_isced_and_separate_berlin(self):
        _,rows,_,_,_=self.run_frame()
        self.assertEqual([x[0] for x in rows[:8]],['age15_29','age15_29','age30_44','age30_44',
            'age45_59','age45_59','age60plus','age60plus'])
        self.assertEqual(rows[0][1],'male');self.assertEqual(rows[1][1],'female')
        self.assertEqual(rows[4][2],'advanced_vocational_or_tertiary')
        self.assertEqual(rows[2][3],'berlin')
    def test_unknown_sex_suppresses_just_that_grouping(self):
        _,rows,_,d,_=self.run_frame(lambda h,r:r[0].__setitem__(h.index('gndr'),'7'))
        self.assertEqual(d['survey_sex']['status'],'UNSUPPORTED');self.assertTrue(all(x[1]=='NA' for x in rows))
        self.assertEqual(d['education']['status'],'EXECUTED')
    def test_under_target_age_suppresses_age_without_invented_bin(self):
        _,rows,_,d,_=self.run_frame(lambda h,r:r[0].__setitem__(h.index('agea'),'14'))
        self.assertEqual(d['age']['status'],'UNSUPPORTED');self.assertTrue(all(x[0]=='NA' for x in rows))
    def test_unclassifiable_education_not_declared_missing(self):
        _,rows,_,d,_=self.run_frame(lambda h,r:r[0].__setitem__(h.index('eisced'),'55'))
        self.assertEqual(rows[0][2],'NA');self.assertEqual(d['education']['status'],'EXECUTED')
    def test_region_level_and_unknown_region_suppress_whole_component(self):
        for f,v in [('regunit','2'),('region','DEZ')]:
            _,rows,_,d,_=self.run_frame(lambda h,r:r[0].__setitem__(h.index(f),v))
            self.assertEqual(d['regionalEastWest']['status'],'UNSUPPORTED');self.assertTrue(all(x[3]=='NA' for x in rows))
    def test_integral_numeric_tokens_are_canonicalized(self):
        def change(h,r):
            for f in ('gndr','eisced','regunit','prtvgde2'):r[0][h.index(f)]='1.0'
        _,rows,_,d,_=self.run_frame(change)
        self.assertTrue(all(x['status']=='EXECUTED' for x in d.values()));self.assertEqual(rows[0][-1],'party_1')
    def test_vote_filter_inconsistency_no_vote_imputation(self):
        _,rows,_,d,_=self.run_frame(lambda h,r:r[0].__setitem__(h.index('vote'),'2'))
        self.assertEqual(rows[0][5],'did_not_vote');self.assertEqual(d['historical_second_vote']['status'],'UNSUPPORTED')
        self.assertTrue(all(x[-1]=='NA' for x in rows))
    def test_structural_missing_party_not_other_party(self):
        def change(h,r):r[0][h.index('vote')]='3';r[0][h.index('prtvgde2')]='66'
        _,rows,_,d,_=self.run_frame(change)
        self.assertEqual(rows[0][5],'not_eligible');self.assertEqual(rows[0][-1],'NA')
        self.assertEqual(d['historical_second_vote']['status'],'EXECUTED')
    def test_lr_cuts_all_valid_rows_even_missing_score_items(self):
        def change(h,r):
            for row in r[:-1]:
                if row[h.index('lrscale')]=='0':row[h.index('synthetic_B34')]='NA'
        _,_,_,d,_=self.run_frame(change)
        self.assertEqual(d['lr_approx_weighted_thirds']['cutpoints']['a'],0)
        self.assertEqual(d['lr_approx_weighted_thirds']['cutpoints']['b'],5)
    def test_rational_lexicographic_ties_and_no_feasible_thirds(self):
        from decimal import Decimal
        self.assertEqual(g.thirds([0,5,10],[Decimal('1.1')]*3)['a'],0)
        self.assertEqual(g.thirds([0,5,10],[Decimal('1.1')]*3)['b'],5)
        self.assertIsNone(g.thirds([5,5],[Decimal('1.1')]*2))
    def test_no_private_call_before_missing_public_gate(self):
        with tempfile.TemporaryDirectory(dir='outputs/loop') as folder:
            root=Path(folder).resolve()
            with patch.object(g.confirm,'checked_preflight',side_effect=AssertionError('private called')) as private:
                with self.assertRaises(s.AccessError):g.prepare(root)
                private.assert_not_called()

if __name__=='__main__':unittest.main()
