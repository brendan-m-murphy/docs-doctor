---
name: documentation-impact-review
description: Review a code, configuration, CLI, schema, or workflow change for documentation consequences and make bounded same-change updates when authorized. Use for pull-request or diff documentation-impact work; not for a general documentation audit or a standalone Python docstring review.
---

# Documentation impact review

Keep current documentation true when software changes. Return one of `no impact`,
`update now`, or `update now + synthesis`; do not use a future cleanup task to leave
known-false documentation in place.

## Establish authority and scope

- Read applicable repository instructions and documentation policy first.
- Determine whether the request is assessment-only or authorizes edits. Review is not
  permission to change files.
- Identify the requested diff or comparison base. Do not silently review unrelated
  working-tree changes.
- Treat source, schemas, parser definitions, public exports, tests, generated help, and
  accepted design records as evidence according to the claim being checked.
- Treat issue and pull-request prose as context, not as proof of current behaviour.

If the change or base cannot be identified safely, report the missing scope instead of
reviewing an arbitrary diff.

## Trace documentation consequences

Inspect changed behaviour and its callers before searching only for changed names.
Check whether the change alters any of these reader-visible contracts:

- public API names, signatures, defaults, accepted values, or deprecations;
- CLI commands, options, output, exit behaviour, or configuration;
- data formats, schemas, units, dimensions, coordinates, metadata, or missing-data
  behaviour;
- workflows, prerequisites, supported versions, environments, or performance
  expectations;
- errors, warnings, safety, destructive effects, recovery, or security guidance;
- scientific assumptions, uncertainty, interpretation, validation limits, or
  unsupported uses; or
- generated API exposure, examples, tutorials, how-to procedures, reference,
  explanation, release notes, and migration guidance.

Search the documentation by concept and user vocabulary as well as exact identifier.
Inspect navigation and cross-links when a page is added, removed, or renamed.

For changed Python docstrings or a Python-object-only request, produce an explicit
handoff to `python-docstring-review`; do not duplicate its object-level review here.

## Decide the outcome

Use exactly one outcome:

- `no impact`: existing documentation remains correct. Give a short evidence-based
  reason.
- `update now`: correctness-sensitive material must change with the implementation.
- `update now + synthesis`: make or specify the immediate correctness update and
  identify a bounded later improvement to flow, explanation, navigation, or
  consolidation.

Deferred synthesis must name the affected reader need, scope, reason, and trigger.
“Update docs later” is not a useful result.

## Apply bounded edits when authorized

- Change only documentation required to keep the reviewed contract correct.
- Preserve the repository's format, terminology, locale, navigation, and generated-file
  policy.
- Link to an authoritative source instead of maintaining unnecessary copies, while
  retaining enough local context for the reader to act safely.
- Preserve qualifications and uncertainty. Ask for domain review before changing
  disputed scientific meaning.
- Do not expand a focused change into a site reorganization. Record a synthesis handoff
  when broader work is justified.

## Validate proportionately

Use the checks already configured by the repository:

- build the affected documentation or generated help;
- run changed examples, doctests, or focused tests where practical;
- run configured Ruff docstring checks for affected Python files;
- run Vale only when the repository has adopted and configured its rules; and
- inspect the rendered page when layout, mathematics, figures, tables, or navigation
  could change meaning.

Do not install, enable, or broaden a linter during an impact review unless requested.
Report checks run, checks unavailable, and any claims still needing human, domain, or
accessibility review.

## Output

Report:

1. reviewed change scope and authority;
2. outcome;
3. affected reader contracts and documentation locations;
4. edits made, or the smallest required edits in assessment-only mode;
5. validation evidence and limitations; and
6. any bounded synthesis or docstring handoff.
