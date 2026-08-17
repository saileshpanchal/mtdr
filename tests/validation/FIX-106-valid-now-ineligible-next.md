# FIX-106 — valid in its current state, ineligible for the state it requests

**Contract expectation:** accepted

The load-bearing case of TDR-0033. A proposed record is structurally sound, semantically coherent and
relationally clean. It requests acceptance and lacks the ratification evidence TDR-0027 requires.

**Validity is relative to the current state.** The missing evidence is required for the *transition*,
not for the state the record legitimately occupies now, so it must not make the record invalid. It
makes the record ineligible, which is a different and more useful thing to be told.

A `pass` here would have meant only that the request may be **placed before** the authorised human
decision-maker. It would not perform the transition, authorise it, or confer standing.

> **Scope note.** This is the transition-eligibility *shape*, proved on a decision record. It is not
> DAC-0033 constraint 3, which requires the incomplete Value Record — a candidate lacking only its
> finance counter-signature — to pass current-state validity while failing eligibility. That proof
> waits on TDR-0019 remediating the VR schema, and DAC-0033 constraint 6 forbids fixing the schema
> opportunistically here. The gap stays visible rather than being quietly satisfied by a neighbouring
> case.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "TDR-9005",
    "ref": "tests/validation/synthetic/TDR-9005-awaiting-ratification.md"
  },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "assessed_state": "proposed",
  "requested_transition": { "from": "proposed", "to": "accepted" },
  "context": {
    "id": "decision-package-complete",
    "resolvable_refs": ["decisions/", "records/decision/"]
  },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "fail",
      "reasons": [
        {
          "code": "ratification-evidence-absent",
          "detail": "The transition to accepted requires evidence of an authorised human act. No such evidence is present, so the request cannot be placed before a decision-maker as complete."
        }
      ],
      "evidence": [
        { "ref": "decisions/TDR-0027-human-ratification-confers-standing.md", "locus": "Decision" }
      ]
    }
  ]
}
```

## Must not

- Report structural or semantic `fail` because ratification evidence is missing. A transition-only
  requirement cannot invalidate a state in which its absence is permitted — this is the exact defect
  TDR-0033 was written to fix.
- Supply, name or infer the ratifying human. Filling in the missing act is the most consequential
  invention a validator could make, and `indeterminate` would not license it either.
- Read `transition-eligibility: pass` — had it passed — as ratification, standing, approval, or
  permission to write `status: accepted`. It means the request is ready to be *asked*.
- Perform or record the transition as a side effect of assessing it.
- Present the three passes as an overall pass with a caveat. The eligibility failure is the finding.
