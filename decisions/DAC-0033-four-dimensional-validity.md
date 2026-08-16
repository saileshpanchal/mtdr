---
id: DAC-0033
tdr_id: TDR-0033
title: Assure independent validity dimensions and transition eligibility
status: accepted
disposition: proceed-with-constraints
assessed_at: 2026-08-13
accountable_owner: Sailesh Panchal
review_date: 2026-09-13
confidence: medium
supersedes: none
---

# DAC-0033 — Assure independent validity dimensions and transition eligibility

> **Standing carried forward 2026-08-16.** Human review confirmed this case preserves the accepted
> Gate-B DAC-0025 findings, constraints, exclusions and scope while rebinding them to TDR-0033 under
> TDR-0031. This is an accepted representation of the earlier assurance ruling, not a new assurance
> judgement and not authorisation to implement or release.

## Uncertainty

Known: schema-valid objects can violate semantics; intrinsically sound records can have broken or
unavailable relationships; legitimately incomplete current states can be ineligible for transition;
and validators cannot establish human authority. The VR schema currently contradicts its own
candidate lifecycle by globally requiring `finance_countersignatory`. Unknown: the exact versioned
result contract and which results are legal for each package-specific rule. Assumption: independent
dimension reports can remain useful without becoming a success pipeline. Confidence is medium
pending fixtures and a second implementation.

## Adversarial projection

Fully routed for validator, evidence and authority abuse. A tool may compress results into one green
badge, treat `indeterminate` as permission to infer, hide a relational failure behind intrinsic
validity, repair a record during validation, or turn eligibility into promotion. Controls are
dimension-specific evidence, legal result vocabularies, immutable assessed inputs, must-not probes
and the TDR-0027 authority boundary. Residual exposure belongs to the standard maintainer and each
validator operator.

## Customer-outcome projection

Routed lightly but materially. A false-positive eligibility result can legitimise consequential
records affecting customers. A false-negative validity result can suppress honest incomplete
candidates, especially evidence about cohorts whose owners, baselines or recognition routes are
missing from organisational material.

## Control side-effects

Four dimensions and four result values can create validation fatigue, fragmented tooling and
status theatre. Treating every unavailable relationship as failure would make offline and
zero-install use impractical; treating it as harmless would conceal organisational inconsistency.
Layer-specific legal outcomes and concise reasons are required to avoid both effects.

## Execution capability

The repository has strict schemas, semantic fixtures, relational checks and behavioural probes, but
not one versioned result contract or end-to-end implementation that reports the four dimensions
without mutation or promotion. The existing VR schema cannot yet represent the proving candidate.
That correction belongs to TDR-0019, so TDR-0033 can be adopted conceptually but not claimed as
implemented.

## Risk delta and declared interactions

The decision decreases false certainty, suppressed incomplete evidence and validator-created
authority while increasing result-model and integration complexity. It interacts directly with
TDR-0019, TDR-0032 and TDR-0027 and with every future record language. A shared validator remains a
correlated-failure point, so no aggregate green result may conceal a dimension.

## Risk vector

| Axis | Assessment and basis |
|---|---|
| severity | high — a false readiness result can create apparent legitimacy |
| likelihood | high — schema validity and lifecycle readiness are already conflated |
| exposure volume | high — every object and validator inherits the model |
| velocity | high — automated validation can propagate labels quickly |
| concentration | high — a shared result contract can correlate failures |
| detectability | medium — dimensioned fixtures catch known errors; plausible semantic invention remains hard |
| reversibility | high before a human transition, low after downstream reliance |
| control confidence | medium-low — the principle is clear; implementation and fixtures are incomplete |
| customer-cohort distribution | indirect, concentrated where organisational evidence is incomplete or weakly represented |
| time horizon | continuous across object, specification and validator versions |
| trend | stabilising under release and no-promotion constraints |

## Decision debt

