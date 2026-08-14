---
id: TDR-0027
title: Human ratification confers standing; evidence permits MTDR to represent it as accepted
status: accepted
template: full
decision_date: 2026-08-13
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0002, TDR-0015
confirmed_by_outcome: pending — review after two independent governance mechanisms have recorded ratification evidence, or 2027-02-13, whichever is sooner
---

# TDR-0027 — Human ratification confers standing; evidence permits MTDR to represent it as accepted

> **Ratified 2026-08-13.** Sailesh Panchal, as accountable owner and repository authority, ratified
> the architectural principle below after reviewing DAC-0027. The
> [attributable ratification evidence](evidence/TDR-0027-ratification-2026-08-13.md) preserves the
> act and its constraints. The ruling did not settle the portable evidence protocol, revision
> taxonomy, delegated-authority model or adversarial test suite; those remain owned decision debt
> and constrain automated promotion to `accepted`.

## Context — what was known at the time

The review of the unreleased v1.12–v1.21 branch at
`4754e1ae807f80b4bf6d7da8e23504b106c84363` exposed an ambiguity the current lifecycle cannot carry.
Candidate records on that branch were marked `status: accepted`, while their authors also described
them as not having entered the accepted register. Neither a Git commit, a merge, an agent writing
`accepted`, nor a store persisting a file can demonstrate that an authorised person exercised the
judgement the status claims.

The opposite answer is also incomplete. A private or verbal human assent with no durable,
attributable evidence may still be a valid organisational act, but a later reviewer cannot
distinguish it from assertion or reconstruction. An evidence failure does not give MTDR authority
to declare that a legally or organisationally valid decision never existed. MTDR must therefore
separate what creates standing from what permits the standard to assert that standing.

The question is therefore: **what combination of human act and evidence makes a proposed record a
standing organisational judgement?**

## Decision

The rule is:

> **Standing is conferred by an authorised human ratification of a defined candidate judgement.
> MTDR requires durable, attributable evidence sufficient to establish that ratification before a
> record may represent the judgement's standing as `accepted`.**

The human act supplies authority. Evidence makes the act reviewable. `accepted` represents that
standing; it neither creates standing nor proves it merely by appearing in frontmatter. A missing
or defective evidence record is an evidence and control failure. It prevents MTDR from asserting
`accepted`, but does not by itself prove that the underlying organisational decision never had
standing.

No commit, merge, database write, workflow transition, cryptographic operation, validator result,
register action or agent output **by itself** confers standing. Any of them may carry evidence of an
authorised human act. An agent may assemble that evidence and prepare a transition, but may neither
perform human ratification nor infer it from technical state.

This record specifies evidence semantics, not one ceremony or technology. Evidence must be
sufficient to establish the actor, the authority held at the time, the ratifying act and intent,
the defined candidate judgement that was ratified, and when the act occurred, in a form that
survives review. It may be produced by an offline process. The portable field set and protocol are
decision debt, not part of this judgement.

Ratification binds to the **substantive judgement reviewed**, not necessarily to an eternally
byte-identical file. A substantive change cannot inherit ratification and requires a new governed
act under the accepted immutability and supersession doctrine. A permitted non-semantic correction
may preserve standing when its provenance is retained. The taxonomy for distinguishing those
changes remains decision debt; until it is settled, an ambiguous change is treated as substantive.

The ratifier must possess the required authority at the time of ratification and the evidence must
make that attributable. How authority is granted, delegated, expires or is revoked belongs to the
authority model rather than this decision.

## Evidence

- **Business** — false standing lets proposals drive investment or policy without accountable
  judgement; unverifiable standing makes valid decisions indefensible later.
- **Architecture** — separating standing, evidence and representation preserves portability: a
  file, pull request, document workflow or database may carry evidence without becoming the source
  of organisational authority.
- **Regulatory** — the regulator-neutral accountability shape and its SM&CR worked example are
  recorded in [the TDR specification §8](../records/decision/specification/tdr.md#8-regulatory-framing--worked-examples-not-dependencies).
  This proposal adopts the evidence shape, not a dependency on that regime.
- **Operations** — repositories and document systems need a deterministic promotion gate, while
  organisations retain freedom to define who is authorised to pass it.
- **Customer** — indirect but material: decisions affecting customers must not acquire standing
  through an unattended agent or workflow transition.
- **Data** — ratification evidence must identify the substantive candidate judgement reviewed;
  otherwise later semantic changes can appear to have been approved when they were not.
- **External** — signatures, attestations and approval workflows are candidate evidence patterns,
  but no comparative source is yet cited and none is adopted as the sole ratification mechanism.

## Alternatives rejected

1. **The register creates standing when it accepts a record.** Rejected because storage would be
   mistaken for authority; a merge or API write could manufacture organisational judgement.
2. **Make durable evidence constitutive of organisational standing.** Rejected because an evidence
   or recordkeeping failure does not give MTDR authority to nullify an otherwise valid board,
   regulatory or delegated executive decision.
3. **Allow `accepted` on assertion that an unrecorded human assent occurred.** Rejected because
   MTDR cannot distinguish that assertion from reconstruction and therefore cannot represent the
   judgement as standing.
4. **The accountable owner field proves ratification.** Rejected because recording a person's name
   is an assertion about ownership, not evidence that the person reviewed or ratified this revision.
5. **Do nothing.** Rejected because the same candidate/accepted ambiguity has already allowed an
   unreleased branch to represent unratified judgement as accepted doctrine.

## Options foreclosed

- No tool, merge, database write, workflow transition or agent output can confer standing by itself.
- No MTDR record can represent standing as `accepted` on the basis of anonymous or
  judgement-ambiguous approval evidence.
- A register may govern collection, discovery and lineage, but cannot be treated as the source of
  the authority it records.
- MTDR cannot mandate one Git, signature, identity or workflow technology as the source of standing.
- Evidence failure cannot be used to declare that an externally valid organisational decision
  never existed; it means MTDR may not assert `accepted` until the failure is resolved.

## Consequences and review

Success means two different governance mechanisms, including one capable of representing an
offline act, can preserve attributable ratification evidence for a defined substantive judgement
while neither claims that persistence created authority. Review at the first two such uses or on
2027-02-13. DAC-0027 constrains automated promotion until portable evidence semantics,
semantic-change handling and adversarial evidence tests exist. Delegation and revocation are
learning inputs to the authority model, not reasons to expand this decision into that model.
