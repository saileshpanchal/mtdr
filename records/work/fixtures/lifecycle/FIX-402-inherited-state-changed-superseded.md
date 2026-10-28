# FIX-402 — the inherited state changes; the record is superseded

> **Fictional worked fixture.** Hollin Vale Building Society is invented.

**Proves:** a change to the state in force around the work — here a severity threshold — produces a
**superseding** record, with the same participant throughout.

## Source

**A — In-force record:** OIR-0001, severe defined as *a vulnerable member or a payment of £10,000 or
more*.

**B — Operational risk committee minute, 2026-09-03 (TDR-0188)**

> Agreed: with effect from 1 October an exception is severe at £5,000 or more, following the August
> review. Vulnerable-member criterion unchanged.

The same operations team performs the work before and after.

## Expected

- A candidate **OIR-0002**, `supersedes: OIR-0001`, `effective_from: 2026-10-01`, with the new
  threshold in **You inherit** and `derived_from` citing TDR-0188.
- OIR-0001 left intact, its status transitioning to `superseded` only on ratification.
- Every clause the change did not touch carried forward with its original source marker.

## Must not

- Edit OIR-0001 in place.
- Date the new record from the minute (3 Sep) rather than the stated effective date (1 Oct).
- Mark unchanged clauses as changed, or drop their references.
- Treat the unchanged performer as a reason not to supersede.
