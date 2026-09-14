---
name: python-docstring-review
description: Review or minimally revise Python docstrings affected by a code change using repository policy, public API declarations, source, annotations, and tests. Use for explicit docstring work or policy-required pull-request review; not for tutorials, general prose, or site-wide documentation audits.
---

# Python docstring review

Review the smallest relevant set of modules and objects. Check the caller or maintainer
contract, not only docstring presence and formatting.

## Establish policy and scope

Determine whether the request is assessment-only or authorizes edits. Identify the
explicit files or objects, or the requested diff and comparison base, without absorbing
unrelated working-tree changes.

Resolve policy in this order:

1. applicable repository docstring policy and agent instructions;
2. configured dialect, documentation renderer, linter settings, and consistent nearby
   examples; then
3. policy-neutral PEP 257 structure and useful public-contract checks.

State which authority was used. Never convert Google, numpydoc, Sphinx, or another
dialect without explicit repository or user authority. If local policy and tooling
conflict, report the conflict instead of silently choosing one.

## Determine the reviewed objects

- Use public export declarations, package facades, stubs, generated-reference
  configuration, and documented API pages to determine public status. Naming alone is
  insufficient when the repository defines its surface explicitly.
- Include changed objects whose behaviour, signature, state, or scientific contract
  changed even when their docstring lines did not.
- Include module or package docstrings according to local policy. Without a policy,
  require useful summaries for public modules and packages; do not manufacture a
  filename restatement for every private module.
- Treat inherited documentation as valid when it is accurate and visible. Document an
  override when its contract differs.

## Check semantic contracts

For each relevant object, compare the docstring with annotations, implementation,
tests, examples, and adjacent user documentation. Check only applicable items:

- purpose and observable behaviour;
- parameter meaning, defaults, accepted values, and constraints;
- result or yield meaning, not merely its type;
- state mutation, side effects, caching, cost, and lazy or eager behaviour;
- intentional caller-visible exceptions, warnings, and recovery conditions;
- class responsibility, invariants, lifecycle, constructor inputs, and public
  attributes; and
- scientific units, shapes, dimensions, coordinates, alignment, metadata,
  missing-data treatment, randomness, tolerances, assumptions, limitations, and
  interpretation.

Do not demand every item from every docstring. Require the information a caller or
maintainer needs to use or change that object safely.

## Avoid duplication and misplaced content

- Follow local policy on whether annotations or prose own type information; absent a
  policy, do not repeat annotated types.
- Keep constructor documentation in one repository-selected location rather than
  duplicating the class and `__init__`.
- Do not repeat accurate inherited contracts.
- Reject content-free summaries that merely restate the symbol name.
- Keep tutorials, multi-step workflows, model theory, architecture history, and long
  derivations in authored documentation, with a useful link from the docstring.
- Use comments, not docstrings, for implementation rationale or a local workaround that
  callers do not need.

## Use tools as partial evidence

- Run the repository's configured Ruff checks on the reviewed files. Stable pydocstyle
  `D` rules can check presence and form; enabled `DOC` rules can check selected
  signature relationships.
- Run the affected Sphinx, MkDocs, or API-reference build when practical.
- Run focused tests or examples when they establish described behaviour.
- Run Vale only if the repository has adopted it for docstrings or terminology.

Do not enable new rules, auto-fix prose, or install tools unless requested. A clean
linter result does not prove semantic correctness.

## Report or edit

In assessment mode, report only actionable findings. Each finding contains:

`object and location · policy or authority · evidence · consequence · minimal action`

In edit mode, make the smallest policy-conforming docstring changes, preserve unrelated
code, and rerun focused checks. Do not change behaviour to make it match a docstring
unless the user requested a code change.

Escalate disputed scientific meaning, safety, destructive effects, or public contract
changes to a domain or maintainer review. Hand off broader page work explicitly rather
than expanding this review.

End with the reviewed scope, findings or edits, checks run, checks unavailable, and any
handoff. No findings means only that the declared scope met the checks performed.
