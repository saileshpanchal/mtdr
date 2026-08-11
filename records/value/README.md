# Package — Value

**Language:** value · **Object:** `ovc` — the Operational Value Commitment, the unit of intended value
**Primary record:** `VR` — Value Record · **Status:** Normative (specification v2.0.0)

The value language: the record that preserves what the organisation committed to pursue or preserve,
for whom, under what authority, and how the commitment settled. The object is the commitment; the
record is its governed memory. *Operational Value Record* and *OVR* are deprecated drift names,
retained only in migration and alias tests.

## Contents

| Artefact | Location |
|---|---|
| VR specification (v2.0.0) | [`specification/vr.md`](specification/vr.md) |
| Recovery vocabulary — contribution classes, boundaries, the completeness view | [`specification/value-contribution.md`](specification/value-contribution.md) |
| Schema | [`schema/vr.schema.json`](schema/vr.schema.json) |
| Template | [`templates/vr.md`](templates/vr.md) |
| Worked example | [`examples/example-value-record-practice-skills.md`](examples/example-value-record-practice-skills.md) |
| Conformance fixtures | [`fixtures/`](fixtures/) — 15 fixtures across six value classes and three recovery conditions; see [`fixtures/README.md`](fixtures/README.md) |
| Semantic roles (interpretation) | [`validation/semantic-roles.md`](validation/semantic-roles.md) |
| Admissibility test | [`validation/admission.md`](validation/admission.md) |

The specification governs wherever an overlay appears to differ from it.

## The load-bearing semantics

**The commitment is an accountable pursuit, not a prediction** — the record never claims an outcome
will occur. **`beneficiary` is identity-bearing**: two commitments differing only in whose outcome is
pursued are two commitments, and FIX-003 demonstrates why. **Two independent state axes**: `status`
(`candidate → ratified → settled → superseded`) is what is known about the record; `realisation`
(`not-started → observing → realised | partially-realised | not-realised | attribution-unresolved |
written-off`) is what is known about the value. **Measurement is not attribution** — an observed
movement is never evidence that this commitment caused it, and `attribution-unresolved` is a
legitimate settlement. The **counterfactual is deliberately optional** (spec §5.2); its absence is
never reported as a gap and never inferred.

## Skills

**Authoring path**: [`value-record`](skills/value-record/) — raise, ratify and settle with a human
who holds the commitment.

**Interpretation path** — the full value lifecycle, each skill carrying this language's semantics
over the shared mechanics ([TDR-0023](../../decisions/TDR-0023-portable-skill-architecture.md)):
[`identify-value-contributions`](skills/identify-value-contributions/) →
[`reconcile-value-contributions`](skills/reconcile-value-contributions/) →
[`draft-value-record`](skills/draft-value-record/) →
[`challenge-value-record`](skills/challenge-value-record/) →
[`validate-value-record`](skills/validate-value-record/) → human ratification.

**Entry point**: [`recover-value-records`](skills/recover-value-records/) — the composition skill
that runs the lifecycle end to end and reports candidates, unknowns, conflicts and unclassified
material. It orchestrates and decides nothing; every rule lives in the stage skill it belongs to.

One record, two routes to it. Value is the first package to carry the full lifecycle — the proving
case for the skill architecture; further languages inherit the pattern after admission.
