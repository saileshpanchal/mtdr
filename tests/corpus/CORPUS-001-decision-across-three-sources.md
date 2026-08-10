# CORPUS-001 — a decision assembled across three sources

> **Fictional corpus case.** Meridian Mutual, its people and its programme are invented.

**Category:** multi-document record. A consequential decision whose statement, context and owner sit
in three different artefacts, none of which looks like a decision paper.

## Sources

**A — Steering minutes, `platform-steering-2026-05-08.md`**

> Item 4. Following discussion of the options paper, the migration will proceed on the phased route.
> The big-bang option is not pursued.

**B — Options paper extract, `migration-options-v3.docx`, dated 2026-04-29**

> Option 1 (phased): eighteen months, dual-running costs of £700k, rollback possible at each phase
> gate. Option 2 (big-bang): nine months, no dual-running, rollback only by full restore. Both were
> assessed against the March risk appetite statement.

**C — Email, `re-steering-actions.eml`, dated 2026-05-09**

> Confirming yesterday's steering: Elena Marsh is the accountable owner for the migration decision
> and will take the paper to the risk committee for noting.

## Expected

- Contributions to **one** `consequential-decision`: A → `decision-statement`; B → `context`,
  `alternative-rejected` (Option 2, with its stated costs), `reversal-cost`; C → `accountable-owner`,
  `decision-date` (2026-05-08, evidenced by "yesterday's steering" — not the email's own date).
- **Exactly 1 CandidateAssembly**, grouping basis `explicit-cross-reference` (C names the steering;
  A follows "the options paper") — not "same programme".
- Proportionality: **minimal or full**, with reasoning citing the phase-gate rollback (B) — the
  material supports revisable-at-cost.
- `missing_semantics` includes `confidence`; nothing else mandatory is absent.

## Must not

- Treat the email's date as the decision date — C evidences the decision happened the day before.
- Record "the steering" as owner. Elena Marsh is evidenced; a forum is not an owner.
- Produce three candidates because there are three documents.
- Lose the rejected alternative's stated costs — they are the foreclosure evidence.
