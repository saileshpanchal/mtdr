---
id: DAC-0043
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0043
title: Assure the record-to-specification binding
status: accepted
disposition: proceed-with-constraints
assessed_at: 2026-08-27
accountable_owner: Sailesh Panchal
review_date: 2027-02-27
confidence: high
supersedes: none
---

# DAC-0043 — Assure the record-to-specification binding

> **Accepted 2026-08-27**, `proceed-with-constraints`. Routed because TDR-0043 changes all three
> record families and discharges a release obligation. Its six constraints bind.

## Uncertainty

Known: the gap, its cause, its extent, and that the fix is one optional field. Unknown: whether the
identifier scheme is legible to someone meeting it for the first time with no context — which this
case cannot establish, because everyone who could test it here already knows the answer.

Assumption: that resolution *by rule* is more durable than resolution by service. Confidence is high
because the alternative is checkable — a URL that has already drifted to `/blob/main/` in the
schemas' own `$id` values is the counter-example, sitting in this repository.

## Adversarial projection

The realistic abuse is **`conforms_to` read as a claim it does not make**. The string looks
authoritative and sits at the top of the file, so a reader in a hurry may take it as evidence the
record is valid, current, or accepted. It is none of those: it states which specification the record
is *presented as* conforming to. A forged or mistaken value is as easy to write as a correct one.

The second is **version drift as a quiet lie**. A record backfilled to a version it was never
reviewed against still claims that version. The mitigation is narrow rather than complete: the suite
requires every record's binding to agree with its package manifest, so a record cannot claim a
version this distribution does not ship.

The third is **scheme creep** — the temptation to carry standing, provenance or authority in the same
string because it is already there. Foreclosed in the record.

## Customer-outcome projection

Routed lightly and materially. The people most affected are those reading a record as evidence, long
after the fact, holding only the file: an auditor, a successor, a regulator, someone reconstructing
what an organisation committed to. Until now that reader could not establish what rules the record
claimed to follow. That is a small change to the file and a large change to what the file can be
asked to do.

The countervailing harm is over-trust, addressed above.

## Control side-effects

An optional field creates two populations — records that travel and records that do not — and a
future reader may take absence as a defect rather than a choice. The record states that it is not.
The opposite side-effect, making it required, was rejected for reasons that would have created a
larger problem: invalidating history to add a convenience.

## Execution capability

Fully within reach and done: one optional property on three schemas, additive minor versions, 54
governed records backfilled, and a detached-resolution test the suite runs on every invocation.

## Constraints

Proceed only with these.

1. **The detached test must copy a record OUT and resolve it with no repository present.** A test
   that reads the record in place proves nothing about detachment, and would be the serialisation
   round-trip's mistake repeated — the register already warned that a local precursor "proves nothing
   about a detached record."
2. **Every record's binding must agree with its package manifest**, enforced, so a record cannot
   claim a specification version this distribution does not ship.
3. **The scheme carries type, package and version only.** No standing, provenance, authority or
   integrity claim enters the identifier without a superseding decision.
4. **Resolution stays derivable by rule.** No registry, network call or service may become necessary
   to interpret a record.
5. **The limit is stated, not implied.** TDR-0043 must record that its detached test is executed by
   the author and therefore proves the rule works rather than that the scheme is legible cold. That
   remains DAC-0032 constraint 4's question.
6. **`conforms_to` absence is never reported as invalidity.** The schemas accept its absence, and any
   tooling that treats a record lacking it as non-conformant has misread this decision.

## Review

At the evidence named in TDR-0043, or 2027-02-27. The trigger that reopens this case earlier is any
tool, adopter or projection treating `conforms_to` as evidence of validity, currency or standing.
