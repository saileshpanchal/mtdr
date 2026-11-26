# Independent readability review of the public documentation at `1a2d0e5` — 26 November 2026

Evidence for the release decision. **It is not ratification evidence, and it approves nothing.** It is
the one independent readability review the maintainer asked for, run after the readability pass.

| | |
|---|---|
| Commit reviewed | `1a2d0e54761db08bc0b2c3aaa4a68cff609534a6` (`release/next-candidate`) |
| Reviewer | An AI agent, Claude Sonnet 5.5. Not a person. It did not write the documentation or the readability pass |
| Given | A read-only export of the repository at the commit, and the maintainer's reading order: README, quick start, the relevant record package, installation guidance, the first example. At each stage: does the reader know what to do next, why, and what evidence they need? |
| Result | **1 blocker · 21 fixes · 8 notes** |

**Everything below the line is the reviewer's report, verbatim as delivered**, except that the export's
local path is replaced by `<snapshot>`, and the brackets of Markdown links it quotes from other files
are escaped, so they display as the quoted text and are not followed from this folder.

---

# Readability review: MTDR at 1a2d0e54761db08bc0b2c3aaa4a68cff609534a6

Reviewer stance: first-time enterprise architect who has just found the repository. Paths are relative to the repository root unless stated.

## 1. Verdict

A first-time reader can get from the README to a first record without help, because the quick start, the templates and the full example are clear enough to write one by hand. The reader cannot get a validation result without help. The only validation command the path offers does not assess an authored record, and it exits 0 saying "0 artefact(s) assessed". The other check is a skill that needs an AI assistant, and the installer the README points to does not install the skill that writes the record. Thirty findings: 1 Blocker, 21 Fixes, 8 Notes.

## 2. Stage reports

### Stage 1: README.md

- **Next step**: Clear. Line 23: "**Follow the \[quick start\]\(practice/quickstart.md\).**" A reader would open the quick start, pick a template from the table at lines 29-33 and copy the matching example. The bold link is easy to find. What works: lines 1-8 say what a TDR is and why in plain terms, and the three-row template table is the best navigation in the repository.
- **Why**: Mostly clear from lines 3-5 ("what was known at the time, who was accountable, how confident they were, what they rejected"). The fuller "Why" does not arrive until line 93, after install commands, a route comparison table and a terms paragraph.
- **Evidence**: Not stated. The README never says what the reader needs to bring to write a first TDR (a decision, a named owner, source material) or what they will have at the end.
- Between the "Write your first TDR" heading (line 21) and the "Why" section (line 93), the reader meets: two routes, "candidate", "ratification", "standing", "retrospective candidate", TDR-0048/0049, installation, `mtdr_validation`, `tests/verify.py`. None of it is needed for a first record, and most of it belongs to a route the reader has not chosen.
- Terms used before definition or never defined: MADR and ADR (line 8, "as MADR is to ADR", never expanded on this page), YAML (line 8), "supersedes" (line 17, before the reader knows records have lineage), VR/DAC (lines 106-111, DAC is explained only as "reasoning that challenges those consequences"), OIR/OAR/OER (lines 121-123, never expanded on the page), "Operational Value Commitment" (line 106), "Hermes" (line 77, never explained), "recovery" in the install sense (line 77, "Each package is built for recovery"; the reader has not been told what is being recovered).

### Stage 2: practice/quickstart.md

- **Next step**: Mostly clear. The reader would read the three rules (lines 32-40), then run the six-step loop (lines 49-63). Step 1 is the first action: give a source to the decision-identification skill.
- **Why**: Clear at line 9-13 ("durable, searchable memory of your organisation's consequential decisions"). Line 13, "Success is better decisions, not more records," is a slogan, but harmless.
- **Evidence**: Partly. Step 1 names the input ("meeting minutes, a board paper, a policy, a business case"). Missing: where the finished record is saved, what it is called, how the id is chosen, what a "place to keep records" (line 3) is, and what changes when the owner "confirms" (step 6). The seven evidence dimensions the record needs are never named on this page.
- The page contradicts itself about its own input. Line 17 says the page teaches recording "at the time of a decision, with the person who holds the reasoning taking part". Step 1 (line 49) starts from "meeting minutes, a board paper, a policy, a business case", which is the material the interpretation path works from. Line 28 then says the page "does not yet route someone holding minutes of a past decision to historical recovery". A reader holding minutes cannot tell whether step 1 is for them.
- The loop depends on a skill the installer does not provide (lines 45-47, disclosed). See RD7.
- Validation is covered at lines 65-72, but the only command offered is declared not to apply to the reader's record. See RD1.

