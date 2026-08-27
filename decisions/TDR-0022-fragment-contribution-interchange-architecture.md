---
id: TDR-0022
conforms_to: mtdr/decision/tdr@1.15.0
title: Ratify the fragment-and-contribution interchange model as repository architecture
status: accepted
template: minimal
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0018, TDR-0020, TDR-0021
confirmed_by_outcome: pending — review with TDR-0018, 2027-02-10
---

# TDR-0022 — Ratify the fragment-and-contribution interchange model as repository architecture

## Context — what was known at the time

v1.13.0 shipped the interchange structures — `SourceFragment → RecordContribution → CandidateAssembly` — as part of admitting the interpretation skills (TDR-0018). They were introduced as the contract *between skills*. The restructure now makes them load-bearing for the whole repository: every record package's interpretation path assumes them, and the conformance corpus (TDR-0025) is expressed in them. What was a skills detail is now architecture, and the architectural commitments deserve their own record rather than living implicitly in a release note.

The commitments are three. Records are reconstructed from **fragments**; documents are merely containers, and there is no document→record assumption anywhere in the standard — one paragraph may contribute to value, a sentence within it to authority, and one value record may need contributions from six documents and three transcripts. The pipeline runs `source material → fragment → contribution → assembly → record-specific reconciliation → candidate → validation and challenge → human ratification → governed record`, and no stage may be skipped by a conforming interpretation. And the interchange structures are **not organisational records**: they carry no authority, need not be persisted, and are not peers of the record schemas.

## Decision

The fragment-and-contribution model is repository architecture, not a skills implementation detail. Its normative home moves to the common substrate (`specification/`), every record package's interpretation path is defined against it, and its three commitments above bind every current and future language package. The structures remain interchange structures — a future proposal to persist them, govern them or give them authority is a proposal to create a sixth family, and is answered by TDR-0021's classification test (which they fail, by design).

## Alternatives rejected

1. **Leave the model as a skills-layer convention.** Rejected: conventions that five packages depend on are architecture whether recorded or not; unrecorded, the next package re-decides them.
2. **Promote the structures to record types with lifecycles.** Rejected: it would make the standard a mining-pipeline standard, breaching TDR-0018 and TDR-0020.

## Options foreclosed

- No record package may define its own competing fragment or contribution structure.
- No document-level classification path may be added to any package — the unit is the fragment, permanently.

## Review

With TDR-0018's review: evidence is interpretation skills running on a second runtime against the conformance corpus, fragments-first, with no document→record shortcut observed.
