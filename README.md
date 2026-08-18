# MTDR — Markdown Transformation Decision Record

**TDR** is a standard for recording significant organisational decisions with accountability semantics: what was known at the time, by whom, with what confidence. **MTDR** is its markdown reference format — as MADR is to ADR. The TDR has two sibling records: the **Value Record (VR)** — the governed memory of an Operational Value Commitment, holding the commitment and its settlement as one record (since v1.3.0; v2.0.0 since 1.14.0) — and the **Decision Assurance Case (DAC)** — a TDR preserves the judgement, it does not prove the consequences are acceptable; the DAC records the reasoning that challenges them, before execution (since v1.4.0).

MIT licensed. Tool-neutral. Regulator-neutral. Works alongside what you already run.

## Why

Organisations record the outcomes of decisions, rarely the judgement behind them. When the people who held the context move on, the organisation re-makes decided questions at full cost — and when a board, auditor or supervisor asks a named individual to demonstrate the judgement that was exercised, fragments in a shared drive do not answer the question.

A TDR preserves the judgement at the moment it is exercised: context as it stood, a named accountable owner, stated confidence, evidence assessed across seven dimensions, alternatives rejected, options foreclosed, and lineage connecting each decision to those before and after it.

## Quick start

1. Read [the TDR specification](records/decision/specification/tdr.md) — ten minutes.
2. Take a decision your organisation made in the last month. Apply the proportionality rule (spec §3) and copy the matching template from [`records/decision/templates/`](records/decision/templates/).
3. Better: use the skills at your **next** decision — they are written for humans and structured so AI assistants can apply them directly. Start from your language's package under [`records/`](records/).

## What's here

The repository is organised as **record packages** — one per organisational language — over a
record-neutral substrate ([TDR-0021](decisions/TDR-0021-record-package-architecture.md)):

| Path | Contents |
|---|---|
| [`specification/`](specification/) | The substrate: the [umbrella specification](specification/organisational-records.md), the [contribution model](specification/contribution-model.md) (fragments → contributions → candidates), provenance, identity, uncertainty, [candidacy and ratification](specification/candidacy-and-ratification.md), the [record admission test](specification/record-admission-test.md) and [what conformance means](specification/conformance.md), the [validation-result contract](specification/validation-result.md), the [derivation projection](specification/derivation-projection.md), the [obligation chain](specification/obligation-chain.md) and the [standards boundary](specification/standards-boundary.md) |
| [`records/decision/`](records/decision/) | **The decision language** — TDR spec, DAC spec, schemas, templates, examples, fixtures, validation, and its skills (authoring, drafting, assurance) |
| [`records/value/`](records/value/) | **The value language** — VR v2 spec (the Operational Value Commitment), schema, template, example, fixtures, validation, and its skills |
| [`records/`](records/) | The package index, the extraction and dependency rules, and three **candidate** packages (authority · work · evidence) holding scope only |
| [`skills/shared/`](skills/shared/) | The record-neutral skills: identify contributions · reconcile fragments · challenge · validate · [show me why](skills/shared/show-me/) |
| [`skills/packaging/`](skills/packaging/) | Distribution adapters — deploying the same files through specific runtimes ([TDR-0024](decisions/TDR-0024-packaging-independence.md)) |
| [`schemas/`](schemas/) | The [validation-result contract](schemas/validation-result.schema.json) and, in [`shared/`](schemas/shared/), the interchange schemas for the contribution model |
| [`mtdr_validation/`](mtdr_validation/) | A **non-normative** reference implementation of the result contract. The contract governs; this code does not |
| [`mtdr_packaging/`](mtdr_packaging/) | A **non-normative** generator that assembles distribution bundles from the manifests. It decides where files go and never what they mean |
| [`tests/`](tests/) | Cross-language fixtures, [validation-result fixtures](tests/validation/), deployed-agent probes, the corpus, and the interoperability horizon |
| [`practice/`](practice/) | Practice guides: quick start, operating model, administration & assurance |
| [`spikes/`](spikes/) | **Non-normative** experiments whose findings are recorded — currently the [SHACL relational-validity spike](spikes/shacl-relational-validity/) |
| [`decisions/`](decisions/) | **This standard's own design decisions, recorded as TDRs**, and the [identifier allocation register](decisions/ALLOCATION.md) |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) · [`FAQ.md`](FAQ.md) · [`GOVERNANCE.md`](GOVERNANCE.md) · [`CONTRIBUTING.md`](CONTRIBUTING.md) | The layered architecture and where the standard ends · what a TDR is not · how the repository governs itself · how to challenge a decision |

Files at pre-restructure paths (`spec.md`, `templates/`, `shared/`, …) are pointer stubs preserving
old links; the canonical artefacts live in the packages.

## A standard that uses itself

Every significant decision about the TDR's design is recorded in [`/decisions`](decisions/) using the format itself — including the proportionality ladder, demonstrated rather than asserted. Decisions there are never edited or deleted, only superseded. If you disagree with the reasoning, [propose a superseding TDR](CONTRIBUTING.md): what is now known that was not known at the time?

## Relationship to existing standards

TDRs extend the [ADR](https://adr.github.io/) lineage with gratitude — MADR generalised scope; the TDR adds accountability semantics. TDRs work alongside ADRs, MADR, SAP LeanIX, Confluence and GRC platforms; they replace none of them. See spec §2 and [TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).

## Acknowledgement

This standard emerged from the *Decision Debt* article series. Its development was supported by Digital Transformation Advisory. The standard itself is neutral, open, and belongs to whoever finds it useful.

## Author

Sailesh Panchal · MIT License
