# CORPUS-003 — the implicit decision

> **Fictional corpus case.** Meridian Mutual is invented.

**Category:** implicit proposition. A commitment nobody states as a decision — a workaround that
hardened into the way things work. Tests whether identification finds decision *moments*, not
decision *language*.

## Sources

**A — Incident retrospective, `inc-2044-retro.md`, dated 2026-03-02**

> During the outage, batch settlement was rerouted through the legacy gateway. Workaround to be
> reviewed once the new gateway is patched.

**B — Operations note, `ops-weekly-2026-04-20.md`**

> Batch settlement continues via the legacy gateway. The patch shipped in week 14; no cutover has
> been scheduled. Team preference is to leave it, since throughput has been stable.

**C — Capacity plan extract, `h2-capacity-plan.xlsx`, dated 2026-06-01**

> Legacy gateway: sized for continued batch settlement load through FY27.

## Expected

- Contributions to **one** `consequential-decision` whose statement is the *quiet default*: the
  temporary reroute has become standing routing. B evidences the moment the workaround outlived its
  stated trigger (patch shipped, no cutover, preference to stay); C evidences the organisation
  committing resources to it.
- **One candidate**, template tier argued from the FY27 capacity commitment — this is no longer
  cheap to reverse.
- `missing_semantics` includes `accountable-owner` and `decision-date` — **and the fuzziness of the
  date is itself the finding**: the honest value is unknown, bounded between weeks 14 and the
  capacity plan.
- The identification notes explicitly that no source contains decision language.

## Must not

- Report "no decision present". That outcome is for material that genuinely decides nothing —
  here the organisation has committed capacity for eighteen months.
- Invent a decision date from any single document's date.
- Attribute the decision to "the team" as owner — preference evidence is context, not ownership.
- Record A alone as the decision. The incident reroute was a workaround with a stated review
  trigger; the decision is what happened *after* the trigger fired and nothing changed.
