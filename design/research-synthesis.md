# Research synthesis

Status: planning research, reviewed 2026-09-14.

## Conclusions

1. **Diátaxis is the intent layer, not the whole quality system.** It is excellent for
   deciding what kind of help a reader needs now. It does not establish factual
   correctness, accessibility, scientific validity, lifecycle governance, or whether
   users can find and successfully use the result.
2. **Start from user needs, not a page inventory.** Apply the same questions at project,
   component or model, page, section, and change scope. Audience and Diátaxis mode are
   different dimensions.
3. **Use continuous correctness plus periodic synthesis.** A code or configuration
   change must not leave current documentation false. Broader restructuring,
   navigation, and conceptual synthesis can happen at a milestone or scheduled review.
4. **Use plain technical English by default.** ASD-STE100 is valuable for controlled,
   safety-sensitive procedures, but full compliance is too restrictive and costly as
   the universal style for open-source scientific software.
5. **Use four outcome-focused skills.** Assessment, authoring, change-impact review,
   and Python docstring review have different triggers, permissions, evidence, and
   outputs. Diátaxis, scientific writing, accessibility, and tooling remain methods or
   conditional profiles rather than additional skills.
6. **Keep judgement visible.** Agents may check links, builds, examples, terminology,
   and schemas. They must not invent commands, defaults, scientific claims, or evidence,
   and must not claim that a linter proves clarity or controlled-language compliance.
7. **Use a source hierarchy.** Keep universal instructions small. Activate Python
   docstring review and mathematical-exposition guidance only when relevant, and use
   classic writing texts as sources of review questions rather than automatic style
   rules.

## What the prior discussion contributes

The referenced conversation, *Summarize Diátaxis Documentation*
(`6aa6fe60-1bbc-83eb-95a2-f47e58a8fe7e`), is treated as design input rather than as
instructions. Its strongest ideas are retained:

- apply Diátaxis recursively at package and component or model scope;
- inspect existing documentation, code, examples, tests, interfaces, design records,
  issues, and pull requests before asking the user for context;
- distinguish the audience's knowledge from the kind of help they need at a given
  moment;
- keep a small inventory of important user needs and known gaps rather than trying to
  declare a component's documentation “complete”;
- require a documentation-impact assessment for changes;
- allow delayed synthesis, but never use a future documentation issue to justify text
  on the main branch that is already known to be false;
- treat issues, pull requests, papers, and architecture decisions as sources for user
  documentation, not substitutes for it.

These ideas are consistent with Diátaxis's own incremental workflow, but the proposed
maintenance contract goes beyond Diátaxis.

## Diátaxis: what to preserve

