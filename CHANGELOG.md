# Changelog

All notable changes to the TDR standard (and its MTDR markdown reference format) are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/), and the standard adheres to [Semantic Versioning](https://semver.org/). The *reasoning* behind each significant change lives in [`/decisions`](decisions/) as a TDR — this file is the index to it.

## [1.8.0] — 2026-07-22

### Added
- **Practice guides** ([`/practice`](practice/)) — how to run the discipline day to day, drawn from real practice and kept vendor- and adopter-neutral. A [quick start](practice/quickstart.md) (start with one bounded area, the authoring loop, the three rules that never bend); a [practice operating model](practice/operating-model.md) (read the source before you record it — internal policies are decision collections, external rules are obligation collections; the inner and outer loops, with deterministic validation in code and one semantic curator that proposes and never mutates; the immutability and relationship-index rule, including that there is no `contradicts` record field; the assurance chain from obligation to a named person's attestation, and the line that the tooling never attests; turning on search by coverage rather than count; and governing one's own adoption with a TDR, DAC and VR); and an [administration and assurance guide](practice/administration-and-assurance.md) (scoped-not-flat knowledge, the structured lineage review, the deterministic validator, a three-tier assurance harness with known-answer tests, and reference prompts). Descriptive, not normative. See [TDR-0013](decisions/TDR-0013-practice-guides.md).

### Changed
- `spec.md` bumped to 1.8.0; README gains the `/practice` row. Additive: no field, template or schema change; every v1.x record still validates.

## [1.7.0] — 2026-07-22

### Added
- **Architecture overview** ([`ARCHITECTURE.md`](ARCHITECTURE.md)) — a single-diagram view of the standard's layers whose load-bearing claim is a boundary: *the standard ends at the decision register.* Everything above the register (runtime → skills → records → register) is the standard; the decision graph and any reasoning layer over it are optional consumers, out of scope, and named by whoever builds them — the neutrality the specs give regulators and runtimes, now extended to graph technology. Descriptive, not normative: it draws boundaries [DAC spec §4](spec-decision-assurance.md) (progressive adoption), [spec §6](spec.md) (graph-ready lineage fields) and the record-is-not-the-runtime-object discipline already define. See [TDR-0012](decisions/TDR-0012-architecture-overview.md).

### Changed
- `spec.md` bumped to 1.7.0; README gains the architecture row. Additive: no field, template or schema changes; every v1.x record still validates.

## [1.6.0] — 2026-07-22

### Added
- **Agent deployment pack** ([`/agents`](agents/)) — the release that makes the standard machine-deployable. v1.0.0 made the skills applicable by AI assistants; the major agent runtimes now load the `SKILL.md` format natively, so this release adds the missing layer: vendor-neutral **agent instructions** and a deployment model ([`agents/README.md`](agents/README.md)) — instructions as the enforcement layer, skills loaded natively as method, specifications and templates as reference knowledge, with guidance for runtime memory and multi-agent topologies (specialist outputs are advisory evidence, never verdicts); a first **worked deployment** for Microsoft Copilot Studio ([`agents/copilot-studio.md`](agents/copilot-studio.md)) — runtimes are worked examples, never dependencies, the spec §8 discipline applied to vendors; and **six conformance probes** ([`agents/conformance.md`](agents/conformance.md)) any deployed agent must pass — identification and proportionality, the named-owner refusal, no-baseline-no-claim, assurance routing and the contradiction hunt, the composite-score refusal, supersede-don't-edit. Decided in [TDR-0011](decisions/TDR-0011-agent-deployment-pack.md), which also records why this is a minor release and not a "v2": nothing in the accountability core changes, and the versioning discipline is itself part of the standard.
- First field evidence noted in TDR-0011: an independent runtime (Copilot Studio, reasoning model) applied the unmodified skills to a live steering-committee pack — decisions identified and distinguished from requests and plans, full-template drafts produced, and both held at `proposed` for the named-owner rule, unprompted.

### Changed
- `spec.md` bumped to 1.6.0; README gains the `/agents` row. Additive: no field, template or schema changes; every v1.x record still validates.

## [1.5.0] — 2026-07-17

### Added
- **Temporal risk delta** — `riskDelta` gains optional `effective_from`, `expected_duration`, `expected_trajectory` and `dependency_conditions`: the case declares what risk the decision is expected to change, *when*, and under what conditions; a decision graph determines the accumulated and resultant position at any point in time. A migration that duplicates exposure before reducing it, or concentration that materialises only when a sibling decision lands, is now expressible. See [TDR-0010](decisions/TDR-0010-temporal-risk-delta.md). The worked example populates the new fields.
- **Progressive-adoption ladder** (spec §4): TDR → TDR + DAC → organisational risk context → decision graph → continuous assurance — each rung useful without the next; nothing in the standard requires a graph. The accumulated-and-resultant-risk skill now states explicitly that a graphless adopter's required output is the declared delta and interactions, with the computed resultant position out of scope.
- **No standing states** (spec §5.2.11): `defer-pending-evidence` and `experiment-within-bounded-authority` name their resolving evidence as dated, owned decision-debt items; the review date or a monitoring trigger reopens the disposition.

### Changed
- **Object semantics sharpened** (spec §3): skill outputs are advisory evidence contributing to the case, never verdicts — the synthesis produces the one disposition and its named owner signs it.
- **Headline framing**: "tests whether the decision is fit to execute" replaced with "a TDR preserves the judgement; it does not prove the consequences are acceptable" across spec, DAC spec and README — assurance challenges consequences; it cannot prove safety or fitness.
- Decision-debt definition clarified (spec §5.2.8): the debt lies in the evidence required to sustain confidence in execution, not necessarily in the decision itself. The rejected alternative of renaming it "assurance debt" is recorded in TDR-0010.
- `spec.md` and `spec-decision-assurance.md` bumped to 1.5.0. Additive: all v1.4.0 records still validate.

## [1.4.0] — 2026-07-17

### Added
- **Decision Assurance Case (DAC) specification** ([`spec-decision-assurance.md`](spec-decision-assurance.md)) — the TDR's second sibling record: the TDR records organisational judgement; the DAC records the reasoning that tests whether that judgement is fit to execute. Four questions (exploitability; who is harmed even working-as-designed; whether the controls themselves create poor outcomes; what evidence would disprove the assumptions); a compiler model (reusable reasoning skills compile into one case, one disposition, one owner); six dispositions; a ten-axis **risk vector with trend** and a no-composite-score rule; explicit **uncertainty**, **decision debt** and **learning obligations** blocks; `stale` as the standing-loss state; an explicit **non-goal** (a DAC never proves correctness — it proves systematic challenge). Proportionality governs: bare decisions never need a case. See [TDR-0009](decisions/TDR-0009-decision-assurance-case.md).
- **Eight assurance reasoning skills** ([`/skills`](skills/)) — systems-thinking, systems-dynamics, fraud-and-adversarial-thinking, customer-outcomes, adaptive-capacity (including execution capability: can *this* organisation run this safely), accumulated-and-resultant-risk (the delta is recorded; the resultant position is graph work; interactions are declared for it), counterfactual-and-evidence, and assurance-synthesis (routing + the contradiction hunt + the disposition).
- **DAC template** ([`templates/dac.md`](templates/dac.md)) and **JSON Schema** ([`schema/decision-assurance.schema.json`](schema/decision-assurance.schema.json)) validating the frontmatter and the optional structured `assurance` block.
- **Worked example** ([`examples/example-assurance-agentic-payment.md`](examples/example-assurance-agentic-payment.md)) — a fictional agentic payment journey (delegated authority, consent, fraud incentives, customer outcomes, machine execution) carried through all four projections to a constrained disposition; its structured block validates against the schema.
- An **extension model** (spec §9): domain *patterns* and regulator *profiles* as future layers that keep regulation out of the core — Consumer Duty, HM Treasury's agentic-payments trust framework and BCBS 239 appear as worked examples only.

### Changed
- `spec.md` bumped to 1.4.0; the sibling-record line now names both the VR and the DAC. README and decisions index updated. Additive: no TDR field, schema or template changes; every v1.x record still validates.

### Fixed
- Invalid YAML frontmatter in two previously released skill descriptions — an unquoted `:` mid-sentence made the frontmatter unparseable to strict YAML readers in [`skills/problem-framing-and-decision-capture`](skills/problem-framing-and-decision-capture/SKILL.md) (since 1.0.0) and [`skills/decision-identification`](skills/decision-identification/SKILL.md) (since 1.2.0). Corrected in place under the typo/clarity exemption in `CONTRIBUTING.md` — no judgement changed (the MADR-correction precedent, v1.1.0).

## [1.3.0] — 2026-07-12

### Added
- **Value Record (VR) specification** ([`spec-value-record.md`](spec-value-record.md)) — the TDR's sibling record: the TDR records the decision; the VR records the value case and its life. Five-state lifecycle (`proposed → agreed → realising → reconciled | written-off`, with write-off as a signed state), measured baseline ("no baseline, no claim"), named finance counter-signatory, mandatory reconcile-by date, declared optimism adjustment, and a procurement stage taxonomy. See [TDR-0008](decisions/TDR-0008-add-value-record-as-sibling-record.md). Ships with a template ([`templates/vr.md`](templates/vr.md)) and a worked example ([`examples/example-value-record-practice-skills.md`](examples/example-value-record-practice-skills.md)) that records the value case of this repository's own TDR-0003.
- A fifth practice skill, **Value Record** ([`skills/value-record/`](skills/value-record/SKILL.md)) — when to raise a VR, baseline-first drafting, the reconciliation loop, the write-off discipline, and explicit refusals: no baseline, no named counter-signatory or no reconcile-by date means the VR is not marked agreed.
- **TDR boundary FAQ** ([`FAQ.md`](FAQ.md)) — a TDR is not a consent receipt, identity claim, runtime audit log or model trace; the four adjacent-record contrasts, kept short.
- **Journey disposition guidance** in the decision-identification skill — every journey change starts with a value thesis (recordable as a VR), receives a disposition on the reversibility axis that is itself a decision record, and is promoted one rung at a time, each promotion a superseding record.

### Changed
- `spec.md` bumped to 1.3.0 and now points to the VR specification and the boundary FAQ. README updated accordingly. Additive: no TDR field, schema or template changes; every v1.x record still validates.

## [1.2.0] — 2026-07-06

### Added
- A fourth practice skill, **Decision Identification** ([`skills/decision-identification/`](skills/decision-identification/SKILL.md)) — recognises when a conversation, document or incident contains a decision worth recording, routes it through the proportionality test, and hands off to the existing skills via a tool-neutral **TDR Candidate Envelope**. See [TDR-0007](decisions/TDR-0007-add-decision-identification-skill.md). Additive: no spec, schema or template changes.

## [1.1.0] — 2026-07-05

### Added
- JSON Schema for the frontmatter at [`schema/tdr.schema.json`](schema/tdr.schema.json), referenced from spec §4.1 — see [TDR-0006](decisions/TDR-0006-json-schema-for-frontmatter.md). Additive and backward-compatible; every v1.0 record still validates.
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1).
- This `CHANGELOG.md`.

### Changed
- Credit Michael Nygard (2011) as the origin of the Architecture Decision Record (spec §2).
- Name the FCA's 2026 **Mills Review** explicitly (TDR-0001), so the reference is findable rather than a vague forward-reference.

### Fixed
- Corrected the MADR version: the rename to "Markdown Any Decision Records" and the generalisation of scope to any decision shipped in **MADR 3.0** (2022), not "MADR 4.0" (spec §2; TDR-0001; TDR-0002 ×2). A factual citation correction — no decision or judgement changed, so applied in place under the typo/clarity exemption in `CONTRIBUTING.md`.
- Removed an inconsistent version string from the README ("v1.0" vs the spec's "1.0.0").

## [1.0.0] — 2026-07-05

### Added
- Initial release: the TDR specification (`spec.md`); the MTDR markdown reference format; full, minimal and bare templates; three practice skills (Problem Framing & Decision Capture · Evidence Review · Governance Review); the standard's own design decisions as TDR-0001…TDR-0005; two fictional worked examples; the MIT licence; and a supersede-don't-edit contribution model.
