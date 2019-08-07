"""
ID: wrwwctb1
LANG: PYTHON3
TASK: stamps
3.1.6

key idea
looks like classic dp but is a variation

fewest[v] = fewest possible # of stamps that can make up v cents,
            possibly using all stamps

fewest[v] = min( fewest[v - cent[n]] ) + 1
             n


keeping appending to fewest gives bad alloc on usaco
remedy: at every v, only need access to v - max(cent)
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

filename = 'stamps'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










K, N = map(int, input().split())
cent = []
while True:
    line = input()
    if line == '':
        break
    cent.extend(map(int, line.split()))

assert len(cent) == N

cent = sorted(set(cent))

NN = 10001 # max stamp value + 1. think: at 10000, need info at 0
fewest = [0] * NN

need = 1
while True:
    best = inf
    for i in range(N):
        prev = need - cent[i]
        if prev < 0:
            break
        else:
            cand = fewest[prev % NN]
            if cand < best:
                best = cand
    best += 1
    if best > K:
        break
    else:
        fewest[need % NN] = best
        need += 1
printwrite(need - 1)






fin.close()
fout.close()
del print, input

