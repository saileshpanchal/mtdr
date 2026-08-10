---
name: challenge-value-record
description: Challenge a candidate Value Record with the value language's own failure modes — attribution asserted from measurement, reconciliation semantics leaked into the commitment, a beneficiary assumed rather than evidenced, optimism undeclared, and a falsifying signal that cannot actually fail. Use this skill on every candidate Value Record before ratification, whenever someone asks "would this benefit claim survive scrutiny?" or "is this attribution real?", after the shared structural challenge has run. It never treats a missing counterfactual as a defect, and it treats attribution-unresolved as an honest settlement rather than a finding to fix.
---

# Challenge Value Record

The value language's specialisation of the challenge stage. The **structural mechanics** — walking
every value back to a span, reading spans alone, tense and modality shifts, attacking the grouping,
checking gaps are gaps — are the shared skill's,
[`challenge-record`](../../../../skills/shared/challenge-record/), and run first. This skill then
challenges what only the value language can get wrong.

## The one rule

**Attack the attribution hardest.** Measurement is not attribution, and material destroys the
distinction routinely — a cost line falling near a programme name reads as benefit delivered. Every
attribution claim must be supported by attribution evidence, not by an observation; where it is not,
the finding is that the settlement should read **attribution-unresolved**, and that finding is not a
defect in the record. It is the record being honest.

## The value-specific challenges

1. **Is the beneficiary evidenced, or assumed?** From whose outcome the material actually names — not
   from who wrote the document, and not from who benefits by default.
2. **Has reconciliation leaked into the commitment?** A realised figure rendered as expected value, an
   observed outcome in a commitment section, a settlement judgement before ratification.
3. **Can the falsifying signal actually fail?** "We will monitor benefits closely" cannot. A signal
   that no plausible observation could trigger is a hope wearing instrumentation.
4. **Is the optimism declared, or ambient?** An expected value carried straight from a business case,
   with no declared adjustment and no rationale, imports the case's flattery as fact.
5. **Is the baseline real?** Measured, dated, sourced — not "current state" by assumption, and not
   the target restated as a starting position.
6. **Is protection being lost?** Where the linked decision carried a protective condition, does the
   candidate preserve it as a review boundary — or has protected value been flattened into the
   pursuit's footnotes?
7. **Are the two state axes honest?** `status` and `realisation` claims each supported — never a
   candidate carrying observation states, never a settlement without the counter-signature the
   specification requires.

## What is never a finding

- **A missing counterfactual.** Optional by design ([`specification/vr.md`](../../specification/vr.md)
  §5.2); its absence limits what incremental claims can later be defended, and that consequence may be
  *noted* — but the absence itself is neither reported as a gap nor inferred into existence.
- **`attribution-unresolved` as a settlement.** Forcing it toward realised or written-off is the
  optimistic-settlement failure, in either direction.

## Outputs

Findings most serious first, each naming the statement, what the evidence supports, and what would
resolve it — appended to the shared challenge's structural findings, with the overall
fit-to-propose judgement made across both.

## Anti-patterns

- **Attribution sympathy** — accepting adjacency because the benefit "obviously" came from the
  programme.
- **Counterfactual creep** — demanding one because it would make the assessment easier.
- **Optimism laundering** — challenging the figure but not the absence of a declared adjustment.
- **Signal theatre** — passing a falsifying signal that cannot fail.

## Scope note

Structural challenge is the shared skill's; this adds the value language's semantics only, per
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md). Whether the commitment was
*wise* is not challenged here at all — that is the linked decision's assurance question.
