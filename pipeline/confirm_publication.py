"""Closed-path B/FULL aggregate projection; one technical review before copy.

Reuse the independently checked A schema only for identical scientific fields.
Every new confirmation path is bounded separately. This detects accidental
shape/content drift; mutable shared-file receipts are not unforgeable authority.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True
from pipeline import confirm_runtime as runner
from pipeline import r_runtime as rt
from pipeline import stage_access as access
from pipeline.public_schema import _check, SCHEMA_PATH
ROOT = Path(__file__).resolve().parents[1]
GATE = 'reports/loop/gates/confirm-publication.json'
CODE = ('pipeline/confirm_publication.py', 'pipeline/public_schema.py',
        'data/a-aggregate-public.schema.json')
SCOPES = {'B': 'B fixed-model confirmation; result/publication review still required',
 'FULL': 'Full-DE fixed-model transfer after completed B; includes A/B and is not independent confirmation'}
RULE = 'Only previously frozen scores may remain; no competing model or new score can be selected'


def require(value, code):
    if not value:
        raise ValueError(code)


def object_rule(properties):
    return {'type': 'object', 'properties': properties,
            'required': list(properties), 'additionalProperties': False}


def constant(value):
    kind = 'boolean' if isinstance(value, bool) else ('integer' if isinstance(value, int) else
        'number' if isinstance(value, float) else 'string' if isinstance(value, str) else
        'null' if value is None else 'array' if isinstance(value, list) else 'object')
    rule = {'type': kind, 'const': value}
    if kind == 'array':
        unique = list({json.dumps(x,sort_keys=True): x for x in value}.values())
        rule.update(items={'oneOf': [constant(x) for x in unique]} if unique else {'type': 'null'},
                    minItems=len(value), maxItems=len(value))
    elif kind == 'object':
        rule.update(object_rule({k: constant(v) for k, v in value.items()}))
    return rule


def scores_rule(allowed):
    return {'oneOf': [{'type': 'array', 'items': {'type': 'string', 'enum': allowed},
            'minItems': 0, 'maxItems': len(allowed), 'uniqueItems': True},
            {'type': 'string', 'enum': allowed}]}


def validate_confirmation(value, freeze, code_hashes, arm, evaluated_scores):
    require(arm in SCOPES and isinstance(freeze, dict) and freeze['model'] in ('M2','M3'), 'ARM_MODEL')
    require(evaluated_scores == [s for s in freeze['scores'] if s in evaluated_scores] and
            len(evaluated_scores) >= 2, 'EVALUATED_SCORE_SET')
    schema = json.loads(SCHEMA_PATH.read_text()); k = len(freeze['groups'])
    model = copy.deepcopy(schema['$defs']['model'+str(k)])
    executed = model['oneOf'][0]['properties']
    point = executed['standardized_points']
    labels = [f'{item}|t{j}' for item, categories in freeze['config']['manifest'].items()
              for j in range(1, len(categories))]
    point['properties'].update(thresholds={'type': 'array','items': {'type': 'number'},
        'minItems': len(labels), 'maxItems': len(labels)}, threshold_labels=constant(labels),
        threshold_observed_max_difference={'type': 'number'})
    point['required'] += ['thresholds', 'threshold_labels', 'threshold_observed_max_difference']
    sr = executed['scores']; sr['properties'] = {s: sr['properties'][s] for s in evaluated_scores}
    sr['required'] = list(evaluated_scores)
    efa = copy.deepcopy(schema['$defs']['efa'+str(k)])
    for branch in efa['oneOf']:
        branch['properties']['factor_count'] = constant(k); branch['required'].append('factor_count')
    confirmation = object_rule({'status': {'type':'string','enum':
        ['CRITERIA_PASSED_PENDING_RESULT_REVIEW','NO_PUBLIC_PROFILE']},
        'global_model_passed': {'type':'boolean'},
        'score_criteria_passed': scores_rule(evaluated_scores),
        'retained_scores': scores_rule(evaluated_scores),
        'suppressed_scores': scores_rule(evaluated_scores),
        'evaluated_frozen_scores': constant(evaluated_scores),
        'minimum_scores': constant(2), 'rule': constant(RULE)})
    properties = {p: copy.deepcopy(schema['properties'][p]) for p in
                  ('config','counts','point_moments')}
    properties['limits']=constant(freeze['config']['limits'][:4]+[
        'Frozen A model and score set; no B competition or parameter rescue',
        'Author config status is not evidence of either freeze authority or empirical/result approval'])
    properties.update(schema=constant('life93-fixed-model-confirmation-aggregate-1'),
        arm=constant(arm), scope=constant(SCOPES[arm]), freeze=constant(freeze),
        source_code_pins=constant({p: code_hashes[p] for p in (*access.SOURCE_CODE,'pipeline/ordinal/confirm.R')}),
        efa=efa, model_name=constant(freeze['model']), model=model, confirmation=confirmation)
    document={**object_rule(properties), '$defs': schema['$defs']}
    _check(value, document, document)
    require(value['config'] == freeze['config'], 'FIXED_CONFIG')
    c=value['confirmation']; m=value['model']
    passing = [s for s in evaluated_scores if m.get('scores',{}).get(s,{}).get('passed') is True]
    global_passed = m['status']=='EXECUTED' and m['eligible'] is True
    kept = passing if global_passed and len(passing)>=2 else []
    require(c['global_model_passed']==global_passed and (c['score_criteria_passed'] if isinstance(c['score_criteria_passed'],list) else [c['score_criteria_passed']])==passing and
        (c['retained_scores'] if isinstance(c['retained_scores'],list) else [c['retained_scores']])==kept and
        (c['suppressed_scores'] if isinstance(c['suppressed_scores'],list) else [c['suppressed_scores']])==[s for s in evaluated_scores if s not in kept]
        and c['status']==('CRITERIA_PASSED_PENDING_RESULT_REVIEW' if kept else 'NO_PUBLIC_PROFILE'),
        'DECISION_CONSISTENCY')
    counts=value['counts']
    require(all(isinstance(counts[x],int) and counts[x]>=0 for x in
        ('n_design','n_complete','n_excluded','psus','strata','design_df','zero_psus','contributing_complete_psus'))
        and counts['n_complete']+counts['n_excluded']==counts['n_design'] and
        0<=counts['weighted_missing_mass']<=1, 'COUNT_CONSISTENCY')
    return value


def public_export_preflight(root):
    frozen=access.regular_path(root,GATE,public=True).read_bytes(); gate=json.loads(frozen)
    require(gate.get('schema')=='life93-confirm-publication-1' and
            gate.get('decision')=='ACCEPTED_BOUNDED', 'EXPORT_GATE')
    review=gate.get('review',{})
    require(review.get('scope')=='aggregate-schema-provenance' and bool(review.get('reviewer')), 'EXPORT_REVIEW')
    observed={}
    for entry in [review,*gate.get('artifacts',[])]:
        p=entry.get('path'); expected=entry.get('sha256')
        require(access.valid_sha(expected) and p not in observed, 'EXPORT_PIN')
        observed[p]=rt.digest(access.regular_path(root,p,public=True))
        require(observed[p]==expected,'EXPORT_PIN')
    require(set(CODE).issubset(observed),'EXPORT_CODE_SET')
    return {'gate': hashlib.sha256(frozen).hexdigest(),'code':{p:observed[p] for p in CODE}}


def export_confirmation(arm,label,root=ROOT):
    require(arm in SCOPES and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}',label), 'ARM_LABEL')
    export_gate=public_export_preflight(root)  # All new helper pins before any private read.
    auth=runner.checked_preflight(root,arm)
    own=root/rt.PRIVATE_ROOT/'runtime-runs'/label
    require(own.is_dir() and own.resolve()==own and not own.is_symlink(),'RUN_PATH')
    def private(name):return rt.regular_path(root,str((own/name).relative_to(root)),private=True)
    receipt_path=private('receipt.json'); receipt_bytes=receipt_path.read_bytes()
    receipt_sha=hashlib.sha256(receipt_bytes).hexdigest(); receipt=json.loads(receipt_bytes)
    code=rt.code_hashes(root,runner.CODE_PRIVATE); runtime=rt.validate_runtime(root)
    require(receipt.get('schema')=='r-confirm-runtime-run-v1' and receipt.get('stage')==arm and
        receipt.get('label')==label and receipt.get('exitCode')==0 and receipt.get('runtimeProbeExitCode')==0
        and receipt.get('privateAuthorization')==auth and receipt.get('codeHashes')==code and
        receipt.get('runtimePins')==runtime and receipt.get('runtimePinsAfter')==runtime,'ACTUAL_RUN')
    runner.check_entry_files(private('confirmation-entry.R'),receipt.get('entrySha256'),
                             private('authorization.json'),receipt.get('authorizationFileSha256'))
    path=private('confirmation-aggregate.private.json')
    expected=receipt['filesBeforeFinalReceipt'][path.name]['sha256']; frozen=path.read_bytes()
    require(access.valid_sha(expected) and hashlib.sha256(frozen).hexdigest()==expected,'AGGREGATE_PIN')
    evaluated=auth['freeze']['scores'] if arm=='B' else auth['authorization']['B_retained_scores']
    value=validate_confirmation(json.loads(frozen),auth['freeze'],code,arm,evaluated)
    contract=json.loads(access.regular_path(root,'reports/loop/aggregate-publication-contract.json',public=True).read_text())
    value['attribution']={**contract['source'],'changes':contract['changes'],
       'scope':SCOPES[arm]+'; no ESS endorsement, final validity or release acceptance'}
    require(public_export_preflight(root)==export_gate and runner.checked_preflight(root,arm)==auth and
        rt.code_hashes(root,runner.CODE_PRIVATE)==code and rt.validate_runtime(root)==runtime and
        rt.digest(receipt_path)==receipt_sha and rt.digest(path)==expected,'PRE_COPY_DRIFT')
    dest=root/('reports/phasen/02-b-bestaetigung.json' if arm=='B' else 'reports/phasen/03-full-anwendung.json')
    require(dest.parent.is_dir() and dest.parent.resolve()==dest.parent,'PUBLIC_PATH')
    payload=json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    fd=os.open(dest,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644)
    with os.fdopen(fd,'w') as stream:stream.write(payload)
    return hashlib.sha256(payload.encode()).hexdigest()


def main():
    parser=argparse.ArgumentParser();parser.add_argument('arm',choices=SCOPES);parser.add_argument('label')
    args=parser.parse_args()
    try:print('Fixed confirmation aggregate saved; SHA256 '+export_confirmation(args.arm,args.label))
    except Exception:
        print('CONFIRM_PUBLICATION_REJECTED',file=sys.stderr);return 2
    return 0

if __name__=='__main__':raise SystemExit(main())
