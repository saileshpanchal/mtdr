---
id: DAC-0039
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0039
title: Assure the state-relative requirement invariant
status: accepted
disposition: proceed
assessed_at: 2026-08-18
accountable_owner: Sailesh Panchal
review_date: 2027-02-18
confidence: high
supersedes: none
---

# DAC-0039 — Assure the state-relative requirement invariant

## Uncertainty

Known: the defect, its cause and its extent. The VR specification already ruled the state-relative
case; the schema's own conditional rule already implemented it; a global `required` entry made that
rule unreachable. One field, one line, and a specification that needs no change. Unknown: whether the
invariant as stated is the right generalisation, or whether further record families will meet a shape
it does not cover. Assumption: the pattern — a transition prerequisite encoded as a representation
prerequisite — is general rather than a Value Record accident. Confidence is high, which is unusual
here and is warranted by the correction being narrower than the rule that motivates it.

## Adversarial projection

Routed for misuse of the rule rather than of the code. The realistic abuse is **the invariant read as a
licence**: a future author citing TDR-0039 to make a genuinely universal requirement optional, because
"it is only needed at ratification" is easy to assert about almost any field. The control is that the
invariant carries its own limit — *unless it is genuinely required in every valid lifecycle state* —
and that the VR correction is deliberately one field wide, with the three retained fields named and
reasoned. A second exposure is silent regression in either direction; the suite now asserts both,
because a check that only tested loosening would have permitted re-tightening.

## Customer-outcome projection

Routed lightly and materially. Requiring completeness at the wrong lifecycle moment does not produce
complete records; it produces records completed to satisfy a validator. A beneficiary nobody confirmed
becomes a beneficiary the record asserts, and the cohorts whose evidence is thinnest are exactly the
ones where that substitution happens most often and matters most.

## Control side-effects

The rule could encourage schemas so permissive that nothing is caught early, or authors so cautious
about conditionals that they omit requirements altogether. The counterweight is that conditional
requirements are *more* work to author than global ones, so the failure mode is under-application
rather than over-application — which is what the review trigger watches for.

## Execution capability

Fully within reach and already exercised. The correction is one line; the conditional rule existed;
six schema probes cover candidate, ratified and settled in both directions; three fixtures and three
subjects demonstrate the separation end to end.

## Risk delta and declared interactions

Decreases false rejection of legitimate states, forced completion, and the collapse of structural
validity into transition eligibility. Increases the risk that the rule is over-read. Interacts with
TDR-0019 (unchanged), TDR-0027 (the standing boundary this makes testable), TDR-0033 (whose separation
this applies at authoring time) and every record family not yet admitted.

## Risk vector

| Axis | Assessment and basis |
|---|---|
| severity | medium — a wrongly rejected state produces dishonest records rather than no records |
| likelihood | high — the defect already occurred once, unnoticed, beside its own correct rule |
| exposure volume | medium now, high later — every future record family inherits the pattern |
| velocity | low — schema changes are deliberate and reviewed |
| concentration | medium — one rule governs authoring across all families |
| detectability | high now — the suite asserts the state-relative form in both directions |
| reversibility | high — loosening a required field is backward compatible; every prior record stays valid |
| control confidence | high — the correction is narrower than the rule, and both directions are tested |
| customer-cohort distribution | concentrated where evidence is weakest, which is where forced completion does most damage |
| time horizon | continuous, and most consequential at each new family's admission |
| trend | improving — the rule exists before the families that would have repeated the defect |

## Decision debt

- Apply the invariant when admitting the authority, work and evidence packages, and record whether it
  covered the shapes met — owner Sailesh Panchal, due at each admission.
- Re-examine the wording if a proposed application of the rule would widen rather than relocate a
  requirement — owner Sailesh Panchal, on occurrence.

## Monitoring contract

- Hypothesis: transition prerequisites stay conditional on the states that need them, and every state a
  specification permits is representable. Counter-hypothesis: the rule is cited to remove a genuinely
  universal requirement, or a schema again rejects a permitted state. Test: the state-relative check in
  `tests/verify.py`, in both directions, plus review of every new conditional against the specification
  it implements. Metric is states a specification permits and its schema rejects, and requirements
  loosened past the state that needs them; threshold is one; owner Sailesh Panchal; trigger is block
  the change and reopen TDR-0039 if the invariant rather than its application is at fault.

## Learning obligations

Retain every case where a reviewer and an author disagree about whether a requirement is universal or
transition-specific, with the specification text relied on. That disagreement is the rule's real
working surface, and the VR case suggests it can persist unnoticed next to its own resolution.

## Disposition

**Proceed.** Not proceed-with-constraints: the judgement is supportable and the implementation is
complete, tested in both directions, and narrower than the rule that motivates it. The specification
required no change, the correction is one field, and the three fixtures demonstrate the separation the
rule exists to protect.

The single thing to watch is stated in the adversarial projection and carried into the review trigger:
this invariant relocates requirements to the states that need them. It never removes them.

Skills run: systems-thinking, counterfactual-and-evidence, accumulated-and-resultant-risk,
fraud-and-adversarial-thinking, customer-outcomes (light), adaptive-capacity, assurance-synthesis.
