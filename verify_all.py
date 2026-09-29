#!/usr/bin/env python3
"""Fail-closed one-command replay. Use --list or --certificate ID for a claim."""
import argparse
import platform
import sys
import time
import traceback
import sympy
from verifier import checks

IDS = ('MEM-CORES','MEM-FOUR-MASS','MEM-SPURION','LOCAL-PARENTS','LOCAL-RELATIONS',
       'LOCAL-TEN-WALL','LOCAL-HOSTILE-8','LOCAL-HOSTILE-9','N9-UNIVERSE',
       'N9-LOCAL-RANK','N9-INDICATORS','N9-INDICATOR-RANK','N9-ANNIHILATION','N9-KERNEL',
       'NORM-6','NORM-7','NORM-8','NORM-9','NORM-10','NORM-11','SUPPORT-CUTOFF',
       'N8-UNIT','N9-UNIT','WEIGHT-PROBES','ARTIFACT-HASHES')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate',choices=IDS)
    parser.add_argument('--list',action='store_true',help='List stable claim certificate IDs')
    args=parser.parse_args()
    if not __debug__:
        raise RuntimeError('Verification requires assertions: do not use python -O or PYTHONOPTIMIZE')
    if args.list:
        print('\n'.join(IDS));return
    print(f'[INFO] Python {platform.python_version()}; {platform.system()} {platform.machine()}; SymPy {sympy.__version__}',flush=True)
    start=time.monotonic();chosen=args.certificate
    def passed(message):print('[PASS] '+message,flush=True)
    def selected(*ids):return chosen is None or chosen in ids
    if selected('MEM-CORES'):
        checks.membership_catalogue();passed('membership-core classification');passed('membership-core counts')
    if selected('MEM-FOUR-MASS'):
        checks.four_mass();passed('four-mass two-preimage certificate')
    if selected('MEM-SPURION'):
        checks.spurion_fixture();passed('spurion inversion certificate')
    prototypes=None
    if chosen is None or chosen in ('LOCAL-PARENTS','LOCAL-RELATIONS','N8-UNIT','N9-UNIT','WEIGHT-PROBES') or chosen.startswith(('N9-','NORM-')):
        prototypes=checks.parents()
        passed('29 parent-core exhaustion');passed('3<->3 relation certificates');passed('5<->5 relation certificates')
    if selected('LOCAL-TEN-WALL'):
        checks.overlaps();passed('ten-wall rank-nine certificates')
    for i,n in enumerate((8,9),1):
        if selected(f'LOCAL-HOSTILE-{n}'):
            checks.hostile(n);passed(f'hostile parent {i} determinant')
    if chosen is None or chosen.startswith('N9-'):
        keys,relations=checks.local_n9(prototypes)
        passed('n=9 tile universe = 942');passed('n=9 local relations = 693');passed('rank(L9) = 470')
        if chosen not in ('N9-UNIVERSE','N9-LOCAL-RANK'):
            counts,digest=checks.indicator_n9(keys,relations,lambda s:print(s,flush=True))
            passed('n=9 witnesses = 472');passed('n=9 exact membership decisions = 444624')
            print('[INFO] reconstructed A9 row-major 0/1-byte SHA256: '+digest,flush=True)
            passed('rank(A9) = 472');passed('selected indicator determinant = 4');passed('A9 R9^T = 0')
            print('[INFO] dim L9 = 470; dim ker A9 = 942 - 472 = 470; L9 subset K9 subset ker A9; therefore K9 = L9 (using the stated all-Z local theorem and strict-neighborhood inverse proposition).',flush=True)
            passed('K9 = L9 certificate chain')
    if chosen is None or chosen.startswith('NORM-'):
        for n in checks.normalized(prototypes):
            passed(f'normalized n={n}'+(' determinant = -1' if n==10 else ' determinant = 1' if n==11 else ''))
    if selected('SUPPORT-CUTOFF'):
        checks.membership_catalogue()
        assert not checks.tiles(12,normalized=True)
        passed('support cutoff')
    for n in (8,9):
        if selected(f'N{n}-UNIT'):
            checks.unit_functional(n);passed(f'n={n} signed unit functional')
    if selected('WEIGHT-PROBES'):
        checks.weight_probes();passed('saved unit-weight profile probes')
    if selected('ARTIFACT-HASHES'):
        checks.hashes();passed('publication artifact hashes')
    print(f'[INFO] elapsed seconds: {time.monotonic()-start:.3f}',flush=True)
    if chosen:
        passed('certificate '+chosen)
    else:
        print('ALL PUBLICATION-CRITICAL CERTIFICATES PASSED',flush=True)


if __name__=='__main__':
    try:
        main()
    except Exception:
        print('[FAIL] Publication certificate verification stopped; no ready verdict.',file=sys.stderr,flush=True)
        traceback.print_exc()
        sys.exit(1)
