---
id: TDR-0050
conforms_to: mtdr/decision/tdr@1.15.0
title: Admit a singleton grouping basis — one entry of one source, never one document
status: proposed
template: minimal
decision_date: 2026-11-07
accountable_owner: Sailesh Panchal
confidence: high
maturity: proposed
supersedes: none
derived_from: TDR-0018, TDR-0022, TDR-0043
confirmed_by_outcome: pending — confirm when a recovery outside this repository groups single-source material on the singleton basis and no reviewed assembly uses it across two entries; or 2027-05-07, whichever is sooner
---

# TDR-0050 — Admit a singleton grouping basis — one entry of one source, never one document

> **Proposed. No standing.** Approved in principle by the owner's return of 7 November
> ([evidence](evidence/TDR-0048-0049-owner-return-2026-11-07.md), ruling 5), which asked for the shared
> grouping semantics to be amended through the record that governs them. Nothing here reaches `main`
> while it is proposed.

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
   alike, ratified or returned on its own merits.

## Options foreclosed

- `singleton` never spans two entries, and is never satisfied by a document, meeting, folder or
  programme.
- No further basis is admitted that relates contributions by their container alone.

## Review

On the confirmation evidence, or 2027-05-07. An entry boundary that adopters repeatedly read
differently reopens the definition.
