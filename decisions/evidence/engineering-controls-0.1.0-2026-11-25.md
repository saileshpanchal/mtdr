# Evidence — engineering controls 0.1.0 (proposed): work package, verification and independent review

*25 November 2026. This file is evidence about a proposal. It ratifies nothing, and no record takes
standing from it. The controls it concerns are in [`ENGINEERING-CONTROLS.md`](../../ENGINEERING-CONTROLS.md).*

## Work package

| | |
|---|---|
| Scope | Add `ENGINEERING-CONTROLS.md` (version 0.1.0, proposed, non-normative) and a section in `CONTRIBUTING.md` that links to it. No specification, schema, skill, fixture, validator or decision record changes. |
| Sources | The engineering-controls proposal submitted by the maintainer on 25 November 2026; three proposed amendments from a review of it; this repository's accepted records (`GOVERNANCE.md`, `CONTRIBUTING.md`, TDR-0027, TDR-0037, TDR-0042, `specification/record-admission-test.md`, `decisions/ALLOCATION.md`). |
| Target | The working branch `release/next`. Not `main`. |

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

| Commit | Suite | `v1.30.0`'s tests in this tree | Files changed against `main` (`ea1c3ba`) | History scan |
|---|---|---|---|---|
| `49dcffbba9d9e4e45f95d3163a2905b200cf1d52` (first version) | exit 0; structural, semantic and relational pass; transition eligibility indeterminate on DAC-0032#4, as on `main`; 988 links checked | exit 1 with the same 13 failures as `main`, all from the experimental package under TDR-0046 and TDR-0047; none new | `ENGINEERING-CONTROLS.md`, `CONTRIBUTING.md` | 1 commit, 2 file versions: no hit |
| `695c1a3f7e0cc8920ef1c374b2bda4c74f3bd698` (after the review) | exit 0; the same four results; 991 links checked | the same 13 failures; none new | the same two files (`ENGINEERING-CONTROLS.md` sha256 `5c6c898f0c745b88e7dd3942aaf56c8a818bf98d13b412ce6f5942e3a18a0d15`) | 2 commits, 4 file versions: no hit |

**These are clean-tree runs on one machine. They are not continuous integration**: no workflow has yet
run on this repository.

## Independent review at `49dcffb`

Reviewer: an AI reviewer running a different model from the author's, given the change and its sources
and not the author's conclusions. It ran the suite itself from a clean tree (exit 0), compared Part A
word for word with the submitted proposal, and compared Part B with the three amendments. Result: no
blocking finding, three to fix, four notes.

| # | Finding | Response at `695c1a3` |
|---|---|---|
| F1 | The file claimed that engineering work "nevertheless follows" an unratified proposal, and Part C described unratified practice as established. Most commits on `main` were made directly on it, and this change kept its own baseline and evidence only in the pull request. | The claim is removed. Part C marks each row **recorded** or **proposed** and says what `main`'s history actually shows. This file commits the baseline and the evidence. |
| F2 | A versioned file that waits to be ratified is a second decision mechanism, which `GOVERNANCE.md` rules out. | The file now says the controls become practice only when a decision record in `decisions/` adopts them. |
| F3 | "Ratify … establishes that it is accepted" dropped TDR-0027's separation of the human act from the evidence that lets a record be shown as `accepted`. | The ratification row quotes TDR-0027 in full, and the table of acts restates it. |
| F4 (note) | The release row left out the authorised human act and the generated catalogue. | Both added, from TDR-0042. |
| F5 (note) | "Nothing else is changed" was untrue (heading levels), and the third omission dropped words about this repository's own history. | The heading change is disclosed. In the third passage only the private system's name is left out. |
| F6 (note) | "MTDR closure" cannot be resolved by a public reader. | One editorial line outside Part A explains it. |
| F7 (note) | The attribution "submitted by the maintainer" is supported and claims no ratification. | No change. |

The reviewer also confirmed that the change touches nothing under `records/`, `specification/`,
`schemas/`, `skills/`, `tests/` or `decisions/`, and that it breaches no public boundary. This evidence
file is the one later addition under `decisions/evidence/`.

A second review, of `695c1a3`, is required before the pull request can be put forward for a merge
decision, because the commit changed after the first review.

## What this does not establish

- Not ratification of the controls, and not their adoption: that needs a decision record.
- Not continuous integration.
- Not a review by a person.
