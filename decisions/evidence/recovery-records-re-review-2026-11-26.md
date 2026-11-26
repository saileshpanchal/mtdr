# Targeted re-review of the corrected recovery records at `240b4d0` — 26 November 2026

Evidence for the maintainer's decision on DAC-0048, TDR-0048, TDR-0049 and TDR-0050. **It is not
ratification evidence, and it makes no ratification recommendation.** It is the one targeted re-review
asked for, by the reviewer of [the first review](recovery-records-review-2026-11-26.md), of the
corrections made in `240b4d0907a9f445b867a3320654791c4d9e3c92` in answer to it.

| | |
|---|---|
| Commit reviewed | `240b4d0907a9f445b867a3320654791c4d9e3c92`, against `57d68c0` |
| Reviewer | An AI agent, Claude Sonnet 5.5, the reviewer of the first review. Not a person, and not the author of the corrections |
| Asked | Whether RR1 to RR3 are closed; whether any semantic change was introduced unlabelled; whether each response says what the commit does; and what the corrections broke |
| Result | **RR2 and RR3 closed; RR1 partly closed · 0 new blocking · 1 new should-fix (B1) · 3 unlabelled semantic changes (U1 to U3), none blocking** |

What was done after it is recorded in [the responses](recovery-records-review-2026-11-26-responses.md#after-the-re-review-of-240b4d0),
and was not reviewed again.

**Everything below the line is the reviewer's report, verbatim as delivered.**

---

# Targeted re-review: recovery records at 240b4d0

- **Commit reviewed:** `240b4d0907a9f445b867a3320654791c4d9e3c92` (against `57d68c0`)
- **Reviewer:** Claude Sonnet 5.5 (`claude-sonnet-5-5`). **An AI reviewer, not a person.** I did not write the corrections.
- **Date:** 2026-11-26
- **Method:** `git diff 57d68c0 240b4d0` over the named paths; the commit extracted into the scratchpad. `tests/verify.py` ran there and returned structural, semantic and relational pass, with transition-eligibility indeterminate (release-gated). I checked every relative link and anchor in the four records, the changed fixtures and the changed specifications; none dangles.
- The maintainer's response file was treated as a claim to check, not as evidence.
- No ratification recommendation is made.

## 1. The three blockers

| | Closed? | Evidence |
|---|---|---|
| **RR1** unlabelled extensions | **Partly** | The register E1 to E13 exists: E1 to E8 in `TDR-0049:120-166`, E9 to E12 in `TDR-0048:280-297`, E13 in `TDR-0050:77-81`. It is cross-referenced in italics from `decision-contribution.md:122-125,151-152,167-169,191`, `historical-recovery.md:68-69,119-122`, `admission.md` (criteria 2 and 6), FIX-031 to FIX-034 and FIX-301. Every item I flagged in the first review is now in it. The residual gaps are in section 2 (U1 to U3). |
| **RR2** "identity check repaired" | **Yes** | The word "repaired" no longer appears in the four records. `TDR-0048:77-82`, `:230-234` and `DAC-0048` (*Uncertainty* and *Declared interactions*) now say the check is as released in v1.30.0, that `0650856` is held out, and that Alternative 3 needs that decision first. This matches `57d68c0` and `evidence/identity-check-0650856-evaluation-2026-11-26.md:7-10`. |
| **RR3** invocation defined two ways | **Yes** | One definition, the act's own citation, runs through every place I found. `decision-contribution.md:32` ("the act cites it"); `:94` and `:111` (`cited-material` authority is "only the instrument the act itself cites"); `:122` and `:135` (a paper before whoever acted that names the instrument is applicability evidence only); the schema `invocation_roles` description (`decision-contribution.schema.json:217`); `FIX-520:7-9`. It now agrees with `TDR-0049:79-80`, both recovery skills and FIX-031. A grep for "or in material shown to have been before" finds only the E1 text that records the old reading. **Residual, disclosed:** the suite still enforces only "not `unlinked`/`retrospective`" (`recovery.py:99-102`, unchanged). The narrower rule rests on challenge, and the DAC says so (Re-assessment, R1). |

## 2. Semantic changes in 57d68c0..240b4d0

**Changes that alter meaning or acceptance, and their labels**

| Change | Where | Label | Accurate? |
|---|---|---|---|
| Invocation narrowed to the act's own citation. Pre-decision material that names an instrument becomes applicability evidence. | `decision-contribution.md:32,94,111,122,135-139`; schema `:217`; FIX-520 | E1, "the assistant's resolution", with the owner's question and the 26 November confirmation case | **Yes.** The old broad text was the drafter's and the narrow text was TDR-0049's, so "resolution of two readings" is fair. See U1. |
| FIX-301 D2: applicability finding withdrawn. The authority question goes to `unresolved`, and D2's authority is missing. | `FIX-301:52-62` and the must-not | E3, "the assistant's correction" | **Yes.** SRC-05 states no ward count (checked), and the text matches v1.30.0's "recorded, not adjudicated". |
| Admission criterion 6: "undetermined" limited to historical candidates. Every other candidate states a tier or no record "as before". | `admission.md` criterion 6 | E8, "the drafter's, limited… by the assistant", with owner's question | **Label yes, but the correction is incomplete. See B1.** |
| Admission criterion 2 applied to every candidate | `admission.md` criterion 2 | E12 (new in `TDR-0048:295-297`) | **Yes.** |
| Capture time as a fourth time; partial-date span; creation-time rule | `historical-recovery.md:68-69,119-122` | E11, E9, E10 | **Yes.** E10 states only that the text is silent and the code does not lift. |
| FIX-301 SRC-06 and the FY28 reversal | `FIX-301`, `FIX-034`, spec `:191` | E6, quoting v1.30.0's accepted answer | **Yes.** The quotation matches v1.30.0 verbatim. |
| Authentication and effect self-certifying | FIX-033, spec | E5 and the DAC debt row. Not mitigated; the owner chooses. | **Yes.** |
| FIX-301 V1 `committed_by` left as v1.30.0 had it | `FIX-301` V1 | E7, "the assistant's statement of scope" | **Yes.** |
| What establishes a single act | spec, FIX-032 | E4 | **Yes.** |
| Applicability test | spec, FIX-031, FIX-301 D1 | E2 | **Yes.** |
| Singleton entry-not-document | `TDR-0050:77-81` | E13 | **Yes.** |

**Not in the register, or inaccurately labelled**

- **U1 (minor).** `decision-contribution.md:135-139` adds an obligation, "evidence for the applicability finding, **and the finding says so**", that is not in E1, E2 or the schema.
- **U2 (minor).** `TDR-0050:83-91` says the record "is therefore decided before TDR-0048, or with it". That is a constraint on the order, labelled neither as the drafter's nor as an owner's question. The DAC (*The order of acceptance*) does put the choice to the owner.
- **U3 (design choice).** The new classes `applicability` and `persistence` are *findings*, "reported by fragment, never grouped" (`decision-contribution.md:46-50`), and `continuation_authority` is a closed `evidenced`/`not-evidenced` pair. The return said only "record separately" and "record as observed behaviour". The finding form is the drafter's and is in no E item. It was already present at 57d68c0, and I did not list it then.

## 3. RR4 to RR17 and RR22

| | Response claims | Commit does so? |
|---|---|---|
| RR4 | DAC re-assessed, ruling by ruling | **Yes.** `assessed_at: 2026-11-26`; *Re-assessment* section present. |
| RR5 | Put to the owner (E5), not changed | **Yes.** DAC says "Not mitigated"; debt row added; FIX-033 note. |
| RR6 | 23 November ruling preserved | **Yes.** `evidence/TDR-0048-owner-ruling-2026-11-23.md` says its only source is the commit message and asks for the owner's confirmation. The TDR-0048 quotation matches it. TDR-0049 decision 7 names the candidate view. |
| RR7 | A1 to A6 / R1 to R5 | **Yes.** No stray "sixth ruling", "six rulings" or "ruling 5". |
| RR8 | TDR-0050 lists what relies on it | **Yes.** `TDR-0050:83-98`; Alternative 3 reworded. |
| RR9 | Debt rows and order clarified | **Yes.** DAC debt rows and *The order of acceptance*. |
| RR10 | "If this record is returned" lists | **Yes**, in three records. The TDR-0049 list says `draft-tdr` is reverted for "the undetermined outcome". See B1. |
| RR11 | Criterion 6 narrowed | **Partly.** `admission.md` is narrowed, but `draft-tdr` is not. See B1. |
| RR12 | D2 corrected | **Yes** (E3). |
| RR13 | FY28 labelled | **Yes** (E6). |
| RR14 | 16 versus 17 | **Yes.** DAC, the trial README and the "five wrong answers" (`brackwell-1`, `-2` to `-4`, `-6`) are accurate. `brackwell-1` is the scheme-adoption candidate (checked). |
| RR15 | Gates reworded | **Yes.** All three frontmatter lines read "confirm only when… 2027-05-07 is the review date; reaching it confirms nothing". TDR-0049's gate names "an adopter who is not the drafter over material the drafter did not write". |
| RR16 | V1 scoped | **Yes** (E7). |
| RR17 | "Thirty skills" qualified | **Yes.** `ARCHITECTURE.md:41`, `skills/packaging/README.md:76,104` and `CHANGELOG.md:30` say five are proposed. The DAC says the recheck was the drafter's and the agent was of the drafter's model. |
| RR22 | Changelog says 1.2.0 | **Yes** (`CHANGELOG.md:32`). |

## 4. Anything the corrections broke

**B1 (should-fix; the one new inconsistency of substance). `draft-tdr` still states the unscoped "undetermined" rule.**
- `records/decision/skills/draft-tdr/SKILL.md:40` (and the canonical copy) says: "With no `reversal-cost` contribution at all, the outcome is **undetermined**… (admission.md criterion 6)". It is not limited to historical candidates.
- Criterion 6 now says undetermined applies "for a historical candidate only", and E8 promises that "every other candidate's admission" is as in v1.30.0.
- The skill was left unchanged. The response and the E8 label therefore overstate the correction, and the skill and the criterion contradict each other.
- `TDR-0049` "If this record is returned" lists `draft-tdr` for revert, so the text is known to be edited but is not scoped.

**Smaller points (notes)**
- The TDR-0049 banner calls the four rulings "authority-bearing"; R2 (composite acts) is not obviously so.
- The 26 November confirmation, cited in E1 and the DAC debt row 5, is evidenced only by a hash commitment (`DAC-0048-confirmation-2026-11-26-commitment.json`). Its content is "held by the maintainer", so the E1 example ("4.5 covers a change of date") cannot be checked from the repository.
- The confirmation's four other findings (no evidence kind for an organisation's own log, no non-decision kind for "not yet decided", and so on) are recorded only in the responses file, not in any record's register. This is not an error, since no change was made.
- `TDR-0048:89` still says "five amendments and six rulings", beside the "first/second/third amendment" labels in its Alternatives. These are two sets and the text keeps them apart, but readers must follow both.
- Owner quotations: all quotations in the corrected records match the return. R5 in TDR-0050, "Approve an explicit singleton grouping basis" and "Amend shared grouping semantics through the appropriate governing TDR, with regression fixtures", is exact. The R1 phrase "never invent an authority contribution" in E1 is exact. The same-day correction's "event, source creation and interpretation" in `historical-recovery.md:68` is exact. The 23 November quotation matches its preserved note.
- Mismatch to the return's order: none. The DAC states the order the owner fixed and puts only the TDR-0050 sequencing and the interval to the owner.

## 5. Not checked

- I did not re-run the contemporaneity known answers beyond the suite's own pass.
- I did not read the unpublished confirmation evidence.
- I did not re-read the whole of the unchanged fixtures and skills. I read only `draft-tdr`, `validate-decision-record` and the identify and challenge skills for the invocation and "undetermined" wording.
- I did not review `1a2d0e5` and `a446323` beyond confirming they do not touch the four records.

## Counts

- **New blocking:** 0.
- **New should-fix:** 1 (B1).
- **Unlabelled semantic changes:** 3 (U1, U2, U3), none blocking.
