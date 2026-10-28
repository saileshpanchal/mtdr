# The Operational Inheritance Record (OIR)

**Version:** 1.0.0 · **Status: EXPERIMENTAL — not part of the MTDR standard** · **Licence:** MIT ·
**Author:** Sailesh Panchal

> **This specification is published for review under [TDR-0047](../../../decisions/TDR-0047-experimental-packages.md).**
> It exists to generate the evidence that will decide whether it should exist at all, under the test
> pre-registered and frozen in [TDR-0046](../../../decisions/TDR-0046-oir-experiment-preregistration.md).
> Nothing here is admitted, and **no conformance claim may rest on it.** The record may yet be admitted
> as native state, narrowed, or reclassified as a projection over the records the standard already has.

## 1. What the record is for

Every organisational record answers one question. A decision record answers *what changed?* A value
record answers *why does this matter?* An Operational Inheritance Record answers:

> **What organisational state must a participant inherit before performing operational work?**

Organisations already keep onboarding packs, procedures, run books, playbooks, service documentation
and knowledge bases. Each holds part of the answer; none expresses it as a coherent, governed whole.
So each participant reconstructs the organisation for itself, and the reconstruction leaves with it.

**The record describes the work, never the worker.** Participants change — a person moves role, a team
is reorganised, a service is outsourced, software takes over a deterministic step, an AI participant is
authorised for defined work. The operational capability, and the state built up around it, persists.

## 2. The unit of record

**One record per operational capability** — an enduring body of operational work and the state in force
around it, such as *the movement of customer payments* or *the restoration of a service after
disruption*. A capability may contain several jobs.

> **Experimental hypothesis.** TDR-0046 tests this unit rather than assuming it. A record keyed to a
> participant under a capability's name is the failure the test exists to catch.

An OIR **never** describes a person, a team, a department, a supplier or a technology. If replacing the
participant would require rewriting the record, the record describes a role, a procedure or an
implementation, not inherited state.

## 3. The ten clauses

The record is ten answers. They are **not ten headings to fill in**: most of the answers are kept
elsewhere by the organisation, and the record gathers them for the work being inherited, as they stand
now. A clause is therefore either **asserted** in the record or a **reference** to where the
organisation keeps the answer — and every clause says which (§4).

| # | Clause | Question it answers |
|---|---|---|
| 1 | **Purpose** | why does this operational capability exist? |
| 2 | **You inherit** | what organisational state already applies before work begins? |
| 3 | **Jobs to be done** | what enduring operational jobs must be performed? |
| 4 | **Outcomes** | how do we know each job is being done well? |
| 5 | **You are responsible for** | what stewardship accompanies the jobs? |
| 6 | **You may** | what authority may be exercised? |
| 7 | **You must** | what obligations cannot be varied? |
| 8 | **You should** | what established practices normally guide the work? |
| 9 | **Escalate when** | where do the job, the capability or the authority reach their limits? |
| 10 | **Evidence** | what must performing the work leave behind? |

### 3.1 Purpose

The enduring purpose the capability serves — for the organisation, its customers or its ecosystem.
**Never** the current team, system or operating process. Where the organisation has committed to an
outcome, the purpose is that commitment, referenced: *Protect customers and maintain the safe, timely
movement of money.*

### 3.2 You inherit — inherited context

The organisational state already in force when responsibility transfers, which the participant
inherits and does not create:

- existing services and customer commitments;
- policies and regulatory obligations in force;
- operational assumptions and dependencies;
- service levels and resilience expectations;
- known risks and the controls accepted against them;
- existing decisions that shape the work;
- **what experience has shown about this work** — recurring causes of failure, conditions that have
  previously caused harm;
- **the organisation's own definitions of what counts as severe, material or acceptable** for this
  work.

> **The claim under test.** This is the one clause the series argues no other record carries: the
> state exists before the participant arrives and persists when the participant changes. Whether it
> is genuinely irreducible, or merely gathered from records that already hold it, is question B of
> TDR-0046. This specification states the claim; it does not assume it.

### 3.3 Jobs to be done

Each job is a stable statement of what must be accomplished, written in the functional form:

> **verb + object + contextual clarifier**

*Process customer payment instructions within the applicable service and scheme conditions. Resolve
payment-processing exceptions before they cause avoidable customer harm. Restore the payment service
following an operational disruption.*

**The participant-change test.** A job must remain valid when its performer changes. *Operate the
payment exceptions team* is not a job — it embeds the current structure. *Build the mobile feature* is
not a job — it describes a temporary solution. If changing the participant requires rewriting the job,
it describes a role, procedure or implementation.

The record **names** the jobs that belong to the capability. It does not own them: whether a job
exists, continues or retires is the organisation's decision, and a job carries a reference to the
decision that established it where one exists. Jobs change **by decision, never by the accident of a
reorganisation.**

**Eligibility and allocation are not authority.** Which participants may perform a job, and which are
allocated to it, are organisational decisions made separately. Neither creates authority.

### 3.4 Outcomes

What the organisation seeks from the work and how it recognises success — the measures performance is
judged against. Outcomes **never** prescribe a performer or an implementation, so different
participants can be compared against the same need. One job may serve several outcomes; one outcome
may need several jobs. Where the organisation has committed to an outcome, the clause references that
commitment.

