# Validation-result fixtures

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

Known-answer tests for the result contract itself —
[`specification/validation-result.md`](../../specification/validation-result.md) and
[`schemas/validation-result.schema.json`](../../schemas/validation-result.schema.json), required by
[TDR-0033](../../decisions/TDR-0033-four-dimensional-validity.md).

These are cross-language and therefore outside every package. They test what a result may **say**, not
what any particular validator computes: each fixture carries a complete serialised result and states
whether the contract must accept or reject it. The subjects those results are about live in
[`synthetic/`](synthetic/).

`tests/verify.py` runs them on every invocation.

## What each fixture proves

| Fixture | Expectation | Proves |
|---|---|---|
| [FIX-101](FIX-101-four-dimensions-reported.md) | accepted | The baseline: four dimensions, a named subject, a named specification, no verdict |
| [FIX-102](FIX-102-structural-failure-recorded-not-cascaded.md) | accepted | A structural failure records its dependents explicitly instead of skipping them |
| [FIX-103](FIX-103-unavailable-reference-is-indeterminate.md) | accepted | An unreachable reference is `indeterminate` |
| [FIX-104](FIX-104-broken-reference-is-relational-failure.md) | accepted | A reference the context can see and that is absent is `fail` |
| [FIX-105](FIX-105-incompatible-specification-version.md) | accepted | Individually valid objects can be relationally incompatible by version |
| [FIX-106](FIX-106-valid-now-ineligible-next.md) | accepted | Current-state validity and transition eligibility are different questions |
| [FIX-107](FIX-107-candidate-package-not-applicable.md) | accepted | `not-applicable` where rules genuinely do not exist yet |
| [FIX-108](FIX-108-transition-eligibility-indeterminate.md) | accepted | Eligibility unknown is not eligibility failed |
| [FIX-109](FIX-109-no-aggregate-verdict.md) | rejected | No aggregate verdict may override a dimension |
| [FIX-110](FIX-110-no-standing-conferred.md) | rejected | Validation confers no standing |
| [FIX-111](FIX-111-no-collection-subject.md) | rejected | No collection-conformance claim until its contract exists |
| [FIX-112](FIX-112-no-dimension-omitted.md) | rejected | No dimension may be omitted |
| [FIX-113](FIX-113-structural-not-applicable-rejected.md) | rejected | A skipped check is not an inapplicable one |
| [FIX-114](FIX-114-eligibility-without-a-transition.md) | rejected | Eligibility is always relative to a named requested transition |
| [FIX-115](FIX-115-indeterminate-without-a-reason.md) | rejected | An unexplained negative result is an assertion, not a finding |
| [FIX-116](FIX-116-no-repair-or-inferred-value.md) | rejected | Validators report gaps; they do not fill them |
| [FIX-117](FIX-117-candidate-ineligible-no-standing.md) | accepted | A candidate lacking only its counter-signatory: valid, ineligible, no standing |
| [FIX-118](FIX-118-eligible-still-no-standing.md) | accepted | The same candidate, counter-signed: **eligible, and still no standing** |
| [FIX-119](FIX-119-ratified-standing-evidenced-elsewhere.md) | accepted | Ratified: standing exists, and the result still does not carry it |

The three pairs are the ones to run together, because each pair is separated by a single fact that is
easy to lose: 103/104 (unreachable vs absent), 106/108 (ineligible vs unknown), 113/115 (inapplicable
vs unestablished). Collapsing either half of a pair into the other produces results that look
reasonable and mislead in opposite directions.

## Format

Each fixture carries:

- **`**Contract expectation:** accepted | rejected`** — what the published schema must do with it;
- one fenced `json` block — the complete serialised result;
- a **Must not** section — the ways of getting the right answer by the wrong route.

A fixture without a must-not section is a non-conforming fixture
([TDR-0025](../../decisions/TDR-0025-conformance-architecture.md)), and the suite enforces that here as
everywhere else.

## What these fixtures do not prove

They exercise the contract, not a validator's judgement. Whether an implementation *correctly decides*
that a given record's relational validity is indeterminate is a behavioural claim, tested under
TDR-0032 against the fixtures, corpus and probes — never inferred from the fact that its output
serialises.

**The 117–118–119 sequence is the constructive proof of `validity ≠ eligibility ≠ standing`**, and
118 is the one that matters. 117 shows the machine correctly withholding when a prerequisite is
missing, which is easy. 118 shows it correctly refusing to grant when it has **no mechanical objection
left** — the only condition under which TDR-0027's boundary is genuinely tested. 119 closes it: even
for a ratified record, the result says nothing about standing, because a validator that could confirm
standing could also manufacture it.

DAC-0033 constraint 3 was satisfied by that sequence at 1.29, after
[TDR-0039](../../decisions/TDR-0039-state-relative-requirements.md) corrected the schema so the state
could be represented at all.
