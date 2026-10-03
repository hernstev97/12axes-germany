#!/usr/bin/env python3
"""Fixed public-only local reproduction; no raw/private paths or network.

This guard authenticates published bytes against the bound Root decision.
It cannot authenticate privileged intent or independently reproduce upstream
private estimates. The output stays WIP pending presentation review.
"""

from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

MANIFEST = "reports/loop/packages/RESULTS-V2-001/v1/manifest.json"
MANIFEST_HASH = "3299ad658cca7cbb5621c6f062d4133b831e74d8bf4ca71bcb8e67fff56c4434"
DECISION = "reports/loop/policy-v2-export-decisions.json"
DECISION_HASH = "a87f780a7219253f7f3773d051b7001f438b19b2fb2d0ee820fc22c1157a16df"
OUTPUT = "reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md"
REVIEWERS = {
    "methods_reproducibility": (
        "reports/loop/reviews/RESULTS-V2-001-methods-first.md",
        "1bb14ba2dba3d57612d66c5a50c29ce049606e8fddb062ff6b616f56b60462ee",
        "reports/loop/reviews/RESULTS-V2-001-methods-decision.json",
        "765db3005c736174a3d1f9819ab212917ce50d6143059b8cfce2dac3f6f67806",
    ),
    "sources_constructs_fairness": (
        "reports/loop/reviews/RESULTS-V2-001-sources-first.md",
        "7a2814359b94ab3a73dd22a090b2a10c6b51db6cc243d8586e8ae15bfdc580e8",
        "reports/loop/reviews/RESULTS-V2-001-sources-decision.json",
        "e5c3a730dc6cf71e5b788d4251c109b86a7d510684bf945b17ceaa6e48306065",
    ),
}
# Only these manifest entries are read. All privateAggregates and the other
# upstream gate/receipt references remain metadata; no traversal/stat/read.
PUBLIC_MANIFEST_PATHS = (
    "data/analysevertrag.v2.entwurf.json", "data/politikprofil-v2.fragen.entwurf.json",
    "docs/empirie-plan-v2.entwurf.md", "docs/abdeckung-v2.md", "docs/messformen-v2.entwurf.md",
    "docs/lizenzen.md", "docs/quellen.json", "docs/belegregister.md",
    "pipeline/policy_reference_v2.py", "pipeline/policy_adapter_v2.py",
    "pipeline/policy_analysis_v2.py", "pipeline/policy_export_v2.py", "pipeline/policy_report_v2.py",
)
SOURCE_PREFIXES = (
    "outputs/loop/breadth-data-001/sources/",
    "outputs/loop/breadth-access-002/sources/",
    "outputs/loop/breadth-binding-003/sources/",
)


class PublicBuildError(ValueError):
    def __init__(self):
        super().__init__("policy_thematic_build_error")


def require(condition):
    if not condition:
        raise PublicBuildError() from None


def _duplicates(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value)
        value[key] = item
    return value


def _bad_constant(_):
    raise PublicBuildError() from None


def decode(data):
    return json.loads(data.decode("utf-8"), object_pairs_hook=_duplicates, parse_constant=_bad_constant)


def pinned(path, expected):
    # Every caller establishes an exact metadata path or the pinned public
    # catalogue source prefix before entering this function.
    require(type(path) is str and not PurePosixPath(path).is_absolute()
            and ".." not in PurePosixPath(path).parts)
    target = ROOT / path
    # Reject symlinks in the allowlisted public path before resolution/read.
    # There is no attempt to stat or follow a private target.
    require(not any((ROOT.joinpath(*PurePosixPath(path).parts[:n])).is_symlink()
                    for n in range(1, len(PurePosixPath(path).parts) + 1)))
    data = target.read_bytes()
    require(sha256(data).hexdigest() == expected)
    return data


