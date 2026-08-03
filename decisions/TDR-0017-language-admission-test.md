---
id: TDR-0017
title: Adopt a language admission test, and defer this standard's language specification to evidence
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

# TDR-0017 — Adopt a language admission test, and defer this standard's language specification to evidence

> **Amended before release and admission.** This record was materially amended — broadened from a test of
> *this standard* to a test of any candidate language, and given a seventh criterion. **No superseding record
> is created because the earlier proposal never acquired standing within the accepted register, and nothing
> had relied on it as an
> accepted record.**
>
> Both conditions are required, and the wider one alone would not do. That a record is merely unmerged, or
> merely unreleased, does **not** license rewriting it without trace: once anything has relied on a record as
> accepted, it has standing whatever its branch says. Here nothing had. Superseding in that state would have
> manufactured lineage implying the standard once held a narrower published position that no reader ever saw,
> and false lineage is the worse failure.
>
> Nothing is lost by this. **The repository history retains the earlier proposal; the decision register does
> not represent it as an accepted prior position.** Those are two different kinds of truth and both are kept:
> version control records how a proposal evolved, and lineage records the positions that acquired standing.

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

It also became clear that the test is **not specific to this standard**. The same seven questions apply to any
record type that aspires to be a language — for value, for delegation, for inheritance, for intent. Writing
the test as though it were about the TDR would have to be undone the first time a second record type asked
the same question. So the test below is stated language-neutrally, and this standard is scored against it as
its first subject.

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

**Composition between records is unspecified, and two different things are easily confused here.**
[TDR-0016](TDR-0016-routing-and-disposition-refinements-from-field-application.md) considered a
`same_decision_as` lineage relation and left it out, on the ground that the standard stays neutral on how
records are produced. That is a **provenance-identity** relation, and the question it answers is *how are
records created*. Semantic composition answers a different question — *given two valid records, what does
combining them mean* — which is a matter of interpretation, not production. **TDR-0016 therefore does not
constrain composition, and remains in force.**

The genuine constraint falls elsewhere, and only on part of the criterion: `practice/operating-model.md`
states flatly that there is no `contradicts` field and that contradiction is a review finding and an index
entry, never record frontmatter. That bears on **conflict**, not on composition. So the criterion divides —
composition may be specified by a new decision record, while conflict and precedence remain constrained by a
recorded position that this record does not disturb.

**The static rules a validator would enforce are already enumerated, but nowhere formalised.**
`practice/administration-and-assurance.md` lists them as the deterministic validator's checklist: lineage
references resolve, IDs unique, filename and ID agree, status transitions legal, review dates not overdue,
no dangling references. They are described in prose, shipped as an instruction to adopters, and expressed in
no grammar. TDR-0015 had already flagged one concrete defect in that set: `rejected` is in the status enum
but appears in no §7 transition rule.

## Decision

1. **This standard makes no language or domain-specific-language claim in this release.** It is a record
   format with a defined vocabulary, a closed schema and a lifecycle. That is what §1 says and what it
   continues to say.

2. **Adopt the seven-criterion admission test below, stated for any candidate language**, so that such a
   claim is falsifiable in both directions and so that a second record type need not invent its own test.

3. **Record the distinction that makes criteria 4 to 7 compatible with the boundary**, because without it
   they read as a demand to breach it. **A language specification defines what a conforming interpreter must
   compute; it does not compute.** ISO C defines sequence points and undefined behaviour and executes
   nothing. So the three-layer contract of TDR-0015 extends unchanged, with each layer's share stated in the
   same narrow verbs:

   - **The language defines the meaning of the acts.**
   - **The register or store enforces who may perform them.**
   - **A downstream consumer computes the position.**

   Specifying an interpretation contract therefore adds a normative obligation on *interpreters*, not a
   capability of the record. Nothing here moves enforcement, entitlement or effectiveness into the format,
   and TDR-0015's allocation table stands.

4. **Keep maturity and standing as independent axes** (below). The test measures what a language *is*; it
   says nothing about what standing that language has been given.

5. **Defer this standard's own language specification to evidence, not to argument** — the same disposition
   TDR-0015 applied to effectiveness fields, and the `defer-pending-evidence` disposition the DAC spec
   defines. Two criteria have running implementations to specify against and five do not, and a standard
   should specify what has been built rather than promote what has been drawn.

6. **Composition, if admitted, will be specified in a new decision record.** TDR-0016 remains in force,
   because semantic composition concerns the interpretation of records rather than their production. Not an
   additive field either — recorded here so that a later release can treat it as neither a minor addition nor
   a reversal of something that was never decided.

7. **Fix the two defects this test exposes, now**, because both are worth fixing whatever happens to the
   language question: the `rejected` transition gap (§7) and the undocumented absence of an abstract syntax
   (§11).

