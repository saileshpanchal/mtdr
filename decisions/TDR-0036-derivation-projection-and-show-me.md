---
id: TDR-0036
conforms_to: mtdr/decision/tdr@1.15.0
title: Admit the derivation projection and a record-neutral show-me skill
status: accepted
template: full
decision_date: 2026-08-18
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0018, TDR-0022, TDR-0023, TDR-0033
confirmed_by_outcome: pending — review when two independent participants produce comparable projections of the same records, or 2027-08-18, whichever is sooner
---

# TDR-0036 — Admit the derivation projection and a record-neutral show-me skill

## Context — what was known at the time

The repository could already establish that a record is well formed, coherent, relationally sound and
eligible for a transition. It could not answer the question a reader actually asks first: **why does
this record say that?**

The information was all present. [TDR-0022](TDR-0022-fragment-contribution-interchange-architecture.md)'s
three structures record every value's derivation, and
[`challenge-record`](../skills/shared/challenge-record/) already walks the chain — adversarially, to
find what cannot be defended. What was missing was the same walk in the reading direction, and any
defined form for its output.

Absent a defined form, the question gets answered by a model in prose. That is the failure this record
exists to foreclose, because the prose answer is *fluent*: an account of how a value might have been
reached is easy to generate, reads better than the truth, and is indistinguishable from a real
derivation by anyone who cannot check. A standard whose whole proposition is that organisational memory
should be inspectable cannot leave its inspectability surface to be improvised.

There was also a concrete downstream requirement. Comparing independent participants over one corpus —
the recovery experiment's actual question — means comparing *why* each produced what it did, and free
prose cannot be compared.

## Decision

**1. Admit the derivation projection** ([`specification/derivation-projection.md`](../specification/derivation-projection.md),
[`schemas/shared/derivation-projection.schema.json`](../schemas/shared/derivation-projection.schema.json)):
a defined, versioned, machine-comparable statement of what a record's values were derived from.

**It is a view, not a fourth interchange structure.** It is computed from SourceFragment,
RecordContribution and CandidateAssembly and carries nothing they do not; TDR-0022's three levels are
untouched. Being a view is what keeps it honest — there is nothing in a projection that could be
authored, only things that could be found.

**2. Admit [`show-me`](../skills/shared/show-me/) as a record-neutral shared skill**, on the same
basis as the other four ([TDR-0023](TDR-0023-portable-skill-architecture.md)): the chain being walked
is a property of interpretation, not of any record type. Its one rule:

> **It projects what was recorded and never constructs what was not.**

**3. Five states, and no sixth.** Per field: `supported · inferred · conflicting · missing ·
unsupported`. No `likely`, no `weakly-supported`, no `plausible`, and **no aggregate provenance score
at any level**. Each of those encodes a judgement made at projection time, and a projection that
grades its own evidence has stopped reporting and started assessing. Recorded confidences are carried
through unchanged; nothing new is computed.

**4. `missing` and `unsupported` are constitutionally distinct.** Both have an empty chain. `missing`
is a gap the interpretation declared; `unsupported` is a value nothing accounts for. The schema makes
the distinction mechanical — `missing` requires a declaration and forbids a rendered value,
`unsupported` requires a rendered value and forbids a declaration — because it is the easiest of all
collapses and the most costly: unsupported content is indistinguishable from supported content by
reading, and only the walk exposes it.

**5. "I don't know why" is a valid machine-readable result.** A projection that is largely `missing`
and `unsupported` has not failed; it has reported the state of the organisation's evidence, which is
what it is for. A broken derivation chain is a finding, not a defect to be patched with generated
prose.

**6. The projection is context-free, and validation is not.** Whether a fragment is presently
reachable is relational validity's question under [TDR-0033](TDR-0033-four-dimensional-validity.md).
The projection reports *what was recorded*; the validation result reports *what can currently be
established*. Keeping them apart is what makes two participants' projections of the same records
directly comparable, since nothing in a projection depends on what either could reach.

**7. It judges nothing.** Whether the evidence should support the value remains `challenge-record`'s
work; whether the record has standing remains [TDR-0027](TDR-0027-human-ratification-confers-standing.md)'s.
A complete chain is evidence a human could act on, never the act.

## Evidence

- **Business** — "show me why" is the first question any reviewer, auditor or regulator asks of a
  governed record. A standard that answers it with generated prose is offering the appearance of
  accountability, which is worse than offering none.
- **Architecture** — the structures already carry the derivation; this adds a defined output format
  over them and no new level. It is the same separation JSON Schema draws between a validation
  vocabulary and a defined output format, applied to provenance.
- **Regulatory** — not material to the choice of model. The regulator-neutral discipline applies: a
  projection evidences what was recorded and claims no compliance of any kind.
- **Operations** — a reader given a chain and a rationale reads the rationale. Leaving no field for
  one is the only control that survives contact with a fluent generator.
- **Customer** — indirectly material. Where evidence about underserved cohorts is thin, the states that
  matter most are `missing` and `unsupported`, and a projection that smooths them into a narrative
  removes precisely the signal worth having.
- **Data** — the twelve fixtures in [`tests/inspectability/`](../tests/inspectability/) exercise each
  state and each prohibition; the synthetic subjects are local-government rather than financial
  services, deliberately.
- **External** — no external dependency is taken. W3C PROV remains mapped rather than adopted
  ([TDR-0035](TDR-0035-standards-boundary.md)); a projection is a document, and needs no RDF stack to
  be read or compared.

## Alternatives rejected

1. **Answer "show me why" in prose, with no defined form.** Rejected: the answer is generated, fluent
   and uncheckable, and nothing distinguishes a real derivation from a plausible one.
2. **Extend `challenge-record` to do it.** Rejected: challenge asks whether the record can be
   defended and returns findings; projection asks what produced it and returns none. Merging them
   would make every inspection adversarial and every projection a judgement.
3. **Make the projection a fourth interchange structure.** Rejected: it would carry no information the
   three do not, and a persisted structure can be authored — which is exactly the property a
   projection must not have.
4. **Add a sixth state for partially-supported values.** Rejected: it is a confidence grade under
   another name, and the recorded `epistemic_confidence` already carries what the interpreter thought.
5. **Include an overall provenance score for triage.** Rejected on the DAC-0033 argument one layer
   down: a figure that can be read alone will be read alone, and "87% evidenced" conceals which 13%.
6. **Report reachability in the projection.** Rejected: it would make projections depend on the
   evaluation context and therefore incomparable between participants, for information relational
   validity already reports better.
7. **Do nothing until the recovery experiment needs it.** Rejected: the experiment needs it, and by
   then the improvised prose answer would already be in use.

## Options foreclosed

- No projection may contain a rationale, explanation, justification or note field.
- No projection may contain a score, grade, percentage or aggregate of any kind.
- No sixth field state may be added without superseding this record.
- No projection may carry a suggested, inferred or corrected value.
- No projection may assert or imply standing, ratification or fitness to ratify.
- Reachability and resolution cannot be reported here rather than as relational validity.

## Consequences and review

Success is two independent participants producing projections of the same records that can be compared
field by field, and a disagreement locating *where* their reconstructions diverged rather than
reducing to a score. That comparison is the recovery experiment's real question, and this record is
what makes it askable.

The nearer test is smaller and comes first: a reader who has never seen the sources can take a
projection and know exactly which parts of a record the organisation can account for, and which it
cannot.

Review at the confirmed-by-outcome trigger, or the first time someone asks for a sixth state.
