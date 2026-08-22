---
name: forum-evolution
description: Generate the next bounded change for one governance forum — which job moves, why it can move now, what evidence and authority that requires, what stays with the forum, what monitoring replaces periodic inspection, and when to reassess. Use this skill after a forum has been reconstructed, when someone asks "can we shorten this meeting?", "could the design authority stop reviewing standard patterns?", "should this forum still meet monthly?" or "what would let us delegate these approvals?". It proposes one nudge with exit criteria rather than a target operating model, never assumes that more autonomous execution means fewer forums, and refuses to slow a periodic review while the population sensing that would replace it does not yet exist.
---

# Forum Evolution

One forum, one bounded next change, with the evidence and authority that change would require.

Read [`governance-projection.md`](../../../validation/governance-projection.md) and
[`governance-rules.md`](../../../validation/governance-rules.md) first. This skill consumes a
[`forum-reconstruct`](../forum-reconstruct/) output and produces nothing without one — a projection
about a forum nobody reconstructed is an opinion.

## The typical trajectory, and why it is not a plan

```
AS-IS      human forum receives documents → people reconstruct context
           → discuss routine conformance, exceptions and judgement → minutes become evidence

HYBRID 1   authority and evidence reconstructed beforehand → forum receives a demonstrable case
           → routine evidence assembly disappears → humans focus on contradictions and judgement

HYBRID 2   deterministic conformance handled before the forum → forum handles exceptions, novel
           trade-offs and challenge → evidence and decision record created continuously

HYBRID 3   delegated low-consequence decisions execute within bounded authority
           → forum monitors population outcomes and drift → escalations become event-driven

AGENTIC    routine governance jobs delegated to appropriate participants → forum may shrink, change
           cadence or disappear → retained human and independent authority handles constitutional
           judgement, amendment, material exception and accountability
```

**This is a description of what tends to happen, not a route to follow.** The output is the *next*
step from wherever this forum actually is — with its preconditions, its success evidence and its stop
conditions — never an imagined final organisation.

## The end state is not fewer forums

No projection may assume it (GR-13). A forum can legitimately:

- shrink, as evidence assembly moves out of it;
- change cadence, as inspection becomes monitoring;
- become more strategic, as routine conformance is precomputed;
- **become more consequential** — because independent challenge and accountable judgement get *more*
  valuable at scale, not less, as execution becomes autonomous.

Recommendations address **jobs, authority and evidence**. A recommendation whose content is "hold
fewer meetings" has addressed none of them.

## The seven things every recommendation must state

1. **What job moves** — by job class, from the reconstruction.
2. **Why it can move now** — the evidence that makes it safe today and did not exist before.
3. **What evidence is needed** — the capability that must exist first.
4. **What authority is needed** — mandatory wherever any job is delegated (GR-14). No exceptions,
   including where the delegation looks obviously fine.
5. **What remains with the forum** — explicitly, including everything that stays because it is
   judgement, exception or challenge.
6. **What new monitoring replaces periodic inspection** — see below.
7. **When to reassess** — a trigger, not a date, wherever a trigger exists.

## Three refusals that are structural, not advisory

**Independent challenge is never collapsed into the execution authority it challenges** (GR-15). This
is the most plausible-looking bad recommendation available here, because a challenge forum and a
delivery forum genuinely do see the same evidence, and merging them genuinely does save time. It
removes the only place the decision was examined by someone who did not make it. Every projection
touching a challenge function states `independent_challenge_requirements`.

**Cadence is never reduced while the replacing population sensing does not exist** (GR-16). A periodic
customer-outcome review whose transaction-level conformance has just been automated looks ready to
slow down. The automation sees transactions; the review saw cohorts. Removing it deletes the only
place a pattern *across* transactions was visible. `population_monitoring_required` is mandatory
wherever cadence changes, and lists what must exist first.

**Accountability terminates in a person** (GR-18). `accountability_terminus_requirement` names the
individual who answers for the job after the change, or states plainly that it is unresolved — which
blocks the change rather than qualifying it.

## Worked shapes

```
TDA           precompute architecture conformance → preserve human judgement for novel trade-offs
              → move standard approvals to delegated authority → retain material exceptions and
              constitutional change

Risk forum    continuous risk and evidence projection → remove manual MI assembly → event-driven
              escalation on threshold breach → forum focuses on appetite trade-offs, exceptions and
              challenge

AI governance shared organisational evidence substrate → retain model-risk and AI-specific assurance
              → remove duplicate evidence collection → progressively route routine decisions to
              ordinary governance
```

Each is a *next step* for a forum in a particular state, not a template.

## Output

One `forum-evolution-projection`, `shadow_only` until proven. Preconditions, success evidence and stop
conditions are all mandatory and all non-empty — a nudge with no stop condition is not bounded, and an
unbounded nudge is a reorganisation.

## When to refuse

- **Asked for the target operating model.** Not this release, and not this skill. The output is one
  step with exit criteria.
- **Asked to recommend abolishing a forum.** Address the jobs. If every job has demonstrably moved and
  the authority has followed it, that is what the projection says, and it remains a recommendation
  requiring an authorised decision.
- **Asked to skip the authority step** because the delegation is obviously safe. GR-14 has no
  exception, and "obviously safe" is where delegation drifts.

## Anti-patterns

- **The efficiency read** — every job that could move, moving, with no account of what the forum was
  catching.
- **Aspirational end-state** — a diagram of the future organisation instead of the next authorised step.
- **Silent challenge loss** — a merge recommendation whose independence consequence is not stated.
- **Cadence arithmetic** — halving a meeting's frequency because half its agenda is automatable, with
  no sensing to replace what the other half saw.
