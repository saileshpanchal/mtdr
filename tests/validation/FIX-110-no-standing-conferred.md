# FIX-110 — must-not probe: validation conferring standing

**Contract expectation:** rejected

A result that passes eligibility and then records the subject as ratified. TDR-0027 reserves standing
to the authorised human act; a validator observing that the prerequisites are present has observed
exactly that and nothing more.

The failure mode is not hypothetical. A tool that can write `ratified: true` will be pointed at a
backlog, and standing will have been manufactured by a script — the precise inversion TDR-0027 and
TDR-0031 exist to prevent.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "TDR-9008" },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "assessed_state": "proposed",
  "requested_transition": { "from": "proposed", "to": "accepted" },
  "standing": "accepted",
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    { "dimension": "transition-eligibility", "result": "pass" }
  ]
}
```

## Must not

- Accept the document. `standing`, `ratified`, `accepted`, `approved` and `authority` are all rejected
  by the closed object.
- Read `transition-eligibility: pass` as the transition having occurred, been authorised, or being
  authorisable without a human. It means the request may be *placed before* the decision-maker.
- Write the transition into the subject as a side effect of assessing it. The assessed object is
  byte-identical before and after.
- Record the validator's identity in a way that implies it acted. `validator` is identity only, and
  confers nothing.
