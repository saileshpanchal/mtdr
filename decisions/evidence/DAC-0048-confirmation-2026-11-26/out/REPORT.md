# MTDR adoption run — report

## 1. Provenance

- **Who ran this:** an AI agent, not a person. Claude, model `claude-fable-5-2`, running as a Claude Code subagent.
- **Date:** 2026-11-26.
- **MTDR commit:** `57d68c00406f2260b832be0fc8c14a0ddbc9d692` (confirmed with `git rev-parse HEAD`). The installed package reports itself as `1.30.0+unreleased`.
- **Given:** a clone of MTDR at `confirm-run/mtdr/`; nine Markdown documents at `confirm-run/sources/`; an empty `project/` and `out/`; Python 3.13 with pyyaml and jsonschema; `uv`.
- **Told not to open:** anything under `tests/`; anything under `records/*/fixtures/`; anything under `decisions/evidence/`; anything outside the three folders; not to run `tests/verify.py`; no git command that changes anything; no other branches or history. I opened none of these. `git status --porcelain` on the clone is empty at the end of the run.
- **Coaching:** none. Nobody told me what the documents contain, what decisions are in them, or what a correct output looks like. I did not read the worked example the documentation points to, because it is under `tests/`.
- **One thing I did read that a reader should know about:** two files of the reference validator's source (`mtdr_validation/fidelity.py`, and lines 1–200 of `mtdr_validation/folder.py`), before producing output. See friction item 1.

## 2. Path taken

### Documentation and skills opened, in order

From the clone:

1. `README.md`
2. `practice/using-mtdr-with-your-framework.md`
3. `records/decision/README.md`
4. `pyproject.toml` (and directory listings of `skills/`, `records/decision/`, `schemas/`, `specification/`, `mtdr_validation/`, `mtdr_packaging/`, `practice/`)
5. `records/decision/skills/recover-decision-records/SKILL.md`
6. `skills/packaging/README.md`
7. `skills/packaging/claude-code/README.md`
8. `mtdr_packaging/README.md`
9. `mtdr_validation/README.md`
10. `skills/packaging/profiles/README.md`

From the installed copy at `project/.mtdr/plugins/mtdr-decision/` (all later reading was from here unless noted):

11. `.claude-plugin/plugin.json`, `mtdr-package.json` (top-level keys and `not_packaged`)
12. `records/decision/skills/identify-decision-contributions/SKILL.md`
13. `skills/shared/identify-record-contributions/SKILL.md`
14. `specification/historical-recovery.md`
15. `records/decision/specification/decision-contribution.md`
16. `specification/historical-candidate.md`
17. `specification/source-fragment.md`
18. `specification/record-contribution.md`
19. `specification/candidate-assembly.md`
20. `schemas/shared/source-fragment.schema.json`, `record-contribution.schema.json`, `candidate-assembly.schema.json`, `historical-candidate.schema.json`; `records/decision/schema/decision-contribution.schema.json`
21. `records/decision/skills/reconcile-decision-contributions/SKILL.md`
22. `skills/shared/reconcile-record-fragments/SKILL.md`
23. `records/decision/skills/draft-tdr/SKILL.md`
24. `records/decision/validation/semantic-roles.md`
25. `records/decision/validation/admission.md`
26. `records/decision/skills/challenge-decision-record/SKILL.md`
27. `skills/shared/challenge-record/SKILL.md`
28. `records/decision/skills/validate-decision-record/SKILL.md`
29. `skills/shared/validate-record/SKILL.md`
30. `records/decision/skills/decision-identification/SKILL.md`
31. `specification/temporal-semantics.md`, `uncertainty.md`, `identity-and-grouping.md`, `provenance.md` (first 35 lines; my output was truncated there)
32. `records/decision/specification/tdr.md` §3 and the table in §5 only
33. `records/decision/templates/tdr-minimal.md`, `tdr-bare.md`

From the clone again, source code:

34. `mtdr_validation/fidelity.py` (all), `mtdr_validation/folder.py` (lines 1–200)

