# FIX-514 — must-not probe: attestation read as renewal

**Contract expectation:** rejected

An attestation that claims the decision governs now. Recognising that the organisation decided
something in 2019 is not deciding that it applies today. That takes its own prospective record.

## Document

```json
{
  "contract_version": "1.0.0",
  "event_id": "CRE-9514",
  "candidate_id": "HDC-9501",
  "candidate_digest": "sha256:66f996e3ee06f5d5a13f984837dd65c0bbf1b94887d719b85ea2c4cba26f5b30",
  "act": "attest-account",
  "reviewer": "J. Adeyemi",
  "authority": "Company Secretary, under the board's terms of reference for the decision register",
  "date": "2026-11-21",
  "scope": "The account of the 14 March 2019 decision as evidenced by the minute and paper B/19/07",
  "evidence_ref": "morrow-street/register/evidence/HDC-9501-attestation-2026-11-21.md",
  "governs": true,
  "result_refs": [
    "TDR-9501"
  ]
}
```

## Must not

- Accept `governs: true` on any act.
- Accept it on the grounds that the decision was never superseded.
