# FIX-104 — a reference the context can see and that is not there is a relational failure

**Contract expectation:** accepted

The counterpart to [FIX-103](FIX-103-unavailable-reference-is-indeterminate.md). Here the declared
context covers the whole decision package, the referenced identifier falls squarely inside it, and no
governed representation exists. Nothing is unknown: a published requirement was demonstrably
violated.

The pair exists because the two cases are trivially confusable and have opposite consequences. What
separates them is not the reference — it is the **context**. That is why the context is declared in
the result rather than assumed.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "TDR-9003",
    "ref": "tests/validation/synthetic/TDR-9003-broken-lineage.md"
  },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "assessed_state": "proposed",
  "context": {
    "id": "decision-package-complete",
    "description": "The complete decision package. Every governed TDR identifier is within scope.",
    "resolvable_refs": ["decisions/"]
  },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    {
      "dimension": "relational",
      "result": "fail",
      "reasons": [
        {
          "code": "reference-unresolved",
          "detail": "derived_from cites TDR-0029, which is burnt. No governed representation exists and none ever will."
        }
      ],
      "evidence": [{ "ref": "decisions/ALLOCATION.md", "locus": "TDR-0029 — burnt" }]
    },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [
        { "code": "no-transition-requested", "detail": "No transition was requested of this subject." }
      ]
    }
  ]
}
```

## Must not

- Report `indeterminate`. The context covered the target's namespace; the absence was established,
  not merely unobserved. Softening a demonstrated violation is the mirror of hardening an unknown.
- Fail the structural or semantic dimensions because the relational one failed. The record parses and
  means what it says; it points at something that does not exist.
- Resolve the reference to a nearby identifier. A broken lineage link is not a typo to be corrected by
  a validator, and TDR-0034 exists precisely because near-miss identifiers are not interchangeable.
- Treat a burnt identifier as merely absent-for-now. Burnt is permanent, and the evidence cites the
  register that says so.
