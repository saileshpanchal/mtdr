# FIX-031 — automating transaction conformance does not replace what a periodic review saw

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** cadence and population sensing. **Proves:** GR-16 — a periodic governance job may not be
removed or slowed because transaction-level conformance has been automated, where the replacement
population or cohort sensing does not yet exist. The automation sees transactions; the review saw
cohorts.

## Sources

**A — Customer Outcomes Forum terms of reference, `cof-tor-v2.md`, 2024-06-01**

> The Forum meets monthly to review customer outcome MI across the arrears journey, and to identify
> where outcomes for identifiable groups of customers diverge from the population.

**B — Customer Outcomes Forum minutes, `cof-2025-11-12-minutes.md`**

> The Forum reviewed November MI. Complaint volumes and contact-frequency breaches were within
> tolerance at population level. The Forum noted, from the cohort view, that customers with no
> recorded vulnerability flag but three or more failed contact attempts showed a complaint rate 2.4x
> the population, and commissioned analysis. This group is not visible in the standard exception
> reporting.

**C — Ashcombe design note, `ashcombe-design-v3.md`, section 9, 2026-01-28**

> The engine enforces the CC-11 contact cap as a hard constraint. Every contact decision is checked
> against the cap at decision time; breaches are structurally impossible and no longer require
> detective control.

**D — Governance efficiency proposal, `cof-cadence-proposal-2026-07.md`**

> With contact-frequency breaches now structurally prevented by the Ashcombe engine, and complaint
> volumes reported to the Collections Leadership Team weekly, the Customer Outcomes Forum could move
> from monthly to quarterly.

**E — Ashcombe MI specification, `ashcombe-mi-spec-v1.md`, 2026-06**

> Reporting: contact volumes, cap enforcement events, channel mix, decision latency, model score
> distribution. All measures reported at population level.

## Expected

- The Forum's jobs reconstructed, distinguishing the **transaction-level conformance** job (contact
  cap breaches) from the **population and cohort sensing** job evidenced by B.
- C accepted as genuinely removing the first job — the cap is enforced at decision time and the
  detective control is redundant for that specific breach type.
- D's cadence proposal **refused as stated**, with `population_monitoring_required` non-empty and
  naming what must exist first: cohort-level outcome measures, specifically for groups the standard
  exception reporting does not surface — of which B supplies a worked example that was found only
  because someone looked at the cohort view monthly.
- E recorded as the direct evidence for the refusal: every planned Ashcombe measure is population
  level, so the replacement sensing does not yet exist.
- Any `forum-evolution-projection` here carrying `population_monitoring_required`,
  `stop_conditions` and `accountability_terminus_requirement`, and remaining `shadow_only`.
- The reasoning stated plainly — B's 2.4x cohort was **within tolerance at population level**, which
  is exactly why removing the cohort view is not equivalent to removing a redundant check.

## Must not

- **Accept the cadence reduction because the breach control is genuinely redundant.** It is redundant,
  and that is not the question. This is the failure under test.
- Treat weekly complaint reporting to the Collections Leadership Team as the replacement. It is
  population-level volume reporting to a different body, and B's finding was invisible at population
  level.
- Count "no breaches possible" as an improved outcome measure. It is an improved control, and the
  Forum's outcome job is a different job.
- Recommend the cadence change conditional on cohort MI being "planned". E shows what is planned, and
  it is population level; a precondition satisfied by intent is not satisfied.
- Recommend abolishing the Forum. GR-13 — address the jobs.
- Emit a `cadence_change_candidate` with an empty `population_monitoring_required`. The schema rejects
  it, and the rejection is the point.
