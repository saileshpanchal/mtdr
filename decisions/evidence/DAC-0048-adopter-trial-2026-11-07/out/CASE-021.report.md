# CASE-021 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-021.md` (item A).
Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-021-1 — remote overnight monitoring at the Dunmore treatment works

File `CASE-021-1.hdc.json` · `event_time_ref: CASE-021-C2` (2023-09-04)

**As evidenced:** "**Chair:** So we're agreed — the Dunmore treatment works go to remote monitoring
overnight from October. Lena, it's yours? **Lena Marsh:** Mine." (item A, meeting transcript).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | missing | — |
| decision-date | supported (2023-09-04, the capture's) | **inferred**: normalised from "Recording started 4 September 2023" (C2) |
| accountable-owner | supported (Lena Marsh) | explicit (C3) |

What the evidence did not supply: anything about what was known at the time.

**The four times.** The transcript was **captured** 2023-09-04 (its opening line) and **created**
2023-09-18 (stated file metadata, and also the filename's date). Evidence kind `later-recording`, so the
decision date is the capture's (the matrix: "✓ the capture's"), not the file's.

**Contemporaneity:** no context contribution to grade.

**Admissibility:** 1 ✓ (choice: remote monitoring overnight; consequence: from October, owned by Lena
Marsh) · 2 no context ✓ · 3 ✓ · 4 single artefact, basis recorded ✓ · 5 context reported missing ✓ ·
6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge:**
1. Capture vs creation (decision challenge 2). The date is the capture's, not the file's 2023-09-18.
   Upheld.
2. Owner (5): Lena Marsh accepts "Mine." in the act itself; she is not the chair, whose name is not
   given. Upheld.
3. Authority (6): the forum appears only in the path (`ops-forum/`), which is no basis. None
   contributed.
4. "from October" carries no year. Not completed.

**Recommendation: incomplete** (context missing).

**Validation:** SCHEMA pass; all STRUCT checks pass. Note that C2 is `inferred` (date normalisation is
permitted for `decision-date`, which is not a never-inferred role). TDR-draft checks and review-event
binding not applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-021-F1 | 3–4 | A transcript, metadata and opening | later-recording | 2023-09-04 · 2023-09-18 |
| CASE-021-F2 | 6–8 | A transcript, exchange | later-recording | 2023-09-04 · 2023-09-18 |

## What remains unknown

- **Context** — what was known when the forum agreed. An attester would need the meeting papers or the
  rest of the transcript.
- **The forum and its authority.** The forum is named only in the path.
- **The year of "October"** — not stated, and not completed.
- **Alternatives** — none evidenced.

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

None.

## Unclassified, and found and not used

Nothing unclassified. Found and not used: the filename's date `2023-09-18` (matches the stated creation
date; neither is the decision date).

## Coverage

`sources/CASE-021.md`, item A: examined in full, two fragments, both used.
