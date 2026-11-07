# FIX-512 — must-not probe: an event that no longer binds

**Contract expectation:** accepted
**Binding expectation:** does-not-bind — FIX-501

A well-formed event whose digest is that of a different version of HDC-9501 — one in which the
memo's `considered` read `unknown`. The candidate it names has changed since, or the event was made
against something else. Either way it does not attest the candidate as it stands.

Schema-valid, and the binding check refuses it.

## Document

```json
{
  "contract_version": "1.0.0",
  "event_id": "CRE-9512",
  "candidate_id": "HDC-9501",
  "candidate_digest": "sha256:27b71c57d1e899536e8afc963e43f5603a95bcb520c8d0be6c0d36dc56b1baa6",
  "act": "retain",
  "reviewer": "J. Adeyemi",
  "authority": "Company Secretary, under the board's terms of reference for the decision register",
  "date": "2026-11-21",
  "scope": "The account of the 14 March 2019 decision as evidenced by the minute and paper B/19/07",
  "evidence_ref": "morrow-street/register/evidence/HDC-9501-attestation-2026-11-21.md",
  "governs": false
}
```

## Must not

- Treat the event as applying to the current candidate because the identifiers match.
- Recompute and overwrite the event's digest so that it binds.
