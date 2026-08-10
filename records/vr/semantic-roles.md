# Value Record — semantic roles

Roles a [`RecordContribution`](../../shared/record-contribution.md) may target when
`target_object: ovc`. Field definitions live in [`spec-value-record.md`](../../spec-value-record.md) §4;
this file says only what interpretation may contribute to, and **at which moment**.

## Commitment moment

What makes the commitment governable. These are what material contributes to when a commitment is being
made.

| `semantic_role` | Maps to | Mandatory for a candidate |
|---|---|---|
| `value-thesis` | Body — Value thesis | **Yes** |
| `falsifying-signal` | Body — Value thesis | **Yes** — a thesis without one is a hope, not a claim |
| `baseline` | Body — Baseline | **Yes** — no baseline, no claim |
| `beneficiary` | Body — Value thesis | **Yes** |
| `value-kind` | `value_kind` | **Yes** |
| `expected-value` | Body — Expected value | **Yes** |
| `recognition-route` | Body — Expected value and recognition route | **Yes** |
| `due-point` | `reconcile_by` | **Yes** |
| `finance-countersignatory` | `finance_countersignatory` | **Yes** |
| `linked-decision` | `linked_decisions` | **Yes** — a value claim floating free of any decision is a forecast, not a record |
| `review-boundary` | Body — Value thesis | No |
| `optimism-adjustment` | Body — Optimism adjustment | No |
| `procurement-stage` | `procurement_stage` | No |
| `authority-provenance` | Body — Evidence | No |
| `stewardship` | Body — Evidence | No |

The commitment moment maps onto the OVC grammar. Where material is written in that shape, the mapping
is direct:

| Grammar | Role |
|---|---|
| **Given** | `baseline` |
| **We commit** | `value-thesis`, `expected-value` |
| **For** | `beneficiary` |
| **By** | `due-point` |
| **Settled by** | `recognition-route` |
| **Unless** | `review-boundary` |

Authority provenance is borne outside the sentence, as `authority-provenance` and `stewardship`.

## Reconciliation moment

Relevant only once outcomes are observed. **None of these is ever mandatory for a commitment
candidate**, and requiring them at commitment time is a design error — it asks an organisation to
supply attribution reasoning before there is anything to attribute.

| `semantic_role` | Maps to | Notes |
|---|---|---|
| `observed-outcome` | Body — Realised entries | Dated observation against the baseline |
| `attribution-basis` | Body — Reconciliation | What supports attributing the outcome to the intervention |
| `counterfactual` | Body — Reconciliation | What would plausibly have happened otherwise |
| `competing-cause` | Body — Reconciliation | A material alternative explanation. Repeatable |
| `settlement-judgement` | Body — Reconciliation or write-off | Signed by the finance counter-signatory |

## Measurement is not attribution

`observed-outcome` records that a number moved. `attribution-basis` records why this commitment is
believed to have moved it. **A contribution to the first is never a contribution to the second.**

This is the distinction interpretation most often destroys, because source material destroys it
routinely — a benefits tracker showing a cost line falling next to a project name is evidence of the
first and none of the second. Where attribution is unevidenced, the honest settlement is **outcome
observed, attribution unresolved**, and that is a legitimate state rather than an incomplete one.

## Roles that do not exist, and must not be invented

- **`status`** — a candidate is `proposed`. Evidence that a business case was "approved" contributes to
  `linked-decision` or `value-thesis`, never to status.
- **`realised-value` as a commitment role** — a claim about value realised is an `observed-outcome`, and
  it belongs to the reconciliation moment however early it appears in the material.

## Notes

**`finance-countersignatory` must be a named individual in finance** — not a committee, not a role, not
"Finance". Material almost never supplies one, so this is usually a reported gap, and it is the gap that
most often explains why a benefit was never reconciled.

**`baseline` must carry its measurement date and source.** A baseline contribution without them is
inadmissible, because a benefit measured against nothing can never be reconciled against anything.

**`beneficiary` is mandatory here** while the current specification does not carry it as a distinct
field. This package names the role because interpretation must be able to capture it; the specification
change that gives it a home is the VR v2 work.