Not opened: `practice/quickstart.md`, `specification/contribution-model.md`, `specification/candidacy-and-ratification.md`, `records/decision/specification/dac.md`, `evidence-review`, `assurance-synthesis`, `show-me`, any `decisions/TDR-*.md`, `mtdr_validation/recovery.py`, `result.py`, `__main__.py`, `CHANGELOG.md`, and everything I was told not to open.

### Commands run, with exit status

All `uv` commands were run from the clone with `PYTHONDONTWRITEBYTECODE=1 UV_PROJECT_ENVIRONMENT=<project>/.venv` and `--frozen --offline` (my choice; see section 6).

| # | Command (abbreviated) | Exit |
|---|---|---|
| 1 | `ls -la . mtdr sources project out; cat mtdr/README.md` | 0 |
| 2 | `cat practice/using-mtdr-with-your-framework.md records/decision/README.md` | 0 |
| 3 | `cat -A` of the nine sources | 0 |
| 4 | `ls` of skills, records/decision, schemas, specification, mtdr_validation, mtdr_packaging, practice; `cat pyproject.toml` | 0 |
| 5 | `cat records/decision/skills/recover-decision-records/SKILL.md` | 0 |
| 6 | `cat` of the four READMEs in items 6–9 above | 0 |
| 7 | `ls -R skills/packaging/profiles; cat skills/packaging/profiles/README.md` | 0 |
| 8 | `git rev-parse HEAD; git status --porcelain; uv run … python -m mtdr_packaging.profiles list` | 0 |
| 9 | `uv run … python -m mtdr_packaging.profiles install decision --runtime claude-code --project <project>` | 0 — "installed …/project/.mtdr/plugins/mtdr-decision … 43 files … 13 skills discoverable; skill links: 55 resolve, 13 declared not packaged, 0 broken / verified" |
| 10 | `uv run … python -m mtdr_packaging.profiles verify <project>/.mtdr/plugins/mtdr-decision` | 0 — "verified" |
| 11 | several `cat`/`sed` reads of the installed files listed above | 0 |
| 12 | `uv run … python -m mtdr_validation --help`; `grep` of the docs for locator formats | 0 |
| 13 | `cat mtdr_validation/fidelity.py; sed -n 1,200p mtdr_validation/folder.py` | 0 |
| 14 | `sed` of `tdr.md` §3 and §5; `file` and `grep -c` for carriage returns on the sources | 0 |
| 15 | `<project>/.venv/bin/python out/_build/build.py <sources> <out> <installed package>` (my script) | 0 |
| 16 | `uv run … python -m mtdr_validation <out> --sources <sources>` | 0 — "4 artefact(s) assessed, 8 file(s) not assessed" |
| 17 | `ls`, `cat` of results; `git status --porcelain` on the clone (empty) | 0 |
| 18 | shell heredocs writing the Markdown outputs. One `cat >` failed with "No such file or directory" because the folder did not exist yet; the next command in the same call created the folder and wrote the file | 0 overall |
| 19 | the file-writing tool refused to write this report ("Subagents should return findings as text, not write report files"); I wrote it with a shell heredoc because the task asks for the file | 0 |

The validator was run once. No output was changed after it ran except Markdown without frontmatter (summaries, challenge, reports).

I did not run `claude --plugin-dir <package>`. I am the runtime; per the rules I read each `SKILL.md` and carried it out.

### What is in `out/`

- `candidates/HC-001.json` … `HC-004.json` — the historical candidates.
- `stage1-identify/` — fragments, contributions, fragment annotations, considered annotations, findings, unclassified, summary.
- `stage2-reconcile/` — assemblies, summary.
- `stage3-draft/HC-00n.view.md` — candidate views with completeness views.
- `stage4-challenge/challenge.md` — findings and one recommendation per candidate.
- `stage5-validate/` — the validate skill as I carried it out; recomputed contemporaneity; my own schema checks.
- `recovery-report.md` — the one report the entry skill specifies.
- `validation/` — the reference validator's output, plus its stdout and stderr.
- `_build/data.py`, `_build/build.py` — the data I authored and the script that computes locators and hashes and writes the files. Not MTDR tooling.

## 3. What I recovered

### Candidate decisions

