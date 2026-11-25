# Evidence — engineering controls 0.1.0 (proposed): work package, verification and independent review

*25 November 2026. This file is evidence about a proposal. It ratifies nothing, and no record takes
standing from it. The controls it concerns are in [`ENGINEERING-CONTROLS.md`](../../ENGINEERING-CONTROLS.md).*

## Work package

| | |
|---|---|
| Scope | Add `ENGINEERING-CONTROLS.md` (version 0.1.0, proposed, non-normative) and a section in `CONTRIBUTING.md` that links to it. No specification, schema, skill, fixture, validator or decision record changes. |
| Sources | The engineering-controls proposal submitted by the maintainer on 25 November 2026; three proposed amendments from a review of it; this repository's accepted records (`GOVERNANCE.md`, `CONTRIBUTING.md`, TDR-0027, TDR-0037, TDR-0042, `specification/record-admission-test.md`, `decisions/ALLOCATION.md`). |
| Target | `release/next`, the merge target for the next release baseline. Not `main`. The work is on the branch `ws/controls`. |

**When this baseline was committed.** It was first stated in the pull request's description, which
was written after the first implementation commit (`49dcffb`), and it was first committed in this
file, later still. The controls themselves ask for it to be committed before implementation begins;
this change did not do that.

**Acceptance criteria**

1. The repository's suite passes from a clean tree at the exact commit.
2. The tests of release `v1.30.0`, run unmodified in this tree, show no failure that `main` does not already show.
3. No file under `records/decision/` or `records/value/` changes.
4. The complete history of the branch introduces no private identifier, local path, credential or personal data.
5. An independent review at the exact commit, by a reviewer that did not write the change.

## Verification

Each commit was materialised with `git archive <commit>` into a scratch directory outside any clone.
Environment: macOS 27.3 arm64; uv 0.13.9; Python 3.13.12; dependencies pinned to attrs 26.1.0,
jsonschema 4.26.0, jsonschema-specifications 2025.9.1, pyyaml 6.0.3, referencing 0.37.0, rpds-py
2026.9.1, typing-extensions 4.16.0.

```
uv run --directory <tree> --no-project --python 3.13 --with attrs==26.1.0 --with jsonschema==4.26.0 \
  --with jsonschema-specifications==2025.9.1 --with pyyaml==6.0.3 --with referencing==0.37.0 \
  --with rpds-py==2026.9.1 --with typing-extensions==4.16.0 python tests/verify.py --emit
```

The release's tests are run by taking them from the tag into a second clean copy of the same commit,
then running the same command there. For `49dcffb` and `695c1a3` three paths were taken:
`git archive v1.30.0 tests/verify.py tests/validation tests/inspectability | tar -x -C <second tree>`.
That leaves one helper the suite imports, `tests/adoption/disclosure.py`, at the branch's version, so
it is not quite the release's tests unmodified. For `94e2d0c` the whole folder was also taken,
`git archive v1.30.0 tests | tar -x -C <second tree>`, with the same result.

The history scan reads every version of every file in every commit of the branch, and each commit's
message, author and committer. It looks for credentials, local paths, identifiers of private records,
the names of private systems or clients, and e-mail addresses other than two it does not report: the
maintainer's own address as author and committer, and the no-reply address in co-author trailers.
Every commit on this branch carries both, as `main`'s history already does.

| Commit | Suite | `v1.30.0`'s tests in this tree | Files changed against `main` (`ea1c3ba`) | History scan |
|---|---|---|---|---|
| `49dcffbba9d9e4e45f95d3163a2905b200cf1d52` (first version) | exit 0; structural, semantic and relational pass; transition eligibility indeterminate on DAC-0032#4, as on `main`; 988 links checked | exit 1 with the same 13 failures as `main`, all from the experimental package under TDR-0046 and TDR-0047; none new | `ENGINEERING-CONTROLS.md`, `CONTRIBUTING.md` | 1 commit, 2 file versions: no hit |
| `695c1a3f7e0cc8920ef1c374b2bda4c74f3bd698` (after the review) | exit 0; the same four results; 991 links checked | the same 13 failures; none new | the same two files (`ENGINEERING-CONTROLS.md` sha256 `5c6c898f0c745b88e7dd3942aaf56c8a818bf98d13b412ce6f5942e3a18a0d15`) | 2 commits, 4 file versions: no hit |
| `94e2d0c3b959b4f65b5f2422d54c3edc65a76f2d` (after the second review) | exit 0; the same four results; 992 links checked | the same 13 failures, with the three paths and with the whole of the release's `tests/`; none new | `ENGINEERING-CONTROLS.md` (sha256 `67ed469b6a6fc2549ad6524a026907f100effd23a31cb0e707bdea5fe3b35d0f`), `CONTRIBUTING.md`, and this file | 4 commits: no hit |

**These are clean-tree runs on one machine. They are not continuous integration**: no workflow has yet
run on this repository.

## Independent review at `49dcffb`

Reviewer: an AI reviewer running a different model from the author's, given the change and its sources
and not the author's conclusions. It ran the suite itself from a clean tree (exit 0), compared Part A
word for word with the submitted proposal, and compared Part B with the three amendments. Result: no
blocking finding, three to fix, four notes.

