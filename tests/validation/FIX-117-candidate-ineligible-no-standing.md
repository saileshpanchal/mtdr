# FIX-117 — valid as a candidate, ineligible for ratification, no standing

**Contract expectation:** accepted

The proof DAC-0033 constraint 3 has been waiting for, and the first of three that separate **validity**,
**eligibility** and **standing**.

A Value Record candidate lacking only its finance counter-signatory. It is structurally valid —
[TDR-0039](../../decisions/TDR-0039-state-relative-requirements.md) having corrected the schema so a
transition requirement is no longer an existence requirement — semantically coherent, relationally
clean, and **ineligible** for the transition it requests.

Until 1.29 this state could not be represented at all: the VR schema required a counter-signatory
globally, so the candidate its own specification §4.4 explicitly permits was rejected before any
dimension could report on it.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "VR-9301",
    "ref": "records/value/fixtures/incomplete/VR-9301-candidate-awaiting-countersignature.md"
  },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "assessed_state": "candidate",
  "requested_transition": { "from": "candidate", "to": "ratified" },
  "context": { "id": "value-package-complete", "resolvable_refs": ["records/value/"] },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "fail",
      "reasons": [
        {
          "code": "countersignatory-absent",
          "detail": "The transition to ratified requires a named finance counter-signatory. None is present, so the request cannot be placed before a decision-maker as complete."
        }
      ],
      "evidence": [{ "ref": "records/value/specification/vr.md", "locus": "§4.4" }]
    }
  ]
}
```

## Must not

- Report structural or semantic `fail`. The absence is permitted in this state and disqualifying only
  for the next one — which is the entire distinction TDR-0039 exists to protect.
- Name, infer or suggest a counter-signatory. Ratification requires a *person*, and supplying one is
  the most consequential invention available anywhere in this standard.
- Read the three passes as an overall pass with a footnote. The eligibility failure is the finding.
- Treat the record as having standing because it is well formed. It has none, and nothing here says
  otherwise.
