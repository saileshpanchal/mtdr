---
id: TDR-0034
title: Host governance reconstruction and forum evolution in the decision package as claim-level projections
status: proposed
template: full
decision_date: 2026-08-22
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0018, TDR-0020, TDR-0021, TDR-0022, TDR-0023, TDR-0025, TDR-0027, TDR-0033
confirmed_by_outcome: pending — review after one governance estate has been reconstructed end to end and one forum evolution projection has been authorised and observed, or 2027-08-22, whichever is sooner
---

# TDR-0034 — Host governance reconstruction and forum evolution in the decision package as claim-level projections

> **Proposed, not ratified.** This record carries no standing. Under
> [TDR-0027](TDR-0027-human-ratification-confers-standing.md), standing is conferred by an authorised
> human ratification of a defined candidate judgement, evidenced durably and attributably; no commit,
> merge, workflow transition or agent output confers it. Nothing in the branch that carries this
> record grants itself standing, and no artefact it introduces may be represented as accepted until
> that act occurs and its evidence is recorded.

## Context — what was known at the time

Governance regimes accrete. A regulated organisation cannot remove Model Risk Management, an AI
inventory, Consumer Duty governance, operational resilience governance, audit, complaints handling, a
Technology Design Authority or a risk committee because a common architecture happens to supply the
same property. Each of those mechanisms performs jobs — evidence assembly, routine conformance,
exception handling, trade-off judgement, independent challenge, authority exercise, escalation — and
the jobs survive changes in the mechanism's shape. The organisational question is not *which forums
should be abolished*, it is *what job is each mechanism actually performing, what must remain, what
can currently be demonstrated, and what is the smallest authorised next change*.

An implementation specification arrived proposing that capability be built here. It proposed a
repository layout — a top-level `skills/governance/`, a `rules/governance/`, a
`schemas/experimental/governance/` and an `acceptance/governance/` — and it also stated that where it
conflicts with an accepted repository TDR, the repository TDR wins and the conflict must be surfaced.
Inspection found four such conflicts. That escape hatch, and not the proposed layout, is what
determined the shape of this decision.

Three properties of the repository as it stood constrained every available answer.

**The language model has five packages and three of them are candidates.** `decision` and `value` are
normative; `authority`, `work` and `evidence` hold metadata and scope only until the
[record admission test](../specification/record-admission-test.md) is passed
([TDR-0021](TDR-0021-record-package-architecture.md)). Governance reconstruction needs authority and
inheritance semantics continuously, and neither exists in normative form. A directory confers no
maturity, so nothing could be solved by creating one.

**The boundary sits at the artefact.** [TDR-0020](TDR-0020-open-organisational-record-repository-boundary.md)
and [TDR-0018](TDR-0018-interpretation-skills-and-the-artefact-boundary.md) put whatever consumes
records outside this repository, and `CONTRIBUTING.md` states the dividing line as direction rather
than subject matter: a skill that reads material and yields the standard's own output belongs here;
storage, orchestration and downstream reasoning do not. A governance finding is not obviously on the
producing side of that line, and the Decision Assurance Case is the precedent that settles it — a DAC
consumes a decision record and produces a disposition with constraints, carrying no authority of its
own, and it has lived inside the decision package since TDR-0009.

**North Star supplies two vocabularies the substrate does not carry.** v33 classifies a claim as
`RECORDED`, `OBSERVED`, `INFERRED`, `UNKNOWN` or `CONTRADICTORY`. The substrate instead carries three
never-collapsed confidences ([`uncertainty.md`](../specification/uncertainty.md)) and the
`derivation: explicit | inferred` marker added by [TDR-0026](TDR-0026-value-recovery-vocabulary.md).
These answer different questions and are not inter-derivable. v34 separates execution, suspension,
challenge, veto and amendment authority, and holds that multiplicity is not independence — a
distinction the ten-job forum taxonomy compresses away.

