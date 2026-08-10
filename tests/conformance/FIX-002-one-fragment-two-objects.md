# FIX-002 — one fragment, two objects

> **Fictional worked fixture.** Meridian Mutual, its committee and its numbers are invented.

**Proves** the central architectural claim: interpretation reconstructs organisational state rather
than sorting documents into buckets. A single span contributes to two different objects, and no
`record_type_hint` on the fragment could have expressed that.

## Source

**A — Committee minute, `investment-committee-2026-04-16.md`**

> The Committee approved the investment subject to maintaining complaints below 4%.

That is the whole source. One sentence.

## Expected

- **1 SourceFragment.**
- **At least 3 RecordContributions from that one fragment**, spanning **two different
  `target_object` values**:
  - `target_object: consequential-decision` → `decision-statement` (the approval)
  - `target_object: consequential-decision` → `context` or `option-foreclosed` (the condition as it
    bears on the decision)
  - `target_object: ovc` → `review-boundary` (the 4% threshold — the *Unless* clause of the OVC
    grammar)
- **2 CandidateAssemblies**, one per object, each `status: candidate`.
- **Both carry substantial `missing_semantics`.** The decision candidate is missing
  `accountable-owner` and `decision-date`; the commitment candidate is missing almost everything —
  `value-thesis`, `baseline`, `beneficiary`, `expected-value`, `value-kind`, `recognition-route`,
  `due-point`, `finance-countersignatory`, `falsifying-signal`.
- The commitment candidate is **admissible but very incomplete**, and reported as such.

## Must not

- **Produce one candidate.** Treating the sentence as belonging to a single record is the failure
  this fixture exists to catch.
- **Record "the Committee" as `accountable-owner`.** A forum is not a named individual. The
  committee reference contributes to `context`, and the owner is reported missing.
- **Render "approved" as a status.** Evidence that something was approved contributes to
  `decision-statement`, never to `status`.
- **Discard the commitment candidate for being too thin.** Incompleteness is a result. A skill that
  suppresses sparse candidates will suppress exactly the findings nobody else has noticed.
- **Infer a decision date from the minute's date.** The minute records the approval, so its date is
  evidence — but it is `record time`, and using it as `decision-date` without saying so is the
  document-date error.
- **Invent the investment's value, size or subject.** The source says none of it.

## What this fixture detects

A skill built around "which record type is this document?" cannot pass. It will pick one object,
usually the decision, and the review boundary — the condition the organisation attached to the money
— will disappear entirely.

That is the quiet failure mode: nothing looks wrong, one plausible record is produced, and the
constraint that made the approval conditional is simply gone.
