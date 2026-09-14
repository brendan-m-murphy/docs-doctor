"""Repository structure tests for the documentation skill suite."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


class RepositoryTests(unittest.TestCase):
    """Check portable skill layout and internal documentation links."""

    def test_skill_layout(self) -> None:
        """Require each bundled skill to have matching metadata and UI configuration."""
        skills = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        self.assertGreaterEqual(len(skills), 1)

        for skill in skills:
            with self.subTest(skill=skill.name):
                entry = skill / "SKILL.md"
                interface = skill / "agents" / "openai.yaml"
                self.assertTrue(entry.is_file())
                self.assertTrue(interface.is_file())

                text = entry.read_text()
                self.assertTrue(text.startswith("---\n"))
                frontmatter = text.split("---", 2)[1]
                name = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
                description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
                self.assertIsNotNone(name)
                self.assertIsNotNone(description)
                self.assertEqual(name.group(1), skill.name)

    def test_local_markdown_links(self) -> None:
        """Require relative links in maintained Markdown documents to resolve."""
        roots = [ROOT / "README.md", ROOT / "docs", ROOT / "design", ROOT / "evals"]
        documents = [roots[0]]
        for directory in roots[1:]:
            documents.extend(directory.rglob("*.md"))

        failures: list[str] = []
        for document in documents:
            for destination in MARKDOWN_LINK.findall(document.read_text()):
                if destination.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path_text = destination.split("#", 1)[0]
                if path_text and not (document.parent / path_text).resolve().exists():
                    failures.append(f"{document.relative_to(ROOT)} -> {destination}")

        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
