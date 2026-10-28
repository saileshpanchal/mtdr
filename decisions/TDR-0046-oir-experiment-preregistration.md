---
id: TDR-0046
conforms_to: mtdr/decision/tdr@1.15.0
title: Pre-register the Operational Inheritance Record experiment before building it
status: accepted
template: full
decision_date: 2026-10-28
accountable_owner: Sailesh Panchal
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0021, TDR-0032, TDR-0033, TDR-0047
confirmed_by_outcome: pending — confirm when the deletion attack has run against every pin and an independent reviewer has reported, or 2027-04-28, whichever is sooner
---

# TDR-0046 — Pre-register the Operational Inheritance Record experiment before building it

> **Accepted 2026-10-28. This record admits nothing.** It fixes, before any Operational Inheritance
> Record exists in this repository, the test that will decide whether one should. Evidence:
> [`evidence/TDR-0046-ratification-2026-10-28.md`](evidence/TDR-0046-ratification-2026-10-28.md).
> The frozen criteria are [`evidence/TDR-0046-preregistration.md`](evidence/TDR-0046-preregistration.md).

## Context — what was known at the time

The `work` package has been a **candidate** since the package architecture was adopted
([TDR-0021](TDR-0021-record-package-architecture.md)): primary record the Operational Inheritance
Record (OIR), admission not passed, metadata and scope only. Its README named the question admission
would have to settle — *whether operational inheritance is persistent governed state at all, or a
projection from governed state* — and said a directory must not settle it.

An article series has since set out the OIR as ten clauses answering one question: **what
organisational state must a participant inherit before performing operational work?** The later
articles make one claim about it that no other record type in this standard makes for itself: that
the organisational state already in force around a piece of work — commitments, dependencies, shared
assumptions, accepted risks, what experience has shown, the organisation's own thresholds for what is
severe or material — *exists before the participant arrives and persists when the participant
changes*, and that no other record carries it. The other nine clauses are, on the series' own account,
drawn from what the organisation keeps elsewhere.

The [record admission test](../specification/record-admission-test.md) requires **the four answers,
with the evidence for each — not assertions**. Question 4 — *does it have an independent lifecycle,
rather than merely projecting another record?* — is exactly what is in doubt, and it cannot be
answered from documents. The series defines no lifecycle at all. The research behind it predicts that
only the inherited-context clause is native, has registered a deletion attack to test that, and has
not run it. Whether the OIR is native state or a useful projection can only be established by
**building it, exercising it, removing it, and observing what is lost**.

That creates an apparent circularity — the test of admission needs the thing admission would permit
— which this record and [TDR-0047](TDR-0047-experimental-packages.md) resolve together: permission to
implement is not permission to declare proven.

## Decision

**Run the Operational Inheritance Record as a pre-registered experiment, and fix its test before
building it.**

The criteria are frozen in [`TDR-0046-preregistration.md`](evidence/TDR-0046-preregistration.md) and
the suite refuses any change to that file. In summary:

- **Two questions, never inferred from each other.** *A — does OIR work?* is answered by implementation
  and exercise. *B — must OIR exist as native state?* is answered by a deletion attack. A working
  implementation says nothing about B.
- **The measure is warranted organisational knowledge, not text.** A participant responsible for an
  operational capability is replaced, and the successor must answer five questions from the same
  evidence, with OIR and without it: what state they inherit; which decisions and constraints still
  bind; what they may do and must refuse; what has changed since their predecessor; what follows from
  a proposed decision.
- **Six equivalence dimensions**, every one required — operational facts, authority, temporal state,
  provenance, consequences, **uncertainty**. A reconstruction that confidently invents authority fails
  even when its proposed action is reasonable.
- **An independent-source control.** The scenario corpus was frozen before any OIR existed; a
  without-OIR answer resting on anything OIR introduced is inadmissible, and a clause that only
  *appears* derivable because OIR populated the alternatives counts as not derivable.
- **Possibility decides; cost does not.** Reconstruction that is impossible is evidence for native
  state; reconstruction that is possible but harder is evidence of operational value, **not** of
  necessity. Effort, source dependencies and unresolved questions are recorded as secondary
  observations and may never become criteria after the results are seen.
- **A lifecycle test proves capability-relativity, not nativeness.** Replacing the participant must
  create no new version; changing the inherited state must. Passing rules out a participant-centred
  record and nothing more.
- **Five pins, or the run is void**: the pre-OIR standard (`v1.30.0`, immutable), the OIR
  implementation commit, the corpus hash, the evaluator revision, the resolved runtime.
- **An independent reviewer** — neither this standard's owner nor the assistant that implemented the
  package — may reject the native-state claim even when the implementation works, and conducts an
  evidential challenge, not a code review. Independent review precedes any admission decision.

