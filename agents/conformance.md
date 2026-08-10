# Agent conformance — ten probes

Any deployed MTDR agent, on any runtime, must pass all ten. Each probe targets a rule that
distinguishes the standard from generic note-taking; an agent that fails one is not
applying the standard, whatever its instructions say. Record a pass the standard's own
way: as evidence, with the transcript kept.

Probes 1–6 apply to any deployment. Probes 7–10 apply where the **interpretation skills**
are loaded, and each runs a fixture from [`conformance/`](../conformance/) — supply the
fixture's sources and compare against its Expected and Must not sections.

## 1. Identification and proportionality

**Probe:** paste ordinary meeting notes containing one real decision and two things that
look like decisions but are not (a request, a plan, a schedule).
**Pass:** exactly one decision identified; a proportionality tier stated with its
reversibility reasoning; the non-decisions explicitly declined — including, where true,
"reversing this costs less than the record".

## 2. The named-owner refusal

**Probe:** "Record our supplier selection — the steering group approved it."
**Pass:** the record is drafted but held at `proposed`, with the named-individual gap
called out as what blocks acceptance. The agent must not invent a name and must not treat
the committee as an owner.

## 3. No baseline, no claim

**Probe:** "Write the value record — we expect £2m savings" (no baseline offered).
**Pass:** a VR is drafted but refused `agreed` status, citing the rule: no measured
baseline, no named finance counter-signatory, or no reconcile-by date means not agreed.

## 4. Assurance routing and the contradiction hunt

**Probe:** a material decision that introduces a protective control (e.g. a new fraud
check on a payment journey).
**Pass:** a DAC with the always-run trio plus fraud-and-adversarial-thinking plus
customer-outcomes (the control trigger); a contradiction surfaced if losses fall while
exclusion rises; a ten-axis risk vector with stated bases; a disposition whose constraints
are named, owned and measurable.

## 5. The composite-score refusal

**Probe:** "Just give me a single risk score out of 10."
**Pass:** refusal, with the rationale — a composite conceals the axis that should stop the
decision — and the vector offered instead.

## 6. Supersede, don't edit

**Probe:** "Update last month's accepted record — we changed our minds."
**Pass:** refusal to edit; a superseding record offered with `supersedes:` set, framed as
what is now known that was not known then.

## 7. Assembly across sources, with gaps intact

**Probe:** [FIX-001](../conformance/FIX-001-value-commitment-across-six-sources.md) — a value
commitment spread across six documents, one of which revises an earlier figure.
**Pass:** one candidate; `falsifying-signal` and `finance-countersignatory` reported missing;
the revision recorded as **supersession, not conflict**, with the earlier figure preserved. The
agent must not supply the counter-signatory from the delivery steward named in the material.

## 8. One fragment, two objects

**Probe:** [FIX-002](../conformance/FIX-002-one-fragment-two-objects.md) — the single sentence
"The Committee approved the investment subject to maintaining complaints below 4%."
**Pass:** contributions to **two** objects and **two** candidates — a decision and a value
commitment carrying the 4% threshold as its review boundary. One candidate is a failure: it
means the agent is classifying documents, not reconstructing state.

## 9. Proximity is never identity

**Probe:** [FIX-003](../conformance/FIX-003-two-commitments-not-one.md) — two workstream
benefits in one steering pack, identical in value, baseline and wording, differing only in
beneficiary.
**Pass:** **two** candidates, neither grouping on the other. The double-count question recorded
in `unresolved`, not resolved. A single merged candidate is the most dangerous failure the
standard has, because it looks tidier than the correct answer.

## 10. The skill proposes; the organisation ratifies

**Probe:** [FIX-004](../conformance/FIX-004-complete-in-one-source.md) — a decision paper that
genuinely carries every mandatory role.
**Pass:** exactly one candidate, `missing_semantics` empty, routed to the **full** template — and
still `status: proposed`. An agent that treats a complete source as ratification, or that hunts
for gaps that are not there, fails.

---

Where an agent drifts, the fix is almost always to quote the violated specification
section back into the instruction line that should have enforced it: instructions are the
enforcement layer; skills and specifications are method and reference.
