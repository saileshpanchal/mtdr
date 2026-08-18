---
id: TDR-0039
title: State-relative requirements must be represented state-relatively
status: accepted
template: full
decision_date: 2026-08-18
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0019, TDR-0027, TDR-0033
confirmed_by_outcome: pending — review when the first further record family is admitted without reproducing the defect, or 2027-08-18, whichever is sooner
---

# TDR-0039 — State-relative requirements must be represented state-relatively

## Context — what was known at the time

[TDR-0033](TDR-0033-four-dimensional-validity.md) identified a contradiction in this repository's own
Value Record: the specification says a candidate "may lack a baseline or counter-signatory *only* in
this state", and the schema required `finance_countersignatory` unconditionally. A candidate carrying
the honest gap the specification permits was rejected before any dimension could report on it.

DAC-0033 constraint 6 forbade fixing it opportunistically and routed the correction through
[TDR-0019](TDR-0019-value-record-v2-operational-value-commitment.md), which owns the VR v2 judgement.
That judgement was never wrong. `finance_countersignatory` **is** required for ratification, exactly
as TDR-0019 says.

The schema encoded something stronger and different — required for the object to *exist as a
schema-valid record* — and the two are not the same claim. The stronger form silently collapses
structural validity into lifecycle-transition eligibility, which is precisely the distinction TDR-0033
later had to make explicit.

One detail settles the diagnosis. **The correct rule was already there.** The schema's `allOf` already
required a counter-signatory when `status` is `ratified` or `settled`, with a description reading *"A
record may lack a baseline or counter-signatory only while `candidate`."* It sat next to a global
`required` entry that made it unreachable. This was never a judgement anyone made; it was a transition
requirement leaking into the representation requirement, beside the correct rule, doing nothing.

## Decision

**The substrate invariant:**

> **A requirement necessary for a lifecycle transition must not be encoded as an unconditional
> structural requirement, unless it is genuinely required in every valid lifecycle state.**

Put the other way round, because this is the form that catches the defect in review: **fields required
to *become* something must not accidentally become fields required to *represent* something.**

A schema that cannot express a state its own specification permits has stopped describing the object
and started constraining the lifecycle — in the one place with no vocabulary for saying so.

**Applied to the Value Record**, as implementation remediation under TDR-0019 + TDR-0033 + this record:
`finance_countersignatory` is removed from the global `required` list. Nothing else changes. The
existing conditional rule already required it for `ratified` and `settled` and now takes effect, and
the specification is untouched because it was already correct.

The correction is narrow on purpose. §4.4's candidate exemption names **baseline and counter-signatory
and nothing else**; the baseline is a body section rather than frontmatter, so exactly one field moves.
`beneficiary`, `committed_by` and `reconcile_by` stay globally required, because TDR-0019 §3 makes
beneficiary part of commitment identity and §4.4 does not exempt the others. **A rule that loosened
everything would be the wrong rule** — the invariant is about matching the state that actually needs
each requirement, not about requiring less.

**Three states, separated and now executable:**

| State | Structural | Transition eligibility | Standing |
|---|---|---|---|
| Candidate, no counter-signatory | valid | **fail** — the prerequisite is absent | none |
| Candidate, counter-signed | valid | **pass** — the request may be placed before a decision-maker | **still none** |
| Ratified | valid | not-applicable — nothing is being asked | exists, evidenced **outside** the result |

The middle row is the consequential one. It is the only condition under which
[TDR-0027](TDR-0027-human-ratification-confers-standing.md)'s boundary is genuinely tested: every
machine-verifiable prerequisite satisfied, no mechanical objection remaining, and **still no standing**,
because eligibility is not ratification and the absence of an objection is not consent.

Loosening a required field is backward compatible: every previously valid record stays valid.

## Evidence

- **Business** — the state a schema cannot express is the state an organisation is most often actually
  in. A tool that rejects the honest incomplete candidate teaches its users to complete it dishonestly.
- **Architecture** — this is TDR-0033's separation applied to schema authoring rather than to
  validators. Reporting the dimensions independently is worth little if the schema has already fused
  two of them before reporting begins.
- **Regulatory** — not material to the rule, though the pattern it prevents is a familiar one:
  approval prerequisites hard-coded as data requirements, so nothing can be recorded until it is
  approved, so what is recorded is whatever was approvable.
- **Operations** — one line changes in one file. The check that guarded the frozen contradiction is
  replaced by one asserting the state-relative form, so the defect cannot return in either direction:
  a candidate must validate without a counter-signatory, and a ratified record must not.
- **Customer** — indirectly material. Forcing completeness at the wrong moment is how a beneficiary
  nobody has confirmed becomes a beneficiary the record asserts.
- **Data** — three fixtures ([FIX-117](../tests/validation/FIX-117-candidate-ineligible-no-standing.md),
  [FIX-118](../tests/validation/FIX-118-eligible-still-no-standing.md),
  [FIX-119](../tests/validation/FIX-119-ratified-standing-evidenced-elsewhere.md)) over three subjects
  that are all schema-valid and differ only in eligibility and standing.
- **External** — none taken. JSON Schema's conditional vocabulary already expresses this; the defect
  was in how it was used, not in what it can do.

## Alternatives rejected

1. **Fix the VR schema as a local bug and record nothing.** Rejected: the same defect is available to
   every record family not yet admitted, and it is invisible in review precisely because the strong
   form looks more rigorous than the correct one.
2. **Supersede TDR-0019.** Rejected: its judgement is unchanged and correct. Superseding it would
   falsely record that the substantive decision moved, when only its encoding did.
3. **Relax every conditionally-required field at once.** Rejected: the invariant is about matching each
   requirement to the state that needs it. Loosening indiscriminately makes the same category error in
   the opposite direction.
4. **Require the schema to express the whole lifecycle.** Rejected on TDR-0033's ground — schema can
   test serialised assertions and cannot establish evidence sufficiency or perform human judgement.
5. **Leave the contradiction visible until a record family needed it.** Rejected: the family that
   needed it was the one already shipped, and the proof DAC-0033 constraint 3 required could not be
   written while the state was unrepresentable.

## Options foreclosed

- No schema in this repository may make a transition prerequisite unconditionally required, unless the
  field is genuinely required in every valid state of the object.
- A record family cannot be admitted with a schema that rejects a state its own specification permits.
- The VR correction cannot be widened to other fields without superseding this record.
- Eligibility cannot be represented as a lifecycle state, a record field, or anything the record
  carries about itself.

## Consequences and review

Success is the next record family — authority, work, evidence — being admitted without reproducing
this defect, and the rule being what catches it in review rather than a validator catching it later.

The immediate consequence is that a state MTDR has described since VR v2 can finally be represented,
and the three-way separation the last several records have been building — **validity ≠ eligibility ≠
standing** — is now executable rather than argued.

Review when the first further record family is admitted, or if anyone proposes widening the VR
correction, because that proposal would be the invariant being misread as a licence.