def build_bytes():
    manifest = decode(pinned(MANIFEST, MANIFEST_HASH))
    decision = decode(pinned(DECISION, DECISION_HASH))
    require(manifest["package"] == "RESULTS-V2-001/v1" and manifest["rawAccessAllowed"] is False)
    artifacts = {a["path"]: a["sha256"] for a in manifest["publicArtifacts"]}
    require(len(artifacts) == len(manifest["publicArtifacts"]))
    public_bytes = {p: pinned(p, artifacts[p]) for p in PUBLIC_MANIFEST_PATHS}
    # Authenticate the unchanged libraries before importing/executing them.
    from pipeline.policy_export_v2 import _canonical_hash
    from pipeline.policy_report_v2 import _VARIABLES
    from pipeline.policy_thematic_report_v2 import render_thematic_report
    require(decision["schemaVersion"] == 1
            and decision["decision"] == "ALLOW_REVIEWED_HISTORICAL_REFERENCE_V2"
            and decision["rootReadBothCompleteFirstReports"] is True
            and decision["actualManifestAnd29Public5PrivateBytesVerified"] is True
            and decision["withheldIds"] == ["ESS10SCe03_2:cttresa"])
    analysis = decode(public_bytes["data/analysevertrag.v2.entwurf.json"])
    catalogue = decode(public_bytes["data/politikprofil-v2.fragen.entwurf.json"])
    require(analysis["catalog"] == {"path": "data/politikprofil-v2.fragen.entwurf.json",
                                   "sha256": artifacts["data/politikprofil-v2.fragen.entwurf.json"]})
    for source in catalogue["sources"]:
        path = source["cachedPath"]
        require(type(path) is str and any(path.startswith(prefix) for prefix in SOURCE_PREFIXES)
                and PurePosixPath(path).suffix in {".pdf", ".json", ".html"})
        pinned(path, source["originalBytesSha256"])
    review_decisions = {}
    for role, (report_path, report_hash, decision_path, decision_hash) in REVIEWERS.items():
        pinned(report_path, report_hash)
        role_decision = decode(pinned(decision_path, decision_hash))
        require(set(role_decision) == {"schemaVersion", "role", "reviewManifestSha256", "decision", "studies"}
                and role_decision["schemaVersion"] == 1 and role_decision["role"] == role
                and role_decision["reviewManifestSha256"] == MANIFEST_HASH
                and role_decision["decision"] == "ACCEPTED_BOUNDED")
        mapped = {s["studyId"]: s for s in role_decision["studies"]}
        require(len(mapped) == len(role_decision["studies"]) == 5 and set(mapped) == set(_VARIABLES))
        review_decisions[role] = mapped
    studies = {s["study_id"]: s for s in analysis["studies"]}
    study_decisions = {s["studyId"]: s for s in decision["studyDecisions"]}
    files = {f["studyId"]: f for f in decision["publicFiles"]}
    require(len(studies) == len(study_decisions) == len(files) == 5
            and len(decision["studyDecisions"]) == len(decision["publicFiles"]) == 5
            and set(studies) == set(study_decisions) == set(files) == set(_VARIABLES))
    exports, reviewed = [], 0
    for identity in _VARIABLES:
        item, study, info = study_decisions[identity], studies[identity], files[identity]
        require(info["path"] == "data/reference-v2/" + identity + ".json")
        export = decode(pinned(info["path"], info["sha256"]))
        require(item["schemaVersion"] == 1 and item["decision"] == "ALLOW_REVIEWED_HISTORICAL_REFERENCE_V2"
                and item["edition"] == study["edition"] == export["edition"]
                and item["studyId"] == export["studyId"] == identity
                and item["sourceContractSha256"] == export["sourceContractSha256"] == _canonical_hash(study)
                and item["candidateSha256"] == export["candidateSha256"]
                and item["reviewManifestSha256"] == export["reviewManifestSha256"] == MANIFEST_HASH)
        approved = [q["id"] for q in export["questions"] if q["status"] == "reviewed_historical_reference"]
        expected = [q["question_id"] for q in study["adapter"]["questions"]
                    if q["question_id"] != "ESS10SCe03_2:cttresa"]
        require(approved == item["approvedQuestionIds"] == expected
                and info["reviewedReferenceCount"] == len(approved)
                and info["questionInventoryCount"] == len(export["questions"]))
        reviewer_map = {r["role"]: r for r in item["reviewers"]}
        require(len(reviewer_map) == len(item["reviewers"]) == 2 and set(reviewer_map) == set(REVIEWERS))
        for role, (report_path, report_hash, _, _) in REVIEWERS.items():
            require(reviewer_map[role] == {"role": role, "reportPath": report_path, "sha256": report_hash,
                                          "decision": "ACCEPTED_BOUNDED"})
            role_item = review_decisions[role][identity]
            require(set(role_item) == {"studyId", "candidateSha256", "approvedQuestionIds"}
                    and role_item["candidateSha256"] == item["candidateSha256"]
                    and role_item["approvedQuestionIds"] == approved)
        exports.append(export)
        reviewed += len(approved)
    require(reviewed == 42 and sum(len(s["adapter"]["questions"]) for s in studies.values()) == 43)
    rendered = render_thematic_report(exports, analysis, catalogue).encode("utf-8")
    # Fail on concurrent drift in all public dependencies; private metadata is
    # never used as a path to a file. No upstream claims are newly authenticated.
    pinned(MANIFEST, MANIFEST_HASH)
    pinned(DECISION, DECISION_HASH)
    for path in PUBLIC_MANIFEST_PATHS:
        pinned(path, artifacts[path])
    for source in catalogue["sources"]:
        pinned(source["cachedPath"], source["originalBytesSha256"])
    for _, (report_path, report_hash, decision_path, decision_hash) in REVIEWERS.items():
        pinned(report_path, report_hash)
        pinned(decision_path, decision_hash)
    for info in files.values():
        pinned(info["path"], info["sha256"])
    return rendered


def main():
    try:
        require(sys.argv[1:] in ([], ["--check"]))
        rendered = build_bytes()
        if sys.argv[1:]:
            require((ROOT / OUTPUT).read_bytes() == rendered)
        else:
            (ROOT / OUTPUT).write_bytes(rendered)
        print("Public thematic WIP report reproduced; SHA256 " + sha256(rendered).hexdigest())
        return 0
    except Exception:
        print("policy_thematic_build_error", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
