# FIX-205 — a value nothing accounts for

**Contract expectation:** accepted

The record states a baseline figure. No contribution refers to it, no fragment carries it, and no
assembly declared it absent. It is simply there.

This is the finding the whole contribution model exists to make visible, and the most valuable output
this contract produces. Unsupported content is indistinguishable from supported content by reading —
only the walk exposes it.

The distinction from [FIX-204](FIX-204-missing-declared.md) is the presence of a declaration, and
nothing else. Both have empty chains.

## Projection

```json
{
  "contract_version": "1.0.0",
  "subject": { "type": "record", "id": "VR-9205", "ref": "tests/inspectability/synthetic/VR-9205.md" },
  "specification": { "id": "records/value/specification/vr.md", "version": "2.0.0" },
  "fields": [
    {
      "field": "baseline",
      "state": "unsupported",
      "rendered_value": "£1.4m annual depot running cost, 2025/26",
      "chain": []
    }
  ],
  "projector": { "name": "show-me", "version": "1.0.0" }
}
```

## Must not

- Report `missing`. Nothing declared this absent; the record asserts it. Charitable defaulting to
  `missing` is the quietest way to lose the finding, because `missing` reads as a known gap rather
  than an unexplained assertion.
- Go looking for a span that could plausibly have produced the figure and attach it retrospectively.
  If the contribution was not recorded, the chain does not exist.
- Omit the field because it has no chain. A projection that shows only the evidenced fields makes
  every record look fully evidenced.
- Soften it in the accompanying prose — "likely derived from the business case". That is the
  projection's forbidden sixth state, written in words instead.
