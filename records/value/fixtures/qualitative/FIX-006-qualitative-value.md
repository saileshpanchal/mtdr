# FIX-006 — qualitative value: no currency, still a commitment

> **Fictional worked fixture.** Meridian Mutual is invented.

**Proves:** a committed outcome with a recognisable future condition and a way of knowing is an OVC
whether or not a currency amount appears. The currency filter is the failure under test.

## Sources

**A — Colleague experience paper, `advice-quality-paper.md`, dated 2026-03-19**

> We commit to advisers being able to explain any automated recommendation to a member in plain
> language, without escalating to a specialist team. Today 41% of automated recommendations require
> specialist referral to explain (Q1 referral log). Target: referral-to-explain below 10% by Q2 2027.
> Sponsored under the advice-transformation decision; owner Tomas Lindqvist. We will know it is not
> working if the referral rate plateaus above 25% for two consecutive quarters.

## Expected

- **One CandidateAssembly**, `target_object: ovc`, from a single source (grouping trivially
  evidenced): commitment (explainability without escalation) · beneficiary (members, via advisers —
  the reading stated) · baseline (41%, Q1 referral log) · intended outcome (<10% by Q2 2027) ·
  due-point · committed-by (Tomas Lindqvist) · authority (the advice-transformation decision, as
  `linked-decision` evidence) · **falsifying-signal (plateau above 25% for two quarters)**.
- `value-kind` reasoned to `capacity` (specialist referrals released) or `risk-reduction`, with the
  reading stated — not defaulted.
- `missing_semantics`: `finance-countersignatory`. Nothing else mandatory is absent.

## Must not

- Downgrade the commitment to context because no £ appears.
- Invent a financial proxy ("worth approximately…") to make it look like a benefit.
- Miss the falsifying signal — this fixture's signal genuinely can fail, and it is stated in prose,
  not labelled.
- Report the counterfactual as missing.
