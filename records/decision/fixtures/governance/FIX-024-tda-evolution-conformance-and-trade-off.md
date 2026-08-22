# FIX-024 — precompute the deterministic conformance, keep the trade-off human

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** forum evolution. **Proves:** a projection recommending that deterministic conformance be
precomputed while authorised human judgement is preserved for a genuine cross-domain trade-off — and
that the recommendation names the authority the change would require (GR-14), the monitoring that
replaces inspection, and its stop conditions.

Builds on the reconstruction in [FIX-018](FIX-018-tda-real-jobs-not-stated-purpose.md).

## Sources

**A — the TDA reconstruction from FIX-018**, showing roughly 50 of 80 minutes on `DETERMINISTIC_CONFORMANCE`,
one `TRADE_OFF_JUDGEMENT` item, two exceptions, and 3 analyst-days of manual dashboard assembly.

**B — Architecture Standards register, `arch-standards-v11.md`, 2025-04-01**

> Standards 3, 7, 9 and 11 are expressed as testable conditions with defined pass criteria. Standards
> 1, 2, 4–6, 8, 10 are principles requiring judgement in application.

**C — TDA minutes sample, `tda-minutes-2025-09 to 2026-02.md`**

> Six meetings. 71 changes assessed against Standards 3, 7, 9, 11. 64 conformed with no discussion
> recorded. 7 non-conformances were returned to delivery teams. In no case did the Authority overturn
> the dashboard's conformance assessment.

**D — TDA terms of reference, `tda-tor-v4.md`, section 5**

> Approval of design at Gate 2 is reserved to the Authority. The Authority may not delegate Gate 2
> approval.

## Expected

- One `forum-evolution-projection` for the TDA, `shadow_only: true`.
- `jobs_automatable_or_precomputable` naming the Standards 3, 7, 9, 11 conformance assessment — with
  the reasoning from B (testable conditions with defined pass criteria) and C (64 of 71 conformed
  without discussion, and the Authority never overturned the assessment).
- `jobs_requiring_human_or_independent_judgement` naming the contact-effectiveness against
  data-minimisation trade-off — genuinely cross-domain, with no defined pass criteria, and the item
  the Authority actually spent its judgement on.
- `jobs_unchanged` naming exception handling for the non-conformances, and the escalation route.
- `new_evidence_capability` — continuous conformance assessment against the four testable standards,
  produced before the meeting rather than assembled for it.
- `new_authority_or_delegation_required` — **mandatory here and non-trivial**: D reserves Gate 2
  approval to the Authority and forbids delegation, so precomputing the conformance *evidence* is
  available now, while moving standard approvals to a delegated path is **not**, and would require an
  amendment to the terms of reference by whoever may amend them.
- `population_monitoring_required` — drift in the conformance rate, and any case where a precomputed
  pass would have been overturned.
- `stop_conditions` — a precomputed assessment contradicted by the Authority; a standard reclassified
  from testable to judgement; conformance rate moving materially.
- `accountability_terminus_requirement` naming who answers for a precomputed assessment.

## Must not

- **Recommend delegating Gate 2 approval.** D forecloses it, and the projection must name the
  amendment authority rather than route around the constraint.
- Recommend precomputing Standards 1, 2, 4–6, 8, 10. B says they require judgement in application, and
  the fact that they rarely appear in the minutes is not evidence that they are deterministic.
- Read "64 of 71 conformed with no discussion" as evidence the Authority is unnecessary. It is
  evidence about **that job**, and GR-13 requires the recommendation to address jobs rather than the
  forum's existence.
- Fold the trade-off item into the automatable set because it, too, involved standards. It had no pass
  criteria and the Authority's minute records genuine disagreement.
- Recommend a cadence change. This projection does not touch cadence, so
  `population_monitoring_required` here covers the precomputation rather than a reduced meeting
  frequency — FIX-031 is where cadence is tested.
- Present a target operating model. One bounded nudge, with exit criteria.
