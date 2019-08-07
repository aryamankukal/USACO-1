"""
ID: wrwwctb1
LANG: PYTHON3
TASK: agrinet
3.1.2
"""

import os, sys, re, itertools, functools
from collections import Counter, deque, defaultdict
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'agrinet'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')





def prim(mat):
    N = len(mat)

    est = {0: 0}
    done = set()
    pq = [(0, 0)]

    while pq:
        _, u = heappop(pq)

        if u in done:
            continue

        done.add(u)

        for v in range(N):
            if v in done:
                continue

            if v == u:
                continue

            if v not in est or mat[u][v] < est[v]:
                est[v] = mat[u][v]
                heappush(pq, (est[v], v))

    assert len(done) == N

    mstw = 0
    for u in done:
        mstw += est[u]
    return mstw

N = int(input())
mat = []
while True:
    line = input()
    if line == '':
        break
    line = list(map(int, line.split()))
    mat.extend(line)

mat2 = []
for i in range(N):
    mat2.append(mat[i*N:i*N+N])

printwrite(prim(mat2))





fin.close()
fout.close()
del print, input

