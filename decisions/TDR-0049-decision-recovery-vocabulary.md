---
id: TDR-0049
conforms_to: mtdr/decision/tdr@1.15.0
title: Adopt the decision-recovery vocabulary — contribution classes, the canonical not-a-decision reasons, and the recovery pipeline
status: accepted
template: minimal
decision_date: 2026-11-07
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0023, TDR-0026, TDR-0048
confirmed_by_outcome: pending — confirm only when an implementation outside this repository loads the not-a-decision reasons and the recovery roles from the published vocabulary instead of restating them, and a further independent confirmation, by an adopter who is not the drafter over material the drafter did not write, has run the recovery pipeline end to end. 2027-05-07 is the review date; reaching it confirms nothing
---

# TDR-0049 — Adopt the decision-recovery vocabulary — contribution classes, the canonical not-a-decision reasons, and the recovery pipeline

> **Accepted on 2026-11-27** by the owner's ratification ([evidence](evidence/TDR-0049-ratification-2026-11-27.md)), after
> [TDR-0048](TDR-0048-historical-recovery-doctrine.md).
>
> **Returned on 7 November 2026 and amended** ([the return](evidence/TDR-0048-0049-owner-return-2026-11-07.md)) on the owner's rulings R1 to R4 — decision 6 below —
> and the fixtures they affect, FIX-301 among them. It stays proposed, and its confirmation needs a
> further independent run: the trial of 7 November does not meet it.
>
> **Corrected on 26 November 2026, after an [independent review](evidence/recovery-records-review-2026-11-26.md)**:
> invocation has one definition, the act's own citation; every place this record and its
> specification go beyond a ruling is listed [below](#where-this-record-goes-beyond-the-owners-rulings);
> the *undetermined* proportionality outcome is limited to historical candidates; and what a return
> would revert is [listed](#if-this-record-is-returned). It has no assurance case of its own: its four
> rulings, which bear on authority and on what makes one candidate, are assessed in
> [DAC-0048](DAC-0048-historical-recovery-doctrine.md). It stays proposed.
>
> **Corrected again on 27 November 2026, at the owner's direction** ([preserved](evidence/TDR-0048-0049-0050-owner-dispositions-2026-11-27.md)). The
> owner's condition: an instrument never authenticates itself by an unverified assertion. The
> assistant's recommendations, which the owner directed should proceed: `taxonomy_version` 1.0.0 is
> the vocabulary as ratified, and no separate assurance case is needed, DAC-0048 covering its rulings.
> The direction was an engineering instruction. It decided nothing and ratified nothing, and none of
> these recommendations was the owner's decision until the owner ratified this record. It stays
> proposed.

## Context — what was known at the time

The value language recovers commitments through a contribution vocabulary and five lifecycle skills
under an orchestrator ([TDR-0026](TDR-0026-value-recovery-vocabulary.md)). The decision language had
the shared stages, its roles, its admission test and `draft-tdr`, and nothing that said what a fragment
of a minute or a paper could contribute to a decision before drafting. Its five reasons something is
not a decision lived in one skill's prose — and an implementation that needed them had restated them by
hand, so the skill had become the practical source of normative meaning. TDR-0048 states the recovery
doctrine; it leaves each language to state its own matrix and its own recovery roles.

## Decision

**Give the decision language the recovery layer the value language has, and put its vocabulary in the
specification, not in a skill.**

1. **Seventeen contribution classes**, in
   [`records/decision/specification/decision-contribution.md`](../records/decision/specification/decision-contribution.md),
   carried through the shared `RecordContribution` exactly as value's are. Six never populate a field:
   `challenge`, `corroboration`, `non-decision`, `not-a-decision`, `applicability` and `persistence`;
   the last four are **findings**, reported by fragment and never grouped into a candidate. The `unclassified` outcome, the
   `derivation` marker and the completeness view apply as TDR-0026 defined them.
2. **The five reasons something is not a decision become normative, with stable identifiers** —
   `status-update`, `action`, `preference`, `restatement`, `operational-routine` — defined in the
   specification and published in a versioned machine-readable form,
   [`decision-contribution.schema.json`](../records/decision/schema/decision-contribution.schema.json).
   Its `taxonomy_version` 1.0.0 is the vocabulary as this record ratifies it; artefacts made before
   ratification, the trial of 7 November among them, carried 1.0.0 as a draft.
   `decision-identification` and every recovery skill cite it; a consumer loads it.
3. **No decision evidenced, and evidence that no decision was made, are different findings.** The
   second has kinds — `deferred`, `not-reached`, `withdrawn` — and a deferral that commits is a
   decision.
4. **The recovery roles are declared by the package:** `decision-date` the event role; `context` and
   the seven `evidence-*` roles the context roles, because evidence considered at the time is as
   exposed to hindsight as context; and `accountable-owner`, `alternative-rejected` and the `owner`,
   `authority` and `alternative` classes never inferred. The suite enforces them on every historical
   candidate for a consequential decision, from that declaration — with two more: no finding class is
   carried as a contribution, and the **invocation** role, `authority`, never rests on unlinked or
   retrospective material.
   **The `authority` class is the delegation or instrument cited**, never the forum: *the board agreed*
   is part of the decision statement, and a forum proposed as owner stays `context`, as the semantic
   roles already say. **A finding** is reported as its fragment with a classification object valid
   against the machine-readable form. **For a historical candidate with no `reversal-cost` evidence**, the
   proportionality outcome is stated as *undetermined*, which satisfies admission criterion 6 and never
   defaults to a tier (E8).
5. **The decision language's instance of TDR-0048's evidence matrix** — what each kind of material can
   support, claim by claim.
6. **The owner's rulings R1 to R4 of 7 November**
   ([the return](evidence/TDR-0048-0049-owner-return-2026-11-07.md)), each in the specification:
   - **Applicability is not invocation** (R1). An instrument may establish that authority applied; it does
     not show that whoever acted relied on it. Invocation — the act cites the instrument (E1) — is an
     `authority` contribution. Applicability — the instrument's terms shown to cover the act — is an
     `applicability` finding, beside the candidate, never an authority contribution and never a
     judgement of competence.
   - **One act, one candidate** (R2). One motion carried on one vote is one composite candidate, each
     resolution individually traceable as its own `consequence`; separate votes or decisions are
     separate candidates.
   - **An instrument may record its own adoption** (R3) — contemporaneous, authenticated, with evidence of
     its legal or organisational effect — and is never set aside solely because the instrument is the
     evidence. It never authenticates itself by an unverified assertion, and authenticity the evidence
     does not settle is recorded as unresolved (E5).
   - **Persistence is not a decision** (R4). Continued operation is a `persistence` finding, with its
     authority for continuation flagged; a decision to continue is recovered only from evidence of
     that act.
7. **Five skills**: `identify-decision-contributions`, `reconcile-decision-contributions`,
   `challenge-decision-record` and `validate-decision-record` specialising the shared stages, and
   `recover-decision-records` composing them with `draft-tdr` under TDR-0026's composition ruling.
   `draft-tdr` gains the completeness view, and renders a historical candidate as a candidate view,
   never as a TDR draft ([TDR-0048](TDR-0048-historical-recovery-doctrine.md), amended on 23 November). The standard's skill
   count moves from twenty-five to thirty.

## Alternatives rejected

1. **Leave the reasons in `decision-identification`.** Rejected: a skill's prose is not a contract, and
   the evidence is that consumers restate it rather than cite it.
2. **Use the shared stages directly, with no decision specialisations.** Rejected: the shared stages
   cannot name the decision language's roles, its matrix or its recovery roles without ceasing to be
   record-neutral.
3. **Put the classes in a new interchange schema.** Rejected for the same reason TDR-0026 rejected it:
   the classes ride on the existing `semantic_role`, and only the closed vocabulary itself is published
   as data.

## Options foreclosed

- No not-a-decision reason or contribution class is added, renamed or removed without a superseding
  record — and the machine-readable form's `taxonomy_version` moves with it.
- No recovery skill restates the vocabulary, the doctrine or a shared stage's mechanics.
- No recovery skill produces a review event or confers standing.
- No `applicability` finding becomes an authority contribution, and no `persistence` finding becomes a
  decision, by any route — confidence, duration or repetition included.

## Where this record goes beyond the owner's rulings

The return asks that an amendment applying a ruling to a case the ruling did not name say so. These
are those places. Each is the **drafter's** (written while the records were amended) or the
**assistant's** (a correction of 26 November, after the independent review), and none is the owner's
until the owner decides it. The owner's direction of 27 November ([preserved](evidence/TDR-0048-0049-0050-owner-dispositions-2026-11-27.md)) is
recorded against each question, as the owner's condition or as the assistant's recommendation that the
owner directed should proceed. It was an engineering instruction: it decided and ratified nothing, and
an item became the owner's decision only when the owner ratified this record.

- **E1 — Invocation is the act's own citation** (R1). *The assistant's resolution.* The specification
  also allowed an instrument named in "material shown to have been before whoever acted"; this record
  and both recovery skills said "the act cites the instrument". The narrower reading is kept, because it
  is this record's text and because ruling R1 says to "never invent an authority contribution". Material
  before whoever acted that names the instrument is evidence for the applicability finding, and the
  finding records that it was put before them. Where:
  `decision-contribution.md`, its schema's description, FIX-520. **Owner's question:** may such
  material support an authority contribution? The independent confirmation of 26 November met the case
  (advice that "4.5 covers a change of date", before an act that did not cite it). That evidence is published as [limited internal confirmation evidence](evidence/DAC-0048-confirmation-2026-11-26/). **Assistant's recommendation, applied at the owner's direction of 27 November:**
  keep it as written.
- **E2 — The test for applicability** (R1). *The drafter's.* A span of the instrument and a span of the
  act that brings the act within its terms, and a statement of whether the body that acted is the body
  the instrument names. Where: `decision-contribution.md`, FIX-031, FIX-301 D1.
- **E3 — FIX-301 D2** (R1). *The assistant's correction.* No span of the board's act brings D2 within
  §3.2, so the case records an unresolved authority question, as v1.30.0 did, and no applicability
  finding.
- **E4 — What establishes a single act** (R2). *The drafter's.* One signature or one approval counts
  as one act; choices by different people or at different times are separate; the record of the act
  establishes it, and a shared agenda item does not. Where: `decision-contribution.md`, FIX-032.
- **E5 — What counts as authentication and as effect** (R3). *The drafter's.* Authentication by an
  adopting resolution, a signature, seal, publication or register entry; effect by a commencement that
  has passed or a later act citing it. As written, an instrument's statement of its own signatures and
  register entry authenticates it (FIX-033), so a forged extract would pass. **Owner's question:** may
  authentication and effect be evidenced by the instrument's own text and by consistent conduct, or
  only by independent material and acts that cite it? **Owner's condition, 27 November:** an instrument
  may record its own adoption, but does not establish its own authenticity through an unverified
  assertion; where the supporting evidence is insufficient, authenticity is recorded as unresolved.
  FIX-033's Standing Orders are therefore reported, not a candidate. Where: `decision-contribution.md`, FIX-033,
  FIX-301 SRC-01.
- **E6 — A reported commitment is not recovered** (R4). *The drafter's.* A note that money "has been
  included" evidences that a commitment occurred and supports no candidate. It reverses FIX-301's
  answer accepted in v1.30.0. **Owner's question:** is such a report evidence of a decision to recover,
  with its date unknown, or only evidence that some commitment occurred? **Assistant's recommendation, applied at the owner's direction of 27 November:** keep it
  as written; at ratification, v1.30.0's FIX-301 answer is superseded. Where:
  `decision-contribution.md`, FIX-034, FIX-301 SRC-06.
- **E7 — Ruling R1 and the value language.** *The assistant's statement of scope.* FIX-301's V1 keeps
  `committed_by` and the counter-signatory as v1.30.0 accepted them, although they rest in part on
  scheme paragraphs no act cites. **Owner's question:** does R1 extend to the value language's
  inference of `committed_by`? **Assistant's recommendation, applied at the owner's direction of 27 November:** not in this release.
- **E8 — An undetermined proportionality outcome satisfies admission criterion 6.** *The drafter's,
  limited to historical candidates by the assistant.* No ruling covers it. It is not a relaxation of the
  kind [TDR-0048](TDR-0048-historical-recovery-doctrine.md) forecloses, on this reasoning: the criterion
  requires the outcome to be stated, and [TDR-0017](TDR-0017-language-admission-test.md) already holds
  that an honest "undetermined, because …" discharges a criterion that silence fails. Limiting it to
  historical candidates leaves every other candidate's admission as v1.30.0 had it. **Owner's
  question:** keep it for historical candidates, or revert criterion 6 to its v1.30.0 text? **Assistant's recommendation, applied at the owner's direction of 27 November:** keep it for
  historical candidates. Where:
  `admission.md` criterion 6, and `draft-tdr` §2, which says the same.
- **E14 — Applicability and persistence are findings** (R1, R4). *The drafter's.* The return said to
  record evidenced applicability separately, and persistence as observed behaviour. That both are
  findings, reported by fragment and never inside a candidate, and that `continuation_authority` is
  either `evidenced` or `not-evidenced`, is the drafter's form. Numbered last because the re-review of
  26 November found it unlisted. Where: `decision-contribution.md` *Findings*, its schema.


## Review

On the confirmation evidence, or 2027-05-07. A recurring `unclassified` pattern, or a consumer that
must map the reasons to its own spelling indefinitely, reopens it.
