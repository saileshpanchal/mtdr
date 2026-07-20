# Decision Assurance Case (DAC) — Specification

**Version:** 1.6.0 · **Licence:** MIT · **Author:** Sailesh Panchal

The TDR has a second sibling record. Where the **TDR** records organisational judgement and the
**VR** records the value case, the **Decision Assurance Case (DAC)** records the organisational
reasoning that challenges that judgement's consequences.

> A TDR preserves the judgement. It does not prove the consequences are acceptable.

They are different artefacts with different lifecycles: a TDR is immutable judgement, superseded
when the judgement changes; a DAC is a *challenge* to that judgement, re-run when the world
changes. The distinction matters more, not less, as AI systems begin to draft decisions: the
faster judgement can be produced, the more the discipline lives in how it is tested.

## 1. What a DAC is not

A Decision Assurance Case does not prove that a decision is correct. It proves that the
organisation has **systematically challenged** the decision, documented its assumptions,
identified foreseeable consequences, declared its uncertainty, and defined the evidence that will
determine whether the decision remains appropriate over time. It is a disciplined reasoning
process, not a guarantee of correctness or compliance — and it must never be presented as one.

## 2. The four questions

Every DAC answers four questions about the decision it tests:

1. **How could this decision be exploited?**
2. **Which customers could be harmed, even if it works exactly as designed?**
3. **Could the controls themselves create poor outcomes?**
4. **What evidence would tell us that our assumptions were wrong?**

The third question is the one existing practice misses. Protective controls — authentication,
blocking, limits, additional verification — are product decisions too: they may reduce losses
while creating exclusion, distress, delay or inaccessible journeys. Protection and customer
outcomes cannot be separate assurance exercises, because the tension between them is where the
foreseeable harm lives.

## 3. The compiler model — skills, case, authorisation

Three layers, deliberately separated:

```
Decision (TDR)          — the judgement, recorded
      ↓
Reasoning skills        — reusable challenges, run against the decision (see /skills)
      ↓
Decision Assurance Case — the compiled result of those challenges: one record, one disposition
      ↓
Authorisation           — consumes the disposition before the decision becomes executable
      ↓
Operation               — runtime evidence flows back against the DAC's monitoring contract
```

The skills are reusable; the DAC is what they compile into. This is a compiler model, not a
checklist model: the same skills run against any decision, and the case they produce is specific,
falsifiable and owned. Skill outputs are **advisory evidence** contributing to the case, never
verdicts — the synthesis produces the one disposition, and its named owner signs it. A decision's
record may be accepted while its assurance case says **stop** — the record captures judgement; the
case governs execution.

## 4. When to write a DAC — proportionality and routing

Proportionality governs assurance exactly as it governs recording (TDR spec §3):

| Decision | Assurance |
|---|---|
| One-way door (full template) | **DAC required** before execution |
| Significant, revisable (minimal) | DAC required **when routed** (below) |
| Reversible, low-stakes (bare) | **No DAC.** A bare decision never needs an assurance case |

Routing: for any decision requiring a DAC, three skills always run — **systems-thinking**,
**counterfactual-and-evidence**, **accumulated-and-resultant-risk**. The others are routed by what
the decision declares: adversarial thinking when the decision changes the economics or mechanics
an adversary could exploit (money movement, identity, consent, authority, delegation, data);
customer-outcomes when any customer, member or cohort is affected — and always when the
adversarial pass proposed controls, because controls are product decisions too (§2, question 3);
systems-dynamics when behaviour under growth or stress matters; adaptive-capacity when the
decision constrains future learning or reversal, or execution capability (§5.2 item 5) is in
doubt. **assurance-synthesis** always closes. This paragraph is the normative routing rule; the
skills apply it, they do not extend it.

**Materiality, not category.** The trigger lists above are illustrative, not auto-firing: a lens
is routed by whether the decision *materially* changes what that lens governs, not by whether a
keyword is present. A decision that touches customer data or authority yet changes no economics an
adversary could exploit — an internal-correctness change, a data-at-rest consolidation, a
procurement, or a decision *not* to build — still runs the adversarial lens, but as an
internal-integrity and reconciliation-abuse pass, and may honestly conclude "lightly material,
because …". Customer-outcomes runs wherever customers are affected, including indirectly through
delivery quality or a B2B or internal decision; where the effect is purely second-order, run it
lightly and record why, rather than skipping or padding it. An honest "not material, because …" is
a complete pass; a padded one is not — the seven-dimensions discipline, applied to routing.

