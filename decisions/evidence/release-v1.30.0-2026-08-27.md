# Release record — v1.30.0

The release record [TDR-0042](../TDR-0042-changelog-headings-are-not-releases.md) requires: one tag,
one release record. This is it.

## The authorised act

| Element | Evidence |
|---|---|
| Actor | Sailesh Panchal |
| Authority | Maintainer and repository authority for MTDR |
| Date | 2026-08-27 |
| Act | Authorised the governed transition `pre-release` → `released` |
| Tag | `v1.30.0` |
| Eligibility at the moment of the act | `transition-eligibility: pass` — thirteen gating obligations, all verified |
| Preceded by | Ratification of TDR-0045, taken as a separate act |

**Eligibility is not authority.** `pass` meant the published prerequisites were met and the request
could be placed before whoever decides it ([TDR-0037](../TDR-0037-release-eligibility-from-standing-governance.md)).
The decision was this act, not the computation.

## What is claimed

> **v1.30.0 is the first governed public release of MTDR. It is structurally, semantically and
> relationally verified against its own published contracts. External zero-install adoption evidence
> is not yet claimed and will be gathered through use.**

That wording is fixed by TDR-0045 and narrowed by DAC-0045 constraint 1. **Any wider claim is false**
— including any claim of external validation, proven adoption, ease of installation or usability.

## What is outstanding, and carried rather than hidden

Two obligations from DAC-0032 remain, both surfaced in every validation result under the code
`carried-not-gating`:

| Obligation | Gates | State |
|---|---|---|
| `DAC-0032#4` — zero-install proof by a participant unknown to the author | `externally-validated` | `release-gated`, outstanding |
| `DAC-0032#5` — registration/export round-trip | `registered` | `not-applicable` here; belongs to a register operator |

Neither is discharged, weakened or deleted. Re-scoping changed **when** each blocks, never whether it
exists ([TDR-0044](../TDR-0044-transition-scoped-obligations.md),
[TDR-0045](../TDR-0045-external-validation-follows-publication.md)).

## What the repository now reports about itself

```
subject: repository mtdr · assessed_state: released
requested_transition: released → externally-validated

  structural               pass
  semantic                 pass
  relational               pass
  transition-eligibility   indeterminate — DAC-0032#4 — Zero-install proof: verification release-gated
```

The fourth line is the point. Having released, the repository immediately reports that it is **not
yet eligible for the next transition**, and names why. A release that reported nothing further to
prove would be claiming more than this one does.

## The first external cohort

The author's business architecture team will follow the published instructions uncoached. Under
DAC-0045 constraint 6 their trial is **admissible evidence that does not by itself discharge
`DAC-0032#4`**: they are independent of the authoring role but not unknown to the author. Their
result is to be recorded with its provenance — who ran it, what they were given, what they were not
told, and their raw output rather than a summary — whatever it says. A failure is the more useful
outcome.

## Preceded by

- `baseline-2026-08-21` — the pre-release baseline, which stated it was not this transition.
- Thirty changelog headings, 1.0.0 – 1.29.0, classified as unreleased development labels by TDR-0042.
  **This is the first release. It is not the thirty-first.**
