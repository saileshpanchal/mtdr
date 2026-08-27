---
id: TDR-0019
conforms_to: mtdr/decision/tdr@1.15.0
title: Value Record v2 — specify the Operational Value Commitment, and separate epistemic state from value state
status: accepted
template: full
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: medium
maturity: proposed
supersedes: none
derived_from: TDR-0008, TDR-0018
confirmed_by_outcome: pending — review when a v2 Value Record has been ratified and settled by an organisation other than the author, or 2027-02-10, whichever is sooner
---

# TDR-0019 — Value Record v2: specify the Operational Value Commitment, and separate epistemic state from value state

## Context — what was known at the time

`spec-value-record.md` had stood at 1.3.0 through twelve releases — the only specification in the repository that had not moved since it shipped. Its footer claimed it "versions with `spec.md`", which had been true at 1.3.0 and false ever since.

Two things arrived to change that.

**The commitment/record distinction settled.** The organisational object is an **Operational Value Commitment**; the Value Record is its governed memory. This parallels consequential-decision and TDR exactly. "Operational Value Record" and "OVR" are drift names for the same record, and there is no second value primitive — that question was looked at and closed.

**The interpretation work put the semantics under test.** TDR-0018 admitted skills that reconstruct records from organisational material, and the Value Record package encoded candidate OVC semantics experimentally as roles a contribution could target. One of those roles then justified itself empirically: `conformance/FIX-003` supplies two workstream benefits identical in value, baseline, measurement source, wording, author and document, differing only in who the benefit is for. **The beneficiary clause is the only signal separating them.** Any grouping driven by similarity merges them, producing a coherent, fully evidenced record of a commitment that does not exist.

Two defects were visible by then.

The specification had no field for `beneficiary` at all, so the package required a role the record could not carry.

And the `status` enum — `proposed | agreed | realising | reconciled | written-off` — conflated two independent questions. `proposed` and `agreed` describe what is known about **the record**; `realising`, `reconciled` and `written-off` describe what is known about **the value**. A single field cannot say the two most useful things a value record can say: that a commitment is properly ratified and its value has not arrived, or that an outcome has been observed and nobody can yet say the commitment caused it.

**This is not a redesign of value.** It is the specification catching up with semantics already discovered, and already encoded experimentally in the record package.

## Decision

1. **The Value Record represents an Operational Value Commitment, whose semantic centre is an accountable pursuit — not a prediction.** The record does not claim an outcome will occur; it records that a named person committed the organisation to pursuing or preserving one. A commitment can be honoured and the outcome not arrive; a commitment can be abandoned and the outcome arrive anyway. Neither makes the record wrong.
2. **Eight semantic roles** identify a commitment: *Under · Who commits · For whom · We commit · From · To · By · We will know.* They are **roles to be inferred, not a mandatory sentence grammar** — no record is required to phrase itself this way, and real material almost never does.
3. **`beneficiary` is required and participates in commitment identity.** Not descriptive metadata. A commitment whose beneficiary is unstated is not identifiable.
4. **Two state axes, separated**: `status` (`candidate → ratified → settled → superseded`) records what is known about the record; `realisation` (`not-started → observing → realised | partially-realised | not-realised | attribution-unresolved | written-off`) records what is known about the value.
5. **Evidence is of three kinds — existence, observation, attribution — and is labelled by kind.** Measurement is not attribution. `attribution-unresolved` is a legitimate settlement, not an incomplete one.
6. **Consequential change supersedes.** A change to beneficiary, intended outcome, timing, funding or protected value changes *what was committed to* and requires a superseding record. Revising a measurement method or baseline source is an in-place lifecycle fact.
7. **The counterfactual question is left explicitly open.** A commitment is admissible without an explicit counterfactual. What its absence may prevent is a defensible claim about *incremental* value or attribution — a different thing, preserved as a distinction rather than resolved by making counterfactual reasoning mandatory because it makes value calculation tidier.
8. **v2.0.0 is a breaking change, and the VR specification versions independently of `spec.md`.** Records raised under v1 remain valid v1 records, are not retrospectively invalid, and are superseded by a v2 record when materially changed. The specification carries the v1-to-v2 status mapping.

