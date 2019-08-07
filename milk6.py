"""
ID: wrwwctb1
LANG: PYTHON3
TASK: milk6
4.4.2

key idea
min s-t cut
decorate weights to favor fewer edges and then smaller indexed edges




point 1/3

when using adj matrix but edges might repeat, deleting (u, v) means
    caps[u][v] -= c
not
    caps[u][v] = 0

point 2/3

min s-t cut is a subset of saturated edges found by max s-t flow

point 3/4

min s-t cut can be found by flood fill on final residual graph
but weights need to decorated to favor fewer edges and smaller indexed edges

point 4/4

if not using weight decoration to break ties, after max flow,

for every saturated edge (sorted by decreasing weight and increasing index):
    remove edge
    if max flow decreases by the edge's capacity,
        edge is part of desired min cut

which is much slower
"""

import os, sys, re, time
from collections import Counter, deque, defaultdict
from queue import Queue
from copy import copy, deepcopy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key, partial as functools_partial
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)
# python -m cProfile -s time ha.py

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'milk6'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









def findAug(caps):
    s = 1
    N = len(caps)-1

    pq = [(-inf, s)]
    done = [False] * (N+1)
    est = [0] * (N+1)
    parent = [None] * (N+1)

    while pq:
        uflow, u = heappop(pq)
        uflow *= -1

        if u == N:
            return uflow, parent

        done[u] = True

        for v in range(1, N+1):
            if done[v]:
                continue
            if caps[u][v] == 0:
                continue
            candPush = min(uflow, caps[u][v])
            if est[v] < candPush:
                est[v] = candPush
                parent[v] = u
                heappush(pq, (-candPush, v))
    return 0, []

def maxFlow(caps):
    tot = 0
    while True:
        flow, parent = findAug(caps)
        if flow == 0:
            break
        tot += flow
        # augment
        v = N
        u = parent[v]
        while u != None:
            caps[u][v] -= flow
            caps[v][u] += flow
            v = u
            u = parent[v]
    return tot


N, M = map(int, input().split())
edges = defaultdict(list)
caps = [[0] * (N+1) for n in range(N+1)]
for m in range(1, M+1):
    u, v, c = map(int, input().split())

    '''
    shift weights by 30 bits
    use 10 bits to favor fewer edges. add to each edge 1<<20. total < 1<<30
    use lower 20 bits to favor smaller indexed edges. total ~ 5e5 < 1<<20
    '''
    c <<= 30
    c += 1 << 20
    c += m

    caps[u][v] += c
    edges[u, v].append((c, m))

caps0 = deepcopy(caps)

best = maxFlow(caps)

# flood fill
stack = [1]
visited = [False] * (N + 1)
while stack:
    u = stack.pop()
    visited[u] = True
    for v in range(1, N + 1):
        if caps[u][v] and not visited[v]:
            stack.append(v)

toCut = []
for u in range(1, N + 1):
    if visited[u]:
        for v in range(1, N + 1):
            if caps0[u][v] and not caps[u][v] and not visited[v]:
                toCut.extend(edges[u, v])

toCut.sort(key=lambda edge: edge[1])

printwrite('%d %d' % (best >> 30, len(toCut)))
for edge in toCut:
    printwrite(edge[1])














fin.close()
fout.close()
del print, input

