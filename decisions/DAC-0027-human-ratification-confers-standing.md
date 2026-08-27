---
id: DAC-0027
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0027
title: Assure human ratification as standing and evidence as its accepted representation
status: accepted
disposition: proceed-with-constraints
assessed_at: 2026-08-13
accountable_owner: Sailesh Panchal
review_date: 2026-09-13
confidence: medium
supersedes: none
---

# DAC-0027 — Assure human ratification as standing and evidence as its accepted representation

> **Reassessed and accepted 2026-08-13.** Human review ratified TDR-0027's architectural principle
> and rejected this case's original blanket deferral. This case permits the principle to proceed
> under the constraints below; it does not authorise automated promotion to `accepted`.

## Uncertainty

Known: authorised human ratification can confer organisational standing independently of MTDR, and
Git state, validator output and agent action do not establish that act by themselves. Evidence is
required before MTDR may represent standing as `accepted`. Unknown: the portable evidence protocol
and the complete taxonomy separating substantive change from permitted non-semantic correction.
Assumption: evidence semantics can remain technology-neutral and offline-compatible. Confidence is
medium because the principle is supported while its execution protocol remains unproven.

## Adversarial projection

Fully routed. Evidence may be forged, stale, copied from another judgement, produced under invalid
authority or record a coerced or ambiguous act. An agent may also write `accepted` and cite its own
commit. Controls must establish actor, authority at the time, intent and act, time and the
substantive judgement reviewed. Technical operations may carry that evidence but cannot substitute
for the human act. Residual exposure belongs to the accountable governance authority.

## Customer-outcome projection

Routed because standing records can authorise decisions affecting customers. Weak evidence enables
unaccountable action; overly rigid evidence excludes legitimate decision-makers and may concentrate
authority in administrators of one identity system.

## Control side-effects

Durable evidence improves challengeability but increases identity, privacy and retention burdens.
Byte-identical revision binding would make harmless editorial correction expensive; a loose
subject reference would let semantic changes inherit approval. Until a governed taxonomy exists,
ambiguous changes must be treated as substantive without creating a maintainer exemption.

## Execution capability

The repository can adopt and apply the architectural principle manually. It cannot yet implement a
portable automated promotion protocol: there is no evidence format, semantic-change classifier or
adversarial conformance suite. A complete authority vocabulary is not a prerequisite for the
principle; until the authority model exists, evidence of delegated authority requires human review.

## Risk delta and declared interactions

The decision decreases agent-created authority and unsupported `accepted` representations while
increasing governance and evidence-handling cost. It avoids declaring genuine external authority
non-existent merely because MTDR lacks evidence. It interacts with TDR-0002, TDR-0015, TDR-0019,
TDR-0025 and future authority-language work. Concentrating evidence in one platform transfers
systemic risk to that platform.

## Risk vector

| Axis | Assessment and basis |
|---|---|
| severity | very high — standing is the gateway to consequential authority |
| likelihood | high — current branch history demonstrates the ambiguity |
| exposure volume | high — every governed record transition is affected |
| velocity | high — agents and Git operations can label many records quickly |
| concentration | high if one identity or repository mechanism becomes mandatory |
| detectability | medium — revision mismatches are testable; coercion and ambiguity are harder |
| reversibility | low after downstream reliance on apparent standing |
| control confidence | medium-low — the manual boundary is clear; portable automation is unproven |
| customer-cohort distribution | concentrated on people subject to decisions they cannot challenge |
| time horizon | permanent, with acute risk at each authority transition |
| trend | stabilising under manual constraints; unstable for automation |

## Decision debt

- Define portable evidence semantics for actor, authority at the time, act and intent, substantive
  judgement and time without freezing one field set or technology — owner Sailesh Panchal, due
  2026-09-13.
- Define the governed boundary between substantive change and permitted non-semantic correction,
  including provenance requirements — owner Sailesh Panchal, due 2026-09-13.
- Test forged, stale, copied, judgement-mismatched, coerced and ambiguous evidence, plus an offline
  ratification path — owner Sailesh Panchal, due 2026-09-13.
- Route delegation, expiry and revocation semantics into the authority model; retain manual
  authority review until it exists — owner Sailesh Panchal, due 2027-01-31.
- Compare ratification evidence across at least two governance mechanisms, one not dependent on Git
  — owner Sailesh Panchal, due 2027-01-31.

## Monitoring contract

- Hypothesis: every MTDR `accepted` representation resolves to evidence sufficient to establish an
  authorised human ratification of the substantive judgement represented. Counter-hypothesis: a
  status label, technical event or mismatched evidence passes, or an evidence failure is incorrectly
  used to deny an externally valid decision existed. Test: inspect every transition to `accepted`
  and run the adversarial evidence fixtures before automation is enabled. Metric is unsupported or
  ontologically false standing assertions; threshold is one; owner Sailesh Panchal; trigger is stop
  automated transition, mark the case stale and reopen the evidence mechanics.

## Learning obligations

Retain rejected evidence forms and the reason each failed. Test the model with humans who ratify
outside Git and with delegated authority. Record separately whether a failure concerns the
existence of authority, evidence of authority or MTDR's representation of authority.

## Disposition

**Proceed with constraints.** The architectural principle is supportable; automated execution is
not yet supportable. The constraints are:

1. **No automated promotion to `accepted`.** Owner: Sailesh Panchal. Measure: no MTDR-provided
   workflow, validator or skill changes record status from `proposed` to `accepted` until the
   evidence semantics and adversarial fixtures above are governed and conforming.
2. **Manual accepted transitions require attributable evidence.** Owner: Sailesh Panchal. Measure:
   every new `accepted` representation reviewed during this constraint resolves to evidence of the
   actor, authority at the time, act and intent, substantive judgement and time.
3. **Ambiguous changes are substantive.** Owner: Sailesh Panchal. Measure: until the correction
   taxonomy is governed, no accepted record inherits ratification across an ambiguous change; use
   a new ratification or superseding TDR while retaining provenance.
4. **Delegated authority remains manually assessed.** Owner: Sailesh Panchal. Measure: no automated
   conclusion about delegation, expiry or revocation before the authority model governs it.
5. **Mechanism neutrality is preserved.** Owner: Sailesh Panchal. Measure: the proving comparison
   includes at least one non-Git or offline-capable mechanism before automation is authorised.

Skills run: systems-thinking, counterfactual-and-evidence, accumulated-and-resultant-risk,
fraud-and-adversarial-thinking, customer-outcomes, systems-dynamics, adaptive-capacity and
assurance-synthesis.