## The admission test

A body of records may be claimed to be specified by a **language** when, and only when, all seven of the
following hold. They are recorded so that a reader can check such a claim rather than take it.

| # | Criterion | What it requires |
|---|---|---|
| 1 | **Abstract syntax** | A model of a record and its relations that is independent of any serialisation, with each concrete format defined as a binding of it |
| 2 | **Defined vocabulary** | Terms with fixed meanings, and a closed core, so that an unrecognised term is an error rather than an opinion |
| 3 | **Static rules** | The conditions a well-formed record and a well-formed body of records must satisfy, stated formally enough to be mechanically checked |
| 4 | **Speech acts** | What counts as having decided, superseded, or rejected — as distinct from who is permitted to do so, which is not the language's business |
| 5 | **Composition** | Whether and how two records combine, and what a conflict between them means |
| 6 | **Interpretation contract** | What a conforming interpreter must compute from a body of records, stated normatively |
| 7 | **Complete evaluation semantics** | A conforming interpreter can evaluate **every valid statement and relationship the language defines**, using only the published semantics, **without introducing unstated rules** |

**Criterion 7 is the closure check over the other six, not a seventh item beside them.** Criteria 1 to 6 can
all be satisfied while an implementer still has to invent meaning at the first real conflict, and two
conforming implementations then disagree while both remain conforming. **It is what makes criterion 6
decidable rather than aspirational**: 6 states what an interpreter must compute, 7 states that the language
gives it enough to compute it. A language meeting 1 through 6 but not 7 is a specification with holes in it,
and the holes are exactly where interoperability fails.

The criterion is bounded by what the language itself defines — "every valid statement" is meaningless unless
the language says what a valid statement is, which is criteria 1 and 2 doing their work. Within that bound,
the semantic domains a language must close over are:

**applicability · temporal validity and effectiveness · supersession · consistency · conflict, precedence
and resolution · composition · inheritance · unresolved and indeterminate states**

**Validity and effectiveness are not one property**, which is why the domain names both. A statement may
*exist*, be *valid*, be *in force*, and be *currently applicable* — four distinct states, and a language that
compresses them will eventually be unable to express a decision that is validly made but not yet in force, or
in force but not applicable here. The fourth is where this domain meets the applicability domain: *in force*
is a temporal question, *applies to this situation* is a scope question, and only their conjunction makes a
statement govern a given case.

**Detecting a conflict is not the same as knowing which statement governs**, and precedence is not a special
case of supersession — supersession is one record replacing another over time, whereas precedence decides
between records that are both standing. The domain must cover the specific statement governing over the
general, the inherited constraint against the locally asserted one, records of equal standing that
disagree, and the case where narrower scope or stronger authority decides. It does **not** require every
conflict to resolve automatically. It requires the language to say which of four outcomes obtains:
**governed** (one statement prevails, by a stated rule), **conflicted**, **indeterminate**, or **externally
adjudicated** — the last being a legitimate answer, not a failure, provided the language says so rather than
leaving an implementer to invent a tie-break.

**The last domain is the one most easily mistaken.** Completeness does **not** mean every question yields
true or false. A language is complete over indeterminacy by defining *when a result is unknown,
underdetermined, out of scope, or contingent on evidence the records do not carry* — and saying so in its
semantics rather than leaving an implementer to guess. A criterion 7 that demanded an answer to every
question would demand **false certainty**, and would put itself in direct conflict with §11 and with the
deferral discipline of [TDR-0015](TDR-0015-visibility-and-effectiveness.md).

This standard already has the right instinct here, expressed informally: **§11 is a prose ancestor of an
indeterminacy rule.** It states plainly what the format does not compute, rather than pretending to compute
it. That is what this domain asks for, and the gap is that §11 is prose rather than semantics — not that the
position is wrong.

Note what criterion 7 does *not* say. It is a completeness property **of the semantics**, discharged **by an
interpreter**. It does not make a record executable, and nothing in this test licenses the belief that a
record does anything. Capture still confers nothing (§10). Nor does it establish that two independent
implementers would in fact agree: closure is a property of the published semantics, whereas **reproducibility
is a property demonstrated by independent implementation**, and it is a further and later question than this
test asks.

### Two independent axes

The test above measures **semantic capability** — what a language can express, and what a conforming
interpreter can determine from it. That must not be confused with **institutional standing** — whether the
language is a candidate, a proposal, ratified, or settled convention within some organisation.

*Capability* and *standing* are the precise names. "Maturity" is serviceable prose but ambiguous here,
because the seven criteria are themselves a maturity assessment — of capability specifically, and of nothing
else.

