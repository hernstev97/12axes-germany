#!/usr/bin/env python3
"""Fetch public ESS variable metadata (codelists) for named variables.

Reads only public file metadata caches to resolve variable IDs and queries the
public ESS GraphQL API (no login). Never opens response data. Writes the raw
API response and a fetch receipt under outputs/claude/sources/.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
API = 'https://api.nsd.no/graphql'
FILE_METADATA = {
    'ESS5e03_6': 'outputs/loop/breadth-access-002/sources/ess5-file-metadata.json',
    'ESS8e02_3': 'outputs/loop/breadth-access-002/sources/ess8-file-metadata.json',
    'ESS9e03_3': 'outputs/loop/breadth-access-002/sources/ess9-file-metadata.json',
    'ESS10SCe03_2': 'outputs/loop/breadth-access-002/sources/ess10sc-file-metadata.json',
    'ESS11e04_2': 'outputs/loop/breadth-binding-003/sources/ess11-file-variable-catalogue.json',
}
FIELDS = ('id version name { en } label { en } dataType measurementLevel isWeight '
          'literalQuestion { en } preQuestion { en } postQuestion { en } filter { en } '
          'fullCodeList { value label { en } isMissing }')


def resolve(study: str, names: list[str]) -> list[dict]:
    data = json.loads((ROOT / FILE_METADATA[study]).read_text())
    variables = data['data']['search']['dataFileMetadata']['variableList']
    by_name = {v['name']['en']: v for v in variables}
    missing = [n for n in names if n not in by_name]
    if missing:
        raise SystemExit(f'unknown variables for {study}: {missing}')
    return [by_name[n] for n in names]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', required=True, choices=sorted(FILE_METADATA))
    parser.add_argument('--out', required=True, help='file stem under outputs/claude/sources/')
    parser.add_argument('variables', nargs='+')
    args = parser.parse_args()
    entries = resolve(args.study, args.variables)
    parts = [
        f'v{i}: variableMetadata(id: "{e["id"]}", version: {e["version"]}, instance: PUBLISHED, '
        f'agencyId: INT_ESSERIC) {{ {FIELDS} }}'
        for i, e in enumerate(entries)
    ]
    query = 'query { search { ' + ' '.join(parts) + ' } }'
    body = json.dumps({'query': query}).encode()
    request = urllib.request.Request(API, data=body, headers={
        'Content-Type': 'application/json',
        'User-Agent': '12axes-germany research prototype (LIFE-93, public metadata only)',
    })
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read()
        status = response.status
    out_dir = ROOT / 'outputs/claude/sources'
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f'{args.out}.request.json').write_bytes(body)
    (out_dir / f'{args.out}.json').write_bytes(payload)
    receipt = {
        'method': 'POST', 'url': API, 'utc': started, 'http': status,
        'study': args.study, 'variables': args.variables, 'bytes': len(payload),
        'sha256': hashlib.sha256(payload).hexdigest(),
        'requestSha256': hashlib.sha256(body).hexdigest(),
        'path': f'outputs/claude/sources/{args.out}.json',
        'scope': 'public variable metadata only, no response values or auth',
    }
    with (out_dir / 'fetches.jsonl').open('a') as log:
        log.write(json.dumps(receipt, sort_keys=True) + '\n')
    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
