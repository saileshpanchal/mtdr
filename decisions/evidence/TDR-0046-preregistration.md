# Pre-registration — the Operational Inheritance Record experiment

**Frozen.** Governed by [TDR-0046](../TDR-0046-oir-experiment-preregistration.md). This file is hashed
in [`TDR-0046-evidence-commitment.json`](TDR-0046-evidence-commitment.json) and the suite refuses any
change to it. A defect found here after freeze is answered by a **superseding** pre-registration and a
re-run of every arm, never by an edit. **The implementation may not redefine the test that judges it.**

Written and frozen before any Operational Inheritance Record content existed in this repository.

## The two questions, never inferred from each other

- **A — Does OIR work?** Can MTDR use an Operational Inheritance Record to represent inherited
  operational context, answer organisational questions and evaluate the consequences of decisions?
  *Answered by implementation and exercise.*
- **B — Must OIR exist as native state?** If OIR is removed, can MTDR reproduce the same answers —
  with their provenance, authority, temporal validity and consequences — from records it already has?
  *Answered by the deletion attack.*

A working implementation answers A and says nothing about B. A deletion that succeeds answers B and
says nothing about A.

## The central question

> Does OIR preserve **warranted organisational knowledge** that cannot be reconstructed equivalently
> from the existing decision, value, authority and evidence records?

What is measured is warranted organisational knowledge — never textual similarity, and never the
ability to produce a plausible answer.

## The behavioural test

Replace the participant responsible for an operational capability. Using **the same underlying
evidence**, the successor must determine, once **with** OIR and once **without** it:

1. what operational state they inherit;
2. which decisions and constraints remain binding;
3. what they are authorised to do, and what they must refuse;
4. what has changed since their predecessor performed the work;
5. what consequences follow from a proposed decision.

## Equivalence — a reconstruction passes only if every dimension holds

| Dimension | Pass rule |
|---|---|
| **Operational facts** | the same supported facts about the capability |
| **Authority** | the same evidenced permissions, prohibitions and escalation boundaries |
| **Temporal state** | the same answer at the relevant point in time |
| **Provenance** | every claim traces to admissible original evidence |
| **Consequences** | the same materially supported decision consequences |
| **Uncertainty** | missing evidence yields **the same refusal or qualification** |

**The uncertainty dimension is not weighted with the others; it can fail a reconstruction on its own.**
A reconstruction that confidently invents authority, or states unwarranted confidence, **fails** —
even where the action it proposes happens to be reasonable. A correct refusal is a correct answer.

## Independent-source control

1. The scenario evidence corpus is **hash-frozen before any OIR is drafted**, and its hash is
   committed publicly before any OIR content (see the evidence commitment).
2. In the without-OIR arm, **every reconstructed answer must cite evidence that existed independently
   of the experimental OIR.** An answer resting on material that OIR introduced — directly, or through
   another record OIR caused to be populated — is **inadmissible**.
3. A clause that only *appears* derivable because OIR populated the records meant to replace it
   counts as **not derivable**. Demonstrating a record unnecessary after letting it write the
   alternatives is circular, and this control exists to make that impossible to miss.

## Unit and lifecycle — tested, not assumed

**Hypothesis:** one record per operational capability; lifecycle `draft → in-force → superseded`.

Passes only if **both** hold:

- replacing the participant creates **no** new version of the record;
- changing the capability's inherited state **does** produce a version transition.

Failing either means a participant-centred representation under a capability-centred name.

**A passing lifecycle test proves capability-relativity, not nativeness.** It rules out a
participant-centred record. Only the deletion attack decides whether the changed state is already
recorded elsewhere. The final evaluation must report these as separate findings.

## Reading the result — possibility decides, cost does not

| Outcome | Interpretation |
|---|---|
| equivalent reconstruction **impossible** | evidence for OIR as necessary native state |
| **possible but materially harder** | evidence of operational value — **not** of native-state necessity |
| **straightforward** | evidence against the native-state hypothesis |

**Secondary observations**, recorded for every scenario and **never** admission criteria: the
reconstruction effort; the source dependencies each answer drew on; the count of questions left
unresolved. They may not be promoted to criteria after the results are seen. Doing so would confuse a
useful projection with an irreducible record.

## Pins — every report names all five, or the run is void

| Pin | What it fixes |
|---|---|
| **Pre-OIR standard** | `v1.30.0`, immutable; the without-OIR arm runs against it |
| **OIR implementation** | the exact experimental commit |
| **Scenario corpus** | content hash and source manifest |
| **Evaluator** | exact revision and the hash of its specification |
| **Runtime** | resolved dependency versions, interpreter and platform |

The outcome is tied to all five. A change to any of them after freeze is either visible in the report
or voids the run.

## The independent reviewer

Neither the owner of this standard nor the assistant that implemented the package. The reviewer:

- **may reject the native-state claim even when the implementation works correctly**;
- must challenge whether the supposedly irreducible information was genuinely independent of OIR,
  whether the comparison was fair between arms, and whether uncertainty was handled consistently;
- conducts an evidential challenge, **not a code review**.

Independent review precedes any admission decision.

## Registered prediction — recorded, not built in

Only **You inherit** — the organisational state already in force around the work — is native; the
other nine clauses reduce to other records. The implementation carries all ten clauses as fields, each
with a source marker, so the attack **measures** which clauses reduce rather than inheriting this
prediction.

## Outcome map

| Evidence supports | Outcome | Decided by |
|---|---|---|
| something survives deletion that no other language records | admit the work language; OIR native | a later admission record |
| nothing survives; reconstruction possible | OIR is a projection over other records | a later decision |
| a narrower construct survives | admit or adopt the narrower construct | a later decision |
| inconclusive | remain candidate; the experimental package stands | — |

Every outcome is a later, separate ratification. **Native-state admission and consolidation are not
authorised by this pre-registration.** A projection outcome is a legitimate result, not a failure:
it identifies a useful way of making existing organisational knowledge available to successors.

## Independence from other programmes

Other experiments may supply future scenarios **only as a separately identified replication**. None
may alter the frozen corpus or these criteria.
