---
id: TDR-0050
conforms_to: mtdr/decision/tdr@1.15.0
title: Admit a singleton grouping basis — one entry of one source, never one document
status: accepted
template: minimal
decision_date: 2026-11-07
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0018, TDR-0022, TDR-0043
confirmed_by_outcome: pending — confirm only when a recovery outside this repository groups single-source material on the singleton basis and no reviewed assembly uses it across two entries. 2027-05-07 is the review date; reaching it confirms nothing
---

# TDR-0050 — Admit a singleton grouping basis — one entry of one source, never one document

> **Accepted on 2026-11-27** by the owner's ratification ([evidence](evidence/TDR-0050-ratification-2026-11-27.md)). Answers ruling R5 of the owner's return of 7 November
> ([evidence](evidence/TDR-0048-0049-owner-return-2026-11-07.md)): *"Approve an explicit singleton
> grouping basis"*, and *"Amend shared grouping semantics through the appropriate governing TDR, with
> regression fixtures."* No existing TDR enumerates the grouping bases. This record proposes to be the
> one that governs the singleton basis, and the owner is asked to confirm that it is the appropriate
> one.
>
> **Corrected on 26 November 2026, after an [independent review](evidence/recovery-records-review-2026-11-26.md)**:
> the ruling is quoted rather than glossed, and this record says what already relies on it. It stays
> proposed.
>
> **On 27 November 2026 the owner directed** ([preserved](evidence/TDR-0048-0049-0050-owner-dispositions-2026-11-27.md)) that the assistant's
> recommendations proceed: that this is the governing record ruling R5 asked for, and that its
> confidence be medium, given one trial and an entry boundary no validator can check. The direction
> was an engineering instruction and decided nothing. It stays proposed.

## Context — what was known at the time

A `CandidateAssembly` must state at least one admissible grouping basis
([TDR-0018](TDR-0018-interpretation-skills-and-the-artefact-boundary.md),
[`candidate-assembly.md`](../specification/candidate-assembly.md)), and *same document* is
inadmissible on purpose: two different objects discussed in one place is the normal condition of
organisational material. The five admissible bases all relate one source to another. None fits a
decision whose every contribution comes from a single source — yet FIX-004 has always expected such a
candidate, and said its basis "may cite a single source". An adopter trial of decision recovery on
7 November produced single-source candidates throughout, and each had to cite a basis that described
something it was not.

## Decision

**Add `singleton` as a sixth admissible grouping basis, defined by the entry, not the document.**

1. **What it means.** Every contribution in the assembly comes from **one fragment, or one contiguous
   entry of one source** — one minute item, one email, one numbered section — and the evidence names
   the source and the entry.
2. **What it never means.** It is not *same document*. A document, meeting or pack that records two
   objects is a singleton for neither, reconciliation still splits an entry that records two, and a
   contribution from a second entry needs a basis that crosses entries.
3. **What is checked.** A historical candidate whose assembly cites `singleton` fails if its
   contributions rest on fragments from more than one `source_ref`. Whether the fragments lie within
   one entry is a judgement no validator can make, and the specification says so.
4. **Versioning.** [`candidate-assembly.md`](../specification/candidate-assembly.md) moves to 1.1.0, an
   additive minor version under [TDR-0043](TDR-0043-version-bound-detached-records.md): every assembly
   valid under 1.0.0 stays valid.

## Alternatives rejected

1. **Admit *same document*.** Rejected: its inadmissibility is the invariant the assembly exists to
   protect, and a document is the commonest container of two objects.
2. **Let a single-source assembly omit its basis.** Rejected: the basis is required so that an
   assembly always states why its contributions belong together; an omission would be a default, not a
   claim.
3. **Decide it inside the recovery doctrine (TDR-0048).** Rejected: single-source assemblies are not
   peculiar to historical material, and the basis must be available to value and decision recovery
   alike. It is decided on its own merits, but not independently of TDR-0048, which already relies on
   it (below).

## Options foreclosed

- `singleton` never spans two entries, and is never satisfied by a document, meeting, folder or
  programme.
- No further basis is admitted that relates contributions by their container alone.

## Where this record goes beyond the owner's ruling

- **E13 — The unit is the entry, not the document.** *The drafter's.* Ruling R5 approved "an explicit
  singleton grouping basis" and did not define it. One fragment or one contiguous entry of one source,
  never one document, is the drafter's definition.

## What already relies on it

TDR-0048's text and an accepted fixture use this basis already: integrity rule 8 of
[`historical-candidate.md`](../specification/historical-candidate.md) and the check that enforces it;
the recovery fixtures FIX-522 and FIX-523; the `singleton` value in
[`candidate-assembly.schema.json`](../schemas/shared/candidate-assembly.schema.json); the shared
[`reconcile-record-fragments`](../skills/shared/reconcile-record-fragments/) skill; and
[FIX-004](../records/decision/fixtures/FIX-004-complete-in-one-source.md), which now expects it. So it is
ratified first, in the order the assistant recommended and the owner set on 27 November: TDR-0050,
DAC-0048, TDR-0048, TDR-0049 ([DAC-0048](DAC-0048-historical-recovery-doctrine.md#decision-debt)).


## Review

On the confirmation evidence, or 2027-05-07. An entry boundary that adopters repeatedly read
differently reopens the definition.
