# OpenGHG PR 1720 docstring-review pilot

- Date: 2026-09-14
- Pull request: [OpenGHG 1720](https://github.com/openghg/openghg/pull/1720)
- Mode: assessment only
- Policy: proposed canonical OpenGHG policy in
  [PR 1738](https://github.com/openghg/openghg/pull/1738)

## Scope and evidence

The review covered the changed `DataSchema` implementation, its export, focused tests,
and the accompanying data-specification page. `DataSchema` remains public through
`openghg.store`, while the refactor deliberately preserves an unusual caller-visible
exception split: schema-library failures become OpenGHG `ValidationError`, but a missing
dimension on a required variable remains `ValueError`.

## Findings

1. `openghg/store/_data_schema.py:DataSchema` · public class and constructor policy ·
   the replacement one-line docstring calls the class a compatibility wrapper but does
   not describe `data_vars`, `dtypes`, or `dims`, although those fields define the
   validation contract and are still the public constructor · generated API readers
   cannot configure the class without leaving the reference · document those fields in
   the class docstring, including the dimension-membership and optional-coordinate
   semantics, and link to the longer data-specification page rather than duplicating it.
2. `openghg/store/_data_schema.py:DataSchema.validate_data` · public method and relevant
   exception policy · the one-line docstring does not name the input or the intentional
   `ValidationError` versus `ValueError` outcomes that the PR body, authored page, and
   new tests explicitly preserve · callers cannot tell which recovery branch applies
   from generated API reference · add `Args` and `Raises` entries for the two public
   outcomes.
3. `openghg/store/_data_schema.py:_check_dims` and the three new tests in
   `tests/store/test_data_schema.py` · private-helper and changed-test policy · the helper
   owns the preserved missing-dimension exception behaviour, while the tests distinguish
   three compatibility cases, but none has a docstring · their maintenance intent is
   not recorded beside the executable contract · add one meaningful sentence to the
   helper and each new test.

## Tool comparison

The proposed Ruff `D101`–`D103` ratchet passes because the public objects contain
docstrings and `_check_dims` is syntactically private. That result is correct for the
mechanical question Ruff answers, but it misses all three semantic findings. The
`python-docstring-review` workflow adds value by checking exports, caller-visible
exceptions, tests, and generated-reference context.

The authored `data_spec.rst` page explains the preserved behaviour well. It complements
the API reference but does not remove the need for a usable local contract: readers can
land directly on generated class and method entries. A concise class/method contract
plus a link is sufficient; the docstring need not reproduce the full page.
