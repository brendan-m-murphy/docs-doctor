#!/usr/bin/env python3
"""Preview or install docs-doctor skills and a policy starter in a repository."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


def digest(path: Path) -> str:
    """Return a stable digest for one file or directory tree."""
    result = hashlib.sha256()
    paths = [path] if path.is_file() else sorted(item for item in path.rglob("*") if item.is_file())
    for item in paths:
        result.update(str(item.relative_to(path.parent if path.is_file() else path)).encode())
        result.update(item.read_bytes())
    return result.hexdigest()


def main() -> int:
    """Run the adopter bootstrap."""
    source_root = Path(__file__).resolve().parents[1]
    skills_root = source_root / ".agents" / "skills"
    available = sorted(path.name for path in skills_root.iterdir() if (path / "SKILL.md").is_file())

    parser = argparse.ArgumentParser(
        description="Preview or install docs-doctor skills and a documentation policy starter."
    )
    parser.add_argument("target", type=Path, help="Existing repository directory")
    parser.add_argument(
        "--skill",
        action="append",
        choices=available,
        help="Skill to install; repeat as needed. Defaults to all skills.",
    )
    parser.add_argument("--no-policy", action="store_true", help="Do not create the policy starter")
    parser.add_argument("--write", action="store_true", help="Apply the previewed changes")
    args = parser.parse_args()

    target = args.target.resolve()
    if not target.is_dir():
        parser.error(f"target is not an existing directory: {target}")

    names = list(dict.fromkeys(args.skill or available))
    operations = [(skills_root / name, target / ".agents" / "skills" / name) for name in names]
    policy_destination = target / "docs" / "documentation-policy.md"
    if not args.no_policy:
        operations.append(
            (source_root / "templates" / "documentation-policy.md", policy_destination)
        )

    planned: list[tuple[Path, Path]] = []
    conflicts: list[Path] = []
    for source, destination in operations:
        relative = destination.relative_to(target)
        if not destination.exists() and not destination.is_symlink():
            print(f"CREATE    {relative}")
            planned.append((source, destination))
        elif source.is_dir() == destination.is_dir() and digest(source) == digest(destination):
            print(f"UNCHANGED {relative}")
        else:
            print(f"CONFLICT  {relative}")
            conflicts.append(destination)

    if conflicts:
        print("No files written. Resolve conflicts or use --no-policy when policy already exists.")
        return 2
    if not args.write:
        print("Preview only. Re-run with --write to apply these changes.")
        return 0

    for source, destination in planned:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)

    print("Adoption files installed without overwriting existing content.")
    if args.no_policy:
        print("Next: link the installed skills to your repository's documentation policy.")
    else:
        policy_path = policy_destination.relative_to(target)
        print(f"Next: complete {policy_path} and link it from AGENTS.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
