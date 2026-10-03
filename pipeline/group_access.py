"""Post-B/FULL group selection; only eight predeclared source fields.

Pure helpers never open files. Real preparation requires a public normal-review
receipt and the completed fixed FULL path before any protected source read.
No identifiers, vote substitutes, current-party claims or row output to stdout.
"""
from __future__ import annotations
import argparse
from decimal import Decimal
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
from pipeline import empirical_access as original
from pipeline import stage_access as stage
from pipeline import confirm_runtime as confirm
from pipeline import r_runtime as rt
ROOT=Path(__file__).resolve().parents[1]
CONTRACT='data/group-source-contract.v1.entwurf.json'
GATE='reports/loop/gates/pre-groups.json'
INPUT=stage.PRIVATE+'/GROUPS.csv'
RECEIPT=stage.PRIVATE+'/group-input-receipt.json'
FIELDS=('agea','gndr','eisced','regunit','region','lrscale','vote','prtvgde2')
FAMILIES=('age','survey_sex','education','regionalEastWest','lr_approx_weighted_thirds',
          'vote_participation','historical_second_vote')


def require(value,code):
    if not value:raise ValueError(code)


def thirds(values,weights):
    """Fixed objective; exact decimal-weight fractions preserve exact ties."""
    require(len(values)==len(weights),'LR_LENGTH')
    mass=[Fraction(0)]*11
    for value,weight in zip(values,weights,strict=True):
        if value is not None:
            require(type(value) is int and 0<=value<=10,'LR_CATEGORY')
            w=Fraction(weight);require(w>0,'LR_WEIGHT');mass[value]+=w
    total=sum(mass)
    if total<=0:return None
    cum=[];running=Fraction(0)
    for x in mass:running+=x;cum.append(running)
    choices=[]
    for a in range(10):
        for b in range(a+1,10):
            if cum[a]>0 and cum[b]>cum[a] and total>cum[b]:
                loss=(cum[a]/total-Fraction(1,3))**2+(cum[b]/total-Fraction(2,3))**2
                choices.append((loss,a,b))
    if not choices:return None
    loss,a,b=min(choices)
    return {'a':a,'b':b,'objective':float(loss),'tieRule':'Exact rational objective, lexicographic(a,b)',
            'reference':'All valid DE lrscale before nine-item completeness'}


def token(value):
    value=value.strip()
    return None if value in original.LEXICAL_MISSING else value


def number(value,missing,valid=None):
    value=token(value)
    if value is None:return None
    n=original.integer(value)
    if n in missing:return None
    require(valid is None or n in valid,'UNEXPECTED_GROUP_CODE')
    return n


def group_frame(frozen,contract,core,expected_sha=original.SHA):
    require(set(FIELDS).issubset(contract['fields']),'SOURCE_CONTRACT_FIELDS')
    header,rows=original.table(frozen,expected_sha)
    require(set(FIELDS).issubset(header),'SOURCE_FIELDS')
    positions={name:header.index(name) for name in FIELDS}
    selected=[];weights=[]
    for row in rows:
        meta=original.metadata(header,row)
        if meta['cntry']=='DE':
            selected.append({name:row[positions[name]] for name in FIELDS})
            weights.append(Decimal(row[header.index('anweight')].strip()))
    n=len(selected);columns={f:[None]*n for f in FAMILIES};diagnostics={};levels={}
    groups=contract['groups']
    for family in FAMILIES:
        try:
            if family=='age':
                levels[family]=[b['id'] for b in groups['age']['candidate_bins']]
                for i,row in enumerate(selected):
                    age=number(row['agea'],{999})
                    if age is not None:
                        require(age>=15,'AGE_BELOW_TARGET')
                        columns[family][i]=next(b['id'] for b in groups['age']['candidate_bins']
                            if age>=b['inclusive_min'] and (b['inclusive_max'] is None or age<=b['inclusive_max']))
            elif family in ('survey_sex','education','regionalEastWest'):
                definition=groups[family];levels[family]=[g['id'] for g in definition['groups']]
                cross={value:g['id'] for g in definition['groups'] for value in g['values']}
                field=definition['variable'];missing=set(definition['excluded_missing_codes'])
                unclassified=set(definition.get('excluded_substantive_unclassifiable_codes',[]))
                for i,row in enumerate(selected):
                    value=token(row[field])
                    if family!='regionalEastWest' and value is not None:
                        value=str(original.integer(value))
                    if value is None or value in missing or value in unclassified:continue
                    if family=='regionalEastWest':require(number(row['regunit'],set(),{1,2,3,4})==1,'REGIONAL_LEVEL')
                    require(value in cross,'UNEXPECTED_GROUP_CODE');columns[family][i]=cross[value]
            elif family=='lr_approx_weighted_thirds':
                levels[family]=['lower_lr','middle_lr','upper_lr']
                values=[number(row['lrscale'],{77,88,99},set(range(11))) for row in selected]
                cuts=thirds(values,weights);require(cuts is not None,'NO_FEASIBLE_LR_CUTS')
                for i,v in enumerate(values):
                    if v is not None:columns[family][i]=levels[family][0 if v<=cuts['a'] else 1 if v<=cuts['b'] else 2]
                diagnostics[family]={'cutpoints':cuts}
            elif family=='vote_participation':
                levels[family]=['voted','did_not_vote','not_eligible']
                for i,row in enumerate(selected):
                    vote=number(row['vote'],{7,8,9},{1,2,3})
                    if vote is not None:columns[family][i]=levels[family][vote-1]
            else:
                definition=groups[family];valid=set(definition['valid_values'])
                levels[family]=['party_'+code for code in definition['valid_values']]
                missing=set(definition['excluded_missing_codes'])
                for i,row in enumerate(selected):
                    vote=number(row['vote'],{7,8,9},{1,2,3});party=token(row['prtvgde2'])
                    if party is not None:party=str(original.integer(party))
                    if party is None or party in missing:continue
                    require(party in valid,'UNEXPECTED_GROUP_CODE')
                    require(vote==1,'VOTE_FILTER_INCONSISTENCY');columns[family][i]='party_'+party
            diagnostics[family]={**diagnostics.get(family,{}),'status':'EXECUTED',
                'valid_count':sum(v is not None for v in columns[family]),
                'scope':'Historical reported groups; no latent comparability or current electorate claim'}
        except (ValueError,StopIteration):
            columns[family]=[None]*n
            diagnostics[family]={'status':'UNSUPPORTED','code':'GROUP_INPUT_'+family.upper(),
                'scope':'Entire affected grouping withheld; no guessed category, party or cutpoint'}
    output=[[columns[f][i] if columns[f][i] is not None else 'NA' for f in FAMILIES] for i in range(n)]
    full_header,full_rows,psp=stage.full_frame(frozen,core,expected_sha)
    return list(FAMILIES),output,levels,diagnostics,stage._csv_payload(full_header,full_rows)


