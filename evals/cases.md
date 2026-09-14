# Initial evaluation cases

## Inversions repository assessment

Prompt: [openghg-inversions assessment](prompts/openghg-inversions-assessment.md)

Required outcomes:

- remains read-only and identifies the revision and existing working-tree state;
- produces a small prioritised needs map rather than a page catalogue;
- distinguishes correctness, maintenance/toolchain, and reader-experience problems;
- uses existing repository evidence and reports unavailable validation; and
- does not impose four top-level Diátaxis directories.

## openghg-run docstring review

Prompt: [openghg-run docstrings](prompts/openghg-run-docstrings.md)

Required outcomes:

- discovers Google/Napoleon evidence and the absence of an explicit policy;
- identifies public status and checks semantics beyond missing-docstring counts;
- uses configured Ruff without changing its configuration;
- reports findings only and preserves the live working tree; and
- separates object-level work from broader authored documentation.

## openghg-run change-impact review

Prompt: [openghg-run impact](prompts/openghg-run-impact.md)

Required outcomes:

- identifies affected user contracts across CLI, guides, examples, API, and release
  information;
- returns one defined impact outcome with evidence;
- distinguishes immediate correctness from broader synthesis;
- does not edit the live repository; and
- hands off object-level docstring issues rather than duplicating them.

## Isolated authoring task

Prompt: [development setup authoring](prompts/openghg-run-authoring.md)

Required outcomes:

- edits only the requested page in the isolated clone unless navigation must change;
- targets contributors to an existing checkout rather than repository scaffolding;
- verifies commands and preserves repository-specific environment guidance;
- runs the strict Sphinx build or reports a concrete blocker; and
- does not expand into a site-wide cleanup.

## Dialect preservation fixture

Prompt: [numpydoc dialect conflict](prompts/numpydoc-dialect-conflict.md)

Required outcomes:

- discovers the repository's explicit numpydoc policy and matching Ruff/Sphinx
  configuration;
- does not silently convert one file to Google style;
- identifies the request as a repository policy migration rather than an object-level
  review;
- explains the smallest policy decision and migration scope needed before editing; and
- leaves the fixture unchanged.
