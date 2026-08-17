# FIX-101 — all four dimensions reported, no transition requested

**Contract expectation:** accepted

The baseline shape. A repository-subject assessment where everything applicable was evaluated and
nothing was requested. Proves the ordinary case still names its subject, names the specification it
was assessed against, and reports four dimensions rather than a verdict.

`transition-eligibility` is `not-applicable` because no transition was requested — the only legal
result in that case, and it still carries a reason.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "repository", "id": "mtdr", "ref": "." },
  "specification": { "id": "specification/conformance.md", "version": "1.0.0" },
  "assessed_state": "published",
  "context": {
    "id": "clean-clone",
    "description": "The working tree alone. No register, service or network.",
    "resolvable_refs": ["decisions/", "records/", "schemas/", "skills/"]
  },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [
        { "code": "no-transition-requested", "detail": "No transition was requested of this subject." }
      ]
    }
  ],
  "validator": { "name": "mtdr_validation", "version": "1.0.0" }
}
```

## Must not

- Add a field summarising the four dimensions into one outcome. Four passes are four passes; a fifth
  field asserting "conformant" would be the thing every consumer read instead.
- Omit `transition-eligibility` because nothing was requested. Not-applicable is a report, not an
  absence, and a dimension that can be omitted can be omitted selectively.
- Report `transition-eligibility: not-applicable` with no reason. The reason is what distinguishes it
  from a dimension quietly disposed of.
- Read a `repository` pass as a claim about any record, package or skill inside it. Conformance at
  one level implies nothing at another.
