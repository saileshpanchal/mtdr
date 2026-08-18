---
name: show-me
description: Answer "show me why this record says that" by walking each rendered value back to the contributions, fragments and locators behind it — and reporting honestly where the chain does not exist. Use this whenever someone asks where a value came from, before ratifying anything, when auditing a record's evidence, or when a record says something surprising. One skill serves every record type. It projects what was recorded and never constructs what was not.
---

# Show Me

This skill makes a record inspectable. It is written for humans and usable by AI assistants. Read
[`derivation-projection.md`](../../../specification/derivation-projection.md), then
[`provenance.md`](../../../specification/provenance.md) and
[`contribution-model.md`](../../../specification/contribution-model.md).

It is one skill rather than one per record type, for the reason
[`challenge-record`](../challenge-record/) is: the chain being walked is a property of
*interpretation*, not of any particular record. Field names come from the record package in
[`records/`](../../../records); everything else here is the same whatever is being projected.

## The one rule

**It projects what was recorded and never constructs what was not.**

You are not explaining the record. You are not justifying it, and you are certainly not making it
sound better founded than it is. You are reporting the derivation that exists — and where none exists,
reporting that, in those words.

## What this is not

Not explanation generation. Not retrieval-augmented answering. Not interpretability tooling that
reconstructs a plausible account of how a conclusion might have been reached. Every one of those
produces text where evidence is absent, which is the exact failure this skill exists to make
impossible.

Not a challenge either. Whether the evidence *should* support the value —
whether the span sustains the sentence, whether the grouping holds — is
[`challenge-record`](../challenge-record/)'s work. This skill hands it the chain and stops.

And not a validator. Whether a reference currently resolves is relational validity's question. A
projection is context-free: it reports what was recorded, so that two people running it in different
places get the same answer.

## Process

### 1. Take the record's rendered values, not its contributions

Start from what the record actually says, field by field. Starting from the contributions instead
produces a tidy report in which anything unsupported is simply absent — which is precisely the case
that most needs reporting.

### 2. Walk each value back

Value → contribution → fragment → locator. Carry through, unchanged: the semantic role, the
`derivation` marker, both confidences, the fragment's source reference and hash, and the locator.

Carry them **as recorded**. Do not recompute a confidence, do not summarise a span, do not tidy a
locator into something more readable.

### 3. Assign exactly one of five states

| State | When |
|---|---|
| `supported` | A chain exists and every contribution was read directly from its spans |
| `inferred` | A chain exists and at least one contribution was inferred across spans or from context |
| `conflicting` | Competing chains for the same role, with the recorded conflict named |
| `missing` | No chain, and the assembly declared the semantic absent |
| `unsupported` | No chain, no declaration — the record renders a value nothing accounts for |

**Do not invent a sixth.** Not `likely`, not `weakly supported`, not `plausible`, and no score
anywhere. Each would be a fresh judgement made at projection time, which is what a projection must not
contain.

### 4. Separate `missing` from `unsupported` deliberately

Both have an empty chain, and they mean opposite things. `missing` is a gap the interpretation
recorded and a reader can act on. `unsupported` is a value that arrived from nowhere.

If you cannot tell which, go and look for the declaration rather than choosing the kinder one. The
kinder one is `missing`, and defaulting to it hides the failure this whole model exists to expose.

### 5. Report the breaks as findings

A field that comes back `unsupported` is the most valuable output this skill produces. Say so plainly,
in the projection and in whatever you write around it.

## Outputs

A [derivation projection](../../../specification/derivation-projection.md) — the machine-readable
artefact — and, if a person asked, a reading of it.

The reading may reorganise and summarise for legibility. It may not add anything the projection does
not contain: no rationale, no likelihood, no reassurance, and no overall verdict on how well evidenced
the record is.

## Quality checks

- Did every field in the record get a state, including the ones nobody asked about?
- Is every `supported` field's chain complete to a locator, or was a step waved through?
- Was `missing` versus `unsupported` decided by looking for the declaration, or by feel?
- Does the prose add any claim the projection does not carry?
- Would a reader of the projection alone reach the same understanding as a reader of the prose?

## When to refuse

- **Asked to explain why the record is correct.** This skill reports derivation, not soundness. Offer
  the projection and route the question to [`challenge-record`](../challenge-record/).
- **Asked to fill in a missing chain**, or to describe what the evidence "would have been". Report
  `unsupported` and stop.
- **Asked for a single confidence figure** for the record. There is not one, and computing one would
  discard the field-level states that carry the actual information.

## Anti-patterns

- **Retrospective justification** — writing the account that would have led to the value. The
  cardinal failure, and it is easy, fluent and undetectable by reading.
- **Charitable defaulting** — an unaccounted-for value reported as `missing` because that reads as a
  known gap rather than an unexplained assertion.
- **Silent completion** — projecting only the fields with chains, so the record appears fully
  evidenced.
- **Confidence laundering** — averaging, rounding or upgrading the recorded confidences, or inventing
  a composite.
- **Summarising the span** — paraphrasing the source into something that supports the value more
  neatly than the source does.
- **Answering the challenge question** — drifting from *what produced this* into *is this right*.

## Scope note

This skill projects recorded derivation. What consumes a projection — a review interface, an audit
trail, a report — sits above the artefact boundary and is outside this standard entirely (TDR-0018).