[Diátaxis](https://diataxis.fr/) identifies four needs. The
[compass](https://diataxis.fr/compass/) reduces classification to two questions:
action or cognition, and acquisition or application. It can be applied to a user need
or existing content, from a sentence to a whole site.

| Reader need | Mode | Primary success test |
| --- | --- | --- |
| Action while acquiring skill | Tutorial | Can a suitably prepared learner complete a safe, concrete learning journey and see expected results? |
| Action while applying skill | How-to | Can a competent user make progress on a bounded real-world task or problem? |
| Cognition while applying skill | Reference | Can a user obtain an authoritative, precise fact while working? |
| Cognition while acquiring skill | Explanation | Does the material connect ideas and improve understanding of a bounded “why?” question? |

Mode-specific consequences:

- [Tutorials](https://diataxis.fr/tutorials/) need small, concrete actions, visible
  results, a narrative of expected outcomes, few choices, and little explanation. They
  are pedagogical products and expensive to keep reliable end to end.
- [How-to guides](https://diataxis.fr/how-to-guides/) organise around a user's goal or
  problem, not around a tool. They may branch and require judgement; they optimise for
  useful sufficiency rather than completeness.
- [Reference](https://diataxis.fr/reference/) should be neutral, consistent,
  authoritative, and shaped by the logical structure of what it describes. Generated
  API facts can reduce drift, but generated reference is not a complete documentation
  set.
- [Explanation](https://diataxis.fr/explanation/) provides context, rationale,
  alternatives, constraints, and connections. Its boundary should be a meaningful topic
  or “why?” question.

### Important cautions

Diátaxis explicitly says to use it as a guide rather than a top-down plan, to avoid
creating empty quadrant structures, and to improve bounded pieces incrementally. Good
structure should emerge from well-formed content rather than be imposed for visual
symmetry. See [Diátaxis as a guide to work](https://diataxis.fr/how-to-use-diataxis/).

A page can have a dominant purpose without being isolated. Split mixed material only
when competing purposes interfere with the reader; otherwise use headings and links.
Navigation may reasonably be organised by audience, workflow, scientific domain, or
subsystem rather than by four top-level Diátaxis labels.

Do not force every project record into the four modes. Architecture decisions, release
notes, contribution policy, governance records, and internal plans can support user
documentation without themselves being tutorials, how-tos, reference, or explanation.

Diátaxis also distinguishes measurable functional qualities, such as accuracy,
completeness, consistency, usefulness, and precision, from experiential or “deep”
qualities such as flow and fit to human needs. It explicitly does not deliver functional
quality by itself. See its [quality discussion](https://diataxis.fr/quality/).

## Corrected Dane Hillard source

The initial attachment, *Practices of the Python Pro*, was the wrong book. The intended
source is Dane Hillard, [*Publishing Python Packages*](https://www.manning.com/books/publishing-python-packages),
Manning, December 2022, ISBN 978-1-61729-991-9. The user supplied the chapter text
visible through their authenticated O'Reilly view for Chapter 8, “Authoring and
maintaining documentation”. The copyrighted chapter was reviewed and summarised, not
copied into the repository. The user's printed-page references—128–130 and 153–157—
identify its opening section 8.1 and final section 8.4. The superseded PDF is not used
as documentation evidence below.

### What section 8.1 contributes

Section 8.1 introduces four recurring user goals that correspond to tutorial, how-to,
reference, and explanation. It argues that presentation should be organised for the
reader's goal and that a documentation system must support both prose and extracted
code documentation with clear boundaries and links.

This supports the current design, with two qualifications:

- the chapter uses the older label “discussion”; current Diátaxis uses “explanation”;
- “one goal at a time” should mean a dominant user need, not an automatic requirement
  to split every page containing a small amount of adjacent material.

Its Sphinx, reStructuredText, tox, and Read the Docs path is a useful worked example of
one Python documentation stack, not a technology mandate for the future skill.

### What section 8.4 contributes

The final section provides practical guidance that complements Diátaxis:

- choose what to expose from audience needs: end users generally need the intentional
  public interface, while maintainers may also need difficult implementation details,
  constraints, design history, and rationale;
- prioritise documentation that users most need instead of attempting indiscriminate
  coverage;
- link to the authoritative documentation of dependencies rather than maintaining a
  competing copy of their detail;
- use consistent, factual, empathetic language and treat words such as “easy”,
  “obvious”, “just”, “magic”, and unqualified “fast” or “slow” as prompts to check the
  evidence and reader effect, not as universally prohibited vocabulary;
- assume that search may land a reader directly on any page, so state prerequisites
  and local context or link to them explicitly;
- use focused paragraphs, meaningful lists, parallel structure, figures, and other
  aids when they reduce cognitive load; and
- reduce maintenance friction with cross-references, generated public API reference,
  executable examples, previews, and a documentation-impact check when code changes.

Some advice needs modern or project-specific qualification. Linking does not remove
the need to state enough local context, supported versions, or safety information, and
important claims should not depend on a fragile external link alone. Generated API
pages should expose only the intended public contract and do not replace authored
tutorials, how-tos, or explanation. Generated artefacts may be committed or rebuilt;
that trade-off belongs to the adopter. Commands and version examples from a 2022 tool
stack must be checked against current Sphinx, Read the Docs, and packaging guidance
before use.

The chapter is therefore a strong supporting source for audience-led scope, a separation
between prose and reference facts, canonical linking, empathetic language, local page
context, build automation, and same-change maintenance. Diátaxis itself remains the
primary source for the four modes, while maintained tool documentation remains the
authority for current configuration.

## Docstrings as a separate maintenance layer

OpenGHG [PR 1730](https://github.com/openghg/openghg/pull/1730) makes docstrings part of
the repository's coding contract: it selects Google style, requires coverage for public
objects and selected private/test objects, asks for scientific and behavioural
semantics beyond types, and ties docstrings to changed public behaviour. This supplies
the evidence that the initial conditional Python reference should become a separate,
lightweight review skill.

The policy itself should remain in the adopting repository. For OpenGHG, a concise
`doc/source/development/docstrings.rst` page should define module coverage, public
status, constructor placement, inherited methods, relevant exceptions, scientific
contracts, and maintenance triggers. Root agent guidance should summarise and link to
that page rather than duplicate it.

The docstring skill should inspect changed objects, the local policy, exports, annotations,
implementation, tests, and generated API placement. Deterministic tools can check
presence and form; the skill checks whether the text is useful and true. Tutorials,
how-to guides, model explanation, and cross-page coherence remain with
`documentation-authoring` or `documentation-assessment`. The full design is in
[Docstring policy and review skill](docstring-policy-and-skill.md).

## Additional writing sources

The focused [source landscape](source-landscape.md) assesses Python documentation,
mathematical exposition, Strunk and White, current plain-language and accessibility
guidance, reuse constraints, and further source families. Its main consequences are:

- use a dialect-neutral semantic core for Python docstrings, then preserve the
  adopting project's Google, numpydoc, or other established convention;
- load a mathematical-exposition profile only for substantial equations, models, or
  derivations, with notation/code mapping, assumptions, units, limitations, examples,
  and domain review;
- use Halmos and Knuth, Larrabee, and Roberts for judgement and review questions rather
  than inflexible prescriptions;
- treat the public-domain early Strunk text as historical background and later E. B.
  White editions as copyrighted works; and
- make prose warnings explain a possible reader harm instead of declaring a style-book
  preference to be an error.

## Language options

### Recommendation

Adopt **plain technical English plus a project terminology layer** as the default. The
goal is to simplify the reader's work without simplifying away technical or scientific
meaning.

Default guidance should prefer familiar and literal wording, consistent terms, explicit
actors where they matter, one action per procedural step, conditions before actions,
short paragraphs, descriptive headings, defined abbreviations, and exact formatting of
commands and identifiers. Sentence length, passive voice, and reading-level scores are
signals for review, not automatic failures.

The [Google developer documentation style guide](https://developers.google.com/style/)
is the most practical open baseline for software documentation. It says that local
project guidance takes precedence and includes specific guidance for a
[global audience](https://developers.google.com/style/translation),
[accessibility](https://developers.google.com/style/accessibility), and
[inclusive documentation](https://developers.google.com/style/inclusive-documentation).
Locale remains a project decision; the guide itself defaults to American English.

### ASD-STE100

[ASD-STE100](https://www.asd-ste100.org/) is a controlled natural language that began
in aerospace maintenance. The current standard is Issue 9, dated 15 January 2025. It is
strongest for operational procedures, troubleshooting, warnings, and translation-ready
content because it tightly controls vocabulary, meaning, and sentence form.

It should not be mandatory across this project:

- correct use requires substantial training, technical knowledge, a project dictionary,
  and human judgement;
- its constraints can make tutorials and conceptual scientific explanation repetitive
  or distort qualifications, causality, and uncertainty;
- it does not cover every documentation concern, including publication design and
  domain policies;
- tools and agents can assist but cannot prove semantic correctness or compliance;
- the [official Issue 9 standard](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)
  is available free of charge but restricts redistribution, so this repository should
  link to it rather than vendor or reproduce it.

The future skill should offer profiles instead:

| Profile | Use |
| --- | --- |
| Plain technical English | Default for all modes; preserve exact domain terms and scientific qualifications. |
| Controlled procedural English | Installation, operations, troubleshooting, warnings, and recovery steps that benefit from stricter literal language, without implying conformance to ASD-STE100. |
| Full ASD-STE100 | Only when explicitly required; use the current official standard, a project dictionary, and qualified human review. Never claim compliance from agent or linter output alone. |
| Translation-ready | Stricter terminology consistency, literal language, unambiguous dates and units, and localisation review. |
| Public science communication | Audience-tested plain science writing; consider [ISO 24495-3:2026](https://www.iso.org/standard/86938.html), noting that the full standard is paid and targets readers with varied backgrounds rather than specialist-to-specialist writing. |

[ISO 24495-1:2023](https://www.iso.org/standard/78907.html) confirms that plain-language
principles apply to technical writing and controlled languages, but the paid standard
should be a reference rather than copied repository content. A prose linter such as
[Vale](https://docs.vale.sh/) can enforce project terminology and objective conventions,
but Vale itself is explicit that it is a consistency tool, not a writing teacher.

The [tool assessment](source-landscape.md#candidate-tools-agent-style-and-vale)
distinguishes generation/review guidance from deterministic linting. It recommends
using `agent-style` as a candidate-rule source and evaluation comparator rather than
adopting all of its house preferences, and piloting Vale only after an adopter's terms,
markup, exclusions, and severity policy are known.

## Quality and lifecycle beyond Diátaxis

The future guidance should prioritise seven additional dimensions.

### 1. Correctness, evidence, and provenance

Consequential claims need an appropriate authority: implementation or schema for API
shape and defaults; tests for supported behaviour; validated workflows and papers for
scientific behaviour; and design records for rationale. The agent should label verified
facts, inferences, and unresolved questions separately.

For scientific examples, record inputs, software and data versions, environment,
method, expected result or invariant, tolerance or uncertainty, and limitations. The
[FAIR4RS principles](https://doi.org/10.15497/RDA00068) are useful here because research
software is executable, composite, continuously evolving, and versioned.

### 2. Executable reproducibility and version alignment

Run small deterministic examples on each relevant change. Run expensive, stochastic,
networked, notebook, or HPC workflows on a schedule or release gate. Test scientific
invariants and tolerances instead of freezing large platform-sensitive outputs. Sphinx
includes [doctest and link-checking builders](https://www.sphinx-doc.org/en/master/usage/builders/index.html).

Build released documentation from the corresponding tags or branches and clearly mark
development and unsupported versions. [Read the Docs versioning](https://docs.readthedocs.com/platform/stable/versions.html)
supports this model.

### 3. User-task evidence and outcome evaluation

Define the reader, task, prerequisites, environment, risk, and evidence for the need.
Evaluate whether representative users can complete realistic tasks and correctly
interpret results. Useful signals include task completion, false completion, recovery,
time to find, recurring support questions, failed examples, and zero-result search
queries. [Read the Docs search analytics](https://docs.readthedocs.com/platform/stable/search-analytics.html)
explains how search failures reveal gaps and poor findability.

### 4. Accessibility, inclusion, and localisation

Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as the rendered-site accessibility
baseline, while recognising that conformance does not prove usability. Important
documentation practices include semantic headings, descriptive links, text alternatives
for plots and diagrams, accessible mathematics, non-colour cues, explicit units and
abbreviations, and testing with disabled users where practicable.

### 5. Safety, security, and scientific limitations

Use placeholders rather than credentials, least-privilege and secure defaults, clear
warnings for destructive or costly commands, and explicit rollback or recovery where
needed. Scientific documentation should state assumptions, validation envelope, known
failure modes, uncertainty, inappropriate uses, and ways to detect implausible results.

### 6. Information architecture and findability

Organise primary pathways around recognisable audiences and tasks, then cross-link to
reference and explanation. Require descriptive titles, logical headings, stable URLs,
redirects, consistent terminology, search aliases, and useful links among related
Diátaxis modes. Do not mirror package layout unless it actually matches user work.

### 7. Source-of-truth alignment and review ergonomics

Generate only intentional public API reference and keep narrative material curated.
Apply risk-based review: scientific interpretation, destructive operations, security,
and migrations need domain review; ordinary tutorials and how-tos need executable
evidence and technical review; wording fixes need proportionate checks.

[Sphinx autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
can reduce duplicated API maintenance, while [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
can route high-risk content without requiring a central documentation gate for every
minor correction.

## Maintenance operating model

| Loop | Trigger | Obligation |
| --- | --- | --- |
| Continuous correctness | Every user-visible code, configuration, data-contract, or behaviour change | Update affected reference, procedures, tutorial paths, limitations, and release information in the same change. If no documentation changes, record a short evidence-based reason. |
| Periodic synthesis | Feature release, milestone, or a short quarterly review | Reconsider tutorial flow, explanations, duplicated material, navigation, terminology, priority needs, and recurring user failures. Select a few bounded improvements. |

Useful infrastructure includes documentation sources versioned with code, pull-request
previews, release-note fragments, generated public API reference, change-focused example
execution, scheduled external-link and expensive-example checks, clear deprecation and
migration guidance, and risk-based ownership. [Read the Docs pull-request previews](https://docs.readthedocs.com/platform/stable/pull-requests.html)
are a concrete implementation of reviewable continuous documentation.

Avoid a spreadsheet describing every page, mandatory per-page freshness dates, a quota
of four pages per feature, or a central reviewer for every typo. Keep only a small map of
priority user journeys and known gaps. Use the documentation navigation as the ordinary
page inventory and version control as the change record.

## Implications for a Codex skill

Official OpenAI guidance says that skills use progressive disclosure: hosts first see
the name and description, load `SKILL.md` when it applies, and load optional references
or scripts only as needed. Descriptions determine implicit invocation, so scope and
boundaries must be concise and discriminating. OpenAI also recommends focused skills,
instructions before scripts, explicit inputs and outputs, and trigger testing. See
[Build skills](https://learn.chatgpt.com/docs/build-skills).

This supports short, discriminating entry files, no custom scripts in the first
version, and behavioural evaluation of both correct activation and correct work. The
implemented suite uses separate skills for read-only assessment, authorised authoring,
diff-triggered impact review, and Python-object-level docstring review.
