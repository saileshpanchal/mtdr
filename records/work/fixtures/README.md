# Work fixtures — EXPERIMENTAL

Known-answer fixtures for the experimental Operational Inheritance Record (TDR-0047), organised on the
two things the experiment must not get wrong. Every fixture states **expected** and **must-not**
results; a run satisfying only the first has not passed.

| Axis | Fixtures |
|---|---|
| [`lifecycle/`](lifecycle/) — the capability-relativity hypothesis, in both directions | FIX-401 (participant replaced: no new record) · FIX-402 (inherited state changed: superseded) |
| [`boundaries/`](boundaries/) — what an OIR must never contain | FIX-403 (authority is referenced, never granted) · FIX-404 (a role is not a job) · FIX-405 (experience is context, not practice) |
| [`no-record/`](no-record/) — recovery that correctly yields nothing | FIX-406 (a run book is not an inheritance record) |

**FIX-401 and FIX-402 together test capability-relativity, not nativeness.** Passing both rules out a
participant-centred record; it says nothing about whether the OIR is irreducible. That is TDR-0046's
deletion attack, which these fixtures do not run.

All organisations, people and records are invented.
