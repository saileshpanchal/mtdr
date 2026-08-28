# Identifier allocation register — public `TDR-*` namespace

**Normative.** This file is the single source of truth for public MTDR decision-record identifiers,
under [TDR-0034](TDR-0034-public-allocation-authority.md). No private repository governs, mirrors or
holds a "next free" for this sequence. A contributor allocates correctly from a clone alone.

## State

| Identifier | State | Note |
|---|---|---|
| TDR-0001 – TDR-0027 | allocated | governed representations in `decisions/` |
| **TDR-0028** | **burnt** | allocated on a branch subsequently dropped; never reusable |
| **TDR-0029** | **burnt** | allocated on a branch subsequently dropped; never reusable |
| **TDR-0030** | **burnt** | allocated on a branch subsequently dropped; never reusable |
| TDR-0031 – TDR-0033 | allocated | governed representations in `decisions/` |
| **TDR-0034** | **allocated** | public allocation authority — allocated by the commit introducing this register |
| **TDR-0035** | **allocated** | standards boundary — allocated by the commit introducing the register |
| **TDR-0036** | **allocated** | derivation projection and `show-me` — allocated by the commit introducing them |
| **TDR-0037** | **allocated** | release eligibility from standing governance — allocated by the commit introducing it |
| **TDR-0038** | **allocated** | distribution bundles and the layer boundary — allocated by the commit introducing them |
| **TDR-0039** | **allocated** | state-relative requirements — allocated by the commit introducing it |
| **TDR-0040** | **allocated** | canonical sequencing is not runtime orchestration — allocated by the commit introducing it |
| **TDR-0041** | **allocated** | information scope: access, use and disclosure — allocated by the commit introducing it |
| **TDR-0042** | **allocated** | changelog headings are not releases — allocated by the commit introducing it |
| **TDR-0043** | **allocated** | version-bound detached records — allocated by the commit introducing it |
| **TDR-0044** | **allocated** | transition-scoped obligations — allocated by the commit introducing it |
| **TDR-0045** | **allocated** | external validation follows publication — allocated by the commit introducing it |
| **TDR-0046** | **next free** | derived, not authoritative — see below |

## What the states mean

- **allocated** — exactly one governed representation exists in `decisions/`.
- **burnt** — the identifier was materially published into repository history but acquired no
  standing. No current governed representation may use it, and none ever may. See
  [TDR-0034](TDR-0034-public-allocation-authority.md) §2 and §4: *allocation is irreversible; standing
  is not.*
- **next free** — no representation exists, and the identifier exceeds every allocated and burnt
  identifier.

**Next free is derived, not authoritative.** The durable truth is which identifiers are allocated or
burnt. Next free is a computation over that state — `max(allocated ∪ burnt) + 1` — and is *proved* by
`tests/verify.py` rather than trusted. It appears in the table for human convenience only; if the
table and the computation disagree, the table is wrong.

## Rules

1. **Allocate in the same commit that introduces the record.** Any gap between allocation and artefact
   is a window in which they can diverge — which is how the collision that produced
   [TDR-0031](TDR-0031-reconcile-ratified-judgement-after-identifier-collision.md) happened.
2. **Update this register in that same commit.** Add the row; move the next-free row up.
3. **Never reassign.** Once an identifier has been materially published — a committed branch other
   actors or tooling could have observed — it is never reused, whether or not the proposed record
   gained standing. Privately computing that 0035 is next burns nothing; committing it does.
4. **Never mirror.** A private register may *reference* this file. It must never copy its state.
5. **`DAC-*` follows the same discipline**, and is not separately sequenced: a Decision Assurance Case
   takes the number of the TDR it assures. `DAC-0028`–`DAC-0030` are burnt with their TDRs.

## Enforcement

`tests/verify.py` checks this register against the repository on every run:

- every `allocated` entry has exactly one governed representation;
- no governed representation sits on a `burnt` identifier;
- every governed representation has exactly one `allocated` entry;
- `next free` has no representation and exceeds every allocated and burnt identifier;
- the stated next free equals `max(allocated ∪ burnt) + 1`;
- no `id` appears twice across records.

A boundary enforced by a document is a preference. This one is enforced by the repository.
