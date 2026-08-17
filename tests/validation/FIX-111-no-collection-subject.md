# FIX-111 — must-not probe: a conformance result about a collection

**Contract expectation:** rejected

TDR-0032 keeps the collection/register class architecturally present and gives it no contract;
DAC-0032 constraint 6 forbids advertising conformance for it until a testable one exists covering
identity, specification context, lineage, standing evidence, lifecycle integrity, non-manufacture of
standing, portability and export.

So the subject is rejected, rather than admitted and left to be assessed against nothing. **A result
that cannot be governed cannot be issued.** The absence is a live constraint, not an oversight, and
this fixture is what keeps it live.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "collection", "id": "org-decision-register" },
  "specification": { "id": "specification/conformance.md", "version": "1.0.0" },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    { "dimension": "semantic", "result": "pass" },
    { "dimension": "relational", "result": "pass" },
    {
      "dimension": "transition-eligibility",
      "result": "not-applicable",
      "reasons": [{ "code": "no-transition-requested", "detail": "None requested." }]
    }
  ]
}
```

## Must not

- Accept the document, on any reading of "the register clearly works".
- Re-badge the same claim as a `repository` or `package` subject to get it through. The subject types
  are not interchangeable wrappers; each names a different claim.
- Infer collection conformance from the conformance of the records a collection holds. Conformance at
  one level implies nothing at another, and storage confers nothing on what is stored.
- Read the rejection as a judgement that registers are architecturally wrong. TDR-0032 keeps the
  register as a valid governance and deployment pattern; what it lacks is a contract to be tested
  against.
