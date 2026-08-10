# Uncertainty

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

## The one rule

**Three uncertainties, never collapsed into one.**

A model can be entirely confident that a document says "£10m saving" while the evidence for the £10m
being real is very weak. Those are different facts about different things, and a single score cannot
carry both without destroying the more important one.

| Dimension | The question it answers | Where it lives |
|---|---|---|
| `extraction_confidence` | Did I read these words correctly? | [`RecordContribution`](record-contribution.md) |
| `assembly_confidence` | Do these contributions concern the same object? | [`CandidateAssembly`](candidate-assembly.md) |
| `epistemic_confidence` | How strong is the underlying evidence for the claim? | [`RecordContribution`](record-contribution.md) |

Each uses the standard's existing ladder — `low` · `medium` · `high` — so that values remain
comparable with the `confidence` field defined in [`spec.md`](../records/decision/specification/tdr.md) §4.1. The ladder is shared;
the semantics are not.

## Why they must stay apart

The three fail independently, and each failure needs a different response:

- **Low extraction, high epistemic** — the source is strong but ambiguously worded. Response: read
  more carefully, or reference more fragments.
- **High extraction, low epistemic** — the source states a number plainly, and the number is
  unsupported. Response: record it as claimed, and let the challenge skill surface it. **This is the
  common case in business cases and benefit claims**, and the one a merged score hides.
- **High extraction, high epistemic, low assembly** — every reading is sound, and it is not clear they
  concern the same commitment. Response: do not merge. Report two candidates, or one candidate and an
  unresolved question.

Merged into a single score, all three become "medium", which tells a ratifying human nothing about
what to check.

## Confidence is not probability

The ladder is a judgement, not a calibrated likelihood. Skills must not present it as one, must not
compute arithmetic over it, and must not average the three dimensions into a composite. A composite
score would recreate exactly the collapse this file exists to prevent.

## Uncertainty never resolves itself

A candidate does not become more certain because it has been carried forward, restated, or agreed
verbally. Only new evidence changes `epistemic_confidence`; only a better reading changes
`extraction_confidence`; only a stronger grouping basis changes `assembly_confidence`.

## Anti-patterns

- **The composite score** — one number standing for all three, usually the mean, usually "medium".
- **Confidence inflation on restatement** — the same claim appearing in three documents treated as
  three pieces of evidence, when it is one claim copied twice.
- **Precision theatre** — `0.87` where the standard defines three levels, implying calibration that
  does not exist.
- **Confidence as hedge** — marking everything `medium` so nothing is ever wrong, which makes the
  field carry no information at all.
