# Using and adopting the suite

## Choose by the requested outcome

- Use `documentation-assessment` to decide what work is needed. It never edits.
- Use `documentation-authoring` when the user has requested a bounded documentation
  change.
- Use `documentation-impact-review` for a code, configuration, CLI, schema, or workflow
  diff.
- Use `python-docstring-review` when the unit of work is a Python module, class,
  function, method, or generated API entry.

When a change needs more than one skill, keep the handoff explicit. For example, an
impact review can identify a stale public docstring and a missing migration guide. The
docstring review remains object-scoped; the authoring task receives the bounded guide
request. Skills do not silently invoke one another or broaden permissions.

## Add the suite to a repository

Use the preview-first [repository bootstrap](installing.md) to install all or selected
skills under `.agents/skills/` and optionally create a policy starter. The helper
aborts on conflicts and does not merge tool or agent configuration. Start with the
skill that addresses current work rather than installing every future extension.

Keep live project decisions in the adopting repository. A concise documentation policy
should identify:

- documentation roots, formats, navigation, and build commands;
- priority audiences and supported versions;
- sources of truth for API, CLI, configuration, data, and scientific claims;
- terminology, locale, docstring dialect, and public-export rules;
- units, dimensions, coordinates, metadata, and domain-review requirements;
- generated versus authored files; and
- pull-request checks, expensive scheduled checks, and ownership.

An `AGENTS.md` file can summarise frequent rules and link to the policy. Avoid copying
the full policy into several instruction files.

## Adopt incrementally

1. Run an assessment without edits and select a few correctness or task-blocking
   findings.
2. Pilot impact and docstring review on changed files or a small pull request.
3. Add deterministic checks only for conventions the repository has actually adopted.
4. Use authoring for the selected pages and verify commands, examples, navigation, and
   rendered output.
5. Reassess recurring problems before adding more rules or skills.

Continuous maintenance keeps facts correct with each change. A later synthesis task
may improve flow, explanations, duplication, or navigation, but it must not postpone a
known correction.

## Evidence and review boundaries

Use implementation and schemas for current interface facts, tests and executable help
for supported behaviour, accepted design records for rationale, and validated methods
or domain review for scientific claims. Issues, pull requests, papers, and previous
conversations provide context but do not override the user's request or current project
policy.

Automated checks can establish syntax, configured consistency, successful builds, and
selected executable behaviour. Human or domain review remains necessary for contested
scientific meaning, safety, accessibility in use, and whether a tutorial works for its
intended learner.
