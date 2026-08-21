# Gate-B candidate disposition — 2026-08-21

**Kind:** reconciliation evidence · **Status:** record of an audit, not a decision  
**Audited branch:** `codex/gate-b-decision-drafts` at `f966a05d6c65dbbd01190e424b3ada7d54018a9a`  
**Audited against:** `9cd4ce4` — the live line carrying TDR-0034 … TDR-0039 and the VR-4 freeze  
**Prepared for:** the carry-forward on `reconciliation/gate-b-carry-forward`

## Why this document exists before the records do

[TDR-0031](../TDR-0031-reconcile-ratified-judgement-after-identifier-collision.md) settled how a
*ratified* judgement is reconciled when its identifier collides. Five Gate-B candidates were never
ratified — the Gate-B evidence directory holds ratification records for TDR-0020, TDR-0025 and
TDR-0027 and for nothing else — so **TDR-0031's standing carry-forward does not apply to any of
them.** They carry no standing to preserve.

That makes them ordinary new proposals, and it makes the question ordinary too: *is each judgement
still open?* Three of the five had been answered by later work, wholly or in part, and a
carry-forward that reintroduced them unexamined would re-open settled matters under fresh
identifiers — the failure mode TDR-0031 exists to prevent, arriving from the other direction.

**This document is an audit. It creates nothing, ratifies nothing, and confers nothing.**

## The identifiers are gone, and that is not in question

[ALLOCATION.md](../ALLOCATION.md) records TDR-0028, TDR-0029 and TDR-0030 as **burnt** under
[TDR-0034](../TDR-0034-public-allocation-authority.md): materially published, standing never acquired,
never reusable. The v1.22.0 changelog states the same. No judgement below may be represented on its
original identifier, whatever its disposition.

## Three kinds of outcome, and they must not be conflated

A successor produced during a reconciliation is not automatically a *carry-forward*. Three
different things can happen to a stranded candidate, and describing all three as carry-forward
would misrepresent where each successor's judgement actually came from — which is the precise
failure this reconciliation exists to avoid.

| Kind | What it means | Standing implication |
|---|---|---|
| **Carry-forward** | The stranded judgement is still open and is represented substantially as it stood. The successor's judgement is the candidate's. | None. These candidates were never ratified; nothing carries. |
| **New proposed judgement** | Reconciling the candidate against artefacts that moved produced a *different* judgement. The candidate is the origin of the question, not the author of the answer. | None, and none is implied by the candidate's existence. |
| **Re-stated judgement** | The question is the candidate's and the answer is compatible with it, but the facts it rests on have materially changed, so the record states the current facts rather than transcribing the candidate. | None. |

**No successor on this branch is a carry-forward of standing.** TDR-0031's crosswalk mechanism binds
a ratification act to a new representation, and there is no ratification act here to bind. The
distinction above is about the *provenance of the judgement*, which is a separate question from
standing and is recorded because a reader will otherwise assume the two travel together.

## Disposition

| Gate-B candidate | Disposition | Kind | Successor | Basis |
|---|---|---|---|---|
| TDR-0018 — decompose to admission-only | **open, and a new question** | surfaced only | none | see below |
| TDR-0019 — VR v2 lineage correction | **closed** | disposed | none | v1.29.0 |
| TDR-0023 — sequencing is not orchestration | **open** | **carry-forward** | TDR-0040 | absent from the live line |
| TDR-0028 — five-question information governance | **open** | **new proposed judgement** | TDR-0041 | TDR-0015 accepted, unsuperseded |
| TDR-0029 — release-history classification | **open, and materially changed** | **re-stated judgement** | TDR-0042 | see below |

The orphan assurance cases are **disposed with reasons and not rebound**; see below.

### TDR-0019 — closed

The Gate-B candidate proposed to correct TDR-0019's lineage and add lifecycle constraints. v1.29.0
answered it and answered it the other way: the VR schema was remediated under TDR-0019, TDR-0033 and
[TDR-0039](../TDR-0039-state-relative-requirements.md) **with TDR-0019 left unsuperseded, because its
judgement never changed.** What the schema encoded was a transition requirement leaking into a
representation requirement — a defect in the schema, not in the decision.

Carrying this candidate forward would propose superseding a record that a later, evidenced ruling
established had nothing wrong with it. **No successor record.**

### TDR-0023 — open

The candidate adds one distinction to the accepted portable-skill architecture: **canonical
behavioural sequencing is not runtime orchestration.** A portable skill may normatively require
stage order, re-entry conditions and stopping behaviour; scheduling, model choice, retries,
parallelism and persistence remain outside MTDR.