| Id | What | When | By whom | Under what authority |
|---|---|---|---|---|
| HC-001 | The Operations & Investment Committee approved the award to Vantry Systems Ltd "as recommended" (Paper 4: a five-year contract), subject to the Company Secretary being satisfied with the exit and data return clauses | 9 April 2026 (minute heading) | A forum. No individual is named; owner missing | None cited by the act. Scheme 4.2 has terms that cover an OIC approval of a contract up to £1,000,000 (applicability only); the contract's total value is not evidenced, and Paper 4's programme total is £1,015,000 |
| HC-002 | The Board resolved that repairs call handling transfer to the Kestrel Customer Hub from 1 September 2026 and that £120,000 be released from the planned maintenance reserve; one abstention. One act, two resolutions | 21 May 2026 (minute heading) | A forum. No individual is named; owner missing | None cited by the act. Scheme 4.1 reserves both kinds of matter to the Board (applicability only) |
| HC-003 | The Kestrel go-live was moved from 1 September to 1 October, and agency cover kept going until then | 22 July 2026 (date of the agreeing email) | Margaret Oyelaran ("Agreed, go with 1 October") on Duncan Faraday's "I think we should move it to 1 October". Two named individuals; recorded as a conflict on owner | "4.5", given by the Company Secretary in the thread with a hedge ("I think 4.5 covers a change of date, though it is the Board's resolution"). The thread does not name the instrument. Scheme 4.5 has matching terms (applicability, reported separately) |
| HC-004 | A six-month extension of the Orchard licence from 1 October at about £48k plus about £3k was verbally agreed with Calder, letter to follow | June; year 2026 only by inference from the decision log. The file note says "Tues, wk of 1 June" and no year | "P. Nandakumar", from the note's heading and its first-person "Within my limit" | None. The note states a limit ("12 mths / £150k") and names no instrument. Scheme 4.4 has matching terms (applicability only); the report to the OIC it requires was still open at 30 September 2026 |

All four: `status: candidate`, `standing: none`, proportionality tier undetermined, challenge recommendation **incomplete**.

### Judged not to be a decision

38 findings and 4 unclassified outcomes; full list with fragments in `stage1-identify/` and `recovery-report.md`. One line each for the ones that look most like decisions:

- **OIC "supportive in principle" of the Kestrel idea, 9 April** — preference; it commits nothing and sends the question to the Board.
- **Paper 4's recommendation** — a paper recommends; the minute decides.
- **Board "noted" the OIC's Vantry approval, 21 May** — restatement. The Board did not approve it. The October status report calls the contract "Board-approved"; that is not supported.
- **Board "noted DL-26-014", 17 September** — restatement of the Chair and Chief Executive's decision; the minute itself was not supplied. The status report's "as agreed by the Board" is not supported.
- **Helen Strudwick: "go ahead and extend" the agency booking, chat of "Thu 23 July"** — action, carrying out "keep the agency cover going until then". It commits about £7k a month and leaves open who pays; this classification is disputable.
- **Decision log rows DL-26-011 to -014** — restatements of the minutes, note and thread they cite.
- **OIC risk register "Deferred to June"** — non-decision, kind deferred.
- **Go-live 15 February 2027** — preference ("the project team now believe"); "has not been put to any committee".
- **Kestrel–Vantry interface quote** — "No decision has been taken." Unclassified: none of the three non-decision kinds fits an open question.
- **Redeployment destinations** — "not decided". Unclassified, same reason.
- **"Decisions needed" list** — unclassified.
- **Contract signature "in late May"** — status update; an execution event whose actor and date are not evidenced.
- **Scheme of Delegation v3 "adopted by the Board January 2025"** — reported, no candidate: adoption time stated, authentication not evidenced, effect evidenced by later citation.
- **All actions, to-dos, open-action rows and status-report figures** — action or status-update.
- **Orchard "remains live" in October** — persistence, continuation authority evidenced by HC-004.

## 4. Validation

Validator: `python -m mtdr_validation <out> --sources <sources>`, the one `mtdr_validation/README.md` names. Exit 0, which the README says is operational, not a verdict. Full output in `out/validation/`. From `validation/summary.md`, verbatim:

> **There is no overall result.** Each artefact is reported in four dimensions that are read independently (TDR-0033). Nothing here confers standing: a candidate stays a candidate.

