---
name: reconcile-record-fragments
description: Group contributions gathered from different sources into candidate records without treating proximity as identity — stating the grouping basis, separating supersession from conflict, and reporting what remains missing or unresolved. Use this skill whenever contributions come from more than one source, whenever someone asks "is this the same commitment as that one?", "which version is current?" or "why do these two numbers disagree?", and before drafting any record that draws on multiple documents. It refuses to merge on similarity alone, and it never resolves a conflict the evidence cannot settle.
---

# Reconcile Record Fragments

This skill decides which contributions concern the same organisational object, and produces candidates. It is written for humans and usable by AI assistants. Read [`shared/identity-and-grouping.md`](../../shared/identity-and-grouping.md) and [`shared/candidate-assembly.md`](../../shared/candidate-assembly.md) before using it. `identify-record-contributions` produces its input; the drafting skills consume its output.

## The one rule

**Proximity is never identity.** Two contributions found near each other — same document, same programme, same quarter, same author — are not thereby about the same object. Every grouping states the basis it relied on, and co-occurrence is not one.

This is the invariant the whole design protects. A wrong merge produces a coherent, fully provenanced record of an object that never existed, and nothing about its appearance distinguishes it from a correct one. Every other failure here is recoverable by reading the record. This one is not.

## Process

### 1. Start from separate

The default is that two contributions concern different objects. **Grouping is a claim requiring evidence; separation is not.** This asymmetry is deliberate — an unmerged pair costs a human two minutes of review, and a wrongly merged pair costs the organisation a false record it will act on.

### 2. Find an admissible basis, and name its evidence

Admissible: explicit cross-reference · entity match · ownership · temporal continuity · authority lineage. Record the *actual* identifier, cross-reference or named owner — not the basis type alone. "Entity match" is not a basis; "both name commitment OVC-Retail-14" is.

Not admissible on its own: same document, folder, meeting, programme, author or period, and semantic similarity. Each is satisfied by two genuinely different objects discussed in one place, which is the normal condition of organisational material.

### 3. Seek the reason they are two things

Before accepting a grouping, look for what would break it — different beneficiaries, incompatible baselines, different authority lineages, measures that overlap but do not agree. **A grouping that has not been tested against its own negation has not been tested.** Record what you looked for.

### 4. Separate supersession from conflict

Both look like two contributions disagreeing about one role. They are different findings:

- **Supersession** — the later value replaces the earlier, under the same authority lineage, with documented ordering. The organisation changed its mind, and both readings were correct when made.
- **Conflict** — they cannot both hold, and there is no ordering or shared authority to resolve them. Someone is wrong, or these are two objects.

Date order alone establishes neither. Preferring the more recent value is asserting supersession without evidence for it.

### 5. Report missing semantics

List required roles with no contribution. An empty list is a claim that nothing is missing, and it can be wrong. **A candidate with missing semantics is still a legitimate candidate** — it is an accurate account of what the material supports, and it tells the ratifying owner exactly what to go and find.

### 6. Leave the unsettled unsettled

Where evidence does not decide, put the question in `unresolved`. Two candidates, or one candidate with an open question, are both better outcomes than a confident merge.

### 7. Grade assembly confidence

Separately from the contributions' own confidences. High extraction and high epistemic confidence on every contribution says nothing about whether they concern the same commitment.

## Outputs

[`CandidateAssembly`](../../shared/candidate-assembly.md) structures validating against [`shared/schema/candidate-assembly.schema.json`](../../shared/schema/candidate-assembly.schema.json), each with `status: candidate` — the only legal value. Plus a plain summary naming what was grouped, on what basis, what was deliberately kept apart, and what remains open.

## Quality checks

- Could a reader disagree with each grouping basis? A basis so vague nobody could dispute it ("related programme work") is not a basis.
- Is every supersession backed by shared authority lineage, not just date order?
- Are conflicts recorded rather than silently resolved by dropping the loser?
- Does the candidate count look suspiciously tidy? Collapsing candidates because a long list feels like failure is the most common way this skill goes wrong.
- Would splitting a candidate in two be defensible on the same evidence? If so, say so in `unresolved`.

## When to refuse

- **Merging on similarity alone**, however strong. Report two candidates.
- **Resolving a conflict the evidence cannot settle.** Record it and leave it.
- **Assigning an accountable owner** because one appears plausible. A proposed owner is an interpretation like any other, and only ratification confirms it.
- **Emitting anything beyond `candidate`.** The skill proposes; the organisation ratifies — see [`shared/candidacy-and-ratification.md`](../../shared/candidacy-and-ratification.md).

## Anti-patterns

- **The silent merge** — grouping on similarity, then recording a basis that sounds stronger than what was used.
- **Merge to reduce the count** — a long list of honest candidates beats a short list of invented ones.
- **Supersession by recency** — newest source assumed current.
- **Conflict suppression** — dropping the losing contribution, destroying the evidence that the question was open.
- **The single mega-assembly** — one candidate per document, which is document classification wearing reconciliation's clothing.
- **Premature identity** — fixing the grouping from the first two contributions, then fitting later ones to it.
- **The tidy candidate** — `missing_semantics` empty because the gaps were filled.

## Scope note

This skill reconciles contributions using nothing beyond the contributions themselves and the record packages' role definitions. Implementations holding records in a connected store may resolve identity against existing entities, prior records or an organisational graph — that resolution is downstream implementation, deliberately outside this standard (see TDR-0002, TDR-0018).
