# CASE-018 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-018.md` (one
organisation's material, items A–C). Stages 1–5 run, then stop. One historical candidate, standing
`none`. No review event produced.

## Candidates

### CASE-018-1 — retire the paper ticket stock at all staffed stations

File `CASE-018-1.hdc.json` · `event_time_ref: unknown`

**As evidenced:** "The board agreed to retire the paper ticket stock at all staffed stations from 1
September, as recommended in paper 21/14. Owner: Hana Brightwell, Director of Retail." (item A, the
board minute, quoted).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | partial: one contribution (paper 21/14, `considered: evidenced` by the minute's citation), grade indeterminate | explicit (C4) |
| decision-date | missing | — |
| accountable-owner | supported (Hana Brightwell, Director of Retail) | explicit (C2) |

What the evidence did not supply: when the board decided.

**Contemporaneity, recomputed** (`historical-recovery.md`, literal reading): C4 `indeterminate`, because
the event time is unknown. Not presentable as contemporaneous context.

**Admissibility** (`admission.md`): 1 We decide (retire the stock) and This means (from 1 September,
at all staffed stations) both filled ✓ · 2 no `later` context; C4 indeterminate, reported in
`unresolved` ✓ · 3 every value traces to a located span ✓ · 4 `explicit-cross-reference` (paper 21/14)
and `entity-match` (paper stock) ✓ · 5 missing date reported, not filled ✓ · 6 proportionality stated
as undetermined (below) · 7 no conflicts present ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution exists; no tier chosen.

**Challenge** (shared, then decision-specific), most serious first:
1. Time basis (decision challenge 2). The minute's only date is in its filename
   (`board/2021-05-12-minute.md`); that is no basis, so the decision date is `unknown`. Upheld.
2. Retrospective as explanation (4). Item C, dated 2021-06-01, gives a reason (an unhedged exposure to a
   single printer) and a judgement ("the board was right to remove"). It is used only as corroboration.
3. Grouping attack. Item C's "remove" may refer to the printing contract, a different act from retiring
   the ticket stock. It contributes to no field, so the risk is contained; assembly confidence is
   `medium` for that reason.
4. Paper as decision (4). Paper 21/14 supports context only; its date (2021-04-28) is not the decision's.
5. Owner (5). The owner comes from the minute's own owner line, not from authorship or chairing. Upheld.
6. One decision (9): yes. Confidences differ across contributions (paper context epistemic `medium`). ✓

**Recommendation: incomplete** (decision date missing).

**Validation** (stage 5, recomputed): SCHEMA `historical-candidate.schema.json`, with `schemas/shared/`
loaded as a registry: pass. STRUCT: integrity rules 1–5; `event_time_ref` unknown or a `decision-date`
contribution; `considered` on every context contribution and no other; never-inferred roles carry
`explicit`; roles from the package or vocabulary; `source_hash` and locator reproduce every fragment's
content; no floats: all pass. Not run: TDR schema, recovered-TDR opening and rendered-value coverage
(no draft rendered, by instruction); review-event binding (no event exists).

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-018-F1 | 3–6 | A board minute | act-record | unknown · unknown |
| CASE-018-F2 | 8–10 | B paper 21/14 | cited-material | 2021-04-28 · 2021-04-28 |
| CASE-018-F3 | 12–15 | C risk paper | retrospective | 2021-06-01 · 2021-06-01 |

## What remains unknown

- **The decision date.** An attester would need the minute's dated heading or the meeting record. The
  `2021-05-12` in the filename is not evidence of it.
- **The year of "1 September".** It is the effective date, not the decision date, and is not completed.
- **The instrument the board acted under.** Only "the board" is named.
- **Alternatives** — none evidenced.

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding. No evidence that no decision was made.

## Retrospective material set aside

- **CASE-018-F3** (item C, risk paper, 2021-06-01). It corroborates that the board acted on paper stock.
  It was not allowed to supply the reason (an unhedged exposure to a single printer), the judgement that
  the board "was right", or any date.

## Unclassified, and found and not used

- Nothing unclassified.
- Found and not used: the dates inside the filenames of items A, B and C (no basis). Items B and C have
  stated dates, which were used; item A has none.

## Coverage

`sources/CASE-018.md` (sha256 in the candidate), items A, B, C: all examined, all fragmented, all used.
