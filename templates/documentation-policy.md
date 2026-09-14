# Documentation policy

<!-- Replace bracketed prompts, then remove this comment. -->

## Scope and readers

- Supported versions: [versions or release policy]
- Priority readers: [audiences and their starting knowledge]
- Important tasks and consequences of failure: [tasks and risks]

## Documentation structure

- Source roots and formats: [paths and Markdown, reStructuredText, or notebooks]
- Navigation entry points: [files]
- Authored and generated boundaries: [what is generated and where]
- Local preview and strict build commands: [commands]

Diátaxis modes describe reader needs; they do not require four directories.

## Sources of truth

- Python API and public exports: [source]
- Command-line interface and configuration: [source]
- Supported environments and versions: [source]
- Scientific or numerical claims: [source and required reviewer]
- Design rationale: [accepted decision records]

## Language and terminology

- Locale: [locale]
- Project names and preferred terms: [terms or vocabulary file]
- Accessibility or localisation requirements: [requirements]

Preserve exact identifiers, equations, units, qualifications, and uncertainty.

## Python docstrings

- Dialect: [Google, numpydoc, Sphinx, or other]
- Public-object rule: [how public status is determined and what must be documented]
- Modules, packages, constructors, inherited methods, and exceptions: [decisions]
- Scientific contracts: [units, shapes, dimensions, coordinates, metadata, and limits]
- Ruff checks: [configured rules and command]

## Prose checks

- Vale configuration and command: [configuration or not adopted]
- Blocking rules: [objective project rules]
- Advisory rules: [review prompts]

Automated prose checks do not establish factual correctness, scientific validity,
accessibility in use, or reader success.

## Maintenance

Every user-visible change records one documentation-impact outcome:

- `no impact`
- `update now`
- `update now + synthesis`

Known-false current documentation is corrected with the change. A synthesis task may
defer broader restructuring, consolidation, or explanation. Record ownership, pull-
request checks, scheduled checks, and domain-review requirements here.