### 3.5 You are responsible for

What must remain protected while the work is performed — service integrity, customer outcomes, data
quality, operational risk, service commitments, continuity, keeping the inherited context current,
escalating material issues. A job may finish; the stewardship continues.

**Responsibility never implies authority.** Being responsible for a job does not grant authority to
perform it.

### 3.6 You may — authority

The decisions, actions and state changes the participant may undertake without further approval, and
their financial, operational and risk limits, including whether authority may be delegated further.

**The record grants no authority.** This clause is **always a reference** to the authority instrument
in force — a delegation, a scheme of authority, an authority record — or a declared gap. It is never
asserted inline: a record that states authority without citing where it was delegated has manufactured
it.

### 3.7 You must — obligations

What cannot be varied, whoever performs the work: legal and regulatory obligations, customer
commitments, safety and resilience requirements, policy constraints, segregation of duties, mandatory
controls, evidence retention. Properties of the organisation, not of the participant.

### 3.8 You should — practices

How the organisation has learned to perform the work well: preferred sequences, conventions,
heuristics. A **strong default, not a rule** — it preserves consistency without removing justified
judgement.

**A practice is not a fact.** *How this work has failed before* is inherited context (§3.2), not a
practice. Keeping them apart lets a practice be challenged without losing what the organisation has
learned.

### 3.9 Escalate when

Where the inherited job, capability or authority reach their limits: the job falls outside the
participant's capability; an authority threshold would be exceeded; mandatory obligations conflict;
the evidence is insufficient; consequences exceed an agreed risk boundary; an exception is not covered
by the inherited context. **Escalation is not failure.** It is how governance is preserved when local
authority or capability runs out, and its thresholds draw on the authority delegated and on the
organisation's own definitions of what is serious.

### 3.10 Evidence

What performing the work must leave behind: which participant performed the job, under what
authority, using which inherited context, what decisions and actions occurred, what outcome resulted,
whether obligations were satisfied, when escalation took place. Without it, a future participant
cannot distinguish established practice from informal custom. Evidence is also how experience becomes
inheritance: what one performance showed, the organisation can later decide every future participant
should know.

## 4. The source marker — every clause says where its answer lives

| Marker | Meaning | Requirement |
|---|---|---|
| `asserted` | the answer is stated in this record | the body states it, with its provenance |
| `reference` | the answer is held by another record or instrument | one or more identifiers in `refs`; **the content is not restated** |
| `missing` | the organisation has not established an answer | a declared gap — never filled, never inferred |
| `conflicting` | sources disagree | every conflicting source cited; the conflict is preserved, never resolved |

**Any clause may carry any marker, except `authority`**, which is `reference` or `missing` (§3.6). The
marker is what lets TDR-0046's deletion attack **measure** which clauses reduce to other records: the
specification deliberately does not decide that in advance.

**Unknown is a first-class state.** `missing` is never written as an empty clause, a placeholder or a
plausible default.

## 5. Lifecycle

> **Experimental hypothesis**, tested under TDR-0046.

```
draft  →  in-force  →  superseded
```

- **`draft`** — being assembled; carries no standing.
- **`in-force`** — the inherited state the organisation has accepted for the capability.
- **`superseded`** — replaced by a later record for the same capability.

A record is **superseded when the capability's inherited state changes**, and **never** because the
participant changes. Replacing the team that performs the work produces no new record. Records are
never edited in place; a change of inherited state is a new record carrying `supersedes`.

A passing lifecycle test shows the record is **capability-relative**. It does not show the record is
native state; only the deletion attack bears on that.

## 6. Frontmatter

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | `OIR-nnnn` |
| `conforms_to` | yes | `mtdr/work/oir@1.0.0` |
| `experimental` | yes | `true` — a detached OIR must not be mistakable for a record of the standard |
| `title` | yes | the capability, never a participant |
| `status` | yes | `draft` · `in-force` · `superseded` |
| `effective_from` | yes | the date from which this inherited state applies |
| `accountable_owner` | yes | the named individual accountable for the record being current — not necessarily anyone who performs the work |
| `jobs` | yes | each `{job, established_by}`; `established_by` a decision id, or `unknown` |
| `clauses` | yes | all ten, each `{source, refs}` per §4 |
| `supersedes` | yes | an `OIR-` id, or `none` |
| `derived_from` | yes | ids, or `none` |

The schema is [`../schema/oir.schema.json`](../schema/oir.schema.json).

## 7. Relationships to other records

An OIR refers to decision records, value records and authority instruments **by identifier only**.
It never restates their content and never depends on another package's specification. A reference that
cannot be resolved in the reader's context is not an error in the record; it is reported
`indeterminate` by relational validation, as for any other record.

## 8. What an OIR is not

- **Not a procedure, playbook or run book.** Those explain how to complete a task. The OIR states the
  organisational context within which every such activity occurs, and replaces none of them.
- **Not a description of a person, team, department, supplier or technology.**
- **Not a grant of authority**, and not evidence that anyone is eligible to perform a job.
- **Not everything a participant will ever know** — only the state they inherit.
- **Not a claim that the capability survives by itself.** What persists is the work and the state
  around it; something else must still hold the work within its bounds.
