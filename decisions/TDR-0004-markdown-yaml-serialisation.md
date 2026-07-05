---
id: TDR-0004
title: Markdown with YAML frontmatter as the serialisation format
status: accepted
template: bare
decision_date: 2026-07-05
accountable_owner: Sailesh Panchal
confidence: high
supersedes: none
derived_from: TDR-0001
---

# TDR-0004 — Markdown with YAML frontmatter as the serialisation format

**Decision:** Records are plain markdown files with YAML frontmatter. Humans read the body; machines read the frontmatter.

**Why:** Survives every platform migration, diffs cleanly in version control, needs no tooling to write, and follows the convention the ADR/MADR community already knows.

**Reversible:** Yes — a converter to any richer format can be written later without touching a single existing record. Hence the bare template: this decision does not need a full record, and pretending otherwise is exactly the box-ticking this standard exists to avoid.
