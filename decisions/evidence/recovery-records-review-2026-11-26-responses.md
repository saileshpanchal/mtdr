# Responses to the review of the recovery records — 26 November 2026

How each finding of the [independent review](recovery-records-review-2026-11-26.md) of DAC-0048,
TDR-0048, TDR-0049 and TDR-0050 at `57d68c00406f2260b832be0fc8c14a0ddbc9d692` was dealt with. The
responses are made in the commit that adds this file. **Nothing here ratifies anything**; where a
response is a semantic choice, it is labelled as the drafter's or the assistant's and put to the owner.

One rule decided the direction where a finding could go either way. Where the candidate changed
Decision or Value behaviour accepted in v1.30.0 without a ruling to authorise it, the accepted
behaviour is kept and the change is put to the owner. Where a ruling authorised a change, the change is
kept and each application beyond the ruling's words is labelled.

## Blocking for ratification

| | Response | Where |
|---|---|---|
| **RR1** Extensions unlabelled | **Fixed.** Each extension is listed, numbered E1 to E13, with whose it is and the owner's question, and marked in italics where it applies | TDR-0049 and TDR-0048, *Where this record goes beyond the owner's rulings*; TDR-0050 (E13); `decision-contribution.md`, `historical-recovery.md`, `admission.md`, FIX-031 to FIX-034, FIX-301 |
| **RR2** "The identity check is repaired" | **Fixed**, without reintroducing `0650856`. The records say the check is as released in v1.30.0, that the prior-version change is held out for its own decision, and that Alternative 3 stays rejected on A6 alone, with the option open only once that decision is made | DAC-0048 *Uncertainty* and *Declared interactions*; TDR-0048 *Context* and Alternative 3; [evaluation](identity-check-0650856-evaluation-2026-11-26.md) |
| **RR3** Invocation defined two ways | **Fixed: one definition, the act's own citation** (E1, the assistant's resolution). This is TDR-0049's own text and that of both recovery skills, and ruling R1 says "never invent an authority contribution". Material before whoever acted that names an instrument the act does not cite is evidence for the applicability finding. The validator is unchanged: it enforces the floor (never `unlinked` or `retrospective`), and the specification says challenge checks the rest. The broader reading is put to the owner | `decision-contribution.md` (classes, roles, matrix, *Applicability is not invocation*); its schema's description; FIX-520 |

## Should-fix before ratification

