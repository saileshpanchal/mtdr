# Operational Inheritance Record — semantic roles

**EXPERIMENTAL** (TDR-0047). Roles a [`RecordContribution`](../../../specification/record-contribution.md)
may target when `target_object: operational-capability`. Clause definitions live in
[`oir.md`](../specification/oir.md) §3; this file says only what interpretation may contribute to.

| Clause | `semantic_role` | Frontmatter | Permitted markers |
|---|---|---|---|
| Purpose | `purpose` | `clauses.purpose` | asserted · reference · missing · conflicting |
| You inherit | `inherited-context` | `clauses.inherited_context` | asserted · reference · missing · conflicting |
| Jobs to be done | `jobs` | `jobs[]`, `clauses.jobs` | asserted · reference · missing · conflicting |
| Outcomes | `outcomes` | `clauses.outcomes` | asserted · reference · missing · conflicting |
| You are responsible for | `responsibilities` | `clauses.responsibilities` | asserted · reference · missing · conflicting |
| You may | `authority` | `clauses.authority` | **reference · missing only** |
| You must | `obligations` | `clauses.obligations` | asserted · reference · missing · conflicting |
| You should | `practices` | `clauses.practices` | asserted · reference · missing · conflicting |
| Escalate when | `escalation` | `clauses.escalation` | asserted · reference · missing · conflicting |
| Evidence | `evidence` | `clauses.evidence` | asserted · reference · missing · conflicting |

## Three role rules that are checked, not advised

1. **The participant-change test, for every `jobs` contribution.** Restate the job with a different
   performer — another team, a supplier, a software service, an AI participant. If the job must be
   rewritten, the span described a role, procedure or implementation and contributes no job.
2. **`authority` carries a reference, never a grant.** A span asserting what someone may do without
   citing the instrument that delegated it is contributed with low epistemic confidence and flagged
   unsourced. The drafted clause is `missing` until a source is found — never `asserted`.
3. **Experience is context; defaults are practice.** A span reporting how this work has failed, or
   what has caused harm, is `inherited-context`. A span recommending how the work is normally done is
   `practices`. A span doing both is contributed to both.

## Not roles

Allocation (who performs), procedure (how a task is done), organisational structure (which team) and
eligibility (who could perform) are **not** roles of this record. Spans carrying only these are
reported, so participant leakage is visible, and contribute nothing.
