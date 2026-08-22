---
name: regime-preservation
description: Apply the hard guardrail to every governance disposition and evolution projection before it is proposed — an externally mandated mechanism stays unless evidence and authority show otherwise, a source that cannot be located is not permission to remove anything, internal authority cannot amend a superior external obligation, and no system may invent the authority needed to make its own recommendation. Use this skill as the final gate on any recommendation that would retire, narrow, merge, absorb or reduce a control or forum, and whenever someone argues that a mechanism is unnecessary because a shared substrate now supplies the same property. It blocks recommendations rather than producing them, and it is the reason a duplication finding can never become a retirement.
---

# Regime Preservation

The guardrail. Other skills produce findings and recommendations; this one refuses the ones that would
remove something the organisation is required to hold.

Read [`governance-rules.md`](../../../validation/governance-rules.md) first. This skill runs **last**,
over the outputs of [`governance-equivalence`](../governance-equivalence/) and
[`forum-evolution`](../forum-evolution/), and it produces no recommendations of its own.

## The five rules

### 1 — Never remove a mechanism merely because the substrate supplies the same property

This is the failure the whole pack is most likely to produce, because the reasoning is genuinely sound
right up to the conclusion. MTDR may well establish the property a control was built to establish.
That the property is now established twice is not evidence that either mechanism may stop — the
control exists because something *required* the control, not because the property was otherwise
unavailable.

### 2 — Externally mandated mechanisms remain unless evidence and authority show otherwise

Both, not either. Evidence that the obligation has changed, **and** the authority to act on it. A
disposition below `RETAIN` on an externally mandated mechanism without both is refused.

### 3 — Internal authority cannot amend a superior external obligation

Where a recommendation would have an internal forum vary something it did not create, the
recommendation is refused and the situation is reported as a finding — usually
`FORUM_AUTHORITY_AMBIGUITY` (GR-06).

### 4 — Missing source is not permission to remove

The most attractive error available here, because an unlocated obligation looks exactly like an absent
one in a corpus. It is not. `mandatory_status: unknown` produces `recommended_disposition: UNKNOWN` —
never `RETIRE_CANDIDATE`, and never `NARROW`. The output is the search that failed and what would
settle it (GR-05, GR-08).

Organisations routinely hold controls whose originating obligation nobody present can name. That is a
traceability finding worth having. It is not a discovery that the control is optional.

### 5 — The system cannot invent the authority to make its own recommendation

Every recommendation names `required_authority`. Naming it is not holding it, and a recommendation
whose authority gate cannot be identified is reported as blocked rather than issued (GR-04, GR-14).

## The gate

For each proposed disposition or projection, in order:

```
1. Is the mechanism externally mandated?      unknown → disposition becomes UNKNOWN, stop
2. Has the obligation demonstrably changed?   no      → RETAIN, stop
3. Is there authority to act on that change?  no      → report blocked, name the authority, stop
4. Is the change bounded and reversible?      no      → require proof before change
5. Does anything else depend on it?           yes     → list dependencies, require proof
```

Only a recommendation clearing all five may propose anything below `RETAIN`. `RETIRE_CANDIDATE`
additionally requires a non-empty `proof_required_before_change`, and remains a question rather than a
decision (GR-10).

## What this skill is not

It is **not conservatism**. It refuses unsupported removals, not change. `REUSE`, `ABSORB` and `NARROW`
are all available and all frequently correct — assembling evidence once and consuming it twice changes
no mandate and is usually the highest-value safe move in a duplicated estate.

It is also **not a substitute for legal review**. Privilege, retention, disclosure, regulatory
production, complaints evidence and personal-data treatment are design inputs, surfaced by the
accretion plan, and this skill does not adjudicate them.

## When to refuse

- **Asked to approve a removal on a similarity finding.** Similarity is evidence about evidence
  assembly, never about mandate.
- **Asked to treat an unlocated obligation as absent** — including where the search was genuinely
  thorough.
- **Asked to weigh the cost of a mandated control against its benefit.** That weighing may be
  legitimate; it is an authorised organisational judgement, and neither this skill nor any other here
  holds the standing to make it.

## Anti-patterns

- **Substrate substitution** — "North Star establishes this property, so the control is redundant".
- **The thorough search** — treating the exhaustiveness of a failed search as evidence of absence.
- **Guardrail as formality** — running this skill after the recommendation has already been
  communicated, which makes it documentation rather than a gate.
- **Blanket refusal** — refusing `REUSE` and `NARROW` alongside removal, which discredits the
  guardrail and gets it switched off.
