# Value contributions — the recovery vocabulary

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for interpretation of the value language. **Not a record schema.**
**Adopted by:** [TDR-0026](../../../decisions/TDR-0026-value-recovery-vocabulary.md)

What a fragment of organisational material can contribute to reconstructing an Operational Value
Commitment — **without requiring that it constitutes a Value Record**. Organisations rarely write a
commitment's clauses together: a strategy states an ambition, a board paper defines success
elsewhere, a risk paper constrains it, customer research reveals who benefits, and a later paper
quietly replaces it. The unit of recovery is the fragment; these classes are what fragments carry.

The classes are **interpretive vocabulary carried through the shared
[`RecordContribution`](../../../specification/record-contribution.md) structure** — its
`semantic_role` takes a class name where field-level assignment is premature, and tightens to a
[semantic role](../validation/semantic-roles.md) when drafting maps evidence onto the record. No new
schema exists, deliberately. A fragment can make multiple contributions.

## The thirteen classes

| Class | What we are looking for | Tightens toward |
|---|---|---|
| `beneficiary` | Who is meant to receive value | `beneficiary` |
| `commitment` | What value or outcome is being pursued or preserved | `commitment`, `intended-outcome` |
| `success` | What would constitute success | `intended-outcome`, `recognition-route` |
| `measure` | Quantitative or qualitative evidence of the outcome | `recognition-route`, `baseline`, `falsifying-signal` |
| `constraint` | A boundary within which value must be delivered | `review-boundary` |
| `assumption` | A belief or context underpinning the commitment | body context; `optimism-adjustment` |
| `time` | Horizon, deadline or review period | `due-point` |
| `priority` | Relative significance, where explicitly expressed | body context |
| `protection` | Existing value that must not be destroyed | `commitment` (mode: preserve), `review-boundary` |
| `trade-off` | One value explicitly balanced against another | recorded relationship; `unresolved` |
| `challenge` | Evidence contradicting or questioning the proposition | `conflicts`; challenge findings |
| `supersession` | Evidence that the commitment has changed | `supersessions` |
| `context` | Material needed to interpret another contribution | none — it qualifies, it never populates |

Three classes — `trade-off`, `challenge`, `context` — deliberately never populate a record field.
They exist because losing them loses exactly the disagreement and uncertainty recovery is for.

## The classes are not exhaustive — the `unclassified` outcome

This is the **current normative recovery vocabulary for VR v2.0.0**, not a claim of completeness.
Where material appears relevant to Value but fits no class, the skill reports the **`unclassified`
recovery outcome**: the fragment references, what was recognised, and why classification failed. It
is a reporting outcome, **not a fourteenth semantic role** — nothing is forced into a near-fitting
class, and nothing is dropped.

A recurring unclassified pattern is evidence that the vocabulary is missing an interpretive
distinction, and it routes to a superseding decision. This is the no-invention rule applied to the
vocabulary itself.

## Boundaries — what is *not* a value contribution

The classes are only usable if their edges hold. Four boundary tests, each with the worked contrast:

- **Value ≠ decision.** "We will migrate to the phased route" commits the organisation to an *act*;
  its value contributions are whatever outcome material surrounds it. The decision is the decision
  language's object; a `linked-decision` reference is the join, never a merge.
- **Value ≠ activity.** "Deploy the new CRM platform" is work, not an outcome. An activity fragment
  contributes nothing unless material binds it to an organisational state change — ✗ *Implement CRM*
  / ✓ *customers receive consistent service regardless of channel*.
- **Value ≠ KPI or measure.** A KPI target in a performance pack is a `measure` contribution *at
  most*. Without a `commitment` contribution binding someone to pursue it, there is no candidate —
  a number nobody committed to is the shadow of a claim, not a commitment.
- **Value ≠ generic aspiration.** ❌ *"Improve customer experience"* — rejected not because it is a
  bad ambition, but because nothing in it can be committed to, measured against or falsified.
  ✅ *"The Retail Banking Executive commits the bank to reducing abandoned mortgage applications by
  improving the digital application journey."* Aspiration becomes commitment when authority,
  outcome and accountability attach — often in *later* material, which is why identification never
  finally rejects an aspiration, it reports what is missing.

## The completeness view

Every candidate Value Record carries a completeness view: per mandatory role, one **state** grade —

```
supported | partial | missing | conflicting
```

— plus the one-sentence organisational reading, e.g. *"The organisation appears to have made this
value commitment, but the available evidence does not establish how success is measured or when the
commitment is reviewed."*

**State only, deliberately.** Whether a value was read directly from a span or inferred across spans
is carried by the supporting contributions' `derivation: explicit | inferred` field
([TDR-0026](../../../decisions/TDR-0026-value-recovery-vocabulary.md)) and is reported alongside —
never folded into the grades, so an inferred proposition can never present as a complete one, and an
incomplete one can never hide behind "inferred".

The completeness view preserves the recovery invariant: **failure to recover evidence is not
evidence that the organisational capability or commitment does not exist.**

## The six value classes, and three recovery conditions

Recovery must not privilege the easiest class because currency is easy to detect. The fixture
taxonomy ([`../fixtures/`](../fixtures/)) exercises six **value classes** —

**quantified** · **qualitative** · **normative** · **protective** · **environmental-social** ·
**conflicting**

— and three **recovery conditions**: **incomplete** · **superseded** · **no-value**. The first six
describe kinds of value and value relationships; the last three describe states of the evidence.
They are different axes and are never presented as nine equivalent classes.
