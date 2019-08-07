"""
ID: wrwwctb1
LANG: PYTHON3
TASK: stall4
4.2.3
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
# python -m cProfile -s time ha.py

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'stall4'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')












def findAug(neigs, caps, s, t):
    numNodes = len(neigs)

    pq = [(-inf, s)]
    done = [False] * numNodes
    est = [0] * numNodes
    parent = [None] * numNodes

    while pq:
        uflow, u = heappop(pq)
        uflow *= -1

        if done[u]:
            continue

        if u == t:
            return uflow, parent

        done[u] = True

        for v in neigs[u]:
            if done[v]:
                continue

            cand_push = min(uflow, caps[u, v])
            if est[v] < cand_push:
                est[v] = cand_push
                parent[v] = u
                heappush(pq, (-cand_push, v))
    return 0, []




def addEdge(neigs, caps, u, v):
    neigs[u].add(v)
    caps[u, v] = 1
    neigs[v].add(u)
    caps[v, u] = 0



N, M = map(int, input().split())
neigs = [set() for i in range(N + M + 2)] # neigs[u] = {v1, v2, ...}
caps = {} # caps[u, v] = c
for n in range(1, N+1):
    addEdge(neigs, caps, 0, n)
    line = list(map(int, input().split()))
    for m in line[1:]:
        realm = m + N
        addEdge(neigs, caps, n, realm)
for m in range(1, M+1):
    realm = m + N
    addEdge(neigs, caps, realm, N + M + 1)


tot = 0
while True:
    flow, parent = findAug(neigs, caps, 0, N+M+1)
    if flow == 0:
        break
    tot += flow

    # aug graph
    v = N + M + 1
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

