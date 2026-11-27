# Evaluation of `0650856`, the identity check's `prior_versions` rule

Prepared for the maintainer on 26 November 2026, under the direction to evaluate this change
separately from the documentation that describes it. **It decides nothing.** Whether the change, or a
variant of it, enters the standard is the maintainer's decision, by a governed record.

## The authorised implementation in this release candidate

`release/next-candidate` carries a plain revert of `0650856` (commit `57d68c0`). The identity rule in
`tests/verify.py` and `specification/record-identity.md` are therefore exactly as released in
`v1.30.0` (record identity 1.0.0). This follows the maintainer's direction of 26 November: resolve
the held-out identity-check change separately, and preserve Decision and Value's accepted behaviour.

## What `0650856` does

| Part | Before (`v1.30.0`) | With `0650856` |
|---|---|---|
| `tests/verify.py`, the identity check over this repository's own governed records | A record's `conforms_to` version must equal the manifest's current `specification_version` | It must equal the current version **or** a version listed under the manifest's `prior_versions` |
| `specification/record-identity.md` | 1.0.0. The schema is resolved "in an MTDR distribution whose decision package declares `specification_version: 1.15.0`" | 1.0.1. "…declares version `1.15.0`, as its `specification_version` or among its `prior_versions`", plus: "A prior version a package declares with `schema: null` has no schema to resolve to, and its records are never run against the current one" |

## What it changes in practice

Only one manifest declares a prior version: the value package lists `1.3.0`, the Value Record version
before the breaking 2.0.0 change, with `schema: null` and the comment "v1 records validate
structurally, never against the v2 schema".

| Probe: the VR worked example bound to `vr@1.3.0` | Identity check |
|---|---|
| `v1.30.0` | Rejected: "claims vr@1.3.0; the value manifest ships 2.1.0" |
| With `0650856` (`1ccebdf`) | Accepted |
| Reverted (`57d68c0`) | Rejected, with the same message as `v1.30.0` |

Every governed record in the candidate binds to its package's current version, so neither rule
changes the result of the suite today.

## Two readings

**As a widening.** The review of PR #22 held the change out because it "changes which Decision and
Value records are accepted, and no accepted record authorises it". On this reading the suite would
accept, as one of this repository's governed records, a Value Record bound to a version whose schema
it cannot run.

**As a correction to match accepted text.** The accepted Value Record specification says, in §8:
"Records raised under v1 **remain valid v1 records** and are not retrospectively invalid". The value
manifest at `v1.30.0` already lists `1.3.0` as a prior version with no schema. Record identity 1.0.0
gives a detached v1 record no way to say which specification governs it. On this reading `0650856`
makes record identity agree with §8 and with the manifest, and adds no acceptance the specification
had not already granted.

Both readings are defensible from the text. They differ on whether the identity check states what
this repository requires of its **own** records (current version only, as TDR-0043 says: "required of
this repository's own governed records") or what any distribution must be able to **resolve** (any
version it declares).

## The problem `0650856` set out to fix

If a later release moves a specification to a new minor version (TDR 1.15.0 to 1.16.0, say), every
record in this repository bound to 1.15.0 fails the identity check, although TDR-0043 promises
additive minor versions. Nothing in this release candidate moves a specification version, so nothing
fails now. The problem arrives with the first minor bump.

## Options for a governed decision

| | Rule | `vr@1.3.0` | A future TDR 1.15.0 → 1.16.0 bump | Normative text changes |
|---|---|---|---|---|
| **A** (this candidate) | Current version only | Rejected | Every 1.15.0 record fails | None |
| **B** (`0650856`) | Current, or any declared prior version | Accepted, with no schema to run | Passes, if 1.15.0 is declared prior | `record-identity.md` 1.0.1 |
| **C** | Current, or a declared prior version **within the current major version** | Rejected | Passes, if 1.15.0 is declared prior | `record-identity.md`, a new wording |

## Recommendation

Release with **A**, the authorised implementation. Decide between B and C by a record of its own
before the first minor version bump of any specification, because each changes the normative text of
`record-identity.md` (substrate) and TDR-0043's reach. B is closer to the accepted VR §8; C is the
smaller change to what this repository's suite accepts. Until then, the release lists the issue as a
known limitation.

## Effect on the recovery records

DAC-0048 (lines 41–42 and 131) and TDR-0048 (lines 217–219) state that the identity check "is
repaired" and rely on that for one alternative's reasoning. Under option A those statements are
untrue. The correction is to the records, not to the rule: they should say the check is as released
in `v1.30.0`, that the prior-version question is open, and what follows for the alternative.
