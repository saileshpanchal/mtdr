---
id: TDR-0002
title: Differentiate on accountability semantics, not scope
status: accepted
template: full
decision_date: 2026-07-05
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0001
confirmed_by_outcome: pending — review at spec v1.1
---

# TDR-0002 — Differentiate on accountability semantics, not scope

## Context — what was known at the time

The obvious positioning for a new decision-record standard is scope: "ADRs cover architecture; this covers *any organisational decision*." That ground was already taken. MADR 4.0 renamed itself "Markdown **Any** Decision Records" — the existing community had generalised scope before this standard existed.

What no existing standard carried was the semantics a governance or regulatory test actually asks for:

- **What was known at the time** — context captured at the moment of decision, not reconstructed.
- **By whom** — a named accountable owner, not a committee reference.
- **With what confidence** — stated, not implied.
- **On what evidence** — completeness assessed across defined dimensions (business, architecture, regulatory, operations, customer, data, external).
- **What was given up** — `options_foreclosed` as a first-class field: the futures this decision closes off.
- **Provenance and lineage** — `supersedes`, `derived_from`, `confirmed_by_outcome`.

Engineering decision records answer *"why is the system shaped this way?"* Accountability records answer *"could the person responsible defend this judgement with what they knew at the time?"* Those are different questions, and the second one is the one boards, auditors and supervisors increasingly ask.

## Decision

The TDR differentiates on accountability semantics. Scope is inherited gratefully from the ADR/MADR lineage; the additions are confidence, maturity, evidence completeness, foreclosed options, named accountability, and decision lineage. The specification states plainly that TDRs work alongside ADRs, MADR, SAP LeanIX Architecture Decisions, Confluence and GRC platforms — a TDR can reference an ADR as its architecture evidence.

## Evidence

- **Business** — re-litigation is the interest paid on decision debt: organisations re-making decided questions at full cost. Lineage fields (`supersedes`, `derived_from`, `confirmed_by_outcome`) are the direct countermeasure.
- **Architecture** — lineage fields make flat markdown graph-ready without shipping a graph: any tool can later assemble records into a connected decision history; no tool is required to.
- **Regulatory** — "reasonable steps" regimes attach to named individuals. A record without a named accountable owner and time-of-decision context cannot answer the question as asked. SM&CR and Consumer Duty are worked examples, not dependencies.
- **Operations** — evidence dimensions give reviewers a completeness check ("regulatory dimension not assessed") instead of a false sense of rigour from prose volume.
- **Customer** — the customer evidence dimension forces decisions that affect customers to say so explicitly, at decision time.
- **Data** — explicit fields make records queryable; prose-only records are not.
- **External** — the renaming of MADR 4.0 is itself evidence that scope-based differentiation was exhausted.

## Alternatives rejected

1. **Differentiate on scope.** Rejected: already claimed, and contested ground shrinks. A standard built on "broader than ADR" competes with its own lineage instead of extending it.
2. **Differentiate on tooling.** Rejected: tooling is implementation. A standard that requires particular software is a product with documentation.
3. **Adopt a compliance-framework framing (map fields to specific regulations).** Rejected: binds the standard to jurisdictions and dates. Regulator-neutral fields with regulatory *worked examples* travel; regulation-specific schemas expire.

## Options foreclosed

- The accountability core is the standard's identity from v1. Removing or weakening these semantics later would create a different standard, not a new version — such a change requires a superseding TDR and, in honesty, a different name.
- Field additions remain possible; field *removals* from the accountability core do not.

## Consequences and review

The bet: organisations under accountability pressure will adopt a format that answers the question they are actually asked, even though it demands more discipline than a minimal record. Review at spec v1.1 against contributor challenges and field-usage evidence from early adopters.
