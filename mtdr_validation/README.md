# `mtdr_validation` — reference implementation

**Non-normative.** This is one implementation of the validation-result contract. It is not the
contract.

A conforming independent implementation is governed by
[`specification/validation-result.md`](../specification/validation-result.md) and
[`schemas/validation-result.schema.json`](../schemas/validation-result.schema.json) — **never by
behavioural equivalence with this code**. If this module and those documents disagree, this module is
wrong. Nothing here may be cited as a normative requirement, and no conformance claim may be
expressed as "matches `mtdr_validation`".

The distinction is the one JSON Schema itself makes between a validation vocabulary and any
particular validator's console output, and it matters directly: the recovery experiment compares
independent runtimes, and a runtime is not being measured against this Python.

## What it does

Builds validation results, serialises them to JSON, validates them against the published schema, and
renders a summary that exposes every dimension.

```python
from mtdr_validation import ValidationResult, Dim, PASS, NOT_APPLICABLE

r = ValidationResult(
    subject_type="record", subject_id="TDR-0034",
    subject_ref="decisions/TDR-0034-public-allocation-authority.md",
    spec_id="records/decision/specification/tdr.md", spec_version="1.14.0",
    assessed_state="accepted",
)
r.report(Dim.STRUCTURAL, PASS)
r.report(Dim.SEMANTIC, PASS)
r.report(Dim.RELATIONAL, PASS)
r.report(Dim.TRANSITION, NOT_APPLICABLE, reasons=[("no-transition-requested", "...")])

errors = r.validate()      # [] when the result satisfies the published schema
print(r.summary())
```

## What it deliberately will not do

`summary()` renders four lines and no fifth. There is no `is_valid()`, no `ok`, no exit-code helper
and no truthiness on the result object, because DAC-0033 constraint 8 forbids a normative aggregate
green result — and a convenience property that could be read alone would be read alone.

`report()` will not accept an illegal result for a dimension, and `validate()` re-checks against the
schema rather than trusting the builder. The builder is convenience; the schema is the contract.

Results carry no standing, no repair and no inferred value. `validate()` never modifies the object
assessed, and the caller's inputs are never mutated.

## Requirements

`jsonschema`. Nothing else — no MTDR application, register or service.
