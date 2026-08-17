# FIX-112 — must-not probe: the missing dimension

**Contract expectation:** rejected

Three dimensions reported, the failing one absent. Every field present is true; the document is a lie
by omission, and it is the easiest lie to tell.

The contract requires exactly four dimensions, each appearing exactly once, which is why the count is
fixed in the schema rather than described in prose. A dimension that may be omitted may be omitted
selectively, and it will be the inconvenient one.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "TDR-9009" },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [{ "code": "no-transition-requested", "detail": "None requested." }]
    }
  ]
}
```

## Must not

- Accept the document because everything reported is accurate. Selective truth is the failure mode.
- Accept a result with a dimension reported twice, or with a fifth. Both are rejected by the same
  fixed count.
- Treat an omitted dimension as `not-applicable` by default. Not-applicable is a finding with a
  reason; omission is the absence of a finding, and they must not be readable as the same thing.
- Let an interface hide a dimension for brevity. Summarising is permitted; retaining and exposing every
  dimension is required.
