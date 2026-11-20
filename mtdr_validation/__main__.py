"""Validate a folder of recovery output: `python -m mtdr_validation <folder> [--out <dir>]`.

NON-NORMATIVE. Writes one validation result per historical candidate and review event, and a Markdown
summary, to `<folder>/validation/` unless `--out` says otherwise. The exit status is operational — 0 when
the folder was assessed, 2 when it could not be — and never a conformance verdict: there is none
(DAC-0033 constraint 8). Read the summary.
"""
import argparse
import os
import sys

from .folder import assess_folder, write_results
from .recovery import ROOT


def main(argv=None):
    p = argparse.ArgumentParser(prog='python -m mtdr_validation',
                                description='Assess historical candidates and review events in a folder against the '
                                            'published MTDR contract. No aggregate verdict; see the summary.')
    p.add_argument('folder', help='the folder holding the recovery output')
    p.add_argument('--out', help='where to write the results (default: <folder>/validation)')
    p.add_argument('--standard', default=ROOT, help='the MTDR checkout whose schemas and manifests apply '
                                                    '(default: the one this module ships in)')
    args = p.parse_args(argv)
    if not os.path.isdir(args.folder):
        print(f'not a folder: {args.folder}', file=sys.stderr)
        return 2
    out = args.out or os.path.join(args.folder, 'validation')
    assessments, not_assessed = assess_folder(args.folder, root=args.standard, exclude=[out])
    write_results(args.folder, out, assessments, not_assessed)
    print(f'{len(assessments)} artefact(s) assessed, {len(not_assessed)} file(s) not assessed; '
          f'results and summary in {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
