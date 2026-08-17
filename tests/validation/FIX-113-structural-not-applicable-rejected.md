# FIX-113 — must-not probe: structural validity waved away

**Contract expectation:** rejected

TDR-0033 permits structural `not-applicable` only where no serialised representation forms part of the
typed assessment. Every subject this contract admits has one — `participant` is deliberately excluded,
because execution is a behavioural claim and not a validation result — so the case is unreachable, and
an assessment reaching it has mislabelled something.

This is the dimension with the least defensible reason to be absent and the most obvious motive: it is
the one that fails loudly and mechanically.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "TDR-9010", "ref": "tests/validation/synthetic/TDR-9010-well-formed.md" },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "dimensions": [
    {
      "dimension": "structural",
      "result": "not-applicable",
      "reasons": [{ "code": "not-checked", "detail": "Schema validation was skipped for this run." }]
    },
    { "dimension": "semantic", "result": "pass" },
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

- Accept the document. A check that was skipped is `indeterminate` at best — the honest report that the
  validator does not know — and never "does not apply".
- Accept it because the reason is candid. A truthful reason attached to the wrong result is still the
  wrong result, and the result is what a consumer branches on.
- Admit a subject type without a serialised representation in order to make this legal. If such a
  subject is ever admitted, it arrives with a major version of this contract and its own reasoning.
