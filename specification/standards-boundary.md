# The standards boundary

**Version:** 1.1.0 · **Licence:** MIT · **Author:** Sailesh Panchal

Where this standard sits among the standards it touches. Decided in
[TDR-0035](../decisions/TDR-0035-standards-boundary.md).

An open specification that expects others to build implementations owes them this register. Without
it, every adopter re-derives the same questions — *does MTDR need a graph? a policy engine? an agent
platform?* — and answers them differently, which is how a portable standard quietly acquires an
architecture.

## The layers, and which one MTDR occupies

A register of dispositions answers *what MTDR depends on*. It does not answer the question adopters
actually arrive with, which is **why MTDR exists at all when they already have skills, plugins and a
protocol**. The answer is that those solve different problems, and the confusion is worth ending
explicitly rather than leaving it implicit in a packaging directory.

| Layer | Concern | Who owns it |
|---|---|---|
| **Knowledge and provenance packaging** | How a body of material is packaged, described and shipped | Open Knowledge / data-package formats — *deferred* |
| **Procedural capability** | How a repeatable method is expressed so an agent can apply it | Agent Skills (`SKILL.md`) — **adopted** |
| **Packaging and distribution** | How capability reaches a particular runtime | Agent plugin packaging — *interoperated with* |
| **Interaction** | How a participant is handed material and returns results | MCP — *interoperated with* |
| **Governed semantics and lifecycle** | What an organisational record *means*, what states it may occupy, and what a transition requires | **MTDR** |
| **Standing** | Which commitments the organisation is actually accountable for | **Authorised human acts** — outside every standard here |

Read downward, each layer is a genuine dependency of the one above it in practice and a genuine
*non*-dependency in principle: a governed record is still a governed record with no plugin, no
protocol and no runtime.

Two of these rows are the whole argument.

**Nothing but MTDR occupies the semantics-and-lifecycle layer.** A skill can express a method; it
cannot say that a value commitment lacking a counter-signatory is a valid candidate and an ineligible
ratification. A plugin can ship that skill; a protocol can carry its output. None of them defines what
the output *means* or what may legitimately be done to it next. That gap is why this standard exists,
and it is also why MTDR can adopt the skills layer wholesale without competing with it.

**Nothing at all occupies the standing layer.** It is not that no standard has reached it yet — it is
that it cannot be occupied by a standard. Standing originates in an authorised human act
([TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md)), and every mechanism below
can at most establish that the evidenced preconditions are satisfied
([`obligation-chain.md`](obligation-chain.md)). A tool that appears to supply standing has not solved
the last layer; it has quietly relocated accountability into software.

The practical consequence for an adopter: **you do not choose between MTDR and your agent stack.** You
keep the stack and gain the layer it does not have.

## The dispositions

| Disposition | Meaning |
|---|---|
| **adopt** | MTDR uses it directly. It is a dependency, named and versioned. |
| **map** | MTDR does not use it, and publishes a correspondence so those who do can cross the boundary without loss. |
| **interoperate** | Compatible downstream, through an optional adapter. **Never an architectural dependency.** |
| **defer** | The requirement that would justify a decision does not exist yet. Tracked, not adopted, and revisited when it does. |
| **reject** | Considered and declined, with the reason recorded so it is not silently reconsidered. |

The distinction that carries the most weight is **adopt** versus **interoperate**. Everything MTDR
adopts, an adopter must also have. That is the whole cost of the boundary, and it is why the adopt
column is short.

## The register

