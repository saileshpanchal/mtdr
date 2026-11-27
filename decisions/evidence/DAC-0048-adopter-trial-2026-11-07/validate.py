"""Stage-5 validator for the adopter trial (my own; not the standard's tests/verify.py).

Usage: python -I validate.py <hdc.json> [...]

Checks, each labelled SCHEMA or STRUCT:
  SCHEMA  historical-candidate.schema.json with schemas/shared/ loaded as a registry
  STRUCT  integrity rules 1-5 of specification/historical-candidate.md
  STRUCT  event_time_ref is unknown or a contribution whose semantic_role is decision-date
  STRUCT  contribution_annotations cover every context contribution and no other
  STRUCT  never-inferred roles/classes carry derivation: explicit
  STRUCT  semantic_role is a package role or a vocabulary class (never not-a-decision/non-decision)
  STRUCT  no floating-point numbers anywhere
  STRUCT  every fragment's source_hash and char-offset locator reproduce its content from the file
  STRUCT  every contribution is in the assembly; target_object agrees
  INFO    contemporaneity recomputed per context contribution (historical-recovery.md, literal interval reading)
"""
import calendar
import datetime as dt
import glob
import hashlib
import json
import os
import sys

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

# Sanitised for preservation: the two local paths the trial hard-coded are read from the environment.
STD = os.environ.get("MTDR_ROOT", ".")          # a checkout of the standard at the trial's pin
TRIAL = os.environ.get("TRIAL_ROOT", os.path.dirname(os.path.abspath(__file__)))

schemas = {}
for p in glob.glob(os.path.join(STD, "schemas/shared/*.schema.json")):
    with open(p) as fh:
        s = json.load(fh)
    schemas[os.path.basename(p)] = s
registry = Registry().with_resources(
    [(s["$id"], Resource.from_contents(s)) for s in schemas.values()]
)
HC = Draft202012Validator(schemas["historical-candidate.schema.json"], registry=registry)

with open(os.path.join(STD, "records/decision/schema/decision-contribution.schema.json")) as fh:
    VOCAB = json.load(fh)
CLASSES = set(VOCAB["$defs"]["class"]["enum"])
NEVER_INFERRED = set(VOCAB["$defs"]["never_inferred_roles"]["enum"])
EVENT_ROLE = VOCAB["$defs"]["event_role"]["const"]
CONTEXT_ROLES = set(VOCAB["$defs"]["context_roles"]["enum"])
PACKAGE_ROLES = {
    "decision-statement", "context", "decision-date", "accountable-owner", "confidence",
    "evidence-business", "evidence-architecture", "evidence-regulatory", "evidence-operations",
    "evidence-customer", "evidence-data", "evidence-external", "alternative-rejected",
    "option-foreclosed", "consequence", "reversal-cost", "lineage-supersedes", "lineage-derived-from",
}
NEVER_IN_CANDIDATE = {"not-a-decision", "non-decision"}


def interval(t):
    if t == "unknown":
        return None
    parts = t.split("-")
    y = int(parts[0])
    if len(parts) == 1:
        return dt.date(y, 1, 1), dt.date(y, 12, 31)
    m = int(parts[1])
    if len(parts) == 2:
        return dt.date(y, m, 1), dt.date(y, m, calendar.monthrange(y, m)[1])
    d = dt.date(y, m, int(parts[2]))
    return d, d


def grade(event, capture, creation):
    """historical-recovery.md 'Contemporaneity is computed'. Day = whole-day interval.
    Returns (literal, point) where 'point' is the alternative reading that treats a same-day
    capture as ending 'at' the event's beginning."""
    if event is None:
        return "indeterminate", "indeterminate"
    ev_s, ev_e = event
    out = []
    for strict in (True, False):
        if capture is not None:
            c_s, c_e = capture
            if (c_e < ev_s) if strict else (c_e <= ev_s):
                out.append("contemporaneous")
            elif c_s > ev_e:
                out.append("later")
            else:
                out.append("indeterminate")
        elif creation is not None:
            k_s, k_e = creation
            if (k_e < ev_s) if strict else (k_e <= ev_s):
                out.append("contemporaneous")
            else:
                out.append("indeterminate")
        else:
            out.append("indeterminate")
    return tuple(out)


def has_float(x):
    if isinstance(x, float):
        return True
    if isinstance(x, dict):
        return any(has_float(v) for v in x.values())
    if isinstance(x, list):
        return any(has_float(v) for v in x)
    return False


