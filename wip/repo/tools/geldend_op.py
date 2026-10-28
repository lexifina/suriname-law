"""Prints the law of Suriname as it stood on a given day, read from this repository's history.

    python tools/geldend_op.py 2023-10-26 grondwet art-061   # art. 61 the day before S.B. 2023 no. 157
    python tools/geldend_op.py 2023-10-27 grondwet 61        # the same article, by number, as amended
    python tools/geldend_op.py 2000-01-01 grondwet           # the whole Grondwet on 1 January 2000
    python tools/geldend_op.py --law 2024-01-01 grondwet 163 # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. Standard library only.
"""
import runpy
import sys
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')
