# Value Record — admissibility test

Applied on top of the shared invariants in
[`shared/candidacy-and-ratification.md`](../../shared/candidacy-and-ratification.md). Admissibility
asks whether a candidate is **worth putting in front of a named owner** — not whether the value claim is
true.

## The test

A candidate commitment is admissible when all of the following hold.

1. **A commitment is present, not an aspiration.** The material evidences something the organisation
   undertook to pursue or preserve — not a benefit someone hoped for in a slide.
2. **A decision is linked.** `linked-decision` is evidenced. A value claim floating free of any decision
   is a forecast, not a record, and interpretation does not get to relax that.
3. **Commitment and reconciliation roles are not mixed.** An `observed-outcome` contribution never sits
   in a commitment role, however early in the material it appears.
4. **Attribution is not asserted from measurement.** A candidate carrying `attribution-basis` supported
   only by an `observed-outcome` span is inadmissible. The two require different evidence.
5. **Provenance is complete**, and the `baseline` contribution carries its measurement date and source.
6. **The grouping basis is admissible**, where the candidate draws on more than one source. Value
   commitments are the case where wrong merges are most likely and most damaging — two benefits in one
   programme will describe themselves in near-identical language.
7. **Missing mandatory roles are reported, not filled.**

## Inadmissible

- An expected value with no `baseline`.
- A `value-thesis` with no `falsifying-signal` — a claim that cannot fail is not a claim.
- `finance_countersignatory` set to a committee, a function, or "Finance".
- Attribution language carried over from source material that only measured something.
- A candidate merging two commitments on programme membership or similarity of wording.
- A status beyond `proposed`.

## Admissible but incomplete — the normal case

Commitment candidates assembled from real material are usually missing the beneficiary, the falsifying
signal, the counter-signatory, or all three. **Report them.** These gaps are the most valuable output
this package produces, because each one names a reason the benefit was never going to be reconciled —
and they are invisible until someone tries to assemble the commitment as a whole.

## The settlement states

At reconciliation, the honest outcomes are:

- **realised** — outcome observed, attribution evidenced
- **partially realised** — outcome observed in part, attribution evidenced for that part
- **not realised** — outcome not observed
- **attribution unresolved** — **outcome observed, attribution not evidenced**

The fourth is not a failure of the process. It is frequently the truthful answer, and a standard that
cannot express it forces every observed movement to be claimed or discarded. Interpretation must never
resolve it by inference.

## What this test does not do

It does not assess whether the value claim is **credible**, whether the baseline is **well-chosen**, or
whether the expected value is **realistic**. Those are challenges to the claim, and belong to
[`challenge-record`](../../skills/challenge-record/) and to the human counter-signature the
specification already requires. Admissibility asks only whether the evidence supports proposing this
commitment to a named person.
