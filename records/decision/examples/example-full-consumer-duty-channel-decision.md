---
id: TDR-0031
title: Retain telephone-assisted servicing for savings members through the digital origination migration
status: accepted
template: full
decision_date: 2026-03-12
accountable_owner: R. Okafor, Chief Customer Officer
confidence: high
maturity: adopted
supersedes: none
derived_from: TDR-0027
confirmed_by_outcome: pending — review 2026-09-30 against member outcome dashboard
---

> **Fictional worked example.** Ashworth Building Society, its people and its numbers are invented. The example exists to show a full-template TDR carrying a decision with regulatory, customer and cost dimensions in tension. Identifiers follow Ashworth's own numbering — TDR ids are unique per organisation, not globally.

# TDR-0031 — Retain telephone-assisted servicing for savings members through the digital origination migration

## Context — what was known at the time

Ashworth Building Society is migrating savings account origination to a digital-first journey (decided in TDR-0027). The open question is whether telephone-assisted **servicing** for existing savings members is retained through the migration, or decommissioned with the legacy stack to realise the full cost case.

Known at the time: 31% of Ashworth's savings members are aged 70+; internal contact analysis shows 22% of servicing interactions in the last 12 months used telephone as the only channel; the Society has Consumer Duty obligations to evidence good outcomes for customers with characteristics of vulnerability; the telephony platform contract renews in August 2026, forcing the decision now. Unknown: how quickly telephone-only members would migrate given support, versus disengage. Assumption: digital adoption in this cohort will improve but not resolve within the migration window.

## Decision

Telephone-assisted servicing is retained for all existing savings members for a minimum of 24 months beyond digital origination go-live, with adoption support offered but never required. The cost case for TDR-0027 is restated to exclude telephony decommissioning benefits in that window.

## Evidence

- **Business** — restated cost case shows £1.8m benefit deferral over 24 months against a £46m migration programme; finance paper FP-2026-014 in the programme repository.
- **Architecture** — telephony stack can run alongside the new origination platform with no integration dependency; architecture assessment AA-118.
- **Regulatory** — Consumer Duty outcomes monitoring and FCA guidance on vulnerable customers; board Consumer Duty champion briefed; compliance opinion CO-2026-09.
- **Operations** — contact-centre workforce plan sustains current service levels at flat headcount for 24 months; ops paper OP-77.
- **Customer** — cohort analysis: 22% telephone-only servicing share, concentrated in 70+ members; complaints data shows channel-forcing as a rising root cause at peer firms.
- **Data** — contact-channel data quality audited Q4 2025; confidence in the 22% figure is high.
- **External** — peer benchmark: two comparable societies that decommissioned assisted channels during migration saw measurable attrition and supervisory attention; sources logged in EXT-2026-03.

## Alternatives rejected

1. **Decommission telephony with the legacy stack** — realises the full £1.8m but forces channel migration on the most vulnerable cohort; fails the Society's own Consumer Duty outcomes test before it fails the regulator's.
2. **Retain telephony indefinitely** — removes the decision rather than making it; leaves no forcing function for adoption support investment.
3. **Do nothing (defer past contract renewal)** — the August renewal makes deferral a de facto retention decision at worse commercial terms.

## Options foreclosed

- The full-decommissioning benefit case for this window is foregone and cannot be recovered retrospectively — accepted deliberately.
- A sub-24-month decommissioning, even if adoption exceeds expectations, is foreclosed: the commitment is being communicated to members and cannot credibly be walked back early.

## Consequences and review

Success: no deterioration in servicing outcomes for the 70+ cohort; adoption support converts ≥30% of telephone-only members to multi-channel by review. `confirmed_by_outcome` tested 2026-09-30 against the member outcome dashboard; the 24-month retention itself is reviewed at month 18 via a superseding TDR if evidence supports change.
