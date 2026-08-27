---
id: DAC-0041
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0041
title: Assure the separation of access, use and disclosure within information scope
status: proposed
disposition: proceed-with-constraints
assessed_at: 2026-08-21
accountable_owner: Sailesh Panchal
review_date: 2027-02-21
confidence: medium
supersedes: none
---

# DAC-0041 — Assure the separation of access, use and disclosure within information scope

> **Proposed.** Routed because TDR-0041 supersedes a `full`-template one-way-door record and touches
> authority, disclosure and customer harm. It has no standing, and its disposition binds nothing
> until TDR-0041 is ratified.

## Uncertainty

Known: that the specification and the governing record disagree, exactly where, and that §4.4 is the
one that moved. Unknown: whether **six questions across two groups is the right decomposition**, or
whether it is this author's decomposition finding no resistance. The candidate proposed five in one
group; §4.4 has five in two; this record proposes six in two. Three shapes in three writings is
weak evidence that any of them is settled.

Assumption: that use is genuinely first-class rather than a special case of access downstream of a
projection. If that assumption is wrong the model has one question too many, which is a cheaper error
than one too few but is still an error.

**Confidence is medium and the reason is nameable**: no durable comparative review against
access-control, purpose-limitation, usage-control or information-flow literature is cited. The
decomposition is reasoned from the specification's own text and from operational experience, not from
independent convergence.

## Adversarial projection

The realistic abuse is **the enumeration read as a control framework**. Six named questions in a
governance standard look like six controls, and an adopter under audit pressure has every incentive
to present them as such — "we separate access, use and disclosure" asserted from the fact that a
record format names them. Nothing in the format would contradict the claim.

The second abuse is subtler and worse: **purpose used to launder a use permission**. Because purpose
now qualifies every information-scope question, a participant may argue that a use was in-purpose
after the fact, with no artefact recording what the purpose was at the time. The model makes the
question askable and supplies no answer, and the gap between those is where the abuse sits.

The third is **authority by accumulation** — a participant holding access, use and disclosure
permissions across enough decisions being treated as holding a mandate. The record's final clause
says no, and no mechanism enforces it.

## Customer-outcome projection

Routed materially. Purpose drift harms customers with no visible breach: information legitimately
obtained for servicing gets used for pricing, retention or eligibility, and every individual step
passed the access test. Naming use separately makes the drift describable, which is the only
contribution a record format can make and is not a small one — a harm nobody can name does not get
raised.

The opposite harm is equally real and is routinely under-weighted. **Over-restrictive projection is
a customer outcome too**: the participant who cannot see why a decision was taken cannot explain it
to the person affected by it, and refusing to answer is not a neutral act. The review must examine
both directions or it will optimise one.

## Control side-effects

Enumerating six questions may encourage adopters to build six controls where their existing
governance already answers three of them adequately — the standard creating work by describing
structure. The counterweight is that the record explicitly enforces nothing and adds no field, so
there is nothing to fill in.

The reverse side-effect is that a question named but unenforced can be treated as answered by naming.
This is the misuse the constraints below are aimed at.

## Execution capability

Within reach and mostly already done: §4.4 carries the substance, and reconciling it to a ratified
record is an editorial change to one section. What is **not** within reach is the external
comparative review, which needs someone other than the author.

## Constraints

Proceed only with these.

1. **No specification text changes while TDR-0041 is proposed.** §4.4 is reconciled in the same
   change that ratifies the record, or not at all. A specification edited ahead of its decision is
   the defect this record was written because it found.
2. **The enumeration must state that it is not a control framework**, at the point of use in §4.4 and
   not only in the decision. A caveat that lives only in the register is unavailable to the reader
   who reaches the specification directly.
3. **No core field is added for access, use, disclosure or purpose**, and no `x-` field is treated as
   satisfying any of them. TDR-0015 judgement 1 is retained and this case does not reopen it.
4. **The external comparative review is named as owed, not as done.** TDR-0041's External evidence
   line says no durable review is cited; that wording may not be softened without the review
   actually existing.
5. **The review examines over-restriction as a customer harm**, symmetrically with over-disclosure.
   A review that reports only the second has not discharged this case.
6. **Authority-by-accumulation is tested explicitly** at review: whether any adopter, tool or
   projection has come to treat a set of information-scope permissions as an operating-scope mandate.

## Review

At the adopter evidence named in TDR-0041, or 2027-02-21, whichever is sooner. The trigger that
would reopen this case earlier is any adopter or implementation presenting the six questions as
implemented controls.