The question is therefore: **where does a governance reconstruction capability live, and in what form,
such that it can reconstruct authority it cannot represent, report claims whose epistemic standing
varies within a single output, and recommend change without manufacturing the authority to make it?**

## Decision

Governance reconstruction and forum evolution are implemented as an **additive skill sub-family of
the decision package**, producing **claim-level projections over existing record families**. Six
things follow, and each is load-bearing.

### 1 — Hosting, not semantic ownership

Governance reconstruction is hosted in the decision package because **forums are mechanisms for
consequential judgement, challenge and disposition** — a Technology Design Authority, a Risk
Committee and an AI Governance Forum are not additional kinds of organisational truth, they are
apparatus through which existing Authority, Decision, Evidence, Value and Inheritance semantics are
exercised. The skills live at `records/decision/skills/governance/`, exactly as the eight assurance
skills live at `records/decision/skills/assurance/`.

**The governance skills orchestrate and project across those semantics; they do not redefine them.
Semantic ownership remains with the relevant record family and its specification.** This wording is
constitutional rather than stylistic. `obligation-authority-trace` necessarily spans authority and
inheritance, packages that are not yet admitted, and the decision package must not become their de
facto owner by default. When the OAR and OIR languages mature, nothing in this sub-family may need to
move or be reinterpreted for them to take ownership of what is already theirs.

**No sixth record family is created.** The five-language model of
[`organisational-records.md`](../specification/organisational-records.md) is unchanged.

### 2 — Outputs are projections, carried in one envelope

`GovernanceFinding`, `GovernanceDisposition`, `ForumReconstruction`, `ForumEvolutionProjection`,
`DemonstrabilityResult` and `AccretionStep` are **projections and findings, never constitutional
records**. They fail question 1 of the record admission test by design — they carry interpretation
about organisational meaning rather than organisational meaning itself — which is the test's own
stated answer for anything proposed for persistence on that basis.

They are carried in **one** governance-projection envelope at
`records/decision/schema/governance-projection.schema.json`, package-local alongside `tdr.schema.json`
and `dac.schema.json`. `SourceClaim` receives no envelope shape: it maps onto the existing
`RecordContribution` and duplicating it would be the defect
[TDR-0023](TDR-0023-portable-skill-architecture.md) names.

**This does not amend [TDR-0022](TDR-0022-fragment-contribution-interchange-architecture.md).** The
three ratified interchange structures — `SourceFragment`, `RecordContribution`, `CandidateAssembly` —
are untouched and unextended. The envelope sits *downstream* of them as a skill-output contract, not
beside them as a fourth interchange primitive. **Adding a new projection type must never require a
change to the organisational record model**, so the envelope validates known types against their own
payloads strictly while leaving unknown types open to a generic extension shape.

### 3 — Epistemic state is assessed per claim, never per document or projection

A projection carries `epistemic_assessments[]`, each binding one state to one identified claim with
its basis, its contradictions, the date **as of which** it was assessed, and a rationale. A single
forum reconstruction routinely carries several at once — a stated purpose that is `RECORDED`, an
actual evidence-assembly job that is `OBSERVED`, a de-facto approval authority that is `INFERRED`, a
waiver authority that is `UNKNOWN`, and an accountable owner that is `CONTRADICTORY`. One state per
document or per output would destroy exactly the distinction the vocabulary exists to preserve.

`assessment_as_of` is separate from `produced_at`: when a claim was assessed and when the output was
generated are different facts, and a reconstruction of decision-time state is worthless if they are
conflated.

The five states are defined narrowly for this pack and the definitions are normative for it:
`RECORDED` requires organisational state the evidence shows was formally admitted or authoritative
**for the relevant time**; `OBSERVED` is directly evidenced behaviour, artefact or event **without
asserting authoritative standing**; `INFERRED` is reconstructed from evidence but not directly
established; `UNKNOWN` is insufficient evidence; `CONTRADICTORY` is materially incompatible evidence
that remains unresolved.

