"""Invarianten für öffentliche Pakete und ehrlichen Abschlussstatus."""
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
            self.assertTrue(loop.verify(package)["allPassed"])
            with self.assertRaises(ValueError):
                loop.freeze(root, package, ["docs/plan.md"], {})
            (package / "files/docs/plan.md").write_text("changed archive")
            self.assertFalse(loop.verify(package)["allPassed"])

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

if __name__ == "__main__":
    unittest.main()
