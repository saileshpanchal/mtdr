# FIX-210 — must-not probe: the helpful projection

**Contract expectation:** rejected

An honest `unsupported` finding, alongside the value the projector believes was intended.

It is the sympathetic failure. The suggestion may well be right — and a machine-readable suggestion is
one script away from being applied, after which the record carries a fact no human supplied and no
source contains.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9210" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "baseline",
      "state": "unsupported",
      "rendered_value": "£1.4m annual depot running cost, 2025/26",
      "chain": [],
      "suggested_value": "£1.42m per the FY26 revenue outturn"
    }
  ]
}
```

## Must not

- Accept the document, or `inferred_value`, `corrected`, `normalised` or `probable_source`.
- Put the suggestion in prose instead — "this probably comes from the FY26 outturn". Prose is where an
  inference hides best.
- Attach a candidate fragment "for the reader to check". A fragment in the chain is a claim that it
  contributed; if it did, it would have been recorded.
