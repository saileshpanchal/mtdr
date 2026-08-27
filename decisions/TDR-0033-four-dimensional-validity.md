---
id: TDR-0033
conforms_to: mtdr/decision/tdr@1.15.0
title: Separate structural, semantic, relational and lifecycle-transition validation
status: accepted
template: full
decision_date: 2026-08-13
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0025, TDR-0032, TDR-0027
confirmed_by_outcome: pending — review after the four-layer fixtures and versioned result contract pass in two implementations, or 2027-08-13, whichever is sooner
---

# TDR-0033 — Separate structural, semantic, relational and lifecycle-transition validation

> **Standing carried forward 2026-08-16.** The substantive judgement was ratified on 2026-08-13
> in the collided Gate-B TDR-0025 candidate at `f966a05`. Human review confirmed this fresh
> representation is semantically equivalent under TDR-0031. The permanent
> [reconciliation crosswalk](evidence/TDR-0033-reconciliation-crosswalk-2026-08-16.md) binds the
> source objects, original act and new representation; the
> [carry-forward evidence](evidence/TDR-0033-standing-carry-forward-2026-08-16.md) preserves the
> equivalence confirmation. The 2026-08-16 act did not re-ratify the judgement or create its
> standing.

## Context — what was known at the time

The repository already demonstrated that schema validity is insufficient. A silent merge of two
commitments and a confident unsupported invention can both be well formed. Conversely, the
interpretation fixtures deliberately preserve useful incomplete candidates: missing evidence,
owners and counter-signatories are reported rather than invented or used to suppress the candidate.

The unreleased VR v2 implementation exposed the opposite error. Its specification and fixtures say
a candidate may legitimately lack a finance counter-signatory, but its schema requires that field
globally. A candidate carrying the honest gap therefore fails the schema for the very state in
which the gap is permitted. The defect demonstrates a general rule rather than a VR exception:
validity is relative to the state an object legitimately occupies, not the state it may eventually
be asked to reach.

Two accepted decisions constrain the answer. TDR-0032 makes conformance claims typed by object: a
record, skill artefact, participant execution and collection do not share one conformance claim.
TDR-0027 reserves ratification, standing and `accepted` representation to authorised human acts and
their evidence. Validation must therefore report what can be established about an object without
absorbing either conformance-subject identity or organisational authority.

## Decision

Validation reports four **separate dimensions with explicit dependencies**, not a success pipeline:

1. **Structural validity** — does the serialised object parse and satisfy the machine-readable
   shape applicable to its claimed type, specification version and current state?
2. **Semantic validity** — is the object intrinsically coherent under the published semantics for
   its claimed type and current state? Are required meanings supported, state combinations legal
   and prohibited inferences absent?
3. **Relational validity** — in the declared evaluation context, do required references resolve,
   related objects have compatible identities, states and versions, and published cross-object
   constraints hold?
4. **Lifecycle-transition eligibility** — for a named requested transition, are the published
   prerequisites and required evidence present and sufficient for that request to be placed before
   the authorised human decision-maker?

Each dimension is reported independently with reasons, evidence, the applicable specification and
the context used. A structural failure may prevent some semantic checks from running; an unavailable
reference may make relational validity indeterminate while intrinsic semantics still pass; an
object may be valid in its current state while failing eligibility for a requested next state.

The common result vocabulary is:

| Result | Meaning |
|---|---|
| **pass** | Every applicable published requirement evaluated in this dimension was satisfied. |
| **fail** | At least one applicable published requirement was demonstrably violated. |
| **indeterminate** | The dimension is applicable, but available information is insufficient to establish pass or fail. It is not a softer fail and never permits inference of the missing fact. |
| **not-applicable** | The dimension or requested rule does not apply to this object, state, transition or declared evaluation. |

The versioned validation-result contract defines which results are legal for each dimension and
how unevaluated dependent checks are represented. It must not mechanically offer every result in
every context. At constitutional level:

- structural validity permits `pass`, `fail` or `indeterminate`; it is not applicable only where no
  serialised representation is part of the typed assessment;
- semantic and relational validity permit all four results because package rules and relationships
  can legitimately be absent or unavailable;
- transition eligibility permits all four results and is `not-applicable` when no transition is
  requested or the object type has no governed transition.

**Validity is relative to the current state.** Information required only for a later transition
must not make a state in which it is legitimately absent structurally or semantically invalid. The
absence is retained and may cause transition eligibility to fail or remain indeterminate.

The incomplete Value Record is the proving case. Subject to TDR-0019 settling the VR v2 semantics,
a candidate missing a finance counter-signatory can be structurally and semantically valid as a
candidate, relationally valid where its required references resolve, and ineligible for
ratification. It has no standing, and no repository or example receives an exemption.

**Validation has an epistemic boundary.** A validator may establish consistency with declared MTDR
semantics and available evidence. It must not convert absence of contradiction into truth, evidence
into judgement, or unresolved information into inferred organisational state. It may check that a
£20m claim is represented correctly and cites resolvable evidence; it cannot decide that the claim
is true or that the organisation should invest.

