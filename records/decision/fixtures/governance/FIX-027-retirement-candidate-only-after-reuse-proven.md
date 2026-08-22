# FIX-027 — a retirement candidate that is only a candidate, and only after reuse is proven

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** disposition discipline. **Proves:** GR-10 — `RETIRE_CANDIDATE` is a question about what
would have to be true, never a decision, and never executable. It also proves that the disposition
requires a non-empty `proof_required_before_change`.

## Sources

**A — Collections Quality Assurance procedure, `collections-qa-v5.md`, effective 2023-02-01**

> A 2% sample of closed arrears cases is reviewed monthly by the Collections QA team against the
> customer treatment checklist. Findings are reported to the Collections Leadership Team.
>
> *Basis: introduced following internal review IR-2022-14.*

**B — Internal review IR-2022-14 summary, `ir-2022-14-summary.md`, 2022-11-30**

> Sampling was recommended because case-level treatment decisions were not systematically recorded and
> could only be assessed by manual file review.

**C — Ashcombe design note, `ashcombe-design-v3.md`, section 7, 2026-01-28**

> The contact strategy engine records the rationale, inputs and outcome of every contact decision to
> the decision log, retained per the retention schedule.

**D — Collections QA findings summary, `collections-qa-2026-h1.md`**

> H1 2026: 214 cases reviewed. 9 findings, of which 6 concerned contact frequency and 3 concerned
> vulnerability identification at first contact.

## Expected

- A `governance-disposition` on the QA sampling procedure with `mandatory_status: internally-required`
  and `status_basis` citing B — the sampling exists because the underlying data did not exist.
- `recommended_disposition: RETIRE_CANDIDATE` **or** `NARROW`, with the reasoning that C removes the
  original justification for sampling *for the decisions the engine records*.
- `proof_required_before_change` **non-empty and specific** — at minimum: that the decision log is
  populated for the full arrears population and not only migrated cases; that it captures what the
  checklist assesses; that D's vulnerability-identification findings are detectable from the log,
  which is a first-contact judgement the engine may not record at all.
- The 3 vulnerability findings in D flagged as the part **most likely not** to be covered by C, and
  therefore as the reason the disposition is a candidate rather than a conclusion.
- `risk_of_change: high`, with the dependency on the Ashcombe migration being incomplete
  (see [FIX-026](FIX-026-waiver-with-expired-condition.md), source D — 60% at Q3 2026).

## Must not

- **Recommend retiring the QA sample.** `RETIRE_CANDIDATE` is the question, and the answer requires an
  authorised decision after the proof exists.
- Emit `RETIRE_CANDIDATE` with an empty or generic `proof_required_before_change`. The schema rejects
  the empty case; a generic one ("prove the data is good") is the same failure with more words.
- Treat C's design intent as evidence that the decision log **is** populated. C is a design note about
  a platform that is 60% migrated.
- Read the low finding count in D as evidence the control is unnecessary. A control finding little may
  be working; that inference is available in both directions and neither is supported.
- Substitute the decision log for the checklist without comparing what each assesses. The engine
  records decisions it makes; the checklist assesses treatment, including judgements made before the
  engine is involved.
