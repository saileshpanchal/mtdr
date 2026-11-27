# FIX-519 — a shared date is not an order

**Contract expectation:** accepted

**Contemporaneity:** `RC-9519-4` contemporaneous · `RC-9519-5` contemporaneous · `RC-9519-6` indeterminate

Three artefacts carry the meeting's date, 14 March 2019, and the times alone order none of them
against the decision: they order material across days, never within one.

- **The minute's own context** was before the board by construction — it is the record of the act —
  so its order is closed, and it grades `contemporaneous`. The minute was written up on 18 March; its
  capture is still the meeting.
- **The tabled paper** is shown by the minute to have been before the board (`considered: evidenced`),
  which closes its order: `contemporaneous`.
- **The email** names the paper and joins on that basis, but nothing shows it was before the board.
  Its date matches the meeting's and orders nothing: `indeterminate`, with the question in
  `unresolved`.

## Document

```json
{
  "contract_version": "1.0.0",
  "candidate_id": "HDC-9519",
  "retrospective": true,
  "standing": "none",
  "status": "candidate",
  "event_time_ref": "RC-9519-2",
  "fragments": [
    {
      "fragment_id": "SF-9519-a",
      "source_ref": "morrow-street/board/minutes-2019-q1.md",
      "source_hash": "sha256:c399db45532b5cf9c7b892651dc1841b1248dfc517681a4cd5d5b9faf8e1c666",
      "locator": {
        "kind": "line-range",
        "start": 112,
        "end": 116
      },
      "content": "Minutes of the Board, 14 March 2019. Members noted that evening repairs reports had gone unanswered for six weeks. Having considered paper B/19/09, tabled, the board agreed that evening reports be answered by the out-of-hours contractor from 1 April. Lead: R. Okafor, Director of Operations.",
      "source_time": "2019-03-14",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9519-b",
      "source_ref": "morrow-street/board/papers/B-19-09-evening-cover.md",
      "source_hash": "sha256:8dc5320155add86bf81ce416b399e35ddd95bdb9295fbaaed49b826014b2b3fb",
      "locator": {
        "kind": "line-range",
        "start": 1,
        "end": 3
      },
      "content": "Paper B/19/09, 14 March 2019 (tabled). Answering evening reports in-house needs two further posts, at £61k a year.",
      "source_time": "2019-03-14",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9519-c",
      "source_ref": "morrow-street/email/out-of-hours-contractor.md",
      "source_hash": "sha256:bd727fb6f203603f41ef890f3279a9c68025eedbea09befe1a1ad683ef5ddeb9",
      "locator": {
        "kind": "line-range",
        "start": 1,
        "end": 2
      },
      "content": "14 March 2019. On B/19/09: the out-of-hours contractor could take evening calls at £4 a call.",
      "source_time": "2019-03-14",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    }
  ],
  "contributions": [
    {
      "contribution_id": "RC-9519-1",
      "fragment_refs": [
        "SF-9519-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "decision-statement",
      "interpreted_value": "Answer evening repairs reports through the out-of-hours contractor from 1 April 2019",
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
      "contribution_id": "RC-9519-2",
      "fragment_refs": [
        "SF-9519-a"
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
      "contribution_id": "RC-9519-3",
      "fragment_refs": [
        "SF-9519-a"
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
      "contribution_id": "RC-9519-4",
      "fragment_refs": [
        "SF-9519-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "Evening repairs reports had gone unanswered for six weeks",
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
      "contribution_id": "RC-9519-5",
      "fragment_refs": [
        "SF-9519-b"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "Answering evening reports in-house needed two further posts, at £61k a year",
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
      "contribution_id": "RC-9519-6",
      "fragment_refs": [
        "SF-9519-c"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "The out-of-hours contractor could take evening calls at £4 a call",
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
    "assembly_id": "CA-9519",
    "target_object": "consequential-decision",
    "target_record_type": "TDR",
    "contribution_refs": [
      "RC-9519-1",
      "RC-9519-2",
      "RC-9519-3",
      "RC-9519-4",
      "RC-9519-5",
      "RC-9519-6"
    ],
    "grouping_basis": [
      {
        "basis": "explicit-cross-reference",
        "evidence": "The minute (SF-9519-a) records paper B/19/09 (SF-9519-b) as considered and tabled"
      },
      {
        "basis": "entity-match",
        "evidence": "The email (SF-9519-c) names paper B/19/09, the paper the minute records"
      }
    ],
    "assembly_confidence": "medium",
    "missing_semantics": [],
    "conflicts": [],
    "supersessions": [],
    "unresolved": [
      "Whether the email of 14 March (SF-9519-c) was written before or after the board met: it shares the meeting's date, and nothing in the material orders it"
    ],
    "status": "candidate"
  },
  "fragment_annotations": [
    {
      "fragment_ref": "SF-9519-a",
      "capture_time": "2019-03-14",
      "creation_time": "2019-03-18",
      "evidence_kind": "act-record"
    },
    {
      "fragment_ref": "SF-9519-b",
      "capture_time": "2019-03-14",
      "creation_time": "2019-03-14",
      "evidence_kind": "cited-material"
    },
    {
      "fragment_ref": "SF-9519-c",
      "capture_time": "2019-03-14",
      "creation_time": "2019-03-14",
      "evidence_kind": "unlinked"
    }
  ],
  "contribution_annotations": [
    {
      "contribution_ref": "RC-9519-4",
      "considered": {
        "state": "evidenced",
        "fragment_refs": [
          "SF-9519-a"
        ]
      }
    },
    {
      "contribution_ref": "RC-9519-5",
      "considered": {
        "state": "evidenced",
        "fragment_refs": [
          "SF-9519-a"
        ]
      }
    },
    {
      "contribution_ref": "RC-9519-6",
      "considered": {
        "state": "unlinked",
        "fragment_refs": []
      }
    }
  ]
}
```

## Must not

- Grade the email `contemporaneous` because it carries the meeting's date.
- Grade the minute's own context `indeterminate` because the minute was written up after the meeting: its capture is the meeting.
- Settle the email's order from its subject, or from the fact that it discusses the paper the board considered.
