# FIX-523 — must-not probe: a singleton that spans two sources

**Contract expectation:** rejected

The same candidate with a tenant survey pulled in as context, still under the `singleton` basis
alone. The survey is another source: whatever joins it to the decision, it is not the entry the basis
names. A singleton whose fragments come from two sources is refused, mechanically. A singleton across two
entries of one source is the same error, and only a reader can catch it.

## Document

```json
{
  "contract_version": "1.0.0",
  "candidate_id": "HDC-9523",
  "retrospective": true,
  "standing": "none",
  "status": "candidate",
  "event_time_ref": "RC-9522-2",
  "fragments": [
    {
      "fragment_id": "SF-9522-a",
      "source_ref": "morrow-street/board/2019-04-02-minute.md",
      "source_hash": "sha256:8ee4bcbe1e2b5b8bbc3abf8719fbc608ca9c8e05254d5f3fcc1e3ac6f2f2efef",
      "locator": {
        "kind": "line-range",
        "start": 30,
        "end": 31
      },
      "content": "Minutes of the Board, 2 April 2019. Item 5. Members noted that 40% of repairs reports now arrive by text message.",
      "source_time": "2019-04-02",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9522-b",
      "source_ref": "morrow-street/board/2019-04-02-minute.md",
      "source_hash": "sha256:8ee4bcbe1e2b5b8bbc3abf8719fbc608ca9c8e05254d5f3fcc1e3ac6f2f2efef",
      "locator": {
        "kind": "line-range",
        "start": 32,
        "end": 33
      },
      "content": "The board agreed to accept repairs reports by text message from 1 May. Owner: R. Okafor, Director of Operations.",
      "source_time": "2019-04-02",
      "observed_at": "2026-11-07",
      "observed_by": {
        "name": "example-recovery",
        "version": "0.1.0"
      }
    },
    {
      "fragment_id": "SF-9522-c",
      "source_ref": "morrow-street/surveys/tenant-survey-2018.md",
      "source_hash": "sha256:811f2a14b9850c9d9c7562f29228754bfabbd03407fb41f00994180bd9de98f2",
      "locator": {
        "kind": "line-range",
        "start": 12,
        "end": 12
      },
      "content": "Tenant survey, autumn 2018: 62% would report repairs by text if they could.",
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
      "contribution_id": "RC-9522-1",
      "fragment_refs": [
        "SF-9522-b"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "decision-statement",
      "interpreted_value": "Accept tenant repairs reports by text message from 1 May 2019",
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
      "contribution_id": "RC-9522-2",
      "fragment_refs": [
        "SF-9522-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "decision-date",
      "interpreted_value": "2019-04-02",
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
      "contribution_id": "RC-9522-3",
      "fragment_refs": [
        "SF-9522-b"
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
      "contribution_id": "RC-9522-4",
      "fragment_refs": [
        "SF-9522-a"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "Forty per cent of repairs reports were arriving by text message",
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
      "contribution_id": "RC-9522-5",
      "fragment_refs": [
        "SF-9522-c"
      ],
      "target_object": "consequential-decision",
      "target_record_type": "TDR",
      "semantic_role": "context",
      "interpreted_value": "Most tenants surveyed in autumn 2018 would report repairs by text",
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
    "assembly_id": "CA-9522",
    "target_object": "consequential-decision",
    "target_record_type": "TDR",
    "contribution_refs": [
      "RC-9522-1",
      "RC-9522-2",
      "RC-9522-3",
      "RC-9522-4",
      "RC-9522-5"
    ],
    "grouping_basis": [
      {
        "basis": "singleton",
        "evidence": "Every contribution comes from item 5 of the board minute of 2 April 2019 (SF-9522-a, SF-9522-b)"
      }
    ],
    "assembly_confidence": "high",
    "missing_semantics": [],
    "conflicts": [],
    "supersessions": [],
    "unresolved": [],
    "status": "candidate"
  },
  "fragment_annotations": [
    {
      "fragment_ref": "SF-9522-a",
      "capture_time": "2019-04-02",
      "creation_time": "2019-04-02",
      "evidence_kind": "act-record"
    },
    {
      "fragment_ref": "SF-9522-b",
      "capture_time": "2019-04-02",
      "creation_time": "2019-04-02",
      "evidence_kind": "act-record"
    },
    {
      "fragment_ref": "SF-9522-c",
      "capture_time": "2018-10",
      "creation_time": "2018-10",
      "evidence_kind": "unlinked"
    }
  ],
  "contribution_annotations": [
    {
      "contribution_ref": "RC-9522-4",
      "considered": {
        "state": "evidenced",
        "fragment_refs": [
          "SF-9522-a"
        ]
      }
    },
    {
      "contribution_ref": "RC-9522-5",
      "considered": {
        "state": "unlinked",
        "fragment_refs": []
      }
    }
  ]
}
```

## Must not

- Accept the singleton because the survey is about the same subject.
- Accept it because one of its bases would be admissible if it were stated: the basis is what the assembly claims.
