# Conformance

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

What it means to conform to this standard — for a record, for an implementation, and for the standard
itself. Decided in [TDR-0025](../decisions/TDR-0025-conformance-architecture.md).

## Schema validation is the floor, not the test

A standard is not open because its markdown is on GitHub. It is open when independent implementations
can produce the same **meaning** — and schema validation cannot test meaning. The two failures that
matter most both validate perfectly: the confident invention (a value with no evidence behind it) and
the silent merge (two commitments recorded as one). A conformance model that stops at the schema
certifies exactly the records it should be catching.

## The layered surface

Each **mature** record package carries all seven layers. A package's maturity is measured by which
layers it actually has — a candidate package ([`record-admission-test.md`](record-admission-test.md))
carries none until admitted.

| Layer | What it establishes |
|---|---|
| **Specification** | The semantics, humanly argued |
| **Machine-readable schema** | Well-formedness, mechanically |
| **Normative examples** | What conforming records look like |
| **Counter-examples** | What must *not* happen — material that yields no record, merges that must not occur |
| **Conformance fixtures** | Known-answer tests with expected **and must-not** sections |
| **Validation rules** | The deterministic checks beyond the schema — lineage resolution, legal transitions, identifier agreement |
| **Portable skills** | The lifecycle applied — so conformance is exercised, not just described |

**A fixture without a must-not section is a non-conforming fixture.** Producing the right candidate
by the wrong route — filling a gap that happens to be correct, merging on similarity where the
identifiers also agreed — will be wrong and undetectable on real material, and only the must-not
section catches it.

Cross-language fixtures, the agent probes and the shared corpus live in [`tests/`](../tests/),
outside every package, because a package may never depend sideways on another.

## The horizon test

Stated now, not yet passable, and the reason the corpus exists:

> Given the same source corpus, can independent implementations recognise materially equivalent
> contributions and produce semantically equivalent candidate records?

**Semantically equivalent** is deliberately weaker than byte equality and stronger than schema
validity. Span boundaries, phrasing and fragment counts may differ between implementations. What may
not differ: the objects identified, the semantic roles assigned, the groupings made and refused, the
gaps reported, and the conflicts recorded. Two implementations that disagree on any of those are not
both conforming, whatever their schemas say.

## Conformance of what, exactly

- **A record** conforms to its specification version — the one it was raised under, never a later one
  retroactively ([`records/value/specification/vr.md`](../records/value/specification/vr.md) §8 is the
  worked precedent).
- **An implementation** conforms by passing the fixtures — expected and must-not — for the packages it
  claims, plus the shared corpus.
- **The repository itself** conforms by keeping this file honest: every maturity claim checkable
  against a package's actual contents, every release's compatibility claim verified rather than
  asserted.
