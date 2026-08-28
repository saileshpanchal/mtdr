---
id: TDR-0045
conforms_to: mtdr/decision/tdr@1.15.0
title: External validation follows publication and cannot gate it
status: accepted
template: full
decision_date: 2026-08-27
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0032, TDR-0037, TDR-0044
confirmed_by_outcome: pending — confirm when an independent participant has run the zero-install trial against a published release and the result is recorded, or 2027-02-27, whichever is sooner
---

# TDR-0045 — External validation follows publication and cannot gate it

> **Accepted 2026-08-27.** It re-scopes one obligation under
> [TDR-0044](TDR-0044-transition-scoped-obligations.md) and discharges nothing. Ratified as its own
> act, separately from the release it enables. Evidence:
> [`evidence/TDR-0045-ratification-2026-08-27.md`](evidence/TDR-0045-ratification-2026-08-27.md).
>
> **This is the second re-scoping while a release is pending, which
> [DAC-0044](DAC-0044-transition-scoped-obligations.md) constraint 6 names as the condition that
> reopens its case.** That case is reopened by this record rather than avoided by it, and DAC-0045
> carries the reopened assessment.

## Context — what was known at the time

`DAC-0032#4` requires that *"a participant unknown to the author produces and validates the claimed
objects from a clean distribution without an MTDR application, register, service or maintainer
intervention."* It gates `released`.

It is a good test and it cannot be run. Not because it is difficult, but because of the order of
events it presumes:

> A participant unknown to the author consumes **a published distribution**. Publication is what
> makes an unknown participant possible. So an obligation satisfied only *after* publication cannot
> be a precondition *of* publication.

The gate as configured is unsatisfiable in principle, not merely unsatisfied in fact. Waiting does
not help; nothing that happens before publication can produce the evidence.

**The subject argument, which is the one that matters under
[TDR-0044](TDR-0044-transition-scoped-obligations.md) rule 1.** TDR-0044 permits re-scoping on
subject and forbids it on difficulty or timing. `DAC-0032#4`'s subject is not this repository. Under
[TDR-0032](TDR-0032-typed-multi-object-conformance.md) the conformance subjects are distinct —
record, interchange structure, package, skill artefact, **participant/implementation**, collection,
repository — and #4's measure is about *a participant*: what they can do, unaided, with a
distribution. A claim about participant behaviour implies nothing about repository conformance, and
holding a participant-subject obligation as a repository-transition precondition confuses two
subjects the standard is built to keep apart.

This is also the honest lifecycle of an open standard. A first public release is not a claim of
proven adoption; it is the artefact that makes adoption possible. The interesting question is not
whether the first release is defect-free, but whether the standard makes its defects visible,
traceable and correctable without corrupting history — which is what its own machinery exists to do.

## Decision

**`DAC-0032#4` moves from `gates: released` to `gates: externally-validated`.**

`externally-validated` is a maturity transition, later than `released`, whose conditions concern
**independent consumption**: whether participants unknown to the author can obtain, interpret,
validate and use the published artefacts without intervention. A repository may be `released` and not
`externally-validated`, and that pairing is the normal state of a newly published standard rather
than a deficiency.

The obligation is **retained entire** — measure, owner, note and `release-gated` verification state
unchanged. It is not discharged, not weakened and not deleted. It remains carried in every validation
result under `carried-not-gating`, so a reader of any result sees that MTDR does not claim external
validation.

**What this record does not do**, stated because a re-scoping made under release pressure deserves
the narrowest possible reading:

- It does not assert that MTDR is easy to install, adopt or understand. That is #4's question and it
  remains open.
- It does not create the `externally-validated` transition's full conditions. It names the transition
  and moves one obligation to it. Whatever else gates that transition is a later decision.
- It does not make `released` eligible by itself. Eligibility is computed, and this record only
  changes which obligations the computation reads.

## Evidence

- **Business** — an open standard nobody can obtain generates no external evidence. Gating
  publication on post-publication evidence guarantees the evidence never exists.
- **Architecture** — TDR-0032's typed subjects, applied. #4's subject is a participant; `released`'s
  subject is the repository. The mismatch is structural, not circumstantial.
- **Regulatory** — not material to this decision. It creates no claim about the artefact's quality.
- **Operations** — this is the ordinary lifecycle of published work: release, observe, correct. The
  repository's supersession discipline is what makes correction safe.
- **Customer** — an adopter is better served by a governed artefact carrying an explicit statement
  of what is not yet proven than by no artefact at all.
- **Data** — one field on one register entry changes. Nothing else moves.
- **External** — **no external correspondence is claimed.** That release-then-validate is common
  practice is context, not evidence, and common practice is not an argument this standard accepts on
  its own.

## Alternatives rejected

1. **Leave #4 gating `released`.** Rejected: the gate is unsatisfiable in principle, and a gate that
   can never open is not a control. It would also force the release into an untruthful shape later,
   which is worse than re-scoping it honestly now.
2. **Have the author, or someone the author briefs, run the trial.** Rejected: the measure says
   *unknown to the author* and its own note says it *"cannot be simulated by its author."* Running it
   anyway and recording the result would be manufacturing evidence.
3. **Publish informally, without a governed release, until #4 clears.** Rejected: the repository is
   already public and this changes nothing about the evidence. It would also leave the governed
   release permanently deferred behind a condition publication itself is required to produce.
4. **Weaken #4's measure so it can be met before release.** Rejected outright. Rewriting a test until
   its author passes is the failure this register was built to prevent.
5. **Delete #4.** Rejected: the requirement is real and is the single most valuable piece of external
   evidence this project could hold.

## Options foreclosed

- No obligation may be re-scoped on the grounds that publication has not yet happened, other than
  one whose measure genuinely requires a published artefact to exist.
- `externally-validated` may not become a holding pen. An obligation moved there must have a subject
  that is genuinely external.
- No release may claim external validation, adoption or proven usability while #4 is outstanding.
- MTDR may not later assert #4 satisfied on evidence produced by the author or by anyone the author
  coached through the internals.

## Consequences and review

`released` becomes gated by thirteen obligations, all verified. **The gate reaches `pass`** — and
`pass` means only that the published prerequisites of that transition are met and the request may be
placed before whoever decides it. It is not release authority, which remains an authorised human act
under [TDR-0027](TDR-0027-human-ratification-confers-standing.md).

The release claim this permits is deliberately modest, and any wider claim is false:

> v1.30.0 is the first governed public release of MTDR. It is structurally, semantically and
> relationally verified against its own published contracts. **External zero-install adoption
> evidence is not yet claimed** and will be gathered through use.

Success is an independent participant running the zero-install trial against a published release,
uncoached, with the result recorded whatever it says — a failure being the more useful outcome.
Review at that evidence, or 2027-02-27, whichever is sooner.
