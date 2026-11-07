# CASE-025 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-025.md` (items
A–B). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-025-1 — phased replacement at Hollins

File `CASE-025-1.hdc.json` · `event_time_ref: CASE-025-C2` (2024-02-06)

**As evidenced:** "**Chair:** I'm comfortable we go with the phased replacement at Hollins. **Dev
Anand:** I'll own the phasing — first pumps in May. **Chair:** Good. Done." (item A, transcript,
recording started 6 February 2024, 14:00).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | missing | — |
| decision-date | supported (2024-02-06, the capture's) | **inferred**: normalised from "6 February 2024" (C2) |
| accountable-owner | **partial**: Dev Anand, who owns "the phasing" | explicit (C3) |

What the evidence did not supply: context, and whether owning the phasing is owning the decision.

**Contemporaneity:** no context contribution to grade.

**Admissibility:** 1 ✓ (choice: phased replacement; consequence: first pumps in May, phasing owned) ·
2 none ✓ · 3 ✓ · 4 `ownership` (transcript "I'll own the phasing" ↔ email "Dev owns the Hollins
phasing") and the single transcript ✓ · 5 context reported missing ✓ · 6 undetermined · 7 none ✓.
**Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge**, most serious first:
1. Owner by default (decision challenge 5). The chair voices the choice and "speaks for most of it";
   that is not ownership, and the chair is not named. The owner is Dev Anand, on his own words in the
   act. Upheld, with the scope question open (C3 epistemic `medium`).
2. Preference or decision? "I'm comfortable we go with" alone would be a preference. It is followed by
   a commitment of time ("first pumps in May"), an owner, and closure ("Good. Done."). Treated as a
   decision; epistemic `medium` on C1.
3. Restatement (8). The email of 2024-02-20 restates the transcript's assignment and is counted once
   (`restates: CASE-025-F2`). Its "per the board" is the only naming of a forum outside the path, and
   it comes from later material; no authority is contributed.
4. Evidence kind. The transcript is recorded as `act-record`, not `later-recording`, because its
   creation time is not stated (friction 3.5). The grade is unaffected.

**Recommendation: incomplete** (context missing; owner partial).

**Validation:** SCHEMA pass; all STRUCT checks pass. TDR-draft checks and review-event binding not
applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-025-F1 | 3–4 | A transcript, metadata | act-record | 2024-02-06 · unknown |
| CASE-025-F2 | 6–8 | A transcript, exchange | act-record | 2024-02-06 · unknown |
| CASE-025-F3 | 10 | B email | restatement (of F2) | 2024-02-20 · 2024-02-20 |

## What remains unknown

- **Context** — what was known at the capital board on 6 February 2024.
- **Whether Dev Anand owns the decision, or only its phasing.** An attester would need the board's
  record of who holds the replacement decision.
- **The forum's authority.** The forum is named only in the path and in a later email.
- **The year of "May"; alternatives** (none evidenced, including any non-phased option).

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

The email (item B) is later than the event; it is treated as a restatement of the transcript and
counted once. It was not allowed to supply the forum ("per the board") as authority.

## Unclassified, and found and not used

Nothing unclassified. Found and not used: the date and forum in item A's path.

## Coverage

`sources/CASE-025.md`, items A and B: both examined, fragmented and used.
