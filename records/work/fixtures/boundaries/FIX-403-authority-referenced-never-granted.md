# FIX-403 — authority is referenced, never granted

> **Fictional worked fixture.** Hollin Vale Building Society is invented.

**Proves:** a statement of what a participant may do, with no instrument behind it, yields an
`authority` clause marked **missing**, never asserted.

## Source

**A — Team wiki page "Exceptions — quick facts"**

> Operators can write off balances under £50 without sign-off. Anything bigger goes to the team lead.

No delegation, policy or decision is cited, and none is found in the material supplied.

## Expected

- An `authority` contribution with low epistemic confidence, flagged **unsourced**.
- The drafted clause: `authority: {source: missing}`, with the wiki statement reported as an unsourced
  claim awaiting its delegating instrument.
- An `escalation` contribution for "goes to the team lead", likewise unsourced.

## Must not

- `authority: {source: asserted}` — the schema rejects it, and a skill must not attempt it.
- Cite the wiki page as the authority reference. A description of practice is not a delegation.
- Infer a £50 write-off limit as delegated authority because the practice is long-standing.
- Name the team lead as the holder of a mandate.