| Standard or project | Disposition | Reasoning | What it does not mean |
|---|---|---|---|
| **JSON Schema** (draft 2020-12) | adopt | Every machine contract in this repository is a JSON Schema. It is ubiquitous, has implementations in every language an adopter might use, and separates a validation vocabulary from any validator's output — the same separation the [validation-result contract](validation-result.md) makes. | Schema validity is the floor of conformance, not the test. Structural validity is one of four dimensions. |
| **W3C PROV** | map | MTDR's [provenance model](provenance.md) — fragment, contribution, interpreter, time — corresponds closely to PROV's entity/activity/agent triad. Publishing the correspondence lets a PROV-native estate consume MTDR provenance without MTDR taking a dependency on an RDF stack. | MTDR does not emit PROV, and no conformance claim rests on it. |
| **in-toto Attestations** | map | The Statement layer binds metadata to an *identified subject* under a *versioned predicate type*, with the two versioning independently. The [validation-result contract](validation-result.md) makes the same structural move for the same reason, and publishing the correspondence lets an attestation-native estate read MTDR results without MTDR taking the dependency. **Borrowing a shape is not adopting a framework**, which is why this is a map and not an adopt. | MTDR is not becoming a supply-chain framework, emits no attestations, and no conformance claim rests on one. |
| **Agent Skills (`SKILL.md`)** | adopt | The canonical portable skill surface ([TDR-0023](../decisions/TDR-0023-portable-skill-architecture.md)). Frontmatter is strict, the format is plain, and it travels to any participant that can read a file. | A conforming skill file establishes nothing about the execution that reads it ([TDR-0032](../decisions/TDR-0032-typed-multi-object-conformance.md)). |
| **MCP** | interoperate | A reasonable transport for handing records and skills to a participant. An optional [packaging adapter](../skills/packaging/) may explain how; nothing in the standard requires it. | MCP is not how MTDR is defined, distributed or validated, and a participant without it is not disadvantaged. |
| **Agent plugin packaging** | interoperate | Same argument, different runtime. Packagings are distribution adapters and never normative architecture ([TDR-0024](../decisions/TDR-0024-packaging-independence.md)). | A packaging may explain how to invoke a skill. It may add no record semantics. |
| **A2A (agent-to-agent protocols)** | defer | No participant-to-participant requirement exists in this standard. The artefact boundary means MTDR produces files; what negotiates over them is above that boundary. | Deferred is not rejected. If a governed interchange between participants ever needs specifying, it arrives as a proposal like any other. |
| **Open Knowledge / data-package formats** | defer | The packaging concepts overlap with [record packages](../records/README.md) — manifests, declared dependencies, extractability. The ecosystem is immature enough that binding to it would import instability for a problem MTDR has already solved locally. | Tracked deliberately. The manifest vocabulary should stay mappable rather than drifting somewhere idiosyncratic. |
| **SHACL** | map | [Spiked and executed](../spikes/shacl-relational-validity/README.md). Lineage and record-binding constraints express beautifully in core SHACL; version compatibility and closure need `sh:sparql`. The decisive finding: **SHACL cannot express `indeterminate`** — in SHACL the data graph is the world, so an unreachable reference and an absent one are the same violation, and MTDR requires them to be different. Adopting it would force `indeterminate` to collapse into `fail`, which DAC-0033 identifies as making offline and zero-install use impractical. | Not a judgement that SHACL is unsuitable downstream. Partition by the declared evaluation context first and SHACL validates the reachable subset correctly — as a component under MTDR's context declaration, never as the contract. |
| **W3C Verifiable Credentials** | defer | Portable authority and evidence assertions are a real future need — ratification evidence that travels with a record is exactly the shape VCs address. The candidate `authority` package has not passed admission, so there is nothing yet to bind. | Deferred pending the authority language, not pending interest. Revisit when that package is admitted. |
| **AuthZEN** | interoperate | An authorisation-decision interchange downstream of MTDR. A record can inform an authorisation decision; MTDR does not make one. | MTDR never evaluates authorisation. [TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md) reserves standing to the human act, and no policy result substitutes for it. |
| **Cedar · OPA · OpenFGA** | interoperate | Compatible downstream policy engines. An organisation may drive policy from governed records, and the records are readable without any of them. | **None is an MTDR dependency, and none may become one.** A record whose meaning requires a policy engine is not portable. |
| **SPIFFE / SPIRE** | interoperate | A reference for machine participant identity, useful to anyone running participants at scale. | Outside the kernel. MTDR identifies conformance *subjects*; it does not issue, verify or depend on machine identity. |
| **Mermaid and Markdown inspectability surfaces** | adopt | Diagrams and documents that render everywhere, degrade to readable text, and diff in version control. Inspectability that requires a viewer is not portable inspectability. | Presentation only. No normative semantics may live in a diagram. |
| **Agent-harness research projects** | defer | Implementation research. Interesting for how participants execute skills; nothing there is a standard yet, and the field moves faster than a specification should. | Watching is not adopting, and nothing in this repository may assume a particular harness. |

## The rule the register follows

**Adopt where the standard is mature, ubiquitous and cheap for an adopter to already have. Map where
the concepts correspond but the dependency would not be cheap. Interoperate where the value is real
and downstream. Defer where the requirement has not arrived.**

Applied consistently, that keeps the adopt column at three entries — JSON Schema, `SKILL.md` and
portable markdown — which is close to the minimum a standard of this kind can have while remaining
mechanically checkable. Structural ideas borrowed from elsewhere, such as in-toto's
subject-and-versioned-predicate envelope, sit under **map**: taking a shape costs an adopter nothing,
and calling it adoption would misstate what they need to have.

Every disposition here is revisable by a superseding TDR, and one of them already changed under
evidence: SHACL entered as a spike and left as a map, because the spike was run rather than assumed.
