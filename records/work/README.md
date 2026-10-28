# Package — Work · EXPERIMENTAL

**Language:** work · **Primary record:** `OIR` — the Operational Inheritance Record
**Status:** `experimental` under [TDR-0047](../../decisions/TDR-0047-experimental-packages.md) ·
**Admission:** not passed

> **This package is not part of the MTDR standard.** It is published for open review so that the
> evidence deciding whether it should exist can be gathered in the open. It is excluded from the
> standard's skill totals, from its distribution bundles, and from every conformance and release claim.
> No adopter conforms to MTDR by using it, and none fails to by ignoring it.

## The question it exists to answer

> **What organisational state must a participant inherit before performing operational work?**

Participants change — people, teams, suppliers, software, AI. The work, and the state built up around
it, persists. The OIR describes the work and that state, never the worker:
[`specification/oir.md`](specification/oir.md).

## The question it exists to be judged by

Whether the OIR is **native organisational state** — something lost when it is removed — or a **useful
projection** over the decision, value, authority and evidence records an organisation already keeps.
That is decided by a deletion attack pre-registered, and frozen, **before this package was built**:
[TDR-0046](../../decisions/TDR-0046-oir-experiment-preregistration.md). The package cannot change the
test; the suite refuses any edit to it.

Either answer is a legitimate result. A projection outcome identifies a useful way of making existing
organisational knowledge available to successors.

## What is here

| Layer | Path |
|---|---|
| Specification | [`specification/oir.md`](specification/oir.md) · recovery vocabulary [`specification/inheritance-contribution.md`](specification/inheritance-contribution.md) |
| Schema | [`schema/oir.schema.json`](schema/oir.schema.json) — every clause carries a source marker |
| Template | [`templates/oir.md`](templates/oir.md) |
| Example (fictional) | [`examples/example-oir-payment-exceptions.md`](examples/example-oir-payment-exceptions.md) |
| Fixtures | [`fixtures/`](fixtures/) — expected and must-not |
| Validation | [`validation/semantic-roles.md`](validation/semantic-roles.md) · [`validation/admission.md`](validation/admission.md) |

## Bounded against the other languages

A **decision** may reshape what is inherited; a **value commitment** may be what the work pursues; an
**authority** instrument may delegate what a participant may do. The OIR references each by identifier
and restates none of them. JTBD is the job grammar *within* this scope — it is not a separate language
and creates no record of its own.
