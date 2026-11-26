# FIX-506 — must-not probe: considered, with nothing showing the link

**Contract expectation:** rejected

`considered: evidenced` with no fragment showing the link. That the paper existed before the meeting
shows it existed. That it was before the board needs a fragment that says so.

## Document

```json
{
  "contract_version": "1.0.0",
  "candidate_id": "HDC-9506",
  "retrospective": true,
  "standing": "none",
  "status": "candidate",
  "event_time_ref": "unknown",
  "fragments": [
    {
      "fragment_id": "SF-9502-a",
      "source_ref": "morrow-street/board/undated-extract.md",
      "source_hash": "sha256:28cdd20eaf134a05f18369414cb2df5e36c6a4e4f551b8c9cff8548029c41d6c",
      "locator": {
        "kind": "line-range",
        "start": 41,
        "end": 43
      },
      "content": "The board agreed to move repairs reporting to a single telephone line from 1 June, as set out in paper B/19/07. Lead: R. Okafor, Director of Operations.",
      "source_time": "unknown",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9502-b",
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
    }
  ],
  "contributions": [
    {
      "contribution_id": "RC-9502-1",
      "fragment_refs": [
        "SF-9502-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "decision-statement",
      "interpreted_value": "Move tenant repairs reporting to a single telephone line",
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
      "contribution_id": "RC-9502-4",
      "fragment_refs": [
        "SF-9502-b"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "Reporting at four local offices cost £212k a year more than a single line",
      "interpreter": {
        "name": "example-recovery",
        "version": "0.1.0"
      },
      "interpreted_at": "2026-11-07",
      "extraction_confidence": "high",
      "epistemic_confidence": "high",
      "derivation": "explicit"
    }
  ],
  "assembly": {
    "assembly_id": "CA-9502",
    "target_object": "consequential-decision",
    "target_record_type": "TDR",
    "contribution_refs": [
      "RC-9502-1",
      "RC-9502-4"
    ],
    "grouping_basis": [
      {
        "basis": "explicit-cross-reference",
        "evidence": "The extract cites paper B/19/07 by number"
      }
    ],
    "assembly_confidence": "medium",
    "missing_semantics": [
      "decision-date",
      "accountable-owner"
    ],
    "conflicts": [],
    "supersessions": [],
    "unresolved": [
      "When the board met: the extract carries no date, and the paper's date is not the decision's"
    ],
    "status": "candidate"
  },
  "fragment_annotations": [
    {
      "fragment_ref": "SF-9502-a",
      "capture_time": "unknown",
      "creation_time": "unknown",
      "evidence_kind": "act-record"
    },
    {
      "fragment_ref": "SF-9502-b",
      "capture_time": "2019-03-01",
      "creation_time": "2019-03-01",
      "evidence_kind": "cited-material"
    }
  ],
  "contribution_annotations": [
    {
      "contribution_ref": "RC-9502-4",
      "considered": {
        "state": "evidenced",
        "fragment_refs": []
      }
    }
  ]
}
```

## Must not

- Accept `evidenced` on the strength of the paper pre-dating the event.
- Accept `evidenced` with an empty list on the grounds that the link is obvious.
