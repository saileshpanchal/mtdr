# TDR — semantic roles

Roles a [`RecordContribution`](../../../specification/record-contribution.md) may target when
`target_object: consequential-decision`. Field definitions live in [`spec.md`](../specification/tdr.md) §4; this
file says only what interpretation may contribute to.

## Roles

| `semantic_role` | Maps to | Mandatory for a candidate |
|---|---|---|
| `decision-statement` | Body — Decision | **Yes** |
| `context` | Body — Context, what was known at the time | **Yes** |
| `decision-date` | `decision_date` | **Yes** |
| `accountable-owner` | `accountable_owner` | **Yes** |
| `confidence` | `confidence` | No — rarely stated in source material |
| `evidence-business` | Body — Evidence | No |
| `evidence-architecture` | Body — Evidence | No |
| `evidence-regulatory` | Body — Evidence | No |
| `evidence-operations` | Body — Evidence | No |
| `evidence-customer` | Body — Evidence | No |
| `evidence-data` | Body — Evidence | No |
| `evidence-external` | Body — Evidence | No |
| `alternative-rejected` | Body — Alternatives rejected | No |
| `option-foreclosed` | Body — Options foreclosed | No |
| `consequence` | Body — Consequences and review | No |
| `reversal-cost` | Informs `template` | No |
| `lineage-supersedes` | `supersedes` | No |
| `lineage-derived-from` | `derived_from` | No |

Roles are repeatable. Seven separate `alternative-rejected` contributions from five documents are
normal and correct; do not merge them into one.

## Roles that do not exist, and must not be invented

- **`status`** — a candidate's status is `proposed`. Nothing in source material sets it, and evidence
  that a decision was "approved" contributes to `decision-statement`, not to status. See
  [`shared/candidacy-and-ratification.md`](../../../specification/candidacy-and-ratification.md).
- **`template`** — chosen by applying the proportionality rule to `reversal-cost` evidence, not
  extracted.
- **`maturity`**, **`confirmed_by_outcome`** — lifecycle facts recorded by the organisation after the
  decision, never interpreted from the source that made it.

## Notes on the mandatory four

**`context` is the role most vulnerable to hindsight.** It must carry what was known *at the time*, so
a contribution to it may only come from material created at or before the decision. A later
retrospective explaining why the decision was made is evidence about the decision, not evidence of its
context, and importing it manufactures reasoning nobody had. See the hindsight rule in
[`identify-record-contributions`](../../../skills/shared/identify-record-contributions/).

**`accountable-owner` must be a named individual.** Material routinely names a forum — "the Committee
approved" — and a forum is not an owner. A contribution proposing a committee is a contribution to
`context`, and the owner is reported as missing. This gap is one of the most valuable findings
interpretation produces, because it is exactly what nobody notices until they are asked to defend the
decision.

**`decision-date` is not the document date.** See
[`shared/temporal-semantics.md`](../../../specification/temporal-semantics.md).

**`decision-statement` needs both a choice and a binding consequence.** Material that supports one but
not the other describes a plan or an aspiration. `practice/decision-grammar.md` carries the test — if
**We decide** and **This means** cannot both be filled, there is no decision to record.
