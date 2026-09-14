The evaluation harness must first create a disposable clone at the recorded revision.
Replace `<local-openghg-run-clone>` with an absolute path:

```bash
run_eval_root="$(mktemp -d)"
git clone --shared --no-hardlinks \
  <local-openghg-run-clone> "$run_eval_root/repo"
git -C "$run_eval_root/repo" switch --detach \
  3944d8abe489a0181bba4973c362dfb908a5f20b
git -C "$run_eval_root/repo" status --short
```

The initial status must be clean. Use `$documentation-authoring` from this repository
to revise `docs/development_setup.md` in the resulting `$run_eval_root/repo` path.

Replace repository-scaffolding instructions with a concise setup guide for a developer
contributing to the existing project. Verify commands against the clone, preserve its
chosen tools and supported Python versions, keep the change bounded, and run the
configured strict documentation build. You are authorized to edit only the isolated
clone. Confirm afterwards that only `docs/development_setup.md` has changed.
