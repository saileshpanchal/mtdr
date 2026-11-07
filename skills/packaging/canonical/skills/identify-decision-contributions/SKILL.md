---
name: identify-decision-contributions
description: Identify which spans of supplied organisational material contribute to reconstructing a consequential decision — minutes, papers, emails, transcripts, reviews — asking the decision question of every fragment rather than looking for anything shaped like a record, and annotating each with the times and evidence kind that historical recovery needs. Use this skill when someone asks "was a decision made here?", "who decided this, and when?" or "what did we decide in 2019 and never write down?", and before any decision recovery is reconciled or drafted. It reports what is not a decision, and evidence that no decision was made, as findings in their own right, and it never infers who acted, under what authority, or instead of what.
---

# Identify Decision Contributions

The decision language's specialisation of the identify stage. The **mechanics** — fragmenting before
interpreting, verbatim spans, two confidences graded separately, recovery not failure detection — are
the shared skill's, [`identify-record-contributions`](../../../../skills/shared/identify-record-contributions/),
and are not repeated here. This skill adds what is decision-specific, and what historical material
needs.

## The one rule

**The question is "does this span contribute to reconstructing a decision?" — never "does this
document contain a decision record?"** None will. The choice is in a minute, the options in a paper it
cites, the owner in an email, and whether it happened in a review written a year later.

## The contract

**Input:** source material and its metadata. **Output:** `SourceFragment`s and `RecordContribution`s
with `target_object: consequential-decision`, each carrying a class from
[`decision-contribution.md`](../../specification/decision-contribution.md) as its `semantic_role` until
drafting tightens it; **one fragment annotation per fragment** — capture time, creation time, evidence
kind, and what a restatement restates; **a `considered` annotation on every context contribution**;
`unclassified` outcomes; and a plain summary. Never a TDR, never a candidate.

**"No decision evidenced" is successful execution.** It says the material is silent, not that the
organisation decided nothing.

## The vocabulary

The classes, the five reasons something is not a decision, the kinds of evidence that no decision was
made, and the roles recovery treats specially are defined once, in
[`decision-contribution.md`](../../specification/decision-contribution.md), and are not restated here.
The decision test itself — a commitment of money or time, or a foreclosed option — is
[`decision-identification`](../decision-identification/)'s.

## Decision-specific recognitions

- **A paper recommends; a minute decides.** Options set out in a paper are `alternative` contributions
  only as presented. The decision is where the choice was recorded.
- **The owner is named in the material, or missing.** Never the author of the document, the chair of
  the meeting, a team, or whoever leads such work now.
- **Authority is a reference.** *Under the delegation of 4 February* contributes the instrument. A
  limit stated with no instrument behind it is a claim, flagged, never a grant.
- **Later material corroborates; it never explains.** A review saying the change went live in June is
  `corroboration`. Its account of why the board chose it is not context, however plausible.
- **A deferral is a decision only if it commits.** *We will not proceed until the audit reports*
  commits; *the item was deferred* does not, and is `non-decision: deferred`.

## What historical material adds

Apply [`historical-recovery.md`](../../../../specification/historical-recovery.md) as it stands:

- **Times at their precision, each with a basis.** The fragment's own statement or its source's
  metadata. A folder, a filename or a neighbouring document is no basis, and the time is `unknown`.
- **Capture is not creation.** A transcript written up a week later was captured at the meeting.
- **Pre-dating is not consideration.** A memo that existed before the meeting is `considered:
  unlinked` unless a fragment shows it was before whoever decided.
- **Restatements are marked.** A paper quoted in three emails is one source.
- **Never inferred:** the roles and classes the vocabulary names — who acted, under what authority,
  instead of what. `explicit`, or no contribution.

## Anti-patterns

- **Record hunger** — every agenda item a decision; the proportionality test exists to stop this.
- **Document date as decision date** — the paper's date, the folder's date, the file's date.
- **The plausible owner** — authorship, chairing or current role treated as accountability.
- **Explanation from the outcome** — a later review's reasons filed as what was known.
- **Silence as absence** — *no decision evidenced* reported as *no decision made*.

## Scope note

Mechanics, refusals and the recovery posture are the shared skill's. This skill adds the decision
language's semantics only, per [TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md),
under the vocabulary of [TDR-0049](../../../../decisions/TDR-0049-decision-recovery-vocabulary.md).
