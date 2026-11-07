---
name: validate-decision-record
description: Validate a decision candidate or a recovered TDR against the decision language — the TDR schema at the version the record binds to, the historical candidate contract and its integrity rules, contemporaneity recomputed from the times, the roles never filled by inference, and any review event's binding to the exact candidate. Use this skill as the decision language's final conformance gate, after the shared validation mechanics have run, whenever someone asks "is this candidate valid?" or "can this recovered record be put forward as it stands?". It says which checks were schema-based and which structural, and it never presents a well-formed review event as proof that anyone reviewed anything.
---

# Validate Decision Record

The decision language's specialisation of the validate stage. The **mechanics** — strict parsing, date
normalisation, manifest-driven schema resolution, identifier agreement, lineage resolution — are the
shared skill's, [`validate-record`](../../../../skills/shared/validate-record/), and run first. This
skill adds the checks only the decision language defines.

## The one rule

**Recompute; never trust a stored judgement.** Contemporaneity is computed from the times, a
candidate's disposition from its review events, a binding from the digest. A validator that reads any
of them as data has validated the author, not the artefact.

## The decision-specific checks

1. **The TDR schema, at the bound version.** A recovered or drafted TDR resolves its schema from
   `conforms_to` through the package manifest. `status: proposed` on anything a skill produced.
2. **The historical candidate contract.** The schema — loaded with
   [`schemas/shared/`](../../../../schemas/shared/) as a registry — and the integrity rules of
   [`historical-candidate.md`](../../../../specification/historical-candidate.md): every reference
   resolves inside the candidate; every fragment annotated once; `considered` on every context
   contribution and no other; `event_time_ref` unknown or a contribution to `decision-date`; no finding
   carried as a contribution; no authority resting on unlinked or retrospective material.
3. **Contemporaneity, recomputed** for every context contribution, from capture and creation times
   and its `considered` state against the decision date, at their precision; `indeterminate` wherever
   the date is missing.
4. **The never-inferred roles**, as the [vocabulary](../../specification/decision-contribution.md)
   declares them: an inferred owner, authority or alternative fails.
5. **Classifications against the vocabulary.** Every `not-a-decision` carries one of the five reasons
   by its stable identifier; every `non-decision` its kind; every `applicability` finding what it
   concerns; every `persistence` finding its authority for continuation
   ([`decision-contribution.schema.json`](../../schema/decision-contribution.schema.json)).
6. **Review events, where present:** the schema, and that the event's digest is the digest of the
   candidate as it now stands. **A structural check only** — the event's existence is never proof that
   a valid human act occurred.
7. **A recovered TDR opens with its recovery** — attested as the account, by whom, when — names its
   historical owner as evidenced, and claims nothing about whether the decision governs now.
8. **Contribution coverage and unsupported claims.** Every rendered value traces to a contribution;
   any that does not is an **unsupported claim**, reported by field.

## Outputs

Per the shared contract: pass, fail or indeterminate per check, schema-based versus structural named,
the version validated against — and the unsupported-claim list.

## Anti-patterns

- **The stored grade** — reading a contemporaneity grade or a disposition from the artefact.
- **The self-certifying event** — a well-formed event treated as a review that happened.
- **Version-blind validation** — the shared skill's rule.

## Scope note

Mechanics are the shared skill's; this adds the decision language's rules only, per
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md). Conformance is not
correctness, and validation of an account of the past is not validation of the past.