These are orthogonal, and keeping them so matters in both directions. A body of records can be formally
ratified and still be a thin vocabulary; treating ratification as evidence of completeness is how an
organisation ends up with implementers inventing semantics under the impression that the question was
settled. Equally, a complete and rigorous specification can sit unratified; discounting it for that reason
loses the only artefact that would have made two implementations agree.

So a maturity claim and a standing claim are made separately, and each is evidenced on its own terms. The
governance ladder by which an organisation confers standing is that organisation's business and is not
specified here.

One caution about the capability axis. The seven criteria are **not a state machine**, and meeting them is not
a sequence to be walked in order. A language may have a grammar with incomplete semantics, or settled
semantics never expressed as a formal grammar, or a specification covering only part of what it defines, or
several conforming serialisations of a single abstract syntax. Read the criteria as a **commonly observed
progression** — these capabilities often emerge in roughly this order, but need not. It is a description of
what completeness consists of, not a route by which it must be reached.

### This standard, scored

The score records **only what exists**. Why a capability is absent — whether nobody has written it yet or the
standard decided against it — belongs in the second column, never in the first. That separation is the
two-axis discipline above, applied inside the test: a capability declined on principle and a capability
merely unbuilt score identically, because a reader assessing what an interpreter can rely on is not helped by
knowing which it was.

| # | Criterion | State | Evidence / disposition |
|---|---|---|---|
| 1 | Abstract syntax | **Not met** | §4 defines a file; §6 gives portable lineage, which is a weaker property. Open — see §11 |
| 2 | Defined vocabulary | **Met** | §4.1, `schema/tdr.schema.json`, the `x-` namespace contract at §4.3 |
| 3 | Static rules | **Partly met** | Enumerated as the validator checklist in `practice/administration-and-assurance.md`; no grammar and no reference implementation |
| 4 | Speech acts | **Partly met** | Amendment is not a legal move, only supersession; a superseding record must state what is now known that was not known; a named individual, never a committee. Not stated as a taxonomy; delegation unspecified |
| 5 | Composition | **Not met** | Constraint composition is demonstrated in a reference implementation but **not specified by the language**; conflict and precedence remain unspecified and are constrained by `practice/operating-model.md`. [TDR-0016](TDR-0016-routing-and-disposition-refinements-from-field-application.md) declined a provenance-identity relation, which is a different question |
| 6 | Interpretation contract | **Not met** | §11 states what the format does not compute; it does not yet state what an interpreter must. Deferred by this record |
| 7 | Complete evaluation semantics | **Not met** | The furthest away. Applicability and conflict unspecified; §11 is a prose ancestor of the indeterminacy domain; **inheritance has no representation in this standard at all** |

One met, two partial, four unmet. Adding criterion 7 made the test harder and this standard's score worse.
That is the intended direction: a test is only worth publishing if it can be failed.

## Evidence

- **Architecture.** ARCHITECTURE.md, TDR-0012 and TDR-0015 fix the boundary at the register. The interpreter
  distinction in decision 3 is what allows a language specification to be written later without moving that
  boundary; absent it, criteria 4 to 7 and the boundary contract are in direct conflict, and the conflict
  would surface as an unfixable contradiction in a later specification.
- **Operations (evidence for criterion 5, and the reason for the sequencing).** Composition semantics for
  *constraints* are implemented and test-evidenced in a reference implementation outside this repository: a
  conjunctive attenuation algebra in which a composed envelope is a subset of each parent, attenuation is
  one-way, and an empty constraint set is distinguished from an absent one — **17 passing tests** across its
  two suites — together with a decision calculus whose binding, composition and partial-evaluation
  operations and whose authorisation gate carry **36 passing tests** and a demonstration that calls them.
  This is the strongest evidence in the whole test, and it is evidence for a criterion the standard has **not
  yet specified** — implementation running ahead of specification, which is the harder case to hold honestly.
- **Operations (counter-evidence, and the reason for the deferral).** In that same implementation, the
  entailment and contradiction relations, contradiction detection, applicability computation and
  "current position" are **designed and unbuilt** — scoped honestly in the design record, with no code.
  Five of the seven criteria would therefore be specified from drawings.
- **External.** The precedent for the distinction in decision 3 is ordinary and well tested: language
  standards routinely define required interpreter behaviour without being implementations. That is the whole
  shape of a conformance clause. The precedent for criterion 7 is equally ordinary — a specification that
  leaves evaluation gaps produces implementations that disagree while each claims conformance.
- **Regulatory.** Not material to this decision. A vocabulary claim is not a regulatory claim, and binding
  one to a regime would reverse [TDR-0001](TDR-0001-publish-as-neutral-open-standard.md).
- **Business, Customer, Data.** Not material.

## Alternatives rejected

