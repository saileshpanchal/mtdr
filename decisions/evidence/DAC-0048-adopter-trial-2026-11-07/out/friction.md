# Friction log — first adopter run of `recover-decision-records`

Interpreter: `adopter-trial` v1 · run date 2026-11-07 · 13 runs (CASE-018 … CASE-029, brackwell).
Read: the entry skill, its five stage skills and the four shared stage skills they specialise,
`historical-recovery.md`, `historical-candidate.md`, `decision-contribution.md` and its schema,
`semantic-roles.md`, `admission.md`, `schemas/shared/*`, and the specifications those cite
(`source-fragment.md`, `record-contribution.md`, `candidate-assembly.md`, `temporal-semantics.md`,
`uncertainty.md`, `identity-and-grouping.md`, `candidacy-and-ratification.md`, `provenance.md`,
`tdr.md` §§3–7, `decision-grammar.md`, `decision-identification`, the decision `package.yaml`, TDR-0049).
Not opened: anything under `tests/`, `records/*/fixtures/`, `records/decision/examples/`. I also did
not open the top-level `conformance/FIX-00x` files: nothing I was following cites them, and their names
(e.g. "value commitment across six sources") suggest they may hold answers for material like Brackwell.

Each entry: **where** · **what was hard** · **what I did** · **why**. Severity: **H** (changes outputs or
could not be applied as written), **M** (needed a convention the standard does not supply), **L**
(wording or friction only).

---

## Top five

1. **[H] Same-day context in the act-record can never be contemporaneous.** Every Cabinet and
   programme-board context contribution in Brackwell grades `indeterminate` under the literal rule.
   (§3.6)
2. **[H] Proportionality cannot be applied as written, yet admission criterion 6 requires its outcome.**
   No source in 13 runs has a `reversal-cost` span. (§5.1)
3. **[H] The evidence kinds do not fit the material.** Undated material fits no kind; `considered:
   unknown` has no kind; and whether a note recording a quiet default is an `act-record` or a
   `retrospective` decides whether a candidate exists at all, with no guidance. (§3.3, §3.4, §6.3)
4. **[H] Grouping bases do not fit two common cases.** Single-source candidates must cite a basis the
   standard calls inadmissible; unlinked material can enter only on subject match. (§4.1, §4.2)
5. **[H] The trial material is case files that *describe* documents.** Provenance, time basis and the
   "summary of other material" refusal all bend, and one reading of "recorded metadata" had to be
   chosen and held across all 13 runs. (§1.1, §1.3)

Next most significant: the forum routed to `authority` by one file and `context` by another (§2.1); the
`context`/`evidence-*` loophole (§2.2); findings have no interchange form (§2.3).

---

## 1. Material, provenance and time basis