Adoption is progressive, and each rung is useful without the next: records alone (TDR) → assurance
on material decisions (TDR + DAC) → organisational risk context → a decision graph computing the
resultant position → continuous assurance. Nothing in this standard requires a graph.

## 5. Record structure

A DAC is a single markdown file: YAML frontmatter for machine-readable fields, markdown body for
the reasoning. A JSON Schema is provided at [`schema/decision-assurance.schema.json`](schema/decision-assurance.schema.json).

### 5.1 Frontmatter fields

| Field | Required | Values / format |
|---|---|---|
| `id` | Yes | `DAC-nnnn`, unique within the owning organisation or repository |
| `tdr_id` | Yes | The decision under test |
| `title` | Yes | Declarative statement of what is being assured |
| `status` | Yes | `proposed` \| `accepted` \| `superseded` \| `stale` |
| `disposition` | Yes | `proceed` \| `proceed-with-constraints` \| `experiment-within-bounded-authority` \| `escalate` \| `defer-pending-evidence` \| `stop` |
| `assessed_at` | Yes | ISO 8601 date |
| `accountable_owner` | Yes | A named individual (never a committee) |
| `review_date` | Yes | When the case must be re-examined even if nothing fires |
| `confidence` | Yes | `low` \| `medium` \| `high` — confidence in the assessment itself |
| `supersedes` | Yes | `DAC-nnnn` or `none` |

`stale` is the honesty state: the case automatically loses standing when its TDR is superseded,
its review date passes unexamined, or a monitoring trigger fires — a stale case authorises nothing.

### 5.2 Body sections

1. **Uncertainty** — knowns, unknowns, assumptions (as assumptions, not facts), and confidence.
   A high-quality case often consists chiefly of making uncertainty explicit.
2. **Adversarial projection** — threat actors and incentives; new attack surfaces; abuse cases and
   paths; identity, consent and authority weaknesses; agent manipulation, collusion and delegation
   risks; preventive/detective/recovery controls; residual exposure and its named owner.
3. **Customer-outcome projection** — target market and excluded cohorts; characteristics of
   vulnerability; price and value; understanding; support and redress; distribution chain;
   differential cohort outcomes; foreseeable financial and non-financial harm.
4. **Control side-effects** — for every protective control: false-positive denials, loss of
   access, friction and abandonment, digital exclusion, unequal cohort effects, delayed redress,
   reduced understanding or agency, and displacement (where the abuse moves when the control works).
5. **Execution capability** — can *this* organisation execute this safely: skills available,
   operational and governance maturity, monitoring capability, supplier capability, readiness.
   The same decision may be appropriate for one organisation and reckless for another.
6. **Risk delta and declared interactions** — inherent risk, proposed controls, local residual
   risk; what this decision increases, decreases, transfers and leaves unknown; declared
   interactions (shared controls, shared identity/authority mechanisms, concentration, correlated
   failures, exception accumulation). The delta is **temporal**: the case declares what risk the
   decision is expected to change, from when (`effective_from`), for how long
   (`expected_duration`), on what trajectory (a transition may duplicate risk before reducing it;
   exposure may grow only as adoption scales), and under what conditions
   (`dependency_conditions` — another decision landing, a threshold being crossed). The case
   records the delta; computing the accumulated and resultant organisational position **at any
   point in time** is graph work, outside this standard — but the case must declare the
   interactions and the temporal shape a graph would need.
7. **Risk vector** — see §6. Never a single score.
8. **Decision debt** — deferred evidence, temporary assumptions, known unknowns, manual
   mitigations, and future review commitments, each with an owner and a date. The debt lies in
   the evidence required to sustain confidence in execution, not necessarily in the decision
   itself. Undeclared decision debt is how temporary uncertainty quietly becomes permanent
   architecture.
9. **Monitoring contract** — each risk or harm hypothesis converted to something observable:
   hypothesis, counter-hypothesis, test, metric, threshold, named owner, and the trigger (reopen
   the TDR, narrow authority, suspend, redesign). This is the design-time authoring of the
   decision's monitorable contract: the case writes it once; runtime assurance reads it.
10. **Learning obligations** — every case closes by creating future learning: hypotheses,
    experiments, evidence required — examined at the case's `review_date`. A decision that teaches
    the organisation nothing was assured in name only.
