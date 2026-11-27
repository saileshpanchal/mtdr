# Release record — v1.31.0 (DRAFT)

> **Draft for the maintainer's decision. This is not a release record.** It becomes one only when the
> maintainer authorises the release, at which point the commit, the tag and the date are filled in and
> this banner is removed ([TDR-0042](../TDR-0042-changelog-headings-are-not-releases.md): one tag, one
> release record, one changelog entry). Preparing it ratifies nothing and authorises nothing.

## The proposed act

| Element | Evidence |
|---|---|
| Actor | *To be completed: the maintainer* |
| Authority | Maintainer and repository authority for MTDR |
| Date | *To be completed* |
| Act | *To be completed: authorise publication of the release candidate as v1.31.0* |
| Commit | *To be completed: the exact release-candidate commit approved* |
| Tag | `v1.31.0`, proposed |
| Preceded by | Ratification of TDR-0050, DAC-0048, TDR-0048 and TDR-0049 on 2026-11-27, four separate acts, each with its evidence note in `decisions/evidence/` |

## The version, and why it is a minor one

`v1.31.0` is proposed because every change since `v1.30.0` is additive for records already written:

- **The Decision and Value languages are unchanged** in what a record must contain and in which
  records validate. Their specifications, schemas, templates and worked examples are byte-identical
  to `v1.30.0`. A probe of the identity check (a Value Record bound to `vr@1.3.0`) is rejected
  exactly as `v1.30.0` rejects it.
- **Some existing text was edited in place for decision recovery**: the decision package's admission
  test and semantic roles, five existing skills (three of them shared with the value language), and
  three shared specifications. These edits change how a candidate is interpreted, not how a record
  validates. They belong to the four recovery records and stand only if those are ratified; each record
  lists what a return would revert. One reaches authored candidates: admission criterion 2 now treats
  same-day context as indeterminate unless it is shown to have been before whoever acted.
- **Decision recovery is new.** It brings new specifications (`historical-recovery.md`,
  `historical-candidate.md`), a new schema, five new decision-language skills, a new grouping basis
  in `candidate-assembly.md` (1.1.0), the installer and the folder validator. It is part of the
  release only once its records are ratified.
- **The experimental package state** (TDR-0047) and the Inheritance package are new, and are not part
  of the standard.

The version stays proposed until it is confirmed against compatibility and governance requirements,
and the owner's condition of 27 November keeps it proposed until compatibility checks establish that
no breaking change has been introduced.

**Compatibility checks, 27 November 2026.** Run on the candidate after the owner's direction of 27 November was applied.

| Check | Result |
|---|---|
| Governed records present at `v1.30.0` | None modified; six added (TDR-0046 to TDR-0050, DAC-0048) |
| Decision and Value specifications, schemas, templates and worked examples | Byte-identical to `v1.30.0` |
| `record-identity.md` and the identity check | Identical to `v1.30.0`; the `vr@1.3.0` probe is rejected as `v1.30.0` rejects it |
| The shared candidate-assembly schema | One enumeration value added (`singleton`); every assembly valid under 1.0.0 stays valid |
| `v1.30.0`'s tests over the candidate | The same 13 known failures, all from the experimental package state |

**What does change is interpretation, not validity.** Admission criteria 2 and 6, five existing skills and
FIX-301's expected answers change how a candidate is interpreted, and only if the recovery records are
ratified. No record valid under `v1.30.0` becomes invalid. On this evidence no breaking change has
been found. The version stays proposed until the owner authorises publication.

## What is claimed

> **v1.31.0 adds decision recovery to the decision language, and publishes the Operational
> Inheritance Record as an experimental package. Decision and Value are normative; Authority and
> Evidence remain candidates. The release is verified against its own published contracts. External
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

## Obligations carried, not discharged

| Obligation | Gates | State |
|---|---|---|
| `DAC-0032#4` — zero-install proof by a participant unknown to the author | `externally-validated` | Outstanding |
| `DAC-0032#5` — registration and export round trip | `registered` | Not applicable here; belongs to a register operator |

## Evidence to be attached at the act

*To be completed against the exact approved commit:*

- the repository suite, from a clean clone, with its four-dimension result;
- a GitHub Actions run on Linux and macOS, with its URL;
- `v1.30.0`'s tests over the commit, compared with `release/next`;
- the bundle check and the installer's verification of the `decision` and `value` packages;
- the history scan of the commits the release adds to `main`;
- the independent reviews: PR #22 and its follow-ups, the review of the recovery records, the
  confirmation of decision recovery of 26 November, which is limited internal confirmation evidence
  and not external validation, and the readability review.

## After publication

Independent practitioners are invited to test the release without assistance and to report through
the [independent trial report](https://github.com/saileshpanchal/mtdr/issues/new?template=independent-trial-report.md).
The first planned exercises use only the published release and a separately supplied evidence
corpus: Hermes, then a fresh Claude session, then Microsoft Copilot. They do not gate publication,
and none of them is a participant unknown to the author, so none discharges `DAC-0032#4` by itself.
