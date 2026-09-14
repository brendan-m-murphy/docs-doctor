# OpenGHG docstring-policy pilot

- Date: 2026-09-14
- Repository: `openghg/openghg`
- Audited revision: `4223b11`
- Tracking issue: [OpenGHG 1737](https://github.com/openghg/openghg/issues/1737)
- Draft change: [OpenGHG PR 1738](https://github.com/openghg/openghg/pull/1738)

## Policy result

The existing developer guide names Google style but leaves repository choices implicit.
PR 1730 proposes useful agent guidance, although it is a stacked draft and is not the
right canonical location for the full policy. The pilot adds a short developer page
covering public-export evidence, scientific contracts, private helpers and tests,
constructor placement, inheritance, caller-relevant exceptions, maintenance triggers,
and the boundary between lint and semantic review.

## Measured Ruff baseline

The baseline used the repository-pinned Ruff 0.16.2 release.

| Area | Rule | Findings | Decision |
| --- | --- | ---: | --- |
| Production | `D101`–`D103` | 0 | Enable as a blocking ratchet |
| Tests | `D101`–`D103` | 346 | Exempt mechanically; apply policy to new and materially changed tests |
| Production | `D100` | 1 | Defer until module coverage is resolved |
| Production | `D104` | 30 | Defer until generated package-reference needs are resolved |
| Production | `D417` | 98 | Defer; trial signature completeness separately |
| Production | `D419` | 6 | Clean up in bounded follow-up changes before enabling |

The ratchet cannot determine whether an existing docstring is true, complete, or useful.
The `python-docstring-review` skill remains responsible for comparing changed contracts
with signatures, annotations, exports, source, tests, and generated-reference placement.

## Validation

- `ruff check openghg`: passed with the proposed configuration.
- `ruff format --check openghg`: passed.
- the selected `D101`–`D103` rules against tests: passed with the explicit test
  exception, confirming its scope.
- standalone strict docutils parsing of the new policy page: passed.
- docs-doctor Vale policy on the new page: zero findings.
- full strict Sphinx build: the new page was read without a page-specific warning, then
  the build failed on the existing malformed-docstring, reference, heading, and notebook
  execution baseline.

The broader `ruff check tests` command also reports 80 pre-existing non-docstring
findings. They are unrelated to this policy and were not changed or suppressed.
