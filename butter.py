"""
ID: wrwwctb1
LANG: PYTHON3
TASK: butter
3.2.7

key idea
dijk from every pasture. calc tot travel dist within each dijk run

if decrease key is available: N C log P = 500 * 1450 * log 800 ~ 7e6
for this implementation     : N C log C

can simplify dijk if nodes have consecutive int names

can skip dict membership check (for neig, est)
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

filename = 'butter'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')













def dijk(neig, s, P, cowlocs):
    pq = [(0, s)]
    seen = [False] * (P+1) # was set
    est = [inf] * (P+1) # was dict
    est[s] = 0

    tot = 0

    while pq:
        estu, u = heappop(pq)
        if seen[u]:
            continue

        seen[u] = True

        if cowlocs[u]: # optimization. no need to do this outside
           tot += estu * cowlocs[u]

        for w, v in neig[u]:
            if seen[v]:
                continue

            if estu + w < est[v]:
                est[v] = cand = estu + w
                heappush(pq, (cand, v))
    return tot


#import time
#tt = time.time()

N, P, C = map(int, input().split())
cowlocs = [0] * (P+1) # cowlocs[loc] = # of cows
for n in range(N):
    loc = int(input())
    cowlocs[loc] += 1

neig = [[] for p in range(P+1)]
for c in range(C):
    u, v, w = map(int, input().split())
    neig[u].append((w, v))
    neig[v].append((w, u))


best = inf
for sugar in range(1, P+1):
    tot = dijk(neig, sugar, P, cowlocs)
    if tot < best:
        best = tot

printwrite(best)


#print(time.time()-tt)









fin.close()
fout.close()
del print, input

