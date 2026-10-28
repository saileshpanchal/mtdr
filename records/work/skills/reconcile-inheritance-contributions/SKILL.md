---
name: reconcile-inheritance-contributions
description: EXPERIMENTAL, not part of the MTDR standard (TDR-0047) — group inheritance contributions from different sources into candidate Operational Inheritance Records by operational capability, never by the team, person or supplier that wrote the material. Use this skill whenever inheritance contributions come from more than one source, whenever someone asks "is this the same work as that?" or "did the reorganisation change what is inherited?", and before draft-inheritance-record runs. It applies the shared reconciliation mechanics with the work language's identity semantics, treats a change of participant as no change of state, and preserves conflicting sources rather than choosing between them.
---

# Reconcile Inheritance Contributions

> **Experimental** under [TDR-0047](../../../../decisions/TDR-0047-experimental-packages.md). Not part
> of the MTDR standard.

The work language's specialisation of the reconcile stage. The **mechanics** — separate admissible
grouping bases with named evidence, supersession versus conflict, missing semantics as a claim,
assembly confidence graded separately — are the shared skill's,
[`reconcile-record-fragments`](../../../../skills/shared/reconcile-record-fragments/), and are not
repeated here.

## The one rule

**Group by capability, never by participant.** Two hand-over notes from one team may describe two
capabilities; one capability may be described by three teams over five years. The author of the
material is the weakest identity signal it offers, and the most tempting.

## The contract

**Input:** inheritance contributions from one or many sources. **Output:** `CandidateAssembly`
structures with `target_object: operational-capability`, each `grouping_basis` naming its evidence —
plus, for every grouping question the evidence raises, one of the findings:

reinforcing contributions · contradictions · different capabilities · inherited state changed ·
participant changed only · unresolved ambiguity.

## Inheritance-specific judgements

- **A change of participant is not a change of state.** A reorganisation, a new supplier or an AI
  participant taking on the work produces the finding *participant changed only*, and no supersession.
  This is the judgement the lifecycle hypothesis turns on
  ([`fixtures/lifecycle/`](../../fixtures/lifecycle/)).
- **A change of inherited state is supersession.** A new control, a changed threshold, a retired
  dependency or a decision reshaping the work makes the later material a candidate successor, both
  states preserved with their ordering.
- **Same name, different capability.** Two teams both calling their work "exceptions" may be doing
  two jobs. Group on the jobs and the state around them, not on the label.
- **A team splitting does not split the capability** unless the jobs themselves diverged, by decision.
- **Conflicting authority references are both kept.** Two delegations naming different limits make
  the clause `conflicting`. Recency settles nothing; the instrument in force is a question for the
  authority's owner.

## Anti-patterns

- **Grouping by author** — one candidate per team that wrote material.
- **Reorganisation as supersession** — a new structure chart treated as new inherited state.
- **The merged threshold** — two conflicting limits averaged, or the later one silently preferred.

## Scope note

Mechanics and refusals are the shared skill's. This skill adds the work language's identity semantics
only, per [TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md).
