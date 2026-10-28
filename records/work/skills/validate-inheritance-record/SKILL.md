---
name: validate-inheritance-record
description: EXPERIMENTAL, not part of the MTDR standard (TDR-0047) — validate an Operational Inheritance Record against the experimental OIR specification — the schema resolved from the record's own conforms_to, the source-marker rules a schema cannot see in the body, the lifecycle, and the references the record depends on. Use this skill as the work language's final gate, after the shared validation mechanics have run, whenever someone asks "is this OIR valid?" or "can this be brought into force as it stands?". Every result it produces says the specification is experimental, and no conformance claim may rest on it.
---

# Validate Inheritance Record

> **Experimental** under [TDR-0047](../../../../decisions/TDR-0047-experimental-packages.md). Not part
> of the MTDR standard.

The work language's specialisation of the validate stage. The **mechanics** — strict parsing, date
normalisation, manifest-driven schema resolution, identifier agreement, lineage resolution — are the
shared skill's, [`validate-record`](../../../../skills/shared/validate-record/), and run first. This
skill adds the checks only the work language defines.

## The one rule

**Say it is experimental, every time.** A pass here is conformance to an experimental specification,
not to the MTDR standard. A result that omits that is a false claim about the record, whatever else it
gets right.

## The inheritance-specific checks

1. **Schema, resolved from `conforms_to`** through the package manifest
   ([`package.yaml`](../../package.yaml)) — `experimental: true` present, all ten clauses present, each
   with a source marker; `reference` with at least one ref, `conflicting` with at least two, `missing`
   with none; `authority` only `reference` or `missing`; `unknown` dates and owners only in a draft.
2. **The body agrees with the markers.** A `missing` clause declares the gap and states no content; a
   `reference` clause cites and does not restate; an `asserted` clause carries provenance. Structural:
   the schema cannot read the body.
3. **Jobs are in functional form** — verb + object + contextual clarifier — each with `established_by`
   set to a decision identifier or `unknown`.
4. **The lifecycle coheres.** A `superseded` record has a successor whose `supersedes` names it. A
   successor whose clauses differ from its predecessor's only in who performs the work is reported:
   that is the participant-centred failure the lifecycle hypothesis exists to catch.
5. **References resolve, or are reported `indeterminate`.** A reference unresolvable in the reader's
   context is not an error in the record; it is a relational result that cannot be determined here.
6. **Contribution coverage and unsupported claims.** Every asserted clause traces to at least one
   contribution; any statement with none behind it is an **unsupported claim**, reported by clause.
   Contributions referenced and never used are listed.
7. **Temporal consistency.** Source times, `effective_from` and supersession ordering cohere; a
   successor effective before its predecessor fails structurally.

## Outputs

Per the shared contract: pass, fail or indeterminate per check, schema-based versus structural named,
the specification version validated against — and the statement that it is the experimental OIR
specification, under TDR-0047. The marker view (each clause and its source marker) is reported
alongside, unjudged.

## Anti-patterns

- **The silent experiment** — a result that reads as a statement about the standard.
- **Reference as failure** — a `reference` clause reported as incomplete because its content is not in
  the record.
- **Indeterminate as pass** — an unresolvable reference counted as resolved.

## Scope note

Mechanics are the shared skill's; this adds the work language's rules only, per
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md). Conformance is not
correctness here either — and here it is not even conformance to the standard.
