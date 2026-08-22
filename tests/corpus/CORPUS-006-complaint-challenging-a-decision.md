# CORPUS-006 — a complaint challenging a governed decision

> **Fictional corpus case.** Kingsmere Bank plc and every individual named here are invented.

**Category:** cross-language, and the standing boundary. Material yields a **decision-side**
reconstruction and a **value-side** commitment candidate at once, plus evidence that a
standing / protected-interest concept is **required** — while standing itself remains unresolved and
non-canonical.

This case exists to prove the gap, not to close it. MTDR can reconstruct the complaint, the affected
commitment, the evidence, the challenge path and the standing that *would be required*. It cannot
manufacture the standing, and it cannot determine whether the complaint succeeds.

## Sources

**A — Board minute, `board-2025-09-24-minutes.md`, 2025-09-24**

> The Board confirmed the Bank's commitment that customers in financial difficulty will not be worse
> served by automated collections journeys than by the previous manual process, measured by the
> arrears resolution rate for customers with a recorded vulnerability, against the 2025 baseline of
> 68%. J. Almeida, Chief Customer Officer, accepted accountability for the commitment.

**B — Complaint file, `complaint-2026-05-2211.md`, received 2026-05-19**

> The customer states that between February and April 2026 they received automated contact about
> arrears while under active hardship arrangements, that their attempts to explain their circumstances
> did not change the contact pattern, and that no person reviewed their case. The customer asks the
> Bank to explain who decided that their case would be handled without human review, and on what basis.

**C — Complaint outcome letter, `complaint-2026-05-2211-outcome.md`, 2026-07-02**

> We have upheld your complaint in part. Contact frequency remained within our published limits. We
> accept that your hardship arrangement should have suppressed automated contact and did not, due to a
> configuration issue corrected on 14 June 2026. We have paid £150 in recognition of the distress
> caused.

**D — Customer outcome MI extract, `arrears-outcomes-2026-q1.csv`**

> Arrears resolution rate, customers with recorded vulnerability flag: Q1 2026 — 61%. Population:
> 74%. *Note: vulnerability flag populated for 61% of the arrears population.*

**E — Ashcombe TDA minutes, `tda-2026-02-11-minutes.md`, 2026-02-11** — as in
[FIX-018](../../records/decision/fixtures/governance/FIX-018-tda-real-jobs-not-stated-purpose.md).

## Expected

- **Value side.** A candidate commitment from A — beneficiary *customers in financial difficulty with
  a recorded vulnerability*, a baseline of 68%, a named accountable individual, a Board authority. D
  is **observation** evidence against it, showing 61% against a 68% baseline. Attribution to the
  Ashcombe change is **not** established by D and must be reported as unresolved.
- **Decision side.** The Ashcombe decision reconstructed from E, and B's question — *who decided this
  case would be handled without human review* — routed to it as the decision under challenge.
- **The challenge path reconstructed**: complaint received, investigated, partly upheld, remedy paid,
  configuration corrected. Each step `RECORDED` or `OBSERVED` from B and C.
- **The standing requirement made explicit and left unresolved.** B asks a question on behalf of an
  affected party about a decision the party did not participate in. Reconstructing this needs a concept
  of *who is entitled to require an answer, and on whose behalf* — and no MTDR record family
  represents it. Emit a `governance-finding` naming the required-but-absent concept, cross-referenced
  to TDR-0034's Protected Claim and Standing irreducibility finding.
- **A `CHALLENGE_GAP` finding**: C answers the contact-frequency and configuration questions and does
  not answer B's actual question about who decided and on what basis.
- D's footnote — the flag is populated for 61% of the population — recorded as a limit on what the MI
  can evidence at all, linking to the same coverage challenge raised at the Risk Acceptance Forum in
  [FIX-025](../../records/decision/fixtures/governance/FIX-025-risk-forum-independent-challenge.md).

## Must not

- **Determine whether the complaint should have succeeded**, whether £150 was adequate, or whether the
  partial upholding was correct. MTDR detects, constructs, classifies and routes; it does not
  adjudicate (GR-11). This is the failure under test.
- **Manufacture standing.** Do not represent the customer as holding a Protected Claim, do not create a
  record type for it, and do not approximate it with `beneficiary` on the value candidate. The
  beneficiary of a commitment and the holder of standing to challenge a decision are different
  concepts, and collapsing them is how the gap disappears without being closed.
- Merge the value candidate and the decision candidate into one object. One commitment, one decision,
  two objects, two records — a single candidate means the run is classifying documents rather than
  reconstructing state.
- Treat D's 61% as evidence that the commitment was breached. It is observation without attribution;
  the baseline population and the measured population differ, and the flag covers 61% of the arrears
  population.
- Use C's June configuration finding to explain the February decision. It postdates it (GR-07).
- Record the complaint outcome as superseding the Board commitment. A remedy to one customer is not a
  change to an organisational commitment.
