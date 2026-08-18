# The obligation chain

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

How this standard decides whether a governed transition is permissible from the evidence available.
Decided in [TDR-0037](../decisions/TDR-0037-release-eligibility-from-standing-governance.md).

> **Decision → Constraint → Obligation → Evidence → Current state → Eligibility for next transition**

## 1. What is being claimed, and what is not

This is **the mechanism MTDR currently uses** to determine whether a governed transition is
permissible from available evidence. It is not a universal organisational ontology, and this document
does not claim it is one. It is named here because it recurs — the same shape governs a Value Record
reaching ratification and this repository reaching a release gate — and a mechanism that recurs is
worth stating once rather than reimplementing per record family.

Whether it generalises further is an open question, and the honest way to answer it is to run it.

## 2. The chain

| Step | What it is | Where it lives |
|---|---|---|
| **Decision** | An accepted judgement that establishes a condition | a TDR |
| **Constraint** | The condition, named with an owner and a measure | a DAC disposition |
| **Obligation** | The constraint represented so its state can be read | an obligations register |
| **Evidence** | An artefact that addresses the obligation | fixtures, probes, records |
| **Current state** | What the evidence establishes about the obligation now | `implementation` · `verification` |
| **Eligibility** | Whether the transition's published prerequisites are satisfied | a validation result's fourth dimension |

Each step is a different kind of thing, and the separations are the point. A constraint is not its
evidence; an obligation's state is not a judgement about the decision; and eligibility is not the
transition.

## 3. The strict definition

> **Eligibility answers whether recorded evidence satisfies already-authorised transition conditions.
> It does not decide what those conditions ought to be.**

This is the boundary that erodes quietly rather than breaking loudly. As eligibility acquires logic
there is a standing temptation to keep adding until it begins making organisational judgements —
weighing whether a constraint still matters, deciding a gate is not really necessary this time,
concluding that on balance the transition should proceed. Every one of those is a decision, and
decisions are made by authorised people and recorded as records.

The division of labour, stated so nothing drifts across it:

> decision establishes condition → obligation represents condition → evidence addresses obligation →
> validator computes satisfaction → eligibility reports result → **authorised participant decides and
> acts**

Every step before the last is mechanical. The last is not, and never becomes so. That is what keeps
MTDR from quietly becoming the authority it exists to model.

## 4. Eligibility is not authority

`transition-eligibility: pass` means the evidenced preconditions for a named transition are satisfied,
and therefore that the request **may be placed before** whoever is authorised to decide it. It does
not perform the transition, authorise it, confer standing, or make the resulting state legitimate.
[TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md) reserves that to the
authorised human act, and no accumulation of satisfied obligations substitutes for it.

The converse is equally strict: `fail` reports that a published prerequisite is demonstrably unmet, not
that the transition is forbidden. Whoever holds the authority may still act, and would then be acting
in the knowledge of what is unmet — which is the entire value of computing it.

## 5. The same shape, twice

| | From | Via | To |
|---|---|---|---|
| **Value Record** | candidate | obligations and evidence → eligible for ratification | **human act** → standing |
| **This repository** | pre-release | obligations and evidence → eligible for release | **authorised act** → released |

The symmetry is why this is a general governed-transition pattern rather than a record-specific
convenience, and it is an invariant to preserve: a future record family that invents its own
lifecycle-readiness mechanism has diverged from this one for no reason.

## 6. What "released" means here

The transition this repository computes is the **release gate DAC-0032 and DAC-0033 defined** — the
point at which the typed-conformance and four-dimensional-validity architecture may be presented as
ready for adoption. It is not cutting a version: this repository has published versions throughout,
and each is recorded in the changelog.

Its prerequisites are the fifteen constraints registered in
[`decisions/evidence/DAC-0032-0033-obligations.yaml`](../decisions/evidence/DAC-0032-0033-obligations.yaml),
read by state:

| Obligation state | Contribution to eligibility |
|---|---|
| `implementation: pending` | **fail** — a published prerequisite is demonstrably unmet |
| `verification: pending` or `release-gated` | **indeterminate** — not established either way |
| implemented and verified, or not-applicable | satisfied |

`fail` outranks `indeterminate`, because a demonstrated gap is a stronger finding than an unknown one.
Every contributing obligation is named in the result's reasons: an eligibility result that reported a
bare `fail` would be an assertion rather than a finding, exactly as in the
[validation-result contract](validation-result.md).

## 7. Why compute it at all

A release checklist maintained by hand is a document that describes governance. This is governance:
the gates are **derived from accepted decisions** rather than curated, so a constraint cannot be
quietly dropped from the list, a new constraint cannot be added to a case without appearing in the
gate, and nobody has to remember what was promised.

The repository's own suite therefore reports, on every run, whether it is eligible for the release its
own accepted assurance cases defined — and today it is not, for reasons it names.
