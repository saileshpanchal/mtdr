---
id: DAC-0007
tdr_id: TDR-0112
title: Assure the delegated agent-initiated payments decision before pilot execution
status: accepted
disposition: proceed-with-constraints
assessed_at: 2026-07-02
accountable_owner: A. Fenwick, Chief Risk Officer
review_date: 2026-10-02
confidence: medium
supersedes: none
assurance:
  uncertainty:
    knowns:
      - "Pilot cohort is 5,000 opted-in current-account customers; agent authority capped at £150/txn, £400/month"
      - "Mandates are purpose-bound (household bills, groceries) and revocable in-app in one step"
    unknowns:
      - "Real-world rate at which customers over-delegate and stop reviewing agent activity"
      - "Adversary adaptation speed once mandate mechanics are public"
    assumptions:
      - "ASSUMPTION: customers who delegate retain awareness of their balance position (confidence: low)"
      - "ASSUMPTION: mandate revocation will be discoverable by customers in distress (confidence: medium)"
    confidence_basis: "Pilot design evidenced; behavioural assumptions rest on one 400-person study"
  risk_delta:
    increases:
      - "adversarial: new social-engineering surface — 'set up an agent for me' scams targeting older cohorts"
      - "conduct: customers may not understand agent-initiated payments are not disputable as unauthorised"
    decreases:
      - "operational: fewer missed-bill incidents in the pilot cohort"
    transfers:
      - "fraud pressure moves from card-not-present to mandate-enrolment (channel transfer, monitored)"
    unknowns:
      - "aggregate exposure if agents are later granted merchant-initiated top-ups"
    effective_from: 2026-07-14
    expected_duration: "90-day pilot"
    expected_trajectory: "Enrolment-scam exposure front-loaded in weeks 1-4 while mandate mechanics are novel; operational benefit accrues from week 2; concentration risk grows if either sibling pilot scales"
    dependency_conditions:
      - "Concentration exposure changes shape if either of the two sibling delegated-authority pilots converts to product on the shared identity provider"
      - "Delta is void if the mandate registry caps are raised — a cap increase requires a superseding case"
    declared_interactions:
      - "shares the step-up authentication control with the existing remote-onboarding journey"
      - "shares the mandate registry with two other delegated-authority pilots (concentration)"
      - "correlated failure: one identity provider underpins enrolment for all three pilots"
  risk_vector:
    severity: { level: medium, basis: "capped per-transaction and monthly limits bound worst-case loss" }
    likelihood: { level: medium, basis: "enrolment-scam patterns already observed in analogous products" }
    exposure_volume: { level: low, basis: "5,000-customer pilot, caps enforced at the mandate registry" }
    velocity: { level: high, basis: "agent-initiated flows execute without per-transaction review" }
    concentration: { level: medium, basis: "single identity provider across three delegated pilots" }
    detectability: { level: medium, basis: "per-mandate telemetry exists; cohort-differential reporting is new and unproven" }
    reversibility: { level: high, basis: "one-step revocation; pilot kill-switch tested in rehearsal" }
    control_confidence: { level: medium, basis: "enrolment step-up proven elsewhere; distress-revocation path untested with assistive-technology users" }
    cohort_distribution: "Exposure concentrates in cohorts most susceptible to enrolment coercion — older customers and financially stressed customers"
    time_horizon: "90-day pilot; re-assessed before any cap increase"
    trend: stabilising
  decision_debt:
    - { item: "Assistive-technology journey testing for mandate revocation", kind: deferred-evidence, owner: "L. Okonkwo, Customer Outcomes", due: 2026-08-15 }
    - { item: "Manual review of enrolments flagged as coached until the detection model is trained", kind: manual-mitigation, owner: "R. Shah, Fraud Ops", due: 2026-09-30 }
    - { item: "Single-identity-provider concentration accepted for pilot only", kind: temporary-assumption, owner: "A. Fenwick, CRO", due: 2026-10-02 }
  monitoring_contract:
    - hypothesis: "Purpose-bound caps keep agent-initiated fraud loss below card-baseline for the cohort"
      counter_hypothesis: "Losses stay low while enrolment coercion harms concentrate in older customers"
      test: "Weekly cohort-differentiated fraud and complaint review"
      metric: "Loss per active mandate; coercion-flagged enrolments per 1,000, by cohort"
      threshold: "Cohort differential > 2x cohort average for two consecutive weeks"
      owner: "R. Shah, Fraud Ops"
      trigger: "Suspend new enrolments for affected cohort; reopen TDR-0112"
    - hypothesis: "One-step revocation keeps customers in control of delegated authority"
      counter_hypothesis: "Revocation exists but is not reachable by customers in distress or using assistive technology"
      test: "Representative-cohort journey testing including assistive-technology users"
      metric: "Revocation completion rate; time-to-revoke; abandonment in the revocation journey"
      threshold: "Any tested cohort below 90% unassisted completion"
      owner: "L. Okonkwo, Customer Outcomes"
      trigger: "Redesign revocation journey before cap increase; escalate to CRO"
  learning:
    hypotheses:
      - "Delegation reduces missed-bill harm without reducing balance awareness"
      - "Mandate-enrolment displaces rather than reduces social-engineering attempts"
    experiments:
      - "A/B: monthly agent-activity digest vs none — effect on balance awareness and disputes"
    evidence_required:
      - "Cohort-differentiated outcomes at week 6 and week 12"
      - "Displacement telemetry from the card channel over the same window"
  constraints:
    - "No cap increase before the assistive-technology revocation evidence lands (due 2026-08-15)"
    - "New enrolments pause automatically if coercion-flag threshold breaches"
    - "Identity-provider concentration must be resolved before pilot converts to product"
  skills_run:
    - systems-thinking
    - counterfactual-and-evidence
    - accumulated-and-resultant-risk
    - fraud-and-adversarial-thinking
    - customer-outcomes
    - systems-dynamics
    - adaptive-capacity
    - assurance-synthesis
