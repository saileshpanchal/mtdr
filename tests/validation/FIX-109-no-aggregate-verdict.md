# FIX-109 — must-not probe: the aggregate verdict

**Contract expectation:** rejected

The live breach the contract was written to close. Four dimensions are reported honestly, one of them
failing, and a single top-level field summarises them into a green result. DAC-0033 constraint 8
permits an interface to summarise for usability but forbids a normative aggregate result from
overriding a failure or an indeterminate.

The schema closes every object, so the field is rejected structurally rather than deprecated in prose.
This is deliberate: a discouraged field is a field, and a field that can be read alone will be.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "TDR-9007" },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "conformant": true,
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    {
      "dimension": "relational",
      "result": "fail",
      "reasons": [{ "code": "reference-unresolved", "detail": "derived_from cites TDR-8888." }]
    },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [{ "code": "no-transition-requested", "detail": "None requested." }]
    }
  ]
}
```

## Must not

- Accept the document. The contract rejects `conformant`, and equally `valid`, `overall`, `passed`,
  `score` or any other field that could stand in for the four.
- Accept it "with a warning". A warning is what a consumer ignores.
- Offer a helper that computes such a field on the caller's behalf. The reference implementation has
  no `is_valid()`, no truthiness and no exit-code helper for exactly this reason.
- Treat a process exit status as the missing verdict. An exit code is an operational signal about a
  run, not a conformance judgement about a subject.
