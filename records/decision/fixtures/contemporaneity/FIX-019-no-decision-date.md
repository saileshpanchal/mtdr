# FIX-019 — no decision date: every grade indeterminate

> **Fictional worked fixture.** Ashgrove Rail, its people and its numbers are invented.

**Proves** that a missing decision moment is never assumed, and never inferred from the material's
other dates.

## Sources

**A — Minute extract, `board/extract-paper-tickets.md`, undated**

> The board agreed to retire the paper ticket stock at all staffed stations, as recommended in paper
> 21/14.

**B — Paper 21/14, dated 2021-04-28** — as in FIX-018.

## Expected

- **One candidate**, `decision-date` and `accountable-owner` in `missing_semantics`, and
  `event_time_ref: unknown`.
- **B's context contribution computes `indeterminate`.** With no event time there is nothing for it
  to be contemporaneous with.
- **The candidate is admissible.** The missing date is the finding, reported in `unresolved`.

## Must not

- **Take 2021-04-28, the paper's date, as the decision date** — or any date after it, or the date of
  the extract's file.
- **Grade B `contemporaneous` because papers usually precede the meeting that decides them.**
- **Refuse the candidate for being incomplete.**

## What this fixture detects

The most plausible inference in recovery — the decision happened soon after the paper — presented as
evidence.
