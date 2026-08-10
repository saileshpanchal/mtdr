# Record packages — the extension contract

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

A record package tells an interpretation skill three things about one organisational object: what
semantic roles material can contribute to, what makes a candidate admissible, and where the canonical
specification lives.

## Packages do not duplicate specifications

The specifications, schemas and templates stay where they are — [`spec.md`](../spec.md),
[`spec-value-record.md`](../spec-value-record.md), [`schema/`](../schema/), [`templates/`](../templates/).
A package **points at them**; it never copies them.

This is deliberate. A package holding its own copy of a spec would create two sources of truth that
drift, and the drift would be invisible until a record validated against one and failed the other. The
package adds only what interpretation needs and the specification does not carry.

## Objects and their governed memory

Contributions target **organisational objects**. Records are how those objects are preserved portably.
The distinction matters for interpretation: the question is *"does this evidence help reconstruct an
OVC?"*, not *"does this document contain Value Record fields?"*

| Package | Organisational object | Governed memory | Status |
|---|---|---|---|
| [`tdr/`](tdr/) | Consequential decision — the unit of judgement | TDR | Admitted |
| [`vr/`](vr/) | Operational Value Commitment (OVC) — the unit of intended value | Value Record | Admitted |

## What a package contains

| File | Purpose |
|---|---|
| `README.md` | Manifest — the object, its canonical spec, schema and template, and the skills that draft and challenge it |
| `semantic-roles.md` | The roles a contribution may target, which are mandatory for a candidate, and which belong to which lifecycle moment |
| `admission.md` | The record-specific admissibility test, applied on top of the shared invariants |

## The extension contract

A new record package plugs in without modifying any interpretation skill, any interchange structure, or
any existing package. To add one:

1. Supply the three files above.
2. Name the object with a lowercase-kebab identifier and the record type with an uppercase one, matching
   the patterns in [`shared/schema/record-contribution.schema.json`](../shared/schema/record-contribution.schema.json).
   The patterns are open rather than enumerated **precisely so that a package can be added without a
   schema change**.
3. Add the canonical spec, schema and template at the repository root, following existing convention.
4. Add `draft-<record>` to [`skills/`](../skills/). `identify-record-contributions`,
   `reconcile-record-fragments`, `challenge-record` and `validate-record` need no modification — they
   read the package.
5. Record the decision in [`decisions/`](../decisions/), per `CONTRIBUTING.md`.

`challenge-record` and `validate-record` are deliberately one skill each rather than one per record
type. Structural failures — unsupported interpretation, missing mandatory semantics, provenance gaps,
unresolved conflict — are common to every record; only the role list and the admission test differ, and
both load from the package. This is what stops skill proliferation as further records arrive.

## What is not here, and why

Authority (OAR), Inheritance (OIR), Evidence (OER), Participant and Mandate are **not packages in this
release**. Their status as persistent records remains an open research question, and creating a
directory for each would settle by convention what has not been settled by evidence — the failure the
standard's own supersession discipline exists to prevent.

The contract above deliberately leaves room for any that later qualify. Nothing in this release has to
change to admit them.

---

*Admitted by [TDR-0018](../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md).*
