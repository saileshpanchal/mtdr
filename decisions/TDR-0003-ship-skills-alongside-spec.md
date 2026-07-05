---
id: TDR-0003
title: Ship practice skills alongside the specification
status: accepted
template: minimal
decision_date: 2026-07-05
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0001
confirmed_by_outcome: pending — review 2026-10-05
---

# TDR-0003 — Ship practice skills alongside the specification

## Context — what was known at the time

Formats without practice guidance become shelfware. The hard part of decision records is not the template; it is the discipline of framing the problem, gathering evidence, and reviewing the record at the moment of decision. Existing standards ship a format and assume the practice.

## Decision

The repository ships three skills alongside the specification: **Problem Framing & Decision Capture** (used at the decision, not after it), **Evidence Review** (completeness across the seven evidence dimensions), and **Governance Review** (does this record answer the accountability question as a reviewer would ask it). Written for humans; structured so AI assistants can apply them directly.

## Alternatives rejected

- **Spec-only repository** — rejected: highest adoption barrier, repeats the shelfware failure.
- **Ship software or agents** — rejected: crosses the standard/implementation boundary and ties the format to a stack.

## Options foreclosed

The standard now includes practice, not just format. Future versions must maintain the skills or supersede this record.

## Review

Confidence is medium: the skill set and its boundaries are expected to change with contributor use. Revisable by pull request; this is a two-way door held open on purpose.
