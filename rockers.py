"""
ID: wrwwctb1
LANG: PYTHON3
TASK: rockers
3.4.4

key idea
0-1 knapsack

easier than usaco sol

look ahead or look back?
    always look back when considering correctness. look ahead is confusing

    programming style can be look ahead or look back
        0-1 knapsack: easier with look back
        unbounded   :                  ahead


complete search using c++ works
- easier to think about
- harder to code
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

filename = 'rockers'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










# N songs           1-20
# T mins per cd     1-20
# M cds             1-20

N, T, M = map(int, input().split())

tsong0 = list(map(int, input().split()))

# remove big songs
tsong = [None]
for t in tsong0:
    if t <= T:
        tsong.append(t)
N = len(tsong)-1

# d[t]: max num of songs that can fit in total time t
# order of songs respected
# cd boundaries respected
d = [0] * (M * T + 1)

for n in range(1, N + 1):
    for t in range(M * T, 0, -1):
        trem = t % T
        twholeCD = t - trem

        if t >= tsong[n]:
            # s: previous time from which curr d[t] can be incremented
            if tsong[n] <= trem:
                s = t - tsong[n]
            else:
                s = twholeCD - tsong[n]

            if d[t] < d[s] + 1:
                d[t] = d[s] + 1

printwrite(d[-1])









fin.close()
fout.close()
del print, input

