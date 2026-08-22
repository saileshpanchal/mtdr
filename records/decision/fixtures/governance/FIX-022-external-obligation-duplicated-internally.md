# FIX-022 — an external obligation duplicated by an internal control

> **Fictional corpus case.** Kingsmere Bank plc, the Prudential Model Governance Expectation and every
> reference here are invented; no real regime is described.

**Category:** regime preservation. **Proves:** evidence reuse and narrowing may be recommended where
justified, and removal of a mandated mechanism may not (GR-05). Also proves that an inherited external
obligation is preserved as projected evidence-bearing state and **not** forced into a decision record.

## Sources

**A — Supervisory correspondence extract, `pmge-2024-notification.md`, 2024-05-20**

> Firms are expected to maintain independent validation of material models prior to deployment and at
> least annually thereafter, with validation performed by persons independent of model development.
> Firms should be able to evidence the independence of the validating function.

**B — Model Risk Policy, `model-risk-policy-v9.md`, section 6, effective 2024-08-01**

> All Tier 1 and Tier 2 models require independent validation before deployment and annually
> thereafter. Validation is performed by Model Validation, reporting to the Chief Risk Officer.

**C — AI Assurance Standard, `ai-assurance-standard-v2.md`, section 3, effective 2025-06-01**

> All AI and machine-learning systems require pre-deployment assurance review covering performance,
> robustness, explainability and fairness. Assurance review is performed by the AI Assurance team,
> reporting to the Chief Data Officer.

**D — Ashcombe evidence log, `ashcombe-assurance-evidence.md`, 2026-01**

> Model performance pack, feature stability analysis and holdout results supplied to Model Validation
> (2026-01-12) and, separately, to AI Assurance (2026-01-19). Cohort performance breakdown supplied to
> both. Fairness testing supplied to AI Assurance only.

## Expected

- A `governance-finding` of `DUPLICATE_EVIDENCE`, scoped to the **overlapping evidence** in D — the
  performance pack, feature stability, holdout results and cohort breakdown assembled twice.
- Overlap classified as **same evidence**, and explicitly **not** same purpose — B establishes
  independent validation, C establishes assurance across four distinct properties including fairness,
  which B does not cover.
- A on the record as an **inherited external obligation held as projected evidence-bearing state**,
  naming source, scope and the date it applied from.
- `governance-disposition` on B — `mandatory_status: externally-mandated`, `status_basis` citing A,
  `recommended_disposition: RETAIN`.
- `governance-disposition` on C — `mandatory_status: internally-required`, and at most `NARROW` or
  `REUSE`, scoped to the evidence assembly rather than the review.
- The safe recommendation stated plainly — assemble the shared evidence once and supply it to both
  functions, changing no mandate and no reporting line.

## Must not

- **Recommend retiring or merging either function.** They report to different executives and establish
  different properties; the overlap is in what they are *sent*, not in what they *do*.
- Represent A as a decision Kingsmere took. The Bank did not decide to be subject to it, and recording
  an inherited obligation as an internal judgement destroys the distinction that makes it binding.
  There is no normative record family for inherited obligation, and that absence is a recorded
  irreducibility finding — not a reason to use the nearest available shape.
- Recommend that Model Validation consume AI Assurance's fairness testing as satisfying its own
  independence requirement, or the reverse. Neither is established by the material.
- Read "reporting to the Chief Risk Officer" and "reporting to the Chief Data Officer" as establishing
  independence of either from Ashcombe. That is FIX-030's question and is not answered here.
- Score the duplication as a percentage. A figure invites exactly the reasoning the same-purpose /
  same-evidence distinction exists to prevent.
