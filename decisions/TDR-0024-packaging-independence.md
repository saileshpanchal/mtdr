---
id: TDR-0024
title: Packaging independence — runtime and plugin packagings are distribution adapters, never normative architecture
status: accepted
template: minimal
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0011, TDR-0020
confirmed_by_outcome: pending — review when the skills have shipped through a second distribution surface with zero change to any normative artefact, or 2027-02-10
---

# TDR-0024 — Packaging independence: runtime and plugin packagings are distribution adapters, never normative architecture

## Context — what was known at the time

The agent-plugin ecosystem has converged on a useful shape: instructions, skills, schemas, examples and metadata travelling together as a portable capability package. A record package (TDR-0021) maps onto that shape almost exactly, which makes distribution through such surfaces cheap — and makes the opposite risk acute. TDR-0011 already deployed the standard through one runtime and held the line ("worked examples, never dependencies"); with packaging becoming systematic, the line needs stating as architecture rather than re-arguing per surface. The failure mode is specific: a runtime's packaging constraints — its manifest format, its bundle limits, its selection heuristics — leaking backwards into how skills, schemas or specifications are written.

## Decision

Distribution packagings — for any agent runtime, plugin framework, or surface not yet invented — are **adapters generated or assembled from the normative artefacts, never sources of constraint on them**. The normative source is always the record package and the substrate. Adapter documentation lives in `skills/packaging/`, may name products freely (it is the one place TDR-0020 permits that), and carries per-surface assembly instructions. A change is inadmissible if its only justification is a packaging surface's requirement; the surface gets an adapter-side workaround or goes unsupported.

## Alternatives rejected

1. **Adopt one plugin format as the repository's native structure.** Rejected: it would make one vendor's packaging the standard's skeleton — TDR-0020's quiet-convergence failure, executed in one step.
2. **No packaging documentation at all.** Rejected: adopters deploy somewhere; undocumented deployment produces per-adopter forks of the instructions, which is drift by another route.

## Options foreclosed

- No normative artefact may carry packaging metadata for a specific surface; per-surface metadata lives in the adapter.
- No packaging surface's constraint may motivate a change to a specification, schema, template or skill body.

## Review

At the trigger: a second distribution surface served entirely from adapter-side assembly is the architecture confirmed; a normative edit traced to a packaging constraint is it refuted.
