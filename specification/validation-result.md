# The validation result

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

The versioned contract [TDR-0033](../decisions/TDR-0033-four-dimensional-validity.md) requires: what a
validation result contains, which results are legal in which dimension, and what a result may never
say. Machine contract: [`schemas/validation-result.schema.json`](../schemas/validation-result.schema.json).

This document is normative. The Python in [`mtdr_validation/`](../mtdr_validation/) is **not** — it is
one reference implementation, and a conforming independent implementation is governed by this
document and the schema, never by behavioural equivalence with that code.

## 1. What a result is about

Every result names its subject. There is no untyped result, because under
[TDR-0032](../decisions/TDR-0032-typed-multi-object-conformance.md) there is no untyped claim.

| `subject.type` | The object assessed |
|---|---|
| `record` | A record instance — a TDR, DAC, VR |
| `interchange-structure` | A SourceFragment, RecordContribution or CandidateAssembly |
| `package` | A record package and its normative closure |
| `skill` | A canonical skill artefact |
| `repository` | A complete standards distribution |

Two of TDR-0032's seven subjects are deliberately absent, for different reasons.

**`collection`** — TDR-0032 leaves the collection/register class architecturally present with no
contract, and DAC-0032 constraint 6 forbids advertising conformance for it. The schema rejects it: a
result that cannot be governed cannot be issued. When the collection contract exists, this contract's
major version admits it.

**`participant`** — a participant's execution is a *behavioural* claim, made by passing the applicable
fixtures, corpus and probes. TDR-0033 is explicit that behavioural conformance is not a validation
dimension, and DAC-0033 constraint 7 keeps it a separate claim. It is not a validation result, so it
is not a validation subject. One consequence follows immediately and is enforced in §5: every subject
this contract admits **has** a serialised representation, so structural validity is never
`not-applicable`.

`subject.id` identifies the object; `subject.ref` locates it.

**Conformance at one level implies nothing at another.** A `pass` on a skill artefact is not a claim
about the participant executing it; a `pass` on a record is not standing. Nothing in a result may be
read across subjects.

## 2. Which specification it was assessed against

`specification.id` and `specification.version` are **required and first-class**, not a prose
convention. A result that does not say what it validated against has not made a verifiable claim —
this is the same gap TDR-0032 identified in detached records, and the contract closes it here rather
than leaving it to be inferred from context.

`assessed_state` records the state the object legitimately occupies. **Validity is relative to that
state.** Information required only for a later transition does not make the current state invalid.

## 3. The four dimensions

All four are always present, always reported independently, and are **not a pass pipeline**.

| Dimension | Question |
|---|---|
| `structural` | Does the serialised object parse and satisfy the shape applicable to its claimed type, specification version and current state? |
| `semantic` | Is the object intrinsically coherent under the published semantics for its type and state? |
| `relational` | In the declared evaluation context, do required references resolve, and do published cross-object constraints hold? |
| `transition-eligibility` | For a named requested transition, are the published prerequisites and evidence present and sufficient to place the request before the authorised human decision-maker? |

A structural failure may leave semantic checks unrun; an unavailable reference may make relational
validity indeterminate while intrinsic semantics still pass; an object may be valid now and
ineligible for what it wants to become next. Each of those is a different report, and the contract
requires all four to survive to the interface.

## 4. The result vocabulary

| Result | Meaning |
|---|---|
| `pass` | Every applicable published requirement evaluated in this dimension was satisfied. |
| `fail` | At least one applicable published requirement was demonstrably violated. |
| `indeterminate` | The dimension applies, but available information is insufficient to establish pass or fail. |
| `not-applicable` | The dimension or rule does not apply to this object, state, transition or declared evaluation. |

**`indeterminate` is not a softer `fail`, and it is never permission to infer the missing fact.** It
is the honest report that the validator does not know. A consumer that treats it as either
established outcome has broken this contract.

## 5. Which results are legal where

The contract does not mechanically offer every result in every context.

| Dimension | Legal results | Rule |
|---|---|---|
| `structural` | `pass` · `fail` · `indeterminate` | TDR-0033 permits `not-applicable` only where no serialised representation forms part of the typed assessment. Every subject §1 admits has one, so the case is unreachable and the schema rejects it. It becomes reachable only if a future major version admits a subject without a serialisation. |
| `semantic` | all four | Package rules can legitimately be absent. |
| `relational` | all four | Related objects can legitimately be unavailable. |
| `transition-eligibility` | all four | Must be `not-applicable` when no transition is requested, and must **not** be `not-applicable` when one is. |

Further requirements, all schema-enforced:

- Every dimension appears **exactly once**. A dimension cannot be omitted to avoid reporting it.
- `fail` and `indeterminate` **require at least one reason**. An unexplained negative result is not a
  finding, it is an assertion — and for `indeterminate` the reason must say what information was
  missing, since that is the entire content of the result.
- `not-applicable` requires a reason **stating why it does not apply**, for the same reason: it is the
  result most easily used to make an inconvenient dimension disappear.
- `unevaluated_because` names the dimension whose result prevented a check from running. Dependency
  is recorded explicitly rather than implied by ordering.

## 6. What a result may never contain

The schema closes the object — `additionalProperties: false` throughout — so these are rejected
structurally, not merely discouraged.

- **No aggregate verdict.** There is no `valid`, `conformant`, `overall`, `passed` or `score` field,
  at any level. DAC-0033 constraint 8 permits an interface to summarise for usability but requires
  every dimension to be retained and exposed, and forbids any normative aggregate green result from
  overriding a failure or indeterminate. A field that could be read alone would be read alone.
- **No standing.** No `ratified`, `standing`, `accepted`, `approved` or `authority` field.
  [TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md) reserves standing to the
  authorised human act. `transition-eligibility: pass` means the request may be *placed before* a
  decision-maker; it neither performs nor authorises the transition.
- **No repair.** No `corrected`, `normalised` or `suggested_value` field. A validator reports defects
  and gaps; it does not fill them, and it does not silently mutate what it was given. The assessed
  object is byte-identical before and after.
- **No inference.** A result never contains a value that was absent from the object. This is the same
  rule as the recovery grammar's: *missing means missing.*

## 7. Reasons, evidence, and context

`reasons` are short statements of what was established, each with a `code` a consumer can branch on
and a human `detail`. `evidence` entries reference the artefact and locus that support the reason —
a schema pointer, a file and line, a fixture identifier.

`context` declares the **portable evaluation context** relational validity ran against: what the
validator could see. Relational validity does not require a register or a graph — a graph may compute
it faster, and is not a normative dependency. A reference the context could not reach is reported
`indeterminate` with the unreachable reference named, never `fail`; failing an unavailable reference
would make offline and zero-install use impossible, and passing it would conceal real organisational
inconsistency.

## 8. Serialisation and versioning

A result serialises to JSON and validates against the published schema. `contract_version` is the
version of *this* contract, and is independent of the specification version of the object assessed —
the two version different things and are versioned separately.

A serialised result must reload in a fresh process and yield the same interpretation. Nothing in a
result may depend on the process that produced it.

## 9. What this contract does not do

It does not decide whether a claim is *true*. A validator may establish that a £20m benefit is
represented correctly and cites resolvable evidence. It cannot establish that the benefit exists or
that the organisation should proceed. **Absence of contradiction is not truth; evidence is not
judgement; unresolved information is not inferred state.**

Behavioural conformance is not a fifth dimension. A participant makes its own TDR-0032 claim by
passing the applicable fixtures, corpus and probes; a conforming skill artefact does not imply
conforming execution.
