# Changelog

All notable changes to the TDR standard (and its MTDR markdown reference format) are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/), and the standard adheres to [Semantic Versioning](https://semver.org/). The *reasoning* behind each significant change lives in [`/decisions`](decisions/) as a TDR — this file is the index to it.

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
