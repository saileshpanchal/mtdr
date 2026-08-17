# Spike — does SHACL express MTDR's relational constraints?

**Non-normative.** A spike is an experiment whose finding is recorded. Nothing here is a requirement,
a dependency or a commitment, and no artefact in this directory is part of any conformance claim.

**Run:** `pip install pyshacl && python3 spikes/shacl-relational-validity/run.py`
**Executed:** 2026-08-17, pyshacl 0.40.1 / rdflib 7.6.0.

## Why it was worth asking

[TDR-0033](../../decisions/TDR-0033-four-dimensional-validity.md) made relational validity a
first-class conformance dimension. Before writing bespoke Python relational rules, the honest question
is whether a mature standard already does this — SHACL is a W3C Recommendation, has multiple
implementations, and is designed for exactly this shape of problem.

Four *real* MTDR relational constraints were expressed in [`shapes.ttl`](shapes.ttl) and run against a
conforming graph, a violating graph and one further case chosen deliberately.

## What happened

| Constraint | Expressible? | How |
|---|---|---|
| Lineage resolution — `derived_from` / `supersedes` resolve | **Yes, naturally** | Core SHACL, `sh:class`. Two lines. |
| DAC → TDR binding, including the *related* record's state | **Yes, naturally** | Core SHACL, `sh:node`. Reports both the binding and the nested reason, which maps cleanly onto MTDR's `reasons[]`. |
| Cross-object version compatibility | **Only via `sh:sparql`** | Comparing a value on the focus node against a value on a related node is outside core SHACL's property-pair constraints. |
| Package normative closure, with path-prefix matching | **Only via `sh:sparql`** | Needs `NOT EXISTS` + `STRSTARTS`. Works, and by this point the "shape" is a SPARQL query in a Turtle string. |

Two of four are genuinely elegant. Two are SPARQL wearing a SHACL coat — no worse than Python, and no
more declarative either.

## The finding that decides it

`data-violating.ttl` cites TDR-0029, which is **burnt**: no governed representation exists and, under
[TDR-0034](../../decisions/TDR-0034-public-allocation-authority.md), none ever will.
`data-unreachable.ttl` cites `ORG-TDR-0044`, a real governed record in a distribution this evaluation
context does not include.

MTDR requires **`fail`** for the first and **`indeterminate`** for the second
([FIX-104](../../tests/validation/FIX-104-broken-reference-is-relational-failure.md),
[FIX-103](../../tests/validation/FIX-103-unavailable-reference-is-indeterminate.md)). SHACL reports the
identical violation for both:

```
=== data-violating.ttl — conforms: False
    TDR-0032     derivedFrom      TDR-0029         derived_from must resolve to a decision record

=== data-unreachable.ttl — conforms: False
    TDR-9002     derivedFrom      ORG-TDR-0044     derived_from must resolve to a decision record
```

**In SHACL the data graph is the world.** Absence from the graph is absence, full stop; there is no
vocabulary for "the validator could not see this". The severity ladder does not help — `sh:Warning`
and `sh:Info` are *authoring-time* severity chosen by the shape author, not a runtime epistemic state,
and using `sh:Warning` for unreachability would require the shape author to know in advance which
references will be out of context, which is precisely the runtime fact SHACL cannot observe.

This is not a gap MTDR can absorb. DAC-0033 records both failure modes explicitly: treating every
unavailable relationship as failure "would make offline and zero-install use impractical", and
treating it as harmless "would conceal organisational inconsistency". Adopting SHACL as the relational
contract would force the first.

There is a second, quieter problem. SHACL requires an RDF projection of MTDR records that does not
exist. Building one and making it the relational contract would install a graph as a normative
dependency — the exact thing TDR-0033 declines: *"Relational validity does not require a central
register or graph. Graphs may compute it efficiently but are not normative dependencies."*

## What does work, and is worth keeping

Partition first, then validate. MTDR already declares its evaluation context before assessing
anything. Withhold everything the context cannot reach, report those references `indeterminate`, and
hand SHACL only the part of the world it is entitled to close over:

```
=== data-unreachable.ttl, partitioned by declared context — conforms: True
    (no violations within the declared context)
    outside the context, reported indeterminate by MTDR, never seen by SHACL: ORG-TDR-0044
```

The same graph, the same shapes, the correct answer — because the judgement SHACL cannot make was
made before it ran. Under that arrangement SHACL's violations map onto `fail` and the withheld set
maps onto `indeterminate`, and the four-result vocabulary survives.

That is a good arrangement, and it is not adoption. The interesting decision — what the context can
reach — stays outside SHACL, and so does the result contract.

## Disposition

**Map, not adopt.** SHACL is a sound **export target** for the resolvable subset of MTDR's relational
constraints, and an organisation already running a graph should use it: shapes can be generated from
MTDR's relational rules and evaluated efficiently, under a declared context that MTDR supplies. It is
**not** MTDR's relational conformance language, because the four-result vocabulary does not survive
the translation and adopting it would make a graph a normative dependency.

Recorded either way, which was the point of running it rather than assuming.
