# Synthetic subjects

The records the [inspectability fixtures](../) project. Invented, small, and each carrying exactly one
interesting derivation state so a fixture's finding has a single identifiable cause.

Nothing here has standing, nothing is governed, and the `VR-92xx` range is reserved for synthetic
subjects — outside any sequence [`decisions/ALLOCATION.md`](../../../decisions/ALLOCATION.md) governs.
They are excluded from the repository's own record checks, and `linked_decisions: TDR-9200` names a
synthetic decision that likewise does not exist.

The material is deliberately local-government rather than financial services. Every other fictional
case in this repository is a bank, and a claim made repeatedly — that this is an organisational
language and not a banking ontology — is better demonstrated than asserted.

> **`VR-9204` was not schema-valid when these fixtures were written**, and now is. It is a candidate
> with no finance counter-signatory — which the VR specification §4.4 has always permitted in that
> state and the schema forbade globally. [TDR-0039](../../../decisions/TDR-0039-state-relative-requirements.md)
> corrected that at 1.29. The subject is unchanged; what changed is that the schema can now express
> the state its own specification describes.
>
> `VR-9205`'s defect is not a schema matter at all: its unaccounted-for figure is in the body, where
> no schema reaches. That is the point of the projection — the walk finds what validation cannot.

| Subject | State it carries | Fixture |
|---|---|---|
| `VR-9201.md` | A value read directly from its span | [FIX-201](../FIX-201-supported.md) |
| `VR-9202.md` | A chain with one inferred link | [FIX-202](../FIX-202-inferred.md) |
| `VR-9203.md` | Two sources disagreeing on one role | [FIX-203](../FIX-203-conflicting.md) |
| `VR-9204.md` | A declared gap | [FIX-204](../FIX-204-missing-declared.md) |
| `VR-9205.md` | A figure nothing accounts for | [FIX-205](../FIX-205-unsupported-undeclared.md) |
