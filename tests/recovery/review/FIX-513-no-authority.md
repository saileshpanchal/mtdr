# FIX-513 — must-not probe: an act with no stated authority

**Contract expectation:** rejected

A rejection with no basis stated for the reviewer acting. A review event identifies an act by a
named individual on a stated basis; without the basis the act is not identifiable.

## Document

```json
{
  "contract_version": "1.0.0",
  "event_id": "CRE-9513",
  "candidate_id": "HDC-9501",
  "candidate_digest": "sha256:66f996e3ee06f5d5a13f984837dd65c0bbf1b94887d719b85ea2c4cba26f5b30",
  "act": "reject",
  "reviewer": "J. Adeyemi",
  "date": "2026-11-21",
  "scope": "The account of the 14 March 2019 decision as evidenced by the minute and paper B/19/07",
  "evidence_ref": "morrow-street/register/evidence/HDC-9501-attestation-2026-11-21.md",
  "governs": false
}
```

## Must not

- Accept the event because the reviewer is named.
- Infer the authority from the reviewer's job title.
