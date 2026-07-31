---
id: TDR-0017
title: Adopt an admission test for the language claim, and defer the language specification to evidence
status: accepted
template: full
decision_date: 2026-07-31
accountable_owner: Sailesh Panchal
confidence: medium
maturity: proposed
supersedes: none
derived_from: TDR-0004, TDR-0015, TDR-0016
confirmed_by_outcome: pending — review when the evidence named under Consequences arrives, or 2027-01-31, whichever is sooner
---

# TDR-0017 — Adopt an admission test for the language claim, and defer the language specification to evidence

## Context — what was known at the time

A review of v1.11.0 asked whether this standard has become a **language** rather than a record format, and
whether it should say so. The question is fair. The standard now carries a defined vocabulary, a closed
schema, a lifecycle with legal and illegal transitions, lineage relations between records, two sibling
record types, and a body of practice describing how the records are produced and assured. That is more
structure than a template and less than anything the word "language" is normally used for.

The question matters because the claim is load-bearing in both directions. Claiming a language — or a
domain-specific language — without meeting a stated test is exactly the kind of unfalsifiable claim this
repository asks its adopters not to make (§10, and the claim discipline in [TDR-0001](TDR-0001-publish-as-neutral-open-standard.md)).
Declining the claim without stating what would earn it is no better: it leaves the standard's own
trajectory undocumented, and leaves a reader unable to tell whether the gap is two features or two years.

Four facts about the current state of the repository were established before deciding, and each of them
constrains the answer.

**There is no representation-independent model of a record.** [TDR-0004](TDR-0004-markdown-yaml-serialisation.md)
*fixes* markdown-with-YAML as the serialisation and defends the choice by reversibility — "a converter to
any richer format can be written later". Both schemas are scoped to the YAML frontmatter. Spec §4 says a
TDR **is** a single markdown file. What the standard does have is a weaker and genuinely different property,
stated at §6: lineage is portable and graph-ready without graph tooling. Portability of lineage is not
independence of representation. A third party today cannot write a conforming parser from the specification
alone, because the specification does not describe a record except as a file.

**Three of the properties a language claim would normally require sit outside this standard's boundary by
deliberate and recent decision.** [TDR-0015](TDR-0015-visibility-and-effectiveness.md) allocates
effectiveness computation, entitlement evaluation and projection to the downstream platform, and states that
`status` is never proof of operability or authority and that **capture confers nothing**. Spec §10 says the
record enforces nothing. ARCHITECTURE.md puts the reasoning layer outside the format. Any test that required
the *standard* to compute a current position, resolve who may act, or detect contradiction would require
abandoning the three-layer contract shipped eight days ago.

**Composition between records was declined, not merely omitted.** [TDR-0016](TDR-0016-routing-and-disposition-refinements-from-field-application.md)
considered a `same_decision_as` lineage relation and left it out, on the ground that the standard stays
neutral on how records are produced. `practice/operating-model.md` states flatly that there is no
`contradicts` field and that contradiction is a review finding and an index entry, never record frontmatter.
So composition operators cannot arrive as an additive edit; under this repository's own rules
(§7) reversing a recorded decision requires a superseding record.

**The static rules a validator would enforce are already enumerated, but nowhere formalised.**
`practice/administration-and-assurance.md` lists them as the deterministic validator's checklist: lineage
references resolve, IDs unique, filename and ID agree, status transitions legal, review dates not overdue,
no dangling references. They are described in prose, shipped as an instruction to adopters, and expressed in
no grammar. TDR-0015 had already flagged one concrete defect in that set: `rejected` is in the status enum
but appears in no §7 transition rule.

## Decision

1. **The standard makes no language or domain-specific-language claim in this release.** It is a record
   format with a defined vocabulary, a closed schema and a lifecycle. That is what §1 says and what it
   continues to say.

