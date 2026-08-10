# FIX-001 — a value commitment assembled across six sources

> **Fictional worked fixture.** Ashworth Building Society, its people, programmes and numbers are
> invented. Identifiers follow Ashworth's own numbering.

**Proves:** an Operational Value Commitment reconstructs from material that never contains it whole;
gaps are reported rather than filled; a later revision is recognised as supersession rather than
conflict; and ratification remains outside the skill.

## Sources

**A — Business case extract, `assisted-digital-case.docx`, dated 2026-02-11**

> The programme will reduce cost-to-serve in the contact centre by an estimated £1.4m annually once
> the assisted-digital journey is live across all channels.

**B — Board minute, `board-minutes-2026-03-04.md`**

> The Board noted that the benefit is intended for customers in the assisted-digital cohort — those
> who cannot complete the journey unaided — and not for the digitally confident majority.

**C — Finance baseline paper, `cts-baseline-fy25.xlsx`, dated 2026-01-30**

> Contact centre cost-to-serve, measured over FY25 from the ledger extract, was £6.2m. Source:
> Finance MI pack, January 2026.

**D — Operations note, `recognition-note.md`, dated 2026-03-18**

> Savings will be recognised as a reduction in the contact centre cost line, reviewed at the FY27
> year end.

**E — Email, `re-assisted-digital.eml`, dated 2026-03-20**

> This follows the channel decision recorded as TDR-0031. Priya Raghunathan is stewarding delivery.

**F — Steering pack, `steering-2026-06-02.pdf`**

> Revised target for the assisted-digital benefit, superseding the February figure. The Board's
> February approval stands; the estimate is now £0.9m annually following the scope reduction.

## Expected

- **6 SourceFragments**, one per source, each with a resolvable locator and a source hash.
- **8–12 RecordContributions**, all with `target_object: ovc` and `target_record_type: VR`. A
  conforming distribution: A → `commitment`, `value-kind`, `intended-outcome`; B → `beneficiary`;
  C → `baseline`; D → `recognition-route`, `due-point`; E → `linked-decision`, `stewardship`;
  F → `intended-outcome`, `authority`.
- **Exactly 1 CandidateAssembly**, `status: candidate`.
- **`grouping_basis` cites `entity-match` or `explicit-cross-reference`** with actual evidence — the
  shared assisted-digital benefit, and E's reference to TDR-0031. Not "same programme".
- **`missing_semantics` contains exactly `falsifying-signal`, `committed-by` and
  `finance-countersignatory`.** All three are mandatory and no source supplies any of them.
- **One entry in `supersessions`**: A's `intended-outcome` superseded by F's, basis naming F's
  explicit "superseding the February figure" *and* the shared authority lineage ("the Board's
  February approval stands").
- **`conflicts` is empty.**
- **`epistemic_confidence` on A's `intended-outcome` is not `high`** — "an estimated £1.4m" is an
  estimate with no stated derivation. `extraction_confidence` on the same contribution may be `high`;
  the two diverging here is the point.
- The drafted Value Record carries `status: candidate`, `realisation: not-started`, all three gaps
  marked in place, and a statement that ratification is required.

## Must not

- **Fill `finance_countersignatory`.** Priya Raghunathan appears in E as stewarding delivery. She is
  not in finance and is not offered as a counter-signatory. Recording her is a failure.
- **Treat F as a conflict.** Two figures for one role, with explicit supersession language and a
  shared authority lineage, is supersession.
- **Drop A's £1.4m.** Superseding preserves both values with their ordering; it does not delete the
  earlier one.
- **Record Priya Raghunathan as `committed_by`.** She stewards delivery. Stewardship is not
  committing the organisation, and the two are separate roles precisely so this substitution is
  visible rather than convenient.
- **Emit `status` beyond `candidate`**, or `realisation` beyond `not-started`. No baseline problem
  here — but no counter-signatory and no committer means not ratified.
- **Record £0.9m as a realised or observed value.** It is a revised expectation at commitment time,
  not an `observed-outcome`.
- **Assert the £5.3m implied residual**, or any figure not stated in a source.
- **Group on "same programme".** The evidence for grouping is available and specific; using the weak
  basis when a strong one exists is a failure even though the result is correct.

## What this fixture detects

A skill that produces a complete-looking Value Record here has invented a counter-signatory and a
falsifying signal. Both absences are the finding — between them they name exactly why this benefit
would never have been reconciled, and both are invisible until someone assembles the commitment whole.
