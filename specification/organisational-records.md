# Organisational records — the umbrella specification

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

This repository defines **governed organisational records**: portable, markdown-serialised memory of
the organisational objects that carry accountability — decisions, value commitments, and the further
languages admitted over time. This document is the map; each language's normative semantics live in
its own package under [`records/`](../records/).

## What a governed organisational record is

A record is the **governed memory of one organisational object**. The object is the thing the
organisation did or undertook — a consequential decision, an operational value commitment. The record
is how that object is preserved: a single markdown file with YAML frontmatter for machine-readable
fields and a body for human judgement, carrying a named accountable individual, the context as it
stood, and lineage to the records before and after it.

Three properties hold across every language, and removal of any of them is a different standard, not
a new version:

1. **Accountability core** — a named individual, time-of-decision context, stated confidence,
   evidence, foreclosure, lineage.
2. **Supersede, never edit** — records are immutable once they acquire standing; changes of judgement
   are new records with `supersedes:` set. Lifecycle facts (status transitions, observed outcomes,
   counter-signatures) are the only in-place changes.
3. **Capture confers nothing** — a record enforces nothing, authorises nothing, and proves nothing
   beyond what its evidence carries.

## The language model

The unit of the standard is the **organisational language**: one class of organisational meaning, one
primary record type, one package ([TDR-0021](../decisions/TDR-0021-record-package-architecture.md)).

| Language package | Primary record | Status | Associated artefacts / practice |
|---|---|---|---|
| [`records/decision/`](../records/decision/) | **TDR** — the unit of judgement | Normative | DAC + the assurance skills |
| [`records/value/`](../records/value/) | **VR** — governed memory of an Operational Value Commitment | Normative | value challenge and validation |
| [`records/authority/`](../records/authority/) | OAR | **Candidate** | authority practice |
| [`records/work/`](../records/work/) | OIR | **Candidate** | JTBD / work practice |
| [`records/evidence/`](../records/evidence/) | OER | **Candidate** | evidence projection and validation |

There is **no sixth family** for events, fragments, observations or runtime state. Operational
reality produces source material; the [contribution model](contribution-model.md) interprets it; and
whatever consumes completed records is outside this repository entirely
([TDR-0020](../decisions/TDR-0020-open-organisational-record-repository-boundary.md)).

A language package may contain subordinate artefact types that are semantically dependent on its
primary record — the Decision Assurance Case lives inside the decision package on exactly this rule.
Whether something is a new language or a dependent artefact is decided by the
[record admission test](record-admission-test.md), never by a directory appearing.

## The substrate

This directory and its companions are the record-neutral layer every package builds on:

| Concern | Where |
|---|---|
| The contribution model — fragments, contributions, candidate assemblies | [`contribution-model.md`](contribution-model.md) and its structure files |
| Provenance | [`provenance.md`](provenance.md) |
| Identity and grouping — proximity is never identity | [`identity-and-grouping.md`](identity-and-grouping.md) |
| Temporal semantics | [`temporal-semantics.md`](temporal-semantics.md) |
| Uncertainty — three confidences, never collapsed | [`uncertainty.md`](uncertainty.md) |
| Candidacy and ratification — the skill proposes, the organisation ratifies | [`candidacy-and-ratification.md`](candidacy-and-ratification.md) |
| Admission of new languages and artefacts | [`record-admission-test.md`](record-admission-test.md) |
| What conformance means | [`conformance.md`](conformance.md) |
| Interchange schemas | [`schemas/shared/`](../schemas/shared/) |

**The dependency rule**: a package may depend downward on this substrate and never sideways on
another package. Anything two packages need becomes substrate, by a recorded decision.

## The boundary

The standard ends at the artefact. Its output is standards-conformant portable files, with enough
provenance to understand how each was derived. How those files are stored, indexed, connected,
projected, reasoned over or used is the adopter's business, and this repository neither knows nor
constrains it. See [TDR-0018](../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md)
and [TDR-0020](../decisions/TDR-0020-open-organisational-record-repository-boundary.md), and
[`GOVERNANCE.md`](../GOVERNANCE.md) for how this repository governs itself.
