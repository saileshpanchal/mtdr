---
id: TDR-0023
conforms_to: mtdr/decision/tdr@1.15.0
title: Adopt the portable skill architecture — skills live with record semantics; shared skills must be demonstrably record-neutral
status: superseded
template: minimal
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0003, TDR-0018, TDR-0021
confirmed_by_outcome: pending — review when the value package's lifecycle skills have run end-to-end against the conformance corpus, or 2027-02-10
---

# TDR-0023 — Adopt the portable skill architecture: skills live with record semantics; shared skills must be demonstrably record-neutral

## Context — what was known at the time

Nineteen skills sat in one flat directory: five recording, eight assurance, six interpretation. Some are genuinely record-neutral (`identify-record-contributions` reads any material for any package); most carry one language's semantics (`draft-vr` is the value language, operationally). The flat layout hid that distinction, and the package architecture (TDR-0021) forces it: a package that must extract completely must carry its own skills.

The countervailing risk is premature abstraction — hoisting a skill to "shared" because two packages *might* use it, leaving record semantics stranded in a neutral skill that then quietly specialises.

## Decision

Skills live with the record semantics they carry; `skills/shared/` holds only skills that are **demonstrably record-neutral** — the demonstration being the skill's own text: it must reference no package's roles, admission test or specification except by parameter. Each record package exposes composable skills along one lifecycle — **identify → classify contributions → reconcile → draft → challenge → validate → ratify** (ratify always human, never a skill, per TDR-0018) — with explicit inputs and outputs stated in interchange-structure terms. Skills remain portable markdown (`SKILL.md`, frontmatter `name` + `description`, name equals leaf directory); distribution packaging is TDR-0024's concern and shapes nothing here. Where a shared skill and a package skill both apply, the package skill carries the record semantics and the shared skill the neutral mechanics — duplication of semantics between them is a defect, resolved in the package's favour.

## Alternatives rejected

1. **All skills shared, parameterised by package.** Rejected: record semantics belong with the record; a fully-parameterised drafting skill is a template engine, not a skill.
2. **All skills in packages, nothing shared.** Rejected: fragment capture, provenance and conflict detection are genuinely neutral, and five copies of them would drift into five dialects.
3. **A skill framework or DSL.** Rejected: the portable `SKILL.md` shape is the reason the skills run unmodified across runtimes today.

## Options foreclosed

- No skill enters `skills/shared/` carrying any package's semantics; the neutrality demonstration is reviewable at the pull request.
- The lifecycle stage names are now vocabulary; a package may omit a stage it does not need but may not rename one.

## Review

At the confirmed-by-outcome trigger: the value package's five lifecycle skills, run end-to-end on the corpus, with the shared four untouched — that is the architecture working.
