---
name: governance-equivalence
description: Detect where two or more controls, forums or processes overlap — distinguishing same purpose from same evidence from same workflow from distinct mandated mechanisms that overlap legitimately. Use this skill when someone asks "are we doing this twice?", "why do the risk forum and the design authority both need this pack?", "can these two controls be merged?" or "how much of our control testing is duplicated?", and before any consolidation is contemplated. Overlap is a finding about evidence assembly, never a justification for retirement — two mechanisms required by different mandates may look identical and remain separately mandatory, and similarity alone can never establish that either can go.
---

# Governance Equivalence

Governance estates duplicate. The same evidence is assembled for four forums; the same property is
established by three controls; two committees ask the same question in different words. This skill
finds it — and refuses the conclusion everyone wants to draw from it.

Read [`governance-projection.md`](../../../validation/governance-projection.md) and
[`governance-rules.md`](../../../validation/governance-rules.md) first.

## Four kinds of overlap, never collapsed

| Overlap | Means | Usually implies |
|---|---|---|
| **Same purpose** | both mechanisms establish the same property | a real question about one of them |
| **Same evidence** | both consume substantially the same material | evidence reuse, not mechanism removal |
| **Same workflow** | both run substantially the same process | a process question, not a mandate question |
| **Distinct mandated mechanisms that overlap** | different obligations happen to require similar work | **nothing may be removed** |

The fourth is the one that matters, and it is the one a similarity measure cannot see. A model risk
control and an AI governance control may consume the same inventory, ask the same questions and produce
the same artefact, while being required by two different mandates with two different authorities.
Merging them because they look alike removes a mechanism somebody is required to hold.

## The rule

**Similarity alone cannot justify retirement** (GR-05, GR-10).

An equivalence finding is evidence that *evidence assembly* is duplicated. It supports `REUSE`,
`ABSORB` or `NARROW` where the mandate permits and the authority exists. It supports
`RETIRE_CANDIDATE` only as a **question to be answered after evidence reuse has actually been proven**,
and `RETIRE_CANDIDATE` is never executable (GR-10).

Before any disposition below `RETAIN`, the mandate must be traced
([`obligation-authority-trace`](../obligation-authority-trace/)). Where `mandatory_status` is `unknown`,
the disposition is `UNKNOWN` — not `RETIRE_CANDIDATE`, because an unlocated mandate is not an absent one.

## What to compare

Compare **jobs and evidence**, not names and documents. Two forums with different terms of reference
may perform the same job; two identically-named controls in different divisions may not. Work from
[`forum-reconstruct`](../forum-reconstruct/)'s job classes and evidence lists, and from the reconstructed
controls' `property_established`.

The strongest duplication signal is a **shared source artefact appearing in both mechanisms' evidence**
with each independently reassembling it. That is `FORUM_EVIDENCE_ASSEMBLY_OVERHEAD`, and it is the
finding with the clearest safe remedy: assemble once, consume twice, change no mandate.

## Output

`governance-finding` projections — `DUPLICATE_CONTROL`, `DUPLICATE_EVIDENCE`, `FORUM_JOB_DUPLICATION`,
`FORUM_EVIDENCE_ASSEMBLY_OVERHEAD` — each naming which of the four overlap kinds it is, and
`governance-disposition` projections carrying the mandate status, the basis for it, and what would have
to be proven before anything changed.

## When to refuse

- **Asked which of two duplicate controls to remove.** Report the overlap kind, the mandate status of
  each, and what reuse would have to be proven first. The choice is an authorised organisational
  decision.
- **Asked to score duplication.** A percentage invites exactly the reasoning the four-kind distinction
  exists to prevent.
- **Asked to treat an independent challenge function as duplication of the execution control it
  challenges.** They examine the same subject by design; that is the point of it (GR-15).

## Anti-patterns

- **Semantic similarity as the finding** — two controls "about" the same thing, with no comparison of
  what property each establishes or what mandate requires it.
- **Merging on the pack** — concluding two forums duplicate because they receive the same document,
  when one is exercising authority and the other is challenging it.
- **The efficiency read** — treating every overlap as waste. Deliberate redundancy in a control
  environment is sometimes the control.
- **Retirement by arithmetic** — a duplication count presented as a savings case, which is how a
  mandated mechanism gets removed by a spreadsheet.
