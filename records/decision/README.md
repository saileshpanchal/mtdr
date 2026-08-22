# Package — Decision

**Language:** decision · **Object:** `consequential-decision` — the unit of judgement
**Primary record:** `TDR` — Transformation Decision Record · **Status:** Normative

The decision language, complete: the record that preserves organisational judgement, and the
assurance discipline that challenges a decision's consequences before execution. The **Decision
Assurance Case (DAC)** lives here as a dependent artefact, not a sixth language — its `tdr_id` is
mandatory, its lifecycle is coupled to the TDR's, and its purpose is assurance over the decision
([TDR-0021](../../decisions/TDR-0021-record-package-architecture.md)). Extracting this package yields
a full decision-language implementation, assurance included.

## Contents

| Artefact | Location |
|---|---|
| TDR specification | [`specification/tdr.md`](specification/tdr.md) |
| DAC specification | [`specification/dac.md`](specification/dac.md) |
| Schemas | [`schema/tdr.schema.json`](schema/tdr.schema.json) · [`schema/dac.schema.json`](schema/dac.schema.json) |
| Templates | [`templates/`](templates/) — full · minimal · bare · dac |
| Worked examples | [`examples/`](examples/) — fictional, per `CONTRIBUTING.md` |
| Conformance fixtures | [`fixtures/`](fixtures/) — FIX-004 |
| Semantic roles (interpretation) | [`validation/semantic-roles.md`](validation/semantic-roles.md) |
| Admissibility test | [`validation/admission.md`](validation/admission.md) |
| The Consequential Decision Grammar | [`practice/decision-grammar.md`](practice/decision-grammar.md) — candidate authoring aid |
| Governance projection contract | [`schema/governance-projection.schema.json`](schema/governance-projection.schema.json) · [`validation/governance-projection.md`](validation/governance-projection.md) — **proposed**, TDR-0034 |
| Governance deterministic rules | [`validation/governance-rules.md`](validation/governance-rules.md) — GR-01 to GR-18, **proposed** |
| Governance fixtures | [`fixtures/governance/`](fixtures/governance/) — FIX-018 to FIX-031, **proposed** |

The specification governs wherever an overlay appears to differ from it.

## Skills

**Authoring path** (a human who holds the reasoning):
[`decision-identification`](skills/decision-identification/) →
[`problem-framing-and-decision-capture`](skills/problem-framing-and-decision-capture/) →
[`evidence-review`](skills/evidence-review/) → [`governance-review`](skills/governance-review/)

**Interpretation path** (reconstruction from material): the shared
[`identify-record-contributions`](../../skills/shared/identify-record-contributions/) and
[`reconcile-record-fragments`](../../skills/shared/reconcile-record-fragments/), then
[`draft-tdr`](skills/draft-tdr/) here, then the shared
[`challenge-record`](../../skills/shared/challenge-record/) and
[`validate-record`](../../skills/shared/validate-record/).

**Assurance** ([`skills/assurance/`](skills/assurance/)) — routing is normative in the DAC spec §4:
`systems-thinking`, `counterfactual-and-evidence` and `accumulated-and-resultant-risk` always run;
`fraud-and-adversarial-thinking`, `customer-outcomes`, `systems-dynamics` and `adaptive-capacity` run
on their declared triggers; `assurance-synthesis` always closes.

**Governance reconstruction** ([`skills/governance/`](skills/governance/)) — **proposed under
[TDR-0034](../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md), not accepted.**
Eight skills reconstructing the forums, obligations, authorities and evidence through which
consequential decisions are actually taken, and projecting one bounded next change for a forum:
`governance-reconstruct`, `forum-reconstruct`, `obligation-authority-trace`, `demonstrability-drill`,
`governance-equivalence`, `forum-evolution`, `regime-preservation`, `governance-accretion-plan`.

They live here because forums are **mechanisms for consequential judgement, challenge and
disposition** — not a sixth kind of organisational truth. They orchestrate and project across
Authority, Evidence, Value and Inheritance semantics and **do not redefine them**; semantic ownership
stays with the family that owns it. Their outputs are projections, never records.

One record, two routes to it — there is no interpreted variant of a TDR and an authored variant.

## The proportionality rule applies to candidates

Spec §3 routes a decision to full, minimal or bare by reversal cost, and identification adds the
outcome that matters most — **no record at all**. Interpretation does not suspend this: a candidate
assembled from material describing something cheap to reverse is proposed at the bare tier, or
reported as not warranting a record. A skill producing a full-template candidate for every decision
it finds has misread the standard as an instruction to maximise records.
