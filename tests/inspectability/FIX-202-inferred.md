# FIX-202 — one link in the chain was inferred, so the field is inferred

**Contract expectation:** accepted

Two contributions, one read directly and one inferred across spans. The field is `inferred`, because
the weaker link governs: a chain is only as explicit as its least explicit step.

This is the state most at risk of quiet promotion. An inferred beneficiary reported as `supported`
looks identical to a real one in every downstream view, and the `derivation` marker is the only thing
standing between the two.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9202", "ref": "tests/inspectability/synthetic/VR-9202.md" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "committed_by",
      "state": "inferred",
      "rendered_value": "Director of Environment and Place",
      "chain": [
        {
          "contribution_ref": "RC-9202-a",
          "semantic_role": "committed-by",
          "derivation": "explicit",
          "extraction_confidence": "high",
          "epistemic_confidence": "medium",
          "fragments": [
            {
              "fragment_ref": "SF-9202-a",
              "source_ref": "depot-programme-board-2026-04-02.md",
              "locator": { "kind": "line-range", "start": 8, "end": 9 }
            }
          ]
        },
        {
          "contribution_ref": "RC-9202-b",
          "semantic_role": "committed-by",
          "derivation": "inferred",
          "extraction_confidence": "high",
          "epistemic_confidence": "low",
          "fragments": [
            {
              "fragment_ref": "SF-9202-b",
              "source_ref": "scheme-of-delegation-v4.md",
              "locator": { "kind": "line-range", "start": 117, "end": 121 }
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

- Report `supported` because the explicit contribution "is enough on its own". If the inferred link
  were surplus it would not be in the chain; if it is in the chain, it is part of how the value was
  reached.
- Drop the inferred link to make the field cleaner. That is the same promotion with an extra step.
- Treat `epistemic_confidence: low` as a reason to omit the contribution. Weak evidence recorded is
  worth more than strong evidence implied.
- Add a note explaining why the inference is reasonable. That is retrospective justification, and it
  is the one thing this projection may never carry.