| # | Finding | Response at `695c1a3` |
|---|---|---|
| F1 | The file claimed that engineering work "nevertheless follows" an unratified proposal, and Part C described unratified practice as established. The review added that most commits on `main` were made directly on it (a figure the second review showed to be wrong; see below), and that this change kept its own baseline and evidence only in the pull request. | The claim is removed. Part C marks each row **recorded** or **proposed**. This file commits the baseline and the evidence, after the implementation. |
| F2 | A versioned file that waits to be ratified is a second decision mechanism, which `GOVERNANCE.md` rules out. | The file now says the controls become practice only when a decision record in `decisions/` adopts them. |
| F3 | "Ratify … establishes that it is accepted" dropped TDR-0027's separation of the human act from the evidence that lets a record be shown as `accepted`. | The ratification row quotes TDR-0027's rule in full, and the table of acts restates it. |
| F4 (note) | The release row left out the authorised human act and the generated catalogue. | Both added, from TDR-0042. |
| F5 (note) | "Nothing else is changed" was untrue (heading levels), and the third omission dropped words about this repository's own history. | The heading change is disclosed. In the third passage only the private system's name is left out. |
| F6 (note) | "MTDR closure" cannot be resolved by a public reader. | One editorial line outside Part A explains it. |
| F7 (note) | The attribution "submitted by the maintainer" is supported and claims no ratification. The review suggested, as optional, a line saying that Part B's framing and Part C are not the maintainer's wording. | No change; the optional line was not added. |

The reviewer also confirmed that the change touches nothing under `records/`, `specification/`,
`schemas/`, `skills/`, `tests/` or `decisions/`, and that it breaches no public boundary. This evidence
file is the one later addition under `decisions/evidence/`.

## Second independent review, of `695c1a3` and `cd34649`

Reviewer: an AI reviewer running a different model from the author's, which had not written the change.
It re-ran the suite at both commits (exit 0 at each) and the release's tests (the same 13 failures at
`ea1c3ba`, `49dcffb`, `695c1a3` and `cd34649`). Result: no blocking finding; F2 to F6 answered; F1
partly answered; three new points to fix; three notes.

| # | Finding | Response at `94e2d0c` |
|---|---|---|
| N1 | The baseline row moved the baseline to an evidence record committed after implementation, against the proposal's own "before implementation begins". | The row now says the baseline is committed on the working branch before the first implementation commit. This file says plainly that this change did not do so. |
| N2 | "A commit, a merge, or a tool writing `accepted` establishes none of this" overstated TDR-0027, which says these acts do not confer standing by themselves and may carry evidence of the human act. | The row now follows TDR-0027's wording. |
| N3 | "Most of the commits on `main` to date were made directly on it" was wrong. The figure came from the first review. | Corrected to what the history shows: none of the ten pull requests merged to date records a review, and part of `main`'s history, the release commit and the current tip among it, was committed without a pull request. The message of commit `695c1a3` repeats the wrong statement and is not rewritten; the message of `94e2d0c` corrects it. |
| F1, remainder | The summary line for Part C and the table of acts carried no recorded or proposed mark. | Both now carry it. |
| N4 (note) | "Quotes TDR-0027 in full" overstated a two-sentence quotation. | Now "TDR-0027's rule in full". |
| N5 (note) | Two citations were wider than their sources. | Narrowed: "An accepted decision…"; "A `TDR-*` or `DAC-*` identifier…". |
| N6 (note) | This file gave no command for the release's tests or pattern for the scan, called the merge target a working branch, and left out part of F7. | All four corrected above. |

## Third independent review, of `94e2d0c` and `90c920d`

Reviewer: an AI reviewer running a different model from the author's, which had not written the change.
It re-ran the suite at both commits (exit 0 at each, 992 links checked) and confirmed the statement
about `main`'s history against the repository and the pull requests. Result: no blocking finding, and
**no finding in `ENGINEERING-CONTROLS.md` above the level of a note**; two sentences of this file to
fix; three notes.

| # | Finding | Response |
|---|---|---|
| T1 | This file said the baseline "was stated in the pull request's description when the work began". The pull request was opened after the first implementation commit, and its description already reported results at that commit. | Corrected above. |
| T2 | This file said the scan reads author, committer and messages for e-mail addresses and reported no hit, although every commit carries the maintainer's address and a no-reply trailer. | The two exclusions are now stated above. |
| T3 (note) | Taking three paths from the tag is not quite "the release's tests, unmodified": one imported helper stays at the branch's version. | Stated above. The whole of the release's `tests/` was also run over `94e2d0c`: the same 13 failures. |
| T4 (note) | In the table of acts, the ratification row cites only TDR-0027 for "for this repository, the maintainer"; the maintainer's role is recorded in `GOVERNANCE.md`. | Not changed here. `ENGINEERING-CONTROLS.md` stays at the reviewed commit `94e2d0c`; the citation is to be completed when the file next changes. |
| T5 (note) | The pull request's description still carries two earlier wordings that the files have since corrected. | The description is corrected. It is not part of the merge content. |

The commit that carries this revision changes this file only. It needs a check of its own before the
pull request can be put forward for a merge decision.

## What this does not establish

- Not ratification of the controls, and not their adoption: that needs a decision record.
- Not continuous integration.
- Not a review by a person.
