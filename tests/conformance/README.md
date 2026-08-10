# Cross-language conformance fixtures

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

Known-answer tests for the interpretation skills. Each fixture supplies synthetic source material
and states exactly what a conforming run must produce — and, more importantly, what it must **not**.
Single-language fixtures live in their package (`records/<language>/fixtures/`); this directory holds
the cross-language cases and the index of all four.

These complement the [agent probes](agent-probes.md), which test a deployed
agent's adherence to the standard's rules. These probe whether interpretation reconstructs
organisational state faithfully.

## The fixtures

| Fixture | Proves |
|---|---|
| [FIX-001](../../records/value/fixtures/FIX-001-value-commitment-across-six-sources.md) | A commitment assembles across six sources, with gaps reported and a revision recognised as supersession |
| [FIX-002](FIX-002-one-fragment-two-objects.md) | One span contributes to two different objects — reconstruction, not document classification |
| [FIX-003](../../records/value/fixtures/FIX-003-two-commitments-not-one.md) | Two similar commitments in one programme are **not** merged |
| [FIX-004](../../records/decision/fixtures/FIX-004-complete-in-one-source.md) | A source that does carry a complete record is not fragmented artificially |

FIX-003 is the most important of the four. It is the only one whose failure produces output that
looks *better* than a pass — a single tidy candidate instead of two — which is why it must be run
every time and never judged by appearance.

## How to run

Supply the fixture's sources to `identify-record-contributions`, pass the result through
`reconcile-record-fragments`, then the relevant `draft-*` skill, then `challenge-record`. Compare
against the fixture's **Expected** section.

A run is conforming only if it satisfies both the expected results **and** every entry under
**Must not**. Producing the right candidate by the wrong route — filling a gap that happens to be
correct, merging on similarity where the entity identifiers also agreed — is a failure, because
the same behaviour on real material will be wrong and undetectable.

## Counts are ranges, deliberately

Fragment and contribution counts are stated as ranges. Where a skill draws span boundaries is a
judgement, and a fixture demanding an exact count would test span segmentation rather than
interpretation. What is **not** a range: the number of candidates, the set of reported missing
semantics, and every entry under **Must not**.

## All material here is fictional

Every organisation, individual, figure and programme in these fixtures is invented, per
`CONTRIBUTING.md`. Identifiers follow each fictional organisation's own numbering — record ids are
unique per organisation, not globally.
