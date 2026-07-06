---
id: TDR-0006
title: Provide a JSON Schema for the frontmatter as part of the format specification
status: accepted
template: minimal
decision_date: 2026-07-05
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0002, TDR-0004
confirmed_by_outcome: pending — review at spec v1.2
---

# TDR-0006 — Provide a JSON Schema for the frontmatter as part of the format specification

## Context — what was known at the time

The specification (§4.1) defines a fixed frontmatter field set and sells "YAML frontmatter for machine-readable fields," yet v1.0 shipped no machine-readable schema — the field contract lived only in a prose table. Meanwhile TDR-0002 draws a scope boundary: implementations and tooling belong in their own projects, not in the standard. The open question at v1.1 is whether a JSON Schema falls the wrong side of that boundary.

## Decision

Ship a JSON Schema for the frontmatter at `schema/tdr.schema.json`, as part of the **format specification** — not as tooling. A schema *defines* the format; it does not *implement* anything. It encodes exactly the §4.1 fields, including the conditional requirement of `confidence` and `confirmed_by_outcome` on the full and minimal templates, and validates frontmatter only; the markdown body remains unconstrained human judgement. Extraction pipelines, validators, editors and CI actions that *use* the schema remain out of scope, per TDR-0002.

## Alternatives rejected

- **No schema (prose table only).** Rejected: leaves the "machine-readable" claim asserted rather than demonstrated, and makes every adopter re-derive the same contract by hand.
- **Ship a validator or CLI.** Rejected: that is tooling and crosses the TDR-0002 boundary. The schema is the contract; implementations belong elsewhere.
- **Embed the schema inside `spec.md`.** Rejected: a schema is machine-consumed; it lives as a file tools can fetch, referenced from §4.1.

## Options foreclosed

The frontmatter contract is now dual-homed — the prose table in §4.1 and the schema file — and the two must stay in step: a field change is now a change to both. Per TDR-0002, a removal from the accountability core remains a different-standard change, not a minor version.

## Review

Additive and backward-compatible: no existing record changes, and every v1.0 record already validates. `confirmed_by_outcome` at spec v1.2 — has the schema been used (adopters validating in CI), and did the prose and schema drift apart? A two-way door: the schema can be revised or withdrawn by a superseding TDR without touching a single record.
