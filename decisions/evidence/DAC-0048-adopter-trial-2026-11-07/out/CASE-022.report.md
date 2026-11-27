# CASE-022 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-022.md` (items A,
B–D, E). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-022-1 — replace the Hollins pumps

File `CASE-022-1.hdc.json` · `event_time_ref: CASE-022-C2` (2022-11-10)

**As evidenced:** "the committee approved the replacement, citing the paper." (item E, investment
committee minute 2022-11-10, case-file summary); the paper (item A) concerns "replacing the Hollins
pumps".

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1, from the minute and the paper it cites) |
| context | supported: the paper's £140k claim, cited and contemporaneous (C4) | explicit |
| decision-date | supported (2022-11-10, the minute's) | explicit (C2) |
| accountable-owner | missing | — |

Also `authority`: the investment committee (C3). What the evidence did not supply: who owned the
decision.

**Independence counts once.** C4 rests on the paper (F1) and on one fragment describing three emails
(F2) "each quoting the paper's £140k figure". F2 is annotated `restatement`, `restates: CASE-022-F1`.
**One source, not four.** C4 is `epistemic: low`: the paper states the figure plainly, with nothing
behind it, and the emails add nothing.

**Contemporaneity, recomputed** (literal, per fragment): F1 (capture 2022-11-03) `contemporaneous`; F2
(capture carried as `2022-11`) `indeterminate`, because November 2022 is not wholly before 2022-11-10.
The contribution's grade is the paper's, `contemporaneous`: I treat a restatement as its source when the
source is referenced too. That aggregation rule is mine, not the standard's (friction 3.2).
`considered: evidenced` (F3: "citing the paper").

**Admissibility:** 1 ✓ (choice: replace the pumps; consequence: approved) · 2 context contemporaneous ✓
· 3 ✓ · 4 `explicit-cross-reference` twice (minute cites the paper; emails quote it) ✓ · 5 owner
reported missing ✓ · 6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge:**
1. Corroboration by copying (decision challenge 8). The three emails restate the paper. They are counted
   once, and do not raise C4's epistemic confidence. Upheld.
2. Owner (5): the committee is a forum, not an owner. No owner is named. Not filled.
3. Paper as decision (4): the paper's date (2022-11-03) is not the decision's; the paper states a saving
   and does not decide. Upheld.
4. High extraction, low epistemic on C4. This is the case `uncertainty.md` names.
5. Summary provenance: item E is the case file's summary of the minute (epistemic `medium` on C1).

**Recommendation: incomplete** (owner missing).

**Validation:** SCHEMA pass; all STRUCT checks pass, including the `restates` → fragment-id
resolution (my convention, friction 5.5). TDR-draft checks and review-event binding not applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-022-F1 | 3–4 | A paper | cited-material | 2022-11-03 · 2022-11-03 |
| CASE-022-F2 | 6–7 | B, C, D emails | restatement (of F1) | 2022-11 · 2022-11 |
| CASE-022-F3 | 9–10 | E committee minute | act-record | 2022-11-10 · unknown |

## What remains unknown

- **The accountable owner.** An attester would need the full minute, or a record naming who held the
  replacement decision.
- **What lies behind the £140k figure.** The paper states it; nothing in the material supports it.
- **The emails' individual dates and senders** — given only as a range and "three different senders".
- **Alternatives and authority instrument** — none evidenced beyond "the committee".

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

None.

## Unclassified, and found and not used

Nothing unclassified. The emails are used only as restatements of the paper, counted once.

## Coverage

`sources/CASE-022.md`, items A, B–D (one description), E: all examined, fragmented and used.