### Stage 3: records/decision/README.md

- **Next step**: Not clear. Line 13: "To write a first record, start at the repository's quick start, `practice/quickstart.md`." The reader has just come from there. The page then lists contents and skill chains, with nothing on what to do next for a first record (open `templates/`, open `examples/`).
- **Why**: The opening paragraph (lines 6-11) explains the package's architecture (DAC as "a dependent artefact, not a sixth language"), which does not answer a reader's question of why they are here.
- **Evidence**: Not stated.
- The relative path at line 13 is in code formatting, not a link, and `records/decision/practice/` exists, so a reader standing in this directory could resolve `practice/quickstart.md` to the wrong place.
- Skills section (lines 32-59): two chains of up to nine skill names, plus seven assurance skill names, with no indication of which ones a first-time author uses. Terms not explained: "Semantic roles", "Admissibility test", "FIX-004", "Consequential Decision Grammar" (lines 26-28), "interpretation path" (the README called it "recovery"), "retrospective candidate".
- Line 63: "Spec §3" is not linked.

### Stage 4: installation guidance

Path followed: README lines 67-91, quick start line 45, then `skills/packaging/README.md` (Install and verify), `skills/packaging/profiles/README.md`, `skills/packaging/claude-code/README.md`.

- **Next step**: The command is clear in form. The reader would run `uv run python -m mtdr_packaging.profiles install decision --runtime claude-code --project <dir>` and then `verify`. The prerequisites are not: where to run it (the repository root, after cloning), that `uv` is needed, and which runtime to choose.
- **Why**: Partly. README line 69 says "To have an AI assistant apply the skills, install one record type's package". But line 77 then says the package "leaves out the skill that captures a new decision", so installing does not serve the first-record job the README section is about.
- **Evidence**: The reader is not told what they will have afterwards. I ran it. Output for `install decision --runtime claude-code --project ../work/proj`:
  `installed ../work/proj/.mtdr/plugins/mtdr-decision` / `decision @ unknown: 43 files, tree b9e49b26b0a76411; 13 skills discoverable; skill links: 55 resolve, 13 declared not packaged, 0 broken` / `verified`. The `verify` command on that folder gave the same output and exit 0. `--runtime hermes` placed the package at `.agents/skills/mtdr-decision` and also verified. Both worked; the commands in the documentation are accurate.
- What the output means to a first-time reader is not explained: "tree b9e49b26b0a76411", "13 declared not packaged", "@ unknown".
- Three pages repeat the same two commands with different placeholders (`<your project>`, `<installed package folder>`). Only the Hermes example path (`<your project>/.agents/skills/mtdr-decision`, profiles README line 35) is given. The Claude Code path (`.mtdr/plugins/mtdr-decision`) appears nowhere in prose; the reader finds it only from the installer's output.
- The packaging README, between the reader and the install section, carries an architecture table, a rule, and (lines 98-181) a 6,000-character system prompt. This is useful to someone deploying an agent but pushes the install section to line 43 and the other content below it.

### Stage 5: first worked example (`records/decision/examples/example-full-consumer-duty-channel-decision.md`)

