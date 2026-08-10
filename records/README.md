# Record packages

**The architectural unit of this standard is the record package, and top-level packages correspond to
organisational languages** — one class of organisational meaning, one primary record type, one
package. Decided in [TDR-0021](../decisions/TDR-0021-record-package-architecture.md); the umbrella
specification is [`specification/organisational-records.md`](../specification/organisational-records.md).

| Package | Primary record | Status | Associated artefacts / practice |
|---|---|---|---|
| [`decision/`](decision/) | **TDR** — the unit of judgement | **Normative** | DAC + the eight assurance skills |
| [`value/`](value/) | **VR** — governed memory of an Operational Value Commitment | **Normative** | value challenge and validation |
| [`authority/`](authority/) | OAR | Candidate | authority practice |
| [`work/`](work/) | OIR | Candidate | JTBD / work practice |
| [`evidence/`](evidence/) | OER | Candidate | evidence projection and validation |

There is no sixth family for events, fragments, observations or runtime state.

## What a normative package contains

```
records/<language>/
├── README.md          package manifest — object, record, status, artefact index
├── specification/     the language's normative semantics
├── schema/            machine-readable frontmatter schemas
├── templates/         authoring templates
├── examples/          fictional worked examples
├── fixtures/          known-answer conformance fixtures (expected AND must-not)
├── validation/        semantic roles + the record-specific admissibility test
└── skills/            the language's portable skills
```

A **candidate** package contains a README only — identity, semantic scope, `status: candidate`, and a
statement that the [record admission test](../specification/record-admission-test.md) has not been
passed. A directory confers no maturity.

## The two structural rules

**The extraction test.** Any package must be extractable tomorrow into an independently governed
repository without redesigning the record. If it cannot, the boundary is wrong.

**The dependency rule.** A package may depend *downward* on the substrate —
[`specification/`](../specification/), [`schemas/shared/`](../schemas/shared/),
[`skills/shared/`](../skills/shared/) — and never *sideways* on another package. Cross-language
fixtures live in [`tests/`](../tests/). Anything two packages need becomes substrate, by a recorded
decision.

One refinement, forced by a real relationship: a package's specification may make a **normative
cross-reference to a sibling package's specification** — the value language's mandatory
`linked_decisions` genuinely refers to the decision language (TDR-0008), and on extraction such a
reference becomes a URL to the sibling standard, exactly as a reference to ISO 8601 would. What a
package may never reach sideways for is a sibling's **schemas, skills, templates, validation or
fixtures** — those are dependencies, and dependencies break extraction.

## Adding a language

1. Pass the [record admission test](../specification/record-admission-test.md), recorded as a TDR.
2. Populate the package per the layout above, layer by layer, through normal releases — the
   [conformance layers](../specification/conformance.md) measure its maturity as they land.
3. The shared interpretation skills need no modification: the object and record-type patterns in
   [`schemas/shared/record-contribution.schema.json`](../schemas/shared/record-contribution.schema.json)
   are open rather than enumerated precisely so a package plugs in without a schema change.

Whether something is a language at all — or a dependent artefact that lives *inside* one, as the DAC
lives inside `decision/` — is the admission test's four questions, never a directory appearing.
