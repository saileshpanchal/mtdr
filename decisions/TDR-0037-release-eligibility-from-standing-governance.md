---
id: TDR-0037
conforms_to: mtdr/decision/tdr@1.15.0
title: Derive release eligibility from standing governance, and fix what eligibility may never decide
status: accepted
template: full
decision_date: 2026-08-18
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0025, TDR-0027, TDR-0032, TDR-0033
confirmed_by_outcome: pending — review after the first release actually gated by this computation, or 2027-08-18, whichever is sooner
---

# TDR-0037 — Derive release eligibility from standing governance, and fix what eligibility may never decide

## Context — what was known at the time

Two accepted assurance cases carry fifteen constraints between them, several of them explicitly
blocking release. Those constraints are now registered with their state
([`decisions/evidence/DAC-0032-0033-obligations.yaml`](evidence/DAC-0032-0033-obligations.yaml)), and
the suite already proves the register cannot drift from the cases it records.

What did not exist was any connection between that register and the moment it was written for. The
release gate would have been a person reading fifteen rows and forming a view — which is a checklist
maintained by hand, differing from the governance it describes in exactly the way that matters: it can
be quietly shortened, and nobody notices which promise was dropped.

Meanwhile [TDR-0033](TDR-0033-four-dimensional-validity.md)'s fourth dimension had never been
exercised. Every result this repository produced reported `transition-eligibility: not-applicable`,
because nothing had ever requested a transition. A dimension that is always inapplicable is a
dimension nobody has tested.

The two gaps had one answer, and it was worth taking rather than patching either separately.

## Decision

**1. `released` is a governed transition of this repository, and its eligibility is computed.**
`tests/verify.py` requests the transition `pre-release → released` on every run and reports
eligibility derived from the obligations register: `implementation: pending` contributes **fail**,
`verification: pending` or `release-gated` contributes **indeterminate**, and `fail` outranks
`indeterminate` because a demonstrated gap is a stronger finding than an unknown one. Every
contributing obligation is named.

*Released* here means the gate DAC-0032 and DAC-0033 defined — the point at which the typed-conformance
and four-dimensional-validity architecture may be presented as ready for adoption. It is not cutting a
version; this repository has published versions throughout.

**2. The gates are derived from standing governance, never curated.** They come from accepted
decisions by way of accepted assurance cases. A constraint cannot be dropped from the gate without
being dropped from the case, and a case cannot gain a constraint that the gate does not see — the
suite already refuses both.

**3. The mechanism is named** ([`specification/obligation-chain.md`](../specification/obligation-chain.md)):

> **Decision → Constraint → Obligation → Evidence → Current state → Eligibility for next transition**

Claimed at its actual scope. This is the mechanism MTDR *currently uses* to decide whether a governed
transition is permissible from available evidence. It is **not** a universal organisational ontology,
and this record does not claim it is one. It is named because it recurs, and whether it generalises
further is an open question to be answered by running it.

**4. The strict definition, which is the load-bearing part of this record:**

> **Eligibility answers whether recorded evidence satisfies already-authorised transition conditions.
> It does not decide what those conditions ought to be.**

The division of labour follows, and nothing may drift across it:

> decision establishes condition → obligation represents condition → evidence addresses obligation →
> validator computes satisfaction → eligibility reports result → **authorised participant decides and
> acts**

Every step before the last is mechanical. The last is not, and never becomes so.

**5. Eligibility is not authority.** A `pass` means the evidenced preconditions are satisfied and the
request may be **placed before** whoever is authorised to decide it. It does not perform the
transition, authorise it, or confer standing — [TDR-0027](TDR-0027-human-ratification-confers-standing.md)
reserves that to the human act. Symmetrically, `fail` reports a published prerequisite demonstrably
unmet; it does not forbid anything. Whoever holds the authority may still act, and would be acting in
the knowledge of what is unmet, which is the entire value of computing it.

**6. The same shape governs a Value Record and this repository**, and that symmetry is an invariant to
preserve rather than a coincidence to note: candidate → obligations and evidence → eligible for
ratification → human act → standing, and pre-release → obligations and evidence → eligible for release
→ authorised act → released. A future record family that invents its own readiness mechanism has
diverged from this one for no reason.

## Evidence

- **Business** — a standard asking organisations to derive readiness from governed evidence should
  not decide its own readiness by someone reading a list. The dogfooding is the argument.
- **Architecture** — this uses the existing result contract unchanged rather than adding a mechanism.
  The fourth dimension was specified for exactly this and had never been exercised; a specified
  capability nothing uses is untested.
- **Regulatory** — not material to the decision, though the separation it fixes is the one every
  regulated approval process depends on: evidence gathered mechanically, decision taken by a named
  human.
- **Operations** — the register's state now has a consequence. An obligation moved to `pending` changes
  what the suite reports on the next run, so regressions surface where they happen.
- **Customer** — not material at repository level.
- **Data** — the current computation returns **fail**, naming DAC-0032 constraint 2: detached records
  cannot yet identify their applicable specification version. That is the correct answer, and a
  mechanism whose first honest output is "not eligible" is more trustworthy than one that opened green.
- **External** — no dependency taken. Policy engines remain `interoperate` under
  [TDR-0035](TDR-0035-standards-boundary.md), and this deliberately is not one: it evaluates published
  prerequisites, and does not evaluate policy.

## Alternatives rejected

1. **Maintain a release checklist by hand.** Rejected: it describes governance rather than being it,
   and the failure mode — a constraint silently dropped — is invisible by construction.
2. **Let eligibility weigh whether a constraint still matters.** Rejected, and foreclosed below. That
   is a decision, and decisions are made by authorised people and recorded as records. It is also the
   most attractive extension, which is why it is named.
3. **Report an overall "release readiness" percentage.** Rejected on the DAC-0033 argument: a figure
   readable alone will be read alone, and the identity of the unmet constraint is the whole content.
4. **Treat `release-gated` obligations as fails.** Rejected: they are defined, owned proofs that cannot
   run in this repository state. Reporting them as demonstrated gaps would conflate "not proved" with
   "proved absent", which is the `indeterminate` distinction TDR-0033 exists to protect.
5. **Treat `release-gated` obligations as satisfied.** Rejected for the obvious reason, and it is worth
   recording that this was the tempting one: it is the only option that would have made the gate open.
6. **Wait until the first real release.** Rejected: a gate first exercised at the moment it matters is
   a gate nobody has tested.

## Options foreclosed

- Eligibility can never decide what a transition's conditions ought to be, nor whether one still
  applies.
- Release gates can never be curated by hand rather than derived from accepted cases.
- No eligibility result may perform a transition, authorise one, or confer standing.
- No aggregate readiness score or percentage may be reported.
- A record family with governed transitions cannot invent a parallel readiness mechanism without
  superseding this record.

## Consequences and review

Success is the release gate closing on evidence rather than opinion — and, more tellingly, an
obligation regressing to `pending` and the very next suite run reporting the repository ineligible
without anyone remembering to check.

The nearer consequence is already visible: this repository reports itself **not eligible** for the
release its own accepted assurance cases defined, and names the constraint. That is the mechanism
working, not failing.

Review after the first release actually gated by this computation, or at the confirmed-by-outcome
trigger — and immediately if anyone proposes that eligibility should weigh a constraint's continuing
relevance, because that proposal is the failure mode this record exists to name.