- **Next step**: Clear. The reader compares their draft to this record, section by section. It is 53 lines, labelled fictional at line 16, and uses the template's headings in order. What works: the evidence section shows each dimension with a document reference; the "Alternatives rejected" section includes "do nothing".
- **Why**: Clear from the callout at line 16 (what the example shows).
- **Evidence**: Evidence item references (FP-2026-014, AA-118, CO-2026-09) show what "where it lives" means, but nothing says these are examples of the reader's own document references.
- Nothing annotates the front matter. `conforms_to: mtdr/decision/tdr@1.15.0` (line 3) is copied into every template, with no instruction to keep it unchanged. `status: accepted` and `maturity: adopted` are copied too: the README (line 29) calls this "A record to copy from", and the template defaults are `proposed`.
- Line 13: `confirmed_by_outcome: pending — review 2026-09-30` names a review date that had already passed at the date of this review (2026-11-26) while the field still says `pending`. A reader may take this as a defect in the example.
- No validation output is shown for this record, so the reader still does not know what "valid" looks like (RD1).

## 3. Findings

Severity: Blocker (cannot proceed or will be misled), Fix (proceeds with avoidable difficulty), Note (minor).

### Stage 1

**RD1. Blocker. README.md:83-86; practice/quickstart.md:67-72; mtdr_validation/README.md "Which check you want".**
Quote: "It does not assess a TDR you have authored, and it gives no overall result" (README 85-86); "The command `uv run python -m mtdr_validation <folder>` does a different job" (quickstart 71).
Problem: The reader's goal is a first record and a validation result. The only command on the path is declared not to apply. The alternative is the `validate-record` skill, which needs an AI assistant (the reader has no instruction on how to run it by hand, and no schema command). I ran `uv run python -m mtdr_validation ../work/rec` on a folder holding a copy of the full example, as a reader might: output `0 artefact(s) assessed, 0 file(s) not assessed; results and summary in ../work/rec/validation`, exit 0. A reader who runs it anyway sees a success-shaped exit and a zero count, and may believe the record passed. The path never states what a validation result for an authored TDR looks like, or how to obtain one without an assistant.

**RD2. Fix. README.md:21-33, 39-65, 93.**
Problem: The "Write your first TDR" section is interrupted by the two-route table, the candidate/ratification/standing paragraph, the recovery status table and the TDR-0048/0049 references before the reader reaches "Why" at line 93. A first-time reader must wade through material about a route they have not chosen. The README already says (line 61) that the quick start does not route past decisions; this could sit under Known limitations alone.

**RD3. Fix. README.md:8.**
Quote: "**MTDR** is its markdown reference format, as MADR is to ADR."
Problem: MADR and ADR are never expanded on the page. The line carries the whole explanation of the name for a reader who does not know them. The link to the ADR lineage is at line 193, 185 lines later.

**RD4. Fix. README.md:106-123.**
Quote: "**Value Record (VR)** — the governed memory of an Operational Value Commitment"; table rows "Inheritance | OIR", "Authority | OAR", "Evidence | OER".
Problem: OIR, OAR, OER and "Operational Value Commitment" are used without expansion or definition. DAC is described by effect only ("the reasoning that challenges those consequences before execution").

**RD5. Fix. README.md:77.**
Quote: "Each package is built for recovery, so it leaves out the skill that captures a new decision".
Problem: "Recovery" is not defined at this point, and the sentence tells a reader writing a first record that the install step is not built for them. "Hermes" (line 77) is also unexplained.

**RD6. Note. README.md:10.**
Quote: "MIT licensed. Tool-neutral. Regulator-neutral. Works alongside what you already run."
Problem: Four fragment claims in a row; "works alongside what you already run" is unsupported on the page. Mild padded-slogan effect.

**RD7. Fix. README.md:69-79 and practice/quickstart.md:44-47.**
Quote: "The installed `decision` package is built for recovery: it includes decision-identification and validate-record, but not problem-framing-and-decision-capture, the skill this loop uses to write the record".
Problem: The path sends the reader to install, and install cannot run the step that writes the record. The disclosure is honest, but it leaves the AI-assisted first-record route with no working instruction: the reader must locate the capture skill by hand (`records/decision/skills/problem-framing-and-decision-capture/`) and the README never says to open it directly. Only a reader who reads the Known limitations (line 134-136) learns the same.

