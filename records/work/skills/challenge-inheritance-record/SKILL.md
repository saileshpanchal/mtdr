---
name: challenge-inheritance-record
description: EXPERIMENTAL, not part of the MTDR standard (TDR-0047) — challenge a draft Operational Inheritance Record with the work language's own failure modes — a participant described under a capability's name, authority asserted rather than referenced, responsibility read as authority, experience recorded as practice, a run book in disguise, and a supersession caused only by a change of participant. Use this skill on every draft OIR before it is brought into force, whenever someone asks "would this survive the next reorganisation?" or "where did this authority come from?", after the shared structural challenge has run. It never treats a clause that references another record as a defect.
---

# Challenge Inheritance Record

> **Experimental** under [TDR-0047](../../../../decisions/TDR-0047-experimental-packages.md). Not part
> of the MTDR standard.

The work language's specialisation of the challenge stage. The **structural mechanics** — walking
every statement back to a span, reading spans alone, tense and modality shifts, attacking the
grouping, checking gaps are gaps — are the shared skill's,
[`challenge-record`](../../../../skills/shared/challenge-record/), and run first. This skill then
challenges what only the work language can get wrong.

## The one rule

**Replace the participant and read the record again.** Do it three times: another team, a supplier,
an AI participant. Every sentence that has to change was describing the worker, not the work.

## The inheritance-specific challenges

1. **Is this a capability or a participant?** The title, the purpose and every job, under the
   participant-change test.
2. **Is any authority asserted rather than referenced?** Every limit in **You may** traces to an
   instrument by identifier. One that traces only to a hand-over note is manufactured.
3. **Has responsibility been read as authority?** Being responsible for a job grants nothing.
4. **Has eligibility or allocation been read as authority?** Who may perform a job, and who is
   allocated to it, are separate decisions, and neither creates authority.
5. **Is experience recorded as practice, or practice as fact?** A failure history belongs to
   **You inherit**; a default way of working belongs to **You should**.
6. **Is this a run book in disguise?** Steps, screens and buttons are procedure. The OIR replaces none.
7. **Does a reference restate its source?** Restated content drifts, and the record then carries two
   answers to one question.
8. **Is every `missing` clause genuinely missing** — or was the material that held it not read?
   Conversely, has a `missing` clause been quietly filled?
9. **Are conflicts preserved?** A `conflicting` clause that cites one source has chosen.
10. **Is the inherited state current?** Supersession evidence elsewhere in the material — a changed
    control, a retired dependency — makes this draft stale.
11. **Is a change of participant being treated as a change of state?** A supersession whose only cause
    is a new team, supplier or AI participant fails the lifecycle hypothesis
    ([`fixtures/lifecycle/`](../../fixtures/lifecycle/)).
12. **Is this actually a decision, a value commitment or an authority instrument?** Route it; do not
    force it.

## Dispositions

Exactly one per draft: **split** (two capabilities merged) · **merge** (one capability divided) ·
**reject** (not inherited state — with the boundary test it fails) · **incomplete** (genuine but
under-evidenced, with its `missing` clauses) · **retain** (fit to propose as drafted).

## What is never a finding

- **A clause marked `reference`.** That a clause is held by another record is the information
  TDR-0046's deletion attack measures. Treating it as a defect would have the implementation grade its
  own hypothesis.
- **A clause honestly marked `missing`.** The gap is the record working.
- **Whether the OIR should exist at all.** That is TDR-0046's question, answered by a deletion attack
  and an independent reviewer, never by this skill.

## Anti-patterns

- **Participant sympathy** — accepting a team's name in the title because everyone knows who does it.
- **Authority by plausibility** — passing a limit because it is the obvious one.
- **Reference anxiety** — pressing a `reference` clause to be restated so the record "stands alone".

## Scope note

Structural challenge is the shared skill's; this adds the work language's semantics only, per
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md).
