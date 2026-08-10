# FIX-013 — the financial measure displacing the proposition

> **Fictional worked fixture.** Ashworth Building Society is invented.

**Proves:** where a business case leads with a financial figure, the figure is evidence *about* the
commitment, not the commitment. Recovery must find the actual proposition underneath the number —
and must not let £ displace it.

## Source

**A — Business case, `branch-advice-case.md`, dated 2026-04-08**

> The case delivers £3.2m NPV over five years. Investment in the advice hubs means members in
> branch-served communities keep access to face-to-face financial guidance as the network changes;
> retention modelling attributes the majority of the NPV to members who stay because guidance
> remains available. Baseline: 84% of members in affected communities report access to guidance
> (2025 member survey). Sponsored by Distribution Director Owen Pryce under the network decision
> TDR-0088.

## Expected

- **One CandidateAssembly** whose `commitment` is the *access outcome* — members in branch-served
  communities keep access to face-to-face guidance — with `beneficiary` (those members), `baseline`
  (84%, 2025 survey), `committed-by`, `authority`/`linked-decision` (TDR-0088).
- **The £3.2m NPV enters as a `measure`/`assumption` contribution** — retention modelling as the
  case's financial expression of the outcome — not as the commitment, and its
  `epistemic_confidence` reflects that it is modelled, not measured.
- `value-kind` reasoned with the reading stated: the proposition is protective/qualitative in
  substance even though the case is framed in NPV.
- Completeness: `falsifying-signal` and `finance-countersignatory` missing.

## Must not

- Draft "deliver £3.2m NPV" as the commitment. That is the displacement under test.
- Grade the NPV `epistemic_confidence: high` because the number is precise. Modelled precision is
  not evidence strength.
- Lose the 84% baseline because the case's headline baseline is financial.
- Downgrade the whole candidate to `quantified` mechanically — the class follows the proposition,
  not the headline figure.
