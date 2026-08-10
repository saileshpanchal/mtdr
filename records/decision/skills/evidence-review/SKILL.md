---
name: evidence-review
description: Review the evidence base of a Transformation Decision Record (TDR) for completeness, provenance and calibration across the seven evidence dimensions. Use this skill whenever a drafted TDR needs its Evidence section assessed or strengthened, whenever someone asks "is this decision well evidenced", "what are we missing", or "would this stand up to review" — and before any full-template TDR moves from proposed to accepted.
---

# Evidence Review

This skill assesses whether a TDR's evidence would satisfy the question the record exists to answer: *what was known at the time, by whom, with what confidence?* Read `spec.md` §5 for the dimension definitions.

## Process

### 1. Walk the seven dimensions

For each of **business, architecture, regulatory, operations, customer, data, external**, classify the record's treatment as one of:

- **Present** — evidence stated, with a location.
- **Not material** — explicitly declared, with a one-line justification that survives scrutiny.
- **Absent** — the dimension is silently missing. This is the finding that matters most.

An honest "not material" is worth more than padded prose. A silent absence is worth less than either — it is indistinguishable, later, from evidence that was never considered.

### 2. Check provenance

For every piece of evidence cited: *where does it live, and will that location survive?* A link to a named document in a governed repository passes. "Discussed in the steering meeting" fails — it points at a memory, not a record. Flag evidence whose only home is a person.

### 3. Test "not material" claims

For each declared exclusion, ask: *would a reviewer with no context accept this justification?* "Customer — not material: internal tooling decision with no customer-facing change" passes. "Regulatory — not material" on a channel closure at a regulated firm does not.

### 4. Calibrate confidence against evidence

Compare the frontmatter `confidence` with the evidence actually present:

- `high` confidence with thin evidence → challenge: what is the confidence actually resting on? If it is experience or judgement, say so in the record — that is legitimate evidence, but only when named.
- `low` confidence with strong evidence → challenge: what unstated risk is driving the hesitancy? Capture it in Context; it is exactly the kind of knowledge that evaporates.

### 5. Report

Produce a short completeness summary: dimensions present / not material / absent, provenance failures, and calibration findings. Recommend one of: **sufficient**, **sufficient with noted gaps**, or **return for evidence** — with the specific gaps listed.

## Anti-patterns

- **Volume as rigour** — long Evidence sections that cite much and locate nothing.
- **Dimension box-ticking** — one perfunctory line per dimension to make the section look complete.
- **"Not material" as evasion** — exclusions used to avoid gathering inconvenient evidence.
- **Provenance by anecdote** — evidence whose only source is what someone remembers.
