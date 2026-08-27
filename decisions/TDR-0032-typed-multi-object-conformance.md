---
id: TDR-0032
conforms_to: mtdr/decision/tdr@1.15.0
title: Adopt typed multi-object conformance and make the register an optional collection mechanism
status: accepted
template: full
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: TDR-0012
derived_from: TDR-0020, TDR-0027
confirmed_by_outcome: pending — review after the clean-clone, package-extraction and register round-trip proofs complete, or 2027-02-10, whichever is sooner
---

# TDR-0032 — Adopt typed multi-object conformance and make the register an optional collection mechanism

> **Standing carried forward 2026-08-16.** The substantive judgement was ratified on 2026-08-13
> in the collided Gate-B TDR-0020 candidate at `f966a05`. Human review confirmed this fresh
> representation is semantically equivalent under TDR-0031. The permanent
> [reconciliation crosswalk](evidence/TDR-0032-reconciliation-crosswalk-2026-08-16.md) binds the
> source objects, original act and new representation; the
> [carry-forward evidence](evidence/TDR-0032-standing-carry-forward-2026-08-16.md) preserves the
> equivalence confirmation. The 2026-08-16 act did not re-ratify the judgement or create its
> standing.

## Context — what was known at the time

The repository began as one record format and grew into record packages, shared interchange
structures, portable skills, behavioural probes and collection guidance. Each can be tested, but
not by the same test and not with the same implications.

TDR-0002 declined to bind the standard to software. TDR-0012 then made the decision register the
published conformance boundary: a complete implementation could stop there, but necessarily
extended through it. That judgement made a collection and storage mechanism part of the universal
minimum even though records, skills and packages can be interpreted and tested without installation
in a register. Replacing the register with an undefined "portable artefact" would merely exchange
one ambiguity for another.

The opposite extreme also fails. The current conformance specification says a record conforms to
the specification version under which it was raised, while individual record schemas do not carry
that applicable specification identity or version. A context-free Markdown file may remain human
readable but cannot make an independently verifiable interoperability claim when its governing
semantics cannot be established.

Meanwhile the author's own consultancy builds sophisticated consumers of these records. The temptation this record exists to foreclose is quiet convergence: the standard gradually shaping itself around one consumer's architecture until the open proposition — clone it, use it with any tooling, produce conformant records — becomes true in licence and false in practice.

## Decision

**MTDR conformance is always claimed by a defined object against the specification applicable to
that object.** The normative claim identifies its subject; there is no untyped normative claim that
something is merely "MTDR conformant".

The conformance subjects are distinct:

| Subject | Conformance claim |
|---|---|
| **Record instance** | Its content and declared state conform to an identifiable record type and applicable specification version whose normative semantics are durably resolvable. Standing is a separate claim governed by TDR-0027. |
| **Interchange structure** | The structure conforms to its named shared schema and semantic contract. |
| **Record package** | It contains or durably identifies every normative dependency and compatible version needed to interpret and validate its artefacts, and identifies the applicable reproducible conformance contract. |
| **Skill artefact** | The canonical skill file conforms structurally and semantically to its applicable skill contract. |
| **Participant or implementation** | Its execution conforms behaviourally to the governed envelope by passing the applicable fixtures, corpus and probes. |
| **Collection or register** | Its collection behaviour conforms to a testable collection contract. This class exists architecturally but no normative claim may be made until that contract exists. |
| **Repository** | The complete standards distribution keeps its package, dependency, conformance and compatibility claims coherent and testable. |

**Conformance at one level implies no conformance or standing at another unless a specification
explicitly defines that implication.** A conforming record is not necessarily accepted; a
conforming skill file does not establish conforming execution; a conforming collection does not
give its contents standing; and a conforming package does not establish that a runtime applies its
skills correctly.

The smallest independent record claim is therefore a **version-bound record**, not a context-free
file and not necessarily a complete package. Its record content, record type, applicable
specification identity and version, and normative semantics must be present or durably resolvable.
They need not all be embedded physically in the record.

A package solves a different distribution problem. Its **normative closure** contains or durably
identifies everything required to interpret and validate its artefacts, including compatible
dependency versions. Dependencies are classified as normative, conformance, provenance,
explanatory, navigation or historical. Normative dependencies constrain extraction; applicable
conformance tests must be durably identified and reproducible but need not all travel physically
inside every extracted package. Explanatory hyperlinks do not become normative merely because they
exist.

A register is an optional collection and governance mechanism, not a prerequisite for record,
interchange, package or skill conformance and not a source of organisational standing. Registration
may preserve identity, specification context, lineage, standing evidence, lifecycle integrity and
discoverability. It must not change record semantics or manufacture authority. Collection
conformance becomes a normative claim only when a testable contract covers those responsibilities,
including portability and export.

