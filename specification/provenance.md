# Provenance

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

## The one rule

**No interpreted value exists without a locatable span of source material behind it.**

Provenance is not metadata attached after the fact. It is the chain that makes an interpretation
checkable, and it runs unbroken from the ratified record back to the characters in the source:

```
record field  →  contribution  →  fragment(s)  →  locator + source_hash  →  the source
```

Any break in that chain makes the value unfalsifiable. An unfalsifiable value in a governed record is
worse than a missing one, because it carries the same authority while supporting none of it.

## What travels with the artefact

A candidate record carries enough provenance for a reader to understand how it was derived. At
minimum, per interpreted field: the fragment or fragments behind it, their locators, the source
identifiers and hashes, and the interpreter and version that read them.

What happens to that provenance after ratification is the adopter's decision, not this standard's. A
conforming use may keep it in the record, alongside it, or discard it once a named human has
ratified the record and taken ownership of its content. The standard requires that provenance exist
at the moment of proposal — not that it be preserved forever by everyone.

## The source may change

`source_hash` exists because material moves. A board pack is revised, a spreadsheet is edited, a page
is rewritten. A candidate assembled from a source that has since changed is not automatically wrong,
but it is no longer verifiable against what it claims, and a reader must be able to detect that.

Recording the hash is cheap. Discovering six months later that a record's evidence cannot be located
is not.

## Provenance is not authority

That a value is well-evidenced says nothing about whether anyone was entitled to commit the
organisation to it. Provenance answers *where did this come from*; authority answers *who was entitled
to say it*. This standard carries the first and deliberately does not model the second — see
[`ARCHITECTURE.md`](../ARCHITECTURE.md), where authority is named as a concern that does not appear as
a row, and [`candidacy-and-ratification.md`](candidacy-and-ratification.md).

## Anti-patterns

- **Document-level provenance** — "derived from the Q3 board pack", which locates nothing.
- **Provenance by summary** — a paraphrase of the source recorded as the source.
- **Retrofitted provenance** — deciding the value first and finding a supporting span afterwards. The
  chain runs one way.
- **Provenance as decoration** — carried in the artefact but never checked, so a broken locator is
  never discovered.
