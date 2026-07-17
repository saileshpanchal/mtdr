---
name: systems-thinking
description: Widen a decision from the immediate feature or change to the system it lands in — actors, incentives, dependencies, feedback loops and second-order effects — before the decision is assured. Use this skill at the start of every Decision Assurance Case (it is one of the three always-run assurance skills), and whenever someone says "what could this affect", "who else is touched by this", or a decision is described purely in terms of its intended benefit.
---

# Systems Thinking

This skill identifies interactions; its sibling **systems-dynamics** predicts behaviour. Read
`spec-decision-assurance.md` for where the output lands in the case.

## The one rule

**The decision's stated scope is never the system's scope.** The interesting consequences live
where the decision touches things its author did not mention.

## Process

1. **Draw the boundary — then challenge it.** What is inside the decision's system, and what has
   been placed outside that money, data, incentives or customers actually flow across?
2. **Map actors and incentives.** Everyone the decision touches — customers, colleagues, agents,
   suppliers, intermediaries, adversaries — and what each gains or loses. Incentives predict
   behaviour better than intentions.
3. **Trace dependencies both ways.** What must hold upstream for this decision to work; what
   depends on it downstream. Name the shared mechanisms (a control, an identity scheme, a supplier)
   this decision now also leans on.
4. **Find the loops.** Reinforcing loops (adoption → data → better service → adoption) and
   balancing loops (friction, capacity, appetite). Note which loops the decision strengthens,
   weakens or removes.
5. **Ask where the pressure goes.** Constraints rarely disappear; they move. Risk squeezed out of
   one journey re-appears in another channel, team or cohort — say where.
6. **State second- and third-order hypotheses.** Not certainties: falsifiable hypotheses about
   delayed and indirect consequences, each with the observation that would confirm or kill it.
7. **Ask what the optimised measure damages.** Every decision optimises something; name what that
   optimisation could quietly degrade elsewhere.

## Outputs

System boundary · actor and dependency map · causal hypotheses · reinforcing and balancing loops ·
unintended-consequence hypotheses · system-level monitoring indicators (feed the monitoring contract).

## Anti-patterns

- **Scope worship** — assessing only what the decision says it changes.
- **Intention accounting** — mapping what actors are meant to do instead of what they are paid to do.
- **Loop blindness** — treating consequences as one-shot when the system will iterate them.
- **Certainty inflation** — presenting second-order guesses as findings rather than hypotheses.
