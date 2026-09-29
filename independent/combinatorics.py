"""Standalone rank-two reconstruction. No imports from the research implementation.

Cells are encoded by their complete sets of nonzero unordered two-minors.
The only mathematical input is cyclic interval classes and dim=q+s-4.
"""
from itertools import combinations
from functools import lru_cache


def bases(blocks):
    colors = {v: i for i, block in enumerate(blocks) for v in block}
    return tuple((a, b) for a, b in combinations(sorted(colors), 2)
                 if colors[a] != colors[b])


def classes(key):
    support = sorted({i for pair in key for i in pair})
    pairs = set(key)
    # Start immediately after a boundary, so a wrapping class stays intact.
    start = next(j for j in range(len(support))
                 if tuple(sorted((support[j-1], support[j]))) in pairs)
    order = support[start:] + support[:start]
    result = [[order[0]]]
    for x in order[1:]:
        if tuple(sorted((result[-1][-1], x))) in pairs:
            result.append([x])
        else:
            result[-1].append(x)
    assert bases(result) == key
    return tuple(map(tuple, result))


def profile(blocks):
    sizes = tuple(map(len, blocks))
    return min(t[j:] + t[:j] for t in (sizes, sizes[::-1]) for j in range(len(t)))


@lru_cache(maxsize=None)
def affine(n, key):
    necklace = []
    for i in range(1, n+1):
        necklace.append(set(min(key, key=lambda b: sorted((v-i) % n for v in b))))
    out = []
    for i, a in enumerate(necklace, 1):
        b = necklace[i % n]
        if i not in a:
            assert a == b
            out.append(i)
        elif a == b:
            out.append(i+n)
        else:
            assert a-b == {i} and len(b-a) == 1
            v = next(iter(b-a))
            out.append(v if v > i else v+n)
    return tuple(out)


@lru_cache(maxsize=None)
def loopless(q, dimension):
    s = dimension + 4 - q
    if not 2 <= s <= q:
        return ()
    found = set()
    # Choose boundaries AFTER labels. Each boundary set determines one partition.
    for ends in combinations(range(1, q+1), s):
        blocks = []
        for left, right in zip(ends, ends[1:] + ends[:1]):
            blocks.append(tuple(1 + (left + t) % q for t in range((right-left) % q)))
        found.add(bases(blocks))
    return tuple(sorted(found))


def mechanism(key):
    blocks = classes(key)
    q = sum(map(len, blocks))
    assert q + len(blocks) == 12
    if max(map(len, blocks)) > q-5:
        return 'collapsed/nonadmissible'
    if max(map(len, blocks)) == q-5:
        return 'complement-five'
    if sorted(map(len, blocks)) == [3, 3, 3]:
        return 'spurion'
    assert sorted(map(len, blocks)) == [2, 2, 2, 2]
    return 'four-mass noninjective'


def admissible(key):
    return mechanism(key) in ('complement-five', 'spurion')


def transform(key, mapping):
    return tuple(sorted(tuple(sorted(mapping[x] for x in pair)) for pair in key))


def tiles(n, normalized=False):
    found = set()
    for q in range(6, min(n, 10)+1):
        supports = ([tuple(range(1, n+1))] if q == n else
                    [tuple(range(2, n+1))] if q == n-1 else []) if normalized else combinations(range(1, n+1), q)
        for support in supports:
            for key in loopless(q, 8):
                if admissible(key):
                    found.add(transform(key, dict(enumerate(support, 1))))
    return tuple(sorted(found, key=lambda b: affine(n, b)))


def facets(key):
    blocks = classes(key)
    out = set()
    for j, block in enumerate(blocks):
        if len(block) > 1:
            for x in block:
                out.add(bases(blocks[:j] + (tuple(v for v in block if v != x),) + blocks[j+1:]))
    if len(blocks) > 2:
        for j in range(len(blocks)):
            cyclic = blocks[j:] + blocks[:j]
            out.add(bases((cyclic[0] + cyclic[1],) + cyclic[2:]))
    return tuple(sorted(out))


def transported_rows(n, columns, prototypes, normalized=False):
    index = {key: j for j, key in enumerate(columns)}
    rows = {}
    for proto in prototypes:
        q = proto['n']
        if q > n or (normalized and q < n-1):
            continue
        supports = ([tuple(range(1, n+1))] if q == n else
                    [tuple(range(2, n+1))]) if normalized else combinations(range(1, n+1), q)
        for support in supports:
            for direction in (-1, 1):
                for shift in range(q):
                    mapping = {i: support[(direction*(i-1)+shift) % q] for i in range(1, q+1)}
                    row = [0]*len(columns)
                    for facet in proto['signed_admissible_facets']:
                        key = transform(bases(facet['classes']), mapping)
                        if key in index:
                            row[index[key]] += facet['coefficient']
                        else:
                            assert normalized and set(range(2, n+1)) - {v for b in key for v in b}
                    if not any(row):
                        continue
                    sign = 1 if next(v for v in row if v) > 0 else -1
                    row = tuple(sign*v for v in row)
                    parent = transform(bases(proto['parent_classes']), mapping)
                    rows.setdefault(row, set()).add(affine(n, parent))
    return rows
