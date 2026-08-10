---
id: TDR-0018
title: Admit vendor-neutral interpretation skills; fix the standard's boundary at the artefact
status: accepted
template: full
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: medium
maturity: proposed
supersedes: none
derived_from: TDR-0001, TDR-0002, TDR-0003
confirmed_by_outcome: pending — review when interpretation skills have been run against real organisational material by someone other than the author, or 2027-02-10, whichever is sooner
---

# TDR-0018 — Admit vendor-neutral interpretation skills; fix the standard's boundary at the artefact

## Context — what was known at the time

TDR-0003 already ships skills alongside the specification, and they are already portable: `agents/copilot-studio.md` records a field deployment where "the skill files ran unmodified", and describes that runtime as "a worked example, not a dependency (any runtime that loads the open skill format works)". Skills in this repository are therefore an established part of the standard's surface, not a new category.

Those thirteen skills share one assumption: a human author who already knows the decision, sitting down to record it. The demand now arriving is different — organisations have decisions and value commitments already made, scattered across board packs, minutes, business cases, spreadsheets and correspondence, and want help recognising them.

That work has a property the existing skills do not have to handle. A single source may carry a complete record, but an interpreting skill must never *assume* it does. The semantics of one value commitment routinely sit across several documents written months apart: the proposition in one, the beneficiary in another, the baseline in a third, a revised target in a later meeting note. Reconstructing it means interpreting fragments, grouping them without treating proximity as identity, and reporting what is missing.

This raises a scope question the repository has not answered. `CONTRIBUTING.md` states:

> This repository defines a format and its practice. Implementations — tooling, graph substrates, extraction pipelines, integrations — belong in their own projects, whoever builds them.

Read at its widest, "extraction pipelines" excludes any skill that reads organisational material. Read at its narrowest, it excludes only the infrastructure around such a skill. The ambiguity is load-bearing: it decides whether the standard can describe how its own records are recognised, or whether every adopter must invent that privately and incompatibly.

## Decision

The MTDR repository may provide vendor-neutral skills that help humans or computational tools recognise, interpret, author, challenge, reconcile and validate records conforming to the standard. These skills produce or operate on portable record artefacts. They make no assumption about storage, runtime, graph representation, orchestration or subsequent use.

**The standard ends at the artefact boundary.** Its output is standards-conformant portable files. It has no knowledge of how those files are stored, indexed, connected, projected, reasoned over or used by any downstream system.

The distinguishing test is direction, not subject matter. A skill that reads material and yields a conformant artefact **produces the standard's own output** and belongs here. Indexing, retrieval, orchestration, model selection, graph assembly and persistence **consume** artefacts and remain outside, exactly as TDR-0002 and `CONTRIBUTING.md` require.

Structures that interpretation skills exchange between themselves — evidence fragments, interpreted contributions, candidate assemblies — are **portable skill interchange structures**, not organisational records. They carry no organisational authority, need not be persisted, and are not peers of the record schemas. They exist so independent skills can hand interpretation work to one another predictably.

One consequence is constitutional rather than technical: a skill may determine whether evidence supports an admissible candidate. It may never turn a candidate into organisational truth. **The skill proposes; the organisation ratifies.**

## Evidence

- **Business** — the standard's value rests on adoption, and the barrier is no longer format but recognition: organisations cannot record what they cannot find. A recognition method that is private to each adopter produces incompatible practice under a common format, which is the failure TDR-0001 exists to prevent.
- **Architecture** — the artefact boundary is testable in a way "no tooling" is not. Every deliverable either emits a conformant file or it does not. `ARCHITECTURE.md` already fixes the standard's end at the decision register and states that a conforming implementation "can stop at the register and be complete"; this decision applies the same shape to the skills.
- **Regulatory** — not material to the boundary itself. Material to the ratification rule: a record whose accountable owner was assigned by a tool rather than a person would not survive the "reasonable steps" test the standard exists to support, which is why proposal and ratification are separated here rather than left to implementers.
- **Operations** — one specification serves both authoring and interpretation. There is no machine version of a Value Record and a human version, so adopters maintain one set of semantics rather than two that drift.
- **Customer** — not material to this decision.
- **Data** — interpretation skills read an organisation's material and emit files that organisation owns outright, in its own repositories. Nothing about this decision moves data anywhere, because nothing in this repository moves data at all.
- **External** — no existing decision-record standard specifies how its records are recognised in prior material; the precedent is absent rather than contrary. The nearest analogue is the schema/parser split in data formats, where the format specifies what a conforming parser must produce without specifying the parser.

## Alternatives rejected

1. **Leave `CONTRIBUTING.md` ambiguous and add the skills anyway.** Rejected: the scope boundary is a published commitment, and quietly widening it in practice while the stated rule says otherwise is the corrosion this repository's own discipline exists to prevent. A boundary that moves without a record is not a boundary.
2. **Supersede TDR-0001 to admit extraction pipelines.** Rejected as far too wide, and unnecessary. It would effectively reverse the neutrality commitment to solve a problem that a clarification solves, and would invite exactly the software-binding proposals TDR-0002 declines.
3. **Put interpretation skills in a separate repository.** Rejected: the skills and the specifications they interpret must not version independently, or the interpretation drifts from the standard it claims to serve. It would also produce two descriptions of the same record semantics, one for humans and one for machines — the outcome this decision most wants to avoid.
4. **Declare interpretation out of scope entirely.** Rejected: it does not remove the work, only the standard's account of it. Every adopter would build recognition privately, and the resulting records would be conformant in syntax while incomparable in provenance and confidence.
5. **Specify the interchange structures as record types.** Rejected: it would make this repository a standard for mining pipelines, which is the boundary breach this decision refuses. They are named as interchange structures precisely so they cannot be mistaken for governed records.

## Options foreclosed

- The repository cannot later admit storage, indexing, orchestration or runtime concerns without superseding this record. The boundary is now stated positively rather than resting on a list of excluded implementation categories.
- Interpretation skills cannot be specialised to any runtime. A skill that assumes a particular product is non-conformant with this decision, however useful it is in that product.
- The standard cannot later define a machine-specific variant of any record type. One specification serves both authoring and interpretation, and this forecloses divergence deliberately.
- A skill can never be given authority to ratify. Any future capability that admits records to organisational truth requires a superseding record, not a new skill.

## Consequences and review

Success looks like interpretation skills that run unmodified on a second runtime, and candidate records that a named owner ratifies or rejects on their merits — with the rejected ones rejected because the evidence was insufficient, not because the skill invented something.

The honest uncertainty, and why confidence is medium rather than high: it is not yet demonstrated that interpretation semantics can stay genuinely portable. Authoring skills proved portable because they operate on a human's own knowledge; interpretation skills operate on messy source material, and may turn out to need runtime-specific retrieval assumptions to work at all. If that proves true, the boundary drawn here is right but the skills fall outside it, and this record is superseded to say so.

Review when the skills have been run against real organisational material by someone other than the author, or 2027-02-10, whichever is sooner.