### 1.1 [H] What is the "source" when the supplied material is a case file describing documents?
**Where:** `source-fragment.md` (Fields: `source_ref`, `source_hash`, `locator`; "The locator
resolves"); `identify-record-contributions` §"When to refuse" ("The material is a summary of other
material. Prefer the original.").
**Hard:** each `CASE-0nn.md` names several documents (a minute, a paper, a memo) by path, and either
quotes them (blockquotes) or summarises them in the case file's own words ("the board agreed a single
repairs line, as set out in paper B/19/07"). The document paths cannot be opened. The refusal says
*prefer* the original, under a heading called *When to refuse* — so it is unclear whether summarised
items must be refused or used.
**Did:** `source_ref` = the case file actually supplied (`sources/CASE-020.md`); `source_hash` =
`sha256:` of the file bytes; locator `kind: char-offset` with `[start, end)` into the decoded file, plus
`line_start`/`line_end`, the item letter and the document path or title the case file gives. Used
summarised items (no original exists to prefer) and lowered `epistemic_confidence` to `medium` on
contributions resting on a summary, with a note in `unresolved`.
**Why:** a locator must resolve against something I hold; the inner paths resolve nothing. Refusing
every summarised item would have emptied CASE-020, -022, -026, -028 and -029 of their minutes. The
standard needs to say whether "prefer the original" is a refusal or a confidence matter.

### 1.2 [M] Is markdown markup inside a verbatim span part of the content?
**Where:** `source-fragment.md` "not normalised beyond character encoding".
**Hard:** quoted spans wrap across lines with `> ` prefixes and `**bold**` item labels.
**Did:** content is the exact substring of the file, markup and newlines included, so a validator can
check `text[start:end] == content`.
**Why:** any stripping is normalisation. The standard should say whether presentation markup counts.

### 1.3 [H] What counts as a time's "basis" when all I hold is a description of the document?
**Where:** `historical-recovery.md` "A time has a basis, or it is `unknown`"; identify-decision
"Times at their precision, each with a basis".
**Hard:** the basis is "the fragment's own statement … or its source's recorded metadata", and
"a folder, a filename or a neighbouring document" is not. The case files carry dates in five forms:
inside a filename (`board/2021-05-12-minute.md`), inside a folder (`operations/2019-Q1/`), in the item
label ("Board minute, 2019-03-14"), as stated metadata ("dated 2021-04-28", "file created 2023-09-18",
"recording started 6 February 2024"), and in the quoted text ("Meeting of 14/3/19").
**Did (one rule, applied to all 13 runs):** a date in the item's label, a stated "dated / created /
recording started", or a date in the document's own text is a basis; a date that appears only inside a
path or folder name is not; "undated" or "no date … and none in the metadata" is `unknown`.
Consequences: CASE-018 and CASE-024 decision dates `unknown` (filename only); CASE-020/-026/-029
2019-03-14 (label); CASE-023 2019-03-14 (text); CASE-029's working note and CASE-027's notes `unknown`.
**Why:** it is the only reading under which the filename/folder prohibition means anything. But the
distinction between a case file's label "Board minute, 2019-03-14" and a filename
"2021-05-12-minute.md" is thin, and an adopter with real metadata would face the same question about
document-management fields. The standard should give examples of what "recorded metadata" is.

### 1.4 [M] A minute's capture time and creation time.
**Where:** `historical-recovery.md` "Four times"; `historical-candidate.md` fragment annotations.
**Hard:** a minute is dated for its meeting (capture) but its write-up date (creation) is almost never
stated; the standard's example of `later-recording` is a transcript, but minutes are usually written up
later too.
**Did:** minutes and notes: `capture_time` = the meeting date, `creation_time` = `unknown`. Papers and
notes "dated X": capture = creation = X. CASE-021's transcript: capture 2023-09-04 (recording start),
creation 2023-09-18 (file created).
**Why:** a meeting date is evidence of capture, not of production. Nothing breaks, because capture
governs the grade; but the standard does not say this, and adopters will differ.

### 1.5 [M] Two time fields that can disagree, and one cannot hold a partial date.
**Where:** `source-fragment.schema.json` `source_time` (pattern `YYYY-MM-DD…` or `unknown`) vs the
candidate's `capture_time` / `creation_time` (partial dates allowed); `challenge-record` step 6
("Compare each context contribution's `source_time` against the decision date").
**Hard:** `source_time` cannot carry `2022-03`, and the shared challenge step compares `source_time`,
while the decision challenge recomputes from the annotations. Two places for one fact.
**Did:** set `source_time` only where a full-day date has a basis; omitted it otherwise (it is
optional). Computed contemporaneity only from the annotations.
**Why:** writing `unknown` for a known month would be false; inventing a day is the completed date.
The shared step 6 should point at the annotations for historical material.

### 1.6 [M] A date range in one span.
**Where:** CASE-022 items B–D ("Three emails, 2022-11-07 to 2022-11-09"); annotation time pattern.
**Hard:** one span describes three emails by a range; a time field holds one value.
**Did:** one fragment (splitting would be the reconstructed fragment), times `2022-11`.
**Why:** the month is the only single value the range fits. It makes the emails' own grade
`indeterminate` (November 2022 is not wholly before 2022-11-10) when the range is wholly before. No harm
here because they are restatements, but the format cannot express an interval it needs.

### 1.7 [L] Reformatting a date makes it `inferred`.
**Where:** `historical-recovery.md` "Inference is bounded" ("a date written in another format").
**Did:** `derivation: inferred` for "14/3/19", "4 September 2023", "6 February 2024", "18 February 2026",
"12 May 2026"; `explicit` where the source wrote ISO.
**Why:** that is the letter of the rule; but it means almost every recovered date in prose material is
"inferred", which dilutes the marker for the inferences that matter. A "normalised" value, or a rule that
format conversion stays `explicit`, would carry more information.

## 2. Vocabulary and roles

### 2.1 [H] A forum: `authority` or `context`?
**Where:** `semantic-roles.md` "a forum is not an owner. A contribution proposing a committee is a
contribution to `context`"; `decision-contribution.md` class `authority` = "the body, delegation or
instrument under which it was taken … tightens toward `lineage-derived-from` where it is a recorded
decision; otherwise it qualifies `owner`".
**Hard:** the two files route the same span ("the board agreed") to different places. `authority` has no
tightened role when it is not a recorded decision ("qualifies owner" names no field). Filing the forum as
`context` would also force a `considered` annotation and a contemporaneity grade onto "the board", which
is not "what was known at the time".
**Did:** forum named in the act-record → `semantic_role: authority` (class name, untightened),
`derivation: explicit`; owner reported missing. Where the minute names no body (CASE-029 "the single
repairs line agreed"; CASE-021 forum only in a path) no authority contribution.
**Why:** the recovery vocabulary is the more specific and later text, and the semantic-roles sentence
is about a committee *proposed as owner*. The two files should be reconciled.

### 2.2 [M] `context` vs `evidence-*`: only one of them is time-checked.
**Where:** `decision-contribution.md` classes `context` and `evidence`; "Roles recovery treats
specially" (only `context` is a context role); `admission.md` criterion 2.
**Hard:** a paper's figures are both "what was known" and "material considered". Only a `context`
contribution is graded for contemporaneity and annotated `considered`; the same span filed as
`evidence-business` escapes both. That is a hindsight loophole.
**Did:** filed facts from papers and memos as `context` throughout; used no `evidence-*` role.
**Why:** to keep every pre-decision fact under the contemporaneity test. The context-role set should
probably include the `evidence-*` roles.

### 2.3 [M] Where does a not-a-decision reason or non-decision kind go?
**Where:** identify-decision "Output: … RecordContributions … each carrying a class … as its
`semantic_role`"; `decision-contribution.schema.json` (a separate `{taxonomy_version, class, reason |
non_decision}` object); `record-contribution.schema.json` (no reason field); reconcile-decision
("not grouped into candidates").
**Hard:** a finding is a `RecordContribution` whose `semantic_role` is the class, but the reason has no
field; the vocabulary schema validates an object that nothing embeds; the candidate cannot hold
findings. So findings have no interchange form at all beyond a report.
**Did:** findings appear in each report by fragment id, locator and verbatim span, with the
classification object `{taxonomy_version, class, reason|non_decision}`; every one was validated against
`decision-contribution.schema.json` in my builder.
**Why:** it is the only machine-checkable form the published files give. A findings structure (or a
`reason` slot) is missing.

### 2.4 [M] Which class name, which tightened role, in a handed-on candidate?
**Where:** `decision-contribution.md` ("takes a class name where field-level assignment is premature,
and tightens … when drafting maps the evidence"); entry skill stage 6 (candidates hold what the stages
produced).
**Did:** tightened where a role exists (`decision-statement`, `decision-date`, `accountable-owner`,
`alternative-rejected`, `option-foreclosed`, `consequence`, `context`); class name where none does
(`authority`, `corroboration`, `challenge`). `not-a-decision`/`non-decision` never enter a candidate.
**Why:** the draft stage runs before stop, so tightening has happened. The never-inferred list mixes
role names and class names, so either spelling is checked; good.

### 2.5 [M] A role named in place of a person, and "oversee".
**Where:** identify-decision "The owner is named in the material, or missing"; CASE-023 "The ops
director to oversee".
**Did:** no owner contribution; the role is reported in `unresolved` with the organisation chart set
aside.
**Why:** no individual is named, mapping role to person would be inference on a never-inferred role, and
the chart's year is filename-only. The vocabulary has no place for "a role, not a person, was named" —
it ends up as free text.

### 2.6 [M] "I'll own the phasing" — ownership of part of the decision.
**Where:** CASE-025; `semantic-roles.md` accountable-owner.
**Did:** `accountable-owner: Dev Anand`, explicit, `epistemic: medium`, with the scope question in
`unresolved`.
**Why:** the span names an individual accepting ownership in the meeting; whether "the phasing" is the
whole decision is a reading the attester must settle. The standard is silent on partial ownership.

### 2.7 [M] A restatement that is not-a-decision but is also the only evidence of a decision.
**Where:** `decision-contribution.md` (`restatement` reason vs evidence kind — "different questions,
answered separately"); CASE-027 item 4.
**Did:** classified `not-a-decision: restatement`; raised no candidate for the board's May decision it
restates; reported it as an unknown (the attester would need the board's May minute).
**Why:** the reason and the evidence kind are said to be separate questions but the standard does not
say what to do when the restated decision is not otherwise in the material. A restatement alone would
give a candidate with no act-record and a date of "May" with no year.

## 3. Times and contemporaneity

### 3.1 [M] The event time is a pointer, but how to read the pointed-at value is not specified.
**Where:** `historical-candidate.md` `event_time_ref`.
**Did:** `decision-date` `interpreted_value` is the date string at its precision (`2019-03-14`), so a
reader can parse it.
**Why:** nothing says the value must be machine-readable; a value like "14 March 2019" would satisfy
the schema and defeat recomputation.

### 3.2 [M] Multi-fragment context contributions have no defined grade.
**Where:** `historical-recovery.md` "Contemporaneity is computed" (grades "a contribution", from "its
material").
**Hard:** CASE-022's context contribution rests on the paper (contemporaneous) and on the emails that
restate it (indeterminate at month precision). The rule grades one capture time per contribution.
**Did:** computed and reported the literal grade per fragment. Where I needed one grade for a
contribution I treated a restatement as its source when the source is also referenced (my convention,
labelled as mine in the reports).
**Why:** "independence counts once" points that way, but the computation should say it.

### 3.3 [H] Undated material fits no evidence kind.
**Where:** `historical-recovery.md` evidence kinds; `historical-candidate.schema.json` (`evidence_kind`
required, closed enum).
**Hard:** CASE-029's working note has no date at all. `prior-unlinked` asserts that it pre-dates the
event; `retrospective` that it post-dates it. Neither is evidenced, and a required enum forces one.
**Did:** `prior-unlinked` with `considered: unknown`, both times `unknown`; the forced choice stated in
`unresolved`. The computed grade is `indeterminate` either way.
**Why:** `prior-unlinked` is the only kind that lets the note be *reported* as indeterminate context,
which `admission.md` criterion 2 requires; `retrospective` would bar it entirely on an unproven claim.
An `undated` kind (or making the kind derive from the times) would fix it.

### 3.4 [H] Evidence kinds and `considered` states do not map.
**Where:** matrix in `decision-contribution.md` (cited-material ↔ `considered: evidenced`;
prior-unlinked ↔ `considered: unlinked`); `considered: unknown`.
**Hard:** `unknown` has no evidence kind, so every `considered: unknown` contribution carries a kind
that contradicts it.
**Did:** as 3.3.
**Why:** the two classifications overlap without being orthogonal; either derive one from the other or
say they are independent.

### 3.5 [M] Transcript or act-record?
**Where:** `act-record` vs `later-recording`.
**Hard:** CASE-025's transcript states when recording started but not when the transcript was made.
`later-recording` asserts later production.
**Did:** `act-record` where production is not shown to be later (CASE-025), `later-recording` where it is
(CASE-021). The matrix treats both alike for every claim, so only the label differs.
**Why:** not to assert a production time I cannot evidence.

### 3.6 [H] Same-day context in the act-record computes `indeterminate`. **(Top 1)**
**Where:** `historical-recovery.md` "Contemporaneity is computed": "Each time is read as the interval its
precision allows"; "`contemporaneous` when the capture time ends at or before the event time begins".
**Hard:** a minute's own context ("Members noted the scheme affects collection rounds in four wards";
"Highways works at Calder Road (CP-118) are running behind") is captured on the meeting day, and the
event is the meeting day. Read as whole-day intervals, the capture ends at the end of the day and the
event begins at its start, so the grade is `indeterminate`, never `contemporaneous`. Under criterion 2 it
"cannot be presented as contemporaneous context" — the best context there is (what the deciders noted
in the act itself) is barred, while a paper dated a day earlier passes.
**Did:** applied the literal reading (the challenge skill calls forcing a grade "the backdating attack"),
reported each such contribution in `unresolved`, and showed in the reports the grade an alternative
reading (same-day capture "ends at" the event) would give, labelled as not the spec's.
**Why:** I would rather surface the defect than repair it in my outputs. The rule needs an exception for
context recorded in the act-record itself, or a statement that the act-record's own content is
contemporaneous by construction.

## 4. Grouping

### 4.1 [H] Single-source candidates must cite an inadmissible basis.
**Where:** `candidate-assembly.schema.json` (`grouping_basis` `minItems: 1`, closed enum);
`admission.md` criterion 4 ("where the candidate draws on more than one source");
`candidate-assembly.md` ("same document … not admissible on its own").
**Hard:** a decision, its date and its owner read from one minute entry are grouped because they are in
one document — the basis the standard rules out — and the enum has nothing else.
**Did:** `explicit-cross-reference`, with evidence that names the single act-record and the in-document
structure relied on (the heading dates the entry; the entry records the agreement and names the owner).
**Why:** the schema forced a value; I made the evidence honest so a reader can see the label is a
formality. The enum needs a "single act-record" basis, or the schema should follow criterion 4.

### 4.2 [H] Unlinked material enters only by subject match.
**Where:** `historical-recovery.md` `considered: unlinked`; identify-decision "A memo that existed before
the meeting is `considered: unlinked`"; `identity-and-grouping.md` "Semantic similarity is the weakest
signal"; `candidate-assembly.md` (similarity not admissible on its own).
**Hard:** the `unlinked` state exists for material nothing connects to the act — so by definition it has
no cross-reference, lineage or owner basis. It can join a candidate only by `entity-match` on the
decision's subject, which is close to the similarity the standard excludes.
**Did:** CASE-020's memo and CASE-029's note, and SRC-03 for one Brackwell candidate, joined on
`entity-match` naming the shared subject; assembly confidence lowered to `medium`; stated in
`unresolved` that the grouping is subject matter only.
**Why:** the standard plainly expects unlinked memos to be annotated `considered: unlinked`, which
requires them to be in a candidate. Say so, and say what basis they join on.

### 4.3 [M] One assembly confidence for a mixed assembly.
**Where:** `candidate-assembly.schema.json` `assembly_confidence`.
**Did:** the confidence of the weakest member (`medium` where an unlinked memo joined a `high` core).
**Why:** there is no per-contribution membership grade, so a strong core and a weak attachment share one
value; the reason is in `unresolved`.

## 5. Drafting, challenge, report

### 5.1 [H] Proportionality has nothing to work on, but its outcome is an admission criterion. **(Top 2)**
**Where:** `draft-tdr` step 2 ("on the `reversal-cost` contributions"); `admission.md` criterion 6
("The proportionality outcome is stated … with the reversal-cost reasoning behind it").
**Hard:** none of the 13 runs contains a span about reversal cost. Choosing a tier from the decision's
subject would be reasoning the evidence does not contain; failing criterion 6 would make every candidate
inadmissible, contradicting "Admissible but incomplete — the normal case".
**Did:** stated the outcome as **undetermined — no `reversal-cost` contribution** for every candidate and
treated that statement as meeting criterion 6.
**Why:** it is the only outcome the evidence supports. The standard should say what a recovery does when
reversal cost is silent (which it nearly always will be).

### 5.2 [M] `incomplete` vs `retain`.
**Where:** challenge-decision "Dispositions"; "What is never a finding: A missing owner, date or
alternative honestly reported".
**Hard:** a missing owner is "never a finding", yet `incomplete` is the recommendation for an
under-evidenced candidate, and `retain` means fit to put before a person — which an admissible incomplete
candidate also is.
**Did:** `retain` only where all four mandatory roles are supported; `incomplete` where any is missing or
partial. One candidate in thirteen runs is `retain`.
**Why:** the two recommendations need a stated boundary.

### 5.3 [M] The report has no slot for what stages 3–5 produce.
**Where:** entry skill "The report" ("Nothing else"); draft-tdr outputs (completeness view, tier);
admission; validate (pass/fail per check).
**Did:** carried, inside each candidate's entry: completeness view with derivation alongside, the
reading of what the evidence did not supply, admissibility per criterion, the proportionality outcome,
the challenge's findings and recommendation, and validation results labelled schema/structural.
**Why:** dropping them would hide stages that ran; "nothing else" is about judgement and handover.

### 5.4 [M] No TDR drafts, so challenge and validate run against the candidate, not a draft.
**Where:** entry skill stages 3–5; validate-decision checks 1, 7, 8 (TDR schema, recovered TDR opening,
rendered values).
**Did:** ran the challenge on the candidates' contributions; marked TDR-schema checks "not applicable —
no draft rendered (by instruction)".
**Why:** the brief said not to draft TDRs. The skills assume a draft exists.

### 5.5 [L] `restates` points at what?
**Where:** `historical-candidate.md` "`restates` where the fragment repeats another source"; schema
"The source this fragment repeats".
**Did:** the `fragment_id` of the restated fragment inside the same candidate; my validator checks it
resolves.
**Why:** "source" could mean `source_ref`, which is the same case file for every fragment here; a
fragment id is the only value that identifies what is repeated. No integrity rule covers it.

### 5.6 [M] `considered: evidenced` for the act-record's own context is circular.
**Where:** `historical-candidate.md` integrity 5 ("`evidenced` carries at least one fragment showing the
link").
**Hard:** "Members noted the scheme affects collection rounds in four wards" is itself the proof that
the members had it; the only fragment showing the link is the context fragment.
**Did:** `evidenced`, with the context fragment as its own link.
**Why:** it is true, and the schema needs a fragment. But the standard frames `considered` around
*other* material (a paper before a meeting), and says nothing about context stated in the act itself.

### 5.7 [L] `source_hash` algorithm and format unspecified; fragments not referenced by a claim.
**Where:** `source-fragment.md`; `historical-candidate.md` ("the `SourceFragment`s every claim rests
on").
**Did:** `sha256:<hex>` (matching the digest convention). Each candidate carries only the fragments
its contributions reference; spans examined and not used are listed in the reports by line and offset.
**Why:** there is no integrity rule either way. The identify contract asks for "one fragment annotation
per fragment", but annotations exist only inside candidates, so a fragment that seeds no candidate (a
finding, a set-aside span) has nowhere to carry its times or evidence kind.

### 5.8 [L] Explanation has nowhere to go.
**Where:** `historical-candidate.md` "No rationale, explanation, summary or notes".
**Did:** kept `interpreted_value` to what the span says (I removed explanatory clauses I had first
written into it); every reason a grade or omission was made sits in `assembly.unresolved` or the report.
**Why:** the closure is right, but `unresolved` then carries notes that are not questions. A stranger
will find the reasons only in the report.

## 6. Brackwell (multi-source run)

### 6.1 [M] Three resolutions, one vote: split or not?
**Where:** reconcile-decision "One question per candidate"; `tdr.md` §3 ("a distinct accountable
judgement can be accepted, rejected, changed or superseded independently"); `candidate-assembly.md`
("same meeting" not a basis).
**Hard:** Cabinet carried resolutions 1–3 as one recommendation on one vote. The independence test says
split; the single vote says one act; and grouping the shared context, date and authority into each of
three candidates leans on "same meeting/document", which is not a basis.
**Did:** three candidates (brackwell-2, -3, -4), each repeating the item's date, authority and context
contributions under new ids; the merge reading stated in each `unresolved`. The programme itself
(depots and fleet) was not split, because Cabinet approved it as one thing.
**Why:** the independence test is the only stated criterion. The challenge stage's split/merge
recommendation then had nothing to route back, because I made the split at reconciliation.

### 6.2 [M] Is an instrument's statement of its own adoption a decision?
**Where:** `decision-identification` step 1 ("a policy adopted"); identify-decision "Authority is a
reference … contributes the instrument".
**Hard:** SRC-01 is the scheme of delegation itself, headed "adopted 2025-04-01". One skill makes it a
decision moment; the other treats an instrument as what an authority contribution points at. Nothing
says whether the instrument is the act-record of its own adoption.
**Did:** raised brackwell-1 (adoption, date supported, owner and context missing). Contributed none of
its paragraphs as authority elsewhere, because nothing cites it. Stated the other reading in
`unresolved`.
**Why:** both grammar lines can be filled from the span. An adopter could equally reasonably raise no
candidate.

### 6.3 [H] The quiet default: one skill says decision, the matrix may say no candidate. **(Top 3)**
**Where:** `decision-identification` step 1 ("an incident workaround that silently became the way
things work"); `tdr.md` §3 ("Execution events are evidence … unless a further judgement was actually
exercised"); the matrix (`retrospective` supports occurrence only).
**Hard:** SRC-06 is the only evidence of the Northgate arrangement that stayed. It reports earlier acts
(the temporary set-up; the maintenance schedule) and a present stance ("we have not scheduled a move").
If it is `retrospective` there is no candidate; if `act-record` there is one with no date and no owner.
The quiet default the identification skill most wants found is exactly the case the matrix is least
able to support, because by its nature it has no act-record.
**Did:** `act-record` (the only record of the choice, written by those making it), with the alternative
reading in `unresolved`, decision-statement graded `partial`.
**Why:** classifying it `retrospective` would silently drop a commitment through FY28 that nobody is
shown to have decided, which is the finding recovery exists for. The standard should say how a quiet
default is evidenced.

### 6.4 [M] Material for another package.
**Where:** entry skill (decision language only); `identify-record-contributions` step 3 ("one fragment
may contribute to several objects").
**Hard:** SRC-03 and SRC-04 are mostly value-commitment material (baseline, target, falsifying signal,
beneficiaries, reconcile-by), including a value-language conflict (31 March 2028 vs 31 March 2027). A
decision run has no slot to hand them to a value run.
**Did:** listed them under "found and not used", with the conflict named and marked as value-language.
**Why:** that is the only report section that fits. A cross-package hand-off is missing.

### 6.5 [M] An assurance act on a claim fits no class.
**Where:** `decision-contribution.md` classes; the `unclassified` outcome.
**Hard:** "Counter-signed for financial purposes: R. Adeyemi, Section 151 Officer, 6 March 2026" is a
named individual's personal act under a control (SRC-01 §5.2/5.4), but it is not a decision, an owner,
authority for a decision in the material, evidence considered, or corroboration.
**Did:** reported as `unclassified`, with what was recognised and why each class failed.
**Why:** this is what the outcome is for; the vocabulary invites a superseding decision if it recurs.

### 6.6 [M] A delegation that fits perfectly but is never cited.
**Where:** identify-decision "Authority is a reference"; never-inferred `authority`.
**Hard:** SRC-01 §3.2 reserves to Cabinet commitments affecting more than one ward; Cabinet's minute
notes four wards. §3.3 makes the Director the committing officer within an approved programme; the
programme board is chaired by the Director. Every fit is close, and none is a reference. The
questions the scheme raises (was the Northgate decision within delegation?) have no home except free
text in `unresolved`.
**Did:** no authority contribution from SRC-01 anywhere; the questions put in `unresolved` as what an
attester must settle.
**Why:** the rule is clear and right. But the standard gives no structured place for "authority
question raised by an instrument in the material", so the most consequential governance question in
the run is a sentence.

### 6.7 [M] Later material that diverges from a decision but never mentions it.
**Where:** class `challenge` ("evidence contradicting or questioning the decision").
**Hard:** SRC-06 shows rounds operating out of a depot the programme board retained "for vehicle
storage". It is a challenge in substance, but it does not refer to the board's decision, so attaching it
would be grouping on subject matter.
**Did:** not contributed as `challenge`; recorded as a tension in both candidates' `unresolved` and in
"What remains conflicting".
**Why:** start from separate. The class needs a rule on whether a challenge must refer to the decision.

### 6.8 [L] No named individual anywhere in a council's decisions.
**Where:** `semantic-roles.md` "`accountable-owner` must be a named individual"; admission "Admissible
but incomplete — the normal case".
**Did:** owner missing on all six Brackwell candidates.
**Why:** this is the rule working. But for bodies that decide collectively by design (a Cabinet), it
means no recovered decision can ever be complete. Readers of the report should know that this
reflects the rule, not a defect in the council's records.

### 6.9 [L] Where the binding consequence goes.
**Where:** `semantic-roles.md` ("`decision-statement` needs both a choice and a binding consequence");
role `consequence`.
**Did:** where the consequence is in the same words as the choice ("will not commit … until"), it stays
in `decision-statement`, with an `option-foreclosed` alongside; where it is a separate sentence
("Northgate has been included … on that basis"), it is a `consequence` contribution.
**Why:** the two roles overlap, and the admission test reads "This means" from contributions without
saying which.

### 6.10 [L] Stage 5 has no portable tool outside `tests/`.
**Where:** `validate-decision-record` (checks described in prose); the package's suite lives under
`tests/`, which this trial could not open or run.
**Did:** wrote my own validator (`validate.py`, preserved beside this log): the candidate schema with
`schemas/shared/` as a `referencing` registry, the five integrity rules, the event-time pointer, the
`considered` coverage, never-inferred roles, provenance reproduction from the real files, and
contemporaneity recomputed. All 17 candidates pass; a deliberately broken candidate fails seven checks.
**Why:** "recompute; never trust a stored judgement" needs a recomputation. An adopter without the
repository's tests has to build one.

## What worked without friction

- Loading `schemas/shared/` as a registry by `$id`, exactly as `historical-candidate.md` says,
  resolved every sibling `$ref` first time.
- The closed candidate schema caught nothing I wrote, but made the boundary obvious: no notes, no
  disposition, no stored grade.
- The not-a-decision reasons and non-decision kinds (CASE-027, CASE-028, Brackwell SRC-04/05) were
  unambiguous to apply, and the machine-readable vocabulary validated every classification.
- The matrix decided the retrospective cases (CASE-018 item C, CASE-024 item B) cleanly: corroborate
  occurrence, explain nothing.
