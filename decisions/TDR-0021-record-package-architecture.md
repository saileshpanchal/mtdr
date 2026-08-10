---
id: TDR-0021
title: Adopt the record-package architecture — packages follow organisational languages, and dependent artefacts live with the language they serve
status: accepted
template: full
decision_date: 2026-08-10
accountable_owner: Sailesh Panchal
confidence: high
maturity: proposed
supersedes: none
derived_from: TDR-0008, TDR-0009, TDR-0017, TDR-0018, TDR-0020
confirmed_by_outcome: pending — review when a record package has been extracted into an independently governed repository, or when the first candidate language passes admission, whichever is sooner; else 2027-02-10
---

# TDR-0021 — Adopt the record-package architecture: packages follow organisational languages, and dependent artefacts live with the language they serve

## Context — what was known at the time

The repository's artefacts were organised by *kind* — all specs at root, all schemas in `schema/`, all templates in `templates/`, all skills in `skills/` — which was right for one record type and wrong for five languages. Growing that layout means every language's semantics smeared across six directories, and no way to answer the question that decides whether the standard can federate: *could this record type become an independently governed standard tomorrow?*

Three record types are shipped (TDR, VR, DAC). Three candidate languages (authority, work, evidence) sit under an admission discipline and have accumulated research standing without repository presence. And one classification question had no recorded answer: the DAC has its own specification and schema, yet its `tdr_id` is mandatory, its lifecycle is coupled to the TDR's, and its purpose is assurance *over* a decision — so is it a peer language or part of one?

## Decision

1. **The architectural unit is the record package, and top-level packages correspond to organisational languages** — not to schemas, and not to artefact types. The five languages and their packages:

   | Language package | Primary record | Associated artefacts / practice |
   |---|---|---|
   | `records/decision/` | TDR | DAC + the eight assurance skills |
   | `records/value/` | VR | value-specific challenge and validation |
   | `records/authority/` *(candidate)* | OAR | authority practice |
   | `records/work/` *(candidate)* | OIR | JTBD / work practice |
   | `records/evidence/` *(candidate)* | OER | evidence projection and validation |

   There is no sixth family for events, fragments, observations or runtime state.

2. **A language package may contain subordinate artefact types where those artefacts are semantically dependent on the primary record.** The classification test for anything new, in order:
   1. Does the artefact express a distinct class of organisational meaning?
   2. Can it exist independently of another record family?
   3. Can its package be extracted and remain semantically complete?
   4. Does it have an independent lifecycle — rather than merely assuring, qualifying or projecting another record?

   **The DAC fails 2–4 and therefore lives inside `records/decision/`.** It is the decision language's assurance discipline, not a sixth language, and extracting the decision package must yield a complete decision-language implementation including its assurance practice.

3. **The extraction test is the package-boundary test**: any `records/<language>/` must be extractable tomorrow into an independently governed repository without redesigning the record. If it cannot, the boundary is wrong. A package may depend *downward* on the common substrate — `specification/`, `schemas/shared/`, `skills/shared/` — and never *sideways* on another package. Cross-language fixtures live in `tests/`, outside every package.

4. **A package may exist before its language is admitted, but candidate packages contain metadata and scope only** — identity, semantic scope, `status: candidate`, and a statement that the admission test has not been passed. No normative specification, schema, template, examples, validation rules or skills until admission succeeds. Architectural reservation is thereby separated from semantic admission, and a directory confers no maturity.

## Evidence

- **Business** — federated governance is the credible endgame for a record family standard: value or authority may plausibly acquire their own communities. A layout that cannot federate forecloses that silently.
- **Architecture** — the extraction and no-sideways-links rules are both mechanically checkable, and become part of the verification suite. TDR-0009 already committed a fourth record type to "inherit the sibling conventions or argue against them"; this record is where those conventions become structural.
- **Regulatory** — not material to this decision.
- **Operations** — a contributor to the value language touches one directory. Review scope equals package scope.
- **Customer** — not material to this decision.
- **Data** — none beyond the records themselves.
- **External** — monorepo-with-extractable-modules is the pattern proven by every standards body that later federated; the counter-pattern (one entangled spec) is why some never could.

## Alternatives rejected

1. **Keep organising by artefact kind.** Rejected: five languages across six kind-directories is thirty locations for five coherent things.
2. **DAC as its own package.** Rejected by the classification test: it would create an "extractable" package every record of which carries a mandatory foreign key into another package — extraction theatre.
3. **One repository per language now.** Rejected as premature federation: three languages are not yet admitted, and cross-language discipline (the contribution model, conformance) is still forming. The package boundary keeps the option open at near-zero cost.
4. **No candidate directories until admission.** Rejected: the extension contract would have no worked expression, and the five-language settlement would be visible only in prose. The metadata-only rule removes the false-maturity risk that motivated this alternative.

## Options foreclosed

- No future artefact type gets a top-level package without passing the four-question classification test.
- Package-to-package dependencies are permanently inadmissible; anything two packages need becomes substrate.
- Candidate packages cannot accumulate normative artefacts "temporarily" — admission first, artefacts second.

## Consequences and review

Success looks like the extraction drill passing for every shipped package at every release, and the first candidate admission landing as *additions to an existing empty package* rather than a restructure. Review per the confirmed-by-outcome trigger.