def public_preflight(root=ROOT):
    path=stage.regular_path(root,GATE,public=True);frozen=path.read_bytes();gate=json.loads(frozen)
    require(gate.get('decision')=='ACCEPTED_BOUNDED' and gate.get('schema')=='life93-pre-groups-1','GROUP_GATE')
    review=gate.get('review',{});require(review.get('scope')=='groups-methods-repro' and bool(review.get('reviewer')),'GROUP_REVIEW')
    pins={}
    for entry in [review,*gate.get('artifacts',[])]:
        p=entry.get('path');expected=entry.get('sha256');require(stage.valid_sha(expected) and p not in pins,'GROUP_PIN')
        pins[p]=rt.digest(stage.regular_path(root,p,public=True));require(pins[p]==expected,'GROUP_PIN')
    code=gate.get('reviewedCodeHashes',{})
    require(isinstance(code,dict) and set(confirm.CODE_PRIVATE).union({'pipeline/group_access.py',CONTRACT}).issubset(code),'GROUP_CODE_SET')
    for p,h in code.items():require(pins.get(p)==h and rt.digest(stage.regular_path(root,p,public=True))==h,'GROUP_CODE_PIN')
    require('reports/phasen/03-full-anwendung.json' in pins and 'reports/loop/full-runtime-public.json' in pins,'FULL_PUBLIC_PIN')
    result=json.loads(stage.regular_path(root,'reports/phasen/03-full-anwendung.json',public=True).read_text())
    require(result.get('schema')=='life93-fixed-model-confirmation-aggregate-1' and
        result.get('arm')=='FULL' and result.get('model',{}).get('eligible') is True and
        result.get('confirmation',{}).get('global_model_passed') is True and
        result.get('confirmation',{}).get('status')=='CRITERIA_PASSED_PENDING_RESULT_REVIEW' and
        isinstance(result.get('confirmation',{}).get('retained_scores'),list) and
        len(result['confirmation']['retained_scores'])>=2,'FULL_PROFILE_CRITERIA')
    public=stage.public_preflight(root,'FULL')
    require(result.get('freeze')==public['freeze'] and result.get('model_name')==public['freeze']['model']
        and set(result['confirmation']['retained_scores']).issubset(public['B_retained_scores']),'FULL_SCORE_BINDING')
    return {'gateSha256':hashlib.sha256(frozen).hexdigest(),'pins':pins,'codeHashes':code,'fullPublic':public}


def prepare(root=ROOT):
    authorization=public_preflight(root)  # No private read before new source/code review.
    full=confirm.checked_preflight(root,'FULL');folder=root/stage.PRIVATE
    for p in (folder,root/'data/local'):require(p.is_dir() and p.resolve()==p and p.stat().st_mode&0o777==0o700,'PRIVATE_MODE')
    for p in (root/INPUT,root/RECEIPT):require(not p.exists() and not p.is_symlink(),'DO_NOT_OVERWRITE')
    source=root/stage.SOURCE;require(source.resolve().is_file(),'SOURCE_FILE')
    frozen=source.read_bytes();require(hashlib.sha256(frozen).hexdigest()==original.SHA,'SOURCE_PIN')
    contract=json.loads(stage.regular_path(root,CONTRACT,public=True).read_text())
    core=json.loads(stage.regular_path(root,'data/item-core-v1.json',public=True).read_text())
    header,rows,levels,diagnostics,full_bytes=group_frame(frozen,contract,core)
    require(hashlib.sha256(full_bytes).hexdigest()==full['privatehashes']['fullSha256'],'FULL_ORDER_ORIGIN')
    require(public_preflight(root)==authorization and confirm.checked_preflight(root,'FULL')==full,'PRE_WRITE_DRIFT')
    payload=stage._csv_payload(header,rows)
    rt.exclusive_text(root/INPUT,payload.decode())
    record={'schema':'life93-group-input-1','authorization':authorization,'fullAuthorization':full,
      'input':{'path':INPUT,'sha256':hashlib.sha256(payload).hexdigest()},'sourceSha256':original.SHA,
      'levels':levels,'diagnostics':diagnostics,'rowCount':len(rows),
      'limits':'Private aligned group columns; no IDs. Shared-FS receipts mutable; no race/read isolation guarantee'}
    rt.save_json(root/RECEIPT,record)
    print('GROUP_INPUT_PRIVATE_SAVED')


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:prepare()
    except Exception:print('GROUP_INPUT_OR_GATE_REJECTED',file=sys.stderr);return 2
    return 0
if __name__=='__main__':raise SystemExit(main())
