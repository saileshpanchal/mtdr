---
name: identify-value-contributions
description: Identify which spans of supplied organisational material contribute to reconstructing an Operational Value Commitment — a commitment to pursue or preserve an outcome — asking the value question of every fragment rather than looking for benefit tables. Use this skill on business cases, board packs, budget papers, OKR reviews or benefits trackers when someone asks "what did we actually commit to here?", "whose outcome was this?" or "is there a value commitment buried in this?", and before any value drafting runs. It applies the shared identification mechanics with the value language's roles, and it treats a commitment to protect existing value as fully a commitment — not only growth counts.
---

# Identify Value Contributions

The value language's specialisation of the identify stage. The **mechanics** — fragmenting before
interpreting, verbatim spans, two confidences graded separately, the hindsight rule, recovery-not-
failure-detection — are the shared skill's, [`identify-record-contributions`](../../../../skills/shared/identify-record-contributions/),
and are not repeated here. This skill adds what is value-specific.

## The one rule

**The question is "does this contribute to reconstructing an OVC?" — never "does this document
contain Value Record fields?"** A commitment's semantics are routinely spread across a business case,
a budget line, a steering pack and a later revision, none of which resembles a Value Record. The
record is the serialisation; the commitment is the thing being reconstructed.

## The roles

Defined in [`validation/semantic-roles.md`](../../validation/semantic-roles.md): the eight commitment
roles (*Under · Who commits · For whom · We commit · From · To · By · We will know*) plus value-kind,
counter-signatory and linked decision — **roles to be inferred, not a sentence grammar**. Material
almost never phrases itself this way; recognise the role a span plays, not the words.

## Value-specific recognitions

- **Pursuit and preservation are both commitments.** "Maintain complaint levels below 4% through the
  migration" is as much an OVC as "reduce cost-to-serve by £1.4m" — the outcome is protected rather
  than pursued, and material states protection commitments more quietly than growth ones.
- **Qualitative outcomes are commitments.** A committed outcome with a recognisable future condition
  and a way of knowing is an OVC whether or not a currency amount appears. Do not downgrade
  non-financial commitments to context.
- **Obligations generate commitments.** Where material shows the organisation undertaking an outcome
  *because a regulation or duty requires it*, the obligation is `authority`-relevant evidence and the
  undertaking is the commitment. The obligation itself is not the OVC — the organisation's response
  to it is.
- **The beneficiary clause is the identity signal.** Read it before anything else in the span's
  neighbourhood, because grouping happens downstream and beneficiary is what separates near-identical
  commitments.
- **A benefits-tracker figure is an `observed-outcome`**, however early it appears — reconciliation
  material, never commitment material.

## Outputs

`SourceFragment`s and `RecordContribution`s with `target_object: ovc`, per the shared contract. No
candidate, no record — reconciliation and drafting are later stages.

## Anti-patterns

- **Growth blindness** — finding every pursuit and no preservation.
- **Currency filter** — discarding qualitative commitments because no number is attached.
- **Benefit-table harvesting** — extracting a table's rows as commitments without evidence anyone
  committed to them. A row in a spreadsheet is a claim's shadow, not a commitment.
- **Obligation-as-commitment** — recording the regulation instead of the organisation's undertaking.

## Scope note

Mechanics, refusals and the recovery posture are the shared skill's. This skill adds the value
language's semantics only, per [TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md).
