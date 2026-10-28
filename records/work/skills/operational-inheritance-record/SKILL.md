---
name: operational-inheritance-record
description: EXPERIMENTAL, not part of the MTDR standard (TDR-0047) — raise, draft and maintain an Operational Inheritance Record (OIR), the record of what organisational state a participant must inherit before performing a piece of operational work. Use this skill when work changes hands — a hand-over, a reorganisation, an outsourcing, software or an AI participant taking on defined work — and someone asks "what does the next person need to know before they do this?", "what are they allowed to do here?" or "what has this work taught us?". It describes the work, never the worker; it refuses to state authority without citing where it was delegated, and refuses to supersede a record because the participant changed.
---

# Operational Inheritance Record

> **Experimental.** Published for review under [TDR-0047](../../../../decisions/TDR-0047-experimental-packages.md)
> and governed by the frozen test in [TDR-0046](../../../../decisions/TDR-0046-oir-experiment-preregistration.md).
> Using this skill creates no conformance claim. Whether the OIR is native organisational state or a
> projection over records the standard already has is the experiment's question, not this skill's.

This skill raises and maintains OIRs. It is written for humans and usable by AI assistants. Read
[`specification/oir.md`](../../specification/oir.md) for the clauses and the source marker; the
recovery skills ([`recover-inheritance-records`](../recover-inheritance-records/)) reconstruct an OIR
from material that was never written as one.

## The one rule

**Describe the work, never the worker.** If replacing the participant would require rewriting the
record, the record describes a role, a procedure or an implementation, and inherited state has not yet
been found. Everything else in this skill exists to keep the record true when the participant changes.

## Process

### 1. Name the capability

One record per operational capability: an enduring body of work and the state in force around it.
Title it after the work (*the restoration of the payment service after disruption*), never after a
team, a person, a supplier or a system. Apply the participant-change test to the title before
anything else is written.

### 2. Name the jobs

Each job in the functional form **verb + object + contextual clarifier**, each surviving the
participant-change test. Record `established_by` against each: the decision that established the job
where one exists, `unknown` where none can be found. The record names the jobs; the organisation owns
them. Jobs change by decision, never by the accident of a reorganisation.

### 3. Gather each clause, and say where it lives

Work through the ten clauses. For each, set the source marker before writing a word of content:

- **`reference`** where the organisation already keeps the answer — a decision, a value commitment, a
  policy, a service level, a delegation. Cite it by identifier and **do not restate it**: restated
  content drifts from its source, and the record then carries two answers.
- **`asserted`** only where the answer is stated nowhere else, with its provenance in the body.
- **`missing`** where the organisation has not established an answer. Write what is not known, never a
  plausible default.
- **`conflicting`** where sources disagree. Cite every source; do not choose between them.

### 4. Reference authority; never grant it

The **You may** clause is always a reference to the instrument that delegated the authority, or
`missing`. A limit that appears in a hand-over note with no instrument behind it is a finding, not a
clause. Responsibility does not imply authority, and eligibility or allocation does not create it.

### 5. Keep experience apart from practice

What has gone wrong before, and the organisation's own thresholds for what is severe or material, are
**You inherit**. How the work is normally done well is **You should**. A practice can then be
challenged without losing what the organisation learned.

### 6. Never write the records you reference

If a clause needs a decision, a value commitment or an authority instrument that does not exist, the
clause is `missing` and the absence is routed to the language that owns it. This skill never authors
the referenced record to give itself something to cite: a reference to material the OIR caused to
exist is no evidence the answer was held elsewhere.

### 7. Run the lifecycle

`draft → in-force → superseded`. Moving to `in-force` is the accountable owner's act
([`candidacy-and-ratification.md`](../../../../specification/candidacy-and-ratification.md)); the skill
proposes. **Supersede when the capability's inherited state changes** — a new control, a changed
threshold, a retired dependency, a decision that reshapes the work. **Never supersede because the
participant changed**: a new team, supplier or AI participant inherits the record in force. Records
are never edited in place.

## When to refuse

This skill refuses, and says which:

- **A record titled or scoped to a participant.** Rewrite it around the capability, or report that no
  capability was identified.
- **Authority asserted inline.** Draft the clause as `missing` and report the unsourced claim.
- **An empty clause.** Every clause carries a marker; silence is not `missing`.
- **A supersession whose only cause is a change of participant.**
- **A request to fill a gap or settle a conflict** so the record reads cleanly.
- **A claim that the record, or the skill, is part of the MTDR standard.** It is not, under TDR-0047.

## Quality checks

- Replace the participant with another team, a supplier and an AI participant in turn. Does every
  sentence survive?
- Does every `reference` name something identifiable, and does the body avoid restating it?
- Could a successor tell, from **You inherit** alone, what has gone wrong before and what the
  organisation counts as serious?
- Does **Escalate when** draw its thresholds from referenced authority and the organisation's own
  definitions, rather than from the drafter's judgement?
- Does **Evidence** say what performing the work must leave behind, not which tool records it?

## Anti-patterns

- **The team charter** — a record that describes who does the work under a capability's name.
- **The run book in disguise** — steps, screens and buttons. The OIR replaces no procedure.
- **Manufactured authority** — a limit stated because the work obviously needs one.
- **The onboarding dump** — everything a participant will ever know. Only the inherited state belongs.
- **The tidy record** — `missing` clauses filled because the gaps looked untidy.
- **Self-supplied references** — writing the decision a clause then cites.

## Scope note

This skill authors from the record package alone. Whether the OIR deserves to exist is decided by
TDR-0046's deletion attack and its independent reviewer, never by how well this skill works.
