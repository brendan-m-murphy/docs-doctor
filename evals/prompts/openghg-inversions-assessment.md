The evaluation harness must first create a disposable clone of the refreshed `devel`
revision. Replace `<local-openghg-inversions-clone>` with an absolute path:

```bash
inversions_eval_root="$(mktemp -d)"
git clone --shared --no-hardlinks \
  <local-openghg-inversions-clone> "$inversions_eval_root/repo"
git -C "$inversions_eval_root/repo" switch --detach \
  2d05ad9ecc92c0693bb878c9321d290af47c49d6
git -C "$inversions_eval_root/repo" status --short
```

The initial status must be clean. Use `$documentation-assessment` from this repository
to assess the documentation in the resulting `$inversions_eval_root/repo` path.

Prioritise documentation work that would help users run, understand, and safely modify
the current RHIME workflows. Include a small needs map and concrete evidence. Treat the
target as read-only, do not install dependencies, and do not alter its existing working
tree. Record branch, HEAD, tracked diff, and untracked paths before and after; they must
be identical.
