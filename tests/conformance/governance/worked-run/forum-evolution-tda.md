# Forum evolution projection — Technology Design Authority

Machine-readable: [`forum-evolution-tda.json`](forum-evolution-tda.json). **Shadow only.**

## The next nudge

> Precompute the Standards 3, 7, 9 and 11 conformance assessment continuously and deliver it to the
> Authority as evidence, rather than assembling it by hand for each meeting. **The Authority continues
> to approve.** What changes is who assembles the evidence, and when.

## Why it can move now

The standards register states that Standards 3, 7, 9 and 11 are expressed as **testable conditions
with defined pass criteria**. Across six meetings, 64 of 71 assessments conformed with no discussion
recorded, and in no case did the Authority overturn the dashboard's assessment.

Standards 1, 2, 4–6, 8 and 10 are principles requiring judgement. They are not in scope, and the fact
that they rarely appear in the minutes is not evidence that they are deterministic.

## What stays

- **The cross-domain trade-off.** Contact effectiveness against data minimisation had no pass criteria
  and produced genuine, minuted disagreement. It stays with the Authority.
- Exception handling for non-conformances.
- Escalation of retention matters.
- **Gate 2 approval itself.**

## The authority gate

`jobs_delegable_with_bounds` names standard pattern approvals — and they are **not available now**.
The terms of reference §5 state that Gate 2 approval is reserved to the Authority and **may not be
delegated**.

Precomputing the *evidence* needs no new authority. Moving standard approvals to a delegated path
would require amending the terms of reference, and **who may amend them is `UNKNOWN`**. This
projection names that gate rather than routing around it.

## Preconditions, success, stop

**Preconditions** — three clean parallel cycles; every divergence investigated and explained; the four
source systems' coverage of the estate confirmed.

**Success evidence** — precomputed and manual assessments agree across three cycles; analyst effort
measurably below the 3 person-day baseline; no Gate 2 decision changed by the substitution.

**Stop conditions** — the Authority overturns a precomputed assessment; any of the four standards is
reclassified from testable to judgement; the conformance rate moves materially without explanation;
divergence recurs in more than one cycle.

## Monitoring, challenge, accountability

`population_monitoring_required` — conformance rate by standard tracked for drift; every case where a
precomputed pass would have been overturned; changes assessed as conforming that later generate an
incident.

`independent_challenge_requirements` — precomputation supplies evidence to the Authority; **it must
not become the decision.** The Authority retains the ability to reach a different conclusion, and every
such case is recorded.

`accountability_terminus_requirement` — a named individual must be accountable for the precomputed
assessment. The reconstruction found **no named terminus for the Authority itself**, which has to be
resolved first.

## What this is not

One bounded step with exit criteria. Not a target operating model, and nothing here proposes that the
Authority meet less often or approve fewer things.
