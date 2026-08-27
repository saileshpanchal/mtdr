---
id: TDR-0042
conforms_to: mtdr/decision/tdr@1.15.0
title: Classify every changelog version heading as an unreleased development label
status: accepted
template: minimal
decision_date: 2026-08-21
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0027, TDR-0034, TDR-0037
confirmed_by_outcome: pending — confirm when one reconciled successor is published as a governed release transition with a matching tag, release record and verification evidence
---

# TDR-0042 — Classify every changelog version heading as an unreleased development label

> **Accepted 2026-08-21. It still authorises no release.** A re-stated judgement — a fresh
> decision informed by a stranded candidate, not a carried-forward representation of it.
> Evidence: [`evidence/TDR-0042-ratification-2026-08-21.md`](evidence/TDR-0042-ratification-2026-08-21.md).
>
> The *question* is the one raised on `codex/gate-b-decision-drafts` (`f966a05`), and the answer is
> compatible with what that candidate proposed. The *facts* are not. The candidate addressed ten
> headings; this record addresses thirty. The candidate was written before
> [TDR-0037](TDR-0037-release-eligibility-from-standing-governance.md) made `released` a governed
> transition, which changed the governance context the question sits in.
>
> This record therefore **states the current facts rather than transcribing the candidate's**. That
> candidate was never ratified and its identifier is burnt; nothing here inherits standing, and the
> widened scope is argued on its own evidence under *Context* rather than on the candidate's
> authority. The audit is
> [`evidence/gate-b-candidate-disposition-2026-08-21.md`](evidence/gate-b-candidate-disposition-2026-08-21.md).

## Context — what was known at the time

`CHANGELOG.md` carries **thirty version headings**, `1.0.0` through `1.29.0`, each dated, each in the
form Keep a Changelog uses for published releases.

The repository has **no tags**. Not on the working clone, and not on the origin —
`git ls-remote --tags origin` returns nothing. A GitHub release requires a tag, so the absence of
tags is also the absence of releases. Every heading is a label applied during development.

Two things have happened since the original candidate was written, and they pull in opposite
directions.

**The surface tripled.** The candidate classified `v1.12.0` – `v1.21.0`, the ten labels on the branch
under review. Nineteen more have been added since, and the ten it named are now a minority of the
problem. The reasoning it gave — a version string establishes sequence during work and does not
demonstrate that an artefact was published for adopters — does not stop at a branch boundary.
Classifying only the original ten would leave the other twenty unaddressed while implying, by
omission, that those were releases. **Widening the scope is the same judgement applied to the
evidence as it actually stands, not a new one.**

**The register acquired a mechanism that contradicts the changelog's form.**
[TDR-0037](TDR-0037-release-eligibility-from-standing-governance.md) made `released` a governed
transition of this repository, with eligibility computed from the obligations register rather than a
curated checklist. `tests/verify.py` requests that transition on every run and currently reports it
**not eligible**, naming DAC-0032 constraint 2. So the repository now holds a mechanism stating that
release has never yet been permissible, beside a document whose form asserts thirty releases. Both
are honest in isolation; together they are a contradiction the register has not decided.

The fact has meanwhile been relied on without ever being decided.
[TDR-0027](TDR-0027-human-ratification-confers-standing.md) refers in passing to *"the unreleased
v1.12–v1.21 branch"*, and the v1.22.0 changelog entry describes identifiers burnt on *"a branch
subsequently dropped"*. Unreleasedness is already load-bearing in accepted reasoning and rests on no
record — which is the same defect, in the same repository, that TDR-0034 introduced the allocation
register to stop.

## Decision

**Every version heading in `CHANGELOG.md` — `1.0.0` through `1.29.0` — is an unreleased development
label, not a published release.**

The labels are preserved in the changelog and in commit history as truthful evidence of how the work
evolved. **No retrospective tag or release is created for any of them.**

The first genuine release is a **single governed transition** under TDR-0037: eligibility computed
from the obligations register, an authorised human act, and then one tag, one release record, one
changelog entry that says which commit and which generated catalogue it describes.

**This record does not choose that version number and does not authorise publication.** Eligibility
is not authority (TDR-0037); a record classifying history confers even less.

If ratified, `CHANGELOG.md` gains a statement of its own status in the same change — so a reader
arriving at the file learns what the headings are without having to find this record.
**No changelog text moves while this record is proposed.**

## Alternatives rejected

1. **Tag every labelled commit retrospectively.** Rejected: a tag asserts a published state for which
   no publication evidence exists, and manufacturing thirty of them would make the repository's own
   history the first thing in it that cannot be trusted.
2. **Erase the version labels.** Rejected: the commit history truthfully records how the proposal
   evolved, and labels that did not become releases are still evidence of sequence. Deleting them
   would also be an edit to history made to improve its appearance.
3. **Treat changelog headings as sufficient publication evidence.** Rejected: documentation of
   intended release content is not evidence that an artefact was made available. The form of a
   heading is not a fact about the world.
4. **Classify only the original ten, as the candidate proposed.** Rejected: it addresses a third of
   the surface and implies the rest were released. The candidate's scope was set by the branch under
   review, not by the reasoning.
5. **Wait for the first real release and let it settle the question implicitly.** Rejected: the
   contradiction is being read now, by anyone who opens the changelog, and an implicit answer given
   later is not a record. It would also leave TDR-0027's reliance on "unreleased" resting on nothing.
6. **Do nothing.** Rejected: a reader currently infers thirty releases from a repository that has
   published none, and the register's own release gate says the opposite.

## Options foreclosed

- No retrospective release history may be manufactured for `1.0.0` – `1.29.0` without new evidence
  that a specific labelled artefact was genuinely published.
- The eventual first release cannot claim that each development label was an adopter-facing state.
- A version heading may not, in this repository, be cited as evidence of publication.

## Review

Confirm when one reconciled successor is published as a governed release transition with a matching
tag, release record, changelog entry and verification evidence — at which point this record's
classification becomes historical and the release record becomes the current account.

Reopen earlier if evidence emerges that any labelled artefact was in fact published by some route
that leaves no tag. This record classifies on the evidence available, and says plainly that the
evidence is the absence of tags rather than a positive record of non-publication.

**A DAC is not routed.** This is a bounded release-governance classification with no material
customer, adversarial, authority or execution-risk delta: it creates nothing, publishes nothing, and
authorises nothing. Recording the non-routing is the assurance decision; a ceremonial case would
weaken the proportionality rule this repository demonstrates.
