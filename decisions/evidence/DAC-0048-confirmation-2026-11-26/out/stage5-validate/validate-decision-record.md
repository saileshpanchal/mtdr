# Stage 5 — validate-record, then validate-decision-record (the skill, run by the agent)

Run on 2026-11-26. This is the skill's procedure carried out by the agent. The reference validator's output is separate, in `validation/`.

| # | Check | Kind | Result | Version / note |
|---|---|---|---|---|
| shared 1 | Frontmatter of the four views parses under a strict YAML parser | structural | pass | parsed by the reference validator's YAML load; four keys, no unquoted colon |
| shared 2 | Resolve package manifest (`records/decision/package.yaml`) | structural | indeterminate | the manifest is not in the installed package; candidates are not records and bind to `historical-candidate.md` 1.0.0 |
| shared 3–8 | Conditional requirements, id/filename, lineage ids, status transitions, review dates, `x-` namespace | — | not applicable | no TDR was produced |
| 1 | Candidate views are not TDRs: header shows `candidate_id`, `status: candidate`, `standing: none`, `retrospective: true` | structural | pass ×4 | not validated against the TDR schema |
| 2a | Candidate schema (`historical-candidate.schema.json`, `schemas/shared/` as registry) | schema | pass ×4 | by the reference validator (structural: pass) |
| 2b | Integrity rules: references resolve; each fragment annotated once; `considered` on every context contribution and no other; `event_time_ref` names a `decision-date` contribution; no finding class as a contribution; no authority on unlinked or retrospective material | structural | pass ×4 | build script asserts fragment and context coverage; `HC-003-C05` rests on act-record and cited-material fragments |
| 3 | Contemporaneity recomputed | structural | HC-001: 11 contemporaneous · HC-002: 7 contemporaneous · HC-003: 3 contemporaneous · HC-004: 5 indeterminate, 1 contemporaneous | agent's own implementation of rules 1–6; agrees with the reference validator's summary |
| 4 | Never-inferred roles | structural | pass ×4 | every `accountable-owner`, `authority`, `alternative-rejected` contribution is `explicit`; the four `inferred` contributions are `HC-001-C16` and `HC-004-C11` (consequence), `HC-004-C02` (decision-date) and `HC-003-C14` (lineage) |
| 5 | Classifications against the vocabulary | schema | pass, 38 of 38 | `decision-contribution.schema.json`; see `agent-schema-checks.txt`. The four `unclassified` outcomes carry no classification object |
| 6 | Review events | — | not applicable | none produced |
| 7 | Recovered TDR opens with its recovery | — | not applicable | no recovered TDR; nothing was attested |
| 8 | Contribution coverage of the views | structural | pass ×4 | views are generated from the contributions; each line names its contribution and fragments. Headings, gap statements and the completeness table are the agent's and are not contributions |

Unsupported-claim list: none found in the views' rendered values. The completeness grades and the one-sentence readings are the agent's judgement and trace to no contribution.

Conformance is not correctness. None of this says the account is true.
