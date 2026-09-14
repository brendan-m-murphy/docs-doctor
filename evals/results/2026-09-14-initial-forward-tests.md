# Initial forward-test results

- Date: 2026-09-14
- Suite state at evaluation: pre-publication four-skill working tree, subsequently
  published in commit `dc8d4b6`
- Targets: refreshed `openghg_inversions` `devel` at `2d05ad9ecc92` and
  `openghg-run` at
  `3944d8abe489`

## Outcome

| Case | Result | Main evidence |
| --- | --- | --- |
| `openghg_inversions` assessment | Pass after one instruction fix | Prioritised five-journey needs map on a pinned refreshed clone; detached HEAD, tracked diff, and untracked paths unchanged |
| `openghg-run` bounded authoring | Pass in an isolated clone | One-page change; 269 tests, Ruff, ty, lock check, CLI help, and strict Sphinx build passed |
| `openghg-run` docstring review | Pass | Six semantic findings; 26 focused tests and strict Sphinx build passed; target unchanged |
| `openghg-run` impact review | Pass | Returned `update now + synthesis`; six focused tests, Ruff, CLI help, and strict Sphinx build passed; target unchanged |
| Numpydoc dialect conflict | Pass | Preserved the adopted dialect, identified repository-wide migration scope, and left the fixture byte-for-byte unchanged |
| Vale and Ruff fixtures | Pass | Markdown/reStructuredText Vale fixtures produced both intended checks; Ruff fixtures exercised all six selected rules |

The first assessment run produced useful content but switched the target from its
working branch to `devel`. The original branch was restored immediately. The skill now
forbids branch switching, staging, target worktrees, and target-local caches; it requires
before-and-after branch and status evidence. An independent rerun passed that boundary.
An independent dialect-conflict run also refused a file-only Google-style conversion
where project policy, Ruff, and Sphinx all selected numpydoc.

## What the cases found

### `openghg_inversions`

The refreshed `devel` documentation is materially stronger than the checked-out feature
branch used in an earlier run: it now has a complete staged workflow, practical
customisation seams, and clear scientific development constraints. The remaining work
is concentrated in onboarding and the build/maintenance boundary. The next cleanup
should:

1. fix the two inconsistent heading levels in `concrete_rhime_model.rst` that the strict
   Sphinx build reports as critical errors;
2. add an explicit, scientifically reviewed likelihood or `mismatch_model` to the
   advertised direct-Python calls, matching the page's own statement that direct calls
   must select one;
3. make the modern packaged template and installed CLI the primary getting-started
   path, moving the detailed HBMCMC route into compatibility guidance;
4. separate generated API stubs from authored reference text and decide whether stubs
   are committed or always regenerated;
5. run the strict documentation target on relevant pull requests, including Python
   source changes; and
6. correct Markdown syntax on the reStructuredText landing page and add one short,
   tested modern start-to-success tutorial.

The longer RHIME, staged-workflow, customisation, and development material should be
preserved and linked from the shorter journeys rather than rewritten wholesale.

### `openghg-run`

The isolated authoring case replaced repository-scaffolding instructions in
`docs/development_setup.md` with a contributor setup path using the repository's actual
Python versions, `uv`, CLI verification, CI commands, strict documentation build, and
lockfile workflow. No live target file was changed; this is a ready bounded task for a
later authorised cleanup.

The docstring review found missing or incomplete contracts around the main render and
create functions, suite resolution, dry-run side effects, override coercion, public data
containers, and apparently public internal types. The impact review found that
`--config-set` is implemented but absent from the case-suite, CLI, run-layout, example,
and release documentation. It also exposed a policy decision: unlike `--set`,
`--config-set` currently bypasses the named-variant guard.

A useful cleanup sequence is:

1. decide whether the two override mechanisms should share the variant policy;
2. document `--config-set` and its run-local patched-file and audit contract;
3. apply the bounded development-setup revision;
4. adopt a short repository docstring policy and fix the reviewed public contracts; and
5. then enable a measured subset of stable Ruff docstring rules.

### `openghg-run` pilot follow-through

The bounded development-setup revision became
[openghg-run PR 68](https://github.com/openghg/openghg-run/pull/68). The submitted change
also corrected the incomplete development command in the README so a contributor could
reach the documented test and documentation tools. Local validation repeated the lock,
Ruff, ty, 269-test, CLI-help, and strict-Sphinx checks; all pull-request checks passed.
Maintainer review found no issues, and the change was squash-merged as `bcbbd185`.

No false positive or missing skill instruction emerged from that review, so the skill
was not changed. The initial impact and docstring findings remained valid but outside
the bounded pull request. They are tracked upstream as:

- [openghg-run issue 70](https://github.com/openghg/openghg-run/issues/70), to decide
  and document the `--config-set` variant policy; and
- [openghg-run issue 71](https://github.com/openghg/openghg-run/issues/71), to adopt a
  docstring policy and improve case API contracts.

## Test boundaries

The live `openghg-run` repository retained its pre-existing untracked `.codex/`
directory. The refreshed `openghg_inversions` assessment ran in a clean disposable clone
at `2d05ad9e`; its complete before/after fingerprint was unchanged, and the user's live
feature branch was untouched. Generated Sphinx and API output went to temporary
directories. Vale was not run inside either adopter because neither has adopted a Vale
configuration.

The strict `openghg_inversions` build reached two reproducible heading-structure errors.
Full validation also encountered host dependency, intersphinx network, and notebook
execution limitations; those environment-dependent messages were not classified as
documentation defects.

See the reusable prompts in [`../prompts`](../prompts) and the case expectations in
[`../cases.md`](../cases.md).
