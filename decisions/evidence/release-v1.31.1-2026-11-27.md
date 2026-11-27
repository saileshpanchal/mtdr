# Release record — v1.31.1

The release record [TDR-0042](../TDR-0042-changelog-headings-are-not-releases.md) requires: one tag,
one release record, one changelog entry. This is it. It records the authorised act and the evidence at
the act. The tag and the GitHub Release are created after this record reaches `main`, so this record
names them and does not evidence them.

v1.31.1 is a patch. It corrects text in v1.31.0 and names the source of one quotation. What a record
must contain, and which records validate, are as they were in v1.31.0.

## The authorised act

| Element | Evidence |
|---|---|
| Actor | Sailesh Panchal |
| Authority | Maintainer and repository authority for MTDR |
| Date | 2026-11-27 |
| Source | The owner's written instruction to the maintainer's assistant, 2026-11-27 at 17:55 UTC |
| Act | Authorised publication of MTDR v1.31.1 while hosted CI is unavailable, **as this release's own exception**. The exception given for v1.31.0 was a one-off and is not carried forward. Neither exception is a claim that CI passed |
| Release content | `1e80e3f882cf5cfef529fdcfc41f53069678aeb4`: `main` after [#26](https://github.com/saileshpanchal/mtdr/pull/26) was merged on the maintainer's authorisation. It adds three commits to v1.31.0: `aef2bf0`, `f9f57f9` and `c173847` |
| Commit | The merge commit that brings this record to `main`. Its tree is the tree of the commit that adds this record |
| Tag | `v1.31.1`, to be created at that merge commit |
| GitHub Release | To be published from that tag |
| Eligibility at the act | `transition-eligibility: indeterminate`, on `DAC-0032#4` alone: external validation, which [TDR-0045](../TDR-0045-external-validation-follows-publication.md) places after publication. Unchanged from v1.31.0 |
| Preceded by | v1.31.0, published on 2026-11-27, and the review of it recorded in [#25](https://github.com/saileshpanchal/mtdr/issues/25) |

## The owner's authorisation, verbatim

The instruction opens:

> MTDR v1.31.1 — Patch release authorisation
> Proceed with publishing v1.31.1 from the merged Issue #25 corrections.

On hosted CI it says:

> Record that hosted GitHub CI remains unavailable. This patch release requires its own explicit
> exception; do not carry forward the v1.31.0 exception silently.

The exception for this release is that instruction. It directs publication while hosted CI is
unavailable, and it requires this record to say so in its own right.

The instruction also required: confirm that `main` contains #26 at `1e80e3f`; create this record and
the changelog entry, describing the editorial corrections and the provenance clarification; regenerate
versioned distribution metadata where required, without changing the Decision or Value
specifications, schemas, record versions or normative semantics; run the full local verification
suite and the packaging checks against the final release commit; create the annotated tag at the
exact verified commit and publish the GitHub Release; verify that the tag, this record, the changelog
and the Release identify the same version and commit; close #25 with the release and verification
references; preserve the v1.31.0 tag and release; and introduce no new methodology, governance or
functional change.

## The version, and why it is a patch

Every change since `v1.31.0` corrects text. Eleven files differ, by 17 lines added and 14 removed,
before this record, the changelog entry and the regenerated provenance stamp.

- **Two indexes said four ratified records were proposed.** `GOVERNANCE.md` and `decisions/README.md`
  now list TDR-0048, TDR-0049, TDR-0050 and DAC-0048 as the records themselves do.
- **Six status markers said "proposed under" a ratified record.** Each changes one word, to "accepted
  under", the wording the ratification commits used for the same marker elsewhere.
- **Two dead links.** TDR-0048 and TDR-0049 each linked to a section removed when they were ratified.
  The link is replaced by a bracketed note saying where that list stands. The dated statements around
  it, "It stays proposed" among them, are unchanged.
- **One source named.** The v1.31.0 release record quoted the owner's authorisation and gave no source
  for it. It now has a Source row, marked as added after publication. The quotation was checked
  against the owner's instruction and is word for word, as are the quotations in the four
  ratification notes, which are unchanged.

**Compatibility checks, 27 November 2026.**

| Check | Result |
|---|---|
| Governed records | None added or removed. TDR-0048 and TDR-0049 differ only by the link repair in an opening note; their frontmatter, decisions and evidence are untouched |
| The TDR, DAC and VR specifications; every schema, template and worked example; every skill | Byte-identical to `v1.31.0` |
| `decision-contribution.md` (1.0.0), `contribution-model.md` (1.1.0), `semantic-roles.md` | One word each, in a sentence stating a ratified record's standing. No version moves, and [#19](https://github.com/saileshpanchal/mtdr/issues/19) stays open |
| Fixtures | One word each in the decision fixtures' README and in FIX-004. No expected answer changes |
| The suite | One comment in `tests/verify.py`. No check changes |
| `v1.31.0`'s tests over this tree | Exit 0 |
| `v1.30.0`'s tests over this tree | The same 13 known failures, all from the experimental package state |

No record valid under `v1.31.0` becomes invalid, and none that was invalid becomes valid.

## What is claimed

> **v1.31.1 corrects text in v1.31.0 and names the source of one quotation. Decision and Value are
> normative; decision recovery is normative within the decision language; Authority and Evidence
> remain candidates; the Operational Inheritance Record is experimental. The release is verified
> locally, on Linux, against its own published contracts; hosted CI did not run. External validation
> is not yet claimed and will be gathered through use.**

Under [DAC-0045](../DAC-0045-external-validation-follows-publication.md) constraint 1, no release note,
README or announcement may claim external validation, proven adoption, ease of installation or
usability while `DAC-0032#4` is outstanding.

## Status of each capability

Unchanged from v1.31.0.

| Capability | Status |
|---|---|
| Decision (TDR, DAC) | Normative |
| Value (VR) | Normative |
| Decision recovery | Normative within the decision language: DAC-0048, TDR-0048, TDR-0049 and TDR-0050 ratified on 2026-11-27 |
| Inheritance (OIR) | Experimental: published for review, excluded from every claim |
| Authority (OAR) | Candidate: scope only |
| Evidence (OER) | Candidate: scope only |

## Known limitations

The limitations listed in the [v1.31.0 record](release-v1.31.0-2026-11-27.md#known-limitations) stand,
each where it is tracked. This release resolves none of them. Hosted CI on Ubuntu and macOS did not
run for this release either: verification is local, on Linux only.

## Obligations carried, not discharged

| Obligation | Gates | State |
|---|---|---|
| `DAC-0032#4` — zero-install proof by a participant unknown to the author | `externally-validated` | Outstanding |
| `DAC-0032#5` — registration and export round trip | `registered` | Not applicable here; belongs to a register operator |
| DAC-0048 debt row 5 — a further independent confirmation of decision recovery | TDR-0049's confirmation | Outstanding |
| `confirmed_by_outcome` of TDR-0048, TDR-0049 and TDR-0050 | Each record's confirmation | Pending; a review date confirms nothing |

## Evidence at the act

Run on the tree of the commit that adds this record, before the tag was created. **All local, on
Linux (x86_64, CPython 3.13.18). None of it is hosted CI.**

| Check | Result |
|---|---|
| `uv run tests/verify.py` (uv 0.11.32) | Exit 0. Structural, semantic and relational pass; transition eligibility indeterminate on `DAC-0032#4`, as above; 1,294 links checked |
| `uv sync --locked`, then `uv run tests/verify.py`, with uv 0.13.9, the version the workflows pin | Both exit 0 |
| `python -m mtdr_packaging.generate --check` | 30 skills, 0 problems |
| `v1.31.0`'s tests over the tree | Exit 0 |
| `v1.30.0`'s tests over the tree | The same 13 known failures (7 bundle, 4 skill-count, 1 manifest, 1 identity) |
| The installer: `decision` and `value`, for Claude Code | Install and verify; each package reports version 1.31.1 |
| **Hosted CI, Ubuntu and macOS** | **Did not run.** A dispatch of `verify-candidate` against `1e80e3f` on 27 November, at about 17:59 UTC, was refused by GitHub: *"Actions has been disabled for this user."* The pull request for the corrections, #26, started no run. No workflow run exists |
| History of the commits this release adds to `main` | Scanned for session links, local paths and credentials: none. Commits written by the assistant are attributed to `Claude <noreply@anthropic.com>`; the merge commits carry the maintainer's established identity |

The review behind the release is the fresh-context audit of v1.31.0 recorded in #25, and the editorial
review of its corrections on #26. Neither is external validation.

## After publication

The invitation in the v1.31.0 record stands: independent practitioners are asked to test a published
release without assistance and to report through the
[independent trial report](https://github.com/saileshpanchal/mtdr/issues/new?template=independent-trial-report.md).