### The causal chain this record sits in

```
organisational material → fragments → candidate OVC → Value Record
    → authorised ratification → observed outcomes → Value Realisation
```

The standard defines the record and the skills needed to produce and conform it. **It has no knowledge of what consumes those records, what reasoning system uses them afterwards, or how value realisation is subsequently tracked** — that boundary is TDR-0018's, and this record does not move it.

## Evidence

- **Business** — benefits practice fails at settlement, not at claiming. The three-kinds-of-evidence split and `attribution-unresolved` address the failure directly: an organisation that must record every observed movement as claimed or discarded learns nothing about its own attribution.
- **Architecture** — separating the state axes removes an ambiguity that no downstream consumer could have resolved from the record. A single enum forced any reader to guess which question a value answered.
- **Regulatory** — not material to the field set. Material to `committed_by`: an organisation asked who bound it to a benefit must be able to answer with a person, and the v1 record had no field that asked.
- **Operations** — the package already required `beneficiary` as a role, so implementations following the interpretation path were already capturing it with nowhere to put it. The change closes a gap that existed in practice before it existed in the specification.
- **Customer** — `beneficiary` makes explicit whether a benefit accrues to the organisation or to its customers. FIX-003's two commitments differ on exactly this, and the distinction was previously unrecordable.
- **Data** — a required `beneficiary` makes commitment identity computable rather than inferential, which is what the grouping discipline in `shared/identity-and-grouping.md` needs to be checkable.
- **External** — conventional benefits-realisation frameworks treat attribution as resolved by measurement. Departing from that is deliberate and is the substance of §5.

## Alternatives rejected

1. **Leave `beneficiary` in the package only.** Rejected: the package would require a role the record cannot carry, so a conforming candidate could never become a conforming record. The gap has to close in the specification or not at all.
2. **Add `beneficiary` as optional.** Rejected: FIX-003 shows it is the only signal separating two commitments in the case where separation matters most. Optional identity is not identity.
3. **Keep one `status` enum and add values.** Rejected: the two axes are genuinely independent, and every added value would have to encode a pair. `ratified-but-not-arrived` is not a state; it is two states badly compressed.
4. **Make the counterfactual mandatory.** Rejected — the tempting option, because it makes incremental value calculable. It would force organisations to manufacture counterfactual reasoning at commitment time to satisfy a field, which produces exactly the confident fiction the standard exists to prevent. The distinction between an admissible commitment and a defensible incremental claim is worth keeping.
5. **Resolve the counterfactual question in the other direction — say it is never required.** Rejected: that is equally a settlement, and the evidence does not support one. The question is recorded as open.
6. **Ship as a minor version and claim backward compatibility.** Rejected as untrue. New required fields break prior records. Every release in this repository has asserted "every prior record still validates", and asserting it here would make the claim worthless everywhere it appears.
7. **Retrospectively invalidate v1 records.** Rejected: a record states what was true when written. v1 records remain valid v1 records, exactly as the supersession discipline requires.
8. **Rename the record to Operational Value Record / OVR.** Rejected: OVR is a drift name for this record, not a second primitive, and adopting it would re-open a closed question and strand every existing reference.

## Options foreclosed

- The Value Record can no longer be raised without naming who the value is for, or who committed the organisation. Both are deliberate one-way doors.
- A future version cannot recombine the state axes without superseding this record.
- Attribution can never be satisfied by measurement alone within this standard.
- The specification is now explicitly on its own version line; it cannot be re-coupled to `spec.md` without a superseding record.

## Consequences and review

Success looks like a v2 Value Record ratified and later settled by an organisation other than the author — and, more tellingly, at least one settled as `attribution-unresolved` rather than forced to a verdict.

Confidence is **medium**, for two reasons stated plainly. The counterfactual question is unresolved by design, and a specification carrying an open question at its centre may prove harder to apply than one that answers it badly. And `beneficiary` as an identity-bearing field is justified by a constructed fixture rather than by field evidence; FIX-003 is a strong argument but it is one the author built.

Review when a v2 record has been ratified and settled outside the author's own practice, or 2027-02-10. Absent that evidence, the deferral on counterfactual stands and this record is superseded only to say so.
