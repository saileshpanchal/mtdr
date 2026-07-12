# Value Record (VR) — Specification

**Version:** 1.3.0 · **Licence:** MIT · **Author:** Sailesh Panchal

The **Value Record (VR)** is the sibling record to the Transformation Decision Record ([`spec.md`](spec.md)): the TDR records the decision; the VR records the value case and its life. It is serialised the same way — YAML frontmatter for machine-readable fields, markdown body for human judgement — and it follows the same supersede-don't-edit rule.

---

## 1. Purpose

A VR answers the question that quantified benefit claims almost never survive to hear:

> **Did the value arrive?**

Decisions are routinely justified by a number — a saving, a revenue line, a risk reduced, capacity released. The number does its work in the meeting and is never seen again. Nobody measures the starting point, nobody owns the claim, and nobody is standing at the agreed date to reconcile claim against reality. The organisation learns nothing from its own optimism.

**The VR is the missing second half of a quantified benefit statement: the claim and the reconciliation are one record.**

## 2. Relationship to the TDR

- A **TDR** may exist without a VR — many sound decisions make no quantified benefit claim.
- A **VR** cannot exist without a linked TDR. Value is claimed *in support of a decision*; a value claim floating free of any decision is a forecast, not a record.
- The two lifecycles are independent: a decision may be confirmed by outcome while its value case is written off, and that combination is exactly the kind of organisational knowledge worth keeping.

## 3. When to raise a VR

**Any quantified benefit claim entering a decision gets a VR.** If a number is doing persuasive work in a TDR — in its Context, its Evidence, or its business case references — that number is a claim, and the claim gets a record.

Proportionality applies here too: if the claim is too small to be worth reconciling, take it out of the decision rather than leave it unreconciled. A decision record decorated with numbers nobody intends to check is worse than one with no numbers at all.

## 4. Record structure

A VR is a single markdown file. A template is provided at [`templates/vr.md`](templates/vr.md).

### 4.1 Frontmatter fields

| Field | Required | Values / format |
|---|---|---|
| `id` | Yes | `VR-nnnn`, unique within the owning organisation or repository |
| `title` | Yes | Declarative statement of the value claim |
| `status` | Yes | `proposed` \| `agreed` \| `realising` \| `reconciled` \| `written-off` |
| `linked_decisions` | Yes | `TDR-nnnn` (one or more) — the decision(s) this value case depends on |
| `value_kind` | Yes | `cost` \| `revenue` \| `risk-reduction` \| `capacity` |
| `finance_countersignatory` | Yes | **A named individual in the finance function** — not a committee, not a role. The counter-signatory co-signs the claim, every material state change, and any write-off. |
| `reconcile_by` | Yes | ISO 8601 (`YYYY-MM-DD`) — the date by which the claim must be reconciled against reality |
| `procurement_stage` | Yes | `exploration` \| `pilot` \| `procurement` \| `build` \| `production` \| `retired` — which stage the spend or change sits at |
| `supersedes` | Yes | `VR-nnnn` (one or more) or `none` |
| `derived_from` | Yes | `VR-nnnn` (one or more) or `none` |

The JSON Schema at [`schema/tdr.schema.json`](schema/tdr.schema.json) validates TDR frontmatter only; a VR schema may follow in a later minor version.

### 4.2 Body sections

1. **Value thesis.** What value, of which kind, is claimed — and the **falsifying signal** that would show it is not arriving. A thesis without a falsifying signal is a hope, not a claim.
2. **Baseline.** The measured starting point, with its date and source. **No baseline, no claim.** A benefit measured against nothing can never be reconciled against anything.
3. **Expected value and recognition route.** Where the value shows up — a cost line, a revenue line, a risk reduction, released capacity — and how it is recognised: a budget line that moves, a price or volume change, a movement on the accepted-risk register, hours released and redeployed to named work. "Recognised" means someone in finance can point at it.
4. **Optimism adjustment.** A declared correction applied to the expected value, with its rationale. Business cases flatter; the adjustment states by how much this one is assumed to, and why. Declaring it makes the optimism reconcilable instead of ambient.
5. **Realised entries.** Dated observations against the baseline, appended as they occur.
6. **Evidence.** References with locations that survive — the same provenance discipline as the TDR's evidence review.
7. **Reconciliation or write-off.** Completed at (or before) `reconcile_by`: the claim reconciled against reality, or written off — signed by the finance counter-signatory.

## 5. Lifecycle and counter-signature

```
proposed → agreed → realising → reconciled
                              → written-off
```

- **proposed** — the claim is drafted. It may lack a baseline or counter-signatory *only* in this state.
- **agreed** — the claim is co-signed. A VR must not be marked `agreed` without a measured baseline, a named finance counter-signatory, and a `reconcile_by` date. The value-record skill refuses to do so.
- **realising** — the linked decision is in flight; realised entries accumulate.
- **reconciled** — at `reconcile_by`, the claim has been tested against the baseline and the outcome recorded, whatever it was.
- **written-off** — **a signed state, not an abandonment.** Value that did not arrive is declared, not forgotten. A write-off requires the counter-signatory's signature, states what was learned, and remains in the record set permanently. A written-off VR is the record working, not failing: the organisation now knows something about its own forecasting that it paid full price to learn.

The counter-signatory co-signs the claim at `agreed`, every material state change, and any write-off. A claim nobody in finance will put their name to is not a claim the organisation believes.

## 6. The stage taxonomy

`procurement_stage` locates the spend or change on a single ladder: **exploration → pilot → procurement → build → production → retired**. Each promotion up the ladder is a decision in its own right and is recorded as a superseding record, stating what is now known that was not known at the previous stage. Expected value claimed at `exploration` and still uncorrected at `production` is a claim that has dodged four reconciliation opportunities.

## 7. Lineage and lifecycle rules

The VR follows the TDR's rules exactly (spec §§6–7):

- Records are **never edited or deleted once agreed**. They are **superseded**.
- **Status transitions, realised entries, counter-signatures and the closing reconciliation or write-off are made in place** — they are lifecycle facts, not changes of judgement.
- **Changes to the value thesis, baseline, expected value or optimism adjustment require a superseding VR** stating what is now known that was not known at the time.

This is what makes a body of VRs organisational memory about value: the optimism trail survives its own corrections.

---

*This specification versions with [`spec.md`](spec.md). The reasoning behind its addition is recorded in [TDR-0008](decisions/TDR-0008-add-value-record-as-sibling-record.md).*
