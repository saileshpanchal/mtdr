# Stage 4 — challenge-record, then challenge-decision-record

Run on 2026-11-26 by the same AI agent that drafted the candidates. That is a weakness: the challenger is not independent of the drafter. Recommendations are this stage's output only. They are not written into any candidate and are not review events.

Method: every rendered value in each view walked back to contribution, fragment and locator; each span read alone; tense and modality compared; grouping attacked; gaps checked; contemporaneity recomputed (`stage5-validate/contemporaneity-recomputed.json`); the decision-specific challenges 1–13 applied.

## HC-001 — Vantry award (OIC, 9 April 2026)

Findings, most serious first:

1. **`HC-001-C16` (consequence) says more than the act-record.** The minute says "approved the award … as recommended". "Five-year" and £690,000 come from Paper 4. Marked `inferred`, medium/medium. What would resolve it: the signed contract, or a minute stating term and value.
2. **Three interpreted values carry the interpreter's remarks about absence** (`C03` "names no individual", `C18` "noting, not approving … not mentioned", `C20` "not supported … not carried"). `record-contribution.md` says absence is not a contribution. The remarks are true of the spans but belong in `unresolved`, where they also are. Left as written; not corrected.
3. **`C06`/`C07` alternatives are "as presented", not "as rejected by the Committee".** The minute records no discussion of options A or C. The matrix allows cited material to support alternatives "as presented to the decision"; epistemic set to medium.
4. **Whether the dated paper is the version tabled is not shown.** The minute cites "Paper 4"; the paper's heading matches. Nothing more.
5. **Corroboration of the condition (`C18`) is later material.** It can show the approval occurred and was reported. It is carried as corroboration only; whether the condition was met is in `unresolved`.
6. Owner: honestly missing. Not a finding against the candidate.
7. Authority: none contributed; applicability reported separately (FND-33). Checked that no scheme fragment is in the candidate.
8. Grouping: one act. No split or merge.

Shared judgement: **fit to propose**, as an incomplete candidate. Recommendation: **incomplete** — `accountable-owner` missing.

## HC-002 — Kestrel transfer and reserve release (Board, 21 May 2026)

1. **`HC-002-C11` brings OIC material into the candidate on temporal continuity.** Its fragments are kind `unlinked`, `considered: unknown`, and the value says "Circumstance". A stricter reading would leave it outside the candidate as circumstance only. What would resolve it: the Board paper (Paper 7) or a minute showing the OIC discussion was reported.
2. **A second possible act inside the same minute item** ("It was agreed that agency cover would be kept on hand"). Carried as context (`C10`). A split would be defensible. In `unresolved`.
3. **`C08` savings figure**: stated plainly, nothing behind it. Extraction high, epistemic low.
4. **`C01`/`C05` write "120,000 GBP" where the source says "£120,000".** A rewriting of a stated value, not an inference; the fragment is verbatim.
5. Owner missing; authority missing; alternatives missing. Honest gaps.
6. One motion, one abstention: kept as one composite candidate, each resolution with its own span (`F04-7-RES-A`, `-B`) and consequence contribution.

Shared judgement: **fit to propose**, as an incomplete candidate. Recommendation: **incomplete** — `accountable-owner` missing.

## HC-003 — transfer date moved (22 July 2026)

1. **`HC-003-C04` (Duncan Faraday as owner) is the weakest claim.** His span is "I think we should move it to 1 October" — a proposal to the Chair. That he "signed it off" is only in the chat of the next day and in the log, neither of which may supply an owner. A reader could hold that the evidence shows Margaret Oyelaran alone agreeing to his proposal. Recorded as a conflict rather than resolved.
2. **`HC-003-C03` (Margaret Oyelaran as owner)** rests on her being the sender of "Agreed, go with 1 October". Sender of the act is not the same as author of a document about it; kept, epistemic medium.
3. **`HC-003-C05` (authority) is a paragraph number, hedged, from the Company Secretary, not from either person who acted.** The act-record cites nothing. The evidence that her email was before Margaret Oyelaran is its addressing (`F06-E3-HDR`, not carried in the candidate) and the echo "logged and goes to September". The contract gives no place to record that link for a non-context role.
4. **Decision date.** 22 July is the date of the agreeing email. If the act is the Chief Executive's alone or complete on 13 July, the date differs. Not resolved; carried in `unresolved` by way of the owner question.
5. **`C14` (lineage) is inferred across spans** and uses the organisation's log references; no record identifier exists.
6. **`F08-015` is marked a restatement of a minute not in the material.** Its content cannot be checked against what it restates.
7. Continuation: not at issue. Currency: later material shows the transfer happened on 1 October; nothing later changes it.

Shared judgement: **fit to propose**, as an incomplete candidate. Recommendation: **incomplete** — `accountable-owner` conflicting.

## HC-004 — Orchard extension (file note, June)

1. **The decision date exceeds what the strictest reading allows.** The act-record has no year. `2026` comes from the decision log, which is a restatement of the note; the evidence matrix lets a restatement support a date only "as its source", and the source gives none. I carried `2026-06` as `inferred`, medium/medium, and said so in `unresolved`. On the strict reading the date is **missing**, `event_time_ref` would be `unknown`, and every context grade would be `indeterminate` (five of six already are). What would resolve it: the Calder letter, or the notebook's dated neighbouring pages recorded as source metadata.
2. **`F08-HEAD` is annotated as a restatement of `F05-AGREED`.** A log heading does not restate a file note. The kind was chosen so the heading shares the row's kind. Weak.
3. **Owner (`C03`)** rests on the note's heading plus "Within my limit". "P. Nandakumar" is as written; first name and post are from other documents and are not in the value.
4. **`C05` (alternative)** is a price comparison, not a recorded rejection. Epistemic low.
5. **Context held, not rendered.** Five context contributions grade `indeterminate` because the note has no based time. Not forced either way.
6. **Verbal agreement.** The decision-statement preserves "Verbally agreed. Letter to follow". Whether a binding commitment existed on that day is not evidenced beyond the note.
7. Persistence: Orchard "remains live" past 30 September is reported as a persistence finding (FND-38) with continuation authority evidenced by this act; not read as a decision.

Shared judgement: **fit to propose**, as an incomplete candidate. Recommendation: **incomplete** — `decision-date`, `context` and `accountable-owner` partial.

## Across the set

- Extraction and epistemic confidences differ on 33 of 64 contributions.
- No split or merge is recommended, so stage 2 was not re-run.
- Nothing was routed to the assurance skills: no reversal-cost evidence exists to show any candidate is a one-way door, and this stage does not run them.
- `evidence-review` was not applied dimension by dimension. Dimensions with no contribution are shown as missing in the views, not as "not material".