def check(path):
    res = []

    def r(kind, name, ok, detail=""):
        res.append((kind, name, "pass" if ok else "FAIL", detail))

    with open(path) as fh:
        h = json.load(fh)
    errs = sorted(HC.iter_errors(h), key=lambda e: list(e.path))
    r("SCHEMA", "historical-candidate schema (registry: schemas/shared)", not errs,
      "; ".join(f"{list(e.path)}: {e.message}" for e in errs[:5]))
    r("STRUCT", "no floating-point numbers", not has_float(h))

    frags = {f["fragment_id"]: f for f in h["fragments"]}
    cons = {c["contribution_id"]: c for c in h["contributions"]}
    r("STRUCT", "fragment ids unique", len(frags) == len(h["fragments"]))
    r("STRUCT", "contribution ids unique", len(cons) == len(h["contributions"]))

    bad = [(c, f) for c in cons.values() for f in c["fragment_refs"] if f not in frags]
    r("STRUCT", "integrity 1: contribution fragment_refs resolve", not bad, str(bad))
    a = h["assembly"]
    bad = [c for c in a["contribution_refs"] if c not in cons]
    r("STRUCT", "integrity 2: assembly contribution_refs resolve", not bad, str(bad))
    ann_refs = [x["fragment_ref"] for x in h["fragment_annotations"]]
    r("STRUCT", "integrity 3a: each fragment annotated exactly once",
      sorted(ann_refs) == sorted(frags) and len(ann_refs) == len(set(ann_refs)))
    ca_refs = [x["contribution_ref"] for x in h["contribution_annotations"]]
    r("STRUCT", "integrity 3b: contribution annotations name existing contributions, at most once",
      all(c in cons for c in ca_refs) and len(ca_refs) == len(set(ca_refs)))
    etr = h["event_time_ref"]
    ok4 = etr == "unknown" or etr in a["contribution_refs"]
    r("STRUCT", "integrity 4: event_time_ref unknown or in assembly", ok4, etr)
    ok5 = True
    for x in h["contribution_annotations"]:
        st, fr = x["considered"]["state"], x["considered"]["fragment_refs"]
        if st == "evidenced" and (not fr or any(f not in frags for f in fr)):
            ok5 = False
        if st != "evidenced" and fr:
            ok5 = False
    r("STRUCT", "integrity 5: considered evidenced carries resolving fragments; others none", ok5)

    r("STRUCT", "event_time_ref names a decision-date contribution (or unknown)",
      etr == "unknown" or (etr in cons and cons[etr]["semantic_role"] == EVENT_ROLE), etr)
    ctx = {c for c, v in cons.items() if v["semantic_role"] in CONTEXT_ROLES}
    r("STRUCT", "considered on every context contribution and no other", set(ca_refs) == ctx,
      f"context={sorted(ctx)} annotated={sorted(ca_refs)}")
    bad = [c for c, v in cons.items() if v["semantic_role"] in NEVER_INFERRED and v.get("derivation") != "explicit"]
    r("STRUCT", "never-inferred roles carry derivation: explicit", not bad, str(bad))
    bad = [(c, v["semantic_role"]) for c, v in cons.items()
           if v["semantic_role"] in NEVER_IN_CANDIDATE or v["semantic_role"] not in (PACKAGE_ROLES | CLASSES)]
    r("STRUCT", "semantic_role is a package role or vocabulary class; no finding classes", not bad, str(bad))
    r("STRUCT", "every contribution is in the assembly", set(cons) == set(a["contribution_refs"]))
    r("STRUCT", "target_object agrees", all(v["target_object"] == a["target_object"] for v in cons.values()))
    for x in h["fragment_annotations"]:
        if "restates" in x and x["restates"] not in frags:
            r("STRUCT", f"restates resolves inside candidate ({x['fragment_ref']})", False, x["restates"])

    # provenance: hash and locator reproduce content
    okp, det = True, []
    for f in frags.values():
        p = os.path.join(TRIAL, f["source_ref"])
        with open(p, "rb") as fh:
            raw = fh.read()
        if "sha256:" + hashlib.sha256(raw).hexdigest() != f["source_hash"]:
            okp = False
            det.append(f"{f['fragment_id']}: hash")
        txt = raw.decode("utf-8")
        L = f["locator"]
        if txt[L["start"]:L["end"]] != f["content"]:
            okp = False
            det.append(f"{f['fragment_id']}: locator")
    r("STRUCT", "source_hash and locator reproduce verbatim content", okp, "; ".join(det))

    # contemporaneity, recomputed
    anns = {x["fragment_ref"]: x for x in h["fragment_annotations"]}
    event = None
    if etr != "unknown" and etr in cons:
        try:
            event = interval(str(cons[etr]["interpreted_value"]))
        except Exception:
            r("STRUCT", "event time parses at a legal precision", False, str(cons[etr]["interpreted_value"]))
    lines = []
    for c in sorted(ctx):
        per = []
        for f in cons[c]["fragment_refs"]:
            an = anns[f]
            g = grade(event, interval(an["capture_time"]), interval(an["creation_time"]))
            per.append((f, an["evidence_kind"], g))
        # restatements count as their source when the source is also referenced
        primary = [p for p in per if not (p[1] == "restatement" and anns[p[0]].get("restates") in cons[c]["fragment_refs"])]
        lit = {p[2][0] for p in primary}
        pt = {p[2][1] for p in primary}
        agg = lambda s: "later" if "later" in s else ("contemporaneous" if s == {"contemporaneous"} else "indeterminate")
        lines.append(f"{c}: literal={agg(lit)} point-reading={agg(pt)} per-fragment={[(p[0], p[2][0]) for p in per]}")
    return res, lines


def main():
    fails = 0
    for path in sys.argv[1:]:
        res, lines = check(path)
        print(f"== {os.path.basename(path)}")
        for kind, name, st, det in res:
            if st != "pass":
                fails += 1
            print(f"  [{kind}] {st}: {name}" + (f" -- {det}" if det and st != "pass" else ""))
        for ln in lines:
            print(f"  [INFO] contemporaneity {ln}")
    print(f"TOTAL FAILURES: {fails}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