11. **Disposition** — one of the six, with constraints and conditions stated as testable bounds.
    `proceed-with-constraints` is valid only when the constraints are named, each with an owner
    and a measure — a constraint no one owns is not a constraint. Where the record under test names
    no accountable owner at all, the first constraint is to name one; a case that cannot name an
    owner for the decision itself cannot be `proceed-with-constraints`, and defers. `defer-pending-evidence` and
    `experiment-within-bounded-authority` are never standing states: each names its resolving
    evidence as dated, owned decision-debt items, and the review date or a monitoring trigger
    reopens the disposition — there is always a machine-readable route out.

## 6. The risk vector — no composite score

A single score creates false precision and conceals the reason to stop. The case reports a vector:

**severity · likelihood · exposure volume · velocity · concentration · detectability ·
reversibility · control confidence · customer-cohort distribution · time horizon**

— all ten reported: the first eight each with a stated level and its basis; cohort distribution
and time horizon stated descriptively — plus a **trend** (`improving` \| `deteriorating` \|
`stabilising` \| `oscillating`). Trend is often more important than today's absolute value: a decision may be low
severity and individually tolerable, yet high velocity, poorly detectable and concentrated on one
vulnerable cohort — a composite amber would hide exactly why it should be stopped. The trend is a
point-in-time direction, not the shape of the change over time: non-monotonic shapes — risk that
duplicates before it reduces, or grows only as adoption scales — are carried by
`expected_trajectory` (§5.2.6), not compressed into the trend value.

## 7. Lifecycle and the loop

`proposed → accepted → superseded`, with `stale` as the standing-loss state (§5.1). Lineage and
immutability follow the TDR's rules exactly (spec §§6–7): an accepted case is never edited — a
changed assessment is a superseding case stating what is now known. The full loop the DAC closes:

> **decide → predict → constrain → test → operate → observe → learn → reconsider**

The decision graph an adopter runs should retain both the original predictions and the evidence
that answered them. That is what turns an audit trail into a learning system.

## 8. Regulatory framing — worked examples, not dependencies

The DAC is regulator-neutral. Three regimes illustrate the test it is built to answer:

- **FCA Consumer Duty (UK).** Firms must avoid foreseeable harm and assess, test, understand and
  evidence customer outcomes — with the design-time expectation made explicit: fair-value analysis
  should reflect the assessment made *when decisions are taken*, not retrospective documentation.
  Inadequate fraud protection and inadequate victim support are themselves foreseeable harm; so is
  a fraud control that excludes. The customer-outcome and control-side-effect projections are that
  assessment, at decision time.
- **HM Treasury's agentic-payments trust framework (UK).** Delegated authority, machine-to-machine
  authentication and contested liability concentrate exactly the risks the adversarial projection
  models. An agentic payment journey is the natural first proving ground for a DAC: it contains
  delegated authority, consent, identity, fraud incentives, customer outcomes and machine
  execution in one decision.
- **BCBS 239 (Basel).** The banking system's costliest lesson in *accumulated* exposure: risks
  approved one decision at a time, never aggregated. The declared-interactions requirement (§5.2.6)
  exists so an adopter's graph can do for decision risk what BCBS 239 demanded for financial risk.

Organisations outside financial services will recognise the same shape from their own regulators,
auditors and boards.

## 9. Extension model — patterns and profiles

The core standard stays neutral. Two extension layers are anticipated, each arriving by its own
decision record when real demand exists, never baked into the core:

- **Patterns** — domain assemblies of skills and question emphases (a fraud review pattern, a
  banking pattern, a healthcare pattern, a government pattern).
- **Profiles** — mappings from the DAC's neutral fields to a specific regime's vocabulary (an FCA
  profile, an EBA profile, a NIST profile, an internal-audit profile).

An organisation assembles assurance from reusable components; regulation maps on at the edge.

## 10. Versioning

Follows the TDR specification's rule (spec §9): additive changes are minor versions; anything that
weakens the assurance core — the four questions, proportionality, the risk vector, the stale
state, the non-goal in §1 — would be a different standard, not a new version.

---

*This specification's own adoption is recorded as [TDR-0009](decisions/TDR-0009-decision-assurance-case.md).
Disagree? Propose a superseding TDR — see [CONTRIBUTING](CONTRIBUTING.md).*
