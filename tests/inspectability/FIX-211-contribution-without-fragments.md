# FIX-211 — must-not probe: a contribution with nothing behind it

**Contract expectation:** rejected

A chain link naming a contribution and no fragments. The walk stops one step short of evidence, and
the field still reports `supported`.

`fragments` requires at least one entry, matching the rule the RecordContribution schema already
carries: a contribution with no fragment behind it is an invention. A projection whose purpose is to
expose that cannot be the place it becomes expressible.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9211" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "beneficiary",
      "state": "supported",
      "rendered_value": "Tenants in council-managed housing",
      "chain": [
        {
          "contribution_ref": "RC-9211-a",
          "semantic_role": "beneficiary",
          "derivation": "explicit",
          "fragments": []
        }
      ]
    }
  ]
}
```

## Must not

- Accept the document, or a chain link with `fragments` omitted entirely.
- Accept a fragment with no `source_ref`. A span nobody can locate is not a locator.
- Report the field as `supported` on the strength of the contribution alone. The contribution is an
  interpretation; the fragment is the evidence.
