---
id: VR-0001
title: Shipping practice skills lowers the cost of a first acceptable record
status: ratified
realisation: observing
linked_decisions: TDR-0003
beneficiary: First-time record authors adopting the standard — not the maintainer, and not this repository
committed_by: S. Panchal (maintainer)
authority: TDR-0003, the maintainer's own accepted decision to ship practice skills alongside the specification
value_kind: capacity
finance_countersignatory: S. Panchal (maintainer, acting recognition owner — see note below)
reconcile_by: 2026-10-05
procurement_stage: production
supersedes: none
derived_from: none
---

> **Worked example.** Unlike the fictional TDR examples in this directory, this record references a real decision: [TDR-0003](../../../decisions/TDR-0003-ship-skills-alongside-spec.md), this repository's own decision to ship practice skills alongside the specification. The standard uses itself. **Two fields are adapted, and both weaknesses are the point of showing them.** This repository has no finance function, so the maintainer stands as recognition owner — in an organisation the counter-signatory must be a named individual in finance, distinct from the claimant. And `authority` resolves to the maintainer's own decision, because this repository has no governing body above him; an organisation's authority should trace to something the committer does not themselves control. Raised under [v2.0.0](../specification/vr.md) of the specification.

# VR-0001 — Shipping practice skills lowers the cost of a first acceptable record

## The commitment

The maintainer commits to **pursuing** a reduction in the effort a first-time author spends reaching a record that passes governance review, compared with drafting from the specification alone — for the benefit of first-time authors adopting the standard, under the authority of TDR-0003.

The value kind is capacity: author and reviewer time not spent on returned records. Note what is *not* claimed — that the reduction will occur. The commitment is to pursue it and to settle honestly against the baseline, whichever way it goes.

## Baseline

At 2026-07-05 (v1.0.0), zero of the practice steps — identification, framing, evidence review, governance review — were guided; a spec-only author had only `spec.md` and the templates. Both worked examples drafted at that point required at least one full return at review before the evidence and foreclosure sections held up. Source: this repository's own drafting history.

## Intended outcome and recognition

**Intended outcome:** a first-time author reaches an acceptable record in a single drafting-and-review pass rather than two or more.

**Recognition route:** capacity — review returns per first-time record, observed in contributor pull requests against this repository's `/decisions` and in adopter feedback. Recognised when the returns are visibly about judgement, not about missing or malformed sections.

**Falsifying signal:** first-time records drafted with the skills still routinely return at governance review for the same framing and evidence gaps as spec-only drafts.

## Review boundary

If the skill count grows such that a first-time author must choose among many before starting, the commitment must be reviewed before its due point — added guidance would then be raising the cost it exists to lower, and the falsifying signal would not catch that.

## Optimism adjustment

The baseline observations are the author reviewing the author; that flatters the skills. The expected value is halved for settlement purposes: the claim stands if first-time returns fall at all against the baseline pattern, not only if they vanish.

## Observed outcomes

- 2026-07-06 — External use showed the front of the funnel was unguided; a fourth skill, Decision Identification, was added ([TDR-0007](../../../decisions/TDR-0007-add-decision-identification-skill.md)). An observation about coverage, not an observation against the baseline.

## Evidence

- **Existence** — [TDR-0003](../../../decisions/TDR-0003-ship-skills-alongside-spec.md), the linked decision and the authority this commitment rests on; the skills themselves, in [`/skills`](../skills/).
- **Observation** — none yet against the baseline. The 2026-07-06 entry above is about coverage, not about review returns.
- **Attribution** — none. Even were returns to fall, this repository's contributor population is small and self-selecting, and no basis currently exists for attributing a change to the skills rather than to who happened to show up.

## Attribution and settlement

Due at `reconcile_by` 2026-10-05, alongside the review of TDR-0003.

The honest expectation is that this settles as **`attribution-unresolved`**: the observation may well show returns falling, and the attribution evidence noted above is unlikely to exist by then. That is a legitimate settlement, not a failure to complete the record — and recording it as `realised` because the number moved in the right direction would be exactly the error §5 of the specification exists to prevent.
