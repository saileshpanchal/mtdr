# Changelog

All notable changes to the TDR standard (and its MTDR markdown reference format) are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/), and the standard adheres to [Semantic Versioning](https://semver.org/). The *reasoning* behind each significant change lives in [`/decisions`](decisions/) as a TDR — this file is the index to it.

## [1.6.0] — 2026-07-20

Refinements from the first at-scale field application of the assurance skills — run as agents over
a corpus of thin, machine-derived decision records. Additive: all v1.5.0 records still validate.
The reasoning, and the rejected alternatives, live in [TDR-0011](decisions/TDR-0011-routing-and-disposition-refinements-from-field-application.md).

### Added
- **Internal-integrity variant** of fraud-and-adversarial-thinking (step 1): a decision that
  changes internal correctness or concentrates data/authority without new external economics still
  earns a short pass — reconciliation gaming, insider abuse of the new concentration, error-as-attack.
- **Indirect-effect pass and fair-lending signpost** in customer-outcomes: run the pass lightly and
  say why where customers are affected only second-hand; and for automated eligibility, pricing or
  credit, the cohort analysis *is* the indirect-discrimination test.
- **Compound and thin records** guidance in assurance-synthesis: a fused record is **split**, not
  blended; a thin record's absent inputs are named as decision-debt, and inferred controls are
  declared as inferred, never averaged into a comfortable disposition.

### Changed
- **Routing is by materiality, not category** (DAC spec §4). The trigger lists are illustrative,
  not auto-firing — a lens is routed by whether the decision *materially* changes what it governs.
  This reconciles §4 with the fraud-and-adversarial skill's own "a decision that creates no new
  economics needs little from this skill — say so and stop." The normative routing rule is left
  intact; materiality enters as clarifying guidance beside it.
- **Vacant-owner disposition** (DAC spec §5.2.11): where a record names no accountable owner, the
  first constraint is to name one; a case that cannot name an owner defers rather than proceeds.
- **Trend vs trajectory** (DAC spec §6): a cross-reference clarifying that non-monotonic transition
  shapes are carried by `expected_trajectory` (§5.2.6), not the point-in-time trend value.
- `spec.md` and `spec-decision-assurance.md` bumped to 1.6.0. Additive: no field, schema or
  template changes; every v1.x record still validates.

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
