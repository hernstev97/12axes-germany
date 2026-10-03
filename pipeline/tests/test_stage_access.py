"""Invented fixtures only. No real data/raw or data/local path is inspected."""
from __future__ import annotations

import copy
import csv
import io
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from pipeline import empirical_access as original
from pipeline import stage_access as stage

OUTPUT = Path(__file__).resolve().parents[2] / "outputs/loop/resume-later-access-author"


def contract():
    return {"items": [{"id": name, "variable": "synthetic_" + name,
                       "allowed_values": [0, 1], "integrated_file_missing_codes": [7, 8, 9],
                       "scoring": {"map": {"0": 0, "1": 1}}} for name in stage.ITEM_IDS]}


def payload(rows):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow([*original.METADATA, "pspwght", *[i["variable"] for i in contract()["items"]],
                     "invented_unused_field"])
    writer.writerows(rows)
    return stream.getvalue().encode()


def invented_rows(design=((1, 6), (2, 2))):
    rows, psu = [], 1
    for h, count in design:
        for _ in range(count):
            rows.append(["DE", "11", "4.2", "02.07.2026", str(psu), str(h), "2", "4",
                         *(["0"] * 9), "NEVER_INTERPRETED"])
            psu += 1
    return rows


class PureFrames(unittest.TestCase):
    def b_fixture(self):
        rows = invented_rows()
        raw = payload(rows)
        split = original.assignment(raw, stage.sha_bytes(raw))
        arms = {u["psu"]: u["arm"] for u in split["units"]}
        first_b = True
        for row in rows:
            if arms[int(row[4])] != "B":
                row[8:17] = ["INVALID_NON_B"] * 9
            elif first_b:
                row[8:17] = [".", "7", "NaN", "", "NA", "8", "9", "1.0", "0"]
                first_b = False
        raw = payload(rows)
        return rows, raw, original.assignment(raw, stage.sha_bytes(raw))

    def test_b_selects_before_interpretation_and_keeps_missing_rows(self):
        rows, raw, split = self.b_fixture()
        header, result = stage.confirmation_frame(raw, split, contract(), stage.sha_bytes(raw))
        self.assertEqual(header, ["stratum", "psu", "weight", *stage.ITEM_IDS])
        self.assertEqual(len(result), 3)
        self.assertTrue(all(row[2] == 4 for row in result))
        self.assertEqual(result[0][3:], ["NA"] * 7 + [1, 0])
        self.assertTrue(all(row[0] == 1 for row in result))

    def test_unknown_b_category_stops_and_non_b_unknown_does_not(self):
        rows, raw, split = self.b_fixture()
        b_psu = next(u["psu"] for u in split["units"] if u["arm"] == "B")
        next(row for row in rows if int(row[4]) == b_psu)[8] = "2"
        raw = payload(rows)
        split = original.assignment(raw, stage.sha_bytes(raw))
        with self.assertRaisesRegex(stage.AccessError, "UNEXPECTED_B_CATEGORY"):
            stage.confirmation_frame(raw, split, contract(), stage.sha_bytes(raw))

    def test_mutated_assignment_rejected(self):
        _, raw, split = self.b_fixture()
        split["units"][0]["arm"] = "B" if split["units"][0]["arm"] != "B" else "A"
        with self.assertRaisesRegex(stage.AccessError, "SPLIT_REPRODUCTION"):
            stage.confirmation_frame(raw, split, contract(), stage.sha_bytes(raw))

    def test_exact_integral_design_keys(self):
        rows = invented_rows()
        rows[0][4] = "1.5"
        raw = payload(rows)
        with self.assertRaisesRegex(stage.AccessError, "INTEGER_CODE"):
            original.assignment(raw, stage.sha_bytes(raw))
        rows[0][4] = "1e0"
        raw = payload(rows)
        self.assertEqual(original.assignment(raw, stage.sha_bytes(raw))["units"][0]["stratum"], 1)

    def test_full_original_design_weights_same_order_sensitivity(self):
        rows = invented_rows(tuple((h, 20) for h in range(1, 26)))
        rows[13][8] = "NA"
        rows.append(["ZZ", "11", "4.2", "02.07.2026", "bad", "bad", "bad", "bad",
                     *(["bad"] * 9), "bad"])
        raw = payload(rows)
        header, result, sensitivity = stage.full_frame(raw, contract(), stage.sha_bytes(raw))
        self.assertEqual(header, ["stratum", "psu", "weight", *stage.ITEM_IDS])
        self.assertEqual(len(result), 500)
        self.assertEqual([row[1] for row in result], list(range(1, 501)))
        self.assertEqual([row[2] for row in result], [2.0] * 500)
        self.assertEqual(result[13][3], "NA")
        self.assertEqual(sensitivity, [[4.0]] * 500)

    def test_full_incomplete_design_and_nonpositive_sensitivity_stop(self):
        raw = payload(invented_rows())
        with self.assertRaisesRegex(stage.AccessError, "FULL_DESIGN_FRAME"):
            stage.full_frame(raw, contract(), stage.sha_bytes(raw))
        rows = invented_rows(tuple((h, 20) for h in range(1, 26)))
        rows[0][7] = "0"
        raw = payload(rows)
        with self.assertRaisesRegex(stage.AccessError, "WEIGHT"):
            stage.full_frame(raw, contract(), stage.sha_bytes(raw))


