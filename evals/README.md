# Behavioural evaluations

Evaluations use realistic repositories and requests to test observable decisions, not
the presence of prescribed headings or phrases.

Each run records:

- skill and version or working-tree state;
- target repository and revision;
- prompt, scope, and allowed side effects;
- required and forbidden outcomes;
- tool availability and evidence checked;
- result, limitations, and instruction changes justified by failures.

The initial targets are `openghg_inversions` and `openghg-run`. Runs are read-only and
write any generated output to temporary directories unless an evaluation explicitly
authorizes an isolated fixture edit.

Initial cases cover repository assessment, docstring contract review, documentation
impact from a CLI/configuration change, bounded how-to authoring in an isolated copy,
preservation of an established non-Google docstring dialect, and a four-skill regression
for reader-context leakage and incorrect canonical placement.

Recorded runs:

- [Initial forward tests](results/2026-09-14-initial-forward-tests.md)
- [Cold-reader and placement regression](results/2026-09-14-cold-reader-placement.md)
- [Public installation and update test](results/2026-09-14-public-installation-update.md)

Keep raw generated builds and disposable clones outside the repository; record only
evidence, outcomes, and instruction changes justified by failures.

The built-in runner fixture keeps its public behavior internally consistent with a
small standard-library test:

```bash
PYTHONPATH=evals/fixtures/builtin-runner-project/src \
  python3 -m unittest discover \
    -s evals/fixtures/builtin-runner-project/tests -p 'test_*.py'
```
