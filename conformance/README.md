# Moved

This file is now [`tests/conformance/README.md`](../tests/conformance/README.md) — relocated in the v1.15.0 package restructure
([TDR-0021](../decisions/TDR-0021-record-package-architecture.md)). This stub exists so links in immutable decision records and changelog history
keep resolving; do not add content here.

## Everything in this directory moved

Every file here is a redirect. Single-language fixtures now live with their record package, and
cross-language fixtures under [`tests/conformance/`](../tests/conformance/).

| This stub | Now lives at |
|---|---|
| `README.md` | [`tests/conformance/README.md`](../tests/conformance/README.md) |
| `FIX-001-value-commitment-across-six-sources.md` | [`records/value/fixtures/quantified/FIX-001-value-commitment-across-six-sources.md`](../records/value/fixtures/quantified/FIX-001-value-commitment-across-six-sources.md) |
| `FIX-002-one-fragment-two-objects.md` | [`tests/conformance/FIX-002-one-fragment-two-objects.md`](../tests/conformance/FIX-002-one-fragment-two-objects.md) |
| `FIX-003-two-commitments-not-one.md` | [`records/value/fixtures/conflicting/FIX-003-two-commitments-not-one.md`](../records/value/fixtures/conflicting/FIX-003-two-commitments-not-one.md) |
| `FIX-004-complete-in-one-source.md` | [`records/decision/fixtures/FIX-004-complete-in-one-source.md`](../records/decision/fixtures/FIX-004-complete-in-one-source.md) |
