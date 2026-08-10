# Candidacy and ratification

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

## The one rule

**The skill proposes; the organisation ratifies.**

A skill may determine whether the evidence supports an admissible candidate. It may never turn that
candidate into organisational truth. This is a constitutional separation, not a user-interface
convention, and it is stated in [TDR-0018](../decisions/TDR-0018-interpretation-skills-and-the-artefact-boundary.md)
as a condition of interpretation skills existing here at all.

## The lifecycle

```
Evidence → Contributions → Candidate Assembly → Admissibility Assessment
        → Authorised Ratification → Governed Record
```

Everything to the left of ratification is interpretation, and reversible at no cost. Ratification is
the act that creates accountability, and it is performed by a named individual — never by a committee,
and never by a tool.

## Not to be confused with the language admission test

This repository already uses "admission" for something else: [TDR-0017](../decisions/TDR-0017-language-admission-test.md)
defines a seven-criterion **language** admission test, asking whether a specification qualifies as a
language. That is a question about specifications.

**Admissibility here is a question about a candidate record**: does the evidence support proposing
this to a human? The two never interact, and the naming of this file keeps them apart.

## Admissibility assessment

Admissibility asks whether a candidate is *worth putting in front of a named owner*, not whether it is
correct. A candidate is admissible when:

- every interpreted value traces to a locatable span ([`provenance.md`](provenance.md))
- the grouping basis is stated and admissible ([`identity-and-grouping.md`](identity-and-grouping.md))
- missing mandatory semantics are reported rather than filled
- conflicts are recorded rather than resolved
- the record package's own admission test passes

**A candidate with missing semantics is still admissible.** Incompleteness is information — it tells
the owner precisely what to go and find. Only invention makes a candidate inadmissible.

## What ratification is

Ratification is a named individual accepting accountability for the record's content. It is not review,
approval routing, or a workflow state. Its consequences are the ones the standard already carries: from
that moment the record has an accountable owner, and it is superseded rather than edited
([`spec.md`](../spec.md) §§6–7).

**How ratification is captured, authorised or evidenced is outside this standard.** It happens above
the artefact boundary. What is inside the boundary is the guarantee that no skill performs it.

## Consequences for skill design

- No skill emits a record with `status` beyond what a proposal can justify. Candidates propose;
  `proposed` is the ceiling.
- No skill assigns an accountable owner as fact. It may propose one from evidence, marked as
  interpretation like any other value.
- No skill marks a value commitment agreed, or a decision accepted, on evidence alone.
- A skill that cannot find a named owner reports the gap. It does not select a plausible one, and it
  does not fall back to a team or a committee.

## Anti-patterns

- **Ratification by absence** — treating an unchallenged candidate as accepted.
- **The auto-owner** — inferring the accountable individual from document authorship and recording it
  as fact.
- **Status inflation** — emitting `accepted` because the evidence looked strong.
- **Committee ownership** — naming a forum where the standard requires an individual.
- **Ratification as workflow** — modelling approval steps inside the standard, which is exactly the
  runtime concern the artefact boundary excludes.
