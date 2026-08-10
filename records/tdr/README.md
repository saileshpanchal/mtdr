# Package — TDR

**Object:** `consequential-decision` — the unit of judgement
**Record type:** `TDR` — Transformation Decision Record

| Canonical artefact | Location |
|---|---|
| Specification | [`spec.md`](../../spec.md) |
| Schema | [`schema/tdr.schema.json`](../../schema/tdr.schema.json) |
| Templates | [`templates/tdr-full.md`](../../templates/tdr-full.md) · [`tdr-minimal.md`](../../templates/tdr-minimal.md) · [`tdr-bare.md`](../../templates/tdr-bare.md) |
| Worked examples | [`examples/`](../../examples/) |

This package is an overlay for interpretation. It does not restate the specification, and where the two
appear to differ, **the specification governs**.

| File | Purpose |
|---|---|
| [`semantic-roles.md`](semantic-roles.md) | Roles a contribution may target |
| [`admission.md`](admission.md) | Record-specific admissibility test |

## Skills

| Skill | Role |
|---|---|
| [`identify-record-contributions`](../../skills/identify-record-contributions/) | Finds contributions in supplied material |
| [`reconcile-record-fragments`](../../skills/reconcile-record-fragments/) | Groups them into candidates |
| [`draft-tdr`](../../skills/draft-tdr/) | Assembles a candidate into a conformant record |
| [`challenge-record`](../../skills/challenge-record/) | Challenges the candidate before ratification |
| [`validate-record`](../../skills/validate-record/) | Checks conformance |

The human authoring path — [`decision-identification`](../../skills/decision-identification/),
[`problem-framing-and-decision-capture`](../../skills/problem-framing-and-decision-capture/),
[`evidence-review`](../../skills/evidence-review/),
[`governance-review`](../../skills/governance-review/) — targets the **same specification**. There is
no interpreted variant of a TDR and an authored variant. One record, two routes to it.

## The proportionality rule applies to candidates

`spec.md` §3 routes a decision to full, minimal or bare by reversal cost, and `decision-identification`
adds the outcome that matters most — **no record at all**. Interpretation does not suspend this. A
candidate assembled from material describing something cheap to reverse should be proposed at the bare
tier, or reported as not warranting a record.

**A skill that produces a full-template candidate for every decision it finds has misread the standard
as an instruction to maximise records.**
