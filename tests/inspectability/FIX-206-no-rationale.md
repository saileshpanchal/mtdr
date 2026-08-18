# FIX-206 — must-not probe: the retrospective justification

**Contract expectation:** rejected

A well-formed chain, and a field explaining why the value is reasonable. The explanation is fluent,
plausible and was written after the fact by something that does not know whether it is true.

This is the cardinal failure of inspectability, and it is dangerous precisely because it reads well.
A reader given a chain and a rationale will read the rationale. The contract therefore has nowhere to
put one: no `explanation`, `reasoning`, `justification`, `summary` or `notes`, and the object is
closed so the field is refused rather than discouraged.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9206" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "beneficiary",
      "state": "supported",
      "rendered_value": "Tenants in council-managed housing",
      "chain": [
        {
          "contribution_ref": "RC-9206-a",
          "semantic_role": "beneficiary",
          "derivation": "explicit",
          "fragments": [{ "fragment_ref": "SF-9206-a", "source_ref": "minute.md" }]
        }
      ],
      "notes": "The committee's framing makes tenants the clear intended beneficiary."
    }
  ]
}
```

## Must not

- Accept the document, under any field name. The prohibition is on the *act*, not the spelling.
- Move the rationale into the prose reading instead. The reading may reorganise what the projection
  contains and may add nothing to it.
- Accept a rationale that happens to be accurate. Whether it is accurate is unknowable from the
  projection, which is the entire problem.
- Confuse this with a reason on a validation result. Those state what was *established*; this states
  what someone thought.
