# Tooling and enforcement

Tools enforce selected repository decisions; they do not choose the decisions.

| Tool | Useful evidence | Not established |
| --- | --- | --- |
| [Ruff](https://docs.astral.sh/ruff/rules/#pydocstyle-d) | Python docstring presence, form, and selected signature agreement | Semantic accuracy or a complete scientific contract |
| Sphinx or MkDocs | Parse, build, cross-reference, generated API, and rendered-page behaviour | Reader success or scientific validity |
| [Vale](https://vale.sh/docs/) | Adopted terminology and markup-aware prose patterns | Diátaxis fit, factual correctness, accessibility compliance, or clear mathematics |
| Pytest, doctest, or notebook execution | Current example behaviour and tested invariants | Every supported environment or interpretation |

## Ruff docstring checks

Prefer the repository's existing Ruff installation. For a Google-style project, a
conservative initial policy might be:

```toml
[tool.ruff.lint]
extend-select = ["D100", "D101", "D102", "D103", "D104", "D417"]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

Select rules from the project's policy rather than copying this example blindly. In
particular, do not require `D107` when constructor arguments are canonically documented
on the class. Trial Ruff's preview `DOC` rules as advisory evidence before making them
blocking.

Measure the existing production and test baselines separately. Clean a manageable
production baseline, then enforce it. For legacy tests, begin with changed files or a
bounded cleanup rather than adding a large ignore ledger.

## Vale

Vale is a standalone binary, not a Python dependency. Keep its configuration and rules
in the repository whose terminology they govern. Start with a few tested rules:

- errors for objectively incorrect project or API spellings with a safe correction;
- warnings for adopted conventions that still need interpretation; and
- suggestions for phrases that might obscure conditions or dismiss a reader's
  difficulty.

Do not automatically rewrite scientific qualifications, uncertainty, causality,
equations, identifiers, or code. Run Vale on changed prose first; use scheduled
whole-tree reports to measure older debt.

This repository's [`.vale.ini`](../.vale.ini) and
[`DocsDoctor` rules](../.vale/styles/DocsDoctor) are deliberately small. They test
project spelling and prompt review of a few dismissive expressions. They are examples,
not a reusable universal style.

Configure the adopter's actual source formats. For a mixed Markdown and
reStructuredText project, for example:

```ini
[*.{md,rst}]
BasedOnStyles = ProjectStyle
```

The fixtures under [`tests/vale`](../tests/vale) contain clean and deliberately failing
inputs in Markdown and reStructuredText. Likewise, [`tests/ruff`](../tests/ruff) tests a
small Google docstring rule selection without making it the repository's Python policy.

Run the clean fixtures directly with installed tools:

```bash
vale tests/vale/pass
uvx --from ruff==0.16.0 ruff check \
  --no-cache --config tests/ruff/ruff.toml tests/ruff/pass
```

The matching `fail` fixtures must report both intended Vale rule classes and all six
selected Ruff rules, respectively. They verify that the checks can fail for the intended
reasons, not only that clean prose passes. Vale fixtures cover both Markdown and
reStructuredText.

## Documentation builds

Use the strict build already defined by an adopter and direct generated output to a
temporary directory during read-only assessment. A pull-request build should include
changes to documentation configuration, source pages, Python docstrings, and public
API exposure.

Generate API stubs into a temporary directory before replacing checked-in files. This
reveals stale modules without destroying authored introductions stored beside generated
content. Keep the generated/authored boundary explicit.

Run external link checks on a schedule or before release unless the repository controls
the targets. Network failures and rate limits make them poor default merge gates.
