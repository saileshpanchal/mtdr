# FIX-208 — must-not probe: the provenance score

**Contract expectation:** rejected

Every field reported honestly, and a single number summarising how well evidenced the record is.

It is the same failure as the aggregate conformance verdict, one layer down: a figure that can be read
alone will be read alone, and "87% evidenced" tells a reader nothing about *which* 13% — which is the
only part that matters. Two records at 87% can differ by one unsupported beneficiary.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9208" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "provenance_score": 0.87,
  "fields": [
    {
      "field": "beneficiary",
      "state": "supported",
      "rendered_value": "Tenants in council-managed housing",
      "chain": [
        {
          "contribution_ref": "RC-9208-a",
          "semantic_role": "beneficiary",
          "derivation": "explicit",
          "fragments": [{ "fragment_ref": "SF-9208-a", "source_ref": "minute.md" }]
        }
      ]
    }
  ]
}
```

## Must not

- Accept the document, or `confidence_score`, `coverage`, `completeness` or a count of supported
  fields presented as a proportion.
- Compute one in the prose reading instead.
- Offer one as a convenience for sorting or triage. Sorting records by provenance score is exactly
  the use that would make the number consequential.
