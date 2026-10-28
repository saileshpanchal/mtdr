---
id: OIR-0001
conforms_to: mtdr/work/oir@1.0.0
experimental: true
title: Resolution of payment-processing exceptions
status: in-force
effective_from: 2026-03-02
accountable_owner: Priya Raman
jobs:
  - job: Resolve payment-processing exceptions before they cause avoidable customer harm
    established_by: TDR-0141
  - job: Return payments that cannot be applied within the scheme's return window
    established_by: unknown
clauses:
  purpose:           {source: reference, refs: [VR-0022]}
  inherited_context: {source: asserted}
  jobs:              {source: asserted}
  outcomes:          {source: reference, refs: [VR-0022]}
  responsibilities:  {source: asserted}
  authority:         {source: reference, refs: [DEL-PAY-2025-04]}
  obligations:       {source: reference, refs: [POL-PAYMENTS-7, SCHEME-RULEBOOK-2025]}
  practices:         {source: asserted}
  escalation:        {source: conflicting, refs: [DEL-PAY-2025-04, RUNBOOK-EXC-v6]}
  evidence:          {source: missing}
supersedes: none
derived_from: TDR-0141
---

# OIR-0001 — Resolution of payment-processing exceptions

> **Fictional worked example.** Hollin Vale Building Society, its people, records and decisions are
> invented. **Experimental** — published for review under TDR-0047; not part of the MTDR standard.

## Purpose — *reference: VR-0022*

The society's committed outcome for members whose payments fail in processing. Not restated here.

## You inherit — *asserted*

- **Commitments in force:** inbound payments are applied the same business day; members are told of
  any payment the society cannot apply.
- **Dependencies:** the core ledger's overnight batch; the scheme connection's return window.
- **Shared assumptions:** an exception raised after 15:00 is worked the next business day — assumed by
  operations and by member services, written down by neither until this record.
- **Accepted risk:** the manual repair step is single-operator below £2,500; accepted by TDR-0141
  with dual control above it.
- **What experience has shown:** the largest recurring cause of exceptions is a mismatched
  beneficiary account name after a member changes their surname; three of the last four complaints
  arose from exceptions held over a bank holiday.
- **The society's own thresholds:** an exception is **severe** when it affects a vulnerable member
  or a payment of £10,000 or more; **material** when more than 50 members are affected in a day.

*Provenance:* operations hand-over notes, Feb 2026; complaints review, Jan 2026; TDR-0141.

## Jobs to be done — *asserted*

1. Resolve payment-processing exceptions before they cause avoidable customer harm. *Established by
   TDR-0141.*
2. Return payments that cannot be applied within the scheme's return window. *Established by:
   unknown — the job is performed, but no record of the decision that made it this capability's is
   held.*

## Outcomes — *reference: VR-0022*

## You are responsible for — *asserted*

Member outcomes for every payment in exception · keeping this record's inherited context current ·
escalating material issues.

## You may — *reference: DEL-PAY-2025-04*

The delegation in force. **This record grants nothing.**

## You must — *reference: POL-PAYMENTS-7, SCHEME-RULEBOOK-2025*

## You should — *asserted*

Work severe exceptions first, then by value. Check the member's recent name changes before repairing
an account-name mismatch.

## Escalate when — *conflicting*

The delegation sets escalation at **£10,000**; run book v6 still says **£25,000**. The conflict is
preserved, not resolved: which threshold binds is a question for the delegation's owner.

## Evidence — *missing*

The society has not established what the resolution of an exception must leave behind. Declared, not
filled.
