---
name: draft-vr
description: Assemble reconciled contributions into a standards-conformant Value Record candidate reconstructing an Operational Value Commitment — keeping commitment semantics separate from reconciliation semantics, and never asserting attribution from measurement. Use this skill after reconcile-record-fragments has produced a candidate assembly for a value commitment, whenever someone says "write up the benefit case from these documents" or asks "what did we actually commit to here?", and when a commitment found in existing material needs a conformant draft. It refuses to draft an expected value with no baseline, and it will report an outcome as observed with attribution unresolved rather than claim a benefit the evidence does not carry.
---

# Draft Value Record

This skill turns a [`CandidateAssembly`](../../shared/candidate-assembly.md) for an **Operational Value
Commitment** into a conformant markdown Value Record. It is written for humans and usable by AI
assistants. Read [`spec-value-record.md`](../../spec-value-record.md) for field definitions and
[`records/vr/`](../../records/vr/) for the roles and admission test.

The object is the commitment; the record is its governed memory. What is being reconstructed is what the
organisation undertook to pursue or preserve — not a document's benefit table.

## The one rule

**No baseline, no claim.** The specification's rule survives interpretation intact. A benefit measured
against nothing can never be reconciled against anything, and a drafted record that omits the baseline
has produced something that looks reconcilable and is not.

## Process

### 1. Check admissibility first

Apply [`records/vr/admission.md`](../../records/vr/admission.md). Value commitments are where wrong
merges are most likely — two benefits in one programme describe themselves in near-identical language —
so check the grouping basis with particular care before drafting.

### 2. Separate the two moments

Commitment roles render the record. Reconciliation roles render **realised entries and reconciliation
only** — never commitment sections, however early in the source material they appeared. A benefits
tracker entry is an `observed-outcome`, not an expected value, even when it is the only number in the
document.

### 3. Render the commitment

Value thesis with its falsifying signal, baseline with date and source, beneficiary, value kind,
expected value and recognition route, due point, counter-signatory, linked decision. Where the material
follows the OVC grammar — **Given · We commit · For · By · Settled by · Unless** — the mapping in
[`records/vr/semantic-roles.md`](../../records/vr/semantic-roles.md) is direct.

### 4. Never assert attribution from measurement

An observed movement is not evidence that this commitment caused it. Where the material shows an outcome
and no attribution reasoning, render the outcome and record the settlement as **attribution
unresolved**. See below.

### 5. Mark every gap in place

Beneficiary, falsifying signal and counter-signatory are the roles real material most often lacks. Each
absence is a finding worth surfacing, because each names a reason the benefit was never going to be
reconciled.

## Attribution unresolved is a legitimate output

Where an outcome is observed and attribution is not evidenced, the honest settlement is **outcome
observed, attribution unresolved.** Draft it that way.

This will look like an incomplete record to anyone expecting benefits realisation to produce a yes or a
no. It is not. It is the accurate statement of what the evidence supports, and inventing either a
successful attribution or a write-off would be a fabrication in the direction the reader expects — which
is the hardest kind to notice.

## Outputs

A markdown Value Record with `status: proposed`, commitment and reconciliation sections properly
separated, gaps marked in place, and provenance attached. Plus a statement of what the evidence did not
supply.

## Quality checks

- Does the baseline carry a measurement date and a source?
- Does the value thesis carry a falsifying signal — something that would show the value is not arriving?
- Is `finance_countersignatory` a named individual, or visibly absent? Never a function, never "Finance".
- Has any reconciliation role leaked into a commitment section?
- Is every attribution claim supported by attribution evidence, not by an observation?
- Is `linked_decisions` evidenced rather than assumed from proximity?

## When to refuse

- **No baseline contribution.** Report the gap; do not draft an expected value without one.
- **No linked decision.** A value claim floating free of any decision is a forecast, not a record.
- **The candidate merges two commitments** on programme membership or similar wording.
- **Attribution is asserted in the source but only measurement is evidenced.** Draft the observation;
  refuse the attribution.

## Anti-patterns

- **Attribution by adjacency** — a cost line falling near a project name treated as benefit delivered.
- **The optimistic settlement** — resolving an unresolved attribution because a conclusion was expected.
- **Commitment inflation** — an aspiration in a slide drafted as an undertaking.
- **Baseline by assumption** — "current state" with no measurement behind it.
- **The tidy record** — beneficiary and falsifying signal supplied because their absence looked untidy.
- **Reconciliation leakage** — realised figures rendered as expected value.

## Scope note

This skill drafts from contributions and the record package alone. Tracking, recognition and financial
reconciliation happen in an organisation's own systems — downstream implementation, deliberately outside
this standard (see TDR-0002, TDR-0018).
