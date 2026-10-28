# FIX-404 — a role is not a job

> **Fictional worked fixture.** Hollin Vale Building Society is invented.

**Proves:** the participant-change test separates jobs from roles, teams and implementations.

## Source

**A — Team charter, payment operations**

> The team's responsibilities: operate the payment exceptions team; build the new repair screen;
> manage the BACS returns rota; make sure members whose payments fail are not left out of pocket.

## Expected

- **One** job, from the last clause: *Prevent members whose payments fail from being left out of
  pocket* (or an equivalent verb + object + clarifier), `established_by: unknown`.
- The other three reported with the reason each fails the participant-change test: a team (structure),
  a temporary solution (implementation), a rota (allocation).

## Must not

- Record "Operate the payment exceptions team" as a job.
- Record "Build the new repair screen" as a job.
- Record "Manage the BACS returns rota" as a job.
- Invent the decision that established the surviving job.
