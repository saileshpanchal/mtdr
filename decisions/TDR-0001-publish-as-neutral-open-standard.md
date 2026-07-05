---
id: TDR-0001
title: Publish the Transformation Decision Record as a neutral open standard
status: accepted
template: full
decision_date: 2026-07-05
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: none
confirmed_by_outcome: pending — review 2026-10-05
---

# TDR-0001 — Publish the Transformation Decision Record as a neutral open standard

## Context — what was known at the time

Organisations accumulate decision debt: judgement made without preserving why, on what evidence, against which alternatives, and under whose accountability. Regulatory direction (in UK financial services: SM&CR "reasonable steps", Consumer Duty, and the FCA's 2026 review of AI in retail financial services) increasingly tests whether a *named individual* can demonstrate the judgement exercised at the time — a test that scattered fragments in decks, minutes and email do not pass.

At the date of decision:

- "Transformation Decision Record" was unclaimed as a standard.
- MADR 4.0 had renamed itself "Markdown Any Decision Records" — the *scope* of decision records was already generalised by the existing community.
- Enterprise tools (SAP LeanIX Architecture Decisions, Confluence, GRC platforms) manage decision documentation inside their own boundaries.
- No existing standard carried accountability semantics: confidence, evidence completeness, provenance, foreclosed options, and a named accountable owner.

The author advises organisations on building decision memory. That interest is declared, and it shapes this decision: the *format* must be a common good that travels beyond any single firm's practice, or it is not a standard at all.

## Decision

Publish the TDR as a neutral open standard: public repository, MIT licence, personal authorship, tool-neutral and regulator-neutral, explicitly designed to work alongside existing tools and standards rather than replace them.

## Evidence

- **Business** — standards succeed on adoption, not ownership; a proprietary format would cap adoption at one advisory firm's client base.
- **Architecture** — tool-neutrality requires the format to live outside any product; plain-text records survive every platform migration they will ever meet.
- **Regulatory** — a standard citing SM&CR and Consumer Duty as *worked examples* rather than dependencies travels across sectors and jurisdictions.
- **Operations** — MIT licensing removes procurement and legal friction for adopting teams; nothing to buy, nothing to negotiate.
- **Customer** — not material to this decision at standard level; addressed in worked examples.
- **Data** — open format guarantees organisations own their decision records outright, in their own repositories.
- **External** — the ADR/MADR precedent demonstrates that open, minimal, self-governed standards in this space achieve durable adoption; closed ones do not.

## Alternatives rejected

1. **Proprietary framework.** Rejected: contradicts the works-alongside stance, caps adoption, and makes the accountability record itself vendor-dependent — the exact failure mode the standard exists to prevent.
2. **Propose accountability fields upstream into MADR.** Rejected: MADR is engineering-native and deliberately minimal; governance semantics (accountable owner, evidence completeness, foreclosure) would strain its scope and its community's intent. Working alongside, with lineage credited, respects both.
3. **Publish as a paper or article series only.** Rejected: standards live where they can be versioned, challenged and superseded. A paper cannot receive a pull request.

## Options foreclosed

- Proprietary control over the format can never be asserted after publication.
- Any organisation — including competing advisory firms — may adopt, implement and commercialise practice around the standard. Accepted deliberately: adoption by competitors is evidence the standard works.
- Renaming or re-licensing now carries community cost and requires a superseding TDR.

## Consequences and review

Success looks like adoption and challenge: records written by organisations the author has never met, and superseding TDRs proposed against this folder. Review at 2026-10-05: `confirmed_by_outcome` to be updated with adoption evidence or an honest account of its absence.
