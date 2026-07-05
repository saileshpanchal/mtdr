---
id: TDR-0114
title: Migrate analytics workloads to a managed cloud warehouse; policy administration data remains on-premises this phase
status: accepted
template: minimal
decision_date: 2026-02-04
accountable_owner: D. Lindqvist, Chief Data Officer
confidence: medium
supersedes: none
derived_from: none
confirmed_by_outcome: pending — review at phase close 2026-11
---

> **Fictional worked example.** Meridian Mutual Insurance is invented. The example shows a minimal-template TDR: a significant decision that remains revisable at tolerable cost, recorded proportionately.

# TDR-0114 — Migrate analytics workloads to a managed cloud warehouse; policy administration data remains on-premises this phase

## Context — what was known at the time

Meridian's analytics estate runs on an on-premises warehouse approaching capacity, with a hardware refresh decision due Q3 2026. Analytics workloads are portable; policy administration data carries contractual and residency constraints that have not yet been assessed for cloud hosting. The team has cloud warehouse experience from a 2025 pilot. Unknown: the full cost profile at production scale — pilot economics have historically flattered.

## Decision

Analytics workloads migrate to a managed cloud warehouse in this phase. Policy administration data stays on-premises, with the residency and contractual assessment commissioned as a separate piece of work rather than assumed.

## Alternatives rejected

1. **Migrate everything in one phase** — bundles a portable workload with an unassessed constraint; the residency question deserves its own evidence, not a schedule.
2. **Refresh on-premises hardware for all workloads** — commits five years of capital to capacity the analytics migration would strand.
3. **Do nothing** — the capacity ceiling makes this a decision by default, on worse terms.

## Options foreclosed

Little is permanently foreclosed — analytics workloads can repatriate at known egress and re-platforming cost, estimated in the phase business case. The hardware refresh, once descoped, cannot be reinstated at current pricing.

## Review

`confirmed_by_outcome` tested at phase close (2026-11) against production-scale cost per query versus the pilot baseline. Confidence is `medium` for exactly that reason; if production economics diverge materially, a superseding TDR revisits the phasing. This is a two-way door held open on purpose — hence the minimal template.
