# Task

You are reconstructing governed organisational state from a fixed set of source documents, using the
MTDR standard at the pinned commit recorded in your run manifest.

Read the MTDR material you have been given. Then read the six source documents in the corpus
directory. Produce a capture that records what you did at each of eight boundaries.

## The corpus is closed

The six documents you have been given are **the complete evidence**. There is nothing else to find,
and nothing outside them may be consulted — not the web, not other repositories, not prior knowledge
about any organisation the material may resemble. If something you need is not in the six documents,
that absence is a result, and you record it as one.

## What to produce

Emit one `capture.json` conforming to `protocol/capture.schema.json`, carrying all eight boundaries:

1. **source selection** — the four sets: what you were given, what you read, what any conclusion
   traces back to, and what you read and set aside with a reason for each.
2. **fragments** — the spans of source text you worked from.
3. **contributions** — what each fragment was interpreted to mean, in which semantic role.
4. **assemblies** — how contributions were grouped into candidate records, with conflicts,
   supersessions, missing semantics and unresolved items recorded rather than settled.
5. **candidates** — the resulting records.
6. **projections** — for each record, what each field was derived from.
7. **validations** — the four-dimensional validation result for each record.
8. **eligibility** — for each record, the transition you assessed and its outcome.

Each of boundaries 2 through 8 has a published MTDR schema. Conform to it. Boundary 1 has a schema in
this protocol directory.

## How to work

- **Record what the sources say, not what would make a tidier record.** Where the material is silent,
  the record says so. Where it conflicts, the record carries the conflict.
- **Do not supply human acts.** No ratification, no counter-signature, no acceptance of accountability
  may be inferred from a document that does not carry one.
- **Do not add semantics to the standard.** If reconstruction seems to require a new field, enum value
  or semantic role, do not add one: record that the reconstruction could not be expressed and what was
  missing.
- **Show your derivation.** Every field in every record must be traceable through contributions to
  fragments to source text, or declared as a gap.
- Work only from the corpus and the MTDR material. Do not use the network.

## What is being measured

Whether independent reasoning environments, given identical evidence and the same standard, reconstruct
materially equivalent organisational state — **while preserving uncertainty, and exposing rather than
concealing divergence.**

You are not being scored on agreement with other runs. A recorded gap, a recorded conflict and a
recorded inability to express something are all correct outputs. Resolving an uncertainty the sources
do not resolve is not.
