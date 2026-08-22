---
name: forum-reconstruct
description: Reconstruct what a governance forum actually does from its terms of reference, agendas, packs, minutes, decision logs and outputs — the jobs it really performs rather than its stated purpose, the seven governance powers it exercises separately, and whether its challenge function is genuinely independent. Use this skill on a Technology Design Authority, architecture review board, risk or risk-acceptance committee, model approval or AI governance forum, CAB, Consumer Duty or complaints forum, data governance council, security forum, investment or transformation steering group, or any executive or board subcommittee where consequential decisions are taken. It classifies work into ten job classes, leaves what the evidence cannot support as UNKNOWN, and never concludes that a forum is independent merely because it exists separately.
---

# Forum Reconstruct

A forum's terms of reference say what it is for. Its packs and minutes show what it does. This skill
reconstructs the second, and reports the distance between them as a finding rather than an error.

Read [`governance-projection.md`](../../../validation/governance-projection.md) and
[`governance-rules.md`](../../../validation/governance-rules.md) first.

**The unit of analysis is not the meeting.** It is the governance job the forum performs. A job can
survive the meeting disappearing; a meeting can survive long after its job has moved.

## The twelve questions

Asked of every forum, and answered from evidence or left `UNKNOWN`:

```
Why does it exist?
What obligations / risks / protected interests does it serve?
What decisions does it make?
What authority does it exercise?
What evidence does it consume?
What evidence does it create?
What challenge does it provide?
What is escalated to it?
What does it escalate onward?
What could be decided without the meeting today?
What must remain independent / human / accountable?
What is merely evidence assembly or status reporting?
```

## Job classes

Every observed piece of the forum's work lands in exactly one, with its own claim and epistemic
assessment:

```
EVIDENCE_ASSEMBLY          STATUS_REPORTING         DETERMINISTIC_CONFORMANCE
EXCEPTION_HANDLING         TRADE_OFF_JUDGEMENT      INDEPENDENT_CHALLENGE
AUTHORITY_EXERCISE         AMENDMENT                ESCALATION
ACCOUNTABILITY_ROUTING     UNKNOWN
```

`ACCOUNTABILITY_ROUTING`, not "accountability": the job a forum performs is **routing accountability
to a person**. A forum is never accountable itself, and recording it as such is how accountability
dissolves into apparatus (GR-18).

Where the evidence does not support classification, the class is `UNKNOWN`. A near-fit is the failure
under test.

## The seven powers, reconstructed separately

A forum's authority is not one thing, and compressing it into "the forum approves X" loses the
distinctions that decide whether anything can safely change:

```
execution authority                    who may act
suspension / containment authority     who may stop it
challenge authority                    who may question it
veto / waiver / override authority     who may overrule or excuse
amendment authority                    who may change the governing requirement
escalation route                       where it goes next
accountability terminus                which named individual answers for it
```

Each carries its own claim and assessment. **An unresolved power stays `UNKNOWN`** — never the
adjacent holder, never the forum, never the most senior name in the room. The `accountability_terminus`
resolves to a named individual or is reported unresolved; a committee is not a terminus, exactly as
[`semantic-roles.md`](../../../validation/semantic-roles.md) already holds for records.

## Independence is not multiplicity

That a separate committee exists, with a different name and its own reporting line, establishes
nothing about independence. Assess seven dimensions before concluding (GR-17):

| Dimension | The question |
|---|---|
| Reporting | does the challenger report through the challenged? |
| Incentives | is the challenger measured on the challenged's outcomes? |
| Authority | can the challenger's finding survive the challenged's disagreement? |
| Evidence source | does the challenger see anything the challenged did not prepare? |
| Cognition / model source | is the challenger reasoning from the same models and assumptions? |
| Orchestration | who sets the agenda, the timing and what reaches the table? |
| Suppression / configuration | can the governed owner switch off, reconfigure or scope the challenger? |

Conclude `independent`, `partially-independent`, `not-independent` or `unknown`. As execution becomes
more autonomous this sharpens rather than softens: a challenger drawing on the same evidence, the same
model and the same orchestration as the thing it challenges is not independent of it, whatever its
terms of reference say.

## Output

One `forum-reconstruction` projection per forum, with an assessment per job and per power. Also report
`manual_reconstruction_steps` — the work people do *before* the meeting to rebuild context that the
organisation already held somewhere. That figure is the strongest evidence the estate produces about
what reconstruction currently costs.

## When to refuse

- **Asked whether the forum should exist.** Not this skill's question, and not answerable from a
  reconstruction (GR-13). The `forum-evolution` skill proposes a bounded next change; neither skill
  proposes abolition.
- **Asked to name the accountable owner** where the material names only a committee. Report the
  terminus as unresolved: that gap is one of the most valuable findings this skill produces.
- **Asked to conclude independence** from the org chart.

## Anti-patterns

- **Reading the terms of reference as the answer.** Stated purpose is a `RECORDED` claim about what
  the forum is *for*, and evidence of nothing about what it *does*.
- **Collapsing the powers** — recording "the forum has authority" and losing which of the seven.
- **The confident org chart** — inferring challenge authority from seniority, or a terminus from a
  reporting line.
- **Counting agenda items as jobs.** An agenda is what was scheduled; the minutes show what happened,
  and the gap between them is often the finding.
