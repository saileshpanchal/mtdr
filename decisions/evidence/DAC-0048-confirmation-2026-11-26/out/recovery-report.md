# Recovery report — Tarnmere Homes, nine documents

One report for the whole run, as `recover-decision-records` specifies. Run on 2026-11-26 by an AI agent (Claude, model claude-fable-5-2) executing the installed `mtdr-decision` package at commit 57d68c0. All five stages ran, in order. No review event was produced. Nothing here has standing.

## Candidates

Four historical candidates, each `status: candidate`, `standing: none`, `retrospective: true`. JSON in `candidates/`, candidate views in `stage3-draft/`, challenge in `stage4-challenge/challenge.md`.

| Candidate | What | Event time | Owner as evidenced | Authority invoked | Completeness (statement · context · date · owner) | Recommendation |
|---|---|---|---|---|---|---|
| HC-001 | OIC approved the award to Vantry Systems Ltd "as recommended", subject to the Company Secretary being satisfied with the exit and data return clauses | 2026-04-09 | missing (a forum: the Operations & Investment Committee) | missing | supported · supported · supported · missing | incomplete |
| HC-002 | Board resolved to transfer repairs call handling to the Kestrel Customer Hub from 1 September 2026 and to release £120,000 from the planned maintenance reserve; one abstention | 2026-05-21 | missing (a forum: the Board of Management) | missing | supported · supported · supported · missing | incomplete |
| HC-003 | Kestrel go-live moved to 1 October; agency cover kept going until then | 2026-07-22 | conflicting: Margaret Oyelaran / Duncan Faraday | "4.5", a paragraph number given with a hedge; instrument not named | supported · supported · supported · conflicting | incomplete |
| HC-004 | Six-month extension of the Orchard licence from 1 October, about £48k plus about £3k, verbally agreed with Calder | 2026-06 (inferred; the note has no year) | partial: "P. Nandakumar" | missing (a limit is stated; no instrument is named) | supported · partial · partial · partial | incomplete |

Proportionality tier: undetermined for all four. No span states a reversal cost.

Provenance: every contribution names its fragments; every fragment carries source, SHA-256 of the source as read, a char-offset locator and the verbatim text. The reference validator re-read all fragments against the sources (`validation/summary.md`).

## What remains unknown

What an attester would have to find:

- **HC-001:** the individual who held the decision. The contract's term and total value as approved (the minute gives neither). Whether the condition was discharged for the *data return* clauses, and the report to Tobias Wren due 30 April. Who signed the contract and when. Answers to the members' questions on migration and on Vantry being sold or failing. Reversal cost.
- **HC-002:** the individual who held the decision. Paper 7. Any alternative considered. Whether the agreement on agency cover was a separate act. Reversal cost.
- **HC-003:** which individual held the decision. The instrument that "4.5" refers to, as cited by those who acted. The Board minute of 17 September 2026. Who was to pay for the extended agency cover. Reversal cost.
- **HC-004:** the year, from the act-record or its metadata. The day of the agreement. The Calder letter and its terms, including whether data export tools stay licensed. Confirmation of budget. Reversal cost.

Absence of evidence is not evidence of absence.

## What remains conflicting

- **HC-003, accountable owner.** Two named individuals. Settled by: evidence from the time of who held the decision, or of how the two acted "jointly".
- **Who approved the Vantry contract.** Act-record: the Committee approved; the Board "noted". Status report (later): "The Board-approved Vantry contract". The later description is not carried. Settled by: nothing further is needed for the candidate; the status report is wrong on the evidence supplied, or refers to something not supplied.
- **Who agreed 1 October.** Act-record: Chair and Chief Executive by email; the Board "noted" it on 17 September per the log. Status report: "on 1 October as agreed by the Board". Not carried. Settled by: the 17 September minute.
- **Scope of the Vantry condition.** Minute: "exit and data return clauses". Decision log and open action: "exit clauses". Board minute: "exit clauses had been improved". Settled by: the Company Secretary's report under the 30 April action.
- **Interface count** at different dates (27 on 9 April; 29 of 31 at 30 September and in October) is a sequence, not a conflict.

## What is not a decision

38 findings in `stage1-identify/findings.json`, each with its fragment(s) and a classification object. By stable identifier:

**`not-a-decision` — `status-update` (13):** FND-02 void dashboard live · FND-18 to FND-22 the five open-action rows · FND-23 contract "signed in late May" · FND-24 migration test 2 · FND-27 interfaces 29 of 31 · FND-28 service transferred 1 October · FND-29 agency cover finished 2 October · FND-30 first two weeks' performance · FND-31 transition spend.

**`not-a-decision` — `action` (7):** FND-03 Alison Reddy to review the contract · FND-04 Ngozi Eze to finish interface scoping · FND-06 Helen Strudwick to take the paper to the Board · FND-09 Helen Strudwick to run consultation and report · FND-10 the file note's to-do list · FND-11 "go ahead and extend" the agency booking (commits about £7k a month; funding left open; classification disputable) · FND-12 check the leaflet date.

**`not-a-decision` — `preference` (4):** FND-05 OIC "supportive in principle" of the Kestrel idea · FND-07 Paper 4's recommendation · FND-25 project team "now believe 15 February 2027 is more realistic" · FND-26 a further Orchard extension "would be a bigger conversation".

**`not-a-decision` — `restatement` (6):** FND-08 Board "noted" the OIC's Vantry approval · FND-13 Board "noted DL-26-014" · FND-14 to FND-17 decision log rows DL-26-011 to -014.

