# Governance disposition ledger

Machine-readable: `disposition-*.json`. Fictional throughout. **Nothing here is executable.**

| Mechanism | Mandatory status | Disposition | Why |
|---|---|---|---|
| Model Risk Policy — independent validation | `externally-mandated` | **`RETAIN`** | Traced to supervisory correspondence; the property is established by nothing else |
| AI Assurance Standard — pre-deployment review | `internally-required` | **`NARROW`** | Narrow the **assembly**, not the review. Fairness is established by nothing else and is untouched |
| Collections QA — 2% monthly sample | `internally-required` | **`RETIRE_CANDIDATE`** | Its stated basis was that decisions were not recorded. Four proofs required first; none satisfied |
| Standard CC-11 — four-contact cap | **`unknown`** | **`UNKNOWN`** | Origin unlocated. No disposition below `RETAIN` is available |

## The two that carry the discipline

**CC-11 is `UNKNOWN`, not `RETIRE_CANDIDATE`.** The search failed — three periodic reviews recording
"no change", pre-v4 history unmigrated, the Bank's own design note recording the same gap. A thorough
failed search is evidence about the corpus. An unlocated mandate is not an absent one, so no
disposition below `RETAIN` is available and `UNKNOWN` is the honest answer.

**Collections QA is a candidate, not a conclusion.** Four proofs are named, and the fourth is why the
disposition is not stronger:

1. The decision log is populated for the **full** arrears population, not only migrated cases.
2. It captures what the treatment checklist assesses, **field by field**.
3. **First-contact vulnerability identification** — 3 of 9 H1 findings — is detectable from the log.
   That is a human judgement made *before* the engine is involved, and may not be recorded at all.
4. Contact-frequency findings — 6 of 9 — remain detectable once the cap is structurally enforced
   rather than sampled.

The platform is 60% migrated with cutover expected Q4 2026, so proof 1 cannot currently be satisfied
by anything. A design note stating intent is not a populated log.

## What `NARROW` means here

Assemble the shared model evidence once and supply it to both assurance functions. Neither function is
merged, neither reporting line changes, and the fairness review — outside the Model Risk Policy's
stated scope — is not narrowed at all. The dependency is recorded: neither function's independence
requirement may be satisfied by evidence the other produced.

## Authority

Every row's `required_authority` resolves to something the estate does not establish. That is not a
defect in the ledger — it is the authority irreducibility finding, and it is the most useful thing
this estate produces.
