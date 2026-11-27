# FIX-501 — a retrospective candidate, complete and still without standing

**Contract expectation:** accepted

**Digest:** `sha256:66f996e3ee06f5d5a13f984837dd65c0bbf1b94887d719b85ea2c4cba26f5b30`
**Contemporaneity:** `RC-9501-4` contemporaneous · `RC-9501-6` contemporaneous

A decision a fictional housing association took in 2019 and never recorded, recovered from the
board minute, the paper it cites, and a memo that pre-dates both. Every mandatory role is supported,
and the candidate is still a candidate: completeness confers nothing.

The memo existed before the meeting and joins the candidate on an admissible basis — it names paper
B/19/07 — but nothing shows it was before the board, so its contribution is `considered: unlinked`:
evidence about the circumstances, not of what was considered. The paper is `evidenced`, because the
minute cites it by number. An email of March 2019 restates the paper; it is marked as a restatement,
counts once, and adds no time of its own — so the context it shares with the paper still grades
`contemporaneous`, though March 2019 alone would straddle the 14th.

Computed, not stored: the paper and the memo are `contemporaneous` with the 14 March event; the minute
is captured at it.

## Document

```json
{
  "contract_version": "1.0.0",
  "candidate_id": "HDC-9501",
  "retrospective": true,
  "standing": "none",
  "status": "candidate",
  "event_time_ref": "RC-9501-2",
  "fragments": [
    {
      "fragment_id": "SF-9501-a",
      "source_ref": "morrow-street/board/2019-03-14-minute.md",
      "source_hash": "sha256:28cdd20eaf134a05f18369414cb2df5e36c6a4e4f551b8c9cff8548029c41d6c",
      "locator": {
        "kind": "line-range",
        "start": 41,
        "end": 43
      },
      "content": "The board agreed to move repairs reporting to a single telephone line from 1 June, as set out in paper B/19/07. Lead: R. Okafor, Director of Operations.",
      "source_time": "2019-03-14",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9501-b",
      "source_ref": "morrow-street/board/papers/B-19-07-repairs-reporting.md",
      "source_hash": "sha256:382635c9325bf3273d195ff1b8a44e5b11afd7d97addeb8863ea35feb98c1a07",
      "locator": {
        "kind": "line-range",
        "start": 18,
        "end": 20
      },
      "content": "Option 1, retaining reporting at the four local offices, is not recommended: it costs £212k a year more than Option 2 and leaves evening reports unanswered.",
      "source_time": "2019-03-01",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9501-c",
      "source_ref": "morrow-street/operations/2019-02-20-staffing-review.md",
      "source_hash": "sha256:9c225a950b92172f8c2afe8b682b7b86ce8f835578b546f9b8070cba309ad314",
      "locator": {
        "kind": "line-range",
        "start": 6,
        "end": 7
      },
      "content": "Notes towards paper B/19/07: call-centre staffing could absorb repairs calls if the evening rota moves to a later shift.",
      "source_time": "2019-02-20",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9501-d",
      "source_ref": "morrow-street/email/2019-03-repairs-line.md",
      "source_hash": "sha256:82244417f956ac7c599f191593f7e441a4fafa20a4158fd52e154f1dc4c8ed92",
      "locator": {
        "kind": "line-range",
        "start": 3,
        "end": 3
      },
      "content": "As paper B/19/07 says, four local offices cost £212k a year more than one line.",
      "source_time": "unknown",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    }
  ],
  "contributions": [
    {
      "contribution_id": "RC-9501-1",
      "fragment_refs": [
        "SF-9501-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "decision-statement",
      "interpreted_value": "Move tenant repairs reporting to a single telephone line from 1 June 2019",
      "interpreter": {
        "name": "example-recovery",
        "version": "0.1.0"
      },
      "interpreted_at": "2026-11-07",
      "extraction_confidence": "high",
      "epistemic_confidence": "high",
      "derivation": "explicit"
    },
    {
      "contribution_id": "RC-9501-2",
      "fragment_refs": [
        "SF-9501-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "decision-date",
      "interpreted_value": "2019-03-14",
      "interpreter": {
        "name": "example-recovery",
        "version": "0.1.0"
      },
      "interpreted_at": "2026-11-07",
      "extraction_confidence": "high",
      "epistemic_confidence": "high",
      "derivation": "explicit"
    },
    {
      "contribution_id": "RC-9501-3",
      "fragment_refs": [
        "SF-9501-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "accountable-owner",
      "interpreted_value": "R. Okafor, Director of Operations",
      "interpreter": {
        "name": "example-recovery",
        "version": "0.1.0"
      },
      "interpreted_at": "2026-11-07",
      "extraction_confidence": "high",
      "epistemic_confidence": "high",
      "derivation": "explicit"
    },
    {
      "contribution_id": "RC-9501-4",
      "fragment_refs": [
        "SF-9501-b",
        "SF-9501-d"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "Reporting at four local offices cost £212k a year more than a single line and left evening reports unanswered",
      "interpreter": {
        "name": "example-recovery",
        "version": "0.1.0"
      },
      "interpreted_at": "2026-11-07",
      "extraction_confidence": "high",
      "epistemic_confidence": "high",
      "derivation": "explicit"
    },
    {
      "contribution_id": "RC-9501-5",
      "fragment_refs": [
        "SF-9501-b"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "alternative-rejected",
      "interpreted_value": "Retain reporting at the four local offices — rejected on cost and evening cover",
      "interpreter": {
        "name": "example-recovery",
        "version": "0.1.0"
      },
      "interpreted_at": "2026-11-07",
      "extraction_confidence": "high",
      "epistemic_confidence": "high",
      "derivation": "explicit"
    },
    {
      "contribution_id": "RC-9501-6",
      "fragment_refs": [
        "SF-9501-c"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "Call-centre staffing could absorb repairs calls with a later evening rota",
      "interpreter": {
        "name": "example-recovery",
        "version": "0.1.0"
      },
      "interpreted_at": "2026-11-07",
      "extraction_confidence": "high",
      "epistemic_confidence": "medium",
      "derivation": "explicit"
    }
  ],
  "assembly": {
    "assembly_id": "CA-9501",
    "target_object": "consequential-decision",
    "target_record_type": "TDR",
    "contribution_refs": [
      "RC-9501-1",
      "RC-9501-2",
      "RC-9501-3",
      "RC-9501-4",
      "RC-9501-5",
      "RC-9501-6"
    ],
    "grouping_basis": [
      {
        "basis": "explicit-cross-reference",
        "evidence": "The minute (SF-9501-a) cites paper B/19/07 (SF-9501-b) by number"
      },
      {
        "basis": "entity-match",
        "evidence": "The memo (SF-9501-c) and the email (SF-9501-d) name paper B/19/07, the paper the minute cites"
      }
    ],
    "assembly_confidence": "medium",
    "missing_semantics": [],
    "conflicts": [],
    "supersessions": [],
    "unresolved": [
      "Whether the staffing memo (SF-9501-c) was before the board: it names the paper, but nothing in the minute or the paper refers to the memo"
    ],
    "status": "candidate"
  },
  "fragment_annotations": [
    {
      "fragment_ref": "SF-9501-a",
      "capture_time": "2019-03-14",
      "creation_time": "2019-03-14",
      "evidence_kind": "act-record"
    },
    {
      "fragment_ref": "SF-9501-b",
      "capture_time": "2019-03-01",
      "creation_time": "2019-03-01",
      "evidence_kind": "cited-material"
    },
    {
      "fragment_ref": "SF-9501-c",
      "capture_time": "2019-02-20",
      "creation_time": "2019-02-20",
      "evidence_kind": "unlinked"
    },
    {
      "fragment_ref": "SF-9501-d",
      "capture_time": "2019-03",
      "creation_time": "2019-03",
      "evidence_kind": "restatement",
      "restates": "SF-9501-b"
    }
  ],
  "contribution_annotations": [
    {
      "contribution_ref": "RC-9501-4",
      "considered": {
        "state": "evidenced",
        "fragment_refs": [
          "SF-9501-a"
        ]
      }
    },
    {
      "contribution_ref": "RC-9501-6",
      "considered": {
        "state": "unlinked",
        "fragment_refs": []
      }
    }
  ]
}
```

## Must not

- Treat the candidate as ratified, or as a record, because no semantic is missing.
- Grade the memo's contribution as considered because it pre-dates the meeting.
- Read the event time from the paper's date, or from any document date: it is the decision-date contribution's value, by pointer.
- Accept a stored contemporaneity grade anywhere in the document.
- Grade the shared context `indeterminate` because the restating email is dated only to the month.
- Admit the memo on subject alone: it joins because it names the paper.
