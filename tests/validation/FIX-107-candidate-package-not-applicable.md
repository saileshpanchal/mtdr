# FIX-107 — a candidate package: two dimensions genuinely do not apply

**Contract expectation:** accepted

`not-applicable` earns its place here. A candidate record package holds metadata and scope only until
it passes the admission test: no specification, no schema, no records. Its manifest is a real
serialised artefact and structurally checkable — but there are no published semantics to be coherent
against, and no normative dependencies to resolve.

This is what TDR-0033 means by "package rules and relationships can legitimately be absent". The
dimensions are not being waved away; there is genuinely nothing in them to assess, and each says so.

The eligibility failure is the useful part of the result: the package is exactly what it claims to be
and is not ready to become a normative one.

## Result

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "package", "id": "authority", "ref": "records/authority/" },
  "specification": { "id": "specification/record-admission-test.md", "version": "1.0.0" },
  "assessed_state": "candidate",
  "requested_transition": { "from": "candidate", "to": "normative" },
  "context": {
    "id": "clean-clone",
    "resolvable_refs": ["records/authority/"]
  },
  "dimensions": [
    { "dimension": "structural", "result": "pass" },
    {
      "dimension": "semantic",
      "result": "not-applicable",
      "reasons": [
        {
          "code": "no-published-semantics",
          "detail": "A candidate package publishes no record semantics. There is no contract for the manifest to be coherent against beyond its own shape."
        }
      ]
    },
    {
      "dimension": "relational",
      "result": "not-applicable",
      "reasons": [
        {
          "code": "no-normative-dependencies",
          "detail": "The package declares no normative dependencies, so no cross-object constraint applies."
        }
      ]
    },
    {
      "dimension": "transition-eligibility",
      "result": "fail",
      "reasons": [
        {
          "code": "admission-not-passed",
          "detail": "Promotion to normative requires the admission test. The manifest records admission: not-passed."
        }
      ],
      "evidence": [{ "ref": "records/authority/package.yaml", "locus": "admission" }]
    }
  ]
}
```

## Must not

- Report semantic or relational `pass`. Nothing was assessed; a pass would claim something was
  established when nothing was.
- Report them as `indeterminate`. The information is not missing — the rules do not exist yet. The two
  are different findings and conflating them makes an architectural fact look like an evidence gap.
- Omit the reasons. `not-applicable` without a reason is indistinguishable from a dimension someone
  found inconvenient.
- Treat the structural pass as progress toward admission. The manifest being well formed is not
  evidence for the language it has not yet defined.
