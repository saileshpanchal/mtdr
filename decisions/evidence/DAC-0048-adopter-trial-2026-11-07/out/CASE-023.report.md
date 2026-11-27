# CASE-023 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-023.md` (items
A–B). Stages 1–5 run, then stop. One historical candidate, standing `none`. No review event produced.

## Candidates

### CASE-023-1 — chlorine dosing at Dunmore moves to the automated controller

File `CASE-023-1.hdc.json` · `event_time_ref: CASE-023-C2` (2019-03-14)

**As evidenced:** "Meeting of 14/3/19. Agreed: chlorine dosing at Dunmore moves to the automated
controller. The ops director to oversee." (item A, minute, quoted).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C1) |
| context | missing | — |
| decision-date | supported (2019-03-14) | **inferred**: normalised from "14/3/19" (day-month order; two-digit year read as 2019); extraction `medium` (C2) |
| accountable-owner | **missing** | — |

What the evidence did not supply: a named individual who held the decision, and any context.

**Contemporaneity:** no context contribution to grade.

**Admissibility:** 1 ✓ (choice: automated controller; consequence: dosing moves to it) · 2 none ✓ · 3 ✓
· 4 single act-record ✓ · 5 owner and context reported missing; **no owner filled from the organisation
chart** ✓ · 6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Proportionality:** undetermined. No `reversal-cost` contribution.

**Challenge:**
1. Owner reasoned into place (decision challenge 5). "The ops director to oversee" names a role and
   assigns oversight. Item B names P. Rahman as Operations Director. Joining them would (a) infer a
   never-inferred role, (b) treat oversight as ownership, and (c) rely on a chart whose year appears only
   in its filename (`people/2019-structure.md`), so it has no time basis. Rejected; the owner stays
   missing.
2. Time basis (2): the date comes from the minute's own text, not its filename. Upheld; normalisation
   recorded as `inferred`.
3. Authority (6): the forum is in the path only (`ops-forum/`). None contributed.

**Recommendation: incomplete** (owner and context missing).

**Validation:** SCHEMA pass; all STRUCT checks pass. TDR-draft checks and review-event binding not
applicable.

**Provenance**

| Fragment | Lines | Item | Evidence kind | Capture · creation |
|---|---|---|---|---|
| CASE-023-F1 | 3–6 | A minute | act-record | 2019-03-14 · unknown |

## What remains unknown

- **The accountable owner.** An attester would have to find who held the decision on 14 March 2019 — a
  named individual, evidenced as owner rather than overseer. The role "ops director" is a lead, not an
  answer.
- **Context, alternatives, authority** — none evidenced.

## What remains conflicting

Nothing.

## What is not a decision

No `not-a-decision` or `non-decision` finding.

## Retrospective material set aside

None.

## Unclassified, and found and not used

- Nothing unclassified.
- **Found and not used: item B**, `people/2019-structure.md`: "Operations Director: P. Rahman". It is not
  fragmented into the candidate: the only claim it could support is an owner, and that would be
  inference on a never-inferred role from a document with no time basis (its year is in the filename
  only).

## Coverage

`sources/CASE-023.md`, items A and B: both examined. A fragmented and used; B examined and set aside
for the reason above.
