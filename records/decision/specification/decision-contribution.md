# Decision contributions — the recovery vocabulary

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** **Proposed under [TDR-0049](../../../decisions/TDR-0049-decision-recovery-vocabulary.md) —
no standing until ratified.** Normative for interpretation of the decision language once accepted.
**Not a record schema.** Machine-readable form:
[`../schema/decision-contribution.schema.json`](../schema/decision-contribution.schema.json).

What a fragment of organisational material can contribute to reconstructing a **consequential
decision** — without requiring that it constitutes a TDR. A decision is rarely written down in one
place: a paper sets out the options, a minute records the choice, an email names who will own it, and
a later review says whether it happened.

The classes are **interpretive vocabulary carried through the shared
[`RecordContribution`](../../../specification/record-contribution.md)**, exactly as the value language's
are: `semantic_role` takes a class name where field-level assignment is premature, and tightens to a
[semantic role](../validation/semantic-roles.md) when drafting maps the evidence onto the record. A
fragment can make several contributions.

Recovering decisions from historical material follows
[`specification/historical-recovery.md`](../../../specification/historical-recovery.md) (proposed under
TDR-0048). This file is the decision language's part of it.

## The classes

| Class | What we are looking for | Tightens toward |
|---|---|---|
| `decision-moment` | a commitment of money or time, or a foreclosed option — the choice itself | `decision-statement` |
| `context` | what was known at the time: facts, unknowns, assumptions, constraints, time pressure | `context` |
| `time` | when the decision was taken | `decision-date` |
| `owner` | the individual who held the decision | `accountable-owner` |
| `authority` | the delegation or instrument under which it was taken — **a reference, never a grant** | `lineage-derived-from` where it is a recorded decision; otherwise it is carried as itself, a reference |
| `alternative` | an option considered and not taken | `alternative-rejected` |
| `foreclosure` | a future the decision closes off | `option-foreclosed` |
| `evidence` | material considered, by dimension | `evidence-business` … `evidence-external` |
| `consequence` | what the decision binds the organisation to, and what reversing it would cost | `consequence`, `reversal-cost` |
| `confidence` | the confidence stated at the time | `confidence` |
| `lineage` | an earlier decision revisited, contradicted or built upon | `lineage-supersedes`, `lineage-derived-from` |
| `challenge` | evidence contradicting or questioning the decision | `conflicts`; challenge findings |
| `corroboration` | later material evidencing that the decision occurred | none — it supports existence only, and is **never context** |
| `non-decision` | material recording that no decision was made | none — a finding, with its kind |
| `not-a-decision` | material that resembles a decision and is not one | none — a finding, with its reason |

Four classes — `challenge`, `corroboration`, `non-decision`, `not-a-decision` — deliberately never
populate a record field. Losing them loses exactly the disagreement, the history and the negative
findings recovery is for.

## The five reasons something is not a decision

Stable identifiers. [`decision-identification`](../skills/decision-identification/) names them for
capture; **this table is their definition**, and the skills, the machine-readable form and any
consumer cite it rather than restate it.

| Identifier | What it is |
|---|---|
| `status-update` | reporting that work happened is not deciding anything |
| `action` | a task — "Priya to send the contract" — not a judgement |
| `preference` | an opinion not yet attached to a commitment of money, time or foreclosed options |
| `restatement` | an already-recorded decision repeated in a new setting; it creates no new decision |
| `operational-routine` | a choice fully determined by an existing policy or runbook; the judgement was exercised when the policy was decided |

`restatement` here is a reason a *decision* is not new. The evidence kind of the same name in
[`historical-recovery.md`](../../../specification/historical-recovery.md) is a *source* that repeats
another. They are different questions, answered separately.

## No decision evidenced, and evidence that no decision was made

Two different findings, never merged:

- **No decision evidenced** — the material is silent. It is a statement about the evidence, not about
  the organisation: failing to recover a decision is not evidence that none was taken.
- **Evidence that no decision was made** — the material says so. Its kinds:

| `non-decision` kind | What the material records |
|---|---|
| `deferred` | the question was put off, with nothing committed in the meantime |
| `not-reached` | the meeting ended without a decision |
| `withdrawn` | the proposal was taken away before a decision |

A deferral that itself commits money or time, or forecloses an option — *we will not proceed until the
audit reports* — is a decision, and is contributed as one.

## Roles recovery treats specially

| | Roles | Rule |
|---|---|---|
| **Event role** | `decision-date` | the contribution a historical candidate's `event_time_ref` points at |
| **Context roles** | `context` and the seven `evidence-*` roles | each carries a `considered` annotation, and is graded for contemporaneity — evidence considered at the time is as exposed to hindsight as context |
| **Never inferred** | `accountable-owner`, `alternative-rejected` — and the `owner`, `authority` and `alternative` classes | `derivation: explicit` or no contribution at all |

A **reason** — why the decision was taken — has no field of its own in the TDR. It lives in `context`
and the `evidence-*` roles, and is contributed **only where a span states it**. A reason assembled from
what the outcome suggests is the reconstruction of reasoning the doctrine forbids, whichever role it is
filed under.

## What each kind of material can support

The decision language's instance of the matrix in
[`historical-recovery.md`](../../../specification/historical-recovery.md). ✓ supported, explicitly ·
✗ not supported · ◐ supported only as qualified.

| Evidence kind | Decision | Context | Alternatives | Owner | Authority | Date | That it occurred |
|---|---|---|---|---|---|---|---|
| `act-record` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ its own | ✓ |
| `cited-material` | ✗ a paper recommends, it does not decide | ✓ `considered: evidenced` by the citation | ✓ as presented to the decision | ✗ an author is not an owner | ◐ where it names the instrument | ✗ its date is not the decision's | ✗ |
| `unlinked` | ✗ | ◐ circumstance only, `considered: unlinked`, never what was known by whoever decided | ✗ | ✗ | ✗ | ✗ | ✗ |
| `later-recording` | as `act-record`, graded by **capture** time | as `act-record` | as `act-record` | as `act-record` | as `act-record` | ✓ the capture's | ✓ |
| `retrospective` | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ **only this** |
| `restatement` | as its source, counted once | as its source | as its source | as its source | as its source | as its source | as its source |

**The forum is not an authority contribution.** *The board agreed* is part of the decision-statement
span: the body that acted is in the act. A forum proposed as an owner is not an owner, and goes to
`context` as [`semantic-roles.md`](../validation/semantic-roles.md) says. The `authority` class is for
the delegation or instrument cited — *under the scheme of delegation, §3.2*.

## Findings

A `not-a-decision` or `non-decision` finding is reported as the fragment it rests on, with a
classification object valid against the machine-readable form —
`{taxonomy_version, class, reason}` or `{taxonomy_version, class, non_decision}`. Findings are not
grouped into candidates; they travel in the recovery report, by fragment.

## The `unclassified` outcome

Material relevant to a decision that fits no class is reported as **`unclassified`** — the fragment
references, what was recognised, and why classification failed. A reporting outcome, not a sixteenth
class. A recurring unclassified pattern routes to a superseding decision.

## The completeness view

Every drafted candidate carries, per mandatory role — `decision-statement`, `context`,
`decision-date`, `accountable-owner` — one state grade:

```
supported | partial | missing | conflicting
```

— state only. Whether a value was read directly or inferred is carried on its contributions'
`derivation` and reported alongside, never folded in. Plus the one-sentence reading of what the
evidence did not supply. **Failure to recover evidence is not evidence that the decision was not
taken.**
