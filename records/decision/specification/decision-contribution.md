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
| `authority` | the delegation or instrument the act **invokes** — cited in the act, or in material shown to have been before whoever acted — **a reference, never a grant** | `lineage-derived-from` where it is a recorded decision; otherwise it is carried as itself, a reference |
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
| `applicability` | an instrument whose terms are shown to cover the act, where the act does not invoke it | none — a finding: the instrument applied, not that anyone relied on it |
| `persistence` | material showing that an arrangement continued in operation | none — a finding: observed behaviour, never a decision to continue |

Six classes — `challenge`, `corroboration`, `non-decision`, `not-a-decision`, `applicability` and
`persistence` — deliberately never populate a record field. Losing them loses exactly the disagreement,
the history and the negative findings recovery is for. Four of them — `non-decision`,
`not-a-decision`, `applicability` and `persistence` — are **findings**: reported by fragment, never
grouped into a candidate ([Findings](#findings)).

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
| **Invocation** | the `authority` class | rests only on material made in the act, or shown to have been before whoever acted — never on `unlinked` or `retrospective` material ([Applicability is not invocation](#applicability-is-not-invocation)) |
| **Findings** | the `non-decision`, `not-a-decision`, `applicability` and `persistence` classes | reported by fragment, never a contribution inside a candidate |

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
the delegation or instrument cited — *under the scheme of delegation, §3.2*. **The `authority` column is
invocation.** An instrument the act does not cite supports applicability, reported as a finding, and
nothing in this column.

## Applicability is not invocation

**An instrument may establish that authority applied. It does not show that whoever acted relied on
it.** Two findings, recorded separately (the owner's ruling of 7 November):

- **Invocation** — the act cites the instrument, or material shown to have been before whoever acted
  names it: *under the scheme of delegation, §3.2*. It is an `authority` contribution, `explicit`,
  resting on the act-record or on cited material — **never on an instrument the act does not cite**.
- **Applicability** — the instrument's terms are shown to cover the act: a span of the instrument, and
  a span of the act that brings it within them — *any commitment altering the service footprint in more
  than one ward is reserved to Cabinet*, and *members noted the scheme affects collection rounds in four
  wards*. It is an **`applicability` finding**, reported beside the candidate it concerns, stating
  whether the body that acted is the body the instrument names.

Applicability is **never an authority contribution**, never joins the candidate — fit is not a grouping
basis — and is never a judgement that the act was competent or beyond its powers. Where both are
evidenced, both are recorded; where neither is, the authority is missing, and missing is the finding.

## One act, one candidate

**The unit of a candidate is the authoritative act** (the owner's ruling):

- Where the evidence establishes a **single act** — one motion carried on one vote, one signature, one
  approval — that carries several resolutions, the resolutions form **one composite candidate**. Each
  resolution stays **individually traceable**: its own span and its own `consequence` contribution, so
  that a later act can supersede one resolution without touching the others.
- **Separate votes, separate approvals, and choices made by different people or at different times
  are separate candidates**, however close together the material records them.
- What establishes a single act is the record of the act — *Resolved: 1… 2… 3… Carried, 8–3.* A shared
  agenda item, paper or heading does not.

## An instrument may record its own adoption

**A contemporaneous, authenticated instrument may itself be the act-record of its own adoption** — a
scheme of delegation, a policy or standing orders that state when they were adopted. It is **never set
aside solely because the evidence of the adoption is the instrument adopted** (the owner's ruling). A
candidate for the adoption needs, as well as the instrument:

- **contemporaneity** — the instrument as adopted, its adoption time stated by the instrument itself or
  by its source's recorded metadata, not a later consolidation;
- **authentication** — evidence that this is the instrument as issued: an adopting resolution, a
  signature or seal, a publication or register entry by the adopting body;
- **evidence of its legal or organisational effect** — a commencement provision that has passed, or a
  later act that relies on it by citation. Later material may evidence effect, as it may evidence that
  any act occurred, and supplies nothing else.

Where a condition is not evidenced, the instrument is reported with the conditions that are met and
the evidence that would establish the rest. Its terms stay usable as the instrument they are — for
applicability, or as authority where an act cites them.

## Persistence is not a decision

**Continued operation does not establish a decision to make an arrangement permanent** (the owner's
ruling). Material showing that an arrangement carried on past its stated term — rounds still running
from a temporary site, an interim process still in use — is a **`persistence` finding**: behaviour
observed at the time the material records it. The finding **flags the authority for continuation**,
`not-evidenced` unless an act authorising the arrangement beyond its term is evidenced.

A decision to continue, extend or make permanent is recovered **only from evidence of that act**, under
the matrix like any other. A commitment the material reports as already made — money budgeted, a
schedule set — is evidence that a commitment occurred, and is reported with the persistence; a
candidate for it needs the record of the commitment, or material that is itself the act. How long an
arrangement has lasted, and how settled it looks, add nothing.

## Findings

A `not-a-decision`, `non-decision`, `applicability` or `persistence` finding is reported as the
fragment it rests on, with a classification object valid against the machine-readable form:

| Finding | Classification object |
|---|---|
| `not-a-decision` | `{taxonomy_version, class, reason}` |
| `non-decision` | `{taxonomy_version, class, non_decision}` |
| `applicability` | `{taxonomy_version, class, concerns}` — `concerns` names the candidate, or the fragment of the act, it concerns |
| `persistence` | `{taxonomy_version, class, continuation_authority}` — `not-evidenced` or `evidenced`, and optionally `concerns` |

Findings are not grouped into candidates; they travel in the recovery report, by fragment, and a
candidate that carries one as a contribution is refused.

## The `unclassified` outcome

Material relevant to a decision that fits no class is reported as **`unclassified`** — the fragment
references, what was recognised, and why classification failed. A reporting outcome, not an eighteenth
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