Searched on the live line: the phrase *runtime orchestration* occurs once, in
[TDR-0032](../TDR-0032-typed-multi-object-conformance.md) §99, and there only as an item in a list of
things conformance does not require. The positive distinction is stated nowhere — not in TDR-0032, not
in [TDR-0038](../TDR-0038-distribution-bundles-and-the-layer-boundary.md)'s falsification criterion, not
in the layer boundary at `specification/standards-boundary.md`. Those are adjacent and none is this.

The judgement is unrepresented, and the successor states it substantially as the candidate did.
**Successor TDR-0040, proposed — a genuine carry-forward.**

### TDR-0028 — open

TDR-0015 is `accepted` and unsuperseded on the live line. The candidate's five-question model —
knowledge and access · authority · permitted use · disclosure · purpose and context — is
unrepresented anywhere in the register.

**Successor TDR-0041, proposed — a new proposed judgement, not a carry-forward.** The
candidate proposed five *information-governance* questions. Specification §4.4 has since
become five *scope* questions in two groups, renaming visibility to access, promoting
disclosure, and naming use as a distinction outside the record.
Reconciling the candidate against that produced a different formulation — six questions in two
groups, with use promoted and purpose qualifying all three information-scope questions. **The
candidate is the origin of the question; it is not the author of this answer.** The successor
carries the candidate's proposed supersession of TDR-0015 as a proposal and not as a fact, and
narrows it to TDR-0015's third judgement alone.

### TDR-0029 — open, and the facts have moved

The candidate classified v1.12.0 – v1.21.0 as unreleased development labels. That framing is now
too narrow to be carried forward verbatim. As at `9cd4ce4`:

- `CHANGELOG.md` carries **thirty** version headings, 1.0.0 through 1.29.0, each dated;
- the repository has **zero** tags;
- [TDR-0037](../TDR-0037-release-eligibility-from-standing-governance.md) has since made `released` a
  governed transition of this repository, and `tests/verify.py` reports it **not eligible**, naming
  DAC-0032 constraint 2.

So the register now contains a mechanism that says this repository has never been eligible to
release, beside a changelog whose form asserts thirty releases. Both are honest in isolation. The
question the candidate raised is not merely still open — the surface it applies to has tripled, and
it now has a governed transition to be consistent with.

**Successor TDR-0042, proposed — a re-stated judgement, not a carried-forward
representation.** The question is the candidate's and the answer is compatible with it, but
the facts have materially changed and the governance context with them. The
record states the current facts rather than transcribing the candidate's, and says so in its own
text.

### TDR-0018 — open, and not the same question any more

The candidate decomposed accepted TDR-0018 into admission-only, relocating the conformance boundary
to the then-proposed TDR-0020 and the standing rule to the then-proposed TDR-0027.

**Both destinations now exist with standing** — the standing rule as
[TDR-0027](../TDR-0027-human-ratification-confers-standing.md), the conformance boundary as TDR-0032.
The decomposition's purpose is served. What is not settled is its premise: accepted TDR-0018 still
asserts *"the standard ends at the artefact boundary"*, and TDR-0032 has since made conformance a
typed claim and the register optional. Whether TDR-0032 narrowly superseded part of TDR-0018 —
judgement-granular supersession, as it did for TDR-0012 — is **a question about an accepted record
that no record has asked**.

That is a new substantive judgement, not a representation recovery. Deciding it inside a
reconciliation is precisely the drift a reconciliation must not permit.

**No successor drafted. Recorded here as an open question for human review.**

## The orphan assurance cases

Gate-B carries DAC-0017, DAC-0018, DAC-0019, DAC-0020, DAC-0021, DAC-0023 and DAC-0025. None is
carried forward by this reconciliation.

- **DAC-0020 and DAC-0025** assure the judgements that reached the live line as TDR-0032 and
  TDR-0033, whose own accepted cases — DAC-0032 and DAC-0033 — are already the register's
  representation of that assurance, with fifteen constraints tracked in
  [`DAC-0032-0033-obligations.yaml`](DAC-0032-0033-obligations.yaml).
- **DAC-0017, DAC-0018, DAC-0019, DAC-0021 and DAC-0023** would assure records already `accepted`.
  A Decision Assurance Case records the reasoning that challenges a decision's consequences
  **before execution**. Whether one may be admitted retrospectively, and what it would mean if it
  reached a disposition other than proceed, is an unasked question about the DAC's own semantics.

**No orphan DAC is carried forward.** New assurance is routed by materiality against the successors
actually drafted, which is a different thing from rebinding an old case to a new number.

## What this audit did not do

- It did not ratify anything, and confers no standing on any successor.
- It did not edit any accepted record.
- It did not reuse a burnt identifier.
- It did not decide the TDR-0018 question it surfaces.
- It did not treat the Gate-B text as authority. Where a candidate's facts had moved, the successor
  states the current facts and says that it does.
