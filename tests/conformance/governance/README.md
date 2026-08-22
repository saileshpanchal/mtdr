# Governance conformance

**Status:** proposed under [TDR-0034](../../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md).
Not accepted, and carrying no standing.

Behavioural conformance for the [governance skills](../../../records/decision/skills/governance/) —
a **participant execution** claim under
[TDR-0032](../../../decisions/TDR-0032-typed-multi-object-conformance.md), separate from the artefact
conformance that [`verify.py`](../../verify.py) establishes. A conforming skill file does not imply
conforming execution.

| Holds | |
|---|---|
| [`governance-probes.md`](governance-probes.md) | AT-01 to AT-13 — what a conforming run must produce, and must not |
| [`worked-run/`](worked-run/) | One complete run over the fixture estate: the machine-readable projections and the inspectable reports |

These complement the [agent probes](../agent-probes.md), which test a deployed agent's adherence to
the standard's rules generally. These test whether governance reconstruction is faithful.

## Semantic comparison, not byte comparison

`worked-run/` is a **reference run**, not an expected output. A model-executed skill will not reproduce
its prose, its ordering or its phrasing, and a probe demanding that would be testing text generation
rather than reconstruction.

The distinction is deliberate and follows the two-layer split
[`conformance.md`](../../../specification/conformance.md) already draws:

- the **JSON is deterministic** — every projection validates against
  [`governance-projection.schema.json`](../../../records/decision/schema/governance-projection.schema.json)
  exactly, and `verify.py` check 10 enforces it plus the claim-reference resolution;
- the **execution is tested by invariants** — the seven listed in AT-01, and each probe's own
  Pass and Must-not sections.

## All material here is fictional

Kingsmere Bank plc, Project Ashcombe and every individual named are invented, per
[`CONTRIBUTING.md`](../../../CONTRIBUTING.md).
