# CORPUS-004 — a candidate that cannot yet be completed

> **Fictional corpus case.** Ashworth Building Society is invented.

**Category:** incomplete record. The material genuinely evidences a value commitment, and genuinely
cannot complete it. The correct output is an admissible, visibly incomplete candidate — not a
completed record, and not a refusal.

## Sources

**A — Town-hall slide, `member-value-townhall.pptx`, slide 9, dated 2026-05-20**

> We are committing to return £2m a year to members through better savings rates by the end of 2027.

**B — Programme brief, `member-value-brief.md`, dated 2026-05-27**

> The member-value commitment announced at the town hall is sponsored by the CFO's office.
> Measurement approach to be agreed with Finance.

## Expected

- Contributions to **one** `ovc`: A → `commitment`, `beneficiary` (members), `intended-outcome`
  (£2m/year via savings rates), `due-point` (end 2027); B → `authority` (partial — "the CFO's
  office", a function, flagged as such).
- **One CandidateAssembly**, admissible — beneficiary is evidenced, which is the one blocking role —
  with `missing_semantics` listing at least: `baseline`, `committed-by` (a named individual; "the
  CFO's office" is a function), `finance-countersignatory`, `falsifying-signal`, `value-kind`
  clarification (rate give-up is a cost to the Society and value to members — the material supports
  the beneficiary reading), and `linked-decision`.
- The candidate is proposed with the gaps stated as what ratification must supply.

## Must not

- Refuse the candidate for incompleteness — beneficiary is present; everything else is reportable.
- Promote "the CFO's office" to `committed_by` — a function is not a named individual.
- Infer a baseline from the £2m figure. The target is not the starting position.
- Mark anything beyond `status: candidate` / `realisation: not-started`.
- Report the missing counterfactual as a gap — it is optional by design and never inferred.
