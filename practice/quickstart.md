# Quick start — building decision memory

You do not need a graph, a platform, or a new tool to get value from this standard. You need a place to
keep records, and the discipline to write good ones. This page gets you from nothing to a first useful
record set.

## What you are building

A durable, searchable memory of your organisation's consequential decisions — what was decided, why, on
what evidence, and how you will know whether it was right. Recording is drafting-assisted (a person, or an
AI assistant applying the [skills](../skills/)); the judgement is always a named human's.

Success is better decisions, not more records.

## Three rules that never bend

1. **A named individual owns every decision.** A committee endorses; it does not own. If no owner can be
   named, the record stays `proposed` and says what is missing. Never invent one.
2. **Only use sources you are cleared to use.** Before running confidential or regulated material through
   an AI assistant, confirm the environment is approved for that class of data. This is not a one-off
   blanket clearance — revisit it whenever the tool, its data handling, or who can see the output changes.
3. **The assistant never decides and never attests.** Its output is advice. A decision — and any statement
   that the organisation "complies" — is a named person's judgement, made with the evidence in front of them.

## The loop, per decision

1. Give the source — meeting minutes, a board paper, a policy, a business case — to the
   [decision-identification](../skills/decision-identification/SKILL.md) skill. Do not rewrite it; paste or
   attach it as it is.
2. Confirm which candidates are real decisions. Status updates, plans, action lists and opinions are not
   decisions; if reversing something costs less than recording it, do not record it.
3. Draft each record at the proportional template ([full, minimal or bare](../templates/)) with the
   [capture](../skills/problem-framing-and-decision-capture/SKILL.md) skill.
4. **Review** it: is it actually a decision; is the title right; is the owner identified; is enough context
   captured; is anything assumed that was not stated; would a stranger understand it in two years?
5. **Improve, do not just approve** — this is where the value is. Ask: what evidence is missing; what
   assumptions have we made; what alternatives were rejected; what risks did we accept; what would
   invalidate this decision?
6. Have the named owner confirm, then save the accepted record. Records are never edited afterwards; a
   changed judgement is a [superseding record](../spec.md#7-status-and-lifecycle).

## Start with one bounded area

Do not try to record everything at once. Pick one bounded, high-value area you own and understand well —
a single policy domain, one programme, one product line — and make its decisions explicit first. A small,
coherent, trustworthy record set is worth far more than a large scattered one, and it is what makes the
later capabilities (searching, cross-checking, assurance) actually work.

## Where to go next

- [The practice operating model](operating-model.md) — the phases, the two loops, and how records connect
  to controls, evidence and attestation.
- [Administration and assurance](administration-and-assurance.md) — connecting a record set for search,
  the validator, and how to test that an assistant applies the standard faithfully.
- [Deploying the standard as an agent](../agents/) — running the skills on the AI runtime you already have.
