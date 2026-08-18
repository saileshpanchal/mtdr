# FIX-207 — must-not probe: a sixth state

**Contract expectation:** rejected

`likely` — a hedge between `inferred` and `unsupported`, offered in good faith because the evidence
felt partial.

There are five states and no sixth. `likely`, `weakly-supported` and `plausible` all encode a
judgement made at projection time about how good the evidence is, and a projection that grades its own
evidence has stopped reporting and started assessing. The recorded `epistemic_confidence` already
carries what the interpreter thought; anything further is new.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9207" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "beneficiary",
      "state": "likely",
      "rendered_value": "Tenants in council-managed housing",
      "chain": [
        {
          "contribution_ref": "RC-9207-a",
          "semantic_role": "beneficiary",
          "derivation": "inferred",
          "fragments": [{ "fragment_ref": "SF-9207-a", "source_ref": "minute.md" }]
        }
      ]
    }
  ]
}
```

## Must not

- Accept the document, or any other value outside the five.
- Add a state for "unreachable". Whether a fragment can presently be read is relational validity's
  question; the projection reports recorded derivation and is context-free, which is what makes two
  participants' projections comparable.
- Encode the same hedge as a numeric strength on the field or the chain.
