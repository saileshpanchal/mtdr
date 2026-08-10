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
| Schema | [`schema/vr.schema.json`](schema/vr.schema.json) |
| Template | [`templates/vr.md`](templates/vr.md) |
| Worked example | [`examples/example-value-record-practice-skills.md`](examples/example-value-record-practice-skills.md) |
| Conformance fixtures | [`fixtures/`](fixtures/) — FIX-001 (six-source assembly) · FIX-003 (proximity is never identity) |
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

**Interpretation path**: the shared
[`identify-record-contributions`](../../skills/shared/identify-record-contributions/) and
[`reconcile-record-fragments`](../../skills/shared/reconcile-record-fragments/), then
[`draft-vr`](skills/draft-vr/) here, then the shared
[`challenge-record`](../../skills/shared/challenge-record/) and
[`validate-record`](../../skills/shared/validate-record/).

One record, two routes to it. The full per-value lifecycle skill set — identify · reconcile · draft ·
challenge · validate as value-specific skills — is this package's next planned increment, proving the
skill architecture with Value as the first case.
