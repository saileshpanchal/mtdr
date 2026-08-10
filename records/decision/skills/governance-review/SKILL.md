---
name: governance-review
description: Review a Transformation Decision Record (TDR) from the stance of an external reviewer — a board member, auditor, or supervisor — to test whether it answers the accountability question. Use this skill before a TDR is accepted, whenever someone asks "would this satisfy an audit", "could we defend this decision", "does this demonstrate reasonable steps", or when reviewing a body of TDRs for lineage integrity and proportionality.
---

# Governance Review

This skill reviews a TDR as the least sympathetic competent reader would: someone with authority, no context, and a specific question. Read `spec.md` §§4–8 first.

## The stance

Do not review as the author's colleague. Review as the person who will one day ask: *show me the judgement that was exercised here.* Every test below is a version of that question.

## Tests

### 1. The accountability test

Is `accountable_owner` a named individual? Could that individual, using **this record alone**, demonstrate that reasonable judgement was exercised with the information available at the time? (In UK financial services this is the SM&CR "reasonable steps" shape; every regulated and governed organisation has its equivalent.) If the answer requires documents the record does not cite, the record fails as evidence — however good the decision was.

### 2. The time-capsule test

Could a stranger reconstruct the judgement — the context, the pressure, the trade-offs — without interviewing anyone? Look for hindsight leakage: outcome knowledge written into the Context section, alternatives described with suspicious neatness, risks that only became visible later presented as foreseen.

### 3. The foreclosure honesty test

Does **Options foreclosed** name real foreclosures, or is it decorative? Cross-examine against the Decision: most significant decisions close something off. An empty foreclosure section on a full-template TDR is usually an unasked question, not an absence of consequence.

### 4. The lineage integrity test

- Do all `supersedes` and `derived_from` references resolve to real records?
- Is every superseded record's `status` marked `superseded`, its content untouched?
- Are there content edits where a superseding record should exist? Judgement is never revised in place — that is the difference between memory and documentation.
- Are `confirmed_by_outcome` entries past their review trigger still `pending`? Overdue confirmations are silent debt.

### 5. The proportionality test

Does the template tier match the reversibility of the decision? Flag both failure modes: a bare record for a one-way door (under-recorded judgement) and a full record for a trivially reversible choice (box-ticking that erodes the instrument).

## Outcome

Record one of:

- **Pass** — the record answers the accountability question as asked.
- **Pass with notes** — accepted, with named gaps for the next review.
- **Return** — specific tests failed; the record goes back with the failures listed. Return the record, not the decision: the decision may be sound and merely under-evidenced.

## Anti-patterns

- **Sympathetic review** — assessing what the author meant rather than what the record says.
- **Quality theatre** — passing records because the prose is polished; polish is not evidence.
- **Re-litigating the decision** — the review tests the record, not whether the reviewer would have decided differently. Disagreement with an accepted decision is expressed as a proposed superseding TDR, not a failed review.
