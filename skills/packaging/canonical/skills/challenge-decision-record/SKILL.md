---
name: challenge-decision-record
description: Challenge a candidate decision record with the decision language's own failure modes — hindsight presented as context, an owner or authority manufactured, a paper's options read as the decision, a retrospective read as an explanation, one source counted several times, and an attestation read as a renewal. Use this skill on every drafted or recovered TDR candidate before it is put to a named individual, whenever someone asks "would this survive scrutiny?" or "did they really decide that, then?", after the shared structural challenge has run. It applies the evidence matrix claim by claim, routes the evidence-review and assurance questions rather than restating them, and records its recommendation beside the candidate, never in it.
---

# Challenge Decision Record

The decision language's specialisation of the challenge stage. The **structural mechanics** — walking
every value back to a span, reading spans alone, tense and modality, attacking the grouping, checking
gaps are gaps — are the shared skill's, [`challenge-record`](../../../../skills/shared/challenge-record/),
and run first. This skill then challenges what only the decision language can get wrong.

## The one rule

**Attack the hindsight hardest.** A recovered decision reads well precisely when someone who knew the
outcome filled it in. Every sentence of context must survive the question *could this have been
written on the day?*

## The decision-specific challenges

1. **Is every context contribution contemporaneous?** Recompute each grade from its times and its
   `considered` state ([`historical-recovery.md`](../../../../specification/historical-recovery.md));
   a `later` contribution is not context, and an `indeterminate` one cannot be presented as context.
   Material dated the decision's own day is the commonest trap: the date orders nothing.
2. **Does every time have a basis?** The fragment's own statement or its source's metadata. A time
   resting on a folder, a filename or a neighbouring document is `unknown` — test every one.
3. **Was the material considered, or did it merely exist?** A pre-dating memo with no link is
   circumstance.
4. **Does each claim rest on a kind of material that can support it?** Apply the matrix in
   [`decision-contribution.md`](../../specification/decision-contribution.md) claim by claim: a paper
   does not decide, an author is not an owner, a retrospective supports occurrence and nothing else.
5. **Is the owner evidenced, or reasoned into place?** Who chaired, who wrote, who leads such work now —
   none of them is the owner unless a span says so. The person attesting the account is never the
   owner.
6. **Is the authority a reference to something real — and did the act invoke it?** A stated limit
   with no instrument is a claim. An instrument that fits but is not cited is applicability, a finding:
   if it has been recorded as authority, that is the manufactured authority this skill exists to catch.
7. **Are the alternatives the ones considered, or the ones that would have been sensible?**
8. **Has one source been counted several times?** Follow every restatement to what it restates.
9. **Is this one act?** Separate acts split; one decision across several candidates merges; one
   motion carried on one vote stays one composite candidate, each resolution traceable.
10. **Is continuation being read as a decision?** An arrangement that outlived its term is persistence
    unless an act extending it is evidenced.
11. **Is it still current — and is anyone reading the account as though it were?** Supersession
    elsewhere in the material, and any suggestion that attesting the account renews the decision.
12. **Is the evidence complete for its dimensions?** Apply [`evidence-review`](../evidence-review/)'s
    discipline rather than re-deriving it.
13. **What would the assurance lenses find?** Where the candidate is a one-way door, route it to the
    [assurance skills](../assurance/assurance-synthesis/) — this skill does not run them.

## Dispositions

Exactly one **recommendation** per candidate: **split** · **merge** · **reject** (not a decision, with
the boundary it fails) · **incomplete** (admissible, with any mandatory role missing or partial, and its
gaps named) · **retain** (admissible, every mandatory role supported — fit to put before a named
individual).

**A recommendation is this skill's output and nothing more.** It is never written into the candidate,
and it becomes a review event only when a named individual acts on it
([`historical-candidate.md`](../../../../specification/historical-candidate.md)).

## What is never a finding

- **A missing owner, date or alternative honestly reported.** The gap is the candidate working.
- **`indeterminate` contemporaneity.** It is a finding about the evidence; forcing it either way is
  the backdating attack, however well meant.

## Anti-patterns

- **Hindsight sympathy** — accepting a reason because it is obviously right.
- **Date repair** — completing a partial date so that a grade clears.
- **Owner by default** — the senior person in the room recorded as accountable.
- **Recommendation as act** — writing `retain` into the candidate.

## Scope note

Structural challenge is the shared skill's; this adds the decision language's semantics only, per
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md). Whether the decision was
*wise* is not challenged here at all — that is the assurance case's question.
