# FIX-516 — must-not probe: a rejection that produces something

**Contract expectation:** rejected

A rejection that names a record as its result. Rejecting a candidate produces nothing, and an event
that says otherwise is a record created under the wrong act.

## Document

```json
{
  "contract_version": "1.0.0",
  "event_id": "CRE-9516",
  "candidate_id": "HDC-9501",
  "candidate_digest": "sha256:66f996e3ee06f5d5a13f984837dd65c0bbf1b94887d719b85ea2c4cba26f5b30",
  "act": "reject",
  "reviewer": "J. Adeyemi",
  "authority": "Company Secretary, under the board's terms of reference for the decision register",
  "date": "2026-11-21",
  "scope": "The account of the 14 March 2019 decision as evidenced by the minute and paper B/19/07",
  "evidence_ref": "morrow-street/register/evidence/HDC-9501-attestation-2026-11-21.md",
  "governs": false,
  "result_refs": [
    "TDR-9516"
  ]
}
```

## Must not

- Accept `result_refs` on a rejection or a retention.
