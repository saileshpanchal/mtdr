# Inheritance contributions — the recovery vocabulary

**Version:** 1.0.0 · **Status: EXPERIMENTAL — not part of the MTDR standard** (TDR-0047)

What a [`SourceFragment`](../../../specification/source-fragment.md) can contribute to an Operational
Inheritance Record, carried through the shared
[`RecordContribution`](../../../specification/record-contribution.md) structure — **not a new
interchange structure**. Organisational material rarely states inheritance as such; it is scattered
across hand-over notes, run books, support matrices, terms of reference, incident reviews and
onboarding packs.

## The object

| Field | Value |
|---|---|
| `target_object` | `operational-capability` |
| `target_record_type` | `OIR` |

The shared contract leaves `target_object` open *for an object supplied by a later record package*.
This is that object. No shared specification or schema changes.

## The question

> **Does this span contribute to the organisational state a participant must inherit before
> performing this operational work?**

Not *does this document look like an OIR?* — none will.

## Contribution classes — one per clause

`semantic_role` takes one of the ten clause keys: `purpose` · `inherited-context` · `jobs` ·
`outcomes` · `responsibilities` · `authority` · `obligations` · `practices` · `escalation` ·
`evidence`. A fragment may contribute to several. *"Repairs over £2,500 need a second operator,
per the March delegation"* contributes to `authority` (a reference to the delegation) and to
`inherited-context` (an accepted control).

For `authority`, the contribution is **always the reference** — the instrument that delegated the
authority — never the authority itself.

## Boundary tests — what is not inheritance

| Material | What it is | Contributes |
|---|---|---|
| *"Ana covers exceptions on Tuesdays"* | **allocation** — who performs, not what is inherited | nothing; reported, so participant leakage is visible |
| *"Click Repair, enter the new sort code, press Submit"* | **procedure** — how to do a task | nothing; the OIR replaces no run book |
| *"The exceptions team"* | **structure** — a current organisational unit | nothing; a team is not a job |
| *"Operators may write off up to £50"* with no instrument cited | an authority **claim** without provenance | `authority` with `epistemic_confidence: low`, flagged unsourced — never an inline grant |
| *"It failed twice last winter on name changes"* | **experience** about this work | `inherited-context`, not `practices` |
| *"Check recent name changes first"* | **practice** — a default way of working | `practices` |

## The `unclassified` outcome

Material relevant to inheritance that fits no clause is reported as **unclassified** — fragment refs,
what was recognised, why classification failed — and **never** near-fitted into a clause. A recurring
unclassified pattern is evidence for the experiment, not a reason to add an eleventh clause.

## Derivation

`derivation: explicit | inferred` is carried as for every package. A clause whose content is inferred
across spans is never presented as asserted fact in the drafted record; the completeness of each
clause is reported by its source marker, and the derivation travels with its contributions.
