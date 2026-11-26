# CASE-027 — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over `sources/CASE-027.md` (item A,
five numbered entries). Stages 1–2 run. Stages 3–5 had nothing to act on: no decision was evidenced, so
nothing was drafted, challenged or validated. Then stop.

## Candidates

**None.** Zero candidates, with the evidence below. This says the material records no new decision. It
does not say the organisation decided nothing.

## What remains unknown

- **The board decision restated in entry 4.** "As agreed by the board in May, paper tickets go in
  September." restates a board decision whose act-record is not in this material. An attester who wanted
  that decision recovered would need the board's minute. The year of "May" is not known: the notes'
  date (2021-07-01) is in their filename only, which is no basis.
- **When the notes were taken** — unknown, for the same reason.

## What remains conflicting

Nothing.

## What is not a decision

Each finding is a span of `sources/CASE-027.md` (`sha256:c638950be1776c0b2aea1b0e8379628a02dbc62176f35171dd1136af03689252`;
locator char-offset `[start, end)`, observed 2026-11-07 by `adopter-trial` v1), classified against
`decision-contribution.schema.json` v1.0.0. Every classification object below validated against that
schema.

| Fragment | Lines · offsets | Verbatim span | Classification | Reason |
|---|---|---|---|---|
| CASE-027-F1 | 5 · [101, 149) | "1. Barrier upgrades at Fenwick are 80% complete." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"status-update"}` | Reports that work happened; commits nothing. |
| CASE-027-F2 | 6 · [152, 199) | "2. Sam to circulate the revised rota by Friday." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"action"}` | A task, not a judgement. |
| CASE-027-F3 | 7 · [202, 259) | "3. Most of us would rather keep the old timetable layout." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"preference"}` | An opinion attached to no commitment of money or time and no foreclosed option. |
| CASE-027-F4 | 8 · [262, 326) | "4. As agreed by the board in May, paper tickets go in September." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"restatement"}` | An already-taken decision repeated in a new setting. Creates no new decision. |
| CASE-027-F5 | 9 · [329, 392) | "5. Fares rise 3.1% in January, per the regulated fares formula." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"operational-routine"}` | Fully determined by an existing formula; the judgement was exercised when the formula was set. |

**Evidence that no decision was made:** none. The material does not record a deferral, a meeting that
ended without a decision, or a withdrawn proposal.

## Retrospective material set aside

None.

## Unclassified, and found and not used

- Nothing unclassified.
- Found and not used: entry 4 also *evidences* (as a restatement) that a board decision about paper
  tickets was taken. Its source is not in the material, so it seeds no candidate. The not-a-decision
  reason `restatement` and the evidence kind `restatement` are separate questions (friction 2.7).

## Coverage

`sources/CASE-027.md`: the heading (line 3) and all five entries (lines 5–9) examined. Every entry is
classified above. No span was left unexamined.
