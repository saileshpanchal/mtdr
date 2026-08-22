# Worked run — the reference reconstruction

**Status:** proposed under [TDR-0034](../../../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md).
Not accepted, and carrying no standing.

One complete run of the [governance skills](../../../../records/decision/skills/governance/) over the
[fixture estate](../../../../records/decision/fixtures/governance/) — the Project Ashcombe decision at
the fictional Kingsmere Bank plc, approved 2026-02-11.

## This is a reference, not an expected output

A model-executed skill will not reproduce this prose, its ordering or its phrasing, and a probe
demanding that would test text generation rather than reconstruction. Compare against it
**semantically**, using AT-01's seven invariants.

Two layers, deliberately:

| Layer | Compared how |
|---|---|
| `*.json` — the projections | **Exactly.** Each validates against [`governance-projection.schema.json`](../../../../records/decision/schema/governance-projection.schema.json); `verify.py` check 10 enforces the schema, the claim-reference resolution and `carries_standing: false` |
| `*.md` — the reports | **Semantically.** Required findings present, prohibited findings absent, epistemic classifications matching, authority unresolved where it is unresolved |

## What a reviewer should be able to do with it

Take any recommendation in the reports and trace it back through the chain AT-10 requires —
recommendation, finding, source artefact, extracted claim, governing rule, epistemic assessment,
required authority gate — without leaving this directory and the fixtures it cites.

Where that chain stops at an authority nothing resolves to, that is not a defect in the run. It is the
authority irreducibility finding, and it is the most useful thing the estate produces.
