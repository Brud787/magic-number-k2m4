#!/usr/bin/env python3
"""Release maintainer utility. Does not run during certificate verification."""
from pathlib import Path
import hashlib

ROOT=Path(__file__).resolve().parent
EXCLUDED={'.venv','__pycache__','.pytest_cache','.DS_Store','SHA256SUMS.txt'}


def main():
    files=[p for p in ROOT.rglob('*') if p.is_file() and not any(s in EXCLUDED for s in p.relative_to(ROOT).parts)]
    lines=[hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix() for p in sorted(files)]
    (ROOT/'SHA256SUMS.txt').write_text('\n'.join(lines)+'\n')
    print(f'Frozen {len(lines)} files. SHA256SUMS.txt excludes itself and runtime caches.')


if __name__=='__main__':main()
