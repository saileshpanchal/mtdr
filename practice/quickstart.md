# Quick start — building decision memory

You do not need a graph, a platform, or a new tool to get value from this standard. You need a place to
keep records, and the discipline to write good ones. This page gets you from nothing to a first useful
record set.

## What you are building

A durable, searchable memory of your organisation's consequential decisions: what was decided, why, on what
evidence, and how you will know whether it was right. A person can draft a record, and so can an AI assistant
applying the [skills](../skills/); the judgement is always a named human's.

Success is better decisions, not more records.

## Which route this page is

This page teaches writing a record at the time of a decision, with the person who holds the reasoning taking
part. The decision package calls this the **authoring path**.

Recovering a decision that was made in the past and never recorded at the time is the **interpretation path**:
reconstruction from the material that survives. It has its own rule, "Recover what can be evidenced. Preserve
what cannot. Never turn a contemporary interpretation into historical authority", and what it produces is "a
retrospective candidate with no standing": a proposal nobody has ratified, never a record by default. For that
route, start at the [`recover-decision-records`](../records/decision/skills/recover-decision-records/SKILL.md)
skill and [historical recovery](../specification/historical-recovery.md), which is accepted under TDR-0048.

This page does not yet route someone holding minutes of a past decision to historical recovery
([#15](https://github.com/saileshpanchal/mtdr/issues/15)). The
[README](../README.md#two-routes-to-the-same-record) sets the two routes side by side.

## Three rules that never bend

1. **A named individual owns every decision.** A committee endorses; it does not own. If no owner can be
   named, the record stays `proposed` and says what is missing. Never invent one.
2. **Only use sources you are cleared to use.** Before running confidential or regulated material through
   an AI assistant, confirm the environment is approved for that class of data. This is not a one-off
   blanket clearance: revisit it whenever the tool, its data handling, or who can see the output changes.
3. **The assistant never decides and never attests.** Its output is advice. A decision — and any statement
   that the organisation "complies" — is a named person's judgement, made with the evidence in front of them.

## The loop, per decision

Each skill named below is a `SKILL.md` file: a written procedure you can follow by hand, or have an AI
assistant apply ([deploying the standard as an agent](../skills/packaging/)).

If you install the `decision` package for an assistant, note that it is built for recovering past
decisions. It includes decision-identification and validate-record, but not
problem-framing-and-decision-capture, the skill step 3 uses to write the record. Point the assistant at
that skill in the repository instead ([#15](https://github.com/saileshpanchal/mtdr/issues/15)).

1. Give the source for the decision being made now — the paper going to the meeting, the draft
   minutes, the business case, the policy being changed — to the
   [decision-identification](../records/decision/skills/decision-identification/SKILL.md) skill. Do not
   rewrite it; paste or attach it as it is. If the decision was taken in the past and you are working
   only from what survives, this is the interpretation path, above, not this loop.
2. Confirm which of the decisions it proposes are real. Status updates, plans, action lists and opinions are not
   decisions; if reversing something costs less than recording it, do not record it.
3. Draft each record at the template that matches what the decision would cost to reverse
   ([full, minimal or bare](../records/decision/templates/)), with the
   [capture](../records/decision/skills/problem-framing-and-decision-capture/SKILL.md) skill. The full
   template asks for the evidence considered under seven headings: business, architecture, regulatory,
   operations, customer, data and external. For a full record, collect what you have under each before
   you draft.
4. **Review** it: is it actually a decision; is the title right; is the owner identified; is enough context
   captured; is anything assumed that was not stated; would a stranger understand it in two years?
5. **Improve, do not just approve** — this is where the value is. Ask: what evidence is missing; what
   assumptions have we made; what alternatives were rejected; what risks did we accept; what would
   invalidate this decision?
6. Have the named owner confirm the record. Confirming changes its `status` from `proposed` to
   `accepted`. Save it with the next free identifier in your organisation (`TDR-0001`, `TDR-0002`, …)
   at the start of its file name, as in `TDR-0001-retain-the-servicing-channel.md`: an identifier is
   unique within an organisation, not globally, and must match the file name. Records are never edited
   afterwards; a changed judgement is a
   [superseding record](../records/decision/specification/tdr.md#7-status-and-lifecycle).

## Check the record

The shared [`validate-record`](../skills/shared/validate-record/SKILL.md) skill checks a record against its
specification: required fields, allowed values, lineage references that resolve, and agreement between
identifier and filename. It checks conformance only. A record can validate and still be wrong.

No command yet checks a record written by this loop. Work through the `validate-record` checklist by
hand, or have an assistant apply it. The record's YAML header must also satisfy
[`tdr.schema.json`](../records/decision/schema/tdr.schema.json), which any JSON Schema validator can
check once the header is converted to JSON.

The command `uv run python -m mtdr_validation <folder>` does a different job: it assesses the output of a
recovery ([`mtdr_validation/`](../mtdr_validation/README.md)). Run on a folder of TDRs, it reports
`0 artefact(s) assessed`, which is not a pass.

## Start with one bounded area

Do not try to record everything at once. Pick one bounded, high-value area you own and understand well —
a single policy domain, one programme, one product line — and make its decisions explicit first. A small,
coherent, trustworthy record set is worth far more than a large scattered one, and it is what makes the
later capabilities (searching, cross-checking, assurance) actually work.

## Where to go next

- [The decision package](../records/decision/README.md) — the specification, the templates, worked examples, and
  the skills on each route.
- [Using MTDR with your framework](using-mtdr-with-your-framework.md) — reconstruction across a body of
  existing documents.
- [The practice operating model](operating-model.md) — the phases, the two loops, and how records connect
  to controls, evidence and attestation.
- [Administration and assurance](administration-and-assurance.md) — connecting a record set for search,
  the validator, and how to test that an assistant applies the standard faithfully.
- [Deploying the standard as an agent](../skills/packaging/) — running the skills on the AI runtime you already have.
