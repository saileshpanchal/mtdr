---
id: TDR-0007
title: Add a decision-identification skill in front of the capture skill
status: accepted
template: bare
decision_date: 2026-07-06
accountable_owner: Sailesh Panchal
supersedes: none
derived_from: TDR-0003
---

# TDR-0007 — Add a decision-identification skill in front of the capture skill

**Decision:** Ship a fourth skill, **Decision Identification**, that recognises when
a conversation, document or incident contains a decision worth recording, routes it
through the proportionality test, and hands off to the existing three skills via a
tool-neutral TDR Candidate Envelope. Identification stays tool-neutral: it searches
"whatever store of TDRs the organisation keeps"; graph-assisted resolution of lineage,
policy links or impact is downstream implementation and stays outside this standard
(per TDR-0002).

**Why:** The existing skills assume you already know a decision is being made. The
front of the funnel — noticing the decision moment at all, and saying "no record
needed" with a reason — was undocumented practice.

**Reversible:** Yes — remove the skill directory and supersede this record; nothing
in the spec, schema or templates depends on it. Cheap to reverse, hence the bare
template.
