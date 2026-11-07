---
id: TDR-0048
conforms_to: mtdr/decision/tdr@1.15.0
title: Recover what can be evidenced, preserve what cannot, and never turn a contemporary interpretation into historical authority
status: proposed
template: full
decision_date: 2026-11-07
accountable_owner: Sailesh Panchal
confidence: medium
maturity: proposed
supersedes: none
derived_from: TDR-0018, TDR-0022, TDR-0027, TDR-0033, TDR-0036, TDR-0043
confirmed_by_outcome: pending — confirm when an implementation outside this repository has produced historical candidates from real material, consumed this contract as published, and a named individual has attested or rejected at least one of them; or 2027-05-07, whichever is sooner
---

# TDR-0048 — Recover what can be evidenced, preserve what cannot, and never turn a contemporary interpretation into historical authority

> **Proposed. No standing.** Assured by [DAC-0048](DAC-0048-historical-recovery-doctrine.md), which
> must be accepted before this record is.
>
> This record and the specification text it introduces travel together. **None of it reaches `main`
> while this record is proposed**: if it is returned, the branch is revised, and the standard is
> untouched. Every file it adds is headed *proposed under TDR-0048*, and those headings change in place
> only on ratification.
>
> **Returned on 7 November 2026 and amended** ([the return](evidence/TDR-0048-0049-owner-return-2026-11-07.md)): a shared calendar date is not an order, and
> the contemporaneity rules now say so. The record stays proposed.

## Context — what was known at the time

Organisations hold far more decisions than they ever recorded. They are in minutes, papers, business
cases and transcripts, taken by people who have since moved on, and they still shape what the
organisation does. An adopter building a tool to recover them from such material asked this standard
one question and could not get an answer: *whether, and how, a reconstructed record may exist and be
labelled.* Until it is answered, everything such a tool produces is stranded, and each implementation
invents its own rules for the hardest part of the work.

What the standard said, in November 2026:

- **The value language has a recovery path; the decision language does not.** Value recovery runs
  identify → reconcile → draft → challenge → validate, with a contribution vocabulary and an
  orchestrating skill ([TDR-0026](TDR-0026-value-recovery-vocabulary.md)). The decision package has
  roles, an admission test and a drafting skill, and nothing between them.
- **The hindsight rule exists, but is not normative.** *Reconstructing reasoning is forbidden;
  recovering contemporaneous evidence is legitimate; outcome knowledge is never evidence.* It is
  stated in the shared identification skill, in the decision package's semantic roles and admission
  test, and in a release note (1.13.0). No decision record decides it, and no specification states
  it.
- **Three texts read, at face value, as forbidding recovery altogether.** `decision-identification`
  names *retro-mining* an anti-pattern — "identification serves capture at the moment of decision, not
  archaeology". The full template says of Context "never reconstruct after the fact", and the TDR
  specification says the same. Each is right about *reasoning*. None distinguishes reconstructing what
  people must have thought from surfacing what they wrote down at the time, and an adopter cannot tell
  from them which is permitted.
- **Three texts constrain any answer.** The [contribution model](../specification/contribution-model.md)
  says the interchange structures "need not be persisted", are "not peers of the record schemas", and
  that treating them so would make this repository "a standard for mining pipelines, which TDR-0018
  explicitly refuses". [Candidacy and ratification](../specification/candidacy-and-ratification.md)
  puts "how ratification is captured, authorised or evidenced" outside the standard and names
  *ratification as workflow* an anti-pattern. [TDR-0027](TDR-0027-human-ratification-confers-standing.md)
  requires durable, attributable evidence of the human act before a record represents standing, and
  forbids any agent or technical state from conferring it.
- **The record format cannot carry recovery metadata.** The TDR schema is closed, and its `confidence`
  is the owner's confidence at the time of decision. Adding a field means a specification version, and
  until this branch's earlier repair the identity check would have failed every immutable record on any
  version bump.
- **The adopter's own evidence.** Its corpus assessment of a structured decision log (July 2026) found
  accountable owners named in few entries and decision dates evidenced only at folder level. Whatever
  this record decides, most recovered candidates will be incomplete.

The owner reviewed a draft of this record's approach on 6–7 November 2026 and set the principle it
must serve — *recover what can be evidenced; preserve what cannot; never turn a contemporary
interpretation into historical authority* — with five amendments and six rulings, recorded below.

**Unknown at the time:** whether the four times and the evidence kinds are the right granularity for
material beyond minutes, papers and transcripts; whether a reviewer can apply the matrix consistently;
and whether any implementation will consume the contract as published rather than copy it.

## Decision

**State the hindsight rule normatively, give recovery a structure that cannot acquire standing, and
keep the historical record, its present attestation and any current authority three different
things.**

### The doctrine — [`specification/historical-recovery.md`](../specification/historical-recovery.md)

