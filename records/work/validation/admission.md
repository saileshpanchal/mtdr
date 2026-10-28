# Operational Inheritance Record — admissibility test

**EXPERIMENTAL** (TDR-0047). Applied on top of the shared invariants in
[`candidacy-and-ratification.md`](../../../specification/candidacy-and-ratification.md). Admissibility
asks whether a candidate OIR is **worth putting in front of a named owner** — not whether the
inherited state is right, and not whether the record family deserves to exist (TDR-0046 asks that).

A candidate is admissible when all of these hold:

1. **A capability is identified, not a participant.** The title and every job survive the
   participant-change test. A candidate titled after a team, person, supplier or system is
   inadmissible as drafted.
2. **At least one job is evidenced** in verb + object + contextual-clarifier form.
3. **Inherited context is present or declared missing** — never silently absent. Its `missing`
   marker is an admissible state; an empty clause is not.
4. **Authority is referenced or declared missing.** A candidate asserting authority inline is
   inadmissible: the record grants none.
5. **Every clause carries a source marker**, and every `reference` names something resolvable in
   principle — an identifier, not a description.
6. **Conflicts are preserved.** Where sources disagree the clause is `conflicting` with every source
   cited; a candidate that chose between them is inadmissible.
7. **No practice is a fact about the work, and no fact is a practice.**
8. **Provenance is complete** for every asserted clause.
9. **Missing clauses are reported, not filled.**
