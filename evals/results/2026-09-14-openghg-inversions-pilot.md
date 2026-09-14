# Refreshed `openghg_inversions` pilot

- Date: 2026-09-14
- Default branch: `devel`
- Audited revision: `2d05ad9ecc92c0693bb878c9321d290af47c49d6`
- Live checkout: read-only; its feature branch and pre-existing untracked files were
  preserved

## Revalidation

The default-branch revision is unchanged from the initial forward evaluation, so its
verified findings remain current. Open pull requests change the coordination picture:

- [PR 626](https://github.com/openghg/openghg_inversions/pull/626) owns executable
  standard and multisector tutorials;
- [PR 673](https://github.com/openghg/openghg_inversions/pull/673) and
  [PR 674](https://github.com/openghg/openghg_inversions/pull/674) add specialised
  likelihood material to the customisation guide; and
- [PR 649](https://github.com/openghg/openghg_inversions/pull/649) owns release
  automation and maintainer guidance.

The pilot did not duplicate those changes. The smallest independent correction was the
invalid heading hierarchy in the concrete-model explanation. It was reviewed and
merged in [PR 677](https://github.com/openghg/openghg_inversions/pull/677) as
`df581dcc`.

## Current needs map

| Scope | Audience and state | Need | Mode | Current coverage and evidence | Validation | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| First standard or multisector RHIME run | Scientist new to modern RHIME | Reach a small successful inversion from supported inputs | Tutorial | The base branch lacks a short start-to-success route; PR 626 adds executable tutorials and fixtures | Exercise recorded tutorial commands and expected outputs | High until PR 626 lands |
| Likelihood customisation | Model developer who understands the standard runner | Choose a supported seam and change one likelihood safely | How-to | `customising_rhime.rst` provides the main seam; PRs 673 and 674 add specialised routes but still have context and placement gaps | Cold-reader check, focused numerical tests, domain review | High within active PRs |
| Concrete RHIME graph | Scientific reviewer or model developer | Understand equations, graph names, assumptions, and alternatives | Explanation | `concrete_rhime_model.rst` is the canonical detailed explanation; its invalid subsection hierarchy was fixed in PR 677 | Targeted Sphinx build and rendered heading inspection | Immediate defect resolved |
| Python interfaces | Developer using or extending public objects | Find accurate signatures and caller contracts | Reference | Generated stubs expose a broad API, while the strict build reports docstring parse errors and many unresolved targets | API regeneration and strict Sphinx build | High maintenance debt |
| Documentation change workflow | Contributor changing code or docs | Detect broken reference and authored pages before merge | How-to/maintenance | Docs deploy runs on pushes to `devel`, not pull requests; the strict target currently fails on pre-existing warnings | Pull-request docs job with a measured baseline | High |
| RHIME architecture changes | Maintainer or scientific developer | Preserve explicit scientific order and execution boundaries | Explanation/reference | Development guidance and active roadmap are strong and are named in `AGENTS.md` | Focused tests plus scientific review | Covered; preserve and link |

## Cold-reader and placement checks on active work

PR 673 calls `run_rhime_co2_cached_sigma` a “first-class production route” and later
calls the ordinary fixed-OU likelihood a “fallback.” The patch establishes that the
specialised runner is built in and versioned, but it does not identify “production” as
API support, project recommendation, or operational adoption. The visible code path
also does not establish an automatic fallback. The smallest correction is to state the
supported interface and availability directly, and to use “remains available” unless a
real fallback transition is implemented and tested. “Matched” should name the graph,
sampler, and cache invariant it relates rather than relying on shared author context.

PR 674 places a partial call to `run_rhime_from_prepared_inputs` in the customisation
how-to, but the snippet depends on undefined `prepared`, `run_spec`, `artifact`, and
`prepared_identity`. It neither constructs the reusable artifact nor links to a
complete preparation procedure. A reader landing on the page cannot perform the task.
The bounded remedy is either a complete, tested setup path with the artifact-creation
step, or canonical reference/explanation for the specialised component with a short
contextual link from the customisation guide.

These are semantic context and placement findings, not reasons to add Vale rules for
the words “production,” “matched,” or “fallback.” The likelihood mathematics, prior
scales, cache identity, and numerical guarantees require the existing scientific and
numerical review; this pilot does not edit them.

## Build evidence

A strict Sphinx baseline in an isolated checkout reproduced the two level-skip errors
in `docs/usage/concrete_rhime_model.rst`. It also reported two unrelated docstring parse
errors and hundreds of pre-existing unresolved-reference warnings. After changing only
the two subsection underline styles, a targeted Sphinx build succeeded and rendered
both as third-level HTML headings. All pull-request checks passed, and maintainer review
accepted the repair without changes. The broader warning backlog and missing
pull-request documentation validation are tracked in
[issue 679](https://github.com/openghg/openghg_inversions/issues/679), coordinated with
the incremental-preview work in
[issue 629](https://github.com/openghg/openghg_inversions/issues/629).

No skill change is justified by this pass: the current cold-reader, status-dimension,
and canonical-placement checks identified the observed problems. The bounded repair has
been reviewed, and remaining work is either owned by active pull requests or tracked in
an upstream issue, so the pilot is complete.
