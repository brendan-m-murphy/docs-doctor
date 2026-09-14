"""Tests for the repository-adoption helper."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "adopt.py"


class AdoptTests(unittest.TestCase):
    """Exercise preview, installation, repeat use, and conflict handling."""

    def run_adopt(self, target: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        """Run the helper against a temporary repository."""
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(target), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_preview_does_not_write(self) -> None:
        """Keep the default mode read-only."""
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            result = self.run_adopt(target)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Preview only", result.stdout)
            self.assertFalse((target / ".agents").exists())
            self.assertFalse((target / "docs").exists())

    def test_write_installs_all_skills_and_policy(self) -> None:
        """Install the default adoption set."""
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            result = self.run_adopt(target, "--write")

            self.assertEqual(result.returncode, 0, result.stderr)
            installed = {path.name for path in (target / ".agents" / "skills").iterdir()}
            expected = {path.name for path in (ROOT / ".agents" / "skills").iterdir()}
            self.assertEqual(installed, expected)
            self.assertTrue((target / "docs" / "documentation-policy.md").is_file())

    def test_selected_skill_can_be_installed_without_policy(self) -> None:
        """Support a small project-specific installation."""
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            result = self.run_adopt(
                target,
                "--skill",
                "python-docstring-review",
                "--no-policy",
                "--write",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            skills = list((target / ".agents" / "skills").iterdir())
            self.assertEqual([path.name for path in skills], ["python-docstring-review"])
            self.assertFalse((target / "docs").exists())

    def test_repeat_is_unchanged(self) -> None:
        """Allow an unchanged installation to be checked again."""
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            self.assertEqual(self.run_adopt(target, "--write").returncode, 0)

            result = self.run_adopt(target, "--write")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("UNCHANGED", result.stdout)

    def test_conflict_aborts_before_writing(self) -> None:
        """Do not partly install when an existing destination differs."""
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            policy = target / "docs" / "documentation-policy.md"
            policy.parent.mkdir(parents=True)
            policy.write_text("Existing policy\n")

            result = self.run_adopt(target, "--write")

            self.assertEqual(result.returncode, 2)
            self.assertIn("CONFLICT", result.stdout)
            self.assertFalse((target / ".agents").exists())
            self.assertEqual(policy.read_text(), "Existing policy\n")


if __name__ == "__main__":
    unittest.main()