| | Response | Where |
|---|---|---|
| **RR4** DAC-0048 not re-assessed | **Fixed.** Re-assessed on 26 November: rulings R1 to R4 lens by lens, the 23 November amendment and the corrections. `assessed_at` moves to 2026-11-26. Whether TDR-0049 needs its own case is put to the owner | DAC-0048 *Re-assessment* |
| **RR5** Self-certified authentication | **Assessed, and put to the owner** (E5). The risk is recorded as not mitigated, with the two options, and added to the decision debt. The text is not changed, because which option to take is a semantic choice the drafter flagged as an owner's question | DAC-0048 *Re-assessment* and debt; TDR-0049 E5; FIX-033 |
| **RR6** 23 November amendment unevidenced | **Fixed as far as the evidence allows.** The ruling is preserved as its only record shows it, the commit message of `4aa7d5f`, and the owner is asked to confirm its words. The engine runs of 20 and 22 November are not in the repository, and the note says so. TDR-0049's decision 7 now names the candidate view | [`TDR-0048-owner-ruling-2026-11-23.md`](TDR-0048-owner-ruling-2026-11-23.md); TDR-0048 banner; TDR-0049; CHANGELOG |
| **RR7** Ruling numbers | **Fixed.** TDR-0048's six are A1 to A6; the return's five are R1 to R5, and every record uses them. The review of 6–7 November is not preserved, and TDR-0048 says so | TDR-0048, TDR-0049, TDR-0050, FIX-301 |
| **RR8** TDR-0050 not independent | **Fixed in the text.** TDR-0050 lists what already relies on it and what a return would revert, and its third alternative no longer claims independence. The order follows: TDR-0050 before TDR-0048, or with it | TDR-0050; TDR-0048 *What this record relies on* |
| **RR9** Ratification order and debt | **Clarified, and put to the owner.** Debt rows 1 and 2 are drafted (the matrix; FIX-029 and FIX-030) and become normative with TDR-0049. The interval in which TDR-0048 would be normative without a decision-package matrix is stated, with the choice of ratifying in one sitting | DAC-0048 *Decision debt*, *The order of acceptance* |
| **RR10** In-place edits | **Listed.** Each record says which existing text was edited for it and is reverted if it is returned. Nothing is reverted now, because the release waits for ratification | TDR-0048, TDR-0049, TDR-0050, *If this record is returned*; the draft release record |
| **RR11** Criterion 6 relaxed | **Narrowed, and put to the owner** (E8). The undetermined outcome satisfies criterion 6 for a historical candidate only, so every other candidate's admission is as v1.30.0 had it. TDR-0049 gives the reason it is not the relaxation TDR-0048 forecloses, using TDR-0017's rule that an honest "undetermined, because …" discharges a criterion. Reverting criterion 6 entirely is the alternative | `admission.md` criterion 6; TDR-0049 decision 4 and E8 |
| **RR12** FIX-301 D2 | **Fixed** (E3, the assistant's correction). No span of the board's act brings D2 within §3.2, so there is no applicability finding. The authority question is recorded as unresolved, as v1.30.0 recorded it | FIX-301 D2 and *Must not* |
| **RR13** FY28 reverses an accepted answer | **Labelled, and put to the owner** (E6). Ruling R4 reverses v1.30.0's D3, the permanent arrangement. The FY28 point goes further than R4's words, and the fixture now quotes the answer v1.30.0 accepted beside the drafter's | FIX-301 SRC-06; FIX-034; `decision-contribution.md`; TDR-0049 E6 |
| **RR14** 16 versus 17 | **Fixed.** DAC-0048 and the trial README say that why the report said sixteen is not established, and that the drafter's "arithmetic slip" is a reading, not evidence. They also say which trial candidates are now wrong answers. There are five, not four: `brackwell-1`, the scheme's adoption, is one too | DAC-0048 *Uncertainty*; trial README |
| **RR15** Confirmation gate wording | **Fixed.** Each gate says "confirm only when", and that 2027-05-07 is a review date that confirms nothing. TDR-0049's gate names the further independent confirmation, by an adopter who is not the drafter, over material the drafter did not write | TDR-0048, TDR-0049 and TDR-0050 frontmatter; TDR-0048 *Consequences* |
| **RR16** FIX-301 V1 `committed_by` | **Scoped, and put to the owner** (E7). V1 stays as v1.30.0 accepted it, and the fixture says that ruling R1 was given for the decision language and is not extended to Value without the owner's decision | FIX-301 V1; TDR-0049 E7 |
| **RR17** Overreach | **Fixed.** Every "thirty skills" says five are proposed under TDR-0049. DAC-0048 says the recheck was the drafter's, and that the agent was of the drafter's model | CHANGELOG, ARCHITECTURE, `skills/packaging/README.md` (twice); DAC-0048 |

## Notes

| | Disposition |
|---|---|
| **RR18** TDR-0050 | **The gloss is corrected**: the banner and the changelog quote ruling R5 instead of "approved in principle", because a misquotation of the owner in a record to be ratified is material. TDR-0050 now asks the owner to confirm that it is the appropriate governing record. **Not changed**: `confidence: high`, and the singleton check's reach to historical candidates only. Both are for the owner |
| **RR19** Partial-span fixture; creation-time ambiguity | **Deferred, and put to the owner** as E9 and E10 in TDR-0048, with the drafter's first question. No fixture is added in this increment |
| **RR20** Terminology drift after 23 November | **Deferred.** `validate-decision-record` still says `status: proposed` "on anything a skill produced". Correcting it changes a canonical skill, which needs its own authorisation, and the owner's ruling of 23 November authorised only the change it named. Recorded for the owner |
| **RR21** Rulings 1 to 4 only in the decision vocabulary | **Deferred.** Another language's recovery is unconstrained by them until a record says otherwise. Recorded as a known limitation of the doctrine |
| **RR22** Changelog version; scope | **The version is fixed**: the changelog says the umbrella specification moves to 1.2.0, in two steps. The scope point stands as the reviewer left it: the branch also carries engineering controls, the experimental package, packaging and tooling, which belong to the release candidate rather than to these records |

## The drafter's five questions

All five are open and go to the owner with the ratification package: partial dates and consideration
(E9); the operations note (E6); scheme authentication (E5); `taxonomy_version` 1.0.0, which the
records do not answer; and V1's `committed_by` (E7).

## What the independent confirmation and the readability review added

- **The confirmation of 26 November met the RR3 case.** For one candidate, the adopter used the broader
  reading, recording an instrument named in the Company Secretary's advice as authority for an act
  that did not cite it. It also found that the broader reading cannot show its own condition in a
  candidate, because `considered` is allowed only on context roles. Both are cited in E1.
- **The confirmation's other findings on the records** go to the owner with the ratification package
  rather than into these corrections, because each would change the vocabulary. They are: no evidence
  kind fits an organisation's own decision log; no `non-decision` kind fits "not yet decided"; the
  not-a-decision reasons have no place for a body noting another's decision; and no form exists for a
  joint owner.
- **The readability review's findings** are on the public documentation, not on these records, and are
  answered separately.
