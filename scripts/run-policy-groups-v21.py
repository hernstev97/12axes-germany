#!/usr/bin/env python3
"""Reproduce three frozen historical group candidates in a fresh local checkout.

Requires the exact locally supplied raw files and public source caches. Existing
private runs are preserved. No public export, old runner or automatic release.
"""

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pipeline.policy_group_access_v21 import AccessPins, PolicyGroupAccessError, run_group_reference

STUDIES = ('ESS5e03_6', 'ESS8e02_3', 'ESS9e03_3')
PINS = AccessPins(
    manifest_sha256='73868d634da6a47fc7e5e72c858a4e93479785b892ffd6de65fda0c4243726a4',
    group_contract_sha256='9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702',
    study_contract_sha256='8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b',
    freeze_sha256='cfeb130f0975c6fab281c3a3eb1f7120f8667458d197f998cb1703211e061c09',
    frozen_commit='c8fe45333c8be0bf9e8cfa84fe160509802e9184',
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', required=True, choices=[*STUDIES, 'all'])
    args = parser.parse_args()
    selected = STUDIES if args.study == 'all' else (args.study,)
    try:
        local = subprocess.run(['git', 'rev-parse', 'analyseplan-v2.1^{}'], cwd=ROOT,
                               text=True, capture_output=True, check=True).stdout.strip()
        remote = subprocess.run(['git', 'ls-remote', 'origin', 'refs/tags/analyseplan-v2.1',
                                 'refs/tags/analyseplan-v2.1^{}'], cwd=ROOT,
                                text=True, capture_output=True, check=True).stdout.splitlines()
        refs = {row.split()[1]: row.split()[0] for row in remote}
        if local != PINS.frozen_commit or refs.get('refs/tags/analyseplan-v2.1^{}') != PINS.frozen_commit:
            raise ValueError('plan_tag_mismatch')
        if any((ROOT / 'data/local/policy-groups-v21' / study / 'run.json').exists()
               for study in selected):
            raise ValueError('existing_private_run_use_fresh_checkout')
        for study in selected:
            print(json.dumps(asdict(run_group_reference(ROOT, study, PINS)), sort_keys=True), flush=True)
        return 0
    except PolicyGroupAccessError as error:
        print(json.dumps({'status': 'failed', 'staticErrorCode': error.code.value}), file=sys.stderr)
    except ValueError as error:
        # The only ValueErrors in this wrapper have fixed messages above.
        print(json.dumps({'status': 'failed', 'staticErrorCode': str(error)}), file=sys.stderr)
    except (OSError, subprocess.SubprocessError, KeyError, IndexError):
        print(json.dumps({'status': 'failed', 'staticErrorCode': 'verification_failed'}), file=sys.stderr)
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
