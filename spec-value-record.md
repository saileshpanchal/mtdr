# Value Record (VR) — Specification

**Version:** 2.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

The **Value Record (VR)** is the sibling record to the Transformation Decision Record ([`spec.md`](spec.md)): the TDR records the decision; the VR records an **Operational Value Commitment** and its life. It is serialised the same way — YAML frontmatter for machine-readable fields, markdown body for human judgement — and it follows the same supersede-don't-edit rule.

---

## 1. Purpose

A VR answers the question that quantified benefit claims almost never survive to hear:

> **Did the value arrive — and can we say why?**

Decisions are routinely justified by a number: a saving, a revenue line, a risk reduced, capacity released. The number does its work in the meeting and is never seen again. Nobody measures the starting point, nobody is named as committing the organisation, nobody records whose outcome it was meant to be, and nobody is standing at the agreed date to reconcile claim against reality.

**The VR is the missing second half of a quantified benefit statement: the commitment and its settlement are one record.**

### 1.1 The commitment is an accountable pursuit, not a prediction

This is the specification's centre and everything else follows from it. A Value Record does **not** claim that an outcome will occur. It records that a named person committed the organisation to **pursuing or preserving** an outcome, for a named beneficiary, under a traceable authority, from a measured starting condition, by a stated point, with a stated way of knowing.

A commitment can be honoured and the outcome still not arrive. A commitment can be abandoned while the outcome arrives anyway for unrelated reasons. **Neither case makes the record wrong**, and a specification that cannot express them is measuring forecasting accuracy rather than accountability.

## 2. Relationship to the TDR

- A **TDR** may exist without a VR — many sound decisions make no quantified benefit claim.
- A **VR** cannot exist without a linked TDR. Value is committed *in support of a decision*; a value claim floating free of any decision is a forecast, not a record.
- The two lifecycles are independent: a decision may be confirmed by outcome while its value case is written off, and that combination is exactly the kind of organisational knowledge worth keeping.

## 3. When to raise a VR

**Any quantified benefit claim entering a decision gets a VR.** If a number is doing persuasive work in a TDR — in its Context, its Evidence, or its business case references — that number is a commitment in waiting, and it gets a record.

Proportionality applies here too: if the claim is too small to be worth settling, take it out of the decision rather than leave it unsettled. A decision record decorated with numbers nobody intends to check is worse than one with no numbers at all.

## 4. Record structure

A VR is a single markdown file. A template is provided at [`templates/vr.md`](templates/vr.md).

### 4.1 The eight semantic roles

A commitment is complete when eight roles can be identified. They are **roles to be inferred, not a mandatory sentence grammar** — no record is required to phrase itself this way, and material almost never does.

| Role | Question | Carried by |
|---|---|---|
| **Under** | Under what authority is the organisation bound? | `authority` |
| **Who commits** | Who commits the organisation? | `committed_by` |
| **For whom** | Whose outcome is being pursued or preserved? | `beneficiary` |
| **We commit** | What is being pursued or preserved? | `title` · body §1 |
| **From** | What is the measured starting condition? | body §2 |
| **To** | What is the intended outcome? | body §3 |
| **By** | By what point? | `reconcile_by` |
| **We will know** | How will we know — including how we would know it is *not* arriving? | body §3 |

### 4.2 Frontmatter fields

