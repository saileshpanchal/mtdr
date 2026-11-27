# FIX-023 — assemble a date across spans, never infer an owner

> **Fictional worked fixture.** Kestrel Valley Water, its people and its numbers are invented.

**Proves** where `inferred` is permitted and where it never is.

## Sources

**A — Minute, `ops-forum/minute-14-3-19.md`**

> **Operations forum minutes, 2019 series.** …
>
> Thursday 14 March. Agreed: chlorine dosing at Dunmore moves to the automated controller. The ops
> director to oversee.

**B — Organisation chart, `people/2019-structure.md`** — Operations Director: P. Rahman.

## Expected

- **`decision-date: 2019-03-14`, `derivation: inferred`** — the day from the entry's text, the year
  from the minute's own header: a value assembled across two spans of one source. Permitted.
- **`accountable-owner` is missing.** The minute names a role, not a person.

## Must not

- **Contribute "P. Rahman" as owner, `inferred` from the chart** — a never-inferred role, and the
  contract refuses it (see `tests/recovery/candidate/FIX-509`).
- **Contribute "P. Rahman" as owner, marked `explicit`.** No span joins the role in the minute to the
  name on the chart for that meeting.
- **Leave the year out, or take it from the file's name.** The header states it, and the inference
  across spans is the permitted case.
- **Mark a date the text states in full as `inferred`.** Rewriting a stated date is `explicit`.

## What this fixture detects

The line between tidying a value the evidence states and supplying one it does not.
