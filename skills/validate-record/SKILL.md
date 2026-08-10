---
name: validate-record
description: Determine whether a record conforms to its specification — required fields, schema where one exists, enumerated values, lineage references that resolve, identifier and filename agreement, and legal status transitions. Use this skill before a record enters a register, whenever someone asks "is this valid?" or "will this pass validation", and as the final gate after drafting and challenge. It checks conformance only, and deliberately says nothing about whether the record's content is true, its evidence sufficient, or its judgement sound.
---

# Validate Record

This skill checks conformance. It is written for humans and usable by AI assistants. Read
[`spec.md`](../../spec.md) §4 and the relevant record package in [`records/`](../../records/).
[`practice/administration-and-assurance.md`](../../practice/administration-and-assurance.md) carries the
deterministic validator checklist this skill implements.

## The one rule

**Conformance is not correctness.** A record can validate perfectly and be entirely wrong. This skill
reports only whether the record is well-formed against its specification — never whether it should be
believed. Anyone treating a validation pass as assurance has misread both this skill and the standard.

## Process

### 1. Parse the frontmatter strictly

Use a strict YAML parser. Frontmatter is validated as JSON, so normalise native date types to ISO-8601
strings first — both schemas carry this caveat explicitly.

**Watch for the unquoted colon.** A colon mid-sentence in an unquoted scalar silently breaks parsing;
this is a defect the standard has already shipped once, recorded at v1.4.0.

### 2. Validate against the schema, where one exists

- TDR → [`schema/tdr.schema.json`](../../schema/tdr.schema.json)
- DAC → [`schema/decision-assurance.schema.json`](../../schema/decision-assurance.schema.json)
- **Value Record → no schema yet.** `spec-value-record.md` §4.1 says one "may follow in a later minor
  version". Validate against the specification's field table and the package's role list instead, and
  report that the check was structural rather than schema-based. **Do not silently pass a VR as
  schema-valid.**

### 3. Check the conditional requirements

TDR full and minimal templates additionally require `confidence` and `confirmed_by_outcome`. The schema
enforces this; state it in the output so a reader knows it was checked.

### 4. Check identifier and filename agreement

The `id` matches the filename, and ids are unique within the register. Note that ids are unique **per
organisation, not globally** — the worked examples deliberately use invented org-local numbering.

### 5. Resolve lineage references

Every `supersedes`, `derived_from` and `linked_decisions` id resolves to a record that exists. A
dangling reference is a validation failure, not a warning — it is how a register quietly stops being
navigable.

### 6. Check status transitions are legal

Records are superseded, never edited (`spec.md` §§6–7). A record moving from `superseded` back to
`accepted`, or a Value Record moving out of `written-off`, is a failure.

### 7. Check review dates

`reconcile_by` and `review_date` in the past, on a record not yet reconciled or reviewed, are reported
as overdue. Overdue is a finding, not an invalidity.

### 8. Check the `x-` namespace

Adopter fields are permitted on TDR frontmatter under `x-`, named `x-<owner>-<field>`. **Schema validity
implies nothing about security** — a record may validate while carrying a classification that nothing
enforces. Note the namespace is defined for `tdr.schema.json` only.

## Outputs

A pass or fail per check, with failures naming the field and the rule. Plus an explicit statement of
which checks were schema-based and which structural, so a Value Record result is never mistaken for a
schema pass.

## Quality checks

- Was a strict parser used, or one that tolerated malformed YAML?
- Were dates normalised before validation?
- Did every lineage reference get resolved against the actual register, rather than pattern-matched?
- Does the output distinguish invalid from overdue?

## When to refuse

- **Asked to fix rather than report.** Correcting a record is drafting work, and doing it inside
  validation hides that the record ever failed.
- **Asked to validate against a schema that does not exist.** Report the absence; do not substitute a
  near-neighbour schema.

## Anti-patterns

- **Validation as assurance** — a pass presented as evidence the record is sound.
- **Lenient parsing** — accepting frontmatter a strict parser would reject, so the defect surfaces later
  in someone else's tooling.
- **Pattern-matched lineage** — checking an id looks like an id rather than resolving it.
- **Silent VR passes** — reporting a Value Record as schema-valid when no VR schema exists.
- **Fixing in place** — repairing what should have been reported.

## Scope note

This skill validates a record against its specification. Registering, storing, indexing or enforcing
anything on the basis of the result is downstream implementation, deliberately outside this standard
(see TDR-0002, TDR-0018).