| | Rule |
|---|---|
| **Forbidden** | reconstructing *reasoning*: inferring what people must have believed, inventing alternatives, writing the rationale the outcome suggests, stating an authority nobody is evidenced to have held |
| **Permitted** | recovering *contemporaneous evidence* of what was decided, considered, constrained or left unresolved |
| **Required** | the result is a **retrospective candidate with no standing**, immutable once written, held until a named individual attests the organisation's present account of it; incompleteness stays visible and is never filled to promote |

**Three things, never one** — the owner's first amendment, made normative:

| | What it is | How it comes to exist |
|---|---|---|
| **The historical decision** | what the organisation decided, supported by contemporaneous evidence | recovered |
| **The present attestation** | what a named individual now accepts as the organisation's evidenced account of that past | an act of ratification, scoped to the account |
| **A current governing decision** | what a contemporary authority decides applies from now on | **only** a separate prospective record — confirming, superseding or retiring |

A fully evidenced historical decision **may** be recorded as a TDR, under the existing admission rules
and the existing schema. Its ratification confers no retrospective authority and does not silently
renew the decision. The recovered record says so in its opening, in the way a ratified record already
carries a banner: *recovered; attested as the organisation's account on a date, by a named individual;
whether the decision still governs is not established by this attestation.* Its Evidence section
names the candidate it was recovered from.

### The six rulings

1. **The attester is not the owner.** `accountable_owner` is the historical owner as evidenced, or
   missing — and missing is the finding. The attester accepts accountability for the record as an
   account of the past, not for the decision it describes.
2. **An incomplete candidate is a legitimate terminal state.** There is no obligation to promote it.
3. **A recovered record is a TDR — conditionally.** Only with complete admissible evidence, and with
   historical recognition kept distinct from current governance.
4. **Outcome knowledge is never decision-time evidence.** Retrospective material may corroborate that
   a decision occurred; it never supplies its context, alternatives, rationale or owner.
