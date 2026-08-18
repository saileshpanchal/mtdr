# FIX-201 — a value walked back to its span

**Contract expectation:** accepted

The ordinary case, and the one that establishes what "supported" costs. Every contribution behind the
value was read directly from a span, each span has a locator, and both confidences are carried through
as they were recorded rather than recomputed.

Note what a `supported` state does *not* claim: that the value is correct, that the span sustains the
sentence, or that the record should be ratified. It claims that the derivation exists and is explicit.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9201", "ref": "tests/inspectability/synthetic/VR-9201.md" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "beneficiary",
      "state": "supported",
      "rendered_value": "Tenants in council-managed housing",
      "chain": [
        {
          "contribution_ref": "RC-9201-a",
          "semantic_role": "beneficiary",
          "derivation": "explicit",
          "extraction_confidence": "high",
          "epistemic_confidence": "medium",
          "fragments": [
            {
              "fragment_ref": "SF-9201-a",
              "source_ref": "housing-committee-minute-2026-03-11.md",
              "source_hash": "sha256:6f1c0b9a",
              "locator": { "kind": "line-range", "start": 42, "end": 44 }
            }
          ]
        }
      ]
    }
  ],
  "projector": { "name": "show-me", "version": "1.0.0" }
}
```

## Must not

- Report `supported` where any contribution in the chain is `inferred`. That is what `inferred` is
  for, and the two are not degrees of the same thing.
- Recompute, average or upgrade the confidences. `high` extraction with `medium` epistemic is a real
  and common combination — the words were read correctly; the claim behind them is weaker.
- Summarise or paraphrase the span into something that supports the value more neatly.
- Read `supported` as a judgement that the record is right. Whether the span sustains the sentence is
  `challenge-record`'s question.
