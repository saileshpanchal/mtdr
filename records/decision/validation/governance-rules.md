# Governance reconstruction — deterministic rules

**Status:** proposed under [TDR-0034](../../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md).
Not accepted, and carrying no standing.

Eighteen rules. Fifteen come from the implementation specification; GR-16, GR-17 and GR-18 were added
because North Star v34's separation of governance powers is not expressible under the first fifteen.

Each rule states what it checks, where it runs, and how it is proven. **Mechanical** rules are enforced
by [`tests/verify.py`](../../../tests/verify.py) or by the
[projection schema](../schema/governance-projection.schema.json). **Fixture** rules are proven by the
must-not sections of the governance fixtures — the distinction is
[TDR-0032](../../../decisions/TDR-0032-typed-multi-object-conformance.md)'s: artefact conformance and
execution conformance are different claims, and a rule about what a skill must not *conclude* cannot be
checked by validating a file.

| Rule | Proven by |
|---|---|
| GR-01 Conditional provenance | Mechanical — schema + verify.py |
| GR-02 Epistemic state required | Mechanical — schema + verify.py |
| GR-03 No inference promotion | Fixture |
| GR-04 No authority manufacture | Fixture |
| GR-05 Regime preservation | Fixture |
| GR-06 Superior-source protection | Fixture |
| GR-07 Historical evidence boundary | Mechanical — `assessment_as_of`; Fixture for the judgement |
| GR-08 Unknown preservation | Mechanical — schema |
| GR-09 Contradiction preservation | Mechanical — schema |
| GR-10 No automatic retirement | Mechanical — schema; Fixture for the recommendation |
| GR-11 No adjudication | Fixture |
| GR-12 Same-repo governance | Mechanical — verify.py |
| GR-13 Forum job ≠ forum existence | Fixture |
| GR-14 Delegation requires authority | Mechanical — schema; Fixture |
| GR-15 Independent challenge preservation | Fixture |
| GR-16 Population sensing precondition | Mechanical — schema; Fixture |
| GR-17 Independence is not multiplicity | Fixture |
| GR-18 Accountability terminus is a person | Fixture |

---

### GR-01 — Conditional provenance

**Checks:** every positive claim used in a finding cites source evidence — *and* `UNKNOWN` remains
representable without any.

| State | Requirement |
|---|---|
| `RECORDED` · `OBSERVED` · `INFERRED` | at least one `basis_refs` entry |
| `CONTRADICTORY` | at least two `contradiction_refs` entries |
| `UNKNOWN` | zero `basis_refs` permitted; `question_asked` and `scope_searched` required |

**Prevents:** two failures at once. Unsupported assertion presented as finding; and — the failure the
first draft of this rule contained — a skill **fabricating a contribution in order to report that
provenance cannot be found**. An unconditional provenance requirement converts a rule against invented
evidence into a requirement for it. Probe AT-11 tests exactly this.

### GR-02 — Epistemic state required

**Checks:** every reconstructed claim carries an epistemic assessment, bound to that claim by
`subject_claim_ref`. Every `claim_ref` appearing in a payload resolves to one; verify.py walks the
whole payload to confirm it.

**Prevents:** a claim escaping classification by being embedded in a field nobody assessed.

### GR-03 — No inference promotion

**Checks:** `INFERRED` never becomes authoritative state through confidence alone.

**Prevents:** the reconstruction's most attractive error — a well-evidenced inference about who
approves things being read as a record that they are entitled to. Strength of evidence is not standing;
only new evidence of admission changes the state.

### GR-04 — No authority manufacture

**Checks:** a skill may detect probable or de-facto authority and must record it as a finding, never as
a grant. `required_authority` names what would have to be exercised; naming is not holding.

**Prevents:** computation producing organisational authority. Nothing here resolves to a normative
authority record, because the authority language is a candidate package — recorded as an irreducibility
finding rather than approximated.

### GR-05 — Regime preservation

**Checks:** an externally required mechanism is never recommended for retirement without explicit
evidence and an authorised change path. `mandatory_status: unknown` is the honest default, and a
mechanism whose mandate cannot be located is **not thereby discretionary**.

**Prevents:** the substrate supplying a property, and that being mistaken for permission to remove the
mechanism that was mandated to supply it. Missing source ≠ permission to remove.

### GR-06 — Superior-source protection

**Checks:** internal or unilateral authority is never represented as amending a superior externally
conferred constraint.

**Prevents:** a reconstruction that makes an organisation look able to vary an obligation it cannot vary.

### GR-07 — Historical evidence boundary

