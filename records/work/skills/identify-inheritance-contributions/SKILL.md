---
name: identify-inheritance-contributions
description: EXPERIMENTAL, not part of the MTDR standard (TDR-0047) — identify which spans of supplied organisational material contribute to the state a participant must inherit before performing a piece of operational work, asking the inheritance question of every fragment rather than looking for anything shaped like a record. Use this skill on hand-over notes, run books, support matrices, terms of reference, incident reviews and onboarding packs when someone asks "what would the next person need to know?" or "what does this work carry with it?", and before any inheritance drafting runs. It reports participant leakage instead of absorbing it, and it contributes an authority claim only as a reference to the instrument that delegated it.
---

# Identify Inheritance Contributions

> **Experimental** under [TDR-0047](../../../../decisions/TDR-0047-experimental-packages.md). Not part
> of the MTDR standard.

The work language's specialisation of the identify stage. The **mechanics** — fragmenting before
interpreting, verbatim spans, two confidences graded separately, the hindsight rule, recovery-not-
failure-detection — are the shared skill's,
[`identify-record-contributions`](../../../../skills/shared/identify-record-contributions/), and are
not repeated here. This skill adds what is inheritance-specific.

## The one rule

**The question is "does this span contribute to the state a participant must inherit before doing
this work?" — never "does this document look like an OIR?"** None will. Inherited state is scattered
across material written for other purposes, most of it in the voice of whoever did the work last.

## The contract

**Input:** arbitrary source material plus its source metadata. **Output:** `SourceFragment`s and
`RecordContribution`s with `target_object: operational-capability`, each carrying its clause as
`semantic_role`, its `derivation`, both confidences and temporal context — plus **participant-leakage
reports**, any **`unclassified` outcomes**, and a plain summary. **Never an OIR, never a candidate.**

**"No inheritance contribution identified" is successful execution, not failure.**

## The vocabulary

The ten clause keys of [`specification/inheritance-contribution.md`](../../specification/inheritance-contribution.md),
with the role rules of [`validation/semantic-roles.md`](../../validation/semantic-roles.md). A
fragment may contribute to several clauses. Material relevant to inheritance that fits none is
reported as `unclassified` — never near-fitted, never dropped, never an eleventh clause.

## Inheritance-specific recognitions

- **Participant leakage is reported, not absorbed.** Allocation (*Ana covers Tuesdays*), procedure
  (*click Repair, then Submit*), structure (*the exceptions team*) and eligibility (*only Level 2 staff*)
  contribute nothing. Each is listed, so a reader can see how much of the material was about the
  worker rather than the work.
- **Authority is contributed as its source, or flagged.** A span that cites the instrument contributes
  that reference to `authority`. A span that states a limit with no instrument contributes with low
  epistemic confidence, flagged unsourced. The limit itself is never the contribution.
- **Experience is context.** *It failed twice last winter on name changes* is `inherited-context`.
  *Check recent name changes first* is `practices`. A span doing both contributes to both.
- **The organisation's thresholds are context.** What counts as severe, material or acceptable for
  this work is `inherited-context`, and frequently also feeds `escalation`.
- **Hand-over notes are rich and participant-voiced.** *I always ring the scheme desk before ten* may
  carry a dependency, a practice and an allocation at once. Separate them; do not discard the span
  because it is personal.
- **A job must survive the participant-change test at identification.** A span that names work only
  as a team's remit contributes no job.

## Anti-patterns

- **Run-book harvesting** — steps contributed as practices.
- **Team-charter harvesting** — a team's remit contributed as jobs.
- **Authority by assertion** — a stated limit contributed as if delegated.
- **Experience flattened into practice** — the failure history lost inside a recommendation.
- **Leakage absorbed** — allocation silently dropped, so the record looks capability-centred when the
  material was not.

## Scope note

Mechanics, refusals and the recovery posture are the shared skill's. This skill adds the work
language's semantics only, per
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md).
