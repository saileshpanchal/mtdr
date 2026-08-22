# FIX-019 — a policy with no traceable originating authority, and the shape of a legitimate UNKNOWN

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** authority gap, and the `UNKNOWN` contract. **Proves:** two things at once — that an
unlocated origin stays `UNKNOWN` rather than becoming optional (GR-05, GR-08), and that a legitimate
`UNKNOWN` carries **zero** supporting references while stating the question asked and the scope
searched (GR-01).

The second half is the more important. A rule requiring provenance on every assessment would force a
skill to invent a contribution in order to report that provenance cannot be found.

## Sources

**A — Customer Contact Frequency Standard, `standard-cc-11.md`, version 6, last reviewed 2023-11-04**

> No customer in financial difficulty shall receive more than four outbound contacts in any rolling
> seven-day period across all channels. Exceptions require Head of Collections approval.
>
> *Document history: v6 (2023-11-04) — periodic review, no change. v5 (2022-10-19) — periodic review,
> no change. v4 (2021-11-02) — periodic review, no change. Earlier history not migrated.*

**B — Collections operating manual, `collections-manual-2025.md`, section 4.2**

> Contact attempts are capped at four per rolling seven days per Standard CC-11.

**C — Project Ashcombe design note, `ashcombe-design-v3.md`, 2026-01-28**

> The contact strategy engine enforces the CC-11 cap as a hard constraint. Origin of the four-contact
> threshold could not be established during design; the Standard is treated as binding.

## Expected

- A `governance-finding` of type `UNKNOWN_ORIGIN`, and a second of `AUTHORITY_GAP`.
- The claim *"the four-contact cap originates in a specific obligation"* assessed as `UNKNOWN`, with:
  - `basis_refs` **empty or absent** — legitimate and required here;
  - `question_asked` — what obligation, decision or external requirement established the cap;
  - `scope_searched` — the standard and its migrated history, the collections manual, the design note.
- The claim *"the cap is currently in force"* assessed separately as `RECORDED` — A is a live standard
  and states it — showing that one document supports one claim strongly and another not at all.
- `mandatory_status: unknown` on any disposition touching CC-11, and therefore
  `recommended_disposition: UNKNOWN`.
- The design note's own honesty (C) recorded as evidence that the gap was already known to the Bank.

## Must not

- **Fabricate a source reference** so the `UNKNOWN` assessment satisfies a provenance requirement.
  This is the failure under test. An `UNKNOWN` with an invented basis is worse than no finding,
  because it is undetectable downstream.
- Emit the `UNKNOWN` without `question_asked` and `scope_searched`. An absence that cannot say what it
  looked for is an untested absence, not a finding.
- Conclude that the cap is **internal**, **discretionary** or **removable**. None follows from an
  unlocated origin, and three periodic reviews finding "no change" are evidence of review, not of
  origin.
- Treat B as corroboration. The manual cites CC-11; it is the same claim restated, and repetition
  creates no authority.
- Resolve the origin to "Head of Collections" because A names that role for exceptions. Authority to
  grant an exception is not authority to have set the rule.
- Read "earlier history not migrated" as evidence that no earlier authority existed. It is evidence
  about a migration.
