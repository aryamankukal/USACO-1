"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fc
5.1.2
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

filename = 'fc'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










from functools import reduce

def graham(pts):
    def turn(a, b, c):
        ux = b[0] - a[0]
        uy = b[1] - a[1]
        vx = c[0] - b[0]
        vy = c[1] - b[1]
        return ux * vy - uy * vx
    def keepLeft(existingPts, currPt):
        while len(existingPts) >= 2 and\
              turn(existingPts[-2], existingPts[-1], currPt) < 0:
            existingPts.pop()
        if len(existingPts) == 0 or existingPts[-1] != currPt:
            existingPts.append(currPt)
        return existingPts
    pts.sort()
    lower = reduce(keepLeft, pts, [])
    upper = reduce(keepLeft, reversed(pts), [])
    if len(upper) <= 2:
        return lower
    else:
        return lower + upper[1:-1]

def length(pts):
    ans = 0
    for i in range(-1, len(pts)-1):
        ans += hypot(pts[i][0] - pts[i+1][0], pts[i][1] - pts[i+1][1])
    return ans

N = int(input())
cows = []
for n in range(N):
    x, y = map(float, input().split())
    cows.append([x, y])

convHull = graham(cows)

printwrite('%.2f' % length(convHull))









fin.close()
fout.close()
del print, input

