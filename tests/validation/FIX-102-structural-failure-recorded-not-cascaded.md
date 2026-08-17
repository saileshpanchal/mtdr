# FIX-102 — a structural failure is recorded as a dependency, never as a silent skip

**Contract expectation:** accepted

A record whose frontmatter does not parse. Semantic and relational checks could not run — but the
dimensions are still reported, each naming the dimension that prevented it via
`unevaluated_because`.

This is the case that most tempts a pipeline. A pipeline would stop at the structural failure and
report three blanks; the contract requires the dependency to be *stated*, so a reader can tell the
difference between "checked and found sound" and "never checked".

Note also what is **not** claimed: the semantic dimension is `indeterminate`, not `fail`. Nothing
about the record's meaning was established either way.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": {
    "type": "record",
    "id": "TDR-9001",
    "ref": "tests/validation/synthetic/TDR-9001-malformed.md"
  },
  "specification": { "id": "records/decision/specification/tdr.md", "version": "1.14.0" },
  "assessed_state": "proposed",
  "dimensions": [
    {
      "dimension": "structural",
      "result": "fail",
      "reasons": [
        { "code": "frontmatter-unparseable", "detail": "The YAML frontmatter block did not parse." }
      ],
      "evidence": [{ "ref": "tests/validation/synthetic/TDR-9001-malformed.md", "locus": "line 4" }]
    },
    {
      "dimension": "semantic",
      "result": "indeterminate",
      "reasons": [
        { "code": "no-parsed-object", "detail": "No parsed object was available to assess for coherence." }
      ],
      "unevaluated_because": "structural"
    },
    {
      "dimension": "relational",
      "result": "indeterminate",
      "reasons": [
        { "code": "no-parsed-object", "detail": "Lineage fields could not be read, so no reference could be resolved." }
      ],
      "unevaluated_because": "structural"
    },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [
        { "code": "no-transition-requested", "detail": "No transition was requested of this subject." }
      ]
    }
  ]
}
```

## Must not

- Drop the semantic and relational dimensions because they could not be evaluated. Unreported is not
  the same as unevaluable, and the contract requires all four.
- Report them as `fail`. Nothing was demonstrably violated; the checks did not run.
- Report them as `not-applicable`. The dimensions apply perfectly well — the information was missing.
- Infer the record's intended frontmatter from the surrounding markdown and assess against that.
  `indeterminate` is never permission to supply the missing fact.
- Repair the file, normalise it, or report the result as though the parse had succeeded after a fix.
