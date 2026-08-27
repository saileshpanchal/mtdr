---
id: TDR-0044
conforms_to: mtdr/decision/tdr@1.15.0
title: An obligation gates a named transition, not every transition
status: proposed
template: full
decision_date: 2026-08-27
accountable_owner: Sailesh Panchal
confidence: high
maturity: proposed
supersedes: none
derived_from: TDR-0032, TDR-0033, TDR-0037
confirmed_by_outcome: pending — confirm when a second transition is defined and the register partitions cleanly between them, or 2027-02-27, whichever is sooner
---

# TDR-0044 — An obligation gates a named transition, not every transition

> **Proposed.** No standing. It changes how eligibility is computed and does not by itself make any
> transition eligible.

## Context — what was known at the time

[TDR-0037](TDR-0037-release-eligibility-from-standing-governance.md) made `released` a governed
transition and computed eligibility from the obligations register rather than a curated checklist.
That was right, and it left one thing unstated: **the register records what an obligation requires,
and never which transition requires it.**

Every obligation is therefore treated as a prerequisite of the only transition the repository
requests. Two of the fifteen cannot be satisfied by this repository at all:

- **DAC-0032 constraint 5** — the registration/export round-trip. Its implementation is
  `not-applicable` because *nothing in this repository performs registration*, and its own note says
  the proof *"requires a register, and belongs to whoever operates one."*
- DAC-0032 constraint 4 — the zero-install proof — needs a participant unknown to the author. That
  one is genuinely a prerequisite of publishing; it is simply not yet done.

The difference matters. Constraint 4 is a test this repository has not run. **Constraint 5 is a test
about a different subject entirely** — a register operator's system — and under
[TDR-0032](TDR-0032-typed-multi-object-conformance.md), *conformance is always claimed by a defined
subject, and a claim at one level implies nothing at another*. An obligation whose subject is a
register cannot be a precondition of a standards repository publishing its specification, and holding
one there produces a gate that can never open for reasons outside the gate-keeper's control.

There are only two honest ways out, and one of them is not available. Marking constraint 5 satisfied
would manufacture evidence. Deleting it would lose a real requirement that a register operator must
still meet. What is missing is the vocabulary to say *"required, and required of something else."*

## Decision

**Every obligation names the transition it gates.**

The obligations register gains one field per entry:

```yaml
gates: released        # or: registered
```

Eligibility for a requested transition is computed from **only those obligations that gate it**.
Obligations gating a different transition are reported as *carried*, never as unmet, and never
silently dropped.

**`DAC-0032#5` moves from `gates: released` to `gates: registered`** — a transition this repository
does not perform and does not define the conditions of beyond the constraint itself. The obligation
is retained in full, with its measure, owner and note unchanged. It is not discharged, not weakened
and not deleted; it is **addressed to the subject that can actually satisfy it.**

Three rules keep this from becoming an escape hatch:

1. **Re-scoping an obligation is a decision, never an edit.** Moving an obligation between
   transitions requires a record saying why, and the reason must be about *subject* — that the
   obligation's measure concerns a different thing — never about difficulty or timing.
2. **A transition with no obligations gating it is not thereby eligible.** An empty gate reports
   `indeterminate`, not `pass`. Nothing becomes eligible by having its prerequisites moved away.
3. **Carried obligations are reported in every result.** A reader of any validation result sees what
   the repository still owes and to whom, whether or not it gates the transition being requested.

## Evidence

- **Business** — a gate that cannot open for reasons outside the gate-keeper's control is not a gate;
  it is an outage. The pressure it creates is to weaken the obligation, which is the failure this
  register exists to prevent.
- **Architecture** — this is TDR-0032's typed-subject rule applied to obligations. A constraint about
  a register is a constraint on a register, and eligibility for a repository transition should not
  read it.
- **Regulatory** — an obligations register that mixes what an organisation owes with what its
  counterparties owe cannot be used to demonstrate either.
- **Operations** — the register becomes usable by more than one actor: an operator can read what is
  addressed to them without inheriting a standards repository's publication conditions.
- **Customer** — not directly material.
- **Data** — one enumerated field. No obligation's measure, owner, evidence or note changes.
- **External** — **no external correspondence is claimed.** The shape resembles conditions-precedent
  scoping in other governance vocabularies, but none is cited and no dependency is taken.

## Alternatives rejected

1. **Mark constraint 5 satisfied.** Rejected: it manufactures evidence for a proof nobody ran, which
   is precisely what [TDR-0027](TDR-0027-human-ratification-confers-standing.md) forbids in the
   adjacent case of standing.
2. **Delete constraint 5.** Rejected: the requirement is real. A register operator must still show
   that storage alone produces no `accepted` transition, and deleting the obligation loses the only
   published statement of it.
3. **Weaken its measure until this repository can meet it.** Rejected: rewriting a test so the
   author passes is worse than failing it, and it would leave the actual risk unaddressed.
4. **Leave the gate permanently `indeterminate`.** Rejected: `indeterminate` is a truthful report of
   an unestablished fact, not a resting state for a fact that will never be established here. Using
   it that way would drain the meaning it carries under
   [TDR-0033](TDR-0033-four-dimensional-validity.md).
5. **A boolean `blocks_release` flag.** Rejected: it encodes one transition as privileged and would
   need replacing the moment a second is defined. Naming the transition scales; a boolean does not.

## Options foreclosed

- No obligation may be moved between transitions without a record stating the subject-based reason.
- No transition becomes eligible by having its obligations re-scoped away from it.
- An obligation may never be dropped from the register on the grounds that nothing here can satisfy
  it. Re-scoping is the only permitted move, and it preserves the obligation entire.
- `gates` may not grow into a general routing mechanism carrying priority, severity or waiver.

## Consequences and review

Success is a second transition being defined and the register partitioning cleanly between them
without any obligation being edited to fit. Failure looks like `gates` becoming the field people
change when a release is inconvenient — which the first rule above exists to make visible, since each
move must carry a reason about subject.

Immediate effect: with constraint 5 carried rather than gating, `released` is gated by fourteen
obligations, thirteen verified and one — the zero-install proof — outstanding. **The gate does not
open by this decision.** It reports `indeterminate` naming constraint 4 until a participant unknown
to the author has run it.

Review at that second transition, or 2027-02-27, whichever is sooner.
