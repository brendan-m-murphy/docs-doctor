# Cold-reader and placement regression

- Date: 2026-09-14
- Suite state: candidate cold-reader and placement upgrade
- Fixture: `evals/fixtures/builtin-runner-project`
- Method: independent agents received one neutral prompt, the selected skill, and the
  fixture. They did not receive `evals/cases.md`, prior findings, or the expected result.

## Outcome

| Skill | Result | Observed decision |
| --- | --- | --- |
| `documentation-assessment` | Pass | Distinguished architectural recipe status from operational recommendation, identified missing runnable guidance and ambiguous comparisons, and failed the page-promise and canonical-home tests. |
| `documentation-authoring` | Pass | Created a dedicated usage page in a disposable copy, updated navigation and the related customisation page, and limited edits to three documentation files. |
| `documentation-impact-review` | Pass | Returned `update now`, required the contradictory status and fallback claims to change, rehomed the built-in route, and handed the object-level review to the docstring skill. |
| `python-docstring-review` | Pass | Replaced the ambiguous production qualifier with observable fixed-OU cached-update behaviour and handed the conflicting page status to broader documentation work. |

The agents did not object to “production emissions,” where the word describes a
scientific category, or to the release-qualified standard workflow identified by public
policy. The regression therefore did not reduce the task to a prohibited-word check.

## Fixture correction during evaluation

The first draft made the toy runner a no-op and named a standard-runner symbol that did
not exist. Independent agents correctly prioritised those simpler factual defects. The
fixture was revised before acceptance: the runner now validates its input, performs a
small deterministic amplitude/state calculation, returns a typed record, and has two
passing standard-library tests. The control page now describes a workflow status rather
than inventing an API.

This correction keeps the evaluated difficulty focused on reader-context leakage,
status dimensions, and canonical placement. It also demonstrates why forward tests
should judge decisions rather than merely look for expected phrases.

## Validation

- Four skill directories passed `quick_validate.py`.
- Repository and link tests passed.
- The fixture's two focused unit tests passed.
- Ruff passed for repository helpers and fixture Python.
- Vale reported no findings across maintained prose and the fixture.

No OpenGHG repository was changed during this evaluation. Authoring edits remained in a
disposable directory under `/tmp`.