- **Write the specification now.** Rejected on evidence, not on principle. Two of seven criteria have running
  code to specify against; five would be specified from designs that have never executed. A specification
  that normatively required entailment, contradiction detection and applicability computation before any of
  them existed would be an aspiration published in the imperative mood — and it would be very hard to
  narrow later, because implementers would have built against it.
- **State the test as a test of this standard.** Rejected as a scoping error that would have to be undone.
  The same seven questions apply to any record type that aspires to be a language, and the test is more
  useful, and more honestly falsifiable, when the thing being judged is not also the thing doing the judging.
- **Adopt the criteria as first proposed, unamended.** Rejected. As originally worded, several read as
  obligations on the standard to compute effectiveness, resolve authority and detect contradiction. Meeting
  them in that reading would contradict TDR-0015 and spec §10 — the standard would have to abandon the
  boundary contract in order to pass its own test. Decision 3 keeps the criteria and fixes the reading.
- **Score the current state as passing on syntax.** Rejected as false. It is the cheapest criterion to earn
  and the precondition for a third-party parser, and claiming it while §4 still defines a record as a file
  would be exactly the unfalsifiable claim this standard exists to discourage.
- **Stop at six criteria.** Rejected. Without the closure check, a language can satisfy every structural
  criterion and still leave two conforming implementations disagreeing about what a body of records means.
  That is the failure the test exists to prevent, and it would have passed unnoticed.
- **Fold standing into the maturity ladder** — treat a ratified record set as thereby a mature language.
  Rejected: it makes the test unfalsifiable by governance, and it is the specific error that lets an
  organisation believe a question is settled while implementers are still inventing semantics.
- **Claim the language, or the domain-specific language, now.** Rejected. Four criteria are unmet — one of
  them with implementation evidence but no specification — and the claim would fail the standard's own
  discipline on its first contact with a reader who checked.
- **Say nothing, and leave the question to the reader.** Rejected: silence is the state that lets the claim
  drift upward by implication. A stated test that the standard currently fails is more useful, and more
  honest, than an unstated one it might be argued into passing.
- **Add composition operators quietly as an additive minor.** Rejected, though not for the reason first
  recorded. Composition reverses nothing: TDR-0016 declined a provenance-identity relation, which is a
  different question, so there is no earlier decision here to supersede. What composition needs is a **new**
  decision record making the semantics explicit — not an additive edit that would let a substantive
  interpretation rule arrive without ever being decided. `practice/operating-model.md` separately holds the
  position on contradiction, which constrains conflict rather than composition.

## Options foreclosed

Publishing the test sets an expectation that later releases must meet it before claiming a language, and a
reader may now hold the standard to criteria it would otherwise have been free to redefine. That is the
intent. Stating the test language-neutrally also commits any sibling record type that later makes the same
claim to the same seven criteria — deliberately, since a per-record-type test would be worth nothing.
Recording the interpreter distinction commits any future specification to a shape: an interpretation
contract stated as a normative obligation on interpreters, never as a capability of the record. A future
decision that wanted the record itself to compute anything would have to supersede both this record and
TDR-0015.

## Consequences and review

**Success looks like** the deferred criteria being settled by implementations that exist, and the standard
either meeting the test and saying so, or not meeting it and continuing to say that.

`confirmed_by_outcome` is tested when the evidence arrives. Specifically:

- **Abstract syntax (criterion 1).** A serialisation other than markdown-with-YAML, in use, that a reader
  would recognise as carrying the same records — the demonstration that the model is separable from the
  file. This is the one criterion that needs no adopter evidence to *begin*: it needs the specification
  writing.
- **Composition (criterion 5).** At least one register in which two records genuinely combine or conflict in
  a way an adopter had to resolve, and a statement of how they resolved it — which is what a new composition
  TDR would be written against.
- **Interpretation (criterion 6).** At least one implementation that computes a current position from a body
  of records, with its rules written down — so the interpretation contract is specified from something that
  runs rather than from something drawn.
- **Complete evaluation semantics (criterion 7).** A worked pass over the eight domains in which each is
  either given semantics or **explicitly given indeterminate semantics** — a statement of when the answer is
  unknown, underdetermined, out of scope or contingent on external evidence. The criterion is failed by
  silence, not by uncertainty: an honest "undetermined, because …" discharges it; a gap does not. Whether two
  independent implementers would then actually reach the same conclusions from the specification alone is a
  further question, later than this test, and not answered by satisfying criterion 7.
- **Speech acts (criterion 4).** The delegation question: whether a decision recorded by one named
  individual on another's authority is one act or two. This is the open half of the criterion, and it is not
  answerable from this repository alone.

Absent that evidence by the review date, the deferral stands and this record is superseded only to say so.
