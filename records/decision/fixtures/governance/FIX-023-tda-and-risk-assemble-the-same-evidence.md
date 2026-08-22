# FIX-023 — the design authority and the risk forum assemble the same evidence separately

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** duplication. **Proves:** `FORUM_EVIDENCE_ASSEMBLY_OVERHEAD` — the duplication with the
clearest safe remedy. Assemble once, consume twice, change no mandate and no forum.

## Sources

**A — TDA pack, Ashcombe section, `tda-2026-02-11-pack.pdf`, pages 14–22**

> Contents: solution architecture; data flows; retention position; model performance summary
> (AUC 0.79, holdout Jan 2026); cohort performance breakdown by vulnerability flag; dependency map;
> Standard 3, 7, 9 and 11 conformance assessment.
>
> *Prepared by: Ashcombe delivery team. Pack cut-off 2026-02-04.*

**B — Risk Acceptance Forum pack, Ashcombe section, `raf-2026-02-18-pack.pdf`, pages 3–11**

> Contents: change description; data flows; retention position; model performance summary
> (AUC 0.79, holdout Jan 2026); cohort performance breakdown by vulnerability flag; residual risk
> assessment; control mapping; proposed risk acceptance.
>
> *Prepared by: Ashcombe delivery team. Pack cut-off 2026-02-11.*

**C — Delivery team retrospective note, `ashcombe-retro-2026-03.md`**

> Pack preparation for TDA and RAF took approximately 6 person-days in February. The two packs share
> most of their content but are laid out to each forum's template and cut at different dates, so they
> were built separately.

## Expected

- A `governance-finding` of `FORUM_EVIDENCE_ASSEMBLY_OVERHEAD`, `OBSERVED`, basis A, B and C.
- Overlap classified as **same evidence** — data flows, retention position, model performance, cohort
  breakdown appear in both, from one source, assembled twice.
- Overlap explicitly **not** same purpose. The TDA is assessing architectural conformance and design;
  the RAF is accepting residual risk. Each pack carries content the other does not.
- The differing cut-off dates (2026-02-04, 2026-02-11) recorded as a **second, separate finding** — the
  two forums assessed the same change against materially different evidence vintages, which is a
  traceability issue independent of the duplication.
- The safe remedy stated — assemble the shared evidence once, with one cut-off, consumed by both
  forums against their own templates.
- `reconstruction_metrics` carrying the 6 person-days from C, attributed to C rather than estimated.

## Must not

- **Recommend merging the TDA and the Risk Acceptance Forum.** They perform different jobs on
  different questions; a shared input is not a shared purpose.
- Recommend that one forum accept the other's conclusion. Nothing here establishes that either is
  entitled to rely on the other, and FIX-025 is where the independence question is tested.
- Treat the shared AUC figure as two pieces of evidence. It is one measurement, reported twice.
- Invent a saving. C supports 6 person-days of preparation; it does not support a claim about how much
  of that a shared assembly would remove.
- Resolve the cut-off difference by preferring the later pack. Both are what their forum saw.
