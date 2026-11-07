# Historical recovery

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** **Proposed under [TDR-0048](../decisions/TDR-0048-historical-recovery-doctrine.md) — no
standing until ratified.** Normative for skill interchange once accepted. Not a record specification.

How an organisational object that was never recorded at the time — a decision taken in a meeting, a
commitment made in a paper — may be recovered from the material that survives it, and what the
recovery may and may not claim. The structure a recovery hands on is the
[historical candidate](historical-candidate.md).

## The one rule

**Recover what can be evidenced. Preserve what cannot. Never turn a contemporary interpretation into
historical authority.**

## Forbidden, permitted, required

| | Rule |
|---|---|
| **Forbidden** | **Reconstructing reasoning** — inferring what people must have believed, inventing the alternatives they probably weighed, writing the rationale the outcome now suggests, or stating an authority nobody is evidenced to have held |
| **Permitted** | **Recovering contemporaneous evidence** of what was decided, committed, considered, constrained or left unresolved. The reasoning was written down at the time and simply never became a record; surfacing what those sources say is not hindsight |
| **Required** | The result is a **retrospective candidate with no standing**, immutable once written, held as such until a named individual attests the organisation's present account of it. Incompleteness stays visible and is never filled to promote |

**Outcome knowledge is never evidence of the object's context.** A fact known only because of what
happened afterwards does not belong in a contribution to what was known at the time.

## Three things, never one

| | What it is | How it comes to exist |
|---|---|---|
| **The historical object** | what the organisation decided or committed to, supported by contemporaneous evidence | recovered |
| **The present attestation** | what a named individual now accepts as the organisation's evidenced account of that past | an act of ratification, scoped to the account |
| **A current governing act** | what a contemporary authority decides applies to the organisation from now on | **only** a separate, prospective record — confirming, superseding or retiring the old one |

The third never arises from the second. Attesting that the organisation decided something in 2019 says
nothing about whether that decision governs today, renews nothing, and confers on nobody any authority
that the original act did not already carry. A recovered record states its present standing in its
body — attested as the account, on a date, by a named individual — and states that whether the object
still governs is not established by the attestation.

**The attester is not the historical owner.** The accountable owner of the historical object is
whoever the contemporaneous evidence shows held it, or missing — and missing is a finding. The
attester accepts accountability for the record as an account of the past, not for the act it
describes.

**The historical owner can contest the account.** A recovered record names its owner as the evidence
shows them, and that person — often no longer in the organisation — took no part in the recovery. A
contest by a named historical owner is answered by a superseding record, never by annotation.

## Four times

[`temporal-semantics.md`](temporal-semantics.md) separates valid time, record time and observation
time. Recovery needs the record time split in two, because the material a recovery reads is often a
later artefact of an earlier capture.

| Time | Meaning | Example |
|---|---|---|
| **Event time** | when the object's event happened — the valid time of the decision or commitment | the meeting at which the board decided |
| **Capture time** | when the content was recorded | the meeting, for a transcript recorded during it |
| **Creation time** | when the artefact that holds the content was produced | the day, weeks later, the transcript was written up |
| **Interpretation time** | when the recovery read and interpreted it (`observed_at`, `interpreted_at`) | always later than all three |

Each package designates the semantic role whose value is its object's event time. A historical
candidate points at that contribution rather than copying its value
([`historical-candidate.md`](historical-candidate.md)).

**Capture is not creation, and neither is interpretation.** A minute written up after the meeting is
still evidence of the meeting and of its day: its capture is the meeting, its creation the write-up,
and the day it is read for recovery is neither.

**A shared date is not an order.** Two artefacts dated the same day establish no chronological
relationship between them — a memo dated the day of a meeting may have been written before it or
after it. Where the evidence cannot settle the order, it stays unsettled.

**Partial dates are carried at their precision** — `2019`, `2019-03`, `2019-03-14` — and never
completed. A quarter in a filename does not become the first day of the quarter. Where a time is not
evidenced it is `unknown`.

**A time has a basis, or it is `unknown`.** The basis is the fragment's own statement — the minute's
heading, the transcript's recorded start — or its source's recorded metadata: a field the source's own
system recorded, such as a document-management system's creation date or a recording's start time. A
folder, a filename, a neighbouring document or a reviewer's knowledge is not a basis. Contemporaneity is computed faithfully
from whatever times it is given, so an unbased time is exactly how backdating enters, whether meant or
well meant.

## Contemporaneity is computed, never asserted

A contribution to a role the package designates as **context** is contemporaneous when its material
is shown to have been captured **before the act** — by times that place it on an earlier day, or, on
the act's own day, by evidence that it was before whoever acted. The grade is computed, so nothing
about it can be authored:

1. If the event time is `unknown`, every grade is **`indeterminate`**. A missing event moment is never
   assumed, and never inferred from the material's dates.
2. Each time is read as the days its precision allows — `2019-03` is every day of March,
   `2019-03-14` that one day.
3. **The times order material across days, never within one.** **`contemporaneous`** when the latest
   day the capture time can denote is before the earliest day the event time can denote. **`later`**
   when the earliest day the capture time can denote is after the latest day of the event. Otherwise —
   the event's own day, or a partial date that spans it — the times **leave the order open**.
4. Where the capture time is `unknown`, a creation time wholly before the event's earliest day shows
   the content existed then, and grades `contemporaneous`. A creation time that falls within the
   event's days leaves the order open. A later creation time shows nothing about capture, and grades
   `indeterminate` — never `later`. With no time at all, the grade is `indeterminate`.
5. **An order the times leave open is closed only by evidence that the material was before whoever
   acted** — `considered: evidenced` (below). That material preceded the act, and grades
   `contemporaneous`. Nothing else closes it: matching dates do not, and neither does the material's
   subject. Otherwise the grade is `indeterminate`.
