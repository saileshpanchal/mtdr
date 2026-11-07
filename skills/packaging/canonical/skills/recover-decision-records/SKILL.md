---
name: recover-decision-records
description: Recover decisions an organisation took and never recorded, end to end — identify, reconcile, draft, challenge, validate — as one entry point, producing retrospective candidates that never acquire standing because they were reconstructed. Use this skill whenever someone says "find the decisions in these minutes", "what did we decide and never write down?" or "recover the decision history of this programme", on any material from one transcript to a document estate. It orchestrates the decision language's recovery stages and contains none of their semantics; every stage's rules live in that stage's own skill.
---

# Recover Decision Records

The decision language's **composition skill** — the entry point that runs historical recovery end to
end. It orchestrates; it decides nothing. Every semantic rule lives in the stage it belongs to, and
this skill carries no second copy of any of them
([TDR-0026](../../../../decisions/TDR-0026-value-recovery-vocabulary.md)'s composition ruling;
duplication is a defect, [TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md)).

## The one rule

**Recover what can be evidenced. Preserve what cannot. Never turn a contemporary interpretation into
historical authority** ([`historical-recovery.md`](../../../../specification/historical-recovery.md)).
No stage invents the missing transition: what identification did not find, nothing later supplies.

## The pipeline

Run the stages in order, handing each output to the next unmodified:

1. **[`identify-decision-contributions`](../identify-decision-contributions/)** — fragments, classified
   contributions, fragment and `considered` annotations, not-a-decision and non-decision findings,
   `unclassified` outcomes; possibly nothing, which is success.
2. **[`reconcile-decision-contributions`](../reconcile-decision-contributions/)** — one assembly per
   decision, with reasons.
3. **[`draft-tdr`](../draft-tdr/)** — a draft at the routed tier, with its completeness view; or the
   finding that no record is warranted.
4. **[`challenge-decision-record`](../challenge-decision-record/)** — the shared structural challenge,
   then the decision language's; one **recommendation** per candidate. Split and merge route back to
   stage 2 with the challenge's reasons.
5. **[`validate-decision-record`](../validate-decision-record/)** — the contract, recomputed.
6. **Stop.** What the stages produced is handed on as **historical candidates**
   ([`historical-candidate.md`](../../../../specification/historical-candidate.md)): fragments,
   contributions, annotations and assembly together, `standing: none`. **This skill produces no review
   event.** Attesting an account is a named individual's act, and whether a recovered decision governs
   now is a separate prospective decision.

## The report

One report for the whole run:

- **Candidates** — each with its completeness view, its recommendation, and its provenance.
- **What remains unknown** — missing owners, dates and alternatives, stated as what an attester would
  have to find. Absence of evidence is not evidence of absence.
- **What remains conflicting** — with what would settle each.
- **What is not a decision** — each finding with its reason, by stable identifier, and each piece of
  evidence that no decision was made, with its kind.
- **Retrospective material set aside** — what corroborates and what it was not allowed to explain.
- **What was unclassified, and what was found and not used.**
- **Coverage** — every source examined, so that *no candidates* can be read as what it is.
- **Nothing else.** No judgement on whether a decision was wise, no reflection on what might have been
  decided better, no handover. Those read candidates; they are not recovery.

**Zero candidates is a success only when the report shows the coverage, every classification and all
unresolved evidence.** Confident emptiness, with its evidence, is the pass.

## When to refuse

- **Asked to skip a stage** — a partial run is reported as a partial run.
- **Asked to attest, ratify, or mark a candidate reviewed** — outside every stage.
- **Asked to decide whether a recovered decision still applies** — a prospective decision, not
  recovery.
- **Asked to go looking for material.** The skill examines what it is given.

## Anti-patterns

- **Semantics creep** — this skill accumulating rules the stages own.
- **The silent loop** — applying a split or merge without re-running reconciliation.
- **The tidy history** — a report that reads as a narrative the sources do not individually support.

## Scope note

Orchestration only. How the candidates are kept, indexed, reviewed or connected is the adopter's
business ([TDR-0018](../../../../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md)).
