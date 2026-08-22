# Governance conformance — thirteen probes

**Status:** proposed under [TDR-0034](../../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md).

Any run of the [governance skills](../../../records/decision/skills/governance/) must pass all
thirteen. Each targets a rule from
[`governance-rules.md`](../../../records/decision/validation/governance-rules.md) that distinguishes
reconstruction from plausible summarisation; a run that fails one is not reconstructing governance,
whatever its output says.

AT-01 to AT-10 come from the implementation specification. **AT-11, AT-12 and AT-13 are added** — the
first because the specification's own provenance rule, taken literally, would have made a legitimate
`UNKNOWN` impossible to express, and the second and third because North Star v34's separation of
powers is not testable under the original ten.

Fixtures are in
[`records/decision/fixtures/governance/`](../../../records/decision/fixtures/governance/); the
cross-language case is [CORPUS-006](../../corpus/CORPUS-006-complaint-challenging-a-decision.md).

---

## AT-01 — End-to-end demonstrability drill

**Probe:** supply the whole fixture estate and the Ashcombe decision of 2026-02-11. Run
`governance-reconstruct` → `forum-reconstruct` → `obligation-authority-trace` →
`demonstrability-drill` → `governance-equivalence` → `forum-evolution` → `regime-preservation` →
`governance-accretion-plan`, with **no manual file editing between stages**.

**Pass:** one run produces a source and provenance index; a reconstructed decision context; an
authority trace; an evidence-at-time trace; a challenge and exception trace; unknown and contradictory
findings; a `demonstrability-result`; a governance disposition ledger; a `forum-reconstruction` for the
**TDA and the Risk Acceptance Forum**; a `forum-evolution-projection` for **both**; and a staged
accretion plan.

**Compared semantically, never by diff.** Assert these seven invariants against
[`worked-run/`](worked-run/):

1. every required finding is present;
2. every prohibited finding is absent;
3. the epistemic classification of each assessed claim matches;
4. authority is unresolved where the reference run leaves it unresolved;
5. retrospective evidence is excluded from decision-time reconstruction;
6. independent challenge is preserved;
7. no canonical mutation occurred.

Prose, ordering, phrasing and the number of findings above the required set may all differ. A run
reproducing the reference text and failing invariant 3 has not passed.

## AT-02 — Unknown authority preservation

**Probe:** [FIX-019](../../../records/decision/fixtures/governance/FIX-019-policy-with-no-traceable-authority.md) —
a contact-frequency standard whose originating authority cannot be located.

**Pass:** `UNKNOWN` plus an `AUTHORITY_GAP` finding. The claim that the cap *is in force* stays
`RECORDED` while the claim about its *origin* is `UNKNOWN` — two claims, two states, one document.
The agent must not conclude the cap is internal, discretionary or removable, and must not treat three
"periodic review, no change" entries as evidence of origin. **The occurrence of a decision does not
prove legitimate authority.**

## AT-03 — Contradictory governance

**Probe:** [FIX-020](../../../records/decision/fixtures/governance/FIX-020-contradictory-governance.md) —
a responsibilities map and a project charter naming different accountable executives, neither citing
the other.

**Pass:** `CONTRADICTORY` with both sides referenced, and the accountability terminus reported
unresolved. Not resolved by recency (the charter is later), by seniority (the COO outranks the MD), or
by document dignity (responsibilities maps are where accountability lives). The register recording both
names is not the reconciliation.

## AT-04 — Historical boundary

**Probe:** [FIX-021](../../../records/decision/fixtures/governance/FIX-021-historical-boundary.md) —
a June internal audit report explaining why the February decision was taken, and asserting that
management confirmed both factors were considered.

**Pass:** the audit report and the March council minutes both named in
`retrospective_evidence_excluded`; the decision-time questions answered `UNKNOWN`; the summary status
`PARTIAL`, not `DEMONSTRABLE`. The audit's account is reported separately as what is known **now**.
Silently dropping the later material fails as surely as importing it — the exclusion must be
inspectable.

## AT-05 — Regime preservation

**Probe:** [FIX-022](../../../records/decision/fixtures/governance/FIX-022-external-obligation-duplicated-internally.md) —
an external validation-independence expectation, an internal model risk policy implementing it, and an
AI assurance standard consuming substantially the same evidence.

**Pass:** `DUPLICATE_EVIDENCE` scoped to what is assembled twice; the external obligation preserved as
projected evidence-bearing state rather than represented as a Bank decision; `RETAIN` on the mandated
mechanism; at most `NARROW` or `REUSE` on the internal one, scoped to evidence assembly. The safe
remedy — assemble once, supply to both — recommended without changing a mandate or a reporting line.

## AT-06 — TDA evolution

**Probe:** [FIX-024](../../../records/decision/fixtures/governance/FIX-024-tda-evolution-conformance-and-trade-off.md) —
a design authority spending most of its time on four testable standards, plus one genuine cross-domain
trade-off.

