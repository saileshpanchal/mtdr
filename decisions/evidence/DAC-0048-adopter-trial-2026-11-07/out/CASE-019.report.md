# CASE-019 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-019.md` (items
A–B). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-019-1 — retire the paper ticket stock at all staffed stations

File `CASE-019-1.hdc.json` · `event_time_ref: unknown`

**As evidenced:** "The board agreed to retire the paper ticket stock at all staffed stations, as
recommended in paper 21/14." (item A, a minute extract, stated as undated).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | partial: paper 21/14, `considered: evidenced` by the citation, grade indeterminate | explicit (C3) |
| decision-date | missing | — |
| accountable-owner | missing | — |

What the evidence did not supply: when the board decided, and who owned the decision.

**Contemporaneity, recomputed:** C3 `indeterminate` (event time unknown).

**Admissibility:** 1 ✓ (choice; binding consequence: the stock is retired at all staffed stations) ·
2 C3 indeterminate, reported ✓ · 3 ✓ · 4 `explicit-cross-reference` ("paper 21/14") ✓ · 5 date and
owner reported missing ✓ · 6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge:**
1. Time basis: the extract is stated to be undated, and its filename carries no date. `unknown` upheld.
2. Owner: none named; the board is a forum. Not filled. Not a finding against the candidate.
3. The paper's date (2021-04-28) is not the decision's. Upheld.
4. Extract: the minute is partial (epistemic `medium` on C1). Whether the full minute names an owner or a
   date is unknown.

**Recommendation: incomplete** (date and owner missing).

**Validation:** SCHEMA pass; STRUCT integrity rules 1–5, event-time pointer, `considered` coverage,
never-inferred roles, roles, provenance reproduction, no floats: all pass. TDR-draft checks and
review-event binding not applicable (no draft, no event).

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-019-F1 | 3–6 | A minute extract | act-record | unknown · unknown |
| CASE-019-F2 | 8–10 | B paper 21/14 | cited-material | 2021-04-28 · 2021-04-28 |

## What remains unknown

- **The decision date.** An attester would need the full minute or the meeting it records.
- **The accountable owner.** No individual is named. An attester would need the full minute or a record
  naming who held the decision.
- **Alternatives and authority instrument** — none evidenced beyond "the board".

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

None in the material.

## Unclassified, and found and not used

Nothing unclassified; nothing found and left unused.

## Coverage

`sources/CASE-019.md`, items A and B: both examined, fragmented and used.