The mtdr repository remains an **open organisational-records standards and skills repository**.
Its job is to provide portable definitions, schemas, examples, validation rules and reusable
skills that allow humans or machines to identify, construct, challenge and validate governed
organisational records from arbitrary organisational material.

**The repository knows about:** organisational record languages; their semantics and schemas; source fragments and provenance; contribution classification; assembly and reconciliation rules; validation; examples and conformance fixtures; portable skills for working with those records.

**The repository does not know about:** any consumer product or platform; graphs or graph
databases; a particular document store or register implementation; **runtime orchestration**;
organisational runtimes; or what happens to a completed record downstream. Portable behavioural
sequencing inside a canonical skill is governed separately by TDR-0023 and is not runtime
orchestration.

The zero-install acceptance test is: someone can clone the standards distribution, use its
specifications and canonical skills with a compatible participant, and produce and validate typed
conformance claims **without installing an MTDR application, register or service and without
maintainer interpretation**. The same artefact must then enter and leave a register without its
semantics, conformance or standing changing merely because it was stored.

This decision narrowly supersedes TDR-0012's judgement that a complete conforming implementation
necessarily extends through a decision register. It retains TDR-0012's runtime neutrality, its
separation of records, skills and consumers, its conclusion that graphs and higher-order reasoning
are optional, its rejection of mandatory vendor platforms and its recognition of the register as a
valid deployment and governance pattern.

## Evidence

- **Business** — a standard shaped by one consumer caps its adoption at that consumer's reach, which is the failure TDR-0001 was written to prevent. The author's interest in downstream consumers is declared, exactly as it was in TDR-0001, and this record is the structural control on it.
- **Architecture** — [the conformance specification](../specification/conformance.md) already
  distinguishes record, implementation and repository claims. The package manifests separately
  identify normative contents and specification versions. Typed claims make those existing
  differences explicit without treating one as the universal boundary.
- **Regulatory** — not material to this decision.
- **Operations** — contributors and adopters need to state both the claim object and the applicable
  test. The generic phrase "MTDR conformant" is operationally insufficient.
- **Customer** — not material at repository level.
- **Data** — the record schemas currently do not carry their applicable specification version, so
  a detached record cannot yet establish the conformance context the accepted model requires. That
  is explicit release-blocking debt, not evidence against the model.
- **External** — [TDR-0001](TDR-0001-publish-as-neutral-open-standard.md) records the ADR/MADR
  portability precedent. That precedent supports neutrality but does not prove the accepted typed
  boundary; the clean-clone, extraction and round-trip tests remain missing evidence.

## Alternatives rejected

1. **Keep the register as the universal minimum under TDR-0012.** Rejected because it
   makes storage a prerequisite for artefacts whose meaning and behaviour can be tested in
   isolation, defeating zero-install portability.
2. **Treat a context-free Markdown file as the universal minimum.** Rejected because human
   readability does not establish the applicable semantics or specification version.
3. **Make the record package the universal minimum.** Rejected because record, skill, behaviour and
   collection make different claims; forcing a complete package into every record claim confuses
   distribution with instance validity.
4. **Use "portable artefact" as one generic claim.** Rejected because it collapses structurally
   different objects and allows conformance at one level to be inferred at another.
5. **Remove the register from the architecture entirely.** Rejected because collection memory,
   lineage, standing-evidence preservation and export are real governance responsibilities. The
   register is optional for other claims, not architecturally irrelevant.

## Options foreclosed

- No normative claim may say only "MTDR conformant" without naming its conformance subject.
- No claim at one level implies conformance or standing at another unless explicitly specified.
- A context-free record with no durably resolvable governing semantics cannot make an independently
  verifiable conformance claim.
- The repository cannot require a particular register, storage, runtime-orchestration or graph
  implementation without superseding this record.
- No implementation may advertise normative collection or register conformance until the testable
  collection contract exists.
- Registration cannot alter record conformance or confer standing; TDR-0027 governs `accepted`.
- The author's own consumers get no privileged surface: anything they need from the standard must arrive as an open proposal like anyone else's.

## Consequences and review

Success is a clean-clone participant producing typed conformance claims without an application or
register; an extracted package retaining normative closure; and a registration/export round-trip
preserving semantics, conformance and standing. DAC-0032 blocks public release of the new
architecture until those proofs pass and prohibits collection-conformance advertising until its
contract exists. Review at the confirmed-by-outcome trigger; the consumer-name scan remains
reportable at every release.
