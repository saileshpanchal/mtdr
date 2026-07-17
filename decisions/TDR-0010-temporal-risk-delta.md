---
id: TDR-0010
title: Make the risk delta temporal, and sharpen the DAC's object semantics
status: accepted
template: minimal
decision_date: 2026-07-17
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0009
confirmed_by_outcome: pending — review 2026-10-05, alongside TDR-0009
---

# TDR-0010 — Make the risk delta temporal, and sharpen the DAC's object semantics

## Context — what was known at the time

External review of the just-released v1.4.0 identified that the risk delta was static — a
before/after snapshot — when real decisions change risk *over time*: a migration duplicates
exposure before reducing it; concentration materialises only when another decision lands;
a pilot becomes unsafe as adoption scales. A static delta cannot tell a decision graph when the
declared change holds. The same review pressed for the DAC's object semantics to be unambiguous
(skill outputs advisory, never verdicts), for `defer-pending-evidence` and
`experiment-within-bounded-authority` to have a machine-readable route out rather than becoming
permanent holding states, and for the standard to state that adoption is progressive — a graph
must never be an implicit prerequisite for conformance.

## Decision

Ship as v1.5.0, additive:

- **Temporal risk delta.** `riskDelta` gains optional `effective_from`, `expected_duration`,
  `expected_trajectory` and `dependency_conditions`. The principle enters spec §5.2.6: the case
  declares what risk the decision is expected to change, when, and under what conditions; the
  graph determines the accumulated and resultant position *at any point in time*.
- **Object semantics.** Spec §3 states that skill outputs are advisory evidence contributing to
  the case, never verdicts — the synthesis produces the one disposition, its named owner signs it.
- **No standing states.** Spec §5.2.11: `defer-pending-evidence` and
  `experiment-within-bounded-authority` name their resolving evidence as dated, owned
  decision-debt items; the review date or a monitoring trigger reopens the disposition.
- **Progressive adoption.** Spec §4 states the ladder — TDR → TDR + DAC → organisational risk
  context → decision graph → continuous assurance — each rung useful without the next; and the
  accumulated-and-resultant-risk skill states that for a graphless adopter its required output is
  the declared delta and interactions, with the computed position explicitly out of scope.
- **Wording.** "Fit to execute" framing replaced with "a TDR preserves the judgement; it does not
  prove the consequences are acceptable" — "safe" and "fit" overclaim what assurance can prove.

## Alternatives rejected

- **Rename decision debt to "assurance debt"** — rejected: the standard's origin is the *Decision
  Debt* article series (acknowledged in the README); renaming the field severs the lineage. The
  reviewer's definitional point is adopted instead as spec text: the debt lies in the evidence
  required to sustain confidence in execution, not necessarily in the decision itself.
- **Drop accumulated-and-resultant-risk from the always-run trio** — rejected: the proposal made
  the skill optional while keeping its output (the declared delta and interactions) mandatory,
  which mandates the artefact while optionalising the discipline that produces it honestly. The
  ritual-completion concern is answered inside the skill instead: the resultant position is
  explicitly out of scope for a standalone adopter.
- **Remove systems-dynamics as premature** — rejected: shipped in v1.4.0, distinct in kind
  (systems-thinking identifies structure; systems-dynamics predicts behaviour at scale), and
  routed rather than always-run, so its overlap cost is already contained. Removing a published
  skill would be a weakening of the assurance core (spec §10).
- **Fold uncertainty and decision debt back into counterfactual-and-evidence** — rejected: both
  shipped as first-class blocks in v1.4.0; demoting them is a removal from a published standard.

## Options foreclosed

The temporal fields commit the delta to being a time-shaped declaration; a future graph
implementation that ignores `effective_from`/`dependency_conditions` is non-conforming with the
declared intent. The trio is confirmed as normative; changing it now requires a superseding TDR.

## Review

Confidence high: every change is additive and the rejections preserve published semantics.
`confirmed_by_outcome` reviewed 2026-10-05 with TDR-0009 — evidence sought: whether adopters
populate the temporal fields, and whether any deferred disposition is found standing past its
review date.
