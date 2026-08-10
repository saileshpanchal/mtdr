# Value fixtures

Known-answer conformance fixtures for the value language, organised on **two different axes** —
which the layout deliberately does not flatten into nine equivalent classes:

**Six value classes** — kinds of value and value relationships. Recovery must not privilege the
easiest class because currency is easy to detect; value is not synonymous with incremental benefit,
and organisations also value things they are explicitly trying not to lose.

| Class | Fixtures |
|---|---|
| [`quantified/`](quantified/) | FIX-001 (six-source assembly) · FIX-013 (the measure displacing the proposition) |
| [`qualitative/`](qualitative/) | FIX-006 (no currency, still a commitment) · FIX-014 (three wordings, one commitment) |
| [`normative/`](normative/) | FIX-007 (the obligation is not the commitment) |
| [`protective/`](protective/) | FIX-005 (preservation is fully a commitment) |
| [`environmental-social/`](environmental-social/) | FIX-008 (a beneficiary outside the organisation) |
| [`conflicting/`](conflicting/) | FIX-003 (proximity is never identity) · FIX-009 (commitments in tension) · FIX-017 (the explicit trade-off) |

**Three recovery conditions** — states of the evidence, not kinds of value:

| Condition | Fixtures |
|---|---|
| [`incomplete/`](incomplete/) | FIX-015 (committed but unmeasured — the completeness view) · FIX-016 (the `unclassified` outcome) |
| [`superseded/`](superseded/) | FIX-010 (the SME proposition across five sources) |
| [`no-value/`](no-value/) | FIX-011 (a KPI is not a commitment) · FIX-012 (activity is not value) |

Every fixture states **expected** and **must-not** results, and a run satisfying only the first has
not passed ([`specification/conformance.md`](../../../specification/conformance.md)). The
contribution vocabulary the fixtures exercise is
[`specification/value-contribution.md`](../specification/value-contribution.md); cross-language and
record-neutral cases live in [`tests/`](../../../tests/). Flat `FIX-*.md` files at this level are
pointer stubs from the pre-classification layout.

All material is fictional and marked as such, per [`CONTRIBUTING.md`](../../../CONTRIBUTING.md).
