---
name: challenge-record
description: Challenge a candidate record before it reaches the person asked to ratify it — unsupported interpretation, missing mandatory semantics, provenance gaps, unresolved conflict, and claims the evidence does not carry. Use this skill on every candidate a drafting skill produces, whenever someone asks "is this actually supported?", "what is wrong with this draft?" or "would this survive a challenge?", and always before ratification. One skill serves every record type, because the structural failures are common; the role list and admission test load from the record package.
---

# Challenge Record

This skill attacks a candidate record. It is written for humans and usable by AI assistants. Read
[`shared/candidacy-and-ratification.md`](../../../specification/candidacy-and-ratification.md), then the relevant
record package in [`records/`](../../../records) for its roles and admission test.

It is deliberately one skill rather than one per record type. The failures that matter here —
interpretation unsupported by evidence, gaps quietly filled, conflicts quietly resolved — are properties
of *interpretation*, not of any particular record. Only the role list and admission test differ, and
both load from the package.

## The one rule

**Assume the draft is wrong and try to show it.** A challenge that sets out to confirm the record will
confirm it. The useful question is not "is this reasonable?" — a fabricated record is always reasonable
— but "which sentence here would I be unable to defend if the owner disputed it?"

## What this is not

Not an assurance case. A package may define an assurance discipline that challenges a record's
*consequences* — the decision package's DAC is the worked example — and that is a different act with
its own record, found through the package in [`records/`](../../../records/). This skill challenges
whether **the candidate faithfully represents its evidence.** A record can pass here and still
describe a terrible decision, correctly.

## Process

### 1. Walk every rendered value back to a span

For each statement in the draft, find the contribution, then the fragment, then the locator. Any
statement that cannot be walked back is **unsupported** — the single most important finding this skill
produces, because unsupported content is indistinguishable from supported content by reading.

### 2. Read each span alone

Without the surrounding document, does the span sustain what the record says? Spans routinely support
something weaker, hedged, or conditional than the sentence they produced.

### 3. Hunt for tense and modality shifts

"Will reduce" rendered as "reduced". "Proposed" rendered as "agreed". "The committee noted" rendered as
"the committee approved". These are small edits with large consequences, and they travel in one
direction — towards the record being more definite than its evidence.

### 4. Test the grouping

Take the candidate's `grouping_basis` and try to break it. Different beneficiaries, incompatible
baselines, separate authority lineages. **If you can construct a plausible account in which these are
two objects, say so** — even where the merge still looks more likely.

### 5. Check the gaps are gaps

Every mandatory role either evidenced or visibly missing. A field reading "not applicable", "TBC" or
"standard practice" where the source was silent is a filled gap wearing a gap's clothing.

### 6. Check for hindsight

Does any part of the context depend on knowing how things turned out? Compare each context
contribution's `source_time` against the decision date.

### 7. Test the confidences

Are extraction and epistemic confidence ever different? Uniform confidence across a whole candidate
means one of them was not assessed.

## Outputs

A findings list, most serious first. For each: the statement challenged, what the evidence actually
supports, and what would resolve it. Plus an overall judgement — **fit to propose**, or **not fit to
propose**, with reasons.

"Not fit to propose" is a normal and useful outcome. It is much cheaper than a ratified record nobody
can defend.

## Quality checks

- Did the challenge examine every rendered value, or only the ones that looked doubtful?
- Is each finding actionable — naming what would resolve it?
- Was the grouping actively attacked, or merely accepted?
- Would an unsympathetic reader find something this challenge missed?

## When to refuse

- **The candidate carries no provenance.** There is nothing to challenge against; return it.
- **Asked to approve rather than challenge.** This skill does not ratify, and cannot be used to confer
  standing on a record.

## Anti-patterns

- **Confirmation reading** — checking the record is coherent rather than supported. Fabrications are
  coherent.
- **Cosmetic findings** — tone and formatting raised while an unsupported claim passes.
- **Deference to volume** — a long evidence list treated as strong evidence.
- **Single-pass challenge** — stopping at the first finding rather than examining every value.
- **Accepting the grouping** — the hardest judgement in the candidate, and the one most often waved
  through.
- **Challenging the decision instead of the record** — that is the DAC's work, not this.

## Scope note

This skill challenges a candidate against its own evidence and its record package. Challenging a
decision's consequences is the Decision Assurance Case's work; enforcing anything at all is outside this
standard entirely (see TDR-0002, TDR-0018).
