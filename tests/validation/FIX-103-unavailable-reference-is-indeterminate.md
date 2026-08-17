# FIX-103 — an unreachable reference makes relational validity indeterminate, never failed

**Contract expectation:** accepted

The record is intrinsically sound and cites a record held elsewhere. The declared evaluation context
could not reach it — an offline clone, a partial distribution, a private repository the assessor has
no access to.

This is the case DAC-0033 calls out in both directions. Reporting `fail` would make offline and
zero-install use impossible, since every partial context would manufacture failures. Reporting `pass`
would conceal genuine organisational inconsistency behind a shrug. `indeterminate`, with the
unreachable reference named in the context, is the only honest report.

The distinction from [FIX-104](FIX-104-broken-reference-is-relational-failure.md) is the whole point:
there, the context *could* see the target and the target was not there.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "TDR-9002",
    "ref": "tests/validation/synthetic/TDR-9002-external-lineage.md"
  },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "assessed_state": "accepted",
  "context": {
    "id": "partial-distribution",
    "description": "This package only. The cited record is governed in a distribution not present.",
    "resolvable_refs": ["records/decision/"],
    "unreachable_refs": ["ORG-TDR-0044"]
  },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    {
      "dimension": "relational",
      "result": "indeterminate",
      "reasons": [
        {
          "code": "reference-unreachable",
          "detail": "derived_from cites ORG-TDR-0044, which the declared context cannot reach. Whether it resolves is unknown, not false."
        }
      ],
      "evidence": [{ "ref": "tests/validation/synthetic/TDR-9002-external-lineage.md", "locus": "derived_from" }]
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

- Report `fail`. An assessor who cannot see a thing has not established that the thing is wrong, and
  a contract that fails the unreachable makes portable validation impossible.
- Report `pass` because the reference is "probably fine". That is inference dressed as tolerance.
- Silently widen the context to go and find the reference. The context is *declared*; a validator that
  quietly reaches outside it has produced a result nobody can reproduce.
- Let the relational indeterminate suppress the structural and semantic passes, or vice versa. Three
  different findings, reported independently.
- Require a register or graph to make this determinate. Relational validity runs against a declared
  portable context; a graph may compute it faster and is not a normative dependency.
