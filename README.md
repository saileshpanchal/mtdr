# MTDR — Markdown Transformation Decision Record

**TDR** is a standard for recording significant organisational decisions with accountability semantics: what was known at the time, by whom, with what confidence. **MTDR** is its markdown reference format — as MADR is to ADR. The TDR has two sibling records: the **Value Record (VR)** — the value case and its life, the claim and the reconciliation as one record (since v1.3.0) — and the **Decision Assurance Case (DAC)** — a TDR preserves the judgement, it does not prove the consequences are acceptable; the DAC records the reasoning that challenges them, before execution (since v1.4.0).

MIT licensed. Tool-neutral. Regulator-neutral. Works alongside what you already run.

## Why

Organisations record the outcomes of decisions, rarely the judgement behind them. When the people who held the context move on, the organisation re-makes decided questions at full cost — and when a board, auditor or supervisor asks a named individual to demonstrate the judgement that was exercised, fragments in a shared drive do not answer the question.

A TDR preserves the judgement at the moment it is exercised: context as it stood, a named accountable owner, stated confidence, evidence assessed across seven dimensions, alternatives rejected, options foreclosed, and lineage connecting each decision to those before and after it.

## Quick start

1. Read [`spec.md`](spec.md) — ten minutes.
2. Take a decision your organisation made in the last month. Apply the proportionality rule (spec §3) and copy the matching template from [`/templates`](templates/).
3. Better: use the skills in [`/skills`](skills/) at your **next** decision — they are written for humans and structured so AI assistants can apply them directly.

## What's here

| Path | Contents |
|---|---|
| [`spec.md`](spec.md) | The TDR specification |
| [`spec-value-record.md`](spec-value-record.md) | The Value Record specification — the TDR's sibling record |
| [`spec-decision-assurance.md`](spec-decision-assurance.md) | The Decision Assurance Case specification — challenges a decision's consequences before execution |
| [`FAQ.md`](FAQ.md) | Boundary FAQ — what a TDR is not |
| [`/templates`](templates/) | Full, minimal and bare TDR templates, the VR template and the DAC template |
| [`/skills`](skills/) | Recording: Decision Identification · Problem Framing & Decision Capture · Evidence Review · Governance Review · Value Record. Assurance: Systems Thinking · Systems Dynamics · Fraud & Adversarial Thinking · Customer Outcomes · Adaptive Capacity · Accumulated & Resultant Risk · Counterfactual & Evidence · Assurance Synthesis |
| [`/examples`](examples/) | Fictional worked examples (full and minimal) |
| [`/decisions`](decisions/) | **This standard's own design decisions, recorded as TDRs** |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to challenge a decision — by superseding it |

## A standard that uses itself

Every significant decision about the TDR's design is recorded in [`/decisions`](decisions/) using the format itself — including the proportionality ladder, demonstrated rather than asserted. Decisions there are never edited or deleted, only superseded. If you disagree with the reasoning, [propose a superseding TDR](CONTRIBUTING.md): what is now known that was not known at the time?

## Relationship to existing standards

TDRs extend the [ADR](https://adr.github.io/) lineage with gratitude — MADR generalised scope; the TDR adds accountability semantics. TDRs work alongside ADRs, MADR, SAP LeanIX, Confluence and GRC platforms; they replace none of them. See spec §2 and [TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).

## Acknowledgement

This standard emerged from the *Decision Debt* article series. Its development was supported by Digital Transformation Advisory. The standard itself is neutral, open, and belongs to whoever finds it useful.

## Author

Sailesh Panchal · MIT License
