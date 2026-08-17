#!/usr/bin/env python3
"""Run the SHACL relational-validity spike. Non-normative — see README.md.

    pip install pyshacl && python3 spikes/shacl-relational-validity/run.py

Prints, for each data graph, which shapes reported violations. The interesting output is not that
the violating graph fails — it is that the unreachable graph fails *identically* to it.
"""
import os
import sys

try:
    from pyshacl import validate
    from rdflib import Graph
except ImportError:
    sys.exit("this spike needs pyshacl: pip install pyshacl")

HERE = os.path.dirname(os.path.abspath(__file__))
SH = "http://www.w3.org/ns/shacl#"


CONTEXT_PREFIX = "https://github.com/saileshpanchal/mtdr/"


def run(data_file, partition=False):
    data = Graph().parse(os.path.join(HERE, data_file), format="turtle")
    outside = []
    if partition:
        # MTDR declares its evaluation context before validating. Everything the context cannot
        # reach is removed here and reported separately, so SHACL only ever sees the part of the
        # world it is entitled to reason about under a closed-world assumption.
        for s, p, o in list(data):
            if hasattr(o, "startswith") and str(o).startswith("http") \
               and not str(o).startswith(CONTEXT_PREFIX):
                data.remove((s, p, o))
                outside.append(str(o).rsplit("/", 1)[-1])
    shapes = Graph().parse(os.path.join(HERE, "shapes.ttl"), format="turtle")
    conforms, results, _ = validate(data, shacl_graph=shapes, advanced=True, debug=False)
    findings = []
    q = """
        PREFIX sh: <http://www.w3.org/ns/shacl#>
        SELECT ?focus ?path ?value ?msg WHERE {
            ?r a sh:ValidationResult .
            OPTIONAL { ?r sh:focusNode ?focus }
            OPTIONAL { ?r sh:resultPath ?path }
            OPTIONAL { ?r sh:value ?value }
            OPTIONAL { ?r sh:resultMessage ?msg }
        }
    """
    for focus, path, value, msg in sorted(results.query(q), key=lambda t: str(t[0])):
        findings.append((
            str(focus).rsplit("/", 1)[-1] if focus else "?",
            str(path).rsplit("#", 1)[-1] if path else "(sparql)",
            str(value).rsplit("/", 1)[-1] if value else "",
            " ".join(str(msg).split())[:90] if msg else "",
        ))
    return conforms, findings, outside


for data_file in ("data-conforming.ttl", "data-violating.ttl", "data-unreachable.ttl"):
    conforms, findings, _ = run(data_file)
    print(f"\n=== {data_file} — conforms: {conforms}")
    for focus, path, value, msg in findings:
        print(f"    {focus:<12} {path:<16} {value:<16} {msg}")
    if not findings:
        print("    (no violations)")

print("""
The two failing graphs are the finding. data-violating.ttl cites a burnt identifier that will never
have a governed representation; data-unreachable.ttl cites a real record held in a distribution this
context does not include. MTDR requires `fail` for the first and `indeterminate` for the second
(TDR-0033; tests/validation/FIX-104 and FIX-103). SHACL reports the same violation for both, because
in SHACL the data graph is the world.""")

conforms, findings, outside = run("data-unreachable.ttl", partition=True)
print(f"\n=== data-unreachable.ttl, partitioned by declared context — conforms: {conforms}")
for focus, path, value, msg in findings:
    print(f"    {focus:<12} {path:<16} {value:<16} {msg}")
if not findings:
    print("    (no violations within the declared context)")
for ref in outside:
    print(f"    outside the context, reported indeterminate by MTDR, never seen by SHACL: {ref}")

print("""
Partitioning first is what makes SHACL usable. MTDR declares its evaluation context before
validating; everything the context cannot reach is withheld and reported `indeterminate`, and SHACL
sees only the part of the world it is entitled to close over. The judgement SHACL cannot make is
made before it runs — which is exactly why SHACL can be a component and not the contract.""")
