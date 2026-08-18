# FIX-203 — two chains for one role, and the conflict is named

**Contract expectation:** accepted

Competing contributions for the same semantic role, with no ordering and no shared authority to
settle them. The projection reports both chains and points at the `conflicts` entry in the assembly
that recorded the disagreement.

`conflict_ref` is required for exactly this reason: a projection that asserted a conflict without one
would be *finding* a conflict rather than *reporting* one, which is interpretation, and interpretation
happened earlier.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9203", "ref": "tests/inspectability/synthetic/VR-9203.md" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "reconcile_by",
      "state": "conflicting",
      "chain": [
        {
          "contribution_ref": "RC-9203-a",
          "semantic_role": "reconcile-by",
          "derivation": "explicit",
          "extraction_confidence": "high",
          "epistemic_confidence": "medium",
          "fragments": [
            {
              "fragment_ref": "SF-9203-a",
              "source_ref": "fleet-business-case-v2.md",
              "locator": { "kind": "line-range", "start": 61, "end": 61 }
            }
          ]
        },
        {
          "contribution_ref": "RC-9203-b",
          "semantic_role": "reconcile-by",
          "derivation": "explicit",
          "extraction_confidence": "high",
          "epistemic_confidence": "medium",
          "fragments": [
            {
              "fragment_ref": "SF-9203-b",
              "source_ref": "capital-programme-schedule.md",
              "locator": { "kind": "cell-range", "sheet": "FY27", "range": "D14:D14" }
            }
          ]
        }
      ],
      "conflict_ref": "CA-9203.conflicts[0]"
    }
  ],
  "projector": { "name": "show-me", "version": "1.0.0" }
}
```

## Must not

- Render a single value by choosing between the two. `conflicting` carries no `rendered_value`
  precisely so that no choice can be smuggled in as a projection.
- Resolve by recency, by source dignity, or by which document looks more official. None of those is
  authority lineage.
- Report `conflicting` without `conflict_ref`. A conflict the assembly did not record is one this
  projection invented.
- Report two separate fields to avoid the conflict. The role is one role.
