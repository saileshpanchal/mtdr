# FIX-511 — an attestation of the account, bound to the exact candidate

**Contract expectation:** accepted
**Binding expectation:** binds — FIX-501

A named individual attests the organisation's account of the 2019 decision, and a recovered record
is made. The event binds to FIX-501 by digest, so it attests that candidate and no other version of it.

`governs: false`. The attester accepts the account of the past; whether the decision still governs the
association is not established here, and takes a separate, prospective record.

## Document

```json
{
  "contract_version": "1.0.0",
  "event_id": "CRE-9511",
  "candidate_id": "HDC-9501",
  "candidate_digest": "sha256:27c2ae28bffe4b4818718a1acb409377d7d2d520ab1ac12e68cb76fa6acad020",
  "act": "attest-account",
  "reviewer": "J. Adeyemi",
  "authority": "Company Secretary, under the board's terms of reference for the decision register",
  "date": "2026-11-21",
  "scope": "The account of the 14 March 2019 decision as evidenced by the minute and paper B/19/07",
  "evidence_ref": "morrow-street/register/evidence/HDC-9501-attestation-2026-11-21.md",
  "governs": false,
  "result_refs": [
    "TDR-9501"
  ]
}
```

## Must not

- Read the attestation as renewing the 2019 decision.
- Record the attester as the decision's accountable owner. The owner is R. Okafor, as evidenced.
- Treat the event as proof that the attestation happened: it identifies an act, it does not evidence one.
