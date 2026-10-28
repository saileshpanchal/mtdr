---
id: TDR-0047
conforms_to: mtdr/decision/tdr@1.15.0
title: Admission to the experimental runtime is not admission to the standard
status: accepted
template: minimal
decision_date: 2026-10-28
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0021, TDR-0024, TDR-0037
confirmed_by_outcome: pending — confirm when a second candidate uses this route without a bespoke governance process, or when the first experimental package is admitted, narrowed or withdrawn, whichever is sooner; else 2027-04-28
---

# TDR-0047 — Admission to the experimental runtime is not admission to the standard

> **Accepted 2026-10-28.** General, not specific to any one candidate. Evidence:
> [`evidence/TDR-0047-ratification-2026-10-28.md`](evidence/TDR-0047-ratification-2026-10-28.md).

## Context — what was known at the time

[TDR-0021](TDR-0021-record-package-architecture.md) gave packages two states. A **candidate** holds
metadata and scope only; a **normative** package has passed the record admission test. Nothing sits
between them.

That works when admission can be decided from argument. It fails when the question admission must
answer can only be settled by running the thing — when the evidence that a record family is needed
comes from implementing it, exercising it against organisational material, and observing what is lost
when it is removed. Under the two states, such a candidate can never acquire the evidence its
admission requires, because it may hold nothing until it is admitted.

The Operational Inheritance Record is the first such case ([TDR-0046](TDR-0046-oir-experiment-preregistration.md)).
It will not be the last: the authority and evidence candidates face the same question in different
forms. An open standard also needs its experiments in the open — review by people who did not build
them is part of how the evidence is gathered.

## Decision

**A third package state, `experimental`.** A package in it may carry every layer a normative package
carries — specification, schema, templates, examples, fixtures, validation rules and skills — and is
published on `main` for open review. It is **not part of the standard**, and the repository says so
mechanically rather than by label alone:

1. **Excluded from the standard's stated skill totals.** Statements of how many skills the standard
   has count admitted packages only.
2. **Excluded from the distribution bundles.** An experimental skill is loadable from the repository,
   never shipped as part of the standard's catalogue. Admission by distribution is not admission.
3. **Excluded from every conformance and release claim.** No release claim, conformance claim or
   eligibility computation rests on an experimental package.
4. **Announced in every repository validation result**, so no reader of a result can miss that the
   tree contains material that is not the standard.
5. **Governed by a pre-registration.** An experimental package names the accepted record that froze
   its test, and the suite refuses any change to the frozen criteria. **An implementation may not
   redefine the test that judges it.**

**Promotion is a decision, and only a decision.** An experimental package becomes `normative` only by
an admission record under the record admission test, through a traceable change to its status — not a
reimplementation. It may equally be narrowed, converted to a projection, or withdrawn; each is a
recorded decision.

The record admission test is unchanged and still governs admission. Extraction, boundary and
conformance checks **run** on experimental packages, because their results are part of the admission
evidence.

## Alternatives rejected

1. **Keep two states; build experiments outside the repository.** Rejected: the experiment then tests
   something other than the standard's own package machinery, and its review is no longer open.
2. **Build experiments on a branch that never merges.** Rejected: an open-source experiment needs open
   review, and a branch nobody reads gathers none.
3. **Admit provisionally, as normative with a caveat.** Rejected: a caveat is prose; distribution,
   counts and claims would all treat the package as the standard.
4. **A bespoke route per candidate.** Rejected: each candidate would then negotiate its own governance,
   which is the cost this record exists to remove.

## Options foreclosed

- No experimental package may be counted, distributed or claimed as part of the standard.
- No experimental package may exist without a governing pre-registration whose criteria it cannot
  change.
- No experimental package becomes normative except by an admission decision.

## Review

Confirm when a second candidate uses this route without a bespoke process, or when the first
experimental package is admitted, narrowed or withdrawn. Review on that evidence, or 2027-04-28.
