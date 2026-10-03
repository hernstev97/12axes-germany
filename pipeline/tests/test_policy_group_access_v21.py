"""Real guarded I/O exercised only in owned synthetic temporary repositories."""

from copy import deepcopy
import csv
from dataclasses import fields, replace
import hashlib
from io import StringIO
import json
import os
from pathlib import Path
import stat
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from pipeline import policy_group_access_v21 as access


REPO = Path(__file__).parents[2]
OUT = REPO / "outputs/loop/policy-group-access-v21/synthetic-repositories"
PRIVATE_ID = "SYNTHETIC_PRIVATE_IDENTIFIER_DO_NOT_SERIALIZE"
SECRET = "SYNTHETIC_UNSELECTED_CELL_DO_NOT_SERIALIZE"


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


class SyntheticRepo:
    """No original raw/local byte is read, copied or statted by this fixture."""

    def __init__(self):
        OUT.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="guard-", dir=OUT)
        self.root = Path(self.temporary.name)
        self.study = json.loads((REPO / access.STUDY_CONTRACT_PATH).read_bytes())
        self.group = json.loads((REPO / access.GROUP_CONTRACT_PATH).read_bytes())
        self.catalog_bytes = (REPO / access.CATALOG_PATH).read_bytes()
        self.rows = {}
        self.headers = {}
        self.source_paths = set()
        for current in self.study["studies"]:
            sid = current["study_id"]
            grouping = next(item for item in self.group["studies"] if item["studyId"] == sid)
            header = ["cntry", "idno", "essround", "edition", "vote", grouping["columns"]["party2"],
                      "pspwght", "dweight", "anweight", *(q["variable"] for q in current["adapter"]["questions"]),
                      "unselected_column"]
            row = ["DE", PRIVATE_ID, str(current["round"]), current["edition"], "1", "1", "1", "1", "2",
                   *(q["categoryCodes"][0] for q in current["adapter"]["questions"]), SECRET]
            self.headers[sid] = header; self.rows[sid] = [row]
            self.write_csv(sid)
        self.write(access.CATALOG_PATH, self.catalog_bytes)
        for key, reference in self.group["references"].items():
            if key not in {"catalogue", "analysisContract"}:
                reference["sha256"] = self.write(reference["path"], b"Synthetic public source fixture, no real judgment.\n")
                self.source_paths.add(reference["path"])
        exposure = self.group["priorExposure"]
        exposure["externalShareExposureSource"]["sha256"] = self.write(
            exposure["externalShareExposureSource"]["path"], b'{"fixture":"synthetic exposure boundary"}\n')
        self.source_paths.add(exposure["externalShareExposureSource"]["path"])
        context = exposure["knownDataContext"]
        context["reference"]["sha256"] = self.write_json(context["reference"]["path"], context["context"])
        self.source_paths.add(context["reference"]["path"])
        for source in self.group["sources"]:
            source["originalBytesSha256"] = self.write(
                source["cachedPublicDocumentationPath"], ("Synthetic source placeholder: " + source["id"] + "\n").encode())
            self.source_paths.add(source["cachedPublicDocumentationPath"])
        self.runtime_paths = set(access._RUNTIME_MODULES) | {"pipeline/policy_group_access_v21.py"}
        for path in self.runtime_paths:
            self.write(path, (REPO / path).read_bytes())
        self.reviewers = []
        for role in sorted(access.REVIEW_ROLES):
            path = f"reports/loop/reviews/synthetic-{role}.md"
            sha = self.write(path, b"Synthetic bounded protocol report; no empirical or scientific acceptance.\n")
            self.reviewers.append({"role": role, "reportPath": path, "sha256": sha, "decision": "ACCEPTED_BOUNDED"})
        self.extra_artifacts = set()
        self.commit = "1" * 40
        self.seal()

    def close(self):
        self.temporary.cleanup()

    def write(self, relative, blob):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(blob)
        return digest(blob)

    def write_json(self, relative, value):
        return self.write(relative, (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode())

    def current(self, sid):
        return next(item for item in self.study["studies"] if item["study_id"] == sid)

    def grouping(self, sid):
        return next(item for item in self.group["studies"] if item["studyId"] == sid)

    def write_csv(self, sid):
        stream = StringIO(newline="")
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(self.headers[sid]); writer.writerows(self.rows[sid])
        blob = stream.getvalue().encode()
        current = self.current(sid)
        self.write(current["input"]["path"], blob)
        current["input"].update(sha256=digest(blob), bytes=len(blob))
        self.grouping(sid)["opaqueInputReference"].update(sha256=digest(blob), bytes=len(blob))

    def cell(self, sid, column, value, row=0):
        self.rows[sid][row][self.headers[sid].index(column)] = value
        self.write_csv(sid)

    def seal(self):
        study_sha = self.write_json(access.STUDY_CONTRACT_PATH, self.study)
        self.group["references"]["analysisContract"]["sha256"] = study_sha
        for item in self.group["studies"]:
            item["opaqueInputReference"]["obtainedFrom"]["sha256"] = study_sha
        group_sha = self.write_json(access.GROUP_CONTRACT_PATH, self.group)
        artifact_paths = access.CORE_ARTIFACTS | self.source_paths | self.extra_artifacts
        artifacts = [{"path": path, "sha256": digest((self.root / path).read_bytes())} for path in sorted(artifact_paths)]
        self.manifest = {"schemaVersion": 1, "package": access.PACKAGE, "artifacts": artifacts}
        self.seal_manifest(group_sha=group_sha, study_sha=study_sha)

    def seal_manifest(self, *, group_sha=None, study_sha=None):
        group_sha = group_sha or digest((self.root / access.GROUP_CONTRACT_PATH).read_bytes())
        study_sha = study_sha or digest((self.root / access.STUDY_CONTRACT_PATH).read_bytes())
        manifest_sha = self.write_json(access.MANIFEST_PATH, self.manifest)
        freeze = {"schemaVersion": 1, "package": access.PACKAGE, "frozenCommit": self.commit,
                  "planTag": access.PLAN_TAG, "reviewedManifestSha256": manifest_sha,
                  "groupContractSha256": group_sha, "studyContractSha256": study_sha}
        freeze_sha = self.write_json(access.FREEZE_PATH, freeze)
        self.gate = {"schemaVersion": 1, "package": access.PACKAGE, "decision": access.DECISION,
                     "reviewedManifestSha256": manifest_sha, "frozenCommit": self.commit,
                     "planTag": access.PLAN_TAG, "allowedStudyIds": ["ESS5e03_6"],
                     "reviewers": deepcopy(self.reviewers)}
        self.write_json(access.GATE_PATH, self.gate)
        self.pins = access.AccessPins(manifest_sha, group_sha, study_sha, freeze_sha, self.commit)

    def allow(self, sid):
        self.gate["allowedStudyIds"] = [sid]
        self.write_json(access.GATE_PATH, self.gate)

    def run(self, sid="ESS5e03_6"):
        return access.run_group_reference(self.root, sid, self.pins)

    def private_path(self, sid="ESS5e03_6"):
        return self.root / f"data/local/policy-groups-v21/{sid}/run.json"

    def older_output(self):
        path = self.private_path()
        parent = self.root / "data"
        for component in ("local", "policy-groups-v21", "ESS5e03_6"):
            parent /= component; parent.mkdir(exist_ok=True, mode=0o700); parent.chmod(0o700)
        path.write_bytes(b"older private synthetic aggregate\n"); path.chmod(0o600)
        return path.read_bytes()


class AccessTests(unittest.TestCase):
    def setUp(self):
        self.repo = SyntheticRepo()
        self.addCleanup(self.repo.close)

    def assert_no_raw(self, action, code=None):
        calls = []
        original = access._read_fd_file
        def read(fd, relative):
            calls.append(relative)
            if relative.startswith(("data/raw/", "data/local/")):
                raise AssertionError("raw_or_local_path_reached_before_guard")
            return original(fd, relative)
        with patch.object(access, "_read_raw_bytes") as raw, patch.object(access, "_read_fd_file", side_effect=read):
            with self.assertRaises(access.PolicyGroupAccessError) as caught:
                action()
            raw.assert_not_called()
        self.assertFalse(any(path.startswith(("data/raw/", "data/local/")) for path in calls))
        if code is not None:
            self.assertIs(caught.exception.code, code)
        self.assertNotIn(PRIVATE_ID, str(caught.exception))
        self.assertNotIn(SECRET, str(caught.exception))

    def assert_static_failure(self, action, code=None):
        before = self.repo.older_output()
        with self.assertRaises(access.PolicyGroupAccessError) as caught:
            action()
        self.assertNotIn(PRIVATE_ID, str(caught.exception))
        self.assertNotIn(SECRET, str(caught.exception))
        if code is not None:
            self.assertIs(caught.exception.code, code)
        self.assertTrue(self.repo.private_path().read_bytes() == before)

    def test_real_api_all_five_sources_private_only(self):
        for sid in access.v2_io.STUDIES:
            with self.subTest(study=sid):
                self.repo.allow(sid)
                receipt = self.repo.run(sid)
                self.assertEqual(receipt.status, access.PRIVATE_STATUS)
                payload = json.loads(self.repo.private_path(sid).read_bytes())
                self.assertEqual(payload["status"], access.PRIVATE_STATUS)
                self.assertEqual(len(payload["candidate"]["groups"]), len(self.repo.grouping(sid)["groupsInDeclaredApiOrder"]))
                self.assertTrue(all(len(g["questions"]) == len(self.repo.current(sid)["adapter"]["questions"])
                                    for g in payload["candidate"]["groups"]))
                self.assertTrue(receipt.output_sha256 == digest(self.repo.private_path(sid).read_bytes()))
                rendered = self.repo.private_path(sid).read_text()
                self.assertNotIn(PRIVATE_ID, rendered)
                self.assertNotIn(SECRET, rendered)
                self.assertNotIn("_records", rendered)
                self.assertNotIn("reviewed_historical_reference", rendered)

    def test_legacy_runners_and_exports_never_called(self):
        with patch.object(access.v2_io, "run_study_reference", side_effect=AssertionError("legacy_runner")), \
             patch.object(access.analysis_api, "prepare_study_references", side_effect=AssertionError("legacy_marginals")), \
             patch.object(access.analysis_api, "expose_prepared_candidate", side_effect=AssertionError("legacy_candidate")), \
             patch.object(access.export_api, "build_reviewed_reference_export", side_effect=AssertionError("public_export")):
            self.repo.run()

    def test_explicit_gate_subset(self):
        self.assert_no_raw(lambda: self.repo.run("ESS8e02_3"), access.AccessErrorCode.STUDY_NOT_ALLOWED)

    def test_missing_gate_old_gate_cannot_unlock(self):
        (self.repo.root / access.GATE_PATH).unlink()
        self.repo.write_json(access.v2_io.GATE_PATH, {"decision": access.DECISION})
        self.assert_no_raw(self.repo.run)

    def test_gate_strings_shape_and_allowed_ids_fail_closed(self):
        original = deepcopy(self.repo.gate)
        edits = [lambda g: g.update(decision="ALLOW"), lambda g: g.update(decision="ALLOW_HISTORICAL_DESCRIPTIVE_V2"),
                 lambda g: g.update(package="EMPIRICAL-V2-001/v1"), lambda g: g.update(extraPermission=True),
                 lambda g: g.update(schemaVersion=True), lambda g: g.update(allowedStudyIds=[]),
                 lambda g: g.pop("allowedStudyIds"), lambda g: g.update(allowedStudyIds=["ESS5e03_6", "ESS5e03_6"]),
                 lambda g: g.update(allowedStudyIds=["foreign"]), lambda g: g.update(planTag="analyseplan-v2")]
        for edit in edits:
            gate = deepcopy(original); edit(gate); self.repo.write_json(access.GATE_PATH, gate)
            self.assert_no_raw(self.repo.run)

    def test_duplicate_json_gate_key_rejected(self):
        self.repo.write(access.GATE_PATH, b'{"schemaVersion":1,"schemaVersion":1}\n')
        self.assert_no_raw(self.repo.run)

    def test_review_paths_roles_decisions_hashes(self):
        original = deepcopy(self.repo.gate)
        edits = [lambda g: g["reviewers"][1].update(role=g["reviewers"][0]["role"]),
                 lambda g: g["reviewers"][1].update(reportPath=g["reviewers"][0]["reportPath"]),
                 lambda g: g["reviewers"][0].update(reportPath="reports/loop/authors/author.md"),
                 lambda g: g["reviewers"][0].update(reportPath="reports/loop/reviews/../authors/author.md"),
                 lambda g: g["reviewers"][0].update(decision="APPROVED"),
                 lambda g: g["reviewers"][0].update(sha256="0" * 64)]
        for edit in edits:
            gate = deepcopy(original); edit(gate); self.repo.write_json(access.GATE_PATH, gate)
            self.assert_no_raw(self.repo.run)

    def test_empty_review_report_is_not_positive_evidence(self):
        report = self.repo.gate["reviewers"][0]
        report["sha256"] = self.repo.write(report["reportPath"], b" \n")
        self.repo.write_json(access.GATE_PATH, self.repo.gate)
        self.assert_no_raw(self.repo.run)

    def test_pins_are_external_and_strict(self):
        original = self.repo.pins
        for altered in (replace(original, manifest_sha256="0" * 64), replace(original, frozen_commit="short"),
                        replace(original, plan_tag="analyseplan-v2"), {"decision": "ALLOW"}):
            self.repo.pins = altered
            self.assert_no_raw(self.repo.run)

    def test_frozen_provenance_must_match(self):
        path = self.repo.root / access.FREEZE_PATH
        freeze = json.loads(path.read_bytes()); freeze["planTag"] = "analyseplan-v2"
        sha = self.repo.write_json(access.FREEZE_PATH, freeze)
        self.repo.pins = replace(self.repo.pins, freeze_sha256=sha)
        self.assert_no_raw(self.repo.run)

    def test_manifest_artifact_drift_prevents_raw(self):
        self.repo.write(access.CATALOG_PATH, b"synthetic changed public bytes\n")
        self.assert_no_raw(self.repo.run)

    def test_duplicate_manifest_artifact(self):
        self.repo.manifest["artifacts"].append(deepcopy(self.repo.manifest["artifacts"][0]))
        self.repo.seal_manifest(); self.assert_no_raw(self.repo.run)

    def test_manifest_cannot_open_raw_local_or_state(self):
        for path in (self.repo.current("ESS5e03_6")["input"]["path"], "data/local/private.json", "reports/loop/state.json"):
            self.repo.write(path, b"synthetic forbidden extra\n")
            self.repo.manifest["artifacts"].append({"path": path, "sha256": digest(b"synthetic forbidden extra\n")})
            self.repo.seal_manifest(); self.assert_no_raw(self.repo.run)
            self.repo.manifest["artifacts"].pop()

    def test_required_source_pin_cannot_be_omitted(self):
        path = self.repo.group["sources"][0]["cachedPublicDocumentationPath"]
        self.repo.manifest["artifacts"] = [a for a in self.repo.manifest["artifacts"] if a["path"] != path]
        self.repo.seal_manifest(); self.assert_no_raw(self.repo.run)

    def test_runtime_source_diff_even_resealed_is_rejected(self):
        self.repo.write("pipeline/policy_report_v2.py", b"# changed fixture runtime source\n")
        self.repo.seal(); self.assert_no_raw(self.repo.run)

    def test_loaded_runtime_drift_fails_guard(self):
        altered = dict(access._LOADED_RUNTIME_HASHES); altered["pipeline/policy_groups_v21.py"] = "0" * 64
        with patch.object(access, "_runtime_hashes", return_value=altered):
            self.assert_no_raw(self.repo.run)

    def test_full_source_and_rules_binding(self):
        original = deepcopy(self.repo.group)
        edits = [lambda g: g["displayPolicy"].update(minimumValidQuestionCount=99),
                 lambda g: g["weightPolicy"]["ratioDiagnostic"].update(scope="all_DE"),
                 lambda g: g["studies"][0]["nationalParty2Field"].update(fieldId="00000000-0000-0000-0000-000000000000"),
                 lambda g: g["studies"][0]["groupsInDeclaredApiOrder"].pop(),
                 lambda g: g["studies"][0]["fileMetadataReference"].update(metadataVersion=1),
                 lambda g: g["sources"][0].update(publicUrl="https://example.invalid/"),
                 lambda g: g["priorExposure"].update(privateV2MarginalSoftwareRunNowKnown=False)]
        for edit in edits:
            self.repo.group = deepcopy(original); edit(self.repo.group); self.repo.seal()
            self.assert_no_raw(self.repo.run)

    def test_wrong_fixed_raw_path_fails_before_raw(self):
        self.repo.current("ESS5e03_6")["input"]["path"] = "data/raw/elsewhere.csv"
        self.repo.seal(); self.assert_no_raw(self.repo.run)

    def test_public_component_symlink_rejected(self):
        path = self.repo.root / self.repo.gate["reviewers"][0]["reportPath"]
        target = path.with_name("synthetic-real-report.md"); path.rename(target); path.symlink_to(target.name)
        self.assert_no_raw(self.repo.run)

    def test_root_component_symlink_rejected(self):
        path = self.repo.root.parent / (self.repo.root.name + "-link")
        path.symlink_to(self.repo.root, target_is_directory=True)
        self.addCleanup(path.unlink)
        self.assert_no_raw(lambda: access.run_group_reference(path, "ESS5e03_6", self.repo.pins))

    def test_raw_symlinks_in_leaf_and_parent(self):
        raw = self.repo.root / self.repo.current("ESS5e03_6")["input"]["path"]
        target = raw.with_name("synthetic-real.csv"); raw.rename(target); raw.symlink_to(target.name)
        self.assert_static_failure(self.repo.run)
        raw.unlink(); target.rename(raw)
        parent = raw.parent; new_parent = parent.with_name(parent.name + "-real"); parent.rename(new_parent)
        parent.symlink_to(new_parent.name, target_is_directory=True)
        self.assert_static_failure(self.repo.run)

    def test_raw_hash_before_decoder_or_party_api(self):
        raw = self.repo.root / self.repo.current("ESS5e03_6")["input"]["path"]
        raw.write_bytes(raw.read_bytes() + b"\xff")
        with patch.object(access.groups_api, "prepare_group_references") as prepare, \
             patch.object(access.v2_io, "_metadata_and_response_text") as metadata:
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.RAW_IDENTITY_MISMATCH)
            prepare.assert_not_called(); metadata.assert_not_called()

    def test_raw_byte_count_independently_checked(self):
        self.repo.current("ESS5e03_6")["input"]["bytes"] += 1
        self.repo.grouping("ESS5e03_6")["opaqueInputReference"]["bytes"] += 1
        self.repo.seal()
        self.assert_static_failure(self.repo.run, access.AccessErrorCode.RAW_IDENTITY_MISMATCH)

    def test_invalid_encoding_after_identity_before_party(self):
        sid = "ESS5e03_6"; raw = self.repo.current(sid)["input"]["path"]
        blob = b"\xff"
        self.repo.write(raw, blob)
        self.repo.current(sid)["input"].update(bytes=len(blob), sha256=digest(blob))
        self.repo.grouping(sid)["opaqueInputReference"].update(bytes=len(blob), sha256=digest(blob))
        self.repo.seal()
        with patch.object(access.groups_api, "prepare_group_references") as prepare:
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.INVALID_CSV)
            prepare.assert_not_called()

    def test_all_de_metadata_precedes_party_interpretation(self):
        sid = "ESS5e03_6"
        self.repo.rows[sid].append(list(self.repo.rows[sid][0])); self.repo.rows[sid][1][1] += "_SECOND"
        self.repo.cell(sid, "vote", SECRET, row=0)
        self.repo.cell(sid, "edition", "7.1", row=1); self.repo.seal()
        with patch.object(access.groups_api, "prepare_group_references") as prepare:
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.INVALID_METADATA)
            prepare.assert_not_called()

    def test_metadata_numeric_rule_only(self):
        sid = "ESS5e03_6"
        self.repo.cell(sid, "essround", "5.0"); self.repo.cell(sid, "edition", "3.60"); self.repo.seal()
        self.repo.run()
        for column, value in (("essround", "5.00"), ("essround", "+5"), ("edition", "03.6"), ("edition", "3.6 ")):
            self.repo.cell(sid, "essround", "5"); self.repo.cell(sid, "edition", "3.6")
            self.repo.cell(sid, column, value); self.repo.seal()
            with patch.object(access.groups_api, "prepare_group_references") as prepare:
                self.assert_static_failure(self.repo.run, access.AccessErrorCode.INVALID_METADATA)
                prepare.assert_not_called()

    def test_response_zero_fraction_and_blanks_preserved(self):
        sid = "ESS5e03_6"; question = self.repo.current(sid)["adapter"]["questions"][0]
        for value in ("1", "1.0", "1.00"):
            self.repo.cell(sid, "vote", value); self.repo.cell(sid, self.repo.grouping(sid)["columns"]["party2"], value)
            self.repo.cell(sid, question["variable"], value); self.repo.seal(); self.repo.run()
        self.repo.cell(sid, question["variable"], ""); self.repo.seal(); self.repo.run()
        payload = json.loads(self.repo.private_path().read_bytes())
        reasons = payload["candidate"]["groups"][0]["questions"][0]["missing_reasons"]
        self.assertTrue(any(r["reason"] == "export_blank_unclassified" and r["count"] == 1 for r in reasons))

    def test_unknown_selected_literals_static_fatal(self):
        sid = "ESS5e03_6"; columns = ["vote", self.repo.grouping(sid)["columns"]["party2"],
                                           self.repo.current(sid)["adapter"]["questions"][0]["variable"]]
        original_rows = deepcopy(self.repo.rows[sid])
        for column in columns:
            for value in ("01", "+1", "1e0", "1.5", " 1", "1 ", SECRET):
                self.repo.rows[sid] = deepcopy(original_rows); self.repo.cell(sid, column, value); self.repo.seal()
                self.assert_static_failure(self.repo.run, access.AccessErrorCode.GROUP_PREPARATION_REJECTED)

    def test_genuine_party9_and_noanswer9_are_distinct(self):
        sid = "ESS11e04_2"; self.repo.cell(sid, "prtvgde2", "9")
        self.repo.cell(sid, "gincdif", "9"); self.repo.seal(); self.repo.allow(sid); self.repo.run(sid)
        payload = json.loads(self.repo.private_path(sid).read_bytes())
        chosen = next(g for g in payload["candidate"]["groups"] if g["party2_code"] == "9")
        self.assertEqual(chosen["eligible_case_count"], 1)
        self.assertTrue(any(r["reason"] == "No answer" and r["count"] == 1 for r in chosen["questions"][0]["missing_reasons"]))

    def test_duplicate_identifier_static_no_output_change(self):
        self.repo.rows["ESS5e03_6"].append(list(self.repo.rows["ESS5e03_6"][0]))
        self.repo.write_csv("ESS5e03_6"); self.repo.seal()
        self.assert_static_failure(self.repo.run, access.AccessErrorCode.GROUP_PREPARATION_REJECTED)

    def test_header_and_row_shape_do_not_leak(self):
        sid = "ESS5e03_6"; self.repo.headers[sid][0] = SECRET
        self.repo.write_csv(sid); self.repo.seal()
        self.assert_static_failure(self.repo.run, access.AccessErrorCode.INVALID_CSV)

    def test_nonselected_and_non_de_cells_not_interpreted(self):
        sid = "ESS5e03_6"
        foreign = [SECRET] * len(self.repo.headers[sid]); foreign[0] = "FR"
        self.repo.rows[sid].append(foreign); self.repo.write_csv(sid); self.repo.seal(); self.repo.run()
        self.assertNotIn(SECRET, self.repo.private_path().read_text())

    def test_backend_error_and_record_object_rejected_without_leak(self):
        with patch.object(access.groups_api, "prepare_group_references", side_effect=ValueError(SECRET)):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.GROUP_PREPARATION_REJECTED)
        with patch.object(access.groups_api, "prepare_group_references", return_value=SimpleNamespace(_records=[PRIVATE_ID])):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.INVALID_PRIVATE_AGGREGATE)

    def test_promoted_question_status_is_not_serialized(self):
        original = access.groups_api.prepare_group_references
        def promoted(*args):
            prepared = original(*args)
            first = prepared.groups[0]
            question = replace(first.questions[0], status="reviewed_historical_reference")
            group = replace(first, questions=(question, *first.questions[1:]))
            return replace(prepared, groups=(group, *prepared.groups[1:]))
        with patch.object(access.groups_api, "prepare_group_references", side_effect=promoted):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.INVALID_PRIVATE_AGGREGATE)

    def test_private_modes_receipt_allowlist_and_no_extra_outputs(self):
        receipt = self.repo.run()
        private = self.repo.private_path()
        self.assertEqual(stat.S_IMODE(private.stat().st_mode), 0o600)
        for path in (private.parent, private.parent.parent, private.parent.parent.parent):
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o700)
        self.assertEqual(set(f.name for f in fields(receipt)), {
            "study_id", "status", "started_utc", "finished_utc", "gate_sha256", "manifest_sha256",
            "group_contract_sha256", "study_contract_sha256", "freeze_sha256", "input_sha256",
            "output_sha256", "private_path", "exit_code"})
        self.assertNotIn(PRIVATE_ID, repr(receipt)); self.assertNotIn(SECRET, repr(receipt))
        self.assertEqual([path.name for path in private.parent.iterdir()], ["run.json"])

    def test_private_output_symlink_and_permissions_fail(self):
        before = self.repo.older_output(); private = self.repo.private_path()
        target = private.with_name("foreign-synthetic.json"); private.rename(target); private.symlink_to(target.name)
        with self.assertRaises(access.PolicyGroupAccessError):
            self.repo.run()
        self.assertTrue(target.read_bytes() == before)
        private.unlink(); target.rename(private); private.chmod(0o644)
        with self.assertRaises(access.PolicyGroupAccessError) as caught:
            self.repo.run()
        self.assertIs(caught.exception.code, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        self.assertTrue(private.read_bytes() == before)

    def test_private_parent_symlink_fails(self):
        before = self.repo.older_output(); local = self.repo.root / "data/local"
        target = local.with_name("synthetic-local-real"); local.rename(target); local.symlink_to(target.name, target_is_directory=True)
        with self.assertRaises(access.PolicyGroupAccessError) as caught:
            self.repo.run()
        self.assertIs(caught.exception.code, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        self.assertTrue((target / "policy-groups-v21/ESS5e03_6/run.json").read_bytes() == before)

    def test_write_fsync_failure_preserves_old_output(self):
        with patch.object(access.os, "fsync", side_effect=OSError("synthetic disk failure")):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)

    def test_replace_failure_preserves_old_output(self):
        with patch.object(access.os, "replace", side_effect=OSError("synthetic rename failure")):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)

    def test_directory_fsync_after_replace_rolls_back(self):
        original = access.os.fsync; calls = 0
        def fail_once(fd):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("synthetic post-replace fsync failure")
            return original(fd)
        with patch.object(access.os, "fsync", side_effect=fail_once):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        self.assertEqual([p.name for p in self.repo.private_path().parent.iterdir()], ["run.json"])

    def test_temporary_name_collision_does_not_delete_foreign_file(self):
        before = self.repo.older_output()
        foreign = self.repo.private_path().with_name(".run-collision.tmp")
        foreign.write_bytes(b"foreign synthetic temporary\n"); foreign.chmod(0o600)
        with patch.object(access.secrets, "token_hex", return_value="collision"):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        self.assertTrue(foreign.read_bytes() == b"foreign synthetic temporary\n")
        self.assertTrue(self.repo.private_path().read_bytes() == before)

    def test_backup_name_collision_does_not_delete_foreign_file(self):
        before = self.repo.older_output()
        foreign = self.repo.private_path().with_name(".previous-run-collision.tmp")
        foreign.write_bytes(b"foreign synthetic backup\n"); foreign.chmod(0o600)
        with patch.object(access.secrets, "token_hex", return_value="collision"):
            self.assert_static_failure(self.repo.run, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        self.assertTrue(foreign.read_bytes() == b"foreign synthetic backup\n")
        self.assertTrue(self.repo.private_path().read_bytes() == before)

    def test_double_filesystem_failure_keeps_old_private_backup(self):
        before = self.repo.older_output()
        original_replace = access.os.replace; original_fsync = access.os.fsync
        replacements = syncs = 0
        def fail_recovery(*args, **kwargs):
            nonlocal replacements
            replacements += 1
            if replacements == 2:
                raise OSError("synthetic restore failure")
            return original_replace(*args, **kwargs)
        def fail_directory_sync(fd):
            nonlocal syncs
            syncs += 1
            if syncs == 2:
                raise OSError("synthetic post-rename sync failure")
            return original_fsync(fd)
        with patch.object(access.os, "replace", side_effect=fail_recovery), \
             patch.object(access.os, "fsync", side_effect=fail_directory_sync):
            with self.assertRaises(access.PolicyGroupAccessError) as caught:
                self.repo.run()
        self.assertIs(caught.exception.code, access.AccessErrorCode.PRIVATE_OUTPUT_FAILED)
        backups = list(self.repo.private_path().parent.glob(".previous-run-*.tmp"))
        self.assertEqual(len(backups), 1)
        self.assertTrue(backups[0].read_bytes() == before)
        self.assertEqual(stat.S_IMODE(backups[0].stat().st_mode), 0o600)


if __name__ == "__main__":
    unittest.main()