| Field | Required | Values / format |
|---|---|---|
| `id` | Yes | `VR-nnnn`, unique within the owning organisation or repository |
| `title` | Yes | Declarative statement of what is being pursued or preserved |
| `status` | Yes | `candidate` \| `ratified` \| `settled` \| `superseded` — the **epistemic** state |
| `realisation` | Yes | `not-started` \| `observing` \| `realised` \| `partially-realised` \| `not-realised` \| `attribution-unresolved` \| `written-off` — the **value** state |
| `linked_decisions` | Yes | `TDR-nnnn` (one or more) |
| `beneficiary` | Yes | **Whose outcome this is.** Identity-bearing — see §4.3 |
| `committed_by` | Yes | **A named individual** who commits the organisation — not a committee, not a role |
| `authority` | Yes | The authority under which the organisation is bound — a mandate, delegation, board approval or governing decision, traceable to something |
| `value_kind` | Yes | `cost` \| `revenue` \| `risk-reduction` \| `capacity` |
| `finance_countersignatory` | Yes | **A named individual in the finance function.** Co-signs at ratification, every material state change, and any write-off |
| `reconcile_by` | Yes | ISO 8601 (`YYYY-MM-DD`) |
| `procurement_stage` | Yes | `exploration` \| `pilot` \| `procurement` \| `build` \| `production` \| `retired` |
| `supersedes` | Yes | `VR-nnnn` (one or more) or `none` |
| `derived_from` | Yes | `VR-nnnn` (one or more) or `none` |

Validated by [`schema/vr.schema.json`](schema/vr.schema.json).

### 4.3 Beneficiary participates in commitment identity

`beneficiary` is **not descriptive metadata.** Two commitments identical in value, baseline, measure, timing and wording, differing only in who the outcome is for, are **two commitments** — and treating them as one produces a coherent, fully evidenced record of something that does not exist.

This is not a hypothetical. It is the failure demonstrated in [`conformance/FIX-003`](conformance/FIX-003-two-commitments-not-one.md), where the beneficiary clause is the *only* signal separating two workstream benefits written to the same template by the same author in the same document. Anything grouping on similarity merges them.

**A commitment whose beneficiary is unstated is not identifiable**, which is why the field is required rather than encouraged.

### 4.4 The two state axes are independent

`status` records **what is known about the record**. `realisation` records **what is known about the value**. Conflating them — as this specification did until v2.0.0 — makes it impossible to say the two most useful things a value record can say: that a commitment is properly ratified and its value has not arrived, or that an outcome has been observed and nobody can yet say the commitment caused it.

```
status:       candidate → ratified → settled
                                   → superseded
realisation:  not-started → observing → realised | partially-realised
                                      | not-realised | attribution-unresolved
                                      | written-off
```

- **candidate** — proposed but not ratified. Whether drafted by a person or assembled from evidence, a candidate has no organisational standing. It may lack a baseline or counter-signatory *only* in this state.
- **ratified** — an authorised organisational act has admitted it. Requires a measured baseline, a named `committed_by`, a named `finance_countersignatory`, a stated `beneficiary` and a `reconcile_by` date.
- **settled** — the commitment has reached its conclusion, whatever that was. `realisation` says which.
- **superseded** — replaced by a later record.

### 4.5 Body sections

1. **The commitment.** What is being pursued or preserved, for whom, by whom, under what authority. The *We commit · For whom · Who commits · Under* roles in prose.
2. **Baseline.** The measured starting condition, with its date and source. **No baseline, no claim.** A benefit measured against nothing can never be settled against anything.
3. **Intended outcome and recognition.** The target condition, where the value shows up, how it is recognised, and the **falsifying signal** that would show it is not arriving. "Recognised" means someone in finance can point at it. A thesis without a falsifying signal is a hope, not a commitment.
4. **Review boundary.** *Optional.* Conditions under which the commitment must be reviewed or challenged before its due point.
5. **Optimism adjustment.** *Optional.* A declared correction applied to the expected value, with its rationale. Business cases flatter; declaring the adjustment makes the optimism settleable instead of ambient.
6. **Observed outcomes.** Dated observations against the baseline, appended in place as they occur. **An observation is not an attribution** — see §5.
7. **Evidence.** The three kinds in §5, each labelled. References with locations that survive.
8. **Attribution and settlement.** Completed at or before `reconcile_by`, and co-signed by the finance counter-signatory.

## 5. Three kinds of evidence

A Value Record carries evidence of three distinct things, and **collapsing them is the most common failure in benefits practice**:

