# CASE-028 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-028.md` (items
A–C). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-028-1 — no further capital to Dunmore until the asset survey reports

File `CASE-028-1.hdc.json` · `event_time_ref: CASE-028-C3` (2023-06-07)

**As evidenced:** "The board will not commit further capital to Dunmore until the asset survey reports,
expected in December." (item B, capital board minute 2023-06-07, item 5, quoted).

This is a deferral that **commits**: it forecloses capital commitment until a named condition is met. The
vocabulary contributes it as a decision, not as `non-decision: deferred`.

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | missing | — |
| decision-date | supported (2023-06-07) | explicit (C3) |
| accountable-owner | missing | — |

Also `option-foreclosed`: committing further capital to Dunmore before the survey reports (C2);
`authority`: the capital board (C4). What the evidence did not supply: who owned it, and what was known.

**Contemporaneity:** no context contribution to grade.

**Admissibility:** 1 ✓ (choice: withhold further capital; consequence: none committed until the survey
reports) · 2 none ✓ · 3 ✓ · 4 single act-record ✓ · 5 owner and context reported missing ✓ · 6
undetermined · 7 none ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge:**
1. Is it a decision? Item 4 and item 5 sit side by side in one minute: one is a deferral that commits
   nothing, the other a deferral that commits. Same meeting, different findings. Kept apart; same-meeting
   is no basis for grouping.
2. "expected in December" is an expectation, with no year; not a commitment, not completed.
3. Owner (5): the board is a forum. Not filled.

**Recommendation: incomplete** (owner and context missing).

**Validation:** SCHEMA pass; all STRUCT checks pass. TDR-draft checks and review-event binding not
applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-028-F2 | 7–10 | B minute 2023-06-07, item 5 | act-record | 2023-06-07 · unknown |

## What remains unknown

- **The accountable owner and the context** of the Dunmore commitment.
- **Whether the asset survey reported, and what followed.** Not in the material.
- **What became of the Hollins pump replacement after June 2023.** See below: the July minute's silence
  settles nothing.

## What remains conflicting

Nothing.

## What is not a decision

Spans of `sources/CASE-028.md` (`sha256:e9841d0b0d4a4e5653db153c9fafb59f5a112fc0495dbb15894924af1f5c6b8e`).

| Fragment | Lines · offsets | Verbatim span | Classification | Reason |
|---|---|---|---|---|
| CASE-028-F1 | 5 · [90, 165) | "The Hollins pump replacement was deferred to the next meeting. No decision." | `{"taxonomy_version":"1.0.0","class":"non-decision","non_decision":"deferred"}` | **Evidence that no decision was made**: the question was put off with nothing committed in the meantime. |

The classification validated against `decision-contribution.schema.json`.

**No decision evidenced — item C.** "Capital board minute, 2023-07-05 — no mention of Hollins." This is
**silence**, a statement about the evidence, not about the organisation. It is not evidence that the
Hollins replacement was dropped, decided elsewhere or deferred again. It is not a `non-decision`, which
needs material that *says* no decision was made.

## Retrospective material set aside

None.

## Unclassified, and found and not used

Nothing unclassified. Item C was examined; it holds no span that contributes to anything (its whole
content is a description of an absence).

## Coverage

`sources/CASE-028.md`, items A, B, C: all examined. A classified (`non-decision: deferred`); B fragmented
and used in CASE-028-1; C examined, no decision evidenced.
