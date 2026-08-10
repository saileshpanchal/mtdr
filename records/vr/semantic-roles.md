# Value Record — semantic roles

Roles a [`RecordContribution`](../../shared/record-contribution.md) may target when
`target_object: ovc`. Field definitions live in [`spec-value-record.md`](../../spec-value-record.md) §4;
this file says only what interpretation may contribute to, and **at which moment**.

## The eight roles

A commitment is identified when these eight can be inferred. They are **roles, not a required sentence
grammar** — no source is expected to phrase itself this way, and real material almost never does. The
skill's job is to recognise the role a span is playing, not to find the words.

| Role | Question | `semantic_role` | Field |
|---|---|---|---|
| **Under** | Under what authority is the organisation bound? | `authority` | `authority` |
| **Who commits** | Who commits the organisation? | `committed-by` | `committed_by` |
| **For whom** | Whose outcome is pursued or preserved? | `beneficiary` | `beneficiary` |
| **We commit** | What is pursued or preserved? | `commitment` | `title`, body §1 |
| **From** | What is the measured starting condition? | `baseline` | body §2 |
| **To** | What is the intended outcome? | `intended-outcome` | body §3 |
| **By** | By what point? | `due-point` | `reconcile_by` |
| **We will know** | How will we know — including that it is *not* arriving? | `recognition-route`, `falsifying-signal` | body §3 |

## Commitment moment

All eight roles above belong here, plus:

| `semantic_role` | Mandatory | Notes |
|---|---|---|
| `value-kind` | **Yes** | `cost` · `revenue` · `risk-reduction` · `capacity` |
| `linked-decision` | **Yes** | A value claim floating free of any decision is a forecast |
| `finance-countersignatory` | **Yes** | A named individual in finance |
| `review-boundary` | No | Conditions triggering review before the due point. **Not one of the eight** |
| `optimism-adjustment` | No | |
| `procurement-stage` | No | |

Every role in the table of eight is mandatory except that `recognition-route` and
`falsifying-signal` jointly discharge *We will know* — both are required, because a way of knowing the
value arrived is not a way of knowing it did not.

## Beneficiary is identity-bearing

`beneficiary` is **not descriptive metadata**. Two commitments identical in value, baseline, measure,
timing and wording, differing only in who the outcome is for, are **two commitments**.

[`conformance/FIX-003`](../../conformance/FIX-003-two-commitments-not-one.md) is the demonstration: the
beneficiary clause is the only signal separating two workstream benefits written to the same template by
the same author in the same document. Any grouping driven by similarity merges them and produces a
coherent, fully evidenced record of a commitment that does not exist.

So `beneficiary` is load-bearing for [`identity-and-grouping`](../../shared/identity-and-grouping.md),
not merely for completeness. **Group after reading the beneficiary, never before.**

## Reconciliation moment

Relevant only once outcomes are observed. **None is ever mandatory for a commitment candidate.**
Requiring them at commitment time asks an organisation for attribution reasoning before there is
anything to attribute.

| `semantic_role` | Notes |
|---|---|
| `observed-outcome` | Dated observation against the baseline |
| `attribution-basis` | What supports attributing the outcome to *this* commitment |
| `counterfactual` | What would plausibly have happened otherwise. **Optional — see below** |
| `competing-cause` | A material alternative explanation. Repeatable |
| `settlement-judgement` | Co-signed by the finance counter-signatory |

## Measurement is not attribution

`observed-outcome` records that a number moved. `attribution-basis` records why this commitment is
believed to have moved it. **A contribution to the first is never a contribution to the second.**

Source material destroys this distinction routinely — a benefits tracker showing a cost line falling
next to a project name is evidence of the first and none of the second. Where attribution is
unevidenced, the honest settlement is `realisation: attribution-unresolved`.

## The counterfactual is deliberately optional

A commitment is admissible without one. What its absence may prevent is a *defensible claim about
incremental value or attribution* — a different thing, and the distinction is preserved deliberately
(`spec-value-record.md` §5.2). Interpretation must not treat a missing counterfactual as a gap to
report against the commitment, and must not infer one.

## Roles that do not exist, and must not be invented

- **`status`** and **`realisation`** — a candidate is `status: candidate`, `realisation: not-started`.
  Evidence that a business case was "approved" contributes to `linked-decision` or `commitment`, never
  to either state field.
- **`realised-value` as a commitment role** — a claim about value realised is an `observed-outcome`,
  and belongs to the reconciliation moment however early it appears in the material.

## Notes

**`committed_by` and `finance_countersignatory` must both be named individuals**, and they are usually
different people. Material almost never supplies the counter-signatory, so it is the most commonly
reported gap — and it is frequently the reason a benefit was never reconciled.

**`baseline` must carry its measurement date and source.** A baseline contribution without them is
inadmissible: a benefit measured against nothing can never be settled against anything.

**`authority` must be traceable to something** — a mandate, a delegation, a board approval, a governing
decision. "Agreed at the programme board" is a start; the board and the date make it a contribution.
