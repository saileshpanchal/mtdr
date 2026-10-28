# FIX-401 — the participant changes; the record does not

> **Fictional worked fixture.** Hollin Vale Building Society is invented.

**Proves:** replacing the participant that performs a capability's work produces **no** new OIR and no
supersession, because the inherited state has not changed.

## Source

**A — In-force record:** OIR-0001, *Resolution of payment-processing exceptions*, effective
2026-03-02, accountable owner Priya Raman.

**B — Operating-model change notice, 2026-09-14**

> From 1 October the payment exceptions work moves from the Leeds operations team to the shared
> service centre. No change to delegations, thresholds, scheme obligations or the member commitment.
> Hand-over sessions 22–30 September.

## Expected

- The output states that the change is an **allocation** change, and that OIR-0001 remains in force.
- **No new OIR.** No `supersedes` record. `status` of OIR-0001 unchanged.
- The allocation is reported as allocation — a decision of its own, recordable as a decision record —
  and kept out of the inheritance record.

## Must not

- Draft OIR-0002 for "the shared service centre's payment exceptions".
- Supersede OIR-0001 because the performer changed.
- Write the shared service centre, or the Leeds team, into any clause.
- Treat the hand-over sessions as a change to inherited context.
