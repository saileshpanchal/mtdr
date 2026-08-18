# FIX-209 — must-not probe: the filled gap

**Contract expectation:** rejected

`missing`, with a value rendered anyway — the placeholder that makes a record look complete while the
state field quietly says it is not.

The contract forbids `rendered_value` on `missing` for that reason. A declared gap has nothing to
render, and every plausible placeholder — "TBC", "not applicable", "to be confirmed", an empty string
— reads downstream as content.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9209" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "finance_countersignatory",
      "state": "missing",
      "rendered_value": "TBC",
      "chain": [],
      "reported_at": "CA-9209.missing_semantics[0]"
    }
  ]
}
```

## Must not

- Accept the document, whatever the placeholder text.
- Accept `missing` without `reported_at`. A gap nothing declared is `unsupported`, and the two must
  stay distinguishable.
- Accept `unsupported` *without* `rendered_value`. It is the mirror error: an unaccounted-for value
  with no value is a declared gap, and should be reported as one.