**This does not extend the substrate and must not be mapped onto it.** `derivation` answers *how was
this produced*, the three confidences answer *how strong is it*, and epistemic state answers *what
standing does this projected claim have*. `RECORDED` is not `explicit` — an explicit statement in a
meeting pack can be an observation about governance without ever having been admitted organisational
state — and an `INFERRED` claim can carry high epistemic confidence and remain `INFERRED`. Whether
these classes are fundamental enough to become record-neutral across every MTDR language is a
separate constitutional question requiring its own decision and compatibility analysis; it is not
settled as a side effect of this pack.

### 4 — Provenance requirements are conditional on epistemic state

Every positive claim requires provenance — but a rule requiring at least one source reference on
*every* assessment would force a skill to manufacture a contribution in order to report that
provenance cannot be found, which is the failure the rule exists to prevent. Provenance is therefore
conditional: `RECORDED`, `OBSERVED` and `INFERRED` require supporting basis; `CONTRADICTORY` must
reference the incompatible claim or evidence sets; and `UNKNOWN` **may carry zero supporting
references**, must identify the question asked and the scope searched, and **must never fabricate a
contribution to satisfy a schema**.

### 5 — Governance powers are reconstructed separately

Reconstruction distinguishes, per forum and per job and where evidence permits: **execution
authority · suspension or containment authority · challenge authority · veto, waiver or override
authority · amendment authority · escalation route · accountability terminus.** Each carries its own
epistemic assessment, and an unresolved power stays `UNKNOWN` rather than collapsing into an adjacent
one.

**Multiplicity is not independence.** A separate forum, a different name or a distinct reporting line
establishes nothing; independence is assessed against reporting, incentives, authority, evidence
source, cognition or model source, orchestration, and whether the governed owner can suppress or
configure the challenger. **The accountability recursion terminates in an accountable individual,
never in a committee abstraction** — the rule
[`semantic-roles.md`](../records/decision/validation/semantic-roles.md) already states for records,
applied to projections.

This exposes the separation as a **projection**. It adds no canonical semantics and creates no
authority record.

### 6 — Nothing produced here carries standing

The envelope states `carries_standing: false` structurally. No skill may manufacture authority,
adjudicate a challenge, determine whether an affected party's substantive claim succeeds, retire a
control or forum automatically, or place a new mechanism in an execution path before shadow
operation. Detection of probable or de-facto authority is a finding about the estate, never a grant.
An externally mandated mechanism is not removable because a missing source could not be located, and
internal authority cannot be represented as amending a superior external obligation.

## Conflicts surfaced

The implementation specification proposed four structures this repository already refuses. Each is
recorded here rather than silently redirected, because the specification asked for exactly that.

| Specification proposed | Accepted decision that refuses it | Resolved as |
|---|---|---|
| top-level `skills/governance/` | [TDR-0023](TDR-0023-portable-skill-architecture.md) — skills live with the record semantics they carry; `skills/shared/` holds only demonstrably record-neutral skills, and governance skills carry governance semantics | `records/decision/skills/governance/` |
| `rules/governance/` | [TDR-0025](TDR-0025-conformance-architecture.md) — deterministic checks beyond the schema are a package's validation layer, and no `rules/` convention exists | `records/decision/validation/` |
| `schemas/experimental/governance/` | [TDR-0021](TDR-0021-record-package-architecture.md) — a directory confers no maturity, and there is no experimental-schema convention to shelter under | `records/decision/schema/`, package-local |
| `acceptance/governance/` | [TDR-0025](TDR-0025-conformance-architecture.md) — cross-package tests live in `tests/`, single-language fixtures in the package | `tests/conformance/governance/` and `records/decision/fixtures/governance/` |

The specification's own precedence rule produced this table. A capability that asks organisations to
demonstrate governance rather than assert it has no standing to exempt its own construction from the
constitution it is built on.

