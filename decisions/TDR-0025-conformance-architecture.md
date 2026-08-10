---
id: TDR-0025
title: Conformance architecture — schema validation alone is insufficient; examples, counter-examples, fixtures and semantic equivalence form the test surface
status: accepted
template: minimal
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0006, TDR-0017, TDR-0018, TDR-0021
confirmed_by_outcome: pending — review when two independent implementations have been run against the same corpus and their contributions compared, or 2027-08-10
---

# TDR-0025 — Conformance architecture: schema validation alone is insufficient; examples, counter-examples, fixtures and semantic equivalence form the test surface

## Context — what was known at the time

A standard is not open because its markdown is on GitHub. It is open when independent implementations can produce the same *meaning* — and schema validation cannot test that. The repository's own history shows the gap: the v1.13.0 fixtures exist precisely because a structurally valid candidate can be semantically wrong in ways no schema detects (a silent merge of two commitments validates perfectly), and TDR-0017 scored the standard's own interpretation contract as unmet. What the fixtures established ad hoc — expected results *and* must-not results, because the right answer by the wrong route is still wrong — now needs to be the stated conformance model rather than a good habit.

## Decision

Conformance is a layered surface, and each **mature** record package carries all of it: the specification; a machine-readable schema; normative examples; **counter-examples** (material that must *not* yield a record, merges that must *not* happen); conformance fixtures with expected and must-not sections; validation rules; and the package's portable skills. Cross-language fixtures and the shared corpus live in `tests/`. The horizon test, stated now and not yet passable: *given the same source corpus, can independent implementations recognise materially equivalent contributions and produce semantically equivalent candidate records?* That is deliberately stronger than schema validity and deliberately weaker than byte equality — span boundaries and phrasings may differ; objects, roles, groupings, gaps and conflicts may not. Candidate packages (TDR-0021) carry none of this until admitted; a package's maturity is measured by which conformance layers it actually has, not by its directory existing.

## Alternatives rejected

1. **Schema validation as the conformance bar.** Rejected: it certifies well-formedness of exactly the failures that matter most — the confident invention and the silent merge both validate.
2. **Byte-equivalence between implementations.** Rejected: it would make span segmentation normative, which TDR-0018's fixtures already deliberately refuse ("counts are ranges").
3. **Defer conformance until a second implementation exists.** Rejected: the corpus is what makes a second implementation attemptable; deferring it defers the standard being testably open.

## Options foreclosed

- No package may be described as mature while missing a conformance layer; the description is checkable against the package's contents.
- Fixtures without a must-not section are non-conforming fixtures — the discipline established at v1.13.0 is now binding.

## Review

At the trigger: the comparison of two independent implementations over one corpus, whatever it shows, is the evidence — a documented divergence is a successful review with a finding, not a failed one.
