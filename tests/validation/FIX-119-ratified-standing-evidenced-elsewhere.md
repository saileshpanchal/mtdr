# FIX-119 — ratified: standing exists, and the result still does not carry it

**Contract expectation:** accepted

The third state, completing **validity ≠ eligibility ≠ standing**.

A named individual has ratified the commitment. The record now says `status: ratified` and the
organisation is accountable for it. Assessing it produces:

- three content dimensions reporting on the record as it now stands;
- `transition-eligibility: not-applicable`, because **no transition is being requested** — the record
  is in the state it was moved to, not asking to move again.

And the result says **nothing whatever about standing**. Not that it exists, not that it is valid, not
that the ratification was proper. Standing is evidenced by the ratification act, which lives outside
this contract and outside the record — the record merely *represents* it, on evidence
([TDR-0027](../../decisions/TDR-0027-human-ratification-confers-standing.md),
[TDR-0031](../../decisions/TDR-0031-reconcile-ratified-judgement-after-identifier-collision.md)).

A validator that could confirm standing could also manufacture it, which is why it cannot see it at
all.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "VR-9303",
    "ref": "records/value/fixtures/incomplete/VR-9303-ratified.md"
  },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "assessed_state": "ratified",
  "context": { "id": "value-package-complete", "resolvable_refs": ["records/value/"] },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [
        {
          "code": "no-transition-requested",
          "detail": "The record is being assessed in its current state. Nothing is being asked of it."
        }
      ]
    }
  ]
}
```

## Must not

- Add a field asserting that standing exists, is valid, or was properly conferred. There is nowhere to
  put one, deliberately.
- Report `transition-eligibility: pass` because the record already made the transition. Eligibility is
  always relative to a *requested* transition, and none was requested.
- Treat the three passes as retrospective endorsement of the ratification. They describe the record,
  not the act.
- Infer from `status: ratified` that the act occurred. The record *represents* an act it does not
  contain; the evidence for it is elsewhere, and a validator that accepted the record's own word would
  let any file confer standing on itself.