## Irreducibility findings

Six concepts could not be represented in existing normative families. They are not the same kind of
gap, and recording them as one list would repeat the imprecision this pack exists to expose.

| Finding | Type of gap |
|---|---|
| v33 epistemic state against `derivation` and the three confidences | shared assessment capability gap |
| required authority has nothing to resolve to — `authority` (OAR) is a candidate package | canonical family dependency gap |
| an inherited external obligation has no representation — `work` (OIR) is a candidate package | canonical family dependency gap |
| Protected Claim and Standing — who is entitled to challenge, and on whose behalf | constitutional semantic gap |
| amendment tier — which changes require which order of authority | constitutional semantic gap |
| a forum's own lifecycle — chartered, merged, narrowed, retired | canonical subject/lifecycle gap |

**These gaps prevent authoritative representation, not reconstruction.** This capability may identify,
describe and route every one of them while preserving each as unresolved; it may not close any of them
by semantic substitution. In particular, **an external obligation must not be forced into a decision
record because the inheritance language is unavailable** — it is preserved as evidence-bearing
projected state with the absent canonical representation named. Recording the gap is the useful
output; filling it with the nearest available shape would destroy the evidence that the gap exists.

The authority dependency deserves separate note: this pack is the first capability in the repository
that needs operational authority semantics continuously and cannot obtain them. That is the failing
query the authority package's admission has been waiting for, and it now has evidence rather than an
assertion.

## Evidence

- **Business** — governance estates already absorb substantial recurring cost in pack preparation,
  audit evidence assembly, complaint reconstruction and repeated context reconstruction before
  meetings. Reconstructing what each mechanism does, and evidencing what can actually be demonstrated,
  addresses that cost without asking any organisation to remove a mechanism it is required to hold.
- **Architecture** — the four conflicts above were each resolved by an accepted decision rather than
  by preference, and the resolution left the five-language model, the three interchange structures and
  the artefact boundary unchanged. The Decision Assurance Case is the direct precedent for a
  non-authoritative, constraint-bearing output living inside the decision package.