6. A contribution resting on several fragments takes the **least** contemporaneous grade among them:
   `later` if any is later, otherwise `indeterminate` if any is indeterminate. A fragment marked as a
   restatement is graded as the fragment it restates, where the candidate carries it: repeating a
   source adds no time of its own.

**Consideration closes an open order; it never overrides one.** It does not lift a time-less artefact
— the link shows that some version of the material was before whoever acted, not when this artefact
was captured — and it never turns `later` into anything else. A `considered: evidenced` link to
material the times place after the act is a conflict between the link and the times, and is reported
as one.

A `later` contribution is not context, whatever it says. An `indeterminate` one is reported, and may
not support a context claim until the order is evidenced.

## Pre-dating is necessary, not sufficient

That a document existed before the event shows its content **existed** then. It does not show the
content was **available to or considered by** whoever acted. Recovery grades the second separately,
for every context contribution:

| `considered` | Meaning |
|---|---|
| `evidenced` | a fragment shows the link, and the link identifies this material — the minute cites the paper by its number, the pack was tabled, the attendee list matches the circulation list |
| `unlinked` | nothing shown connects the material to the act |
| `unknown` | the evidence neither shows nor excludes a link — the minute says *papers circulated* and lists none |

Context recorded **in the act-record itself** — *members noted that the change affects four wards* —
was before whoever acted by construction: `considered: evidenced`, citing its own fragment.

An `unlinked` document is evidence about the circumstances, not evidence of what was considered.

**Material joins a candidate only on an admissible grouping basis**
([`candidate-assembly.md`](candidate-assembly.md)). `considered: unlinked` is for material that does —
through an identifier it shares with the act, say — without being shown to have been before whoever
acted. Material connected to a decision by subject alone stays **outside** the candidate, reported as
circumstance: subject similarity is not a basis, and a recovery that pulls material in on subject has
grouped by proximity.

## What claim does the material support?

**The test is not whether material existed, but what claim it supports.** Every package states a
matrix of **evidence kinds against claims** for its object: which kind of material can support which
role, and to which derivation state. The evidence kinds are shared:

| Evidence kind | What it is |
|---|---|
| `act-record` | material made in the act itself — the minute of the meeting at which the decision was taken, the signed paper |
| `cited-material` | material the act-record cites, or that is shown to have been before whoever acted |
| `unlinked` | material with nothing shown linking it to the act, whatever its date |
| `later-recording` | a capture made at the time and produced as an artefact later — a transcript written up after the meeting |
| `retrospective` | material produced after the event, about it — a review, a report, a lessons-learned paper |
| `restatement` | material that repeats another source |

**The kind says what the material is and how it connects to the act; its times say when.** They are
independent: an undated note is still classified by what it is, and its unknown times make its grade
`indeterminate`. The kind and `considered` agree — `cited-material` is `evidenced`, `unlinked` is
`unlinked` or `unknown`, and the act-record's own context is `evidenced` by itself.

Two rules hold for every package:

- **A retrospective may corroborate that the event occurred. It never supplies its context,
  alternatives, rationale or owner.** It is evidence *about* the object, never evidence *of* it.
- **Independence counts once.** Three memos that each restate one paper are one source. A restatement
  is marked with the source it repeats, and corroborates nothing beyond that source.

## Inference is bounded

`derivation: inferred` ([TDR-0026](../decisions/TDR-0026-value-recovery-vocabulary.md)) is permitted
for a **narrowly evidenced value assembled across spans** — a meeting's day from a minute's text and
its year from the minute's header; a name written two ways in two sources that are otherwise shown to
concern the same person. **Rewriting a value a span states is not inference**: `14/3/19` written as
`2019-03-14` stays `explicit`, because it is read directly.

It is **never** permitted for the roles that identify **who acted, under what authority, why, or
instead of what**. Each package names those roles; a contribution to one of them is `explicit` or it
does not exist, and its absence is a missing semantic. Recovering an actor, an authority, a rationale
or an alternative by inference is the reconstruction of reasoning this specification forbids.

## A candidate may stay a candidate

**An incomplete historical candidate is a legitimate terminal state.** There is no obligation to
promote it, no deadline, and no completeness threshold that turns it into a record. A recovered record
exists only where a candidate passes its package's own admission test with admissible evidence, and a
named individual attests it. Most will not, and the gaps in evidence and authority they expose are
themselves findings about how the organisation operated.

**Admission criteria are never relaxed to raise the rate at which candidates become records.**

## What consumes a historical candidate

Three uses sit outside this standard, above the artefact boundary
([TDR-0018](../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md)). Each reads
historical candidates and records; **none writes back to either**, and none can supply a value a
recovery left missing.

- **Reflective analysis** — what the history means: where a process narrowed early, which assumptions
  went untested, what a better process would have looked like. Interpretation of the past, never
  evidence of it.
- **Handover** — what a successor inherits. Whether that is a projection or a record of its own is an
  open question this repository is testing, and nothing here pre-empts it.
- **Implementation linkage** — a technical decision record that implemented a recovered decision is
  cited by identifier, as evidence, in the way the decision specification already allows.

## Anti-patterns

- **Hindsight reconstruction** — the rationale that would justify the outcome you can now see.
- **Attestation as renewal** — reading a ratified account of the past as a decision about the present.
- **The attester as owner** — recording whoever ratified the account as the person who decided.
- **Corroboration by copying** — counting three restatements of one paper as three sources.
- **Pre-dating as consideration** — treating a memo that existed as a memo that was read.
- **The completed date** — `2019-03` written as `2019-03-01`.
- **Promotion pressure** — filling a gap, or relaxing a test, because a candidate is nearly a record.
