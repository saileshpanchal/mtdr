---
name: identify-record-contributions
description: Inspect supplied organisational material and identify which fragments contribute to which governed records — without assuming any single source contains a complete record, and without inventing what is not there. Use this skill when pointing an assistant at board packs, minutes, business cases, spreadsheets or correspondence and asking "are there decisions or value commitments in here?", whenever someone says "we must have agreed this somewhere" or "find the commitments in this pack", and before any drafting skill runs. It emits evidence-backed contributions and reports what is absent — it never produces a record, and it never fills a gap with a plausible value.
---

# Identify Record Contributions

This skill reads organisational material and identifies **contributions** — spans of evidence that bear on a governed record — without assuming that any document contains a whole one. It is written for humans and usable by AI assistants. Read [`shared/README.md`](../../../specification/contribution-model.md) for the three interchange structures, and the record packages in [`records/`](../../../records) for the semantic roles each object defines. `reconcile-record-fragments` takes over once contributions exist.

## The one rule

**Emit nothing the source does not sustain.** A skill that returns no contributions from a document containing none has succeeded. The pressure to find something is the main way interpretation goes wrong, and what it produces — plausible, well-formatted, unfalsifiable — is exactly what a governed record must never carry.

## Reconstruction and the hindsight rule

`spec.md` requires that a record's context be written "in the present tense of the decision" and never reconstructed after the fact, and `decision-identification` names **retro-mining** as an anti-pattern. Both stand. This skill does not contradict them, and the distinction is precise:

- **Reconstructing reasoning is forbidden.** Inferring what someone must have considered, inventing the alternatives they probably weighed, or writing the rationale that would justify the outcome you can now see.
- **Recovering contemporaneous evidence is legitimate.** The reasoning was written down at the time — in a paper, a minute, a business case — and simply never became a record. Surfacing what those sources actually say is not hindsight.

The test is whether every value traces to material created at the time. Where the contemporaneous sources are silent, the answer is `missing_semantics`, never an inference. **Outcome knowledge is not evidence**: if a fact is known only because of what happened afterwards, it does not belong in a contribution to the decision's context.

## Process

### 1. Take the material as given

Do not judge whether a source is the "right" kind of document. Value commitments appear in spreadsheets, decisions appear in email, and constraints appear in appendices. The unit of work is the span, not the document.

### 2. Fragment before interpreting

Capture spans as [`SourceFragment`](../../../specification/source-fragment.md) first — verbatim, located, hashed. Preserve hedges and provisional markers exactly. "circa £10m (TBC)" is not "£10m", and the difference is usually the finding.

Err towards the sentence, and towards the paragraph where a sentence depends on it. A span too small to carry its own meaning will support a contribution it cannot actually sustain.

### 3. Ask what each fragment contributes, to which object

For each fragment, ask **"does this contribute to reconstructing a consequential decision, or an OVC, or something else?"** — not "which record does this document belong to". The question is about organisational objects; records are how those objects are preserved.

One fragment may contribute to several objects. *"The Committee approved the investment subject to maintaining complaints below 4%"* contributes to a decision, to an OVC whose review boundary is the threshold, and to the constraint relation between them. Emit all three. Forcing one reading per fragment loses the other two.

### 4. Name the semantic role from the record package

Roles are defined by the record package, never invented here. If the evidence matches no defined role, it contributes nothing — say so rather than creating a role to hold it.

### 5. Grade both confidences separately

`extraction_confidence` asks whether you read the words correctly. `epistemic_confidence` asks how strong the evidence for the claim is. They routinely diverge, and the case that matters most is **high extraction with low epistemic** — a business case stating a benefit plainly, with nothing behind it. Merging them hides precisely that. See [`shared/uncertainty.md`](../../../specification/uncertainty.md).

### 6. Report absence

Absence is a result, not a failure. A pack that contains a decision with no named owner and no stated alternatives has told you something true and useful. Record the gap; do not close it.

## Outputs

A set of [`SourceFragment`](../../../specification/source-fragment.md) and [`RecordContribution`](../../../specification/record-contribution.md) structures, validating against [`schemas/shared/`](../../../schemas/shared/). Plus a short plain summary a stranger could follow — which objects appear to be present, on what evidence, and what is conspicuously absent.

No record. No candidate. Assembly is the next skill's judgement, and grading it separately is what keeps it examinable.

## Quality checks

- Read each fragment's content alone. Does it sustain the interpreted value without the rest of the document? If not, reference more fragments.
- Does every contribution name a role the record package actually defines?
- Do the two confidences ever differ? If they are always equal, one is not being assessed.
- Is any value supported only by knowing how things turned out? Remove it.
- Would a reader who disagreed with a contribution be able to go to the span and argue? If not, the provenance is too weak.

## When to refuse

- **The source is not the organisation's material.** This skill reads what an adopter supplies; it does not go looking.
- **No span sustains a contribution.** Return nothing, and say what you looked for.
- **The material is a summary of other material.** Prefer the original. A contribution traced to a summary of a board paper is provenance to a paraphrase, and inherits every edit the summariser made.

## Anti-patterns

- **Document classification** — deciding "this is a decision document" and extracting a whole record from it. The unit is the fragment.
- **The confident invention** — high extraction confidence on a value no span states.
- **Hindsight contamination** — importing outcome knowledge into a decision's context because it makes the record read better.
- **Role invention** — creating a semantic role because the evidence fitted none.
- **Gap filling** — supplying a plausible owner, date or baseline where the source is silent.
- **The tidied fragment** — hedges removed because they made the extraction look weaker.
- **One reading per fragment** — stopping at the first object a span contributes to.

## Scope note

This skill identifies contributions from material an adopter supplies. How that material is located, indexed, retrieved, chunked or ranked is downstream implementation, deliberately outside this standard (see TDR-0002, TDR-0018). The skill makes no assumption about storage, runtime, graph representation or orchestration.
