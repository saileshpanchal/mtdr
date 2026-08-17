# FIX-114 — must-not probe: eligibility passed for a transition nobody requested

**Contract expectation:** rejected

No `requested_transition`, and `transition-eligibility: pass`. Eligible for *what*? The result reads
as a general endorsement, which is exactly how it would be quoted.

Eligibility is always relative to a **named** requested transition. Without one the only legal result
is `not-applicable`, and the constraint runs in both directions: a result that names a transition must
actually evaluate it, and may not answer `not-applicable`.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "TDR-9011" },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "assessed_state": "proposed",
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    { "dimension": "transition-eligibility", "result": "pass" }
  ]
}
```

## Must not

- Accept the document, or infer the intended transition from `assessed_state`. A validator guessing
  what was being asked has invented the question as well as the answer.
- Accept the mirror image: a result carrying a `requested_transition` and reporting
  `transition-eligibility: not-applicable`. Something was asked; it must be answered, even if the
  answer is `indeterminate`.
- Read an unqualified eligibility pass as readiness in general. Ready for one named transition is the
  only thing this dimension can ever say.
