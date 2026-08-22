# FIX-020 — contradictory accountable ownership, with no supersession between the sources

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** contradiction. **Proves:** conflicting governance claims produce `CONTRADICTORY` with
both sides referenced, and are never resolved by recency, by seniority, or by which document looks
more official (GR-09).

## Sources

**A — Responsibilities map, `smf-responsibilities-2025-12.md`, 2025-12-15**

> Accountable executive for automated customer contact decisioning: **D. Farrell**, Chief Operating
> Officer. Includes model-driven contact strategies deployed in Collections.

**B — Project Ashcombe charter, `ashcombe-charter-v2.md`, 2026-01-09**

> Senior Responsible Owner: **P. Nkemelu**, Managing Director, Collections and Recoveries. The SRO is
> accountable for the delivery and ongoing operation of the Ashcombe contact strategy, including model
> performance and customer outcomes.

**C — Model risk register extract, `model-register-2026-02.csv`, row for ASH-CS-01**

> Model owner: P. Nkemelu. Accountable executive: D. Farrell. Last review: 2025-11-30.

Neither A nor B cites the other. Neither states that it supersedes anything. C records both names
against different columns without defining the relationship between them.

## Expected

- The claim *"who is the accountable executive for Ashcombe's contact decisioning"* assessed as
  `CONTRADICTORY`, with **at least two** `contradiction_refs` naming A and B.
- A `governance-finding` of type `CONTRADICTORY_GOVERNANCE`, materiality `high`.
- `separated_powers.accountability_terminus` reported as **unresolved**, with the contradiction as its
  basis — two named individuals is not a terminus.
- `recommended_next_evidence` naming what would settle it — a delegation instrument, a committee
  minute allocating the responsibility, or a version of A or B that cites the other.
- C recorded as evidence that the Bank holds **both** readings simultaneously, which strengthens the
  contradiction rather than resolving it.

## Must not

- **Resolve by recency.** B is seven weeks later than A. Date order is not authority lineage, and
  preferring the charter asserts a supersession no source states.
- **Resolve by seniority.** Preferring the COO because a COO outranks an MD is the same error with
  better manners.
- **Resolve by document type** — preferring the responsibilities map because responsibilities maps are
  where accountability lives. That is source dignity, not evidence.
- Read C as the reconciliation. It records both names in different columns and defines neither; a
  register reflecting an ambiguity is not a resolution of it.
- Split into two findings to avoid recording a contradiction. Both claims concern one accountability
  for one thing, and the conflict is the finding.
- Report `accountability_terminus` as "COO and MD jointly". Nothing in the material establishes joint
  accountability, and inventing it is how a contradiction disappears.
