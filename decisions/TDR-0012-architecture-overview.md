---
id: TDR-0012
title: Publish an architecture overview that fixes the standard's boundary at the decision register
status: accepted
template: minimal
decision_date: 2026-07-22
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0011
confirmed_by_outcome: none
---

# TDR-0012 — Publish an architecture overview that fixes the standard's boundary at the decision register

## Context — what was known at the time

With the agent deployment pack (TDR-0011), the standard visibly separated into layers — a
runtime that applies the skills, the skills as an execution model, the records, and the
register that holds them — while the graph and any reasoning layer above it remained optional
consumers. That separation was already implied by the progressive-adoption ladder (DAC spec
§4), the graph-ready lineage fields (spec §6) and the record-is-not-the-runtime-object
discipline, but it had never been drawn as one picture. An architect reading the specs could
not see, at a glance, where the standard ends. The risk of leaving it implicit is that
adopters assume a graph or a platform is a prerequisite — the opposite of the intended
progressive adoption.

## Decision

Add [`ARCHITECTURE.md`](../ARCHITECTURE.md): a single-diagram overview whose load-bearing claim
is a boundary — the standard ends at the decision register; everything above it is the
standard, everything below it is an optional consumer, and a conforming implementation can stop
at the register. The optional layers below the register (a decision graph; a reasoning layer
over it) are described **generically and named by no one** — the same neutrality the specs give
regulators (worked examples, never dependencies) and runtimes (TDR-0011), now extended to graph
technology and any higher-order reasoning product. Descriptive, not normative: it draws
boundaries the specifications already define. Ship as v1.7.0 — additive documentation, no field,
template or schema change.

## Alternatives rejected

- **Name a specific reasoning layer at the top of the diagram** — rejected: naming any
  particular graph engine or intelligence product in the neutral standard couples it to one
  implementation and breaks the portability the overview exists to demonstrate. The top layers
  stay generic; instances are named by their builders, elsewhere.
- **Make the architecture normative (a spec section)** — rejected: it defines no new field or
  rule; it visualises existing ones. A normative section would imply new conformance obligations
  where there are none.
- **Leave the layering implicit in the specs** — rejected: the boundary is the single most
  important thing an evaluating architect needs, and "you can stop at the register" is too
  strong a claim to leave un-drawn.

## Options foreclosed

The register is now the published conformance boundary. Moving it — making a graph or a
reasoning layer part of the standard — would be a change to what conformance means, requiring a
superseding record, not a minor version.

## Review

No outcome trigger: this is an explanatory artefact, confirmed by whether architects read the
boundary correctly. Revisit only if adopters still assume a graph is required.
