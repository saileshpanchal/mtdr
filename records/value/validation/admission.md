# Value Record — admissibility test

Applied on top of the shared invariants in
[`shared/candidacy-and-ratification.md`](../../../specification/candidacy-and-ratification.md). Admissibility
asks whether a candidate is **worth putting in front of a named owner** — not whether the value claim is
true, and not whether the commitment was wise.

## The test

A candidate commitment is admissible when all of the following hold.

1. **A commitment is present, not an aspiration.** The material evidences something the organisation
   undertook to **pursue or preserve** — not a benefit someone hoped for in a slide. The commitment is an
   accountable pursuit; it is not a prediction that the outcome will occur, and a candidate must not be
   rejected for failing to promise one.
2. **A beneficiary is evidenced.** Without it the commitment is not identifiable, and a candidate that
   cannot be identified cannot be safely grouped or superseded. This is the one mandatory role whose
   absence blocks admission outright rather than being reported as a gap.
3. **A decision is linked.** A value claim floating free of any decision is a forecast, not a record.
4. **Commitment and reconciliation roles are not mixed.** An `observed-outcome` contribution never sits
   in a commitment role, however early in the material it appears.
5. **Attribution is not asserted from measurement.** A candidate carrying `attribution-basis` supported
   only by an `observed-outcome` span is inadmissible. The two require different evidence.
6. **Provenance is complete**, and the `baseline` contribution carries its measurement date and source.
7. **The grouping basis is admissible**, where the candidate draws on more than one source — and was
   tested *after* reading the beneficiary, not before.
8. **Missing mandatory roles are reported, not filled.**

## Why beneficiary is the one blocking absence

Every other missing role produces an incomplete but still useful candidate. A missing beneficiary
produces a candidate that **cannot be told apart from a different commitment**, which makes every
downstream grouping, supersession and settlement decision unsafe.

[`conformance/FIX-003`](../fixtures/FIX-003-two-commitments-not-one.md) is the demonstration: two
workstream benefits identical in value, baseline, source, wording, author and document, separable only
by beneficiary. Admit either without it and the register acquires a commitment that does not exist.

## Inadmissible

- No `beneficiary`.
- An expected value with no `baseline`.
- A commitment with no `falsifying-signal` — a claim that cannot fail is not a claim.
- `finance_countersignatory` or `committed_by` set to a committee, a function, or "Finance".
- Attribution language carried over from source material that only measured something.
- A candidate merging two commitments on programme membership or similarity of wording.
- Any `status` other than `candidate`, or any `realisation` other than `not-started`.

## Admissible but incomplete — the normal case

Commitment candidates assembled from real material are usually missing the falsifying signal, the
counter-signatory, the authority, or all three. **Report them.** These gaps are the most valuable output
this package produces, because each names a reason the benefit was never going to be settled — and they
are invisible until someone assembles the commitment whole.

## The counterfactual is not a gap

A commitment is admissible without an explicit counterfactual (`spec-value-record.md` §5.2). Its absence
must **not** be reported as a missing semantic, and must never be inferred.

What the absence may prevent is a defensible claim about *incremental* value or attribution at
settlement. That is a different question, arising later, and this test does not anticipate it.

## The settlement states

At settlement, the honest outcomes are:

- **realised** — outcome observed, attribution evidenced
- **partially realised** — outcome observed in part, attribution evidenced for that part
- **not realised** — outcome not observed
- **attribution unresolved** — **outcome observed, attribution not evidenced**
- **written off** — declared, signed, and stating what was learned

The fourth is not a failure of the process. It is frequently the truthful answer, and a standard that
cannot express it forces every observed movement to be claimed or discarded. Interpretation must never
resolve it by inference.

## What this test does not do

It does not assess whether the value claim is **credible**, whether the baseline is **well-chosen**, or
whether the expected value is **realistic**. Those are challenges to the claim, and belong to
[`challenge-record`](../../../skills/shared/challenge-record/) and to the human counter-signature the
specification requires. Admissibility asks only whether the evidence supports proposing this commitment
to a named person.
