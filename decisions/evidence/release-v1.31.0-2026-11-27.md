# Release record — v1.31.0

The release record [TDR-0042](../TDR-0042-changelog-headings-are-not-releases.md) requires: one tag,
one release record, one changelog entry. This is it. It records the authorised act and the evidence at
the act. The tag and the GitHub Release are created after the commit that adds this record, so this
record names them and does not evidence them.

## The authorised act

| Element | Evidence |
|---|---|
| Actor | Sailesh Panchal |
| Authority | Maintainer and repository authority for MTDR |
| Date | 2026-11-27 |
| Act | Authorised publication of MTDR v1.31.0, **with a one-off exception to the agreed CI requirement**: GitHub Actions is disabled for the account, so hosted Ubuntu and macOS CI could not run. The exception is not a claim that CI passed |
| Release content | `c649049bb45bdc8f8317534d1b551aa7fffef86d`, the ratified release candidate (`release/next-candidate`), merged into `main` by `b6a91a62f1c36abacd80efa1d1b4b68480f7b8d0`, which keeps the CI bootstrap from #24 |
| Commit | The commit on `main` that adds this record |
| Tag | `v1.31.0`, to be created at that commit |
| GitHub Release | To be published from that tag |
| Eligibility at the act | `transition-eligibility: indeterminate`, on `DAC-0032#4` alone: external validation, which [TDR-0045](../TDR-0045-external-validation-follows-publication.md) places after publication. It is not a failed pre-publication gate, and it is not a completed validation |
| Preceded by | Ratification of TDR-0050, DAC-0048, TDR-0048 and TDR-0049 on 2026-11-27, four separate acts, each with its evidence note in `decisions/evidence/` |

## The owner's authorisation, verbatim

> I authorise proceeding with publication despite GitHub Actions being unavailable at account level.
> This is a one-off, owner-approved exception to the previously agreed CI requirement. It is not a
> claim that CI passed.

The direction also required: integrate `c649049bb45bdc8f8317534d1b551aa7fffef86d` into `main`,
keeping the CI bootstrap; finalise this record and the changelog, and run the existing local
verification against the final integrated commit; record that Linux verification passed locally while
hosted CI remained unavailable; create the tag at the final integrated commit and publish the GitHub
Release; preserve the documented capability maturity levels and outstanding confirmation obligations;
and claim no external validation, which remains a post-publication activity under TDR-0045.

## The version, and why it is a minor one

`v1.31.0` is a minor version because every change since `v1.30.0` is additive for records already
written:

- **The Decision and Value languages are unchanged** in what a record must contain and in which
  records validate. Their specifications, schemas, templates and worked examples are byte-identical
  to `v1.30.0`. A probe of the identity check (a Value Record bound to `vr@1.3.0`) is rejected
  exactly as `v1.30.0` rejects it.
- **Some existing text was edited in place for decision recovery**: the decision package's admission
  test and semantic roles, five existing skills (three of them shared with the value language), and
  three shared specifications. These edits change how a candidate is interpreted, not how a record
  validates. They belong to the four recovery records, ratified on 2026-11-27. One reaches authored candidates: admission criterion 2 now treats
  same-day context as indeterminate unless it is shown to have been before whoever acted.
- **Decision recovery is new.** It brings new specifications (`historical-recovery.md`,
  `historical-candidate.md`), a new schema, five new decision-language skills, a new grouping basis
  in `candidate-assembly.md` (1.1.0), the installer and the folder validator. Its records were
  ratified on 2026-11-27.
- **The experimental package state** (TDR-0047) and the Inheritance package are new, and are not part
  of the standard.

The owner's condition of 27 November kept the version proposed until compatibility checks established
that no breaking change had been introduced. They did, and the owner then authorised publication as
v1.31.0.

**Compatibility checks, 27 November 2026.** Run on the candidate after the owner's direction of 27 November was applied.

| Check | Result |
|---|---|
| Governed records present at `v1.30.0` | None modified; six added (TDR-0046 to TDR-0050, DAC-0048) |
| Decision and Value specifications, schemas, templates and worked examples | Byte-identical to `v1.30.0` |
| `record-identity.md` and the identity check | Identical to `v1.30.0`; the `vr@1.3.0` probe is rejected as `v1.30.0` rejects it |
| The shared candidate-assembly schema | One enumeration value added (`singleton`); every assembly valid under 1.0.0 stays valid |
| `v1.30.0`'s tests over the candidate | The same 13 known failures, all from the experimental package state |

**What does change is interpretation, not validity.** Admission criteria 2 and 6, five existing skills and
FIX-301's expected answers change how a candidate is interpreted, under the ratified recovery records.
No record valid under `v1.30.0` becomes invalid. On this evidence no breaking change has been found.

## What is claimed

> **v1.31.0 adds decision recovery to the decision language, ratified, and publishes the Operational
> Inheritance Record as an experimental package. Decision and Value are normative; decision recovery is
> normative within the decision language; Authority and Evidence remain candidates. The release is
> verified locally, on Linux, against its own published contracts; hosted CI did not run. External
> validation is not yet claimed and will be gathered through use.**

