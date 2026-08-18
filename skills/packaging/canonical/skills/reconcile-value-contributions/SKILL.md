---
name: reconcile-value-contributions
description: Group value contributions from different sources into candidate Operational Value Commitments, reading the beneficiary before grouping anything — because two commitments identical in figure, baseline and wording that differ in whose outcome they pursue are two commitments. Use this skill whenever value contributions come from more than one source, whenever someone asks "is this the same benefit as that one?" or "are we double-counting this saving?", and before draft-value-record runs. It applies the shared reconciliation mechanics with the value language's identity semantics, and it records tension between commitments as a finding rather than resolving it.
---

# Reconcile Value Contributions

The value language's specialisation of the reconcile stage. The **mechanics** — start from separate,
admissible grouping bases with named evidence, supersession versus conflict, missing semantics as a
claim, assembly confidence graded separately — are the shared skill's,
[`reconcile-record-fragments`](../../../../skills/shared/reconcile-record-fragments/), and are not
repeated here.

## The one rule

**Group after reading the beneficiary, never before.** `beneficiary` participates in commitment
identity ([`specification/vr.md`](../../specification/vr.md) §4.3): value commitments are where wrong
merges are most likely and most damaging, because two benefits in one programme describe themselves
in near-identical language — and the beneficiary clause is frequently the *only* separating signal.
[`fixtures/conflicting/FIX-003`](../../fixtures/conflicting/FIX-003-two-commitments-not-one.md) is the standing demonstration.

## The contract

**Input:** value contributions from one or many sources. **Output:** candidate groupings **with
reasons** — `CandidateAssembly` structures whose `grouping_basis` names its actual evidence — plus,
for every grouping question the evidence raises, one of the seven findings:

reinforcing contributions · contradictions · different beneficiaries · temporal evolution ·
supersession · unresolved ambiguity · competing value propositions.

"Best bank for Britain" · "help Britain prosper" · "support local businesses" · "grow SME lending"
may or may not be one proposition — the output says which reading the evidence supports, and where
it supports neither, the question goes to `unresolved` rather than being settled by fiat. **Never
resolve conflict merely to produce a cleaner record.**

## Value-specific judgements

- **Shared baselines are a warning, not a basis.** Two workstreams drawing on one measured starting
  position may be two commitments double-counting one saving, or two legitimate draws on one
  baseline. The evidence rarely settles it; `unresolved` carries the question to a human.
- **A revised figure under the same authority lineage is supersession** — the organisation changed
  its commitment, and both values are preserved with their ordering. A different figure with no
  shared lineage is a conflict or a different commitment; recency resolves nothing.
- **Commitments in tension are both real.** A cost-reduction commitment and a service-outcome
  commitment pulling against each other are two valid candidates whose tension is a *finding* —
  recorded in `unresolved` on each, never resolved by preferring one, never merged into a
  compromise commitment nobody made.
- **Protection commitments pair with pursuit commitments.** Material that commits to a pursuit
  "subject to" a protected threshold frequently yields two related candidates — the pursuit and the
  protection — linked by context, not merged.

## Outputs

`CandidateAssembly` structures with `target_object: ovc`, `status: candidate`, per the shared
contract — grouping bases named, gaps listed, tensions recorded.

## Anti-patterns

- **Merge by figure** — same £, same commitment. The figure is the weakest identity signal the
  material offers.
- **The compromise candidate** — averaging two commitments in tension into one nobody made.
- **Double-count denial** — silently splitting a shared baseline to make the sums work.
- **Protection absorbed into pursuit** — the threshold condition flattened into a footnote of the
  growth commitment, which is how protected value disappears from registers.

## Scope note

Mechanics and refusals are the shared skill's. This skill adds the value language's identity
semantics only, per [TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md).
