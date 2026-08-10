---
id: TDR-0026
title: Adopt the value-recovery vocabulary — contribution classes, the completeness view, the derivation marker, and composition skills
status: accepted
template: minimal
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0019, TDR-0022, TDR-0023, TDR-0025
confirmed_by_outcome: pending — review when the recovery lifecycle has run end-to-end against the fictional corpus with zero unsupported assertions, or 2027-02-10
---

# TDR-0026 — Adopt the value-recovery vocabulary: contribution classes, the completeness view, the derivation marker, and composition skills

## Context — what was known at the time

The value package's interpretation path was specified field-first: the semantic roles map contributions onto the record's structure. Recovery from real material works the other way round — organisations rarely write a commitment's clauses together, and a fragment contributes *kinds of meaning* (a constraint, an assumption, a challenge, evidence of supersession) long before anyone knows which record field, if any, will carry it. Some of those kinds — challenge, trade-off, context — deliberately never map to a field at all, yet losing them loses exactly the disagreement and uncertainty recovery exists to preserve.

Three further gaps were visible. Nothing distinguished a value read directly from a span from one inferred across spans, so a candidate's inferences could hide inside its evidence. The reporting of what a candidate lacks mixed evidential state with derivation, so "inferred" could conceal "incomplete". And the lifecycle vocabulary had no ruled place for an orchestrating entry point, though the recovery experiment needs one skill that any independent runtime can be pointed at.

## Decision

1. **The contribution-class vocabulary is adopted** as `records/value/specification/value-contribution.md`: thirteen classes — beneficiary · commitment · success · measure · constraint · assumption · time · priority · protection · trade-off · challenge · supersession · context — defining what a fragment can contribute **without requiring that it constitutes a Value Record**. It is interpretive vocabulary carried through the existing `RecordContribution` structure's package-defined roles, **not another record schema**; a fragment can make multiple contributions.
2. **The classes are not exhaustive**, and the vocabulary says so. An interpreting skill that finds material relevant to Value but unclassifiable under the current vocabulary reports the **`unclassified` recovery outcome** — a reporting outcome, not a fourteenth role. A recurring unclassified pattern is evidence for a superseding decision, never a forced fit.
3. **`derivation: explicit | inferred` is added to the shared `RecordContribution` interchange structure as an optional field.** The distinction is record-neutral — every language's interpretation needs it — so it belongs in the substrate, additively: every prior instance still validates.
4. **The completeness view is adopted** as the candidate-level report: per mandatory role, `supported | partial | missing | conflicting` — **state only**. Derivation is visible through the supporting contributions, never folded into the state grades, so an inferred proposition cannot present as a complete one.
5. **Composition skills are permitted**: a skill may orchestrate the lifecycle stages as a user-facing entry point. It may never contain a second copy of any stage's semantics — the existing duplication-is-a-defect rule, applied to orchestration.

## Alternatives rejected

1. **Extend the semantic-role table instead of adding a class vocabulary.** Rejected: roles map to the record; challenge, trade-off and context deliberately do not, and forcing them into field-shaped roles loses their meaning or drops them.
2. **A ValueContribution schema.** Rejected for now: the shared interchange structure expresses everything the classes need, and specialising the substrate the moment one package finds it convenient is exactly the drift TDR-0022 guards against. Revisit only on demonstrated inexpressibility.
3. **A fourteenth "unclassified" role.** Rejected: it would make a vocabulary gap look like a semantic finding, and would be silently reached for wherever classification is hard.
4. **Folding `inferred` into the completeness grades.** Rejected: it conflates two questions — what the evidence establishes, and how the reading was derived — and benchmark scoring needs them separate.

## Options foreclosed

- No contribution class may be added without a superseding record; the `unclassified` outcome is the evidence route.
- The completeness view can never carry a derivation grade; the interchange structure can never lose the derivation field without a superseding record.
- No composition skill may carry stage semantics; the entry point stays thin permanently.

## Review

At the confirmed-by-outcome trigger: the recovery lifecycle run end-to-end on the fictional corpus, zero unsupported assertions, negatives surviving — and the `unclassified` outcome observed at least once in testing, since a vocabulary that never fails to classify is not being tested.
