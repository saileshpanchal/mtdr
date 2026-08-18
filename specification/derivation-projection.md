# The derivation projection

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

What a record's values were derived from, in a form a machine can compare and a person can read. This
is the contract behind the [`show-me`](../skills/shared/show-me/) skill.

## 1. A view, not a fourth structure

The projection is **computed from** [SourceFragment](source-fragment.md),
[RecordContribution](record-contribution.md) and [CandidateAssembly](candidate-assembly.md), and adds
nothing to them. It introduces no new level to the
[contribution model](contribution-model.md)'s three, and carries no information those three do not
already hold — it re-presents what they hold in the direction a reader asks it: *starting from a value
in the record, what produced it?*

Being a view rather than a structure is what keeps it honest. There is nothing in a projection that
could be authored, only things that could be found.

## 2. What it reports, and what validation reports

Two different questions, deliberately kept apart:

| | Question | Artefact |
|---|---|---|
| **Derivation projection** | What was recorded as the derivation of this value? | this contract |
| **[Validation result](validation-result.md)** | What can currently be established about this object? | TDR-0033's four dimensions |

The projection is therefore **context-free**. It does not check whether a fragment is presently
reachable, whether a reference resolves, or whether an evaluation context can see the source — those
are relational validity's business, and an unreachable reference is `indeterminate` *there*, not a
different state *here*.

That separation has a practical consequence worth the design cost: two participants working from the
same records produce **directly comparable** projections, because nothing in a projection depends on
what either of them could reach.

## 3. The five states

Per record field, exactly one:

| State | Meaning |
|---|---|
| `supported` | A chain exists, and every contribution in it was read directly from its spans. |
| `inferred` | A chain exists, and at least one contribution was inferred across spans or from context. |
| `conflicting` | Competing chains exist for the same role, recorded and unresolved. |
| `missing` | No chain, and the absence was **declared** — the assembly reported the semantic as missing. |
| `unsupported` | No chain, and no declaration. The record renders a value that nothing accounts for. |

**`missing` and `unsupported` are the pair that matters.** Both have an empty chain. The difference is
whether anything says so: `missing` is a gap the interpretation recorded and a reader can act on;
`unsupported` is a value that arrived from nowhere. Collapsing them would hide the single failure that
the whole contribution model exists to make visible — and it is the easiest of all collapses, because
both look like "no evidence" from a distance.

### Five states, and no sixth

No `likely`, no `weakly-supported`, no `plausible`, and **no aggregate provenance score at any level**.
Each of those would return model judgement to a projection whose entire value is that it contains
none. A projection that grades its own confidence has stopped being inspectability and become
explanation.

Confidence is not absent from the projection — each contribution carries the `extraction_confidence`
and `epistemic_confidence` it was recorded with. What is absent is any *new* judgement computed at
projection time.

## 4. "I don't know why" is a valid result

A projection whose fields are largely `missing` and `unsupported` has not failed. It has reported the
state of the organisation's evidence, which is what it is for.

A broken derivation chain is **not a defect to be patched with generated prose**. It is a finding: the
organisation cannot presently say why one of its own records says what it says. That is worth knowing,
it is frequently the most useful thing this contract returns, and any implementation that fills the
gap with a plausible account has destroyed the finding rather than fixed it.

## 5. What a projection may never contain

Closed at every level — `additionalProperties: false` throughout — so these are rejected structurally,
not discouraged in prose.

- **No rationale.** No `explanation`, `reasoning`, `justification`, `summary` or `notes` field. There
  is nowhere to write why the value is *correct*, because the projection does not know and must not
  guess.
- **No score.** No `confidence_score`, `provenance_score`, `completeness` or `coverage` percentage.
- **No repair.** No `suggested_value`, `inferred_value` or `corrected` field. *Missing means missing.*
- **No standing.** Nothing about ratification, acceptance or authority
  ([TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md)). A well-evidenced record
  and a ratified record are different claims.
- **No judgement of the record.** Whether the evidence *should* support the value is
  [`challenge-record`](../skills/shared/challenge-record/)'s work. This contract carries findings from
  neither.

## 6. Shape

```
contract_version
subject.type · subject.id · subject.ref
specification.id · specification.version
fields[]
  field · state · rendered_value?
  chain[]
    contribution_ref · semantic_role · derivation · extraction_confidence · epistemic_confidence
    fragments[]
      fragment_ref · source_ref · source_hash? · locator?
  conflict_ref?   — for `conflicting`, the assembly conflict entry
  reported_at?    — for `missing`, where the absence was declared
projector.name · projector.version
```

State-dependent requirements, all schema-enforced:

| State | Chain | Also required | Also forbidden |
|---|---|---|---|
| `supported` | non-empty, every entry `derivation: explicit` | — | `conflict_ref`, `reported_at` |
| `inferred` | non-empty, at least one entry `derivation: inferred` | — | `conflict_ref`, `reported_at` |
| `conflicting` | at least two entries | `conflict_ref` | `reported_at` |
| `missing` | empty | `reported_at` | `rendered_value`, `conflict_ref` |
| `unsupported` | empty | `rendered_value` | `reported_at`, `conflict_ref` |

`missing` forbids `rendered_value` and `unsupported` requires it, which is the distinction in §3 made
mechanical: a declared gap has nothing to render, and an unaccounted-for value is precisely a rendered
value with nothing behind it.

## 7. Serialisation

JSON, validating against
[`schemas/shared/derivation-projection.schema.json`](../schemas/shared/derivation-projection.schema.json).
`contract_version` versions *this* contract, independently of the record's specification version.

A serialised projection must reload in a fresh process and yield the same interpretation. Nothing in a
projection may depend on the process that produced it — which is also what makes two participants'
projections of the same records comparable field by field.
