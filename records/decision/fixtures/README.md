# Decision fixtures

Known-answer conformance fixtures for the decision language. Every fixture is fictional and carries a
must-not section ([TDR-0025](../../../decisions/TDR-0025-conformance-architecture.md)).

| Directory | What it tests | Fixtures |
|---|---|---|
| — | a decision complete in one source | FIX-004 |
| [`contemporaneity/`](contemporaneity/) | context is what was known at the time, computed from the times | FIX-018 (written after) · FIX-019 (no decision date) · FIX-020 (the memo nobody cited) · FIX-029 (a date from the folder) · FIX-030 (a shared date is not an order) |
| [`admissibility/`](admissibility/) | what each kind of material can support | FIX-021 (captured then, written up later) · FIX-022 (three emails, one paper) · FIX-023 (assemble a date across spans, never infer an owner) |
| [`corroboration/`](corroboration/) | later material evidences that a decision occurred, and nothing else | FIX-024 |
| [`transcript/`](transcript/) | an owner named in speech; prominence is not ownership | FIX-025 |
| [`incomplete/`](incomplete/) | the attester is never the owner; missing is the finding | FIX-026 |
| [`no-decision/`](no-decision/) | the five reasons by identifier; silence and deferral are different findings | FIX-027 · FIX-028 |

The recovery fixtures (FIX-018 onwards) are **proposed under
[TDR-0048](../../../decisions/TDR-0048-historical-recovery-doctrine.md) and
[TDR-0049](../../../decisions/TDR-0049-decision-recovery-vocabulary.md)**. The contract the
retrospective candidate itself must meet is tested in [`tests/recovery/`](../../../tests/recovery/).
