---
name: obligation-authority-trace
description: Trace a governance mechanism, control or forum decision back to the obligation that requires it and the authority that may exercise, challenge, waive or amend it — asking who required this, who may act under it, who may overrule it, and what higher source constrains it. Use this skill when someone asks "why do we do this?", "who says?", "can we change this?", "who could sign this off?" or "what happens if we stop?", and before any disposition or evolution projection is produced, because a recommendation without an authority gate is a recommendation nobody can act on. It never infers that a mechanism is optional because its source cannot be located, and it never represents internal authority as able to amend a superior external obligation.
---

# Obligation and Authority Trace

Every governance mechanism exists because something required it. Often nobody currently working there
knows what. This skill asks, and reports honestly when the answer is not in the material.

Read [`governance-projection.md`](../../../validation/governance-projection.md) and
[`governance-rules.md`](../../../validation/governance-rules.md) first.

## The seven questions

Asked of every mechanism, control and forum decision:

```
Why does this exist?
Who required it?
Who may exercise it?
Who may challenge it?
Who may waive it?
Who may amend the governing requirement?
What higher source constrains it?
```

Each answer is a claim with its own epistemic assessment. Most estates answer three of the seven for
most mechanisms, and the unanswered four are the output.

## The rule that governs every unanswered question

**Do not infer that a mechanism is optional because its source cannot be located.**

This is the single most consequential error available to this skill, and it is attractive because it
resolves an uncomfortable gap into a clean finding. A control whose originating obligation cannot be
found is a control with an **unlocated obligation**. It is not internal, not discretionary, not
unnecessary and not removable. The correct output is `UNKNOWN` with the question asked and the scope
searched, plus an `AUTHORITY_GAP` or `OBLIGATION_GAP` finding (GR-05, GR-08).

The organisation may well have decided this for good reason twelve years ago. Absence of evidence in a
supplied corpus is evidence about the corpus.

## Superior sources

Where an external obligation is traced, record it as **inherited constraint held as projected
evidence-bearing state**, naming the source, its scope and the date it applied from.

**Do not force it into a decision record.** The organisation did not decide to be subject to it, and
representing an inherited obligation as an internal judgement destroys exactly the distinction that
makes it binding. There is currently no normative record family for inherited obligation — the `work`
package is a candidate — and that absence is a recorded irreducibility finding in
[TDR-0034](../../../../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md), not a
problem to be solved by using the nearest available shape.

**Internal authority cannot amend a superior external obligation** (GR-06). Where the material shows
an internal forum varying something it did not create, that is a finding — usually
`FORUM_AUTHORITY_AMBIGUITY` or `CONTRADICTORY_GOVERNANCE` — and never a reconstruction of a valid
amendment.

## De-facto authority

Material frequently shows someone exercising a power no document grants them. Record it as
**`INFERRED` authority-in-practice**, with the observed exercises as basis, and a finding of
`AUTHORITY_GAP`.

**Detection is not conferral** (GR-04). That a person has approved eleven exceptions is evidence that
they approved eleven exceptions. Whether they were entitled to is exactly what the trace could not
establish, and writing it down as though it did is how a reconstruction manufactures the authority it
was supposed to find.

## Output

`governance-finding` projections — `AUTHORITY_GAP`, `OBLIGATION_GAP`, `TRACEABILITY_GAP`,
`UNKNOWN_ORIGIN`, `POLICY_GAP`, `CONTRADICTORY_GOVERNANCE` — and the `required_authority` field that
every downstream disposition and evolution projection depends on. A recommendation whose authority gate
is unnamed cannot be acted on by anyone, which makes naming it the point rather than the paperwork.

## When to refuse

- **Asked to confirm a mechanism can be dropped** on the strength of an unlocated source.
- **Asked who "should" hold a power.** The trace reports who does and who may, from evidence. Who
  ought to is an organisational judgement and sits above the artefact boundary.
- **Asked to resolve a contradiction between two authority claims** by preferring the more senior
  source. Both go on the record (GR-09).

## Anti-patterns

- **The seniority default** — resolving an unlocated authority to the most senior name available.
- **Silent optionality** — an unlocatable obligation disappearing from the output rather than being
  reported as unlocated.
- **Obligation laundering** — an inherited external constraint recorded as an internal decision
  because there was a template for one.
- **Trace theatre** — answering all seven questions for every mechanism, which on a real estate means
  four of them were invented.
