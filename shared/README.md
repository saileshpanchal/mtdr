# Portable skill interchange structures

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. **Not a record specification.**

These structures exist so that independent skills — and independent agents, possibly from different
vendors — can hand interpretation work to one another predictably. They are the contract between the
skills in [`skills/`](../skills/), nothing more.

## What these are not

Read this before anything else in this directory.

- **They are not organisational records.** A record is governed memory of an organisational object,
  and it carries a named accountable owner. These carry none.
- **They carry no organisational authority.** Nothing here admits anything to organisational truth.
- **They need not be persisted.** They are transient working structures. An adopter who runs an
  interpretation skill, ratifies the candidate and keeps only the resulting markdown file has used
  this standard correctly and completely.
- **They are not peers of the record schemas.** `records/*/schema.json` validates governed artefacts.
  The schemas here validate messages passed between skills. Treating them as equivalent would make
  this repository a standard for mining pipelines, which [TDR-0018](../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md)
  explicitly refuses.

The product of this repository remains a well-formed markdown file conforming to a record
specification, carrying enough provenance to understand how it was derived. Everything here is
scaffolding for producing that file.

## The three levels

```
SourceFragment  →  RecordContribution  →  CandidateAssembly
  (immutable)        (interpretation)       (proposal)
```

| Structure | What it is | File |
|---|---|---|
| **SourceFragment** | A span of organisational material, exactly as found. Evidence. | [`source-fragment.md`](source-fragment.md) |
| **RecordContribution** | An interpretation: this fragment may contribute this semantic value to this object. | [`record-contribution.md`](record-contribution.md) |
| **CandidateAssembly** | A proposal: these contributions appear to concern one object. | [`candidate-assembly.md`](candidate-assembly.md) |

The separation is load-bearing. A structure that carried both the verbatim evidence and the
interpretation of it would make the interpretation unfalsifiable — there would be nothing left to
check it against.

## Objects and their governed memory

Contributions are made to **organisational objects**. Records are how those objects are preserved
portably. The two are not the same thing, and the interchange structures target the object.

| Organisational object | Governed memory |
|---|---|
| Consequential decision | TDR — [`records/tdr`](../records/tdr/) |
| Operational Value Commitment (OVC) | Value Record — [`records/vr`](../records/vr/) |

The question an interpretation skill asks is *"does this fragment contribute to reconstructing an
OVC?"* — not *"does this fragment contain fields for a Value Record?"* The record is the
serialisation; the commitment is the thing being reconstructed.

This is also what makes the contract extensible. A new object and its record package supply their own
semantic roles and admission test; the structures here do not change.

## The cross-cutting concerns

| Concern | Rule it carries | File |
|---|---|---|
| Provenance | Every interpreted value traces to a locatable span | [`provenance.md`](provenance.md) |
| Temporal semantics | When it was true, and when it was recorded, are different | [`temporal-semantics.md`](temporal-semantics.md) |
| Identity and grouping | **Proximity is never identity** | [`identity-and-grouping.md`](identity-and-grouping.md) |
| Uncertainty | Three uncertainties, never collapsed into one | [`uncertainty.md`](uncertainty.md) |
| Candidacy and ratification | The skill proposes; the organisation ratifies | [`candidacy-and-ratification.md`](candidacy-and-ratification.md) |

## The one rule

**No interpreted value exists without a locatable span of source material behind it.** A skill that
cannot point at where something came from has not interpreted it — it has invented it, and the
structures here are designed to make that visible rather than plausible.

## Schemas

[`schema/`](schema/) holds one JSON Schema per structure. As with the record schemas, frontmatter and
messages are validated as JSON: normalise dates to ISO-8601 strings before validating.

---

*Admitted by [TDR-0018](../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md),
which fixes the standard's boundary at the artefact and names these as interchange structures rather
than record types.*