**`not-a-decision` — `operational-routine` (1):** FND-01 previous minutes agreed as a correct record.

**Evidence that no decision was made — `non-decision`, kind `deferred` (1):** FND-32 OIC risk register, "Deferred to June".

Three further spans say in terms that no decision has been made and fit none of the three kinds; they are under *unclassified* below.

## What applied, and what persisted

Applicability — an instrument's terms cover an act that does not cite it. Not a judgement of competence.

| Finding | Instrument | Concerns | Body that acted is the body named? | Not shown |
|---|---|---|---|---|
| FND-33 | Scheme of Delegation 4.2 (OIC: contracts over £250,000 and up to £1,000,000) | HC-001 | yes — OIC | the contract's "total value" (6.1); aggregation advice (6.2); Paper 4 shows £690,000, a £235,000 call-off and a programme total of £1,015,000; 4.1 reserves over £1,000,000 to the Board |
| FND-34 | 4.1 (Board: change to repairs service model altering tenant contact) | HC-002 | yes — Board | — |
| FND-35 | 4.1 (Board: virement from a reserve) | HC-002 | yes — Board | that a "release" is a "virement" |
| FND-36 | 4.5 (Chair and Chief Executive jointly, where the next meeting is too late) | HC-003 | yes — the two post-holders, per the 21 May minute | that changing a date the Board had resolved is an approval the Board "would otherwise" give. Invocation is also evidenced, by paragraph number |
| FND-37 | 4.4 (Finance Director: extensions up to 12 months and £150,000 where budget exists; report to next OIC) | HC-004 | yes — if "P. Nandakumar" is the Priya Nandakumar the OIC minute names as Finance Director | that budget exists; the report to the OIC (open at 30 September 2026) |

Persistence:

| Finding | Arrangement | Authority for continuation |
|---|---|---|
| FND-38 | Orchard "remains live" in October 2026, past the 30 September 2026 licence end | evidenced — the extension recovered as HC-004 (a note of a verbal agreement; the letter is not supplied) |

## Retrospective material set aside

| Material | Corroborates | Not allowed to explain |
|---|---|---|
| Board minute 21 May, item 6 (for HC-001) | that the approval occurred and was reported; that the Company Secretary said she was content with exit clauses | the approval's context, reasons or owner |
| Decision log, as at 30 Sept 2026 (all four) | nothing independent — rows restate their named sources | owner ("Taken by" column), authority ("Para 4.5"), or reasons. It was allowed to supply the year for HC-004's date, flagged as the weakest value in the set |
| Chat headed "Thu 23 July" (HC-003) | that the change was treated as settled the next day | that Duncan Faraday "signed it off" as owner |
| Status report for 14 Oct 2026 (HC-001, -002, -003, -004) | contract signed "late May"; transfer on 1 October; £86,000 of £120,000 spent; Calder extended to end of March 2027 | "Board-approved"; "as agreed by the Board"; and first-two-weeks performance, which is outcome knowledge and is in no candidate's context |

## What was unclassified, and what was found and not used

Unclassified (`stage1-identify/unclassified.json`):

- **UNC-01** Kestrel–Vantry interface quote: "No decision has been taken." Open question; none of deferred / not-reached / withdrawn.
- **UNC-02** "Decisions needed" list in the status report.
- **UNC-03** Redeployment destinations: "not decided".
- **UNC-04** The Scheme of Delegation as a record of its own adoption ("Version 3, adopted by the Board January 2025"). Contemporaneity: stated to the month; the material is an extract. Authentication: not evidenced. Effect: evidenced by later citation of paragraph 4.5. No candidate. A January 2025 Board minute would establish the rest.

Found and not used: scheme paragraphs 4.3, 6.1, 6.2, 6.3 and the first 4.1 bullet (quoted in finding notes only); email headers of Helen Strudwick's and Alison Reddy's emails; the status report heading; Paper 4's authors and purpose lines; the apologies, AOB and next-meeting lines of both minutes; the last chat lines on desk space beyond UNC-03.

## Coverage

| Source | Read | Fragments taken | Used in |
|---|---|---|---|
| SRC-01 scheme of delegation (extract) | all | 12 | findings FND-33 to -37; UNC-04 |
| SRC-02 OIC Paper 4 | all | 11 | HC-001, HC-004 (one circumstance), FND-07, FND-33, FND-38 |
| SRC-03 OIC minutes 9 April | all | 15 | HC-001, HC-002 (one circumstance), FND-01 to -06, FND-32 |
| SRC-04 Board minutes 21 May (extract; items 1–5 and 8 "not reproduced") | all supplied | 13 | HC-002, HC-001 (corroboration), FND-08, -09, -34, -35 |
| SRC-05 file note | all | 8 | HC-004, FND-10, FND-37 |
| SRC-06 email thread | all | 12 | HC-003, FND-36 |
| SRC-07 chat transcript | all | 5 | HC-003 (corroboration), FND-11, -12, UNC-03 |
| SRC-08 decision log (extract) | all | 11 | corroboration in all four; FND-13 to -22 |
| SRC-09 project status report | all | 13 | corroboration in all four; FND-23 to -31, -38; UNC-01, -02 |

Material the sources cite that was not supplied: Board Paper 7; Board minutes of 17 September 2026; the Calder letter; the Vantry contract; OIC minutes of 11 June; the consultation outcome letters.
