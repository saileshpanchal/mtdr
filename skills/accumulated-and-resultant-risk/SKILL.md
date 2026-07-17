---
name: accumulated-and-resultant-risk
description: Assess a decision's risk in two contexts — the local consequence of this decision, and the organisation's resultant total position after it interacts with everything already in flight. One of the three always-run assurance skills. Use it inside every Decision Assurance Case, and whenever someone asks "what's our total exposure", "how does this interact with what we've already approved", or approvals are accumulating one decision at a time.
---

# Accumulated and Resultant Risk

The core question: **what is the organisation's current exposure, what does this decision add or
remove, and what is the resultant total position?** The case records the *delta* and declares the
*interactions*; computing the accumulated and resultant position is the work of whatever decision
graph the organisation runs — this skill makes sure the graph has what it needs. Read
`spec-decision-assurance.md` §5.2.6.

## The one rule

**Risk registers hold decisions one at a time; organisations fail in the aggregate.** The exposure
that ends institutions is the one no single approval contained.

## Process

1. **Distinguish the four views** — and never let one impersonate another:

   | View | Meaning |
   |---|---|
   | Inherent risk | Exposure before the proposed controls |
   | Local residual risk | Exposure remaining within this decision after controls |
   | Accumulated risk | Combined contribution of related active decisions |
   | Resultant position | Net organisational exposure after interactions, concentration and transfer |

2. **Record the delta.** By risk type (adversarial, customer harm, operational, conduct,
   technology, data, third party, workforce): what this decision **increases**, **decreases**,
   **transfers** (to which channel, cohort or process) and leaves **unknown**.
3. **Declare the interactions** — the effects a conventional register misses:
   multiple decisions relying on the same control; several agents sharing one identity or
   authority mechanism; concentration in one supplier, model, data source or platform; controls
   that reduce abuse but raise customer harm; risk moved between channels or cohorts; correlated
   failure modes; temporary exceptions accumulating into a permanent operating model; many small
   changes collectively breaching a tolerance; risk velocity outgrowing monitoring capability;
   reversibility decaying as later decisions build on this one.
4. **State the resultant position as far as it can be known** — by risk type, cohort, journey,
   capability, agent and supplier — with its **trend**: `improving`, `deteriorating`,
   `stabilising` or `oscillating`. Trend against appetite matters more than today's snapshot: five
   tolerable decisions on a deteriorating trend are an intolerable sixth.
5. **Check appetite.** Is the resultant position inside the organisation's declared boundaries —
   and who is accountable for the aggregate, as opposed to the parts?

## Worked example — not a dependency

**BCBS 239** arose from banks' inability to aggregate exposures and identify concentrations
quickly and accurately in 2008: every position was approved; the aggregate was never seen. The
same principle applies to transformation and autonomous-decision risk — exposure fragmented across
individual approvals is the failure mode this skill exists to prevent.

## Anti-patterns

- **Local-only assurance** — a decision "within tolerance" assessed against an unexamined total.
- **Register thinking** — listing risks without declaring the interactions between decisions.
- **Snapshot risk** — reporting today's position without its trend.
- **The exception ratchet** — temporary exceptions renewed until they are the operating model,
  never appearing in any aggregate.
