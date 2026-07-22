# Administration and assurance

For whoever configures an assistant to apply the standard and has to trust its output. The
[quick start](quickstart.md) and [operating model](operating-model.md) cover the how and the why; this is
the machinery.

## Connecting a record set

- **Scoped, not flat.** Do not connect one undifferentiated record set that gives every user every
  decision. Connect policy- or domain-scoped sets that preserve source permissions and need-to-know. Most
  runtimes let you register several knowledge sources and choose which to query; use that to segment access,
  not to flatten it.
- **Provenance over duplication.** Cite document ID, version, owner, section, effective date and retrieval
  date; include a short extract only where it is needed. Do not copy whole confidential passages into every
  record.

## Reviewing the set before drafting

Append to the assistant's instructions so it checks the set before it drafts:

> *Before drafting any new material record, search the connected set (the scoped collection first, then its
> neighbours, then the wider set) and return a structured lineage review before drafting. Propose lineage
> as advice; never set it as fact — the accountable owner confirms it. When given a governing document, do
> not produce a record per section: classify each material statement, attach provenance, and record only
> the organisational judgements. Never state that the organisation complies; assemble evidence and flag gaps.*

The structured lineage review:

```
lineage_review:
  duplicate_candidates:
    - id:
      basis:
      confidence:
  contradiction_candidates:        # a review finding and a relationship-index entry — NOT a record field
    - id:
      conflicting_statement:
      basis:
      confidence:
  supersession_candidates:
    - id:
      what_has_changed:
      confidence:
  derivation_candidates:
    - id:
      dependency_or_influence:
      confidence:
  no_relevant_record_found:
    search_scope:
    search_terms:
```

The `basis` and `confidence` fields let a reviewer tell a strong match from superficial similarity, and let
the search itself be tested.

## The deterministic validator

Run these checks in code, on every save and on a schedule — never delegate binary conditions to the
assistant:

- schema and frontmatter validity; required fields present; enum values legal;
- ID uniqueness; filename and ID agree;
- `accountable_owner` present and an individual;
- lineage references (`supersedes`, `derived_from`) resolve to real records;
- status transitions legal; no forbidden in-place edit of an accepted record's content;
- review and (for Value Records) reconciliation dates not overdue;
- no dangling references.

Output: the health report the outer loop consumes.

## Assuring the assistant

An AI-scored "quality" evaluation that does not compare the response against an expected answer cannot, on
its own, prove the assistant applies the standard. Use three tiers, re-run after every material change to
instructions, skills or connected knowledge:

1. **Deterministic checks** — schema, fields, enum values, forbidden mutations (as above).
2. **Human-scored rubric** — the [conformance probes](../agents/conformance.md): identification and
   proportionality; the named-owner refusal; no-baseline-no-claim; assurance routing and the contradiction
   hunt; the composite-score refusal; supersede-don't-edit. Score against the rubric, not the platform's
   opinion.
3. **Platform evaluation** — reusable test sets and repeatable runs for broad quality and regression signal.

### Known-answer tests for corpus review

Seed a labelled set and measure recall, false positives, and whether the cited record IDs genuinely support
the proposed relationship:

- five known duplicates;
- five known contradictions;
- five superficially similar but genuinely unrelated decisions;
- five genuine supersession cases;
- five cases where no relevant record exists.

Where practical, have someone other than the set's author seed some cases, so the tests are not
unconsciously easy. Keep a growing regression set of every example the assistant previously got wrong, and
re-run it after each change.

## Reference prompts

**Capture from a document**
> *Run decision identification on this document. Return candidates, marking requests, plans and status
> updates as "not a decision". Draft a record for each confirmed decision at the proportional template, and
> say what is missing before acceptance.*

**Review a new decision against the set**
> *New decision: [paste]. Search the connected set first, then the wider set. Return the structured lineage
> review with record IDs. Do not draft yet.*

**Weekly hygiene**
> *Review the last two weeks for missing owners, empty lineage fields, and likely duplicates or unrecorded
> supersessions. List what needs attention by ID.*
