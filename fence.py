'''
ID: wrwwctb1
LANG: PYTHON3
TASK: fence
3.3.2

key idea
eulerian tour or circuit

if u has neighbors, choose one (say v), remove edge u->v, recurse on v
if u has no neighbor, prepend u to path, return

where does the description say edges can be repeated?

because minimal ans is required, it's faster that neig[u] supports fast min
because the need to remove u->v, neig[v] needs to support fast search and del

therefore c++ multiset is a good choice (log-time min, delete and search)

not clear if easily doable with py heapq
'''

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

filename = 'fence'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')
ttt = time.time()












def eulerian(ckt, numneigs, mat, s):
    st = [s]
    while st:
        u = st[-1]
        if numneigs[u]:
            v = 0
            while not mat[u][v]:
                v += 1
            mat[u][v] -= 1
            mat[v][u] -= 1
            numneigs[u] -= 1
            numneigs[v] -= 1
            st.append(v)
        else:
            ckt.append(u)
            st.pop()

nmax = 500

F = int(input())

mat = [[0] * (nmax + 1) for i in range(nmax + 1)]

minu = inf

for f in range(F):
    u, v = list(map(int, input().split()))
    mat[u][v] += 1
    mat[v][u] += 1
    minu = min(minu, u, v)

numneigs = [0] * (nmax + 1)
for i in range(1, nmax+ 1):
    numneigs[i] = sum(mat[i])

odd = []
for i in range(1, nmax + 1):
    if numneigs[i] % 2 != 0:
        odd.append(i)

assert len(odd) == 2 or len(odd) == 0

ckt = []
if len(odd) == 2:
    odd.sort()
    eulerian(ckt, numneigs, mat, odd[0])
else:
    eulerian(ckt, numneigs, mat, minu)


for u in ckt[::-1]:
    printwrite(u)















fin.close()
fout.close()
del print, input
print(time.time() - ttt)
