# Interoperability

The horizon test of [`specification/conformance.md`](../../specification/conformance.md): given the
same source corpus, can independent implementations recognise materially equivalent contributions and
produce semantically equivalent candidate records?

[`protocol/`](protocol/) holds the **frozen, pre-registered method** for answering that — currently at
**version 1.1.1**. A documented divergence is a successful run with a finding, not a failure
([TDR-0025](../../decisions/TDR-0025-conformance-architecture.md)).

## Why the method is here before any result is

A protocol published *after* the runs is a method written with the results already known, whatever the
intention. The sequence is therefore fixed:

> design → synthetic falsification → **freeze** → **publish** → execute → observe

This directory holds the freeze. **Nothing has been executed against it.** Its commit hash is recorded
in every subsequent run as `protocol_commit`, and a capture whose pin does not match it is rejected
rather than compared. That is what makes the discipline checkable rather than self-reported: if
something surprising happens, it can be shown that neither the method nor the comparator was changed
afterwards to accommodate it.

### A defect increments the protocol; the freeze is never overwritten

If a defect is found after execution, the frozen protocol is **not edited**. `protocol_version`
increments, a new protocol is pre-registered at a new commit, and every participant re-runs under the
new pin. **The earlier runs stay valid** — as evidence of what the defective protocol produced, which
is itself a result. Discarding them would leave no record that the defect existed. This is
supersession rather than correction: the same discipline this standard applies to its own records.

Version 1.1.0 is that mechanism exercised. 1.0.0 was pre-registered; then a canonical
`environment_digest` normalisation rule and a comparator pin were added. Rather than edit the freeze,
it was incremented and re-registered. No participant had run under 1.0.0, so nothing needed
re-running — but the 1.0.0 freeze remains in this repository's history either way.

1.1.1 is the same mechanism applied to a change small enough to be tempting to wave through:
`PROTOCOL.md` was clarified after the 1.1.0 freeze — a comparator pin described as binding when it is
a starting pin. Editorial, changing no rule. The drift was detected mechanically and answered with an
increment rather than a quiet edit, because **treating a change as too small to increment is how a
freeze stops meaning anything.**

## The proposition under test

> Given the same closed evidence set, the same frozen MTDR specification and skills, and a
> pre-registered reconstruction protocol, independent reasoning environments can reconstruct
> materially equivalent governed organisational state — **while preserving uncertainty, and exposing
> rather than concealing divergence.**

Three clauses, and the last two are not decoration. A run that converges by resolving an uncertainty
the sources leave open has failed the proposition, not confirmed it.

**Failure is a valid result, and possibly the more valuable one.** If the proposition does not hold,
the boundary-level captures say *where* it stops holding — and that would tell this standard more than
a clean convergence could.

## What is non-normative here, and stays that way

Everything in [`protocol/`](protocol/). Two of its contracts are the benchmark's own:

| Contract | |
|---|---|
| [`source-selection.schema.json`](protocol/source-selection.schema.json) | the one boundary MTDR does not already contract |
| [`capture.schema.json`](protocol/capture.schema.json) | the envelope composing the seven public contracts |
| [`environment-keys.yaml`](protocol/environment-keys.yaml) | what the environment digest covers, what it excludes, and how it is normalised |

Neither migrates into the normative schema tree, however useful it proves. **Only a TDR admits a
concept into MTDR**, argued on its own merits — not a promotion earned by a benchmark finding it
handy. The experiment consumes and tests this standard; it does not expand it. If a runtime struggles
with MTDR, that is initially evidence about the runtime, the instructions or the proposition — not
permission to modify the standard until it passes.

## The eight boundaries

Comparison happens at every boundary, not at final-record similarity. Two implementations can land on
similar candidates for different reasons, and final-record comparison misses exactly that.

> source selection → fragment → contribution → assembly → candidate → derivation projection →
> validation → eligibility

Seven of the eight already have public machine contracts, which is why the comparison is possible with
almost no new contract surface:

| Boundary | Contract | Layer |
|---|---|---|
| source selection | [`protocol/source-selection.schema.json`](protocol/source-selection.schema.json) | benchmark |
| fragment | [`schemas/shared/source-fragment.schema.json`](../../schemas/shared/source-fragment.schema.json) | MTDR |
| contribution | [`schemas/shared/record-contribution.schema.json`](../../schemas/shared/record-contribution.schema.json) | MTDR |
| assembly | [`schemas/shared/candidate-assembly.schema.json`](../../schemas/shared/candidate-assembly.schema.json) | MTDR |
| candidate | [`records/value/schema/vr.schema.json`](../../records/value/schema/vr.schema.json) · [`records/decision/schema/tdr.schema.json`](../../records/decision/schema/tdr.schema.json) | MTDR |
| derivation projection | [`schemas/shared/derivation-projection.schema.json`](../../schemas/shared/derivation-projection.schema.json) | MTDR |
| validation | [`schemas/validation-result.schema.json`](../../schemas/validation-result.schema.json) | MTDR |
| eligibility | the fourth dimension of the validation result, captured separately because it is the boundary that matters most | MTDR |

Captures are validated in **two named layers**, and a report says which one failed. An MTDR contract
failure means an implementation emitted a non-conformant artefact — a finding about that
implementation. A benchmark protocol failure means it failed to *report* properly — a rejected run.
Collapsing the two would let a harness defect read as a conformance failure, or worse, the reverse.

## Calibration corpus

[`tests/adoption/brackwell/`](../adoption/brackwell/), against the known answer in
[`FIX-301`](../adoption/FIX-301-brackwell-reconstruction.md). It is the **current** known-answer
calibration case, not a uniquely privileged one; several corpora exercising different failure modes
would be better than one, and the method takes the corpus as a parameter for that reason.

Calibration does not mean identical outputs. **A shared gap is a correct answer, and convergence on a
value where FIX-301 requires a gap is a worse result than divergence.**

## Reproducing a run

You need a checkout of this repository at the pinned commit, the corpus, and
[`protocol/task.md`](protocol/task.md) — whose sha256 is a pin, byte-identical for every participant.
Emit one capture conforming to [`protocol/capture.schema.json`](protocol/capture.schema.json).

The comparison is deliberately **categorical**: signature sets per boundary, built from referents
rather than labels, with **every pairing of participants in its own column**. There is no similarity
score, because a number there would be an unjustified one — and a single aggregate cross-participant
column would hide the case where two agree and one differs, which is the asymmetry most worth
knowing. The participant standing alone is **named**, and that naming is descriptive: nothing in the
comparison lets the count of agreeing participants reach a decision.
Divergences are classified, and every classification carries a `basis` and `evidence` pointing at the
fixture or the source material — **never at how many participants agreed**. Agreement between
implementations is not evidence about the organisation.
