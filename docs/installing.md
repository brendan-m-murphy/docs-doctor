# Install and adopt docs-doctor

There are two useful installation scopes. Choose one; neither changes a project's
documentation policy or tool configuration automatically.

## Install for one repository

Clone or download `docs-doctor`, then preview the repository bootstrap:

```bash
python3 /path/to/docs-doctor/scripts/adopt.py /path/to/project
```

The preview reports every destination as `CREATE`, `UNCHANGED`, or `CONFLICT` and does
not write files. Apply an acceptable preview with:

```bash
python3 /path/to/docs-doctor/scripts/adopt.py /path/to/project --write
```

This installs the four skills under `.agents/skills/` and creates
`docs/documentation-policy.md`. It never overwrites different existing content and
aborts before writing if any destination conflicts.

Install only selected skills by repeating `--skill`:

```bash
python3 /path/to/docs-doctor/scripts/adopt.py /path/to/project \
  --skill documentation-impact-review \
  --skill python-docstring-review \
  --no-policy \
  --write
```

Use `--no-policy` when the project already has an equivalent policy. Run `--help` for
the complete command interface.

After installation:

1. Complete or reconcile the documentation policy with the repository's actual
   conventions.
2. Link the policy from `AGENTS.md` if the project uses one.
3. Add only the Ruff, Vale, documentation-build, or example checks the project has
   adopted. See [Tooling and enforcement](tooling.md).
4. Commit the installed files in the target repository so every contributor and agent
   receives the same skills.

The helper deliberately does not edit `AGENTS.md`, `pyproject.toml`, `.vale.ini`, or CI.
Those files express project decisions, and silently merging generic configuration into
them would be unsafe.

## Install for personal use

Once this repository is public on GitHub, ask Codex to use `$skill-installer` to install
one or more skill paths from it. For example:

```text
Use $skill-installer to install these skills from OWNER/docs-doctor:
.agents/skills/documentation-assessment
.agents/skills/documentation-authoring
.agents/skills/documentation-impact-review
.agents/skills/python-docstring-review
```

Restart Codex if newly installed skills do not appear. A personal installation makes
the skills available across projects, but the target repository's own policy remains
authoritative. The [current Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
describes repository, user, and system discovery scopes.

## Update an adopted repository

Pull the latest `docs-doctor`, then run the bootstrap in preview mode again. Identical
destinations are reported as `UNCHANGED`; local edits are reported as `CONFLICT` and
are never replaced. Review upstream and local versions explicitly before updating a
conflict. This makes local policy adaptations visible instead of treating vendored
skills as disposable generated files.

For a personal installation, use the installer again according to its current update
workflow. Do not assume that updating the central copy updates skills already committed
inside another repository.
