# CASE-024 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-024.md` (items
A–B). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-024-1 — retire the paper ticket stock at all staffed stations

File `CASE-024-1.hdc.json` · `event_time_ref: unknown`

**As evidenced:** "The board agreed to retire the paper ticket stock at all staffed stations from 1
September, as recommended in paper 21/14. Owner: Hana Brightwell, Director of Retail." (item A, board
minute, quoted).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | missing | — |
| decision-date | missing | — |
| accountable-owner | supported (Hana Brightwell, Director of Retail) | explicit (C2) |

Also `authority` the board (C3) and `corroboration` from the review (C4). What the evidence did not
supply: when the board decided, and what it knew.

**Contemporaneity:** no context contribution to grade.

**Admissibility:** 1 ✓ · 2 no context; nothing later admitted as context ✓ · 3 ✓ · 4 `entity-match`
(review "The board retired paper tickets" ↔ minute "retire the paper ticket stock") ✓ · 5 date and
context reported missing ✓ · 6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge**, most serious first:
1. Retrospective read as explanation (decision challenge 4). The review (item B, 2022-03) would supply a
   date ("May 2021"), a reason ("to reduce fraud at unstaffed barriers") and an alternative ("keeping a
   paper option for older passengers, rejecting it on cost"). The matrix allows a retrospective to
   support **only** that the decision occurred. All three are set aside; C4 corroborates occurrence and
   nothing else.
2. Date repair (2). The review's "May 2021" and the minute filename's `2021-05-12` agree, which is
   exactly how a date gets backfilled. Neither is a basis. The date stays `unknown`.
3. Paper 21/14 is cited but not in the material, so no context exists. Not reconstructed.

**Recommendation: incomplete** (date and context missing).

**Validation:** SCHEMA pass; all STRUCT checks pass. TDR-draft checks and review-event binding not
applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-024-F1 | 3–6 | A board minute | act-record | unknown · unknown |
| CASE-024-F2 | 8–11 | B post-implementation review | retrospective | 2022-03 · 2022-03 |

## What remains unknown

- **The decision date.** An attester would need the minute's dated heading or the meeting record.
- **Context.** Paper 21/14 is cited but not supplied; an attester would need it.
- **Alternatives.** None from contemporaneous material. The review's "paper option for older
  passengers" may be a lead for the attester; it is not evidence.
- **The year of "1 September".**

## What remains conflicting

Nothing among contributions. Within the set-aside review, its reason speaks of *unstaffed* barriers
while the minute concerns *staffed* stations. Not used, and not resolved here.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

- **CASE-024-F2** (item B, post-implementation review, dated 2022-03). It **corroborates** that the
  board retired paper tickets. It was **not allowed to explain**: the date ("May 2021"), the reason
  ("to reduce fraud at unstaffed barriers"), the alternative considered and rejected ("keeping a paper
  option for older passengers, rejecting it on cost").

## Unclassified, and found and not used

Nothing unclassified. Found and not used: the date in item A's filename (no basis).

## Coverage

`sources/CASE-024.md`, items A and B: both examined, fragmented and used (B for corroboration only).
