# CASE-020 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-020.md` (items
A–C). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-020-1 — a single repairs line

File `CASE-020-1.hdc.json` · `event_time_ref: CASE-020-C2` (2019-03-14)

**As evidenced:** "the board agreed a single repairs line, as set out in paper B/19/07. Owner: R.
Okafor, Director of Operations." (item A, board minute 2019-03-14, given in the case file's summary
form).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | supported: paper B/19/07, cited, contemporaneous (C5); plus one circumstance, the memo, unlinked (C7) | explicit |
| decision-date | supported (2019-03-14, from the minute's heading) | explicit (C2) |
| accountable-owner | supported (R. Okafor, Director of Operations) | explicit (C3) |

Also: `alternative-rejected` four local offices (C6, explicit, from the cited paper as presented);
`authority` the board (C4). What the evidence did not supply: nothing among the mandatory roles; the
paper's and minute's full text (only summaries were supplied).

**Contemporaneity, recomputed:**

| Contribution | Capture | Event | Grade | `considered` |
|---|---|---|---|---|
| C5 paper B/19/07 | 2019-03-01 | 2019-03-14 | contemporaneous | evidenced (F1: "as set out in paper B/19/07") |
| C7 operations memo | 2019-02-20 | 2019-03-14 | contemporaneous | **unlinked** |

C7 pre-dates the decision, and nothing connects it to the board. It is circumstance, not what the board
knew.

**Admissibility:** 1 ✓ (choice: one line; consequence: repairs handled on a single line) · 2 both
context contributions contemporaneous; C7 rendered only as circumstance ✓ · 3 ✓ · 4
`explicit-cross-reference` (B/19/07) and `entity-match` (repairs calls) ✓ · 5 nothing missing ✓ · 6
undetermined · 7 none ✓. **Admissible.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge**, most serious first:
1. Alternative (decision challenge 7; never-inferred role). C6 "four local offices" rests on the paper's
   own words ("the cost of four local offices against one line") and the minute's citation of that
   paper; the board chose the single line. The matrix allows cited material to support alternatives "as
   presented to the decision". The span sustains "four local offices" as the option set against one
   line, so C6 stands, `explicit`, extraction `high`. Still open: whether four offices was the existing
   arrangement or a proposal. Either way it is the option not taken. Epistemic stays `medium`.
2. Pre-dating as consideration (3). C7 is `unlinked`; challenged and upheld as unlinked. It must not be
   rendered as what was known to whoever decided.
3. Grouping attack. The memo joins on subject matter only (repairs calls on one line); assembly
   confidence `medium`. A reader could keep it out of the candidate without changing any mandatory role.
4. Summary provenance. Items A and B are the case file's summaries, not the documents; epistemic
   `medium` on the decision, owner and context.
5. Owner (5): from the minute's owner line. Upheld.

**Recommendation: retain** (fit to put before a named individual; all four mandatory roles supported).

**Validation:** SCHEMA pass; all STRUCT checks pass (integrity 1–5, event-time pointer to a
`decision-date` contribution, `considered` coverage, never-inferred roles explicit, roles, provenance
reproduction, no floats). TDR-draft checks and review-event binding not applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-020-F1 | 3–4 | A board minute | act-record | 2019-03-14 · unknown |
| CASE-020-F2 | 6 | B paper B/19/07 | cited-material | 2019-03-01 · 2019-03-01 |
| CASE-020-F3 | 8–10 | C operations memo | prior-unlinked | 2019-02-20 · 2019-02-20 |

## What remains unknown

- **The originals of items A and B.** Only the case file's summaries were supplied; an attester should
  read the minute and the paper themselves.
- **Whether "four local offices" was the existing arrangement or a proposed option.**
- **Whether the memo was ever before the board.** Nothing shows it.
- **The authority instrument** — only "the board" is named.

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

None in the material.

## Unclassified, and found and not used

Nothing unclassified. The date in item C's filename was not needed: the item carries a stated date.

## Coverage

`sources/CASE-020.md`, items A, B, C: all examined, fragmented and used.
