# FIX-004 — complete in one source

> **Fictional worked fixture.** Meridian Mutual, its people and its numbers are invented.

**Proves** the constraint is stated correctly. A skill must never *assume* a complete record exists in
a single source — but some sources do carry one, and manufacturing scatter where none exists is its
own failure.

## Source

**A — Decision paper, `data-platform-migration-decision.md`, dated 2026-04-02**

> **Decision.** We will migrate the customer data platform to a managed service, beginning Q3 2026.
>
> **Owner.** Tomas Lindqvist, Director of Data.
>
> **What was known.** The current platform reaches end of vendor support in March 2027. Two viable
> managed services were assessed against our data residency requirements; both meet them. Internal
> capacity to maintain the existing platform falls to one engineer from September 2026.
>
> **Alternatives.** Rebuild in-house — rejected, no capacity. Extend vendor support — rejected,
> quoted at £340k for twelve months with no roadmap beyond it. Do nothing — rejected, unsupported
> platform holding customer data.
>
> **What this forecloses.** Committing to this vendor's data model makes a later move to a third
> provider materially harder; accepted deliberately.
>
> **Confidence.** Medium — the residency assessment is complete, the migration effort estimate is not.
>
> **Review.** Confirm by the end of Q1 2027 against migration completion and incident count.

## Expected

- **1 SourceFragment or several**, at the skill's discretion on span boundaries.
- **Contributions covering all four mandatory decision roles** — `decision-statement`, `context`,
  `decision-date`, `accountable-owner` — plus `alternative-rejected` (three, separately),
  `option-foreclosed`, `confidence`, `consequence`, and `reversal-cost`.
- **Exactly 1 CandidateAssembly**, `target_object: consequential-decision`.
- **`missing_semantics` is empty**, and that empty list is a claim the skill is making.
- **`grouping_basis` may cite a single source** — where all contributions come from one fragment or
  one contiguous document, grouping is trivially evidenced and should say so plainly.
- **The proportionality outcome is `full`**, with the reversal-cost reasoning naming the foreclosure
  and the £340k alternative. This is expensive to reverse.
- **`alternative-rejected` appears three times**, not once. Roles are repeatable.

## Must not

- **Fragment the decision into multiple candidates.** One decision, one candidate.
- **Report missing semantics that are present.** Every mandatory role is evidenced here.
- **Demand corroboration from a second source** before proposing. One sufficient source is
  sufficient.
- **Merge the three alternatives into one contribution.**
- **Emit `status` beyond `proposed`**, or treat the paper's completeness as ratification. A complete
  candidate is still a candidate — the paper's own author is not thereby the ratifying owner, and
  `accountable-owner` here is a *proposed* interpretation like any other.
- **Route to `minimal` or `bare`.** The foreclosure and the cost make this a full-template decision.

## What this fixture detects

Two opposite failures.

A skill over-tuned to scatter will look for the missing pieces of a record that is not missing any,
and will either report phantom gaps or split one decision across several candidates.

A skill that treats source completeness as authority will emit something beyond `proposed` — reasoning
that a document this well-formed must already be the record. It is not. It is a well-formed source,
and the ratification it still needs is the whole point of the separation.
