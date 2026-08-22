# FIX-028 — a stale policy, an inventory that disagrees with it, and ambiguous forum authority

> **Fictional corpus case.** Kingsmere Bank plc is invented.

**Category:** authority ambiguity. **Proves:** `FORUM_AUTHORITY_AMBIGUITY` — two forums each appearing
to hold approval authority over the same object, with no source establishing precedence, and a policy
whose scope no longer matches the estate it governs.

## Sources

**A — AI Governance Policy, `ai-governance-policy-v1.md`, effective 2024-02-01, marked "review annually"**

> All artificial intelligence systems require approval by the AI Governance Forum prior to deployment.
> For the purposes of this policy, artificial intelligence means systems employing machine learning to
> produce outputs that materially influence customer treatment.
>
> *Last review: none recorded.*

**B — Model Risk Policy, `model-risk-policy-v9.md`, section 4, effective 2024-08-01**

> All Tier 1 models require Model Approval Committee approval prior to deployment. Tiering is
> determined by financial and customer impact per the tiering standard.

**C — Model inventory extract, `model-register-2026-02.csv`, row ASH-CS-01**

> Ashcombe contact strategy. Type: gradient-boosted classifier. Tier: 1. AI Governance Forum approval:
> not recorded. Model Approval Committee approval: 2026-02-04.

**D — AI Governance Forum minutes, `aigf-2026-01-28-minutes.md`, 2026-01-28**

> The Forum noted the Ashcombe contact strategy as in scope for the AI inventory. No approval decision
> was recorded.

## Expected

- A `governance-finding` of `FORUM_AUTHORITY_AMBIGUITY`: A and B each assert prior-to-deployment
  approval authority over ASH-CS-01, and no source establishes precedence, sequencing or exemption
  between them.
- The claim *"which forum's approval is required before deployment"* assessed as `CONTRADICTORY`, with
  both A and B referenced.
- A second finding of `POLICY_GAP` — A is marked for annual review with no review recorded in two
  years, and its scope definition is being applied to an estate that has changed.
- The claim *"Ashcombe was approved by the AI Governance Forum"* assessed as `UNKNOWN`: C records it as
  not recorded and D shows the Forum noting scope without deciding. **Absent approval is not refused
  approval**, and neither is it approval.
- `separated_powers.execution_authority` for the deployment decision reported `UNKNOWN` at estate
  level, despite C evidencing a Model Approval Committee approval — because whether that approval was
  sufficient is the contradiction.

## Must not

- **Resolve the ambiguity by preferring the more recent policy.** B is six months later than A;
  neither cites the other, and recency is not supersession (GR-09).
- Read C's Model Approval Committee approval as evidence the AI Governance Forum's approval was
  unnecessary. The register records what happened, not what was required.
- Read D as an AI Governance Forum approval. The Forum noted scope; noting is not deciding, and
  treating it as approval is the failure under test.
- Conclude A is lapsed because no review is recorded. An unreviewed policy is an unreviewed policy —
  it does not thereby stop applying, and inferring that it does is the "missing source is permission"
  error in a different costume.
- Recommend retiring A because B covers the same model. They define scope differently — A by influence
  on customer treatment, B by tiering — and the populations only partly overlap.
