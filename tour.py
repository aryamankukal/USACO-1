"""
ID: wrwwctb1
LANG: PYTHON3
TASK: tour
5.4.1

key idea
ad hoc dp

d[u][v]: num of cities visited. only allow u < v. use d to find ans

     ______ u
    /
   0
    \____________ v

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

filename = 'tour'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











N, V = map(int, input().split())
edge = [[0] * N for n in range(N)]
name2num = {}
for n in range(N):
    name = input()
    name2num[name] = n
for v in range(V):
    nameu, namev = input().split()
    u = name2num[nameu]
    v = name2num[namev]
    edge[u][v] = edge[v][u] = 1

d = [[0] * N for n in range(N)]

# init d for all immediate neighbors of 0
for v in range(1, N): # 0 < v
    if edge[0][v]:
        d[0][v] = 2

for u in range(N):
    for v in range(u + 1, N): # u < v
        # after each loop, all neighbors to the east of u and v will be updated
        # so if d[u][v] == 0 at the beginning of a loop, u-v no communication
        if d[u][v] == 0:
            continue

        # because of the way the double loop is arranged,
        # when reaching a d[u][v], it's already optimal
        # everything that could have made it better has been considered
        for x in range(v + 1, N): # u < v < x ie x is to the east of u and v
            if edge[v][x]:
                d[u][x] = max(d[u][x], d[u][v] + 1)
            if edge[u][x]:
                d[v][x] = max(d[v][x], d[u][v] + 1)

t = N - 1
ans = 1
for u in range(N):
    for v in range(u + 1, N): # u < v
        if u != t and v != t and edge[u][t] and edge[v][t]:
            ans = max(ans, d[u][v] + 1)
        if u != t and v == t and edge[u][t]:
            ans = max(ans, d[u][v])
        if u == t and v != t:
            assert False

printwrite(ans)












fin.close()
fout.close()
del print, input

