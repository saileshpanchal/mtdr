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

1. **Is this genuinely a value commitment?** Who benefits — and is the beneficiary evidenced, or
   assumed from who wrote the document?
2. **Has aspiration been mistaken for commitment?** An ambition with no binding authority is not yet
   a commitment — though later material may bind it, so the finding names what binding is absent.
3. **Has activity been mistaken for value, or a KPI mistaken for value?** Work is not an outcome; a
   target nobody committed to is the shadow of a claim.
4. **Has a financial measure displaced the actual proposition?** The figure is evidence *about* the
   commitment; where the drafted commitment *is* the figure, find the proposition underneath.
5. **Has reconciliation leaked into the commitment?** A realised figure rendered as expected value,
   an observed outcome in a commitment section, a settlement before ratification.
6. **Can the falsifying signal actually fail?** "We will monitor benefits closely" cannot. A signal
   no plausible observation could trigger is a hope wearing instrumentation.
7. **Is the optimism declared, or ambient — and is the baseline real?** Measured, dated, sourced;
   not "current state" by assumption, and not the target restated as a starting position.
8. **Have constraints disappeared, or protection been lost?** Where source material carried a
   boundary or a protective condition, does the candidate preserve it — or has protected value been
   flattened into the pursuit's footnotes?
9. **Have conflicting statements been reconciled without authority?** An authorised weighing in the
   material may be recorded; a weighing the drafting performed is a fabrication.
10. **Is this actually a decision rather than Value?** Route it, do not force it.
11. **Is the supposed commitment still current?** Supersession evidence elsewhere in the estate —
    the challenge reads beyond the candidate's own supporting fragments.
12. **Is there evidence elsewhere that would falsify it?** `challenge`-class contributions exist to
    be found; a challenge that only reads supporting evidence is confirmation with extra steps.

## Dispositions

The output closes with exactly one recommendation per candidate:

**split** (two objects wrongly merged) · **merge** (one object wrongly divided) · **reject** (not a
value commitment — with the boundary test it fails) · **incomplete** (genuine but under-evidenced —
with the completeness view's gaps) · **retain** (fit to propose as drafted).

This is what makes the skill more useful than generic self-criticism: every finding lands on a
disposition a human can act on.

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