**RD8. Note. README.md:78, 135-136.**
Quote: "…governance review. \[`skills/packaging/`\]\(skills/packaging/\) explains both commands…"; "…captures a new decision\n([#15]…"
Problem: Line 78 is a ragged wrap, with the sentence continuing at a different width; lines 135-136 break mid-sentence and the continuation is unindented in the list. Line 100 is a single 330-character line. The file's wrapping is inconsistent.

**RD9. Note. README.md:147-148.**
Quote: "The tests that shipped with v1.30.0 report 13 failures against this release."
Problem: A reader sees failing tests as an unexplained caveat. The cause is given ("experimental package state"), but not what the reader should do or whether it affects them. The installer output, "decision @ unknown" and version "1.30.0+unreleased" in `plugin.json`, adds to the unsettled impression.

### Stage 2

**RD10. Fix. practice/quickstart.md:17, 28 and 49.**
Quote: "writing a record at the time of a decision, with the person who holds the reasoning taking part" vs step 1 "Give the source — meeting minutes, a board paper, a policy, a business case".
Problem: The input to step 1 is the material the interpretation path works from, but the page says that path is not this one. A reader holding minutes cannot tell whether to proceed. The page itself says (line 28) it does not route them.

**RD11. Fix. practice/quickstart.md:62-63.**
Quote: "Have the named owner confirm, then save the accepted record."
Problem: No instruction on what "confirm" changes (the `status` field from `proposed` to `accepted`, per the templates), where to save the file, what to name it, or how the id is allocated. The id rule appears only in `validate-record` ("The `id` matches the filename") and in the full example's note ("ids are unique per organisation, not globally"). The reader has no way to learn it from the path. Line 3 "a place to keep records" is also undefined.

**RD12. Fix. practice/quickstart.md:49-61.**
Problem: The loop does not name the evidence the record needs. The seven dimensions (Business, Architecture, Regulatory, Operations, Customer, Data, External) appear only in the template and the example. The reader cannot tell at steps 1-3 what to collect before drafting, and "Improve, do not just approve" (step 5) asks "what evidence is missing" without naming what evidence is expected.

**RD13. Fix. practice/quickstart.md:44-47.**
Problem: This paragraph carries the loop's tooling caveat inside a sentence that begins "Each skill named below is a `SKILL.md` file." The reader gets definition, deployment link and a limitation in one 60-word block, with one line wrapped at a different width. Step 1 depends on a decision-identification skill and step 3 on a capture skill, but the reader is not told they may read either file as a plain procedure until the middle of this block.

**RD14. Note. practice/quickstart.md:13.**
Quote: "Success is better decisions, not more records."
Problem: Slogan sentence; adds nothing the proportionality rule at step 2 does not. Keep or cut.

### Stage 3

**RD15. Fix. records/decision/README.md:13.**
Quote: "To write a first record, start at the repository's quick start, `practice/quickstart.md`. This page is the package's index."
Problem: The reader has just come from the quick start; the page sends them back. The path is not a link and `records/decision/practice/` exists, so relative resolution is wrong. The page does not say "open the template, open the example", which is what the reader needs.

**RD16. Fix. records/decision/README.md:6-11, 26-28.**
Quote: "The **Decision Assurance Case (DAC)** lives here as a dependent artefact, not a sixth language"; "Semantic roles (interpretation)", "Admissibility test", "FIX-004", "The Consequential Decision Grammar … candidate authoring aid".
Problem: The opening paragraph spends its words on package architecture ("sixth language" is never defined; the README listed three languages and two candidates). The contents table lists artefacts a first-time author does not need, without saying which ones they do (templates, examples, `specification/tdr.md`).

**RD17. Fix. records/decision/README.md:38-59.**
Problem: Two arrow chains of nine skill names and a list of seven assurance skill names, with no sentence saying "start with `decision-identification`", and no explanation of "interpretation path" (the main README and quick start call it "recovery"). Three names for one thing: recovery, interpretation, reconstruction.

**RD18. Note. records/decision/README.md:63.**
Quote: "Spec §3 routes a decision to full, minimal or bare by reversal cost".
Problem: "Spec §3" is not linked, and the reader has not been told which specification.

