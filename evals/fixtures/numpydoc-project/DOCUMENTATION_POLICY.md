# Documentation policy

Public Python objects use numpydoc. Types remain in annotations and are not repeated in
parameter descriptions. A dialect change is a repository-wide policy migration: update
this policy, renderer and linter configuration, reference output, and affected public
docstrings together. A file-only task must not create mixed dialects.
