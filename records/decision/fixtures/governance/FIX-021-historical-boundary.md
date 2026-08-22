# FIX-021 — a later audit finding must not explain a decision it postdates

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** historical boundary. **Proves:** decision-time and retrospective evidence stay distinct
(GR-07). Material created after `historical_as_of` is named in `retrospective_evidence_excluded` and
never used to answer a decision-time question.

This is the drill's most consequential failure mode, and it is invisible in the output unless the
exclusions are listed — because a reconstruction that borrows a later explanation looks *better
reasoned* than the decision actually was.

## Sources

**A — TDA minutes, `tda-2026-02-11-minutes.md`, 2026-02-11** *(decision-time)*

> Item 3. Project Ashcombe. The Authority approved the design at Gate 2 subject to the retention
> question being resolved with the Data Governance Council.

**B — Internal Audit report, `ia-2026-31-collections-automation.md`, issued 2026-06-30**
*(retrospective)*

> The Authority approved the Ashcombe design on the basis of a documented assessment that the contact
> model's disparate-impact testing was adequate for the vulnerable-customer cohort, and on the
> understanding that the retention extension would be time-bounded to 18 months. Management confirmed
> to Audit that both factors were considered at the February meeting.

**C — Data Governance Council minutes, `dgc-2026-03-24-minutes.md`, 2026-03-24** *(retrospective)*

> The Council noted the retention extension requested by Ashcombe and approved 18 months.

The drill runs with `historical_as_of: 2026-02-11`.

## Expected

- `retrospective_evidence_excluded` naming **B and C explicitly**.
- The question *"what evidence was available at the time?"* answered from A alone.
- The question *"was disparate-impact testing considered?"* answered `UNKNOWN` — with
  `question_asked` and `scope_searched` — because no decision-time source evidences it. B's assertion
  that it was considered is a claim made in June about February.
- The question *"was the retention extension time-bounded?"* answered `UNKNOWN` at decision time; A
  records the question as open and routed onward, which is the opposite of settled.
- B and C reported **separately** as what is known *now*, clearly labelled retrospective — both are
  useful, and conflating them with decision-time state is the failure.
- A `governance-finding` of `EVIDENCE_GAP` — the decision-time record does not carry the basis the
  later audit response attributes to it.

## Must not

- **Answer any decision-time question from B or C.** This is the failure under test.
- Treat B's "management confirmed to Audit that both factors were considered" as decision-time
  evidence. It is June testimony about February, and its epistemic state at `historical_as_of` is
  `UNKNOWN`.
- Report the drill's summary as `DEMONSTRABLE` because the combined corpus answers every question. The
  drill asks what could be demonstrated **at the time**, and the answer here is `PARTIAL`.
- Silently drop B and C. Excluding them without naming them makes the exclusion uninspectable, which
  is the same defect as importing them.
- Treat C as evidence that the retention question was resolved *before* the decision. Its date is the
  point.
