---
name: assurance-synthesis
description: Orchestrate a Decision Assurance Case — route the reasoning skills, combine their outputs, hunt the contradictions between them, and produce the single disposition with its constraints. Always the closing skill of a DAC. Use it when the projection passes are done and someone must answer "so may this decision execute, and under what conditions?"
---

# Assurance Synthesis

The compiler's final pass: the skills produce projections; this skill produces **one case, one
disposition, one owner**. Read `spec-decision-assurance.md` §5 for the record it fills.

## The one rule

**The contradictions are the findings.** Any single projection can look tolerable; the case exists
to catch the places where two projections disagree about the same decision.

## Routing

The routing rule is normative in `spec-decision-assurance.md` §4 — the three always-run skills,
the declared triggers for the rest, this skill always closing. Apply it from there; do not
re-derive or extend it. Record which skills ran and why the others were not material — an honest
"not material" beats a padded pass (the seven-dimensions rule, applied to assurance).

## The contradiction hunt

Search the combined outputs for, at minimum:

- Adversarial exposure falls, but vulnerable-cohort exclusion rises.
- Customer friction falls, but identity or authority confidence deteriorates.
- Productivity rises, but operational knowledge concentrates in fewer heads or one supplier.
- Local risk is within tolerance, but the resultant position or its trend is not.
- Controls exist, but their effectiveness cannot be observed (no metric, no threshold, no owner).
- The decision is safe alone, but unsafe alongside a named active decision.

Each contradiction is resolved, constrained, or escalated — never averaged away.

## The disposition

One of six, with constraints stated as testable bounds:

**proceed** · **proceed-with-constraints** (name them, each with an owner and a metric) ·
**experiment-within-bounded-authority** (scope, duration, reversal path, success evidence) ·
**escalate** (to whom, with which unresolved contradiction) · **defer-pending-evidence** (which
evidence, by when, owned by whom) · **stop** (which finding stops it — usually a vector axis, not
a score).

Before closing, verify the case carries: the uncertainty block; decision debt (owned and dated);
the monitoring contract (every hypothesis observable); the learning obligations; and a named
accountable owner for the case itself. A case missing any of these is not complete — it is
`defer-pending-evidence` on itself.

## Anti-patterns

- **Averaging** — blending a red projection and three greens into amber. The vector, never a score.
- **Constraint theatre** — "proceed with constraints" whose constraints no one owns or can measure.
- **Escalation as disposal** — escalating without naming the contradiction the senior owner must resolve.
- **Completion bias** — treating the case as done because every skill produced output, rather than
  because the contradictions between the outputs were confronted.
