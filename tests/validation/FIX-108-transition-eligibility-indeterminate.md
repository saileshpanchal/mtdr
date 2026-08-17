# FIX-108 — eligibility unknown, which is not the same as ineligible

**Contract expectation:** accepted

A requested transition whose prerequisite evidence is *cited* but sits outside the declared context.
The validator cannot see it, so it cannot say whether the prerequisites are met.

Contrast with [FIX-106](FIX-106-valid-now-ineligible-next.md), where the evidence was established to
be absent. Here it may well exist. Reporting `fail` would tell a reader the record is not ready when
in fact the assessment could not tell — and someone would go and manufacture evidence that already
existed.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "TDR-9006",
    "ref": "tests/validation/synthetic/TDR-9006-external-evidence.md"
  },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "assessed_state": "proposed",
  "requested_transition": { "from": "proposed", "to": "accepted" },
  "context": {
    "id": "clean-clone",
    "description": "The distribution alone. The cited ratification evidence is held in a system this context does not reach.",
    "resolvable_refs": ["decisions/"],
    "unreachable_refs": ["evidence://ratification/2026-08-14/board-minute"]
  },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "indeterminate",
      "reasons": [
        {
          "code": "prerequisite-evidence-unreachable",
          "detail": "The record cites ratification evidence the declared context cannot reach. Whether the prerequisites are satisfied is unknown."
        }
      ],
      "evidence": [
        { "ref": "tests/validation/synthetic/TDR-9006-external-evidence.md", "locus": "ratification_evidence" }
      ]
    }
  ]
}
```

## Must not

- Report `fail`. Unknown readiness is not established unreadiness, and the two prompt opposite actions.
- Report `pass` because the record says the evidence exists. A citation is a claim about evidence, not
  the evidence — and eligibility resting on the subject's own assertion is circular.
- Treat the `indeterminate` as licence to proceed with the transition "pending confirmation". It is not
  a soft yes any more than it is a soft no.
- Widen the context to reach the evidence without declaring it. If the context changes, it changes in
  the result, or nobody can reproduce the finding.
