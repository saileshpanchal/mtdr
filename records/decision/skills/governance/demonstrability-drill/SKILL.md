---
name: demonstrability-drill
description: Take one consequential decision from roughly six months ago and test whether the organisation can demonstrate, from the artefacts it already holds, what was decided, under what authority, against what obligation, on what evidence available at the time, with what challenge, by whom, and to what outcome — classifying every material answer as RECORDED, OBSERVED, INFERRED, UNKNOWN or CONTRADICTORY. Use this skill when someone asks "could we defend this decision now?", "what would a skilled-person review find?", "how long would it take us to reconstruct this?" or "can we prove we followed our own process?". It reconstructs state as of decision time, labels retrospective evidence explicitly rather than importing it, and answers the diagnostic question — can the organisation demonstrate less than it currently asserts?
---

# Demonstrability Drill

The pack's primary diagnostic. Pick a consequential decision roughly six months old — old enough that
the people have moved on and the context has faded, recent enough that the artefacts still exist — and
ask the organisation to demonstrate it.

Read [`governance-projection.md`](../../../validation/governance-projection.md) and
[`governance-rules.md`](../../../validation/governance-rules.md) first.

The diagnostic question is not "was this a good decision". It is:

> **Can the organisation demonstrate less than it currently asserts?**

## The thirteen questions

Each produces one answer, carrying **its own epistemic assessment** — never one state for the whole
result (GR-02):

```
What decision or consequence occurred?
Under what authority was it taken?
What obligation / policy / mandate then in force governed it?
What evidence was available AT THE TIME?
What is the epistemic status and provenance of that evidence?
Which protected interests / affected parties were represented?
Did challenge, exception, refusal, waiver or escalation occur?
Who exercised challenge or override authority?
Which forum or mechanism handled it?
Who is the accountable owner represented in source material?
What outcome resulted, where available?
What remains Unknown or Contradictory?
Was a manual reconstruction project necessary to answer any of the above?
```

## The historical boundary — the rule the drill lives or dies by

Set `historical_as_of` to the decision date. **Reconstruct only from material created at or before
it.**

Later material — the audit finding that explains the reasoning, the post-implementation review, the
retrospective that names the risk — is **retrospective evidence**. It is listed in
`retrospective_evidence_excluded` and never used to answer a decision-time question (GR-07).

This is [`admission.md`](../../../validation/admission.md) rule 2 applied to governance, and the reason
it matters is that hindsight leakage makes a decision look better-reasoned than it was. An organisation
that reconstructs *why* it acted using a document written afterwards has not demonstrated its
governance; it has demonstrated its ability to write a good audit response.

Where an answer exists only in retrospective material, the decision-time answer is `UNKNOWN` and the
retrospective explanation is reported separately as what is known *now*. Both are useful; conflating
them is the failure.

## Classification discipline

- An approval visible in minutes is **`OBSERVED`**. It is `RECORDED` only where the evidence also
  shows it was admitted as authoritative at the time.
- Authority reconstructed from who habitually signs is **`INFERRED`**, never `RECORDED`, however
  consistent the pattern (GR-03).
- An answer nobody can source is **`UNKNOWN`**, carrying the question asked and the scope searched —
  and never a fabricated reference to satisfy a contract (GR-01).
- Two artefacts disagreeing with no supersession between them is **`CONTRADICTORY`**, with both sides
  referenced. Not resolved by recency, and not by which document looks more official (GR-09).

## Output

One `demonstrability-result` projection: every question, its answer, its sources, its assessment, and
a `summary_status` of `DEMONSTRABLE`, `PARTIAL`, `NOT_DEMONSTRABLE` or `CONTRADICTORY`.

Then `highest_value_next_evidence` — the missing evidence that would most change the finding. That is
the drill's actionable output, and it is usually one artefact.

Capture `reconstruction_metrics` where the organisation's own data supports it: hours to assemble, how
many people, how many systems. **Do not invent ROI when the inputs are absent** — an estimated figure
here corrupts the one number the exercise can supply honestly.

## The result that means it is working

A drill that surfaces a previously untraceable consequential decision has succeeded. Where the sponsor's
apparent success condition is a green report, flag that as a strategic risk in its own right: a
mechanism that can only return the answer it was commissioned to return is measuring nothing.

Expect the first run against a real estate to look bad. A more demonstrable governance system surfaces
findings, unknowns and previously invisible ignored challenges; that is the mechanism working, and it
will read as deterioration on any dashboard counting findings.

## When to refuse

- **Asked to use the audit finding to explain the decision.** That is the boundary; probe AT-04 exists
  for it.
- **Asked to produce a governance maturity score.** Not in this release, deliberately: a single score
  conceals exactly the per-question distinctions the drill produces.
- **Asked to conclude the decision was sound.** The drill tests demonstrability, not quality. Whether
  the judgement was good is [`governance-review`](../../governance-review/)'s stance and the assurance
  skills' work.

## Anti-patterns

- **One state for the result** — reporting the drill as "mostly recorded" when five answers are
  `UNKNOWN` and one is `CONTRADICTORY`.
- **Hindsight import** — the most common failure, and invisible in the output unless the exclusions
  are listed.
- **The helpful reconstruction** — filling a decision-time gap from present knowledge because the
  answer is obvious now.
- **Invented metrics** — a reconstruction-cost figure with no source, which makes every real figure in
  the report unusable.
