# docs-doctor

`docs-doctor` is a small suite of repository skills for creating, assessing, and
maintaining technical and scientific software documentation. It combines
reader-centred judgement with the checks a project already trusts, such as Ruff,
Sphinx, executable examples, and Vale.

## Skills

| Request | Skill | Result |
| --- | --- | --- |
| “What documentation work is needed?” | `documentation-assessment` | Read-only context brief, prioritised findings, and a small needs map when useful |
| “Write or revise this documentation.” | `documentation-authoring` | A bounded, evidence-backed documentation patch with proportionate validation |
| “What documentation does this change affect?” | `documentation-impact-review` | `no impact`, `update now`, or `update now + synthesis` |
| “Review these Python docstrings.” | `python-docstring-review` | Object-level findings or minimal authorised fixes |

The skills live in [`.agents/skills`](.agents/skills). Diátaxis modes remain reader
needs within assessment and authoring; they are not separate skills or required
directories.

## Quick start

Invoke the relevant skill explicitly while the suite is being piloted:

```text
Use $documentation-assessment to audit the getting-started path. Do not edit files.

Use $documentation-impact-review to review this branch against origin/main and make
the documentation updates required for current correctness.

Use $python-docstring-review to review changed public objects. Report findings only.
```

Repository policy remains authoritative. A skill discovers the local documentation
format, terminology, scientific conventions, public API, and validation commands
before applying general guidance.

## Install in another repository

Preview a local installation without changing the target:

```bash
python3 scripts/adopt.py /path/to/project
```

Apply the preview with `--write`. The helper installs the skills and a concise policy
starter, aborts on conflicts, and never overwrites different existing files. See
[Install and adopt docs-doctor](docs/installing.md) for selective installation,
personal Codex installation from GitHub, and updates.

## Documentation

- [Using and adopting the suite](docs/using-the-suite.md)
- [Installation and repository bootstrap](docs/installing.md)
- [Tooling and enforcement](docs/tooling.md)
- [Research synthesis](design/research-synthesis.md)
- [Repository and evaluation plan](design/repository-plan.md)
- [Source landscape](design/source-landscape.md)

## Development status

The four skills are implemented, published, and structurally validated. Behavioural
evaluation uses isolated copies of `openghg_inversions` and `openghg-run` so their
existing working trees are not contaminated. Initial evaluations and independent
cold-reader regressions are complete; adopter pilots and remaining work are tracked in
[GitHub issues](https://github.com/brendan-m-murphy/docs-doctor/issues). Evaluation
prompts and results live under [`evals`](evals/README.md).

Vale checks this repository's own terminology and a small set of reader-language
prompts. Those rules are local examples, not a style package to impose on adopters.
Run:

```bash
vale README.md docs .agents/skills
```

Validate a changed skill with Codex's skill validator:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  .agents/skills/<skill-name>
```

Run the deterministic clean fixtures with Vale and an isolated pinned Ruff runner:

```bash
vale tests/vale/pass
uvx --from ruff==0.16.0 ruff check \
  --no-cache --config tests/ruff/ruff.toml tests/ruff/pass
```

Run the repository and bootstrap tests with the standard library:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

No documentation linter proves factual correctness, accessibility, scientific
validity, or reader success. The skills report the evidence actually checked and the
review still required.

## License

This project is available under the [MIT License](LICENSE).
