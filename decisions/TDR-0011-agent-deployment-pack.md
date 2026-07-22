---
id: TDR-0011
title: Ship an agent deployment pack; version it as a minor release, not a v2
status: accepted
template: minimal
decision_date: 2026-07-22
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0001, TDR-0003
confirmed_by_outcome: pending — all six conformance probes passed on at least one independent runtime; review 2026-10-05 alongside TDR-0003
---

# TDR-0011 — Ship an agent deployment pack; version it as a minor release, not a v2

## Context — what was known at the time

The skill format this repository has used since v1.0.0 — a `SKILL.md` with YAML
frontmatter and markdown instructions — became natively loadable across the major agent
runtimes in 2026 (Microsoft Copilot Studio in preview, Visual Studio's Copilot, the
Microsoft Agent Framework, alongside the Claude runtimes the format originated in). The
first independent field deployment followed: a Copilot Studio agent on a reasoning model,
loaded with these skill files **unmodified**, identified the decisions in a live
steering-committee pack, distinguished commitments from requests and plans, drafted two
full-template TDRs from the source wording — and held both at `proposed` with the
named-owner gap called out, unprompted. TDR-0003's bet ("structured so AI assistants can
apply them directly") now has evidence from a runtime and model this project does not
control. What was missing was small: the instruction layer that makes an agent *faithful*
(workflow order, normative routing, refusals), per-runtime setup, and a way to test a
deployment. Full conformance evidence (all six probes) did not yet exist at decision time.

## Decision

Add `/agents` — the deployment pack: vendor-neutral agent instructions and deployment
model (`agents/README.md`), per-runtime worked deployments starting with Copilot Studio
(`agents/copilot-studio.md`), and six conformance probes any deployed agent must pass
(`agents/conformance.md`). Runtimes are worked examples, never dependencies — the spec §8
discipline, applied to vendors. Ship as **v1.6.0**: the release that makes the standard
machine-deployable is additive — no field, template or schema changes; every v1.x record
still validates.

## Alternatives rejected

- **Version it 2.0.0** — rejected: spec §9 reserves major versions for changes to the
  accountability core; nothing in the record semantics changes. Inflating a minor into a
  major for positioning would fail the standard's own versioning claim. The milestone
  belongs in the release notes, not the version number.
- **A vendor-specific pack only** — rejected: couples a neutral standard to one runtime;
  the instructions are runtime-agnostic and the skills are portable by construction.
- **Wait for all six conformance probes to pass before shipping** — rejected: the probes
  ARE the instrument adopters (and this project) need in order to produce that evidence;
  shipping them is how the remaining evidence gets made. `confirmed_by_outcome` carries
  the completion condition honestly.
- **Fold the agent instructions into each skill** — rejected: enforcement (workflow,
  routing, refusals) is one layer with one owner; scattering it across thirteen files
  recreates the drift the v1.5.0 review removed.

## Options foreclosed

The pack commits the standard to the open skill format as its deployment surface, and
commits the conformance probes as a public bar: future changes to the six probes are
meaning changes requiring a superseding record.

## Review

`confirmed_by_outcome` completes when one independent runtime passes all six probes;
transcripts kept as evidence. Reviewed 2026-10-05 with TDR-0003, which this decision
part-confirms.
