"""Re-run the suite's own candidate contract over the trial's candidates, at the commit the trial ran on.

Independent of the trial agent: the agent never ran tests/verify.py, and wrote its own validator
(validate.py, beside this file). This applies the standard's checks instead — the historical-candidate
schema with schemas/shared/ as a registry, the integrity rules and the package's recovery roles from
tests/verify.py, and contemporaneity recomputed — every one read from the pinned commit with
`git show`, so later changes to the standard cannot alter the result.

Usage, from a clone of the repository:
    uv run python decisions/evidence/DAC-0048-adopter-trial-2026-11-07/check.py [commit]

The default pin is 7b2fb20. The trial began at 665aa6e; 7b2fb20 landed during the run and changed
specification prose only, so the contract is identical at both. Against a later commit the outputs are
not expected to pass: the contract they were written for has since been amended.
"""
import datetime
import glob
import json
import os
import re
import subprocess
import sys

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

PIN = sys.argv[1] if len(sys.argv) > 1 else '7b2fb20'
HERE = os.path.dirname(os.path.abspath(__file__))


def show(path):
    return subprocess.run(['git', 'show', f'{PIN}:{path}'], capture_output=True, text=True, check=True).stdout


def tree(path):
    out = subprocess.run(['git', 'ls-tree', '--name-only', PIN, path + '/'], capture_output=True, text=True, check=True)
    return out.stdout.split()


schemas = [json.loads(show(p)) for p in tree('schemas/shared') if p.endswith('.schema.json')]
registry = Registry().with_resources((d['$id'], Resource.from_contents(d)) for d in schemas)
validator = Draft202012Validator(next(d for d in schemas if d['$id'].endswith('/historical-candidate.schema.json')),
                                 registry=registry)

vocabulary = {}                                        # the recovery vocabulary as the pinned manifests declare it
for pkg in tree('records'):
    try:
        manifest = yaml.safe_load(show(f'{pkg}/package.yaml')) or {}
    except subprocess.CalledProcessError:
        continue
    if manifest.get('vocabulary') and manifest.get('object'):
        vocabulary[manifest['object']] = json.loads(show(f"{pkg}/{manifest['vocabulary']}"))['$defs']

source = show('tests/verify.py')
ns = {'re': re, 'datetime': datetime, 'VOCABULARY': vocabulary}
exec(source[source.index('def _values'):source.index('def jcs_digest')], ns)
exec(source[source.index('def _interval'):source.index('for _cap, _cre')], ns)

passed, files = 0, sorted(glob.glob(os.path.join(HERE, 'out', '*.hdc.json')))
print(f"contract at {PIN}; {len(files)} candidates")
for f in files:
    doc = json.load(open(f, encoding='utf-8'))
    errors = [f"{'/'.join(map(str, e.absolute_path))}: {e.message}" for e in validator.iter_errors(doc)]
    errors = errors or ns['candidate_integrity'](doc)
    grades = ns['contribution_grades'](doc) if not errors else {}
    passed += not errors
    print(f"{os.path.basename(f):22} {'PASS' if not errors else 'FAIL ' + errors[0][:100]} | "
          f"event={doc['event_time_ref']} | grades={grades}")
print(f"{passed} of {len(files)} pass the suite's own contract at {PIN}")