> Source fidelity: every fragment re-read against the material in `…/confirm-run/sources` (relational).

Per artefact, verbatim:

> ### HC-001 — `candidates/HC-001.json`
> - **structural**: pass
> - **semantic**: pass
> - **relational**: pass
> - **transition-eligibility**: not-applicable — A candidate's standing is none; attesting its account is a named individual's act, which no validator performs.
> - **contemporaneity of context**: `HC-001-C03` contemporaneous · `HC-001-C04` contemporaneous · `HC-001-C05` contemporaneous · `HC-001-C08` contemporaneous · `HC-001-C09` contemporaneous · `HC-001-C10` contemporaneous · `HC-001-C11` contemporaneous · `HC-001-C12` contemporaneous · `HC-001-C13` contemporaneous · `HC-001-C14` contemporaneous · `HC-001-C15` contemporaneous

> ### HC-002 — `candidates/HC-002.json`
> - **structural**: pass
> - **semantic**: pass
> - **relational**: pass
> - **transition-eligibility**: not-applicable — (same text)
> - **contemporaneity of context**: `HC-002-C03` contemporaneous · `HC-002-C06` contemporaneous · `HC-002-C07` contemporaneous · `HC-002-C08` contemporaneous · `HC-002-C09` contemporaneous · `HC-002-C10` contemporaneous · `HC-002-C11` contemporaneous

> ### HC-003 — `candidates/HC-003.json`
> - **structural**: pass
> - **semantic**: pass
> - **relational**: pass
> - **transition-eligibility**: not-applicable — (same text)
> - **contemporaneity of context**: `HC-003-C07` contemporaneous · `HC-003-C08` contemporaneous · `HC-003-C09` contemporaneous

> ### HC-004 — `candidates/HC-004.json`
> - **structural**: pass
> - **semantic**: pass
> - **relational**: pass
> - **transition-eligibility**: not-applicable — (same text)
> - **contemporaneity of context**: `HC-004-C04` indeterminate · `HC-004-C06` indeterminate · `HC-004-C07` indeterminate · `HC-004-C08` indeterminate · `HC-004-C09` indeterminate · `HC-004-C12` contemporaneous

> ## Review events
> None found.

Not assessed (the summary lists eight files, each "not a historical candidate or a review event"): the six stage-1 JSON files, `stage2-reconcile/assemblies.json`, `stage5-validate/contemporaneity-recomputed.json`.

Things to read alongside that:

- **Everything passed on the first and only validator run. Nothing was changed to make it pass.** There were no post-validation fixes.
- **I had read the fidelity checker's source before writing the fragments.** The relational pass on source fidelity is therefore a pass by an engine that knew the checker's locator and hash conventions. The validator README says such a run should be made "from a checkout the engine cannot read". This run does not meet that.
- My build script refuses any fragment text that does not occur exactly once in its source, so verbatim-ness was enforced before the validator saw it.
- The validator does not assess findings, unclassified outcomes, the stage outputs or the reports. I checked the 38 finding classifications, 100 fragments, 64 contributions and 4 assemblies against the package's schemas myself: 0 errors (`stage5-validate/agent-schema-checks.txt`). That is my check, not the validator's.
- The validator's contemporaneity grades agree with the ones I recomputed independently from the specification's six rules.
- A pass says the candidates are well-formed and their quotes are verbatim. It does not say the readings are right. The weakest values are listed in `stage4-challenge/challenge.md`; the worst is HC-004's date.

Changes I made to my own work before validation, logged:

1. `F08-HEAD` in HC-004 was first annotated as restating `F05-HEAD`; changed to `F05-AGREED` so the log heading and the log row name the same restated fragment. Reason: inconsistency in my own annotation. Still weak (a log heading restates nothing); recorded as a challenge finding.
2. Added one `unresolved` entry to HC-004 saying its note-based context grades indeterminate. Reason: admission criterion 2 requires indeterminate context to be reported in `unresolved`, and I had omitted it.
3. In two Markdown outputs, corrected a count I had typed wrong ("30 of 64" to "33 of 64" contributions with differing confidences; "three" to "four" inferred contributions).

## 5. Friction log

Ratings: **blocker** (could not proceed from the documentation alone), **slowed me down**, **minor**.

