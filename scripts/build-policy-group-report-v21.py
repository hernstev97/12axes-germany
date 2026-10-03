#!/usr/bin/env python3
"""Fixed public-only reproduction; no raw/private source, path lookup or network.

Actual report/decision bytes are authenticated, not inferred from status strings.
This verifies public reproduction, not upstream raw estimation or expert approval.
"""

from hashlib import sha256
import json
import os
from pathlib import Path
import stat
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
OUTPUT = "reports/phasen/03-politikprofil-v21-historische-gruppen.md"
ROOT_DECISION = "reports/loop/policy-group-v21-export-decisions.json"
# All readers use this closed map. No JSON-provided path is ever opened.
INPUT_PINS = {
    "data/reference-groups-v21/README.md": "60ba830a02d4371214c29627f255add74d22d70f8f268d83cbeb6c346500342f",
    "data/reference-groups-v21/ESS5e03_6.json": "343d06f921f5a943e742f304255726302b71162fb55d8c73b73d11f2f184b19a",
    "data/reference-groups-v21/ESS8e02_3.json": "fda4e3dab0546ba25ebb2c265d0d930830615697b023fce2075e41c6a562ff3a",
    "data/reference-groups-v21/ESS9e03_3.json": "a1e7f8b116da9d055ffffb2dc5eb2af04e43524962433a9b032f09cbd8b5d093",
    "data/analysevertrag.v2.entwurf.json": "8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b",
    "data/gruppenvertrag.v2.1.entwurf.json": "9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702",
    "data/politikprofil-v2.fragen.entwurf.json": "5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4",
    "reports/loop/policy-group-v21-export-decisions.json": "544f31f83cac1e258ed13559c04373430a5ac0d792c4380421a32bb623ef42bc",
    "reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1.md": "324a7faad5f7c2bb4d8acb2850073a6ac2bcce9607ef3e38c4bd9e668cf3f496",
    "reports/loop/reviews/GROUP-RESULTS-V21-001-sources-first.md": "1d359b82b828ba085705d0fcb6803d5b84a46a15de9ed24e06512cccdcfed058",
    "reports/loop/reviews/GROUP-RESULTS-V21-001-methods-round1-decision.json": "3c99d784d23f070a77a843bb0848f26b16e4f795f951ce60d70346edf389e53a",
    "reports/loop/reviews/GROUP-RESULTS-V21-001-sources-decision.json": "b13ae786173c280caf7d1c70f2eccc5015d87b3842fb256575f4f5fb2e95f960",
    "reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md": "470c73eb0cb3c2fa6569773035fbe5444507a7c15fd11253b306c7120d07dc7f",
    "pipeline/policy_group_export_v21.py": "d566ccc82ac9909d3ae24aec35ce6eb3e196967b6efb192a487ee8ef999a0b56",
    "pipeline/policy_thematic_report_v2.py": "7436cf96cffbf83d6dfdbedf5a320326b0c702037cc24e36e019264519f353bb",
    "pipeline/policy_report_v2.py": "53d68f23f2bf7c57c95e2bdd55ae0059da4dfe8598bcbd12e2681206a9e4d6ea",
    "pipeline/policy_export_v2.py": "27b225b5975f0c321f08adbfa7ccab4e03dae8421f3987d0e104cf4945d0437a",
    "pipeline/policy_groups_v21.py": "9b680b07385cefc665a54e583cf4b44f03d1305b2829a724fb9afbd7103284b6",
    "pipeline/policy_analysis_v2.py": "d7d23c99b84d352f161ea607f575155594ecd1ff365ad89e8f2624b4f9500309",
    "pipeline/policy_adapter_v2.py": "3159243bc6f536359c896e414e8f418955b51e7504e38f3add62a811b0e5500e",
    "pipeline/policy_reference_v2.py": "bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b",
    "pipeline/policy_group_report_v21.py": "feafd91e862d5d8217936613eccf1b81d9a61a16772f6122823344ba7d8221f1",
    "reports/loop/packages/GROUP-RESULTS-V21-001/v1/manifest.json": "dddbcda2fe8a18f46a45ee812100508d9c3ed10c5cca8c8d391be648e474b13a",
    "reports/loop/packages/GROUP-RESULTS-V21-001/v2/manifest.json": "47aa3e3f3cf6043cc81bf25bf6b1228bc007f4a12c3e2866337d91161f114382"
}


