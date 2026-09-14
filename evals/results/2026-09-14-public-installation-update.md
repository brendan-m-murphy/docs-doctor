# Public installation and update test

- Date: 2026-09-14
- Repository: `brendan-m-murphy/docs-doctor`
- Earlier revision: `dc8d4b6abf4c78c295cdf6fda1045067679cba60`
- Current revision: `5356ee291b320dec01a06923be07ed4915e41d51`
- Scope: temporary personal destinations and temporary adopter repositories

## Outcome

| Case | Result | Evidence |
| --- | --- | --- |
| Public personal install | Pass | Codex's GitHub skill installer downloaded all four paths at the pinned current revision. |
| Installed content and structure | Pass | The downloaded tree matched the repository byte for byte, and all four skills passed `quick_validate.py`. |
| Existing destination | Pass | Repeating the install returned exit status 1 and did not overwrite the first existing skill directory. |
| Pinned-revision update | Pass | The initial published revision was moved to a backup, the current revision was installed into the vacated destination, and the result matched current `main`; the distinct backup remained intact. |
| Personal discovery | Pass | The four active laptop copies appear in a later Codex turn's skill catalogue and match the current repository copies byte for byte. |
| Public repository bootstrap | Pass | A fresh public clone produced a read-only preview, installed the four skills and policy, and reported all destinations unchanged on a repeat run. |
| Bootstrap conflict | Pass | A pre-existing different policy caused exit status 2 before any skill was copied; the policy remained unchanged. |

## Commands and observations

The personal cases used Codex's maintained
`install-skill-from-github.py` helper with `--repo brendan-m-murphy/docs-doctor`, four
explicit `--path` values, a pinned `--ref`, and temporary `--dest` directories. The
repository cases ran the downloaded `scripts/adopt.py` first without and then with
`--write`.

The installer has no in-place overwrite mode. A personal update therefore needs an
explicit backup-and-reinstall sequence. This is a useful safety property, but the prior
documentation's instruction to use the installer's “current update workflow” did not
tell a reader what to do. The installation guide now states the tested procedure.

No active personal skill or real adopter repository was changed during these tests.
Temporary backups were retained for inspection.

## Limitations

The repository has no release tag yet, so the test used immutable commit identifiers.
Discovery was confirmed with the active personal installation on a later Codex turn;
the temporary destination was not substituted for the authenticated desktop session's
personal skill root.