- **Regulatory** — the mechanisms in scope include externally mandated ones. GR-05 and GR-06 exist
  because a capability that can recommend narrowing a control must be structurally incapable of
  recommending removal of a mandated one, and because internal authority cannot amend a superior
  external constraint. The regulator-neutral accountability shape in
  [the TDR specification §8](../records/decision/specification/tdr.md#8-regulatory-framing--worked-examples-not-dependencies)
  is adopted as a shape, not as a dependency on any regime.
- **Operations** — a forum cannot act on a recommendation whose basis it cannot trace. Every
  recommendation resolves to a finding, its source artefacts, the extracted claims, the governing
  rule, the epistemic assessment of each material claim, and the authority gate that would be needed.
- **Customer** — material and direct. Complaints, vulnerable-customer treatment and customer-outcome
  governance are among the strongest proving grounds because the evidence obligations already exist.
  The same property makes the adjudication boundary non-negotiable: reconstructing the evidence and
  the standing route for a complaint is useful; determining whether the complaint succeeds is not this
  system's to do.
- **Data** — the substrate's own artefacts supply the evidence for the epistemic finding. The three
  confidences are specified as never-collapsible and `derivation` is specified as never folded into
  completeness grades; neither carries the standing of a projected claim, and a probe over the
  `RecordContribution` schema confirms no field expresses it. That is direct evidence of an absent
  capability rather than an argument for one.
- **External** — North Star v33 and v34 supply the epistemic and separation-of-powers vocabularies.
  Neither is adopted as a dependency: v33's classes are implemented locally to this pack and v34's
  separation is implemented as a projection, precisely so that a later constitutional judgement about
  either remains free.

## Alternatives rejected

1. **Build the specification's proposed layout.** Rejected because each of its four structures is
   refused by an accepted decision, and the specification itself made the repository's decisions
   decisive in that conflict.
2. **Admit a sixth `governance` language.** Rejected because a governance mechanism is apparatus for
   exercising existing semantics rather than a distinct class of organisational meaning, and because
   candidate packages hold metadata and scope only — a sixth directory would ship nothing and would
   contradict the umbrella specification while the question stayed open.
3. **Put the skills in `skills/shared/`.** Rejected because they carry governance semantics and the
   neutrality rule is demonstrable rather than declared: a shared skill may reference no package's
   roles, admission test or specification except by parameter.
4. **Extend `RecordContribution` with an `epistemic_state` field.** Rejected for this release because
   the classes answer a different question from `derivation` and the three confidences, because a
   record-neutral property affecting every language is a constitutional change requiring its own
   compatibility analysis, and because a governance pack is the wrong vehicle for it.
5. **Map the five classes onto the existing constructs.** Rejected because the mapping is lossy in the
   direction that matters: `RECORDED` and `OBSERVED` both collapse into `explicit`, which is precisely
   the difference between what an organisation admitted and what merely happened.
6. **Carry one epistemic state per projection.** Rejected because a forum reconstruction's claims
   legitimately differ in standing from one another, and a single state would report the whole output
   at the level of its weakest or its strongest claim, both of which are false.
7. **Require at least one source reference on every assessment.** Rejected because it makes `UNKNOWN`
   unrepresentable without invention, converting a rule against fabricated provenance into a
   requirement for it.
8. **Six separate schemas, one per output type.** Rejected because six canonical-looking schemas would
   present these projections as six new organisational record types, which is the outcome the
   projection framing exists to prevent.
9. **Prose contracts with no schema.** Rejected because the demonstrability drill and the acceptance
   probes need a deterministic surface, and a contract that cannot be validated cannot be conformed to
   by a second implementation.
10. **Do nothing until the authority and inheritance languages are admitted.** Rejected because the
    reconstruction is possible now and its output is the evidence those admissions require. Waiting
    would preserve the gap and generate nothing that argues for closing it.

## Options foreclosed

- No governance output may be represented as an organisational record, promoted into one
  automatically, or used to mutate canonical state.
- No projection type may be added in a way that requires a change to the organisational record model.
- No epistemic state may be attached to a document, a source or a whole projection rather than to an
  identified claim.
- `UNKNOWN` may never be satisfied by an invented contribution, and the absence of a locatable source
  may never be read as permission to remove a mechanism.
- No skill may manufacture authority, adjudicate a challenge, or execute a retirement.
- Independent challenge may not be collapsed into the execution authority it challenges for
  efficiency, and a periodic job may not be removed on automation of transaction-level conformance
  while the replacement population sensing does not exist.
- The three interchange structures may not be extended or re-specified by this capability.
- Semantic ownership of authority, inheritance, evidence and value may not pass to the decision
  package by virtue of this sub-family hosting skills that read them.

## Consequences and review

Success is a messy, partially contradictory governance corpus yielding a traceable answer to how an
organisation governs one class of consequential decision, what it can prove about that governance, and
what the smallest authorised next change would be — with `UNKNOWN` and `CONTRADICTORY` surviving the
whole pipeline intact, and with the forum questions answered separately: which jobs still require the
forum, which can be precomputed or delegated, which independent challenge must be preserved, and what
evidence would justify the next change in shape or cadence.

DAC-0034 constrains this proposal to shadow operation and blocks any canonical promotion. The
capability is exercisable on the synthetic corpus on acceptance; it is not authorised for an execution
path, for external constitutional custody, or for any claim of constitutional independence.

Review when one governance estate has been reconstructed end to end and one forum evolution projection
has been authorised and its outcome observed, or on 2027-08-22. The epistemic-state question and the
authority-package admission are expected to reopen first, and both should arrive as their own
decisions rather than as amendments to this one.
