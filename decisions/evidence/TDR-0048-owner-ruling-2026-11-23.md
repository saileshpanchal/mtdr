# Owner's ruling of 23 November 2026 — candidate views, not proposed TDRs

This note preserves the ruling that amended [TDR-0048](../TDR-0048-historical-recovery-doctrine.md)
while it was proposed. It is decision input. It is **not ratification evidence**: TDR-0048 stays
`proposed`, and ratification needs a later act that names the content it accepts (TDR-0027).

## Where the ruling is recorded

**The only record of this ruling is the message of commit `4aa7d5f`**, written by the maintainer's
assistant when it applied the ruling on 23 November 2026. The commit message quotes the ruling. This
note copies that quotation; it is not the owner's own record. **The owner is asked to confirm the
words, or to correct them, at ratification.**

| Element | Evidence |
|---|---|
| Actor | Sailesh Panchal, as quoted in commit `4aa7d5f` |
| Authority | Repository authority and accountable owner for MTDR's design decisions |
| Date | 2026-11-23 |
| Ruling, as quoted | *"Render recovered candidates as candidate views, not as proposed TDRs."* |
| What prompted it | A status mismatch the standard itself caused. `draft-tdr` required `status: proposed`, so a rendering said `proposed` beside a candidate that says `status: candidate` and `standing: none`. The commit message says engine runs on 20 and 22 November reproduced it |
| Option chosen | Option A of the status mismatch, as the commit message names it |

## What is not preserved here

- **The engine runs of 20 and 22 November.** They are not in this repository, and this note does not
  establish what they ran or produced.
- **The options the ruling chose between.** TDR-0048 states the two it rejected. The text of the
  options as put to the owner is not preserved.

## What the ruling changed

As commit `4aa7d5f` applied it:

- [`draft-tdr`](../../records/decision/skills/draft-tdr/SKILL.md) §7. A rendering of a historical
  candidate carries the candidate's header (`candidate_id`, `status: candidate`, `standing: none`,
  `retrospective: true`) and the TDR-shaped body. It is deliberately not TDR-valid, and it becomes a
  TDR draft only when a named individual proposes it. §3 and Outputs say so, and
  `recover-decision-records` stage 3 names the view.
- [`historical-recovery.md`](../../specification/historical-recovery.md). A candidate renders as a
  view of a candidate, and rendering confers nothing.
- TDR-0048, amended in place, with the ruling quoted and the two rejected options. There was no TDR
  schema change, and the TDR specification stays at 1.15.0.

The commit message also records that this named change to canonical skills was the owner's ruling, and
that it overrode the instruction not to alter canonical skills for this change only.

## The owner's disposition of 27 November

Asked to confirm the words, the owner directed: *"Preserve the current rule that retrospective
candidates remain candidate views, without inventing evidence of earlier ratification."*
([dispositions](TDR-0048-0049-0050-owner-dispositions-2026-11-27.md)). The rule is therefore kept as
TDR-0048 states it. This note remains the record of a ruling quoted in a commit message. It is not
evidence that anything was ratified on 23 November, and nothing here is read as such.
