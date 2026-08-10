---
name: validate-value-record
description: Validate a Value Record against the value language's specification — the v2 schema with its two state axes, the version the record was raised under, the coupled rules a schema alone cannot see, and the counter-signature obligations at ratification and settlement. Use this skill as the value language's final conformance gate, after the shared validation mechanics have run, whenever someone asks "is this Value Record valid?" or "can this be ratified as it stands?". It validates v1 records as v1 records, and it says which checks were schema-based and which structural.
---

# Validate Value Record

The value language's specialisation of the validate stage. The **mechanics** — strict parsing, date
normalisation, manifest-driven schema resolution, identifier agreement, lineage resolution, the
version-blind anti-pattern — are the shared skill's,
[`validate-record`](../../../../skills/shared/validate-record/), and run first. This skill adds the
checks only the value language defines.

## The one rule

**Validate against the version the record was raised under.** The package manifest
([`package.yaml`](../../package.yaml)) names v2.0.0 with its schema, and v1.3.0 with none: a v1
record validates structurally against the v1 field table and is reported as such —
never run against the v2 schema, and never silently passed as schema-valid.
[`specification/vr.md`](../../specification/vr.md) §8 carries the v1→v2 mapping.

## The value-specific checks

1. **The state axes cohere.** The schema enforces the hard cases (`candidate` carries only
   `not-started`); check the rest against §4.4 — a `settled` record carries a settlement-band
   `realisation`, an `observing` record is `ratified`, and no transition revives a terminal state.
   A signed write-off never reopens.
2. **Ratification requirements met on any `ratified` or `settled` record** — measured baseline with
   date and source in the body, named `committed_by`, named `finance_countersignatory`, stated
   `beneficiary`, `reconcile_by` present. A record may lack these only while `candidate`.
3. **The counter-signatures exist where the specification requires them** — at ratification, at every
   material state change, at settlement or write-off. Presence, not authenticity: whether a
   signature is genuine is the organisation's business, above the artefact boundary.
4. **`linked_decisions` is never `none`** — the schema enforces the pattern; state that it was
   checked, because a value claim floating free of any decision is a forecast, not a record.
5. **Evidence is labelled by kind** — existence · observation · attribution, per §5. Unlabelled
   evidence is a structural finding: the distinction the labels carry is exactly the one the record
   exists to preserve.
6. **A write-off states what was learned.** A `written-off` realisation whose settlement section
   records no learning fails the specification's own definition — a signed state, not an abandonment.

## Outputs

Per the shared contract: pass/fail per check, schema-based versus structural named, and the
specification version each record was validated against.

## Anti-patterns

- **Version-blind validation** — the shared skill's rule, restated because the VR is where it bites:
  a v1 record failing four v2 required fields is a conforming v1 record.
- **Signature inference** — treating a name in frontmatter as evidence the person signed. Presence
  is checkable; assent is not.
- **Axis conflation** — reporting a `ratified` / `not-realised`-track record as somehow inconsistent.
  Properly ratified with the value not arriving is one of the two states the axes exist to express.

## Scope note

Mechanics are the shared skill's; this adds the value language's rules only, per
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md). Conformance is not
correctness, here as everywhere.
