"""
ID: wrwwctb1
LANG: PYTHON3
TASK: beads
1.2.7

key idea
dp for red bead count and blue bead count separately

rR[i], at ith bead, if forcing red and counting toward right, how many?
bR[i] similar for blue
rL[i] similar for red, left
bL[i] blue, left

substructure as in code

if final ans < N:
    rR[i] and bR[i] are correct for i = 0 ~ N-1
    rL[i] and bL[i] are correct for i = N ~ 2N-1
    ans can be found as in code

if final ans == N:
    rR[i] or bR[i] will be >= N for i = 0 ~ N-1
    rL[i] or bL[i] will be >= N for i = N ~ 2N-1
    output will be correctly N


naive n^2 can pass, and is easier to code
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

filename = 'beads'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')
ttt = time.time()










N = int(input())
beads = input()
beads = beads + beads

# count toward right
rR = [0] * 2 * N # red right
bR = [0] * 2 * N
for i in range(2 * N - 2, -1, -1):
    if beads[i] == 'w':
        rR[i] = rR[i+1] + 1
        bR[i] = bR[i+1] + 1
    else:
        if beads[i] == 'r':
            rR[i] = rR[i+1] + 1
            bR[i] = 0
        else:
            rR[i] = 0
            bR[i] = bR[i+1] + 1

# count toward left
rL = [0] * 2 * N
bL = [0] * 2 * N
for i in range(1, 2 * N):
    if beads[i] == 'w':
        rL[i] = rL[i-1] + 1
        bL[i] = bL[i-1] + 1
    else:
        if beads[i] == 'r':
            rL[i] = rL[i-1] + 1
            bL[i] = 0
        else:
            rL[i] = 0
            bL[i] = bL[i-1] + 1

# put 2N-1 entries on N-1 to simplify later code
rL[N - 1] = rL[2 * N - 1]
bL[N - 1] = bL[2 * N - 1]

best = -1
for i in range(N):
    j = i + N - 1
    candR = max(rR[i], bR[i])
    candL = max(rL[j], bL[j])
    cand = candR + candL
    if best < cand:
        best = cand
best = min(best, N)

printwrite(best)















fin.close()
fout.close()
del print, input
print(time.time() - ttt)
