---
id: TDR-0013
title: Add practice guides for building decision memory
status: accepted
template: minimal
decision_date: 2026-07-22
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0003, TDR-0011
confirmed_by_outcome: none
---

# TDR-0013 — Add practice guides for building decision memory

## Context — what was known at the time

The standard specified the record format, the skills, and (from TDR-0011) how to deploy the skills as an
agent, but it did not explain how an organisation actually runs the discipline day to day: how to start,
how a record set becomes searchable memory, how records connect to controls, evidence and attestation, and
how to trust an assistant's output. That gap was being filled privately, in engagement-specific material.
The generalisable parts of that material belong in the open repository, provided they carry no adopter- or
vendor-specific content — neutrality is part of the standard's adoption model.

## Decision

Add a [`/practice`](../practice/) directory with three neutral guides: a
[quick start](../practice/quickstart.md) (start with one bounded area, the loop, the three rules), a
[practice operating model](../practice/operating-model.md) (the source taxonomy, the inner and outer loops,
the deterministic-validator-vs-semantic-curator split, the immutability and relationship-index rule, the
assurance chain, the coverage gate, collections as an optional view, and governing one's own adoption), and
an [administration and assurance guide](../practice/administration-and-assurance.md) (scoped knowledge, the
structured lineage review, the deterministic validator, the three-tier assurance harness with known-answer
tests, and reference prompts). Descriptive, not normative; additive; no field, template or schema change.

## Alternatives rejected

- **Fold the practice material into an adopter-specific pack only** — rejected: the generalisable discipline
  belongs in the open repository so any adopter can run it; the adopter-specific pilot material stays
  private.
- **Ship the policy-decomposition classifier skill alongside** — rejected: that classifier is an adopter
  extension and stays out of the neutral core until evidence across several domains shows it generalises;
  the practice guides describe the *concept* (policies are decision collections) without shipping the
  extension.
- **Make the guides normative** — rejected: they visualise and operationalise existing rules; a normative
  section would imply new conformance obligations where there are none.

## Options foreclosed

The `/practice` directory is now part of the repository's surface; the conformance boundary is unchanged
(the standard still ends at the decision register, per ARCHITECTURE.md and TDR-0012). Practice guidance is
explicitly non-normative and must stay that way.

## Review

No outcome trigger — an explanatory addition, confirmed by whether adopters find the repository easier to
take up. The next planned step is lowering adoption friction further (a ten-minute path, worked examples, a
runnable validator, a community profile).