### Stage 4

**RD19. Fix. README.md:72-73; skills/packaging/README.md:48-51.**
Quote: "uv run python -m mtdr_packaging.profiles install <record-type> --runtime <runtime> --project <your project>"
Problem: No prerequisites (clone the repository, install `uv`), no working directory (it only works from the repository root), and no statement of what `<runtime>` to choose if you use neither Claude Code nor Hermes. The first run silently creates a `.venv` inside the repository (it created one in the read-only snapshot).

**RD20. Fix. skills/packaging/profiles/README.md:33-36 and 47-53.**
Quote: "uv run python -m mtdr_packaging.profiles verify <your project>/.agents/skills/mtdr-decision"
Problem: The only path example is the Hermes one. For `--runtime claude-code` the package lands at `<project>/.mtdr/plugins/mtdr-decision`, which no page states (I found it from the installer's output). Line 52 adds "Run `claude --plugin-dir <package>`", but nothing says whether that is a one-off flag or how to make it permanent, or how to invoke a skill afterwards.

**RD21. Fix. skills/packaging/profiles/README.md:3, 51.**
Quote: "*Generated by `mtdr_packaging.profiles`. Do not edit; regenerate.*"; "The descriptor is a thin engine adapter (owner, 23 Nov 2026)".
Problem: The reader's installation page opens with a generator notice, and "(owner, 23 Nov 2026)" is an opaque parenthetical (whose owner, and what happened on that date?). The same sentence is in `claude-code/README.md:33`.

**RD22. Fix. skills/packaging/claude-code/README.md:20-33.**
Quote: "**66 of their 108 relative links no longer resolve, in 15 of the 30 skills, even inside a full clone**… In a project without the repository, 92 of 108 break."
Problem: The statistics are precise but do not help the reader act: the instruction is one sentence ("Do not collect the skills flat"). The paragraph is machine-shaped: the continuation lines are indented as if code, line 33 is a single run-on sentence of three clauses joined by dashes, and the discovery list at lines 35-40 has uneven spacing. The reader meets the install instruction and then three screens of reasoning.

**RD23. Fix. skills/packaging/README.md:94-181.**
Problem: The agent-instruction block is a 6,000-character system prompt placed before "Memory", "Multiple agents" and "Prove it". It is a deployment artefact, not install guidance; a reader looking for the install steps must scroll past a long block. It also says "thirty `SKILL.md` files" (lines 76, 104) while the install produces 13 skills for the decision package; the count is explained only in `profiles/`.

**RD24. Note. skills/packaging/README.md:11-12.**
Quote: "Since mid-2026 the major agent runtimes load that structure natively".
Problem: Unsourced claim in the install page. The sources page is `runtime-evidence.md`, linked at line 23 but not here.

**RD25. Fix. skills/packaging/README.md:60-65.**
Quote: "3. Run the ten \[agent probes\]\(../../tests/conformance/agent-probes.md\) before trusting the deployment."
Problem: The reader's last install step is to run ten probes, with no hint what a probe is, how long it takes, or whether it is needed for a first trial. Given the README's "Prove it" at line 201, it is presented as mandatory. The link is the only explanation.

**RD26. Note. skills/packaging/README.md:53-54 and install output.**
Problem: Installer output `decision @ unknown: 43 files, tree b9e49b26b0a76411; 13 skills discoverable; skill links: 55 resolve, 13 declared not packaged, 0 broken` is not glossed anywhere; the reader cannot tell whether "unknown" and "13 declared not packaged" are problems.

### Stage 5

**RD27. Fix. README.md:29-33 and records/decision/examples/example-full-consumer-duty-channel-decision.md:2-13.**
Quote: "A record to copy from"; `id: TDR-0031`, `status: accepted`, `maturity: adopted`, `conforms_to: mtdr/decision/tdr@1.15.0`.
Problem: The reader is told to copy from the example, but not to change `id`, `status`, `decision_date`, `accountable_owner`, or to keep `conforms_to`. A copy that keeps `status: accepted` records a decision as accepted that nobody has accepted, against rule 1 of the quick start.

**RD28. Fix. records/decision/examples/example-full-consumer-duty-channel-decision.md:13.**
Quote: "confirmed_by_outcome: pending — review 2026-09-30 against member outcome dashboard"
Problem: The review date (2026-09-30) is already past at the time of this review (2026-11-26) and the field still says `pending`. A reader reads this as a stale or wrong record. Either the example should say it is frozen at its decision date, or the date should be later.

**RD29. Note. README.md:35-37.**
Quote: "§4.1 defines the fields in the templates, all but `conforms_to`, which \[record identity\]\(specification/record-identity.md\) defines."
Problem: Hard to parse on first read; a reader needs two documents to understand the front matter of one record, and the example does not annotate any field.

**RD30. Fix. records/decision/examples/ (all three) and path.**
Problem: The path shows the reader a record but never a validation result for it. A reader who has written a record from the example cannot compare it with a known-good outcome. (This is RD1 seen from the end of the path.)

## 4. Out of scope observations

- The `confidence` field cannot hold "not yet stated" (README line 132, issue #14); I make no proposal.
- The `maturity` field appears in the full template and example but not in the minimal one; I take it to be intended.
- Whether "status: proposed" should be allowed for an approved decision (issue #16) is a rules question.

## 5. What I did

All work read-only on the snapshot except where noted. Snapshot root: `<snapshot>/`.

Reading, in order: `README.md` (204 lines); `practice/quickstart.md` (91 lines); `records/decision/README.md` (67 lines); `skills/packaging/README.md`, `skills/packaging/profiles/README.md`, `skills/packaging/claude-code/README.md`; `records/decision/examples/example-full-consumer-duty-channel-decision.md` (53 lines), with the full template, bare template and the head of the minimal example for comparison. I also read the head of `mtdr_validation/README.md` and `skills/shared/validate-record/SKILL.md` because the path sends the reader there for validation.

Commands and results (all with `cd` into the snapshot; `UV_NATIVE_TLS` deprecation warnings omitted):

1. `uv run python -m mtdr_packaging.profiles list` produced `decision: 13 skills, 29 references`, `value: 10 skills, 20 references`, and three "none" lines for authority, evidence and work. Side effect: uv created `.venv` in the snapshot (outside `work/`), because the README gives no other way to run the command.
2. `uv run python -m mtdr_packaging.profiles install decision --runtime claude-code --project ../work/proj` gave `installed ../work/proj/.mtdr/plugins/mtdr-decision`, then `decision @ unknown: 43 files, tree b9e49b26b0a76411; 13 skills discoverable; skill links: 55 resolve, 13 declared not packaged, 0 broken`, then `verified`. Exit 0.
3. `uv run python -m mtdr_packaging.profiles verify ../work/proj/.mtdr/plugins/mtdr-decision` gave the same line and `verified`. Exit 0.
4. `install decision --runtime hermes --project ../work/proj2` then `verify ../work/proj2/.agents/skills/mtdr-decision`: both `verified`, same counts.
5. `uv run python -m mtdr_validation --help` printed usage for a folder of "recovery output".
6. Copied the full example to `work/rec/TDR-0031.md` and ran `uv run python -m mtdr_validation ../work/rec`: `0 artefact(s) assessed, 0 file(s) not assessed; results and summary in ../work/rec/validation`. Exit 0.
7. `find` on the installed package listed 13 `SKILL.md` files; `problem-framing-and-decision-capture` and `governance-review` are absent, as documented. `.claude-plugin/plugin.json` reads `"version": "1.30.0+unreleased"`.
8. Link checks: `decisions/TDR-0004-markdown-yaml-serialisation.md`, `tests/conformance/agent-probes.md`, `specification/historical-recovery.md`, the capture skill and `records/decision/specification/tdr.md#7-status-and-lifecycle` (heading 7 exists) all resolve.
9. Not run: `uv run tests/verify.py` (the README says it is for contributors), the ten agent probes, and `claude --plugin-dir`, because the path sends the reader to them only after install and they need an agent runtime.
