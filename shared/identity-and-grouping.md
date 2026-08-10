# Identity and grouping

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

## The one rule

**Proximity is never identity.**

Deciding that six contributions from six documents concern *one* commitment is the hardest judgement
in interpretation, and the one with the worst failure mode. A wrong merge produces a coherent,
well-provenanced record of an object that never existed — and it is indistinguishable from a correct
one by inspection.

The admissible grouping bases are listed in
[`candidate-assembly.md`](candidate-assembly.md#admissible-grouping-bases). This file covers how to
apply them.

## The procedure

1. **Start from separate.** The default is that two contributions concern different objects. Grouping
   is a claim that must be evidenced; separation is not.
2. **Find an admissible basis, and name the evidence for it.** Not the basis type alone — the actual
   identifier, the actual cross-reference, the actual named owner.
3. **Look for disconfirming evidence before accepting.** Different beneficiaries, incompatible
   baselines, different authority lineages, overlapping-but-inconsistent measures. **Actively seek the
   reason these are two things.** A grouping that has not been tested against its own negation has not
   been tested.
4. **Grade the result** as `assembly_confidence`, and record what would change it.
5. **Where the evidence does not settle it, do not settle it.** Two candidates, or one candidate with
   the question in `unresolved`, are both better than a confident merge.

## Semantic similarity is the weakest signal

Two value commitments in one programme will describe similar benefits in similar language, because
they were written by the same people to the same template. Similarity is therefore evidence of shared
*context*, which is exactly what proximity already told you, and it is close to worthless as evidence
of shared *identity*.

Structural signals are stronger, roughly in this order: explicit cross-reference, shared identifier,
shared authority lineage, shared named owner for the same subject, documented temporal sequence.

## Temporal context changes the question

Contributions separated in time may be:

- the same object, restated
- the same object, **superseded** — a changed value under the same authority lineage
- **different objects**, where a later commitment replaced an earlier one as an organisational act
  rather than as an amendment

These are genuinely different findings and the evidence that distinguishes them is authority lineage
plus explicit reference, not date order. Date order alone supports none of the three — see
[`temporal-semantics.md`](temporal-semantics.md).

## Identity claims are revisable

An assembly is a proposal, and its grouping is part of the proposal. A ratifying human may split one
candidate into two, or merge two into one, and that is the system working. What must not happen is the
merge being invisible — which is why `grouping_basis` is required rather than optional.

## Anti-patterns

- **Merge by folder** — everything in one directory treated as one object.
- **Merge by embedding distance** — similarity scored, threshold applied, basis unrecorded.
- **Merge to reduce the count** — collapsing candidates because a long list looks like failure. A long
  list of honest candidates is a better result than a short list of invented ones.
- **The unfalsifiable grouping** — a basis recorded so vaguely ("related programme work") that no
  reader could disagree with it.
- **Grouping before extraction is complete** — deciding identity from the first two contributions, then
  fitting later ones to it.
