# FIX-115 — must-not probe: an indeterminate that says nothing

**Contract expectation:** rejected

`indeterminate` with no reason is not a finding. The whole content of the result is *what could not be
established and why* — strip that out and what remains is a shrug a reader will resolve in whichever
direction suits them, usually the convenient one.

The same rule binds `fail` (an unexplained negative is an assertion, not a finding) and
`not-applicable` (the result most easily used to make an inconvenient dimension disappear). Only
`pass` may stand bare: every applicable published requirement was satisfied, and the requirements are
already published.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "TDR-9012" },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "indeterminate" },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [{ "code": "no-transition-requested", "detail": "None requested." }]
    }
  ]
}
```

## Must not

- Accept the document, or accept `"reasons": []`. An empty list is the same omission with punctuation.
- Fill in a generic reason to satisfy the rule. "Could not be determined" restates the result; the
  reason must name the information that was missing.
- Downgrade the dimension to `pass` to avoid having to explain it, or upgrade it to `fail` for the same
  reason. Both convert an unknown into an established outcome.
- Resolve the unknown by inference and report `pass`. `indeterminate` is never permission to supply the
  missing fact — that is the rule this fixture protects by refusing to let the result go unexplained.
