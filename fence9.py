"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fence9
3.4.3

key idea
1 pick's theorem
2 num of grid points on a line segment between two grid points
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

filename = 'fence9'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')











def numGridPtsInBetween(x, y):
    '''
    calculates number of grid points between 0, 0 and x, y,
    excluding end points
    assumes int x, int y
    '''
    return gcd(x, y) - 1



n, m, p = map(int, input().split())

numPtsX = numGridPtsInBetween(p, 0)
numPtsL = numGridPtsInBetween(n, m)
numPtsR = numGridPtsInBetween(n - p, m)

numEdgePts = numPtsX + numPtsL + numPtsR + 3

pts = [[0, 0], [p, 0], [n, m], [0, 0]]
area = 0
for i in range(len(pts) - 1):
    area += pts[i][0] * pts[i+1][1] - pts[i][1] * pts[i+1][0]
area /= 2

# numInPts + numEdgePts / 2 - 1 = area

numInPts = area - numEdgePts / 2 + 1

printwrite(int(numInPts))










fin.close()
fout.close()
del print, input