class PublicPrivateBoundaries(unittest.TestCase):
    def setUp(self):
        OUTPUT.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="invented-", dir=OUTPUT)
        self.root = Path(self.temp.name).resolve()
        self.tags = {"analyseplan-v1": "a" * 40, "erwartungsmodell-v1": "b" * 40,
                     "modell-v1": "c" * 40}
        self.code = {}
        for relative in stage.REQUIRED_CODE:
            self.code[relative] = self.write(relative, b"invented public code or contract\n")
        for relative in (*stage.PLAN_ARTIFACTS, *stage.EXPECTATION_ARTIFACTS):
            if relative not in self.code:
                self.write(relative, b"invented public preregistration artifact\n")
        self.freeze = {"schema": "life93-model-freeze-1", "model": "M3", "scores": ["H", "Z"],
                       "items": list(stage.ITEM_IDS), "groups": stage.GROUPS["M3"],
                       "config": {"items": list(stage.ITEM_IDS),
                                  "input_columns": ["stratum", "psu", "weight", *stage.ITEM_IDS],
                                  "models": stage.GROUPS},
                       "source_code_pins": {p: self.code[p] for p in stage.SOURCE_CODE},
                       "a_result": {"path": stage.A_RESULT,
                                    "sha256": self.write(stage.A_RESULT, b'{"invented":true}\n')}}
        self.write_json(stage.MODEL, self.freeze)
        self.original_gate = self.make_gate("original", [*stage.PLAN_ARTIFACTS,
                                                       *stage.EXPECTATION_ARTIFACTS], None)
        self.original_gate["tags"] = {k: self.tags[k] for k in ("analyseplan-v1", "erwartungsmodell-v1")}
        self.write_json(stage.PRE_A, self.original_gate)
        self.pre_gate = self.make_gate("pre", [stage.MODEL, stage.A_RESULT], stage.B_RECEIPT)
        self.write_json(stage.PRE_B, self.pre_gate)
        self.aggregate = {"schema": "life93-fixed-model-confirmation-aggregate-1", "arm": "B",
                          "freeze": self.freeze, "model_name": "M3",
                          "confirmation": {"status": "CRITERIA_PASSED_PENDING_RESULT_REVIEW",
                                           "global_model_passed": True, "retained_scores": ["H", "Z"],
                                           "minimum_scores": 2}}
        self.write_json(stage.B_RESULT, self.aggregate)
        self.post_gate = self.make_gate("post", [stage.MODEL, stage.B_RESULT], stage.FULL_RECEIPT)
        self.post_gate.update(B_step_completed=True, B_retained_scores=["H", "Z"],
                              b_result={"path": stage.B_RESULT, "sha256": self.hash(stage.B_RESULT)})
        self.write_json(stage.POST_B, self.post_gate)
        self.tag_trees = {
            **{("analyseplan-v1", p): (self.root / p).read_bytes() for p in stage.PLAN_ARTIFACTS},
            **{("erwartungsmodell-v1", p): (self.root / p).read_bytes() for p in stage.EXPECTATION_ARTIFACTS},
            **{("modell-v1", p): (self.root / p).read_bytes() for p in (stage.MODEL, stage.A_RESULT)},
        }
        self.tag_patch = patch.object(stage.subprocess, "run", side_effect=self.git)
        self.tag_patch.start()
        self.version_patch = patch.object(stage.sys, "version_info", (3, 14, 7))
        self.version_patch.start()

    def tearDown(self):
        self.version_patch.stop()
        self.tag_patch.stop()
        self.temp.cleanup()

    def write(self, relative, value, mode=0o600):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value)
        path.chmod(mode)
        return stage.sha_bytes(value)

    def write_json(self, relative, value):
        return self.write(relative, (json.dumps(value, sort_keys=True) + "\n").encode())

    def hash(self, relative):
        return stage.digest(self.root / relative)

    def make_gate(self, label, paths, private_receipt):
        reviews = [{"reviewer": label + str(index), "scope": scope,
                    "path": "reports/invented-" + label + str(index) + ".md",
                    "sha256": self.write("reports/invented-" + label + str(index) + ".md", b"Invented review\n")}
                   for index, scope in enumerate(("methods-repro", "sources-construct-fairness"))]
        gate = {"decision": "ACCEPTED_BOUNDED", "reviews": reviews,
                "artifacts": [{"path": p, "sha256": self.hash(p)} for p in paths], "tags": self.tags}
        if private_receipt:
            gate["runtime"] = {"schema": "r-stage-access-v1", "sourceSha256": stage.SHA,
                               "privateReceiptPath": private_receipt, "reviewedCodeHashes": self.code}
        return gate

    def git(self, command, **kwargs):
        if command[1] == "show":
            ref, relative = command[2].split(":", 1)
            return SimpleNamespace(stdout=self.tag_trees[(ref.split("/")[-1], relative)])
        tag = command[2].split("/")[-1].split("^")[0] if command[1] == "rev-parse" else command[3].split("/")[-1]
        if command[1] == "rev-parse":
            return SimpleNamespace(stdout=self.tags[tag] + "\n")
        return SimpleNamespace(stdout=self.tags[tag] + "\trefs/tags/" + tag + "\n")

    def assert_before_private(self, arm="B"):
        with patch.object(stage, "private_boundary", side_effect=AssertionError("private touched")) as boundary:
            with self.assertRaises(stage.AccessError):
                stage.prepare_stage(self.root, arm)
            boundary.assert_not_called()

    def test_valid_public_gates_need_no_private_paths(self):
        result = stage.public_preflight(self.root, "B")
        self.assertEqual(result["authorization"]["arm"], "B")
        result = stage.public_preflight(self.root, "FULL")
        self.assertEqual(result["authorization"]["B_retained_scores"], ["H", "Z"])

    def test_failed_decision_roles_pin_code_and_tag_precede_private_reads(self):
        alterations = (
            lambda g: g.update(decision="PENDING"),
            lambda g: g["reviews"][1].update(reviewer=g["reviews"][0]["reviewer"]),
            lambda g: g["artifacts"][0].update(sha256="0" * 64),
            lambda g: g["runtime"]["reviewedCodeHashes"].update({"pipeline/stage_access.py": "0" * 64}),
            lambda g: g["tags"].update({"modell-v1": "0" * 40}),
        )
        pristine = copy.deepcopy(self.pre_gate)
        for alter in alterations:
            with self.subTest(alter=alter):
                gate = copy.deepcopy(pristine)
                alter(gate)
                self.write_json(stage.PRE_B, gate)
                self.assert_before_private()

    def test_public_artifact_cannot_alias_private_or_traverse(self):
        for relative in (stage.B_INPUT, "../outside", "/absolute"):
            gate = copy.deepcopy(self.pre_gate)
            gate["artifacts"][0]["path"] = relative
            self.write_json(stage.PRE_B, gate)
            self.assert_before_private()

    def test_tag_tree_mismatch_stops_before_private_reads(self):
        for key in (("modell-v1", stage.MODEL), ("modell-v1", stage.A_RESULT),
                    ("analyseplan-v1", stage.PLAN_ARTIFACTS[0]),
                    ("erwartungsmodell-v1", stage.EXPECTATION_ARTIFACTS[0])):
            previous = self.tag_trees[key]
            self.tag_trees[key] = b"different invented archived bytes\n"
            self.assert_before_private()
            self.tag_trees[key] = previous

    def test_full_requires_completed_positive_b_and_no_restored_score(self):
        for edit in (lambda g: g.update(B_step_completed=False),
                     lambda g: g.update(B_retained_scores=["H", "Z", "F"]),
                     lambda g: g.update(B_retained_scores=["H"]),
                     lambda g: g.update(B_retained_scores=["Z", "H"])):
            gate = copy.deepcopy(self.post_gate)
            edit(gate)
            self.write_json(stage.POST_B, gate)
            self.assert_before_private("FULL")

    def test_full_verifies_actual_b_aggregate_status(self):
        aggregate = copy.deepcopy(self.aggregate)
        aggregate["confirmation"]["global_model_passed"] = False
        self.write_json(stage.B_RESULT, aggregate)
        gate = copy.deepcopy(self.post_gate)
        gate["b_result"]["sha256"] = self.hash(stage.B_RESULT)
        gate["artifacts"][1]["sha256"] = self.hash(stage.B_RESULT)
        self.write_json(stage.POST_B, gate)
        self.assert_before_private("FULL")

    def private_folder(self):
        folder = self.root / stage.PRIVATE
        folder.mkdir(parents=True)
        (self.root / "data/local").chmod(0o700)
        folder.chmod(0o700)
        return folder

    def test_output_overwrite_symlink_alias_traversal_and_permissions(self):
        folder = self.private_folder()
        target = folder / "B.csv"
        target.write_text("invented")
        with self.assertRaisesRegex(stage.AccessError, "DO_NOT_OVERWRITE"):
            stage.private_boundary(self.root, (stage.B_INPUT,))
        target.unlink()
        target.symlink_to(self.root / stage.MODEL)
        with self.assertRaisesRegex(stage.AccessError, "DO_NOT_OVERWRITE"):
            stage.private_boundary(self.root, (stage.B_INPUT,))
        target.unlink()
        with self.assertRaisesRegex(stage.AccessError, "PRIVATE_PATH"):
            stage.private_boundary(self.root, (stage.PRIVATE + "/../B.csv",))
        folder.chmod(0o755)
        with self.assertRaisesRegex(stage.AccessError, "PRIVATE_PARENT_MODE"):
            stage.private_boundary(self.root)

    def test_new_output_is_exclusive_600(self):
        self.private_folder()
        previous_umask = os.umask(0o777)
        try:
            stage.exclusive_write(self.root, stage.B_INPUT, b"invented\n")
        finally:
            os.umask(previous_umask)
        self.assertEqual((self.root / stage.B_INPUT).stat().st_mode & 0o777, 0o600)
        with self.assertRaisesRegex(stage.AccessError, "DO_NOT_OVERWRITE"):
            stage.exclusive_write(self.root, stage.B_INPUT, b"other\n")

    def confirmation_files(self):
        self.private_folder()
        public = stage.public_preflight(self.root, "B")
        self.write_json(stage.ASSIGNMENT, {"inputSha256": stage.SHA, "seed": 2026100301,
                                          "units": [], "scope": "invented receipt fixture"})
        self.write_json(stage.A_RECEIPT, {"schema": "r-runtime-input-v1", "sourceSha256": stage.SHA,
                                         "gateSha256": public["originalGateSha256"],
                                         "empiricalAccessSha256": self.code["pipeline/empirical_access.py"],
                                         "assignment": {"path": stage.ASSIGNMENT,
                                                        "sha256": self.hash(stage.ASSIGNMENT)}})
        self.write(stage.B_INPUT, b"stratum,psu,weight,B34,B35,B36,B40,B41,B42,B43,B44,B45\n")
        receipt = {"schema": "r-confirm-input-v1", "gateSha256": public["gateSha256"],
                   "modelSha256": public["modelSha256"], "sourceSha256": stage.SHA,
                   "codeSha256": self.code,
                   "assignment": {"path": stage.ASSIGNMENT, "sha256": self.hash(stage.ASSIGNMENT)},
                   "assignmentProvenance": {"path": stage.A_RECEIPT, "sha256": self.hash(stage.A_RECEIPT)},
                   "confirmationInput": {"path": stage.B_INPUT, "sha256": self.hash(stage.B_INPUT)}}
        self.write_json(stage.B_RECEIPT, receipt)
        return receipt

    def test_runtime_confirmation_receipt_rehashes_input_and_provenance(self):
        self.confirmation_files()
        public = stage.preflight_confirmation(self.root)
        self.assertEqual(public["privatehashes"]["bSha256"], self.hash(stage.B_INPUT))
        self.write(stage.B_INPUT, b"changed invented bytes\n")
        with self.assertRaisesRegex(stage.AccessError, "PRIVATE_INPUT_PIN"):
            stage.preflight_confirmation(self.root)

    def test_runtime_confirmation_receipt_code_model_and_assignment_bindings(self):
        receipt = self.confirmation_files()
        for change in (lambda r: r.update(modelSha256="0" * 64),
                       lambda r: r.update(codeSha256={}),
                       lambda r: r["assignment"].update(sha256="0" * 64)):
            mutated = copy.deepcopy(receipt)
            change(mutated)
            self.write_json(stage.B_RECEIPT, mutated)
            with self.assertRaises(stage.AccessError):
                stage.preflight_confirmation(self.root)

    def test_runtime_full_receipt_b_receipt_and_sensitivity_bindings(self):
        self.confirmation_files()
        public = stage.public_preflight(self.root, "FULL")
        self.write(stage.FULL_INPUT, b"invented full input\n")
        self.write(stage.SENSITIVITY, b"pspwght\n4\n")
        receipt = {"schema": "r-full-input-v1", "gateSha256": public["gateSha256"],
                   "modelSha256": public["modelSha256"], "sourceSha256": stage.SHA,
                   "codeSha256": self.code, "confirmReceiptSha256": self.hash(stage.B_RECEIPT),
                   "assignment": {"path": stage.ASSIGNMENT, "sha256": self.hash(stage.ASSIGNMENT)},
                   "assignmentProvenance": {"path": stage.A_RECEIPT, "sha256": self.hash(stage.A_RECEIPT)},
                   "fullInput": {"path": stage.FULL_INPUT, "sha256": self.hash(stage.FULL_INPUT)},
                   "sensitivityInput": {"path": stage.SENSITIVITY, "sha256": self.hash(stage.SENSITIVITY)}}
        self.write_json(stage.FULL_RECEIPT, receipt)
        result = stage.preflight_full(self.root)
        self.assertEqual(result["privatehashes"]["sensitivitySha256"], self.hash(stage.SENSITIVITY))
        self.write(stage.SENSITIVITY, b"pspwght\n8\n")
        with self.assertRaisesRegex(stage.AccessError, "PRIVATE_INPUT_PIN"):
            stage.preflight_full(self.root)


if __name__ == "__main__":
    unittest.main()