Lifecycle-transition eligibility is a deterministic report about published prerequisites. It
neither performs nor authorises the transition and does not establish ratification, standing or
permission to represent `accepted`. Those remain governed by TDR-0027.

Relational validity does not require a central register or graph. It runs against a declared,
portable evaluation context and reports unavailable relationships as such. Graphs may compute it
efficiently but are not normative dependencies.

Behavioural conformance is not a validation dimension. Under TDR-0032, a participant or
implementation makes a separate behavioural claim by passing the applicable fixtures, corpus and
must-not probes. A conforming skill artefact does not imply conforming execution, and a valid record
does not prove it was produced by a conforming participant.

Validators preserve the object assessed and report defects, gaps and indeterminacy. They do not
silently repair records, supply missing human information or promote lifecycle state.

## Evidence

- **Business** — preserving incomplete candidates turns missing owners, evidence and prerequisites
  into actionable organisational knowledge instead of validation noise or invented completeness.
- **Architecture** — TDR-0032 supplies typed conformance subjects; TDR-0027 supplies the authority
  boundary. Four independent validity dimensions fill the deterministic space between them without
  claiming either territory.
- **Regulatory** — [the TDR specification's regulator-neutral accountability shape](../records/decision/specification/tdr.md#8-regulatory-framing--worked-examples-not-dependencies)
  requires a reviewer to distinguish what was evidenced from what was judged. Forced certainty or
  validator-created authority would destroy that distinction.
- **Operations** — one Boolean result does not tell a user whether to repair serialisation, resolve
  meaning, retrieve a related object or seek human transition evidence. Dimensioned results do.
- **Customer** — indirectly material: false-positive readiness can legitimise consequential records;
  false-negative validity can hide useful incomplete evidence about underserved cohorts.
- **Data** — [the VR schema](../records/value/schema/vr.schema.json) globally requires
  `finance_countersignatory`, while
  [FIX-001](../records/value/fixtures/quantified/FIX-001-value-commitment-across-six-sources.md) and
  [CORPUS-004](../tests/corpus/CORPUS-004-insufficient-evidence.md) require the gap to remain visible
  in a retained candidate. A direct schema probe confirmed that the fixture-shaped candidate fails
  solely for the missing field. That is direct evidence of the current schema/lifecycle contradiction.
- **External** — not material to choosing this constitutional model: no external validator is made
  a dependency, and the four-valued vocabulary follows from observed repository cases requiring
  violation, insufficient information and inapplicability to remain distinct.

## Alternatives rejected

1. **Return one valid/invalid result.** Rejected because it hides whether failure concerns shape,
   meaning, relationships or readiness and encourages repair or invention in the wrong layer.
2. **Treat the four dimensions as a pass pipeline.** Rejected because relational information can be
   unavailable while intrinsic semantics remain established, and current-state validity need not
   imply eligibility.
3. **Keep human authority as the fourth validation layer.** Rejected because TDR-0027 reserves the
   human act, standing and accepted representation. A validator may report evidence but not perform
   or establish the act.
4. **Combine relational validity with participant behaviour.** Rejected because relationships are
   properties evaluated around an object; behaviour is a TDR-0032 participant/implementation claim.
5. **Keep relational checks inside semantic validity.** Rejected because it would make intrinsic
   meaning depend silently on a collection and conceal whether the object or its context failed.
6. **Make every transition-only field structurally mandatory.** Rejected because it makes useful
   current states invalid and pressures agents to invent the human input required later.
7. **Let JSON Schema carry the full lifecycle.** Rejected because schema can test serialised
   assertions but cannot establish evidence sufficiency for every semantic relationship or perform
   human judgement.
8. **Do nothing.** Rejected because the current schema already rejects a candidate state the
   specification and fixtures require implementations to preserve, while the existing validator
   contract collapses intrinsic, relational and eligibility findings.

## Options foreclosed

- No validator may collapse the four dimensions into one normative valid/invalid result.
- No pass at one dimension implies a pass at another unless the applicable contract explicitly
  defines and evidences that dependency.
- `indeterminate` can never be interpreted as permission to infer, repair or promote.
- A transition-only requirement cannot invalidate a current state in which its absence is permitted.
- Validation cannot perform, authorise or represent a lifecycle transition or standing.
- Behavioural conformance cannot be inferred from record validity or skill-file validity.
- Validators cannot silently mutate the object under assessment.

## Consequences and review

Success is a versioned result object reporting all four dimensions independently; fixtures covering
pass, fail, indeterminate and not-applicable where legal; an incomplete candidate passing current-
state validity while failing eligibility; relational tests for resolved, broken and unavailable
references; and must-not probes proving validation cannot repair, promote, ratify or infer standing.

DAC-0033 blocks public release until those proofs pass and routes the VR schema contradiction to
TDR-0019 rather than authorising an opportunistic fix here. Review when two implementations produce
materially equivalent dimensioned results over the same corpus, or on 2027-08-13.
