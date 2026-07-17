---
name: fraud-and-adversarial-thinking
description: Treat a decision as something an adversary will actively study and exploit — because the decision changed the economics or mechanics of the system. Use this skill inside a Decision Assurance Case whenever a decision touches money movement, identity, consent, authority, delegation to agents, customer data or any control an adversary could game; and whenever someone asks "how could this be abused" or "where does the fraud go".
---

# Fraud and Adversarial Thinking

Wider than traditional threat modelling: it asks how a criminal, a customer's agent, a merchant
agent or a compromised internal actor behaves *because this decision changed what is profitable or
possible*. Read `spec-decision-assurance.md` for where the output lands in the case.

## The one rule

**Adversaries read your release notes.** Every decision that changes the economics of a journey is
studied by someone whose job is to exploit it — assure the decision as if that study has already
happened.

## Process

1. **Price the new opportunity.** What does this decision make cheaper, faster, more scalable or
   less observable for an abuser? A decision that creates no new economics needs little from this
   skill — say so and stop.
2. **Enumerate the actors.** Criminal, opportunistic customer, insider, merchant, supplier, and —
   increasingly — the delegated agent: manipulated, colluding, or operating on compromised
   authority. Each with incentive and capability.
3. **Write the abuse cases.** For each actor, the concrete path: entry point, steps, extraction.
   Abuse cases mirror use cases; if the journey has seven steps, ask what each step yields an
   adversary.
4. **Attack the trust anchors.** What happens when identity, consent or authority is compromised
   rather than merely absent? Delegation chains deserve special attention: can authority be
   accumulated, replayed, or exercised past its purpose?
5. **Attack the controls themselves.** Can a control be bypassed, gamed, exhausted or weaponised —
   including *against customers* (lockout as denial-of-service, disputes as harassment)? Hand every
   control on this list to the customer-outcomes and control-side-effect passes.
6. **Follow the displacement.** When this control succeeds, where does the activity move — which
   channel, journey, cohort or institution inherits it?
7. **State the residue.** Preventive, detective and recovery controls; then the residual exposure,
   honestly, with a **named owner who accepts it**.

## Outputs

Abuse cases and attack paths · trust-anchor and delegation weaknesses · control hypotheses (with
their side-effect handoffs) · displacement hypotheses · residual exposure + named owner · runtime
indicators for the monitoring contract.

## Anti-patterns

- **Checklist threat modelling** — cataloguing generic threats instead of pricing what *this*
  decision changed.
- **Perimeter thinking** — treating insiders and authorised agents as out of scope.
- **Control worship** — counting controls as protection without asking how each is gamed.
- **Silent residue** — ending with controls instead of the exposure that remains and who owns it.