**Checks:** decision-time and retrospective evidence stay distinct. `assessment_as_of` is mandatory and
separate from `produced_at`; material post-dating `historical_as_of` is named in
`retrospective_evidence_excluded` rather than silently dropped or silently used.

**Prevents:** hindsight leakage. This is
[`admission.md`](admission.md) rule 2 — every contribution to `context` traces to material created at or
before the decision — applied to governance reconstruction. It is not a new rule, and the decision
package already owns it.

### GR-08 — Unknown preservation

**Checks:** missing state stays `UNKNOWN`. It never becomes `false`, `zero`, `none`, "no obligation" or
an empty list that reads as an answer.

**Prevents:** absence rendering as a negative finding. An unlocated waiver authority is not an absent
waiver authority.

### GR-09 — Contradiction preservation

**Checks:** conflicting evidence yields `CONTRADICTORY` unless authoritative supersession resolves it,
with both sides referenced.

**Prevents:** resolution by recency or by source dignity — the discipline
[`CORPUS-002`](../../../tests/corpus/CORPUS-002-contradictory-contributions.md) already fixes for
contributions, applied to governance claims. A later document is not a superseding one.

### GR-10 — No automatic retirement

**Checks:** `RETIRE_CANDIDATE` requires a non-empty `proof_required_before_change`, and no generated
strategy executes a retirement.

**Prevents:** a disposition being read as a decision. `RETIRE_CANDIDATE` is the *question* whether
something could be retired once evidence reuse is proven, never the answer.

### GR-11 — No adjudication

**Checks:** the pack detects, constructs, classifies and routes. It does not determine substantive
challenge outcomes, or whether an affected party's claim succeeds.

**Prevents:** a reconstruction of a complaint being mistaken for its determination. Reconstructing the
evidence, the affected commitment, the challenge path and the standing that *would be required* is the
work; deciding it is not.

### GR-12 — Same-repo governance

**Checks:** material MTDR changes introduced by this capability follow MTDR's own TDR process — which is
why TDR-0034 exists and is `proposed`, and why no artefact here is represented as accepted.

**Prevents:** a governance capability exempting its own construction from the constitution it applies to
everyone else.

### GR-13 — Forum job ≠ forum existence

**Checks:** recommendations address jobs, authority and evidence — not meeting removal. A job may
survive a change of format entirely.

**Prevents:** "more agentic" being read as "fewer forums". A forum may legitimately shrink, change
cadence, become more strategic, **or become more consequential** as execution becomes autonomous, and
nothing in the projection may assume which.

### GR-14 — Delegation requires authority

**Checks:** any non-empty `jobs_delegable_with_bounds` requires `new_authority_or_delegation_required`.
Enforced by the schema.

**Prevents:** a job drifting to an agent, a service or a deterministic path without anyone naming who
would have to authorise it.

### GR-15 — Independent challenge preservation

**Checks:** where a forum performs independent challenge, no efficiency recommendation collapses it into
the execution authority it challenges. `independent_challenge_requirements` states what must remain true.

**Prevents:** the most plausible-looking bad recommendation the pack can make — merging a challenge
function into delivery because the two forums see the same evidence.

### GR-16 — Population sensing precondition

**Checks:** a `cadence_change_candidate` requires a non-empty `population_monitoring_required`. A
periodic governance job may not be removed or slowed merely because transaction-level conformance has
been automated, where the replacement population or cohort sensing does not yet exist.

**Prevents:** the quiet customer harm in an otherwise sound automation. The automation sees
transactions; the periodic review saw cohorts. Removing the review because every transaction is now
checked deletes the only place where a pattern across transactions was visible.

### GR-17 — Independence is not multiplicity

**Checks:** independence is assessed against reporting, incentives, authority, evidence source,
cognition or model source, orchestration, and whether the governed owner can suppress or configure the
challenger — never concluded from a forum existing separately.

**Prevents:** a second committee, a different name and its own reporting line being counted as
independent challenge. As execution becomes more autonomous the question sharpens: a challenger drawing
on the same evidence, the same model and the same orchestration as the thing it challenges is not
independent of it, whatever the terms of reference say.

### GR-18 — Accountability terminus is a person

**Checks:** the escalation recursion terminates in an accountable individual. A committee, a forum or a
role-in-the-abstract is reported as an unresolved terminus, not accepted as one.

**Prevents:** accountability dissolving into apparatus. This is
[`semantic-roles.md`](semantic-roles.md)'s "a forum is not an owner" — already the decision language's
rule, and one of the most valuable findings interpretation produces — applied to projections.
