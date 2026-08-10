---
id: TDR-0020
title: State the repository boundary — an open organisational-records standard with no knowledge of its consumers
status: accepted
template: full
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: high
maturity: proposed
supersedes: none
derived_from: TDR-0001, TDR-0002, TDR-0018
confirmed_by_outcome: pending — review when a party unknown to the author has produced conformant records using only this repository, or 2027-02-10, whichever is sooner
---

# TDR-0020 — State the repository boundary: an open organisational-records standard with no knowledge of its consumers

## Context — what was known at the time

The repository began as one record format (TDR-0001) and has grown by accretion into something larger: three shipped record types, nineteen skills, an interchange model for reconstructing records from arbitrary material (TDR-0018), and a settled expectation that further organisational languages — authority, work, evidence — will arrive as they pass an admission discipline.

The boundary rulings made so far each answered one question at a time: TDR-0002 declined to bind the standard to software, TDR-0018 fixed the artefact boundary for interpretation skills. What has never been recorded is the repository's positive identity — what it *is*, stated once, so every later scope question is answered by reference rather than re-litigated.

Meanwhile the author's own consultancy builds sophisticated consumers of these records. The temptation this record exists to foreclose is quiet convergence: the standard gradually shaping itself around one consumer's architecture until the open proposition — clone it, use it with any tooling, produce conformant records — becomes true in licence and false in practice.

## Decision

The mtdr repository is an **open organisational-records standards and skills repository**. Its job is to provide portable definitions, schemas, examples, validation rules and reusable skills that allow humans or machines to identify, construct, challenge and validate governed organisational records from arbitrary organisational material.

**The repository knows about:** organisational record languages; their semantics and schemas; source fragments and provenance; contribution classification; assembly and reconciliation rules; validation; examples and conformance fixtures; portable skills for working with those records.

**The repository does not know about:** any consumer product or platform; graphs or graph databases; document stores; storage of any kind; orchestration; organisational runtimes; or what happens to a completed record downstream.

The test, inherited from TDR-0018 and now applied to the whole repository: someone must be able to clone this repository, use the specifications and skills with whatever agent or tooling they choose, and produce conformant records **without knowing that any particular consumer exists**. Named products may appear only in distribution-adapter documentation as worked examples, per TDR-0024 — never in a specification, schema, template, skill body or fixture.

## Evidence

- **Business** — a standard shaped by one consumer caps its adoption at that consumer's reach, which is the failure TDR-0001 was written to prevent. The author's interest in downstream consumers is declared, exactly as it was in TDR-0001, and this record is the structural control on it.
- **Architecture** — the knows/does-not-know lists are checkable: a grep for consumer names over normative artefacts is a conformance test of the repository itself. Boundaries that are testable get held; boundaries that are vibes do not.
- **Regulatory** — not material to this decision.
- **Operations** — contributors need a scope answer that does not require reading nineteen prior decisions. One record now carries it.
- **Customer** — not material at repository level.
- **Data** — records produced with these skills are the adopter's, in the adopter's storage. The repository knowing nothing about storage is what makes that unconditional.
- **External** — successful open standards (the ADR/MADR lineage, JSON Schema itself) survive precisely because no single consumer's architecture is visible in them.

## Alternatives rejected

1. **Leave the boundary distributed across TDR-0002 and TDR-0018.** Rejected: each answers a narrower question, and scope creep happens in the gaps between narrow answers.
2. **Name the known consumers and their integration points.** Rejected: documenting a consumer is the first step to accommodating it. The repository's ignorance of its consumers is a feature to be defended, not a gap to be filled.
3. **Split the standard and the skills into separate repositories.** Rejected, reaffirming TDR-0018: skills and the specifications they serve must not version independently.

## Options foreclosed

- No normative artefact may ever reference a consumer product, platform or runtime. Worked-example deployment documentation is confined to distribution adapters (TDR-0024).
- The repository can never grow storage, orchestration or graph concerns without superseding this record.
- The author's own consumers get no privileged surface: anything they need from the standard must arrive as an open proposal like anyone else's.

## Consequences and review

Success looks like conformant records produced by someone the author has never met, using tooling the author has never seen. Review at the confirmed-by-outcome trigger; the grep-for-consumer-names check runs from pass 1 and its result is reportable at every release.
