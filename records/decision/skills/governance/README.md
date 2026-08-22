# Governance reconstruction skills

**Status:** proposed under [TDR-0034](../../../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md).
Not accepted, and carrying no standing.

## What this is, and what it is not

This is a **substrate for the governance an organisation already has** — not a framework that replaces
it, and not a governance platform.

Governance regimes accrete. A regulated organisation cannot remove Model Risk Management, an AI
inventory, Consumer Duty governance, operational resilience governance, audit, complaints handling, a
Technology Design Authority or a risk committee because a common architecture happens to supply the
same property. Those mechanisms stay. What this sub-family does is reconstruct **what each one is
actually doing**, evidence what can be demonstrated, and identify the smallest authorised next change.

> Take the governance estate the organisation already has; reconstruct what it really does;
> distinguish record, observation, inference, contradiction and unknown; expose which powers and
> obligations actually exist; and propose one bounded change without pretending that computation
> created the authority to make it.

The sequence is continuous, not a migration:

```
current governance → reconstruct → demonstrate → identify gaps and duplication
   → authorise one bounded nudge → observe the new state → reconstruct again
```

**No skill here assumes the end state is fewer forums.** A forum may shrink, change cadence, become
more strategic — or become *more* consequential, as independent challenge grows more valuable when
execution becomes autonomous.

## Why these live in the decision package

Forums are **mechanisms for consequential judgement, challenge and disposition**. A Technology Design
Authority, a Risk Committee and an AI Governance Forum are not additional kinds of organisational
truth; they are apparatus through which existing Authority, Decision, Evidence, Value and Inheritance
semantics are exercised. So these skills sit beside the [assurance skills](../assurance/) under
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md), and **no sixth record family
is created**.

**These skills orchestrate and project across those semantics. They do not redefine them.** Semantic
ownership stays with the record family that owns it — which matters most where the owning family does
not yet exist normatively: `obligation-authority-trace` spans authority and inheritance, both candidate
packages, and must not become their de facto owner by default.

## The skills

| Skill | Does |
|---|---|
| [`governance-reconstruct`](governance-reconstruct/) | Finds the obligations, policies, authorities, controls, evidence requirements, waivers and accountable roles a corpus evidences |
| [`forum-reconstruct`](forum-reconstruct/) | Reconstructs a forum's real jobs, its seven separated powers, and whether its challenge is genuinely independent |
| [`obligation-authority-trace`](obligation-authority-trace/) | Why does this exist, who required it, who may exercise, challenge, waive or amend it |
| [`demonstrability-drill`](demonstrability-drill/) | Takes one decision from six months ago and tests whether the organisation can demonstrate it |
| [`governance-equivalence`](governance-equivalence/) | Finds overlap, and distinguishes duplicated evidence from separately mandated mechanisms |
| [`forum-evolution`](forum-evolution/) | Proposes one bounded next change for a forum, with its evidence, authority and stop conditions |
| [`regime-preservation`](regime-preservation/) | The guardrail — refuses removals that evidence and authority do not support |
| [`governance-accretion-plan`](governance-accretion-plan/) | Sequences the estate through observe, shadow, measure, reuse, nudge, consolidate, enforce |

The first five reconstruct; the last three propose, and nothing they propose executes. Read in order,
they answer the two questions the pack exists for:

> How does this organisation currently govern this class of consequential decision, what can it prove
> about that governance, and what is the smallest authorised next change that improves demonstrability
> without breaking or pretending to replace existing obligations?

> Which jobs still require this forum, which can now be precomputed or delegated, which independent
> challenge must be preserved, and what evidence would justify the next change in its shape or cadence?

## What every skill here produces

[Projections](../../validation/governance-projection.md), never records. A projection carries
interpretation about organisational meaning rather than organisational meaning itself, fails question 1
of the [record admission test](../../../../specification/record-admission-test.md) by design, and
carries `carries_standing: false` structurally.

Epistemic state is assessed **per claim**, never per document or per output. A single forum
reconstruction routinely carries a `RECORDED` stated purpose, an `OBSERVED` evidence-assembly job, an
`INFERRED` de-facto authority, an `UNKNOWN` waiver authority and a `CONTRADICTORY` accountable owner at
once.

The deterministic rules are [`governance-rules.md`](../../validation/governance-rules.md). The five
that constrain hardest:

- **No authority manufacture** — detecting de-facto authority is a finding, never a grant.
- **Regime preservation** — a mechanism whose mandate cannot be located is not thereby optional.
- **No adjudication** — reconstruct a challenge's evidence and route; never determine its outcome.
- **No automatic retirement** — `RETIRE_CANDIDATE` is a question, not a decision.
- **Unknown and contradictory survive** — end to end, and never resolved by recency or seniority.
