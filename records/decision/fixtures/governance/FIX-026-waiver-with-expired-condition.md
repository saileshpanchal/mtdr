# FIX-026 — a waiver whose condition expired, and was never renewed or withdrawn

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** exception and waiver. **Proves:** a waiver is traced to its condition, its expiry and
its authoriser — and an expired condition is never renewed by inference, however obviously the
organisation carried on relying on it.

## Sources

**A — Exception record, `exception-reg-2025-088.md`, granted 2025-07-14**

> Exception to Architecture Standard 7 (all customer-facing decisioning must expose a
> decision-rationale record) granted to the Collections decisioning platform. Condition: exception
> expires on migration to the Ashcombe platform, or 2026-03-31, whichever is sooner. Authorised by:
> M. Rahimi, Head of Architecture.

**B — TDA minutes, `tda-2026-02-11-minutes.md`, item 2, 2026-02-11**

> Two non-conformances against Standard 7 were noted and returned to the delivery teams for rework.

**C — Estate conformance dashboard extract, `conformance-2026-08.csv`, 2026-08-05**

> Collections decisioning platform — Standard 7 — status: EXCEPTION (2025-088).

**D — Ashcombe delivery status, `ashcombe-status-2026-08.md`, 2026-08-01**

> Migration to the Ashcombe platform is 60% complete. Full cutover now expected Q4 2026.

## Expected

- The waiver reconstructed with all four elements — scope, condition, expiry and authoriser — each
  `RECORDED` from A.
- A `governance-finding` of `UNPROVEN_ASSERTION` or `TRACEABILITY_GAP`: as at C's date the dashboard
  relies on exception 2025-088, whose stated expiry (2026-03-31) has passed and whose alternative
  trigger (migration) has not occurred.
- The claim *"the exception is currently valid"* assessed as `UNKNOWN` — with `question_asked` and
  `scope_searched` — because no source evidences a renewal, an extension or a withdrawal.
- `required_authority` naming Head of Architecture, as the role that authorised the original, for any
  renewal — while recording that whether that role may renew after expiry is itself unestablished.
- D recorded as the reason the condition did not trigger, not as evidence the exception continues.

## Must not

- **Infer renewal from continued reliance.** The dashboard showing EXCEPTION in August is evidence
  that the platform is still relying on it, not that anyone extended it. This is the failure under
  test.
- Treat D's revised timeline as extending the waiver. A delivery date moving does not move a governance
  condition; that is precisely what an expiry date is for.
- Report the exception as *invalid*. Nothing here establishes withdrawal either — the honest state is
  `UNKNOWN`, and both "still valid" and "lapsed" are inventions.
- Read B's two Standard 7 non-conformances as related to this exception. Different subjects, and
  nothing links them.
- Recommend retrospective renewal, or any remedy. The finding is the output; the remedy is an
  authorised decision.
