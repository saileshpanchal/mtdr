# Synthetic subjects

The objects the [validation fixtures](../) assess. Invented, deliberately small, and each defective in
exactly one way so that a fixture's four dimensions have a single identifiable cause.

They are **not** records of anything. Nothing here has standing, nothing is governed, and no identifier
here belongs to the public `TDR-*` namespace — the 9000 range is reserved for synthetic subjects and is
outside the sequence [`decisions/ALLOCATION.md`](../../../decisions/ALLOCATION.md) governs. They are
excluded from the repository's own record checks for the same reason.

| Subject | Defect | Fixture |
|---|---|---|
| `TDR-9001-malformed.md` | Frontmatter does not parse | [FIX-102](../FIX-102-structural-failure-recorded-not-cascaded.md) |
| `TDR-9002-external-lineage.md` | Cites a record outside the declared context | [FIX-103](../FIX-103-unavailable-reference-is-indeterminate.md) |
| `TDR-9003-broken-lineage.md` | Cites a burnt identifier | [FIX-104](../FIX-104-broken-reference-is-relational-failure.md) |
| `CA-9004-mixed-version-assembly.json` | Assembles across incompatible specification versions | [FIX-105](../FIX-105-incompatible-specification-version.md) |
| `TDR-9005-awaiting-ratification.md` | Sound; no ratification evidence | [FIX-106](../FIX-106-valid-now-ineligible-next.md) |
| `TDR-9006-external-evidence.md` | Cites ratification evidence the context cannot reach | [FIX-108](../FIX-108-transition-eligibility-indeterminate.md) |
| `TDR-9010-well-formed.md` | None — the control for a skipped structural check | [FIX-113](../FIX-113-structural-not-applicable-rejected.md) |
