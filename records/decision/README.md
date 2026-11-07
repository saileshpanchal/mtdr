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

The specification governs wherever an overlay appears to differ from it.

## Skills

**Authoring path** (a human who holds the reasoning):
[`decision-identification`](skills/decision-identification/) →
[`problem-framing-and-decision-capture`](skills/problem-framing-and-decision-capture/) →
[`evidence-review`](skills/evidence-review/) → [`governance-review`](skills/governance-review/)

**Interpretation path** (reconstruction from material): [`recover-decision-records`](skills/recover-decision-records/)
runs it end to end — [`identify-decision-contributions`](skills/identify-decision-contributions/) →
[`reconcile-decision-contributions`](skills/reconcile-decision-contributions/) →
[`draft-tdr`](skills/draft-tdr/) → [`challenge-decision-record`](skills/challenge-decision-record/) →
[`validate-decision-record`](skills/validate-decision-record/), each specialising the shared stage of
the same name. Its vocabulary is [`decision-contribution.md`](specification/decision-contribution.md);
material recovered after the event follows [`historical-recovery.md`](../../specification/historical-recovery.md),
and what it hands on is a retrospective candidate with no standing. *Proposed under TDR-0048 and
TDR-0049.*

**Assurance** ([`skills/assurance/`](skills/assurance/)) — routing is normative in the DAC spec §4:
`systems-thinking`, `counterfactual-and-evidence` and `accumulated-and-resultant-risk` always run;
`fraud-and-adversarial-thinking`, `customer-outcomes`, `systems-dynamics` and `adaptive-capacity` run
on their declared triggers; `assurance-synthesis` always closes.

One record, two routes to it — there is no interpreted variant of a TDR and an authored variant.

## The proportionality rule applies to candidates

Spec §3 routes a decision to full, minimal or bare by reversal cost, and identification adds the
outcome that matters most — **no record at all**. Interpretation does not suspend this: a candidate
assembled from material describing something cheap to reverse is proposed at the bare tier, or
reported as not warranting a record. A skill producing a full-template candidate for every decision
it finds has misread the standard as an instruction to maximise records.