5. **Contemporaneity is computed, from four times, at the precision the evidence gives.** Event,
   capture, creation and interpretation time; partial dates never completed; a missing event moment
   makes every grade `indeterminate`, never assumed. Pre-dating shows that material existed, not that
   it was considered, and the second is graded separately. **A shared date is not an order** (the
   owner's same-day correction): the times order material across days, never within one, and an order
   they leave open is closed only by evidence that the material was before whoever acted.
6. **The conservative path.** The TDR specification stays at 1.15.0. Most mined candidates will stay
   candidates, and the doctrine is written for that. A recovered-record provision in the TDR format is
   revisited only on a demonstrated semantic need.

### What material may support — the owner's second amendment

Every package states a matrix of **evidence kinds against claims**: which kind of material can support
which role, and to which derivation state. The kinds are shared — `act-record`, `cited-material`,
`unlinked`, `later-recording`, `retrospective`, `restatement` — what the material is and how it
connects to the act, independently of its times. **Independence counts once**: a
restatement names the source it repeats and corroborates nothing beyond it. **Inference is bounded**:
`inferred` may normalise a narrowly evidenced value, and never supplies who acted, under what
authority, why, or instead of what. The decision package's instance of the matrix is its recovery
vocabulary's to state.

### The historical candidate — [`specification/historical-candidate.md`](../specification/historical-candidate.md)

A **profile over the existing interchange structures**, which it carries unchanged, with the
retrospective facts they cannot carry added beside them and keyed by identifier. `retrospective: true`,
`standing: none` and `status: candidate` are constants. The event time is a pointer to the
contribution that evidences it, never a copy. Contemporaneity is computed, never stored. The schema is
closed against a disposition, a forward link to a record, a rationale, a score and a workflow state.

**Review is appended, never applied** — the owner's third amendment. A named individual's act on a
candidate is a **review event** beside it, bound to the exact candidate by the digest of its RFC 8785
canonical form: who acted, on what authority, when, with what scope, and where the evidence is kept.
`governs` is always `false`. The candidate is never changed, a candidate altered after review no longer
matches its review, and the disposition is a view computed from the events. **The pipeline that
produces candidates produces no events.**

### How this answers the texts that constrain it

- **The contribution model.** The profile states what a retrospective candidate must preserve *if* an
  adopter keeps one. It requires nothing to be kept, says nothing about how candidates are produced,
  stored or reviewed, and is not a record type.
- **Candidacy and ratification.** A review event *identifies* an act and binds it to its subject. It
  does not capture, authorise or evidence the act, models no routing or approval step, and records one
  act.
- **TDR-0027.** A well-formed event, and a reference to evidence, are never presented as proof that a
  valid human act occurred. The suite checks their structure and binding, and says so.

### What this deliberately omits

Rationale; scores; workflow states; reflective analysis of what might have been decided better;
handover. Reflection, handover and the linkage of implementing technical records are named in the
doctrine as read-only consumers above the artefact boundary, and none of them is built here.

## Evidence

- **Business** — a decision nobody recorded still binds the organisation, and the people who took it
  leave. A recovery that invents what they meant is worse than none, because it is believed; a
  recovery that preserves what they wrote, and says plainly what it could not find, is what makes an
  organisation's decision history usable without rewriting it.
- **Architecture** — every structure the doctrine needs already exists in the substrate:
  fragments, contributions, assemblies, the derivation states ([TDR-0036](TDR-0036-derivation-projection-and-show-me.md)),
  the `indeterminate` dimension result ([TDR-0033](TDR-0033-four-dimensional-validity.md)). The
  profile adds annotations beside them and changes none of them. The architecture ruling that records
  are reconstructed from fragments ([TDR-0022](TDR-0022-fragment-contribution-interchange-architecture.md))
  is what makes recovery possible at all; this record says what it may claim.
- **Regulatory** — not assessed by an external reviewer. The separation of a historical account from
  current authority is the property a supervisor would test first, and is stated so it can be tested.
- **Operations** — the adopter evidence shows most candidates will be incomplete. A doctrine that
  needed complete candidates would be unusable; one that relaxed admission to produce records would be
  untrustworthy. Incompleteness as a legitimate terminal state is the operational answer.
- **Customer** — indirect. An organisation that acts on a reconstructed authority nobody held exposes
  the people it serves to decisions with no accountable owner.
- **Data** — every claim traces to a span with a hash, every time is carried at its own precision, and
  the digest makes review tamper-evident. Nothing is computed that a reader cannot recompute.
- **External** — the standard's own record of the hindsight rule (release note 1.13.0), the adopter's
  corpus assessment (July 2026), and the owner's review of this approach (6–7 November 2026). **No
  external comparative review of historical-recovery practice is cited**, and none has been done.

## Alternatives rejected

1. **Keep the blanket prohibition.** Rejected: adopters recover decisions anyway, and without a rule
   each invents its own for the hardest judgement in the work. The prohibition was always about
   reasoning, and saying so costs nothing that the prohibition protected.
2. **Make the historical candidate a record type.** Rejected: a candidate is not organisational
   memory, has no accountable owner, and the contribution model and [TDR-0018](TDR-0018-interpretation-skills-and-the-artefact-boundary.md)
   refuse exactly this.
3. **Add a recovered-record provision to the TDR format now.** Rejected on the owner's sixth ruling:
   no demonstrated semantic need yet. The identity check that would have made a version bump fail every
   record has been repaired, so the option stays open.
4. **Carry the disposition in the candidate.** Rejected on the third amendment: a candidate that can
   record its own ratification can be made to claim one, and could no longer be shown to be the thing
   reviewed.
5. **Let ratification make the decision current.** Rejected on the first amendment: recognising that
   the organisation decided something in 2019 is not deciding that it applies today.
6. **One time, `source_time` before the decision.** Rejected on the second amendment: a transcript
   written up later may preserve a contemporaneous capture, and a memo written earlier may never have
   been read.
7. **Store the contemporaneity grade.** Rejected: a stored grade can be authored wrong; a computed one
   can only be computed wrong, and recomputed.
8. **Promote on completeness, confidence or a threshold.** Rejected: confidence never creates
   authority, and no completeness score is a ratification.
9. **Describe how recovery should run.** Rejected: ingestion, models, prompts and review tools are
   implementation, and a pipeline standard is what TDR-0018 refuses.

## Options foreclosed

- No historical candidate carries standing other than `none`, or any status other than `candidate`.
- No skill writes a review event or a disposition. A challenge's recommendation becomes an event only
  when a named individual acts on it.
- No attestation establishes current authority. Whether a recovered decision governs today always
  takes its own prospective record.
- Inference never supplies who acted, under what authority, why, or instead of what.
- Retrospective material never supplies a decision's context.
- Admission criteria are never relaxed to raise the rate at which candidates become records.
- The profile never describes how candidates are produced, stored or reviewed.

## Consequences and review

If ratified: two substrate specifications, two shared schemas, the recovery contract fixtures and
their checks become the standard's, and every *proposed* heading they carry changes in place. The
decision package's recovery vocabulary and pipeline follow under their own record. Until then, nothing
here is on `main`.

Success is an implementation outside this repository consuming the contract as published, producing
candidates that stay candidates, and a named individual attesting or rejecting at least one — with the
attestation read as an account of the past and nothing more. Failure looks like a recovered record
cited as current authority, an inferred owner in a candidate, or the contract being copied and
reshaped rather than consumed.

Review on that evidence, or 2027-05-07, whichever is sooner. Assurance must test laundering of
reconstructed context into fact, manufactured authority, attestation read as renewal, the attester
recorded as owner, and corroboration by repetition of one source.
