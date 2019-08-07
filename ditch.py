"""
ID: wrwwctb1
LANG: PYTHON3
TASK: ditch
4.2.2
"""

import os, sys, re
from collections import Counter, deque, defaultdict
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key, partial as functools_partial
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'ditch'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










def addEdge(u, v, c, caps, neigs):
    neigs[u].add(v)
    if (u, v) in caps:
        caps[u, v] += c
    else:
        caps[u, v] = c
    # back
    neigs[v].add(u)
    if (v, u) in caps:
        pass
    else:
        caps[v, u] = 0

def findAug(neigs, caps, s, t):
    N_1 = len(neigs)

    pq = [(-inf, s)]
    est = [0] * N_1
    parent = [None] * N_1
    done = [False] * N_1

    while pq:
        uflow, u = heappop(pq)
        uflow = -uflow

        if done[u]:
            continue

        done[u] = True

        if u == t:
            return uflow, parent

        for v in neigs[u]:
            if done[v]:
                continue

            cand_push = min(uflow, caps[u, v])
            if est[v] < cand_push:
                est[v] = cand_push
                parent[v] = u
                heappush(pq, (-cand_push, v))
    return 0, []



M, N = map(int, input().split()) # 0-200 edges, 2-200 nodes

caps = {} # edges[u, v] = c
neigs = [set() for n in range(N+1)] # neigs[u] = set of neigs of node u


for m in range(M):
    S, E, C = map(int, input().split())
    addEdge(S, E, C, caps, neigs)


tot = 0
while True:
    flow, parent = findAug(neigs, caps, 1, N)
    if flow == 0:
        break
    tot += flow

    # update residual graph
    # set caps to zero. no delete neig
    v = N
    while parent[v] != None:
        u = parent[v]
        assert caps[u, v] >= flow
        caps[u, v] -= flow
        caps[v, u] += flow
        v = u



printwrite(tot)












fin.close()
fout.close()
del print, input