| Kind | Establishes | Without it |
|---|---|---|
| **Existence** | That the commitment was made — by whom, for whom, under what authority | There is no commitment, only a claim |
| **Observation** | That an outcome occurred — measured against the baseline | There is nothing to settle |
| **Attribution** | That *this commitment* is why | The outcome is real and unexplained |

**Measurement is not attribution.** A cost line falling next to a programme name is evidence of the second kind and none of the third. Evidence in §4.5's section 7 is labelled by kind so the distinction survives into the record.

### 5.1 Attribution unresolved is a legitimate settlement

Where an outcome is observed and attribution is not evidenced, the honest settlement is `realisation: attribution-unresolved`.

This is **not** an incomplete record. It is the accurate statement of what is known, and a standard unable to express it forces every observed movement to be either claimed or discarded — which is how benefits tracking becomes a record of confidence rather than of value.

### 5.2 The counterfactual question is deliberately open

**A commitment is admissible without an explicit counterfactual.** This specification does not require one.

What its absence may prevent is a *defensible claim about incremental value or attribution*. Those are different things, and the distinction is preserved deliberately rather than resolved by making counterfactual reasoning mandatory because it makes value calculation tidier.

Where a counterfactual and material competing causes are recorded, they belong to settlement — not to the definition of the commitment. **Requiring them at commitment time would ask an organisation for attribution reasoning before there is anything to attribute.**

This question is open, and a later version may settle it in either direction on evidence.

## 6. The stage taxonomy

`procurement_stage` locates the spend or change on a single ladder: **exploration → pilot → procurement → build → production → retired**. Each promotion is a decision in its own right, recorded as a superseding record stating what is now known that was not known at the previous stage. Expected value claimed at `exploration` and still uncorrected at `production` is a claim that has dodged four settlement opportunities.

## 7. Lineage and lifecycle rules

The VR follows the TDR's rules exactly (spec §§6–7):

- Records are **never edited or deleted once ratified**. They are **superseded**.
- **Status and realisation transitions, observed-outcome entries, counter-signatures and the closing settlement are made in place** — they are lifecycle facts, not changes of judgement.

### 7.1 Consequential change changes the commitment

A change to any of **beneficiary · intended outcome · timing · funding · protected value** is a change to *what the organisation committed to*, and requires a **superseding VR** — not an update to the existing one.

This is the distinction between changing a commitment and correcting its measurement. Revising a measurement method or a baseline source is an in-place lifecycle fact. Changing who the outcome is for, or what it is, produces a different commitment that happens to resemble the old one. **Recording that as an update destroys the evidence that the organisation changed its mind**, which is the one thing the record exists to preserve.

## 8. Versioning and v1 records

This specification versions independently of [`spec.md`](spec.md), which it tracked only until v1.3.0.

**v2.0.0 is a breaking change**: `beneficiary`, `committed_by`, `authority` and `realisation` are new required fields, and the `status` enum has changed. Records raised under v1 **remain valid v1 records** and are not retrospectively invalid — they are superseded by a v2 record when materially changed, per §7. The v1 status values map as follows.

| v1 `status` | v2 `status` | v2 `realisation` |
|---|---|---|
| `proposed` | `candidate` | `not-started` |
| `agreed` | `ratified` | `not-started` |
| `realising` | `ratified` | `observing` |
| `reconciled` | `settled` | `realised` \| `partially-realised` \| `not-realised` \| `attribution-unresolved` |
| `written-off` | `settled` | `written-off` |

A write-off remains **a signed state, not an abandonment.** Value that did not arrive is declared, not forgotten. It requires the counter-signatory's signature, states what was learned, and stays in the record set permanently. A written-off VR is the record working, not failing.

---

*The reasoning behind this record's addition is in [TDR-0008](decisions/TDR-0008-add-value-record-as-sibling-record.md); behind v2.0.0, in [TDR-0019](decisions/TDR-0019-value-record-v2-operational-value-commitment.md).*
