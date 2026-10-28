---
name: draft-inheritance-record
description: EXPERIMENTAL, not part of the MTDR standard (TDR-0047) — assemble reconciled inheritance contributions into a draft Operational Inheritance Record in which every one of the ten clauses says where its answer lives (asserted, reference, missing or conflicting). Use this skill after reconcile-inheritance-contributions has produced a candidate assembly, whenever someone says "write up what the next team inherits from these documents", and when inherited state found in existing material needs a conformant draft. It never restates referenced content, never asserts authority, never fills a missing clause, and always drafts with status draft — bringing a record into force is the accountable owner's act.
---

# Draft Inheritance Record

> **Experimental** under [TDR-0047](../../../../decisions/TDR-0047-experimental-packages.md). Not part
> of the MTDR standard.

This skill turns a [`CandidateAssembly`](../../../../specification/candidate-assembly.md) for an
**operational capability** into a markdown OIR. Read [`specification/oir.md`](../../specification/oir.md)
for the clauses and [`validation/`](../../validation/) for the roles and the admissibility test. Use
[`templates/oir.md`](../../templates/oir.md).

## The one rule

**Every clause says where its answer lives.** The source marker is set before the content is written,
and the content never contradicts it: a `reference` cites and does not restate; a `missing` clause
states what is not known; a `conflicting` clause cites every source. The markers are what let the
record be checked, superseded, and judged under TDR-0046.

## Process

### 1. Check admissibility first

Apply [`validation/admission.md`](../../validation/admission.md). A candidate that identifies a
participant rather than a capability is not drafted as an OIR; the finding is reported.

### 2. Title the capability and render the jobs

The title and each job survive the participant-change test. Each job carries `established_by`: a
decision identifier where the material supplies one, otherwise `unknown`. Never infer the decision.

### 3. Render the ten clauses

For each clause, from its contributions:

- several contributions agree and cite a source → **`reference`**, the identifiers in `refs`;
- the answer is stated only in the material, with provenance → **`asserted`**;
- no contribution → **`missing`**;
- contributions disagree → **`conflicting`**, every source in `refs`.

**`authority` is `reference` or `missing`, never `asserted`.** An unsourced limit in the material is
reported beneath the clause as an unsourced claim; it is not drafted as authority.

### 4. Frontmatter

`conforms_to: mtdr/work/oir@1.0.0`, `experimental: true`, `status: draft`. `effective_from` is the
date the inherited state applies from, and `accountable_owner` the named individual accountable for
the record — each `unknown` where the evidence does not supply it. Never the drafting date, never the
material's author: the schema accepts `unknown` only in a draft, so the gap must be closed before the
record can come into force. `supersedes` names the predecessor only where reconciliation found
*inherited state changed*, never *participant changed only*.

### 5. Mark every gap in place

**Inherited context, authority and escalation** are the clauses real material most often lacks or
leaves participant-voiced. Each `missing` marker is a finding about what a successor would not be told.

## The discipline

**Populate only what the evidence supports. Missing means missing. Referenced means referenced, not
copied.** A weak but faithful draft is better than a complete-looking record whose clauses cannot be
traced.

## Outputs

A markdown OIR with `status: draft`, plus the **marker view**: each clause with its source marker and
the contributions behind it, the unsourced authority claims, the participant leakage carried forward
from identification, and any `unclassified` outcomes.

## When to refuse

- **No capability identified** — only a participant, a team or a system.
- **No job evidenced** in functional form.
- **Asked to bring the record into force.** `in-force` is the accountable owner's act.
- **Asked to resolve a conflict, fill a gap, or copy a referenced record's content** "so it reads on
  its own".

## Anti-patterns

- **Restatement** — the delegation's limits copied into **You may**. The copy drifts; the reference
  does not.
- **Manufactured authority** — a limit drafted because the work obviously needs one.
- **The participant-shaped record** — a title or jobs that name the current team.
- **Practice as fact** — a failure history rendered as a recommendation, losing what happened.
- **The tidy record** — every clause populated because a missing one looked unfinished.

## Scope note

This skill drafts from contributions and the record package alone. It does not judge whether a clause
*reduces* to another record — a `reference` marker is data for TDR-0046's deletion attack, not a
verdict.
