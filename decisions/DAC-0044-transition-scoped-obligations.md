---
id: DAC-0044
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0044
title: Assure transition-scoped obligations
status: proposed
disposition: proceed-with-constraints
assessed_at: 2026-08-27
accountable_owner: Sailesh Panchal
review_date: 2027-02-27
confidence: high
supersedes: none
---

# DAC-0044 — Assure transition-scoped obligations

> **Proposed.** Routed because this changes what *eligible* means, and it does so while a release is
> being sought. That combination is the whole reason to assure it.

## Uncertainty

Known: that constraint 5's subject is a register and not this repository, and that the register had
no vocabulary for saying so. Unknown: whether `gates` is the right granularity, or whether a second
transition will reveal obligations that gate both and need something richer than one name.

Assumption: that re-scoping on subject is distinguishable, in practice, from re-scoping on
convenience. **The whole case rests on that assumption**, and it is a judgement a schema cannot make.

## Adversarial projection

Routed hardest here, because the abuse is obvious and the timing is suspicious.

**The realistic abuse is `gates` becoming the field you change when a release is inconvenient.** An
obligation that will not clear before a deadline can be re-scoped to a transition that does not exist
yet, and the gate turns green without anything being satisfied. Nothing about the mechanism prevents
this; only the requirement to state a subject-based reason, in a record, makes it visible.

That this decision is being made *while seeking a release* is exactly the circumstance in which the
move is least trustworthy. The mitigating facts are checkable rather than asserted: constraint 5's
`implementation` was `not-applicable` **before** this decision existed, its note said the proof
belongs to a register operator **before** any release was sought, and re-scoping it does not open
the gate — constraint 4 still holds it `indeterminate`. A gate-weakening move that leaves the gate
shut is weak evidence of gate-weakening intent.

**The second abuse is the empty gate**: moving every obligation off a transition and reading the
absence as satisfaction. Foreclosed mechanically — an empty gate fails rather than passes.

**The third is quiet drift**: an obligation re-scoped without a record. The suite requires a stated
reason on any non-default gate, which catches the silent case but not a plausible-sounding false one.

## Customer-outcome projection

Indirect and real. The people who rely on a governed release are relying on the gate meaning
something. Every mechanism that lets a gate open more easily transfers risk to them, and the
honest mitigation is not that this mechanism cannot be abused but that each abuse leaves a record
with a name on it.

## Control side-effects

Splitting the register by transition can make each view look complete when the whole is not — a
reader checking `released` may never see what is owed to `registered`. Countered by carrying every
non-gating obligation in every result rather than filtering it out.

The opposite side-effect: transitions proliferating so that each obligation gates its own, leaving no
gate with any real content. The review trigger watches for it.

## Execution capability

Within reach and done: one enumerated field, an eligibility computation scoped to it, two enforced
rules, and carried obligations printed in every run.

## Constraints

Proceed only with these.

1. **Re-scoping is a decision with a subject-based reason, never an edit.** A reason about timing,
   difficulty or release pressure is not admissible, and a reviewer should reject one.
2. **An empty gate reports `indeterminate`, never `pass`.** Enforced.
3. **Carried obligations appear in every validation result**, whatever transition was requested.
   Enforced.
4. **`gates` carries a transition name and nothing else** — no priority, severity, waiver or
   expiry. Any of those would turn a scope into a dial.
5. **This decision discharges nothing.** Constraint 5 remains outstanding against `registered`, and
   any statement that MTDR has satisfied it is false.
6. **At review, count the re-scopings.** More than one further move, or any move whose reason is not
   plainly about subject, reopens this case.

## Review

At the second defined transition, or 2027-02-27. The trigger that reopens it earlier is any
obligation being re-scoped while a release is pending — including this one, read again in hindsight.
