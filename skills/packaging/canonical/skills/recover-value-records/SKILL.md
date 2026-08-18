---
name: recover-value-records
description: Examine supplied organisational material for value — identify source fragments that contribute to Value Records, reconcile fragments concerning the same proposition, construct supported candidate VRs, challenge them against the source estate, validate the resulting artefacts, and report what remains unknown, unclassified or conflicting. Use this skill as the entry point for value recovery — "what value commitments has this organisation actually made?", "recover Value Records from these documents", "what did we commit to across this estate?" — on any material, from one paper to a document estate. It orchestrates the value lifecycle and contains none of its semantics; every stage's rules live in the stage's own skill.
---

# Recover Value Records

The value language's **composition skill** — the user-facing entry point that runs the lifecycle
end to end. It orchestrates; it decides nothing. Every semantic rule lives in the stage skill it
belongs to, and this skill deliberately contains no second copy of any of them
([TDR-0026](../../../../decisions/TDR-0026-value-recovery-vocabulary.md); duplication is a defect,
[TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md)).

## The one rule

**No stage is allowed to invent the missing transition.** Where identification found nothing,
reconciliation has nothing to group; where reconciliation left a conflict, drafting carries it;
where drafting left a gap, challenge and validation report it. The pipeline's honesty is exactly the
honesty of its weakest stage, and this skill's job is to make sure no stage is skipped, reordered,
or quietly patched over by the next.

## The pipeline

Run the stages in order, handing each stage's output to the next unmodified:

1. **[`identify-value-contributions`](../identify-value-contributions/)** — fragments and classified
   contributions from the supplied material; `unclassified` outcomes; possibly nothing, which is
   success.
2. **[`reconcile-value-contributions`](../reconcile-value-contributions/)** — candidate groupings
   with reasons; the seven findings; tensions and supersessions recorded, never resolved.
3. **[`draft-value-record`](../draft-value-record/)** — one conformant candidate per assembly,
   completeness view attached; or the finding that no candidate is warranted.
4. **[`challenge-value-record`](../challenge-value-record/)** — the shared structural challenge,
   then the twelve value questions; one disposition per candidate: split · merge · reject ·
   incomplete · retain. **Split and merge route back to stage 2** with the challenge's reasons as
   input — not silently applied.
5. **[`validate-value-record`](../validate-value-record/)** — conformance, contribution coverage,
   the unsupported-claim list, temporal consistency.
6. **Stop.** Ratification is a named human's act
   ([`specification/candidacy-and-ratification.md`](../../../../specification/candidacy-and-ratification.md)).
   The skill proposes; the organisation ratifies.

## The report

One report for the whole run, whatever the material's size:

- **Candidates** — each with its completeness view, disposition, and provenance.
- **What remains unknown** — missing semantics by candidate, stated as what ratification must
  supply; the recovery invariant restated where it applies (absence of evidence is not evidence of
  organisational absence).
- **What remains conflicting** — unresolved conflicts and tensions, with what would settle each.
- **What was unclassified** — value-relevant material the vocabulary could not place; the evidence
  route for the vocabulary itself.
- **What was found and not used** — leads routed elsewhere (a decision identification, an
  observed outcome awaiting its commitment), and contributions no candidate consumed.
- **Nothing else.** No portfolio view, no prioritisation, no organisational judgement — those
  belong above the artefact boundary, to whatever consumes the records.

## When to refuse

- **Asked to skip a stage** ("just draft the records, don't bother challenging") — the pipeline is
  the conformance claim; a partial run is reported as a partial run.
- **Asked to ratify, score priorities, or judge what the organisation should value** — outside every
  stage, so outside this skill.
- **Asked to go looking for material.** The skill examines what an adopter supplies.

## Anti-patterns

- **Semantics creep** — this skill accumulating rules the stage skills should own. Any instruction
  here that changes *what* a stage decides, rather than *when it runs*, is a defect.
- **The silent loop** — applying a split/merge disposition without re-running reconciliation on the
  challenge's reasons.
- **Report inflation** — padding the unknowns section with speculation. Unknown means the evidence
  does not say; it never means "probably".

## Scope note

Orchestration only, per TDR-0026's composition ruling. How this skill is invoked on a given runtime
is the distribution adapter's business ([`skills/packaging/`](../../../../skills/packaging/)); what
happens to the recovered records afterwards is nobody's business but the adopter's
([TDR-0018](../../../../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md)).
