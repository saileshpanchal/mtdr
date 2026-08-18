# FIX-204 — a declared gap

**Contract expectation:** accepted

The interpretation looked for the semantic, did not find it, and said so. The projection reports
`missing` and points at where the absence was declared.

There is no `rendered_value`, because there is nothing to render: the record does not claim a finance
counter-signatory, and the projection does not manufacture the appearance of one.

This is the useful half of the pair with [FIX-205](FIX-205-unsupported-undeclared.md). A declared gap
tells a reader exactly what to go and find.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9204", "ref": "tests/inspectability/synthetic/VR-9204.md" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "finance_countersignatory",
      "state": "missing",
      "chain": [],
      "reported_at": "CA-9204.missing_semantics[0]"
    }
  ],
  "projector": { "name": "show-me", "version": "1.0.0" }
}
```

## Must not

- Carry a `rendered_value`. A declared gap has nothing to render, and a placeholder — "TBC", "not
  applicable", an empty string — is a filled gap wearing a gap's clothing.
- Nominate a plausible counter-signatory from the finance names elsewhere in the sources. That is the
  single most consequential invention available here.
- Report `unsupported`. The absence was declared; treating a recorded finding as an unexplained one
  discards the interpretation's most useful output.
- Treat the gap as a defect in the projection. It is a finding about the organisation's evidence.
