"""
ID: wrwwctb1
LANG: PYTHON3
TASK: rectbarn
6.1.2

review

dp
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

filename = 'rectbarn'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










R, C, P = map(int, input().split())
#matrix = [[True] * C for _ in range(R)]
badpts = [set() for _ in range(R)] # list of sets

for _ in range(P):
    i, j = map(int, input().split())
    #matrix[i-1][j-1] = False
    badpts[i-1].add(j-1)


height = [0] * C # height of center pillar of 1
hl = [-1] * C # every row of center pillar has a left boundary. max of these
hr = [ C] * C
ret = 0

for i in range(R):
    rowl = -1 # if matrix ij == 1, going left would eventually hit a 0 or a wall, rowl is the index of it
    rowr = C
    for j in range(C):
        if j not in badpts[i]:
            height[j] += 1
        else:
            height[j] = 0

    for j in range(C):
        if j in badpts[i]:
            rowl = j
            hl[j] = -1
        else:
            hl[j] = max(rowl, hl[j])

    for j in range(C-1, -1, -1):
        if j in badpts[i]:
            rowr = j
            hr[j] = C
        else:
            hr[j] = min(rowr, hr[j])

    for j in range(C):
        ret = max(ret, (hr[j] - hl[j] - 1) * height[j])



printwrite(ret)









fin.close()
fout.close()
del print, input

