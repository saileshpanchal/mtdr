# Adoption

The acceptance case for taking public MTDR and applying it to somebody else's framework.

Everything else in [`tests/`](../) checks the standard against itself. This checks the standard against
a stranger: material MTDR has never seen, produced by people who were not thinking about records, read
by someone with no access to the authors.

| | |
|---|---|
| [`brackwell/`](brackwell/) | A fictional local authority's fleet and depot modernisation framework — six documents |
| [`FIX-301`](FIX-301-brackwell-reconstruction.md) | What a conforming reconstruction produces, and what it must never do |

## The test

> Clone MTDR. Take this framework. Follow only the published instructions for your runtime. Can you
> reconstruct the expected candidate records — and show me why?

Deliberately **not** financial services. Every other fictional case in this repository is a bank, and
"this is an organisational language, not a banking ontology" is a claim better demonstrated than
repeated. The reconstruction should require no local-government semantics to be added anywhere; if it
does, that is the finding.

## Progressive disclosure

A run that loads the whole repository into context has not demonstrated portability, it has
demonstrated that context windows are large. The staged budget in
[`disclosure.py`](disclosure.py) measures what selecting and running one skill actually costs: the
catalogue alone, then one skill's body, then the reference knowledge it names. `tests/verify.py`
reports the three figures and fails if the catalogue stops being a small fraction of the corpus.
