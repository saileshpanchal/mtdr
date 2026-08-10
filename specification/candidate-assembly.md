# CandidateAssembly

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

A proposal: *these contributions appear to concern one organisational object.* The hardest structure
here, and the one where reconstruction actually happens.

## The one rule

**Proximity is never identity.** Two contributions found near each other — same document, same
programme, same quarter, same author — are not thereby about the same object. Every assembly states
the basis on which it grouped, and co-occurrence alone is not an admissible basis.

This is the invariant the whole design protects. An assembly that silently merges two different value
commitments because they appeared in one steering pack has produced a record of something that never
existed, and it will look exactly as well-evidenced as a correct one.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `assembly_id` | Yes | Stable identifier |
| `target_object` | Yes | The object being reconstructed |
| `target_record_type` | Yes | The record type that would preserve it |
| `contribution_refs` | Yes | The contributions grouped |
| `grouping_basis` | Yes | Why these belong together. One or more admissible bases, each naming the evidence for it |
| `assembly_confidence` | Yes | Do these contributions concern the same object? |
| `missing_semantics` | Yes | Required roles for which no contribution exists. **Empty list is a claim**, not a default |
| `conflicts` | Yes | Competing contributions for one role that cannot both hold |
| `supersessions` | Yes | Where a later contribution replaces an earlier one for the same role |
| `unresolved` | Yes | Questions the evidence cannot settle |
| `status` | Yes | Always `candidate`. There is no other legal value |

## Admissible grouping bases

- **Explicit cross-reference** — one source names the other, or both name a common identifier
- **Entity match** — the same named commitment, programme, decision or artefact identifier
- **Ownership** — the same named accountable individual for the same subject matter
- **Temporal continuity** — a documented sequence, where later material refers to earlier state
- **Authority lineage** — the same governing decision or delegation

**Not admissible on its own:** same document, same folder, same meeting, same programme, same author,
same period, semantic similarity. Each may *support* a grouping alongside an admissible basis. None
establishes identity by itself, because each is satisfied by two genuinely different objects
discussed in one place — which is the normal condition of organisational material.

## Conflict and supersession are different

Both look like two contributions disagreeing about one role. They are not the same finding:

- **Supersession** — the later value replaces the earlier one, under the same authority lineage, with
  a documented temporal ordering. The organisation changed its mind, and both readings were correct
  when made.
- **Conflict** — two contributions that cannot both hold, with no ordering or no shared authority to
  resolve them. Someone is wrong, or they concern different objects.

Resolving a conflict is not this structure's job; **recording it accurately is.** An assembly that
quietly resolves a conflict by preferring the more recent value has asserted supersession without
evidence for it.

## Missing is a first-class result

Half the question is *what is still missing?* An assembly reports required roles with no contribution
as `missing_semantics`, and an empty list asserts that nothing is missing — a claim that can be wrong,
not a default state.

A candidate with missing mandatory semantics is still a legitimate candidate. It is not a failure; it
is an accurate account of what the material supports, and it tells the ratifying human exactly what to
go and find.

## What it never holds

- **No ratified status.** `status` is always `candidate`. Admission is a separate constitutional act —
  see [`candidacy-and-ratification.md`](candidacy-and-ratification.md).
- **No accountable owner as fact.** A contribution may propose one; only ratification confirms it.

## Anti-patterns

- **The silent merge** — grouping on similarity and recording a basis that sounds stronger than what
  was actually used.
- **The tidy candidate** — `missing_semantics` empty because the skill filled the gaps with plausible
  values rather than reporting them.
- **Supersession by recency** — assuming the later document wins, without shared authority lineage.
- **The single mega-assembly** — one candidate per document, which is document classification wearing
  reconstruction's clothing.
- **Conflict suppression** — dropping the losing contribution instead of recording the conflict, which
  destroys the evidence that the question was ever open.
