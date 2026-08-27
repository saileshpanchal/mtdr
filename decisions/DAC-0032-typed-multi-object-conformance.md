---
id: DAC-0032
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0032
title: Assure typed multi-object conformance and the optional register boundary
status: accepted
disposition: proceed-with-constraints
assessed_at: 2026-08-13
accountable_owner: Sailesh Panchal
review_date: 2026-09-13
confidence: medium
supersedes: none
---

# DAC-0032 — Assure typed multi-object conformance and the optional register boundary

> **Standing carried forward 2026-08-16.** Human review confirmed this case preserves the accepted
> Gate-B DAC-0020 findings, constraints, exclusions and scope while rebinding them to TDR-0032 under
> TDR-0031. This is an accepted representation of the earlier assurance ruling, not a new assurance
> judgement and not authorisation to release.

## Uncertainty

Known: a mandatory register creates an implicit runtime dependency; a context-free file lacks the
versioned semantic context required for an independently verifiable claim; record, package, skill,
execution, collection and repository obligations differ. Unknown: the portable record-version
binding, the classified normative closure of each package and the eventual collection contract.
Assumption: typed claims and durably resolvable dependencies can preserve portability without
making every record a self-contained archive. Confidence is medium pending the proving exercises.

## Adversarial projection

Routed for boundary and authority abuse. A supplier may advertise generic "MTDR conformance" while
passing only schema validation, present a valid skill file as proof of conforming agent behaviour,
or claim that storing records makes them accepted. Controls are typed claims, explicit
non-implication, TDR-0027 standing evidence and must-not tests. Residual exposure is owned by the
standard maintainer and each future collection-contract owner.

## Customer-outcome projection

Not directly material at standards-repository level. Indirect harm arises if portability claims
cause adopters to accept incomplete governance or if a mandatory platform excludes smaller users.

## Control side-effects

Making the register optional for record and package claims may be misread as removing governance.
Conversely, context requirements can grow until a supposedly independent record needs the whole
repository. Dependency classification and typed claims must preserve the middle without turning
documentation and historical links into accidental normative closure.

## Execution capability

The repository can enforce some typed distinctions and package structure locally, but cannot yet
support all ratified claims. Record instances do not identify their governing specification
version; package links are unclassified; no independent clean-clone or complete extraction proof
exists; and collection conformance has no normative contract. These gaps constrain implementation
and release, not the architectural judgement.

## Risk delta and declared interactions

The decision decreases platform dependency and category errors while increasing version,
dependency and claim-governance complexity. It interacts with TDR-0012, TDR-0021, TDR-0023,
TDR-0025 and TDR-0027. Risk remains unstable until record binding, extraction and round-trip proofs
exist, but the prohibition on generic claims reduces immediate ambiguity.

## Risk vector

| Axis | Assessment and basis |
|---|---|
| severity | high — the boundary determines what every adopter must trust |
| likelihood | medium — artefact and collection concerns are already conflated |
| exposure volume | high — repository-wide and inherited by every package |
| velocity | medium — copied artefacts spread quickly |
| concentration | high — one boundary rule governs all consumers |
| detectability | medium — typed scans expose generic claims; hidden dependency and behaviour drift require trials |
| reversibility | medium-low after external adoption |
| control confidence | medium-low — architectural separations are clear; proving mechanics are incomplete |
| customer-cohort distribution | portability helps small adopters; governance ambiguity harms least-supported users first |
| time horizon | first independent use through the first collection integration |
| trend | stabilising under claim and release constraints |

## Decision debt

- Define how a detached record durably identifies its record type, applicable specification identity and version — owner Sailesh Panchal, due 2026-09-13.
- Classify package dependencies as normative, conformance, provenance, explanatory, navigation or historical and prove normative closure after extraction — owner Sailesh Panchal, due 2026-09-13.
- Run a clean-clone zero-install trial with a participant unknown to the author and no maintainer intervention — owner Sailesh Panchal, due before public release.
- Run registration and export round-trips proving semantics, conformance and standing do not change merely through storage — owner Sailesh Panchal, due before public release.
- Define and separately govern a testable collection contract covering identity, specification context, lineage, standing evidence, lifecycle integrity, no manufacture of standing, portability and export — owner Sailesh Panchal, due before any normative collection-conformance claim.
- Add must-not evidence for generic claims, cross-level implication, storage-created authority and conforming-skill/non-conforming-execution cases — owner Sailesh Panchal, due before public release.

## Monitoring contract

- Hypothesis: every conformance claim names its object and applicable contract; a clean-clone user
  can produce a version-bound conforming record without a service; an extracted package retains
  normative closure; and registration/export changes neither semantics nor standing.
  Counter-hypothesis: a generic claim passes, hidden context or orchestration is necessary, or the
  round-trip changes meaning or authority. Test: scan normative claims, run the clean-clone and
  extraction exercises, then compare pre-registration and post-export artefacts and standing
  evidence. Metric is generic claims, undocumented normative dependencies and material semantic or
  standing differences; threshold is one; owner Sailesh Panchal; trigger is block release, prohibit
  the affected claim and reopen TDR-0032 if the architecture itself is falsified.

## Learning obligations

Retain the dependency classification, full clean-clone, extraction and round-trip transcripts,
including confusion about conformance subjects and standing. Record every hidden dependency and
cross-level inference rather than helping the participant around it.

## Disposition

**Proceed with constraints.** The typed multi-object architecture is supportable; release and some
claim types are not yet supportable. The constraints are:

1. **Typed normative claims only.** Owner: Sailesh Panchal. Measure: normative surfaces contain no
   generic "MTDR conformant" claim without naming record, interchange, package, skill,
   participant/implementation, collection or repository as the subject.
2. **Version-bound detached records.** Owner: Sailesh Panchal. Measure: before release, a detached
   record can identify and durably resolve its record type, applicable specification identity and
   version, and validate without repository-private interpretation.
3. **Classified normative closure.** Owner: Sailesh Panchal. Measure: every package dependency is
   classified and an extracted package passes its applicable conformance contract with no
   undocumented normative dependency; the complete corpus may remain durably referenced.
4. **Zero-install proof before release.** Owner: Sailesh Panchal. Measure: a participant unknown to
   the author produces and validates the claimed objects from a clean distribution without an MTDR
   application, register, service or maintainer intervention.
5. **Registration/export round-trip before release.** Owner: Sailesh Panchal. Measure: pre-entry and
   post-export comparisons show no material change in semantics, conformance or standing, and
   storage alone produces no `accepted` transition.
6. **No collection-conformance advertising yet.** Owner: Sailesh Panchal. Measure: no normative
   "MTDR-conformant register/collection" claim until a separately governed, testable collection
   contract covers identity, specification context, lineage, standing evidence, lifecycle
   integrity, no manufacture of standing, portability and export.
7. **Narrow lineage preserved.** Owner: Sailesh Panchal. Measure: TDR-0012 remains immutable
   historical evidence; TDR-0032 displaces only register-as-universal-minimum and explicitly retains
   runtime neutrality, optional consumers and the register as a valid pattern.

Skills run: systems-thinking, counterfactual-and-evidence, accumulated-and-resultant-risk,
fraud-and-adversarial-thinking, customer-outcomes (light), systems-dynamics, adaptive-capacity and
assurance-synthesis.
