# CORPUS-002 — contradictory contributions with no ordering

> **Fictional corpus case.** Ashworth Building Society is invented.

**Category:** contradiction. Two sources state incompatible values for the same semantic role, with
no shared authority lineage and no documented ordering — a **conflict**, which must be recorded, not
resolved.

## Sources

**A — Programme board pack, `q2-board-pack.pdf`, page 12, undated section**

> The branch consolidation decision was approved with a customer-impact threshold of 5% complaint
> uplift, above which the rollout pauses.

**B — Operations runbook, `consolidation-runbook-v2.md`, revision date 2026-06-14**

> Pause threshold: 8% complaint uplift, per the approval.

Both claim to state "the" approved threshold. Neither cites the other. The board pack's section is
undated; the runbook is dated but is an operational document citing an approval it does not quote.

## Expected

- Contributions from both sources to the same `consequential-decision`, same role (the threshold as a
  condition of the decision).
- **One CandidateAssembly** — the entity match ("the branch consolidation decision", "per the
  approval") is admissible — with **one entry in `conflicts`** naming both contributions.
- `unresolved` states what would settle it: the approval minute itself, which neither source is.
- `epistemic_confidence` on both threshold contributions: not `high` — each is a report of an
  approval, not the approval.

## Must not

- **Resolve by recency.** The runbook's revision date is not authority lineage; date order alone
  establishes nothing, and preferring 8% asserts a supersession without evidence.
- **Resolve by source dignity** — preferring the board pack because boards outrank runbooks is the
  same error with better manners.
- Split into two candidates to avoid recording the conflict. The entity match is real; the conflict
  is the finding.
- Average, range, or otherwise blend the two values.
