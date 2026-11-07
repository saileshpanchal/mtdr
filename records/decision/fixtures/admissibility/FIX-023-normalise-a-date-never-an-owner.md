# FIX-023 — normalise a date, never infer an owner

> **Fictional worked fixture.** Kestrel Valley Water, its people and its numbers are invented.

**Proves** where `inferred` is permitted and where it never is.

## Sources

**A — Minute, `ops-forum/minute-14-3-19.md`**

> Meeting of 14/3/19. Agreed: chlorine dosing at Dunmore moves to the automated controller. The ops
> director to oversee.

**B — Organisation chart, `people/2019-structure.md`** — Operations Director: P. Rahman.

## Expected

- **`decision-date: 2019-03-14`, `derivation: inferred`** — a narrowly evidenced normalisation of
  the minute's own `14/3/19`. Permitted.
- **`accountable-owner` is missing.** The minute names a role, not a person.

## Must not

- **Contribute "P. Rahman" as owner, `inferred` from the chart** — a never-inferred role, and the
  contract refuses it (see `tests/recovery/candidate/FIX-509`).
- **Contribute "P. Rahman" as owner, marked `explicit`.** No span joins the role in the minute to the
  name on the chart for that meeting.
- **Read `14/3/19` as 3 February** or leave it unparsed: the normalisation is the permitted case.

## What this fixture detects

The line between tidying a value the evidence states and supplying one it does not.
