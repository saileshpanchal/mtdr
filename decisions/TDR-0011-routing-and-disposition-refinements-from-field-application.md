---
id: TDR-0011
title: Refine DAC routing and disposition from the first at-scale field application
status: accepted
template: minimal
decision_date: 2026-07-20
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0009
confirmed_by_outcome: pending — review 2026-10-20, alongside TDR-0009
---

# TDR-0011 — Refine DAC routing and disposition from the first at-scale field application

## Context — what was known at the time

v1.4.0/v1.5.0 defined the Decision Assurance Case and its reasoning skills but had not yet been
applied at scale. The first such application — running the assurance skills as agents over a
corpus of **machine-derived (transcript-extracted) decision records**, each thin and without a
stated owner — exercised the routing rule and the dispositions against inputs the standard had not
been pressed on before. Several seams surfaced, independently and repeatedly:

- **Routing read as category-matching, not materiality.** §4 lists the adversarial trigger as a
  flat set (money, identity, consent, authority, data). Applied literally it auto-fires on any
  decision that concentrates data or touches authority — an internal-correctness change, a
  procurement, a decision *not* to build — while the fraud-and-adversarial skill's own text says a
  decision that creates no new economics "needs little from this skill — say so and stop." The rule
  and the skill pulled in opposite directions, and customer-outcomes had the same ambiguity for
  decisions that reach customers only indirectly.
- **Thin records forced inference.** With no owner, evidence or alternatives in the source, the
  contradiction hunt had to reason about controls the record never proposed, which sat awkwardly
  against the no-averaging rule.
- **Disposition edge cases.** `proceed-with-constraints` assumes a named owner exists to hold each
  constraint; the source records named none. And records that fused two decisions of different risk
  had no explicit route other than assuring the blend.

## Decision

Ship as v1.6.0, additive — every v1.5.0 record still validates. The normative routing rule is left
intact; the refinements are added as clarifying guidance around it.

- **Materiality, not category** (DAC spec §4). The trigger lists are illustrative, not auto-firing:
  a lens is routed by whether the decision *materially* changes what the lens governs. A
  data/authority decision with no new external economics still runs adversarial thinking, but as an
  internal-integrity and reconciliation-abuse pass; customer-outcomes runs on indirect effects but
  lightly, recording why. An honest "not material, because …" is a complete pass.
- **Internal-integrity variant** (fraud-and-adversarial skill, step 1) and the **indirect-effect
  pass** (customer-outcomes) are stated in the skills, cross-referencing §4.
- **Fair-lending signpost** (customer-outcomes, step 1): for automated eligibility, pricing or
  credit, the cohort analysis is the indirect-discrimination test.
- **Compound and thin records** (assurance-synthesis): a fused record is **split**, not blended;
  a thin record's absent inputs are named as decision-debt, and inferred controls are declared as
  inferred and never averaged into comfort.
- **Vacant-owner disposition** (DAC spec §5.2.11): where the record names no accountable owner, the
  first constraint is to name one; a case that cannot name an owner defers rather than proceeding.
- **Trend vs trajectory** (DAC spec §6): a one-line cross-reference clarifying that non-monotonic
  transition shapes are carried by `expected_trajectory` (§5.2.6), not the point-in-time trend.

## Alternatives rejected

- **De-duplicate records that describe the same underlying decision, in-core.** Field application
  surfaced two records of one decision (an extraction artefact). Rejected per the scope boundary
  and [TDR-0002](TDR-0002-differentiate-on-accountability-semantics.md): de-duplicating extraction
  output is a tooling and pipeline concern, not the standard's. A `same_decision_as` lineage
  relation was considered and left out — the standard stays neutral on how records are produced.
- **Add a risk-vector trend value for "duplicates before reducing".** Rejected: the non-monotonic
  shape is already expressible via `expected_trajectory` (§5.2.6, added in v1.5.0); a cross-
  reference in §6 suffices, and a second overlapping field would be redundant.
- **Rewrite the normative routing rule.** Rejected: the rule stays as written so v1.5.0 records
  continue to conform; materiality enters as clarifying guidance beside it, not as a replacement.
