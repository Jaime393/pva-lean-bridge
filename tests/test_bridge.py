import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bridge", ROOT / "cli.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "paper.tex"
        self.path.write_text("\\begin{theorem}First line\nSecond line\\end{theorem}")

    def test_source_is_not_proved(self):
        r = MODULE.build_backlog(self.path)
        self.assertEqual(r["distinct_statements"], 1)
        self.assertFalse(r["original_claims_proved"])
        self.assertFalse(r["lean_compilation_executed"])
        self.assertFalse(r["files_written"])

    def test_content_ids_and_duplicate_occurrences(self):
        content = self.path.read_text()
        self.path.write_text(content + "\n" + content)
        r = MODULE.build_backlog(self.path)
        self.assertEqual(r["statement_occurrences"], 2)
        self.assertEqual(r["distinct_statements"], 1)
        self.assertEqual(r["statements"][0]["occurrences"], 2)

    def test_all_generated_source_is_comment(self):
        output = Path(self.temp.name) / "out"
        r = MODULE.build_backlog(self.path, output)
        code = (output / r["statements"][0]["file"]).read_text()
        self.assertTrue(all(line.startswith("--") for line in code.splitlines()))
        self.assertNotIn(":= by", code)

    def test_no_overwrite(self):
        output = Path(self.temp.name) / "out"
        output.mkdir()
        sentinel = output / "sentinel"
        sentinel.write_text("preserve")
        with self.assertRaises(ValueError):
            MODULE.build_backlog(self.path, output)
        self.assertEqual(sentinel.read_text(), "preserve")

    def test_missing_source_not_created(self):
        missing = Path(self.temp.name) / "missing.tex"
        with self.assertRaises(ValueError):
            MODULE.build_backlog(missing)
        self.assertFalse(missing.exists())

    def test_commented_environment_ignored(self):
        self.path.write_text("% \\begin{theorem}Hidden\\end{theorem}\n")
        self.assertEqual(MODULE.build_backlog(self.path)["distinct_statements"], 0)

    def test_wrapper_matches_canonical(self):
        values = []
        for script in (ROOT / "cli.py", ROOT / "scripts/bridge.py"):
            p = subprocess.run([sys.executable, str(script), "--tex", str(self.path)],
                               capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            values.append(json.loads(p.stdout))
        self.assertEqual(*values)


if __name__ == "__main__":
    unittest.main()
