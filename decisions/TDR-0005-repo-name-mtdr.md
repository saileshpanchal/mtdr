---
id: TDR-0005
title: Name the repository MTDR — Markdown Transformation Decision Record
status: accepted
template: minimal
decision_date: 2026-07-05
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0001, TDR-0004
confirmed_by_outcome: pending — hardens at repo launch
---

# TDR-0005 — Name the repository MTDR (Markdown Transformation Decision Record)

## Context — what was known at the time

The repository needed a name before launch. "Transformation Decision Record" is unclaimed as a standard. The nearest community convention is the ADR lineage, where **MADR** names the markdown reference format of Architecture (now "Any") Decision Records — the format, not the concept.

A naming decision is cheap today and expensive after launch: once cited, forked and linked, a rename carries community cost.

## Decision

The repository is named **MTDR — Markdown Transformation Decision Record**, articulated in exact parallel to the ADR lineage:

- **TDR** is the standard: the record, its accountability semantics, its fields. Records keep `TDR-nnnn` identifiers.
- **MTDR** is the markdown reference format of TDRs — this repository — as MADR is to ADR.

This articulation signals lineage to the existing decision-record community while keeping the serialisation out of the standard's identity, consistent with TDR-0004 (markdown is reversible) and TDR-0002 (the differentiator is accountability, not format).

## Alternatives rejected

- **`tdr-standard`** — rejected: generic, and carries no lineage signal to the community most likely to adopt and challenge this work.
- **Rename the entire standard MTDR** — rejected: would bind the serialisation into the standard's identity, contradicting TDR-0004's stated reversibility, and would shift the perceived differentiator toward format rather than accountability semantics.

## Options foreclosed

After launch, renaming requires a superseding TDR and carries citation, fork and link breakage across the community. The TDR/MTDR articulation becomes the public vocabulary.

## Review

Accepted by the accountable owner on 2026-07-05. This record was written as `proposed` and confirmed the same day — demonstrating the maturity field in practice: not every decision is final at the moment it is written down, but it is recorded from the moment it exists. Status transitions are updated in place; changes to decision *content* require a superseding TDR.