- Define the versioned validation-result contract, reasons, evidence references, evaluation context and legal outcomes by dimension — owner Sailesh Panchal, due 2026-09-13.
- Add fixtures independently exercising structural, semantic, relational and eligibility results, including legal `indeterminate` and `not-applicable` cases — owner Sailesh Panchal, due 2026-09-13.
- Add the incomplete VR candidate proving structural/semantic pass and eligibility fail without inventing a finance counter-signatory — owner Sailesh Panchal, due 2026-09-13 through TDR-0019 remediation.
- Add relational fixtures for resolved, broken, incompatible-version and unavailable relationships without requiring a register — owner Sailesh Panchal, due 2026-09-13.
- Add must-not probes proving validation cannot mutate, repair, promote, ratify, infer standing or treat `indeterminate` as permission — owner Sailesh Panchal, due 2026-09-13.
- Reconcile the VR schema with state-relative candidate validity only through TDR-0019 — owner Sailesh Panchal, due 2026-09-13.
- Make every validator output identify its TDR-0032 conformance subject and applicable specification identity/version — owner Sailesh Panchal, due 2026-09-13.
- Run two implementations against the same corpus and compare dimensioned outcomes and reasons — owner Sailesh Panchal, due by 2027-08-13.

## Monitoring contract

- Hypothesis: each assessment reports structural, semantic, relational and eligibility dimensions
  independently; incomplete current states remain valid where permitted; no result causes mutation,
  authority or standing. Counter-hypothesis: a layer is collapsed, unavailable evidence is inferred,
  a transition-only requirement invalidates the current state, or validation changes status or
  content. Test: run all dimension fixtures and must-not probes against each implementation and
  compare the input before and after. Metric is unreported dimensions, illegal result values,
  cross-dimension implications, input mutations and authority/standing inferences; threshold is one;
  owner Sailesh Panchal; trigger is block release, mark this case stale and reopen TDR-0033 if the
  architecture rather than its implementation is falsified.

## Learning obligations

Retain every case where reviewers disagree whether a result is `fail`, `indeterminate` or
`not-applicable`, together with the applicable rule and available evidence. Preserve incomplete
candidates and original invalid objects unchanged. Record separately what is invalid now, what is
unknown, and what blocks a requested transition.

## Disposition

**Proceed with constraints.** The constitutional validity model is supportable; implementation and
release are not yet supportable. The constraints are:

1. **Versioned result contract before release.** Owner: Sailesh Panchal. Measure: every validation
   result identifies the typed TDR-0032 subject, applicable specification identity/version, four
   dimensions, reasons, evidence and evaluation context, and rejects illegal outcomes by dimension.
2. **Independent layer fixtures.** Owner: Sailesh Panchal. Measure: fixtures exercise pass, fail,
   indeterminate and not-applicable wherever legal for each dimension without treating the four
   dimensions as a pass pipeline.
3. **Incomplete-candidate proof.** Owner: Sailesh Panchal. Measure: after TDR-0019 governs the schema
   correction, a candidate VR lacking only transition-required finance counter-signature passes
   current-state structural and semantic validity and fails ratification eligibility.
4. **Relational portability.** Owner: Sailesh Panchal. Measure: resolved, broken, incompatible and
   unavailable-reference fixtures produce distinct relational results from a declared portable
   evaluation context without requiring a register or graph.
5. **No authority or mutation.** Owner: Sailesh Panchal. Measure: must-not probes prove validators
   never repair input, fill missing human information, promote state, ratify, infer standing or use
   `indeterminate` as permission; byte comparison preserves the assessed object.
6. **VR correction only through TDR-0019.** Owner: Sailesh Panchal. Measure: no opportunistic change
   to the VR schema or lifecycle under TDR-0033; the inconsistency remains explicit until the VR v2
   judgement is ratified and remediated.
7. **Behaviour remains a separate claim.** Owner: Sailesh Panchal. Measure: participant execution is
   tested and reported under TDR-0032 behavioural conformance, never as a fifth record-validity
   dimension or an implication from skill-file validity.
8. **No aggregate normative verdict.** Owner: Sailesh Panchal. Measure: interfaces may summarise for
   usability but retain and expose every dimension; no normative aggregate green result overrides a
   failure or indeterminate result.

Skills run: systems-thinking, counterfactual-and-evidence, accumulated-and-resultant-risk,
fraud-and-adversarial-thinking, customer-outcomes (light), systems-dynamics, adaptive-capacity and
assurance-synthesis.
