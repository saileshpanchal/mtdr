# FIX-212 — must-not probe: a projection conferring standing

**Contract expectation:** rejected

Every field supported, and the projection recording that the record is therefore ratified.

Well-evidenced and ratified are different claims, and the gap between them is
[TDR-0027](../../decisions/TDR-0027-human-ratification-confers-standing.md): standing originates in an
authorised human act. A complete derivation chain is evidence a human could act on, and never the act.

The temptation is real because the inference feels safe — everything is supported, so what is left to
decide? What is left is the decision.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9212" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "standing": "ratified",
  "fields": [
    {
      "field": "beneficiary",
      "state": "supported",
      "rendered_value": "Tenants in council-managed housing",
      "chain": [
        {
          "contribution_ref": "RC-9212-a",
          "semantic_role": "beneficiary",
          "derivation": "explicit",
          "fragments": [{ "fragment_ref": "SF-9212-a", "source_ref": "minute.md" }]
        }
      ]
    }
  ]
}
```

## Must not

- Accept the document, or `ratified`, `accepted`, `approved`, `authority` or `fit_to_ratify`.
- Infer readiness for ratification from a fully supported projection. Whether the prerequisites for a
  transition are met is transition-eligibility's report, and even that confers nothing.
- Present a complete chain as an argument for ratification in the prose reading.
