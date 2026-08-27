---
id: TDR-0034
conforms_to: mtdr/decision/tdr@1.15.0
title: Govern public TDR identifier allocation in this repository, and make allocation irreversible
status: accepted
template: full
decision_date: 2026-08-16
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0001, TDR-0020, TDR-0027, TDR-0031
confirmed_by_outcome: pending — review when a contributor unknown to the author has allocated a public identifier without consulting any private repository, or 2027-02-16, whichever is sooner
---

# TDR-0034 — Govern public TDR identifier allocation in this repository, and make allocation irreversible

## Context — what was known at the time

The public `TDR-*` sequence was governed by a register held in a **private** repository. That register had been correct when written and had since fallen sixteen identifiers behind: it recorded "allocated 0001–0017, next free 0018" while this repository had reached TDR-0033.

In that window a real collision occurred. Two branches allocated the same identifier to different substantive judgements, and [TDR-0031](TDR-0031-reconcile-ratified-judgement-after-identifier-collision.md) was required to reconcile a ratified human act with an accepted record occupying the number it had claimed. The reconciliation succeeded, and its cost — a full constitutional decision, an assurance case, three evidence artefacts and a permanent crosswalk — is the measure of what the arrangement was worth.

The failure was structural, not administrative. **A contributor could not consult the register that governed the identifier they were about to allocate**, because it was in a repository they had no access to. Every condition for collision was present by design: an authoritative allocator invisible to the people doing the allocating.

That also violates a boundary this repository has already committed to. [TDR-0020](TDR-0020-open-organisational-record-repository-boundary.md) states that someone must be able to clone this repository and produce conformant records **without knowing that any particular consumer exists**. A public sequence governed by a private file fails that test directly.

Two mature precedents bear on where allocation belongs. `adr-tools` numbers decisions from the log held with the project; the Rust RFC process derives identity from its own public process. Both embody one principle: **allocation authority sits inside the contribution system that can actually see and arbitrate collisions.** Rust's use of pull-request numbers is not adopted here, for a reason specific to this standard — MTDR identifiers are durable record identities that must survive GitHub, offline operation and other hosting. The repository owns its namespace; a hosting platform is one execution environment.

## Decision

**1. Public namespace, public authority, one source of truth.** This repository governs `TDR-*` and `DAC-*`. Private repositories govern only their own namespaces. **No normative mirrors:** a private register may *reference* the public namespace but must never copy its state, because two records of one truth is precisely the drift this standard exists to eliminate.

[`decisions/ALLOCATION.md`](ALLOCATION.md) is the normative human-readable allocation register. **Allocation occurs in the same commit that introduces the record**, so identity and artefact cannot drift independently. A contributor never inspects a private repository to make a conformant contribution.

**2. Allocation is irreversible; standing is not.**

> **Once a TDR identifier has been materially published into repository history, it is never reassigned, irrespective of whether the proposed record subsequently gains standing.**

These are different properties, and TDR-0031's ruling that reservation confers no standing does **not** imply that unreserved identifiers may be recycled:

- **Standing** — whether a record is constitutionally recognised. Governed, and revocable in the sense that a proposal may never acquire it.
- **Identity** — whether an identifier has already been used to refer to a particular attempted judgement. Acquired on publication, permanently.

*Materially published* means a committed branch that other actors or tooling could have observed. Privately computing that 0035 is next, or typing an identifier before committing it, burns nothing.

**3. The repository enforces this, not a document.** Allocation invariants are machine-checked, defined by state:

- `allocated` → exactly one governed representation exists;
- `burnt` → no current governed representation may use it;
- `next-free` → no representation exists, and it exceeds every allocated and burnt identifier;
- every governed representation → exactly one corresponding allocated entry.

**Next-free is derived, not authoritative.** The durable truth is which identifiers are allocated or burnt; next-free is a computation over that state, and is proved to equal `max(allocated ∪ burnt) + 1` rather than trusted.

**4. TDR-0028, TDR-0029 and TDR-0030 are burnt.** They were allocated to proposed records on a branch subsequently dropped. They acquired address but never standing, and may survive in commits, links, local clones or later forensic reconstruction. Reusing them would make TDR-0030 mean one thing in historical evidence and another here — the exact ambiguity TDR-0031 was written to resolve.

**History may contain failed propositions; it must never contain ambiguous identities.**

## Evidence

- **Business** — a standard whose identifier allocation requires private access is not adoptable by anyone outside the private estate, which caps adoption at the author's own practice and contradicts TDR-0001.
- **Architecture** — the invariants are mechanically checkable, and are checked. A boundary enforced by a document is a preference; one enforced by the repository is a boundary. `adr-tools` and the Rust RFC process independently converge on allocation-inside-the-contribution-system.
- **Regulatory** — not material to this decision.
- **Operations** — an external contributor can now allocate correctly from a clone alone. The private register's maintenance burden for the public sequence disappears rather than being renegotiated.
- **Customer** — not material at repository level.
- **Data** — none beyond the records themselves.
- **External** — the collision is the strongest evidence available, and it is this repository's own: the arrangement failed in practice, was expensive to repair, and the repair is documented in TDR-0031.

## Alternatives rejected

1. **Bring the private register current and keep it authoritative.** Rejected: it repairs the symptom and preserves the cause. The register would be correct until the next lapse, and contributors still could not see it.
2. **Public allocation with a private normative mirror.** Rejected: two records of one truth. The mirror would drift exactly as the original did, and there would be no principled way to say which was wrong.
3. **Derive identifiers from pull-request numbers, as the Rust RFC process does.** Rejected on a property specific to this standard: MTDR identifiers are durable record identities that must survive GitHub, offline operation and alternative hosting. Binding identity to one platform's counter would make the namespace a hostage to that platform.
4. **Reclaim 0028–0030 as free.** Strictly permitted by TDR-0031, since no governed representation occupies them — and rejected. Three integers cost effectively nothing; referential ambiguity in a governance system costs a great deal.
5. **Allocate in a separate commit from the record.** Rejected: any gap between allocation and artefact is a window in which they can diverge, which is how the collision happened.

## Options foreclosed

- No private repository may again govern, mirror or hold a "next free" for the public sequence.
- Burnt identifiers can never be reclaimed without superseding this record.
- Identity can never be derived from a hosting platform's numbering without superseding this record.
- Allocation can never be separated from the commit that introduces the record.

## Consequences and review

Success looks like a contributor unknown to the author allocating a public identifier correctly from a clone alone, and the invariants catching a duplicate before it reaches main rather than after.

This record repairs an implementation that was violating an existing boundary rather than establishing a new one — [TDR-0020](TDR-0020-open-organisational-record-repository-boundary.md) already required exactly this, and the private allocator was inconsistent with it throughout.

The wider discipline these rulings share, worth stating once because the next language package will need it: **identity is persistent, standing is governed, conformance is typed, evidence is contextual, and absence of proof remains visible.**

Review at the confirmed-by-outcome trigger, or when the first identifier is allocated by someone other than the author.
