"""Invarianten für öffentliche Pakete und ehrlichen Abschlussstatus."""
import copy
import hashlib
import json
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("loop", Path(__file__).parents[1] / "loop.py")
loop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loop)

class LoopSafetyTests(unittest.TestCase):
    def test_raw_secret_and_external_symlink_cannot_be_frozen(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            (root / "docs").mkdir()
            external = Path(outside) / "private.txt"
            external.write_text("synthetic placeholder")
            (root / "docs/outside.md").symlink_to(external)
            (root / "data/raw").mkdir(parents=True)
            (root / "data/raw/file.csv").write_text("synthetic placeholder")
            for name in ["data/raw/file.csv", "./data/raw/file.csv", "data//raw/file.csv", "data/local/file.csv", ".env", "../outside.md", "docs/outside.md"]:
                with self.subTest(name=name), self.assertRaises(ValueError):
                    loop.public_input(root, name)

    def test_snapshot_keeps_source_changes_separate_and_detects_archive_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            source = root / "docs/plan.md"
            source.write_text("original synthetic plan")
            package = root / "reports/loop/packages/unit/v1"
            loop.freeze(root, package, ["docs/plan.md"], {"id": "synthetic-unit"})
            source.write_text("new synthetic plan")
            self.assertTrue(loop.verify(package, root)["allPassed"])
            with self.assertRaises(ValueError):
                loop.freeze(root, package, ["docs/plan.md"], {})
            (package / "files/docs/plan.md").write_text("changed archive")
            self.assertFalse(loop.verify(package, root)["allPassed"])

    def test_done_with_missing_prerequisite_or_finding_is_rejected(self):
        for state in [
            {"status": "DONE"},
            {"status": "DONE", "blockingFindingIds": ["synthetic-F01"]},
            {"status": "DONE", "dependencies": [{"status": "BLOCKIERT"}]},
            {"status": "RUNNING", "checks": {"review": "durchgeführt"}},
        ]:
            with self.subTest(state=state):
                self.assertTrue(loop.validate_state(state))
        self.assertEqual(loop.validate_state({"status": "RUNNING", "checks": {"review": "NICHT_GEPRÜFT"}}), [])

    def test_internal_file_and_directory_aliases_are_rejected_before_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            for forbidden in ["data/raw", "data/local", "outputs", "node_modules", ".agents"]:
                target = root / forbidden
                target.mkdir(parents=True)
                (target / "synthetic.txt").write_text("synthetic protected placeholder")
                alias = root / "docs" / (forbidden.replace("/", "-") + "-alias")
                alias.symlink_to(target, target_is_directory=True)
                output = root / "reports/loop/packages/unit/v1"
                with self.subTest(forbidden=forbidden), self.assertRaises(ValueError):
                    loop.freeze(root, output, [str(alias.relative_to(root)) + "/synthetic.txt"], {})
                self.assertFalse(output.exists())
            for target_name in [".env.synthetic", "docs/public.txt"]:
                target = root / target_name
                target.write_text("synthetic placeholder")
                alias = root / "docs" / ("secret" if target_name.startswith(".env") else "public")
                alias.symlink_to(target)
                with self.assertRaises(ValueError):
                    loop.public_input(root, str(alias.relative_to(root)))

    def test_output_anchor_and_archive_aliases_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs/plan.md").write_text("synthetic plan")
            (root / "reports/loop").mkdir(parents=True)
            (root / "reports/loop/packages").symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                loop.freeze(root, root / "reports/loop/packages/unit/v1", ["docs/plan.md"], {})
            self.assertEqual(list(Path(outside).iterdir()), [])
        for alias in ["files", "files/docs", "files/docs/plan.md", "manifest.json"]:
            with self.subTest(alias=alias), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "docs").mkdir()
                source = root / "docs/plan.md"
                source.write_text("synthetic plan")
                package = root / "reports/loop/packages/unit/v1"
                loop.freeze(root, package, ["docs/plan.md"], {})
                target = package / alias
                # Preserve synthetic original, redirect path to another location.
                saved = target.with_name(target.name + "-original")
                target.rename(saved)
                target.symlink_to(saved, target_is_directory=saved.is_dir())
                with self.assertRaises(ValueError):
                    loop.verify(package, root)

    def test_normalized_duplicates_and_empty_archives_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs/plan.md").write_text("synthetic plan")
            package = root / "reports/loop/packages/unit/v1"
            for names in [[], ["docs/plan.md", "docs//plan.md"]]:
                with self.assertRaises(ValueError):
                    loop.freeze(root, package, names, {})
                self.assertFalse(package.exists())

    def complete_fixture(self, root):
        (root / "docs").mkdir()
        (root / "docs/plan.md").write_text("synthetic plan only, not scientific evidence")
        package = root / "reports/loop/packages/unit/v1"
        loop.freeze(root, package, ["docs/plan.md"], {})
        manifest = package / "manifest.json"
        sha = hashlib.sha256(manifest.read_bytes()).hexdigest()
        state = {"status": "DONE", "completionEvidence": {}}
        for phase in ["setup", "release"] + ["phase-" + str(i) for i in range(10)]:
            report = root / "reports/loop" / (phase + "-acceptance.json")
            report.write_text(json.dumps({"phase": phase, "status": "BESTANDEN",
                "manifestSha256": sha, "scope": "synthetic formal fixture, not real acceptance",
                "checks": [{"status": "BESTANDEN", "evidence": "synthetic fixture"}]}))
            state["completionEvidence"][phase] = {"status": "BESTANDEN", "manifest": str(manifest.relative_to(root)),
                "manifestSha256": sha, "report": str(report.relative_to(root)),
                "reportSha256": hashlib.sha256(report.read_bytes()).hexdigest()}
        return state

    def test_done_rejects_each_open_requirement_with_otherwise_bound_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = self.complete_fixture(root)
            self.assertEqual(loop.validate_state(state, root), [])
            cases = [{"checks": {"empirical": status}} for status in loop.CHECK_STATUSES - {"BESTANDEN"}]
            cases += [{"dependencies": [{"id": "human", "status": status}]} for status in
                ["IN_DIESER_PHASE_NICHT_ERFORDERLICH", "BLOCKIERT", "unknown"]]
            cases += [{"workPackages": [{"id": "work", "status": "RUNNING"}]},
                {"activeAgents": [{"name": "synthetic-active-agent"}]},
                {"blockingFindingIds": ["synthetic-F01"]}]
            for change in cases:
                case = copy.deepcopy(state)
                case.update(change)
                with self.subTest(change=change):
                    self.assertTrue(loop.validate_state(case, root))
            self.assertTrue(loop.validate_state({"status": "RUNNING", "dependencies": [{"status": "unknown"}]}, root))

    def test_done_rejects_fabricated_missing_mismatched_or_tampered_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = self.complete_fixture(root)
            for change in [{"manifestSha256": "x" * 64}, {"manifestSha256": "0" * 64},
                {"manifest": "reports/loop/packages/missing/manifest.json"},
                {"report": "reports/loop/missing.json"}, {"reportSha256": "0" * 64},
                {"report": state["completionEvidence"]["release"]["report"],
                 "reportSha256": state["completionEvidence"]["release"]["reportSha256"]}]:
                case = copy.deepcopy(state)
                case["completionEvidence"]["setup"].update(change)
                with self.subTest(change=change):
                    self.assertTrue(loop.validate_state(case, root))
            report = root / state["completionEvidence"]["setup"]["report"]
            value = json.loads(report.read_text())
            value["manifestSha256"] = "0" * 64
            report.write_text(json.dumps(value))
            case = copy.deepcopy(state)
            case["completionEvidence"]["setup"]["reportSha256"] = loop.digest(report)
            self.assertTrue(loop.validate_state(case, root))
            (root / "reports/loop/packages/unit/v1/files/docs/plan.md").write_text("tampered synthetic archive")
            self.assertTrue(loop.validate_state(state, root))

if __name__ == "__main__":
    unittest.main()