2. **Adopt a stated admission test, so the claim is falsifiable in both directions.** A future release may
   claim to specify a language when, and only when, all six of the following hold. They are recorded here so
   that a reader can check the claim rather than take it, and so that the standard cannot quietly promote
   itself.

   | # | Criterion | State at v1.12.0 |
   |---|---|---|
   | 1 | An **abstract syntax**: a model of a record and its relations that is independent of any serialisation, with markdown-with-YAML defined as one binding of it | **Not met.** §4 defines a file; §6 gives portable lineage, which is a weaker property |
   | 2 | A **defined vocabulary** with fixed meanings, and a closed core | **Met.** §4.1, `schema/tdr.schema.json`, the `x-` namespace contract at §4.3 |
   | 3 | **Static rules** stated formally enough to be mechanically checked | **Enumerated, not formalised.** The checklist exists in `practice/administration-and-assurance.md`; no grammar, no reference implementation |
   | 4 | **Speech acts**: what counts as having decided, superseded, or rejected — as distinct from who is permitted to do so | **Partly met.** Amendment is not a legal move; only supersession is. A superseding record must state what is now known that was not known. A named individual, never a committee. Not named as a taxonomy, and delegation is unspecified |
   | 5 | **Composition**: whether and how two records combine, and what a conflict between them means | **Not met, and declined.** See TDR-0016 and `practice/operating-model.md` |
   | 6 | An **interpretation contract**: what a conforming interpreter must compute from a body of records, stated normatively | **Not met.** §11 states what the format does not compute; it does not yet say what an interpreter must |

3. **Record the distinction that makes criteria 4, 5 and 6 compatible with the boundary**, because without it
   they read as a demand to breach it. **A language specification defines what a conforming interpreter must
   compute; it does not compute.** ISO C defines sequence points and undefined behaviour and executes
   nothing. So the three-layer contract of TDR-0015 extends unchanged, with the standard's share stated in
   the same narrow verbs:

   - **The standard defines the meaning of the acts.**
   - **The register or store enforces who may perform them.**
   - **A downstream consumer computes the position.**

   Specifying criterion 6 therefore adds a normative obligation on *interpreters*, not a capability of the
   record. Nothing in this decision moves enforcement, entitlement or effectiveness into the format, and
   TDR-0015's allocation table stands.

4. **Defer the language specification to evidence, not to argument** — the same disposition TDR-0015 applied
   to effectiveness fields, and the `defer-pending-evidence` disposition the DAC spec defines. The resolving
   evidence is named under Consequences. Two criteria have running implementations to specify against and
   four do not, and the standard should specify what has been built rather than promote what has been drawn.

5. **Composition, if it arrives, arrives by superseding TDR-0016** — not as an additive field. Recorded here
   so that a later release cannot treat it as a minor addition.

6. **Fix the two defects this test exposes, now**, because both are worth fixing whatever happens to the
   language question: the `rejected` transition gap (§7) and the undocumented absence of an abstract syntax
   (§11).

## Evidence

- **Architecture.** ARCHITECTURE.md, TDR-0012 and TDR-0015 fix the boundary at the register. The interpreter
  distinction in decision 3 is what allows a language specification to be written later without moving that
  boundary; absent it, criteria 4–6 and the boundary contract are in direct conflict, and the conflict would
  surface as an unfixable contradiction in a v2 specification.
- **Operations (evidence for criterion 5, and the reason for the sequencing).** Composition semantics for
  *constraints* are implemented and test-evidenced in a reference implementation outside this repository: a
  conjunctive attenuation algebra in which a composed envelope is a subset of each parent, attenuation is
  one-way, and an empty constraint set is distinguished from an absent one — **17 passing tests** across its
  two suites — together with a decision calculus whose binding, composition and partial-evaluation
  operations and whose authorisation gate carry **36 passing tests** and a demonstration that calls them.
  This is the strongest evidence in the whole test, and it is evidence for the criterion the standard has
  formally declined.
