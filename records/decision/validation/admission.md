# TDR — admissibility test

Applied on top of the shared invariants in
[`shared/candidacy-and-ratification.md`](../../../specification/candidacy-and-ratification.md). Admissibility
asks whether a candidate is **worth putting in front of a named owner** — not whether it is correct.

## The test

A candidate decision is admissible when all of the following hold.

1. **A decision is present, not a plan.** Both a choice and a binding consequence are evidenced —
   **We decide** and **This means** can each be filled from contributions. Material describing intent,
   status or aspiration fails here, and failing is the correct outcome.
2. **The context contributions are contemporaneous.** Every contribution to `context` traces to
   material created at or before `decision-date`. A candidate whose context depends on later material
   is inadmissible until that contribution is removed.
3. **Provenance is complete.** Every interpreted value traces to a locatable span. No exceptions, and
   no value carried "for completeness".
4. **The grouping basis is admissible**, where the candidate draws on more than one source.
5. **Missing mandatory roles are reported, not filled.** A candidate missing `accountable-owner` is
   admissible; a candidate with an invented one is not.
6. **The proportionality outcome is stated** — the template tier, or a recommendation of no record,
   with the reversal-cost reasoning behind it.
7. **Conflicts are recorded, not resolved.**

## Inadmissible

- Any value with no span behind it.
- A committee or role recorded as `accountable-owner`.
- `context` containing outcome knowledge — what was learned afterwards, presented as what was known.
- A status beyond `proposed`.
- A candidate assembled solely on co-occurrence.
- A full-template candidate where the evidence describes something cheap to reverse.

## Admissible but incomplete — the normal case

Most real material yields candidates missing something. **This is a result, not a failure.** A
candidate with a clear decision, sound context, a date, and no named owner is exactly the finding worth
surfacing: it tells the organisation that a decision it acted on has nobody attached to it.

Report it, list the gap, and let a named person close it. Do not withhold the candidate because it is
incomplete, and do not complete it to make it presentable.

## What this test does not do

It does not assess whether the decision was **good**, whether the reasoning was **sound**, or whether
the consequences are **acceptable**. Challenging consequences is the Decision Assurance Case's work
([`spec-decision-assurance.md`](../specification/dac.md)); challenging the candidate's
*interpretation* is [`challenge-record`](../../../skills/shared/challenge-record/)'s. Admissibility asks only
whether the evidence supports proposing this to a human.