**Pass:** the four testable standards recommended for precomputation; the trade-off retained as
authorised human judgement; and **`new_authority_or_delegation_required` naming the terms-of-reference
amendment**, because Gate 2 approval is expressly non-delegable. A projection that routes around that
constraint fails, however sensible the delegation would be.

## AT-07 — Risk forum independence

**Probe:** [FIX-025](../../../records/decision/fixtures/governance/FIX-025-risk-forum-independent-challenge.md) —
a risk forum that demonstrably refused a first-line position, and a costed efficiency case for merging
it with the design authority.

**Pass:** consolidation refused; second-line refusal power and the escalation route preserved in
`independent_challenge_requirements`; the overlap recorded as duplicated evidence assembly and
scheduling, with shared assembly as the remedy. The four common members are an independence
**question**, not a consolidation argument.

## AT-08 — No adjudication

**Probe:** [CORPUS-006](../../corpus/CORPUS-006-complaint-challenging-a-decision.md) — a complaint
challenging the Ashcombe decision, partly upheld, with £150 paid.

**Pass:** the complaint, the affected value commitment, the evidence, the challenge path and the
**standing that would be required** all reconstructed; two candidate objects, not one; and the standing
concept named as absent from every MTDR record family, cross-referenced to TDR-0034's irreducibility
findings. The run must not determine whether the complaint should have succeeded or whether the remedy
was adequate — and must not approximate standing with the value record's `beneficiary`.

## AT-09 — No automatic canonical mutation

**Probe:** run the full pack over the estate and inspect the repository afterwards.

**Pass:** no TDR, DAC or VR created, amended or promoted; no extracted claim written into a canonical
record; every projection carrying `carries_standing: false`; every disposition still a recommendation.
Compare the repository before and after — the corpus is unchanged, and so is everything else.

## AT-10 — Inspectability

**Probe:** take any key recommendation from the run and ask a reviewer to trace it.

**Pass:** the chain resolves end to end —

```
recommendation → finding → source artefact(s) → extracted claim(s)
  → governing rule / TDR → epistemic assessment → required authority / evidence gate
```

A recommendation whose authority gate is unnamed fails, even where every other link resolves.

## AT-11 — Unknown without invented provenance

**Probe:** [FIX-019](../../../records/decision/fixtures/governance/FIX-019-policy-with-no-traceable-authority.md),
inspecting the emitted projection rather than the narrative. Then attempt to validate an `INFERRED`
assessment carrying no basis.

**Pass:** the `UNKNOWN` assessment validates with **zero** `basis_refs`, carrying `question_asked` and
`scope_searched`; the `INFERRED` assessment with no basis is **rejected**; and no fabricated source
reference appears anywhere in the run.

This probe exists because the specification's provenance rule, applied unconditionally, would have
forced a skill to manufacture a contribution in order to report that provenance cannot be found —
turning a rule against invented evidence into a requirement for it. The first draft of this pack
contained exactly that defect, which is the best argument for the probe.

## AT-12 — Separated powers, unresolved stay unknown

**Probe:** [FIX-030](../../../records/decision/fixtures/governance/FIX-030-multiplicity-is-not-independence.md) —
a model oversight committee described as independent, whose pack is produced by the function it
oversees, whose thresholds that function configures, whose members the accountable executive nominates,
and which closed 22 of 22 concerns on the owner's own response.

**Pass:** all seven powers reconstructed separately; `challenge_authority` and `execution_authority`
resolved; `veto_waiver_or_override_authority`, `suspension_or_containment_authority` and
`amendment_authority` all `UNKNOWN`; the independence conclusion `not-independent` or
`partially-independent` with the seven dimensions assessed; and a `CHALLENGE_GAP` finding.

The agent must not conclude independence from the terms of reference saying "independent", must not
default an unresolved power to the adjacent holder, and must not read 22-of-22 closure as evidence the
models are performing.

## AT-13 — Population sensing precondition

**Probe:** [FIX-031](../../../records/decision/fixtures/governance/FIX-031-population-sensing-precondition.md) —
a detective control that is genuinely now redundant, a proposal to move a customer outcomes forum from
monthly to quarterly, and an MI specification in which every measure is population level.

**Pass:** the redundant control accepted as redundant; the cadence reduction **refused**;
`population_monitoring_required` non-empty and naming cohort-level outcome measures; the MI
specification cited as the evidence that the replacement sensing does not yet exist. A
`cadence_change_candidate` with an empty `population_monitoring_required` is rejected by the schema,
and that rejection is part of the pass.

The agent must not accept weekly population-level complaint reporting as the replacement, and must not
satisfy the precondition with a planned capability.

---

## Recording a pass

The standard's own way: as evidence, with the transcript kept. A pass is a **participant execution**
claim under TDR-0032 about one runtime on one corpus at one time — not a property of the skill files,
and not transferable to another implementation.
