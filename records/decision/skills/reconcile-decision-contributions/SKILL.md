---
name: reconcile-decision-contributions
description: Group decision contributions from different sources into candidate decisions, one question per candidate, splitting compound decisions and telling supersession from conflict — so that a choice recorded in a minute, the options in a paper it cites and an owner named in an email become one candidate only on admissible evidence. Use this skill whenever decision contributions come from more than one source, whenever someone asks "is this the same decision as that one?" or "did we change our minds, or contradict ourselves?", and before draft-tdr runs. It applies the shared reconciliation mechanics with the decision language's identity semantics, counts restatements of one source once, and never takes a date from a document.
---

# Reconcile Decision Contributions

The decision language's specialisation of the reconcile stage. The **mechanics** — admissible grouping
bases with named evidence, supersession versus conflict, missing semantics as a claim, assembly
confidence graded separately — are the shared skill's,
[`reconcile-record-fragments`](../../../../skills/shared/reconcile-record-fragments/), and are not
repeated here.

## The one rule

**One act per candidate.** *Adopt the platform, migrate the data and restructure the team*, decided by
three people at three meetings, is three decisions with three owners and three reversal costs, however
often they appear in one paragraph. A candidate that carries two acts will be ratified as one, and
whichever is weaker inherits the stronger one's evidence. **One act carrying several resolutions** —
one motion, one vote — is one composite candidate, each resolution kept traceable as its own
contribution ([One act, one candidate](../../specification/decision-contribution.md#one-act-one-candidate)).

## The contract

**Input:** decision contributions from one or many sources. **Output:** `CandidateAssembly` structures
with `target_object: consequential-decision`, each `grouping_basis` naming its evidence, and for every
grouping question one of the findings:

reinforcing contributions · contradictions · compound decision split · supersession · different
decisions · unresolved ambiguity.

## Decision-specific judgements

- **The minute's citation is the strongest basis.** *As set out in paper B/19/07* is an explicit
  cross-reference; the same programme, the same quarter or the same author is not a basis at all.
- **A revised decision under the same authority is supersession.** Both readings are kept, with their
  order. A different choice with no shared authority is a conflict, or a different decision.
- **Recency settles nothing.** The later document is not the later decision.
- **Independence counts once.** Three emails quoting one paper add one source, not three, to the
  evidence for any contribution — follow each `restates` to its source before counting
  ([`historical-recovery.md`](../../../../specification/historical-recovery.md)).
- **The date is the decision's, or missing.** Never a paper's, a folder's, or the earliest document's.
  A candidate without one is legitimate, and its contemporaneity is indeterminate.
- **`not-a-decision` and `non-decision` findings are not grouped into candidates.** They are carried
  to the report, with their reasons and kinds, as the vocabulary defines them.

## Anti-patterns

- **Merge by topic** — the same subject treated as the same decision.
- **The compound candidate** — three acts ratified as one.
- **The carved vote** — one motion split into three candidates, so that each resolution looks
  separately authorised.
- **Grouping by fit** — an instrument joined to a decision because its terms cover it. That is an
  applicability finding, reported beside the candidate.
- **Corroboration by copying** — a restated source counted each time it is restated.
- **Recency as supersession** — the newer document assumed to replace the older.

## Scope note

Mechanics and refusals are the shared skill's. This skill adds the decision language's identity
semantics only, per [TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md).