- **Operations (counter-evidence, and the reason for the deferral).** In that same implementation, the
  entailment and contradiction relations, contradiction detection, applicability computation and
  "current position" are **designed and unbuilt** — scoped honestly in the design record, with no code.
  Four of the six criteria would therefore be specified from drawings.
- **External.** The precedent for the distinction in decision 3 is ordinary and well tested: language
  standards routinely define required interpreter behaviour without being implementations. That is the whole
  shape of a conformance clause.
- **Regulatory.** Not material to this decision. A vocabulary claim is not a regulatory claim, and binding
  one to a regime would reverse [TDR-0001](TDR-0001-publish-as-neutral-open-standard.md).
- **Business, Customer, Data.** Not material.

## Alternatives rejected

- **Write the specification now.** Rejected on evidence, not on principle. Two of six criteria have running
  code to specify against; four would be specified from designs that have never executed. A specification
  that normatively required entailment, contradiction detection and applicability computation before any of
  them existed would be an aspiration published in the imperative mood — and it would be very hard to
  narrow later, because implementers would have built against it.
- **Adopt the test as first proposed, unamended.** Rejected. As worded, three of its criteria read as
  obligations on the standard to compute effectiveness, resolve authority and detect contradiction. Meeting
  them in that reading would contradict TDR-0015 and spec §10 — the standard would have to abandon the
  boundary contract in order to pass its own test. Decision 3 keeps the criteria and fixes the reading.
- **Score the current state as passing on syntax.** Rejected as false. It is the cheapest criterion to earn
  and the precondition for a third-party parser, and claiming it while §4 still defines a record as a file
  would be exactly the unfalsifiable claim this standard exists to discourage.
- **Claim the language, or the domain-specific language, now.** Rejected. Four criteria are unmet and one is
  actively declined. The claim would fail the standard's own discipline on its first contact with a reader
  who checked.
- **Say nothing, and leave the question to the reader.** Rejected: silence is the state that lets the claim
  drift upward by implication. A stated test that the standard currently fails is more useful, and more
  honest, than an unstated one it might be argued into passing.
- **Add composition operators quietly as an additive minor.** Rejected: TDR-0016 decided against a
  composition relation on the record, and `practice/operating-model.md` states the position on contradiction
  in terms. Reversing that by addition rather than by supersession would break §7 in the standard's own
  repository.

## Options foreclosed

Publishing the test sets an expectation that later releases must meet it before claiming a language, and a
reader may now hold the standard to criteria it would otherwise have been free to redefine. That is the
intent. Recording the interpreter distinction also commits the standard to a shape for any future
specification: an interpretation contract stated as a normative obligation on interpreters, never as a
capability of the record. A future decision that wanted the record itself to compute anything would have to
supersede both this record and TDR-0015.

## Consequences and review

**Success looks like** the deferred criteria being settled by implementations that exist, and the standard
either meeting the test and saying so, or not meeting it and continuing to say that.

`confirmed_by_outcome` is tested when the evidence arrives. Specifically:

- **Abstract syntax (criterion 1).** A serialisation other than markdown-with-YAML, in use, that a reader
  would recognise as carrying the same records — the demonstration that the model is separable from the
  file. This is the one criterion that needs no adopter evidence to *begin*: it needs the specification
  writing.
- **Composition (criterion 5).** At least one register in which two records genuinely combine or conflict in
  a way an adopter had to resolve, and a statement of how they resolved it — which is what a superseding
  TDR would be written against.
- **Interpretation (criterion 6).** At least one implementation that computes a current position from a body
  of records, with its rules written down — so the interpretation contract is specified from something that
  runs rather than from something drawn.
- **Speech acts (criterion 4).** The delegation question: whether a decision recorded by one named
  individual on another's authority is one act or two. This is the open half of the criterion, and it is not
  answerable from this repository alone.

Absent that evidence by the review date, the deferral stands and this record is superseded only to say so.
