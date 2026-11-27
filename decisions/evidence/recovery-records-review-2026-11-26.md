# Independent review of the recovery records at `57d68c0` — 26 November 2026

Evidence for the maintainer's decision on DAC-0048, TDR-0048, TDR-0049 and TDR-0050. **It is not
ratification evidence, and it makes no ratification recommendation.**

| | |
|---|---|
| Commit reviewed | `57d68c00406f2260b832be0fc8c14a0ddbc9d692` (`release/next-candidate`) |
| Reviewer | An AI agent, Claude Sonnet 5.5. Not a person. Not the drafter of the records, whose commits are co-authored with Claude Opus 5.5 |
| Given | The repository at the commit; the maintainer's return of 7 November; and the five questions the drafter flagged in draft pull request 12, quoted to it because they are not in the repository |
| Result | **3 blocking for ratification · 14 should-fix before ratification · 5 notes** |

The maintainer's assistant re-checked RR1, RR2, RR3 and RR22 against the commit before filing this,
and they hold. RR2 arises from the assistant's own revert of `0650856` in that commit.

**Everything below the line is the reviewer's report, verbatim as delivered.** Nothing is
corrected, reordered or summarised. Line numbers refer to the files at `57d68c0`.

---

# Independent review: DAC-0048, TDR-0048, TDR-0049, TDR-0050

- **Commit:** `57d68c00406f2260b832be0fc8c14a0ddbc9d692` (`release/next-candidate`)
- **Reviewer model:** Claude Sonnet 5.5 (`claude-sonnet-5-5`)
- **Date:** 2026-11-26
- **AI reviewer, not a person.** I did not write the records. This is evidence for the owner's decision, not a ratification recommendation.
- **Method:** I read files at the commit by extracting it into the scratchpad. I diffed against `v1.30.0` and ran `tests/verify.py` in that extraction. The run ended with structural, semantic and relational passing and transition-eligibility indeterminate (release-gated). I did not capture its exit code.
- **Line numbers** refer to the committed files.

## 1. Ruling by ruling

| Ruling | Status | Where | Notes |
|---|---|---|---|
| 1. Authority by fit | **Applied with drafter extension**, and internally inconsistent (RR3, RR12) | `records/decision/specification/decision-contribution.md:32,43,94,111,124-140`; `TDR-0049:68-74`; `FIX-031`; `FIX-301:40-45`; `historical-candidate.md:83-85`; `mtdr_validation/recovery.py:99-102` | The recovery specs carry it. DAC-0048 and TDR-0048 carry no text on it. |
| 2. Three resolutions, one vote | **Applied with drafter extension** | `decision-contribution.md:142-153`; `TDR-0049:75-77`; `FIX-032`; `FIX-301:34-39`; reconcile skill `:100-107` | Extensions: "one signature, one approval", "different people or at different times", and "what establishes a single act is the record of the act". |
| 3. Scheme adoption | **Applied with drafter extension** | `decision-contribution.md:155-172`; `TDR-0049:78-80`; `FIX-033`; `FIX-301:73-79` | The drafter defines what counts as authentication and effect (RR5). |
| 4. Persistence | **Applied with drafter extension** | `decision-contribution.md:174-186`; `TDR-0049:81-83`; `FIX-034`; `FIX-301:58-71`; schema `continuation_authority` | The FY28 treatment goes beyond the ruling and reverses a prior accepted answer (RR13). |
| 5. Singleton grouping | **Applied**; the definition (entry, not document) is the drafter's | `TDR-0050`; `candidate-assembly.md:42-56` (v1.1.0); `candidate-assembly.schema.json:58-64`; `FIX-522/523`; `FIX-004`; `recovery.py:68-73` | It is a new TDR with `supersedes: none`, and no governing TDR is named (RR18). |
| Same-day correction | **Applied with drafter extension** | `historical-recovery.md:68-74,87-123`; `TDR-0048:123-128`; DAC constraint 3 `:253-257`; `FIX-030`; `FIX-519`; `verify.py:627-643`; `recovery.py:134-155` | Extensions: partial dates that span the event, the creation-time rules, and the capture time as a fourth time. |

