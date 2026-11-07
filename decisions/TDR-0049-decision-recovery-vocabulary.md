---
id: TDR-0049
conforms_to: mtdr/decision/tdr@1.15.0
title: Adopt the decision-recovery vocabulary — contribution classes, the canonical not-a-decision reasons, and the recovery pipeline
status: proposed
template: minimal
decision_date: 2026-11-07
accountable_owner: Sailesh Panchal
confidence: medium
maturity: proposed
supersedes: none
derived_from: TDR-0023, TDR-0026, TDR-0048
confirmed_by_outcome: pending — confirm when an implementation outside this repository loads the not-a-decision reasons and the recovery roles from the published vocabulary instead of restating them, and the recovery pipeline has run end to end over material its authors did not write; or 2027-05-07, whichever is sooner
---

# TDR-0049 — Adopt the decision-recovery vocabulary — contribution classes, the canonical not-a-decision reasons, and the recovery pipeline

> **Proposed. No standing.** Depends on [TDR-0048](TDR-0048-historical-recovery-doctrine.md), and is
> ratified only after it. Like it, nothing here reaches `main` while it is proposed.

## Context — what was known at the time

The value language recovers commitments through a contribution vocabulary and five lifecycle skills
under an orchestrator ([TDR-0026](TDR-0026-value-recovery-vocabulary.md)). The decision language had
the shared stages, its roles, its admission test and `draft-tdr`, and nothing that said what a fragment
of a minute or a paper could contribute to a decision before drafting. Its five reasons something is
not a decision lived in one skill's prose — and an implementation that needed them had restated them by
hand, so the skill had become the practical source of normative meaning. TDR-0048 states the recovery
doctrine; it leaves each language to state its own matrix and its own recovery roles.

## Decision

**Give the decision language the recovery layer the value language has, and put its vocabulary in the
specification, not in a skill.**

1. **Fifteen contribution classes**, in
   [`records/decision/specification/decision-contribution.md`](../records/decision/specification/decision-contribution.md),
   carried through the shared `RecordContribution` exactly as value's are. Four never populate a field:
   `challenge`, `corroboration`, `non-decision`, `not-a-decision`. The `unclassified` outcome, the
   `derivation` marker and the completeness view apply as TDR-0026 defined them.
2. **The five reasons something is not a decision become normative, with stable identifiers** —
   `status-update`, `action`, `preference`, `restatement`, `operational-routine` — defined in the
   specification and published in a versioned machine-readable form,
   [`decision-contribution.schema.json`](../records/decision/schema/decision-contribution.schema.json).
   `decision-identification` and every recovery skill cite it; a consumer loads it.
3. **No decision evidenced, and evidence that no decision was made, are different findings.** The
   second has kinds — `deferred`, `not-reached`, `withdrawn` — and a deferral that commits is a
   decision.
4. **The recovery roles are declared by the package:** `decision-date` the event role, `context` the
   context role, and `accountable-owner`, `alternative-rejected` and the `owner`, `authority` and
   `alternative` classes never inferred. The suite enforces them on every historical candidate for a
   consequential decision, from that declaration.
5. **The decision language's instance of TDR-0048's evidence matrix** — what each kind of material can
   support, claim by claim.
6. **Five skills**: `identify-decision-contributions`, `reconcile-decision-contributions`,
   `challenge-decision-record` and `validate-decision-record` specialising the shared stages, and
   `recover-decision-records` composing them with `draft-tdr` under TDR-0026's composition ruling.
   `draft-tdr` gains the completeness view and states when a draft was recovered. The standard's skill
   count moves from twenty-five to thirty.

## Alternatives rejected

1. **Leave the reasons in `decision-identification`.** Rejected: a skill's prose is not a contract, and
   the evidence is that consumers restate it rather than cite it.
2. **Use the shared stages directly, with no decision specialisations.** Rejected: the shared stages
   cannot name the decision language's roles, its matrix or its recovery roles without ceasing to be
   record-neutral.
3. **Put the classes in a new interchange schema.** Rejected for the same reason TDR-0026 rejected it:
   the classes ride on the existing `semantic_role`, and only the closed vocabulary itself is published
   as data.

## Options foreclosed

- No not-a-decision reason or contribution class is added, renamed or removed without a superseding
  record — and the machine-readable form's `taxonomy_version` moves with it.
- No recovery skill restates the vocabulary, the doctrine or a shared stage's mechanics.
- No recovery skill produces a review event or confers standing.

## Review

On the confirmation evidence, or 2027-05-07. A recurring `unclassified` pattern, or a consumer that
must map the reasons to its own spelling indefinitely, reopens it.
