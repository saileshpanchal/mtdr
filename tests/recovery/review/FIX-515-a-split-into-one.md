# FIX-515 — must-not probe: a split with one successor

**Contract expectation:** rejected

A split names two or more successor candidates. A split into one is a relabelling, and would
let a candidate be replaced without the replacement being reviewed as such.

## Document

```json
{
  "contract_version": "1.0.0",
  "event_id": "CRE-9515",
  "candidate_id": "HDC-9501",
  "candidate_digest": "sha256:66f996e3ee06f5d5a13f984837dd65c0bbf1b94887d719b85ea2c4cba26f5b30",
  "act": "split",
  "reviewer": "J. Adeyemi",
  "authority": "Company Secretary, under the board's terms of reference for the decision register",
  "date": "2026-11-21",
  "scope": "The account of the 14 March 2019 decision as evidenced by the minute and paper B/19/07",
  "evidence_ref": "morrow-street/register/evidence/HDC-9501-attestation-2026-11-21.md",
  "governs": false,
  "result_refs": [
    "HDC-9515-a"
  ]
}
```

## Must not

- Accept a split with fewer than two results.