- **Not applied or contradicted:** I found no ruling wholly "not applied". The only contradiction is the two definitions of invocation (RR3).
- **Rulings 1 to 4 in DAC-0048 and TDR-0048:** neither record mentions them (RR4).
- **Labelling:** none of the extensions is labelled as the drafter's anywhere in the repository (RR1).
- **Extra amendment:** TDR-0048 also carries a 23 November amendment that is outside the return (RR6).

## 2. 16 versus 17

**Seventeen is established from evidence.**
- `out/` holds 17 `*.hdc.json` files: eleven for the cases and six for Brackwell. CASE-027 produced none.
- `sha256sum -c SHA256SUMS` passes.
- `check-output.txt` reads "17 of 17".
- `friction.md:470` reads "All 17".

**Why "sixteen" was reported is not evidenced.**
- DAC-0048 `:47-51` and the trial README `:38-40` call it "an arithmetic slip in one sentence".
- The sentence is quoted only in the README. The agent's report is not preserved in the evidence directory.
- "One run, one report, one set of files" is the drafter's assertion.
- The pin moved during the run, and the README `:20` says which version of two files the agent read "is **not established**". The owner's "different trial stages" reading is excluded by assertion, not by artefact (RR14).

## 3. Findings

### Blocking for ratification

**RR1. The owner's labelling condition is not met anywhere in the repository.**
- Evidence: the return (`:70-74`) says an amendment that applies a ruling to a case it did not name "says so".
- A grep of the four records, the specs, skills, fixtures, tests, CHANGELOG and return finds no marking. "Drafter" appears only in a DAC debt row and in the return itself.
- Unlabelled extensions:
  - invocation by "material shown to have been before whoever acted" (`decision-contribution.md:32,129-131`)
  - the D2 applicability mismatch (`FIX-301:52-57`)
  - "one signature, one approval" and "different people or times" (`:144-153`)
  - the authentication and effect tests, including "by citation" (`:164-168`)
  - the FY28 treatment (`FIX-034`, `FIX-301:68-71`)
  - the partial-date span and the creation-time rules (`historical-recovery.md:91,102-110`)
  - the "undetermined" proportionality outcome
- The drafter's flagged questions exist only in the draft pull request body, which is not in the repository.
- Why it matters: the owner cannot ratify content "named" under TDR-0027 while the ruling-versus-drafter line is outside the record.

**RR2. The records state that the identity check "is repaired", and the tip reverts that repair.**
- Evidence: DAC-0048 `:41-42` ("the identity check that would have blocked one is repaired") and `:131` ("the repaired identity check").
- TDR-0048 `:70-71` and `:217-219` ("has been repaired, so the option stays open").
- Commit `57d68c0` reverts `0650856`: "The repair is left for a governed decision." `tests/verify.py` and `record-identity.md` return to v1.30.0.
- The return accepted the "identity-check repair" only "subject to successful CI and clean-clone verification" (`:52`).
- Why it matters: Alternative 3's stated reason rests on a premise the tree contradicts, and ratifying would attest it.

**RR3. "Invocation" is defined two ways, which is the core of ruling 1.**
- The broad reading is in `decision-contribution.md:32` ("cited in the act, **or in material shown to have been before whoever acted**"), `:129-131`, and matrix `:111` ("◐ where it names the instrument").
- The narrow reading is in `TDR-0049:70-71` ("the act cites the instrument") and `identify-decision-contributions/SKILL.md:46-49` ("An instrument the act does not cite … is an `applicability` finding"). `challenge-decision-record/SKILL.md:35-37` and `FIX-031` read the same way.
- Under the skill, a tabled paper that names the scheme yields an applicability finding. Under the specification, it yields an authority contribution.
- The validator (`recovery.py:99-102`) enforces only the broad rule, refusing `unlinked` or `retrospective` kinds.
- Why it matters: ruling 1 turns on this line ("does not prove the decision-maker relied on it"), and the owner cannot ratify two statements of it.

### Should-fix before ratification

