---
name: systems-dynamics
description: Predict how a decision's system behaves over time and under change — growth, stress, tipping points, dominant loops and the new equilibrium — where systems-thinking identifies the interactions, this skill runs them forward. Use it when adoption could scale, when behaviour under stress matters, when a decision changes the economics of a journey, or whenever someone asks "what happens if this takes off" or "what happens when it breaks".
---

# Systems Dynamics

Systems thinking identifies interactions. Systems dynamics predicts behaviour. Different questions;
this skill answers the second. Read `spec-decision-assurance.md` for where the output lands.

## The one rule

**A system's behaviour at 2× is not its behaviour at 1× twice.** Assurance done only at today's
volumes assures a system that will not exist.

## Process

1. **Double it.** What happens if adoption, volume or delegation doubles? Which control, team,
   supplier or data source saturates first — and what happens at that saturation?
2. **Stress it.** Behaviour under load, outage, incident and attack. Which balancing loops
   (capacity, review, human approval) quietly disappear under pressure, and what do they stop
   restraining when they do?
3. **Find the tipping points.** Thresholds beyond which behaviour changes qualitatively — where
   fraud becomes economic at scale, where a queue becomes abandonment, where a manual mitigation
   stops being performable.
4. **Name the dominant loop.** Of the loops the systems-thinking pass mapped, which comes to
   dominate as the system grows? Reinforcing loops that are negligible today may govern the
   end-state.
5. **Describe the new equilibrium.** Systems do not return to the old normal; they settle
   somewhere new. Describe the settled state the decision plausibly produces — including for the
   adversary, whose behaviour also reaches equilibrium.
6. **State the velocity.** How fast does each failure mode develop relative to how fast the
   organisation can detect and respond? Velocity feeds the risk vector directly.

## Outputs

Scaling hypotheses with saturation points · stress behaviour · tipping-point thresholds (these
become monitoring thresholds) · dominant-loop analysis · projected equilibrium · velocity
assessment for the risk vector.

## Anti-patterns

- **Linear extrapolation** — assuming 2× volume means 2× everything.
- **Static adversary** — modelling the attacker at today's economics while scaling the system.
- **Equilibrium denial** — assuring the transition and ignoring the settled state.
- **Stress amnesia** — treating the loops that vanish under pressure as permanent controls.
