# FIX-116 — must-not probe: the helpful validator

**Contract expectation:** rejected

A failure reported accurately, alongside the value the validator thinks should have been there. It is
the most sympathetic of the must-not probes and the most dangerous: a suggestion in a machine-readable
field is one script away from being applied, and the record will then carry a fact no human supplied.

A validator reports defects and gaps. It does not fill them, does not normalise the input, and does
not carry a corrected shadow copy of the object alongside the finding.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9013" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "assessed_state": "candidate",
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    {
      "dimension": "semantic",
      "result": "fail",
      "reasons": [{ "code": "beneficiary-absent", "detail": "No beneficiary is stated." }],
      "suggested_value": { "beneficiary": "SME customers" }
    },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [{ "code": "no-transition-requested", "detail": "None requested." }]
    }
  ]
}
```

## Must not

- Accept the document. `suggested_value`, `corrected` and `normalised` are all rejected by the closed
  object, at every level.
- Smuggle the suggestion into `detail` as "the beneficiary is probably SME customers". Prose is where
  an inference hides best; the reason states what is missing, not what it might have been.
- Repair the assessed object and report on the repaired version. The assessed object is byte-identical
  before and after — *missing means missing*, the same rule the recovery grammar applies to fragments.
- Report `indeterminate` instead, on the grounds that the beneficiary might be inferable. The
  beneficiary is a required meaning and it is absent; that is a demonstrated violation, and
  inferability is not evidence.