**RR4. DAC-0048 was not re-assessed for the content that followed it.**
- Its banner (`:21-23`) covers only the same-day correction, the count, and the debt.
- It has no text on adoption, applicability, persistence or composite acts. Yet `:19` says "authority and delegation are its subject", and the fraud lens (`:33`) names "manufactured authority".
- Ruling 3 (an instrument as its own adoption) opens a self-certification surface that the adversarial projection (`:137-155`) does not assess.
- `assessed_at` is 2026-11-07, and the 23 November TDR-0048 amendment is not mentioned.
- TDR-0049 (`template: minimal`) decides the four authority-bearing rulings with no assurance case of its own.
- Why it matters: the owner ratifies DAC-0048 first, and its assurance predates the semantic content it assures.

**RR5. Authentication and effect can be self-certified.**
- Spec `:164-168` accepts "a signature or seal… register entry" and "a commencement provision that has passed".
- FIX-033 `:13-14` treats a typed "Signed: … Register entry SO-22" line inside the instrument as authentication (`:29-33`).
- Brackwell SRC-01 fails only because its header gives a date and nothing else (`FIX-301:73-79`).
- Why it matters: the pass/fail line is whether the instrument asserts its own signatures, so a forged extract passes. This is the DAC's own named exploit.

**RR6. The 23 November amendment to TDR-0048 is unevidenced and outside the return.**
- TDR-0048 `:29-33` quotes an owner ruling ("Render recovered candidates as candidate views…") and "the 20 and 22 November engine runs".
- No file in `decisions/evidence/` preserves that ruling or those runs.
- The only record is commit `4aa7d5f`'s message. The CHANGELOG does not mention it.
- DAC-0048 and TDR-0049 are not updated: TDR-0049 `:86-88` still says `draft-tdr` "states when a draft was recovered".
- Why it matters: the 7 November act was preserved as evidence, and this one was not.

**RR7. "Ruling" and "ruling 5" name different things.**
- TDR-0048 uses "five amendments and six rulings" (`:76-78`), "The six rulings" (`:113`), and "the owner's sixth ruling" (`:217`). Its ruling 5 is contemporaneity.
- The return's ruling 5 is singleton grouping, cited as "ruling 5" in TDR-0050 `:18-21`.
- TDR-0049 uses "the owner's four rulings".
- The 6 to 7 November review is not preserved in the repository.
- Why it matters: a ratifier reading "ruling 5" cannot tell which act is meant.

