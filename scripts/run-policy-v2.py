#!/usr/bin/env python3
"""Reproduce frozen historical candidates in a fresh local checkout.

No public statistics/export or old v1 execution. Existing private runs are
preserved: use a separate checkout for reproduction rather than overwrite.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pipeline.policy_access_v2 import AccessPins, PolicyAccessError, STUDIES, run_study_reference

PINS = AccessPins(
    manifest_sha256='c3abae78ae5425aa275ebd137a10c0a7d0c1cbb299828ba1f13d1789ac955f6c',
    contract_sha256='8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b',
    freeze_sha256='a9a38fd5926ed3e83a1e335340991de21e8f25198e7544af42b6ba7382856c7a',
    frozen_commit='6702f187394aed903f04c03cf48b46708c2ff4e4',
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', required=True, choices=[*STUDIES, 'all'])
    args = parser.parse_args()
    selected = list(STUDIES) if args.study == 'all' else [args.study]
    try:
        local = subprocess.run(['git', 'rev-parse', 'analyseplan-v2^{}'], cwd=ROOT,
                               text=True, capture_output=True, check=True).stdout.strip()
        remote = subprocess.run(['git', 'ls-remote', 'origin', 'refs/tags/analyseplan-v2',
                                 'refs/tags/analyseplan-v2^{}'], cwd=ROOT,
                                text=True, capture_output=True, check=True).stdout.splitlines()
        refs = {row.split()[1]: row.split()[0] for row in remote}
        remote_target = refs.get('refs/tags/analyseplan-v2^{}', refs.get('refs/tags/analyseplan-v2'))
        if local != PINS.frozen_commit or remote_target != PINS.frozen_commit:
            raise ValueError('plan_tag_mismatch')
        if any((ROOT / 'data/local/policy-v2' / study / 'run.json').exists() for study in selected):
            raise ValueError('existing_private_run_use_fresh_checkout')
        for study in selected:
            receipt = run_study_reference(ROOT, study, PINS)
            print(json.dumps(asdict(receipt), sort_keys=True), flush=True)
        return 0
    except PolicyAccessError as error:
        print(json.dumps({'status': 'failed', 'staticErrorCode': error.code.value}), file=sys.stderr)
        return 1
    except ValueError as error:
        # Only fixed messages from this wrapper; never parser/response text.
        print(json.dumps({'status': 'failed', 'staticErrorCode': str(error)}), file=sys.stderr)
        return 1
    except (OSError, subprocess.SubprocessError, KeyError, IndexError):
        print(json.dumps({'status': 'failed', 'staticErrorCode': 'verification_failed'}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