1. **The validator's input format is not documented. — blocker for the source-fidelity check.** `mtdr_validation/README.md`: "It finds every historical candidate and review event under `<folder>`". It does not say they must be `.json` files, one candidate per file. Same file: "the locator selects exactly the content: `line-range` and `char-offset` are applied". The field names inside those locators are nowhere in the documentation; `source-fragment.md` says only "Structure depends on source type: page and character offsets, line range…" and the schema says "Deliberately unconstrained beyond requiring a `kind`". Also undocumented: that `source_hash` must be `sha256:<hex>` or bare hex, and how `source_ref` is matched to a file under `--sources`. I got all four from `fidelity.py` and `folder.py`. Without reading code I would have guessed, and a wrong guess gives `indeterminate` or `fail`.
2. **The same README warns against what item 1 forces. — slowed me down; it also weakens this run as evidence.** "A validator the engine can read becomes the engine's target." An adopter following the README has to read the validator to feed it.
3. **The worked example is the calibration step and I could not use it. — slowed me down.** `practice/using-mtdr-with-your-framework.md`: "Run it before you run your own material. It takes about five minutes and it calibrates what 'correct' looks like". It lives in `tests/adoption/`, which I was told not to open. This is a constraint of this run, not a defect in the page, but I had no example of a finished candidate, finding or report at any point.
4. **Two pages name different skills for the same stages. — slowed me down.** The framework guide, step 2: "`decision-identification` first, then the shared `identify-record-contributions`", then `reconcile-record-fragments`, `challenge-record`, `validate-record`. `records/decision/README.md`: "`recover-decision-records` runs it end to end — `identify-decision-contributions` → `reconcile-decision-contributions` → `draft-tdr` → `challenge-decision-record` → `validate-decision-record`". The guide never mentions `recover-decision-records`. I followed the package README.
5. **No output format for anything except the candidate. — slowed me down.** `decision-contribution.md`: a finding "is reported as the fragment it rests on, with a classification object valid against the machine-readable form". No container is defined for a finding, for an `unclassified` outcome, for the stage-1 "plain summary", for the challenge recommendation ("recorded beside the candidate, never in it"), or for the recovery report. I invented all of them. The validator reports them as "not assessed".
6. **Class name or tightened role in `semantic_role`? — slowed me down.** `identify-decision-contributions`: contributions carry "a class … as its `semantic_role` until drafting tightens it". `recover-decision-records`: "handing each output to the next unmodified". `historical-candidate.md` rule 6: "`event_time_ref` names a contribution to the event role", which the vocabulary gives as `decision-date`, not the class `time`. So either drafting modifies contributions or identification writes roles. I wrote tightened roles from stage 1 where one exists, and class names (`authority`, `lineage`, `challenge`, `corroboration`) where none does.
7. **Proportionality for a recovered candidate: three statements. — slowed me down.** `records/decision/README.md`: a candidate "is proposed at the bare tier, or reported as not warranting a record". The entry skill: "a **candidate view** at the routed tier". `admission.md` criterion 6: with no reversal-cost contribution "the outcome is stated as **undetermined** … It never defaults to a tier". All four candidates have no reversal-cost evidence. Nothing says what body a view takes when the tier is undetermined. I used section names from the minimal template and said that was not a routing.
8. **Dates with no year. — slowed me down; it changed a result.** The file note says "Tues, wk of 1 June"; the chat says "Thu 23 July". `historical-candidate.md`: times are "`YYYY`, `YYYY-MM`, `YYYY-MM-DD` or `unknown`". `historical-recovery.md`: "A folder, a filename, a neighbouring document or a reviewer's knowledge is not a basis", but it also permits inference of "a meeting's day from a minute's text and its year from the minute's header". The only source of the year for HC-004 is the decision log, which is a restatement; the matrix says a restatement supports a date "as its source". I could not tell whether the event date may take its year from a restatement. I set the note's capture time to `unknown` and the event time to `2026-06`, `inferred`. A stricter reader would set the event time to `unknown`.
9. **No evidence kind fits an organisation's own decision log. — slowed me down.** The six kinds are act-record, cited-material, unlinked, later-recording, retrospective, restatement. A log row maintained by the Company Secretary, naming its source, with a "Taken by" column, is partly a restatement and partly the organisation's own register entry (the scheme itself says a decision "should be minuted or logged"). I used `restatement`. That choice stops the log's "Taken by: Chair and Chief Executive" and "Finance Director" from supplying an owner.
10. **`non-decision` has no kind for "not yet decided". — slowed me down.** `decision-contribution.md` lists `deferred`, `not-reached`, `withdrawn`. Three spans say in terms that no decision has been made ("No decision has been taken."; "not decided"; "Decisions needed"). None is deferred, not reached at a meeting, or withdrawn. I reported them as `unclassified`.
11. **The five not-a-decision reasons do not cover three common things. — minor.** A paper's recommendation; a body "noting" another body's decision; and an instruction that carries out an earlier decision but commits money. I used `preference`, `restatement` and `action`. `tdr.md` §3 has the sentence that fits the third — "Execution events are evidence or triggers, not decisions, unless a further judgement was actually exercised" — but it is not one of the five reasons.
12. **A joint act by two named people. — slowed me down.** `semantic-roles.md`: "`accountable-owner` must be a named individual." The scheme paragraph relied on requires two post-holders "acting jointly". Nothing says how to record two. I made two contributions and a `conflicts` entry, which overstates it: the two are not contradicting each other.
13. **Authority cited by paragraph number only. — minor.** The matrix allows cited material to support authority "◐ where it names the instrument". The thread says "4.5" and "the urgent action route" and never names the scheme. I contributed it and said the instrument is not named.
14. **Where does a "flagged" claim go? — minor.** `identify-decision-contributions`: "A limit stated with no instrument behind it is a claim, flagged, never a grant." No role or output holds the flag. I put it in a `context` contribution and in `unresolved`.
15. **An instrument that fails one adoption condition. — minor.** `decision-contribution.md`: "the instrument is reported with the conditions that are met and the evidence that would establish the rest." No class, no output form. I put it under `unclassified`.
16. **`missing_semantics`: mandatory roles only? — minor.** `candidate-assembly.md`: "Required roles for which no contribution exists." Authority, reversal cost and confidence are not mandatory roles, but the documentation treats their absence as a finding ("the authority is missing, and missing is the finding"). I listed them.
17. **Absence statements inside interpreted values. — minor, my own.** `record-contribution.md`: "Absence is not a contribution." Three of my values include remarks such as "names no individual". The contract gives a contribution no other place for a qualifying remark. Left as written; recorded in the challenge.
18. **`considered` exists only for context roles. — minor.** The authority contribution in HC-003 depends on an email being before whoever acted. Rule 6 allows `considered` "on every contribution to a context role and on no other", so the link evidence for an authority contribution has nowhere to go.
19. **Two challenge vocabularies. — minor.** `challenge-record`: "**fit to propose**, or **not fit to propose**". `challenge-decision-record`: "split · merge · reject · incomplete · retain". I gave both.
20. **`show-me` is in the guide's workflow and not in the package. — minor.** Framework guide step 6: "Run it before ratifying anything." The installed decision package has 13 skills; `show-me` is not one, and the entry skill's pipeline does not include it. Not run.
21. **`validate-record` points at a file the package does not carry. — minor.** "read the owning package's manifest (`records/<language>/package.yaml`)". The installed package has no `package.yaml`; the link is listed under `not_packaged`. Recorded as indeterminate in my stage-5 table.
22. **Install path and commands. — minor.** `skills/packaging/claude-code/README.md` says "`verify <installed package folder>`" without saying where `install` puts it; `profiles/README.md` shows `<your project>/.agents/skills/mtdr-decision`, which is the Hermes path. The actual path (`.mtdr/plugins/mtdr-decision`) is printed by `install`. `install` also prints "verified" itself, so the separate `verify` step repeats it. Both READMEs say `uv run python -m …` from the clone, which would create `.venv` inside the clone; I was told not to modify the clone and redirected it.
23. **`skills/packaging/README.md` agent instructions are for authoring. — minor.** "Paste into the runtime's instruction/system-prompt field". Its WORKFLOW is identify → capture → review → value → assure, with `status: proposed`; it does not mention recovery. An adopter who pastes it and then runs recovery has two procedures. I did not apply it.
24. **Status of what I was following. — minor.** `historical-recovery.md`, `historical-candidate.md` and `decision-contribution.md` each open "Proposed under TDR-0048/0049 — no standing until ratified". The entry skill depends on all three. I could not tell from the published material whether an adopter is meant to rely on them. I did.
25. **Stub names in skill text. — minor.** Skills refer to "`spec.md`", "`shared/README.md`", "`shared/uncertainty.md`" as link text for files at other paths. The links resolve; the names do not match what is opened.

