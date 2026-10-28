---
name: recover-inheritance-records
description: EXPERIMENTAL, not part of the MTDR standard (TDR-0047) — recover Operational Inheritance Records from organisational material end to end — identify, reconcile, draft, challenge, validate — as one entry point, whenever someone asks "what does the next team inherit from all this?", "recover the inheritance records from these hand-over packs" or "what would a successor need to know across this estate?". It orchestrates the work language's lifecycle and contains none of its semantics; every stage's rules live in the stage's own skill.
---

# Recover Inheritance Records

> **Experimental** under [TDR-0047](../../../../decisions/TDR-0047-experimental-packages.md). Not part
> of the MTDR standard.

The work language's **composition skill** — the user-facing entry point that runs the lifecycle end to
end. It orchestrates; it decides nothing. Every semantic rule lives in the stage skill it belongs to,
and this skill deliberately contains no second copy of any of them
([TDR-0026](../../../../decisions/TDR-0026-value-recovery-vocabulary.md)'s composition ruling;
duplication is a defect, [TDR-0023](../../../../decisions/TDR-0023-portable-skill-architecture.md)).

## The one rule

**No stage is allowed to invent the missing transition.** Where identification found nothing,
reconciliation has nothing to group; where reconciliation left a conflict, drafting carries it; where
drafting left a clause `missing`, challenge and validation report it. No stage fills what an earlier
one left open.

## The pipeline

Run the stages in order, handing each stage's output to the next unmodified:

1. **[`identify-inheritance-contributions`](../identify-inheritance-contributions/)** — fragments and
   contributions; participant leakage; `unclassified` outcomes; possibly nothing, which is success.
2. **[`reconcile-inheritance-contributions`](../reconcile-inheritance-contributions/)** — candidate
   groupings by capability, with reasons and findings.
3. **[`draft-inheritance-record`](../draft-inheritance-record/)** — one draft per assembly, with its
   marker view; or the finding that no draft is warranted.
4. **[`challenge-inheritance-record`](../challenge-inheritance-record/)** — the shared structural
   challenge, then the work language's; one disposition per draft. **Split and merge route back to
   stage 2** with the challenge's reasons as input.
5. **[`validate-inheritance-record`](../validate-inheritance-record/)** — schema, body against markers,
   lifecycle, references, unsupported claims.
6. **Stop.** Bringing a record into force is the accountable owner's act
   ([`candidacy-and-ratification.md`](../../../../specification/candidacy-and-ratification.md)).

## The report

One report for the whole run, headed as experimental under TDR-0047:

- **Drafts** — each with its marker view, disposition and provenance.
- **What remains unknown** — `missing` clauses by draft, stated as what the accountable owner must
  supply. Absence of evidence is not evidence of organisational absence.
- **What remains conflicting** — with what would settle each.
- **Participant leakage** — how much of the material described the worker rather than the work.
- **What was unclassified, and what was found and not used** — including leads routed to the decision,
  value or authority languages.
- **Nothing else.** No judgement on whether the OIR should exist: a count of `reference` markers is
  not a finding about native state. That is TDR-0046's deletion attack, run elsewhere and reviewed
  independently.

## When to refuse

- **Asked to skip a stage** — a partial run is reported as a partial run.
- **Asked to bring records into force**, or to judge what the organisation should require of its
  participants.
- **Asked whether the OIR should be admitted to the standard.**
- **Asked to go looking for material.** The skill examines what is supplied.

## Anti-patterns

- **Semantics creep** — this skill accumulating rules the stage skills should own.
- **The silent loop** — applying a split or merge without re-running reconciliation.
- **The verdict report** — reading the marker tally as evidence for or against the record family.

## Scope note

Orchestration only. How the skill is loaded is the runtime's business; experimental skills are never
part of the standard's distribution bundles ([`skills/packaging/`](../../../../skills/packaging/)), and
what happens to recovered records afterwards is the adopter's
([TDR-0018](../../../../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md)).
