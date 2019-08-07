"""
ID: wrwwctb1
LANG: PYTHON3
TASK: inflate
3.1.3

key idea
unbounded knapsack


point 1/2: compare 0-1 and unbounded knapsack

bottomup1 is similar to 0-1 knapsack. careful
bottomup2 is given in cs161

point 2/2: topdown dp may be too deep. consider
10000 1 (10000 minutes available)
10000 1 (one kind. needs only 1 min)
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

filename = 'inflate'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










def bottomup1(M, N, point, minute):
    a = [0] * (M+1)
    for n in range(1, N+1):
        for m in range(1, M+1):
            if m >= minute[n]:
                cand = a[m-minute[n]] + point[n]
                # 0/1 knapsack would either need prev or run backwards
                if cand > a[m]:
                    a[m] = cand
    return a[-1]

def bottomup2(M, N, point, minute):
    a = [0] * (M+1)
    for m in range(1, M+1):
        for n in range(1, N+1):
            if m >= minute[n]:
                cand = a[m-minute[n]] + point[n]
                if cand > a[m]:
                    a[m] = cand
            else:
                break # minute is sorted
    return a[-1]


M, N = map(int, input().split())
mp = [(-1, -1)]
minute = [-1]
for n in range(N):
    p, m = map(int, input().split())
    mp.append((m, p))

mp.sort()
minute, point = zip(*mp)

printwrite(bottomup2(M, N, point, minute))








fin.close()
fout.close()
del print, input

