# Package — Value Record

**Object:** `ovc` — the Operational Value Commitment, the unit of intended value
**Record type:** `VR` — Value Record

| Canonical artefact | Location |
|---|---|
| Specification | [`spec-value-record.md`](../../spec-value-record.md) |
| Schema | None yet — see below |
| Template | [`templates/vr.md`](../../templates/vr.md) |
| Worked example | [`examples/example-value-record-practice-skills.md`](../../examples/example-value-record-practice-skills.md) |

This package is an overlay for interpretation. It does not restate the specification, and where the two
appear to differ, **the specification governs**.

| File | Purpose |
|---|---|
| [`semantic-roles.md`](semantic-roles.md) | Roles a contribution may target, by lifecycle moment |
| [`admission.md`](admission.md) | Record-specific admissibility test |

## The object is the commitment; the record is its memory

This distinction drives interpretation. The question asked of material is **"does this contribute to
reconstructing an Operational Value Commitment?"** — not "does this document contain Value Record
fields?" A commitment's semantics are routinely spread across a business case, a budget line, a
steering pack and a later revision, none of which resembles a Value Record.

*Operational Value Record* and *OVR* are deprecated names for this record, retained only for migration
and alias tests. The record is the **Value Record**.

## Two semantic moments

A commitment and its reconciliation are different acts, separated in time, and material contributes to
them differently. [`semantic-roles.md`](semantic-roles.md) marks which moment each role belongs to.

```
Commitment semantics → Ratified Value Record → Observation entries → Reconciliation → Settlement
```

**Measurement is not attribution.** Observing that a number moved is not evidence that this commitment
moved it. Counterfactual and competing-cause reasoning belongs to reconciliation and must never be
required at commitment time.

## No schema yet

`spec-value-record.md` §4.1 states that the JSON Schema validates TDR frontmatter only, and "a VR schema
may follow in a later minor version". That remains true. Candidates are validated against the
specification's field table and this package's admission test until a schema exists.

## Skills

`identify-record-contributions` · `reconcile-record-fragments` · [`draft-vr`](../../skills/draft-vr/) ·
[`challenge-record`](../../skills/challenge-record/) · [`validate-record`](../../skills/validate-record/)

The human authoring path — [`value-record`](../../skills/value-record/) — targets the **same
specification**. One record, two routes to it.
