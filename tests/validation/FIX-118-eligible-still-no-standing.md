# FIX-118 — eligible for ratification, and still without standing

**Contract expectation:** accepted

The more consequential half of the pair, and the one easy to forget.

The same candidate, now carrying its counter-signatory. Every machine-verifiable prerequisite is
satisfied: structurally valid, semantically coherent, relationally clean, and
`transition-eligibility: pass`.

**It still has no standing.** Eligibility means the request may be *placed before* whoever is
authorised to decide it. The record remains a candidate, and remains one until a named individual
accepts accountability for it.

That is what makes this fixture the real test of
[TDR-0027](../../decisions/TDR-0027-human-ratification-confers-standing.md): the first fixture shows
the machine correctly withholding when something is missing, which is easy. This one shows it
correctly refusing to grant when it has **no mechanical objection left** — which is the only condition
under which the boundary is ever actually tested.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "VR-9302",
    "ref": "records/value/fixtures/incomplete/VR-9302-candidate-eligible.md"
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
      "result": "pass",
      "evidence": [
        { "ref": "records/value/specification/vr.md", "locus": "§4.4 ratified prerequisites" }
      ]
    }
  ]
}
```

## Must not

- **Represent the record as `ratified`, or write standing into it, on the strength of this result.**
  Four passes are four passes; none of them is an act.
- Emit a field, flag or label meaning "ready to ratify" as though it were a lifecycle state. The
  eligibility result *is* that statement, and it is deliberately not part of the record.
- Perform the transition as a side effect of assessing it. The assessed object is byte-identical
  before and after.
- Treat the absence of any remaining mechanical objection as consent. It is the absence of an
  objection, which is not the same thing and never becomes it.
- Read `pass` as approval of the commitment. Whether the saving is real, wise or achievable is
  nowhere in this result.