**RR8. TDR-0050 is not independent of TDR-0048, though the return asks for it to stand on its own merits.**
- `historical-candidate.md:90-91` (TDR-0048's text) has integrity rule 8 on `singleton`.
- `recovery.py:68-73` enforces that rule. FIX-522/523 test it.
- The schema enum (`candidate-assembly.schema.json:58-64`) and the shared reconcile skill (`skills/shared/reconcile-record-fragments/SKILL.md:24`) already list `singleton`, while `candidate-assembly.md:43-44` says "admissible once it is ratified".
- FIX-004, an accepted fixture, now requires `singleton` (`FIX-004:40-43`).
- Why it matters: rejecting TDR-0050 alone leaves dangling references across TDR-0048's text, the schema, a shared skill and an accepted fixture.

**RR9. The ratification order has a gap and an inverted debt.**
- DAC-0048 debt row 1 (`:224`) and row 2 (`:225`) are due "with TDR-0049, **before this case is accepted**". The return puts DAC-0048 first and TDR-0049 last.
- `historical-recovery.md:80-85,151-153` requires "every package states a matrix". TDR-0048 would be normative before any decision-language instance exists.
- `package.yaml:59-64` lists the two proposed specs as `class: normative` dependencies.
- Why it matters: it is unclear whether acceptance of TDR-0049 is a precondition of ratifying DAC-0048.

**RR10. Existing normative Decision and Value text was edited in place ahead of acceptance (question 5).**
- **Unchanged (verified against v1.30.0):** `tdr.md`, `dac.md`, both schemas, the templates, `records/value/`, and `record-identity.md`. No existing TDR, DAC or VR validates differently.
- **Changed in place:**
  - `admission.md` criteria 2 and 6
  - `semantic-roles.md`
  - `draft-tdr`: `status: proposed` is no longer "always"
  - `decision-identification`: "Retro-mining" is renamed
  - shared skills used by Value (`identify-record-contributions`, `challenge-record`, `reconcile-record-fragments`)
  - `candidate-assembly` 1.1.0 and its schema enum
  - `contribution-model` 1.1.0
  - `FIX-004`
  - `FIX-301` (the adoption acceptance case)
  - `package.yaml` (`lifecycle`, `orchestration`, normative dependencies)
- Why it matters: if any record is returned, these edits remain unless someone reverts them by hand.

**RR11. Admission criterion 6 was relaxed, against the doctrine's own foreclosure.**
- `admission.md:26-29`: "undetermined… satisfies this criterion". It is not scoped to recovered material.
- TDR-0048 `:244` and `historical-recovery.md:206-207` say "Admission criteria are never relaxed to raise the rate at which candidates become records".
- The change comes from trial friction item H2.
- Why it matters: a change to an admission criterion sits beside a rule against such changes, with no stated reason it is not one.

**RR12. FIX-301's D2 applicability finding is not supported by an act span.**
- The test (`decision-contribution.md:132-136`) is a span of the instrument and a span of the act that brings it within the instrument's terms.
- D1 has the minute's "four wards". SRC-05 says only that Northgate is "retained for vehicle storage" and states no ward count.
- FIX-301 `:52-57` asserts a "footprint change across more than one ward" and a "mismatch", which comes close to competence while claiming not to.
- Why it matters: ruling 1 was extended to D2 without the evidence its own test requires, and the extension is unlabelled.

**RR13. The FY28 treatment reverses a prior accepted answer.**
- The v1.30.0 FIX-301 must-not read: "Report SRC-06 as 'no decision present'. The organisation has committed maintenance budget through FY28; that is a decision whatever the document calls itself."
- Now `FIX-301:68-71`, `FIX-034` and `decision-contribution.md:184-186` say it is "reported, not recovered", and no evidence kind is assigned to the note.
- The return's ruling 4 speaks only to continuation.
- Why it matters: this is a drafter judgement that reverses an accepted answer.

**RR14. The 16 versus 17 reconciliation.**
- Section 2 sets out the evidence; the cause of "sixteen" is asserted, not evidenced.
- The trial's own outputs include candidates that the amended FIX-301 now forbids: `brackwell-2` to `-4` (the split vote) and `brackwell-6` (the permanent arrangement).
- DAC-0048 `:49-51` says "All seventeen meet the suite's own contract" and does not say that four would now be wrong answers. Only the README (`:52-55`) says so, and only about the vote.
- Why it matters: the reconciliation is correct on the count but leaves the cause unverifiable.

**RR15. The confirmation gate is worded more weakly than the return.**
- `TDR-0049:13` (and TDR-0048 `:13`): "confirm when … or 2027-05-07, whichever is sooner", and "material its authors did not write".
- DAC row 5 says "an adopter who is not the drafter, over material the drafter did not write".
- The return says TDR-0049's gate is satisfied "only by a further independent confirmation".
- Why it matters: read literally, the date alternative could satisfy a "confirmation".

**RR16. FIX-301 contradicts itself on whether the scheme had effect.**
- `FIX-301:73-79` holds that nothing shows the scheme "had effect".
- The same file's V1 table (`:93,113`) still derives `committed_by` from SRC-01 §3.3 (cited by no act) and the counter-signature from §5.2.
- Why it matters: the fixture treats one instrument as effective on the Value side and as unproven on the Decision side (question 5).

**RR17. Overreach: statements that present proposed or non-independent material as settled.**
- `CHANGELOG.md:26`, `ARCHITECTURE.md:41`, and `skills/packaging/README.md:49,77` state "thirty skills". Five are proposed under TDR-0049.
- DAC `:49-50` says "rechecked independently of the agent". The check was by the drafter (README `:49`, `:79`).
- The DAC omits that the agent was "of the same model as the drafter" (README `:11`).
- Why it matters: the standard's stated totals and the trial's independence claims run ahead of acceptance.

### Notes

**RR18. TDR-0050.**
- "Approved in principle" (`:18`) is the drafter's gloss. The return says "Approve an explicit singleton grouping basis".
- `confidence: high` (`:9`) sits beside a boundary condition the validator cannot check (`:52-54` of the spec) and a single trial.
- Context (`:24-27`) cites TDR-0018 for "must state at least one admissible grouping basis". No TDR enumerates the bases, so the "appropriate governing TDR" the return named is not identified.
- The `singleton` check runs only on historical candidates, so a non-historical or Value assembly spanning two sources passes unchecked.

**RR19. Partial-span case has no published fixture, and the creation-time rules are ambiguous.**
- The partial-date case appears only as known answers in `verify.py:633-634`, not as a published fixture.
- `historical-recovery.md:103-110` is ambiguous on whether `considered: evidenced` can lift a later creation time. The code (`recovery.py:152`) does not lift it, and the spec says only "indeterminate".

**RR20. Terminology drift after 23 November.**
- "Draft" versus "candidate view" (`draft-tdr` §7, `TDR-0049:87`).
- `validate-decision-record:100-105` says "status: proposed on anything a skill produced", while §7 says a view carries `status: candidate`.

**RR21. Rulings 1 to 4 live only in the decision vocabulary.**
- The doctrine (`historical-recovery.md`, TDR-0048) is silent on them, so another language's recovery is unconstrained.

**RR22. Housekeeping and scope.**
- `CHANGELOG.md:28` says the umbrella specification "moves to 1.1.0". The file says 1.2.0 (`organisational-records.md:3`).
- The branch also carries engineering controls, OIR, packaging and tooling. I did not assess these against "do not broaden the current increment".
- `main` does not contain any of the four records; I checked.

## 4. The drafter's five questions

1. **Partial dates and consideration:** the rule is written (`historical-recovery.md:91,102,107-110,116-117`) and the code applies it. It is unlabelled, and no published fixture covers it. **Owner question:** should evidence that a minute cited a paper close the order for a paper dated only to the month containing the meeting, when that paper may have been finalised after it?
2. **Ops note:** reported but not recovered, in `FIX-034`, `FIX-301:68-71` and `decision-contribution.md:184-186`. No evidence kind is assigned, and it reverses a prior accepted answer (RR13). **Owner question:** is a report that a money commitment "has been included" evidence of a decision to recover, with an unknown date, or only evidence that some commitment occurred?
3. **Scheme authentication:** answered in `FIX-301:73-79`. The normative text says "by citation" but does not say conduct without citation is not effect, and it allows self-asserted signatures (RR5). **Owner question:** may authentication and effect be evidenced by the instrument's own text and by consistent conduct, or only by independent material and acts that cite it?
4. **`taxonomy_version` 1.0.0:** not answered by the records. The schema `const` is `1.0.0` both at `665aa6e` (15 classes) and at the tip (17 classes). TDR-0049 `:104` governs only after acceptance. **Owner question:** does `1.0.0` denote the vocabulary as accepted, with earlier artefacts treated as drafts, or must it move now that two classes were added after the trial?
5. **FIX-301 V1 `committed_by`:** not answered, and unresolved in the file (RR16). The record does not say whether ruling 1 reaches the Value language. **Owner question:** does ruling 1 extend to the Value language's inference of `committed_by` and the counter-signature requirement from instrument terms that the cited act does not cite?

## 5. What I did not check

- I did not read the 17 trial candidates' JSON or the case reports beyond counts.
- I did not read the 23 `tests/recovery/` fixtures in full, nor `historical-candidate.schema.json` and `candidate-review-event.schema.json`.
- I did not independently re-derive the contemporaneity grades beyond reading `recovery.py` and the known answers.
- I did not verify TDR-0050's claim that every assembly valid under 1.0.0 stays valid.
- I did not review the packaging profiles, engineering controls, OIR, CI, or the clean-clone verification the return made a condition of the tooling acceptance.
- I did not see draft pull request 12 or its body.
- I did not verify the pin timestamps (`665aa6e`, `7b2fb20`).
- I did not run the suite under `uv` with the lockfile. I used system Python with the installed `jsonschema` and `yaml`.

## 6. Counts

- **Blocking for ratification:** 3 (RR1 to RR3)
- **Should-fix before ratification:** 14 (RR4 to RR17)
- **Note:** 5 (RR18 to RR22)
- **Total:** 22

I make no ratification recommendation; that is the owner's act.
