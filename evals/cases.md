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

## Built-in runner context and placement regression

Fixture: [`builtin-runner-project`](fixtures/builtin-runner-project)

Prompts:

- [assessment](prompts/builtin-runner-assessment.md);
- [authoring](prompts/builtin-runner-authoring.md);
- [impact review](prompts/builtin-runner-impact.md); and
- [docstring review](prompts/builtin-runner-docstrings.md).

The evaluator receives the selected prompt and fixture, not these expected outcomes.
Across the four skill scopes, the evaluations should:

- identify that the sampled-timescale comparison and “matched” relationship are not
  introduced for the reader;
- distinguish a supported public export and architectural production recipe from a
  recommended or adopted operational workflow;
- reject “fallback” unless repository evidence establishes fallback behaviour;
- recognise that a built-in runner does not fulfil the customisation page's promise and
  choose a canonical usage home with a short link from the related page;
- make the public docstring describe observable behaviour in its normal API-reference
  context, without demanding a tutorial or duplicated type information;
- preserve the legitimate “production emissions” use and the explicitly supported
  standard workflow; and
- keep docstring and broader page work in their respective skill scopes.
