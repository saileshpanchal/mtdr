# FIX-105 — incompatible versions between related objects are a relational failure

**Contract expectation:** accepted

Both objects exist, both are individually sound, and they cannot be interpreted together: a v1-shaped
Value Record is cited by a candidate assembled under the v2 semantics, where the beneficiary and
realisation axes mean different things.

TDR-0032 requires related objects to have *compatible* identities, states **and versions**. This is
the version arm, and it is why `specification.version` is a required field rather than a courtesy —
without it, neither object could state what it was assessed under and the incompatibility would be
invisible.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "interchange-structure",
    "id": "CA-9004",
    "ref": "tests/validation/synthetic/CA-9004-mixed-version-assembly.json"
  },
  "specification": { "id": "specification/candidate-assembly.md", "version": "1.0.0" },
  "assessed_state": "assembled",
  "context": {
    "id": "value-package-complete",
    "description": "The complete value package, both specification versions present.",
    "resolvable_refs": ["records/value/"]
  },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    {
      "dimension": "relational",
      "result": "fail",
      "reasons": [
        {
          "code": "incompatible-specification-version",
          "detail": "The assembly is governed by VR 2.0.0 semantics and cites VR-9101, raised under 1.3.0. The realisation axis does not carry across the versions."
        }
      ],
      "evidence": [
        { "ref": "records/value/package.yaml", "locus": "records[VR].prior_versions[1.3.0].schema: null" }
      ]
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

- Pass because both objects validate individually. Compatibility is a property *between* objects, and
  the whole reason relational validity is a separate dimension is that it cannot be established from
  either object alone.
- Migrate the v1 record to v2 semantics to make the assessment succeed. A record conforms to the
  specification version it was raised under, never a later one applied retroactively.
- Report `indeterminate`. Both versions were reachable and both are published; the incompatibility is
  established, not unknown.
- Report the failure on the semantic dimension. The assembly is intrinsically coherent — folding this
  into semantics would hide whether the object or its context was at fault.
