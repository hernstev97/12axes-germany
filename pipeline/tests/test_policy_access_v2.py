"""Synthetic-only gate/hash/CSV/persistence boundary tests for the v2 runner."""

import copy
import csv
from dataclasses import asdict, replace
import hashlib
from io import StringIO
import json
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch

from pipeline import policy_access_v2 as access


PROJECT = Path(__file__).resolve().parents[2]
FIXTURE_PARENT = PROJECT / "outputs/loop/policy-access-v2/fixtures"


def sha(blob):
    return hashlib.sha256(blob).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


class SyntheticPackage:
    def __init__(self, root):
        self.root = root
        # Public source-contract/catalog bytes are allowed input. Their real raw
        # paths/hashes are never dereferenced: every input is replaced below.
        self.contract = json.loads((PROJECT / access.CONTRACT_PATH).read_text())
        self.catalog = json.loads((PROJECT / access.CATALOG_PATH).read_text())
        for relative in access.CORE_ARTIFACTS - {access.CONTRACT_PATH, access.CATALOG_PATH}:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((PROJECT / relative).read_bytes())
        self.extra = "docs/synthetic-pin.md"
        (root / self.extra).parent.mkdir(parents=True, exist_ok=True)
        (root / self.extra).write_text("Synthetic package pin.\n")
        self.reports = ["reports/loop/reviews/synthetic-methods.md", "reports/loop/reviews/synthetic-sources.md"]
        for relative in self.reports:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Synthetic bounded-decision fixture; no scientific review.\n")
        for study in self.contract["studies"]:
            self.set_csv(study["study_id"])
        self.resign()

    def study(self, identity):
        return next(s for s in self.contract["studies"] if s["study_id"] == identity)

    def set_csv(self, identity, *, response=None, round_value=None, edition_value=None,
                duplicate_id=False, empty=False, unrelated="SYNTHETIC-UNSELECTED-PAYLOAD"):
        study = self.study(identity)
        questions = study["adapter"]["questions"]
        header = ["cntry", "idno", "essround", "edition", "pspwght", "dweight", "anweight", *[q["variable"] for q in questions], "unused"]
        output = StringIO(newline="")
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(header)
        for n in range(100):
            values = [q["categoryCodes"][0] for q in questions]
            if response is not None:
                values[0] = response
            if empty:
                values[0] = ""
            writer.writerow(["DE", "SYNTHETIC-PERSON-" + str(0 if duplicate_id else n),
                             round_value or str(study["round"]), edition_value or study["edition"],
                             "1", "1", "1", *values, unrelated])
        # Non-DE contents, including metadata/answers, remain uninterpreted.
        writer.writerow(["FR", "SYNTHETIC-NONDE", "not-a-round", "not-an-edition", "bad", "bad", "bad",
                         *["uninterpreted" for _ in questions], unrelated])
        blob = output.getvalue().encode("utf-8")
        path = self.root / study["input"]["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(blob)
        study["input"]["sha256"] = sha(blob)
        study["input"]["bytes"] = len(blob)

    def resign(self):
        write_json(self.root / access.CATALOG_PATH, self.catalog)
        self.contract["catalog"] = {"path": access.CATALOG_PATH, "sha256": sha((self.root / access.CATALOG_PATH).read_bytes())}
        write_json(self.root / access.CONTRACT_PATH, self.contract)
        artifact_paths = sorted(access.CORE_ARTIFACTS | {self.extra})
        manifest = {"schemaVersion": 1, "package": access.PACKAGE,
                    "artifacts": [{"path": p, "sha256": sha((self.root / p).read_bytes())} for p in artifact_paths]}
        write_json(self.root / access.MANIFEST_PATH, manifest)
        manifest_sha = sha((self.root / access.MANIFEST_PATH).read_bytes())
        contract_sha = sha((self.root / access.CONTRACT_PATH).read_bytes())
        freeze = {"schemaVersion": 1, "package": access.PACKAGE, "frozenCommit": "a" * 40,
                  "planTag": access.PLAN_TAG, "reviewedManifestSha256": manifest_sha,
                  "contractSha256": contract_sha}
        write_json(self.root / access.FREEZE_PATH, freeze)
        self.pins = access.AccessPins(manifest_sha, contract_sha, sha((self.root / access.FREEZE_PATH).read_bytes()), "a" * 40)
        self.gate = {"schemaVersion": 1, "package": access.PACKAGE, "decision": "ALLOW_HISTORICAL_DESCRIPTIVE_V2",
                     "reviewedManifestSha256": manifest_sha, "frozenCommit": "a" * 40, "planTag": access.PLAN_TAG,
                     "reviewers": [{"role": role, "reportPath": p, "sha256": sha((self.root / p).read_bytes()),
                                    "decision": "ACCEPTED_BOUNDED"}
                                   for role, p in zip(sorted(access.REVIEW_ROLES), self.reports)]}
        write_json(self.root / access.GATE_PATH, self.gate)

    def gate_write(self):
        write_json(self.root / access.GATE_PATH, self.gate)

    def run(self, identity="ESS9e03_3"):
        return access.run_study_reference(self.root, identity, self.pins)

    def private(self, identity="ESS9e03_3"):
        return json.loads((self.root / f"data/local/policy-v2/{identity}/run.json").read_text())


class PolicyAccessTests(unittest.TestCase):
    def setUp(self):
        FIXTURE_PARENT.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=FIXTURE_PARENT, prefix="synthetic-")
        self.fixture = SyntheticPackage(Path(self.temp.name))

    def tearDown(self):
        self.temp.cleanup()

    def no_raw_failure(self, *, pins=None):
        original = access._read_repo_bytes
        raw_reads = []
        def guarded(root, relative):
            if relative.startswith("data/raw/"):
                raw_reads.append(relative)
                raise AssertionError("Synthetic raw I/O occurred before rejection")
            return original(root, relative)
        with patch.object(access, "_read_repo_bytes", side_effect=guarded):
            with self.assertRaises(access.PolicyAccessError) as caught:
                access.run_study_reference(self.fixture.root, "ESS9e03_3", pins or self.fixture.pins)
        self.assertEqual(raw_reads, [])
        self.assertRegex(str(caught.exception), r"^policy_access_error: [a-z_]+$")
        self.assertFalse((self.fixture.root / "data/local").exists())

    def test_only_exact_positive_gate(self):
        baseline = copy.deepcopy(self.fixture.gate)
        for bad in [True, "ALLOW", "allowed", "ACCEPTED_BOUNDED", "reviewed_historical_reference", None, []]:
            with self.subTest(kind=type(bad).__name__):
                self.fixture.gate = copy.deepcopy(baseline)
                self.fixture.gate["decision"] = bad
                self.fixture.gate_write()
                self.no_raw_failure()
        self.fixture.gate = copy.deepcopy(baseline)
        self.fixture.gate["schemaVersion"] = True
        self.fixture.gate_write(); self.no_raw_failure()

    def test_old_gate_is_not_consulted(self):
        old = self.fixture.root / "reports/loop/gates/pre-empirical.json"
        write_json(old, self.fixture.gate)
        (self.fixture.root / access.GATE_PATH).unlink()
        self.no_raw_failure()

    def test_review_roles_paths_decisions_and_hashes(self):
        baseline = copy.deepcopy(self.fixture.gate)
        variants = [
            lambda g: g["reviewers"][1].update(role=g["reviewers"][0]["role"]),
            lambda g: g["reviewers"][1].update(reportPath=g["reviewers"][0]["reportPath"]),
            lambda g: g["reviewers"][0].update(decision="ACCEPTED"),
            lambda g: g["reviewers"][0].update(sha256="0" * 64),
            lambda g: g["reviewers"][0].update(reportPath="reports/loop/authors/other.md"),
            lambda g: g["reviewers"][0].update(reportPath="reports/loop/reviews/../../state.md"),
        ]
        for change in variants:
            self.fixture.gate = copy.deepcopy(baseline); change(self.fixture.gate)
            self.fixture.gate_write(); self.no_raw_failure()

    def test_empty_review_file_is_not_positive_evidence(self):
        p = self.fixture.root / self.fixture.reports[0]
        p.write_bytes(b"")
        self.fixture.gate["reviewers"][0]["sha256"] = sha(b"")
        self.fixture.gate_write(); self.no_raw_failure()

    def test_pin_changes_stop_before_raw(self):
        for key in ["manifest_sha256", "contract_sha256", "freeze_sha256", "frozen_commit", "plan_tag"]:
            value = "0" * 40 if key == "frozen_commit" else "wrong-tag" if key == "plan_tag" else "0" * 64
            with self.subTest(pin=key):
                self.no_raw_failure(pins=replace(self.fixture.pins, **{key: value}))

    def test_all_artifacts_are_verified(self):
        (self.fixture.root / self.fixture.extra).write_text("Changed synthetic public artifact.\n")
        self.no_raw_failure()

    def test_duplicate_manifest_artifact_is_rejected(self):
        p = self.fixture.root / access.MANIFEST_PATH
        manifest = json.loads(p.read_text()); manifest["artifacts"].append(copy.deepcopy(manifest["artifacts"][0]))
        write_json(p, manifest)
        self.fixture.pins = replace(self.fixture.pins, manifest_sha256=sha(p.read_bytes()))
        self.fixture.gate["reviewedManifestSha256"] = self.fixture.pins.manifest_sha256
        freeze = json.loads((self.fixture.root / access.FREEZE_PATH).read_text())
        freeze["reviewedManifestSha256"] = self.fixture.pins.manifest_sha256
        write_json(self.fixture.root / access.FREEZE_PATH, freeze)
        self.fixture.pins = replace(self.fixture.pins, freeze_sha256=sha((self.fixture.root / access.FREEZE_PATH).read_bytes()))
        self.fixture.gate_write(); self.no_raw_failure()

    def test_wrong_study_path_and_catalog_identity_fail(self):
        original = self.fixture.study("ESS9e03_3")["input"]["path"]
        self.fixture.study("ESS9e03_3")["input"]["path"] = "data/raw/ess8-ed2.3/ESS8e02_3.csv"
        self.fixture.resign(); self.no_raw_failure()
        self.fixture.study("ESS9e03_3")["input"]["path"] = original
        self.fixture.catalog["studies"][0]["fileMetadataId"] = "false-public-source-identity"
        self.fixture.resign(); self.no_raw_failure()

    def test_duplicate_study_question_and_adapter_extra_fail(self):
        baseline = copy.deepcopy(self.fixture.contract)
        self.fixture.contract["studies"].append(copy.deepcopy(self.fixture.contract["studies"][0]))
        self.fixture.resign(); self.no_raw_failure()
        self.fixture.contract = copy.deepcopy(baseline)
        q = self.fixture.study("ESS9e03_3")["adapter"]["questions"]
        q.append(copy.deepcopy(q[0])); self.fixture.resign(); self.no_raw_failure()
        self.fixture.contract = copy.deepcopy(baseline)
        self.fixture.study("ESS9e03_3")["adapter"]["freeInterpretation"] = True
        self.fixture.resign(); self.no_raw_failure()

    def test_numeric_rules_are_required_before_raw(self):
        for key in ["metadata", "responseSerialization"]:
            baseline = copy.deepcopy(self.fixture.contract)
            field = "normalizationRule" if key == "metadata" else "rule"
            self.fixture.study("ESS9e03_3")[key][field] = "guess-from-file"
            self.fixture.resign(); self.no_raw_failure()
            self.fixture.contract = baseline

    def test_fixed_evidence_differs_for_known_ess11_and_new_files(self):
        for identity, wrong in [("ESS5e03_6", "historical_v1_identity_plus_gated_metadata_check"),
                                ("ESS11e04_2", "user_file_label_plus_gated_metadata_check")]:
            study = self.fixture.study(identity); before = study["input"]["editionEvidence"]
            study["input"]["editionEvidence"] = wrong
            self.fixture.resign(); self.no_raw_failure()
            study["input"]["editionEvidence"] = before

    def test_extra_gate_fields_and_duplicate_json_keys_fail_closed(self):
        self.fixture.gate["allowAnything"] = True
        self.fixture.gate_write(); self.no_raw_failure()
        self.fixture.gate.pop("allowAnything")
        blob = json.dumps(self.fixture.gate)
        blob = '{"schemaVersion":1,' + blob[1:]
        (self.fixture.root / access.GATE_PATH).write_text(blob)
        self.no_raw_failure()

    def test_manifest_cannot_hash_raw_as_a_public_artifact(self):
        path = self.fixture.root / access.MANIFEST_PATH
        manifest = json.loads(path.read_text())
        study = self.fixture.study("ESS9e03_3")
        manifest["artifacts"].append({"path": study["input"]["path"], "sha256": study["input"]["sha256"]})
        write_json(path, manifest)
        changed = sha(path.read_bytes())
        self.fixture.pins = replace(self.fixture.pins, manifest_sha256=changed)
        self.fixture.gate["reviewedManifestSha256"] = changed
        freeze = json.loads((self.fixture.root / access.FREEZE_PATH).read_text()); freeze["reviewedManifestSha256"] = changed
        write_json(self.fixture.root / access.FREEZE_PATH, freeze)
        self.fixture.pins = replace(self.fixture.pins, freeze_sha256=sha((self.fixture.root / access.FREEZE_PATH).read_bytes()))
        self.fixture.gate_write(); self.no_raw_failure()

    def test_raw_sha_and_byte_count_precede_csv_decode(self):
        study = self.fixture.study("ESS9e03_3")
        (self.fixture.root / study["input"]["path"]).write_bytes(b"\xff\xfe\x00")
        with patch.object(access, "_metadata_and_response_text", side_effect=AssertionError("CSV was decoded too early")):
            with self.assertRaises(access.PolicyAccessError) as caught:
                self.fixture.run()
        self.assertEqual(caught.exception.code, access.AccessErrorCode.RAW_IDENTITY_MISMATCH)
        self.fixture.set_csv("ESS9e03_3")
        study["input"]["bytes"] += 1
        self.fixture.resign()
        with self.assertRaises(access.PolicyAccessError) as caught:
            self.fixture.run()
        self.assertEqual(caught.exception.code, access.AccessErrorCode.RAW_IDENTITY_MISMATCH)

    def test_de_metadata_before_selected_answer_interpretation(self):
        self.fixture.set_csv("ESS9e03_3", response="unknown", round_value="8.0")
        self.fixture.resign()
        with patch.object(access.adapter_api, "parse_study_csv", side_effect=AssertionError("Adapter ran before metadata check")):
            with self.assertRaises(access.PolicyAccessError) as caught:
                self.fixture.run()
        self.assertEqual(caught.exception.code, access.AccessErrorCode.INVALID_METADATA)

    def test_late_bad_de_metadata_prevents_all_response_normalization(self):
        study = self.fixture.study("ESS9e03_3")
        path = self.fixture.root / study["input"]["path"]
        rows = list(csv.reader(StringIO(path.read_text(), newline="")))
        rows[-2][rows[0].index("edition")] = "2.3"
        text = StringIO(newline=""); csv.writer(text, lineterminator="\n").writerows(rows)
        blob = text.getvalue().encode(); path.write_bytes(blob)
        study["input"].update(sha256=sha(blob), bytes=len(blob)); self.fixture.resign()
        with patch.object(access, "_normalize_response", side_effect=AssertionError("Responses touched before all DE metadata")):
            with self.assertRaises(access.PolicyAccessError) as caught:
                self.fixture.run()
        self.assertEqual(caught.exception.code, access.AccessErrorCode.INVALID_METADATA)

    def test_duplicate_header_error_is_static(self):
        study = self.fixture.study("ESS9e03_3"); path = self.fixture.root / study["input"]["path"]
        rows = list(csv.reader(StringIO(path.read_text(), newline="")))
        rows[0][-1] = rows[0][0]
        text = StringIO(newline=""); csv.writer(text, lineterminator="\n").writerows(rows)
        blob = text.getvalue().encode(); path.write_bytes(blob)
        study["input"].update(sha256=sha(blob), bytes=len(blob)); self.fixture.resign()
        with self.assertRaises(access.PolicyAccessError) as caught:
            self.fixture.run()
        self.assertEqual(str(caught.exception), "policy_access_error: invalid_csv")

    def test_metadata_numeric_equivalence_without_year_guessing(self):
        self.fixture.set_csv("ESS9e03_3", round_value="9.0", edition_value="3.300")
        self.fixture.resign()
        self.assertEqual(self.fixture.run().status, access.PRIVATE_STATUS)
        for bad in ["9.00", "+9", "9e0", " 9", "2026"]:
            self.fixture.set_csv("ESS9e03_3", round_value=bad); self.fixture.resign()
            with self.assertRaises(access.PolicyAccessError) as caught:
                self.fixture.run()
            self.assertEqual(caught.exception.code, access.AccessErrorCode.INVALID_METADATA)

    def test_response_integer_zero_fraction_equivalence(self):
        candidates = []
        for code in ["1", "1.0", "1.00"]:
            self.fixture.set_csv("ESS9e03_3", response=code); self.fixture.resign()
            self.fixture.run(); candidates.append(self.fixture.private()["candidate"])
        self.assertEqual(candidates[0], candidates[1]); self.assertEqual(candidates[0], candidates[2])

    def test_unknown_response_syntax_stays_fatal_static(self):
        for code in ["01", "+1", "1e0", "1.5", " 1", "1 ", "\t1"]:
            self.fixture.set_csv("ESS9e03_3", response=code); self.fixture.resign()
            with self.assertRaises(access.PolicyAccessError) as caught:
                self.fixture.run()
            self.assertEqual(caught.exception.code, access.AccessErrorCode.ADAPTER_REJECTED)
            self.assertEqual(str(caught.exception), "policy_access_error: adapter_rejected")

    def test_empty_cell_and_genuine_api_no_answer_are_distinct(self):
        self.fixture.set_csv("ESS9e03_3", empty=True); self.fixture.resign(); self.fixture.run()
        reasons = self.fixture.private()["candidate"]["questions"][0]["missing_reasons"]
        self.assertEqual(next(r["count"] for r in reasons if r["reason"] == access.EMPTY_REASON), 100)
        self.assertEqual(next(r["count"] for r in reasons if r["reason"] == "No answer"), 0)
        self.fixture.set_csv("ESS9e03_3", response="9.0"); self.fixture.resign(); self.fixture.run()
        reasons = self.fixture.private()["candidate"]["questions"][0]["missing_reasons"]
        self.assertEqual(next(r["count"] for r in reasons if r["reason"] == access.EMPTY_REASON), 0)
        self.assertEqual(next(r["count"] for r in reasons if r["reason"] == "No answer"), 100)

    def test_duplicate_person_is_static_and_not_exported(self):
        self.fixture.set_csv("ESS9e03_3", duplicate_id=True); self.fixture.resign()
        with self.assertRaises(access.PolicyAccessError) as caught:
            self.fixture.run()
        self.assertEqual(str(caught.exception), "policy_access_error: adapter_rejected")
        self.assertFalse((self.fixture.root / "data/local").exists())

    def test_private_permissions_atomic_output_and_no_person_leak(self):
        output, errors = StringIO(), StringIO()
        with patch("sys.stdout", output), patch("sys.stderr", errors):
            receipt = self.fixture.run()
        self.assertEqual(output.getvalue(), ""); self.assertEqual(errors.getvalue(), "")
        public = json.dumps(asdict(receipt)); private_path = self.fixture.root / receipt.private_path
        serialized = private_path.read_text()
        for marker in ["SYNTHETIC-PERSON", "SYNTHETIC-UNSELECTED-PAYLOAD", "SYNTHETIC-NONDE", "_records", "_answers"]:
            self.assertNotIn(marker, public); self.assertNotIn(marker, serialized)
        self.assertNotIn("category_counts", public); self.assertNotIn("proportion", public)
        self.assertNotIn("reviewed_historical_reference", serialized)
        self.assertEqual(stat.S_IMODE(private_path.stat().st_mode), 0o600)
        for parent in [private_path.parent, private_path.parent.parent, private_path.parent.parent.parent]:
            self.assertEqual(stat.S_IMODE(parent.stat().st_mode), 0o700)
        foreign = private_path.parent / "unrelated.txt"; foreign.write_text("Keep synthetic sibling.\n")
        self.fixture.run()
        self.assertEqual(foreign.read_text(), "Keep synthetic sibling.\n")
        self.assertEqual(list(private_path.parent.glob(".run-*.tmp")), [])

    def test_raw_symlink_and_private_output_symlink_are_rejected(self):
        study = self.fixture.study("ESS9e03_3")
        raw = self.fixture.root / study["input"]["path"]
        other = self.fixture.root / "synthetic-copy.csv"; other.write_bytes(raw.read_bytes())
        raw.unlink(); raw.symlink_to(other)
        with self.assertRaises(access.PolicyAccessError):
            self.fixture.run()
        raw.unlink(); self.fixture.set_csv("ESS9e03_3"); self.fixture.resign()
        local = self.fixture.root / "data/local"
        foreign = self.fixture.root / "synthetic-other"; foreign.mkdir(); local.symlink_to(foreign)
        with self.assertRaises(access.PolicyAccessError):
            self.fixture.run()
        self.assertEqual(list(foreign.iterdir()), [])

    def test_all_five_fixed_studies_create_only_separate_private_candidates(self):
        receipts = [self.fixture.run(identity) for identity in access.STUDIES]
        self.assertEqual({r.study_id for r in receipts}, set(access.STUDIES))
        for receipt in receipts:
            self.assertEqual(receipt.private_path, f"data/local/policy-v2/{receipt.study_id}/run.json")
            candidate = self.fixture.private(receipt.study_id)["candidate"]
            self.assertEqual(candidate["study_id"], receipt.study_id)
            self.assertTrue(all(q["source"]["study_id"] == receipt.study_id for q in candidate["questions"]))
        self.assertFalse((self.fixture.root / "web").exists())

    def test_atomic_failure_preserves_previous_candidate_and_siblings(self):
        receipt = self.fixture.run()
        path = self.fixture.root / receipt.private_path
        previous = path.read_bytes()
        sibling = path.parent / "synthetic-sibling.txt"; sibling.write_text("Preserve this file.\n")
        with patch.object(access.os, "replace", side_effect=OSError("Synthetic message must not escape")):
            with self.assertRaises(access.PolicyAccessError) as caught:
                self.fixture.run()
        self.assertEqual(str(caught.exception), "policy_access_error: private_output_failed")
        self.assertEqual(path.read_bytes(), previous)
        self.assertEqual(sibling.read_text(), "Preserve this file.\n")
        self.assertEqual(list(path.parent.glob(".run-*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
