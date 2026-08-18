---
id: TDR-0038
title: Generate distribution bundles from the manifests, and codify the layer boundary
status: accepted
template: full
decision_date: 2026-08-18
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0020, TDR-0023, TDR-0024, TDR-0032, TDR-0035
confirmed_by_outcome: pending — review when someone outside this project has deployed a bundle to a runtime and produced governed records without maintainer help, or 2027-08-18, whichever is sooner
---

# TDR-0038 — Generate distribution bundles from the manifests, and codify the layer boundary

## Context — what was known at the time

The deployment pack was one hand-written page and one worked example. It asserted that the skills load
unmodified in several named runtimes, and nobody had checked. It also carried a skill count that had
quietly drifted, which is a small instance of the general problem: **a claim about the outside world,
written once and never re-examined, decays silently.**

Underneath sat a larger ambiguity. Adopters arrive with an agent stack already — skills, plugins, a
protocol — and reasonably ask what MTDR adds. The answer existed across
[TDR-0024](TDR-0024-packaging-independence.md), [TDR-0032](TDR-0032-typed-multi-object-conformance.md)
and [TDR-0035](TDR-0035-standards-boundary.md), and nowhere in one place, so it was being reconstructed
per conversation.

## Decision

**1. Verify runtimes, and keep the verification as an artefact.**
[`skills/packaging/runtime-evidence.md`](../skills/packaging/runtime-evidence.md) records, per runtime:
discovery mechanism, canonical-skill compatibility, progressive-disclosure behaviour, invocation,
transformations required, source, date, and **what could not be verified**. Research embedded
invisibly in an adapter cannot be re-checked when the runtime changes; research recorded as evidence
can.

**2. The falsification criterion, which governs every adapter this repository will ever ship:**

> **If supporting a runtime requires changing the meaning of a canonical MTDR artefact, that runtime
> is unsupported — it is not a reason to change MTDR.**

Adapters translate **packaging and invocation, never semantics**.

**3. Bundles are generated from the manifests** by [`mtdr_packaging`](../mtdr_packaging/), which is
non-normative on the same terms as `mtdr_validation`. The catalogue is enumerated from each
`package.yaml`, never hand-maintained, and the suite proves the bundles are neither stale nor
divergent nor semantically altered.

**4. One collection, not one per surface.** Every runtime verified reads canonical `SKILL.md` files
directly, so five copies would demonstrate only that copying works. A single collection every surface
points at makes a divergent catalogue *impossible* rather than merely detectable. Per-surface content
is reduced to what is genuinely per-surface: where the files go, how they are invoked, and what
remains unverified.

**5. Collection is the only transformation, and the links stay broken.** MTDR stores skills two levels
deep because they live with the record semantics they serve (TDR-0023), and no runtime scans that
shape — so a bundle collects them flat. Their canonical relative links then do not resolve inside the
bundle, and **they are not rewritten**, because rewriting them would modify a canonical artefact. The
bundle instead requires the reference-knowledge layer to be deployed alongside.

The finding underneath is recorded rather than smoothed over: **for MTDR the natural distribution unit
is a subset of the repository, not a flat directory of skill files.** Runtimes want the flat shape; the
standard will not acquire one to suit them.

**6. Codify the layer boundary** ([`specification/standards-boundary.md`](../specification/standards-boundary.md)):
knowledge and provenance packaging · procedural capability (`SKILL.md`) · packaging and distribution ·
interaction (MCP) · **governed semantics and lifecycle (MTDR)** · **standing (authorised human acts)**.

Two rows carry the argument. **Nothing but MTDR occupies the semantics-and-lifecycle layer** — a skill
expresses a method but cannot say that a commitment lacking a counter-signatory is a valid candidate
and an ineligible ratification. **Nothing at all occupies the standing layer**, and nothing can: a tool
that appears to supply standing has relocated accountability into software. An adopter does not choose
between MTDR and their agent stack; they keep the stack and gain the layer it lacks.

## Evidence

- **Business** — the first adopter question is what else they must install and what this replaces. Both
  are now answered on one page, from checked facts.
- **Architecture** — the verification found every runtime `direct`: none requires a transformed skill
  file. The strongest available evidence for TDR-0024 turns out to be that there is almost nothing for
  a packaging adapter to do.
- **Regulatory** — not material.
- **Operations** — bundles regenerate from the manifests, and drift is a suite failure rather than a
  discovery. The skill count cannot drift again; nor can a catalogue.
- **Customer** — not material at repository level.
- **Data** — the Agent Skills specification admits six frontmatter fields; MTDR's contract permits two,
  and the suite has enforced that since before any of this was checked. Narrow frontmatter is *why*
  every runtime reads these files unmodified — a field outside the spec makes packaging fail hard, so
  the narrowest surface is the most portable one.
- **External** — five runtimes checked against their own documentation, three from primary sources and
  two from secondary ones with the shortfall named. Nothing was inferred to complete the matrix.

## Alternatives rejected

1. **Keep hand-written deployment pages.** Rejected: they assert facts about other people's software
   with no date, no source and no way to notice when they stop being true.
2. **Generate five full copies of the skills, one per surface.** Rejected: it proves only that copying
   works, and makes divergence possible in order to then detect it. One collection makes it impossible.
3. **Rewrite relative links so they resolve inside the bundle.** Rejected under the criterion above.
   Convenience for a bundle reader is not a reason to modify a canonical artefact.
4. **Flatten the canonical skill layout to match what runtimes scan.** Rejected: it would invert
   TDR-0023 — putting the standard's structure at the disposal of its consumers, which is the failure
   TDR-0020 was written to prevent.
5. **Include a runtime whose loader could not be verified, to complete the set.** Rejected. Two rows
   carry secondary evidence and say so; a guessed path is worse than an absent one.
6. **Leave the layer boundary implicit across three records.** Rejected: it was being reconstructed per
   conversation, and inconsistently.

## Options foreclosed

- No adapter may modify a canonical artefact, in any respect, for any runtime.
- No runtime may be listed as supported without evidence recorded with its source and date.
- No catalogue may be hand-maintained.
- No surface may advertise a different catalogue from any other.
- The canonical skill layout cannot be flattened to suit a runtime without superseding this record.
- No packaging surface may add record semantics, and none may claim behavioural conformance.

## Consequences and review

Success is someone outside this project deploying a bundle to a runtime and producing governed records
without maintainer help — the zero-install proof DAC-0032 constraint 4 has been waiting for, which this
record makes attemptable but does not satisfy.

The nearer consequence is that the repository's claims about other people's software are now dated,
sourced and re-checkable, and two of them are marked provisional because they could not be verified
from a primary source. That is a less comfortable page than the one it replaces, and a more useful one.

Review at the confirmed-by-outcome trigger, or whenever a runtime changes how it loads skills.