Under [DAC-0045](../DAC-0045-external-validation-follows-publication.md) constraint 1, no release note,
README or announcement may claim external validation, proven adoption, ease of installation or
usability while `DAC-0032#4` is outstanding.

## Status of each capability

| Capability | Status |
|---|---|
| Decision (TDR, DAC) | Normative |
| Value (VR) | Normative |
| Decision recovery | Normative within the decision language: DAC-0048, TDR-0048, TDR-0049 and TDR-0050 ratified on 2026-11-27 |
| Inheritance (OIR) | Experimental: published for review, excluded from every claim |
| Authority (OAR) | Candidate: scope only |
| Evidence (OER) | Candidate: scope only |

## Known limitations

Each is tracked, and none is resolved by wording in this release.

| Limitation | Tracked in |
|---|---|
| A proposed TDR that honestly marks a required value as unknown fails the TDR schema | [#14](https://github.com/saileshpanchal/mtdr/issues/14) |
| Authoring a new decision and recovering a historical one are not yet separated for a newcomer | [#15](https://github.com/saileshpanchal/mtdr/issues/15) |
| What `status: proposed` means when the decision itself was already approved | [#16](https://github.com/saileshpanchal/mtdr/issues/16) |
| `confirmed_by_outcome` when no review was set | [#17](https://github.com/saileshpanchal/mtdr/issues/17) |
| No package manifest declares `specification/record-identity.md` | [#18](https://github.com/saileshpanchal/mtdr/issues/18) |
| No rule says whether an editorial change to a specification changes its version | [#19](https://github.com/saileshpanchal/mtdr/issues/19) |
| Copying skills flat into an agent's skills folder breaks their links; the installer supports Claude Code and Hermes only | `skills/packaging/` |
| A later minor version of a specification would fail records bound to the earlier one; the fix (`0650856`) is held out for a governed decision | This record |
| `v1.30.0`'s own tests report 13 failures, all from the experimental package state it predates | This record |
| Hosted CI on Ubuntu and macOS did not run: GitHub Actions is disabled for the account. Verification is local, on Linux only | This record |

## Obligations carried, not discharged

| Obligation | Gates | State |
|---|---|---|
| `DAC-0032#4` — zero-install proof by a participant unknown to the author | `externally-validated` | Outstanding |
| `DAC-0032#5` — registration and export round trip | `registered` | Not applicable here; belongs to a register operator |
| DAC-0048 debt row 5 — a further independent confirmation of decision recovery | TDR-0049's confirmation | Outstanding. The confirmation of 26 November is limited internal confirmation evidence |
| `confirmed_by_outcome` of TDR-0048, TDR-0049 and TDR-0050 | Each record's confirmation | Pending; a review date confirms nothing |

## Evidence at the act

Run on the final integrated tree, the commit that adds this record, before the tag was created. **All
local, on Linux (x86_64, CPython 3.13.18). None of it is hosted CI.**

| Check | Result |
|---|---|
| `uv run tests/verify.py` (uv 0.11.32) | Exit 0. Structural, semantic and relational pass; transition eligibility indeterminate on `DAC-0032#4`, as above; 1,286 links checked |
| `uv sync --locked`, then `uv run tests/verify.py`, with uv 0.13.9, the version the workflows pin | Both exit 0 |
| `python -m mtdr_packaging.generate --check` | 30 skills, 0 problems |
| `v1.30.0`'s tests over the tree | The same 13 known failures (7 bundle, 4 skill-count, 1 manifest, 1 identity), all from the experimental package state |
| The installer: `decision` and `value`, for Claude Code | Install and verify; each package reports version 1.31.0 |
| **Hosted CI, Ubuntu and macOS** | **Did not run.** The workflow `verify-candidate` (id 432757756) is registered and active on `main`; a dispatch against `c649049` on 27 November, at about 13:15 UTC, was refused by GitHub: *"Actions has been disabled for this user."* No workflow run exists |
| History of the commits this release adds to `main` | Scanned for session links, local paths and credentials: none. Commits written by the assistant are attributed to `Claude <noreply@anthropic.com>`; the others carry the maintainer's established identity, under the exception recorded on #22 |

The reviews behind the release: PR #22's independent review and its follow-ups; the review of the
recovery records, its targeted re-review and the responses; the readability review and its responses;
and the confirmation of decision recovery of 26 November, which is limited internal confirmation
evidence and not external validation.

## After publication

Independent practitioners are invited to test the release without assistance and to report through
the [independent trial report](https://github.com/saileshpanchal/mtdr/issues/new?template=independent-trial-report.md).
The first planned exercises use only the published release and a separately supplied evidence
corpus: Hermes, then a fresh Claude session, then Microsoft Copilot. They do not gate publication,
and none of them is a participant unknown to the author, so none discharges `DAC-0032#4` by itself.
