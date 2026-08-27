---
id: TDR-0040
conforms_to: mtdr/decision/tdr@1.15.0
title: Canonical behavioural sequencing is normative; runtime orchestration is not
status: accepted
template: minimal
decision_date: 2026-08-21
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: TDR-0023
derived_from: TDR-0018, TDR-0024, TDR-0026, TDR-0032
confirmed_by_outcome: pending — review when an independent runtime has been shown to preserve the sequence without being told how to schedule it, or 2027-02-21, whichever is sooner
---

# TDR-0040 — Canonical behavioural sequencing is normative; runtime orchestration is not

> **Accepted 2026-08-21.** A carry-forward of an unresolved Gate-B judgement, ratified
> on its own merits — standing originates in that act, not in the Gate-B candidate,
> which was never ratified. Evidence:
> [`evidence/TDR-0040-ratification-2026-08-21.md`](evidence/TDR-0040-ratification-2026-08-21.md).
>
> This record proposes to supersede [TDR-0023](TDR-0023-portable-skill-architecture.md) **narrowly**,
> adding one distinction and retaining every other judgement in it. TDR-0023 remains accepted unless
> and until a named human ratifies this record.
>
> The judgement is the one drafted on `codex/gate-b-decision-drafts` (`f966a05`) and is represented
> here substantially as it stood there. That candidate was never ratified and its identifier is
> burnt, so **nothing about standing is carried** — what carries is the judgement, and it carries as
> a proposal. The audit establishing that it is still open, and classifying this successor as a
> carry-forward, is
> [`evidence/gate-b-candidate-disposition-2026-08-21.md`](evidence/gate-b-candidate-disposition-2026-08-21.md).

## Context — what was known at the time

TDR-0023 put skills next to the semantics they carry and named the lifecycle stages — identify →
classify → reconcile → draft → challenge → validate → ratify. It said nothing about whether the
*order* of those stages is part of the standard.

At the time the question was theoretical. It is not now, because the repository has since shipped a
skill whose entire content is order. [`recover-value-records`](../records/value/skills/recover-value-records/)
requires the five stages to run in sequence, requires each stage's output to be handed to the next
**unmodified**, routes a split or merge disposition **back to stage 2** rather than applying it
silently, and **stops** at the ratification boundary. Those are requirements about behaviour, and the
skill is explicit that they are the whole of its job: *"it orchestrates; it decides nothing."*

Nothing in the register says whether such a requirement is inside the standard's boundary.
[TDR-0032](TDR-0032-typed-multi-object-conformance.md) mentions runtime orchestration once, in a list
of things a conformance claim does not require. Read alone — and it is currently the only reading
available — that says a multi-stage requirement is out of scope, which would make the shipped entry
point's rules unenforceable claims about nothing.

**The gap is load-bearing rather than tidy.** TDR-0032 makes conformance a claim by a *typed
subject*, one of which is participant behaviour. A participant conformance claim needs behaviour to
be conformant *to*. And the VR-4 reconstruction protocol's first calibration criterion is that every
arm "respects the same boundaries — nobody skips a stage or fuses two" — a criterion with nothing to
test against if the sequence was never normative.

The countervailing risk is the one TDR-0024 and TDR-0038 exist to hold: a standard that specifies
*how* work is executed has begun specifying a runtime, and the packaging evidence at v1.28 shows
five runtimes reading canonical skills directly precisely because MTDR asks so little of them.

## Decision

**Canonical behavioural sequencing is normative. Runtime orchestration is not.**

A portable skill **may** require that stages run in a stated order, define the conditions under which
work returns to an earlier stage, state what may never be skipped or fused, and state where
execution must stop. These specify the behaviour that must survive every runtime, and a participant
that does not exhibit them has not performed the skill.

A runtime's scheduling of agents, models, tools, retries, parallelism, persistence, context handling
and user interaction is **how** that behaviour is realised. It remains outside MTDR, and no canonical
artefact may specify it.

Two consequences fix the boundary where it can be tested:

1. **An entry point governs sequence, not meaning.** It is conformant only while every semantic
   judgement is delegated to the stage that owns it and it stops at the human-ratification boundary.
   A second normative copy of a stage's rules inside an entry point is a defect, resolved in the
   stage's favour — TDR-0023's existing rule, now with the case it was written for.
2. **A normative sequence is only normative if it terminates.** A repeated return to an earlier stage
   must end in an explicit unresolved or human-review outcome. A loop with no stated stopping
   behaviour specifies nothing a runtime could fail to do.

The test that separates the two: **does the requirement change what is produced, or only how the
producing was arranged?** The first is sequence and belongs here. The second is orchestration and
does not.

## Alternatives rejected

1. **Treat every multi-stage requirement as runtime orchestration.** Rejected: it leaves the standard
   unable to require propose-before-ratify or challenge-before-validate, so a runtime could reorder
   the lifecycle, skip challenge entirely, and still claim to be running the same skills. It would
   also delete the only thing VR-4's calibration criterion can measure against.
2. **Make the sequence a property of the record rather than the skill.** Rejected: a record carries
   judgement, not controls (spec §10). A record that encoded the process by which it was produced
   would make process compliance visible as record content and unenforceable in the same breath.
3. **Say nothing and let the shipped entry point stand on its own text.** Rejected: an obligation
   that exists only inside the artefact it governs cannot be appealed to when a runtime declines it,
   and TDR-0032 currently reads against it.
4. **Specify the sequence and a reference execution model together.** Rejected: that is a runtime,
   and TDR-0038's falsification criterion already names the failure — if supporting a runtime
   requires changing a canonical artefact's meaning, the runtime is unsupported; the reverse move,
   changing MTDR to describe a runtime, is the same error facing the other way.

## Options foreclosed

- No canonical artefact may specify model choice, tool scheduling, persistence, retries, context
  management or platform coordination. These are runtime concerns **even when they execute a
  normative sequence**.
- No entry point may acquire semantics of its own. Sequencing authority is not an opening through
  which meaning enters at the composition layer.
- No normative sequence may be published without stated stopping behaviour.
- The standard cannot later require a particular execution topology — agents, pipelines, queues or
  passes — without superseding this record.

## Review

Success is an independent runtime preserving the sequence, the re-entry conditions and the stopping
point without being told how to schedule anything, and a divergence at a stage boundary being
diagnosable as a runtime finding rather than as a difference of opinion about whether the boundary
existed. VR-4 is the first evidence that could show this, and is also the first that could falsify
it: if preserving the sequence turns out to require runtime-specific instruction, the distinction
drawn here is wrong and this record is superseded to say so.

Review on that evidence, or 2027-02-21, whichever is sooner.

**A DAC is not routed.** This is a boundary clarification over already-shipped behaviour, with no
material customer, adversarial, authority or execution-risk delta beyond what TDR-0023, TDR-0024 and
TDR-0032 already assured. Recording the non-routing is the assurance decision; a ceremonial case
would weaken the proportionality rule this repository demonstrates.
