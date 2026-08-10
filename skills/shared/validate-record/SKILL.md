---
name: validate-record
description: Determine whether a record conforms to its specification — required fields, schema where one exists, enumerated values, lineage references that resolve, identifier and filename agreement, and legal status transitions. Use this skill before a record enters a register, whenever someone asks "is this valid?" or "will this pass validation", and as the final gate after drafting and challenge. It checks conformance only, and deliberately says nothing about whether the record's content is true, its evidence sufficient, or its judgement sound.
---

# Validate Record

This skill checks conformance. It is written for humans and usable by AI assistants. Read the
relevant record package in [`records/`](../../../records/) — its manifest, specification and schema
are the authority this skill applies.
[`practice/administration-and-assurance.md`](../../../practice/administration-and-assurance.md) carries the
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

### 2. Resolve the record's package, then validate against the schema its manifest names

Determine the record type from its `id` prefix, then read the owning package's manifest
(`records/<language>/package.yaml`): it names the specification, the specification version, and the
schema — or names a prior version with no schema. This skill hard-codes no package's paths; the
manifest is the lookup ([TDR-0023](../../../decisions/TDR-0023-portable-skill-architecture.md)).

**Validate every record against the specification version it was raised under, never a later one
retroactively.** Where the manifest lists a prior version with no schema, validate structurally
against that version's field table and say so. Reporting a legacy record as failing a newer schema is
version-blind validation, and it is wrong even when every reported failure is technically true.

### 3. Check the conditional requirements

A package's schema may carry conditional requirements — fields required only for certain template
tiers or states. The schema enforces them; state in the output that they were checked, so a reader
knows the conditionals ran rather than assuming the flat required-list was the whole test.

### 4. Check identifier and filename agreement

The `id` matches the filename, and ids are unique within the register. Note that ids are unique **per
organisation, not globally** — the worked examples deliberately use invented org-local numbering.

### 5. Resolve lineage references

Every `supersedes`, `derived_from` and `linked_decisions` id resolves to a record that exists. A
dangling reference is a validation failure, not a warning — it is how a register quietly stops being
navigable.

### 6. Check status transitions are legal

Records are superseded, never edited. The legal transitions are the package specification's; a
record re-entering a state its specification marks terminal — a `superseded` record revived, a
signed write-off reopened — is a failure.

### 7. Check review dates

Any due-date field the package specification defines that is in the past, on a record not yet
closed against it, is reported as overdue. Overdue is a finding, not an invalidity.

### 8. Check the `x-` namespace

Where the package's schema opens an `x-` adopter namespace, extensions are named
`x-<owner>-<field>`. **Schema validity implies nothing about security** — a record may validate while
carrying a classification that nothing enforces. A namespace one package's schema opens is not
thereby open in another's; check the schema at hand.

## Outputs

A pass or fail per check, with failures naming the field and the rule. Plus an explicit statement of which checks were
schema-based and which structural, and which specification version each record was validated against.

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
- **Version-blind validation** — running a legacy record against a later schema and reporting the newer required fields as failures.
- **Fixing in place** — repairing what should have been reported.

## Scope note

This skill validates a record against its specification. Registering, storing, indexing or enforcing
anything on the basis of the result is downstream implementation, deliberately outside this standard
(see TDR-0002, TDR-0018).