---

> **Fictional worked example.** Halford & Vane Bank, its people and its numbers are invented. The
> example shows a full Decision Assurance Case for an **agentic payment journey** — the standard's
> natural first proving ground (spec §8). Identifiers follow the bank's own numbering.

# DAC-0007 — Assure the delegated agent-initiated payments decision before pilot execution

Assures **TDR-0112** ("Pilot delegated agent-initiated payments for household spending"), accepted
2026-06-24. The TDR records the judgement; this case tests what it could cause. Per the non-goal
(spec-decision-assurance §1), nothing here proves the decision correct — it proves the challenge
was systematic and the uncertainty declared.

## How the four questions were answered

**How could it be exploited?** The adversarial pass priced the change: enrolment, not transaction,
is the new economics — coaching a customer into creating a mandate beats stealing a card, because
the resulting payments are *authorised*. Abuse cases centre on coached enrolment, mandate-purpose
gaming, and authority accumulated across small caps. Recovery is the weak anchor: agent-initiated
payments sit outside the unauthorised-payment dispute path, so redress depends on the coercion
flag, which is new.

**Who could be harmed even working as designed?** The customer-outcome pass found the design
concentrates convenience in confident digital cohorts and risk in cohorts susceptible to coercion
— and that "working as designed" includes customers losing track of delegated spending they no
longer review. Non-financial harm (distress on discovering unrecognised-but-authorised payments)
is foreseeable and was previously unassessed.

**Could the controls themselves create poor outcomes?** Yes — twice. The step-up authentication at
enrolment excludes assistive-technology users at a measured 3× abandonment differential in the
analogous onboarding journey; and the coercion-flag manual review adds a delay that lands hardest
on financially stressed customers making time-critical bill payments. Both are in the monitoring
contract with cohort-differentiated thresholds; the first is decision debt with a date.

**What evidence would show the assumptions were wrong?** The two monitoring hypotheses' counter-
hypotheses, plus the reopening condition: any deterioration of the vector's `trend` from
stabilising, or the balance-awareness A/B showing delegation degrades awareness, reopens TDR-0112.

## The synthesis

The contradiction hunt surfaced the case's defining tension: **fraud exposure falls while
vulnerable-cohort exposure rises** — losses are capped and observable, but the harm channel moves
to enrolment coercion and inaccessible revocation, which are neither. Local residual risk is
within appetite; the *declared interactions* (shared step-up control, shared mandate registry,
single identity provider across three pilots) mean the resultant position depends on decisions
outside this case — flagged for the organisation's aggregate view with a `stabilising` trend that
must be re-read before any cap increase.

Disposition: **proceed-with-constraints** — the three constraints in the frontmatter, each owned,
each testable, with the pilot's kill-switch rehearsed. The alternative dispositions were argued:
*stop* failed the do-nothing baseline (missed-bill harm is real and measured); *experiment* was
rejected because the pilot already is the bounded experiment; *proceed* unqualified failed on the
assistive-technology evidence gap.
