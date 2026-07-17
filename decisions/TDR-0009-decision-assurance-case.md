---
id: TDR-0009
title: Add the Decision Assurance Case as the TDR's second sibling record
status: accepted
template: minimal
decision_date: 2026-07-17
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0002, TDR-0003, TDR-0008
confirmed_by_outcome: pending — review 2026-10-05, alongside TDR-0003 and TDR-0008
---

# TDR-0009 — Add the Decision Assurance Case as the TDR's second sibling record

## Context — what was known at the time

AI accelerates the production of decisions; the TDR preserves them; neither proves a decision is
safe to execute. The gap shows sharpest where protective controls are involved: fraud and customer
outcomes are assured separately today, so the foreseeable harm that lives in their tension — a
control that reduces losses while excluding, delaying or distressing customers — is nobody's
finding. Regulators have made the design-time expectation explicit (outcome assessment at the
moment of decision, not retrospective documentation; aggregation of exposures, not one-at-a-time
approval), and agentic execution raises the cost of a weakly challenged decision from a slow
programme to an operational event. The VR (TDR-0008) had already established the sibling-record
pattern: one decision, multiple records with different lifecycles.

## Decision

Add the **Decision Assurance Case (DAC)** as the TDR's second sibling record and first-class
artefact: the TDR records organisational judgement; the DAC records the organisational reasoning
that tests whether that judgement is fit to execute. Ship as one release: the DAC specification
(four questions, compiler model of reusable reasoning skills compiling into one case, six
dispositions, ten-axis risk vector with trend and a no-composite-score rule, uncertainty and
decision-debt and learning blocks, `stale` as a standing-loss state); a template; a frontmatter +
structured-block JSON Schema; **eight reasoning skills** (systems-thinking, systems-dynamics,
fraud-and-adversarial-thinking, customer-outcomes, adaptive-capacity,
accumulated-and-resultant-risk, counterfactual-and-evidence, assurance-synthesis); and an
agentic-payment worked example. Proportionality governs: bare decisions never need a case. The
case records the risk *delta* and declares interactions; computing the resultant organisational
position is graph work outside the standard. Patterns and profiles are anticipated as extension
layers, never core.

## Alternatives rejected

- **A separate compliance checklist after the decision** — rejected: recreates the split this
  record exists to close; the control-side-effect insight requires one integrated case.
- **Gate TDR acceptance on the assurance case** — rejected: the record captures judgement and may
  be accepted while the case says stop; assurance gates *execution*, not recording. Conflating
  them would corrupt the record's time-of-decision honesty.
- **A composite risk score** — rejected: false precision; a single amber conceals the axis that
  should stop the decision.
- **Fold assurance into the existing skills** — rejected: evidence-review checks a record's
  completeness; challenging the judgement and projecting its consequences are different work with
  a different output (a disposition, owned).

## Options foreclosed

The DAC's non-goal is committed: it must never be presented as proof of correctness or compliance.
The sibling-record pattern is now load-bearing (TDR · VR · DAC); a fourth record type inherits its
conventions or argues against them by superseding TDR.

## Review

Confidence medium: the skill set and routing will move with adopter use (exactly as TDR-0003
anticipated for the original skills). `confirmed_by_outcome` reviewed 2026-10-05 with TDR-0003 and
TDR-0008 — evidence sought: cases written by adopters, and whether the contradiction hunt
(assurance-synthesis) surfaces findings single projections missed.
