# Temporal semantics

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

## The one rule

**When something was true and when it was recorded are different facts, and neither is the date on the
document.**

Interpretation deals with at least three distinct times, and conflating them is how a reconstruction
quietly invents a sequence of events that did not happen.

| Time | Meaning |
|---|---|
| **Valid time** | When the thing was, or is to be, the case in the organisation |
| **Record time** | When it was written down in the source |
| **Observation time** | When the interpreting skill read it (`observed_at`) |

Valid time and record time are the bitemporal pair. Observation time belongs to the interpretation
run, not to the organisation, and must never be mistaken for either.

## The document date is not the valid time

A board pack dated March may record a decision taken in January, a commitment beginning in April, and
a baseline measured the previous financial year. Four times, one document date. Taking the document
date as the decision date is one of the most common and most damaging interpretation errors, because
the result is plausible, precise and wrong.

Where valid time is not stated, it is **unknown**. `unknown` is an honest value and belongs in
`missing_semantics`; an inferred date presented as fact does not.

## Ordering does not establish sequence

That document B is dated after document A does not establish that B's content supersedes A's. It may
restate it, contradict it, describe a different object, or have been drafted first and circulated
later. Supersession requires shared authority lineage and, ideally, explicit reference — see
[`candidate-assembly.md`](candidate-assembly.md#conflict-and-supersession-are-different).

## Tense is evidence

"We will reduce" · "we have reduced" · "we expect to have reduced" carry genuinely different claims,
and the difference is frequently the whole finding. Preserve the tense in the fragment content and
respect it in the interpreted value. A commitment recorded as an achievement is a fabrication, however
small the edit that produced it.

## What this standard does not do

It does not compute the current position from a body of records. `spec.md` §11 is explicit — *"a body
of TDRs supports the current position; it does not compute it"* — and nothing here changes that.
Temporal semantics exist so that interpretations are honestly timestamped, not so that a skill can
resolve them into a timeline. Resolution belongs above the artefact boundary.

## Anti-patterns

- **Document date as decision date** — precise, plausible, usually wrong.
- **Recency as authority** — the newest source assumed to be current.
- **Tense laundering** — intention recorded as outcome.
- **Silent date inference** — a quarter inferred from a filename and presented as `valid_time`.
- **Timeline construction** — assembling a narrative sequence the sources do not individually support.
