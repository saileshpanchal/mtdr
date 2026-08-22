---
name: governance-accretion-plan
description: Generate a staged adoption plan across a selected governance estate, running observe then shadow then measure then reuse then nudge then consolidate then enforce, with preconditions, success evidence and a stop condition on every stage. Use this skill after forums have been reconstructed and their evolution projections produced, when someone asks "where do we start?", "what would a rollout look like?" or "how do we sequence this without breaking anything?". It never places a new mechanism in the critical path at first stage, surfaces legal review as a design input rather than a downstream approval, refuses to invent return-on-investment where the organisation's own cost data is absent, and treats the discovery of a previously untraceable consequential decision as evidence the mechanism works.
---

# Governance Accretion Plan

The estate-level output. Individual forums get evolution projections; this sequences them into an
adoption path that can be stopped at any stage.

Read [`governance-rules.md`](../../../validation/governance-rules.md) first. This skill consumes
[`forum-evolution`](../forum-evolution/) projections and the disposition ledger, and every step it
emits has already passed [`regime-preservation`](../regime-preservation/).

## The seven phases

```
PHASE 0  BASELINE     inventory, forum reconstruction, demonstrability drill, reconstruction-cost
                      baseline
PHASE 1  OBSERVE      no governance-path change. Surface gaps, duplication and unknowns
PHASE 2  SHADOW       structured evidence and projections generated alongside current forums, with
                      no execution dependency
PHASE 3  REUSE        existing forums and regimes consume shared evidence where proven
PHASE 4  NUDGE        bounded routine jobs move out of meetings or into delegated or deterministic
                      paths. Exceptions, independent challenge and judgement retained
PHASE 5  CONSOLIDATE  duplicated workflows and forums narrowed only where evidence and authority
                      justify it
PHASE 6  ENFORCE      selected properties enforced, only after proven shadow operation, legal and
                      risk review, and explicit authority
```

**Shadow before path.** No first-stage plan places MTDR, or any new commitment mechanism, in the
critical path. The sequence is `observe → shadow → measure → reuse → nudge → consolidate → enforce`,
and skipping to `reuse` because the shadow output looks convincing is the failure mode this ordering
exists to prevent.

Phases may be entered per forum rather than across the estate at once. A TDA at `NUDGE` and a
complaints forum at `OBSERVE` is a normal and usually better plan than an estate-wide phase gate.

## Start where evidence already exists

Prefer proving grounds with existing consequential decisions and existing evidence obligations, not
novel agentic use cases. Complaints, vulnerable-customer treatment, credit decisions, financial
promotions, TDA decisions and risk acceptances all carry evidence duties already, which means the
baseline is measurable and the shadow output is checkable against something.

**The architecture is organisational; agents inherit it later.** A plan that starts with the newest
technology starts where the evidence is thinnest.

## Measure reconstruction economics — and never invent them

Where the organisation's data supports it, capture current cost and time for governance-pack
preparation, audit evidence assembly, complaint reconstruction, risk and TDA paper production,
regulator and supervisor requests, skilled-person and assurance exercises, legal discovery, duplicated
control testing, and meeting preparation with its repeated context reconstruction.

**Do not invent ROI when the inputs are absent.** One estimated figure makes every real figure in the
plan unusable, and the numbers this exercise can produce honestly are the most persuasive thing it has.

## Legal is part of design

Every plan surfaces legal review for privilege, retention, disclosure, regulatory production,
complaints evidence and personal-data treatment. `PHASE 6 ENFORCE` requires
`legal_review_required: true` structurally.

These are design inputs. Routing them as downstream approvals produces a plan that gets stopped at the
point it becomes expensive to change.

## Two things to say out loud

**A more demonstrable governance system initially surfaces more findings, more unknowns and more
previously invisible ignored challenges.** That is the mechanism working. It will read as
deterioration on any dashboard counting findings, and a plan that does not warn its sponsor about this
in advance will be stopped at Phase 1 for succeeding.

**Where the sponsor's apparent success condition is only a green report, record it as a strategic
risk.** The desired condition is the opposite — discovery of a previously untraceable consequential
decision is evidence the mechanism works. A programme that can only return the answer it was
commissioned to return is measuring nothing, and that is a finding about the programme.

## Output

One `accretion-step` projection per step, each with a phase, preconditions, success evidence, a stop
condition and a next-phase gate. Steps are proposals requiring authorised decisions; nothing here
executes, schedules or commits anything.

## When to refuse

- **Asked to start at REUSE or later** because the case is obvious. The baseline is what later stages
  are measured against; without it, nothing can be shown to have improved.
- **Asked for a business case with no cost data.** Report what the estate does not measure — that is
  itself a finding worth having.
- **Asked to commit dates.** Stages gate on evidence, not calendar.

## Anti-patterns

- **Phase compression** — collapsing observe and shadow because the findings are already convincing.
- **Estate-wide gates** — holding a ready forum at Phase 2 because a different forum is not ready.
- **Invented benefit** — a savings figure derived from a duplication count.
- **The unstoppable plan** — steps with success evidence and no stop condition, which is a programme
  rather than an accretion.
