# FIX-018 — the TDA's real jobs are not its stated purpose

> **Fictional corpus case.** Kingsmere Bank plc, Project Ashcombe and every individual named here are
> invented.

**Category:** forum reconstruction. **Proves:** a forum's terms of reference are a `RECORDED` claim
about what it is *for*, and evidence of nothing about what it *does*. The reconstruction reads the
packs and minutes, and reports the distance between them as a finding.

This is the spine of the governance corpus. Project Ashcombe — replacing Kingsmere's arrears-contact
decisioning with an automated, model-driven contact strategy — is the consequential decision the other
fixtures reconstruct from different angles.

## Sources

**A — Technology Design Authority terms of reference, `tda-tor-v4.md`, effective 2024-09-01**

> The TDA exists to assure that material change to the Bank's technology estate is architecturally
> coherent, strategically aligned and consistent with the Bank's target architecture. The Authority
> provides architectural challenge and approves design at Gate 2.

**B — TDA pack, `tda-2026-02-11-pack.pdf`, 2026-02-11, agenda and timings**

> 1. Minutes and matters arising (5 min)
> 2. Estate conformance dashboard — 14 changes assessed against Architecture Standards 3, 7, 9, 11 (35 min)
> 3. Project Ashcombe — arrears contact automation, Gate 2 design approval (20 min)
> 4. Standard pattern approvals — 9 changes, all conforming (15 min)
> 5. AOB (5 min)

**C — TDA minutes, `tda-2026-02-11-minutes.md`, 2026-02-11**

> Item 2. The Authority reviewed the conformance dashboard. Twelve changes conformed. Two
> non-conformances were noted against Standard 7 and returned to the delivery teams for rework. No
> discussion was required on the twelve.
>
> Item 3. Project Ashcombe. The Authority discussed at length the trade-off between contact
> effectiveness and the Bank's data minimisation position, the two being in tension where the model
> requires transaction-level features. R. Idowu argued the retention extension was disproportionate;
> the Chair noted that the alternative reduced model performance for the customers least able to
> engage. The Authority approved the design at Gate 2 subject to the retention question being
> resolved with the Data Governance Council.
>
> Item 4. Nine standard pattern approvals were taken as read and approved.
>
> Pre-meeting: the secretariat confirmed that assembling the conformance dashboard required 3 days of
> analyst effort across four systems, as in prior months.

## Expected

- One `forum-reconstruction` projection for the TDA, with an assessment per job.
- `stated_purpose` from A, `RECORDED` — the terms of reference are in force and say this.
- `inferred_jobs` reading, from B and C, at least:
  - `DETERMINISTIC_CONFORMANCE` — items 2 and 4, `OBSERVED`, roughly 50 minutes of an 80-minute
    meeting, with the twelve conforming changes and nine standard patterns requiring no discussion;
  - `EVIDENCE_ASSEMBLY` — the conformance dashboard, `OBSERVED`, with `manual_reconstruction_steps`
    carrying the 3 analyst-days;
  - `TRADE_OFF_JUDGEMENT` — item 3's contact effectiveness against data minimisation, `OBSERVED`,
    and genuinely cross-domain;
  - `EXCEPTION_HANDLING` — the two Standard 7 non-conformances, `OBSERVED`;
  - `ESCALATION` — the retention question routed onward to the Data Governance Council, `OBSERVED`.
- `separated_powers.execution_authority` and `challenge_authority` both `INFERRED` from the minutes,
  with the basis named.
- The **distance finding** — `FORUM_EVIDENCE_ASSEMBLY_OVERHEAD` — that a forum whose stated purpose is
  architectural challenge spends most of its time on deterministic conformance and on evidence that
  was assembled by hand beforehand.

## Must not

- **Report the stated purpose as what the forum does.** A says "provides architectural challenge";
  B and C show one item of challenge and four of conformance and assembly. Both are true; only one is
  the answer to what the forum does.
- Classify the whole forum with **one** epistemic state. The purpose is `RECORDED`, the jobs are
  `OBSERVED`, and the powers are `INFERRED` — reporting the reconstruction as any single one of these
  is the failure under test.
- Record `AUTHORITY_EXERCISE` as `RECORDED` from "the Authority approved". The minutes evidence that
  the approval happened; nothing here shows the approval was admitted as authoritative state, so it is
  `OBSERVED` and the entitlement behind it is `INFERRED` at best.
- Count agenda items as jobs. Item 1 is not a governance job, and item 3's 20 allocated minutes are
  not evidence of how long the discussion took.
- Recommend anything. This fixture reconstructs; FIX-024 is where the evolution projection is tested.
