# Changelog

All notable changes to the TDR standard (and its MTDR markdown reference format) are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/), and the standard adheres to [Semantic Versioning](https://semver.org/). The *reasoning* behind each significant change lives in [`/decisions`](decisions/) as a TDR — this file is the index to it.

## [1.4.0] — 2026-07-17

### Added
- **Decision Assurance Case (DAC) specification** ([`spec-decision-assurance.md`](spec-decision-assurance.md)) — the TDR's second sibling record: the TDR records organisational judgement; the DAC records the reasoning that tests whether that judgement is fit to execute. Four questions (exploitability; who is harmed even working-as-designed; whether the controls themselves create poor outcomes; what evidence would disprove the assumptions); a compiler model (reusable reasoning skills compile into one case, one disposition, one owner); six dispositions; a ten-axis **risk vector with trend** and a no-composite-score rule; explicit **uncertainty**, **decision debt** and **learning obligations** blocks; `stale` as the standing-loss state; an explicit **non-goal** (a DAC never proves correctness — it proves systematic challenge). Proportionality governs: bare decisions never need a case. See [TDR-0009](decisions/TDR-0009-decision-assurance-case.md).
- **Eight assurance reasoning skills** ([`/skills`](skills/)) — systems-thinking, systems-dynamics, fraud-and-adversarial-thinking, customer-outcomes, adaptive-capacity (including execution capability: can *this* organisation run this safely), accumulated-and-resultant-risk (the delta is recorded; the resultant position is graph work; interactions are declared for it), counterfactual-and-evidence, and assurance-synthesis (routing + the contradiction hunt + the disposition).
- **DAC template** ([`templates/dac.md`](templates/dac.md)) and **JSON Schema** ([`schema/decision-assurance.schema.json`](schema/decision-assurance.schema.json)) validating the frontmatter and the optional structured `assurance` block.
- **Worked example** ([`examples/example-assurance-agentic-payment.md`](examples/example-assurance-agentic-payment.md)) — a fictional agentic payment journey (delegated authority, consent, fraud incentives, customer outcomes, machine execution) carried through all four projections to a constrained disposition; its structured block validates against the schema.
- An **extension model** (spec §9): domain *patterns* and regulator *profiles* as future layers that keep regulation out of the core — Consumer Duty, HM Treasury's agentic-payments trust framework and BCBS 239 appear as worked examples only.

### Changed
- `spec.md` bumped to 1.4.0; the sibling-record line now names both the VR and the DAC. README and decisions index updated. Additive: no TDR field, schema or template changes; every v1.x record still validates.

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