class PublicGroupBuildError(ValueError):
    def __init__(self):
        super().__init__("policy_group_build_error")


def require(condition):
    if not condition:
        raise PublicGroupBuildError() from None


def _duplicates(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value)
        value[key] = item
    return value


def _bad_constant(_):
    raise PublicGroupBuildError() from None


def decode(data):
    return json.loads(data.decode("utf-8"), object_pairs_hook=_duplicates, parse_constant=_bad_constant)


def _parent(path):
    # Paths are already fixed by membership, never accepted from documents.
    descriptor = os.open(ROOT, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in path.split("/")[:-1]:
            following = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = following
        return descriptor
    except Exception:
        os.close(descriptor)
        raise


def _read_fixed(path):
    require(type(path) is str and path in {*INPUT_PINS, OUTPUT})
    parent = _parent(path)
    descriptor = None
    try:
        descriptor = os.open(path.split("/")[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
        require(stat.S_ISREG(os.fstat(descriptor).st_mode))
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = None
            return stream.read()
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent)


def pinned(path):
    require(type(path) is str and path in INPUT_PINS)
    data = _read_fixed(path)
    require(sha256(data).hexdigest() == INPUT_PINS[path])
    return data


def build_bytes():
    # Authenticate complete public inputs and every local runtime dependency
    # before importing the pure renderer. Reviewer prose is only hashed here.
    public = {path: pinned(path) for path in INPUT_PINS}
    root = decode(public[ROOT_DECISION])
    from pipeline.policy_group_report_v21 import render_historical_group_report, REVIEWERS, STUDY_IDS
    analysis = decode(public["data/analysevertrag.v2.entwurf.json"])
    groups = decode(public["data/gruppenvertrag.v2.1.entwurf.json"])
    catalogue = decode(public["data/politikprofil-v2.fragen.entwurf.json"])
    require(analysis["catalog"] == {"path": "data/politikprofil-v2.fragen.entwurf.json", "sha256": INPUT_PINS["data/politikprofil-v2.fragen.entwurf.json"]})
    require(groups["references"]["catalogue"] == analysis["catalog"])
    roles = {}
    for role, info in REVIEWERS.items():
        # These are module constants pinned before import, never JSON paths.
        require(INPUT_PINS[info[0]] == info[1] and INPUT_PINS[info[2]] == info[3])
        roles[role] = decode(public[info[2]])
    require(type(root["publicFiles"]) is list and len(root["publicFiles"]) == 3)
    for info, sid in zip(root["publicFiles"], STUDY_IDS, strict=True):
        fixed_path = "data/reference-groups-v21/" + sid + ".json"
        require(info["path"] == fixed_path and info["sha256"] == INPUT_PINS[fixed_path])
    exports = [decode(public["data/reference-groups-v21/" + sid + ".json"]) for sid in STUDY_IDS]
    rendered = render_historical_group_report(exports, analysis, groups, catalogue, root, roles).encode("utf-8")
    # A concurrent public byte change fails before output creation.
    for path in INPUT_PINS:
        pinned(path)
    return rendered


def _write_output(data):
    parent = _parent(OUTPUT)
    descriptor = None
    try:
        descriptor = os.open(OUTPUT.split("/")[-1], os.O_WRONLY | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK, 0o644, dir_fd=parent)
        require(stat.S_ISREG(os.fstat(descriptor).st_mode))
        os.ftruncate(descriptor, 0)
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = None
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.fsync(parent)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent)


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if args == ["--help"]:
        print("Usage: python scripts/build-policy-group-report-v21.py build | --check | --help")
        print("Fixed public inputs only; --help reads no report inputs. No raw reproduction or publication.")
        return 0
    try:
        require(args in (["build"], ["--check"]))
        rendered = build_bytes()
        if args == ["--check"]:
            require(_read_fixed(OUTPUT) == rendered)
        else:
            _write_output(rendered)
        print("public_group_report_" + ("checked" if args == ["--check"] else "built") + " sha256=" + sha256(rendered).hexdigest())
        return 0
    except Exception:
        print("policy_group_build_error", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