**The comparator is pinned, not frozen in place.** The pre-OIR standard is the immutable `v1.30.0`
tag, hashed in [`TDR-0046-comparator-freeze.json`](evidence/TDR-0046-comparator-freeze.json). The rest
of the standard remains free to evolve; the without-OIR arm always runs against the tag. The
experiment's own commits change nothing in the comparator set.

**The evidence is committed before the implementation.** Its hashes — corpus, evaluator
specification, pre-registration, comparator — are published in
[`TDR-0046-evidence-commitment.json`](evidence/TDR-0046-evidence-commitment.json) in the same commit
as this record, which precedes every commit carrying OIR content. The corpus itself stays private and
is disclosed only as a hash.

### The admission test, answered as far as evidence allows

| Question | Answer now | Evidence the experiment adds |
|---|---|---|
| 1. A distinct class of organisational meaning? | **Provisionally yes** — inherited operational state, stated by the series and reserved by this repository since the package architecture | exercise: does an OIR carry anything the other records do not express? |
| 2. Exists independently of another record family? | **Provisionally yes** — the record references other records by identifier only; the package depends on none | the experimental package's dependency closure and boundary checks |
| 3. Extractable and semantically complete? | **Provisionally yes** | the extraction trial, run on the experimental package |
| 4. An independent lifecycle, not a projection? | **UNRESOLVED** | the deletion attack — the whole of question B |

### The failing query, bounded against every language

*What organisational state must a participant inherit before performing this operational work, and
which of it remains in force when the participant changes?*

| Language | What it answers | Why it does not answer the query directly |
|---|---|---|
| **Decision** | what was decided, by whom, when, and what that forecloses | a decision is a judgement at a moment; the query asks for the standing state that applies to a piece of work across many decisions, as it stands now |
| **Value** | what the organisation committed to pursue or preserve, for whom | commitments say why work matters, not what a participant must understand before doing it |
| **Authority** *(candidate)* | who may act, and within what limits | what a participant may do is not what it must understand before doing it |
| **Evidence** *(candidate)* | what is known, and how | evidence supports answers; it does not select which state applies to this work |

Whether the query can nonetheless be **computed** from those records is precisely question B. This
record does not assume the answer.

### Registered prediction — recorded, not built in

Only the inherited-context clause is native; the other nine reduce to other records. The experimental
package implements all ten clauses as fields, each with a source marker, so the attack measures which
clauses reduce instead of inheriting this prediction.

### Outcome map

Admit the work language with the OIR as native state · treat the OIR as a projection over existing
records · admit a narrower construct · remain a candidate. **Each is a later, separate decision. This
record authorises none of them.** A projection outcome is a legitimate result, not a failure: it
identifies a useful way of making existing organisational knowledge available to successors.

## Evidence

- **Business** — continuity of operational work across changes of team, supplier, technology and AI
  participant is the problem the series names; whether it needs a new record or a new view of existing
  ones has direct consequences for what every adopter must maintain.
- **Architecture** — the standard's substrate was built for this: the contribution structure's
  `target_object` is deliberately open *"for an object supplied by a later record package"*, and no
  shared specification or schema has to change for the experiment to run.
- **Regulatory** — not material to this record; nothing it authorises is a claim about any adopter.
- **Operations** — the experiment is bounded: its evidence is frozen, its judge is separate from its
  implementation, and the standard's other work is not blocked while it runs.
- **Customer** — not directly material.
- **Data** — the scenario corpus is private organisational material and never enters this repository;
  only its hash is published.
- **External** — the series' grammar and the research programme's pre-registered deletion attack
  (designed October 2026, not yet run) are the external inputs. They are cited by description and
  date; **no external result is claimed, because none exists yet.**

## Alternatives rejected

1. **Admit now, on the series' argument.** Rejected: the admission test demands evidence, and the
   evidence for question 4 does not exist. Admitting on an argument is the assertion the test forbids.
2. **Wait for the deletion attack before building anything.** Rejected: the attack needs an
   implementation to remove. Waiting makes the evidence impossible to obtain.
3. **Build without pre-registering.** Rejected: an implementation built first can shape the test that
   judges it — choosing scenarios it handles, or reading cost as necessity after the results are in.
4. **Freeze the whole standard on `main` for the life of the experiment.** Rejected: it would block
   unrelated work indefinitely. Pinning an immutable tag gives the comparator the same protection
   without the cost.
5. **Encode the prediction in the schema** — inherited context as the only native field. Rejected: the
   package would then pre-decide the attack's per-clause answer.

## Options foreclosed

- No admission, consolidation or native-state claim may rest on this record.
- The pre-registered criteria may not change. A defect is answered by a superseding pre-registration
  and a re-run of every arm.
- Reconstruction cost may never be promoted to an admission criterion after the results are seen.
- No result may be reported without all five pins.

## Consequences and review

The experimental package follows under [TDR-0047](TDR-0047-experimental-packages.md), published for
open review. Confirm when the deletion attack has run against every pin and the independent reviewer
has reported — whatever either says. Review on that evidence, or 2027-04-28, whichever is sooner.
