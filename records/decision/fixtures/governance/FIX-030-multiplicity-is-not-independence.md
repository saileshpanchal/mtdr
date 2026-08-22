# FIX-030 — separated powers reconstructed, and multiplicity that is not independence

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** separation of powers. **Proves:** the seven governance powers are reconstructed
separately with unresolved ones staying `UNKNOWN` (GR-04), and that independence is assessed against
seven dimensions rather than concluded from a forum existing separately (GR-17).

## Sources

**A — Model Oversight Committee terms of reference, `moc-tor-v2.md`, 2025-03-01**

> The Committee provides independent oversight of model performance across the Bank. The Committee is
> chaired by the Head of Model Performance and reports to the Collections Leadership Team. Members are
> nominated by the Managing Director, Collections and Recoveries.

**B — Model Oversight Committee operating note, `moc-operating-note.md`, 2025-03-01**

> The Committee's monitoring pack is produced by the Collections Analytics team. The Committee's
> monitoring thresholds are configured by Collections Analytics in agreement with the model owner.
> Where the Committee identifies a performance concern, it refers the matter to the model owner for
> response.

**C — Model Oversight Committee minutes sample, `moc-minutes-2025-06 to 2026-02.md`**

> Nine meetings. 22 performance concerns raised, 22 referred to model owners, 22 closed on model owner
> response. No matter escalated beyond the Collections Leadership Team. No threshold changed at the
> Committee's request.

**D — Ashcombe charter, `ashcombe-charter-v2.md`** — Senior Responsible Owner and model owner:
P. Nkemelu, Managing Director, Collections and Recoveries.

## Expected

- The seven powers reconstructed **separately** for the Model Oversight Committee, with at least these
  outcomes:
  - `challenge_authority` — the Committee, `OBSERVED` from A and C;
  - `execution_authority` — the model owner, `OBSERVED` from B and D;
  - `veto_waiver_or_override_authority` — **`UNKNOWN`**. Nothing in A–C gives the Committee power to
    refuse, block or require. It refers; the owner responds; the matter closes;
  - `suspension_or_containment_authority` — **`UNKNOWN`**;
  - `amendment_authority` — **`UNKNOWN`**;
  - `escalation_route` — Collections Leadership Team, `OBSERVED`, and never exercised beyond it;
  - `accountability_terminus` — P. Nkemelu, `INFERRED`, and cross-referenced to the contradiction in
    [FIX-020](FIX-020-contradictory-governance.md).
- An `independence_assessment` across all seven dimensions, concluding **`not-independent`** or
  `partially-independent`, on the basis that: the Committee reports through the function it oversees;
  its members are nominated by the accountable executive of that function; its evidence is produced by
  that function's analytics team; its thresholds are configured by that team in agreement with the
  model owner; and 22 of 22 concerns closed on the owner's own response.
- A `governance-finding` of `CHALLENGE_GAP`, materiality `high` — a forum described as independent
  oversight whose challenge the governed owner can configure, supply and answer.

## Must not

- **Conclude the Committee is independent because A says "independent oversight" and it is a separate
  committee with its own terms of reference.** This is the failure under test. Multiplicity is not
  independence.
- Default `veto_waiver_or_override_authority` to the Committee because it is the oversight body, or to
  the model owner because they hold execution. Neither is established; `UNKNOWN` is the answer.
- Collapse `challenge_authority` and `veto_waiver_or_override_authority` into one power. The Committee
  demonstrably holds the first and demonstrably is not shown to hold the second, and that gap is the
  finding.
- Read 22-of-22 closure as evidence the models are performing. It is evidence about the closure
  mechanism, and it is equally consistent with a challenge function that cannot make anything stick.
- Record the Collections Leadership Team as the accountability terminus. A committee is not a terminus
  (GR-18).
- Recommend abolishing or merging the Committee. The finding is that its independence is not
  established; the remedy is an authorised decision about reporting, nomination, evidence source and
  threshold control.
