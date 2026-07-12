---
id: TDR-0008
title: Add the Value Record as the TDR's sibling record
status: accepted
template: minimal
decision_date: 2026-07-12
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0002
confirmed_by_outcome: pending — review 2026-10-05, alongside TDR-0003
---

# TDR-0008 — Add the Value Record as the TDR's sibling record

## Context — what was known at the time

TDRs preserve the judgement behind decisions, but the quantified benefit claims that justify those decisions still evaporate: claimed in a business case, persuasive in the meeting, never baselined, never reconciled. The accountability semantics of TDR-0002 stop at the decision; the value case attached to it had no record with the same discipline — no named owner, no lineage, no honesty field. Adopters applying the TDR to transformation portfolios were asking where the benefit claim lives.

## Decision

Add the **Value Record (VR)** as the TDR's sibling record: the TDR records the decision; the VR records the value case and its life. Shipped as a sibling specification ([`spec-value-record.md`](../spec-value-record.md)), a template, a practice skill, and a worked example. A VR cannot exist without a linked TDR. The core disciplines: no baseline, no claim; a named finance counter-signatory who co-signs the claim, material state changes and any write-off; a mandatory reconcile-by date; a declared optimism adjustment; and write-off as a signed state. The standard stays tool-neutral: no benefits software, no finance-system bindings.

## Alternatives rejected

1. **Fold value fields into the TDR** — bloats every record for a claim most decisions do not make, and merges two lifecycles that end differently; one question per record.
2. **Leave benefit tracking to PMO and benefits-realisation tooling** — repeats the fragments-in-a-shared-drive failure the TDR exists to fix, one layer up.
3. **Do nothing** — leaves the standard recording judgement while the numbers that justified the judgement stay unaccountable.

## Options foreclosed

The standard now defines two record types and must maintain both, or supersede this record. The `VR-nnnn` id namespace and the five-state value lifecycle are claimed; a future redesign of either is a superseding decision, not an edit.

## Review

Confidence is medium: the field set is expected to be tested by adopters with live benefit registers. Revisable at tolerable cost — the VR documents can be removed and this record superseded; nothing in the TDR spec, schema or templates depends on them. Reviewed 2026-10-05 alongside TDR-0003, whose value case is itself recorded as the worked example VR-0001.
