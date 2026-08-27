---
id: TDR-0035
conforms_to: mtdr/decision/tdr@1.15.0
title: Publish a standards boundary — what this standard adopts, maps, interoperates with and defers
status: accepted
template: full
decision_date: 2026-08-17
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0001, TDR-0020, TDR-0024, TDR-0032
confirmed_by_outcome: pending — review when an independent implementation has been built against this register without asking which external standards are required, or 2027-08-17, whichever is sooner
---

# TDR-0035 — Publish a standards boundary: what this standard adopts, maps, interoperates with and defers

## Context — what was known at the time

This repository already commits to being independently usable. [TDR-0001](TDR-0001-publish-as-neutral-open-standard.md)
publishes it as a neutral open standard; [TDR-0020](TDR-0020-open-organisational-record-repository-boundary.md)
requires that someone can clone it and produce conformant records without knowing that any particular
consumer exists; [TDR-0024](TDR-0024-packaging-independence.md) makes packagings distribution adapters
rather than architecture; [TDR-0032](TDR-0032-typed-multi-object-conformance.md) makes the zero-install
test explicit.

None of those says which *external standards* an adopter must also have. The register was
reconstructible — JSON Schema is obviously adopted, a graph obviously is not — but only by reading
fifteen decisions and inferring. An adopter who does not do that reading will guess, and different
adopters will guess differently. That is how a portable standard acquires an architecture nobody
decided on.

The immediate trigger was sharper. [TDR-0033](TDR-0033-four-dimensional-validity.md) made relational
validity a first-class dimension, and the obvious next step was to write bespoke relational rules in
Python. Writing a validation language when SHACL exists would be an expensive thing to get wrong by
default, so the question was worth asking properly rather than answering by preference.

## Decision

**Publish [`specification/standards-boundary.md`](../specification/standards-boundary.md): a register
naming every external standard this specification touches, with a reasoned disposition and an explicit
statement of what that disposition does not mean.**

The vocabulary is `adopt | map | interoperate | defer | reject`. The load-bearing distinction is
**adopt versus interoperate**: *everything MTDR adopts, an adopter must also have.* That is the entire
cost of the boundary, and it is why the adopt column has three entries — JSON Schema, the `SKILL.md`
skill surface and portable markdown. Structural ideas borrowed from elsewhere, such as in-toto's
subject-and-versioned-predicate envelope, are **mapped, not adopted**: taking a shape costs an adopter
nothing, and calling it adoption would misstate what they need to have.

The selection rule, stated so future entries are decided rather than negotiated:

> **Adopt** where the standard is mature, ubiquitous and cheap for an adopter to already have.
> **Map** where the concepts correspond but the dependency would not be cheap. **Interoperate** where
> the value is real and downstream. **Defer** where the requirement has not arrived.

**Each row states what its disposition does not mean.** A register of one-word verdicts would be read
as endorsement; the foreclosure column is where the actual boundary lives.

### The SHACL question, decided on evidence

SHACL entered this register as a spike and left it as a **map**, because the spike was
[executed rather than assumed](../spikes/shacl-relational-validity/README.md). Four real MTDR
relational constraints were expressed as shapes and run.

Two express beautifully in core SHACL — lineage resolution via `sh:class`, and DAC-to-record binding
including a condition on the related record's state via `sh:node`, which even reports the nested reason
in a form that maps onto the result contract's `reasons`. Two need `sh:sparql`, at which point the
shape is a SPARQL query in a Turtle string and no more declarative than Python.

The decision turns on neither of those. **SHACL cannot express `indeterminate`.** In SHACL the data
graph is the world: a reference to a burnt identifier that will never exist, and a reference to a real
record held in a distribution this context cannot reach, produce the identical violation. MTDR requires
`fail` for the first and `indeterminate` for the second, and DAC-0033 names both failure modes of
getting this wrong — treating every unavailable relationship as failure makes offline and zero-install
use impractical; treating it as harmless conceals real organisational inconsistency. The severity ladder
does not rescue it: `sh:Warning` is an authoring-time choice by the shape author, not a runtime
epistemic state, and using it for unreachability would require knowing in advance which references will
be out of context — which is precisely the fact SHACL cannot observe.

There is a second objection, quieter and also sufficient. SHACL needs an RDF projection of MTDR records
that does not exist; building one and making it the relational contract installs a graph as a normative
dependency, which TDR-0033 explicitly declines.

What the spike *did* establish is worth keeping: **partition by the declared evaluation context first,
then validate.** Withhold what the context cannot reach, report it `indeterminate`, and hand SHACL only
the part of the world it is entitled to close over. The same graph and the same shapes then give the
correct answer, because the judgement SHACL cannot make was made before it ran. That is a good
arrangement for a graph-native adopter and it is not adoption — the interesting decision stays outside
SHACL, and so does the result contract.

## Evidence

- **Business** — an adopter's first question is what else they must install. A standard that cannot
  answer it in one page is answering it in a procurement meeting instead, badly.
- **Architecture** — the adopt/interoperate line is the same line TDR-0024 draws for packagings and
  TDR-0032 draws for the register. This record applies it outward rather than inventing a new rule.
- **Regulatory** — not material to this decision.
- **Operations** — the register is checkable. The suite verifies every row carries a legal disposition
  and a stated reason, so a row cannot be added as a bare verdict.
- **Customer** — not material at repository level.
- **Data** — none beyond the register itself.
- **External** — the SHACL spike is the strongest evidence here and it is first-hand: shapes written
  against real constraints, run under pyshacl 0.40.1, with the finding recorded either way. The
  in-toto Statement layer and JSON Schema's separation of vocabulary from output are both structural
  precedents this repository has already followed.

## Alternatives rejected

1. **Leave the boundary implicit in the existing decisions.** Rejected: it is reconstructible only by
   reading fifteen records, which means it will be guessed instead.
2. **Adopt SHACL for relational validity.** Rejected on the evidence above: the four-result vocabulary
   does not survive the translation, and a graph would become a normative dependency.
3. **Reject SHACL outright.** Rejected as overreach. It works correctly on a context-partitioned
   subset, and a graph-native adopter should use it; refusing to say so would waste a real finding.
4. **Adopt W3C PROV rather than mapping it.** Rejected: the concepts correspond, and the dependency
   would oblige every adopter to carry an RDF stack for a correspondence a document can express.
5. **Defer the whole register until an adopter asks.** Rejected: the first adopter is exactly who
   cannot afford to wait for it, and by then the guesses are already in their architecture.
6. **Publish dispositions without the foreclosure column.** Rejected: one-word verdicts read as
   endorsement, and "interoperate" without "never a dependency" is how a dependency arrives.

## Options foreclosed

- No external standard may become an MTDR dependency without an entry in this register saying so.
- No graph, policy engine, agent platform, transport or machine-identity system may be required to
  interpret, validate or produce a conformant record.
- SHACL cannot become the relational conformance language without superseding this record.
- A register row cannot be added as a bare verdict: disposition, reasoning and foreclosure or nothing.

## Consequences and review

Success is an independent implementation built from this register without asking which external
standards are required, and a SHACL-based relational checker built by someone else that agrees with
MTDR's results on the reachable subset while reporting the rest as unknown.

The register is deliberately revisable, and one entry already moved under evidence rather than opinion.
That is the standard the remaining fourteen should be held to when they are revisited: **run it, then
record what happened, including when the answer is inconvenient.**

Review at the confirmed-by-outcome trigger, or whenever a deferred entry's requirement actually
arrives.
