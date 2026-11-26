# CASE-029 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-029.md` (items
A–B). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-029-1 — the single repairs line

File `CASE-029-1.hdc.json` · `event_time_ref: CASE-029-C2` (2019-03-14)

**As evidenced:** "Board minute, 2019-03-14 — the single repairs line agreed." (item B, case-file
summary).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | **partial**: one contribution, the undated working note, indeterminate, `considered: unknown` | explicit (C3) |
| decision-date | supported (2019-03-14) | explicit (C2) |
| accountable-owner | missing | — |

What the evidence did not supply: an owner, and any context that can be shown to have existed at the
time.

**Contemporaneity, recomputed:** C3 `indeterminate`. The note's capture and creation are both
`unknown`: there is no date in its text and none in its recorded metadata, and its folder
(`operations/2019-Q1/`) is no basis. So rule 4 cannot apply, and the grade is indeterminate.
`considered: unknown`: nothing shows the note was before the board, and nothing shows it pre-dated the
meeting.

**Admissibility:** 1 ✓ · 2 C3 indeterminate, **reported in `unresolved`, not presented as context** ✓ ·
3 ✓ · 4 `entity-match` ("One line for repairs" ↔ "the single repairs line") ✓ · 5 owner reported
missing ✓ · 6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge**, most serious first:
1. Backdating (decision challenge 2). The folder name `2019-Q1` would place the note in the quarter of
   the decision and make it look contemporaneous. A folder is no basis. Completing it to `2019` or
   `2019-03` would be date repair. The grade stays `indeterminate`.
2. Alternatives (7). "four offices" appears in the note, but the note is undated and unlinked; it cannot
   support an alternative. None contributed.
3. Evidence kind (friction 3.3). Recorded as `prior-unlinked` only because the enumeration has no kind
   for undated material; pre-dating is **not** established, and the grade does not depend on the label.
4. Authority (6). The minute's words are passive ("the single repairs line agreed"); no agreeing body is
   named in the span, so no authority is contributed. (Contrast CASE-020 and CASE-026, where "the board
   agreed".)

**Recommendation: incomplete** (owner missing; context partial).

**Validation:** SCHEMA pass; all STRUCT checks pass. TDR-draft checks and review-event binding not
applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-029-F1 | 3–6 | A working note | prior-unlinked (forced; see challenge 3) | unknown · unknown |
| CASE-029-F2 | 8 | B board minute | act-record | 2019-03-14 · unknown |

## What remains unknown

- **When the working note was written**, and whether anyone who decided saw it. An attester would need
  the file's real history or a citation of it.
- **The accountable owner.**
- **Who agreed** (the minute's words name no body) and under what authority.

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

None.

## Unclassified, and found and not used

Nothing unclassified. Found and not used: the folder name `operations/2019-Q1/` (no basis for any time).

## Coverage

`sources/CASE-029.md`, items A and B: both examined, fragmented and used.