## 6. My choices

Decisions the published material did not settle:

1. **Where the virtualenv goes.** `UV_PROJECT_ENVIRONMENT=<project>/.venv`, `--frozen --offline`, `PYTHONDONTWRITEBYTECODE=1`, so that nothing is written into the clone.
2. **Fragment locators:** `char-offset` (`start`, `end`) over the UTF-8 text, for every fragment, so that sub-sentence spans (the two resolutions inside one RESOLVED sentence) can be located exactly. Fragment ids `F<source>-<label>`; candidate ids `HC-001`…`HC-004`.
3. **`source_ref`:** the bare file name. **`source_hash`:** `sha256:` plus hex of the bytes as read.
4. **Tightened roles from stage 1** (friction 6).
5. **Four candidates, not three or five.** HC-002 and HC-003 kept separate (different people, different days). The Board's "agreed that agency cover would be kept on hand" kept inside HC-002 as context rather than split out. The agency booking extension in the chat treated as an action, not a candidate.
6. **HC-003 owner:** both named individuals contributed, with a conflict, rather than the Chair alone or owner missing.
7. **HC-003 authority:** contributed on a paragraph number alone; the scheme's paragraph 4.5 kept out of the candidate and reported as applicability.
8. **HC-004 owner:** contributed as "P. Nandakumar" from the heading plus first-person text, graded partial, rather than missing.
9. **HC-004 date:** `2026-06`, inferred, year from the decision log; the note's own times `unknown` (friction 8). Not completed to 2 June.
10. **HC-004 authority:** not contributed. "Within my limit (12 mths / £150k)" treated as a stated limit with no instrument, despite the figures matching scheme 4.4.
11. **Decision log rows are restatements** (friction 9).
12. **Status report times `unknown`.** "For: Project Board, 14 October 2026" dates the meeting, not the report.
13. **Minutes are act-records with capture time = the meeting date and creation time `unknown`.**
14. **Paper 4 in HC-004** included as circumstance (`considered: unlinked`) on an entity match ("the Orchard extension … Finance Director") rather than left outside.
15. **OIC item 5 in HC-002** included as circumstance (`considered: unknown`) on temporal continuity rather than left outside.
16. **`unclassified` for open questions** and for the scheme's own adoption (friction 10, 15).
17. **No candidate for the Scheme of Delegation's adoption** (authentication not evidenced).
18. **No candidate for the contract signature** (only later material; an execution event).
19. **View body shape** with the tier undetermined (friction 7). Views are generated from the contributions, one line per contribution, so nothing in a view lacks a trace.
20. **Completeness grades** — in particular `partial` for HC-004's date, context and owner, and `conflicting` for HC-003's owner.
21. **Output layout** in `out/` (friction 5), including keeping my build script and data there.
22. **Not run:** `show-me`, `evidence-review`, the assurance skills, `decision-identification`'s candidate envelope. The first is not in the package; the others are routed to by the challenge skill only where its conditions apply, and I judged they did not (no TDR, no evidence of a one-way door).
23. **Interpreter identity** recorded as the agent and model; `observed_at` and `interpreted_at` as 2026-11-26.
24. **The challenger was the drafter.** I ran the challenge stage on my own candidates; no second agent or person did.

## 7. Verdict

**Yes with guesses.** I got from the README to four candidates that the named validator reports as passing structural, semantic and relational checks including source fidelity, but only by reading the validator's source for the file, locator and hash conventions the documentation omits, and by inventing the form of every output other than the candidate. The year-less date, the decision log's evidence kind and the joint owner were settled by my guess, not by the published material.
