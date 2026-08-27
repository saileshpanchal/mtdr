---
id: TDR-0043
conforms_to: mtdr/decision/tdr@1.15.0
title: A record binds itself to the specification that governs it
status: proposed
template: full
decision_date: 2026-08-27
accountable_owner: Sailesh Panchal
confidence: high
maturity: proposed
supersedes: none
derived_from: TDR-0032, TDR-0033, TDR-0039
confirmed_by_outcome: pending — confirm when a record has been read and validated outside this repository by someone holding nothing but the file, or 2027-02-27, whichever is sooner
---

# TDR-0043 — A record binds itself to the specification that governs it

> **Proposed.** No standing. Discharges [DAC-0032](DAC-0032-typed-multi-object-conformance.md)
> constraint 2, the one obligation deliberately deferred past `baseline-2026-08-21`.

## Context — what was known at the time

[TDR-0032](TDR-0032-typed-multi-object-conformance.md) established that **the smallest independent
conformance claim is a version-bound record**. DAC-0032 constraint 2 turned that into an obligation:
*before release, a detached record can identify and durably resolve its record type, applicable
specification identity and version, and validate without repository-private interpretation.*

It was not met, and the obligations register said so without softening it: *"Unaddressed, and not
partially addressed… the record's own binding is a change to the record schemas and has not been
made."*

The gap is precise. Each package manifest already binds record type to specification and version —
`records/decision/package.yaml` names TDR at 1.15.0 and DAC at 1.12.0. **A detached record cannot
reach the manifest.** One file, in a ticket or an export, carries `id`, `title`, `status` and no
statement of what it is a conforming instance *of*. Resolving it requires knowing where it came
from, which is exactly the repository-private interpretation the constraint forbids.

That condition is ordinary rather than exotic. Records are pasted into papers, attached to tickets,
exported into other estates and recovered from backups years later. The register is
[optional](TDR-0032-typed-multi-object-conformance.md) — it is a collection mechanism, not a
prerequisite for conformance — so a record outside one is not a degraded case. It is the case the
standard said it supported.

## Decision

**Every record may carry one field binding it to the specification that governs it**, in a scheme
published at [`specification/record-identity.md`](../specification/record-identity.md):

```yaml
conforms_to: mtdr/decision/tdr@1.15.0
```

`mtdr/<package>/<record>@<version>` — the standard, the organisational language, the record type,
and the specification version the record is presented as conforming to.

**The schema resolves by rule, not by lookup.** `records/<package>/schema/<record>.schema.json`, in
an MTDR distribution whose package declares that `specification_version`. No registry is fetched,
hosted or kept alive. A registry is a service, and a record that needed a service to remain
interpretable would have failed this constraint rather than met it.

**The field is optional in the schema and required of this repository's own governed records**, the
requirement enforced by `tests/verify.py`. Two consequences follow deliberately:

1. **Every record authored before the field existed still validates.** MTDR does not invalidate
   records to add a convenience, and the specifications take additive minor versions — TDR 1.15.0,
   DAC 1.12.0, VR 2.1.0 — rather than the major versions a new required field would force.
2. **`conforms_to` is a property of a record that intends to travel.** A record that never leaves
   its register loses nothing by omitting it. A record that leaves and omits it is interpretable
   only by whoever already knows its origin.

Under [TDR-0039](TDR-0039-state-relative-requirements.md) the field is valid in **every** lifecycle
state, so nothing here encodes a transition prerequisite as a representation requirement.

## Evidence

- **Business** — a decision record's value is that it outlives the context that produced it. A
  record that cannot be interpreted once separated from its repository has a shorter useful life
  than the decision it preserves.
- **Architecture** — this completes TDR-0032's smallest-claim proposition. A version-bound record was
  named as the smallest independent conformance claim while nothing in a record actually bound its
  version, which made the claim true only inside the repository that hosted it.
- **Regulatory** — a record produced as evidence is read by people who did not author it, in systems
  that did not produce it. "Which rules did this claim to follow?" is the first question asked of it,
  and until now the record could not answer.
- **Operations** — resolution by rule means an adopter's tooling needs no network call, no registry
  and no service to interpret a record it has been handed.
- **Customer** — not directly material.
- **Data** — the binding names a specification version, not a schema hash. A version is a promise
  about meaning; a hash is a promise about bytes, and the weaker claim is the honest one here.
- **External** — the shape is unremarkable and deliberately so: a namespaced identifier with a
  semantic version is how most portable formats declare their own contract. **No external
  correspondence is claimed**, and no dependency is taken.

## Alternatives rejected

1. **Make the field structurally required.** Rejected: it invalidates every record authored before
   it existed, forces major versions on all three specifications, and breaks the FIX-117/118/119
   proof set whose whole point is three subjects that are *all schema-valid*. The obligation's own
   measure says a detached record **can** identify itself — a capability, which an optional field
   with an enforced repository requirement supplies exactly.
2. **A resolvable URL, such as the schema's `$id`.** Rejected: it binds record interpretability to a
   host staying up and a path not moving. The current `$id` values already point at
   `/blob/main/` — web pages rather than raw schemas — which is the failure mode in miniature.
3. **A registry mapping identifiers to specifications.** Rejected: a registry is a service, and this
   standard does not require one to interpret a record. Derivation by rule needs nothing running.
4. **Pin the schema by content hash.** Rejected: it makes an editorial change to a schema look like a
   different contract, and answers a question about bytes when the question asked is about meaning.
5. **Leave it to the register.** Rejected: TDR-0032 made the register optional. An obligation
   discharged only for records that happen to sit in one is not discharged.
6. **Do nothing and narrow the constraint.** Rejected: unlike DAC-0032 constraints 4 and 5, this one
   is fully within this repository's power to satisfy, and narrowing a constraint you *can* meet is
   how a release gate stops meaning anything.

## Options foreclosed

- No future record family may ship without a way to bind itself to its specification.
- Resolution may not later require a network service, a registry or a maintainer.
- The identifier scheme may not be re-purposed to carry standing, provenance or authority; each has
  its own mechanism and conflating them here would put four claims in one string.
- A record's `conforms_to` may never be read as a claim about its package, its register or the
  participant that produced it (TDR-0032).

## Consequences and review

Success is a record read and validated outside this repository by someone holding nothing but the
file and the published scheme. The suite proves the mechanical half now — a record copied alone into
an empty directory, its type and version resolved from `conforms_to`, and validation performed
against the schema that identifier names.

The honest limit: **the suite's detached test is still run by this repository's author.** It proves
the resolution rule works. It does not prove the scheme is legible to someone encountering it cold,
which is what DAC-0032 constraint 4 exists to test and why that constraint remains outstanding.

Review at that evidence, or 2027-02-27, whichever is sooner.
