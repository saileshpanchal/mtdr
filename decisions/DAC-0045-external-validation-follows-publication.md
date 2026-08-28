---
id: DAC-0045
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0045
title: Assure the re-scoping of the zero-install proof
status: accepted
disposition: proceed-with-constraints
assessed_at: 2026-08-27
accountable_owner: Sailesh Panchal
review_date: 2027-02-27
confidence: medium
supersedes: none
---

# DAC-0045 — Assure the re-scoping of the zero-install proof

> **Accepted 2026-08-27**, `proceed-with-constraints`, its six constraints binding. This case
> exists because [DAC-0044](DAC-0044-transition-scoped-obligations.md)
> constraint 6 said it must: *"More than one further move, or any move whose reason is not plainly
> about subject, reopens this case."* This is that further move, made while the same release is
> pending. **DAC-0044's case is reopened here rather than avoided.**

## Uncertainty

Known: that `DAC-0032#4` cannot be satisfied before publication, because publication is what makes an
unknown participant possible. That much is structural and not a matter of judgement.

Unknown, and this is where the case is genuinely uncertain: **whether the subject argument is sound
or merely available.** TDR-0044 permits re-scoping on subject and forbids it on timing. The
circularity here reads as a timing problem, and the subject argument — that #4's measure concerns a
*participant* rather than the repository — is correct but was not the reason the move was first
proposed. The order in which an argument is found is not proof that it is wrong, and it is not
nothing either.

**Confidence is medium, one grade below DAC-0044's, deliberately.** The first re-scoping had a fact
that predated any release: constraint 5's implementation read `not-applicable` long before. This one
has no such independent marker.

## Adversarial projection

Routed hardest, and the honest reading is uncomfortable.

**This is the second obligation moved off `released` in a single session, by the person seeking the
release, using a mechanism ratified in that same session.** Every individual step is defensible and
the pattern is exactly what a gate being dismantled would look like. Recording that is not
rhetorical: a reader in a year should meet the objection in the file rather than have to construct
it.

What distinguishes it from dismantling, and each is checkable:

- The gate was `indeterminate` before this move and `pass` after it, so unlike constraint 5's
  re-scoping **this one does open the gate**. That is the strongest reason to distrust it and it is
  stated first.
- #4 is retained entire, `release-gated`, and surfaced in every result under `carried-not-gating`. A
  reader of any validation result sees MTDR does not claim external validation.
- The permitted release claim is narrowed in TDR-0045 itself, and any wider claim is declared false
  in the record rather than left to discretion.
- No measure was rewritten. The alternative of weakening #4 until the author could pass it was
  considered and rejected outright.

**The residual risk is real and is not mitigated away**: `externally-validated` could become a
holding pen for anything inconvenient. Foreclosed in TDR-0045, watched at review, and countable —
there are now two re-scopings, and a third would be evidence of a pattern rather than of two sound
judgements.

## Customer-outcome projection

An adopter takes a governed artefact that states plainly what is not yet proven. That is better than
no artefact, and better than an artefact whose gate was left permanently shut. The harm to guard
against is the release being *read* as an adoption claim — addressed by narrowing the permitted
claim in the record.

## Control side-effects

Naming a transition creates a place to put things. The countervailing pressure is that every move
needs a record with a name and a subject-based reason, and that the count is visible.

## Execution capability

One field on one register entry. Nothing else changes.

## Constraints

Proceed only with these.

1. **The release claim is limited to what TDR-0045 states.** No release note, README, announcement or
   artefact may claim external validation, proven adoption, ease of installation or usability while
   #4 is outstanding.
2. **#4 stays `release-gated` and carried in every result.** It is not re-stated as pending, not
   marked not-applicable, and not removed.
3. **A third re-scoping requires this case to be re-opened and re-assessed before it lands**, not
   after. Two is a judgement; three is a pattern.
4. **`externally-validated` gains no other obligation without its own record**, so it cannot quietly
   become the place inconvenient constraints go.
5. **The evidence that eventually discharges #4 must be uncoached**, and its provenance recorded:
   who ran it, what they were given, what they were not told, and their raw output rather than a
   summary.
6. **The first intended participants are the author's own business architecture team, and that must
   be recorded as a partial answer.** They are independent of the *authoring role* but they are not
   *unknown to the author*, which is what the measure says. Their trial is admissible evidence and it
   does not, by itself, discharge #4. Recording it as full discharge would be reinterpreting a
   measure to fit the participants available — the quieter form of the failure constraint 1 of
   DAC-0044 forbids.

## Review

At the evidence named in TDR-0045, or 2027-02-27, whichever is sooner. This case reopens immediately
on any third re-scoping, on any release claim exceeding the permitted one, or on #4 being recorded as
discharged by evidence from a coached or author-adjacent participant.
